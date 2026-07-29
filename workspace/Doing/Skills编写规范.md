---
title: Skills 编写规范
type: draft
created: 2026-05-18
updated: 2026-05-18
status: doing
tags: [Agent, Skills, 上下文工程, 程序性记忆]
related:
  - [[Skills-System]]
  - [[Context-Engineering]]
  - [[Progressive-Disclosure]]
  - [[ACI]]
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
---

# Skills 编写规范

> **用途**：把本文档交给**任意智能体**（Cursor、Codex、OpenClaw、自研 Agent 等），让它按同一套约定**编写或审校 Skill**。  
> **原则来源**：[[Skills-System]]、[[Context-Engineering]]（与运行时无关的 Agent 工程经验）。  
> **文件格式**：正文采用与 [Cursor Agent Skills](https://cursor.com/docs) 兼容的目录与 frontmatter，便于跨环境复用；**本文档不绑定某一 IDE**。

---

## 0. 文档服务对象

| 角色 | 读本文档做什么 |
|------|----------------|
| **Skill 作者 Agent** | 把用户给的 SOP / 规范 / 流程，落成可挂载的 Skill 包 |
| **运行时 Agent** | 按路由规则扫描 description、按需加载正文 |
| **人类维护者** | 定边界、审 description、控制 Skill 数量与粒度 |

Skill 的本质：**程序性记忆**——「怎么做某件事」；不是系统提示里的百科全书，也不是替代工具的万能插件。

---

## 1. 先判断：该不该做成 Skill

| 形态 | 适用 | 不适用 |
|------|------|--------|
| **Skill** | 可复用流程、团队规范、检查清单、领域 SOP | 一次性对话、极低频、纯百科知识 |
| **普通文档 / 知识库** | 查阅为主、无需每轮路由 | 需要精确「何时自动执行」的硬规则（应进系统提示 / 策略层） |
| **工具 / MCP** | 有状态、连外部系统、需结构化 I/O | 纯静态说明、可过滤的读操作 |
| **Shell / 已有命令** | 一条命令能完成 | 仍需大量「何时、为何、例外」判断 |

**决策口诀**：

1. **Skills 先于新工具**——领域知识用可加载文档管，比堆工具更灵活。  
2. **能用命令就不加工具**；**只需静态知识就不上重型集成**。  
3. **常驻层只放索引**（name + 短 description）；正文按需加载。  
4. 低频流程用普通文档；需要时再**显式点名**加载，不要塞进默认 Skill 列表。

---

## 2. 交付物：目录结构（格式对齐 Cursor，语义通用）

每个 Skill 是一个**目录**，至少包含 `SKILL.md`。与 Cursor Skills 格式一致，其他运行时只要实现「读目录 + 解析 frontmatter + 按需读正文」即可复用。

```
<skill-name>/
├── SKILL.md              # 必填：元数据 + 核心指令
├── reference.md          # 可选：长参考、API 表
├── examples.md           # 可选：输入输出样例
└── scripts/              # 可选：可执行脚本（由 Agent 执行，非人类手册）
```

**存放位置由部署环境决定**（本文档不规定）——例如项目内 `.cursor/skills/`、个人配置目录、或 Agent 工作区的 `skills/`。实现方在接入文档中说明路径即可。

---

## 3. `SKILL.md` 与元数据

### 3.1 推荐结构

```markdown
---
name: skill-name-here
description: >-
  第三人称；WHAT + WHEN + DON'T + 反例。见 §4。
disable-model-invocation: true
---

# Skill 标题

## 何时使用
## 步骤 / 工作流
## 反模式（勿误用）
## 附加资源
- [reference.md](reference.md)
```

### 3.2 元数据字段（与 Cursor 对齐）

| 字段 | 约束 | 含义（与运行时无关） |
|------|------|----------------------|
| `name` | ≤64 字符；`[a-z0-9-]` | Skill 唯一 ID |
| `description` | ≤1024 字符，非空 | **路由索引**，通常常驻上下文 |
| `disable-model-invocation` | 建议默认 `true` | `true`：仅在被用户/策略**显式选中**时加载全文；`false`：允许运行时根据 description **自动选用**（慎用，易误触发） |

其他运行时专有字段不要塞进 Skill；环境配置放在 Agent 的部署说明里。

### 3.3 体量与渐进式披露

- **`SKILL.md` 建议 < 500 行**；超出则拆 `reference.md`、`examples.md`。  
- **description = 索引，SKILL.md = 摘要流程，reference = 细节**——三层渐进加载。  
- 附属文件从 `SKILL.md` **只链一层**，避免深层引用导致只读到片段。  
- 默认模型已具备通用能力：**只补充它没有且稳定需要的知识**。

### 3.4 自由度分级

| 自由度 | 场景 | 写法 |
|--------|------|------|
| 高 | 评审、权衡 | 原则 + 判断标准 |
| 中 | 报告、纪要 | 模板 + 允许变体 |
| 低 | 发布、迁移、删数据 | 逐步清单 + `scripts/` |

可重复、易错的步骤优先固化成脚本，而不是每次让模型重写代码。

---

## 4. `description` 怎么写（最重要）

`description` 是**路由条件**，不是功能说明书。每个**已注册** Skill 的 description 都会进入常驻上下文；Skill 越多，冗长描述的成本线性上升。

### 4.1 必含四要素

1. **WHAT** — 一句话能力  
2. **WHEN（Use when）** — 用户意图、文件类型、关键词、任务名  
3. **DON'T（Don't use when）** — 明确排除  
4. **反例** — 1～3 条「Not for …」；缺反例时误触发率显著上升，**不是可选项**

推荐句式（第三人称，便于注入系统层）：

```yaml
description: >-
  [能力]. Use when [触发]. Don't use when [排除].
  Not for [反例1]; not for [反例2]. Output: [交付物].
```

### 4.2 长短与精度

```yaml
# ❌ 功能罗列（~45 tokens，常驻成本高）
description: |
  Handles complete deployment to production including checks,
  rollback, and verification. Use before any production deploy.

# ✅ 路由条件（~9 tokens）
description: Use when deploying to production or rolling back. Don't use for local or staging-only deploys.
```

- **太短**（如 `help with backend`）→ 误触发泛滥。  
- **太长** → 路由精度提升有限，多 Skill 时上下文爆炸。  

### 4.3 写法要求

| 维度 | 要求 |
|------|------|
| 人称 | 第三人称（「Processes…」「Use when…」） |
| 触发词 | 用户会说的词、扩展名、命令名 |
| 用户原文 | 若指定固定措辞，**原文写入** description 或正文，勿擅自改写 |
| 语言 | 与团队/用户一致；多语言环境可中英关键词并存 |

### 4.4 示例

```yaml
description: >-
  Extract text and tables from PDFs. Use when user works with .pdf or asks for PDF extraction.
  Don't use for scanned pages without OCR. Not for encrypted PDFs without password.

description: >-
  Review code for security and team standards. Use when reviewing PRs, diffs, or explicit code review requests.
  Don't use for architecture-only chats without code. Not for style-only passes unless requested.

description: >-
  Draft commit messages from staged diffs per repo conventions. Use when user asks to commit or write message.
  Don't use for git status/log only. Not for amending pushed commits unless user explicitly requests.
```

---

## 5. 正文怎么写

### 5.1 推荐章节

1. Quick start（3～7 步）  
2. 检查清单（`- [ ]`）  
3. 输出模板（固定格式时给完整 fenced 模板）  
4. Examples（真实 Input → Output，1～2 组）  
5. 条件分支（A → 流程 1，B → 流程 2）  
6. 验证闭环（必须执行的命令 / 脚本）  
7. 附加资源链接  

### 5.2 有副作用的 Skill

若涉及**写库、删文件、调付费 API、发外网、改生产**，正文必须写清：

- 执行前需用户确认的条件  
- 限流（批量写、遇 429 退避、禁止无意义循环调用）  
- 验证与回滚  

### 5.3 与系统提示、记忆的分工

| 层级 | 内容 | 特征 |
|------|------|------|
| 系统提示 / 策略 | 身份、绝对禁止、项目硬约束 | 短、稳、每轮必需 |
| Skill `description` | 路由索引 | 短、常驻 |
| `SKILL.md` | 怎么做（程序性记忆） | 按需加载 |
| `reference.md` 等 | 低频细节 | 二次按需 |
| 语义记忆（如 MEMORY.md） | 跨会话事实 | 与 Skill 互补，不互相替代 |

不变的前缀有利于缓存；**动态信息**（当前时间、本轮输入、工具返回）不要写进 Skill 常驻部分。

---

## 6. 运行时如何加载（任意 Agent 通用）

以下约定与具体产品无关；实现方在 Agent 配置里落地即可。

1. **每轮先扫描**已注册 Skill 的 `description`（低成本）。  
2. **有明确匹配**再读取对应 `SKILL.md` 全文（及链出的附属文件）。  
3. 多个匹配时选**最具体**的一个。  
4. **无匹配则不加载**；默认**一次只加载一个** Skill（除非用户要求组合）。  
5. 不要依赖模型「想起来再用」；也不要一次灌入多个长 Skill。  
6. `disable-model-invocation: true` 时，须用户点名或策略显式触发后再加载正文。

可在 Agent 的「工具说明 / 系统策略」中写死上述规则，与 Skill 包解耦。

---

## 7. 反模式清单

| # | 反模式 | 正确做法 |
|---|--------|----------|
| 1 | 几百行手册塞进 `SKILL.md` | 拆 `reference.md` / `examples.md` |
| 2 | 一个 Skill 包打 review + deploy + debug + oncall | 拆成多个窄 Skill |
| 3 | description 只写「我能做什么」 | Use when / Don't use when + 反例 |
| 4 | 没有反例 | 至少 2 条 Not for |
| 5 | 极低频 SOP 也注册为默认 Skill | 普通文档 + 显式加载 |
| 6 | 用 Skill 替代有状态工具 | 工具 / MCP + 短 Skill 说明何时调用 |
| 7 | 路径 `scripts\foo.py` | 正斜杠 `scripts/foo.py` |
| 8 | 写死「某月前用旧 API」 | 分「当前 / 已废弃」 |
| 9 | 术语混用 | 全文统一 |
| 10 | 命名 `helper`、`utils` | `deploy-production`、`review-security` |
| 11 | 有写操作无确认与限流 | 补 §5.2 |
| 12 | 把百科知识塞进 Skill 代替知识库 | 百科进 wiki/文档，Skill 只留流程 |

---

## 8. 创建 Skill 的工作流（作者 Agent）

任务含糊时**先与人类确认**，再落盘。

**Phase 1 — 发现**：目的与边界、触发话术、交付物形态、是否必须保留原文。  
**Phase 2 — 设计**：`name`、`description` 草稿、章节大纲、是否要 scripts。  
**Phase 3 — 实现**：建目录、写 `SKILL.md`、附属文件；默认 `disable-model-invocation: true`。  
**Phase 4 — 验收**：跑 §9 检查表；description 超 ~150 字尝试压缩且不失边界。

---

## 9. 交付前检查表

```markdown
### 核心
- [ ] name：小写连字符，≤64
- [ ] description：第三人称，WHAT + WHEN + DON'T + 反例
- [ ] description ≤1024 字符，尽量短
- [ ] SKILL.md < 500 行或已拆分
- [ ] 术语一致

### 结构
- [ ] 有可执行步骤或清单
- [ ] 复杂任务有分支或模板
- [ ] 附属引用仅一层
- [ ] 无易过期的时间条件

### 路由
- [ ] 与现有 Skill 描述不过度重叠
- [ ] Don't use when 能挡住常见误触发
- [ ] 非高频 Skill 未强行加入默认注册表

### 副作用（若适用）
- [ ] 执行前确认
- [ ] 限流与批量策略
- [ ] 验证 / 回滚

### 格式
- [ ] 符合 SKILL.md frontmatter 约定（§3.2）
- [ ] 脚本路径用正斜杠
```

---

## 10. 最小可行模板

````markdown
---
name: skill-name
description: >-
  [Capability]. Use when [triggers]. Don't use when [exclusions].
  Not for [counter-example 1]; not for [counter-example 2]. Output: [artifact].
disable-model-invocation: true
---

# [Title]

## Quick start
1. …
2. …

## Checklist
- [ ] …

## Output template
```markdown
…
```

## Examples
**Input:** …  
**Output:** …

## Do not use for
- …

## Additional resources
- [reference.md](reference.md)
````

---

## 附录 A：与 Cursor 格式的关系（可选阅读）

- **本文档**：面向任意智能体的**编写原则与路由语义**。  
- **Cursor**：当前业界较完整的 Skill **文件格式**参考实现之一；`name` / `description` / `disable-model-invocation` 等字段按 Cursor 约定书写，即可在 Cursor 中直接使用。  
- **其他运行时**：只需实现「注册表 + description 扫描 + 按需读 `SKILL.md`」；路径与自动发现策略自行定义。  
- 原则冲突时：**路由边界与安全以本文档为准**；**frontmatter 字段名与目录布局以 Cursor 兼容格式为准**，便于一份 Skill 多环境复用。

---

## 变更记录

| 日期 | 说明 |
|------|------|
| 2026-05-18 | 初稿 |
| 2026-05-18 | 服务对象改为任意智能体；Cursor 降为格式参考（附录） |
