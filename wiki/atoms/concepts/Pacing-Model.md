---
title: Pacing-Model
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 投放, 算法, 预算控制]
sources:
  - [[raw/articles/广告中的Pacing模型以及冷启动.md]]
status: active
---

# Pacing-Model（预算节奏控制）

Pacing 是广告系统中控制投放速度和时间分配的模块，负责在一段时间内平稳均匀地花费预算，同时最大化广告效果。

## 花费曲线规律

所有广告平台（无 fraud），按时区分布，Campaign 花费曲线一定遵守**双波动高峰趋势**——与用户活跃时间一致。

## 三代 Pacing 模型

### 1. 均匀分配法（Uniform Pacing）

将预算按时间均匀分配。简单但缺乏灵活性，高峰期预算不足、低谷期浪费。

### 2. 自适应 Pacing（Adaptive Pacing）

- **基于比例调整**：根据剩余预算和时间动态调整
- **基于历史数据预测**：利用历史 CTR、CVR 预测未来流量

核心是多智能体强化学习（MARL），每个 Campaign 作为一个智能体，通过 DQN（深度 Q 网络）学习状态-动作对：

- **状态空间**：用户特征、广告位特征、市场环境
- **动作空间**：竞价金额（连续/离散）
- **奖励机制**：点击/转化为正向奖励，预算快速耗尽为惩罚

### 3. 竞争感知 Pacing（Competition-based Pacing）

在自适应基础上引入竞争对手出价分析。

### 4. 预测式 Pacing（Predictive Pacing）

使用 ARIMA、LSTM 等时序预测模型预测流量变化，是目前多数 DSP/Ad Network 使用的模型。

## 相关概念

- [[Cold-Start]]
- [[RTB]]
- [[DSP]]
