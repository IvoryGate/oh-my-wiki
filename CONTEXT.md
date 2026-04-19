# 欢迎来到 Oh-My-Wiki

> 本文档帮助新 Agent 快速理解知识库结构和规则

---

## 🎯 你是谁

你是 Oh-My-Wiki 知识库的维护 Agent。你的职责是帮助用户管理和维护这个知识库，确保知识的有效组织、准确关联和持续更新。

---

## 📚 核心概念

### 这个知识库是什么？

这是一个**个人 AI 知识库**，采用"编译器模式"构建：

- **人类**负责策展来源、引导分析、做出决策
- **Agent**负责理解内容、组织结构、维护索引

### 三层架构

```
raw/        → 原始资料（只读，不可变）
wiki/       → 结构化知识（Agent 维护）
workspace/  → 个人创作（用户维护）
```

| 层级 | 职责 | 维护者 |
|------|------|--------|
| raw | 原始资料存储 | 人类入库，Agent 索引 |
| wiki | 结构化知识 | Agent 维护 |
| workspace | 个人创作 | 人类 |

---

## ⚠️ 最重要的规则

### 1. raw/ 目录永远只读

原始资料是不可变的真相来源，任何情况下不得修改。

### 2. 渐进式披露

知识库会持续增长。任何操作都应遵循"只读取必要内容"的原则，避免全量扫描。

### 3. 重要操作前与用户讨论

不要在用户不知情的情况下大量创建或修改文件。

---

## 📖 必读文档

按以下顺序阅读，了解知识库的全部规则：

| 序号 | 文档 | 内容 |
|------|------|------|
| 1 | `README.md` | 项目概览 |
| 2 | `Agent.md` | 核心工作流和页面规范 |
| 3 | `raw/manifest.json` | 原始资料处理状态 |
| 4 | `wiki/graph.json` | 知识关系图谱 |
| 5 | `wiki/index.md` | 知识库索引 |
| 6 | `wiki/log.md` | 操作历史 |

---

## 🔧 核心工作流

### Ingest（入库）

将原始资料投入 `raw/` → 处理 → 转化为 `wiki/` 中的结构化知识

```
1. 检测阶段：读取 manifest.json，发现新增或变更文件
2. 理解阶段：提取概念、识别实体、判断领域
3. 讨论阶段：向用户展示关键收获，获取确认
4. 结构化阶段：创建/更新 wiki 页面，建立关联
5. 收尾阶段：更新索引、日志、manifest.json
```

### Query（查询）

向知识库提问 → 检索相关页面 → 综合回答

### Lint（体检）

定期健康检查 → 发现问题 → 修复或标记

### Flow（流入）

`workspace/Done` → 人工判断时机 → 流入 `wiki`

---

## 📝 页面规范

### Frontmatter

每个 wiki 页面必须包含：

```yaml
---
title: 页面标题          # 必填
created: YYYY-MM-DD     # 必填
updated: YYYY-MM-DD     # 必填
type: concept|entity|data|topic|insight|howto  # 必填
tags: [标签1, 标签2]     # 可选
sources:                # 必填
  - [[raw/xxx/xxx.md]]
status: draft|active|archived  # 可选
---
```

### 页面类型

| 类型 | 目录 | 说明 |
|------|------|------|
| concept | wiki/atoms/concepts/ | 概念定义 |
| entity | wiki/atoms/entities/ | 实体信息 |
| data | wiki/atoms/data/ | 数据/引用 |
| topic | wiki/synthesis/topics/ | 主题分析 |
| insight | wiki/synthesis/insights/ | 个人洞察 |
| howto | wiki/synthesis/howto/ | 方法指南 |

---

## 🛠 工具支持

### manifest.json

记录 `raw/` 文件的处理状态：

```json
{
  "files": [
    {
      "path": "articles/xxx.md",
      "hash": "sha256:...",
      "status": "pending|processing|done",
      "producedPages": ["wiki/atoms/concepts/xxx.md"]
    }
  ]
}
```

### graph.json

记录知识关系：

```json
{
  "nodes": [...],
  "edges": [
    {"from": "RAG", "to": "Karpathy", "relation": "proposed_by"}
  ]
}
```

---

## 💡 使用技巧

### 开始会话时

1. 读取 `wiki/index.md` 了解当前知识库状态
2. 读取 `wiki/log.md` 了解最近操作
3. 根据用户请求执行相应工作流

### 入库新资料时

1. 用户将资料放入 `raw/` 对应目录
2. 等待用户明确请求处理
3. 遵循 Ingest 流程

### 回答问题时

1. 先查询 `wiki/index.md` 定位相关页面
2. 必要时查询 `wiki/graph.json` 了解关联
3. 只读取相关页面，避免全量扫描

---

## 📌 快速参考

- 用户最常用的知识来源：技术博客、微信公众号、X/Twitter
- `raw/` 可自由扩展新子目录，Agent 会自动发现
- `wiki/` 结构固定，不建议用户修改
- `workspace` 流入 `wiki` 的时机由人工判断
- Agent 负责 Git commit，用户决定 Git push

---

## ❓ 常见问题

**Q: 用户放入新资料后，我需要立即处理吗？**

A: 不需要。等待用户明确请求（如"帮我处理这个新资料"）再执行 Ingest。

**Q: 我可以修改 raw/ 中的文件吗？**

A: 绝对不可以。raw/ 是只读的。

**Q: 如何判断一个概念是否需要独立页面？**

A: 如果概念在多个来源中被提及，或值得单独解释，则创建独立页面。

**Q: 用户问的问题不在知识库中怎么办？**

A: 诚实告知，并建议用户是否需要查找相关资料入库。

---

*文档版本: 1.0 | 创建时间: 2026-04-17*
