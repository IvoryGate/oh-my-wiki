---
title: Mediation-Platform
aliases: [聚合平台, Mediation, 聚合]
created: 2026-10-15
updated: 2026-10-15
type: concept
domain: 增长与营销
description: 聚合平台（Mediation）分发 Publisher 流量、桥接买量与变现的生态角色
tags: [主题/广告技术, 域/增长与营销]
sources:
  - "[[raw/articles/广告作弊Ad Fraud（一）.md]]"
status: active
---

# 聚合平台（Mediation）

> 能够独立对接多个上游 ad network 的工具，分发 publisher 的广告位流量，实现收益效率最大化。

## 生态位置

Publisher 的一个广告位可以请求多家 network 的广告，聚合平台在其中做竞价与分配，决定每次展示给谁。它是买量与变现两侧的桥：

- 变现侧：广告主竞价 → 聚合平台分发展示 → publisher 获得收入
- 买量侧：聚合平台背后的 network 流量池，也是其他广告主投放时的下游供给

## 常见聚合平台

| 聚合平台 | 所属 | 前身 |
|---|---|---|
| AdMob | Google | — |
| MAX | AppLovin | Twitter 的 Mopub |
| LevelPlay | Unity（整合 ironSource） | ironSource 聚合 |
| Helium | Chartboost | — |

## 买量与变现同源的误区

"同一家公司的买量和变现产品"（如 AppLovin 的 AppDiscovery+MAX、Unity Ads+LevelPlay）并不自动意味着：

- 归因数据自动打通
- 变现收入自动回传买量侧作为优化信号
- 变现收益可直接抵扣广告费（取决于具体账户与合同）

变现收益再投入买量是一种经营策略，能否简化流程要看平台实际提供的功能。

## 与相邻概念的关系

- [[程序化广告]]：聚合主要发生在 publisher 侧广告位，不经 ADX 的流量由 network 直采；经 ADX 的流量才进入 RTB 生态
- 子渠道：聚合使下游出现二级嵌套——network 的初级渠道下还有其聚合的具体 app（子渠道）
- [[Ad-Fraud]]：聚合链路也是流量透明度检查的关键环节

## 来源

- [[raw/articles/广告作弊Ad Fraud（一）.md]]
