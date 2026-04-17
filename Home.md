---
created: 2026-04-17
type: homepage
---

# OH-MY-WIKI

> 知识复利，日积月累

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
