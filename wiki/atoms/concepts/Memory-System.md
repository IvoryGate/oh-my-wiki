---
id: memory-system
title: Memory System
aliases:
  - 记忆系统
  - Agent记忆
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - AI
  - Agent
  - 记忆
  - 工程实践
---

## 定义

Agent 不具备原生的时间连续性，会话结束后上下文随之清空。Memory System 是让系统具备 **跨会话一致性** 的基础设施。

## 四种记忆类型

| 类型 | 存储位置 | 作用 | 特点 |
|------|----------|------|------|
| **工作记忆** | 上下文窗口 | 当前任务所需最小信息 | token 有限，需主动管理 |
| **程序性记忆** | Skills 文件 | 怎么做某件事，操作流程 | 按需加载不默认常驻 |
| **情景记忆** | JSONL 会话历史 | 发生了什么 | 磁盘持久化，支持检索 |
| **语义记忆** | MEMORY.md | Agent 主动写入的重要事实 | 每次启动时注入系统提示 |

## ChatGPT 四层记忆

1. **Session Metadata**：设备、地点、使用模式，不持久化
2. **User Memory**：约 33 条关键偏好事实，持久化，每次注入
3. **Conversation Summary**：约 15 个最近对话的轻量摘要，持久化
4. **Current Session**：当前对话滑动窗口，不持久化

## 记忆整合触发

```
tokenUsage / maxTokens >= 0.5  → 触发整合
```

### 整合流程

1. 对待整合消息做 llmSummarize
2. 摘要追加到 MEMORY.md
3. 更新 lastConsolidatedIndex

### 失败回退

- 把原始消息写入 archive/
- 保留完整历史，避免整合失败时丢失上下文
- **系统只移动指针，不删除原始消息**

## 设计原则

> 记忆库规模不大时，结构化 Markdown 加关键词搜索已经足够，只有当规模超过几千条、确实需要语义相似度检索时，再考虑引入向量检索。

## 相关概念

- [[Context-Engineering]]
- [[Skills-System]]
- [[Agent-Loop]]

## 来源

- [[你不知道的 Agent：原理、架构与工程实践]] §5
