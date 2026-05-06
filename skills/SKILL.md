# Ingest Skill — 摄入新资料到 LLM Wiki

将一个原始资料（URL 或本地文件）处理并整合到 wiki 中。

## 用法

```bash
# 从 URL 摄入
python3 skills/ingest.py --url "https://example.com/article"

# 从本地文件摄入
python3 skills/ingest.py --file /path/to/article.md

# 指定标题和作者
python3 skills/ingest.py --url "https://..." --title "文章标题" --author "作者"
```

## 流程

1. **获取内容**：抓取 URL 或读取本地文件，存入 `raw/`
2. **生成摘要**：提取关键要点，创建 `wiki/sources/<slug>.md`
3. **提取实体**：识别人物、工具、概念等，创建或更新 `wiki/entities/<entity>.md`
4. **更新主题**：关联或创建 `wiki/topics/<topic>.md`
5. **更新导航**：更新 `index.md`（统计数据 + 新页面条目）
6. **记录日志**：追加操作记录到 `log.md`
7. **Git 提交**：自动 commit

## 页面格式

参见 AGENTS.md 中的模板定义。

## 注意事项

- `raw/` 下的文件不可变，只追加不修改
- 一个源可能影响 10-15 个 wiki 页面
- 实体页已存在时只更新，不覆盖
- 优先中文撰写，技术术语保留英文
