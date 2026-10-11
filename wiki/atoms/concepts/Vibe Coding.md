---
title: "Vibe Coding"
created: 2026-10-11
updated: 2026-10-11
type: concept
domain: Agent-First 开发
description: 以自然语言驱动 AI 生成代码的编程方式。
tags: [域/Agent-First开发]
sources:
  - [[raw/columns/菜鸟教程AI智能体/31 Vibe Coding 入门教程.md]]
  - [[raw/columns/菜鸟教程AI智能体/15 第一个 AI Agent.md]]
status: active
---

# Vibe Coding

## 核心定义

Vibe Coding（氛围编程）是一种编程范式：不逐行手写代码，而是用自然语言描述想要什么，AI 写代码，人负责审查和把控方向。

- 由前特斯拉 AI 总监、OpenAI 联合创始人 [[Karpathy]] 于 2025 年 2 月首次提出
- 他的描述：「I just vibe. I don't even touch the keyboard sometimes. I just talk to the AI, it writes the code, I review it, and we iterate.」
- 角色转变：从「写代码的人」变为「描述需求的人」，即从程序员变成产品经理 + 架构师
- 不是让 AI 替代思考，而是让 AI 处理低价值重复劳动，人专注于理解问题、设计架构、验证结果

核心工作流四步：**描述需求 → 审查 Diff → 迭代修改 → 交付**。其中审查是最重要环节——必须看懂 AI 改了什么（逻辑正确性、安全性、数据流向、命名规范、冗余代码）。

## 与传统编程的对比

- **输入方式**：逐行手写代码 vs 自然语言描述需求
- **关注点**：语法、API、实现细节 vs 需求、架构、验证
- **调试方式**：手动断点/日志 vs 把错误信息丢给 AI 让它修复
- **速度**：取决于打字速度和熟练度 vs 取决于需求描述的清晰程度
- **核心技能**：编程语言掌握度 vs 需求拆解 + 结果验证能力
- **适用场景**：所有编程任务 vs 原型开发、CRUD、脚本工具、UI 页面

提示词用「四要素模型」：做什么（功能）、用什么（技术栈）、怎么约束（限制边界）、期望格式（输出偏好）。核心原则是越具体越好，模糊的需求只会得到模糊的代码。

## 为什么现在可行

1. **大模型编码能力飞跃**：GPT-5.5、Claude 5、Gemini 等模型代码生成准确率大幅提升，能理解项目上下文、遵循最佳实践、处理边界情况，并可处理超长上下文、一次性阅读整个项目
2. **AI 编程工具爆发**：Cursor、Claude Code、GitHub Copilot、Windsurf 等把 AI 深度集成进开发流程，不仅能补全代码，还能修改文件、运行终端命令、搜索代码库
3. **Agent 模式出现**：工具可自主执行多步骤任务——读文件、写代码、跑测试、根据结果修错，下达一个初始指令后自行循环迭代直到完成

常见误区：AI 可替代所有编程知识（门槛降低但未消除）、一次性描述全部功能（AI 注意力有上限）、不读 AI 写的代码直接合入（危险）。

## 主流工具

- **Agent / AI IDE**：Qoder（深度代码库理解、多 Agent、Repo Wiki）、Trae（对话驱动开发）、Cursor（项目级理解、多文件修改）
- **CLI Agent**：Claude Code（终端执行复杂任务）、OpenAI Codex（理解任务并执行完整开发流程）
- **编程助手**：GitHub Copilot（补全、聊天、Agent）、Windsurf（Cascade 工作流、自动多文件修改）
- **在线平台**：Bolt.new（一句话生成完整应用）、v0 by Vercel（React 页面生成）、Replit AI（云开发协作）、Lovable（从描述生成 SaaS）、Firebase Studio（AI + 后端集成）

新手建议从 Qoder 或 Trae 开始：操作类似 VS Code，学习曲线平缓，不改变熟悉的编辑器环境。

## 0 代码实践入口

零代码路径可从 AI Agent 平台切入，以 MonkeyCode 为例：

- 覆盖需求 → 设计 → 开发 → Review 全流程，免费、无需安装、内置云端开发环境
- 注册登录后进入控制台直接输入需求，例如「写一个 JavaScript 猜数字小游戏：随机 1 到 100，猜大提示太大、猜小提示太小」
- 点击执行并选择模型（国内很多模型免费支持，如 qwen3.8-flash），任务完成后查看生成的效果地址
- 可切换不同模型对比生成效果，或用「重新优化整个界面」这类自然语言指令继续迭代

与 [[Harness-Engineering]] 的关联：Vibe Coding 描述人与 AI 的协作方式，而如何组织模型、工具、数据形成可靠工作流属于编排层的工程问题。

## 参考

- [[Karpathy]]
- [[Agent-First-Development]]
- [[Harness-Engineering]]

## 来源

- [[raw/columns/菜鸟教程AI智能体/31 Vibe Coding 入门教程.md]]
- [[raw/columns/菜鸟教程AI智能体/15 第一个 AI Agent.md]]
