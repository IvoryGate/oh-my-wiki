---
id: architecture-constraints
title: Architecture Constraints
aliases:
  - 架构约束
  - 架构不变量
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[工程技术：在智能体优先的世界中利用 Codex]]"
tags:
  - AI
  - Agent
  - 架构
  - 软件工程
---

## 定义

Architecture Constraints 是通过强制执行不变量，而非对实施过程进行微观管理，令智能体能够快速交付且不会削弱基础的架构原则。

## 核心原则

> 通过强制执行不变量，而非对实施过程进行微观管理。

## 示例：分层架构

每个业务域划分为固定的层，依赖方向经过严格验证：

```
Types → Config → Repo → Service → Runtime → UI
```

横切关注点（认证、连接器、遥测、功能标志）通过单一的显式接口进入：**Providers**。

## 强制执行方式

- 自定义的 linter（由 Codex 生成）
- 结构测试机械地强制执行
- 错误信息在智能体情境中注入修复指令

## "品味不变式"

- 结构化日志记录
- 模式和类型的命名约定
- 文件大小限制
- 特定平台的可靠性要求

## 为什么对 Agent 重要

> 对于编码智能体来说，严格边界和可预测结构是早期先决条件：有了约束，速度才不会下降，架构才不会漂移。

## 中央 vs 本地

- **中央层面**：强制执行边界
- **本地层面**：允许自主权

> 你非常重视界限、正确性和可重复性。在这些边界内，你允许团队或智能体在解决方案的表达方式上拥有很大的自由。

## 相关概念

- [[Agent-First-Development]]
- [[Harness-Engineering]]

## 来源

- [[工程技术：在智能体优先的世界中利用 Codex]]
