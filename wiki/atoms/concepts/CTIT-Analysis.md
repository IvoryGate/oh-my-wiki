---
title: CTIT-Analysis
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, 数据分析, 出海投放]
sources:
  - [[raw/articles/广告作弊Ad Fraud（三）.md]]
  - [[raw/articles/广告作弊Ad Fraud（五）.md]]
status: active
---

# CTIT-Analysis（点击到安装时间分析）

CTIT（Click Time to Install）是分析广告流量质量的核心指标，通过点击/曝光与安装之间的时间差分布来识别作弊。

## 两个关键时间戳

| 时间戳 | 说明 |
|--------|------|
| Click Time to Install Begin | 点击到安装开始的时间差 |
| Click Time to Install | 点击到安装完成的时间差 |

## 正常 vs 异常分布

- **正常 CTIT**：遵守正态分布曲线
- **过短 CTIT**：安装监听劫持特征（监听 App 抢先上报点击）
- **过长 CTIT**：大点击撞库或视频渠道频繁曝光撞自然用户
- **双曲线重合异常**：install_begin_time > install_time 必有问题

## 在 MMP 中的应用

- AppsFlyer：通过 raw data 中的 Attribution Touch Time、Install Time 等字段计算
- Adjust：Distribution Outlier（DO）类比 CTIT
- Singular：TTI Outliers Detection

## 相关概念

- [[Attribution-Hijacking]]
- [[Click-Flooding]]
- [[Fake-Installation]]
- [[Protect360]]
