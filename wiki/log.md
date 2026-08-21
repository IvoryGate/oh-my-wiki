# 操作日志

> 记录知识库的所有变更历史

---

## [2026-08-21] ingest | 入库写作三篇（清脑/阿宝哥/皮卡小宝）

### 新增页面（10）
- 概念: [[写作起步-日常书写]] — 写作的爬行阶段，外化工作记忆、启动元认知
- 概念: [[写作价值心法]] — 写长久有用的；内部动机 vs 外部动机
- 概念: [[顶级信息论与输入输出比]] — 顶级信息论 + 10万:1千 + 知识写作vs经验写作
- 概念: [[滑梯理论]] — 易读性、故事/痛点开头、情绪先于理性
- 概念: [[作品意识与打磨意识]] — 精品/打磨 vs 日更
- 概念: [[SCQ法则]] — 背景-冲突-疑问的讲故事结构
- 实体: [[清脑作者]] / [[阿宝哥]] / [[皮卡小宝]] — 三位作者
- 主题: [[写作方法论]] — 心法→起步→技法→逻辑表达的写作主线

### 更新页面（1）
- [[Pyramid-Principle]] — 由原「技术大纲三上下」扩展为完整解读：结论先行、总结概括、归类分组（四顺序）、SCQ 法则，关联 MECE/SCQ

### 来源
- [[raw/articles/关于写作，这是我目前能想到最全的.md]]
- [[raw/articles/写了 200 多篇文章后，我总结的写作心得.md]]
- [[raw/articles/如何逻辑思考，清晰表达？《金字塔原理》和本文值得一读！.md]]

---

## [2026-08-18] chore | 移除被 git 追踪的空文件

### 背景
根目录 `AAR-Model.md` 反复出现：实为 0 字节空文件（git 在 2026-07-29 的 move 提交中把空文件误判为重命名产生），被 git 追踪后，任何 pull/checkout/同步操作都会将其从索引恢复。

### 处理
- `git rm` 根目录 `AAR-Model.md`（真实内容在 [[AAR-Model|wiki/atoms/concepts/AAR-Model.md]]，不受影响）
- `git rm --cached` `raw/articles/未命名.md`（解除追踪，后经用户确认删除该空文件）

### 涉及文件
- AAR-Model.md（根目录，已删除）
- raw/articles/未命名.md（解除追踪）
## [2026-08-18] ingest | 入库机器学习加餐/总结课与中文技术文档写作规范

### 新增页面（5）
- 概念: [[机器学习工程师]] — 数据岗位三角色分工、工程化/产品化核心职责
- 概念: [[马尔可夫链]] — 马尔可夫性、稳态分布、极限定理与"结构性宿命"启示
- 主题: [[机器学习模型体系]] — 从线性回归出发的模型演化脉络（synthesis 首批主题页）
- 主题: [[贝叶斯学习模型体系]] — 从高斯分布出发的贝叶斯模型体系
- 指南: [[中文技术文档写作规范]] — 合并 7 个章节文件（标点/数值/段落/链接/体系/文本/标题）

### 来源
- [[raw/articles/如何成为机器学习工程师？.md]]
- [[raw/articles/总结课 机器学习的模型体系.md]]
- [[raw/articles/总结课 贝叶斯学习的模型体系.md]]
- [[raw/articles/马尔可夫链的宿命论.md]]
- [[raw/articles/marks.md]] 等 7 个写作规范章节

### 修复
- manifest.json 损坏条目：补回「01 CLAP模型」缺失的 path 字段，哈希同步为当前值
- graph.json 补回缺失节点「知识体系」（其边仍存在，7-29 修复时误删）

### graph.json 更新
- 新增 5 节点、16 边；补回「知识体系」节点
- 统计修正为与实际数组一致：136 节点（127 概念/6 实体/2 主题/1 指南）、72 边
- 注：此前 stats 声称 123 边，实际数组仅 56 边，本次一并修正

### 涉及文件
- wiki/atoms/concepts/机器学习工程师.md
- wiki/atoms/concepts/马尔可夫链.md
- wiki/synthesis/topics/机器学习模型体系.md
- wiki/synthesis/topics/贝叶斯学习模型体系.md
- wiki/synthesis/howto/中文技术文档写作规范.md
- wiki/index.md
- wiki/graph.json
- raw/manifest.json

---

## [2026-07-29] create | 机器学习话题追踪

- 创建 `workspace/topics/MachineLearning/` 话题追踪目录
- 创建 `_tracker.md`：知识地图覆盖 9 个子领域、50+ 概念、进度表
- 现有 58 个 ML 概念页均为 draft，待后续完善

---

## [2026-07-29] update | 首页改造为仪表盘风格

- 标题从「知识库索引」改为「Oh-My-Wiki」
- 新增「状态总览」：合并统计与活跃领域概览
- 新增「正在进行」：列出 workspace 6 篇活跃文章
- 新增「快速导航」：领域关键词快速跳转
- 精简 Dataview 查询，移除非必需分页查询
- 原有原子知识/知识流转/图谱/最近更新保持不变

---

## [2026-07-29] lint | 全面维护：统计修正、图谱修复、索引补齐

### 变更内容
- **wiki/index.md**：概念统计 110→125，总计 116→131；补齐知识管理（4）、媒介理论（5）、开发工具（1）缺失分组；补齐 22 个缺失的机器学习概念条目；更新最近更新列表
- **wiki/graph.json**：移除重复节点「直觉」（重复出现 2 次），修正统计：132→131 节点，126→125 概念
- 新增 workspace 文章（Doing/ 目录）均已正常记录，无需额外操作
- 发现 `碎碎念-写在离开北京前夕.md` 缺少 frontmatter，已记录待处理

### 涉及文件
- wiki/index.md
- wiki/graph.json

---

## [2026-07-03] lint | 标签体系优化

### 改造内容
- 精简标签体系：133 个标签 → ~25 个（8 领域标签 + 17 主题标签）
- 消除同义/重叠标签：机器学习/ML、敏捷/敏捷开发/敏捷管理 等合并
- 消除多余粒度：去除仅用于 1 页的碎片标签
- 去除实体角色型标签：研究员、作家、专栏作者 等

### 新标签体系

**领域标签（每页 1 个）**：
`机器学习` (58) · `广告归因` (22) · `Agent工程` (15) · `软件工程` (6) · `复盘` (6) · `技术写作` (5) · `媒介理论` (5) · `知识管理` (6)

**主题标签（跨领域，0-3 个/页）**：
`分类` · `回归` · `神经网络` · `概率图模型` · `贝叶斯` · `集成学习` · `降维` · `特征工程` · `优化` · `过拟合` · `聚类` · `学习理论` · `统计` · `归因模型` · `广告技术` · `复盘模型` · `过程模型` · `结构化思维` · `媒介生态` · `认知` · `方法论` · `架构`

### 涉及文件
- 所有 116 个 wiki 页面的 frontmatter tags 字段

---

## [2026-04-29] 入库 | 软件工程系列文章

### 新增概念（7个）
- 软件工程 — 工程化方法开发维护软件：过程+方法+工具
- 软件危机 — 60年代暴露的开发维护问题
- 瀑布模型 — 传统分阶段过程模型
- 工程思维 — 用项目视角解决问题的思考方式
- 人月神话 — 经典项目管理著作
- 敏捷开发 — 2001年轻量级开发方法

### graph.json 更新
- 新增 7 节点、8 边
- 更新统计：125→132 节点，115→123 边

### 来源
- [[raw/articles/00 开篇词 你为什么应该学好软件工程？.md]]
- [[raw/articles/01 到底应该怎样理解软件工程？.md]]
- [[raw/articles/02 工程思维：把每件事都当作一个项目来推进.md]]

---

## [2026-04-27] 入库 | 娱乐至死视频

### 新增概念（5个）
- 媒介即隐喻 — 媒介不只是信息通道，它本身就在塑造文化形态
- 娱乐至死 — 整个社会把一切都变成娱乐，严肃思考被自愿交出
- 伪语境 — 电报创造的信息泛滥但无法指导行动的状态
- 哥波尼世界 — 电报+摄影术创造的无连续性信息环境
- 奥威尔与赫胥黎 — 两种反乌托邦警告的对比

### graph.json 更新
- 新增 5 节点、7 边
- 更新统计：120→125 节点，108→115 边

### 来源
- [[raw/videos/2026-04-26-【30分钟读一本书】总沉迷短视频难以自拔？细读《娱乐至死》警惕媒介的隐秘影响.md]]

## [2026-04-26] 入库 | 知识体系视频

### 新增概念（4个）
- 知识体系 — 多个知识点互相联系形成整体
- 经典知识联系 — 人类研究明白的知识联系类型（因果/互补/时序/等价/前提结论/概念层级/矛盾/互斥等）
- 工作记忆 — 容量约4个单位，需外化
- 直觉 — 有规律的信息处理过程，非瞎猜

### graph.json 更新
- 新增 4 节点、6 边
- 更新统计：116→120 节点，102→108 边

### 来源
- [[raw/videos/2026-04-26-四个步骤，建立知识体系的简单方法，借助直觉，直觉不是瞎猜，不是超能力【吸收人类优秀学习理论32】.md]]

## [2026-04-23] lint | graph.json 修复

- 修复 graph.json 结构错误（JSON 损坏，节点数据重复）
- 重建 graph.json：116 节点、102 边
- 更新 stats：概念 110，实体 6，总计 116

## [2026-04-23] lint | 知识库完整修复

### 来源链接修复
- 为 87 个概念页添加"来源"部分
- 格式：## 来源 → [[raw/articles/xxx.md]]

### manifest.json 补充
- 登记机器学习 40 讲（40 篇文章）
- 统计：26 → 66

### 缺失概念页创建
- 反向传播、激活函数、过拟合、损失函数、交叉熵、梯度下降、超参数、Softmax

### graph.json 更新
- 新增 9 个节点、25 条边
- 更新统计：概念 91→100，节点 97→106，边 89→114

### index.md 更新
- 概念数 101→110，总数 107→116

## [2026-04-23] lint | 健康检查与修复

- 创建缺失概念页：岭回归、LASSO、PAC可学习性、VC维、贝叶斯定理、核函数、变量消除、自编码器
- 更新 graph.json：新增 8 个节点、新增 17 条边，修正统计数据
- 更新 wiki/index.md：概念数从 93 更新为 101
- 保留 Tmux 页面（用户确认保留）

## [2026-04-23] ingest | 机器学习40讲 15-40（26篇）

- 来源: [[raw/articles/15 从回归到分类：联系函数与降维.md]] 至 [[raw/articles/40 结构学习：基于约束与基于评分.md]]
- 创建概念页: Logistic回归、线性判别分析、联系函数、广义线性模型、支持向量机、核技巧、K近邻、聚类分析、基函数扩展、感知器、神经网络、深度学习、表示学习、决策树、集成学习、梯度提升、随机森林、概率图模型、朴素贝叶斯、贝叶斯网络、马尔可夫随机场、高斯网络、高斯过程、隐马尔可夫模型、线性动态系统、推断、变分推断、MCMC、EM算法、混合模型、结构学习
- 注: 公式待未来详细校准

## [2026-04-23] ingest | 机器学习40讲 01-14 补录入库

- 来源: [[raw/articles/01 频率视角下的机器学习.md]] 至 [[raw/articles/14 非线性降维：流形学习.md]]
- 创建概念页: 频率学派、贝叶斯学派、最大似然估计、计算学习理论、正则化、主成分分析、流形学习、距离度量、降维、线性回归、特征工程

## [2026-04-22 20:30] ingest | 广告竞价与数据差异文章（3篇）
- 来源:
  - [[raw/articles/广告竞价背后的逻辑和模型算法（一）.md]]
  - [[raw/articles/广告竞价背后的逻辑和模型算法（二）.md]]
  - [[raw/articles/渠道MMPBI的数据差异剖析.md]]
- 创建概念页:
  - [[DSP]] - 需求方平台
  - [[ADX]] - 广告交易所
  - [[SSP]] - 供应方平台
  - [[RTB]] - 实时竞价
- 更新 [[Attribution-Gap]] 补充数据差异内容
- 更新 manifest.json 和 graph.json

## [2026-04-22 12:00] ingest | SimoneLee 归因系列文章（4篇）

## [2026-04-21 20:00] lint | 知识库健康检查与修复
- 修复断裂链接: 26个文件中的 `[[文章标题]]` 格式链接改为 `[[raw/articles/文件名.md]]`
- 创建概念页: [[马尔可夫链归因]]
- 为孤立页面添加入链: ACI, Attribution-Gap, Codex, DDD, Duplicate-Attribution, Long-Task-Management, Multi-Agent-Organization, Network-Cognition-Gap, erickfang
- 更新过时页面: [[LLM-Wiki]], [[Karpathy]] 更新时间
- 生成健康检查报告: [[lint-report-2026-04-21.md]]

## [2026-04-21 18:00] ingest | 归因文章 2 篇
- 来源: [[raw/articles/广告归因8种模型：预算怎么分才不浪费？]], [[raw/articles/用户到底被哪个广告打动了？三种主流归因模型全解析]]
- 创建概念页: [[多触点归因]], [[线性归因]], [[时间衰减归因]], [[U型归因]], [[Shapley值]]
- 补充 Last-Click-Rule 关联

---

## 日志格式

```
## [YYYY-MM-DD HH:MM] 类型 | 对象
- 操作描述
- 相关页面: [[xxx]]
```

**操作类型**：
- `ingest`: 处理原始资料
- `query`: 知识查询归档
- `lint`: 健康检查修复
- `flow`: workspace 流入 wiki
- `create`: 直接创建内容
- `update`: 更新内容

---

## 2026年4月

## [2026-04-20] lint | 知识库健康检查
- 修正 `graph.json` 中 `stats.totalEdges` 与实有边数不一致；补 `Pyramid-Principle` → `MECE` 边并同步统计
- 修复断裂或不当 wikilink：`RAG` 中「知识图谱」、`Audience-Definition`/`User-App-Pair` 中 `Channel-Strategy` → `Channel-Launch-Strategy`、`OpenAI` 中 `Aardvark`
- 说明：多处正文仍用 `[[文章标题]]` 指代 raw，Obsidian 需依赖同名解析；建议逐步改为 `[[raw/articles/….md]]`（与 2026-04-19 lint 口径一致）

## [2026-04-20] update | raw 路径修正（鹅厂技术写作）
- 资料已移至 `raw/articles/鹅厂多位技术同学关于如何写好技术文章的经验.md`
- 已同步：[[MECE]]、[[Pyramid-Principle]]、[[Title-4U-Formula]] 的 `sources`、`wiki/graph.json`、`raw/manifest.json`、`wiki/log.md` 历史条目中的链接

## [2026-04-20 12:00] ingest | 写作方法论与 DDD 视频稿
- 新入库 raw（manifest 登记）:
  - [[raw/articles/如何撰写一篇阅读10w+博文（10个成功秘诀）.md]]
  - [[raw/articles/程序员怎样才能写出一篇好的博客或者技术文章.md]]
  - [[raw/articles/鹅厂多位技术同学关于如何写好技术文章的经验.md]]
  - [[raw/videos/2026-04-19-白话讲解领域驱动设计domain driven design (DDD).md]]
- 创建概念页:
  - [[Blog-Content-Writing-Practices]] — 通用博文写作要点（受众、结构、SEO、引用、校对、CTA）
  - [[Tech-Blog-Article-Types]] — 程序员技术博客四类与流量/分发
  - [[Pyramid-Principle]] — 金字塔大纲三「上下」
  - [[MECE]] — 分类不重叠不遗漏
  - [[Title-4U-Formula]] — 标题 4U
  - [[DDD]] — 领域驱动设计分层与战术概念精要
- 创建实体页:
  - [[Phodal]]
- 更新 `wiki/graph.json`: 新增节点 7；边新增 6、移除 Tmux 悬空边 5，合计 43 条
- 更新 `wiki/index.md` 统计与索引区块

## [2026-04-19 15:00] lint | 知识库健康检查与修复
- 删除未处理的视频文件: `raw/videos/BV1ju6QBzENE.md`
- 更新 manifest.json 状态:
  - 两篇复盘文章状态从 `processing` 改为 `done`
  - 统计: total 11, pending 0, processing 0, done 11
- 统一 sources 链接格式:
  - 28 个页面的 sources 从 `"[[标题]]"` 改为 `[[raw/articles/文件名.md]]`
  - 涉及 Agent 系列、归因系列、受众系列所有页面
- 修复断裂链接:
  - `[[知识图谱]]` 改为内联说明（不创建独立页面）
- 修复范围:
  - concepts: 23 个页面
  - entities: 3 个页面 (Codex, OpenAI, erickfang)

## [2026-04-19 10:00] ingest | 复盘方法论文章
- 来源: 张鹏《跟着高手学复盘》专栏
- 来源文章:
  - [[raw/articles/01 CLAP模型：一个优秀的复盘模型是什么样的？.md]]
  - [[raw/articles/02 OPTM框架：怎么使用CLAP模型？.md]]
- 创建概念页:
  - [[FuPan]] - 复盘方法论：通过对过去的分析优化未来
  - [[CLAP-Model]] - 复盘四环节：对比-逻辑-认知-规划
  - [[OPTM-Framework]] - 复盘三层框架：组织-流程-工具方法
  - [[PDCA-Model]] - 戴明环：质量管理经典模型
  - [[PDF-Model]] - 柳传志环：沙盘推演-执行-复盘
  - [[AAR-Model]] - 任务后检视：美军敏捷复盘方法
- 创建实体页:
  - [[ZhangPeng]] - 复盘专家，《跟着高手学复盘》专栏作者
- 建立知识链接 11 条
- 更新 graph.json: 节点 38 个，边 37 条
- 核心洞察:
  - CLAP 弥补 PDCA 缺乏战略调整机制的局限
  - CLAP 在 OPTM 框架下提高 PDF 的可复制性
  - AAR 是 CLAP 的敏捷简化版本

## [2026-04-18 15:30] ingest | 增长营销系列文章
- 来源: erickfang《出海增长浅谈》系列
- 来源文章:
  - [[raw/articles/关于归因你可能不知道的那些事(一）.md]]
  - [[raw/articles/关于归因你可能不知道的那些事（二）-Skan篇.md]]
  - [[raw/articles/关于归因你可能不知道的那些事（三）-策略篇.md]]
  - [[raw/articles/增长从确定目标开始.md]]
  - [[raw/articles/如何定义受众-正篇.md]]
  - [[raw/articles/如何定义受众-科普篇.md]]
  - [[raw/articles/渠道不起量的原因都在这里了！.md]]
- 创建概念页:
  - [[MMP-Attribution]] - 第三方归因解决方案
  - [[SKAN-Attribution]] - Apple 官方归因体系
  - [[Last-Click-Rule]] - 广告归因核心规则
  - [[Duplicate-Attribution]] - 重复计费问题
  - [[Attribution-Gap]] - MMP 与大媒体归因差异
  - [[User-App-Pair]] - 用户覆盖模型
  - [[Audience-Definition]] - 受众定义三问
  - [[High-Value-Channel]] - 高价值渠道识别
  - [[Channel-Launch-Strategy]] - 渠道起量六要素
  - [[Network-Cognition-Gap]] - 渠道能力差异
- 创建实体页:
  - [[erickfang]] - 出海增长专家
- 建立知识链接 10 条
- 更新 graph.json: 节点 31 个，边 26 条

## [2026-04-18 11:30] update | 知识库架构升级
- 添加 `workspace/topics/` 目录用于新话题积累
- 创建话题追踪模板: [[wiki/templates/topic-tracker.md]]
- 创建综合知识模板: [[wiki/templates/synthesis-template.md]]
- 更新 Agent.md: 添加知识沉淀规则、更新机制
- 更新 wiki/index.md: 反映新的知识流转规则

**核心变更**：
1. **两条沉淀路径**：
   - 单篇: `Done/` → `wiki/synthesis/howto` 或 `insights`
   - 系列: `topics/` → `wiki/synthesis/topics`
2. **更新机制**：已有内容直接在 `wiki/synthesis/` 更新，不回流
3. **状态标记**：`status: stable|evolving|outdated` + 变更日志

## [2026-04-18 10:50] ingest | Agent 工程实践文章
- 来源: [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
- 来源: [[raw/articles/工程技术：在智能体优先的世界中利用 Codex.md]]
- 创建概念页:
  - [[Agent-Loop]] - Agent 核心循环模式
  - [[Workflow-vs-Agent]] - 工作流与智能体区分
  - [[Agent-Control-Patterns]] - 五种控制模式
  - [[Harness-Engineering]] - 验收基础设施
  - [[Context-Engineering]] - 上下文工程
  - [[Skills-System]] - Skills 按需加载系统
  - [[ACI]] - Agent-Computer Interface
  - [[Memory-System]] - 记忆系统
  - [[Multi-Agent-Organization]] - 多 Agent 组织
  - [[Agent-Evaluation]] - Agent 评测
  - [[Agent-Tracing]] - Agent 追踪
  - [[Long-Task-Management]] - 长任务管理
  - [[Agent-First-Development]] - 智能体优先开发
  - [[Architecture-Constraints]] - 架构约束
  - [[Progressive-Disclosure]] - 渐进式披露
- 创建实体页:
  - [[Codex]] - OpenAI 代码生成智能体
  - [[OpenAI]] - OpenAI 公司
- 建立知识链接 16 条
- 更新 graph.json: 节点 20 个，边 16 条

## [2026-04-17 23:20] create | .gitignore
- 创建 .gitignore 文件
- 忽略 Obsidian 个人偏好配置（workspace.json, data.json）
- 保留共享配置（app.json, community-plugins.json, manifest.json）
- 忽略系统文件、临时文件、导出文件

## [2026-04-17 23:15] create | Agent 入门文档
- 创建 CONTEXT.md: 新 Agent 快速理解知识库
- 创建 PROMPT.md: 快速启动指南
- 创建 .cursorrules: Cursor IDE 配置
- 更新 README.md: 添加"为新 Agent 准备"章节

## [2026-04-17 23:00] update | Obsidian 插件配置
- 配置 Homepage: 启动打开 wiki/index.md
- 配置 Dataview: 启用内联查询和 JavaScript
- 配置 Marp Slides: 16:9 尺寸，默认主题
- 创建 CSS 片段: oh-my-wiki.css（表格美化、链接增强）
- 创建插件配置指南: [[wiki/templates/plugin-config.md]]

## [2026-04-17 22:50] create | 知识库扩展
- 添加 raw/social/ 目录支持社交媒体内容
- 创建 Dataview 查询模板: [[wiki/templates/dataview-queries.md]]
- 创建 Marp 幻灯片模板: [[wiki/templates/marp-template.md]]
- 更新 Agent.md: 添加插件集成规则和 Frontmatter 规范

## [2026-04-17 22:40] ingest | llm-wiki.md
- 来源: [[raw/articles/llm-wiki.md]]
- 创建概念页: [[LLM-Wiki]], [[RAG]]
- 创建实体页: [[Karpathy]]
- 建立关系: LLM-Wiki --proposed_by--> Karpathy
- 建立关系: LLM-Wiki --compares_to--> RAG

## [2026-04-17 22:30] create | 知识库初始化
- 创建目录结构
- 创建 manifest.json 和 graph.json
- 编写 Agent.md 和 README.md
- 创建 index.md 和 log.md
