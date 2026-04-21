---
id: agent-loop
title: Agent Loop
aliases:
  - Agent循环
  - AI Agent主循环
  - 感知-决策-行动-反馈循环
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - AI
  - Agent
  - 架构
  - 核心模式
---

## 定义

Agent Loop 是 AI Agent 的核心执行模式，通过 **感知 → 决策 → 行动 → 反馈** 四个阶段不断循环，直到任务完成。

## 核心实现

```typescript
const messages: MessageParam[] = [{ role: "user", content: userInput }];

while (true) {
  const response = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 8096,
    tools: toolDefinitions,
    messages,
  });

  if (response.stop_reason === "tool_use") {
    const toolResults = await Promise.all(
      response.content
        .filter((b) => b.type === "tool_use")
        .map(async (b) => ({
          type: "tool_result" as const,
          tool_use_id: b.id,
          content: await executeTool(b.name, b.input),
        }))
    );
    messages.push({ role: "assistant", content: response.content });
    messages.push({ role: "user", content: toolResults });
  } else {
    return response.content.find((b) => b.type === "text")?.text ?? "";
  }
}
```

## 关键特性

1. **稳定性**：循环本身相当稳定，从最小实现扩展到支持子 Agent、上下文压缩和 Skills 加载，主循环基本不变
2. **外部扩展**：新增能力通过三种方式接入：
   - 扩展工具集和 handler
   - 调整系统提示结构
   - 把状态外化到文件或数据库

## 设计原则

- 模型负责推理，外部系统负责状态和边界
- 循环体不应变成巨大的状态机
- 新能力叠加在循环外部，而非改动循环内部

## 相关概念

- [[ACI]] - Agent-Computer Interface，支持 Agent Loop 的行动阶段
- [[Multi-Agent-Organization]] - 多 Agent 组织与协作模式

- [[Workflow-vs-Agent]]
- [[Agent-Control-Patterns]]
- [[Harness-Engineering]]

## 来源

- [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]] §1
