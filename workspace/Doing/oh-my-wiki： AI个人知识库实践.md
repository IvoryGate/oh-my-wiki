---h
title: oh-my-wiki：我的 AI 辅助知识管理实践
type: draft
category: insight
created: 2026-04-19
updated: 2026-04-19
ajtatus: doing
tags: [知识管理, AI, LLM, 个人效率]
related:
  - [[LLM-Wiki]]
  - [[RAG]]
  - [[Progressive-Disclosure]]
---

# oh-my-wiki： AI个人知识库实践

> Oh-my-wiki 是一场将个人知识库“代码化“的实验：通过 Agent 将原始资料自动编译为持续增量的结构化共识，让 AI 负责繁琐的维护，人类专注深度的创作。
> oh-my-wiki 不是一堆随意躺在硬盘中的文件夹和文件的集合，而是一个有源码、有构建产物、有检查，有合并策略的文档工程。


## 写在前面的话

传统的RAG知识库

我个人不是很认同使用RAG做知识库的方式，RAG的检索太粗暴，

我更倾向于通过语义的方式进行检索

## 设计理念

我希望这个知识库，既有ai驱动的部分，又能有一个给笔者自由创作的舞台，因此在第一层划分出了三个纬度：raw、wiki、workspace。

其中raw是经过甄别的高质量的原始数据，wiki是经过编译形成的数据网络，workspace是交由你自由创作的空间，除了在你明确要求的情况下，agent在其他任何时候都不该侵入该空间。

## 注意事项

无论是在做数据分析，还是做个人知识库这种数据驱动的内容。对于源数据的质量都有较高的要求。因此，对于本项目中的/raw目录中的内容，应当是基于你的认知判断过的具有价值的内容，再往里面放。

## 数据流向

使用者通过obsidian-web-clipper插件或者别的任何方式，提取文本内容放入/raw目录中，交给agent对原始知识进行“编译”，转化成concept，entity等原子内容，构建整个知识库的地基，

## 总结

简单来说，raw是源码，wiki是构建产物，workspace是特性分支。
