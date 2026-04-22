---
id: mmp-attribution
title: MMP 归因
aliases:
  - 第三方归因
  - MMP Attribution
  - Mobile Measurement Partner
type: concept
created: 2026-04-18
updated: 2026-04-22
sources:
  - [[raw/articles/关于归因你可能不知道的那些事(一）.md]]
  - [[raw/articles/出海投放基础知识之归因（一）.md]]
tags:
  - 增长
  - 营销
  - 归因
  - 广告
---

## 定义

MMP (Mobile Measurement Partner) 归因是第三方归因公司提供的移动广告归因解决方案，覆盖所有主流平台。

## 常用 MMP 平台

海外主流 MMP 平台：
- Appsflyer
- Adjust
- Singular
- Branch
- Tenjin
- Kochava
- Appmetrica

## 成功归因公式

一个成功的归因 = 归因规则 + 归因模型 + 归因方法 + 归因窗口期

## 核心流程

1. **集成 SDK**：App 集成归因公司 SDK，收集所有新增激活信息
2. **大媒体认领**：激活信息发给大媒体，大媒体匹配自己的展示/点击数据
3. **结果返回**：大媒体把认领结果发给归因公司（未必是全部）
4. **数据入库**：归因公司把所有展示点击信息入库
5. **重新匹配**：按 last click 原则重新匹配
6. **报表呈现**：得出最终归因结果

## 核心规则

- **点击归因窗口**：7 天
- **展示归因窗口**：半天到一天
- **优先级**：点击 > 展示
- **原则**：Last Click

## 与大媒体的 Gap

| Gap 来源 | 说明 | 占比 |
|----------|------|------|
| 展示归因 Gap | 大媒体默认展示归因，MMP 不一定认可 | ~30% |
| 点击归因 Gap | 其他渠道 Last Click 抢走归因 | ~10% |

## 常见误区

> 其他渠道会"偷"大媒体的归因？**错误！**

实际情况：
- 大媒体是展示就归因给自己
- MMP 按点击优先原则，归因给其他渠道
- **是大媒体多认领了其他渠道贡献的安装**

## 相关概念

- [[SKAN-Attribution]]
- [[Last-Click-Rule]]
- [[Attribution-Gap]]

## 来源

- [[raw/articles/关于归因你可能不知道的那些事(一）.md]]
- [[raw/articles/出海投放基础知识之归因（一）.md]]
