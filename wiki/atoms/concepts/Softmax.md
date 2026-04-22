---
title: "Softmax"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [机器学习, 分类, 神经网络]
sources:
  - [[raw/articles/17 几何角度看分类：支持向量机.md]]
status: draft
---

# Softmax

## 核心定义

Softmax 是多分类问题的输出层函数，将 logits 转换为概率分布。

## 数学形式

$$\text{Softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{K} e^{x_j}}$$

## 特点

- 输出所有类别概率之和为 1
- 指数运算放大差异
- 常用作交叉熵损失的输入

## 与 Sigmoid 的关系

- Sigmoid：二分类，等价于 K=2 的 Softmax
- Softmax：多分类推广

## 参考

- [[交叉熵]]
- [[Logistic回归]]