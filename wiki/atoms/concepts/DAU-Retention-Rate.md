---
title: DAU-Retention-Rate
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 数据统计, 出海投放]
sources:
  - [[raw/articles/出海投放基础知识之数据统计（一）.md]]
status: active
---

# DAU-Retention-Rate（日活与留存率）

DAU 和留存率是衡量应用健康度的核心指标，基于 [[Session-Tracking]] 统计。

## DAU（日活跃用户）

一天内至少有一次互动的唯一用户数。

**唯一用户标识：**
- 用户 ID（已登录，优先）
- 设备 ID（未登录）
- Session ID

> 一个用户 ID + 当天至少一个 Unique Session = 一个活跃用户

## Retention Rate（留存率）

### 广告主侧

留存数 = 当天日活 / 总体用户数

### 广告平台侧

- **总体留存**：与广告主侧计算逻辑相同
- **[[Cohort-Analysis|群组（Cohort）留存]]**：按安装日期分组，追踪每批用户的后续留存

### Cohort 留存示例

| 安装日 | 用户数 | 4日数据 |
|--------|--------|---------|
| 1月1日 | 3 | RR D2（第3天）|
| 1月2日 | 5 | RR D1（第2天）|
| 1月3日 | 4 | 积累中 |

衡量广告平台效果时，看 Cohort 数据更有对比意义。

## 相关概念

- [[Session-Tracking]]
- [[Cohort-Analysis]]
- [[ROAS-Data-Reconciliation]]
