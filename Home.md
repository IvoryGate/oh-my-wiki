---
created: 2026-04-17
type: homepage
---

# <center>🎮 OH-MY-WIKI</center>

<center>

> *"知识复利，日积月累"*

</center>

---

## <center>📊 知识图谱热力图</center>

<center>

` ```heatmap `

` ` `

</center>

> 💡 **使用说明**：Heatmap Tracker 会在后台自动追踪 `wiki/` 和 `workplace/` 文件夹中的文件创建和修改记录，生成类似 GitHub 贡献图的热力图。请在 Obsidian 中使用命令面板执行 "Heatmap Tracker: Open View" 来查看你的知识贡献热力图。

---

<center>

| 📚 **概念** | 👤 **实体** | 📝 **主题** | 💡 **洞察** |
|:---:|:---:|:---:|:---:|
| 2 | 1 | 0 | 0 |

</center>

---

## 🚀 快速导航

<table>
<tr>
<td width="50%">

### 📥 入库新资料

```bash
raw/articles/     # 文章
raw/videos/       # 视频
raw/social/       # 社交媒体
```

</td>
<td width="50%">

### 📤 最近更新

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "页面",
  type as "类型",
  updated as "时间"
FROM "wiki"
WHERE type
SORT updated DESC
LIMIT 5
```

</td>
</tr>
</table>

---

## 📈 知识成长追踪

### 按类型统计

```dataview
TABLE WITHOUT ID
  type as "类型",
  length(rows) as "数量"
FROM "wiki"
WHERE type
GROUP BY type
SORT length(rows) DESC
```

### 活跃概念

```dataview
TABLE WITHOUT ID
  link(file.link, title) as "概念",
  length(sources) as "来源数",
  updated as "更新"
FROM "wiki/atoms/concepts"
SORT length(sources) DESC
LIMIT 5
```

---

## 🎯 今日目标

- [ ] 入库一篇新资料
- [ ] 学习一个新概念
- [ ] 完善一个知识页面
- [ ] Git push 今日成果

---

## 🕐 时间线

```dataview
TABLE WITHOUT ID
  updated as "日期",
  choice(
    type = "concept", "💡 概念",
    type = "entity", "👤 实体",
    type = "topic", "🎯 主题",
    type = "insight", "💭 洞察",
    type = "howto", "📖 指南",
    "📄 其他"
  ) as "类型",
  link(file.link, title) as "内容"
FROM "wiki"
WHERE type
SORT updated DESC
LIMIT 10
```

---

## 📊 知识库健康度

| 指标 | 状态 | 说明 |
|------|:---:|------|
| 孤立页面 | ✅ | 无孤立内容 |
| 矛盾检测 | ✅ | 无冲突描述 |
| 链接完整 | ✅ | 双向链接正常 |
| 索引同步 | ✅ | graph.json 已更新 |

---

## 🎨 今日灵感

> *"维护知识库最累的不是阅读和思考，而是记账。读文章、判断价值、决定方向 — 这些是人该干的事。整理格式、更新链接、维护索引 — 这些 bookkeeping 的活，交给 AI 干最合适。"* — **Karpathy**

---

## 🔗 外部链接

| 资源 | 链接 |
|------|------|
| 方法论来源 | [LLM Wiki by Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) |
| 架构思想 | [ZeromaX訸 - 离散数学视角](https://www.bilibili.com/video/BV1ju6QBzENE) |
| Obsidian | [官网](https://obsidian.md) |

---

<center>

**Made with ❤️ by Human + AI**

*最后更新: 2026-04-17*

</center>
