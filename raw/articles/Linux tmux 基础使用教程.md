---
title: "Linux tmux 基础使用教程"
source: "https://www.zouht.com/3846.html"
author:
published:
created: 2026-04-19
description: "如果你有断开 ssh 仍保持程序运行的需求，大概率听说过 screen 这个命令。但作为一个 37 岁的老程序，它确…"
tags:
  - "clippings"
---
如果你有断开 ssh 仍保持程序运行的需求，大概率听说过 screen 这个命令。但作为一个 37 岁的老程序，它确实有点老了，本篇文章的内容便是它的现代替代 —— tmux 的基础使用教程。

当然，因为我自己主要使用 Windows 开发，只是有时需要在 Linux 服务器上进行运维 / 运行代码。因此这篇文章的深度和广度相比网上大神的长篇大论肯定是差很多的，但是如果你和我的需求差不多，我觉得这个程度的学习已经很够用了。

## 1 基础概念

tmux 对窗口的管理是分层的，从上到下可以分为：Server, Session, Window, Pane.

- Server (服务器): 就是运行 tmux 的服务器，一个服务器可以运行多个会话.
- Session (会话): 一个会话将会占满一整个终端屏幕，一个会话可以打开多个窗口.
- Window (窗口): 一个窗口将会完整显示在会话屏幕上，但一个窗口可以分为多个窗格.
- Pane (窗格): 每个窗格都是一个可以交互的终端，可以独立运行程序。

上述层级结构用图来表示如下所示：

![https://assets.zouht.com/img/blog/3846-01.webp](https://assets.zouht.com/img/blog/3846-01.webp)

接下来我们会逐层来讲解它们的用法。

## 2 Session 会话

Session 是独立存在，互不影响的。一个 Session 启动后，里面运行的程序不会随用户断开 ssh 而关闭，只会因为 Session 关闭而关闭。

同时，一个 Session 创建后，环境变量、当前目录等状态是独立的，一个 Session 就好似一个真实的 ssh 连接，拥有完整且独立的环境。

## 2.1 新建 Session

要使用 tmux，第一件事就是创建一个新的 Session，新建方式如下：

- `tmux` ：创建一个默认名称的 Session，名称会依次命名为 0, 1, 2, …
- `tmux new` ：同上
- `tmux new -s [名称]` ：创建一个自定义名称的 Session.

例如用 `tmux new -s demo-session` 创建一个新 Session，效果如下：

![https://assets.zouht.com/img/blog/3846-02.webp](https://assets.zouht.com/img/blog/3846-02.webp)

可以看到，Session 视图下方会显示一条状态条，就像浏览器的标签页一样。状态条从左到右是：Session 名称，打开的 Window 列表（相当于标签页），服务器名，时间。而状态条上面便是终端界面了。

## 2.2 脱离 Session

如果要脱离 (Detach) 一个启动的 Session，需要使用快捷键： Ctrl + B, D

需要强调的是， Ctrl + B 叫做 prefix，用于表明这个命令是输给 tmux 的，因此所有 tmux 快捷键都是以 prefix 开头的。 **按完 prefix 请松手** ，再按后续的具体命令。 **按完 prefix 请松手** ，再按后续的具体命令。

脱离后可以看到返回一条信息，提示已经从 demo 中脱离了出来。

![https://assets.zouht.com/img/blog/3846-03.webp](https://assets.zouht.com/img/blog/3846-03.webp)

## 2.3 显示 Session 列表

如果要列出当前已启动的 Session，可以使用命令： `tmux list-sessions`

可以看到我启动了三个 Session，分别命名为 demo, demo2, demo3.

![https://assets.zouht.com/img/blog/3846-04.webp](https://assets.zouht.com/img/blog/3846-04.webp)

## 2.4 连接已创建的 Session

如果要连接 (Attach) 一个已经创建的 Session，命令如下：

- `tmux attach` ：默认连接最近使用的 Session.
- `tmux attach -t [名称]` ：连接指定名称的 Session.

另外，tmux 实际上是可以多个用户连接同一个 Session 的。如果连接到相同 Session，每个人看到的内容都是完全同步的，这对于演示操作来说还是挺好的。

## 2.5 关闭已创建的 Session

如果要关闭已经创建的 Session，有几种方式：

- 如果连接着一个 Session，想关闭当前这个 Session： `exit`
- 如果连接着一个 Session，想关闭 **除了当前的** 其他 **所有** Session： `tmux kill-session -a`
- 关闭指定名称的 Session： `tmux kill-session -t [名称]`
- **强制** 关闭所有 Session（不推荐）： `tmux kill-server`

## 3 Window 窗口

一个 Session 中可以打开多个 Window，Window 会继承它所在 Session 的环境变量，同时 Window 之间也是独立存在，互不影响的。Window 会因为对应 Session 的关闭而关闭。

用浏览器来类比，一个 Session 是一个浏览器窗口，而一个 Window 是当前浏览器窗口的一个标签页。如下图所示：

![https://assets.zouht.com/img/blog/3846-05.webp](https://assets.zouht.com/img/blog/3846-05.webp)

Window 是在 Session 中启动的，因此下文所有 Window 操作必须在某个 Session 内。

## 3.1 新建和关闭 Window

如果要新建 (create) Window，可以使用快捷键： Ctrl + B, C

创建新 Window 后，注意下面的 tmux 状态栏，可以发现列表中已经多了一个 Window。列表中的数字代表 Window 编号，冒号后显示的是对应 Window 中正在运行的程序名。最后如果以 `*` 结尾，则是当前使用的 Window，最后如果以 `-` 结尾，则是上一个使用的 Window。

![https://assets.zouht.com/img/blog/3846-06.webp](https://assets.zouht.com/img/blog/3846-06.webp)

如果要关闭，可以使用 Ctrl + B, Ctrl + & （带确认，输入 y 回车）

需要提醒的是，操作指令是 & ，而不是 7 ，因此记得按 `SHIFT` 键，同时把输入法关了。

## 3.2 切换 Window

如果要切换 Window，使用快捷键是很方便的：

- Ctrl + B, P ：切换到前 (previous) 一个 Window.
- Ctrl + B, N ：切换到后 (next) 一个 Window.
- Ctrl + B, $$数字$$ ：切换到对应序号的 Window.
- Ctrl + B, W ：使用列表切换，上下键选择，回车确认。如果你开了超多 Window 则很实用。

![https://assets.zouht.com/img/blog/3846-07.webp](https://assets.zouht.com/img/blog/3846-07.webp)

## 4 Pane 窗格

一个 Window 可以切分为多个 Pane，这是我觉得 tmux 非常实用的一点。例如如果你想在运行代码的同时监控服务器状态，便可以直接左右分屏：

![https://assets.zouht.com/img/blog/3846-08.webp](https://assets.zouht.com/img/blog/3846-08.webp)

Pane 是在 Window 中启动的，因此下文所有 Pane 操作必须在某个 Window 内。

## 4.1 切分和关闭 Pane

如果要将当前的 Pane 进行切分，可以用快捷键：

- Ctrl + B, % ：竖直切分
- Ctrl + B, " ：水平切分

需要提醒的是，操作指令是 % 和 " ，而不是 4 和 ,，因此记得按 `SHIFT` 键，同时把输入法关了。

另外大家可能会觉得这个快捷键设计得莫名其妙，但是大家低头看下键盘， % 是不是刚好在键盘横向中点， " 是不是正好是纵向中点，这样想必好记多了吧。

如果要关闭，可以使用 Ctrl + B, Ctrl + X （带确认，输入 y 回车）

## 4.2 切换 Pane

如果要切换当前的 Pane，可以用： Ctrl + B, 方向键 来导航。

另外，激活的 Pane 的识别方式是观察边框，绿色边框围起来的就是当前激活的 Pane.

![https://assets.zouht.com/img/blog/3846-09.webp](https://assets.zouht.com/img/blog/3846-09.webp)

## 4.3 调整 Pane 大小

如果要调整当前激活的窗格的大小，可以使用快捷键：

- 1 个单位微调： Ctrl + B, Ctrl + 方向键
- 5 个单位调整： Ctrl + B, Alt + 方向键

## 5 杂项

## 5.1 滚动历史记录

进入 tmux 后，可以发现鼠标滚轮的窗口滚动失效了。如果要滚动历史记录，可以使用以下方式：

- Ctrl + B, `[`：进入滚动模式，这个时候就能拿滚轮滚动了，最后按 q 退出。
- Ctrl + B, `PageUp` ：进入滚动模式同时往上滚一页，这个时候就能拿滚轮滚动了，最后按 q 退出。

## 5.2 启用鼠标支持

现代的 CLI 已不是枯燥乏味的纯命令行了，tmux 是可以支持鼠标操作的。

新建配置文件 `~/.tmux.conf` ，在里面填写 `set -g mouse on` ，即可开启鼠标支持。开启鼠标支持后 tmux 多了很多实用的特性，例如：

- 右键菜单，按住右键可以调出
- 左键按住窗格边缘拖动来缩放大小
- 左键点击窗格，可以激活该窗格
- 左键点击窗口，可以切换到该窗口
- 直接拿滚轮滚动历史记录
- ……

![https://assets.zouht.com/img/blog/3846-10.webp](https://assets.zouht.com/img/blog/3846-10.webp)

不过开启鼠标操作后，可能会与一些 SSH 客户端已有的快捷操作冲突，例如 Windows Terminal 的左键框选，右键粘贴就会和 tmux 的左右键冲突。大家按自己情况决定是否启用吧。