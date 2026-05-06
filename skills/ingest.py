#!/usr/bin/env python3
"""
Ingest — 摄入新资料到 LLM Wiki

按 Karpathy LLM Wiki 模式：
1. 抓取内容 → 存入 _raw/（不可变）
2. 创建 source 摘要骨架 → wiki/sources/
3. 去重检查（URL/标题）
4. 更新 log.md

Usage:
    python3 skills/ingest.py --url "https://example.com/article"
    python3 skills/ingest.py --url "https://..." --title "标题" --author "作者"
    python3 skills/ingest.py --file /path/to/article.md
"""
import argparse, hashlib, json, os, re, subprocess, sys
from datetime import datetime
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = WIKI_ROOT / "_raw"
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
    sources = [f for f in SOURCES_DIR.glob("*.md") if f.name != ".gitkeep"]
    entities = [f for f in ENTITIES_DIR.glob("*.md") if f.name != ".gitkeep"]
    topics = [f for f in TOPICS_DIR.glob("*.md") if f.name != ".gitkeep"]
    synthesis = [f for f in (WIKI_DIR / "synthesis").glob("*.md") if f.name != ".gitkeep"]
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


def find_existing_source(url: str = None, title: str = None) -> Path | None:
    """Check if a source already exists by URL or title in _raw/ or wiki/sources/."""
    # Check by URL in _raw files
    if url:
        for f in RAW_DIR.glob("*.md"):
            content = f.read_text(encoding="utf-8", errors="replace")
            if url in content:
                return f
    # Check by slug in wiki/sources
    if title:
        slug = slugify(title)
        candidate = SOURCES_DIR / f"{slug}.md"
        if candidate.exists():
            return candidate
    return None


def fetch_url_content(url: str) -> tuple[str, str]:
    """Fetch URL and return (text_content, html_title)."""
    import urllib.request
    print(f"Fetching: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw_html = resp.read().decode("utf-8", errors="replace")

    # Extract title from HTML
    title = ""
    m = re.search(r'<title>(.*?)</title>', raw_html)
    if m:
        title = m.group(1).split('\\')[0].split('|')[0].strip()

    # Simple HTML → text
    raw_html = re.sub(r'<script[^>]*>.*?</script>', '', raw_html, flags=re.DOTALL)
    raw_html = re.sub(r'<style[^>]*>.*?</style>', '', raw_html, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', raw_html)
    text = re.sub(r'\s+', ' ', text).strip()
    return text, title


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

    # Ensure directories exist
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Get content
    raw_content = ""
    title = args.title or ""

    if args.url:
        # Dedup check by URL
        existing = find_existing_source(url=args.url)
        if existing:
            print(f"⚠️  URL already ingested: {existing}")
            print(f"    Skipping duplicate ingest.")
            return
        raw_content, html_title = fetch_url_content(args.url)
        if not title:
            title = html_title or "untitled"
    else:
        raw_path = Path(args.file)
        raw_content = raw_path.read_text(encoding="utf-8")
        if not title:
            title = raw_path.stem

    slug = slugify(title)

    # Dedup check by slug
    existing_source = SOURCES_DIR / f"{slug}.md"
    if existing_source.exists():
        print(f"⚠️  Source already exists: {existing_source}")
        print(f"    Use a different --title to ingest as a new source.")
        return

    # Step 2: Save to _raw/ (immutable)
    raw_path = RAW_DIR / f"{slug}.md"
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"- URL: {args.url or 'local file'}\n")
        if args.author:
            f.write(f"- Author: {args.author}\n")
        f.write(f"- Date: {today}\n")
        f.write(f"- Ingested: {datetime.now().isoformat()}\n\n")
        f.write(raw_content)
    print(f"✓ Raw saved: _raw/{slug}.md")

    # Step 3: Create source summary skeleton
    with open(existing_source, "w", encoding="utf-8") as f:
        author_line = f"author:: [[{args.author}]]" if args.author else ""
        f.write(f"""---
type:: Source
source-type:: {args.source_type}
{author_line}
date:: {today}
url:: {args.url or ''}
raw-file:: _raw/{slug}.md
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
    print(f"✓ Source skeleton: wiki/sources/{slug}.md")

    # Step 4: Update log
    append_log(f"{title}")
    print(f"✓ Log updated")

    # Step 5: Summary
    pages = count_pages()
    print(f"\n📊 Wiki: {pages['total']} pages ({pages['sources']}S / {pages['entities']}E / {pages['topics']}T)")
    print(f"\n⏭️  Next: 让 LLM 填写 source 摘要，提取实体，更新 topic 页面")


if __name__ == "__main__":
    main()
