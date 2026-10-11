---
title: "MCP"
created: 2026-10-11
updated: 2026-10-11
type: concept
domain: Agent 架构与工程
description: 标准化连接模型与工具数据源的开放协议。
tags: [域/Agent架构与工程]
sources:
  - [[raw/columns/菜鸟教程AI智能体/44 AI Agent 工具与外部集成.md]]
status: active
---

# MCP

## 核心定义

MCP（Model Context Protocol，模型上下文协议）是一种开放标准协议，用于标准化 AI 应用与外部工具、资源和服务之间的连接方式。它的设计目标是成为 AI 领域的"USB 接口"，让不同的 Agent 和工具能够安全地互操作。

## 协议动机

在 MCP 出现之前，每个 AI 应用接入外部能力往往需要单独编写集成代码。MCP 的核心设计理念有三条：

- **标准化：**统一的协议格式，不同的 Agent 和工具可以互操作。
- **安全性：**明确的权限控制，Agent 只能访问授权的资源。
- **可扩展性：**易于添加新的工具和数据源。

通过 MCP，开发者可以将文件系统、数据库、搜索服务等能力以统一的协议接口提供给支持 MCP 的应用，例如一个数据库 MCP Server 可以向 AI 应用提供受控的查询工具。

## Client/Server 结构

MCP 采用客户端与服务器协作的架构，主要包含三种角色：

- **MCP Host：**运行 AI 应用的宿主环境，如 Claude Desktop、AI 编码助手等，负责协调连接与交互。
- **MCP Client：**在 Host 中建立并维护与 MCP Server 的连接，与 Server 保持 1:1 连接。
- **MCP Server：**向客户端提供工具、资源或提示模板等能力的服务端程序。

通信流程分四步：连接建立（Client 与 Server 交换能力信息）→ 工具发现（Client 查询 Server 提供哪些工具和资源）→ 工具调用（Client 发送请求，Server 执行并返回结果）→ 资源访问（Client 读写 Server 提供的资源）。

## Server 实现

MCP Server 的实现围绕两个核心环节：声明可用工具，以及响应工具调用。

- 声明阶段：Server 列出工具清单，每个工具包含名称、功能描述和参数模式（inputSchema），供 Client 发现。
- 调用阶段：Client 发送工具调用请求，Server 校验参数后执行实际逻辑（如读写文件、查询数据库），再把结果返回给 Client。

教程中的示例用官方 SDK 构建了一个文件系统 Server，注册 read_file、write_file、list_directory 三个工具并通过标准输入输出运行——具体代码见来源文，此处不复述。

## 与工具调用的关系

MCP 不是 Tool Calling（工具调用）的替代品，两者解决的问题不同：

- **Tool Calling：**侧重模型如何选择工具并生成调用参数，是模型与外部执行系统之间的协作机制。
- **MCP：**侧重外部工具和数据能力如何以标准化方式提供给 AI 应用。

也就是说，Tool Calling 回答"模型怎么发起调用"，MCP 回答"工具怎么被统一接入"。开发者也可以直接通过普通函数或 HTTP API 实现工具调用，并不一定需要使用 MCP；在 Agent 的五层架构中，MCP 与 Tool Calling、API、Database 同属工具层（能力扩展层）。

## 参考

- [[AI Agent]]
- [[ACI-Agent-Computer-Interface]]
- [[Skills-System]]

## 来源

- [[raw/columns/菜鸟教程AI智能体/44 AI Agent 工具与外部集成.md]]
