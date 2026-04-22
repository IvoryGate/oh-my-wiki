# 知识库索引

> 最后更新: 2026-04-22（入库归因系列文章）

## 统计概览

| 类型 | 数量 |
|------|------|
| 概念 (concepts) | 48 |
| 实体 (entities) | 6 |
| 主题 (topics) | 0 |
| 洞察 (insights) | 0 |
| 指南 (howto) | 0 |
| **总计** | **54** |

---

## Dataview 动态查询

> 安装 [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) 插件后，以下查询会自动更新

### 所有概念 (按更新时间排序)

```dataview
TABLE title as "概念", created as "创建日期", updated as "更新日期"
FROM "wiki/atoms/concepts"
SORT updated DESC
```

### 所有实体 (按更新时间排序)

```dataview
TABLE title as "实体", created as "创建日期", updated as "更新日期"
FROM "wiki/atoms/entities"
SORT updated DESC
```

### 最近更新的页面

```dataview
TABLE title as "标题", type as "类型", updated as "更新日期"
FROM "wiki"
WHERE type
SORT updated DESC
LIMIT 10
```

---

## 原子知识 (atoms)

> 稳定的、可复用的知识砖块

### 概念 (concepts)

#### Agent 架构与工程

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[Agent-Loop]] | Agent 核心循环模式：感知-决策-行动-反馈 | 2026-04-18 |
| [[Workflow-vs-Agent]] | 工作流与智能体的核心区别 | 2026-04-18 |
| [[Agent-Control-Patterns]] | 五种 Agent 控制模式 | 2026-04-18 |
| [[Harness-Engineering]] | 验收基础设施：测试、验证与约束 | 2026-04-18 |
| [[Context-Engineering]] | 上下文工程：防止 Context Rot | 2026-04-18 |
| [[Skills-System]] | Skills 按需加载系统 | 2026-04-18 |
| [[ACI]] | Agent-Computer Interface：工具设计原则 | 2026-04-18 |
| [[Memory-System]] | Agent 记忆系统：四种记忆类型 | 2026-04-18 |
| [[Multi-Agent-Organization]] | 多 Agent 组织与协作模式 | 2026-04-18 |
| [[Agent-Evaluation]] | Agent 评测体系 | 2026-04-18 |
| [[Agent-Tracing]] | Agent 追踪与可观测性 | 2026-04-18 |
| [[Long-Task-Management]] | 长任务管理与跨 Session 恢复 | 2026-04-18 |

#### Agent-First 开发

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[Agent-First-Development]] | 智能体优先开发模式 | 2026-04-18 |
| [[Architecture-Constraints]] | 架构约束与不变量 | 2026-04-18 |
| [[Progressive-Disclosure]] | 渐进式披露原则 | 2026-04-18 |

#### LLM 与知识管理

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[LLM-Wiki]] | 使用 LLM 构建个人知识库的模式 | 2026-04-17 |
| [[RAG]] | 检索增强生成技术 | 2026-04-20 |

#### 增长与营销

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[MMP-Attribution]] | 第三方归因解决方案 | 2026-04-18 |
| [[SKAN-Attribution]] | Apple 官方归因体系 (iOS) | 2026-04-18 |
| [[Last-Click-Rule]] | 广告归因核心规则 | 2026-04-18 |
| [[多触点归因]] | 多触点归因模型体系 | 2026-04-21 |
| [[线性归因]] | 每个触点平均分配功劳 | 2026-04-21 |
| [[时间衰减归因]] | 离转化越近权重越高 | 2026-04-21 |
| [[U型归因]] | 首尾重点加权 | 2026-04-21 |
| [[Shapley值]] | 博弈论公平归因 | 2026-04-21 |
| [[Duplicate-Attribution]] | 一个激活付多份钱的问题 | 2026-04-18 |
| [[Attribution-Gap]] | MMP 与大媒体归因差异 | 2026-04-18 |
| [[User-App-Pair]] | 用户覆盖模型 (人货场) | 2026-04-20 |
| [[Audience-Definition]] | 受众定义三问 | 2026-04-20 |
| [[High-Value-Channel]] | 高价值渠道识别 | 2026-04-18 |
| [[Channel-Launch-Strategy]] | 渠道起量六要素 | 2026-04-18 |
| [[Network-Cognition-Gap]] | 渠道能力差异 | 2026-04-18 |
| [[归因链接]] | 广告追踪技术链接 | 2026-04-22 |
| [[助攻率]] | 非最后点击渠道贡献率 | 2026-04-22 |

#### 复盘与方法论

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[FuPan]] | 复盘方法论：通过对过去的分析优化未来 | 2026-04-19 |
| [[CLAP-Model]] | 复盘四环节：对比-逻辑-认知-规划 | 2026-04-19 |
| [[OPTM-Framework]] | 复盘三层框架：组织-流程-工具方法 | 2026-04-19 |
| [[PDCA-Model]] | 戴明环：质量管理经典模型 | 2026-04-19 |
| [[PDF-Model]] | 柳传志环：沙盘推演-执行-复盘 | 2026-04-19 |
| [[AAR-Model]] | 任务后检视：美军敏捷复盘方法 | 2026-04-19 |

#### 写作与技术博客

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[Blog-Content-Writing-Practices]] | 博文写作的通用实践要点（受众、结构、SEO、引用与校对等） | 2026-04-20 |
| [[Tech-Blog-Article-Types]] | 技术博客四类：细节型、干货型、实践总结型、杂谈型及流量特征 | 2026-04-20 |
| [[Pyramid-Principle]] | 金字塔原理在技术大纲中的三个「上下」 | 2026-04-20 |
| [[MECE]] | 相互独立、完全穷尽的分类原则 | 2026-04-20 |
| [[Title-4U-Formula]] | 标题 4U：紧迫、独特、明确、有用 | 2026-04-20 |

#### 软件架构与建模

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[DDD]] | 领域驱动设计：分层、战术模式与模块化要点 | 2026-04-20 |

### 实体 (entities)

| 实体 | 描述 | 更新日期 |
|------|------|----------|
| [[ZhangPeng]] | 复盘专家，《跟着高手学复盘》专栏作者 | 2026-04-19 |
| [[erickfang]] | 出海增长专家，《出海增长浅谈》作者 | 2026-04-18 |
| [[Codex]] | OpenAI 代码生成智能体 | 2026-04-18 |
| [[OpenAI]] | AI 研究和部署公司 | 2026-04-20 |
| [[Karpathy]] | AI 研究员，LLM Wiki 提出者 | 2026-04-17 |
| [[Phodal]] | 技术写作者（黄峰达），Phodal 博客 | 2026-04-20 |

---

## 综合知识 (synthesis)

> 沉淀后的成品，带有个人判断和实践痕迹

### 主题 (topics)

> 领域性的综合指南，从 `workspace/topics/` 沉淀而来

*暂无内容*

### 洞察 (insights)

> 跨越多个领域的个人洞察，从 `workspace/Done/` 沉淀而来

*暂无内容*

### 指南 (howto)

> 可操作的步骤指南，从 `workspace/Done/` 沉淀而来

*暂无内容*

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
```

---

## 最近更新

> 详细日志见 [[log.md]]

1. [2026-04-22] 入库 SimoneLee 归因系列文章（4篇），创建 2 个概念页
2. [2026-04-21] 健康检查与修复：修复断裂链接、创建马尔可夫链归因页面、为孤立页面添加入链
3. [2026-04-21] 入库归因文章 2 篇，创建 5 个概念页
3. [2026-04-20] lint：修正 graph 边统计、断裂链接（RAG/受众/OpenAI），补 Pyramid↔MECE 边
4. [2026-04-20] 入库写作与 DDD 资料（4 篇 raw），创建 6 个概念页、1 个实体页；修正 graph 中 Tmux 的悬空边
5. [2026-04-19] 入库复盘方法论文章（2 篇），创建 6 个概念页、1 个实体页
6. [2026-04-18] 入库增长营销系列文章（6 篇），创建 10 个概念页、1 个实体页
7. [2026-04-18] 架构升级：添加知识沉淀机制、话题追踪、更新机制
8. [2026-04-18] 入库 Agent 工程实践文章，创建 17 个概念页、2 个实体页
9. [2026-04-17] 入库 [[raw/articles/llm-wiki.md]]，创建 LLM Wiki 相关知识页
