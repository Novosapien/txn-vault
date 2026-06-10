#!/usr/bin/env python3
"""Wikilink integrity checker for the content/ knowledge graph.

Every [[wikilink]] must resolve to an existing markdown file (matched by
shortest-path basename, the Obsidian convention used in this vault).

Skips fenced code blocks so mermaid node syntax like `A2A[[A2A Endpoint]]`
is not mistaken for a wikilink.

Usage: python3 scripts/check-wikilinks.py [content_dir]
Exit code 0 if all links resolve, 1 otherwise.
"""
import os
import re
import sys
import glob

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
FENCE = re.compile(r"^\s*(```|~~~)")


def basenames(content_dir):
    index = {}
    for path in glob.glob(os.path.join(content_dir, "**", "*.md"), recursive=True):
        base = os.path.splitext(os.path.basename(path))[0]
        index.setdefault(base, []).append(path)
    return index


def links_in(path):
    """Yield (line_no, target) for every wikilink outside fenced code blocks."""
    in_fence = False
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for m in WIKILINK.finditer(line):
                yield i, m.group(1).strip()


def main():
    content_dir = sys.argv[1] if len(sys.argv) > 1 else "content"
    index = basenames(content_dir)

    broken = []
    for path in glob.glob(os.path.join(content_dir, "**", "*.md"), recursive=True):
        for line_no, target in links_in(path):
            base = os.path.splitext(os.path.basename(target))[0]
            if base not in index:
                broken.append((path, line_no, target))

    dupes = {b: ps for b, ps in index.items() if len(ps) > 1}

    if broken:
        print(f"BROKEN WIKILINKS: {len(broken)}")
        for path, line_no, target in broken:
            print(f"  {path}:{line_no} -> [[{target}]]")
    else:
        print("OK: all wikilinks resolve to an existing file.")

    if dupes:
        print("\nAMBIGUOUS basenames (same name in multiple files):")
        for base, paths in dupes.items():
            print(f"  {base}: {paths}")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
