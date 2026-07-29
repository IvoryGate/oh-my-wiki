---
title: fish脚本入门
type: note
created: 2026-06-09
updated: 2026-06-09
status: doing
---

# fish脚本入门

## fish是什么

以后有空再写

## 变量

变量是存储和处理数据的基本单元

**作用域**

fish使用标志参数声明作用域：
    1. `-l` 或 `--local` 当前函数内可见
    2. `-g` 或 `--global` 当前会话可见

**赋值**

不使用`=`，使用`set`进行赋值：

```
set name "Tom"
set number 42
```

