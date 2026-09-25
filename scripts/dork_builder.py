#!/usr/bin/env python3
"""dork_builder.py - builds advanced search queries for one or more domains.

What it does
------------
Renders passive-reconnaissance query templates for Google, Bing or DuckDuckGo.
It performs no network requests: it only prints text. DuckDuckGo does not
reliably support the inurl: and intitle: operators, so the DuckDuckGo set uses
equivalent site: and quoted-phrase variants.

Usage
-----
    python3 scripts/dork_builder.py --domain example.com --output google
    python3 scripts/dork_builder.py --domain example.com --output all
    python3 scripts/dork_builder.py -d a.com -d b.com --output ddg
    python3 scripts/dork_builder.py --domain example.com --save dorks.txt

Example output
--------------
    $ python3 scripts/dork_builder.py -d example.com --output all | wc -l
    38
"""
from __future__ import annotations

import argparse
import sys

GOOGLE = [
    'site:{d} filetype:pdf | filetype:doc | filetype:docx | filetype:xls | filetype:xlsx',
    'site:{d} filetype:sql | filetype:bak | filetype:log | filetype:env',
    'site:{d} inurl:login | inurl:admin | inurl:portal | inurl:dashboard',
    'site:{d} intitle:"index of"',
    'site:{d} inurl:api | inurl:graphql | inurl:swagger | inurl:openapi',
    'site:{d} inurl:backup | inurl:old | inurl:test | inurl:staging | inurl:dev',
    'site:{d} "confidential" | "internal use only"',
    'site:{d} "password" | "passwd" | "pwd" filetype:txt | filetype:conf',
    'site:{d} (ext:owasp | ext:mdb | ext:key | ext:pem | ext:ppk)',
    'site:{d} inurl:.git | inurl:.svn | inurl:.ds_store',
    'site:{d} inurl:wp-content | inurl:wp-admin',
    'site:{d} -inurl:www',
    'site:{d} "@{d}" filetype:pdf',
    'site:{d} "index of /" "parent directory"',
]
BING = [
    'site:{d} filetype:pdf',
    'site:{d} filetype:xlsx | filetype:docx | filetype:pptx',
    'site:{d} inurl:login | inurl:signin | inurl:admin',
    'site:{d} intitle:"index of"',
    'site:{d} inbody:"api key" | inbody:"apikey" | inbody:"secret"',
    'site:{d} inurl:api | inurl:rest | inurl:swagger',
    'site:{d} ext:sql | ext:bak | ext:log',
    'site:{d} contains:"internal"',
]
DDG = [
    '{d} filetype:pdf',
    '{d} filetype:xlsx',
    '{d} site:{d} login admin',
    '{d} "index of" "{d}"',
    '{d} site:{d} "api key"',
    'site:{d} "swagger" OR "openapi"',
    'site:{d} "backup" OR "old" OR "test"',
    'site:{d} "parent directory"',
]
ENGINES = {"google": GOOGLE, "bing": BING, "ddg": DDG}

def build(domains, engines):
    blocks = []
    for domain in domains:
        for engine in engines:
            templates = ENGINES[engine]
            blocks.append(f"# {engine.upper()} dorks for {domain}  ({len(templates)} queries)\n")
            for template in templates:
                blocks.append(template.format(d=domain))
            blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"

def main(argv=None):
    parser = argparse.ArgumentParser(description="Build passive-reconnaissance dorks for domains.")
    parser.add_argument("-d", "--domain", action="append", required=True, dest="domains",
                        help="domain to build queries for; repeat the flag for several domains")
    parser.add_argument("--output", choices=["google", "bing", "ddg", "all"], default="google",
                        help="target engine (default: google)")
    parser.add_argument("--save", metavar="FILE",
                        help="write the result to FILE instead of only printing it")
    args = parser.parse_args(argv)

    if not args.domains:
        parser.error("at least one --domain is required")

    engines = list(ENGINES) if args.output == "all" else [args.output]
    text = build(args.domains, engines)
    sys.stdout.write(text)

    if args.save:
        try:
            with open(args.save, "w", encoding="utf-8") as fh:
                fh.write(text)
        except OSError as exc:
            print(f"error: cannot write {args.save}: {exc}", file=sys.stderr)
            return 2
        print(f"# saved to {args.save}", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
