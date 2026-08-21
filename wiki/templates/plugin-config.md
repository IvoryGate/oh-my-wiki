# Obsidian 插件配置指南

> 针对知识库优化的插件设置说明

---

## 已安装插件一览

| 插件 | 版本 | 用途 | 状态 |
|------|------|------|------|
| **Dataview** | 0.5.68 | 动态查询与统计 | ✅ 已配置 |
| **Homepage** | 4.4.0 | 启动打开首页 | ✅ 已配置 |
| **Marp Slides** | 0.46.1 | 幻灯片生成 | ✅ 已配置 |
| **BRAT** | - | 主题管理 | 默认配置 |

---

## Dataview 配置

### 核心设置

| 设置项 | 值 | 说明 |
|--------|-----|------|
| 启用内联查询 | ✅ | 支持 `= ...` 语法 |
| 启用 JavaScript | ✅ | 支持 `$= ...` 语法 |
| 刷新间隔 | 2500ms | 自动更新查询结果 |
| 日期格式 | yyyy-MM-dd | 与知识库 frontmatter 一致 |

### 常用查询语法

**列出所有概念**：
```dataview
TABLE title, created, updated
FROM "wiki/atoms/concepts"
SORT updated DESC
```

**按标签筛选**：
```dataview
LIST
FROM "wiki"
WHERE contains(tags, "AI")
```

**最近更新**：
```dataview
TABLE title, type, updated
FROM "wiki"
WHERE type AND updated >= date(today) - dur(7 days)
SORT updated DESC
```

---

## Homepage 配置

### 核心设置

| 设置项 | 值 | 说明 |
|--------|-----|------|
| 默认页面 | `wiki/index` | 启动时打开知识库索引 |
| 启动时打开 | ✅ | 自动加载首页 |
| 打开模式 | 替换所有笔记 | 清爽启动 |
| 刷新 Dataview | ✅ | 确保数据最新 |

### 使用方式

- 启动 Obsidian → 自动打开 `wiki/index.md`
- 点击侧边栏首页图标 → 快速返回

---

## Marp Slides 配置

### 核心设置

| 设置项 | 值 | 说明 |
|--------|-----|------|
| 主题 | default | 白色背景 |
| 尺寸 | 16:9 | 标准宽屏 |
| 页码 | ✅ | 显示页码 |
| 导出目录 | `export/` | 导出文件位置 |

### 使用方式

1. 创建 Marp 文档：
   ```markdown
   ---
   marp: true
   paginate: true
   ---
   
   # 幻灯片标题
   
   ---
   
   ## 第二页
   内容...
   ```

2. 预览：点击 Marp 图标
3. 导出：命令面板 → "Marp: Export to PDF/PPTX"

---

## CSS 片段

### oh-my-wiki.css

位置：`.obsidian/snippets/oh-my-wiki.css`

**启用方式**：
1. 设置 → 外观 → CSS 代码片段
2. 刷新
3. 启用 `oh-my-wiki`

**功能**：
- Dataview 表格美化
- 双向链接样式增强
- 标签样式优化
- 页面类型标识（概念/实体/主题）
- 响应式布局
- 打印优化

---

## 核心插件配置

已启用的核心插件：

| 插件 | 状态 | 说明 |
|------|------|------|
| 文件浏览器 | ✅ | 导航 |
| 全局搜索 | ✅ | 快速查找 |
| 快速切换 | ✅ | Ctrl/Cmd + O |
| 关系图谱 | ✅ | 可视化知识关联 |
| 反向链接 | ✅ | 查看入链 |
| 出链 | ✅ | 查看出链 |
| 标签面板 | ✅ | 标签导航 |
| 日记 | ✅ | 日常记录 |
| 模板 | ✅ | 模板插入 |
| 书签 | ✅ | 收藏页面 |
| 大纲 | ✅ | 文档结构 |
| 字数统计 | ✅ | 写作辅助 |
| 幻灯片 | ✅ | 基础演示 |
| 随机笔记 | ✅ | 发现孤立内容 |
| 画布 | ✅ | 可视化思考 |
| 工作区 | ✅ | 布局保存 |

---

## 推荐快捷键

| 功能 | 默认快捷键 | 建议 |
|------|-----------|------|
| 快速切换 | Ctrl/Cmd + O | 保持 |
| 全局搜索 | Ctrl/Cmd + Shift + F | 保持 |
| 命令面板 | Ctrl/Cmd + P | 保持 |
| 插入模板 | - | 建议 Ctrl/Cmd + T |
| 切换预览 | Ctrl/Cmd + E | 保持 |
| 首页 | - | 建议 Ctrl/Cmd + H |

---

## 使用流程建议

### 启动 Obsidian 时

```
1. 自动打开 wiki/index.md
2. Dataview 查询自动刷新
3. 查看最近更新和统计数据
```

### 入库新资料时

```
1. 将资料放入 raw/ 对应目录
2. 唤起 Agent 处理
3. Agent 更新 wiki 页面
4. Dataview 自动反映变化
```

### 查询知识时

```
1. 在 wiki/index.md 查看概览
2. 或使用 Ctrl/Cmd + O 快速切换
3. 或使用 Ctrl/Cmd + Shift + F 全局搜索
4. 查看关系图谱发现关联
```

### 生成演示时

```
1. 告诉 Agent 要演示的主题
2. Agent 生成 Marp 格式文档
3. 使用 Marp Slides 预览和导出
```

---

*配置更新时间: 2026-04-17*
