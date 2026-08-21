---
title: "VC维"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [机器学习, 学习理论]
sources:
  - [[raw/articles/04 计算学习理论.md]]
status: draft
---

# VC维

## 核心定义

VC 维（Vapnik-Chervonenkis Dimension）是对假设空间复杂度的一种度量，以两位统计学习理论先驱 Vladimir Vapnik 和 Alexey Chervonenkis 的名字命名。

## 形式化定义

假设空间的 VC 维是能被该假设空间 **打散**（shatter）的最大数据集的大小。

**打散**：对于容量为 $m$ 的数据集，如果假设空间能对其所有 $2^m$ 种分类结果进行正确划分，则称该数据集被打散。

## 典型模型的 VC 维

| 模型 | VC 维 | 说明 |
|------|-------|------|
| 线性分类器 | $d+1$ | $d$ 维空间的超平面 |
| 神经网络 | 与权数量相关 | 复杂模型 VC 维更高 |
| $y=\sin(kx)$ | 无穷大 | 可拟合任意模式 |

## VC 维与泛化

- VC 维有限 $\Rightarrow$ PAC 可学习
- VC 维越大：训练误差更低，但泛化误差可能增大
- 体现偏差-方差折中

## 参考

- [[计算学习理论]]
- [[PAC可学习性]]