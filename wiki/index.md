# Oh-My-Wiki

```dataviewjs
dv.paragraph(`> 最后更新: ${dv.current().file.mtime.toFormat("yyyy-MM-dd HH:mm")}（随文件修改自动更新）`);
```
> 统计与页面列表由 Dataview 实时生成，**请勿手工维护数字或表格**；操作日志见 `wiki/log.txt`

## 状态总览

```dataviewjs
const pages = dv.pages('"wiki"').where(p => p.type);
const byType = {};
for (const p of pages) byType[p.type] = (byType[p.type] || 0) + 1;
dv.table(["统计", "数量"], [
  ["概念 concept", byType["concept"] || 0],
  ["实体 entity", byType["entity"] || 0],
  ["主题 topic", byType["topic"] || 0],
  ["指南 howto", byType["howto"] || 0],
  ["**总计**", pages.length],
]);
const tagCount = {};
for (const p of pages) for (const t of (p.tags || [])) tagCount[t] = (tagCount[t] || 0) + 1;
const top = Object.entries(tagCount).sort((a, b) => b[1] - a[1]).slice(0, 5)
  .map(([k, v]) => `${k}(${v})`).join(" · ");
dv.paragraph(`**活跃标签 Top5**：${top}`);
```

## 正在进行

| 文章 | 标签 |
|------|------|
| [[决策树与集成学习：从Bagging到梯度提升.md\|决策树与集成学习]] | 机器学习, 决策树, 集成学习 |
| [[VPN-机场-代理-梯子.md\|VPN、机场、代理、梯子]] | vpn, proxy, network |
| [[终端实用效率指南.md\|终端实用效率指南]] | terminal, cli, 效率 |
| [[增长系数预测.md\|增长系数预测]] | 增长, 广告, boosting |
| [[ffmpeg视频剪辑入门.md\|FFmpeg 视频剪辑入门]] | ffmpeg, 视频剪辑 |
| [[如何构建知识体系.md\|如何构建知识体系]] | 知识管理, 学习方法 |

## 快速导航

**Agent工程** · **软件工程** · **增长与营销** · **复盘与方法论** · **媒介理论** · **机器学习** · **写作与技术博客** · **知识管理**

---

## 原子知识 (atoms)

> 稳定的、可复用的知识砖块

### 概念 (concepts)

> 按 domain 分组（domain 存于各页 frontmatter）

```dataviewjs
const pages = dv.pages('"wiki/atoms/concepts"').where(p => p.domain).array();
const byDomain = {};
for (const p of pages) (byDomain[p.domain] = byDomain[p.domain] || []).push(p);
const domains = Object.keys(byDomain).sort((a, b) => a.localeCompare(b, "zh-Hans-CN"));
for (const d of domains) {
  const rows = byDomain[d].sort((a, b) => (a.updated < b.updated ? 1 : a.updated > b.updated ? -1 : 0));
  dv.header(4, `${d} (${rows.length})`);
  dv.table(["概念", "描述", "更新日期"],
    rows.map(p => [p.file.link, p.description || "", p.updated]));
}
```

### 实体 (entities)

```dataview
TABLE description AS "描述", updated AS "更新日期"
FROM "wiki/atoms/entities"
SORT file.name
```

---

## 综合知识 (synthesis)

> 沉淀后的成品，带有个人判断和实践痕迹

### 主题 (topics)

> 领域性的综合指南，从 `workspace/topics/` 沉淀而来

```dataview
TABLE description AS "描述", updated AS "更新日期"
FROM "wiki/synthesis/topics"
SORT updated DESC
```

### 洞察 (insights)

> 跨越多个领域的个人洞察，从 `workspace/Done/` 沉淀而来

*暂无内容*

### 指南 (howto)

> 可操作的步骤指南，从 `workspace/Done/` 沉淀而来

```dataview
TABLE description AS "描述", updated AS "更新日期"
FROM "wiki/synthesis/howto"
SORT updated DESC
```

---

## 知识流转规则

```
raw/                # 原始资料入库
  │
  ↓ Agent 提取
  │
wiki/atoms/         # 原子知识（概念、实体）
  │
  ↓ 你实践使用
  │
workspace/          # 实践过程
  ├── Done/         # 单篇完成 → wiki/synthesis/howto 或 insights
  └── topics/       # 话题积累 → wiki/synthesis/topics
  │
  ↓ 沉淀成熟
  │
wiki/synthesis/     # 综合知识（带个人判断）
  │
  ↓ 认知深化时直接更新
  │
（保持 status 和变更日志）
```

---

## 知识图谱

> 使用 [Obsidian Graph View](obsidian://graph) 查看完整知识图谱
> `wiki/graph.json` 由 gen-graph skill 从页面链接生成，语义关系存于 `wiki/graph.relations.json`

### 核心关系

```
Agent-Loop ──implements──> Agent-Control-Patterns
     │
     └──relates_to──> Workflow-vs-Agent

Harness-Engineering ──includes──> Agent-Evaluation
        │
        └──includes──> Agent-Tracing

Agent-First-Development ──requires──> Harness-Engineering
           │
           ├──uses──> Progressive-Disclosure
           │
           └──requires──> Architecture-Constraints

Codex ──enables──> Agent-First-Development
  │
  └──developed_by──> OpenAI

MMP-Attribution ──compares_to──> SKAN-Attribution
      │
      ├──uses──> Last-Click-Rule
      │
      └──measures──> Attribution-Gap

User-App-Pair ──foundation_of──> Audience-Definition
      │
      └──explains──> Network-Cognition-Gap

Audience-Definition ──identifies──> High-Value-Channel
        │
        └──requires──> Channel-Launch-Strategy

CLAP-Model ──improves──> PDCA-Model
    │
    ├──improves──> PDF-Model
    │
    ├──belongs_to──> FuPan
    │
    └──supported_by──> OPTM-Framework

AAR-Model ──simplifies──> CLAP-Model
    │
    └──belongs_to──> FuPan

ZhangPeng ──proposed──> CLAP-Model
    │
    └──proposed──> OPTM-Framework

MECE ──supports──> Pyramid-Principle
Pyramid-Principle ──uses──> MECE

Phodal ──authored──> Tech-Blog-Article-Types
    │
    └──relates_to──> Blog-Content-Writing-Practices
            │
            └──relates_to──> Title-4U-Formula

DDD ──relates_to──> Architecture-Constraints

Pyramid-Principle ──uses──> SCQ法则
SCQ法则 ──belongs_to──> Pyramid-Principle

写作价值心法 ──relates_to──> 顶级信息论与输入输出比
滑梯理论 ──relates_to──> 写作价值心法
写作起步-日常书写 ──uses──> 工作记忆
作品意识与打磨意识 ──relates_to──> 中文技术文档写作规范

清脑作者 ──authored──> 写作价值心法
阿宝哥 ──authored──> 作品意识与打磨意识
皮卡小宝 ──authored──> SCQ法则
```
