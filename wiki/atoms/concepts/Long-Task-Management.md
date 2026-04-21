---
id: long-task-management
title: Long Task Management
aliases:
  - 长任务管理
  - 跨Session任务
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - AI
  - Agent
  - 任务管理
  - 工程实践
---

## 定义

Long Task Management 是让 Agent 在更长时间跨度内稳定推进任务的工程实践。

## 问题

长任务最常见的失败：
1. session 结束时任务还没做完
2. 上下文先耗尽
3. 下一轮无法准确恢复现场

## 解决方案：双 Agent 模式

### Initializer Agent

只在第一轮运行一次，负责：
- 生成 feature-list.json
- 生成 init.sh
- 初始 git commit
- 创建 claude-progress.txt

### Coding Agent

循环执行多个 session：
- 从文件系统恢复现场
- 定位当前任务
- 实现一个功能
- 跑测试，更新 passes 字段
- 提交代码后退出

> 即使中途崩溃，也能直接从文件系统里的状态继续，而不是从头再来。

## 进度管理原则

> **进度要放在文件里，不要放在上下文里**

```json
{
  "tasks": [
    {"id": "1", "desc": "读取现有配置", "status": "completed"},
    {"id": "2", "desc": "修改数据库 schema", "status": "in_progress"},
    {"id": "3", "desc": "更新 API 接口", "status": "pending"}
  ]
}
```

约束：同一时间只能有一个 `in_progress`

## 后台 I/O 处理

把慢速 subprocess 放到后台线程，通过通知队列在下一轮 LLM 调用前注入结果。

## 任务状态约束

- 状态显式记录为外部控制对象
- 连续多轮未更新任务状态时，自动注入 `<reminder>` 提示

## 相关概念

- [[Agent-Loop]]
- [[Memory-System]]

## 来源

- [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]] §6
