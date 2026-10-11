---
title: "Agent开发与工程"
type: topic
domain: Agent 架构与工程
description: Agent 工程全景：基础概念 → 循环/上下文/记忆 → 多智能体 → 驾驭与循环工程 → 评测与部署
tags: [域/Agent架构与工程]
category: topics
status: stable
version: 1.0
created: 2026-10-11
updated: 2026-10-11
next_review: 2027-01-11
confidence: low
sources:
  - [[raw/columns/菜鸟教程AI智能体/00 AI Agent(智能体) 教程.md]]
  - [[raw/columns/菜鸟教程AI智能体/02 AI Agent 核心组件.md]]
  - [[raw/columns/菜鸟教程AI智能体/14 Agent 架构.md]]
  - [[raw/columns/菜鸟教程AI智能体/28 Harness Engineering.md]]
related_atoms:
  - [[AI Agent]]
  - [[Agent-Loop]]
  - [[Context-Engineering]]
  - [[Memory-System]]
  - [[ACI-Agent-Computer-Interface]]
  - [[MCP]]
  - [[Multi-Agent-Organization]]
  - [[Harness-Engineering]]
  - [[Loop Engineering]]
  - [[Agent-Evaluation]]
  - [[Vibe Coding]]
  - [[多模态Agent]]
---

# Agent开发与工程

> Agent 工程的完整分层：先回答"Agent 是什么"（[[AI Agent]]），再逐层解决运行机制、协作扩展、工程方法与质量保障。

## 背景

[[大模型应用技术栈]] 的使用层向上延伸即 Agent。与被动应答的 LLM 不同，Agent 以"感知-模型-工具-记忆"的循环自主推进任务——工程挑战也从"提示词写得好不好"变为"循环、上下文与工具体系设计得好不好"。

## 分层全景

| 层 | 组件 | 关键页面 |
|----|------|----------|
| 概念层 | Agent 与传统模型的区别、四组件与五层架构 | [[AI Agent]]、[[Workflow-vs-Agent]] |
| 运行层 | 核心循环、ReAct、规划 | [[Agent-Loop]]、[[Loop Engineering]] |
| 资源层 | 上下文、记忆、工具接口 | [[Context-Engineering]]、[[Memory-System]]、[[ACI-Agent-Computer-Interface]]、[[Skills-System]] |
| 协作层 | 多智能体角色分工与组织 | [[Multi-Agent-Organization]] |
| 协议层 | 工具生态标准 | [[MCP]] |
| 质量层 | 验收基础设施、评测与安全 | [[Harness-Engineering]]、[[Agent-Evaluation]] |
| 开发范式 | Agent 优先的编程方式 | [[Vibe Coding]]、[[Agent-First-Development]] |

## 三条工程主线

- **循环可靠性**：Loop Engineering 把"意图→行动→观察→调整"的内外循环要素化（自动触发、并行隔离、子 Agent、持久记忆），与 [[Harness-Engineering]] 的验收侧互为表里
- **资源管理**：上下文是稀缺资源——[[Context-Engineering]] 管"放什么进去"，[[Memory-System]] 管"跨轮次留什么"，[[ACI-Agent-Computer-Interface]] 管"怎么调用外部能力"
- **规模扩展**：单 Agent 循环到 [[Multi-Agent-Organization]] 的分工协作，复杂度从"写好提示"转向"组织好系统"

## 与相邻知识的联系

- [[大模型应用技术栈]]：Agent 之下的基座与增强层
- [[多模态Agent]]：感知环节的模态扩展
- [[AAR-Model]] / [[Pacing-Model]] / [[Long-Task-Management]]：Agent 行为分析的既有视角

## 来源

- [[raw/columns/菜鸟教程AI智能体/00 AI Agent(智能体) 教程.md]]
- [[raw/columns/菜鸟教程AI智能体/02 AI Agent 核心组件.md]]
- [[raw/columns/菜鸟教程AI智能体/14 Agent 架构.md]]
- [[raw/columns/菜鸟教程AI智能体/28 Harness Engineering.md]]

## 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-10-11 | 1.0 | 初版（菜鸟教程AI智能体 系列 50 篇沉淀：5 概念页 + 13 页归纳 + 分层综述） |
