---
title: "Transformer"
created: 2026-10-11
updated: 2026-10-11
type: concept
domain: 机器学习
description: 编码器-解码器与自注意力构成的序列建模架构
tags: [域/机器学习, 主题/神经网络]
sources:
  - [[raw/columns/菜鸟教程NLP/12 Transformer 架构.md]]
status: active
---

# Transformer

## 核心定义

Transformer 是一种基于自注意力机制（Self-Attention）的深度学习模型，由 Google 团队在 2017 年的论文《Attention Is All You Need》中首次提出。它采用经典的编码器-解码器（Encoder-Decoder）结构，完全依赖注意力机制捕捉输入序列中的全局依赖关系，无需循环或卷积结构。与 RNN 不同，Transformer 可以一次性并行处理整个输入，是 GPT、BERT 等现代大语言模型的核心基础。

## 编码器-解码器结构

Transformer 每个部分都由多层相同模块堆叠而成。

**编码器（Encoder）** 的核心组件：

- 多头自注意力（Multi-Headed Self-Attention）：并行计算输入中所有词之间的关系，捕捉不同子空间的语义信息
- 前馈网络（Feed-Forward Network）：对每个词的表示做非线性变换和特征提取
- 残差连接与层归一化：缓解梯度消失、稳定训练过程

**解码器（Decoder）** 在编码器基础上增加了两层：

- 掩码多头注意力（Masked Multi-Headed Self-Attention）：训练时防止"作弊"，只能看到当前及之前的词，不能看未来的词
- 多头交叉注意力（Multi-Headed Cross-Attention）：让解码器查询编码器的输出，融合源序列信息
- 顶部线性层（Linear）：将输出映射到词表，得到下一个词的概率分布

## 自注意力与多头注意力

自注意力是 Transformer 的核心思想，其缩放点积公式为：

`Attention(Q, K, V) = softmax(QKᵀ / √d_k)V`

- Q（Query）、K（Key）、V（Value）由输入经线性变换得到
- √d_k 是缩放因子，防止点积过大导致梯度消失
- 计算流程：求相似度得分 → softmax 转为权重 → 加权求和得到输出

多头注意力（Multi-Head Attention）将自注意力并行执行多次，每个头学习不同的注意力模式（如局部/全局依赖、语法/语义特征），最后拼接结果，从而捕捉更丰富的上下文信息。

## 位置编码

Transformer 没有循环或卷积结构，无法直接感知序列顺序，因此需要显式注入位置信息：

- 使用正弦/余弦函数计算位置编码，分别对应向量的偶数维和奇数维
- 参数包括位置 pos、维度索引 i 和向量维度 d_model（通常与词向量维度相同）
- 特点：相对位置敏感、长度可扩展（可处理比训练时更长的序列）、确定性计算无需学习

## 并行优势与局限

与传统架构对比：

- 并行性：完全并行处理整个序列，训练效率远高于逐时间步计算的 RNN/LSTM
- 长距离依赖：任意两个词可直接建立依赖关系，解决长距离依赖问题
- 可扩展性：模型规模可轻松扩大，且迁移学习友好（预训练 + 微调范式）
- 局限：自注意力的空间复杂度为 O(n²)，处理长序列时内存消耗较大

## 参考

- [[注意力机制]]
- [[Seq2Seq]]
- [[深度学习]]
- [[BERT]]
- [[GPT]]

## 来源

- [[raw/columns/菜鸟教程NLP/12 Transformer 架构.md]]
