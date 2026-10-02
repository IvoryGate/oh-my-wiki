---
name: Lint
description: Oh-My-Wiki 知识库健康检查：断链、孤页、frontmatter 完整性、标签词表、index 反漂移、graph.json 一致性。当用户要求"lint / 体检 / 健康检查"，或完成一批页面增删改后做收尾校验时使用。
---

# Lint

## 原则

- **源头**（frontmatter + `[[链接]]`）是唯一事实源；index 由 Dataview 实时生成、graph.json 由 gen-graph 生成，两者**不再手工校验数字，而是校验"没有退化成手工维护"**。
- 修复分域：`raw/` 永远只读；`workspace/` 正文不可改（仅 YAML）；`wiki/` 自由修复。
- 报告输出到会话中，摘要追加到 `wiki/log.txt`。

## Workflow

1. 运行检查器（一条命令覆盖全部项目）：

   ```bash
   python .opencode/skills/lint/scripts/check.py
   ```

2. 检查项目与判定：

   | 项目 | 级别 | 说明 |
   |------|------|------|
   | 断链 | 错误 | wiki 内容页的 `[[链接]]` 无法解析（含别名）；已知历史项见脚本内 KNOWN_BROKEN |
   | frontmatter 完整性 | 错误 | 必填 title/created/updated/type/tags/description；概念页必填 domain |
   | 标签词表 | 错误 | 不同标签数必须等于脚本顶部 EXPECTED_TAG_COUNT（当前 30） |
   | index 反漂移 | 错误 | index 中出现手工统计数字或手工概念表格行（应由 Dataview 生成） |
   | graph.json 一致性 | 错误 | 调用 gen-graph 的 --check；不一致即重建 |
   | 孤页 | 警告 | 无入链的 wiki 内容页，仅列出不判失败 |

3. 修复问题（遵守修复分域），修复后重跑 `check.py` 直到全绿。
4. 将检查结果摘要（问题数、修复数、遗留警告）追加到 `wiki/log.txt`。

## 新页面最低 frontmatter 规范

```yaml
---
title: 页面标题        # 必填
created: YYYY-MM-DD    # 必填
updated: YYYY-MM-DD    # 必填
type: concept          # concept|entity|topic|howto 必填
domain: 领域名         # 概念页必填（见 wiki/index.md 分组，Dataview GROUP BY 依据）
description: 一句话    # 必填（index 表格与检索依据）
tags: [标签]           # 必填，只能取既有词表
---
```
