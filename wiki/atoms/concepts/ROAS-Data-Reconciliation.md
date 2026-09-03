---
title: ROAS-Data-Reconciliation
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 数据分析, ROAS, 出海投放]
sources:
  - [[raw/articles/Unity平台ROAS开启条件和数据差异问题.md]]
  - [[raw/articles/渠道MMPBI的数据差异剖析 1.md]]
status: active
---

# ROAS-Data-Reconciliation（ROAS 数据对齐）

ROAS（Return on Ad Spend）= Revenue / Cost。不同平台间 ROAS 数据经常出现差异，根因在于 D0/D1 定义规则不同。

## 数据传递链路

```
广告平台 → MMP SDK → MMP 服务器 → MMP 后台
                    ↘ 广告平台后台
应用内事件 → MMP SDK → MMP 服务器 → 回传给广告平台
```

## 差异根因

### 1. D0 定义规则不同

| 平台 | D0 定义 |
|------|---------|
| AppsFlyer | Calendar day（自然日）|
| Unity | Rolling 24 hours |
| Adjust | Rolling 24 hours |

**示例**：UTC 12月15日 10:00 安装，12月16日 04:00 产生 ad revenue
- AppsFlyer 记为 D1（跨自然日）
- Unity 记为 D0（仍在 24 小时内）

### 2. 数据回传延迟

- Cost 通过 API 每天同步四次
- Ad Revenue 从应用 SDK 上报给 MMP 有延迟
- 最近 1-2 天数据不准确

### 3. MMP 后台配置

- 事件埋点定义不清晰
- 回传窗口期设置（建议 ≥15 天）
- 是否回传 Organic/其他渠道数据

## 数据差异排查思路

1. 确认时区是否一致
2. 导出双方 raw data 对比
3. 按 IFA 逐条比对差异
4. 排除回传延迟影响（对比 3-5 天前数据）

## 常见坑

| 问题 | 原因 |
|------|------|
| ROAS 每天微小差距 | 时区问题 |
| 平台无 RR D7 数据 | 事件回传窗口期设为 7 天 |
| MMP 无成本数据 | 广告平台不支持 API 传输 |
| MMP 数据远高于广告平台 | Cohort 视角 vs Overview 视角混淆 |
| BI 数据远低于平台 | 金额单位错误（美分→美元）|

## 相关概念

- [[Cohort-Analysis]]
- [[Session-Tracking]]
- [[DAU-Retention-Rate]]
- [[MMP-Attribution]]
