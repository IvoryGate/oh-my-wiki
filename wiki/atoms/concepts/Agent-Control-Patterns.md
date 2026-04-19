---
id: agent-control-patterns
title: Agent 控制模式
aliases:
  - Agent Control Patterns
  - AI系统控制模式
  - 五种控制模式
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - AI
  - Agent
  - 架构模式
  - 设计模式
---

## 定义

大多数 AI 系统拆开看，都是以下五种控制模式的组合：

## 五种模式

### 1. 提示链 (Prompt Chaining)

- **结构**：任务拆成顺序步骤，每步 LLM 处理上一步的输出
- **特点**：中间可加代码检查点
- **适用**：生成后翻译、先写大纲再写正文这类线性流程

### 2. 路由 (Routing)

- **结构**：对输入分类，定向到对应的专用处理流程
- **特点**：简单问题走轻量模型，复杂问题走强模型
- **适用**：技术咨询和账单查询走不同逻辑

### 3. 并行 (Parallelization)

两种变体：
- **分段法**：把任务拆成独立子任务并发跑
- **投票法**：同一任务跑多次取共识
- **适用**：高风险决策或需要多视角的场景

### 4. 编排器-工作者 (Orchestrator-Workers)

- **结构**：中央 LLM 动态分解任务，委派给工作者 LLM，综合结果
- **案例**：nanobot 的 spawn 工具、learn-claude-code 的子 Agent 模式

### 5. 评估器-优化器 (Evaluator-Optimizer)

- **结构**：生成器产出，评估器给反馈，循环直到达标
- **适用**：翻译、创意写作这类质量标准难以用代码精确定义的任务

## 选择原则

关键看任务本身适合哪一种设计，很多场景并不需要完整的 Agent 自主权，把其中几种模式搭起来就够了。

## 相关概念

- [[Agent-Loop]]
- [[Workflow-vs-Agent]]

## 来源

- [[你不知道的 Agent：原理、架构与工程实践]] §1
