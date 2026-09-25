#!/usr/bin/env python3
"""username_check.py - checks whether a username exists on several platforms.

What it does
------------
Requests each platform's profile URL and classifies the answer:
  200         -> FOUND      the profile route responds
  404         -> NOT_FOUND  the platform states the profile does not exist
  other code  -> UNKNOWN    anti-bot block, redirect or login wall: check manually

Known limitations, observed during testing (2026-09):
  - news.ycombinator.com answers 200 even for usernames that do not exist.
  - pypi.org/user/ answers 200 for names that are not registered.
  - gitlab.com, codeberg.org and npmjs.com apply 403 or login redirects to scripts.
A FOUND result does not prove the account belongs to the person under
investigation; it only proves the route responds. No API keys are used.

Usage
-----
    python3 scripts/username_check.py torvalds
    python3 scripts/username_check.py torvalds octocat --workers 8
    python3 scripts/username_check.py torvalds --platforms github,gitlab,reddit
    python3 scripts/username_check.py --file usernames.txt --csv out.csv
    python3 scripts/username_check.py torvalds --dry-run

Example output
--------------
    $ python3 scripts/username_check.py torvalds --platforms github,keybase
    platform    username    status       url
    github      torvalds    FOUND        https://github.com/torvalds
    keybase     torvalds    FOUND        https://keybase.io/torvalds
"""
from __future__ import annotations

import argparse
import csv
import sys
from concurrent.futures import ThreadPoolExecutor

import requests
import urllib3

urllib3.disable_warnings()

PLATFORMS = {
    "github": "https://github.com/{u}",
    "gitlab": "https://gitlab.com/{u}",
    "reddit": "https://www.reddit.com/user/{u}",
    "hackernews": "https://news.ycombinator.com/user?id={u}",
    "keybase": "https://keybase.io/{u}",
    "pypi": "https://pypi.org/user/{u}/",
    "codeberg": "https://codeberg.org/{u}",
    "bitbucket": "https://bitbucket.org/{u}/",
    "npm": "https://www.npmjs.com/~{u}",
    "devto": "https://dev.to/{u}",
}
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
}
TIMEOUT = 15

def probe(url):
    """Return (status, final_url)."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT,
                            allow_redirects=True, verify=False, stream=True)
        code, final = resp.status_code, resp.url
        resp.close()
        if code == 200:
            return "FOUND", final
        if code == 404:
            return "NOT_FOUND", final
        return f"UNKNOWN({code})", final
    except Exception as exc:
        return f"ERROR({type(exc).__name__})", url

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check username presence across platforms.",
        epilog="The normal mode performs HTTP requests; --dry-run lists them without contacting anything.",
    )
    parser.add_argument("usernames", nargs="*", help="one or more usernames")
    parser.add_argument("--file", metavar="FILE", help="file with one username per line")
    parser.add_argument("--platforms", default=",".join(PLATFORMS),
                        help="comma-separated platform list (default: all)")
    parser.add_argument("--workers", type=int, default=6,
                        help="number of concurrent workers (default: 6)")
    parser.add_argument("--csv", metavar="FILE", help="write the result table to FILE")
    parser.add_argument("--dry-run", action="store_true",
                        help="list the URLs that would be checked and exit without HTTP requests")
    args = parser.parse_args(argv)

    usernames = list(args.usernames)
    if args.file:
        try:
            with open(args.file, encoding="utf-8") as fh:
                usernames += [line.strip() for line in fh if line.strip()]
        except OSError as exc:
            print(f"error: cannot read {args.file}: {exc}", file=sys.stderr)
            return 2
    if not usernames:
        parser.error("provide at least one username, or use --file")
    if args.workers < 1:
        parser.error("--workers must be at least 1")

    chosen = [p.strip() for p in args.platforms.split(",") if p.strip()]
    missing = [p for p in chosen if p not in PLATFORMS]
    if missing:
        parser.error(f"unknown platforms: {', '.join(missing)}")

    jobs = [(p, u, PLATFORMS[p].format(u=u)) for u in usernames for p in chosen]

    if args.dry_run:
        for platform, username, url in jobs:
            print(f"{platform:<12}{username:<16}{url}")
        print(f"{len(jobs)} checks would run (dry-run: no HTTP requests made)")
        return 0

    rows = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = pool.map(lambda job: probe(job[2]), jobs)
        for (platform, username, url), (status, final) in zip(jobs, results):
            rows.append({"platform": platform, "username": username,
                         "status": status, "url": final})

    print(f"{'platform':<12}{'username':<16}{'status':<18}url")
    for row in rows:
        print(f"{row['platform']:<12}{row['username']:<16}{row['status']:<18}{row['url']}")

    if args.csv:
        try:
            with open(args.csv, "w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=["platform", "username", "status", "url"])
                writer.writeheader()
                writer.writerows(rows)
        except OSError as exc:
            print(f"error: cannot write {args.csv}: {exc}", file=sys.stderr)
            return 2
        print(f"# CSV written: {args.csv}", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
