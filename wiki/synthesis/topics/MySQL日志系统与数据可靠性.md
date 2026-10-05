---
title: "MySQL日志系统与数据可靠性"
type: topic
description: redo log 与 binlog 的分工、两阶段提交、双 1 落盘策略，以及 crash-safe、备份恢复与可用性诊断
tags: [数据库, 优化]
category: topics
status: stable
version: 1.0
created: 2026-10-05
updated: 2026-10-05
confidence: medium
sources:
  - [[raw/columns/MySQL实战45讲/02  日志系统：一条SQL更新语句是如何执行的？.md]]
  - [[raw/columns/MySQL实战45讲/15  答疑文章（一）：日志和索引相关问题.md]]
  - [[raw/columns/MySQL实战45讲/23  MySQL是怎么保证数据不丢的？.md]]
  - [[raw/columns/MySQL实战45讲/29  如何判断一个数据库是不是出问题了？.md]]
  - [[raw/columns/MySQL实战45讲/31  误删数据后除了跑路，还能怎么办？.md]]
  - [[raw/columns/MySQL实战45讲/32  为什么还有kill不掉的语句？.md]]
  - [[raw/columns/MySQL实战宝典/21  数据库备份：备份文件也要检查！.md]]
related_atoms:
  - [[redo log]]
  - [[binlog]]
  - [[两阶段提交]]
  - [[MySQL执行路径与基础架构]]
---

# MySQL日志系统与数据可靠性

> 02 → 15 → 23 是一条明确的递进链：日志是什么 → 异常重启怎么恢复 → 怎么保证日志本身是完整的。三篇串起来才是完整的 crash-safe。

## 一、WAL 与两份日志的分工

**WAL（Write-Ahead Logging）**："关键点就是先写日志，再写磁盘，也就是先写粉板，等不忙的时候再写账本。"

| | redo log | binlog |
|---|---|---|
| 归属 | **InnoDB 引擎特有** | **MySQL Server 层** |
| 性质 | **物理日志**，记录"在某个数据页上做了什么修改" | **逻辑日志**，记录语句原始逻辑 |
| 写法 | **循环写，空间固定**（建议 4 个文件 × 1GB = 4GB） | **追加写入** |
| 作用 | 提供 **crash-safe**：异常重启后已提交记录不丢 | 归档与主备复制 |

## 二、一条更新语句的完整路径

更新语句走查询那套 Server 层流程 → 进入 InnoDB：

1. 先写 redo log buffer，**commit 时**才写入 redo log 文件
2. 写 binlog
3. 两份日志逻辑必须一致，因此引入**两阶段提交**

**两阶段提交**：把 redo log 的写入拆成 **prepare** 和 **commit** 两步，"为了让两份日志之间的逻辑一致"。原文用反证法说明不这样做的后果：主备数据不一致。

- **XID**：redo log 与 binlog **共有的数据字段**，崩溃恢复时用来关联两者
- 注意"commit 步骤"是最后一步，与"commit 语句"是两个概念

## 三、崩溃恢复的判断规则（15 篇）

15 篇回应 02 篇评论区的追问（"两阶段提交的不同瞬间异常重启，怎么保证数据完整性"），给出时刻 A / 时刻 B 的分析与恢复判断规则：以 XID 关联两份日志，判断 prepare 的 redo log 是否已有对应 binlog。

配套机制：
- **binlog-checksum**（**MySQL 5.6.2 之后**）：验证 binlog 内容正确性
- **redo log buffer**：一块先存 redo 日志的内存，commit 时才写入文件
- **脏页**：数据页被修改后与磁盘不一致

## 四、落盘策略与"双 1"（23 篇）

23 篇的主题是"MySQL 怎么保证 redo log 和 binlog 是**完整的**"，与 02、15 串成 crash-safe 全貌。

- `innodb_flush_log_at_trx_commit`：**0 / 1 / 2**，建议 **1**，不建议 0
- `sync_binlog`：**0 / 1 / N**，常见 **100~1000**，不建议 0
- **"双 1"** = 两参数都设 1 → 一个事务提交前**等待两次刷盘**（redo prepare + binlog）
- 后台线程**每隔 1 秒**刷一次 redo log buffer；主动写盘触发条件是 buffer 达到 `innodb_log_buffer_size` 的**一半**
- **write 与 fsync 的区别**：write 只写入文件系统的 page cache（不持久化），**fsync 才持久化到磁盘、才占磁盘 IOPS**
- **组提交（group commit）**：多个并发事务由 leader 一次 fsync 持久化，"组员越多，节约磁盘 IOPS 的效果越好"（原文示例 LSN = 50 / 120 / 160）
- 相关参数：`binlog_cache_size`（每线程）、`binlog_group_commit_sync_delay`（微秒）、`binlog_group_commit_sync_no_delay_count`（次数），两者为**或**关系

## 五、数据可靠性 = 预防 + 恢复 + 校验

### 恢复到任意时间点（02 → 31）

方法论：**全量备份 + 依次重放 binlog**。31 篇把它落成操作手册：

```
0 点全备 → 恢复到临时库 → 取 0 点后日志 → 跳过误删语句
```

- 跳过误操作：`--stop-position` / `--start-position`；GTID 场景用 `set gtid_next=gtid1; begin; commit;`
- 加速：`change replication filter replicate_do_table = (tbl_name)`
- **Flashback**：改 binlog 内容拿回原库重放，前提是 `binlog_format=row` + `binlog_row_image=FULL`
- **延迟复制备库**（MySQL 5.6 引入）：`CHANGE MASTER TO MASTER_DELAY = N`，例 N=3600
- 预防手段：`sql_safe_updates = on`、账号分离（只给 DML）、删除前改名后缀 **`_to_be_deleted`**
- 恢复周期取决于备份频率：一周一备时第 6 天误删可能要恢复 6 天日志，**按天计算**

### 备份系统本身要检查（宝典 21）

- 逻辑备份（用 INSERT 形式）vs 物理备份（直接备份表空间文件与重做日志）
- `mysqldump -A --single-transaction`（`--single-transaction` 必加）；`mysqlpump --default-parallelism=8` 并发 >1 时**不能一致性备份**，生产不推荐
- **Clone Plugin**：MySQL **8.0.17** 推出
- 策略示例：**1 周 1 次全量** + 实时增量；备份文件**至少 2 个副本、2 个机房**
- **权限隔离**："可以访问线上数据库权限的同学一定不能访问离线备份系统，反之亦然"
- 核心结论与 31 篇呼应：**备份文件要检查**（恢复 → 叠加增量 → 挂为从库 → 数据核对）
- 事故参照：微盟事件 **2020-02-23**，**300 万商户**

> 三篇共同结论：**预防与校验远比事后处理重要。**

## 六、可用性诊断与 kill（29 → 32）

**发现故障的四级演进**：`select 1` → 查表 → 更新 → 内部统计

- 并发连接"影响并不大，就是多占一些内存"；**并发查询太高才是 CPU 杀手**
- 内部统计用 `performance_schema`（**MySQL 5.6+**，全开性能**下降约 10%**，统计单位皮秒），异常阈值示例：单次 IO **> 200 毫秒**
- **外部检测天然有随机性**（定时轮询）；**MHA 默认用 select 1**
- `innodb_thread_concurrency`：默认 0，建议 **64~128**

**kill 不掉的语句（32 篇）**：
- kill "并不是马上停止的意思，而是告诉执行线程说，这条语句已经不需要继续执行了，可以开始执行停止的逻辑了"
- 生效前提是语句执行过程中有多处**埋点**；线程没执行到埋点（如卡在 `innodb_thread_concurrency` 判断、每 10 毫秒循环一次）就 kill 不掉
- MySQL 通信是**停等协议**：语句没返回时，再往同一连接发命令也无用

## 关联阅读

- 执行链路上的组件见 [[MySQL执行路径与基础架构]]
- 长事务与锁的代价见 [[MySQL事务隔离与锁机制]]

## 来源

- [[raw/columns/MySQL实战45讲/02  日志系统：一条SQL更新语句是如何执行的？.md]]
- [[raw/columns/MySQL实战45讲/15  答疑文章（一）：日志和索引相关问题.md]]
- [[raw/columns/MySQL实战45讲/23  MySQL是怎么保证数据不丢的？.md]]
- [[raw/columns/MySQL实战45讲/29  如何判断一个数据库是不是出问题了？.md]]
- [[raw/columns/MySQL实战45讲/31  误删数据后除了跑路，还能怎么办？.md]]
- [[raw/columns/MySQL实战45讲/32  为什么还有kill不掉的语句？.md]]
- [[raw/columns/MySQL实战宝典/21  数据库备份：备份文件也要检查！.md]]

## 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-10-05 | 1.0 | 初版，由 MySQL实战45讲 02/15/23/29/31/32 + MySQL实战宝典 21 汇总 |
