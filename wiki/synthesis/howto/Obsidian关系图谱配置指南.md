---
title: Obsidian关系图谱配置指南
created: 2026-10-06
updated: 2026-10-07
type: howto
domain: LLM 与知识管理
description: 本库图谱的身份分色、过滤开关、力学参数与 39 词标签命名空间配置方法
tags: [域/LLM与知识管理]
sources:
  - "[Obsidian Graph View 官方帮助](https://obsidian.md/help/plugins/graph)"
status: active
---

# Obsidian关系图谱配置指南

面向 oh-my-wiki 的图谱配置，四步走：**身份分色 → 过滤降噪 → 力学布局 → 标签命名空间**。

> 图谱设置存于 `.obsidian/graph.json`，**已随仓库分发**（2026-10-08 移出 gitignore，pull 即得配色与开关）——换设备后照本文核对即可。

## 一、Filters 四开关

| 开关 | 建议 | 原因 |
|------|------|------|
| **Tags** | **开** | 标签作为节点入图。曾因 `clippings`（177 篇剪藏共用一词）糊成全图最大星团；2026-10-06 标签纳管后 39 词分布均匀，标签桥接三区的连接正是标签体系的价值（用户偏好常开） |
| **Attachments** | **开** | 附件入图；当前库内暂无附件文件（图片断链待补），补图后自动吃到分组色 |
| **Orphans** | **开** | 孤页常显——否则 workspace 里 26 篇零链接文章在图里完全不可见 |
| **Unresolved** | 开 | 让断链在图里现形 |

> 本库当前值（2026-10-07 起）：`showTags/showAttachments/showOrphans=true`、`hideUnresolved=false`（即 Unresolved 开）；4 个图谱书签同步这四开关。

搜索框支持查询语法，是最强的降噪手段：

```
path:"wiki"                只看知识层
-path:"raw"                排除剪藏
path:"wiki/atoms/concepts" 只看概念层
file:RAG                   按文件名
```

## 二、颜色分组（12 条）

颜色分组按**自上而下首个匹配**生效（first-match-wins），排序分三层：**附件置顶**（须先于 workspace/raw 路径命中，否则树下的图片被正文身份色抢先）→ **7 条内容身份**（回答"谁写的"：你写的 workspace、Agent 生成的 wiki、剪藏的 raw，外加项目文档）→ **4 条标签命名空间殿后**（`tag:` 查询同样会命中带标签的**正文**，必须排在所有 path 组之后，落到这里的就只剩纯标签节点）。

**配色设计（2026-10-07 二次改版：连续渐变色板）**：8 色一整条渐变——明度从亮到暗**等差递减**，色相从橙黄**单调过渡**到靛蓝（经红/品红/紫），用 OKLCH 感知均匀插值、等彩度（依据《色彩搭配原理》：等角度步长＝等感知变化），不再是"四色各做四档"。端点互补对仍取 [Paletton 方案](https://paletton.com/#uid=72P0U0kllllaFw0g0qFqFg0w0aF)（靛蓝 CSS 233° ↔ 橙黄 CSS 44°）：

- ✍️ **亮橙黄＝你手写**（workspace）— 渐变最亮端，人工创作
- 🤖 **紫→靛蓝＝Agent 维护**（wiki）— 渐变最暗端，族内 4 级明度阶梯分聚类（越活跃越亮）
- 📰 **中段珊瑚/鲑红＝外来与文档**（raw、项目文档）— 处在你与 Agent 之间
- 🏷️ **青绿 4 级＝标签索引**（#域/#主题/#任务/#方法）— 色相在橙黄→靛蓝渐变弧**之外**，专属元数据身份；`tag:#域` 依官方规则命中全部嵌套子标签
- 🖼️ **石板灰＝附件** — 中性材料色，不参与渐变
- 第 4 梯位 玫红 `#D47885` 为**备用分组色**，暂无查询占用

**数组顺序＝命中优先级**；梯位＝颜色在渐变中的位置，两者无关：

| 位置 | 查询 | 色 | 含义 |
|------|------|----|------|
| 置顶 | `path:"attachments"` | 石板灰 `#8F95A8` | 附件/图片（防被正文色抢先，非渐变） |
| 1 | `path:"workspace"` | 亮橙黄 `#FDD89A` | 你的个人创作（最亮端） |
| 2 | `file:"AGENTS.md" OR file:"README.md" OR file:"CONTEXT.md" OR file:"Home.md" OR file:"PROMPT.md" OR file:"BOUNDARY.md"` | 珊瑚橙 `#FCB47E` | 项目文档 |
| 3 | `path:"raw"` | 鲑红 `#EE937D` | 原始剪藏 |
| 4 | —（备用） | 玫红 `#D47885` | 预留分组色 |
| 5 | `path:"wiki/synthesis"` | 品红 `#B3638C` | 综合层（最活跃→wiki 最亮） |
| 6 | `path:"wiki/atoms/concepts"` | 玫紫 `#8D528F` | 概念页（稳定） |
| 7 | `path:"wiki/atoms"` | 紫 `#64448A` | 其余原子（实体/数据） |
| 8 | `path:"wiki"` | 靛蓝 `#38387D` | wiki 兜底（最暗端） |
| 殿后 | `tag:#域` | 青绿 `#52BFB9` | 标签·域（13 词，结构骨架→最亮） |
| 殿后 | `tag:#主题` | 青绿 `#2FA29D` | 标签·主题（20 词） |
| 殿后 | `tag:#任务` | 青绿 `#168580` | 标签·任务（4 词） |
| 殿后 | `tag:#方法` | 青绿 `#0F6864` | 标签·方法（2 词） |

等价的 JSON（关闭 Obsidian 后贴进 `.obsidian/graph.json` 的 `colorGroups`）：

```json
"colorGroups": [
  { "query": "path:\"attachments\"",      "color": { "a": 1, "rgb": 9409960 } },
  { "query": "path:\"workspace\"",        "color": { "a": 1, "rgb": 16636058 } },
  { "query": "path:\"wiki/synthesis\"",   "color": { "a": 1, "rgb": 11756428 } },
  { "query": "path:\"wiki/atoms/concepts\"","color": { "a": 1, "rgb": 9261711 } },
  { "query": "path:\"wiki/atoms\"",       "color": { "a": 1, "rgb": 6571146 } },
  { "query": "path:\"wiki\"",             "color": { "a": 1, "rgb": 3684477 } },
  { "query": "path:\"raw\"",              "color": { "a": 1, "rgb": 15635325 } },
  { "query": "file:\"AGENTS.md\" OR file:\"README.md\" OR file:\"CONTEXT.md\" OR file:\"Home.md\" OR file:\"PROMPT.md\" OR file:\"BOUNDARY.md\"", "color": { "a": 1, "rgb": 16561278 } },
  { "query": "tag:#域",                   "color": { "a": 1, "rgb": 5423033 } },
  { "query": "tag:#主题",                 "color": { "a": 1, "rgb": 3121821 } },
  { "query": "tag:#任务",                 "color": { "a": 1, "rgb": 1475968 } },
  { "query": "tag:#方法",                 "color": { "a": 1, "rgb": 1009764 } }
]
```

> rgb = `(R << 16) | (G << 8) | B`。若主题色压过分组色，属 Obsidian 已知个案，恢复图谱默认设置或补一条 CSS 即可。

**本库已于 2026-10-07 按上述换版写入 `.obsidian/graph.json`**（含 §一 四开关全开），无需手贴；该文件自 2026-10-08 起入库，clone/pull 直接生效，仅当手工贴旧 JSON 时才需照此核对。

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
| 健康体检 | `-path:"raw"` | 找孤页（Orphans 已常开），配合 lint |
| 流入检查 | `path:"workspace"` | 看创作是否已关联知识库 |

**日常导航优先用 Local Graph**（右侧栏打开当前笔记）：`depth` 拉到 2~3 看二阶影响，比全库图谱有用得多。

## 五、标签命名空间（2026-10-06 重构并扩容，39 词）

**原则**：`domain` 给 Dataview，`tag` 给 Obsidian——图谱分组查询**吃不到 frontmatter 自定义字段**（只认 `path/tag/file`），所以域级信息必须在 tag 里保留一份，两处顶层**故意重复**。

```
#域/     13 个  与 frontmatter domain 一一对齐（tag 内不能有空格，故 domain 值里的空格去掉）
            机器学习 增长与营销 数据库 写作与技术博客 Agent架构与工程 复盘与方法论
            LLM与知识管理 媒介理论 Agent-First开发 软件架构与建模 软件工程 开发工具 面试方法论
#任务/    4 个  分类 回归 降维 聚类          （ML 任务类型）
#方法/    2 个  结构化思维 排版规范           （写作与思维方法）
#主题/   20 个  优化 广告归因 概率图模型 反作弊 贝叶斯 统计 神经网络 认知
            数据分析 学习理论 特征工程 集成学习 广告技术 MMP
            视频剪辑 网络与代理 终端与Shell 个人随笔 视觉设计 经济与金融   （2026-10-06 新增 6 词）
```

- **193 个内容页每页恰好 1 个域标签**；每页同时可挂任务/方法/主题标签（细粒度），域标签不重复
- lint **子集校验**：`check.py` 内 `VOCAB`（39 词，与 `EXPECTED_TAG_COUNT = 39` 双处同步）——wiki/workspace/raw 三区所有标签必须 ∈ 词表，词表外即报错
- **workspace 与 raw 已于 2026-10-06 纳入本命名空间**：workspace 71 个自由词归并入词表（ffmpeg→`主题/视频剪辑`、UA→`域/增长与营销` 等）；raw 177 篇剪藏按专栏目录/主题归域，`clippings`/`bilibili` 来源标签删除

## 六、关联通道的两个机制

1. **frontmatter 里的 `[[链接]]` 必须加引号** `"[[概念名]]"` 才会被识别进图谱与反链——YAML 会把裸的 `[[A]]` 解析成嵌套数组而非字符串。`workspace/` 的 `related` 字段已按此统一
2. **wiki→raw 的 730 条引用边**：主视图用 `-path:"raw"` 滤掉，另存一个溯源视图看引用关系——结构与溯源分开看

## 来源

- [Obsidian Graph View 官方帮助](https://obsidian.md/help/plugins/graph)

## 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-10-07 | 1.4 | 四开关默认全开（Tags/Attachments/Orphans/Unresolved，含 4 书签）；分组 7→12：附件 `path:"attachments"` 置顶（石板灰）、4 条标签命名空间殿后（青绿 4 级，`tag:#域` 命中嵌套子标签），正文不会被 tag 查询劫持 |
| 2026-10-07 | 1.3 | 二次改版：4 色×4 档模块化配色改为 8 色连续渐变（OKLCH 等差明度、等彩度，橙黄→靛蓝经红/品红/紫），梯位＝身份（1 手写 / 2 文档 / 3 剪藏 / 4 备用 / 5–8 wiki 阶梯）；graph.json 与 4 个书签同步 |
| 2026-10-07 | 1.2 | 配色换版：Paletton 靛蓝(233°)↔橙黄(44°)互补色卡，色相＝身份（橙黄=手写/靛蓝=Agent/石板灰=剪藏）、明度＝聚类，7 组全部替换 |
| 2026-10-06 | 1.1 | 词表 33→39（+视频剪辑/网络与代理/终端与Shell/个人随笔/视觉设计/经济与金融）；workspace 71 自由词与 raw 177 篇剪藏归域纳入 lint 子集校验 |
| 2026-10-06 | 1.0 | 初版：身份分组 7 条、四开关、力学实测值、33 词标签命名空间、related 引号机制 |
