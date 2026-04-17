---
title: RAG
created: 2026-04-17
updated: 2026-04-17
type: concept
tags: [AI, 检索, 知识管理]
sources:
  - [[raw/articles/llm-wiki.md]]
status: active
---

# RAG（Retrieval-Augmented Generation）

> 检索增强生成，一种结合外部知识库与大语言模型的技术方案

## 核心定义

RAG 让 LLM 在生成回答前先检索相关文档，将检索到的内容作为上下文，从而增强模型的知识范围和回答准确性。

## 工作流程

```
用户提问 → 向量检索 → 获取相关文档 → 拼接上下文 → LLM生成回答
```

## 局限性

根据 Karpathy 的分析：

- 每次查询都从零检索，无知识积累
- 需要向量数据库基础设施
- 跨文档推理困难
- 查询之间不存在持续构建的持久化结构

## 与 LLM Wiki 的对比

参见 [[LLM-Wiki]]

核心差异：RAG 是"解释器模式"，LLM Wiki 是"编译器模式"。

## 相关概念

- [[LLM-Wiki]]：编译器模式的知识管理
- [[知识图谱]]：另一种知识组织方式
