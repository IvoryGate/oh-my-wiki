---
title: "广告作弊Ad Fraud（五）"
source: "https://mp.weixin.qq.com/s/A3-I-rFIW2HAuCx_FKThwg"
author:
  - "[[SimoneLee]]"
published:
created: 2026-09-04
description: "Adjust和Singular的防作弊方案"
tags:
  - "clippings"
---
SimoneLee 出海流量研究僧 *2025年2月17日 10:30*

Hello，大家好。

我是目前研究出海投放&变现业务的SL。

这篇文章非常简单地聊一下Adjust以及Singular以及他们提供的解决方案，其实各家MMP的方案基本大同小异。

Adjust

Adjust根据我的理解，提供如下两层验证方案：一类是基础验证。一类是高阶验证。

基础验证（1）IP过滤（from MaxMind）

- RI AIP （Rejected Install Anonymous IP）
- RR AIP（Rejected Reattribution Anonymous IP）

\*RI代表NUA；RR代表再营销。

基础验证（2）Device ID验证

- Rejected Install Malformed Advertising Id

\*验证Advertising Id格式，如GAID、IDFA，独有。

高阶验证（1）分布模型（Distribution Model）

- Rejected Installs Too Many Engagements (RI TME) 类比聚类
- Rejected Installs Distribution Outlier (RI DO) 类比CTIT
- Rejected Reattributions Too Many Engagements (RR TME) 类比聚类
- Rejected Reattributions Distribution Outlier (RR DO) 类比CTIT

\*主防虚假安装。

高阶验证（2）点击过滤（click filter）

- Rejected Install Click Injection (RI CI)
- Rejected Reattribution Click Injection (RR CI)

\*主防归因劫持。

Singular

Fake Installs Protection Methods 基础验证

Attribution Manipulation Protection Methods高阶验证

- TTI Outliers Detection类比CTIT
- Geo-Bleed Detection点击与安装上报之间的物理距离验证
- Hyper-Engagement类比聚类

\*验证物理距离，独有。

General Protection Methods IP验证

好了，今天的内容就到这里。

Bye!

关注我，获取更多广告投放变现知识！

防作弊 · 目录