# audit

Link-health reports for the README.

## How a report is produced

```bash
DATE=$(date -u +%F)
python3 scripts/link_checker.py README.md audit/links-status-$DATE.csv --all
```

## Files

| File | Contents |
|---|---|
| `latest.md` | Summary of the most recent check, with totals and report date |
| `links-status-YYYY-MM-DD.csv` | Every URL from that run with its status, HTTP code, final URL and source line |

The CSV is generated with `--all`, so it contains one row per unique URL inspected, including `OK` rows. Without `--all`, the checker writes only non-`OK` rows.

## Status meanings

| Status | Meaning |
|---|---|
| `OK` | The link responds without a detected redirect |
| `REDIRECT` | The link redirects elsewhere; update it to the canonical URL when appropriate |
| `BLOCKED` | HTTP 400, 401, 403, 406, 412, 429 or 444; usually a WAF, geo-restriction or login wall, not automatically a dead link |
| `NO_RESPONSE` | Timeout, DNS failure, TLS error or connection refusal; retry before changing anything |
| `DEAD` | HTTP 404, 410 or 451; the link is unavailable and should be reviewed |

## Maintenance rule

A summary is valid only for the date it was produced. Link availability depends on date, network, WAF policy and geography, so `latest.md`, the CSV and the badge in the main README should be regenerated together from a single run.
