# 操作日志

> 记录知识库的所有变更历史

---

## 日志格式

```
## [YYYY-MM-DD HH:MM] 类型 | 对象
- 操作描述
- 相关页面: [[xxx]]
```

**操作类型**：
- `ingest`: 处理原始资料
- `query`: 知识查询归档
- `lint`: 健康检查修复
- `flow`: workplace 流入 wiki
- `create`: 直接创建内容
- `update`: 更新内容

---

## 2026年4月

## [2026-04-17 23:20] create | .gitignore
- 创建 .gitignore 文件
- 忽略 Obsidian 个人偏好配置（workspace.json, data.json）
- 保留共享配置（app.json, community-plugins.json, manifest.json）
- 忽略系统文件、临时文件、导出文件

## [2026-04-17 23:15] create | Agent 入门文档
- 创建 CONTEXT.md: 新 Agent 快速理解知识库
- 创建 PROMPT.md: 快速启动指南
- 创建 .cursorrules: Cursor IDE 配置
- 更新 README.md: 添加"为新 Agent 准备"章节

## [2026-04-17 23:00] update | Obsidian 插件配置
- 配置 Homepage: 启动打开 wiki/index.md
- 配置 Dataview: 启用内联查询和 JavaScript
- 配置 Marp Slides: 16:9 尺寸，默认主题
- 创建 CSS 片段: oh-my-wiki.css（表格美化、链接增强）
- 创建插件配置指南: [[wiki/templates/plugin-config.md]]

## [2026-04-17 22:50] create | 知识库扩展
- 添加 raw/social/ 目录支持社交媒体内容
- 创建 Dataview 查询模板: [[wiki/templates/dataview-queries.md]]
- 创建 Marp 幻灯片模板: [[wiki/templates/marp-template.md]]
- 更新 Agent.md: 添加插件集成规则和 Frontmatter 规范

## [2026-04-17 22:40] ingest | llm-wiki.md
- 来源: [[raw/articles/llm-wiki.md]]
- 创建概念页: [[LLM-Wiki]], [[RAG]]
- 创建实体页: [[Karpathy]]
- 建立关系: LLM-Wiki --proposed_by--> Karpathy
- 建立关系: LLM-Wiki --compares_to--> RAG

## [2026-04-17 22:30] create | 知识库初始化
- 创建目录结构
- 创建 manifest.json 和 graph.json
- 编写 Agent.md 和 README.md
- 创建 index.md 和 log.md
