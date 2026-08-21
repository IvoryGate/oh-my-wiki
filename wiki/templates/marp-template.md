---
marp: true
theme: default
paginate: true
---

# Marp 演示模板

> 基于 Markdown 的幻灯片生成工具

---

## 什么是 Marp？

Marp 是一个将 Markdown 转换为幻灯片的工具：

- **简洁**：使用熟悉的 Markdown 语法
- **Obsidian 集成**：支持插件实时预览
- **导出**：PDF、PPTX、HTML

---

## 基础语法

### 分页

使用 `---` 分隔幻灯片页面

### 标题

```markdown
# 一级标题 → 幻灯片标题
## 二级标题 → 正文标题
```

### 列表

- 普通列表项
- 支持 **加粗** 和 *斜体*
- 也支持 `代码`

---

## 进阶功能

### 图片

![width:600px](attachment:image.png)

### 代码块

```python
def hello():
    print("Hello, Marp!")
```

### 两栏布局

<div class="columns">
<div>

## 左栏

- 项目 1
- 项目 2

</div>
<div>

## 右栏

- 项目 3
- 项目 4

</div>
</div>

---

## 从知识库生成演示

### 方法一：手动组装

1. 从 wiki 页面复制关键内容
2. 粘贴到 Marp 模板
3. 调整格式和分页

### 方法二：Dataview 辅助

使用 Dataview 查询生成表格，作为幻灯片素材：

```dataview
TABLE title as "概念", tags as "标签"
FROM "wiki/atoms/concepts"
LIMIT 5
```

---

## 自定义主题

在 frontmatter 中设置：

```yaml
---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
color: #333
---
```

### 可用主题

- `default`：白色背景
- `gaia`：深色背景
- `uncover`：简洁风格

---

## 导出方式

1. **Obsidian 插件**：点击 Marp 图标导出
2. **CLI**：`npx @marp-team/marp-cli slides.md -o slides.pdf`
3. **VS Code**：安装 Marp 插件

---

## 知识库演示示例

### 常用场景

- 项目汇报
- 技术分享
- 学习笔记展示
- 读书分享

---

# 谢谢！

> 使用方法：复制此模板，替换内容，启用 Obsidian Marp 插件预览
