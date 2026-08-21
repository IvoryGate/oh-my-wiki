---
id: agent-evaluation
title: Agent Evaluation
aliases:
  - Agent评测
  - AI系统评测
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - Agent工程
---

## 定义

Agent Evaluation 是判断 Agent 行为是否正确的评测体系。评测的核心是：**测试用例、评分标准和自动验证**。

## Agent 评测结构复杂度

### 传统 Single-turn 评测
Prompt → Response → 判断对错

### Agent 评测
准备工具、运行环境、任务 → Agent 多次调用工具、修改环境状态 → 评分（看最终环境结果）

## 核心概念

| 概念 | 说明 |
|------|------|
| **task** | 任务 |
| **trial** | 单次运行 |
| **grader** | 评分器 |
| **transcript** | 完整执行记录 |
| **outcome** | 环境最终结果 |
| **agent harness** | 被评测的 Agent 运行框架 |
| **evaluation harness** | 评测基础设施 |
| **evaluation suite** | 一批任务的集合 |

## 两个核心指标

| 指标 | 用途 | 问题 |
|------|------|------|
| **Pass@k** | 开发阶段 | "这个 Agent 理论上能不能做到？" |
| **Pass^k** | 上线前 | "已有功能有没有被改坏？" |

⚠️ 混用容易误判

## 三类评分器

| 类型 | 确定性 | 适用场景 |
|------|--------|----------|
| **代码评分器** | 最高 | 有明确答案的任务（字符串匹配、单测、结构比对） |
| **模型评分器** | 中等 | 需要判断语义质量 |
| **人工评分器** | 可靠但慢 | 建立基准、校准自动评分器 |

## 核心原则

1. **有明确正确答案就优先用代码评分器**
2. **"看 Agent 怎么说" 和 "看系统最后变成什么样" 是两件事**
3. **先修评测，再改 Agent** — 评测出问题会导致失真信号

## 如何启动评测体系

- 20-50 个真实失败案例就够启动
- 来源优先选已经在手动检查的内容
- 环境隔离：每次运行从干净状态开始
- 测试用例同时覆盖正例和反例

## 相关概念

- [[Harness-Engineering]]
- [[Agent-Tracing]]

## 来源

- [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]] §8
