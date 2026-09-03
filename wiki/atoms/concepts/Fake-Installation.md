---
title: Fake-Installation
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, 出海投放]
sources:
  - [[raw/articles/广告作弊Ad Fraud（二）.md]]
  - [[raw/articles/广告作弊Ad Fraud（一）.md]]
status: active
---

# Fake-Installation（虚假安装）

虚假安装是指安装行为并非由真实用户完成，分为 [[Device-Farm|设备农场]] 和机器人两大类。

## 设备农场进化史

虚拟机 → 刷机/改机 → 设备农场 → 云端设备 → 积分墙 → 混量

| 阶段 | 说明 |
|------|------|
| 虚拟机 | 电脑模拟手机设备 |
| 刷机 | 修改 GAID、IMEI 等设备信息 |
| 改机 | 逆向应用环境参数，伪造协议 |
| 设备农场 | 单个真实设备反复刷量 |
| 云端设备 | 设备农场上云 |
| 积分墙 | 地推/Digital Turbine/Tapjoy 等合规边界模糊 |
| 混量 | 真实流量混合虚假/劫持流量 |

## 机器人

通过恶意代码反编译 MMP/广告平台 SDK，模拟安装行为。常见于开源 SDK，通过 MITM 攻击劫持 SSL 通信。

## 检测方法

### 投放/运营侧

- **货不对板**：投放国家与设备语言不匹配
- **OS Version**：异常低版本或过于集中的设备
- **New Device Rate**：>20% 为危险信号
- **IP/VPN 检验**：MaxMind 等 IP 验证
- **素材维度**：非正常规格素材上报点击/曝光
- **[[Protect360|Appsflyer Rule]]**：自定义黑白名单

### 产品侧

- **风控系统**：时序算法识别非人类行为
- **设备传感器验证**：陀螺仪、亮度、USB 调试等
- **闭源 SDK**：防止反编译
- **CUID 埋点**：绑定安装事件与用户身份

## 相关概念

- [[Device-Farm]]
- [[Attribution-Hijacking]]
- [[Protect360]]
- [[CTIT-Analysis]]
