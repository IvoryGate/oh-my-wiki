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

## [2026-04-18 15:30] ingest | 增长营销系列文章
- 来源: erickfang《出海增长浅谈》系列
- 来源文章:
  - [[raw/articles/关于归因你可能不知道的那些事(一）.md]]
  - [[raw/articles/关于归因你可能不知道的那些事（二）-Skan篇.md]]
  - [[raw/articles/关于归因你可能不知道的那些事（三）-策略篇.md]]
  - [[raw/articles/增长从确定目标开始.md]]
  - [[raw/articles/如何定义受众-正篇.md]]
  - [[raw/articles/如何定义受众-科普篇.md]]
  - [[raw/articles/渠道不起量的原因都在这里了！.md]]
- 创建概念页:
  - [[MMP-Attribution]] - 第三方归因解决方案
  - [[SKAN-Attribution]] - Apple 官方归因体系
  - [[Last-Click-Rule]] - 广告归因核心规则
  - [[Duplicate-Attribution]] - 重复计费问题
  - [[Attribution-Gap]] - MMP 与大媒体归因差异
  - [[User-App-Pair]] - 用户覆盖模型
  - [[Audience-Definition]] - 受众定义三问
  - [[High-Value-Channel]] - 高价值渠道识别
  - [[Channel-Launch-Strategy]] - 渠道起量六要素
  - [[Network-Cognition-Gap]] - 渠道能力差异
- 创建实体页:
  - [[erickfang]] - 出海增长专家
- 建立知识链接 10 条
- 更新 graph.json: 节点 31 个，边 26 条

## [2026-04-18 11:30] update | 知识库架构升级
- 添加 `workplace/topics/` 目录用于新话题积累
- 创建话题追踪模板: [[wiki/templates/topic-tracker.md]]
- 创建综合知识模板: [[wiki/templates/synthesis-template.md]]
- 更新 Agent.md: 添加知识沉淀规则、更新机制
- 更新 wiki/index.md: 反映新的知识流转规则

**核心变更**：
1. **两条沉淀路径**：
   - 单篇: `Done/` → `wiki/synthesis/howto` 或 `insights`
   - 系列: `topics/` → `wiki/synthesis/topics`
2. **更新机制**：已有内容直接在 `wiki/synthesis/` 更新，不回流
3. **状态标记**：`status: stable|evolving|outdated` + 变更日志

## [2026-04-18 10:50] ingest | Agent 工程实践文章
- 来源: [[raw/articles/你不知道的 Agent：原理、架构与工程实践.md]]
- 来源: [[raw/articles/工程技术：在智能体优先的世界中利用 Codex.md]]
- 创建概念页:
  - [[Agent-Loop]] - Agent 核心循环模式
  - [[Workflow-vs-Agent]] - 工作流与智能体区分
  - [[Agent-Control-Patterns]] - 五种控制模式
  - [[Harness-Engineering]] - 验收基础设施
  - [[Context-Engineering]] - 上下文工程
  - [[Skills-System]] - Skills 按需加载系统
  - [[ACI]] - Agent-Computer Interface
  - [[Memory-System]] - 记忆系统
  - [[Multi-Agent-Organization]] - 多 Agent 组织
  - [[Agent-Evaluation]] - Agent 评测
  - [[Agent-Tracing]] - Agent 追踪
  - [[Long-Task-Management]] - 长任务管理
  - [[Agent-First-Development]] - 智能体优先开发
  - [[Architecture-Constraints]] - 架构约束
  - [[Progressive-Disclosure]] - 渐进式披露
- 创建实体页:
  - [[Codex]] - OpenAI 代码生成智能体
  - [[OpenAI]] - OpenAI 公司
- 建立知识链接 16 条
- 更新 graph.json: 节点 20 个，边 16 条

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
