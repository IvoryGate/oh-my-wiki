---
title: Attribution-Hijacking
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, 归因, 出海投放]
sources:
  - [[raw/articles/广告作弊Ad Fraud（三）.md]]
  - [[raw/articles/广告作弊Ad Fraud（一）.md]]
status: active
---

# Attribution-Hijacking（归因劫持）

归因劫指广告平台利用 last click 归因模型的"漏洞"，抢夺自然 Organic 或其他渠道用户的行为。与 [[Fake-Installation|虚假安装]] 的最大区别是：归因劫持的安装都是真实用户。

## 损失

1. **直接损失**：本该给 A 渠道的付款走到了 B 渠道；若劫持的是自然用户，则为纯额外支出
2. **深度损失**：A 渠道依靠回传做算法定向，劫持量级大时 A 渠道很难跑起，甚至被 MMP 拒绝

## 分类

### 点击类

- **[[Click-Flooding|大点击撞库]]**：向 MMP 发送大量虚假点击"撞库"归因
- **监听安装**（安卓独有）：通过 BroadcastReceiver 监听系统广播，抢在用户安装前上报点击
- **渠道劫持**：第三方应用商店引导用户从非预期渠道下载

### 曝光类

- 曝光归因开启过高（50%+ 来自 VTA 不正常）
- Onelink 概率归因风险

## 识别方法

| 指标 | 说明 |
|------|------|
| CVR | 安装/点击比极低（万次点击仅 1 次安装）|
| ATP | 归因交互类型占比，正常 CTA:VTA ≈ 8:2 |
| [[CTIT-Analysis]] | 点击到安装时间分布异常 |
| 助攻率 | 与自然流量趋势呈反向波动 |
| 归因模型占比 | engaged_click/engaged_view 占比异常 |

## 相关概念

- [[Fake-Installation]]
- [[Click-Flooding]]
- [[CTIT-Analysis]]
- [[Last-Click-Rule]]
- [[MMP-Attribution]]
