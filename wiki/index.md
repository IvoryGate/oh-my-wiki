# 知识库索引

> 最后更新: 2026-04-18

## 统计概览

|| 类型 | 数量 |
||------|------|
|| 概念 (concepts) | 17 |
|| 实体 (entities) | 3 |
|| 主题 (topics) | 0 |
|| 洞察 (insights) | 0 |
|| 指南 (howto) | 0 |
|| **总计** | **20** |

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

|| 概念 | 描述 | 更新日期 |
||------|------|----------|
|| [[Agent-Loop]] | Agent 核心循环模式：感知-决策-行动-反馈 | 2026-04-18 |
|| [[Workflow-vs-Agent]] | 工作流与智能体的核心区别 | 2026-04-18 |
|| [[Agent-Control-Patterns]] | 五种 Agent 控制模式 | 2026-04-18 |
|| [[Harness-Engineering]] | 验收基础设施：测试、验证与约束 | 2026-04-18 |
|| [[Context-Engineering]] | 上下文工程：防止 Context Rot | 2026-04-18 |
|| [[Skills-System]] | Skills 按需加载系统 | 2026-04-18 |
|| [[ACI]] | Agent-Computer Interface：工具设计原则 | 2026-04-18 |
|| [[Memory-System]] | Agent 记忆系统：四种记忆类型 | 2026-04-18 |
|| [[Multi-Agent-Organization]] | 多 Agent 组织与协作模式 | 2026-04-18 |
|| [[Agent-Evaluation]] | Agent 评测体系 | 2026-04-18 |
|| [[Agent-Tracing]] | Agent 追踪与可观测性 | 2026-04-18 |
|| [[Long-Task-Management]] | 长任务管理与跨 Session 恢复 | 2026-04-18 |

#### Agent-First 开发

|| 概念 | 描述 | 更新日期 |
||------|------|----------|
|| [[Agent-First-Development]] | 智能体优先开发模式 | 2026-04-18 |
|| [[Architecture-Constraints]] | 架构约束与不变量 | 2026-04-18 |
|| [[Progressive-Disclosure]] | 渐进式披露原则 | 2026-04-18 |

#### LLM 与知识管理

|| 概念 | 描述 | 更新日期 |
||------|------|----------|
|| [[LLM-Wiki]] | 使用 LLM 构建个人知识库的模式 | 2026-04-17 |
|| [[RAG]] | 检索增强生成技术 | 2026-04-17 |

### 实体 (entities)

|| 实体 | 描述 | 更新日期 |
||------|------|----------|
|| [[Codex]] | OpenAI 代码生成智能体 | 2026-04-18 |
|| [[OpenAI]] | AI 研究和部署公司 | 2026-04-18 |
|| [[Karpathy]] | AI 研究员，LLM Wiki 提出者 | 2026-04-17 |

---

## 综合知识 (synthesis)

> 沉淀后的成品，带有个人判断和实践痕迹

### 主题 (topics)

> 领域性的综合指南，从 `workplace/topics/` 沉淀而来

*暂无内容*

### 洞察 (insights)

> 跨越多个领域的个人洞察，从 `workplace/Done/` 沉淀而来

*暂无内容*

### 指南 (howto)

> 可操作的步骤指南，从 `workplace/Done/` 沉淀而来

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
workplace/          # 实践过程
├── Done/           # 单篇完成 → wiki/synthesis/howto 或 insights
└── topics/         # 话题积累 → wiki/synthesis/topics
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
```

---

## 最近更新

> 详细日志见 [[log.md]]

1. [2026-04-18] 架构升级：添加知识沉淀机制、话题追踪、更新机制
2. [2026-04-18] 入库 Agent 工程实践文章，创建 17 个概念页、2 个实体页
3. [2026-04-17] 入库 [[raw/articles/llm-wiki.md]]，创建 LLM Wiki 相关知识页
