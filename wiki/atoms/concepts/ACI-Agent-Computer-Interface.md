---
id: aci-agent-computer-interface
title: ACI (Agent-Computer Interface)
aliases:
  - Agent-Computer Interface
  - Agent计算机接口
type: concept
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[你不知道的 Agent：原理、架构与工程实践]]"
tags:
  - AI
  - Agent
  - 工具设计
  - 工程实践
---

## 定义

ACI (Agent-Computer Interface) 是工具设计的一种理念：**工具应对应 Agent 的目标，而不是底层 API 操作**。

## 工具设计演进

### 第一代：API 封装
每个 API Endpoint 对应一个工具，粒度过细，Agent 往往需要协调多个工具才能完成一个目标。

### 第二代：ACI
工具对应目标而非操作。例如：
- ❌ 分别暴露 `create_file`, `write_content`, `set_permissions`
- ✅ 直接给一个 `create_script(path, content, executable)`

### 第三代：Advanced Tool Use

| 方向 | 说明 | 效果 |
|------|------|------|
| **Tool Search** | 动态工具发现，Agent 按需发现工具定义 | 上下文保留率 95%，准确率从 49% → 74% |
| **Programmatic Tool Calling** | 模型用代码编排多个工具调用，中间结果不进入 LLM 上下文 | token 消耗从 150,000 → 2,000 |
| **Tool Use Examples** | 每个工具附带 1-5 个真实调用示例 | 准确率从 72% → 90% |

## ACI 设计三原则

类比 HCI 对人的影响，工具设计对 Agent 的影响一样直接：

1. **参数描述直接约束格式**：不要模糊
2. **错误结构化给出修正建议**：不只是返回字符串
3. **定义和实现绑在一起**：用 Zod 等工具

### 差的工具设计

```typescript
// 差：参数模糊，出错只返回字符串，Agent 不知道怎么修正
const tool = {
  name: "update_yuque_post",
  input_schema: {
    properties: {
      post_id: { type: "string" },
      content: { type: "string" },
    },
  },
};
return "Error: update failed";
```

### 好的工具设计

```typescript
const updateTool = betaZodTool({
  name: "update_yuque_post",
  description: "更新语雀文章内容，不适合创建新文章",
  inputSchema: z.object({
    post_id: z.string().describe("语雀文章 ID，纯数字字符串，如 '12345678'"),
    title: z.string().optional().describe("文章标题，不改时可省略"),
    content_markdown: z.string().describe("Markdown 格式正文"),
  }),
  run: async (input) => {
    const post = await getPost(input.post_id);
    if (!post) throw new ToolError("文章 ID 不存在", {
      error_code: "POST_NOT_FOUND",
      suggestion: "请先调用 list_yuque_posts 获取有效的 post_id",
    });
    return await updatePost(input.post_id, input.title, input.content_markdown);
  },
});
```

## 调试原则

> 调试 Agent 时应先检查工具定义，大多数工具选择错误的原因出在描述不准确，不在模型能力。

## 相关概念

- [[Agent-Loop]]
- [[Context-Engineering]]

## 来源

- [[你不知道的 Agent：原理、架构与工程实践]] §4
