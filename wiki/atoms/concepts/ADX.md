---
title: ADX 广告交易所
created: 2026-04-22
updated: 2026-04-22
type: concept
tags: [广告归因, 广告技术]
sources:
  - [[raw/articles/广告竞价背后的逻辑和模型算法（一）.md]]
status: active
---

# ADX 广告交易所

> Ad Exchange，广告交易的中心枢纽

## 定义

ADX（Ad Exchange）是连接广告买卖双方的交易平台，负责管理 DSP 和 SSP 之间的广告位交易。

## 核心职能

1. **接收请求**：从 SSP 接收广告位请求
2. **转发请求**：将请求发送给多家 DSP
3. **竞价管理**：组织竞价，选择胜出者
4. **结果反馈**：告知 DSP 竞价结果
5. **下发广告**：将胜出广告发送给用户设备

## 竞价流程

```
Request → Auction → Response → Win → Fill → Show
```

| 阶段 | 说明 |
|------|------|
| Request | SSP 向 ADX 发送广告位请求 |
| Auction | ADX 向 DSP 发送竞价请求 |
| Response | DSP 返回出价和广告物料 |
| Win | ADX 选出最高出价者 |
| Fill | 下发广告物料 |
| Show | 广告展示 |

## 相关概念

- [[DSP]]
- [[SSP]]

## 来源

- [[raw/articles/广告竞价背后的逻辑和模型算法（一）.md]]