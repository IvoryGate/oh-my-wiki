---
title: "redo log"
created: 2026-10-05
updated: 2026-10-05
type: concept
domain: 数据库
description: InnoDB 特有的物理日志，循环写入，提供 crash-safe 能力
tags: [数据库, 优化]
sources:
  - [[raw/columns/MySQL实战45讲/02  日志系统：一条SQL更新语句是如何执行的？.md]]
  - [[raw/columns/MySQL实战45讲/15  答疑文章（一）：日志和索引相关问题.md]]
  - [[raw/columns/MySQL实战45讲/23  MySQL是怎么保证数据不丢的？.md]]
status: draft
---

# redo log

## 核心定义

redo log 是 **InnoDB 引擎特有的物理日志**，记录"在某个数据页上做了什么修改"。它的核心价值是提供 **crash-safe** 能力：数据库异常重启后，已提交的修改不会丢。

> 类比（原文）：**WAL，Write-Ahead Logging**——"先写日志，再写磁盘，也就是先写粉板，等不忙的时候再写账本。"

## 关键特性

- **循环写，空间固定**：建议配置 4 个文件、每个 1GB（共 4GB）；写满后从头覆盖，因此**不能用它做归档**（归档靠 binlog）
- **两阶段写入**：prepare → commit。`commit` 步骤是最后一步，与"commit 语句"是两个不同概念
- **XID**：redo log 与 binlog 共有的字段，崩溃恢复时用于关联两者
- **redo log buffer**：一块先存放 redo 日志的内存，commit 时才写入 redo log 文件
- **落盘时机**：
  - `innodb_flush_log_at_trx_commit` 取值 **0 / 1 / 2**，建议 **1**（每次 commit 都 fsync），不建议 0
  - 后台线程**每隔 1 秒**刷一次；buffer 达到 `innodb_log_buffer_size` 的一半时也会主动写盘
- **write 与 fsync 的区别**：write 只写到文件系统 page cache（不持久化），**fsync 才持久化到磁盘、才占 IOPS**

## 与其他日志的关系

| 对比项 | redo log | binlog |
|--------|----------|--------|
| 归属 | InnoDB 引擎 | Server 层 |
| 内容 | 物理日志 | 逻辑日志 |
| 写法 | 循环写 | 追加写 |

两份日志必须逻辑一致，因此引入 [[两阶段提交]]；binlog 的细节见 [[binlog]]。

## 常见疑问（15 篇答疑）

- redo log 多大合适：受文件数 × 单文件大小限制，过小会频繁触发 checkpoint 驱动刷盘
- redo log buffer 在异常重启时是否会丢：buffer 是内存，未 fsync 的部分确实可能丢，这正是 `innodb_flush_log_at_trx_commit=1` 要解决的问题

## 来源

- [[raw/columns/MySQL实战45讲/02  日志系统：一条SQL更新语句是如何执行的？.md]]
- [[raw/columns/MySQL实战45讲/15  答疑文章（一）：日志和索引相关问题.md]]
- [[raw/columns/MySQL实战45讲/23  MySQL是怎么保证数据不丢的？.md]]

> 见 [[MySQL日志系统与数据可靠性]]
