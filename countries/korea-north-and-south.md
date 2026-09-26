# Korea (North & South)

> Last reviewed: 2026-09-25.

#### North Korea (DPRK)

##### Digital Landscape
Internet penetration <1% of the population. The country uses **Kwangmyong**, a closed intranet, instead of the global internet. Mobile phones (~6 million subscribers on Koryolink) are restricted to domestic calls and Kwangmyong. Foreign diplomats and elites have limited internet access.

##### Intelligence Agency & OSINT Tradecraft
- **Main intelligence agency:** Reconnaissance General Bureau (**RGB**), under the Korean People's Army. URL: https://en.wikipedia.org/wiki/Reconnaissance_General_Bureau (Wikipedia, official RGB page is not publicly accessible).
- **Cyber operations:** Bureau 121, the cyber warfare unit, operates from North Korea and overseas (notably from China, Malaysia, and other countries with DPRK diplomatic presence).
- **OSINT unit / tradecraft:** DPRK uses OSINT for foreign intelligence collection, primarily through Bureau 35 (foreign intelligence gathering).
- **Publicly verifiable tradecraft points:**
  - **HRNK report on RGB** — https://www.hrnk.org/documentations/the-reconnaissance-general-bureau-the-kim-regimes-precious-treasured-sword — documents RGB structure and operations.
  - **38 North OSINT interview** — https://www.38north.org/2024/12/open-source-intelligence-and-north-korea-an-interview-with-uk-air-vice-marshal-ret-sean-corbett/ — interview on OSINT use for DPRK monitoring.
- **Korea Herald on RGB expansion** — https://www.koreaherald.com/article/10805054.

##### Government Sources (Verified URLs)
North Korea has no publicly accessible government databases. All OSINT on DPRK uses external sources:

| Source | URL | Function | Status |
|---|---|---|---|
| 38 North | https://www.38north.org | US-Korea Institute analysis | ⚠️ 403, live in browser |
| NK News | https://www.nknews.org | DPRK-focused news and analysis | ✅ 200 |
| NK Pro | https://www.nknews.org/pro | Premium DPRK analysis (paid) | ✅ 200 |
| NKEconWatch | https://www.nkeconwatch.com | DPRK economy watch | ⚠️ 403, live in browser |
| OpenSanctions DPRK | https://www.opensanctions.org/datasets/ | UN sanctions | ✅ 200 |

##### Local Sources & Press
- **External:** NK News, 38 North, Daily NK (https://www.dailynk.com), Korea Herald, Yonhap (South Korean news agency).
- **Defector organisations:** Daily NK (sources inside DPRK), North Korea Strategy Center (https://nksc.co.kr).
- **OSINT community:** CSIS Beyond Parallel (https://beyondparallel.csis.org), Center for Strategic and International Studies Korea Chair.

##### Country-Specific OSINT Tools
- **38 North** — satellite imagery analysis of DPRK facilities.
- **NK News** — comprehensive news aggregator.
- **Daily NK** — sources inside DPRK.
- **CSIS Beyond Parallel** — satellite imagery and analysis.
- **OpenSanctions DPRK datasets** — UN sanctions list.

##### Legal & OPSEC Considerations
- **Sanctions:** North Korea is under comprehensive UN, US, EU sanctions. Any interaction with DPRK entities may violate sanctions.
- **OPSEC:** DPRK intelligence actively targets researchers, defectors, and journalists investigating the regime. Avoid contact with DPRK-affiliated entities.

##### Notable Cases
- **Sony Pictures hack (2014).** FBI attributed to North Korea's Bureau 121 (Lazarus Group). URL: https://www.fbi.gov/news/pressrel/press-releases/update-on-sony-investigation
- **WannaCry ransomware (2017).** Attributed to Lazarus Group by Google, Microsoft, and US government.
- **DPRK IT worker fraud (2024-2025).** DOJ indictments of DPRK IT workers using fake identities to obtain remote work at US companies. URL: https://www.fbi.gov/wanted/cyber/fraudulent-remote-it-workers-from-dprk

---

#### South Korea (ROK)

##### Digital Landscape
Internet penetration ~98% (KISA 2024). **Naver** (~70% market share) and **Daum/Kakao** dominate search over Google. **KakaoTalk** is the universal messaging app (~95% of smartphone users). X, Instagram, YouTube, Facebook are the main social platforms. South Korea has one of the world's most advanced OSINT ecosystems.

##### Intelligence Agency & OSINT Tradecraft
- **Main agency:** National Intelligence Service (**NIS**) — https://eng.nis.go.kr/ (English site; the official site https://www.nis.go.kr is mostly Korean-language).
- **Defence intelligence:** Defence Intelligence Agency (국군정보사령부, KDIA).
- **OSINT unit / tradecraft:** NIS acknowledges OSINT collection; the public *NIS Act* regulates intelligence activity. The South Korean government has a sophisticated OSINT capability focused on DPRK monitoring.
- **Publicly verifiable tradecraft points:**
  - **Asia Society report on ROK intelligence** — https://asiasociety.org/korea/risks-intelligence-failure-rok-and-why-it-matters — documents intelligence reform efforts.
  - **OSINT landscape in South Korea (Lukio blog)** — https://osintteam.blog/overview-of-the-osint-landscape-in-south-korea-61b699276339 ✅ — comprehensive overview of OSINT tools for Korean sources.

##### Government Sources (Verified URLs)

| Source | URL | Function | Status |
|---|---|---|---|
| Hometax | https://www.hometax.go.kr | Tax authority, business registration | ⚠️ Timeout |
| data.go.kr | https://www.data.go.kr | Open data portal | ⚠️ Timeout |
| NICE (business credit) | https://www.nice.co.kr | Business credit information | ⚠️ Timeout |
| DART (financial disclosures) | https://dart.fss.or.kr | Financial Supervisory Service disclosures | ⚠️ Timeout |
| Koreabizwire | https://www.koreabizwire.com | Business news (English) | ✅ 200 |

##### Local Sources & Press
- **Quality press:** Hankyoreh, Chosun Ilbo, JoongAng Ilbo, Dong-a Ilbo, Korea Herald, Yonhap (news agency), Korea Joongang Daily (English).
- **Investigative NGOs:** Newstapa (https://www.newstapa.com), News Cokeba, SisaIN.
- **OSINT community:** OSINT Korea community, Lukio blog (https://osintteam.blog).

##### Country-Specific OSINT Tools
- **Hometax** — tax authority business registration lookup.
- **NICE** — business credit information.
- **DART** — financial supervisory disclosures.
- **YouthBoBo (유스보보)** — people search engine.
- **KakaoTalk account lookup** — phone number to KakaoTalk account matching (grey-market).

##### Legal Considerations
- **Personal Information Protection Act (PIPA, 2011)** — strict data protection law, stronger than GDPR in some aspects.
- **Access to information:** Official Information Disclosure Act (1998).
- **National Security Law (1948)** — restricts content promoting North Korea; criminalises praise of DPRK.
- **SLAPP risk:** Criminal defamation suits are common against journalists.

##### Notable Cases
- **2016 Park Geun-hye scandal.** Investigation led by JTBC journalist Seo Won-choi, using leaked tablet computer contents. URL: https://en.wikipedia.org/wiki/2016_South_Korean_political_scandal
