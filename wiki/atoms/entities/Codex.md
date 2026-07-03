---
id: codex
title: Codex
aliases:
  - OpenAI Codex
  - Codex CLI
type: entity
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/工程技术：在智能体优先的世界中利用 Codex.md]]
tags:
  - Agent工程
---

## 定义

Codex 是 OpenAI 开发的代码生成智能体，能够端到端驱动软件开发流程。

## 核心能力

### 端到端自主

给定一个提示，Codex 可以：

1. 验证代码库的当前状态
2. 重现已报告的漏洞
3. 录制演示故障的视频
4. 实施修复措施
5. 通过运行应用程序来验证修复
6. 录制第二个视频，演示解决方案
7. 打开 Pull Request
8. 回应智能体和人类反馈
9. 检测并修复构建故障
10. 仅在需要判断时才交由人工处理
11. 合并更改

### 可观测性集成

- 使用 LogQL 查询日志
- 使用 PromQL 查询指标
- 完整可观测性栈按任务临时创建，任务完成即销毁

### 工作方式

- 经常单次运行在单个任务上持续工作超过六个小时（通常在人类睡眠时间）
- 直接使用标准开发工具（gh、本地脚本、嵌入代码仓库的技能）
- 智能 Agent 对智能 Agent 审核 PR

## 实践数据

> 3 个工程师 5 个月写了百万行代码，将近 1500 个 PR

## 相关实体

- [[OpenAI]]

## 相关概念

- [[Agent-First-Development]]
- [[Harness-Engineering]]

## 来源

- [[raw/articles/工程技术：在智能体优先的世界中利用 Codex.md]]
