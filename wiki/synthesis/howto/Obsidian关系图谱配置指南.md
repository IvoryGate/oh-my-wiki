---
title: Obsidian关系图谱配置指南
created: 2026-10-06
updated: 2026-10-06
type: howto
domain: LLM 与知识管理
description: 本库图谱的身份分色、过滤开关、力学参数与 33 词标签命名空间配置方法
tags: [域/LLM与知识管理]
sources:
  - "[Obsidian Graph View 官方帮助](https://obsidian.md/help/plugins/graph)"
status: active
---

# Obsidian关系图谱配置指南

面向 oh-my-wiki 的图谱配置，四步走：**身份分色 → 过滤降噪 → 力学布局 → 标签命名空间**。

> 图谱设置存于 `.obsidian/graph.json`，**未随仓库分发**——换设备或重装后照本文重配即可。

## 一、Filters 四开关

| 开关 | 建议 | 原因 |
|------|------|------|
| **Tags** | **关** | 标签会作为节点入图。本库曾因 `clippings`（177 篇剪藏）形成全图最大枢纽，把所有剪藏焊成一个星团糊在正中央；关掉只隐藏标签节点，**笔记全部保留** |
| **Attachments** | 关 | workspace 图片等附件入图无信息量 |
| **Orphans** | 平时关 | 体检时打开找孤页，配合 lint 使用 |
| **Unresolved** | 保持开 | 让断链在图里现形 |

> 本库当前值：`showTags/showAttachments/showOrphans=false`、`hideUnresolved=false`（即 Unresolved 开）。体检要看孤页时，在 Filters 里临时打开 Orphans。

搜索框支持查询语法，是最强的降噪手段：

```
path:"wiki"                只看知识层
-path:"raw"                排除剪藏
path:"wiki/atoms/concepts" 只看概念层
file:RAG                   按文件名
```

## 二、身份分组（7 条）

颜色分组按**自上而下首个匹配**生效（first-match-wins），因此最具体的排最前。这 7 条回答"谁写的"——你写的（workspace）、Agent 生成的（wiki）、剪藏的（raw），外加项目文档：

| # | 查询 | 色 | 含义 |
|---|------|----|------|
| 1 | `path:"workspace"` | 绿 `#3FA862` | 你的个人创作 |
| 2 | `path:"wiki/synthesis"` | 橙 `#E8833A` | 综合层（活跃） |
| 3 | `path:"wiki/atoms/concepts"` | 蓝 `#3D7EE8` | 概念页（稳定） |
| 4 | `path:"wiki/atoms"` | 青 `#22B5C4` | 其余原子（实体/数据） |
| 5 | `path:"wiki"` | 紫 `#8B5CF6` | wiki 兜底（index/templates） |
| 6 | `path:"raw"` | 灰 `#9AA3AD` | 原始剪藏（低存在感） |
| 7 | `file:"AGENTS.md" OR file:"README.md" OR file:"CONTEXT.md" OR file:"Home.md" OR file:"PROMPT.md" OR file:"BOUNDARY.md"` | 棕 `#A97C50` | 项目文档 |

等价的 JSON（关闭 Obsidian 后贴进 `.obsidian/graph.json` 的 `colorGroups`）：

```json
"colorGroups": [
  { "query": "path:\"workspace\"",        "color": { "a": 1, "rgb": 4171874 } },
  { "query": "path:\"wiki/synthesis\"",   "color": { "a": 1, "rgb": 15237946 } },
  { "query": "path:\"wiki/atoms/concepts\"","color": { "a": 1, "rgb": 4030184 } },
  { "query": "path:\"wiki/atoms\"",       "color": { "a": 1, "rgb": 2274756 } },
  { "query": "path:\"wiki\"",             "color": { "a": 1, "rgb": 9133302 } },
  { "query": "path:\"raw\"",              "color": { "a": 1, "rgb": 10134445 } },
  { "query": "file:\"AGENTS.md\" OR file:\"README.md\" OR file:\"CONTEXT.md\" OR file:\"Home.md\" OR file:\"PROMPT.md\" OR file:\"BOUNDARY.md\"", "color": { "a": 1, "rgb": 11107408 } }
]
```

> rgb = `(R << 16) | (G << 8) | B`。若主题色压过分组色，属 Obsidian 已知个案，恢复图谱默认设置或补一条 CSS 即可。

**本库已于 2026-10-06 直接写入 `.obsidian/graph.json`**（含下列三开关），无需手贴；重装设备时才需照此重配。

## 三、Display / Forces（本库实测值）

本库页面已过 190，用**展开簇团型**参数：

```
Text fade threshold   -1.50   标签只在放大时出现，避免糊成一片
Node size              1.52   被引越多越大，看枢纽
Link thickness         0.71
Center force           0.65   调低让集群散开
Repel force           12.40   调高避免挤成一坨
Link force             0.90
Link distance        （默认 500，可试 300 看是否更紧凑）
```

原则：**Center 越低越能分出簇团；Repel 越高越不重叠；Link distance 越短越紧凑**。先调 Forces 让结构出来，再调 Display 调观感——**别指望靠调参数救没分色的图**，颜色分组才是降噪的第一步。

## 四、常用过滤视图（Bookmarks）

| 视图 | 查询 | 用途 |
|------|------|------|
| 知识层 | `path:"wiki"` | 只看知识结构 |
| 枢纽概念 | `path:"wiki/atoms/concepts"` | 节点越大＝被引越多 |
| 健康体检 | `-path:"raw"`（配 Orphans 开） | 找孤页，配合 lint |
| 流入检查 | `path:"workspace"` | 看创作是否已关联知识库 |

**日常导航优先用 Local Graph**（右侧栏打开当前笔记）：`depth` 拉到 2~3 看二阶影响，比全库图谱有用得多。

## 五、标签命名空间（2026-10-06 重构，33 词）

**原则**：`domain` 给 Dataview，`tag` 给 Obsidian——图谱分组查询**吃不到 frontmatter 自定义字段**（只认 `path/tag/file`），所以域级信息必须在 tag 里保留一份，两处顶层**故意重复**。

```
#域/     13 个  与 frontmatter domain 一一对齐（tag 内不能有空格，故 domain 值里的空格去掉）
            机器学习 增长与营销 数据库 写作与技术博客 Agent架构与工程 复盘与方法论
            LLM与知识管理 媒介理论 Agent-First开发 软件架构与建模 软件工程 开发工具 面试方法论
#任务/    4 个  分类 回归 降维 聚类          （ML 任务类型）
#方法/    2 个  结构化思维 排版规范           （写作与思维方法）
#主题/   14 个  优化 广告归因 概率图模型 反作弊 贝叶斯 统计 神经网络 认知
            数据分析 学习理论 特征工程 集成学习 广告技术 MMP
```

- **192 个内容页每页恰好 1 个域标签**，lint 以 `EXPECTED_TAG_COUNT = 33` 校验词表数量
- 每页同时可挂任务/方法/主题标签（细粒度），域标签不重复
- **workspace 的 tags 是你的自由词表**（ffmpeg、UA、jottings…约 70 个），不参与 lint 校验、也未纳入本命名空间

## 六、关联通道的两个机制

1. **frontmatter 里的 `[[链接]]` 必须加引号** `"[[概念名]]"` 才会被识别进图谱与反链——YAML 会把裸的 `[[A]]` 解析成嵌套数组而非字符串。`workspace/` 的 `related` 字段已按此统一
2. **wiki→raw 的 730 条引用边**：主视图用 `-path:"raw"` 滤掉，另存一个溯源视图看引用关系——结构与溯源分开看

## 来源

- [Obsidian Graph View 官方帮助](https://obsidian.md/help/plugins/graph)

## 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-10-06 | 1.0 | 初版：身份分组 7 条、四开关、力学实测值、33 词标签命名空间、related 引号机制 |
