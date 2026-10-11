---
title: RAG
created: 2026-04-17
updated: 2026-10-11
type: concept
domain: LLM
description: 检索增强生成技术
tags: [域/LLM]
sources:
  - [[raw/columns/菜鸟教程AI智能体/12 RAG 与知识检索.md]]
  - [[raw/columns/菜鸟教程AI智能体/27 GraphRAG 入门教程.md]]
  - [[raw/columns/菜鸟教程AI智能体/42 Python 实现 RAG 与知识检索.md]]
  - [[raw/columns/菜鸟教程AI/12 RAG 检索增强生成.md]]
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

## GraphRAG

针对上述"跨文档推理困难、无持久结构"的局限，GraphRAG 给出图增强方案：先将文档构建成知识图谱并做社区检测，检索时结合图结构与社区摘要回答全局性问题（如"这批文档的共同主题是什么"），而非只取相似片段。详见 [[raw/columns/菜鸟教程AI智能体/27 GraphRAG 入门教程.md]]。

## 与 LLM Wiki 的对比

参见 [[LLM-Wiki]]

核心差异：RAG 是"解释器模式"，LLM Wiki 是"编译器模式"。

## 相关概念

- [[LLM-Wiki]]：编译器模式的知识管理
- 知识图谱（Knowledge Graph）：另一种知识组织方式（库内未单独建页，可用 Obsidian Graph View 浏览链接网络，本库配色与过滤见 [[Obsidian关系图谱配置指南]]）

## 来源

- [[raw/articles/llm-wiki.md]]
- [[raw/columns/菜鸟教程AI/12 RAG 检索增强生成.md]]
- [[raw/columns/菜鸟教程AI智能体/12 RAG 与知识检索.md]]
- [[raw/columns/菜鸟教程AI智能体/27 GraphRAG 入门教程.md]]
- [[raw/columns/菜鸟教程AI智能体/42 Python 实现 RAG 与知识检索.md]]

