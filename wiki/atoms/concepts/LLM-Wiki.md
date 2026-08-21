---
title: LLM Wiki
created: 2026-04-17
updated: 2026-04-21
type: concept
tags: [知识管理]
sources:
  - [[raw/articles/llm-wiki.md]]
status: active
---

# LLM Wiki

> 一种使用大语言模型构建个人知识库的模式

## 核心定义

LLM Wiki 是 Andrej Karpathy 提出的一种知识管理模式。核心思想是：**让 LLM 将原始资料"编译"成结构化的知识网络，而不是每次查询时重新检索原始文档。**

## 与 RAG 的本质区别

| 传统 RAG | LLM Wiki |
|----------|----------|
| 解释器模式 | 编译器模式 |
| 查询时重新检索 | 入库时预先编译 |
| 知识不积累 | 知识复利增长 |
| 无持久化结构 | 生成中间表示 |

## 三层架构

```
Raw Sources     →  原始资料（只读）
The Wiki        →  结构化知识（LLM维护）
The Schema      →  配置规则（工作流定义）
```

## 核心操作

### Ingest（入库）
新资料进入时：
- LLM 阅读理解
- 与用户讨论关键收获
- 写入摘要页
- 更新相关实体/概念页
- 维护索引和日志

### Query（查询）
基于已编译的知识回答问题，高质量答案可归档为新页面。

### Lint（体检）
定期健康检查：矛盾、孤立页面、过时信息、缺失概念。

## 核心洞察

> "维护知识库最累的不是阅读和思考，而是记账。读文章、判断价值、决定方向 — 这些是人该干的事。整理格式、更新链接、维护索引 — 这些 bookkeeping 的活，交给 AI 干最合适。"

## 相关概念

- [[RAG]]：检索增强生成，LLM Wiki 的对比方案
- 知识图谱（Knowledge Graph）：另一种知识组织方式，以实体-关系为核心的图结构

## 相关实体

- [[Karpathy]]：LLM Wiki 的提出者

## 延伸阅读

- [原始 Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
