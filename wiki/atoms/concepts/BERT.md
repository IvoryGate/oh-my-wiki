---
title: "BERT"
created: 2026-10-11
updated: 2026-10-11
type: concept
domain: 机器学习
description: 基于 Transformer 编码器的双向预训练语言模型
tags: [域/机器学习, 主题/神经网络]
sources:
  - [[raw/columns/菜鸟教程NLP/15 BERT 系列模型.md]]
  - [[raw/columns/菜鸟教程NLP/14 预训练模型.md]]
status: active
---

# BERT

## 核心定义

BERT（Bidirectional Encoder Representations from Transformers）是 Google 于 2018 年提出的自然语言处理模型，彻底改变了 NLP 的研究与应用范式。它基于 [[Transformer]] 的编码器部分构建，通过掩码语言模型（MLM）等预训练任务学习双向上下文的通用语言表示，再针对下游任务微调。BERT 属于预训练模型中的 Encoder 架构代表，适合分类、问答等理解类任务。

## 架构定位与输入层

**编码器架构**：BERT 的核心是多层 Transformer 编码器块，每个块包含自注意力机制（双向捕捉上下文依赖）、前馈神经网络、残差连接与层归一化，输出每个输入词对应的上下文相关向量表示。

**输入嵌入（Embedding）** 由三部分组成：

- 词嵌入（Token Embeddings）：词汇的语义信息
- 位置嵌入（Position Embeddings）：词在序列中的位置
- 段嵌入（Segment Embeddings）：区分句子，服务句对任务

## 预训练任务

BERT 通过两种预训练任务实现双向上下文理解：

1. **掩码语言模型（Masked Language Modeling, MLM）**：随机遮盖 15% 的输入 token 并替换为 `[MASK]`，模型根据上下文预测被遮盖的原词。预测时经全连接层（激活函数为 GELU）映射到词表，再用 softmax 选出概率最高的词
2. **下一句预测（Next Sentence Prediction, NSP）**：判断两个句子是否连续出现，学习句子间关系

双向性是关键创新：与只能从左到右的传统语言模型不同，BERT 同时考虑左右上下文。

**训练配置**：

| 参数 | BERT-base | BERT-large |
| --- | --- | --- |
| 层数 | 12 | 24 |
| 隐藏层大小 | 768 | 1024 |
| 注意力头数 | 12 | 16 |
| 总参数量 | 110M | 340M |

## 微调与变体

**标准微调流程**：添加任务适配层（分类/回归层）→ 使用较小学习率（2e-5 到 5e-5）→ 批次 16 或 32 → 训练 2-4 个 epoch。

常用微调策略：

- 全参数微调：性能最优，计算成本高
- 特征提取（冻结 BERT）：计算高效，性能次优
- 适配器（Adapter）：参数高效，需架构修改
- 提示学习（Prompt）：小样本效果好，需设计提示模板

**主流变体**：

- RoBERTa：更大批次、更长训练、移除 NSP、动态遮盖
- ALBERT：跨层参数共享与嵌入分解，参数量减少 89%
- DistilBERT：知识蒸馏压缩；ELECTRA：生成器-判别器架构替代 MLM
- 中文模型：BERT-wwm（全词遮盖）、ERNIE（融入知识图谱）等

## 参考

- [[Transformer]]
- [[注意力机制]]

## 来源

- [[raw/columns/菜鸟教程NLP/15 BERT 系列模型.md]]
- [[raw/columns/菜鸟教程NLP/14 预训练模型.md]]
