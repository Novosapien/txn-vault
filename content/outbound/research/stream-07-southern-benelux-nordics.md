---
description: "Stream 07 raw research: 40 national statutory registers and ecosystem directories across Southern Europe, Benelux, the Nordics and DACH"
---

> **Section:** [[research]]
> **Validation:** [[validation-07-southern-benelux-nordics]]
> **Status:** raw research output, recorded verbatim. Read the validation report alongside it: several counts in this file were corrected.

# Stream 07: Phase 1a, Phase 1b and the remaining EEA

Spain, Portugal, Greece (Phase 1a). Netherlands, Belgium, Austria (Phase 1b).
Nordics, Baltics, Germany, France, Italy, Ireland (opportunistic).

CEE and pan-European sources are owned by other streams and are deliberately
absent here.

## Summary

40 sources recorded under the full entry schema (Spain 5, Portugal 5, Greece 3,
Netherlands 3, Belgium 4, Austria 3, Nordics 4, Baltics 4, Germany 3, France 2,
Italy 2, Ireland 2), plus a dead-ends table of 9 sources that were searched for
and either do not exist, are gone, or turned out not to publish what they are
widely assumed to publish.

Of the 40, 31 are Verified (page fetched and read this pass), 4 are Reported and
5 are Unverified with the failure reason recorded.

The headline finding is that **the official registries are the best sources in
this region and almost nobody prospects from them.** Three in particular are
worth more than the rest of this file put together:

1. **Italy, Registro Imprese, startup innovative.** A statutory public register
   of 11,544 companies, published as a full downloadable ZIP/Excel and PDF, and
   refreshed *weekly*. Legally mandated, free, no login, no scraping fight.
   Nothing else in Europe is this complete or this machine-readable.
2. **Greece, Elevate Greece.** The National Startup Registry run by the General
   Secretariat for Research & Innovation. Filterable by industry, technology,
   region, headcount and total funding. Phase 1a market, government-operated,
   and effectively invisible to non-Greek prospectors.
3. **Spain, ENISA "empresa emergente" certification.** Roughly 2,394 companies
   certified under Ley 28/2022, with a public search tool by year, sector and
   autonomous community, mirrored by a second lookup at the Colegio de
   Registradores against the Mercantile Registry. A company certifies as an
   *empresa emergente* years before it launches a card programme. This is a
   greenfield list by construction.

The second-best category is the **national community directory that lists
every member company by name with a website link**: Start it @KBC (1,700+
Belgian startups, industry and year filters), Bundesverband Deutsche Startups
(1,200+ members as an HTML table), Digital Wallonia (6,824 mapped actors), and
The Hub (11,113 Nordic startups across five countries with stage and industry
filters). All four are free, unauthenticated and never used for outbound.

### Best documented ecosystems

- **Italy.** Statutory register, weekly bulk download. Best in Europe.
- **Belgium.** Unusually good for its size. Start it @KBC, imec.istart and
  Digital Wallonia between them cover most of the Flemish and Walloon startup
  base with public, filterable, linked lists.
- **Estonia.** Dealroom-backed national database, around 1,500 companies,
  curated by the government agency.
- **Germany.** Association member table plus HTGF's 800-company portfolio plus
  deutsche-startups.de's A-Z, which together give near-complete coverage.
- **Nordics as a bloc.** The Hub is a single source covering DK, SE, NO, FI, IS.

### Worst documented ecosystems

- **Netherlands.** Surprisingly poor for a Phase 1b market. Techleap, the
  national scaleup agency, publishes reports and gated "LEAPs" workspaces but
  **no public company database**. There is no Dutch equivalent of Elevate
  Greece or the Registro Imprese. Holland Fintech's member directory is the
  best available and it is a paid-membership list, not an ecosystem census.
- **Austria.** The national fintech directory is dead (DNS gone). Fintech
  Austria lists about 30 members. aws Connect is registration-walled. The
  ecosystem view has been outsourced to a Dealroom subdomain that blocked our
  fetch. Austria is the weakest of the three Phase 1b markets by a wide margin.
- **Denmark.** Copenhagen Fintech, the obvious source, publishes aggregate
  numbers (630+ alumni) and a handful of success stories but no roster at all.
- **Latvia and Lithuania.** Both have official startup support registers that
  are referenced in official documentation but whose list pages we could not
  retrieve (404 and 403 respectively).
- **France.** Station F, with 1,000+ residents, publishes only a 40-company
  highlight reel. The national ecosystem view is a Dealroom subdomain.

### What I could NOT verify

Recorded honestly, per the anti-fabrication rules:

| Item | What was tried | Outcome |
|---|---|---|
| Italy weekly bulk download files | `curl -I` on `startup.registroimprese.it/isin/report?fileId=startup.zip` and `.pdf` | Connection reset by peer from this sandbox. The download links and weekly cadence were read on the fetched index page. The files themselves were not retrieved. Marked Reported, not Verified. |
| Italy `startup.registroimprese.it/isin/search` | WebFetch | ECONNRESET. Search UI described from the fetched static portal page only. |
| Elevate Greece registered-company count | WebFetch of `/startup-registry/`, `/the-startup-database/`, `/analytics/` | Filters confirmed on the database page. The *count* (897) comes from search-result text, not a fetched page. Treated as Reported. |
| Barcelona Tech City members | WebFetch of `/en/members/` and `/en/socios/` | "unable to verify the first certificate", a TLS chain failure from this environment, twice. Cannot confirm the directory is public. |
| `map.startuplithuania.lt` | WebFetch | HTTP 403. Exists (linked from search results) but unreadable here. |
| `austria.dealroom.co` | WebFetch | HTTP 403. Link source verified on austrianstartups.com. |
| `uni.fund/portfolio/` (Greece) | WebFetch | HTTP 403. |
| `startupper.gr` (Greek startup media) | WebFetch | HTTP 403. Publishes Elevate Greece registration round-ups per search snippets, unconfirmed. |
| `brutkasten.com` (Austrian startup media) | WebFetch | HTTP 403. |
| `ecosystem.startupestonia.ee/companies.startups/` | WebFetch | HTTP 403 on the Dealroom-hosted subdomain. The parent page at startupestonia.ee was fetched and describes it. |
| Latvia LIAA "supported startups" list | WebFetch of `business.gov.lv/atbalsta-programmas/jaunuznemumu-atbalsts` | HTTP 404. The list is said in official material to be published under "Atbalstītie jaunuzņēmumi". URL not found. |
| Enterprise Ireland client company directory | WebFetch of `/en/company-directory` and `irishadvantage.com/companies/` | 404 and a redirect to a generic global page. No public client roster located. |
| Wayra portfolio | WebFetch of `wayra.com` then `startups.telefonica.com` | Root page fetched but returned only page headers. The directory could not be characterised. |
| aws Connect (Austria) | WebFetch of `aws.at/en/aws-connect-1/` | Description read. The platform itself (`awsconnect.at`) not fetched and likely registration-gated. |
| RNi accredited-incubator file | WebFetch of both RNi pages on startupportugal.com | Pages fetched. The actual 146-incubator list lives in an external Google Sheet and Drive PDF whose URLs were not exposed in the fetched HTML. |

Also note: **the web-search budget for this session was exhausted partway
through** (200 of 200 calls, shared with other streams). Everything after that
point was verified by direct URL fetch only, which biases the second half of
this file toward sources whose URLs were guessable. Countries covered late,
Norway, Sweden, Finland and Ireland, are almost certainly under-covered
relative to what exists.

---

# SPAIN (Phase 1a)

### ENISA, Registro público de empresas emergentes certificadas

- **Type:** register
- **Geography:** Spain
- **Homepage:** https://www.enisa.es/
- **List page:** https://www.enisa.es/sobre-enisa/consuta-datos-publicos/#buscador-certificaciones
- **Publicly listed?** yes
- **Machine readable?** JS-rendered search UI (no export link exposed on the fetched page)
- **Update cadence:** Continuous. ENISA certifies in weekly batches. The homepage counter moved from 2,132 (reported March) to 2,394 on the page fetched today.
- **Why it surfaces card candidates:** Certification under Ley 28/2022 is applied for by companies up to five years old (seven in biotech, energy and industrial) that have never scaled. It is a tax-status filing, not a funding event, so a company appears here long before it appears in any funding database and years before it would consider a card programme. This is a structurally greenfield list for a Phase 1a market.
- **Approximate list size:** 2,394 certified companies (homepage counter, 2026-08-25)
- **Confidence:** Verified
- **Evidence:** Fetched `enisa.es` homepage (counter "2.394 empresas certificadas"), `/servicios/certificacion/` (which links to the buscador anchor), and `/sobre-enisa/consuta-datos-publicos/` which describes the tool as filtering certifications granted under Ley 28/2022 by year, sector and autonomous community. The page rendered in an offline/read-only mode, so export options could not be confirmed.
- **Last checked:** 2026-08-25

### Colegio de Registradores, Empresas emergentes (ENISA)

- **Type:** register
- **Geography:** Spain
- **Homepage:** https://www.registradores.org/
- **List page:** https://www.registradores.org/en/empresas-emergentes-enisa
- **Publicly listed?** yes
- **Machine readable?** JS-rendered search form
- **Update cadence:** Tracks Mercantile Registry filings, so effectively continuous.
- **Why it surfaces card candidates:** This is the second view of the same population: ENISA-certified startups as recorded against their Mercantile Registry entry. Cross-referencing the two gives legal entity, registry number and province, which is what turns a name into a prospectable account. Useful as the enrichment layer on top of the ENISA list rather than as a discovery source in its own right.
- **Approximate list size:** unknown (no count shown). Upper bound is the ENISA population of about 2,394.
- **Confidence:** Verified
- **Evidence:** Fetched the page. It is a free citizen-information tool, no login, described as querying "empresas emergentes certificadas como tales por ENISA que figuran inscritas en los Registros Mercantiles" with multiple search criteria. Specific criteria and result format are not stated on the landing page.
- **Last checked:** 2026-08-25

### Lanzadera, proyectos / startups aceleradas

- **Type:** accelerator
- **Geography:** Spain (Valencia, national intake)
- **Homepage:** https://lanzadera.es/
- **List page:** https://lanzadera.es/proyectos/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, JS filtering, individual profile pages at `lanzadera.es/startups/<slug>/`
- **Update cadence:** Twice-yearly cohorts. Cohort filter values on the live page run ENE23, MAR24, SEPT24, MAR25, SEPT25, SEPT26, so the list is current to this month's intake.
- **Why it surfaces card candidates:** Juan Roig's accelerator is the largest in Spain by throughput (1,700+ accelerated) and takes revenue-generating SMEs, not just tech startups. 80% of the September 2025 intake was already billing. Marketplaces, logistics and vertical SaaS in that population have real payout and spend problems and no card programme. The sector filter includes fintech, but the greenfield value is in the non-fintech verticals.
- **Approximate list size:** 1,700+ accelerated companies total, around 120 per cohort
- **Confidence:** Verified
- **Evidence:** Fetched `/proyectos/`. Confirmed 40+ sector filters, business-model filters (SaaS, marketplace, e-commerce, subscription), cohort-year filter including SEPT26, A-Z sort, and per-company profile links.
- **Last checked:** 2026-08-25

### AEFI, Asociación Española de Fintech e InsurTech, asociados

- **Type:** community
- **Geography:** Spain
- **Homepage:** https://www.asociacionfintech.es/
- **List page:** https://www.asociacionfintech.es/aefi/asociados/
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid, no visible filters
- **Update cadence:** Membership-driven. Homepage claims 160 members, the grid rendered about 130 logos. Reported to have grown from 115 to 186 across recent years.
- **Why it surfaces card candidates:** Lower greenfield value than the register, since many AEFI members already issue. Its use is the opposite direction: it is the **exclusion list** for Spain. Anything on this grid with a Revolut, N26 or Checkout profile is not greenfield, and knowing that cheaply is worth as much as a new name.
- **Approximate list size:** about 130 logos rendered, 160 claimed
- **Confidence:** Verified
- **Evidence:** Fetched `/aefi/asociados/`. Logo grid under "Nuestros Asociados", no vertical filters on the page despite AEFI being internally organised into 13 verticals. Names visible include PayPal, N26, Qonto, SeQura, Nickel, Checkout.com, Flywire, Fundeen, Prosegur Crypto.
- **Last checked:** 2026-08-25

### El Ecosistema Startup, actores directory and daily newsletter

- **Type:** media
- **Geography:** Spain (and Spanish-speaking LatAm)
- **Homepage:** https://ecosistemastartup.com/
- **List page:** https://ecosistemastartup.com/actores/
- **Publicly listed?** yes
- **Machine readable?** HTML (directory format not characterised on the fetched homepage)
- **Update cadence:** Daily. Every article on the homepage carried today's date, 2026-08-25.
- **Why it surfaces card candidates:** This is an ongoing-signal source, not a first-hit source. The "Daily Shot Startupero" newsletter covers the Spanish ecosystem in Spanish, including cohort announcements and small rounds that never reach the English-language fintech press. It is where the Lanzadera SEPT26 intake gets named before Sifted notices.
- **Approximate list size:** unknown for `/actores/`. Newsletter is daily.
- **Confidence:** Verified
- **Evidence:** Fetched the homepage. Confirmed daily cadence (four articles dated 25 Aug 2026), the `/actores/` directory link, the `/category/blog/actualidad/` news section and the daily newsletter product.
- **Last checked:** 2026-08-25

---

# PORTUGAL (Phase 1a)

### IAPMEI, StartUP Visa, incubadoras certificadas

- **Type:** register
- **Geography:** Portugal
- **Homepage:** https://www.iapmei.pt/
- **List page:** https://www.iapmei.pt/media/b6766fc5/20260811-212009_Lista-final-Incubadoras-certificadas-2026.pdf
- **Publicly listed?** yes
- **Machine readable?** PDF
- **Update cadence:** Annual. Applications for new certification and renewal run each December. The current list was published 22 January 2026.
- **Why it surfaces card candidates:** This is a source-of-sources, and that is exactly why it matters. 94 state-certified incubators, each legally required to host and support foreign-founder companies applying for a Portuguese residence visa. Every one of them is a small, named, addressable list-holder in a Phase 1a market, and the certification list is the only complete enumeration of them. Work the list to find the cohort pages.
- **Approximate list size:** 94 certified incubators
- **Confidence:** Verified
- **Evidence:** Fetched the IAPMEI news item announcing the new list. It states 94 certified incubators, a January 2026 publication date, a December application window, and links the PDF at the media path above.
- **Last checked:** 2026-08-25

### RNi, Portugal Incubators (Rede Nacional de Incubadoras)

- **Type:** register
- **Geography:** Portugal
- **Homepage:** https://startupportugal.com/pt/bem-vindo-a-rni-portugal-incubators/
- **List page:** https://startupportugal.com/pt/bem-vindo-a-rni-portugal-incubators/rni-portugal-incubators-membros/
- **Publicly listed?** partial
- **Machine readable?** Google Sheet plus PDF, hosted off-site
- **Update cadence:** Annual accreditation round. 146 incubators accredited in 2025 (43 tech, 103 local).
- **Why it surfaces card candidates:** Broader than the StartUP Visa list and split tech/local, which matters. The 103 local incubators sit in Portuguese secondary cities and host exactly the non-tech SME population that has never touched card issuing. Includes addresses, contacts and websites.
- **Approximate list size:** 146 accredited incubators
- **Confidence:** Verified (page). Unverified (the list file itself).
- **Evidence:** Fetched both RNi pages on startupportugal.com. The members page states 146 accredited in 2025 and confirms the list carries addresses, contacts and websites, but delivers it via an external Google Sheets document and a Drive PDF whose URLs were not present in the fetched HTML. Contact given as rni@startupportugal.com.
- **Last checked:** 2026-08-25

### Unicorn Factory Lisboa, portfolio

- **Type:** incubator
- **Geography:** Portugal (Lisbon)
- **Homepage:** https://unicornfactorylisboa.com/
- **List page:** https://unicornfactorylisboa.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with "Load More", links out to each company's own website
- **Update cadence:** Rolling. Programmes are Incubation, Scaling Up and Thematic. Portfolio has accumulated since 2012.
- **Why it surfaces card candidates:** Municipally backed, 820+ companies, and critically each card carries the company's own website URL rather than an internal profile. Filterable by vertical, so the AgriTech, HealthTech and AdTech slices can be pulled directly as a greenfield list while the FinTech slice is used for exclusion.
- **Approximate list size:** 820+ startups supported since 2012
- **Confidence:** Verified
- **Evidence:** Fetched `/portfolio/`. Confirmed vertical filters (AdTech, AI, AgriTech, FinTech, HealthTech and others), programme-type filter, "Visit website" links per company, "Load More" pagination, and the 820+ figure.
- **Last checked:** 2026-08-25

### Portugal Fintech Report, ecosystem map

- **Type:** media
- **Geography:** Portugal
- **Homepage:** https://www.portugalfintech.org/
- **List page:** https://www.portugalfintech.org/portugal-fintech-report-2024
- **Publicly listed?** partial. The ecosystem map with company names renders on the page. The full report is gated behind a HubSpot form.
- **Machine readable?** HTML on the landing page, gated PDF behind the form
- **Update cadence:** Annual. Editions exist for 2017 to 2024. A 2025 edition is advertised at `report.portugalfintech.org/2025` (that URL 404'd on fetch).
- **Why it surfaces card candidates:** Two uses. The Payments (12) and Emerging Fintechs (10) buckets are exclusion. The Lending & Credit (13), Insurtech (12), Real Estate (3) and Wealth/ESG (5) buckets are the target: Portuguese financial-adjacent companies that hold customer relationships and money movement but have not issued a card.
- **Approximate list size:** 90+ Portuguese and international fintechs mapped by category
- **Confidence:** Verified
- **Evidence:** Fetched the 2024 report page. The category breakdown and counts above were read directly off the rendered ecosystem map. Full report requires a form submission at share.hsforms.com. Also fetched `/research`, which indexes editions back to 2017 and a separate "Fintech Solutions List" PDF.
- **Last checked:** 2026-08-25

### FIF, Fórum Insurtech Fintech Portugal, associados

- **Type:** community
- **Geography:** Portugal
- **Homepage:** https://fifportugal.pt/
- **List page:** https://fifportugal.pt/en/associados/
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid with outbound website links
- **Update cadence:** Membership-driven, cadence not stated on the page.
- **Why it surfaces card candidates:** The smaller, more incumbent-flavoured of Portugal's two fintech bodies (reference partners are Abreu Advogados, MGEN, PwC). Its Healthtech forum is the interesting one: Portuguese health platforms with payout flows and no card. Low volume, decent quality.
- **Approximate list size:** about 30 corporate members
- **Confidence:** Verified
- **Evidence:** Fetched the page. About 30 logo cards, each with a website link. Three thematic forums named: Insurtech, Fintech & Digital Payments, Healthtech. No per-member sector labelling on the grid.
- **Last checked:** 2026-08-25

---

# GREECE (Phase 1a)

### Elevate Greece, Εθνικό Μητρώο Νεοφυών Επιχειρήσεων (National Startup Registry)

- **Type:** register
- **Geography:** Greece
- **Homepage:** https://elevategreece.gov.gr/
- **List page:** https://elevategreece.gov.gr/the-startup-database/
- **Publicly listed?** yes
- **Machine readable?** JS-rendered (Mantis IMS platform), filterable
- **Update cadence:** Rolling. Companies apply through a GSRI-run digital portal in periodic calls (`registry.elevategreece.gov.gr/latest-call`). Greek media track the count climbing in batches (789, then 805, then 897).
- **Why it surfaces card candidates:** The single highest-value source in Phase 1a. It is the official Greek startup register, run by the General Secretariat for Research & Innovation, and it exposes exactly the fields you need to qualify: industry, technology, region, employee count and total funding raised. Registration is driven by tax and grant incentives, so companies enter the registry at seed stage and earlier, well before a card programme is on anyone's roadmap. Greek-language, government-hosted, and essentially unprospected by non-Greek vendors.
- **Approximate list size:** 897 registered companies (reported)
- **Confidence:** Verified for the database and its filters. Reported for the count.
- **Evidence:** Fetched `/en/startup-registry/`, `/the-startup-database/` and `/analytics/`. The database page confirms filters for Startup, Industry, Technology, Region, Employee count and Total funding, plus outbound links to company websites. The analytics landing page describes Elevate Greece as "the official platform" but does not itself carry the statistics. The 897 figure comes from search-result text, not from a page we retrieved.
- **Last checked:** 2026-08-25

### Marathon Venture Capital, portfolio

- **Type:** VC portfolio
- **Geography:** Greece (Athens), Greek founders internationally
- **Homepage:** https://marathon.vc/
- **List page:** https://marathon.vc/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid, per-company pages
- **Update cadence:** Per investment. Entries are status-labelled (Exited, Inactive), so the page is actively maintained rather than append-only.
- **Why it surfaces card candidates:** Greece's leading seed fund. Portfolio pages of seed funds update at term-sheet signature, ahead of the announcement, which is exactly the "know the deal is on the street" signal Ian described. Sectors listed skew AI, robotics, cybersecurity and software: greenfield by definition.
- **Approximate list size:** about 29 companies including exits
- **Confidence:** Verified
- **Evidence:** Fetched `/portfolio/`. About 29 logos, clickable to individual portfolio pages, Exited/Inactive status labels, Athens address, InnovFin Equity and EFSI backing disclosed.
- **Last checked:** 2026-08-25

### VentureFriends, portfolio

- **Type:** VC portfolio
- **Geography:** Greece-anchored, pan-European
- **Homepage:** https://venturefriends.vc/
- **List page:** https://venturefriends.vc/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards with domain filter, per-company pages at `/portfolio-companies/<slug>`, plus outbound links
- **Update cadence:** Per investment. "Load more" pagination indicates a long tail.
- **Why it surfaces card candidates:** Explicitly filterable by domain including SaaS, Fintech and Energytech. The SaaS and marketplace slices are the target list: European vertical SaaS at seed and Series A is precisely the "will need cards and does not know it yet" population.
- **Approximate list size:** unknown, 11 visible before pagination
- **Confidence:** Verified
- **Evidence:** Fetched `/portfolio`. Confirmed the domain filter (SaaS, Fintech, Energytech among others), per-company pages, "Load more", and Athens and Helsinki geography references. Horizon 2020 InnovFin Equity support disclosed.
- **Last checked:** 2026-08-25

---

# NETHERLANDS (Phase 1b)

### Holland FinTech, member directory

- **Type:** community
- **Geography:** Netherlands plus international members
- **Homepage:** https://www.hollandfintech.com/
- **List page:** http://www.hollandfintech.com/members/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, "Load more" pagination, per-member profile pages
- **Update cadence:** Membership-driven. 300+ member companies claimed across the network.
- **Why it surfaces card candidates:** The best-structured filter set of any fintech association in this stream: Primary Sector, Customer Type, Products/Services, Primary Country, Primary Market. Filtering Customer Type to Startups and Primary Country to Netherlands, while excluding Products equals Payments, produces a Dutch greenfield shortlist directly. Given how little else the Netherlands publishes, this is the workhorse source for a Phase 1b market.
- **Approximate list size:** 200+ rendered, 300+ claimed
- **Confidence:** Verified
- **Evidence:** Fetched `http://www.hollandfintech.com/members/` (the https non-www URL 301s to this host). Confirmed the five filter axes above, card layout with logos, "Load more", and member names including 3S Money, Airwallex, Tink, Treezor, Factris, FINOM, Owlin, Cryptorefills, Lender & Spender.
- **Last checked:** 2026-08-25

### Fintech Netherlands, directory

- **Type:** community
- **Geography:** Netherlands
- **Homepage:** https://fintechnetherlands.com/
- **List page:** https://fintechnetherlands.com/directory/
- **Publicly listed?** yes
- **Machine readable?** HTML profile cards with descriptions, contacts and website links
- **Update cadence:** Self-serve. Companies join by completing a membership form, so the list grows continuously rather than in cohorts.
- **Why it surfaces card candidates:** A second, independent Dutch list with a different composition to Holland Fintech, split into Featured, Banking, Fintech solutions, Associations and Professional services. Because listing is free-form self-registration rather than paid membership, it catches smaller and newer Dutch companies that never join Holland Fintech.
- **Approximate list size:** unknown, no count published
- **Confidence:** Verified
- **Evidence:** Fetched `/directory/`. Confirmed the five sections, free public access, per-company profiles with logos, descriptions, contacts and website links, and the join-by-form mechanism. Named entries include Backbase, Ockto, Twikey, UbiOps. Site is copyright "Wisselbanck".
- **Last checked:** 2026-08-25

### Rockstart, portfolio

- **Type:** accelerator
- **Geography:** Netherlands and Denmark (Copenhagen and Amsterdam programmes)
- **Homepage:** https://www.rockstart.com/
- **List page:** https://www.rockstart.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, four filter axes, outbound website links
- **Update cadence:** Annual cohorts. Year filter runs 2012 through 2026, so the page is current.
- **Why it surfaces card candidates:** The single best-instrumented accelerator list in the Benelux and Nordics overlap. 247 companies with a funding-stage filter showing 105 Pre-Seed and 126 Seed, the exact stage band where a card programme has never been considered. The AgriFood (57) and Energy (64) domains are pure greenfield. The Fintech vertical (23) is the exclusion set.
- **Approximate list size:** 247 portfolio companies
- **Confidence:** Verified
- **Evidence:** Fetched `/portfolio/`. Confirmed counts by Domain (Emerging Tech 126, Energy 64, AgriFood 57), by Year (2012 to 2026), by Funding Status (Pre-Seed 105, Seed 126, Series A 12, Series B 3, Acquired 1) and 40+ verticals including Fintech 23. Each card carries a direct link to the company's own site.
- **Last checked:** 2026-08-25

---

# BELGIUM (Phase 1b)

### Start it @KBC, community startup directory

- **Type:** incubator
- **Geography:** Belgium (Antwerp, Ghent, Hasselt, Leuven, Kortrijk, Brussels, Liège), plus hubs in Hungary, Czechia, UK and US
- **Homepage:** https://startit-x.com/en/accelerate/start-it-kbc
- **List page:** https://startit-x.com/en/accelerate/all-startups
- **Publicly listed?** yes
- **Machine readable?** HTML cards, 81 pages of pagination, industry and year filters, direct outbound website links
- **Update cadence:** Rolling intake (applications accepted year-round). Year filter runs 2014 to 2026.
- **Why it surfaces card candidates:** The strongest single Phase 1b source. 1,700+ active Belgian startups, each card carrying industry tags, founding year and the company's own URL. 60+ industry categories including Fintech, Retail and Healthcare. Free programme, no equity taken, so the intake is far broader and earlier-stage than an equity accelerator: it captures companies that no funding database has ever indexed. Note the CEE hubs (Prague, Budapest, Győr) overlap the MVP markets, which is a bonus for the CEE stream.
- **Approximate list size:** 1,700+ active startups. 1,000+ claimed community historically.
- **Confidence:** Verified
- **Evidence:** Fetched `/en/accelerate/all-startups`. Confirmed the "1700+ active startups" heading, 60+ industry filters, 2014 to 2026 year filter, 81 pages of pagination, and card contents (logo, name, industry, year, website link) with examples A.I.R. Distillations, Agriflight, AICON. Also fetched the parent programme page.
- **Last checked:** 2026-08-25

### imec.istart, portfolio

- **Type:** accelerator
- **Geography:** Belgium primary. Also Netherlands, Italy, Spain, Germany.
- **Homepage:** https://www.imecistart.com/
- **List page:** https://www.imecistart.com/en/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid, six filter axes, per-company portfolio pages
- **Update cadence:** Cohort-based. Cohort-year filter present.
- **Why it surfaces card candidates:** Ranked the world's top university-linked accelerator by UBI Global. Six filter axes (Domain, Life cycle, Technologies, Status, Cohort year, Country) and crucially the Country filter spans Belgium, Netherlands, Italy, Spain and Germany, which means one list covers a Phase 1b market, a Phase 1a market and two opportunistic ones. Deep-tech and B2B SaaS heavy, so no card programmes anywhere in it.
- **Approximate list size:** 300+ startups since 2011
- **Confidence:** Verified
- **Evidence:** Fetched `/en/portfolio` and `/en/belgium`. Confirmed the six filters, the 300+ figure, the five-country spread, logo-grid format with clickable per-company pages, and a "Work at a Startup" jobs section.
- **Last checked:** 2026-08-25

### Digital Wallonia, Cartographie des acteurs

- **Type:** register
- **Geography:** Belgium (Wallonia)
- **Homepage:** https://www.digitalwallonia.be/
- **List page:** https://www.digitalwallonia.be/fr/cartographie/
- **Publicly listed?** yes
- **Machine readable?** HTML, paginated (568 pages), free, no login
- **Update cadence:** Continuously maintained by the Walloon regional digital agency. Profiles are updated by the companies themselves.
- **Why it surfaces card candidates:** A government-run census of the Walloon digital economy: 6,824 mapped actors, of which 2,400+ digital-sector companies and 400+ tech startups, plus 100 research centres. Francophone Belgium is systematically under-covered by English-language startup databases, so this is genuinely fringe. Profiles carry products, services, networks, contacts and websites.
- **Approximate list size:** 6,824 actors mapped, 2,400+ companies, 400+ startups
- **Confidence:** Verified
- **Evidence:** Fetched `/fr/cartographie/`. Confirmed "6 824 acteurs", 568 pages of pagination with Précédent/Suivant controls, a filters affordance ("voir les filtres") with focus options on digital-sector companies and tech startups, thematic category URLs (AI, cybersecurity, circular economy), and free public access.
- **Last checked:** 2026-08-25

### FinTech Belgium, members

- **Type:** community
- **Geography:** Belgium
- **Homepage:** https://www.fintechbelgium.be/
- **List page:** https://www.fintechbelgium.be/members
- **Publicly listed?** yes
- **Machine readable?** HTML cards with logo, name and "Read More" per member. "Older Posts" pagination.
- **Update cadence:** Membership-driven. 100+ members across startups, scale-ups and corporates.
- **Why it surfaces card candidates:** Mostly an exclusion list for Belgium (Bancontact Company, Euronext and DigiTeal are all payments-native). The value is in the long tail of B2B tooling members, Cerrix, Contract.fit, Datavillage and Data.be, which are financial-adjacent SaaS with no issuing.
- **Approximate list size:** 100+ members
- **Confidence:** Verified
- **Evidence:** Fetched `/members`. Confirmed public per-member cards and "100+ members", with names including Abbove, A-Cube, Aera Payment & Identification, AlmaxTech, Bancontact Company, Basikon, Cerrix, Contract.fit, Datavillage, DigiTeal, Euronext.
- **Last checked:** 2026-08-25

---

# AUSTRIA (Phase 1b)

Austria is the weakest-documented of the three Phase 1b markets. Recorded
honestly: two live sources, one dead, one gated.

### Fintech Austria, members

- **Type:** community
- **Geography:** Austria
- **Homepage:** https://fintechaustria.org/
- **List page:** https://fintechaustria.org/members/
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid linking directly to each company's website (no internal profile pages)
- **Update cadence:** Membership-driven. Cadence not stated.
- **Why it surfaces card candidates:** Small (about 30) and incumbent-heavy. N26, Bitpanda, Raiffeisen and Payolution are all exclusions. Its real function for TXN is as a starting map of who the Austrian fintech-adjacent players are, given that the national directory that used to do this job is dead (below).
- **Approximate list size:** about 30 members
- **Confidence:** Verified
- **Evidence:** Fetched `/members/`. About 30 logo cards, each linking out to the member's own site rather than an internal profile. Names confirmed: cashpresso, Finnest, Payolution, N26, Bitpanda, Wikifolio. Individual member URLs of the form `/members/<slug>/` also exist (raiffeisen, bitpanda, fait, seasonax).
- **Last checked:** 2026-08-25

### AustrianStartups, Startup Landscape (Dealroom)

- **Type:** register
- **Geography:** Austria
- **Homepage:** https://austrianstartups.com/
- **List page:** https://austria.dealroom.co/
- **Publicly listed?** partial (Dealroom free tier)
- **Machine readable?** JS-rendered
- **Update cadence:** Dealroom-maintained, continuous.
- **Why it surfaces card candidates:** The only ecosystem-wide Austrian company view still standing. Austria has recorded 3,400+ startup foundings since 2012 employing around 30,000 people, concentrated in IT/software, life sciences and consumer goods: a large greenfield base with almost no public enumeration.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** The link is verified. Fetched `austrianstartups.com` and confirmed it points to `https://austria.dealroom.co/` as its "Startup Landscape". The Dealroom page itself returned HTTP 403 on fetch, so its contents, count, filters and free-tier limits are unconfirmed. AustrianStartups' own member area runs on Hivebrite and no public member directory URL was exposed.
- **Last checked:** 2026-08-25

### aws Connect (Austria Wirtschaftsservice)

- **Type:** community
- **Geography:** Austria
- **Homepage:** https://www.aws.at/en/aws-connect-1/
- **List page:** http://www.awsconnect.at
- **Publicly listed?** no (likely registration-gated)
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** aws is the Austrian federal promotional bank. aws Connect is described as Austria's largest independent innovation network, with 2,900+ registered users spanning startups, investors, corporates and research institutions. If it can be browsed, it is a state-backed census of Austrian innovators. If it cannot, it is a dead end and should be dropped rather than kept as a maybe.
- **Approximate list size:** 2,900+ registered users (accounts, not necessarily distinct companies)
- **Confidence:** Reported
- **Evidence:** Fetched `aws.at/en/aws-connect-1/`, which gives the 2,900+ figure and the `awsconnect.at` URL and describes the platform as matchmaking-oriented. The platform itself was not fetched. The description implies registration is required to browse. Treat as unconfirmed until someone logs in and checks.
- **Last checked:** 2026-08-25

---

# NORDICS

### The Hub, Nordic startup database

- **Type:** register
- **Geography:** Denmark, Sweden, Norway, Finland, Iceland
- **Homepage:** https://www.thehub.io/
- **List page:** https://www.thehub.io/startups
- **Publicly listed?** yes
- **Machine readable?** HTML cards, 741 pages of pagination, six filter axes
- **Update cadence:** Continuous. It is a hiring platform, so profiles are refreshed whenever a company posts a role, which means the data decays far slower than a static directory.
- **Why it surfaces card candidates:** The best single source in the Nordics and one of the best in this whole file. 11,113 startups across five countries with per-country counts (DK 5,233, SE 2,373, NO 2,279, FI 1,434, IS 24), filterable by industry (including Fintech), startup stage (Idea through Growth), company size, and whether they are currently fundraising. The "looking for funding" flag is a live intent signal: a company raising now is a company about to have a spend problem. Backed by Danske Bank, free, unauthenticated.
- **Approximate list size:** 11,113 startups
- **Confidence:** Verified
- **Evidence:** Fetched `/startups`. Confirmed all per-country counts above, the 11,113 total, 741 pages of pagination, and the filter axes (Country, Industry, Startup stage, Company size, Funding status, Impact/SDG). Partners listed include Mesh and Danske Bank Growth.
- **Last checked:** 2026-08-25

### SISP, Swedish Incubators & Science Parks, members

- **Type:** register
- **Geography:** Sweden
- **Homepage:** https://www.sisp.se/
- **List page:** https://www.sisp.se/medlemmar
- **Publicly listed?** yes
- **Machine readable?** HTML cards, paginated, filterable
- **Update cadence:** Membership-driven. 58 member innovation environments.
- **Why it surfaces card candidates:** Sweden's answer to the Portuguese incubator register, a source-of-sources. 58 science parks and incubators, filterable by region, industry, competency and organisation type, each with links to its own site. Sweden has no national startup register, so working outward from the 58 regional incubators is the only systematic route to the Swedish long tail outside Stockholm.
- **Approximate list size:** 58 member innovation environments
- **Confidence:** Verified
- **Evidence:** Fetched `/medlemmar`. Confirmed "58 Innovationsmiljöer som är medlemmar", card format organised by Swedish region with industries and competencies listed, at least 4 pages of pagination, filters by region, industry, competency and type (science park, incubator, or both), and links to member pages and external sites.
- **Last checked:** 2026-08-25

### NCE Finance Innovation, cluster members

- **Type:** community
- **Geography:** Norway (Bergen-anchored, national)
- **Homepage:** https://financeinnovation.no/
- **List page:** https://financeinnovation.no/members
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid, each logo hyperlinked to the member's website
- **Update cadence:** Membership-driven. 80 to 90 members.
- **Why it surfaces card candidates:** Norway's designated national financial-innovation cluster (Norwegian Centres of Expertise programme). The roster deliberately mixes startups with banks, insurers, consultancies and academia, so the startup slice is small but pre-qualified as financially literate and Norwegian-domiciled. DNB, Vipps and Visa on the list mark the exclusions.
- **Approximate list size:** 80 to 90 members ("80+ cluster members" on the members page, "90 member companies" on the homepage)
- **Confidence:** Verified
- **Evidence:** Fetched both `financeinnovation.no` (states 90 member companies) and `/members` (states 80+ cluster members). Logo-card grid, each a hyperlink to the member's site, split into "Cluster Members" and "The Community". Named: DNB, Vipps, Visa, Deloitte, PwC and Nordic banks alongside fintech startups.
- **Last checked:** 2026-08-25

### Maria 01, members directory

- **Type:** incubator
- **Geography:** Finland (Helsinki)
- **Homepage:** https://maria.io/
- **List page:** https://maria.io/community/directory/
- **Publicly listed?** partial
- **Machine readable?** HTML, gated beyond a preview
- **Update cadence:** Rolling tenancy. 200+ companies in the campus community since 2016.
- **Why it surfaces card candidates:** The largest startup campus in the Nordics and the centre of gravity for Finnish early-stage. Directory is tabbed by Startups, Investors, Partners, Global Network and Ecosystem Organisations. Caveat: only a preview is public. The page prompts "Want to browse and connect with the remaining 180+ startups?" and routes to a partner or investor application, so roughly 20 of 200+ are visible without applying.
- **Approximate list size:** 200+ companies, about 20 publicly visible
- **Confidence:** Verified (including the gating)
- **Evidence:** Fetched `maria.io` and `/community/directory/`. Confirmed the 200+ figure, the five directory tabs, and the explicit gate on the remaining 180+ startups. Industry and stage filters could not be confirmed from the public view. `maria.io/companies` returns 404.
- **Last checked:** 2026-08-25

---

# BALTICS

### Startup Estonia, startup database

- **Type:** register
- **Geography:** Estonia
- **Homepage:** https://startupestonia.ee/
- **List page:** https://startupestonia.ee/startup-database/ then https://ecosystem.startupestonia.ee/companies.startups/
- **Publicly listed?** yes
- **Machine readable?** JS-rendered (Dealroom)
- **Update cadence:** Continuous. Dealroom ingests and verifies via machine learning, with Startup Estonia curating. The parent page cites around 15,000 monthly visitors, so it is actively maintained.
- **Why it surfaces card candidates:** Government-agency-curated national database of around 1,500 startups plus 120 support organisations, filterable by location, status, type, verification, growth stage and industry, with a companion list of accelerators and investors at `ecosystem.startupestonia.ee/investors.accelerators/`. Estonia's e-residency base means an unusually high count of very small, very new companies, dead centre of the greenfield segment.
- **Approximate list size:** around 1,444 to 1,500 startups, 120 support organisations
- **Confidence:** Verified for the parent page and filter description. The Dealroom-hosted list subdomain returned 403 and was not read directly.
- **Evidence:** Fetched `/startup-database/`. It names Dealroom as the platform, gives around 1,500 startups and 120 support organisations, lists the six filter axes, and exposes both `ecosystem.startupestonia.ee` URLs. Direct fetch of `companies.startups/` returned HTTP 403.
- **Last checked:** 2026-08-25

### Startin.LV, Latvian Startup Association members

- **Type:** community
- **Geography:** Latvia
- **Homepage:** https://startin.lv/
- **List page:** https://startin.lv/members/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with logos and outbound links, category tabs
- **Update cadence:** Membership-driven since 2016. 100+ members claimed, about 150 rendered.
- **Why it surfaces card candidates:** The only browsable enumeration of the Latvian startup base we could actually retrieve. The state's own LIAA "supported startups" list could not be found (see dead ends). Tabbed All, Startups, Ecosystem Players and Corporates, so the Startups tab isolates the target population directly. Latvia is small enough that 150 names is a meaningful fraction of the whole market.
- **Approximate list size:** about 150 organisations rendered, 100+ members claimed
- **Confidence:** Verified
- **Evidence:** Fetched `/members/`. Confirmed the three-category structure, card format with logo and outbound website link, and names including Tournated, Spotwise, Supliful, Printful, AmorphousHealth, PrimePrometics, Swedbank, plus SSE Riga and Riga Business School as ecosystem players.
- **Last checked:** 2026-08-25

### Startup Lithuania, ecosystem map and Dealroom database

- **Type:** register
- **Geography:** Lithuania
- **Homepage:** https://www.startuplithuania.com/
- **List page:** https://map.startuplithuania.lt/intro (and https://www.startuplithuania.com/dealroom-database/)
- **Publicly listed?** yes (believed)
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Startup Lithuania is the state-backed ecosystem facilitator (under Innovation Agency Lithuania). Its own published sector analysis puts Business Software & HR at 25% and Financial Technology at 14% of Lithuanian startups, so three-quarters of the base is non-fintech B2B software, which is the greenfield target. Lithuania also has the largest licensed-EMI population in the EU, which makes the exclusion problem acute and the map correspondingly valuable.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** `map.startuplithuania.lt/intro` returned HTTP 403 on fetch. The URL and its description ("Explore the Lithuanian Startup Ecosystem") come from search results, and the Dealroom database page URL from the same. Neither was retrieved. Do not treat as real until someone opens it in a browser.
- **Last checked:** 2026-08-25

### Invest Lithuania, Fintech Landscape report

- **Type:** media
- **Geography:** Lithuania
- **Homepage:** https://investlithuania.com/
- **List page:** https://investlithuania.com/fintech-overview-2026/ (2025-2026 edition). https://investlithuania.com/report/fintech-report/ (2024-2025 edition).
- **Publicly listed?** partial
- **Machine readable?** PDF
- **Update cadence:** Annual, now in its 8th edition.
- **Why it surfaces card candidates:** Lists 248 registered and active Lithuanian fintechs at end-2025 (282 in the prior edition). Primarily an exclusion and competitive-intel source rather than a greenfield one, since most of these hold EMI or PI licences. Its greenfield use is narrow but real: EMIs that have a licence and customer money but have not issued a card are the shortest sales cycle TXN will ever get.
- **Approximate list size:** 248 active fintechs (end-2025)
- **Confidence:** Reported
- **Evidence:** Counts and edition history come from search-result text describing Invest Lithuania's own pages. Neither report page was fetched (search budget was exhausted before this could be followed up). Verify before use.
- **Last checked:** 2026-08-25

---

# GERMANY

### Bundesverband Deutsche Startups, Mitgliederliste

- **Type:** community
- **Geography:** Germany
- **Homepage:** https://deutschestartups.org/
- **List page:** https://mitglieder.deutschestartups.org/memberview/mitgliederliste/
- **Publicly listed?** yes
- **Machine readable?** HTML table, the cleanest structure in this entire file
- **Update cadence:** Membership-driven. 1,200+ members.
- **Why it surfaces card candidates:** A three-column HTML table of organisation name (hyperlinked), city, and membership type, with no login required. Membership type is the key field: filtering to `Startup` and excluding `Startup / Alumni`, `Investoren`, `Förderer`, `Partner` and `Business Angel` yields a clean list of currently-active German startups with their locations. Trivially parseable, unusually complete, and no one prospects from it.
- **Approximate list size:** 1,200+ organisations
- **Confidence:** Verified
- **Evidence:** Fetched the member-view URL. Confirmed a three-column table (name, location, type), the six membership types listed above, roughly 1,200+ entries, and full public access with names, cities, URLs and classifications visible without authentication.
- **Last checked:** 2026-08-25

### High-Tech Gründerfonds, portfolio

- **Type:** VC portfolio
- **Geography:** Germany
- **Homepage:** https://www.htgf.de/
- **List page:** https://www.htgf.de/en/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with filters, plus a downloadable "Portfolio Matrix" PDF
- **Update cadence:** Per investment. HTGF is the most active seed investor in Germany by deal count, so the page moves weekly.
- **Why it surfaces card candidates:** 800+ companies, 500 active, filterable by German federal state, which is the only practical way to build a regional German prospect list. HTGF invests only at pre-seed and seed, so every active portfolio company is by definition pre-card-programme. The Digital Tech branch is the target. Life Sciences and Deep Tech are noise.
- **Approximate list size:** 800+ total, 500 active
- **Confidence:** Verified
- **Evidence:** Fetched `/en/portfolio/`. Confirmed the 800+ and 500 figures, three investment areas (Industrial/Climate/Deep Tech, Life Sciences & Chemistry, Digital Tech), filters by Status (Active, Exit, IPO), by all 16 German states plus International, and by sub-category, individual company profile links, and a downloadable Portfolio Matrix PDF.
- **Last checked:** 2026-08-25

### deutsche-startups.de, Startups A-Z and "Brandneu"

- **Type:** media
- **Geography:** Germany
- **Homepage:** https://www.deutsche-startups.de/
- **List page:** https://www.deutsche-startups.de/verzeichnisse/startups-a-z/
- **Publicly listed?** yes
- **Machine readable?** HTML, alphabetically anchored, one profile page per company
- **Update cadence:** Daily. The homepage fetched today carried five newly-founded companies dated 2026-08-25.
- **Why it surfaces card candidates:** This is the best ongoing-signal source in Germany and it is a German-language trade blog, which is exactly why it is uncontested. Two products matter. The "Brandneu" section profiles companies at the moment of founding, before any funding and before any database indexes them. The DealMonitor and StartupTicker log rounds and acquisitions daily. The A-Z directory carries full legal entity names including GmbH, AG, UG and GbR form, which is what makes an entry prospectable.
- **Approximate list size:** hundreds of entries in the A-Z directory
- **Confidence:** Verified for the A-Z directory and the daily cadence. The "Brandneu" section URL was not confirmed.
- **Evidence:** Fetched the homepage (confirming StartupTicker, DealMonitor, Brandneu and weekly reviews, plus five newly-founded companies dated 25 Aug 2026: Fyrcе Care, AmbuMetric, ElternCrew, Spree Monitoring, naion.tech) and `/verzeichnisse/startups-a-z/` (confirming alphabetical anchors, hyperlinked per-company profiles, legal-form suffixes, free access). The A-Z page did not expose a link to Brandneu. Its URL still needs to be found.
- **Last checked:** 2026-08-25

---

# FRANCE

### France FinTech, annuaire des membres

- **Type:** community
- **Geography:** France
- **Homepage:** https://francefintech.org/
- **List page:** https://francefintech.org/membres/
- **Publicly listed?** yes
- **Machine readable?** HTML logo cards with per-member profile pages, category-filtered
- **Update cadence:** Membership-driven. Cadence not stated.
- **Why it surfaces card candidates:** The category navigation is the useful part: Financement, Banking, Regtech, Paiement, Services Fonctionnels, Assurtech, Gestion de risque, Gestion d'actifs. `Paiement` is the exclusion set. `Assurtech` (33 members), `Financement` and `Gestion d'actifs` are French financial-services companies that move customer money and have no card. Each member has a profile page rather than just a logo link.
- **Approximate list size:** 33 in Assurtech alone. Total across nine categories not stated.
- **Confidence:** Verified
- **Evidence:** Fetched `/membres/` (which resolved to the Assurtech view). Confirmed 33 Assurtech members as logo cards with clickable per-member profile pages, and the nine-way category navigation including a "Tous" view.
- **Last checked:** 2026-08-25

### La French Tech, programme cohorts and ecosystem data

- **Type:** register
- **Geography:** France
- **Homepage:** https://lafrenchtech.gouv.fr/en/
- **List page:** https://lafrenchtech.gouv.fr/en/programme/french-tech-tremplin/ and https://lafrenchtech.gouv.fr/en/programme/french-tech-next40-120/. Ecosystem view at http://france-ecosystem.dealroom.co/
- **Publicly listed?** yes for cohorts, partial for the Dealroom view
- **Machine readable?** HTML cohort pages. JS-rendered Dealroom.
- **Update cadence:** Annual. Next40/120 is on its 6th promotion ("Class of 2026"). Tremplin announced its 5th cohort of 102 laureates at VivaTech.
- **Why it surfaces card candidates:** Next40/120 is the wrong end: those are scaled companies that already issue. French Tech Tremplin is the right end. 102 laureates per cohort, a state programme aimed at founders from under-represented backgrounds, meaning very early companies that no VC database has indexed and no competitor is watching. Government-published, named, annual.
- **Approximate list size:** 102 Tremplin laureates (5th cohort). 120 in Next40/120.
- **Confidence:** Verified for the programme pages and cohort sizes. Reported for the Dealroom ecosystem view.
- **Evidence:** Fetched `lafrenchtech.gouv.fr/en/` (confirming the 6th Next40/120 promotion, Class of 2026, and the 102 Tremplin laureates) and `/en/data-on-the-start-up-ecosystem/` (which points to `france-ecosystem.dealroom.co` and confirms no CSV export, no API and no downloadable dataset are offered).
- **Last checked:** 2026-08-25

---

# ITALY

### Registro Imprese, Sezione speciale startup innovative

- **Type:** register
- **Geography:** Italy
- **Homepage:** https://startup.registroimprese.it/
- **List page:** https://startup.registroimprese.it/isin/static/startup/index.html?slideJump=32
- **Publicly listed?** yes
- **Machine readable?** Full-list ZIP/Excel and PDF download (`/isin/report?fileId=startup.zip`, `/isin/report?fileId=startup.pdf`), plus a search UI and a quarterly dashboard
- **Update cadence:** Weekly. The page labels the files "Elenco settimanale" and maintains a historical weekly archive. Companies are separately obliged to confirm their data annually within six months of year-end.
- **Why it surfaces card candidates:** The best source in this file, and arguably in Europe. This is a statutory public register: any Italian company meeting the innovative-startup criteria (under five years, under 5m euro production value, no profit distribution, no merger origin) must be listed in a special section of the Business Register, and the whole thing is published free as a bulk file every week. 11,544 companies with legal name, region, province, production value, headcount, capital, founding date and ATECO industry code. No scraping, no gate, no login, no rate limit. The same portal also publishes a list of certified incubators in the same PDF and Excel format. Italy is opportunistic in TXN's phasing, but the source quality is so far above everything else that it justifies attention out of turn, and it is the template to ask for in every other market.
- **Approximate list size:** 11,544 innovative startups (Lombardy 3,181). 12,172 enterprises with completed profiles including innovative SMEs.
- **Confidence:** Verified for the register, the counts, the file paths and the weekly cadence, all read on the fetched page. Reported for the files themselves, see below.
- **Evidence:** Fetched `startup.registroimprese.it/isin/home` (12,172 profiled enterprises, search by name, region, province, production value, employees, capital, founding date, ATECO) and `/isin/static/startup/index.html?slideJump=32`, which is where the 11,544 count, the "Elenco settimanale" label, the ZIP and PDF report paths, the historical weekly archive, the quarterly dashboard, the ICT sector reports and the certified-incubators list were all read. The download URLs themselves could not be retrieved: `curl -I` on both returned "Recv failure: Connection reset by peer" from this sandbox, and `/isin/search?0=` returned ECONNRESET via WebFetch. The site appears to block non-browser clients. Someone must confirm the files open in a browser before this is relied on operationally.
- **Last checked:** 2026-08-25

### ItaliaFintech, i nostri soci

- **Type:** community
- **Geography:** Italy
- **Homepage:** https://www.italiafintech.org/
- **List page:** https://www.italiafintech.org/i-nostri-soci/
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid with a sector label under each logo
- **Update cadence:** Membership-driven.
- **Why it surfaces card candidates:** Small but unusually well-labelled. Every member carries a category (Lending, Pagamenti, Wealth Management, RegTech, Trading, Invoice Trading, Open Banking, TechFin, Embedded Banking, PayTech, Blockchain, Insurtech, Digital Identity). The "Bud" tier is the interesting one: 16 members explicitly defined as under three years old or under 1m euro revenue, admitted at a symbolic fee. That is a self-identifying list of very early Italian fintechs, Berilo, Crypfy, Identifai and 13 others, none of which will have a card programme.
- **Approximate list size:** 40 (24 full members plus 16 "Bud" members)
- **Confidence:** Verified
- **Evidence:** Fetched `/i-nostri-soci/`. Confirmed the 24 plus 16 split, the "Bud" eligibility definition, the 13 sector labels, and named members (Nexi, Qonto, Trade Republic, Capital.com as full. Berilo, Crypfy, Identifai as Bud).
- **Last checked:** 2026-08-25

---

# IRELAND

### NDRC, accelerator cohorts

- **Type:** accelerator
- **Geography:** Ireland (Dublin, Galway, Cork, Kerry)
- **Homepage:** https://www.ndrc.ie/
- **List page:** https://www.ndrc.ie/alumni
- **Publicly listed?** partial. The alumni page is a hub linking to per-cohort pages rather than a single roster.
- **Machine readable?** HTML, one page per cohort
- **Update cadence:** Two cohorts a year. Cohort pages run 2021 H1 through 2025 H2.
- **Why it surfaces card candidates:** Correcting a common assumption: NDRC is still operating. It was widely reported to have lost its state contract, and it would have been easy to write it off from memory. The live site shows current programmes, 100k euro investment per company, 200+ mentors, 50+ VC relationships and 56m euro raised by its startups over three years, with news through November 2025. Cohorts are pre-seed Irish software companies, greenfield by definition. The per-cohort structure also means each page is a dated, bounded list, which is ideal for a monthly diff.
- **Approximate list size:** about 10 cohort pages. Portfolio names visible on the homepage include Glitch, Barespace, Nory, DevAlly, Meta-Flux, Source, Kreoh, Induct, MARC, Archways, Solidroad, StoreHero, AnotherTrip, Ceartas, Hatched Analytics, Linda.
- **Confidence:** Verified
- **Evidence:** Fetched `ndrc.ie` (current programming, news to November 2025, the funding and mentor figures, and the named alumni above) and `/alumni` (a navigation hub of per-cohort links by year and half, 2021 to 2025, with no consolidated roster on the page itself). `/portfolio` returns 404.
- **Last checked:** 2026-08-25

### Fintech Ireland, ecosystem maps

- **Type:** register
- **Geography:** Ireland
- **Homepage:** https://fintechireland.com/
- **List page:** https://fintechireland.com/fintech-ireland-map.html
- **Publicly listed?** yes
- **Machine readable?** No. JPG and PNG images only, not parseable without OCR.
- **Update cadence:** Versioned but slow. The regulated emoney and payments map is at v21 "as at 10 October 2024", nearly two years stale as of today.
- **Why it surfaces card candidates:** Honestly, it mostly does not. This is the opposite of what this research pass is for: it maps 88 already-licensed Irish payments, emoney and crypto firms, companies that by definition already have card programmes or have chosen not to. Recorded here so the next person does not spend an afternoon rediscovering it and mistaking it for a prospect list. Its one legitimate use is exclusion, and its staleness undermines even that.
- **Approximate list size:** 88 fintech licences
- **Confidence:** Verified
- **Evidence:** Fetched the map page. Confirmed three image-based maps (Regulated Fintech Ecosystem v15, Registered VASPs v10, Regulated Emoney and Payments Firms v21 as at 10 Oct 2024), the 88-licence figure, a RegTech Ireland map v3.5, and a submission process via survey or email to FintechMap@fintechireland.com. No text list, no PDF of names.
- **Last checked:** 2026-08-25

---

# Dead ends and negative findings

Recorded because a confirmed absence saves the next person the search. All
checked 2026-08-25.

| Source | Expected | Actual | Confidence |
|---|---|---|---|
| `austrianfintech.directory`, "FinTech Directory Austria" | National Austrian fintech ecosystem directory, still cited in search results | Domain does not resolve (`getaddrinfo ENOTFOUND`). Defunct. Austria has no national fintech directory. | Verified |
| `swedishfintech.se`, Swedish Fintech Association | Member directory | Domain does not resolve. Sweden's fintech association member list was not located under any URL tried. | Verified |
| `startupgreece.gov.gr`, Greek government startup portal | Government startup directory | Domain does not resolve. Its function appears to have been absorbed by Elevate Greece. | Verified |
| `egg.nbg.gr`, EGG "enter grow go", National Bank of Greece accelerator | Cohort lists | Domain does not resolve. Greece's longest-running bank accelerator has no reachable site at the expected address. Worth one more attempt under a different domain before writing it off. | Verified (this URL only) |
| Techleap (Netherlands) | National scaleup agency with an ecosystem database | Fetched `techleap.nl` and `/stateofdutchtech`. Publishes a PDF report and gated "LEAPs" workspaces. No public company database or dashboard. This is the main reason the Netherlands is poorly documented. | Verified |
| Copenhagen Fintech | Nordic fintech hub with a lab roster | Fetched `/startups`. Publishes aggregates only (630+ alumni, 380+ demo-day pitches) plus a handful of success stories (Predicti, Monthio, DoLand, Januar). No roster, no directory, no searchable list. | Verified |
| Station F (France) | Directory of 1,000+ resident startups | Fetched `/startups`. It is a highlight reel of about 20 companies, plus the annual curated Future 40 at `future40.stationf.co`. No searchable registry, no sector filters, no per-company links. | Verified |
| Startupxplore (Spain) | Public Spanish startup database | Fetched `/en/startups`. It has become a CNMV-regulated co-investment platform, login required, and showed no open equity opportunities at all on the day checked. Not a directory. | Verified |
| Enterprise Ireland client directory | Public roster of EI-backed Irish companies | `/en/company-directory` 404s. `irishadvantage.com/companies/` 301s to a generic global landing page. No public client roster located. Ireland's state agency does not publish its client list in a form we could find. | Verified |
