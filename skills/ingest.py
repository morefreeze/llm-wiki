#!/usr/bin/env python3
"""
Ingest — 摄入新资料到 LLM Wiki

Usage:
    python3 skills/ingest.py --url "https://example.com/article"
    python3 skills/ingest.py --file /path/to/article.md --title "标题" --author "作者"
"""
import argparse, json, os, re, subprocess, sys
from datetime import datetime
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = WIKI_ROOT / "raw"
WIKI_DIR = WIKI_ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
ENTITIES_DIR = WIKI_DIR / "entities"
TOPICS_DIR = WIKI_DIR / "topics"
INDEX_FILE = WIKI_ROOT / "index.md"
LOG_FILE = WIKI_ROOT / "log.md"


def slugify(text: str) -> str:
    """Convert title to filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s\u4e00-\u9fff-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = text[:80].rstrip('-')
    return text or "untitled"


def count_pages() -> dict:
    """Count current wiki pages."""
    sources = list(SOURCES_DIR.glob("*.md"))
    entities = list(ENTITIES_DIR.glob("*.md"))
    topics = list(TOPICS_DIR.glob("*.md"))
    synthesis = list((WIKI_DIR / "synthesis").glob("*.md"))
    return {
        "total": len(sources) + len(entities) + len(topics) + len(synthesis),
        "sources": len(sources),
        "entities": len(entities),
        "topics": len(topics),
        "synthesis": len(synthesis),
    }


def append_log(entry: str):
    """Append an entry to log.md."""
    today = datetime.now().strftime("%Y-%m-%d")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n## [{today}] ingest | {entry}\n")


def main():
    parser = argparse.ArgumentParser(description="Ingest a source into LLM Wiki")
    parser.add_argument("--url", help="URL to fetch")
    parser.add_argument("--file", help="Local file to ingest")
    parser.add_argument("--title", help="Override title")
    parser.add_argument("--author", help="Author name")
    parser.add_argument("--source-type", default="article", help="article|paper|video|book")
    args = parser.parse_args()

    if not args.url and not args.file:
        parser.error("Must provide --url or --file")

    today = datetime.now().strftime("%Y-%m-%d")

    # Step 1: Get content
    raw_content = ""
    title = args.title or "untitled"

    if args.url:
        import urllib.request
        print(f"Fetching: {args.url}")
        req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw_html = resp.read().decode("utf-8", errors="replace")
        # Simple HTML to text
        raw_html = re.sub(r'<script[^>]*>.*?</script>', '', raw_html, flags=re.DOTALL)
        raw_html = re.sub(r'<style[^>]*>.*?</style>', '', raw_html, flags=re.DOTALL)
        raw_content = re.sub(r'<[^>]+>', ' ', raw_html)
        raw_content = re.sub(r'\s+', ' ', raw_content).strip()
        # Extract title from HTML
        m = re.search(r'<title>(.*?)</title>', raw_html)
        if m and not args.title:
            title = m.group(1).split('\\')[0].split('|')[0].strip()
        slug = slugify(title)
        raw_path = RAW_DIR / f"{slug}.md"
    else:
        raw_path = Path(args.file)
        raw_content = raw_path.read_text(encoding="utf-8")
        if not args.title:
            title = raw_path.stem
        slug = slugify(title)

    # Step 2: Save to raw/
    if args.url:
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"- URL: {args.url}\n")
            if args.author:
                f.write(f"- Author: {args.author}\n")
            f.write(f"- Date: {today}\n\n")
            f.write(raw_content)
        print(f"✓ Raw saved: {raw_path}")
    else:
        print(f"✓ Using existing file: {raw_path}")

    # Step 3: Create source summary skeleton
    source_path = SOURCES_DIR / f"{slug}.md"
    if not source_path.exists():
        author_prop = f"author:: [[{args.author}]]" if args.author else ""
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(f"""---
type:: Source
source-type:: {args.source_type}
{author_prop}
date:: {today}
url:: {args.url or ''}
raw-file:: {raw_path.relative_to(WIKI_ROOT)}
created:: [[{today}]]
---
# {title}

## 一句话总结
> （待 LLM 填写）

## 关键要点
1. （待 LLM 填写）

## 详细笔记
（待 LLM 填写）

## 与其他资料的关系
（待 LLM 填写）

## 引用此资料的页面
（待 LLM 填写）
""")
        print(f"✓ Source skeleton: {source_path}")
    else:
        print(f"→ Source exists: {source_path}")

    # Step 4: Update log
    append_log(title)
    print(f"✓ Log updated")

    # Step 5: Print summary
    pages = count_pages()
    print(f"\n📊 Wiki stats: {pages['total']} pages ({pages['sources']} sources, {pages['entities']} entities, {pages['topics']} topics)")
    print(f"\n⏭️  Next steps:")
    print(f"   1. Read raw content and fill in source summary: {source_path}")
    print(f"   2. Extract entities → create/update in {ENTITIES_DIR}/")
    print(f"   3. Update related topics in {TOPICS_DIR}/")
    print(f"   4. Update {INDEX_FILE}")
    print(f"   5. git commit")


if __name__ == "__main__":
    main()
