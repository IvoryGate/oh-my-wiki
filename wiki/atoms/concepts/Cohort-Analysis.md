---
title: Cohort-Analysis
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 数据分析, 出海投放]
sources:
  - [[raw/articles/什么是Cohort队列？.md]]
  - [[raw/articles/Unity平台ROAS开启条件和数据差异问题.md]]
status: active
---

# Cohort-Analysis（队列分析）

Cohort 是根据共有特征（安装时间、购买行为、注册来源等）将用户分组，然后追踪同组用户在生命周期内的行为轨迹。

## 两种维度

| 维度 | 说明 | 示例 |
|------|------|------|
| 时间维度 | 基于时间点分组 | 10月注册用户、11月注册用户 |
| 行为维度 | 基于事件分组 | 低于 ¥10 付费、¥10-20 付费 |

## 核心指标

- **RR（留存率）**：同 cohort 用户在不同时间点是否仍活跃
- **LR（流失率）**：离开或停止使用的比例
- **ARPU**：每用户平均收入
- **[[ROAS-Data-Reconciliation|ROAS]]**：收入/成本
- **CR（转化率）**：注册到购买的转化

## Cohort vs Overview

- **Overview**：宏观指标展示（如每天新增多少用户）
- **Cohort**：同周期对比（如 1月注册用户在 2月的活跃率 vs 12月注册用户）

## 实际应用

通过 Cohort 视角对比 ROAS D0/D3/D7，可排除大 R（大额付费）影响，更真实评估渠道质量。

> 注意：AppsFlyer 用 calendar day 定义 D0，Unity 用 rolling 24 hours，Adjust 也用 rolling 24 hours——这是 ROAS 数据差异的根因。

## 相关概念

- [[ROAS-Data-Reconciliation]]
- [[DAU-Retention-Rate]]
- [[Session-Tracking]]
