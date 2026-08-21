---
title: Nginx 入门
type: draft
created: 2026-07-30
updated: 2026-07-30
status: doing
tags: [nginx, web, 服务器]
---
# nginx 入门

## 为什么要学习nginx

显然，当你购置了一台云服务器后，有的东西是不可避免的。当你准备在这台服务器上部署多个服务（个人博客，个人资源站，图床等），nginx注定是一个绕不开的话题。尽管在 ai 发展如此迅速的今天，这些工作完全可以 all in ai ，但是作为一个保守派，我还是喜欢自己把一些东西搞清楚的掌握感。本文主要围绕着我自己这台小服务上的nginx配置展开，不会涉及很复杂的内容，以掌握基础的配置，了解基本原理为主。

## 核心概念

### 什么是 nginx

nginx 是一个高性能的 Web 服务器和反向代理（这里讲一下正向代理与反向代理的区别）服务器。处理静态文件、转发请求、反向代理。

它做三件事：
- 处理静态文件：直接返回 HTML、图片、CSS 等资源
- 反向代理：把请求转发给后端服务
- TLS 终止：终结 HTTPS 加密，减轻后端负担
nginx 为什么高性能？因为它采用事件驱动、非阻塞 IO 架构，单个进程就能并发处理大量连接。具体怎么做到的，看下面的进程模型。

### 正向代理与反向代理

正向代理隐藏客户信息，突破访问限制。反向代理隐藏服务后端。

正向代理替"客户端"说话，反向代理替"服务器"说话。
维度	正向代理	反向代理
替谁说话	客户端	服务器
隐藏什么	客户端身份	后端实现
典型场景	突破访问限制	你服务器上的 nginx
访问方式	客户端主动配置代理	用户只感知域名

### 进程模型

一个 master 进程负责调度，多个 worker 进程负责干活。
- master：读取配置、管理 worker、处理信号（如 reload）
- worker：真正处理请求，事件驱动地并发服务
- 为什么 reload 不断连：master 加载新配置、平滑拉起新 worker，处理中的旧连接不受影响
这一点到后面讲管理命令时会有直观感受。

### 层级结构（不确定要不要放在这里）

http {} -> server {} -> location {}

下一层级继承上一层级的配置，下一层级配置可覆盖上一层级同名配置。

配置层级：http → server → location
http {
    server {          # 对应一个站点
        listen 80;
        location / {  # 对应一个 URL 路径
            ...
        }
    }
}
两条规则：
- 继承：下层继承上层的配置
- 覆盖：同名配置，下层覆盖上层

## just do it

### 准备服务器环境

- 一台 Linux 云服务器（Ubuntu/Debian）
- 检查系统版本
- 使用 root 或带 sudo 的用户
- 检查端口连通性
    - 服务器上检查端口是否被监听：`ss -tlnp`
    - 本地测试服务器是否连通：`curl -I http://服务器 IP` 或 `telnet 服务器 IP 80`
    - 这里需要注意有两组防火墙的存在
        - 服务器防火墙：ufw / firewalld / iptables
        - 提供云服务的厂商的安全组策略，需要在控制台配置相关规则
80 端口与 443端口，

### nginx 的下载与安装

```shell
# 安装
sudo apt update && sudo apt install nginx
# 验证安装
nginx -v
```



### nginx 的目录结构

```shell
/etc/nginx/
├── nginx.conf           # 主配置
├── sites-available/     # 可用站点
└── sites-enabled/       # 启用站点（软链接）
```

核心机制：available 放配置，enabled 里 ln -s 才生效
这里启动与关闭就是创建和删除软链接

### nginx 的基础管理命令

```shell
sudo systemctl status nginx    # 查看状态
sudo systemctl start nginx     # 启动
sudo systemctl stop nginx      # 停止
sudo systemctl restart nginx   # 重启（断连）
sudo systemctl reload nginx    # 重载（优雅，不断连）
nginx -t
```

### hello world

动手验证前面的知识：
- 在 /var/www/ 建一个 hello.html
- 在 sites-available/ 写一个 server block（监听 80，指向该文件）
- ln -s 到 sites-enabled/
- sudo nginx -t 验证 → sudo systemctl reload nginx
- 浏览器访问 http://务器IP/hello.html

## 实战
