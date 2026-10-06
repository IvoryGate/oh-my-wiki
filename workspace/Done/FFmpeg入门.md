---
title: FFmpeg 入门
type: draft
created: 2026-10-03
updated: 2026-10-04
status: doing
tags:
  - 域/开发工具
  - 主题/视频剪辑
---
# FFmpeg 入门

## 引言

最近在工作中遇到一个任务：混剪视频——把表现好的素材和有潜力的（留存好或回收好）素材裁切拼接在一起。一方面扩充素材，另一方面希望用好的素材带动有潜力的素材，形成一条可以撑量的新素材。如果只有两三条视频需要处理的话，即使用剪映或 PR 也是相当简单的任务。但在工作中有大量的素材需要处理，当上面这个过程重复几十上百次时，在剪映或 PR 上做就不那么有效率了。

这个任务的大致流程如下：

```mermaid
flowchart LR
    A[导入素材] --> B[找时间点]
    B --> C[裁剪]
    C --> D[调整尺寸]
    D --> E[调整音量]
    E --> F[拼接]
    F --> G[导出]
```

这些步骤并不涉及什么审美，只是在重复执行同样的规则，因此自然地想到用 FFmpeg 来做，也正好借这个机会把相关知识学到位。这篇就先从最基础的开始：怎么安装，ffmpeg、ffprobe、ffplay 这三个命令各是干什么的，以及一些基本的命令。

## 下载与配置

根据自己的设备选择对应的安装方法，装完用 `ffmpeg -version` 验证即可。

### macOS

```shell
brew install ffmpeg
```

Homebrew 会自动把 `ffmpeg` 加入 PATH。如果提示找不到命令，把 brew 的安装路径加进 shell 配置：

```shell
# Apple Silicon
export PATH="/opt/homebrew/bin:$PATH"
# Intel
export PATH="/usr/local/bin:$PATH"
```

将对应行写入 `~/.zshrc`（zsh）或 `~/.bash_profile`（bash），保存后 `source` 生效。

### Ubuntu/Debian

```shell
sudo apt install ffmpeg
```

### Windows

```shell
winget install ffmpeg
```

winget 会自动配置环境变量。也可以从[官网](https://ffmpeg.org/download.html)下载 zip 压缩包，解压后把 `bin` 目录添加到系统 PATH。

### 验证

```shell
ffmpeg -version
```

## 快速开始

### FFmpeg 是什么

> A complete, cross-platform solution to record, convert and stream audio and video.
> 
> —— [ffmpeg.org](https://ffmpeg.org/)

FFmpeg 全称 Fast Forward MPEG，是一套完整的跨平台音视频录制、转换与推流解决方案，也是目前领先的多媒体框架。

它是一个没有图形化界面的软件，我们可以通过参数控制它输入什么文件、做什么处理、输出到哪里。这样的好处就是，它可以脚本化，一个任务写一个脚本然后复用就可以了。这样也完美地满足了前面提到的需求。

### 三件套分工

FFmpeg 装完之后会有三个命令，后面所有的操作都由它们完成：

- **`ffmpeg`** — 音视频处理：格式转换、裁剪、加工多媒体文件，核心处理都从它出
- **`ffprobe`** — 查看信息：输出编码、分辨率、时长、码率这些流信息，动手前先用它看一眼
- **`ffplay`** — 播放音视频：简易播放器，不用等导出就能直接看效果

### 基础命令

假设现在有两个视频 `part1.mp4` 和 `part2.mp4`。

**看信息**

```shell
ffprobe part1.mp4
```

**预览**

```shell
ffplay part1.mp4

# -ss 是起点，-t 是时长：从 1 分钟处开始，预览 10 秒
ffplay -ss 00:01:00 -t 10 part1.mp4
```

**裁剪**

```shell
# 取前 10 秒
ffmpeg -i part1.mp4 -t 10 seg1.mp4

# 跳到 1 分钟处，取 10 秒
ffmpeg -ss 00:01:00 -i part2.mp4 -t 10 seg2.mp4

# 裁完看结果
ffplay seg1.mp4
ffplay seg2.mp4
```

**调整尺寸**

```shell
# -vf 是画面滤镜，缩放到宽 1280，高度按比例自动算（-2 是取偶数）
ffmpeg -i part1.mp4 -vf "scale=1280:-2" output.mp4
```

**调整音量**

```shell
# -af 是音频滤镜，loudnorm 把响度拉到平台标准
ffmpeg -i part1.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11 output.mp4
```

**拼接**

清单文件 `files.txt`（文件顺序就是拼接顺序）：

```text
file 'seg1.mp4'
file 'seg2.mp4'
```

```shell
# -f concat 按清单拼接，-c copy 不重新编码
# -safe 0：关闭路径检查，允许任意文件名
ffmpeg -f concat -safe 0 -i files.txt -c copy output.mp4
```

前提是各段的编码、分辨率一致：尺寸不同的段拼不到一起，参数对不上就得先重新编码、统一规格再拼。

> `-c copy` 为什么能这么快？这会在后面介绍原理的文章中讲到。

**转换格式**

```shell
# -i 指定输入文件，默认重新编码：mov → mp4
ffmpeg -i input.mov output.mp4

# -c copy：只换封装、不重新编码，基本秒完成
ffmpeg -i input.mov -c copy output.mp4
```

**改变编码与压制**

```shell
# -c:v 指定视频编码器，-crf 控制画质（18～28，越小越清晰）
ffmpeg -i part1.mp4 -c:v libx264 -crf 23 output.mp4
```

**提取音频**

```shell
# -vn 丢掉视频只留音频，-c:a 指定音频编码器
ffmpeg -i part1.mp4 -vn -c:a libmp3lame output.mp3
```

**截图**

```shell
# -frames:v 1：只输出一帧画面，就是截图
ffmpeg -ss 00:00:05 -i part1.mp4 -frames:v 1 shot.jpg
```

**转 GIF**

```shell
# 每秒抽 10 帧、宽 480，动图就出来了
ffmpeg -i part1.mp4 -vf "fps=10,scale=480:-2" output.gif
```

## 结语

回到开头那个混剪流程。假设有一个尺寸为 1920×1080 的视频 `part1.mp4` 和一个尺寸为 1280×720 的视频 `part2.mp4`，要从两条里各取 10 秒，拼成一条尺寸、音量一致的新素材。把这几步串成一个脚本：

```bash
# 准备：先用 ffprobe 看规格、ffplay 找入点，把时间记下来
#   ffprobe part1.mp4
#   ffplay -ss 00:00:05 -t 10 part1.mp4

# 1. 裁剪：按入点各取 10 秒
ffmpeg -ss 00:00:05 -i part1.mp4 -t 10 seg1.mp4
ffmpeg -ss 00:01:00 -i part2.mp4 -t 10 seg2.mp4

# 2. 调整尺寸：两条都缩到宽 1280，保证参数一致
ffmpeg -i seg1.mp4 -vf "scale=1280:-2" seg1_720.mp4
ffmpeg -i seg2.mp4 -vf "scale=1280:-2" seg2_720.mp4

# 3. 调整音量：两条响度对齐
ffmpeg -i seg1_720.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11 seg1_loud.mp4
ffmpeg -i seg2_720.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11 seg2_loud.mp4

# 4. 拼接清单（顺序就是拼接顺序）
cat > files.txt <<'EOF'
file 'seg1_loud.mp4'
file 'seg2_loud.mp4'
EOF

# 5. 拼接导出，-c copy 不重新编码
ffmpeg -f concat -safe 0 -i files.txt -c copy output.mp4

# 看结果
ffplay output.mp4
```

这样的话，开头那个需要重复几十上百次的任务，就变成给这个脚本套一层循环的事儿。在后面的文章中，会进一步补充完善相关知识。

- 《FFmpeg 原理入门》：弄明白命令为什么这样写：容器与编码、时间基、滤镜图这些概念。
- 《FFmpeg 命令速查》：按任务直接查阅。按任务分组的命令表，参数改改就能用。