---
id: workflow-vs-agent
title: Workflow vs Agent
aliases:
  - 工作流与智能体
  - Workflow与Agent区别
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - Agent工程
---

## 定义

Anthropic 对这两类系统的区分标准：

| 类型 | 控制权 | 执行路径 |
|------|--------|----------|
| **Workflow** | 代码 | 预先写死 |
| **Agent** | LLM | 动态决定 |

核心区别：**控制权掌握在谁手里**。

## 误区

很多标着 "Agent" 的产品，深入看其实更接近 Workflow。

## 选择原则

两者本身并无高下之分，真正重要的是 **给任务找到更适合的解决方案**：

- 需要确定性执行 → Workflow
- 需要灵活决策 → Agent
- 混合场景 → 组合使用

## 相关概念

- [[Agent-Loop]]
- [[Agent-Control-Patterns]]

## 来源

- [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]] §1
