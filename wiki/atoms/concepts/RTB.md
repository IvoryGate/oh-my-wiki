---
title: RTB 实时竞价
created: 2026-04-22
updated: 2026-04-22
type: concept
tags: [广告归因, 广告技术]
sources:
  - [[raw/articles/广告竞价背后的逻辑和模型算法（一）.md]]
status: active
---

# RTB 实时竞价

> Real-Time Bidding，广告位的实时竞价购买

## 定义

RTB 是一种程序化广告技术，允许广告主在广告位展示的瞬间实时出价竞拍。

## 核心参与方

| 角色 | 全称 | 职责 |
|------|------|------|
| DSP | Demand-Side Platform | 广告主需求方平台 |
| SSP | Supply-Side Platform | 发布商供应方平台 |
| ADX | Ad Exchange | 广告交易所 |
| DMP | Data Management Platform | 数据管理平台 |

## 竞价流程

```
1. 用户访问页面
2. SSP 向 ADX 发送 Ad Request
3. ADX 转发请求给多家 DSP
4. DSP 根据用户特征出价
5. ADX 竞价（通常二价拍卖）
6. 胜出广告展示给用户
```

## 二价拍卖

- 胜出者支付**第二高**出价
- 鼓励广告主报出真实价格

## 相关概念

- [[DSP]]
- [[ADX]]
- [[SSP]]

## 来源

- [[raw/articles/广告竞价背后的逻辑和模型算法（一）.md]]