# -*- coding: utf-8 -*-
"""gen_graph.py — 从 wiki 页面链接重建 graph.json（派生件自动生成）

用法:
  python gen_graph.py            生成 wiki/graph.json
  python gen_graph.py --check    只校验：现有 graph.json 是否与从链接推导的结果一致（不写入）

输入:
  wiki/**/*.md（排除 index.md 与 templates/）中的 [[链接]]      → 基础边 relation=links_to
  raw/**/*.md 中的文件                                          → 节点 type=source
  页面中指向 raw/ 的链接（正文 ## 来源 段与 frontmatter sources） → 边 relation=cites
  wiki/graph.relations.json 中的语义关系（策展判断件，优先级更高）

输出:
  wiki/graph.json —— 派生件，禁止手工编辑；不一致时用本脚本重建
"""
import re
import json
import sys
import io
from pathlib import Path
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def find_root() -> Path:
    """从脚本位置向上找含 wiki/ 的仓库根"""
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "wiki").is_dir():
            return parent
    raise SystemExit("找不到仓库根（含 wiki/ 的目录）")


ROOT = find_root()


def load_wiki_pages():
    """返回 {stem: {path, type, fm, text}}，index 与 templates 排除"""
    pages = {}
    for p in sorted((ROOT / "wiki").rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if p.name == "index.md" or "templates" in rel.split("/"):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
        fm, body = (m.group(1), m.group(2)) if m else ("", text)
        tm = re.search(r"^type:\s*(\S+)", fm, re.M)
        pages[p.stem] = {
            "path": rel,
            "type": tm.group(1) if tm else "",
            "fm": fm,
            "text": text,
        }
    return pages


def load_raw_files():
    """返回 {raw_id: {path, title}}，raw_id = 去掉 .md 的相对路径

    raw/ 是只读原始资料，此处仅登记为图谱节点，不做任何写入。
    """
    raws = {}
    base = ROOT / "raw"
    if not base.is_dir():
        return raws
    for p in sorted(base.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        rid = rel[:-3] if rel.endswith(".md") else rel
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
        title = ""
        if m:
            tm = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", m.group(1), re.M)
            if tm:
                title = tm.group(1).strip()
        raws[rid] = {"path": rel, "title": title or p.stem}
    return raws


def build_resolver(pages, raw_files=None):
    """stem 与 aliases → stem 的解析器（wiki 页；raw/ 路径解析为 raw 节点 id）"""
    raw_files = raw_files or {}
    by_lower = defaultdict(list)
    alias_map = {}
    for stem, info in pages.items():
        by_lower[stem.lower()].append(stem)
        fm = info["fm"]
        m = re.search(r"^aliases:\s*\n((?:[ \t]+-(?:[ \t]+)?.*\n?)+)", fm, re.M)
        if m:
            for a in re.findall(r"^[ \t]+-[ \t]*(.+)$", m.group(1), re.M):
                alias_map.setdefault(a.strip().strip("\"'").lower(), stem)
        m2 = re.search(r"^aliases:\s*\[(.*?)\]", fm, re.M)
        if m2:
            for a in m2.group(1).split(","):
                alias_map.setdefault(a.strip().strip("\"'").lower(), stem)

    def resolve(target: str):
        t = target.replace("\\|", "|").split("|")[0].split("#")[0].strip()
        if not t:
            return None
        if "/" in t:  # 路径式链接：wiki/ 页面 或 raw/ 原始资料
            if t.startswith("wiki/"):
                t = t[3:]
                if t.endswith(".md"):
                    t = t[:-3]
                return t if t in pages else None
            if t.startswith("raw/"):
                rid = t[:-3] if t.endswith(".md") else t
                return rid if rid in raw_files else None
            return None
        if t in pages:
            return t
        hits = by_lower.get(t.lower(), [])
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:  # 同名歧义（大小写冲突）：跳过
            return None
        return alias_map.get(t.lower())

    return resolve


def build_graph():
    pages = load_wiki_pages()
    raw_files = load_raw_files()
    resolve = build_resolver(pages, raw_files)

    nodes = [
        {"id": stem, "type": info["type"], "path": info["path"]}
        for stem, info in pages.items()
    ]
    nodes += [
        {"id": rid, "type": "source", "path": info["path"], "title": info["title"]}
        for rid, info in raw_files.items()
    ]
    nodes.sort(key=lambda n: n["id"])

    edge_map = {}

    # 1) 基础边：正文/frontmatter 中的链接（wiki → wiki 为 links_to；wiki → raw 为 cites）
    for stem, info in pages.items():
        clean = re.sub(r"```.*?```", "", info["text"], flags=re.S)
        for m in re.finditer(r"\[\[([^\[\]]+?)\]\]", clean):
            target = resolve(m.group(1))
            if target and target != stem:
                rel = "cites" if target.startswith("raw/") else "links_to"
                edge_map.setdefault(
                    (stem, target),
                    {"from": stem, "to": target, "relation": rel, "context": ""},
                )

    # 2) 语义策展层：graph.relations.json（优先级高于链接默认值）
    overlay_path = ROOT / "wiki" / "graph.relations.json"
    skipped = []
    if overlay_path.exists():
        overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
        for r in overlay.get("relations", []):
            fr, to = resolve(r.get("from", "")), resolve(r.get("to", ""))
            if not fr or not to:
                skipped.append(f"{r.get('from')}->{r.get('to')}")
                continue
            edge_map[(fr, to)] = {
                "from": fr,
                "to": to,
                "relation": r.get("relation", "relates_to"),
                "context": r.get("context", ""),
            }
    if skipped:
        print(f"⚠ overlay 中 {len(skipped)} 条关系端点无法解析，已跳过: {skipped}")

    edges = sorted(edge_map.values(), key=lambda e: (e["from"], e["to"]))

    by_type = defaultdict(int)
    for n in nodes:
        by_type[n["type"]] += 1
    stats = {
        "totalNodes": len(nodes),
        "totalEdges": len(edges),
        "byType": {k: by_type[k] for k in sorted(by_type)},
    }

    import datetime
    return {
        "version": 1,
        "lastUpdated": datetime.date.today().isoformat(),
        "nodes": nodes,
        "edges": edges,
        "stats": stats,
    }


def main():
    check = "--check" in sys.argv
    new = build_graph()
    path = ROOT / "wiki" / "graph.json"

    if check:
        if not path.exists():
            print("✗ graph.json 不存在，请运行本脚本生成")
            sys.exit(1)
        old = json.loads(path.read_text(encoding="utf-8"))
        diffs = []
        # lastUpdated 为生成日期，不参与比较
        for key in ("nodes", "edges", "stats"):
            if old.get(key) != new.get(key):
                diffs.append(key)
        if diffs:
            print(f"✗ graph.json 与链接推导结果不一致（差异字段: {diffs}）")
            print(f"  现有: 节点{len(old.get('nodes', []))} 边{len(old.get('edges', []))} "
                  f"stats={old.get('stats')}")
            print(f"  推导: 节点{len(new['nodes'])} 边{len(new['edges'])} stats={new['stats']}")
            print("  修复: python gen_graph.py")
            sys.exit(1)
        print(f"✓ graph.json 一致（节点 {new['stats']['totalNodes']}，"
              f"边 {new['stats']['totalEdges']}）")
        return

    path.write_text(
        json.dumps(new, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"✓ 已生成 {path.relative_to(ROOT).as_posix()}："
          f"节点 {new['stats']['totalNodes']}，边 {new['stats']['totalEdges']}，"
          f"byType={new['stats']['byType']}")


if __name__ == "__main__":
    main()
