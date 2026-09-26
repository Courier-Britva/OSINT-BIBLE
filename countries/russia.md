# Russia

> Last reviewed: 2026-09-25.

#### Digital Landscape
Internet penetration ~88% (RUNet 2024). Yandex dominates search (~65% market share). VKontakte (VK) is the dominant social network; Odnoklassniki (OK) for older demographic. Telegram is the dominant messaging app (post-2022 blocking of Western platforms). X, Facebook and Instagram are **blocked** (since March 2022). LinkedIn has been blocked since 2016.

#### Intelligence Agency & OSINT Tradecraft
- **External intelligence agency:** Sluzhba Vneshney Razvedki (**SVR**) — https://www.svr.gov.ru
- **Military intelligence:** Glavnoye Upravleniye General'nogo Shtaba (**GRU**) — https://structure.mil.ru/structure/forces/hq/general.htm
- **Domestic security service:** Federal'naya Sluzhba Bezopasnosti (**FSB**) — https://www.fsb.ru
- **OSINT unit / tradecraft:** Russian intelligence services use OSINT as part of their active measures and disinformation campaigns. The GRU's Unit 26165 (Fancy Bear / APT28) has been documented using OSINT to identify targets for spear-phishing and influence operations (Mueller Report, 2019; Bellingcat investigations).
- **Publicly verifiable tradecraft points:**
  - **CSIS Russia Shadow War analysis** — https://www.csis.org/analysis/russias-shadow-war-against-west ✅ — documents Russian intelligence tradecraft including OSINT use.
  - **CheckFirst investigation on GRU Information Operations Troops** — https://checkfirst.network/unveiling-grus-information-operations-troops-with-osint-and-medals — uses OSINT to map GRU units through medal analysis.
  - **Bellingcat Russia investigations** — https://www.bellingcat.com/tag/russia/ — multiple investigations using Russian probiv databases.
- **What is NOT verified (myth-busting):**
  - "Every Russian troll is GRU" — many influence operations are conducted by private actors (IRA, Prigozhin's networks) with loose state coordination.
  - "Russian intelligence has perfect access to all Russian data" — Russian investigators also use grey-market probiv bots, suggesting they don't have direct access to all databases.

#### Government Sources (Verified URLs)

| Source | URL | Function | Status |
|---|---|---|---|
| ФНС (Federal Tax Service) | https://www.nalog.gov.ru/rn77/ | Federal Tax Service | ✅ 200 |
| ЕГРЮЛ (Unified State Register of Legal Entities) | https://egrul.nalog.ru | Russian business registry | ⚠️ 307 redirect |
| Pravo.gov.ru | https://publication.pravo.gov.ru | Official legal portal | ⚠️ Timeout |
| Rosstat | https://www.rosstat.gov.ru | Federal statistics | ✅ 200 |
| Kremlin | https://en.kremlin.ru | Presidential administration | ✅ 200 |

#### Local Sources & Press
- **Independent press (in exile):** Meduza (https://meduza.io ✅, Riga-based), Novaya Gazeta Europe (https://novayagazeta.eu), The Moscow Times (https://www.themoscowtimes.com).
- **Investigative NGOs:** OCCRP Russian partners, Bellingcat Russia desk, Agentstvo (https://agentstvo.net).
- **OSINT community:** Russian-speaking OSINT community on Telegram (pro-Ukrainian investigative channels: InformNapalm, Cyber Resistance,.peacekeeper).

#### Country-Specific OSINT Tools
- **RuPEP** (Russian Political Exposed Persons) — https://rupep.org/en ⚠️ Timeout — database of Russian elites and PEPs.
- **Meduza** — independent Russian-language news.
- **Agentstvo** — investigative journalism.
- **InformNapalm** — OSINT community documenting Russian military actions.
- **Peacekeeper (Mirotvorets)** — Ukrainian-run database of pro-Russian actors (controversial).
- **Russian Telegram channels** — main source for real-time OSINT on Russian military, political events.

#### Legal Considerations & OPSEC
- **"Fake news" law (March 2022):** Criminalises publication of "false information" about the Russian military, punishable by up to 15 years imprisonment. This affects any OSINT investigator publishing about Russian military actions.
- **Foreign agent law:** Individuals and organizations receiving foreign support must register as "foreign agents".
- **VPN legality:** VPNs are technically legal but providers must block sites on the Russian government's blacklist. Many VPN providers have left the Russian market.
- **OPSEC:** Investigators publishing about Russia from outside should use sock puppets, never real identities. Russian intelligence has a documented history of targeting diaspora investigators.

#### Notable Cases
- **MH17 (2014).** Bellingcat used open VK posts, satellite imagery, and geolocation to attribute the downing of MH17 to Russian forces. URL: https://www.bellingcat.com/app/uploads/2015/10/MH17-The-Open-Source-Evidence-EN.pdf ✅
- **Skripal poisoning (2018).** Bellingcat identified the GRU officers behind the Salisbury poisoning using Russian leaked databases. URL: https://www.bellingcat.com/news/europe/2018/10/09/full-report-skripal-poisoning-suspect-dr-alexander-mishkin-hero-russia/
- **Navalny poisoning (2020).** Bellingcat and The Insider identified an FSB team of chemical-weapons experts that had trailed Navalny. URL: https://www.bellingcat.com/news/2020/12/14/fsb-team-of-chemical-weapon-experts-implicated-in-alexey-navalny-novichok-poisoning/
