# Brazil

> Last reviewed: 2026-09-25.

#### Digital Landscape
Brazil had 187.9 million internet users at the start of 2024 (86.6% penetration) per DataReportal's *Digital 2024: Brazil*. WhatsApp is the dominant communication layer — roughly 147–148 million users, ~93% of internet users send messages online — making it the primary OSINT surface. Google dominates search; YouTube is the second social platform after WhatsApp.

#### Intelligence Agency & OSINT Tradecraft
- **Main agency:** Agência Brasileira de Inteligência (**ABIN**), subordinated to the Institutional Security Cabinet (GSI/PR). Public site: https://www.gov.br/abin/en
- **OSINT unit / tradecraft:** ABIN does not publicly advertise a dedicated OSINT directorate. Its *Desafios de Inteligência – Edição 2026* public report describes OSINT as a collection discipline integrated into its Obtaining (Obtenção) area, but no named OSINT unit is publicly attributed. The Brazilian intelligence community (SISBIN) coordinates civilian + military intelligence; ABIN is the central body.
- **Publicly attributable tradecraft:** None specifically attributable beyond ABIN's public acknowledgement that it collects open-source information as part of its mandate. The most mature Brazilian OSINT tradecraft is practised by investigative journalists (Agência Pública, Piauí) and civil-society investigators, not by ABIN.

#### Government Sources (Verified URLs)

| Source | URL | Function |
|---|---|---|
| Receita Federal — CNPJ | https://www.gov.br/receitafederal/pt-br/assuntos/cadastros-e-registros-especiais/cnpj | Business registry lookup |
| CNPJ Comprovante | https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp | Registration/situation certificate |
| Diário Oficial da União (DOU) | https://www.in.gov.br/servicos/diario-oficial-da-uniao | Federal official gazette |
| Imprensa Nacional | https://www.gov.br/imprensanacional/pt-br | Print house & gazette archive |
| Portal de Compras (Comprasnet) | https://www.gov.br/compras/pt-br | Federal procurement contracts |
| Portal da Transparência | https://portaldatransparencia.gov.br/ | CEIS (sanctioned companies), public spending |

**Court records:** Jusbrasil (https://www.jusbrasil.com.br/consulta-processual) and Escavador (https://www.escavador.com) are the two principal case-law aggregators; both index CNJ-connected tribunals. The official CNJ platform is https://www.cnj.jus.br.

**Property registry:** Brazil has no unified federal property registry; each Cartório de Registro de Imóveis (notary office) keeps its own records.

#### Local Sources & Press
- **Quality press:** Folha de S.Paulo (https://www.folha.uol.com.br/), O Globo (https://oglobo.globo.com), Estadão (https://www.estadao.com.br), Valor Econômico (https://valor.globo.com).
- **Investigative / non-profit:** Agência Pública (https://apublica.org), Agência Lupa (https://piaui.folha.uol.com.br/lupa/ fact-checking), The Intercept Brasil (https://www.intercept.com.br/), Instituto Socioambiental (https://www.socioambiental.org).
- **Open-data portals:** dados.gov.br (federal open data), TSE Eleições (https://divulgacandcontas.tse.jus.br) for electoral/campaign finance.

#### Country-Specific OSINT Tools
- **Jusbrasil** & **Escavador** — case-law search (the closest Brazilian equivalent to US PACER).
- **Consulta CNPJ Receita** — corporate registry lookup (free; CAPTCHA-protected).
- **CNPJ.biz / ReceitaAWS** — community wrappers over the Receita Federal CNPJ API.
- **TSE DivulgaCandContas** — campaign finance & candidate asset declarations.
- **OSINT-Tools-Brazil** (GitHub: `bgmello/OSINT-Tools-Brazil`) — community-curated list.
- **OSINT Brasil** blog (https://osintbrasil.blogspot.com) — practitioner write-ups.

#### Legal Considerations
- **Data protection:** **LGPD** — *Lei Geral de Proteção de Dados*, Law 13.709/2018, in force since 18 Sep 2020. Enforced by ANPD (https://www.gov.br/anpd/pt-br).
- **Access to information:** *Lei de Acesso à Informação* (LAI), Law 12.527/2011 — every citizen can request government records; FalaBR (https://falabr.cgu.gov.br) is the central portal.
- **SLAPP risk:** No dedicated anti-SLAPP statute; journalists face criminal defamation suits under the *Código Penal* (arts. 138–145).
- **Internet regulation:** *Marco Civil da Internet* (Law 12.965/2014) governs intermediary liability and data retention.

#### Notable Cases
- **Operação Lava Jato (Operation Car Wash)** — 2014–2021 anti-corruption task force led by the Curitiba federal court (Judge Sérgio Moro) and the *Ministério Público Federal*. Convictions included former president Lula (later annulled by STF in 2021), Odebrecht/Novonor executives, and Petrobras directors. OSINT tradecraft was light; the case was built on plea bargains (*delação premiada*) and leaks. Verified URLs: https://en.wikipedia.org/wiki/Operation_Car_Wash · https://apublica.org/especial/vaza-jato (the "Vaza Jato" leak archive).
