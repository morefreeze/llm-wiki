#!/usr/bin/env python3
"""
Lint — 检查 LLM Wiki 的健康状况

Usage:
    python3 skills/lint.py              # 完整检查
    python3 skills/lint.py --fix        # 自动修复可修复的问题
    python3 skills/lint.py --quick      # 快速检查（只看统计）
"""
import argparse, re, sys
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = WIKI_ROOT / "raw"
WIKI_DIR = WIKI_ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
ENTITIES_DIR = WIKI_DIR / "entities"
TOPICS_DIR = WIKI_DIR / "topics"
SYNTHESIS_DIR = WIKI_DIR / "synthesis"
INDEX_FILE = WIKI_ROOT / "index.md"
LOG_FILE = WIKI_ROOT / "log.md"


class WikiPage:
    def __init__(self, path: Path):
        self.path = path
        self.rel = path.relative_to(WIKI_ROOT)
        self.content = path.read_text(encoding="utf-8") if path.exists() else ""
        self.title = path.stem
        self.frontmatter = {}
        self.body = self.content

        # Parse frontmatter
        parts = self.content.split('---')
        if len(parts) >= 3:
            self.body = '---'.join(parts[2:])
            for line in parts[1].strip().split('\n'):
                if ':: ' in line:
                    key, val = line.split(':: ', 1)
                    self.frontmatter[key.strip()] = val.strip()

        # Extract heading
        m = re.search(r'^#\s+(.+)', self.content, re.MULTILINE)
        if m:
            self.title = m.group(1).strip()

        # Extract [[wikilinks]]
        self.outlinks = re.findall(r'\[\[([^\]]+)\]\]', self.content)

        # Check for TODO placeholders
        self.todos = re.findall(r'（待[^）]*填写）|TODO|FIXME', self.content)

        self.category = ""
        if "sources" in str(self.rel):
            self.category = "source"
        elif "entities" in str(self.rel):
            self.category = "entity"
        elif "topics" in str(self.rel):
            self.category = "topic"
        elif "synthesis" in str(self.rel):
            self.category = "synthesis"


def lint():
    issues = []
    warnings = []
    stats = defaultdict(int)

    # Collect all pages
    all_pages = []
    for d in [SOURCES_DIR, ENTITIES_DIR, TOPICS_DIR, SYNTHESIS_DIR]:
        if d.exists():
            for f in d.glob("*.md"):
                if f.name != ".gitkeep":
                    all_pages.append(WikiPage(f))

    stats["total_pages"] = len(all_pages)

    # Build link map: page name → page
    page_map = {}
    for p in all_pages:
        page_map[p.path.stem] = p
        page_map[p.title] = p

    # Also index raw files
    raw_files = set()
    if RAW_DIR.exists():
        for f in RAW_DIR.glob("*.md"):
            raw_files.add(f.name)

    print("🔍 LLM Wiki Lint Report")
    print("=" * 50)

    for page in all_pages:
        stats[f"category_{page.category}"] += 1

        # Check 1: Empty pages (only frontmatter)
        body_stripped = page.body.strip()
        if len(body_stripped) < 50:
            issues.append(f"⚠️  {page.rel}: Page body is nearly empty ({len(body_stripped)} chars)")

        # Check 2: TODO/FIXME placeholders
        if page.todos:
            issues.append(f"📝 {page.rel}: Has {len(page.todos)} unfilled placeholder(s)")

        # Check 3: Missing frontmatter properties
        if page.category == "source":
            for prop in ["type", "source-type", "created"]:
                if prop not in page.frontmatter:
                    issues.append(f"🏷️  {page.rel}: Missing property '{prop}'")
        elif page.category == "entity":
            for prop in ["type", "created"]:
                if prop not in page.frontmatter:
                    warnings.append(f"💡 {page.rel}: Missing property '{prop}'")

        # Check 4: Broken wikilinks
        for link in page.outlinks:
            # Check if target page exists
            target_slug = link.split('/')[-1].lower().replace(' ', '-')
            found = any(
                target_slug in p.path.stem.lower() or link in p.title or link in p.path.stem
                for p in all_pages
            )
            if not found:
                # Check if it's a cross-reference to raw/ or index/log
                if link not in ["index", "log"]:
                    warnings.append(f"🔗 {page.rel}: Broken wikilink '[[{link}]]' — target page not found")

        # Check 5: Orphan pages (no inbound links)
        page_slug = page.path.stem.lower()
        inbound = sum(1 for p2 in all_pages if page_slug in p2.path.stem.lower() and p2.path != page.path)
        # Simpler: check if anyone links TO this page
        inbound = 0
        for p2 in all_pages:
            if p2.path == page.path:
                continue
            for link in p2.outlinks:
                if page.path.stem in link or page.title in link:
                    inbound += 1
                    break
        if inbound == 0 and page.category not in ("source",):
            warnings.append(f"🏝️  {page.rel}: Orphan page (no inbound links)")

    # Check 6: index.md consistency
    index_content = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    for page in all_pages:
        if page.path.stem not in index_content and page.title not in index_content:
            warnings.append(f"📋 {page.rel}: Not listed in index.md")

    # Check 7: Raw files without source summary
    for raw_name in raw_files:
        raw_slug = Path(raw_name).stem
        has_source = any(raw_slug in s.path.stem for s in all_pages if s.category == "source")
        if not has_source:
            issues.append(f"📂 raw/{raw_name}: No source summary in wiki/sources/")

    # Print results
    print(f"\n📊 Statistics:")
    print(f"   Total pages: {stats['total_pages']}")
    print(f"   Sources: {stats.get('category_source', 0)}")
    print(f"   Entities: {stats.get('category_entity', 0)}")
    print(f"   Topics: {stats.get('category_topic', 0)}")
    print(f"   Synthesis: {stats.get('category_synthesis', 0)}")

    if issues:
        print(f"\n❌ Issues ({len(issues)}):")
        for issue in issues:
            print(f"   {issue}")
    else:
        print(f"\n✅ No issues found!")

    if warnings:
        print(f"\n⚠️  Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"   {w}")

    # Suggestions
    print(f"\n💡 Suggestions:")
    if stats.get('category_entity', 0) < 5:
        print("   → Extract more entities from existing sources")
    if stats.get('category_topic', 0) < 3:
        print("   → Create cross-source topic pages")
    if stats.get('category_synthesis', 0) == 0:
        print("   → Try writing a synthesis page comparing multiple sources")
    print("   → Run `git log --oneline` to review wiki history")

    return len(issues) == 0


def main():
    parser = argparse.ArgumentParser(description="Lint the LLM Wiki")
    parser.add_argument("--quick", action="store_true", help="Quick stats only")
    args = parser.parse_args()

    if args.quick:
        # Just count
        for d in [SOURCES_DIR, ENTITIES_DIR, TOPICS_DIR, SYNTHESIS_DIR]:
            count = len([f for f in d.glob("*.md") if f.name != ".gitkeep"]) if d.exists() else 0
            print(f"{d.relative_to(WIKI_ROOT)}: {count} pages")
        return

    ok = lint()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
