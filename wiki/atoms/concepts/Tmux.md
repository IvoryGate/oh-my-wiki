---
title: "Tmux"
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [开发工具]
sources:
  - "[[raw/articles/Linux tmux 基础使用教程.md]]"
status: active
---

## 概念

**Tmux** (Terminal Multiplexer) 是一个开源的终端复用器，它允许用户在单个终端窗口中创建、管理和操作多个独立的终端会话、窗口和窗格。它是 `screen` 命令的现代替代品，特别适用于需要在 SSH 连接断开后仍保持程序运行的需求。

## 核心架构：四层结构

Tmux 的管理是分层的，从上到下依次为：

1.  **Server (服务器)**: Tmux 运行的底层环境，可以管理多个 Session。
2.  **Session (会话)**: 一个独立的终端环境，可以跨越 SSH 连接的断开而保持运行。一个 Session 可以包含多个 Window。
3.  **Window (窗口)**: 类似于浏览器的标签页，一个 Session 中可以打开多个 Window，每个 Window 占据一个完整的终端屏幕。
4.  **Pane (窗格)**: 一个 Window 可以被分割成多个 Pane，每个 Pane 是一个独立的终端实例，可以在其中运行程序。

这种层级结构可以用以下图示表示：

![Tmux 架构图](https://assets.zouht.com/img/blog/3846-01.webp)

## 主要功能与快捷键

Tmux 的操作都通过 `Prefix` 快捷键（默认为 `Ctrl + B`）触发，之后再按具体指令。

### Session 管理

*   **新建 Session**:
    *   `tmux` 或 `tmux new`: 创建默认命名的 Session (0, 1, 2, ...)。
    *   `tmux new -s [名称]`: 创建自定义名称的 Session。
*   **脱离 Session (Detach)**: `Prefix + D`
    *   允许用户断开 SSH 连接后，Session 及其内运行的程序仍保持运行。
*   **列出 Sessions**: `tmux list-sessions`
*   **连接 Session (Attach)**:
    *   `tmux attach`: 连接最近使用的 Session。
    *   `tmux attach -t [名称]`: 连接指定名称的 Session。
*   **关闭 Session**:
    *   在 Session 内: `exit`
    *   关闭除当前 Session 外的所有 Session: `tmux kill-session -a`
    *   关闭指定 Session: `tmux kill-session -t [名称]`
    *   强制关闭所有 Session: `tmux kill-server` (不推荐)

### Window 管理

*   **新建 Window**: `Prefix + C`
*   **切换 Window**:
    *   `Prefix + P`: 上一个 Window。
    *   `Prefix + N`: 下一个 Window。
    *   `Prefix + [数字]`: 切换到指定编号的 Window。
    *   `Prefix + W`: 列表式切换 Window。
*   **关闭 Window**: `Prefix + Ctrl + &` (需确认)

### Pane 管理

*   **切分 Pane**:
    *   `Prefix + %`: 竖直切分。
    *   `Prefix + "`: 水平切分。
*   **切换 Pane**: `Prefix + 方向键` (绿色边框指示当前激活 Pane)。
*   **调整 Pane 大小**:
    *   `Prefix + Ctrl + 方向键`: 微调。
    *   `Prefix + Alt + 方向键`: 大幅度调整。
*   **关闭 Pane**: `Prefix + Ctrl + X` (需确认)

### 其他

*   **滚动历史记录**: `Prefix + [` 进入滚动模式，按 `q` 退出。
*   **启用鼠标支持**: 在 `~/.tmux.conf` 文件中添加 `set -g mouse on`。开启后支持鼠标拖动调整 Pane 大小、点击切换 Pane/Window 等。

## 来源

*   [[raw/articles/Linux tmux 基础使用教程.md]]
