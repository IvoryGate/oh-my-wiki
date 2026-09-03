---
title: Device-Farm
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, 出海投放]
sources:
  - [[raw/articles/广告作弊Ad Fraud（二）.md]]
status: active
---

# Device-Farm（设备农场）

设备农场是 [[Fake-Installation|虚假安装]] 的主要形式之一。作弊平台通过模拟器重置设备 ID，反复刷新并虚拟点击广告主广告，批量大规模下载安装应用。

## 成本与洗白

- 设备农场成本已非常高昂，利润极低
- **洗白**：走代理刷头部 Ad Network + 大 App 量来绕过 MMP 检测
- 2024 年后 MMP 设置渠道和代理双向握手验证

## 识别特征

- IP 分布高度集中
- 设备信息库中新设备比例异常高
- 安装行为缺乏真实的用户交互模式

## 相关概念

- [[Fake-Installation]]
- [[Attribution-Hijacking]]
- [[CTIT-Analysis]]
