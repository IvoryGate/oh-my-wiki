---
id: agent-tracing
title: Agent Tracing
aliases:
  - Agent追踪
  - 可观测性
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - AI
  - Agent
  - 可观测性
  - 调试
---

## 定义

Agent Tracing 是记录和追踪 Agent 执行过程的系统能力，是排查 Agent 问题的基础设施。

## 为什么需要 Trace

> 没有 Trace 能力，失败案例就没法稳定复现。传统只监控延迟和错误率的 APM 往往帮助有限，接口层看起来可能一切正常，但真正的问题出在模型某一轮做出了错误决策。

## Trace 里需要记录什么

```
每次 Agent 运行：
├── 完整 Prompt，含系统提示
├── 多轮交互的完整 messages[]
├── 每次工具调用 + 参数 + 返回值
├── 推理链（如有 thinking 模式）
├── 最终输出
└── token 消耗 + 延迟
```

## 两层可观测性

| 层级 | 方式 | 作用 |
|------|------|------|
| **第一层** | 人工抽样标注 | 摸清失败模式，给第二层提供校准数据 |
| **第二层** | LLM 自动评估 | 全量覆盖，以第一层为校准依据 |

⚠️ 只跑第二层评分标准容易漂移，只靠第一层规模上覆盖不了

## 在线评测采样策略

对 10%-20% 的 Trace 运行在线评测：

- **负反馈触发**：用户明确不满意 → 100% 进队列
- **高成本对话**：token 消耗超阈值 → 优先审查
- **时间窗口采样**：每天固定时间段随机采
- **模型或 Prompt 变更后**：头 48 小时全量审查

## 事件流架构

```typescript
// Agent 执行时 emit 事件
on tool_start: emit { type, tool_name, input, timestamp }
on tool_end:   emit { type, tool_name, result, duration }
on turn_end:   emit { type, turn_output }

// 多路下游订阅，Agent 核心代码不变
agent.on("event") -> write_to_logs
agent.on("event") -> update_ui
agent.on("event") -> send_to_eval_framework
```

> 事件一次发布，多路消费，主循环不需要为了任何下游改代码。

## 相关概念

- [[Agent-Evaluation]]
- [[Harness-Engineering]]

## 来源

- [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]] §9
