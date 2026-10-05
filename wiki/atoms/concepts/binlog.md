---
title: "binlog"
created: 2026-10-05
updated: 2026-10-05
type: concept
domain: 数据库
description: Server 层的逻辑日志，追加写入，用于归档与主备复制
tags: [域/数据库, 主题/优化]
sources:
  - [[raw/columns/MySQL实战45讲/02  日志系统：一条SQL更新语句是如何执行的？.md]]
  - [[raw/columns/MySQL实战45讲/15  答疑文章（一）：日志和索引相关问题.md]]
  - [[raw/columns/MySQL实战45讲/23  MySQL是怎么保证数据不丢的？.md]]
  - [[raw/columns/MySQL实战45讲/31  误删数据后除了跑路，还能怎么办？.md]]
status: draft
---

# binlog

## 核心定义

binlog 是 **MySQL Server 层**的**逻辑日志**，记录语句的原始逻辑（或行变更），**追加写入**，是归档与主备复制的基础。

## 关键特性

- **归属 Server 层**：所有存储引擎共用，与 InnoDB 是否开启无关——这也是为什么 redo log（引擎层）与 binlog（Server 层）需要 [[两阶段提交]] 来保持一致
- **追加写**：不会被覆盖，可长期保留 → 恢复到任意时间点的依据
- **完整性校验**：binlog-checksum（**MySQL 5.6.2 之后**），用于验证 binlog 内容正确
- **落盘策略**：`sync_binlog` 取值 **0 / 1 / N**，常见 **100~1000**，不建议 0（0 表示由系统决定何时 fsync）
- **"双 1"**：`innodb_flush_log_at_trx_commit = 1` 且 `sync_binlog = 1` → 一个事务提交前等待两次刷盘
- **组提交**：多个并发事务由 leader 一次 fsync 持久化，"组员越多，节约磁盘 IOPS 的效果越好"
- **binlog cache**：每线程一块缓存，由 `binlog_cache_size` 控制，事务提交时才写入 binlog 文件

## 主要用途

1. **归档与数据恢复**：全备 + 依次重放 binlog = 恢复到任意时间点
   - `--stop-position` / `--start-position` 定位重放边界
   - GTID 场景用 `set gtid_next=gtid1; begin; commit;` 跳过误操作
2. **主备复制**：主库写 binlog，备库拉取并重放（见 [[MySQL日志系统与数据可靠性]]）
3. **Flashback 闪回**：改写 binlog 内容反向重放，**前提**是 `binlog_format=row` + `binlog_row_image=FULL`

## 行格式对恢复的影响

- `binlog_format = row`：记录行的实际变更，可做 Flashback，复制更可靠
- 语句级格式在有随机函数、非确定性操作时会导致主备不一致

## 来源

- [[raw/columns/MySQL实战45讲/02  日志系统：一条SQL更新语句是如何执行的？.md]]
- [[raw/columns/MySQL实战45讲/15  答疑文章（一）：日志和索引相关问题.md]]
- [[raw/columns/MySQL实战45讲/23  MySQL是怎么保证数据不丢的？.md]]
- [[raw/columns/MySQL实战45讲/31  误删数据后除了跑路，还能怎么办？.md]]

> 见 [[MySQL日志系统与数据可靠性]]
