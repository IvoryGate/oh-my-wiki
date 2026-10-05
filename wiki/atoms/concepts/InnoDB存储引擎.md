---
title: "InnoDB存储引擎"
created: 2026-10-05
updated: 2026-10-05
type: concept
domain: 数据库
description: MySQL 默认存储引擎——索引组织表、buffer pool 与改进 LRU，以及与其他引擎的取舍
tags: [数据库]
sources:
  - [[raw/columns/MySQL实战45讲/38  都说InnoDB好，那还要不要使用Memory引擎？.md]]
  - [[raw/columns/MySQL实战45讲/33  我查这么多数据，会不会把数据库内存打爆？.md]]
  - [[raw/columns/MySQL实战宝典/07  表的访问设计：你该选择 SQL 还是 NoSQL？.md]]
status: draft
---

# InnoDB存储引擎

## 核心定义

InnoDB 是 **MySQL 5.5.5 起的默认存储引擎**，属于存储引擎层；与之相对的连接器、分析器、优化器、执行器等都在 **Server 层**（见 [[MySQL执行路径与基础架构]]）。它的两个根本特征：

1. **索引组织表**：数据按主键组织成 B+ 树，即 [[聚簇索引]]
2. **Buffer Pool 内存管理**：数据页在内存中管理，配合 WAL 同时加速更新与查询

## Buffer Pool 与改进版 LRU（33 篇）

**作用**：
- 加速更新——配合 WAL 免去随机写盘
- **更重要的作用是加速查询**——WAL 下磁盘页是旧的，直接读内存最新页即可，**无需先把 redo log 应用到数据页**

**容量与健康度**：
- `innodb_buffer_pool_size` **建议设为可用物理内存的 60%~80%**
- 命中率看 `show engine innodb status` 的 **"Buffer pool hit rate"**（示例 99.0%），**稳定线上系统要在 99% 以上**

**改进版 LRU**（防全表扫描污染缓存）：
- 按 **5:3** 把链表分成 **young 区 / old 区**，`LRU_old` 位于链表 **5⁄8 处**
- 新页插入 `LRU_old`（old 区头部）
- old 区页被访问时：**在链表中存在超过 1 秒才移到头部**，短于 1 秒不动
- 阈值参数 **`innodb_old_blocks_time`，默认 1000（毫秒）**
- 效果：顺序全表扫描的页首末访问间隔 < 1 秒 → 始终留在 old 区并快速淘汰，**对 young 区域完全没有影响**

## 与其他引擎/形态的对比

| 维度 | InnoDB | Memory 引擎 | MyISAM |
|------|--------|------------|--------|
| 组织方式 | 索引组织表 | **堆组织表**，主键为 hash 索引 | — |
| 锁粒度 | 行锁 | **只支持表锁** | 表锁 |
| 数据持久化 | 持久 | **重启全清空** | 持久 |
| count(*) | 需 MVCC 逐行判断 | — | **存总数，直接返回** |
| 特性 | 事务、MVCC、行锁 | 不支持 Blob/Text，`varchar(N)` 当 `char(N)` | 无事务 |

**结论（38 篇）**："我建议你把普通内存表都用 InnoDB 表来代替"——Memory 唯一合理用途是**内存临时表**。

> 双 M 主从场景的坑：备库内存表重启后会向主库发 `DELETE` 清表。

## 访问方式的收敛（宝典 07）

InnoDB 表可以通过三种协议访问，**底层都是表、都存 InnoDB**：SQL、**Memcached 插件**（5.6+，端口 11211，绕过 SQL 解析，实测快 **54.33%**）、**X Protocol**（5.7+，端口 33060）。原文的价值主张是"用 MySQL 打造成 SQL & NoSQL 的文档数据库"，**利于收敛技术栈**。

## 来源

> 见 [[MySQL存储结构与表设计]]、[[MySQL性能诊断与资源管理]]
