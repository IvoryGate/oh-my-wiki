---
name: Gen Graph
description: 从 wiki 页面链接重建 wiki/graph.json 知识图谱。当新增/删除/合并页面后需要同步图谱、或校验 graph.json 是否与实际链接一致时使用。
---

# Gen Graph

## 原则

- `wiki/graph.json` 是**派生件**：nodes、edges、stats 全部从页面 frontmatter 与 `[[链接]]` 推导，**禁止手工编辑**。
- `wiki/graph.relations.json` 是**判断件（语义策展层）**：人工/Agent 维护的 relation 标注（proposed_by、requires 等），脚本生成时与链接合并，同 `(from, to)` 时此文件优先。
- Obsidian Graph View 直接从链接渲染，不读 graph.json；graph.json 的价值是语义 relation 标注与外部程序消费。

## Workflow

1. 校验一致性（不写入，不一致退出码 1）：

   ```bash
   python .opencode/skills/gen-graph/scripts/gen_graph.py --check
   ```

2. 页面有增删改（新页、删除、合并）后重建：

   ```bash
   python .opencode/skills/gen-graph/scripts/gen_graph.py
   ```

3. 新增语义关系时编辑 `wiki/graph.relations.json` 的 `relations` 数组，格式：
   `{ "from": "页面名", "to": "页面名", "relation": "语义", "context": "" }`；
   端点页面被删除后该条会自动失效（生成时跳过并告警），可顺手清理。

4. 操作完成后将结果追加到 `wiki/log.txt`。

## 边的语义

| 来源 | relation | 说明 |
|------|----------|------|
| 页面 `[[链接]]` | `links_to` | 默认基础边，脚本自动推导 |
| `graph.relations.json` | 自定义 | 策展语义，覆盖同名链接边 |
