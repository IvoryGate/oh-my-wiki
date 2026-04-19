# Oh-My-Wiki

> 个人 AI 知识库：高内聚 · 低耦合 · 领域边界清晰

---

## 核心理念

**知识复利**：每一次学习和探索都在为知识库积累价值，而非消耗完就消失。

**人机协作**：人类负责策展、判断、决策；Agent 负责理解、组织、维护。

**渐进演进**：知识库随时间自然生长，结构持续优化。

---

## 架构设计

```
oh-my-wiki/
│
├── raw/                          # 原始资料（只读）
│   ├── articles/                 # 通用文章（博客、公众号、网页）
│   ├── papers/                   # 学术论文
│   ├── videos/                   # 视频内容
│   ├── podcasts/                 # 播客文稿
│   ├── books/                    # 书籍笔记
│   ├── social/                   # 社交媒体（Twitter/X、微博等）
│   └── manifest.json             # 文件状态索引
│   # 注：可自由添加新子目录，Agent 会自动发现
│
├── wiki/                         # 知识库（Agent 维护）
│   ├── atoms/                    # 原子知识（稳定）
│   │   ├── concepts/             # 概念定义
│   │   ├── entities/             # 实体信息
│   │   └── data/                 # 数据/引用
│   │
│   ├── synthesis/                # 综合知识（活跃）
│   │   ├── topics/               # 主题分析
│   │   ├── insights/             # 个人洞察
│   │   └── howto/                # 方法指南
│   │
│   ├── index.md                  # 内容索引
│   ├── log.md                    # 操作日志
│   └── graph.json                # 知识关系图谱
│
├── workspace/                    # 个人创作
│   ├── Todo/                     # 待办
│   ├── Doing/                    # 进行中
│   └── Done/                     # 已完成 → 流入 wiki
│
└── Agent.md                      # Agent 工作流配置
```

---

## 三层架构

| 层级 | 职责 | 维护者 | 特性 |
|------|------|--------|------|
| **raw** | 原始资料存储 | 人类入库，Agent 索引 | 只读、不可变 |
| **wiki** | 结构化知识 | Agent 维护 | 可更新、交叉引用 |
| **workspace** | 个人创作 | 人类 | 按时间流转 |

---

## 数据流向

```
         人类决策
            │
    ┌───────┼───────┐
    ▼       ▼       ▼
  入库    创作    流入
raw/   workspace  wiki
    │       │       │
    └───────┴───────┘
            │
            ▼
       Agent 编译
    • 理解内容
    • 提取结构
    • 建立关联
    • 维护索引
```

---

## 核心工作流

### Ingest（入库）
将原始资料投入 raw/ → Agent 处理 → 转化为 wiki 中的结构化知识

### Query（查询）
向知识库提问 → Agent 检索相关页面 → 综合回答

### Lint（体检）
定期健康检查 → 发现矛盾、孤立、过时 → 修复或标记

### Flow（流入）
workspace/Done → 人工判断时机 → 流入 wiki

---

## 设计原则

### 高内聚
- atoms 层：每个概念/实体聚焦单一主题
- synthesis 层：每个主题有明确的整合目标

### 低耦合
- 通过 ID（文件名）解耦引用
- 通过 graph.json 追踪依赖关系
- 修改影响范围可控

### 领域边界清晰
- raw：物理边界（来源类型天然互斥）
- wiki：逻辑边界（知识领域 Agent 判断）
- workspace：时间边界（Todo/Doing/Done）

---

## 方法论来源

本知识库体系融合了两个方法论来源：

1. **ZeromaX 訸**（B站 UP 主）
   - 《从离散数学角度思考笔记、代码架构》
   - 核心思想：图论 + 集合论视角的组织方法论

2. **Andrej Karpathy**
   - [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
   - 核心思想：编译器模式的知识管理

---

## 快速开始

### 入库新资料
```bash
# 将资料放入对应目录
cp article.md raw/articles/
# 唤起 Agent 处理
# Agent 会自动：理解 → 讨论 → 写入 wiki → Git commit
```

### 查询知识
```
直接向 Agent 提问，Agent 会：
1. 检索 wiki/index.md
2. 定位相关页面
3. 综合回答
```

### 个人创作
```
1. 在 workspace/Todo/ 创建想法
2. 移动到 workspace/Doing/ 开始工作
3. 完成后移动到 workspace/Done/
4. 判断时机成熟后，让 Agent 流入 wiki
```

---

## Obsidian 插件支持

### Dataview（动态查询）

安装 [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) 插件后：

- `wiki/index.md` 中的查询会自动更新
- 无需手动维护统计数据
- 可自定义查询模板（见 `wiki/templates/dataview-queries.md`）

### Marp（幻灯片生成）

安装 [Marp](https://marp.app/) 插件后：

- 可将 wiki 内容转换为演示文稿
- Agent 支持生成 Marp 格式输出
- 模板见 `wiki/templates/marp-template.md`

### Graph View（知识图谱）

Obsidian 内置功能：

- 双向链接 `[[概念名]]` 自动出现在图谱
- Agent 维护 `graph.json` 确保关系准确
- 可视化知识关联

---

## 版本管理

本知识库使用 Git 进行版本管理：

- Agent 负责本地 commit
- 用户决定何时 push 到远程
- 支持回滚和变更追踪

---

## 用户与 Agent 边界

> 详细说明见 [[BOUNDARY.md]]

### 简单理解

| 你负责 | Agent 负责 |
|--------|-----------|
| 决定学什么 | 理解内容 |
| 策展资料 | 提取结构 |
| 个人创作 | 维护 wiki |
| 最终决策 | 执行细节 |

### 你可以直接做什么

- ✅ 直接编辑 `workspace/`（你的创作空间）
- ✅ 直接放入资料到 `raw/`（入库新内容）
- ✅ 直接修改 wiki 中的错别字、标签（小改动）

### 你需要让 Agent 做什么

- 🔄 `raw/` → `wiki/`：说"入库这个资料"
- 🔄 `workspace/Done` → `wiki/`：说"可以流入 wiki 了"
- 🔍 查询知识：直接提问
- 📊 维护结构：让 Agent 创建/删除 wiki 页面

### 典型对话

```
你：我剪藏了一篇文章到 raw/articles/，帮我入库
Agent：[读取] [讨论] [确认] [创建页面] [commit]

你：workspace/Done 里的学习笔记可以流入 wiki 了
Agent：[读取] [讨论] [确认] [创建页面] [清理] [commit]

你：知识库里有哪些关于 AI 的内容？
Agent：[检索] [回答]
```

---

## 为新 Agent 准备

当需要让新的 LLM 理解这个知识库时：

### 快速开始

1. **发送 Prompt**：复制 `PROMPT.md` 中的内容给新 LLM
2. **附加文件**：附加 `CONTEXT.md` 和 `Agent.md`
3. **确认理解**：让 Agent 简要说明它理解的知识库结构

### 文档说明

| 文档 | 用途 | 给谁看 |
|------|------|--------|
| `CONTEXT.md` | 知识库概览，核心概念 | 新 Agent 首先阅读 |
| `Agent.md` | 详细工作流和规范 | Agent 工作时参考 |
| `PROMPT.md` | 快速启动指南 | 用户参考 |
| `.cursorrules` | IDE 配置 | Cursor 等 IDE |

### 针对不同工具

| 工具 | 建议方式 |
|------|----------|
| Claude Code | 自动读取 Agent.md |
| ChatGPT | 附加 CONTEXT.md + Agent.md |
| Cursor | 自动读取 .cursorrules |
| 其他 | 发送 PROMPT.md 内容 |

---

## 未来扩展

- [ ] 接入 qmd 本地搜索引擎
- [ ] 向量检索支持
- [ ] 多人协作支持

---

*构建时间: 2026-04-17*
