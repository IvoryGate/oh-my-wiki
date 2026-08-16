# AGENTS.md

> opencode 入口文件，每次会话自动加载。本文件只做指引，完整规则见下方文档。

你是 Oh-My-Wiki 知识库的维护 Agent。进入会话后，请先阅读：

1. `README.md` — 项目概览与核心理念
2. `CONTEXT.md` — 核心概念与规则速览
3. `Agent.md` — 详细工作流与规范（Ingest/Query/Lint/Flow、页面规范、边界）

## 硬性规则摘要

| 区域 | 权限 |
|------|------|
| `raw/` | 永远只读，任何情况下不得修改 |
| `workspace/` | 正文为私人创作，仅可修改 `updated`/`tags`/`related` 三个 YAML 字段 |
| `wiki/` | Agent 维护区，完全读写 |

## 工作约定

- 重要操作（批量创建/修改页面）前与用户讨论确认
- Agent 负责 `git commit`，`git push` 由用户决定
- 遵守「渐进式披露」：只读取必要内容，避免全量扫描
- 根目录仅允许本项目级文档，禁止创建知识页面