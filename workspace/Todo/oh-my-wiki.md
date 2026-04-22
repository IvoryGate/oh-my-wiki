# oh-my-wiki

> oh-my-wiki 不是一堆随意躺在硬盘中的文件夹和文件的集合，而是一个有源码、有构建产物、有检查，有合并策略的文档工程。

## 为什么要建立这样的知识库

最近看到网上很火的Karpathy的llm-wiki理论。

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

对于第一层，划分为raw/、wiki/、workspace/三个部分，其中raw/是
