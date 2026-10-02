# Security Policy

The OSINT-BIBLE registry lists publicly available sources and tools for lawful
open-source intelligence work. The repository is documentation and tooling, not
a service that processes user data.

## Reporting a problem with a listed tool or source

If you believe a tool, dataset or registry listed in this repository:

- facilitates doxxing, stalking or harassment,
- sells or trades personal data outside lawful bases,
- evades authentication or bypasses lawful access controls,
- has changed ownership or terms in a way that creates new risk, or
- is otherwise unsafe to include in an OSINT reference,

open a GitHub issue with the `security-review` label, or email the maintainer
listed in `CITATION.cff`. Include the entry id (for example `osint-industries`
from `data/tools.json` or `kvk-handelsregister` from `data/sources.yml`) so the
record can be located.

## Reporting a vulnerability in this repository

For vulnerabilities in the repository's own code (Python scripts under
`scripts/`, GitHub workflows, schema files), open a GitHub issue with the
`security` label or email the maintainer. Do not include proof-of-concept
content that could itself be harmful.

## Scope

This policy covers:

- the `data/` and `schema/` files,
- the `scripts/` Python tooling,
- the GitHub workflows under `.github/workflows/`,
- generated artifacts produced by `scripts/build_readme.py`.

It does **not** cover external resources that are merely linked from this
repository; those resources are governed by their own security policies.
