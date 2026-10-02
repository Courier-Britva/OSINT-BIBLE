"""Targeted YAML parser for sources.yml.

This handles exactly the structure used by the repo:

version: 1
sources:
  - id: foo
    name: Foo
    url: https://...
    category: bar
    country: "NL"
    region: Western Europe
    purpose: ...
    cost: free
    language: [en, nl]
    tags: [a, b, c]
    verified: "2026-09-30"
    status: ok
    readme_section: sources:company

Not a general YAML parser. Just enough for our own file.
"""
from __future__ import annotations

import re
from pathlib import Path


def _unquote(val: str) -> str:
    val = val.strip()
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]
    return val


def _split_inline_list(val: str) -> list[str]:
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [_unquote(x) for x in inner.split(",")]
    return [_unquote(val)]


def load_sources_yml(path: Path) -> list[dict]:
    sources: list[dict] = []
    current: dict | None = None
    in_list_value = None  # when a key starts a multi-line list (rare in our files)
    multiline_buffer: list[str] = []

    with path.open(encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if not line.strip() or line.strip().startswith("#"):
                continue
            # New list item: '  - id: value'
            m = re.match(r"^  - ([a-z_]+):\s*(.*?)\s*$", line)
            if m:
                if current is not None:
                    sources.append(current)
                key, val = m.group(1), m.group(2)
                current = {key: _unquote(val)} if val else {key: None}
                continue
            # Plain key: '    key: value' or '    key:' or '    key: [a, b]'
            m = re.match(r"^    ([a-z_]+):\s*(.*?)\s*$", line)
            if m and current is not None:
                key, val = m.group(1), m.group(2)
                if val == "":
                    # could be start of multi-line; rare in our file
                    current[key] = None
                elif val.startswith("["):
                    current[key] = _split_inline_list(val)
                else:
                    current[key] = _unquote(val)
                continue
            # List item under a key: '      - foo'
            m = re.match(r"^      - (.+?)\s*$", line)
            if m and current is not None:
                # Find the most recent key with value None -> it should be a list
                for k in reversed(list(current.keys())):
                    if current[k] is None:
                        current[k] = [m.group(1)]
                        break
                else:
                    # Fallback: store under 'tags' if present and None
                    if current.get("tags") is None:
                        current["tags"] = [m.group(1)]
                continue

    if current is not None:
        sources.append(current)

    return sources
