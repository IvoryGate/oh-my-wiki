---
title: Protect360
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, MMP, AppsFlyer, 出海投放]
sources:
  - [[raw/articles/广告作弊Ad Fraud（四）.md]]
  - [[raw/articles/广告作弊Ad Fraud（五）.md]]
  - [[raw/articles/除了三方归因的付费P360服务，广告投放如何防作弊Ad Fraud？.md]]
status: active
---

# Protect360（AppsFlyer 防作弊套件）

AppsFlyer 提供的防作弊体系，分为免费的 Protect LITE 和付费的 Protect 360。

## 防作弊框架

两套组合方案：
- **实时检测（real-time）**：归因判定时拦截虚假安装，数据实时更新
- **归因后再检测（post-attribution）**：归因完成后重新验证，每天 UTC 10 时更新

## 四层防作弊漏斗

| 层级 | 说明 |
|------|------|
| 点击 | ip_blacklist、invalid_fingerprint、click_capping、click_signing |
| 安装 | 虚假设备/机器人特征 |
| 聚类 | 行为特征聚类，类似信号的频域分析 |
| 事件 | 应用内事件异常检测 |

## 功能模块

- **Protect LITE**（免费）：基础实时拒绝激活
- **Protect 360**（付费）：全功能解锁
- **Validation Rule**：自定义验证规则（CTIT Gap、忠实用户定义等）
- **Event Rule**：事件顺序验证（防 SDK 破解刷事件）
- **Fraud Protection Studio (FPS)**：自定义标记/上报阈值

## 使用注意

- 月初 8 号之后再核减上月流量（PAF 报告定稿）
- 观察助攻率波动检测渠道劫持
- 同一 network 子渠道分布分析

## 相关概念

- [[Ad-Fraud]]
- [[Attribution-Hijacking]]
- [[Fake-Installation]]
- [[CTIT-Analysis]]
- [[MMP-Attribution]]
