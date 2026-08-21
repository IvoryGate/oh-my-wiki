---
title: DSP 需求方平台
created: 2026-04-22
updated: 2026-04-22
type: concept
tags: [广告归因, 广告技术]
sources:
  - [[raw/articles/广告竞价背后的逻辑和模型算法（一）.md]]
status: active
---

# DSP 需求方平台

> Demand-Side Platform，管理广告主需求方的平台

## 定义

DSP（Demand-Side Platform）是广告技术栈中的需求方平台，帮助广告主管理和优化广告投放。

## 核心角色

- **Demand 端**：代表广告主利益
- **对接 ADX**：从广告交易所获取流量
- **出价决策**：根据用户特征实时出价

## 工作流程

```
用户设备 → SSP → ADX → DSP（出价） → ADX（竞价） → 展示
```

## 与 ADX 的关系

- ADX 发出广告请求
- DSP 根据用户信息出价
- ADX 汇总所有 DSP 出价，选择最高者

## 相关概念

- [[ADX]]
- [[SSP]]
- [[RTB]]

## 来源

- [[raw/articles/广告竞价背后的逻辑和模型算法（一）.md]]