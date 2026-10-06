---
title: ffmpeg 简单剪辑
type: note
created: 2026-07-23
updated: 2026-07-23
status: doing
tags: [域/开发工具, 主题/视频剪辑]
---
# 豪意冲天之ffmpeg快剪

## 使用场景

最近在工作中有一个需求，混剪视频，通过将表现好的素材和表现好的或者有点潜力的（留存好或回收好）的素材剪辑在一起。一方面是扩充素材，另一方面希望通过好的素材带动有潜力的素材形成一条新的可以撑量的素材。这并不是一个复杂的任务，如果只有两三条视频需要处理，只需要用剪映或者 PR 拖到时间轴上裁剪拼接一下就结束了，但是真正在工作中，有大量的素材需要处理，当这个任务反复重复几十上百次时，在剪映或者 PR 上做就不那么有效率了。

```mermaid
flowchart LR
    A[导入素材] --> B[找时间点]
    B --> C[裁剪]
    C --> D[调整尺寸]
    D --> E[调整音量]
    E --> F[拼接]
    F --> G[导出]
```

这些步骤大部分并不需要什么审美判断，只是在重复执行同样的规则。

## 裁剪与拼接

| 你要做什么 | 命令 |
|-----------|------|
| 取前 N 秒 | `ffmpeg -i in.mp4 -t 30 out.mp4` |
| 跳过开头取 N 秒 | `ffmpeg -i in.mp4 -ss 10 -t 20 out.mp4` |
| 裁剪时间段 | `ffmpeg -i in.mp4 -ss 00:01:00 -to 00:01:30 out.mp4` |
| 无损切割（不重新编码） | `ffmpeg -i in.mp4 -c copy -ss 10 -t 20 out.mp4` |

## 画面处理

| 你要做什么 | 命令 |
|-----------|------|
| 缩放到指定尺寸 | `ffmpeg -i in.mp4 -vf scale=1080:1920 out.mp4` |
| 缩放+保持比例+填充黑边 | `ffmpeg -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" out.mp4` |
| 裁剪画面区域 | `ffmpeg -i in.mp4 -vf "crop=w:h:x:y" out.mp4` |
| 加图片水印 | `ffmpeg -i in.mp4 -i logo.png -filter_complex "overlay=10:10" out.mp4` |
| 旋转画面 | `ffmpeg -i in.mp4 -vf "rotate=PI/2" out.mp4` |

## 音频处理

| 你要做什么 | 命令 |
|-----------|------|
| 统一音量（loudnorm） | `ffmpeg -i in.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11 out.mp4` |
| 替换音频 | `ffmpeg -i in.mp4 -i audio.mp3 -c:v copy -map 0:v -map 1:a -shortest out.mp4` |
| 提取音频 | `ffmpeg -i in.mp4 -vn -c:a libmp3lame out.mp3` |
| 静音指定片段 | `ffmpeg -i in.mp4 -af "volume=enable='between(t,0,5)':volume=0" out.mp4` |

## 速度与格式

| 你要做什么 | 命令 |
|-----------|------|
| 快放/慢放 2 倍 | `ffmpeg -i in.mp4 -vf "setpts=0.5*PTS" -af "atempo=2.0" out.mp4` |
| 转 GIF | `ffmpeg -i in.mp4 -vf "fps=10,scale=480:-1" out.gif` |
| 转 H.265 压缩 | `ffmpeg -i in.mp4 -c:v libx265 -crf 28 out.mp4` |

## 完整示例：两段视频混剪（竖屏 1080×1920）

```shell
ffmpeg -i input_0.mp4 -i input_2.mp4 -filter_complex \
      "[0:v]trim=duration=30,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2[v0]; \
       [0:a]atrim=duration=30,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[a0]; \
       [1:v]trim=duration=30,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2[v1]; \
       [1:a]atrim=duration=30,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[a1]; \
       [v0][a0][v1][a1]concat=n=2:v=1:a=1" \
    output.mp4
```

```shell
ffmpeg -i input_0.mp4 -i input_1.mp4 -filter_complex \
    "[0:v]trim=duration=30,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2[v0]; \
     [0:a]atrim=duration=30,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[a0]; \
     [1:v]trim=duration=30,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2[v1]; \
     [1:a]atrim=duration=30,asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11[a1]; \
     [v0][a0][v1][a1]concat=n=2:v=1:a=1[outv][outa]" \
    -map [outv] -map [outa] \
    output.mp4
```


