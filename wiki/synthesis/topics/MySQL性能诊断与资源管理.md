---
title: "MySQL性能诊断与资源管理"
type: topic
domain: 数据库
description: 刷脏页导致的抖动、饮鸩止渴的救火手段清单、内存的边界（边读边发与改进 LRU）
tags: [域/数据库, 主题/优化]
category: topics
status: stable
version: 1.0
created: 2026-10-05
updated: 2026-10-05
confidence: medium
sources:
  - [[raw/columns/MySQL实战45讲/12  为什么我的MySQL会“抖”一下？.md]]
  - [[raw/columns/MySQL实战45讲/22  MySQL有哪些“饮鸩止渴”提高性能的方法？.md]]
  - [[raw/columns/MySQL实战45讲/33  我查这么多数据，会不会把数据库内存打爆？.md]]
  - [[raw/columns/MySQL实战45讲/44  答疑文章（三）：说一说这些好问题.md]]
related_atoms:
  - [[InnoDB存储引擎]]
  - [[行锁与表锁]]
  - [[MySQL索引体系与查询优化]]
---

# MySQL性能诊断与资源管理

> 这四篇回答三类问题：**为什么会突然变慢**（12）、**救火时哪些手段有毒**（22）、**大查询会不会撑爆内存**（33），44 篇则把 join、去重、自增三个易错点补上。

## 一、"抖"的元凶：刷脏页（12）

**脏页 = 内存中已修改但尚未落盘的数据页**。"MySQL 偶尔'抖'一下的那个瞬间，可能就是在刷脏页（flush）。"

**四种触发时机**：
1. **redo log 写满**（最被动、影响最大）
2. **buffer pool 空间不足**（要淘汰干净页前先刷脏页）
3. 空闲时后台线程定期刷
4. 正常关闭时刷

**三个关键参数**：

| 参数 | 口径 |
|------|------|
| `innodb_io_capacity` | 应设为**磁盘 IOPS**，用 `fio` 工具实测 |
| `innodb_max_dirty_pages_pct` | **默认 75%**，不要让脏页比例长期接近它 |
| `innodb_flush_neighbors` | **SSD 设 0**；**8.0 起默认 0** |

**刷的速度** = `max(F1(脏页比例), F2(redo log 写入速度)) × innodb_io_capacity`——即"脏页多"和"日志写得快"两者取更急的那个来限速。

## 二、饮鸩止渴清单（22）

22 篇的自评口径：这些手段**主要集中在 Server 层**。原文给的总结是——**"但，如果是无损方案的话，肯定不需要等到这个时候才上场。"**

| # | 救火手段 | 毒性 | 原文的正确做法 |
|---|---------|------|--------------|
| 1 | **调高 `max_connections`** | 大量资源耗在权限验证上，"已经连接的线程拿不到 CPU 资源去执行业务的 SQL 请求" | 先踢空闲连接；避免短连接。计数规则：**只要连着就占一个位置**，不看是否 running |
| 2 | **盲目 `kill connection + id`** | 踢到**事务内空闲**的连接只能回滚；客户端下次请求才收到 `ERROR 2013 (HY000): Lost connection...`，应用若用失效句柄重试 → 看起来"MySQL 一直没恢复"（作者碰过**不下 10 次**） | `show processlist` + `information_schema.innodb_trx`（`trx_mysql_thread_id`）区分事务内外，**优先断开事务外空闲**；**必须通知业务开发团队**；也可预设 `wait_timeout` |
| 3 | **重启 + `–skip-grant-tables`** | "风险极高，是我特别不建议使用的方案"；MySQL 8.0 启用它会**默认连带打开 `–skip-networking`** | 不要用 |
| 4 | 慢查询①**索引没设计好** | 本可上线前发现 | 紧急 `alter table`（**5.6+ 支持 Online DDL**）；理想是备库先 `set sql_log_bin=off` → alter → 主备切换 → 另一端同样操作；平时用 **gh-ost** |
| 5 | 慢查询②**语句没写好** | 属 18 篇那类错误 | 改写 SQL，或用 **MySQL 5.7 的 `query_rewrite`** 重写规则 + `call query_rewrite.flush_rewrite_rules()` |
| 6 | 慢查询③**选错索引** | 不处理会持续拖垮高峰 | 加 **`force index`**（也可用查询重写功能加） |
| 7 | **QPS 突增时重写成 `select 1`** | 两个副作用：**误伤共用同一 SQL 模板的功能**、**后面业务逻辑一起失败** → 所有选项里**优先级最低** | 优先①去掉该功能白名单；②独立账号则删用户并断连接；③才用重写。依赖规范运维：虚拟化、白名单、业务账号分离 |

**事前审计**（原文给的预防）：测试环境开 slow log 并把 **`long_query_time` 设为 0** → 插入**模拟线上数据**回归 → 检查 **`Rows_examined`** 是否符合预期；工具用 **`pt-query-digest`**。

> **边界提醒**：22 篇**没有** `like '%xx%'`、join 无索引、内存临时表代价、大结果集无节流这几条（已全文核实）——那些属于 18/34/37 篇的内容，不要挂到 22 名下。

## 三、大查询会不会撑爆内存（33）

**结论：不会**——因为 MySQL 是**"边读边发"**。

### Server 层

- 结果集**不完整保存**：取行写入 **`net_buffer`**（**`net_buffer_length` 默认 16k**）→ 写满就发 → 清空继续
- 返回 `EAGAIN` / `WSAEWOULDBLOCK` 表示本地网络栈（**socket send buffer**，默认见 `/proc/sys/net/core/wmem_default`）写满 → **暂停读数据**
- 所以单个查询占用内存**最大就是 `net_buffer_length`**，200G 大表也不会把 100G 内存吃光
- 金句："反过来想想，逻辑备份的时候，可不就是做整库扫描吗？如果这样就会把内存吃光，逻辑备份不是早就挂了？"

**两个状态的辨识**（易错点）：
- **`Sending data`**：**不一定是发送**，而是"处于执行器过程中的任意阶段"（构造锁等待场景也能看到它）
- **`Sending to client`**：才是**服务端网络栈写满、等待客户端接收**

**客户端接口**：`–quick` → `mysql_use_result`（读一行处理一行，客户端慢就会卡在 `Sending to client`）；正常业务建议 **`mysql_store_result`**；结果集极大时（评论区案例：**客户端占近 20G**）才改回 `mysql_use_result`。调优：**调大 `net_buffer_length`** 可快速减少 `Sending to client` 线程。

### InnoDB 层

- Buffer Pool 除了加速更新（配合 WAL），**更重要的作用是加速查询**——直接读内存最新页，无需先 apply redo log
- 命中率：`show engine innodb status` → **"Buffer pool hit rate"**（示例 99.0%），**稳定线上系统要在 99% 以上**
- 容量：**`innodb_buffer_pool_size` 建议为可用物理内存的 60%~80%**
- **改进版 LRU**：按 **5:3** 分 young / old 区，`LRU_old` 在链表 **5⁄8 处**；新页进 old 区；old 区页**访问时存在超过 1 秒才上移**（**`innodb_old_blocks_time` 默认 1000 毫秒**）
- 效果：全表扫描的页首末访问间隔 < 1 秒 → 始终留在 old 区快速淘汰，**对 young 区域零影响**

**代价提醒**：全表扫描**耗 IO**，业务高峰期仍不能在主库执行。

> 边界：33 篇**没有**讨论连接数与内存的关系，也没提 `sort_buffer` / `join_buffer` / `tmp_table_size` 的分配方式（已核实）——本批中 `join_buffer` 的说明在 44 篇。

## 四、答疑三：四个易错结论（44）

1. **left join 时左边不一定是驱动表**——MySQL 中 `NULL` 与任何值的等值/不等值判断**结果都是 NULL**（`select NULL = NULL` 也返回 NULL），导致 `where` 里的被驱动表条件使 left join 语义等同 join，**优化器会改写成 join**（`explain` 后 `show warnings` 可见）
   - **要保留 left join 语义，被驱动表的条件必须全写在 `on` 里**（否则结果从 6 行变 4 行）
   - 普通 join 的条件写 `on` 还是 `where` **没区别**（都被改写成同一条，执行计划相同）
2. **SNLJ 比 BNL 慢的原因**：SNLJ 每轮都要全表扫描 → 数据不在 Buffer Pool 要等磁盘、**拉低命中率**且把这些页顶到链表头部；即便都在内存，**"找下一个记录"是类指针操作，join_buffer 是数组，遍历更便宜**
3. **只去重时 `distinct` 与 `group by` 性能完全相同**：语义与执行流程一致（建临时表 + 字段唯一索引，**唯一键冲突就跳过**）
4. **statement 格式下备库自增不会不一致**：insert 前固定写 **`SET INSERT_ID=n`**；row 格式天然无此问题

**关于"好问题"**："能够帮我们扩展一个逻辑的边界的问题，就是好问题……进而可以帮助我们建立自己的知识网络。"

## 五、诊断的执行顺序

```
1. 看状态      → show processlist（Sending data / Sending to client / 锁等待）
2. 看事务      → information_schema.innodb_trx
3. 看执行计划  → explain（type=ALL、Using filesort 是信号）
4. 看慢日志    → slow log + Rows_examined + pt-query-digest
5. 看引擎状态  → show engine innodb status（Buffer pool hit rate、死锁现场）
6. 看统计      → ANALYZE TABLE / SHOW HISTOGRAM
```

## 关联阅读

- 加锁导致的等待见 [[MySQL事务隔离与锁机制]]、[[行锁与表锁]]
- 索引与执行计划见 [[MySQL索引体系与查询优化]]
- 可用性诊断与 kill 的更多细节见 [[MySQL日志系统与数据可靠性]] 第六节

## 来源

- [[raw/columns/MySQL实战45讲/12  为什么我的MySQL会“抖”一下？.md]]
- [[raw/columns/MySQL实战45讲/22  MySQL有哪些“饮鸩止渴”提高性能的方法？.md]]
- [[raw/columns/MySQL实战45讲/33  我查这么多数据，会不会把数据库内存打爆？.md]]
- [[raw/columns/MySQL实战45讲/44  答疑文章（三）：说一说这些好问题.md]]

## 变更日志

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-10-05 | 1.0 | 初版，由 MySQL实战45讲 12/22/33/44 汇总 |
