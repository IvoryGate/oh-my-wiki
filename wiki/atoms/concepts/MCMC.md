---
title: "MCMC"
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [机器学习, 近似推断, 蒙特卡洛]
sources:
  - [[raw/articles/37 随机近似推断：MCMC.md]]
status: draft
---

# MCMC

## 核心定义

马尔可夫链蒙特卡洛（Markov Chain Monte Carlo）通过构建马尔可夫链进行蒙特卡洛采样。

## 基本思想

1. 构建马尔可夫链，使平稳分布 = 目标分布
2. 从链上采样，用样本估计期望

## 经典算法

| 算法 | 说明 |
|------|------|
| Metropolis-Hastings | 通用框架 |
| Gibbs采样 | 条件分布采样 |
| Hamiltonian MC | 利用梯度信息 |

## 特点

- 通用性强
- 计算量大
- 可处理复杂分布

## 参考

- [[推断]]