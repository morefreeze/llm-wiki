#!/usr/bin/env python3
"""
Refactor wiki from subdirectory structure to Logseq namespace convention.

Before: wiki/entities/harness.md  →  link [[harness]]
After:  wiki/entity___harness.md  →  link [[entity/harness]]
"""
import os
import re
import subprocess
from pathlib import Path

WIKI_DIR = Path(__file__).parent / "wiki"

# Collect all page names by type
def get_pages(subdir):
    d = WIKI_DIR / subdir
    if not d.exists():
        return []
    return [f.stem for f in d.glob("*.md")]

entities = get_pages("entities")
sources  = get_pages("sources")
topics   = get_pages("topics")

print(f"Entities: {len(entities)}, Sources: {len(sources)}, Topics: {len(topics)}")

# Build replacement map: old_name -> new_wiki_name
# e.g. "harness" -> "entity/harness"
replacements = {}
for name in entities:
    replacements[name] = f"entity/{name}"
for name in sources:
    replacements[name] = f"source/{name}"
for name in topics:
    replacements[name] = f"topic/{name}"

# Sort by length descending to avoid partial substitution
sorted_names = sorted(replacements.keys(), key=len, reverse=True)

def replace_links(content):
    """Replace [[X]] with [[entity/X]], [[source/X]], or [[topic/X]] as appropriate."""
    for name in sorted_names:
        new_name = replacements[name]
        # Match [[name]] but NOT [[already/prefixed/name]] or [[entity/name]] etc.
        pattern = r'\[\[' + re.escape(name) + r'\]\]'
        replacement = f'[[{new_name}]]'
        content = re.sub(pattern, replacement, content)
    return content

# Step 1: git mv files
print("\n--- Renaming files ---")
prefix_map = {
    "entities": "entity",
    "sources":  "source",
    "topics":   "topic",
}
for subdir, prefix in prefix_map.items():
    src_dir = WIKI_DIR / subdir
    if not src_dir.exists():
        continue
    for f in sorted(src_dir.glob("*.md")):
        new_name = f"{prefix}___{f.name}"
        dst = WIKI_DIR / new_name
        result = subprocess.run(
            ["git", "mv", str(f), str(dst)],
            cwd=WIKI_DIR.parent,
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  ERROR: {result.stderr.strip()}")
        else:
            print(f"  {f.relative_to(WIKI_DIR.parent)} -> {dst.relative_to(WIKI_DIR.parent)}")

# Step 2: update links in all markdown files under the wiki root and project root
print("\n--- Updating links ---")
files_to_update = (
    list(WIKI_DIR.glob("*.md")) +  # wiki/*.md (the renamed files)
    list(WIKI_DIR.parent.glob("*.md"))  # index.md, log.md, AGENTS.md
)

for fpath in files_to_update:
    if not fpath.exists():
        continue
    original = fpath.read_text(encoding="utf-8")
    updated = replace_links(original)
    if updated != original:
        fpath.write_text(updated, encoding="utf-8")
        print(f"  Updated links in: {fpath.relative_to(WIKI_DIR.parent)}")

print("\nDone. Run 'git status' to review changes.")
