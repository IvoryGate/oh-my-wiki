---
id: skills-system
title: Skills System
aliases:
  - Skills系统
  - Agent Skills
  - 按需加载技能
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
tags:
  - Agent工程
---

## 定义

Skills 是上下文工程里非常有效的一种模式，核心思路：**系统提示只保留索引，完整知识按需加载**。

## 实现示例

```typescript
const systemPrompt = `
可用 Skills：
- deploy: 部署到生产环境的完整流程
- code-review: 代码审查检查清单
- git-workflow: 分支策略和 PR 规范
`;

async function executeLoadSkill(name: string): Promise<string> {
  return fs.readFile(`./skills/${name}.md`, "utf-8");
}
```

## Skill 描述符设计原则

1. **足够短**：避免常驻上下文持续涨 token
2. **路由条件而非功能介绍**："何时该用我" 比 "我能做什么" 重要
3. **包含反例**：没有反例时准确率从 73% 掉到 53%，加上反例后升到 85%

### 好的描述符写法

```typescript
// 低效（约 45 tokens）
description: |
  This skill handles the complete deployment process to production.
  It covers environment checks, rollback procedures, and post-deploy
  verification. Use this before deploying any code to production.

// 高效（约 9 tokens）
description: Use when deploying to production or rolling back.
```

## 调用规则

- 每次回复前先扫描 available_skills
- 有明确匹配时再读取对应 SKILL.md
- 多个匹配时优先选最具体的那个
- 没有匹配就不读取，一次只加载一个

## 数量控制

- 常驻系统提示只放高频 Skill
- 低频的需要时再手动引入
- 极低频的直接用文档替代

## 常见反模式

1. 正文几百行工作手册全塞进 Skill 正文
2. 一个 Skill 试图覆盖多件事
3. 有副作用的 Skill 没有显式限制调用时机

## 相关概念

- [[Context-Engineering]]
- [[Agent-Loop]]

## 来源

- [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]] §3
