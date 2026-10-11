---
title: "Loop Engineering"
created: 2026-10-11
updated: 2026-10-11
type: concept
domain: Agent 架构与工程
description: 以核心循环与六大要素组织智能体运行的工程方法。
tags: [域/Agent架构与工程]
sources:
  - [[raw/columns/菜鸟教程AI智能体/30 Loop Engineering.md]]
status: active
---

# Loop Engineering

## 核心定义

Loop Engineering（循环工程）是设计、运营和持续改进反馈循环的工程实践，这些循环使 AI 编程 Agent 能够自主完成规划、执行代码修改、观察结果并在多轮迭代中完成任务。

一句话概括：把你从「提示 Agent 的人」变成「设计提示 Agent 的系统」的工程师。

- 一个 Loop 是递归目标系统：你定义一个目的，Agent 不断迭代，直到工作真正完成
- 优化对象从单条指令变为整套自动决定「提示什么、何时提示、结果是否可接受」的系统
- 衡量标准从第一个回复的质量变为最终输出的结果质量
- 与 [[Harness-Engineering]] 构成演进序列：Prompt（怎么问）→ Context（给什么信息）→ Harness（如何组织能力）→ Loop（如何持续创造结果）

## 起源与背景

2026 年 6 月，两句话引爆了这个概念：

- Anthropic Claude Code 负责人 Boris Cherny：「我不再直接提示 Claude 了……我的工作是编写 Loop。」
- 开发者 Peter Steinberger：「你不应该再手动提示 AI 编程助手了。你应该设计让 Agent 自己提示自己的 Loop。」
- 随后 Google 工程师 Addy Osmani 在 Substack 发表长文，将这一实践正式命名并系统化为 Loop Engineering

背景是 AI 编程工具的三代演进：第一代自动补全（Copilot 早期，人类主导决策）→ 第二代对话式（ChatGPT、Claude.ai，人类手动推进每一步）→ 第三代 Agent 自主循环（Claude Code、OpenAI Codex Agent，自主规划、执行、验证）。

第三代出现后，工程师的核心竞争力从会写提示词变成会设计 Loop。

## 核心循环

Agent 执行任务时内置「内循环」：感知（Perceive）→ 推理（Reason）→ 行动（Act）→ 观察（Observe）。Loop Engineering 工作在内循环的上一层——外循环由你设计：按计划发现任务 → 分派 Agent → 验证结果 → 记录状态 → 开启下一轮。

Agent Loop 的基础结构由五个阶段首尾相连：

1. **意图（Intent）**：定义目标结果，成功是什么样子、约束是什么
2. **上下文（Context）**：收集相关代码、文档、报错日志、约定规范
3. **行动（Action）**：编辑文件、运行命令、调用工具、草拟方案
4. **观察（Observation）**：获取测试结果、编译错误、运行时输出、代码 Diff
5. **调整（Adjustment）**：根据观察更新计划，重复循环直到完成或被阻塞

Loop 的力量不在于单独步骤，而在于**闭环**：测试失败是新的上下文，类型错误是错误假设的信号，Review 评论是驱动下一步行动的新观察。

## 六大构成要素

1. **自动触发器（Automations）**：Loop 的心跳，定义「什么时候、做什么」。没有自动触发，Loop 只是「你做了一次的操作」。可用 `/loop` 定时触发、`/goal` 运行到可验证条件成立；需注意 Token 成本，建议从慢节奏起步
2. **并行隔离（Worktrees）**：用 Git Worktree 为每个 Agent 提供独立工作目录，共享同一 Git 历史但文件改动隔离，消除机械性文件冲突。真正的上限是人的审查速度，而非工具能开多少 Worktree
3. **技能文件（Skills）**：包含 `SKILL.md` 的文件夹，写明项目约定、构建步骤与历史教训，Agent 会话开始时加载，避免每次从零推断项目规范
4. **连接器（Connectors / MCP）**：基于 MCP（模型上下文协议）让 Agent 读 Issue 追踪、查数据库、调用 API、发 Slack 消息，是「给出修复方案」与「自动开 PR、关联 Ticket、通知频道」之间的核心差异。须配置最小权限，高风险操作人工审批
5. **子 Agent（Sub-Agents）**：把写代码的 Agent 和检查代码的 Agent 分开，采用「制作者-检查者」（Maker-Checker）模式——写了代码的模型评分会过于宽容，独立检查器（甚至用更强模型）能抓住被自圆其说忽略的问题
6. **持久记忆（Memory）**：模型在对话之间完全遗忘，跨对话的 Loop 必须把状态写进仓库里的文件。仓库记得，即使模型不记得

## 与 Prompt Engineering 的区别

- **优化对象**：单条手写指令 vs 自动决定提示时机与验收的整套系统
- **工作单位**：一次手动输入的对话轮次 vs 跨越多轮次自动运行的完整工作流
- **失败模式**：模型给出差劲回答 vs Loop 设计不良——循环太早停止、忽视错误信号、无法验证完成
- **层次关系**：Loop 由多个 Prompt 组成，写得差的 Prompt 放进 Loop 只会让糟糕工作更快产出；Loop Engineering 是 Prompt Engineering 之上的层次，而非替代

常见风险：验证仍是人的责任、理解债（Comprehension Debt）积累更快、认知投降（Cognitive Surrender）——接受 Loop 返回的任何结果是最舒适也最隐性的危险。

## 参考

- [[Agent-Loop]]
- [[Harness-Engineering]]
- [[AI Agent]]

## 来源

- [[raw/columns/菜鸟教程AI智能体/30 Loop Engineering.md]]
