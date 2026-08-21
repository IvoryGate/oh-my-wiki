---
title: "EM算法"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [机器学习]
sources:
  - [[raw/articles/39 隐变量下的参数学习：EM方法与混合模型.md]]
status: draft
---

# EM算法

## 核心定义

期望最大化算法（Expectation-Maximization）用于含隐变量的参数估计。

## 两步迭代

| 步骤 | 说明 |
|------|------|
| E步 | 计算后验分布 $Q(\theta) = p(Z \mid X, theta^{old})$ |
| M步 | 最大化期望 $\theta^{new} = \arg\max_theta Q(theta)$ |

## 应用

- 混合模型
- 聚类
- 隐马尔可夫模型

## 特点

- 收敛保证
- 初始值敏感
- 局部最优

## 来源

- [[raw/articles/39 隐变量下的参数学习：EM方法与混合模型.md]]