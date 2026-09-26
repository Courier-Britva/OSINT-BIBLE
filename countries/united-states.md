# United States

> Last reviewed: 2026-09-25.

#### Digital Landscape
Internet penetration ~93% of ~335M (Pew/ITU). Google (~88% market share), Bing, DuckDuckGo and Brave dominate search. Facebook, Instagram, X/Twitter, TikTok, Reddit, LinkedIn, Snapchat and Discord are the dominant social platforms; messaging skews to iMessage, WhatsApp, SMS (still heavily used for 2FA), Signal (journalistic) and Telegram (extremist/cyber-criminal). The US is also headquarters to most of the global OSINT-vendor stack (Palantir, Recorded Future, Sayari, Maltego ownership, Blackbird.AI, OSINT Industries).

#### Intelligence Agency & OSINT Tradecraft
- **Lead civilian foreign-intelligence agency:** Central Intelligence Agency (CIA) — https://www.cia.gov ✅
- **Lead signals-intelligence agency:** National Security Agency (NSA) — https://www.nsa.gov
- **Federal law-enforcement & domestic intel:** Federal Bureau of Investigation (FBI) — https://www.fbi.gov
- **OSINT dedicated unit:** **Open Source Enterprise (OSE)**, organisational descendant of the Open Source Center (OSC, est. 2005), itself descended from the Foreign Broadcast Information Service (FBIS, est. 1941). OSE sits under the CIA's Directorate of Digital Innovation (DDI) but coordinates across the IC through the Open Source Inter-Agency Center (OSIAC) reporting to the Director of National Intelligence.
- **Publicly verifiable tradecraft points:**
  - **ODNI Intelligence Community Open Source Strategy 2024-2026** — https://www.dni.gov/files/ODNI/documents/IC_OSINT_Strategy.pdf ⚠️ 403 to bots, downloadable in any browser. This is the first public IC document that formally elevates OSINT to a first-tier INT alongside HUMINT/SIGINT/GEOINT/MASINT.
  - **State Department OSINT Strategy 2024-2026** — corroborates the IC-wide elevation.
  - **FBIS historical lineage (declassified):** CIA Historical Review Program released the FBIS collection guide and millions of translated foreign-broadcast transcripts (1941-1995).
  - **WMD Commission (Silberman-Robb, 2005):** publicly recommended elevating OSINT — documented origin of the Open Source Center.
- **What is NOT verified (myth-busting):**
  - There is no public confirmation that the CIA runs sockpuppet armies at scale. The single documented case is the 2014 AP story on "ZunZuneo", a fake Cuban Twitter.
  - "The NSA reads every email" — actual Snowden-disclosed programs (PRISM, UPSTREAM, XKEYSCORE) targeted traffic under FISA §702; bulk domestic collection was narrowed by the USA FREEDOM Act 2015.
  - The CIA did *not* create the internet (DARPA did, 1969). CIA venture arm In-Q-Tel did fund Keyhole (→ Google Earth) and Palantir.

#### Government Sources (Verified URLs)

| Source | URL | Function | Status |
|---|---|---|---|
| SEC EDGAR | https://www.sec.gov/edgar | Corporate filings (10-K, 10-Q, 13D, S-1) | ⚠️ 403 bot-block, live in browser |
| PACER | https://pacer.uscourts.gov | Federal court records | ✅ 200 |
| OFAC SDN search | https://sanctionssearch.ofac.treas.gov | Sanctions / PEP screening | ✅ 200 |
| Data.gov | https://data.gov/ | Federal open data portal | ✅ 200 |
| FOIA.gov | https://www.foia.gov | FOIA portal & requester info | ✅ 200 |
| Federal Register | https://www.federalregister.gov | Presidential docs, rules, notices | ✅ 200 |
| USCourts.gov | https://www.uscourts.gov | Federal case statistics & finder | ✅ 200 |
| SAM.gov | https://sam.gov | Federal contractor registry + exclusions | ✅ 200 |
| FEC | https://www.fec.gov/data/ | Campaign finance data | ✅ 200 |

**State-level company registers:** The US has no federal companies register. Each state runs its own Secretary of State business search (e.g. California https://bizfileonline.sos.ca.gov/search/business, Delaware https://icis.corp.delaware.gov/ecorp/entitysearch/namesearch.aspx, New York https://apps.dos.ny.gov/publicInquiry/).

#### Local Sources & Press
- **Quality press:** New York Times, Washington Post, Wall Street Journal, ProPublica, Reuters, AP, Bloomberg, Los Angeles Times, Miami Herald, Texas Tribune, CALmatters.
- **Investigative NGOs:** ProPublica (Pulitzer-winning nonprofit), International Consortium of Investigative Journalists (ICIJ) — https://www.icij.org ✅, Center for Public Integrity, OpenSecrets (https://www.opensecrets.org ⚠️ 403, live in browser), LittleSis (https://littlesis.org ✅).
- **OSINT community:** Bellingcat (US-originated, Amsterdam-based since 2018), IntelTechniques (Michael Bazzell), OSINT Framework (Lockfale), SANS SEC497/SEC487 training, Trace Labs, OSINT Curious, The OSINT Newsletter.
- **Academic OSINT:** National Security Institute (George Mason U.), Harvard Belfer Center, Stanford Internet Observatory, Texas A&M Scowcroft Institute.

#### Country-Specific OSINT Tools
- **CourtListener** (Free Law Project) — https://www.courtlistener.com ✅ — PACER alternative for federal appellate/district opinions and the RECAP archive.
- **OpenCorporates US state data** — https://opencorporates.com — pulls from 50+ state SOS feeds.
- **OpenSanctions US datasets** — https://www.opensanctions.org/datasets/ ✅ — FBI Most Wanted, OFAC SDN, BIS Denied Persons, SAM exclusions.
- **Sayari** — https://sayari.com ⚠️ — commercial, strong on corporate-network construction.
- **Palantir Gotham / Foundry** — used by US defense & law-enforcement.
- **Maltego** — https://www.maltego.com ✅ — graph-based link analysis.
- **Recorded Future** — https://www.recordedfuture.com ⚠️ — commercial threat intel.
- **OSINT Industries** — https://osint.industries — email/username → linked accounts.

#### Legal Considerations
- **First Amendment** protects newsgathering broadly but is not absolute.
- **Computer Fraud and Abuse Act (CFAA), 18 U.S.C. § 1030** — https://www.law.cornell.edu/uscode/text/18/1030 ✅. Post-*Van Buren v. United States* (2021) the Supreme Court narrowed "exceeds authorised access" but ToS-violation scraping with a login remains risky.
- **Electronic Communications Privacy Act (ECPA)** and **Stored Communications Act (SCA)** govern interception and access to stored comms.
- **FOIA (1966)** — https://www.foia.gov ✅ — the strongest federal transparency lever. State public-records laws vary (California PRA, Texas PIA, Florida Sunshine Law).
- **State privacy laws:** California CCPA/CPRA (2020/2023), Virginia VCDPA, Colorado CPA, Connecticut CTDPA, Utah UCPA, Texas TDPSA (2024).
- **No federal GDPR-equivalent.** Investigators publishing personal data of US persons are largely constrained by defamation, false-light and tortious-interference law.
- **SLAPP risk:** 32 states have anti-SLAPP statutes (California, Texas, New York, Florida among the strongest).
- **State secret / classification:** 18 U.S.C. § 798 (Espionage Act) relevant if an investigator receives leaked classified docs.
- **OPSEC:** US-based investigators can be subpoenaed by grand jury. Border searches under 8 CFR 287 — devices can be searched at the US border without reasonable suspicion.

#### Notable Cases
- **MH17 (2014, Netherlands-led but Bellingcat-driven).** Bellingcat used open VK posts, satellite imagery, geolocation of a Buk TELAR transport and matched social-media timestamps to attribute the downing of MH17 to Russian forces. Methodology PDF: https://www.bellingcat.com/app/uploads/2015/10/MH17-The-Open-Source-Evidence-EN.pdf ✅. The case is the textbook example of OSINT-as-evidence (used by the JIT and cited in the Dutch court verdict in absentia against Russians Girkin/Dubinsky/Pulatkij in 2022).
- **1MDB kleptocracy asset recovery (2016-2024).** DOJ Civil forfeiture complaints — https://en.wikipedia.org/wiki/1Malaysia_Development_Berhad_scandal — used leaked bank records, SEC filings, real-estate records from NYC registry and shell-company filings from BVI/Seychelles.
- **Boston Marathon bombing misidentification (2013).** The cautionary counter-example: Reddit/Twitter crowd-sleuths wrongly identified missing student Sunil Tripathi as a suspect; he was later found dead by suicide. Teaching case on confirmation bias in OSINT.
- **January 6 Capitol riot (2021).** Sedition Hunters (https://seditionhunters.org) and the FBI used Parler video metadata and facial matches to identify >1,400 suspects.

#### Standard country template — 7 categories (2026-09)

##### (1) Open bases and statistics
- [U.S. Census Bureau](https://www.census.gov/) — official national statistics
- [GovInfo](https://www.govinfo.gov/) — official publications of the federal government
  *(official statistics portal covered above: Data.gov)*

##### (2) Legal and tax information
- [Regulations.gov](https://www.regulations.gov/) — federal rulemaking dockets and public comments
  *(company filings covered above: SEC EDGAR, OpenCorporates)*

##### (3) Maps and cadastre
- No single federal cadastre: parcel and cadastral data are held at county and state level

##### (4) Vehicles and licence plates
- No public lookup: registration data is state-held and not queryable nationally

##### (5) People: names, documents, social accounts, phones, identifiers
- No national public people register: searches are per-state and per-court, not centralised
  *(court records covered above: CourtListener, PACER, USCourts)*

##### (6) Public procurement
- [USAspending](https://www.usaspending.gov/) — federal awards and spending

##### (7) WHOIS and infrastructure
- Pending: the ARIN WHOIS interface previously linked no longer resolves; substitute not yet confirmed
