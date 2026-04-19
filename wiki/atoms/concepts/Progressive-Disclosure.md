---
id: progressive-disclosure
title: Progressive Disclosure
aliases:
  - 渐进式披露
  - 渐进揭示
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - [[raw/articles/工程技术：在智能体优先的世界中利用 Codex.md]]
tags:
  - AI
  - Agent
  - 上下文
  - 信息架构
---

## 定义

Progressive Disclosure 是一种信息架构原则：智能体从一个小而稳定的切入点开始，并被指导下一步该去哪里查看，而不是一开始就被淹没。

## AGENTS.md 设计

> AGENTS.md 是地图，不是百科全书。

### 失败的"大型 AGENTS.md"方法

- **情境是稀缺资源**：巨大的指令文件会挤掉任务、代码和相关文档
- **过多的指导反而变得无效**：当一切都"重要"时，一切都不重要
- **它会立即腐烂**：一本庞杂的手册会变成陈旧规则的坟场
- **这很难核实**：单个 blob 不适合机械检查

### 正确做法

- 保持约 100 行作为索引
- 知识库位于结构化的 `docs/` 目录
- 使用 linter 和 CI 作业验证知识库的更新状况

## 知识存储布局

```
AGENTS.md          # 索引，约100行
ARCHITECTURE.md
docs/
├── design-docs/
├── exec-plans/    # 执行计划作为一等公民
├── generated/
├── product-specs/
├── references/
└── ...
```

## 计划作为一等公民

- 临时轻量计划用于小幅变更
- 复杂工作记录在执行计划中，附带进度和决策日志
- 活跃计划、已完成计划和已知技术债务都已版本控制并集中存放

## 相关概念

- [[Context-Engineering]]
- [[Skills-System]]

## 来源

- [[工程技术：在智能体优先的世界中利用 Codex]]
