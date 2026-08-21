---
title: "PAC可学习性"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [机器学习, 学习理论]
sources:
  - [[raw/articles/04 计算学习理论.md]]
status: draft
---

# PAC可学习性

## 核心定义

PAC（Probably Approximately Correct）可学习性是机器学习理论中的核心概念，指一个学习算法能够在多项式时间内，以较大概率学习到一个近似正确的模型。

## 两个核心参数

| 参数 | 含义 | 描述 |
|------|------|------|
| $\epsilon$ (准确度) | 近似正确 | 模型的误差控制在 $\epsilon$ 范围内 |
| $\delta$ (置信度) | 概率 | 学习成功的概率至少为 $1-\delta$ |

## 形式化定义

如果一个假设空间是 PAC 可学习的，则存在一个学习算法，对于任意分布的训练数据，只需多项式数量的样本，就能以至少 $1-\delta$ 的概率输出一个泛化误差小于 $\epsilon$ 的假设。

## 关键结论

- **有限假设空间都是 PAC 可学习的**
- VC 维有限 $\Rightarrow$ PAC 可学习
- 样本复杂度与 $\epsilon$、$\delta$ 成反比

## 参考

- [[计算学习理论]]
- [[VC维]]