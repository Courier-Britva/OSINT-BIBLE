# Egypt

> Last reviewed: 2026-09-30. Every URL in this file was live-checked on that date.
> Access notes: `OK-200` = responded; `BLOCKED-403/geo` = a WAF or geo-restriction
> blocked the automated probe but the resource is reachable in a browser from
> Egypt/EU; `UNVERIFIED` = the probe failed at check time and the entry is NOT
> approved for use yet.

#### Digital Landscape

Internet penetration is high but the network is tightly regulated. Article 57 of
the 2018 Cybercrime Law (Law 175/2018) allows the state to block sites for
"threatening national security." Facebook and Messenger, WhatsApp and YouTube
are widely used; X/Twitter is widely used by journalists and analysts.
Instagram and TikTok are mainstream. Telegram is used both for news and for
dissident organising, and is intermittently throttled. Independent VPN use is
common because domestic filtering targets news and human-rights sites.
Government services are consolidated on the Digital Egypt platform. Sources for
the legal environment: Freedom House, [Egypt — Freedom on the Net 2024](https://freedomhouse.org/country/egypt/freedom-net/2024)
and [Mada Masr](https://madamasr.com) (independent).

#### Intelligence Agency & OSINT Tradecraft

- **National Security Agency (Amn al-Dawla al-Aali / NSS)** — the domestic
  intelligence service; no public website. Documented in the public literature
  on Egyptian security services and in human-rights reporting.
- **General Intelligence Service (GIS / Al-Mukhabarat al-Amma)** — foreign
  intelligence; no public website.
- **Military Intelligence (CIO)** — subordinate to the armed forces.
- **Openly documented tradecraft facts:**
  - Egypt operates the country's filter and interception infrastructure through
    Telecom Egypt and the National Telecommunications Regulatory Authority;
    independent verification is in the Freedom House report above.
  - Pegasus / spyware research that names Egypt as a customer is published by
    [Citizen Lab](https://citizenlab.ca/) — e.g. the 2017 Aks/NSO Egypt findings.
- **Myth-busting:** claims that Egypt's intelligence runs a public "OSINT unit"
  are not documented in primary sources; do not assert it.

#### Government Sources — Verified URLs

| Source | URL | Scope | Status |
|---|---|---|---|
| CAPMAS (statistics agency) | https://www.capmas.gov.eg | National statistics, census | OK-200 |
| Central Bank of Egypt | https://www.cbe.org.eg | Banking, FX, monetary data | OK-200 |
| Egyptian Exchange (EGX) | https://www.egx.com.eg | Listed-company disclosures | OK-200 |
| GAFI (investment authority) | https://www.gafi.gov.eg | Company incorporation, incentives | OK-200 |
| Invest in Egypt | https://www.investinegypt.gov.eg | Investor-facing government portal | OK-200 |
| Digital Egypt | https://digital.gov.eg | e-Government service gateway | BLOCKED/geo — live in browser |
| Egypt State Information Service | https://www.sis.gov.eg | Official press and country info | UNVERIFIED at check time |

Company registry note: no free, self-service national company registry
equivalent to UK Companies House was confirmed during this verification pass.
GAFI and the EGX disclosure pages are the practical official starting points.
**Do not add an "official company registry" URL here unless a primary source
is fetched and confirmed.**

#### Local Sources & Press

- **Independent / investigative:** [Mada Masr](https://madamasr.com) (OK-200),
  [Egypt Independent](https://www.egyptindependent.com) (OK-200).
- **Rights monitoring (verify before citing):**
  [Egypt Watch](https://egyptwatch.net) and
  [Egyptian Initiative for Personal Rights](https://egyptianinitiative.org) —
  both returned connection errors on 2026-09-30; re-verify in a browser before
  use.
- **State media:** Al-Ahram, Al-Akhbar — treat as official-voice, not
  corroborating.
- **Regional OSINT:** the [OCCRP ID database index](https://id.occrp.org/databases/)
  and [Africa Check](https://africacheck.org) cover Egyptian corporate and
  fact-check material.

#### Country-Specific OSINT Tools

- **[OCCRP Aleph](https://aleph.occrp.org/)** — cross-border corporate and leak
  records containing Egyptian entities (intermittent 503 under load; retry).
- **[ICIJ Offshore Leaks](https://offshoreleaks.icij.org/)** — Egyptian names
  in Panama / Pandora / Paradise Papers.
- **[OpenSanctions](https://www.opensanctions.org/)** — Egyptian PEP and
  sanctions entries.
- **[Open Ownership map](https://www.openownership.org/en/map/)** — check the
  current status of an Egyptian beneficial-ownership register on the live map
  before asserting it.
- **[OSINT for Countries — Egypt](https://github.com/OSINT-for-countries)** —
  community index; use as a lead generator, verify each link independently.

#### Ultimate Beneficial Ownership (UBO) Sources

| Register | URL | Coverage | Access |
|---|---|---|---|
| OpenOwnership global map | https://www.openownership.org/en/map/ | Country register status (Egypt currently has no public central UBO register) | live |
| OpenCorporates (Egypt slice) | https://opencorporates.com/companies?jurisdiction_code=eg | Companies registered in Egypt, with cross-jurisdictional officers | freemium |
| ICIJ Offshore Leaks | https://offshoreleaks.icij.org/ | Egyptian names in offshore leaks | free |

#### Public Procurement & Tendering

| Portal | URL | Scope | Access |
|---|---|---|---|
| Egyptian Government Procurement Portal (EGP) | https://egp.gov.eg/ | Federal public tenders | OK-200 |
| General Authority for Investment (GAFI) tenders | https://www.gafi.gov.eg | Investment-related tenders | OK-200 |

#### Notable Cases

- **Ousted president trial records (2011–2015)** — court documents and official
  gazette notices published in the national press; a worked example of
  building a chronology from state media plus independent reporting.
- **Egyptian airliner MS804 (2016)** — an investigation where ADS-B and
  [Flightradar24](https://www.flightradar24.com/) tracks became primary evidence.
- **Freedom of the Net country reports** — annual, citable baseline for
  censorship events ([Freedom House](https://freedomhouse.org/country/egypt/freedom-net/2024)).

#### Legal Considerations

- **Cybercrime Law 175/2018 (Art. 57)** — site blocking on national-security
  grounds.
- **Press Law and media regulation** — licensing requirements for journalism.
- **Personal data:** Egypt has no GDPR-equivalent omnibus law in force; sectoral
  rules apply. Do not assume a lawful basis for handling personal data sourced
  in Egypt.
- **OPSEC:** investigations touching state security, the military or the
  presidency carry documented risk to sources and researchers. Use
  compartmentation, non-Egyptian infrastructure and no direct contact through
  domestic platforms.
- This section is a summary of public legal sources, not legal advice.
