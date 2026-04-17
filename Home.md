---
created: 2026-04-17
type: homepage
---

# OH-MY-WIKI

> 知识复利，日积月累

## 知识贡献

```contributionGraph
title: 知识贡献图
graphType: default
dateRangeValue: 365
dateRangeType: LAST_DAYS
startOfWeek: 1
showCellRuleIndicators: true
showTitle: false
dataSource:
   type: PAGE
   value: 'wiki'
   dateField:
     type: FILE_MTIME
fixedScaleSize: 1.5
fillTheScreen: true
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
