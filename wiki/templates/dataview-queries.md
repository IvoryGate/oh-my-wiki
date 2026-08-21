# Dataview 查询模板

> 本页面收集常用的 Dataview 查询，方便复制使用

---

## 基础查询

### 按类型列出所有页面

```dataview
TABLE title as "标题", type as "类型", created as "创建日期"
FROM "wiki"
WHERE type
SORT type, created DESC
```

### 按标签筛选

```dataview
LIST
FROM "wiki"
WHERE contains(tags, "AI")
SORT updated DESC
```

### 按来源追溯

```dataview
TABLE title as "标题", type as "类型"
FROM "wiki"
WHERE contains(sources, [[raw/articles/llm-wiki.md]])
SORT updated DESC
```

---

## 统计查询

### 每种类型的数量

```dataview
TABLE length(rows) as "数量"
FROM "wiki"
WHERE type
GROUP BY type
```

### 每月创建的页面数

```dataview
TABLE length(rows) as "数量"
FROM "wiki"
WHERE type
GROUP BY created
```

---

## 维护查询

### 孤立页面（无入链）

```dataview
LIST
FROM "wiki"
WHERE type AND !file.inlinks
```

### 最近 7 天更新

```dataview
TABLE title as "标题", type as "类型", updated as "更新日期"
FROM "wiki"
WHERE type AND updated >= date(today) - dur(7 days)
SORT updated DESC
```

### 待处理状态

```dataview
TABLE title as "标题", type as "类型", status as "状态"
FROM "wiki"
WHERE status = "draft"
SORT updated DESC
```

---

## 高级查询

### 知识图谱：某个概念的所有关联

```dataview
LIST
FROM "wiki"
WHERE contains(file.outlinks, [[LLM-Wiki]]) OR contains(file.inlinks, [[LLM-Wiki]])
```

### 按领域聚合

```dataview
TABLE rows.title as "页面"
FROM "wiki"
WHERE type
GROUP BY type
```

---

## 自定义查询示例

### 创建演示幻灯片素材

```dataview
TABLE title as "概念", file.link as "链接"
FROM "wiki/atoms/concepts"
SORT title
```

> 将结果复制到 Marp 幻灯片中使用

---

## 使用说明

1. 安装 [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) 插件
2. 启用 Dataview 的 JavaScript 查询（可选）
3. 将 `dataview` 代码块复制到任意页面即可生效

### 查询语法速查

| 语法 | 用途 |
|------|------|
| `TABLE` | 表格输出 |
| `LIST` | 列表输出 |
| `FROM "path"` | 指定目录 |
| `WHERE condition` | 过滤条件 |
| `SORT field DESC` | 排序 |
| `GROUP BY field` | 分组 |
| `LIMIT n` | 限制数量 |
