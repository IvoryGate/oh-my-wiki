---
title: "15 第一个 AI Agent"
source: "https://www.runoob.com/ai-agent/first-ai-agent.html"
author:
published:
created: 2026-10-11
description: "15 第一个 AI Agent"
tags:
  - "域/Agent架构与工程"
---
# 第一个 AI Agent

AI Agent 平台种类繁多，但核心目的相同：让模型从回答问题升级为自动执行任务，有的主打零代码拖拽，有的强调工程化定制，也有专门做流程集成或多代理协作。

不同层级的使用场景拆成三个面向：搭建速度、系统衔接、可控深度。

| 核心需求 | 推荐工具 | 关键优势 |
| --- | --- | --- |
| Dumate，桌面级 AI 办公智能体 | [Dumate 官网](https://www.dumate.cn/download?track=1063479t&sub_track=02bI&dutoken=3.s%3A%2F%C2%A5%5EQ9WHho4Mkk%5E%25) | 直接在平台里创建任务，让 AI 编码，在云端开发环境中使用终端、文件管理和预览 |
| MonkeyCode，AI 应用开发平台 | [MonkeyCode 官网](https://monkeycode-ai.com/?ic=019d94af-c5d0-7207-a923-89d7ccf67d91) | 直接在平台里创建任务，让 AI 编码，在云端开发环境中使用终端、文件管理和预览 |
| 小云雀，剪映的 AI 视频生成 | [剪映-小云雀](https://xyq.jianying.com?utm_medium=paidads&utm_source=aitools&utm_campaign=hw_xyq_runoob) | 字节自研 Seedance 2.0 视频模型 + Seedream 5.0 图像模型，搭配豆包大模型做文案理解 |
| 自动化触发与系统对接 | [n8n](https://github.com/n8n-io/n8n) | 集成面广，可自托管，常规内部系统都能打通 |
| 开发者可控的深度定制 | [Dify](https://github.com/langgenius/dify)  / [LangChain](https://github.com/langchain-ai/langchain) | 前者提供完整开源方案；后者适合构建复杂推理链路 |
| 多角色协作与任务分解 | [AutoGen](https://github.com/microsoft/autogen)  / [CrewAI](https://github.com/crewAIInc/crewAI) | 前者强调动态协作；后者以清晰角色体系驱动流程 |

---

## 0 代码进行 Vibe Coding

MonkeyCode 不仅是可以进行 Vibe Coding 的 AI 编程工具，它覆盖了 需求 → 设计 → 开发 → Review 全流程，免费使用，无需安装，内置云端开发环境。

### 注册与登录

**首次使用 MonkeyCode，先完成账号注册。
点击
[进入官网](https://monkeycode-ai.com/?ic=019d94af-c5d0-7207-a923-89d7ccf67d91)
，右上角注册或直接登录，成功后会自动进入主界面开始使用。**

进入页面后，点击右上角 **注册** 创建新账号，已有账号可直接登录使用。

[![](https://www.runoob.com/wp-content/uploads/2026/06/runoob_1782647945371.png)](https://monkeycode-ai.com/?ic=019d94af-c5d0-7207-a923-89d7ccf67d91)

注册成功后，我们进入控制台，输入我们的需求：

```

帮我写一个 JavaScript 小游戏：程序随机生成 1 到 100 的数字，让我猜，猜大了提示「太大了」，猜小了提示「太小了」，猜中了就结束。
```

![](https://www.runoob.com/wp-content/uploads/2026/06/runoob-1_1782648182489.png)

点击执行，并选择模型，国内的很多模型都是免费支持的，这里采用 qwen3.8-flash：

![](https://www.runoob.com/wp-content/uploads/2025/12/runoob_1789519233346.png)

开始任务：

![](https://www.runoob.com/wp-content/uploads/2025/12/runoob_1789519428847.png)

任务完成后可以查看生成的效果地址：

![](https://www.runoob.com/wp-content/uploads/2025/12/runoob_1789519479566.png)

查看效果：

![](https://www.runoob.com/wp-content/uploads/2025/12/runoob_1789519492315.png)

### 切换不同模型

我们也可以切换模型，这样可以比较不同模型生成的效果，**旗舰版还执行 Astra。**

![](https://www.runoob.com/wp-content/uploads/2025/12/runoob_1789519106330.png)

使用不同模型再测试这个应用，左边上角可以切换模型：

![](https://www.runoob.com/wp-content/uploads/2026/04/runoob1_1782649117873.png)

输入以下内容：

```

重新优化整个界面
```

![](https://www.runoob.com/wp-content/uploads/2026/04/runoob2_1782649117873.png)

修改完成后，访问它生成的链接：

![](https://www.runoob.com/wp-content/uploads/2026/04/runoob3_1782649117873.png)

完整效果，好多了：

![](https://www.runoob.com/wp-content/uploads/2026/04/runoob4_1782649117873.png)
