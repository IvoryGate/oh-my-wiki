---
title: "LASSO"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [机器学习, 正则化, 线性回归]
sources:
  - [[raw/articles/12 正则化处理：收缩方法与边际化.md]]
status: draft
---

# LASSO

## 核心定义

LASSO（Least Absolute Shrinkage and Selection Operator）是对线性回归的 L1 正则化改进，通过在损失函数中添加参数向量的 L1 范数来抑制过拟合，同时实现特征选择。

## 数学形式

$$\tilde E(\mathbf{w}) = \frac{1}{2}\sum_{n=1}^{N}(y_n - \mathbf{w}^T \mathbf{x}_n)^2 + \lambda \|\mathbf{w}\|_1$$

其中 $\lambda > 0$ 是正则化系数。

## 几何意义

- 解空间是方形（$|w_1| + |w_2| < t$）
- 切点最可能出现在顶点，导致某些权重直接为 0
- 自动进行特征选择

## 与岭回归对比

| 特性 | LASSO | 岭回归 |
|------|-------|--------|
| 正则项 | L1 范数 | L2 范数平方 |
| 解空间 | 方形 | 球形 |
| 特征选择 | 是 | 否 |

## 来源

- [[raw/articles/12 正则化处理：收缩方法与边际化.md]]