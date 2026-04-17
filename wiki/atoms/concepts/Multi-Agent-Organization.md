---
id: multi-agent-organization
title: Multi-Agent Organization
aliases:
  - 多Agent组织
  - Agent协作模式
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[你不知道的 Agent：原理、架构与工程实践]]"
tags:
  - AI
  - Agent
  - 架构
  - 协作
---

## 定义

Multi-Agent Organization 是多个 Agent 协作完成任务的组织模式。

## 两种工作模式

| 模式 | 特点 | 缺点 |
|------|------|------|
| **指挥者模式** | 同步协作，人与单个 Agent 紧密互动 | session 结束 context 就没了，产出短暂 |
| **统筹者模式** | 异步委派，人在起点和终点出现 | 需要可持久化工件 |

> 多 Agent 的主要价值：把人的持续参与，变成对工件的最终审核。

## 常见组织方式

主 Agent 作为 Orchestrator 统筹全局，下挂多个子 Agent 独立并行工作：

- **JSONL inbox 协议**：通信
- **Worktree**：隔离文件修改
- **任务图**：管理依赖关系

## 子 Agent 的作用

> 子任务里的搜索、试错和调试过程，不该污染主 Agent 的上下文。主 Agent 真正需要的只是结论。

```typescript
// 子 Agent 有独立的 messages[]，跑完只回传摘要
const result = await runAgentLoop(task, { messages: [] });
return summarize(result); // 主 Agent 上下文里只有这一行
```

## 协作协议

```typescript
// 消息结构：结构化，有状态，append-only，崩溃可恢复
{
  request_id, from_agent, to_agent,
  content,
  status: 'pending' | 'approved' | 'rejected',
  timestamp
}
```

## 子 Agent 限制

1. **深度限制**：防止无限递归生成孙 Agent
2. **最小系统提示**：只给 Tooling、Workspace、Runtime 三节，不带 Skills 和 Memory

## 幻觉放大风险

多个 Agent 频繁互动时，错误会被一层层放大。需要 **交叉验证** 打断链条。

## 实施顺序

1. 可持久化任务图
2. 有身份的队友
3. 结构化通信协议
4. 交叉验证或外部反馈

## 相关概念

- [[Agent-Loop]]
- [[Agent-Control-Patterns]]

## 来源

- [[你不知道的 Agent：原理、架构与工程实践]] §7
