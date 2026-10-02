#!/usr/bin/env python3
"""build_readme.py - renders registry-driven tables into README.md.

The README keeps a marker pair per section:

    <!-- AUTOGEN:sources:company:START -->
    ...generated table...
    <!-- AUTOGEN:sources:company:END -->

This script replaces everything between the markers, so the curated prose stays
hand-written and only the link tables are generated (no more stale links).

Usage:
    python3 scripts/build_readme.py                     # write README.md
    python3 scripts/build_readme.py --check             # exit 1 if out of date
    python3 scripts/build_readme.py --readme README.md --data data/sources.yml
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: python3 -m pip install pyyaml")

START = "<!-- AUTOGEN:{key}:START -->"
END = "<!-- AUTOGEN:{key}:END -->"


def render_table(rows: list[dict]) -> str:
    lines = ["| Source | Purpose | Access | Verified |",
             "|---|---|---|---|"]
    for s in sorted(rows, key=lambda x: x["name"].lower()):
        cost = s.get("cost", "-")
        lines.append(
            f"| [{s['name']}]({s['url']}) | {s.get('purpose', '')} | {cost} | {s.get('verified', '')} |"
        )
    return "\n".join(lines)


def build(readme: str, sources: list[dict]) -> tuple[str, int]:
    """Return (new_readme, number_of_blocks_updated)."""
    updated = 0
    for m in list(re.finditer(r"<!-- AUTOGEN:(sources:[\w-]+):START -->", readme)):
        key = m.group(1)
        rows = [s for s in sources if s.get("readme_section") == key and not s.get("deprecated")]
        if not rows:
            continue
        block_re = re.compile(
            re.escape(START.format(key=key)) + r".*?" + re.escape(END.format(key=key)),
            re.DOTALL,
        )
        replacement = (START.format(key=key) + "\n" + render_table(rows) + "\n"
                       + END.format(key=key))
        readme, n = block_re.subn(lambda _: replacement, readme, count=1)
        updated += n
    return readme, updated


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--data", default="data/sources.yml")
    ap.add_argument("--check", action="store_true",
                    help="do not write; fail if the README is out of date")
    args = ap.parse_args()

    readme_path = Path(args.readme)
    original = readme_path.read_text(encoding="utf-8")
    doc = yaml.safe_load(Path(args.data).read_text(encoding="utf-8")) or {}
    new, updated = build(original, doc.get("sources") or [])

    if updated == 0:
        print("no AUTOGEN blocks found - add marker pairs to the README first")
        return 1 if args.check else 0
    if new == original:
        print(f"README already up to date ({updated} block(s))")
        return 0
    if args.check:
        print(f"README out of date - {updated} block(s) need regeneration")
        return 1
    readme_path.write_text(new, encoding="utf-8")
    print(f"README updated - {updated} block(s) regenerated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
