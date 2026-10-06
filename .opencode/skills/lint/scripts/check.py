# -*- coding: utf-8 -*-
"""check.py — Oh-My-Wiki 知识库健康检查（lint skill 的可执行检查器）

用法: python check.py [--no-graph]
退出码: 0 全部通过（警告不计入）; 1 存在错误

检查项目:
  1. 断链        wiki 内容页 [[链接]] 无法解析（含别名解析）
  2. frontmatter 必填字段与格式（概念页必填 domain）
  3. 标签词表    wiki/workspace/raw 全部标签 ∈ VOCAB（39 词，含引用去引号）
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

EXPECTED_TAG_COUNT = 39  # 标签词表策略（2026-10-06 扩容：域13/任务4/方法2/主题20，与下方 VOCAB 双处同步）

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
        if target.startswith(("http", "wiki/")):  # raw/ 目标纳入校验：resolve() 可直接判定文件是否存在
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
# 词表 39 词 = 域13/任务4/方法2/主题20（2026-10-06 扩容：+视频剪辑/网络与代理/终端与Shell/
# 个人随笔/视觉设计/经济与金融；同批将 workspace 与 raw 标签纳入校验，覆盖三区）
VOCAB = frozenset("""
域/机器学习 域/增长与营销 域/数据库 域/写作与技术博客 域/Agent架构与工程 域/复盘与方法论
域/LLM与知识管理 域/媒介理论 域/Agent-First开发 域/软件架构与建模 域/软件工程 域/开发工具 域/面试方法论
任务/分类 任务/回归 任务/降维 任务/聚类
方法/结构化思维 方法/排版规范
主题/优化 主题/广告归因 主题/概率图模型 主题/反作弊 主题/贝叶斯 主题/统计 主题/神经网络 主题/认知
主题/数据分析 主题/学习理论 主题/特征工程 主题/集成学习 主题/广告技术 主题/MMP
主题/视频剪辑 主题/网络与代理 主题/终端与Shell 主题/个人随笔 主题/视觉设计 主题/经济与金融
""".split())
if len(VOCAB) != EXPECTED_TAG_COUNT:
    errors.append(f"词表定义 {len(VOCAB)} 词 != EXPECTED_TAG_COUNT={EXPECTED_TAG_COUNT}（改词表需同步两处）")


def collect_tags(fm: str):
    """提取 frontmatter 标签：行内 [a, b] 或块式 - a（统一去引号）"""
    mi = re.search(r"^tags:[ \t]*(\[[^\]]*\])", fm, re.M)
    if mi:
        return [t.strip().strip("\"'") for t in mi.group(1).strip("[]").split(",") if t.strip()]
    mb = re.search(r"^tags:[ \t]*\n((?:[ \t]+-[ \t]*.*\n?)+)", fm, re.M)
    if mb:
        return [t.strip().strip("\"'")
                for t in re.findall(r"^[ \t]+-[ \t]*(.+?)\s*$", mb.group(1), re.M)]
    return []


used = set()
out_of_vocab = defaultdict(list)
for r in sorted(all_md):
    if not r.startswith(("wiki/", "raw/", "workspace/")):
        continue
    if "templates" in r.split("/"):
        continue
    fm = fm_and_body(r)[0]
    if not fm:
        continue
    for t in collect_tags(fm):
        if not t or t.startswith("-"):   # 假标签检测（历史 bug：- -- ）
            errors.append(f"{r}: 非法标签值 {t!r}")
            continue
        used.add(t)
        if t not in VOCAB:
            out_of_vocab[t].append(r)
if out_of_vocab:
    errors.append("词表外标签: " + "; ".join(
        f"#{t} × {len(fs)}（如 {fs[0]}）" for t, fs in sorted(out_of_vocab.items())))
unused = sorted(VOCAB - used)
if unused:
    warnings.append("词表内零使用: " + " ".join("#" + u for u in unused))

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
print(f"标签: {len(used)} 个在用 / 词表 {len(VOCAB)}")
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
