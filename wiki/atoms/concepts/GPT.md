---
title: "GPT"
created: 2026-10-11
updated: 2026-10-11
type: concept
domain: 机器学习
description: 基于 Transformer 解码器的自回归生成模型
tags: [域/机器学习, 主题/神经网络]
sources:
  - [[raw/columns/菜鸟教程NLP/16 生成式预训练模型.md]]
  - [[raw/columns/菜鸟教程NLP/14 预训练模型.md]]
status: active
---

# GPT

## 核心定义

GPT（Generative Pre-trained Transformer）是基于 [[Transformer]] 解码器的自回归（Autoregressive）生成式预训练模型，由 OpenAI 自 2018 年起持续迭代。它通过大规模无监督预训练学习通用语言知识，再针对具体任务微调或直接通过提示使用。作为预训练模型中的 Decoder 架构代表，GPT 擅长文本生成，是生成式大语言模型的核心路线。

## 自回归原理与 Next-Token Prediction

自回归语言模型通过前文预测下一个词的概率分布：

`P(x_t | x_<t) = P(x_t | x_1, x_2, ..., x_{t-1})`

- 词序列的联合概率分解为各位置条件概率的连乘：`P(x) = ∏ P(x_t | x_<t)`
- 训练使用最大似然估计，最大化各位置对数似然之和
- 生成时按 Next-Token Prediction 逐词生成：每次基于已生成的前文预测下一个词，再拼接回输入继续生成，直到产生结束标记

**解码器架构关键组件**：

1. 掩码自注意力（Masked Self-Attention）：通过上三角掩码防止信息泄露，每个词只关注前面的词，保证单向（从左到右）上下文
2. 位置编码：注入序列顺序信息
3. 前馈网络：逐位置特征变换

## 发展历程

- **GPT-1**（2018）：12 层 Transformer 解码器、1.17 亿参数，首次展示"预训练 + 微调"两阶段范式的有效性
- **GPT-2**（2019）：15 亿参数，移除微调阶段，展示 zero-shot 学习能力，上下文窗口 1024 tokens
- **GPT-3**（2020）：1750 亿参数、96 层，实现 few-shot 学习与上下文学习（in-context learning），无需微调即可完成多种 NLP 任务
- **GPT-4**（2023）：多模态（文本 + 图像）、更长上下文记忆（32k tokens）、增强的推理与指令跟随能力

## 文本生成与解码策略

典型解码策略对比：

| 策略 | 特点 |
| --- | --- |
| 贪婪搜索 | 每步取概率最高的词，确定性高但缺乏多样性 |
| 随机采样 | 可调温度与候选范围，创造性好但可能不连贯 |
| Beam Search | 平衡生成质量与多样性 |

常见生成控制参数：

- temperature：控制随机性（0-1）
- top_k：候选词数量；top_p：核采样阈值
- max_length：最大生成长度；repetition_penalty：重复惩罚因子

**Prompt Engineering** 是使用 GPT 类模型的重要配套技术：明确表达意图、提供上下文、结构化格式、few-shot 示例驱动，并可配合角色设定、步骤分解与思维链（CoT）等技巧。

## 参考

- [[Transformer]]
- [[注意力机制]]

## 来源

- [[raw/columns/菜鸟教程NLP/16 生成式预训练模型.md]]
- [[raw/columns/菜鸟教程NLP/14 预训练模型.md]]
