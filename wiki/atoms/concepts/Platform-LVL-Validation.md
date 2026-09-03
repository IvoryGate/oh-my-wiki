---
title: Platform-LVL-Validation
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [广告, 反作弊, Google, Apple, Amazon]
sources:
  - [[raw/articles/广告作弊Ad Fraud（六）.md]]
status: active
---

# Platform-LVL-Validation（应用商店验证防作弊）

各应用商店平台提供的安装来源与合法性验证机制，用于防止盗版、伪造安装和未经授权的运行。

## Google License Verification Library (LVL)

验证应用合法授权，防止未授权安装。

**安全机制：**
- 响应数据签名（Google 私钥加密，本地公钥验证）
- 随机化验证请求（nonce 防重放攻击）
- 响应内容混淆（Base64 + 混淆）
- 代码混淆（ProGuard/R8）

需配合 Google Play Integrity API 进行更严格检查。AppsFlyer 中标记为 Bots 类型。

## Apple App Store Install Validation

苹果利用自身生态完成验证，无需 SDK。

**三个环节：**
1. **Receipt Validation**：验证应用来源和合法性（设备 ID、Bundle ID 等）
2. **App Store Server API**：检测安装来源，防假安装和内购欺诈
3. **Device Integrity Checks**：检查越狱、模拟器、Hook

## Amazon DRM API

通过 Appstore SDK 的 DRM API 验证应用合法性。

**安全机制：**
- 服务器签名验证
- **设备绑定 & 账户验证**（独有）：授权与 Amazon 账户绑定
- 授权数据加密 & 反篡改

## 相关概念

- [[Ad-Fraud]]
- [[Protect360]]
- [[Fake-Installation]]
