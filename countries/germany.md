# Germany

> Last reviewed: 2026-09-25.

#### Digital Landscape
Internet penetration ~93% (Bitkom 2024). Google dominates search; alternative privacy-focused search engines (Ecosia, Metager) have notable market share. WhatsApp is the dominant messaging app; Telegram is notably stronger in Germany than in other Western European countries (used by political fringe, anti-vax, Reichsbürger). X and LinkedIn are the main professional networks.

#### Intelligence Agency & OSINT Tradecraft
- **Foreign intelligence agency:** Bundesnachrichtendienst (**BND**) — https://www.bnd.bund.de
- **Domestic intelligence agency (Verfassungsschutz):** Bundesamt für Verfassungsschutz (**BfV**) — https://www.verfassungsschutz.de
- **Military intelligence:** Militärischer Abschirmdienst (**MAD**) — https://www.bmvg.de/de
- **OSINT unit / tradecraft:** BND has an OSINT branch (Open Source Intelligence), but its work is classified. The BfV publishes the annual *Verfassungsschutzbericht* (Constitutional Protection Report) which uses OSINT analysis of extremism and disinformation.
- **Publicly verifiable tradecraft points:**
  - BND's legal basis is the **BND-Gesetz (BND Act, 2020)** — https://www.gesetze-im-internet.de/bndg/, which explicitly regulates OSINT collection.
  - BfV publishes *Verfassungsschutzbericht* annually (https://www.verfassungsschutz.de/SiteGlobals/Forms/Suche/Publikationensuche_Formular.html?nn=678360) — uses OSINT to map extremism.
  - **Federal Office for Information Security (BSI)** — https://www.bsi.bund.de — publishes threat reports based on OSINT.
- **What is NOT verified:** Specific BND OSINT operations are not publicly attributed. Avoid claims about "BND sockpuppets" without source.

#### Government Sources (Verified URLs)

| Source | URL | Function | Status |
|---|---|---|---|
| Unternehmensregister | https://www.unternehmensregister.de/en | Federal business registry | ✅ 200 |
| Bundesanzeiger | https://www.bundesanzeiger.de/pub/en/start | Federal gazette (annual financial statements) | ✅ 200 |
| Transparenzregister | https://www.transparenzregister.de | UBO register (implementing EU AMLD) | ✅ 200 |
| Datenportal der Bundesregierung | https://www.govdata.de | Federal open data portal | ✅ 200 |
| Destatis | https://www.destatis.de | Federal statistics office | ✅ 200 |
| Bundestag | https://www.bundestag.de | Parliamentary records (DIP) | ✅ 200 |

#### Local Sources & Press
- **Quality press:** Süddeutsche Zeitung, Frankfurter Allgemeine Zeitung (FAZ), Die Zeit, Der Spiegel, Die Welt, Handelsblatt, Tagesschau (public broadcaster ARD), ZDF heute.
- **Investigative NGOs:** Correctiv (https://correctiv.org/en ✅), Netzpolitik.org, Frag Den Staat (https://fragdenstaat.de, FOIA platform), OCCRP Germany partner.
- **OSINT community:** OSINT Deutsch (Telegram), IntelTechniques Germany, BSI Cyber-Sicherheitskonferenz.

#### Country-Specific OSINT Tools
- **Unternehmensregister** — official federal business registry (paid for full filings, free for basic info).
- **Bundesanzeiger** — federal gazette with annual financial statements of all German companies.
- **Transparenzregister** — UBO register (implementing EU 4th AMLD).
- **Frag Den Staat** — FOIA platform (https://fragdenstaat.de) — sends and tracks freedom-of-information requests.
- **Correctiv Research Hub** — investigative OSINT tools and methodology.
- **Netzpolitik.org** — digital rights and surveillance investigative site.

#### Legal Considerations
- **Data protection:** GDPR (DSGVO in German) + Bundesdatenschutzgesetz (BDSG). Regulated by BfDI (https://www.bfdi.bund.de).
- **Access to information:** Informationsfreiheitsgesetz (IFG, 2005) — federal FOIA. Each state (Land) has its own IFG.
- **Stasi files**: The **BStU** (Federal Commissioner for the Stasi Records, now BStU archives at Bundesarchiv) holds millions of records of the former East German secret police — accessible to researchers and individuals.
- **Network Enforcement Act (NetzDG, 2017)** — requires social platforms to remove "manifestly illegal" content within 24h.
- **SLAPP risk:** No specific anti-SLAPP law, but criminal defamation is rarely used against journalists.

#### Notable Cases
- **Wirecard scandal (2020).** Financial fraud at Wirecard AG, exposed by Financial Times (Dan McCrum) using OSINT on Asian phantom operations. Correctiv contributed with follow-up investigations. URLs: https://en.wikipedia.org/wiki/Wirecard_scandal
- **Cum-Ex Files (2018).** Cross-border tax fraud scheme exposed by Correctiv and partners. URL: https://correctiv.org/en/thema/latest-stories/cumex-files-en/
- **NSU (National Socialist Underground, 2011).** Neo-Nazi terror cell; investigation heavily criticised for intelligence failures.

#### Standard country template — 7 categories (2026-09)

##### (1) Open bases and statistics
- [Bundesregierung](https://www.bundesregierung.de/) — federal government portal
  *(official statistics covered above: Destatis; open data covered above: GovData)*

##### (2) Legal and tax information
- *(company register, federal gazette and transparency register covered above)*

##### (3) Maps and cadastre
- Address-to-parcel conversion is administered per federal state; there is no single national cadastre

##### (4) Vehicles and licence plates
- No public plate lookup: queries are limited to the registered holder

##### (5) People: names, documents, social accounts, phones, identifiers
- The Melderegister is not publicly accessible; requests are made through the municipality

##### (6) Public procurement
- *(official publication channel covered above: Bundesanzeiger)*

##### (7) WHOIS and infrastructure
- [DENIC](https://www.denic.de/) — .de registry
  *(authorities covered above: BSI, BND, Verfassungsschutz)*

##### Access note
- Several German government portals return 4xx to automated clients while working normally in a browser. Confirm in a browser before treating any of them as dead.
