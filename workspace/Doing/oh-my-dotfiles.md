---
title: .dotfiles 秘籍：macOS Shell 环境深度定制
type: note
created: 2026-04-19
updated: 2026-04-19
status: doing
tags: [macOS, dotfiles, 效率工具]
---

# oh-my-dotfiles

## 简介

本文档记录了我在 macOS 上配置通用 dotfiles 的过程和关键点，主要涵盖以下工具的配置：

- **状态栏**: Sketchybar
- **终端美化**: Startship
- **窗口管理器**: Aerospace
- **系统监控**: btop
- **版本控制**: Git
- **Shell**: Fish
- **系统信息**: Neofetch
- **文件管理器**: Yazi
- **终端复用**: Tmux
- **效率工具**: Raycast
- **文本编辑器**: Neovim (with LazyGit integration)
- **模糊搜索**: fzf
- **Git UI**: LazyGit

## 配置目标

*   提高开发效率
*   统一 macOS 环境下的配置
*   实现配置文件的版本控制与同步

## homebrew

> **The Missing Package Manager for macOS (or Linux)**

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## stow

> 在 Linux 系统中，管理配置文件（尤其是 dotfiles）、软件包或多版本工具时，我们常常面临文件散落、版本混乱或重复配置的问题。**GNU Stow**（简称 Stow）是一款轻量级的符号链接（symlink）管理工具，旨在通过创建和维护符号链接，帮助用户将分散的文件组织成模块化结构，实现「一处存储，多处链接」的高效管理。
> 
> Stow 的核心优势在于**简单、无依赖**（仅需 Perl 解释器，几乎所有 Linux 发行版预装）和**可移植性**。它不修改文件内容，仅通过符号链接关联文件，因此非常适合管理 dotfiles、本地编译软件、多版本工具等场景。

**在macos上安装stow**

```shell
brew install stow
```

