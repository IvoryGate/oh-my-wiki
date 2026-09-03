---
title: Ad-Fraud
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, 出海投放]
sources:
  - [[raw/articles/广告作弊Ad Fraud（一）.md]]
  - [[raw/articles/除了三方归因的付费P360服务，广告投放如何防作弊Ad Fraud？.md]]
status: active
---

# Ad-Fraud（广告作弊）

广告作弊是指通过虚假手段伪造广告曝光、点击或安装行为，从而骗取广告主预算的行为。在移动广告生态中，作弊行为严重影响投放效果和预算效率。

## 作弊分类

广告作弊按安装是否由真实用户产生，分为两大类：

1. **[[Attribution-Hijacking|归因劫持]]**：真实用户，但归因被错误劫持
2. **[[Fake-Installation|虚假安装]]**：非真实用户，伪造设备或代码

## 作弊生态背景

广告行业参与者：
- **大媒体**（Meta、Google、TikTok）：自归因，不遵循第三方 MMP 规则
- **DSP**：通过 Ad Exchange 采买流量
- **Ad Network**：直接对接 Publisher 流量
- **网盟**：DSP 前身，部分从业者作弊频发
- **代理**：撮合上下游，无自有渠道

## 防作弊工具

- [[Protect360]]：AppsFlyer 付费防作弊套件
- Fraud Blocker、Spider AF（日本）、mFilterIt（印度）
- [[Platform-LVL-Validation|应用商店验证]]：Google LVL、Apple Receipt Validation、Amazon DRM

## 相关概念

- [[Attribution-Hijacking]]
- [[Fake-Installation]]
- [[Device-Farm]]
- [[Click-Flooding]]
- [[CTIT-Analysis]]
- [[Protect360]]
- [[MMP-Attribution]]
