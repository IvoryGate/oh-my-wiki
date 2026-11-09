---
title: SQL 实战基础
type: draft
created: 2026-11-09
updated: 2026-11-09
status: doing
tags: [域/数据库]
---

# SQL 实战基础

> MySQL 学习系列第 1 篇。章节目标与验收题见 [[workspace/topics/MySQL/大纲|系列大纲]]。

## 开篇

- [ ] 从 Sakila 的电影租赁场景引出本章。读者从一条单表查询开始，最后能独立查询、汇总、连接和修改练习数据，并核对结果。
- [ ] 介绍练习用到的三张表。`film` 的一行是一部电影，`inventory` 的一行是一份库存副本，`rental` 的一行是一次租借。
- [ ] 补上 Navicat 连接实际对应的服务端版本。待运行 `SELECT VERSION()` 核对。

## 单表查询

- [ ] 从「找出片长超过 120 分钟的电影」讲 `SELECT`、`FROM`、列名和 `WHERE`，再用实际问题补条件组合、范围、文本匹配、去重和 `NULL`。
- [ ] 用 `ORDER BY` 和 `LIMIT` 写出「最长的 5 部电影」。对照片长相同的记录，解释第二个排序字段如何决定先后。
- 按片长降序、编号升序取前 5 部，实测返回编号 141、182、212、349、426，片长均为 185 分钟。用这组数据引出并列排序。

## 分组与汇总

- [ ] 用库存表解释 `COUNT(*)` 和 `GROUP BY`。依次回答「这部电影共有几份」「每家门店各有几份」「多部电影在各店分别有几份」。
- [ ] 用 `WHERE` 筛选参与统计的记录，用 `HAVING` 筛选汇总后的组。补 `SUM`、`AVG`、`MIN`、`MAX` 和 `COUNT(DISTINCT 列)` 的实际用法。
- 实测显示 141 号电影在门店 1 有 3 份，在门店 2 有 2 份。租借记录中 `COUNT(*)` 为 16,044，`COUNT(return_date)` 为 15,861，两者相差 183 笔未归还记录。

## 多表查询

- [ ] 用 `inventory.film_id` 连接 `film.film_id`，给库存清单加上片名。解释表别名、`ON` 和一对多连接后的行数。
- 141 号电影的 5 份副本连接电影表后，实测仍有 5 行，片名 `CHICAGO NORTH` 出现 5 次。
- [ ] 用 `LEFT JOIN` 和 `rental_id IS NULL` 找没有租借记录的库存副本。待补本地输出，以及匹配多条、匹配零条时的结果对照。
- [ ] 用同一个例子核对右表筛选条件放在 `ON` 或 `WHERE` 时的差别，再用 `COUNT(rental_id)` 统计含零次租借的结果。

## 拆解复杂查询

- [ ] 用子查询和 `EXISTS`、`NOT EXISTS` 表达是否存在关联记录。与前面的 `LEFT JOIN` 例题核对结果。
- [ ] 完成「每家门店租借次数最多的 3 部电影」。先连接库存与租借，按门店和电影统计租借次数，再用 `WITH` 整理中间结果，以 `ROW_NUMBER()` 分组排名。
- [ ] 写明并列时的排序规则，并选一家门店手工核对排名。

## 建表与增删改

- [ ] 在独立练习库建两张关联表，练习基本字段类型、主键、外键、`NOT NULL`、`UNIQUE` 和默认值。
- [ ] 练习 `INSERT`、`UPDATE` 和 `DELETE`，用 `SELECT` 核对受影响的记录。补一个重复值或无效关联触发约束的例子。
- [ ] 用 `START TRANSACTION` 开启事务，分别演示提交和回滚对数据修改结果的影响，记录操作前后查询。

## 一条查询怎样执行

- [ ] 串起从 Navicat 发送 SQL，到 MySQL 解析语句、选择计划、执行器向 InnoDB 取数据并返回结果的过程。
- [ ] 用 `EXPLAIN` 读计划，用 `EXPLAIN ANALYZE` 读实际行数。解释两份计划中的读取、筛选、排序和返回条数。

### 已有实验

在 `sakila.film` 中筛选片长超过 120 分钟的电影。两次查询分别按片长降序和编号升序取前 5 条。

| 排序方式 | 读取记录 | 筛选节点输出 | 额外排序 | 返回记录 |
|---|---:|---:|---|---:|
| `ORDER BY length DESC` | 1,000 | 457 | 有 | 5 |
| `ORDER BY film_id ASC` | 13 | 5 | 无 | 5 |

- [ ] 补两条实测 SQL 和计划片段，解释主键顺序怎样支持提前停止。分别写出两个排序条件回答的业务问题。

## 综合练习

- [ ] 独立查询「每家门店未归还笔数最多的 3 部电影」。从选表、连接、筛选到汇总排名，用小样本核对答案。
- [ ] 用一份执行计划讲清查询如何读取和返回数据，再核对一次练习库的修改结果。

## 参考资料

- 《MySQL 实战 45 讲》第 01 讲。用于核对查询执行流程。
- 核对每张表的一行代表什么。[Sakila 库存表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-inventory.html)、[Sakila 租借表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-rental.html)。
- 核对连接规则和执行计划。[MySQL 8.0 JOIN 手册](https://dev.mysql.com/doc/refman/8.0/en/join.html)、[EXPLAIN 手册](https://dev.mysql.com/doc/refman/8.0/en/explain.html)。
