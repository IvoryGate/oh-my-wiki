---
created: 2026-04-17
updated: 2026-07-29
type: homepage
tags: [home, dashboard]
---

# OH-MY-WIKI

> 知识复利，日积月累

## 状态总览

| 统计 | 数量 | 活跃领域 |
|------|------|----------|
| 概念 | 125 | 机器学习(58) · 广告归因(22) · Agent工程(15) |
| 实体 | 6 | 软件工程(6) · 复盘(6) · 知识管理(6) |
| **总计** | **131** | 媒介理论(5) · 技术写作(5) |

## 正在进行

| 文章 | 标签 |
|------|------|
| [[workspace/Doing/VPN-机场-代理-梯子.md\|VPN、机场、代理、梯子]] | vpn, proxy, network |
| [[workspace/Doing/终端实用效率指南.md\|终端实用效率指南]] | terminal, cli, 效率 |
| [[workspace/Doing/增长系数预测.md\|增长系数预测]] | 增长, 广告, boosting |
| [[workspace/Doing/ffmpeg视频剪辑入门.md\|FFmpeg 视频剪辑入门]] | ffmpeg, 视频剪辑 |
| [[workspace/Doing/如何构建知识体系.md\|如何构建知识体系]] | 知识管理, 学习方法 |

## 快速导航

**Agent工程** · **软件工程** · **增长与营销** · **复盘与方法论** · **媒介理论** · **机器学习** · **写作与技术博客** · **知识管理**

---

## 知识贡献

```contributionGraph
graphType: default
days: 365
startOfWeek: 1
fillTheScreen: false
cellStyle:
  borderRadius: ""
  minWidth: 12px
  minHeight: 12px
fixedScaleSize: 1
dataSource:
  type: PAGE
  value: '"wiki" or "workspace"'
  dateField:
    type: FILE_MTIME
dateRangeType: LATEST_DAYS
dateRangeValue: 365
titleStyle:
  fontSize: 16px
cellStyleRules: []
enableMainContainerShadow: true
showCellRuleIndicators: true
```

## 最近更新

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "页面",
  type as "类型",
  updated as "时间"
FROM "wiki"
WHERE type
SORT updated DESC
LIMIT 10
```
