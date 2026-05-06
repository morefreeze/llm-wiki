#!/usr/bin/env python3
"""
Query — 搜索 LLM Wiki 并返回相关页面内容

Usage:
    python3 skills/query.py "MCP 代码执行"
    python3 skills/query.py "agent efficiency" --detail
    python3 skills/query.py "渐进式发现" --full
"""
import argparse, re, sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"
INDEX_FILE = WIKI_ROOT / "index.md"


def search_files(query: str, directory: Path) -> list:
    """Search markdown files for query terms."""
    results = []
    terms = query.lower().split()
    for f in sorted(directory.rglob("*.md")):
        try:
            content = f.read_text(encoding="utf-8")
        except:
            continue
        lower = content.lower()
        score = sum(lower.count(t) for t in terms)
        if score > 0:
            # Extract title from first heading or filename
            title = f.stem
            m = re.search(r'^#\s+(.+)', content, re.MULTILINE)
            if m:
                title = m.group(1).strip()
            results.append((score, f, title, content))
    results.sort(key=lambda x: -x[0])
    return results


def extract_summary(content: str, max_chars: int = 300) -> str:
    """Extract the first meaningful paragraph after frontmatter."""
    # Skip frontmatter
    parts = content.split('---')
    body = '---'.join(parts[2:]) if len(parts) > 2 else content
    # Skip headings, find first paragraph
    lines = body.strip().split('\n')
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('|') and not stripped.startswith('---') and not stripped.startswith('```'):
            # Collect a few lines for context
            chunk = '\n'.join(lines[i:i+5]).strip()
            return chunk[:max_chars]
    return "(empty)"


def main():
    parser = argparse.ArgumentParser(description="Query the LLM Wiki")
    parser.add_argument("query", help="Search terms")
    parser.add_argument("--detail", action="store_true", help="Show summaries")
    parser.add_argument("--full", action="store_true", help="Show full content of top results")
    parser.add_argument("--max", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--dir", choices=["all", "sources", "entities", "topics"], default="all")
    args = parser.parse_args()

    # Determine search directories
    if args.dir == "all":
        dirs = [WIKI_DIR / "sources", WIKI_DIR / "entities", WIKI_DIR / "topics", WIKI_DIR / "synthesis"]
    else:
        dirs = [WIKI_DIR / args.dir]

    # Search
    all_results = []
    for d in dirs:
        if d.exists():
            all_results.extend(search_files(args.query, d))

    if not all_results:
        print(f"❌ No results for: '{args.query}'")
        print("\n💡 Try broader terms, or check index.md for all pages:")
        print(f"   cat {INDEX_FILE}")
        sys.exit(0)

    # Display results
    print(f"🔍 Results for '{args.query}' ({len(all_results)} found, showing top {min(args.max, len(all_results))}):\n")

    for i, (score, path, title, content) in enumerate(all_results[:args.max]):
        rel = path.relative_to(WIKI_ROOT)
        category = rel.parts[1] if len(rel.parts) > 2 else "wiki"
        print(f"  [{i+1}] {title}")
        print(f"      📁 {rel} (score: {score}, category: {category})")

        if args.full:
            print()
            # Print full content minus frontmatter
            parts = content.split('---')
            body = '---'.join(parts[2:]) if len(parts) > 2 else content
            print(body[:2000])
            if len(body) > 2000:
                print(f"\n      ... (truncated, {len(body)} chars total)")
        elif args.detail:
            summary = extract_summary(content)
            print(f"      📝 {summary[:200]}")

        # Show wiki links
        links = re.findall(r'\[\[([^\]]+)\]\]', content)
        if links:
            unique_links = sorted(set(links))[:8]
            print(f"      🔗 → {', '.join(unique_links)}")
        print()

    # Suggest related queries
    all_text = ' '.join(c for _, _, _, c in all_results[:5])
    terms_found = set(re.findall(r'\[\[([^\]]+)\]\]', all_text))
    if terms_found:
        print(f"💡 Related entities: {', '.join(sorted(terms_found)[:10])}")


if __name__ == "__main__":
    main()
