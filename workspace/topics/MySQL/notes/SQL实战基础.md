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

## 实验环境

查询在本机的 Sakila 样例库中执行。`film` 的一行是一部电影，`inventory` 的一行是一份库存副本，`rental` 的一行是一次租借。[Sakila 库存表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-inventory.html)、[Sakila 租借表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-rental.html)

建表、增删改和删表在独立练习库中执行。每段 SQL 后是命令行实测输出。多个语句的输出按执行顺序排列，执行计划只保留树形部分。

服务端版本通过以下语句确认。

```sql
SELECT VERSION() AS mysql_version;
```

```text
+---------------+
| mysql_version |
+---------------+
| 8.0.34        |
+---------------+
1 row in set (0.00 sec)
```

## 单表查询

先明确从哪张表查、结果里一行代表什么，再写筛选、排序与取几条。

### 选出需要的行和列

先查片长超过 120 分钟的电影中，编号最小的 5 部。`FROM` 指定电影表，`SELECT` 指定结果列，`WHERE` 决定哪些行入选。

```sql
SELECT film_id, title, length
FROM sakila.film
WHERE length > 120
ORDER BY film_id ASC
LIMIT 5;
```

```text
+---------+-----------------+--------+
| film_id | title           | length |
+---------+-----------------+--------+
|       5 | AFRICAN EGG     |    130 |
|       6 | AGENT TRUMAN    |    169 |
|      11 | ALAMO VIDEOTAPE |    126 |
|      12 | ALASKA PHANTOM  |    136 |
|      13 | ALI FOREVER     |    150 |
+---------+-----------------+--------+
5 rows in set (0.00 sec)
```

第一条的编号是 5，后面还出现了 6、11、12 和 13。`LIMIT` 取的是符合筛选条件并按要求排列后的前 5 条。

### 组合筛选条件

片长必须超过 120 分钟，分级可以是 `PG` 或 `PG-13`。括号把两个分级放在同一组，`AND` 再把分级要求与片长要求连起来。

```sql
SELECT film_id, title, length, rating
FROM sakila.film
WHERE length > 120
  AND (rating = 'PG' OR rating = 'PG-13')
ORDER BY film_id ASC
LIMIT 5;
```

```text
+---------+-----------------------------+--------+--------+
| film_id | title                       | length | rating |
+---------+-----------------------------+--------+--------+
|       6 | AGENT TRUMAN                |    169 | PG     |
|      12 | ALASKA PHANTOM              |    136 | PG     |
|      13 | ALI FOREVER                 |    150 | PG     |
|      33 | APOLLO TEEN                 |    153 | PG-13  |
|      35 | ARACHNOPHOBIA ROLLERCOASTER |    147 | PG-13  |
+---------+-----------------------------+--------+--------+
5 rows in set (0.00 sec)
```

### 筛选范围和文本

把条件改成片长在 120～150 分钟、分级为 `PG` 或 `PG-13`。片名须以 `A` 开头，且至少还有一个字符，同时排除以 `AD` 开头的片名。`BETWEEN` 包含两个端点，`IN` 列出允许值。`LIKE` 里的 `_` 匹配一个字符，`%` 匹配零个或多个字符。

```sql
SELECT film_id, title, length AS length_minutes, rating
FROM sakila.film
WHERE length BETWEEN 120 AND 150
  AND rating IN ('PG', 'PG-13')
  AND title LIKE 'A_%'
  AND title NOT LIKE 'AD%'
ORDER BY film_id
LIMIT 5;
```

```text
+---------+-----------------------------+----------------+--------+
| film_id | title                       | length_minutes | rating |
+---------+-----------------------------+----------------+--------+
|      12 | ALASKA PHANTOM              |            136 | PG     |
|      13 | ALI FOREVER                 |            150 | PG     |
|      35 | ARACHNOPHOBIA ROLLERCOASTER |            147 | PG-13  |
|      36 | ARGONAUTS TOWN              |            127 | PG-13  |
|      37 | ARIZONA BANG                |            121 | PG     |
+---------+-----------------------------+----------------+--------+
5 rows in set (0.01 sec)
```

### 筛选空值

在租借表里，归还时间为空表示这笔记录尚未登记归还。用 `IS NULL` 找出这些记录，用 `IS NOT NULL` 筛选已登记归还的记录。[MySQL 空值说明](https://dev.mysql.com/doc/refman/8.0/en/problems-with-null.html)

**尚未登记归还**

```sql
SELECT rental_id, return_date
FROM sakila.rental
WHERE return_date IS NULL
ORDER BY rental_id
LIMIT 5;
```

```text
+-----------+-------------+
| rental_id | return_date |
+-----------+-------------+
|     11496 | NULL        |
|     11541 | NULL        |
|     11563 | NULL        |
|     11577 | NULL        |
|     11593 | NULL        |
+-----------+-------------+
5 rows in set (0.00 sec)
```

**已登记归还**

```sql
SELECT rental_id, return_date
FROM sakila.rental
WHERE return_date IS NOT NULL
ORDER BY rental_id
LIMIT 2;
```

```text
+-----------+---------------------+
| rental_id | return_date         |
+-----------+---------------------+
|         1 | 2005-05-26 22:04:30 |
|         2 | 2005-05-28 19:40:33 |
+-----------+---------------------+
2 rows in set (0.00 sec)
```

### 确定并列结果的顺序

如果要查最长的 5 部，先按片长降序排列，片长相同再按编号升序排列。

```sql
SELECT film_id, title, length
FROM sakila.film
WHERE length > 120
ORDER BY length DESC, film_id ASC
LIMIT 5;
```

```text
+---------+----------------+--------+
| film_id | title          | length |
+---------+----------------+--------+
|     141 | CHICAGO NORTH  |    185 |
|     182 | CONTROL ANTHEM |    185 |
|     212 | DARN FORRESTER |    185 |
|     349 | GANGS PRIDE    |    185 |
|     426 | HOME PITY      |    185 |
+---------+----------------+--------+
5 rows in set (0.00 sec)
```

这 5 部电影都是 185 分钟。第二个排序字段确定了并列记录的顺序。如果只写片长，且并列跨过第 5 条，具体入选的电影可能随执行计划而变。[MySQL LIMIT 优化说明](https://dev.mysql.com/doc/refman/8.0/en/limit-optimization.html)

### 列出不同的分级

结果一行代表一种分级时，只选择 `rating`，再用 `DISTINCT` 合并相同的结果。多选 `film_id` 后，去重依据就变成分级与电影编号的组合。[MySQL SELECT 手册](https://dev.mysql.com/doc/refman/8.0/en/select.html)

```sql
SELECT DISTINCT rating
FROM sakila.film
WHERE length > 120
ORDER BY rating;
```

```text
+--------+
| rating |
+--------+
| G      |
| PG     |
| PG-13  |
| R      |
| NC-17  |
+--------+
5 rows in set (0.00 sec)
```

### 在结果中计算和转换值

`AS` 给表达式的结果起名。这里用 `CASE` 做片长分类，用 `SUBSTRING` 截取片名，`LOWER`、`UPPER` 转换字母大小写，`CHAR_LENGTH` 数字符，`ROUND` 按指定小数位四舍五入。

```sql
SELECT film_id,
       CASE WHEN length > 120 THEN 'long' ELSE 'regular' END AS length_group,
       LOWER(SUBSTRING(title, 1, 7)) AS short_title,
       UPPER('dvd') AS media,
       CHAR_LENGTH(title) AS title_chars,
       ROUND(rental_rate, 1) AS rounded_rate
FROM sakila.film
WHERE film_id IN (5, 141)
ORDER BY film_id;
```

```text
+---------+--------------+-------------+-------+-------------+--------------+
| film_id | length_group | short_title | media | title_chars | rounded_rate |
+---------+--------------+-------------+-------+-------------+--------------+
|       5 | long         | african     | DVD   |          11 |          3.0 |
|     141 | long         | chicago     | DVD   |          13 |          5.0 |
+---------+--------------+-------------+-------+-------------+--------------+
2 rows in set (0.00 sec)
```

### 显示日期与缺失值

`DATE` 取日期部分，`DATEDIFF` 比较两个日期相差几天。`IFNULL` 可指定一个替代值，`COALESCE` 取从左往右第一个有值的参数。

```sql
SELECT rental_id, DATE(rental_date) AS rental_day,
       DATEDIFF(return_date, rental_date) AS days_out,
       COALESCE(DATE_FORMAT(return_date, '%Y-%m-%d'), 'open') AS returned_on,
       IFNULL(DATEDIFF(return_date, rental_date), -1) AS days_or_unknown
FROM sakila.rental
WHERE rental_id IN (1, 11496)
ORDER BY rental_id;

SELECT NOW() AS server_time, FORMAT(16044.5, 2) AS display_number;
```

```text
+-----------+------------+----------+-------------+-----------------+
| rental_id | rental_day | days_out | returned_on | days_or_unknown |
+-----------+------------+----------+-------------+-----------------+
|         1 | 2005-05-24 |        2 | 2005-05-26  |               2 |
|     11496 | 2006-02-14 |     NULL | open        |              -1 |
+-----------+------------+----------+-------------+-----------------+
2 rows in set (0.00 sec)

+---------------------+----------------+
| server_time         | display_number |
+---------------------+----------------+
| 2026-11-09 15:54:33 | 16,044.50      |
+---------------------+----------------+
1 row in set (0.00 sec)
```

`days_or_unknown` 中的 `-1` 是这个查询选用的显示值。`NOW()` 随执行时间变化，`FORMAT` 返回用于展示的文本。

把片长筛选改成 120～150 分钟后，实测结果包含恰好 150 分钟的 13 号电影。可以用这一行核对范围的右端点。

## 分组与汇总

先确定每组代表什么，再选计数或金额口径。分组字段变了，结果每一行的含义也会变。

### 按电影和门店数副本

库存表一行是一份副本。按电影编号和门店编号分组后，每组 `COUNT(*)` 就是该片在该店的副本数。

```sql
SELECT film_id, store_id, COUNT(*) AS copies
FROM sakila.inventory
WHERE film_id IN (141, 182)
GROUP BY film_id, store_id
ORDER BY film_id, store_id;
```

```text
+---------+----------+--------+
| film_id | store_id | copies |
+---------+----------+--------+
|     141 |        1 |      3 |
|     141 |        2 |      2 |
|     182 |        1 |      2 |
+---------+----------+--------+
3 rows in set (0.00 sec)
```

141 号电影在两家门店分别有 3 份和 2 份。182 号电影只出现在门店 1 的结果里。

### 筛选分组结果

`WHERE` 先限定参与统计的电影，`HAVING` 再筛选已经算出副本数的组。

```sql
SELECT film_id, store_id, COUNT(*) AS copies
FROM sakila.inventory
WHERE film_id IN (141, 182)
GROUP BY film_id, store_id
HAVING COUNT(*) >= 3
ORDER BY film_id, store_id;
```

```text
+---------+----------+--------+
| film_id | store_id | copies |
+---------+----------+--------+
|     141 |        1 |      3 |
+---------+----------+--------+
1 row in set (0.00 sec)
```

### 计数口径由表达式决定

`COUNT(*)` 数所有行，`COUNT(return_date)` 数归还时间有值的行。两者相减得到未归还笔数。`COUNT(DISTINCT store_id)` 数不同门店。

```sql
SELECT COUNT(*) AS total_rentals,
       COUNT(return_date) AS returned_rentals,
       COUNT(*) - COUNT(return_date) AS open_rentals
FROM sakila.rental;

SELECT film_id, COUNT(*) AS copies,
       COUNT(DISTINCT store_id) AS stores
FROM sakila.inventory
WHERE film_id IN (141, 182)
GROUP BY film_id
ORDER BY film_id;
```

```text
+---------------+------------------+--------------+
| total_rentals | returned_rentals | open_rentals |
+---------------+------------------+--------------+
|         16044 |            15861 |          183 |
+---------------+------------------+--------------+
1 row in set (0.00 sec)

+---------+--------+--------+
| film_id | copies | stores |
+---------+--------+--------+
|     141 |      5 |      2 |
|     182 |      2 |      1 |
+---------+--------+--------+
2 rows in set (0.00 sec)
```

实测总租借数 16,044，登记归还 15,861，差值为 183。

### 汇总金额

付款表一行是一笔付款。以客户为组，分别计算笔数、总金额、平均金额和单笔金额的范围。

```sql
SELECT customer_id, COUNT(*) AS payments,
       SUM(amount) AS total_amount, ROUND(AVG(amount), 2) AS avg_amount,
       MIN(amount) AS min_amount, MAX(amount) AS max_amount
FROM sakila.payment
WHERE customer_id IN (1, 2)
GROUP BY customer_id
HAVING COUNT(*) >= 10
ORDER BY customer_id;
```

```text
+-------------+----------+--------------+------------+------------+------------+
| customer_id | payments | total_amount | avg_amount | min_amount | max_amount |
+-------------+----------+--------------+------------+------------+------------+
|           1 |       32 |       118.68 |       3.71 |       0.99 |       9.99 |
|           2 |       27 |       128.73 |       4.77 |       0.99 |      10.99 |
+-------------+----------+--------------+------------+------------+------------+
2 rows in set (0.01 sec)
```

## 多表查询

先找到表之间的连接键，再决定结果要保留哪些记录。租借表通过副本编号连接库存表，库存表再通过电影编号连接电影表。

### INNER JOIN 补上片名

`INNER JOIN` 只保留满足 `ON` 条件的配对。这里每份库存副本匹配一部电影，所以同一个片名会在多行出现。

```sql
SELECT i.inventory_id, f.title, i.store_id
FROM sakila.inventory AS i
INNER JOIN sakila.film AS f
    ON i.film_id = f.film_id
WHERE i.film_id = 141
ORDER BY i.store_id, i.inventory_id;
```

```text
+--------------+---------------+----------+
| inventory_id | title         | store_id |
+--------------+---------------+----------+
|          649 | CHICAGO NORTH |        1 |
|          650 | CHICAGO NORTH |        1 |
|          651 | CHICAGO NORTH |        1 |
|          652 | CHICAGO NORTH |        2 |
|          653 | CHICAGO NORTH |        2 |
+--------------+---------------+----------+
5 rows in set (0.00 sec)
```

### 沿关系连接三张表

一笔租借对应一份副本，一份副本对应一部电影。把这两段关系串起来，结果就能同时显示租借编号、片名和门店。

```sql
SELECT r.rental_id, f.title, i.store_id
FROM sakila.rental AS r
INNER JOIN sakila.inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN sakila.film AS f ON i.film_id = f.film_id
WHERE f.film_id = 141
ORDER BY r.rental_id
LIMIT 5;
```

```text
+-----------+---------------+----------+
| rental_id | title         | store_id |
+-----------+---------------+----------+
|       225 | CHICAGO NORTH |        1 |
|      1462 | CHICAGO NORTH |        2 |
|      2846 | CHICAGO NORTH |        1 |
|      3818 | CHICAGO NORTH |        2 |
|      5340 | CHICAGO NORTH |        1 |
+-----------+---------------+----------+
5 rows in set (0.00 sec)
```

### LEFT JOIN 找没有租借记录的副本

`LEFT JOIN` 先保留每份库存副本。没找到对应租借时，右表列会填为 `NULL`。每笔真实租借都有 `rental_id`，所以可以用它判断是否匹配。[MySQL JOIN 手册](https://dev.mysql.com/doc/refman/8.0/en/join.html)

```sql
SELECT i.inventory_id, i.film_id, i.store_id, r.rental_id
FROM sakila.inventory AS i
LEFT JOIN sakila.rental AS r ON i.inventory_id = r.inventory_id
WHERE r.rental_id IS NULL
ORDER BY i.inventory_id
LIMIT 10;
```

```text
+--------------+---------+----------+-----------+
| inventory_id | film_id | store_id | rental_id |
+--------------+---------+----------+-----------+
|            5 |       1 |        2 |      NULL |
+--------------+---------+----------+-----------+
1 row in set (0.01 sec)
```

本机实测只返回库存副本 5。它对应电影 1、门店 2，租借编号是 NULL。

### 保留零库存的电影

从电影表出发做左连接。没匹配到库存时，`COUNT(*)` 仍会数到那行补空的结果，`COUNT(i.inventory_id)` 得到 0。

```sql
SELECT f.film_id, f.title, COUNT(*) AS joined_rows,
       COUNT(i.inventory_id) AS copies
FROM sakila.film AS f
LEFT JOIN sakila.inventory AS i ON f.film_id = i.film_id
GROUP BY f.film_id, f.title
ORDER BY copies, f.film_id
LIMIT 4;
```

```text
+---------+----------------+-------------+--------+
| film_id | title          | joined_rows | copies |
+---------+----------------+-------------+--------+
|      14 | ALICE FANTASIA |           1 |      0 |
|      33 | APOLLO TEEN    |           1 |      0 |
|      36 | ARGONAUTS TOWN |           1 |      0 |
|      38 | ARK RIDGEMONT  |           1 |      0 |
+---------+----------------+-------------+--------+
4 rows in set (0.01 sec)
```

### 区分 ON 和 WHERE 的筛选时机

拿 652 号副本做对照。放在 `ON` 中的条件限定哪些副本可以配对。放在 `WHERE` 中的条件筛选连接结果，右侧补出的 `NULL` 不满足等于 652 的条件。

**条件在 ON**

```sql
SELECT f.film_id, i.inventory_id
FROM sakila.film AS f
LEFT JOIN sakila.inventory AS i
    ON f.film_id = i.film_id AND i.inventory_id = 652
WHERE f.film_id IN (141, 182)
ORDER BY f.film_id;
```

```text
+---------+--------------+
| film_id | inventory_id |
+---------+--------------+
|     141 |          652 |
|     182 |         NULL |
+---------+--------------+
2 rows in set (0.00 sec)
```

**条件在 WHERE**

```sql
SELECT f.film_id, i.inventory_id
FROM sakila.film AS f
LEFT JOIN sakila.inventory AS i ON f.film_id = i.film_id
WHERE f.film_id IN (141, 182)
  AND i.inventory_id = 652
ORDER BY f.film_id;
```

```text
+---------+--------------+
| film_id | inventory_id |
+---------+--------------+
|     141 |          652 |
+---------+--------------+
1 row in set (0.00 sec)
```

条件放在 ON 时，两部电影都保留，182 号的库存编号是 NULL。条件移到 WHERE 后，只留下 141 号与副本 652 的配对。

### 换一边保留记录

`RIGHT JOIN` 保留右边的电影表。按相同连接键筛选无匹配的记录，就可以找出没有库存副本的电影。

```sql
SELECT f.film_id, f.title
FROM sakila.inventory AS i
RIGHT JOIN sakila.film AS f ON i.film_id = f.film_id
WHERE i.inventory_id IS NULL
ORDER BY f.film_id
LIMIT 4;
```

```text
+---------+----------------+
| film_id | title          |
+---------+----------------+
|      14 | ALICE FANTASIA |
|      33 | APOLLO TEEN    |
|      36 | ARGONAUTS TOWN |
|      38 | ARK RIDGEMONT  |
+---------+----------------+
4 rows in set (0.00 sec)
```

### 枚举组合与自连接

`CROSS JOIN` 枚举指定电影与门店的组合，适合生成检查清单。两份不同别名的电影表还可以相互连接，例如找片长与 141 号相同的其他电影。

```sql
SELECT f.film_id, s.store_id
FROM sakila.film AS f
CROSS JOIN sakila.store AS s
WHERE f.film_id IN (141, 182)
ORDER BY f.film_id, s.store_id;

SELECT f2.film_id, f2.title, f2.length
FROM sakila.film AS f1
INNER JOIN sakila.film AS f2
    ON f1.length = f2.length AND f1.film_id <> f2.film_id
WHERE f1.film_id = 141
ORDER BY f2.film_id
LIMIT 3;
```

```text
+---------+----------+
| film_id | store_id |
+---------+----------+
|     141 |        1 |
|     141 |        2 |
|     182 |        1 |
|     182 |        2 |
+---------+----------+
4 rows in set (0.03 sec)

+---------+----------------+--------+
| film_id | title          | length |
+---------+----------------+--------+
|     182 | CONTROL ANTHEM |    185 |
|     212 | DARN FORRESTER |    185 |
|     349 | GANGS PRIDE    |    185 |
+---------+----------------+--------+
3 rows in set (0.00 sec)
```

### 把零次租借也计入统计

对比库存副本 5 和 649。先保留每份副本，再数右表中有租借编号的行。

```sql
SELECT i.inventory_id, COUNT(*) AS joined_rows,
       COUNT(r.rental_id) AS rentals
FROM sakila.inventory AS i
LEFT JOIN sakila.rental AS r ON i.inventory_id = r.inventory_id
WHERE i.inventory_id IN (5, 649)
GROUP BY i.inventory_id
ORDER BY i.inventory_id;
```

```text
+--------------+-------------+---------+
| inventory_id | joined_rows | rentals |
+--------------+-------------+---------+
|            5 |           1 |       0 |
|          649 |           2 |       2 |
+--------------+-------------+---------+
2 rows in set (0.00 sec)
```

副本 5 保留了一行，但右边没有租借编号，因此实际租借次数是 0。

## 拆解复杂查询

把问题拆成能独立核对的步骤。先确定集合或汇总口径，再用子查询、公共表表达式和窗口函数整理结果。

### 用 UNION 合并结果

两个查询都返回门店编号。`UNION` 合并并去重，`UNION ALL` 保留各查询返回的每一行。两边的结果需要有相同列数，并且对应列的类型可以兼容。

**UNION**

```sql
SELECT store_id FROM sakila.inventory WHERE inventory_id IN (649, 652)
UNION
SELECT store_id FROM sakila.inventory WHERE inventory_id = 650
ORDER BY store_id;
```

```text
+----------+
| store_id |
+----------+
|        1 |
|        2 |
+----------+
2 rows in set (0.00 sec)
```

**UNION ALL**

```sql
SELECT store_id FROM sakila.inventory WHERE inventory_id IN (649, 652)
UNION ALL
SELECT store_id FROM sakila.inventory WHERE inventory_id = 650
ORDER BY store_id;
```

```text
+----------+
| store_id |
+----------+
|        1 |
|        1 |
|        2 |
+----------+
3 rows in set (0.00 sec)
```

### 保留两边未匹配的记录

MySQL 8.0 的连接语法提供左连接和右连接。要得到全外连接的结果，可以先取左连接，再用 `UNION ALL` 补上仅出现在右侧的行。这个小样本的左边是 1、2，右边是 2、3。[MySQL JOIN 手册](https://dev.mysql.com/doc/refman/8.0/en/join.html)

```sql
WITH a AS (SELECT 1 AS id UNION ALL SELECT 2),
     b AS (SELECT 2 AS id UNION ALL SELECT 3)
SELECT a.id AS left_id, b.id AS right_id
FROM a LEFT JOIN b ON a.id = b.id
UNION ALL
SELECT a.id, b.id
FROM b LEFT JOIN a ON a.id = b.id
WHERE a.id IS NULL
ORDER BY left_id, right_id;
```

```text
+---------+----------+
| left_id | right_id |
+---------+----------+
|    NULL |        3 |
|       1 |     NULL |
|       2 |        2 |
+---------+----------+
3 rows in set (0.00 sec)
```

### 用子查询表达条件

子查询可以先求出最长片长，再把该值交给外层查询。`EXISTS` 和 `NOT EXISTS` 则检查有没有对应记录。

```sql
SELECT film_id, title, length
FROM sakila.film
WHERE length = (SELECT MAX(length) FROM sakila.film)
ORDER BY film_id
LIMIT 3;

SELECT f.film_id, f.title,
       EXISTS (SELECT 1 FROM sakila.inventory AS i
               WHERE i.film_id = f.film_id) AS has_inventory
FROM sakila.film AS f
WHERE f.film_id IN (141, 182)
ORDER BY f.film_id;

SELECT f.film_id, f.title
FROM sakila.film AS f
WHERE NOT EXISTS (
    SELECT 1 FROM sakila.inventory AS i WHERE i.film_id = f.film_id
)
ORDER BY f.film_id
LIMIT 4;
```

```text
+---------+----------------+--------+
| film_id | title          | length |
+---------+----------------+--------+
|     141 | CHICAGO NORTH  |    185 |
|     182 | CONTROL ANTHEM |    185 |
|     212 | DARN FORRESTER |    185 |
+---------+----------------+--------+
3 rows in set (0.00 sec)

+---------+----------------+---------------+
| film_id | title          | has_inventory |
+---------+----------------+---------------+
|     141 | CHICAGO NORTH  |             1 |
|     182 | CONTROL ANTHEM |             1 |
+---------+----------------+---------------+
2 rows in set (0.00 sec)

+---------+----------------+
| film_id | title          |
+---------+----------------+
|      14 | ALICE FANTASIA |
|      33 | APOLLO TEEN    |
|      36 | ARGONAUTS TOWN |
|      38 | ARK RIDGEMONT  |
+---------+----------------+
4 rows in set (0.00 sec)
```

最后一条可以与前面的 `RIGHT JOIN` 结果对照。

### 用 WITH 和窗口函数做门店排行

要找每家门店租借次数最多的 3 部电影，先统计每个门店与电影组合的租借次数，再用 `ROW_NUMBER()` 在每家门店内编号。次数相同时按电影编号升序，结果可以复现。

```sql
WITH rental_counts AS (
    SELECT i.store_id, i.film_id, COUNT(*) AS rental_count
    FROM sakila.rental AS r
    INNER JOIN sakila.inventory AS i ON r.inventory_id = i.inventory_id
    GROUP BY i.store_id, i.film_id
), ranked AS (
    SELECT store_id, film_id, rental_count,
           ROW_NUMBER() OVER (
               PARTITION BY store_id ORDER BY rental_count DESC, film_id ASC
           ) AS rn
    FROM rental_counts
)
SELECT rk.store_id, rk.rn, rk.film_id, f.title, rk.rental_count
FROM ranked AS rk
INNER JOIN sakila.film AS f ON rk.film_id = f.film_id
WHERE rk.rn <= 3
ORDER BY rk.store_id, rk.rn;
```

```text
+----------+----+---------+----------------------+--------------+
| store_id | rn | film_id | title                | rental_count |
+----------+----+---------+----------------------+--------------+
|        1 |  1 |     535 | LOVE SUICIDES        |           20 |
|        1 |  2 |      55 | BARBARELLA STREETCAR |           18 |
|        1 |  3 |     489 | JUGGLER HARDLY       |           18 |
|        2 |  1 |     450 | IDOLS SNATCHERS      |           20 |
|        2 |  2 |     228 | DETECTIVE VISION     |           19 |
|        2 |  3 |     396 | HANGING DEEP         |           19 |
+----------+----+---------+----------------------+--------------+
6 rows in set (0.03 sec)
```

## 建表与增删改

按本节顺序执行即可复现。`CREATE DATABASE` 在名字被占用时会报错，复现时可以替换成自己新建的练习库名。

### 创建练习库与关联表

本节按顺序在本次新建的练习库运行。电影表和副本表都用 InnoDB。副本编号自增，电影编号通过外键引用电影表，状态由默认值与 `CHECK` 约束共同管理。

```sql
CREATE DATABASE sql_lab_20261109_9ab9e9 CHARACTER SET utf8mb4;

USE sql_lab_20261109_9ab9e9;

CREATE TABLE lab_film (
    film_id SMALLINT UNSIGNED NOT NULL,
    title VARCHAR(128) NOT NULL,
    PRIMARY KEY (film_id),
    UNIQUE KEY uq_lab_film_title (title)
) ENGINE=InnoDB;

CREATE TABLE lab_copy (
    copy_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    film_id SMALLINT UNSIGNED NOT NULL,
    store_id TINYINT UNSIGNED NOT NULL DEFAULT 1,
    status VARCHAR(12) NOT NULL DEFAULT 'ready',
    PRIMARY KEY (copy_id),
    CONSTRAINT fk_lab_copy_film FOREIGN KEY (film_id) REFERENCES lab_film (film_id),
    CONSTRAINT ck_lab_copy_status CHECK (status IN ('ready', 'rented'))
) ENGINE=InnoDB;

SHOW TABLES;
```

```text
Query OK, 1 row affected (0.02 sec)

Query OK, 0 rows affected (0.04 sec)

Query OK, 0 rows affected (0.03 sec)

+-----------------------------------+
| Tables_in_sql_lab_20261109_9ab9e9 |
+-----------------------------------+
| lab_copy                          |
| lab_film                          |
+-----------------------------------+
2 rows in set (0.00 sec)
```

### 插入指定记录和查询结果

用 `INSERT INTO ... SELECT` 复制两部电影的编号和片名，再用 `INSERT ... VALUES` 创建两份练习副本。查询确认编号和默认值由数据库填入。

```sql
INSERT INTO lab_film (film_id, title)
SELECT film_id, title FROM sakila.film WHERE film_id IN (141, 182);

INSERT INTO lab_copy (film_id) VALUES (141), (182);

SELECT * FROM lab_film ORDER BY film_id;

SELECT copy_id, film_id, store_id, status FROM lab_copy ORDER BY copy_id;
```

```text
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

+---------+----------------+
| film_id | title          |
+---------+----------------+
|     141 | CHICAGO NORTH  |
|     182 | CONTROL ANTHEM |
+---------+----------------+
2 rows in set (0.00 sec)

+---------+---------+----------+--------+
| copy_id | film_id | store_id | status |
+---------+---------+----------+--------+
|       1 |     141 |        1 | ready  |
|       2 |     182 |        1 | ready  |
+---------+---------+----------+--------+
2 rows in set (0.00 sec)
```

### 观察约束怎样拦截写入

分别尝试插入重复标题和不允许的状态。这个实验用 `INSERT IGNORE` 将这两种冲突作为警告处理，并用 `SHOW WARNINGS` 观察原因。[MySQL CHECK 约束说明](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html)

```sql
INSERT IGNORE INTO lab_film (film_id, title) VALUES (9999, 'CHICAGO NORTH');

SHOW WARNINGS;

INSERT IGNORE INTO lab_copy (film_id, status) VALUES (141, 'unknown');

SHOW WARNINGS;

SELECT COUNT(*) AS copies_after_warnings FROM lab_copy;
```

```text
Query OK, 0 rows affected, 1 warning (0.00 sec)

+---------+------+----------------------------------------------------------------------+
| Level   | Code | Message                                                              |
+---------+------+----------------------------------------------------------------------+
| Warning | 1062 | Duplicate entry 'CHICAGO NORTH' for key 'lab_film.uq_lab_film_title' |
+---------+------+----------------------------------------------------------------------+
1 row in set (0.00 sec)

Query OK, 0 rows affected, 1 warning (0.00 sec)

+---------+------+----------------------------------------------------+
| Level   | Code | Message                                            |
+---------+------+----------------------------------------------------+
| Warning | 3819 | Check constraint 'ck_lab_copy_status' is violated. |
+---------+------+----------------------------------------------------+
1 row in set (0.00 sec)

+-----------------------+
| copies_after_warnings |
+-----------------------+
|                     2 |
+-----------------------+
1 row in set (0.00 sec)
```

### 修改、回滚和提交

第一次把副本状态改为 `rented`，查询确认修改后回滚。第二次修改同一份副本并删除另一份，再提交并查询结果。`WHERE` 指明要改动的记录。

**修改后回滚**

```sql
START TRANSACTION;

UPDATE lab_copy SET status = 'rented' WHERE copy_id = 1;

SELECT copy_id, status FROM lab_copy WHERE copy_id = 1;

ROLLBACK;

SELECT copy_id, status FROM lab_copy WHERE copy_id = 1;
```

```text
Query OK, 0 rows affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

+---------+--------+
| copy_id | status |
+---------+--------+
|       1 | rented |
+---------+--------+
1 row in set (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

+---------+--------+
| copy_id | status |
+---------+--------+
|       1 | ready  |
+---------+--------+
1 row in set (0.00 sec)
```

**修改和删除后提交**

```sql
START TRANSACTION;

UPDATE lab_copy SET status = 'rented' WHERE copy_id = 1;

DELETE FROM lab_copy WHERE copy_id = 2;

COMMIT;

SELECT copy_id, film_id, status FROM lab_copy ORDER BY copy_id;
```

```text
Query OK, 0 rows affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

Query OK, 1 row affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

+---------+---------+--------+
| copy_id | film_id | status |
+---------+---------+--------+
|       1 |     141 | rented |
+---------+---------+--------+
1 row in set (0.00 sec)
```

### 修改表结构和索引

用 `ALTER TABLE` 增加备注列，并用 `SHOW COLUMNS` 验证。随后创建门店索引，从元数据确认它对应的列，再删除索引与备注列。

```sql
ALTER TABLE lab_copy ADD COLUMN note VARCHAR(80) NULL;

SHOW COLUMNS FROM lab_copy LIKE 'note';

CREATE INDEX idx_lab_copy_store ON lab_copy (store_id);

SELECT INDEX_NAME, COLUMN_NAME
FROM information_schema.STATISTICS
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'lab_copy'
  AND INDEX_NAME = 'idx_lab_copy_store';

DROP INDEX idx_lab_copy_store ON lab_copy;

ALTER TABLE lab_copy DROP COLUMN note;
```

```text
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| note  | varchar(80) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
1 row in set (0.00 sec)

Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

+--------------------+-------------+
| INDEX_NAME         | COLUMN_NAME |
+--------------------+-------------+
| idx_lab_copy_store | store_id    |
+--------------------+-------------+
1 row in set (0.00 sec)

Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

### 用视图保存查询定义

创建一个展示练习副本和片名的视图，再把定义替换为只显示待租副本。实验中剩下的一份已经是已租状态。

```sql
CREATE VIEW lab_copy_view AS
SELECT c.copy_id, f.title, c.status
FROM lab_copy AS c INNER JOIN lab_film AS f ON c.film_id = f.film_id;

SELECT * FROM lab_copy_view ORDER BY copy_id;

CREATE OR REPLACE VIEW lab_copy_view AS
SELECT c.copy_id, f.title, c.status
FROM lab_copy AS c INNER JOIN lab_film AS f ON c.film_id = f.film_id
WHERE c.status = 'ready';

SELECT * FROM lab_copy_view ORDER BY copy_id;

DROP VIEW lab_copy_view;
```

```text
Query OK, 0 rows affected (0.01 sec)

+---------+---------------+--------+
| copy_id | title         | status |
+---------+---------------+--------+
|       1 | CHICAGO NORTH | rented |
+---------+---------------+--------+
1 row in set (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Empty set (0.00 sec)

Query OK, 0 rows affected (0.01 sec)
```

### 保存查询结果、清空表和删除表

在 MySQL 中可用 `CREATE TABLE ... SELECT` 将结果写到新表。`TRUNCATE TABLE` 清空其中的记录，表仍可查询。`DROP TABLE` 删除表本身。最后按依赖顺序删掉本次创建的对象，再删除练习库。[MySQL 建表查询语句](https://dev.mysql.com/doc/refman/8.0/en/create-table-select.html)

**创建查询快照并清空**

```sql
CREATE TABLE film_snapshot AS
SELECT film_id, title FROM sakila.film WHERE film_id IN (141, 182);

SELECT film_id, title FROM film_snapshot ORDER BY film_id;

TRUNCATE TABLE film_snapshot;

SELECT COUNT(*) AS rows_after_truncate FROM film_snapshot;
```

```text
Query OK, 2 rows affected (0.02 sec)
Records: 2  Duplicates: 0  Warnings: 0

+---------+----------------+
| film_id | title          |
+---------+----------------+
|     141 | CHICAGO NORTH  |
|     182 | CONTROL ANTHEM |
+---------+----------------+
2 rows in set (0.00 sec)

Query OK, 0 rows affected (0.03 sec)

+---------------------+
| rows_after_truncate |
+---------------------+
|                   0 |
+---------------------+
1 row in set (0.00 sec)
```

**删除练习表并清理练习库**

```sql
DROP TABLE film_snapshot;

DROP TABLE lab_copy;

DROP TABLE lab_film;

SHOW TABLES;

DROP DATABASE sql_lab_20261109_9ab9e9;

SELECT COUNT(*) AS lab_schema_remaining
FROM information_schema.SCHEMATA
WHERE SCHEMA_NAME = 'sql_lab_20261109_9ab9e9';
```

```text
Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.01 sec)

Empty set (0.00 sec)

Query OK, 0 rows affected (0.01 sec)

+----------------------+
| lab_schema_remaining |
+----------------------+
|                    0 |
+----------------------+
1 row in set (0.00 sec)
```

本次把这些表结构操作放在提交后的独立步骤中。MySQL 的普通建表、改表、清空表和删表等语句会隐式提交。[MySQL 隐式提交说明](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html)

## 一条查询怎样执行

Navicat 或命令行客户端把 SQL 发给 MySQL 服务端。服务端解析语句，优化器选出读取路径，执行器按计划向 InnoDB 取数据并返回结果。以下用片长查询对照两种路径。

### 查看计划与实际读取

`EXPLAIN FORMAT=TREE` 显示计划和估算。`EXPLAIN ANALYZE` 实际运行这条查询，补充各节点输出的行数与耗时。

**查看预计执行路径**

```sql
EXPLAIN FORMAT=TREE
SELECT film_id, title, length
FROM sakila.film
WHERE length > 120
ORDER BY length DESC
LIMIT 5;
```

```text
-> Limit: 5 row(s)  (cost=103 rows=5)
    -> Sort: sakila.film.length DESC, limit input to 5 row(s) per chunk  (cost=103 rows=1000)
        -> Filter: (sakila.film.length > 120)  (cost=103 rows=1000)
            -> Table scan on film  (cost=103 rows=1000)
```

**实测按片长排序**

```sql
EXPLAIN ANALYZE
SELECT film_id, title, length
FROM sakila.film
WHERE length > 120
ORDER BY length DESC
LIMIT 5;
```

```text
-> Limit: 5 row(s)  (cost=103 rows=5) (actual time=0.385..0.385 rows=5 loops=1)
    -> Sort: sakila.film.length DESC, limit input to 5 row(s) per chunk  (cost=103 rows=1000) (actual time=0.384..0.384 rows=5 loops=1)
        -> Filter: (sakila.film.length > 120)  (cost=103 rows=1000) (actual time=0.0348..0.329 rows=457 loops=1)
            -> Table scan on film  (cost=103 rows=1000) (actual time=0.0325..0.275 rows=1000 loops=1)
```

**实测按编号排序**

```sql
EXPLAIN ANALYZE
SELECT film_id, title, length
FROM sakila.film
WHERE length > 120
ORDER BY film_id ASC
LIMIT 5;
```

```text
-> Limit: 5 row(s)  (cost=0.349 rows=1.67) (actual time=0.0172..0.023 rows=5 loops=1)
    -> Filter: (sakila.film.length > 120)  (cost=0.349 rows=1.67) (actual time=0.0167..0.0222 rows=5 loops=1)
        -> Index scan on film using PRIMARY  (cost=0.349 rows=5) (actual time=0.0143..0.0206 rows=13 loops=1)
```

| 实测步骤 | 按片长降序 | 按编号升序 |
|---|---:|---:|
| 读取记录 | 1,000 | 13 |
| 筛选节点输出 | 457 | 5 |
| 额外排序 | 有 | 无 |
| 返回记录 | 5 | 5 |

按片长排序时，这份计划读完表里的记录，再从候选中选出前 5 条。按编号排序时，主键索引直接提供编号顺序，读到第 13 条时找齐了 5 条，查询便能停止。两条 SQL 回答不同的业务问题，这组实验展示的是排序要求怎样改变读取路径。[MySQL 排序优化说明](https://dev.mysql.com/doc/refman/8.0/en/order-by-optimization.html)

## 综合练习

把筛选、连接、汇总和组内排名放到同一个问题中，再选一组回到明细核对。

### 核对每家门店的未归还排行

把全量租借排行改成未归还排行。在聚合前限定 `return_date IS NULL`，然后在每家门店内编号。这里每一行代表一家门店里一部电影的未归还笔数。

```sql
WITH open_counts AS (
    SELECT i.store_id, i.film_id, COUNT(*) AS open_rentals
    FROM sakila.rental AS r
    INNER JOIN sakila.inventory AS i ON r.inventory_id = i.inventory_id
    WHERE r.return_date IS NULL
    GROUP BY i.store_id, i.film_id
), ranked AS (
    SELECT store_id, film_id, open_rentals,
           ROW_NUMBER() OVER (
               PARTITION BY store_id ORDER BY open_rentals DESC, film_id ASC
           ) AS rn
    FROM open_counts
)
SELECT rk.store_id, rk.rn, rk.film_id, f.title, rk.open_rentals
FROM ranked AS rk
INNER JOIN sakila.film AS f ON rk.film_id = f.film_id
WHERE rk.rn <= 3
ORDER BY rk.store_id, rk.rn;
```

```text
+----------+----+---------+-----------------------+--------------+
| store_id | rn | film_id | title                 | open_rentals |
+----------+----+---------+-----------------------+--------------+
|        1 |  1 |     189 | CREATURES SHAKESPEARE |            2 |
|        1 |  2 |     205 | DANCES NONE           |            2 |
|        1 |  3 |     388 | GUNFIGHT MOON         |            2 |
|        2 |  1 |     243 | DOORS PRESIDENT       |            2 |
|        2 |  2 |       1 | ACADEMY DINOSAUR      |            1 |
|        2 |  3 |       2 | ACE GOLDFINGER        |            1 |
+----------+----+---------+-----------------------+--------------+
6 rows in set (0.01 sec)
```

独立核对时，任选结果中的一个门店和电影组合。回到租借明细，按副本编号连接库存表，数一下归还日期为空的记录是否与排行一致。

### 回到明细核对排行

拿门店 1 的 189 号电影核对，直接查出它的未归还租借编号。

```sql
SELECT r.rental_id, i.inventory_id
FROM sakila.rental AS r
INNER JOIN sakila.inventory AS i ON r.inventory_id = i.inventory_id
WHERE i.store_id = 1 AND i.film_id = 189
  AND r.return_date IS NULL
ORDER BY r.rental_id;
```

```text
+-----------+--------------+
| rental_id | inventory_id |
+-----------+--------------+
|     12524 |          857 |
|     12716 |          858 |
+-----------+--------------+
2 rows in set (0.00 sec)
```

两条租借明细与排行中的 2 笔相符。

试着独立改写需求。查询每家门店有过未归还记录的电影种数，再选一家门店核对计数的对象。

## 参考资料

- 查询执行流程参考《MySQL 实战 45 讲》第 01 讲。
- 核对 SQL 语法目录与跨数据库写法。[菜鸟教程 SQL 教程](https://www.runoob.com/sql/sql-tutorial.html)、[菜鸟教程移动版目录](https://m.runoob.com/sql/)。
- 核对库存副本与租借记录的关系。[Sakila 库存表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-inventory.html)、[Sakila 租借表](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-rental.html)。
- 核对聚合与执行计划中各数字的含义。[MySQL 聚合函数](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html)、[MySQL EXPLAIN](https://dev.mysql.com/doc/refman/8.0/en/explain.html)。
