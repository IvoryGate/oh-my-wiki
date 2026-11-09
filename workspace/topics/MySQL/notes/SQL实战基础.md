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

第一次在 Navicat 打开电影表时，我看到电影编号从 1 往下排，以为查询结果也会默认按编号排列。后来我查片长最长的 5 部电影，把排序条件里的电影编号去掉，返回的结果就变了。两条语句都能运行，却规定了不同的排序规则。

写 SQL 时，先把问题说具体。以「查出片长超过 120 分钟的电影中最长的 5 部」为例，我需要确定查哪张表、显示哪些字段、怎样筛选，以及片长相同的电影该怎么排。规则写清楚之后，还要拿几条记录核对结果。

本章用 Sakila 的电影租赁数据练习。`film` 的一行是一部电影，`inventory` 的一行是一份门店库存副本，`rental` 的一行是一次租借。我们先从电影表选出符合条件的记录，再把查询扩展到多表统计。最后在练习库中修改数据，并用执行计划观察 MySQL 怎样取得查询结果。[Sakila 库存表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-inventory.html)、[Sakila 租借表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-rental.html)

<!-- 实验环境待在 Navicat 的实际连接中运行 SELECT VERSION() 后补入。 -->

## 单表查询

### 选出需要的行和列

先查一个简单的问题。**片长超过 120 分钟的电影中，编号最小的 5 部是什么？** 结果里一行对应一部电影，只需要显示电影编号、片名和片长。

```sql
SELECT film_id, title, length
FROM sakila.film
WHERE length > 120
ORDER BY film_id ASC
LIMIT 5;
```

`FROM` 指定数据来源，`sakila.film` 表示 Sakila 数据库里的电影表。`SELECT` 列出要显示的字段。想让列名显示单位时，可以写 `length AS length_minutes`，这个名字用于当前查询的输出。

`WHERE length > 120` 只保留片长超过 120 分钟的记录。`ORDER BY film_id ASC` 将这些记录按编号升序排列，`LIMIT 5` 取排在最前面的 5 条。实测结果如下。

| 电影编号 | 片名 | 片长（分钟） |
|---:|---|---:|
| 5 | AFRICAN EGG | 130 |
| 6 | AGENT TRUMAN | 169 |
| 11 | ALAMO VIDEOTAPE | 126 |
| 12 | ALASKA PHANTOM | 136 |
| 13 | ALI FOREVER | 150 |

编号 1～5 中只有编号 5 的电影超过 120 分钟，结果还出现了编号 6、11、12 和 13。这能帮助我们核对需求。这里取的是**符合条件的记录中排在最前面的 5 条**。

### 把筛选条件写清楚

如果还要求电影分级为 `PG` 或 `PG-13`，就用 `AND` 连接片长和分级要求，用括号把两个分级选项放在一起。

```sql
WHERE length > 120
  AND (rating = 'PG' OR rating = 'PG-13')
```

同一列有多个允许值时，可以把括号里的条件写成 `rating IN ('PG', 'PG-13')`。这样看一眼就能知道两个分级都要满足前面的片长要求。

范围条件要写清端点。例如「至少 120 分钟、不到 150 分钟」写作 `length >= 120 AND length < 150`。查片名以 `A` 开头，可以用 `title LIKE 'A%'`，其中 `%` 匹配零个或多个字符。

有时要筛选某一列尚未记录的值。比如查未归还的租借，在 `sakila.rental` 中用 `WHERE return_date IS NULL`。`NULL` 表示归还时间缺失，`IS NULL` 专门检查这一状态。[MySQL 空值说明](https://dev.mysql.com/doc/refman/8.0/en/problems-with-null.html)

### 让排序和业务问题一致

把问题换成「最长的 5 部电影」，排序的第一项就应改为片长。片长相同时，再按电影编号升序排列。

```sql
SELECT film_id, title, length
FROM sakila.film
WHERE length > 120
ORDER BY length DESC, film_id ASC
LIMIT 5;
```

实测返回的电影编号是 141、182、212、349 和 426，片长都是 185 分钟。第一项排序在这些记录之间分不出先后，第二项排序才决定编号小的排在前面。只按片长排序时，同片长记录的顺序由执行过程决定。如果并列跨过第 5 条，入选的电影也可能变化。[MySQL LIMIT 优化说明](https://dev.mysql.com/doc/refman/8.0/en/limit-optimization.html)

### 用 DISTINCT 列出不同的值

如果问题是「片长超过 120 分钟的电影有哪些分级」，结果里一行就应该代表一种分级。查询只选 `rating`，再用 `DISTINCT` 合并重复结果。

```sql
SELECT DISTINCT rating
FROM sakila.film
WHERE length > 120
ORDER BY rating;
```

`DISTINCT` 按 `SELECT` 中列出的值去重。如果同时选了 `rating` 和 `film_id`，就会按这两个值的组合去重。一种分级可以对应多个电影编号，因此仍可能出现多行相同的分级。[MySQL SELECT 手册](https://dev.mysql.com/doc/refman/8.0/en/select.html)

### 单表查询练习

独立写一条 SQL，找出分级为 `PG` 或 `PG-13`、片长在 120～150 分钟之间（含两端）的电影。显示编号、片名和片长，按片长降序取 5 部，片长相同则按编号升序。运行后用几条原始记录核对筛选边界和排序规则。

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
