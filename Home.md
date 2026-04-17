---
created: 2026-04-17
type: homepage
---

# OH-MY-WIKI

> 知识复利，日积月累

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
  value: '"wiki" or "workplace"'
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
