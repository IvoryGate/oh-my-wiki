---
title: "Logistic 回归"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [机器学习, 分类, 逻辑回归]
sources:
  - [[raw/articles/15 从回归到分类：联系函数与降维.md]]
  - [[raw/articles/16 建模非正态分布：广义线性模型.md]]
status: draft
---

# Logistic 回归

## 核心定义

Logistic 回归（Logistic Regression）是一种基于概率的分类算法，通过 **联系函数**（Link Function）将线性回归的连续输出转换为类别概率。

## 数学表达式

二分类问题的后验概率：

$$p(C_1 \mid \mathbf{x}) = \frac{1}{1 + \exp(-a)} = \sigma(a)$$

其中 $a = \mathbf{w}^T \mathbf{x} + b$，$\sigma(\cdot)$ 是 **对数几率函数**（Logistic Function）。

## 与线性回归的区别

| 特性 | 线性回归 | Logistic 回归 |
|------|---------|--------------|
| 输出类型 | 连续值 | 概率值 (0,1) |
| 联系函数 | 无 | $\sigma(x) = 1/(1+e^{-x})$ |
| 损失函数 | MSE | 对数似然 |

## 参数估计

Logistic 回归使用 **最大似然估计**（MLE）确定参数，无法直接给出解析解，需要数值优化。

## 参考

- [[线性判别分析]]：另一种线性分类方法，假设数据服从正态分布
- [[广义线性模型]]：Logistic 回归是 GLM 的特例