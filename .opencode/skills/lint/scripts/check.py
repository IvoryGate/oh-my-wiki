# -*- coding: utf-8 -*-
"""check.py — Oh-My-Wiki 知识库健康检查（lint skill 的可执行检查器）

用法: python check.py [--no-graph]
退出码: 0 全部通过（警告不计入）; 1 存在错误

检查项目:
  1. 断链        wiki 内容页 [[链接]] 无法解析（含别名解析）
  2. frontmatter 必填字段与格式（概念页必填 domain）
  3. 标签词表    不同标签数 == EXPECTED_TAG_COUNT
  4. index 反漂移 不得出现手工统计数字/手工概念表格（应由 Dataview 生成）
  5. graph.json  调用 gen-graph --check（--no-graph 跳过）
  6. 孤页        无入链的内容页（警告，不判失败）
"""
import re
import io
import sys
import json
import subprocess
from pathlib import Path
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

EXPECTED_TAG_COUNT = 31  # 标签词表策略（调整词表时同步此值）

KNOWN_BROKEN = {
    # workspace 正文不可编辑，已知历史断链（历史 lint 已记录，用户未选择处理）
    "workspace/topics/Agent/_tracker.md":
        ["核心架构与实现", "Agent核心循环", "控制模式", "工程实践"],
}
SKIP_DIRS = {".git", ".obsidian", ".playwright-mcp", ".claude", "node_modules"}
# 断链检查排除：项目文档（引用外部/历史路径）与模板
BROKEN_EXCLUDE = {"Agent.md", "README.md", "CONTEXT.md", "AGENTS.md"}
DATE_RE = r"^\d{4}-\d{2}-\d{2}$"


def find_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "wiki").is_dir():
            return parent
    raise SystemExit("找不到仓库根（含 wiki/ 的目录）")


ROOT = find_root()
errors, warnings = [], []


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


# ---------- 收集所有 md ----------
all_md = {}
for p in ROOT.rglob("*.md"):
    if any(x in p.parts for x in SKIP_DIRS):
        continue
    all_md[rel(p)] = p


def fm_and_body(r: str):
    t = all_md[r].read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", t, re.S)
    return (m.group(1), m.group(2)) if m else ("", t)


# ---------- 解析器：basename + aliases（wiki 优先） ----------
basename = defaultdict(list)
alias_map = {}
for r in all_md:
    basename[r.rsplit("/", 1)[-1][:-3].lower()].append(r)
    blk = fm_and_body(r)[0]
    if blk:
        m = re.search(r"^aliases:\s*\n((?:[ \t]+-(?:[ \t]+)?.*\n?)+)", blk, re.M)
        if m:
            for a in re.findall(r"^[ \t]+-[ \t]*(.+)$", m.group(1), re.M):
                alias_map[a.strip().strip("\"'").lower()] = r
        m2 = re.search(r"^aliases:\s*\[(.*?)\]", blk, re.M)
        if m2:
            for a in m2.group(1).split(","):
                alias_map[a.strip().strip("\"'").lower()] = r


def resolve(t: str):
    """链接目标 → 相对路径；支持 [[path.md\\|alias]] / [[X|Y]] / [[X#head]]"""
    t = t.replace("\\|", "|")
    t = t.split("|")[0].split("#")[0].strip()
    if not t:
        return None
    if "/" in t:
        q = t if t.endswith(".md") else t + ".md"
        return q if (ROOT / q).exists() else None
    if t.endswith(".md"):
        t = t[:-3]
    tl = t.lower()
    hits = basename.get(tl, [])
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        wk = [h for h in hits if h.startswith("wiki/")]  # 同名歧义约定为 wiki 页
        if len(wk) == 1:
            return wk[0]
        return None
    return alias_map.get(tl)


def links_of(r: str) -> list:
    text = all_md[r].read_text(encoding="utf-8", errors="replace")
    clean = re.sub(r"```.*?```", "", text, flags=re.S)   # 代码块
    clean = re.sub(r"`[^`\n]*`", "", clean)              # 行内代码（字面示例非链接）
    return re.findall(r"\[\[([^\[\]]+?)\]\]", clean)


def is_content(r: str) -> bool:
    """wiki 内容页（有 frontmatter 的知识页面）"""
    if not r.startswith("wiki/"):
        return False
    if r in ("wiki/index.md",) or "templates" in r.split("/"):
        return False
    return bool(fm_and_body(r)[0])


# ---------- 1) 断链 ----------
broken = defaultdict(list)
check_broken = [r for r in all_md
                if r not in BROKEN_EXCLUDE
                and "templates" not in r.split("/")
                and not r.startswith("raw/")
                and not r.startswith(".opencode/")]
for r in check_broken:
    for target in links_of(r):
        if target.startswith(("http", "raw/", "wiki/")):
            continue
        if resolve(target) is None and target not in KNOWN_BROKEN.get(r, []):
            broken[r].append(target)
if broken:
    n = sum(len(v) for v in broken.values())
    errors.append(f"断链 {n} 处: " +
                  "; ".join(f"{k}: {sorted(set(v))}" for k, v in list(broken.items())[:8]))

# ---------- 2) frontmatter 完整性 ----------
REQUIRED = ["title", "created", "updated", "type", "description"]
for r in sorted(all_md):
    if not is_content(r):
        continue
    fm = fm_and_body(r)[0]
    typ = ""
    for f in REQUIRED:
        m = re.search(rf"^{f}:\s*(\S.*)$", fm, re.M)
        if not m:
            errors.append(f"{r}: 缺 frontmatter 字段 {f}")
            continue
        if f == "type":
            typ = m.group(1).strip()
            if typ not in ("concept", "entity", "data", "topic", "insight", "howto"):
                errors.append(f"{r}: type 非法 {typ}")
        if f in ("created", "updated") and not re.match(DATE_RE, m.group(1).strip()):
            errors.append(f"{r}: {f} 非 YYYY-MM-DD: {m.group(1).strip()}")
    if typ == "concept" and not re.search(r"^domain:\s*\S", fm, re.M):
        errors.append(f"{r}: 概念页缺 domain")
    if not re.search(r"^tags:\s*\S", fm, re.M):
        errors.append(f"{r}: 缺 tags")

# ---------- 3) 标签词表 ----------
tag_set = set()
for r in sorted(all_md):
    if not is_content(r):
        continue
    fm = fm_and_body(r)[0]
    mi = re.search(r"^tags:\s*\[(.*?)\]", fm, re.M)
    if mi:
        tag_set.update(t.strip() for t in mi.group(1).split(",") if t.strip())
    else:
        mb = re.search(r"^tags:\s*\n((?:[ \t]+-(?:[ \t]+)?.*\n?)+)", fm, re.M)
        if mb:
            tag_set.update(t.strip() for t in re.findall(r"^[ \t]+-[ \t]*(.+)$", mb.group(1), re.M))
if len(tag_set) != EXPECTED_TAG_COUNT:
    errors.append(f"标签数 {len(tag_set)} != {EXPECTED_TAG_COUNT}: {sorted(tag_set)}")
# 假标签检测（历史 bug：- -- ）
bad_tags = {t for t in tag_set if t.startswith("-") or t.startswith("--") or not t.strip()}
if bad_tags:
    errors.append(f"非法标签值: {sorted(bad_tags)}")

# ---------- 4) index 反漂移 ----------
idx_path = ROOT / "wiki" / "index.md"
idx = idx_path.read_text(encoding="utf-8")
if "dataviewjs" not in idx and "```dataview" not in idx:
    errors.append("index 缺少 Dataview 查询块（应由 Dataview 生成统计与表格）")
if re.search(r"^\| (概念|实体|主题|指南|总计) \|", idx, re.M):
    errors.append("index 出现手工统计表格（应由 Dataview 实时生成）")
if re.search(r"^\| \[\[[^\]]+\]\] \| .+ \| \d{4}-\d{2}-\d{2} \|", idx, re.M):
    errors.append("index 出现手工概念表格行（应由 Dataview GROUP BY domain 生成）")

# ---------- 5) graph.json 一致性 ----------
graph_script = ROOT / ".opencode" / "skills" / "gen-graph" / "scripts" / "gen_graph.py"
if "--no-graph" in sys.argv:
    print("(跳过 graph 校验)")
elif graph_script.exists():
    r = subprocess.run([sys.executable, str(graph_script), "--check"],
                       capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout or "") + (r.stderr or "")
    if r.returncode != 0:
        errors.append("graph.json 不一致: " + out.strip().replace("\n", " | "))
    else:
        print(out.strip())
else:
    warnings.append("gen-graph skill 不存在，跳过 graph 校验")

# ---------- 6) 孤页（警告） ----------
inbound = defaultdict(set)
for r in all_md:
    if r == "wiki/index.md" or "templates" in r.split("/"):
        continue
    for target in links_of(r):
        t = resolve(target)
        if t and t != r:
            inbound[t].add(r)
orphans = []
for r in sorted(all_md):
    if not is_content(r) or not r.startswith("wiki/"):
        continue
    if not inbound[r]:
        orphans.append(r.rsplit("/", 1)[-1][:-3])

# ---------- 汇总 ----------
counts = defaultdict(int)
pages = [r for r in all_md if is_content(r)]
for r in pages:
    tm = re.search(r"^type:\s*(\S+)", fm_and_body(r)[0], re.M)
    if tm:
        counts[tm.group(1)] += 1

print("=== Lint 结果 ===")
print(f"页面: 总{len(pages)} 概念{counts['concept']} 实体{counts['entity']} "
      f"主题{counts['topic']} 指南{counts['howto']}")
print(f"标签: {len(tag_set)} 个")
print(f"断链: {sum(len(v) for v in broken.values())} 处")
print(f"孤页: {len(orphans)} 个" + (f" → {orphans}" if orphans else ""))
if warnings:
    print("\n警告:")
    for w in warnings:
        print(f"  ! {w}")
if errors:
    print("\n!! 错误:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("\n=== 全部通过 ===")
