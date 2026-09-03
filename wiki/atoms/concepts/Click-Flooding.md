---
title: Click-Flooding
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, 归因, 出海投放]
sources:
  - [[raw/articles/广告作弊Ad Fraud（三）.md]]
status: active
---

# Click-Flooding（大点击撞库）

大点击撞库是 [[Attribution-Hijacking|归因劫持]] 的典型形式。渠道在接收到广告主的推广单子后，向 MMP 大量发送虚假/恶心的点击数据，通过 last click 规则"撞库"抢夺归因。

## 作弊能力分级

| 级别 | 手段 |
|------|------|
| 弱 | 小广告位易误触，上报点击 |
| 中 | 多个广告前后叠加，一次点击上报多条 |
| 强 | 广告位透明度 100%，用户正常点击即上报 |
| 极端 | 无广告位，默认后台运行随机上报点击 |

## 识别方法

- **CVR 极低**：万次点击仅 1 次安装
- **[[CTIT-Analysis|CTIT]] 曲线过长**：大量随机点击拉长分布
- 渠道不能带来任何实际帮助

## 相关概念

- [[Attribution-Hijacking]]
- [[CTIT-Analysis]]
- [[Last-Click-Rule]]
