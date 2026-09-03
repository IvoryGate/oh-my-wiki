---
title: Session-Tracking
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 数据统计, 出海投放]
sources:
  - [[raw/articles/出海投放基础知识之数据统计（一）.md]]
status: active
---

# Session-Tracking（会话追踪与统计）

Session（会话）是用户与应用一段连续交互过程的记录，是统计 DAU、留存率等指标的基础。

## Session 定义

- **唯一标识**：随机生成的 Session ID
- **行为触发**：启动应用/访问特定页面/登录/从后台切入
- **超时机制**：闲置超时（如 15/30/50 分钟）则 Session 结束

## MMP 统计差异

| MMP | 统计方式 | 默认间隔 |
|-----|----------|----------|
| AppsFlyer | af_app_opened 事件 | 10 分钟（1分钟-24小时可调）|
| Adjust | session callback | 30 分钟 |

## 聚合平台统计

聚合平台仅在请求广告后才统计 Session，与应用本身的 Session 数不同。

## 数据一致性要点

- 内部闲置时间与 MMP 保持一致
- 统一选择 0 时区上报
- 优先使用用户 ID（可一一映射）而非设备 ID

## 相关概念

- [[DAU-Retention-Rate]]
- [[Cohort-Analysis]]
- [[ROAS-Data-Reconciliation]]
