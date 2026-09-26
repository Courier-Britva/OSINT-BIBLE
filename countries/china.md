# China

> Last reviewed: 2026-09-25.

#### Digital Landscape
Internet penetration ~73% (1.05 billion users, CNNIC 2024). The Great Firewall blocks Google, Facebook, X, WhatsApp, YouTube, Telegram and most Western platforms. **Baidu** is the dominant search engine (~70% market share). **WeChat** (Weixin) is the universal super-app; **Weibo** is the main microblog; **Douyin** (Chinese TikTok) dominates short video; **Xiaohongshu** (RED) is the lifestyle social platform; **Bilibili** is the youth video platform.

#### Intelligence Agency & OSINT Tradecraft
- **Civilian intelligence agency:** Ministry of State Security (**MSS**) — https://www.gov.cn
- **Military intelligence:** The **PLA Strategic Support Force (SSF)** was **disbanded in April 2024** and replaced by the **Information Support Force (ISF)** — verified by IISS: https://www.iiss.org/online-analysis/online-analysis/2024/05/chinas-new-information-support-force ⚠️ 403, and CNA: https://www.cna.org/our-media/indepth/2024/08/chinese-information-support-force. The ISF consolidates cyber, electronic warfare, and information operations.
- **OSINT unit / tradecraft:** The MSS has a Cyber Bureau responsible for offensive cyber operations. The PLA ISF conducts intelligence collection through cyber means. Both use OSINT as part of targeting for espionage.
- **Publicly verifiable tradecraft points:**
  - **Recorded Future research on Chinese AI military intelligence** — https://www.recordedfuture.com/research/artificial-eyes-generative-ai-chinas-military-intelligence — documents PLA use of generative AI for intelligence.
  - **US DoD Annual Report on Military and Security Developments Involving the PRC** (2024) — https://media.defense.gov/2024/dec/18/2003615520/-1/-1/0/military-and-security-developments-involving-the-peoples-republic-of-china-2024.pdf — public report on Chinese military capabilities including cyber.
- **What is NOT verified (myth-busting):**
  - "China uses social credit score as mass surveillance tool" — the social credit system is real but fragmented across provinces; the dystopian version portrayed in Western media is exaggerated.
  - "Every Chinese student abroad is a spy" — this is a harmful stereotype; documented cases of student informants are rare.

#### Government Sources (Verified URLs)

| Source | URL | Function | Status |
|---|---|---|---|
| National Enterprise Credit Info (gsxt) | http://www.gsxt.gov.cn | National business registry | ⚠️ 521 — slow, may require China-based access |
| creditchina.gov.cn | http://www.creditchina.gov.cn | Credit information portal | ⚠️ 412 |
| gov.cn | https://www.gov.cn | Central government portal | ✅ 200 |
| Shanghai Stock Exchange | https://www.sse.com.cn | Stock exchange filings | ⚠️ Timeout |
| Shenzhen Stock Exchange | https://www.szse.cn/index/index.html | Stock exchange filings | ⚠️ Timeout |
| China Court | https://www.chinacourt.cn/index.shtml | Court judgments (limited) | ✅ 200 |

**Note:** Most Chinese government portals are slow or block foreign IPs. Use China-based VPN (legality varies) or third-party commercial aggregators like Sayari, Sayari Graph, or ChinаFAQs.

#### Local Sources & Press
- **Domestic (state-controlled):** Xinhua, People's Daily, China Daily, Global Times, Caixin (most independent of major outlets).
- **Independent / diaspora:** China Digital Times (https://chinadigitaltimes.net), The China Project (formerly SupChina, https://thechinaproject.com, ceased operations 2024), ChinaFile (https://www.chinafile.com).
- **Investigative NGOs:** ASPI Australian Strategic Policy Institute (https://www.aspi.org.au) — Xinjiang Data Project documenting detention camps (https://xjdp.aspi.org.au).
- **OSINT community:** Chinese-speaking OSINT community is small due to censorship. GlobeTowns (Twitter/X), ChinaAnalysts.

#### Country-Specific OSINT Tools
- **National Enterprise Credit Information Publicity System (gsxt.gov.cn)** — official business registry (requires China-based access).
- **ASPI Xinjiang Data Project** — https://xjdp.aspi.org.au — database of detention camps.
- **ChinaFile Documentary Center** — https://www.chinafile.com/library — leaked documents and reports.
- **China Digital Times** — https://chinadigitaltimes.net — censored content archive.
- **Sayari Graph** (commercial) — corporate network analysis with strong China coverage.
- **Shahit.biz** (Xinjiang Victims Database) — https://shahit.biz/eng/ ✅ — database of detained Uyghurs and other minorities.

#### Legal Considerations & OPSEC
- **Cybersecurity Law (2017)** and **Data Security Law (2021)** — strict regulations on data handling, cross-border data transfer.
- **Personal Information Protection Law (PIPL, 2021)** — China's GDPR-equivalent.
- **National Intelligence Law (2017)** — requires Chinese organisations and citizens to "support, assist and cooperate with national intelligence efforts" — applies extraterritorially to Chinese nationals abroad.
- **VPN legality:** Personal VPN use is technically illegal but widely tolerated. Commercial VPN providers must register with the government; many Western VPNs are blocked.
- **OPSEC for investigators:** Do not investigate Chinese targets from within China. Use a non-Chinese VPN. Do not contact sources via WeChat (monitored). Use Signal or ProtonMail.

#### Notable Cases
- **ASPI Xinjiang Data Project (2020).** Mapped 380+ detention camps in Xinjiang using satellite imagery, government procurement documents, and leaked construction bids. URL: https://xjdp.aspi.org.au
- **Pegasus Project (2021).** Forbidden Stories and Amnesty International investigation documented use of Pegasus spyware against Uyghur activists.

#### Standard country template — 7 categories (2026-09)

##### (1) Open bases and statistics
- [National Bureau of Statistics](https://www.stats.gov.cn/) — national statistics
- [CNNIC](https://www.cnnic.net.cn/) — internet statistics and the .cn registry

##### (2) Legal and tax information
- *(enterprise credit system covered above: gsxt.gov.cn; credit portal covered above: creditchina.gov.cn)*

##### (3) Maps and cadastre
- State mapping services require a domestic account; there is no open cadastre

##### (4) Vehicles and licence plates
- No public lookup

##### (5) People: names, documents, social accounts, phones, identifiers
- *(court portal covered above: chinacourt.cn)*

##### (6) Public procurement
- [China Government Procurement](https://www.ccgp.gov.cn/) — official procurement notices
  *(HTTP 403 from automated link checks; confirm availability in a browser)*

##### (7) WHOIS and infrastructure
- *(stock exchange disclosure covered above: SSE, SZSE)*
- ICP licence lookup (beian.miit.gov.cn) is unreachable from outside the country and is pending confirmation

##### Access note
- Most Chinese government portals return 4xx to non-domestic clients while working normally from inside China. Confirm in a browser before treating any of them as dead.
