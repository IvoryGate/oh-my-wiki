# 知识库索引

> 最后更新: 2026-04-17

## 统计概览

| 类型 | 数量 |
|------|------|
| 概念 (concepts) | 2 |
| 实体 (entities) | 1 |
| 数据 (data) | 0 |
| 主题 (topics) | 0 |
| 洞察 (insights) | 0 |
| 指南 (howto) | 0 |
| **总计** | **3** |

---

## Dataview 动态查询

> 安装 [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) 插件后，以下查询会自动更新

### 所有概念 (按更新时间排序)

```dataview
TABLE title as "概念", created as "创建日期", updated as "更新日期"
FROM "wiki/atoms/concepts"
SORT updated DESC
```

### 所有实体 (按更新时间排序)

```dataview
TABLE title as "实体", created as "创建日期", updated as "更新日期"
FROM "wiki/atoms/entities"
SORT updated DESC
```

### 最近更新的页面

```dataview
TABLE title as "标题", type as "类型", updated as "更新日期"
FROM "wiki"
WHERE type
SORT updated DESC
LIMIT 10
```

---

## 原子知识 (atoms)

### 概念 (concepts)

| 概念 | 描述 | 更新日期 |
|------|------|----------|
| [[LLM-Wiki]] | 使用 LLM 构建个人知识库的模式 | 2026-04-17 |
| [[RAG]] | 检索增强生成技术 | 2026-04-17 |

### 实体 (entities)

| 实体 | 描述 | 更新日期 |
|------|------|----------|
| [[Karpathy]] | AI 研究员，LLM Wiki 提出者 | 2026-04-17 |

### 数据 (data)

*暂无内容*

---

## 综合知识 (synthesis)

### 主题 (topics)

*暂无内容*

### 洞察 (insights)

*暂无内容*

### 指南 (howto)

*暂无内容*

---

## 最近更新

> 详细日志见 [[log.md]]

1. [2026-04-17] 入库 [[raw/articles/llm-wiki.md]]，创建 LLM Wiki 相关知识页
