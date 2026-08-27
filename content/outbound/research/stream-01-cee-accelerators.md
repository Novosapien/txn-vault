---
description: "Stream 01 raw research: 35 accelerator, incubator and startup-programme sources across the four MVP markets"
---

> **Section:** [[research]]
> **Validation:** [[validation-01-cee-accelerators]]
> **Status:** raw research output, recorded verbatim. Read the validation report alongside it: several counts in this file were corrected.

# Stream 01: Accelerators, incubators and startup programmes in CEE

Markets: Poland, Czech Republic, Romania, Hungary (TXN MVP markets), plus
regional CEE-wide programmes that recruit into those four.

Researched 2026-08-25. Every entry below was reached by fetching a live URL
during this pass unless the Confidence field says otherwise.

## Summary

**What I found.** 35 entries. 32 carry a `Verified` component, meaning the page
was fetched and read during this pass; 6 of those are `Verified` only in part,
with the unverifiable half recorded explicitly. 1 entry is `Reported` and 2 are
`Unverified`. Five programmes are recorded as dead, absorbed or dormant, which
is itself a finding.

**The single best source in this stream is Romanian and almost nobody outside
Romania talks about it.** Rubik Hub's startup portfolio page
(`https://rubikhub.ro/startups/`) carries 600+ startups with a **FinTech
vertical filter**, a **country filter**, the **exact programme and cohort**
each company came through, and **investment raised to date**, all in one flat
HTML page. It is the richest single artefact I found in four countries. It is
also invisible to a naive crawler: it returns HTTP 403 to most automated
fetchers and only yields to a browser user-agent. That combination (high value,
trivially blocked) is exactly why it is uncovered.

**Bank-run programmes are the fintech-dense layer, and they are split.** Two are
excellent and current: **MBH FinTechLab** in Budapest (Hungary's bank-owned
fintech incubator, roughly 30 companies published with descriptions) and
**start it @ČSOB** in Prague (130 startups over 17 cohorts, current cohort
published, applications open to 30 October 2026). Two others that the
English-language lists still cite are effectively gone: mBank's **mAccelerator**
domain is parked, and Alior Bank's **RBL_START** subdomain now redirects to the
retail banking homepage. **PKO's Let's Fintech** is alive and enormous (6,000+
companies screened since 2015) but publishes almost nothing: four partner logos
on the English page. It is a relationship target, not a scrape target.

**What surprised me.**

1. **Design Terminal is gone.** Hungary's best-known startup mentoring brand,
   210+ startups, now 301-redirects to `civitta.com/hu`. It has been absorbed
   into Civitta's consultancy. The programmes continue under Civitta branding
   (V4 Startup Force, ESA BIC Hungary, NAK TechLab) but the Design Terminal
   alumni corpus is no longer published anywhere I could reach.
2. **Nápad roku (Czechia) has 18 years of published cohorts** and is a
   competition, not an accelerator, so it never appears on accelerator lists.
   Every year from 2007 to 2026 has its own results page with founder name,
   sector tag and a paragraph of description. It is the deepest longitudinal
   Czech pre-launch corpus I found.
3. **Innovation Labs, Romania's largest programme (809 supported teams, 25
   universities), does not publish a machine-readable cohort list.** The site is
   a React SPA, the `/teams` route loads from an API I could not locate in the
   bundle, and the WordPress backend at `il.calemis.org` exposes only `mentor`
   via `wp-json`. The cohorts are only reliably available through Romanian tech
   press (StartupCafe, Forbes.ro), which publishes the full qualified list every
   May.
4. **Government portals under-deliver.** `accelerate.gov.ro` looked like a
   Romanian government registry of ecosystem entities and turned out to be a
   library of PDF reports plus a handful of profile pages. `czechstartups.gov.cz`
   (CzechInvest) is an editorial showcase of about 16 famous companies, not a
   database. The one government source that does deliver is Polish:
   `mapadotacji.gov.pl`, which lists EU-grant beneficiaries by company name and
   filters by the "Platformy startowe" programme.

**Market coverage.**

- **Romania: well covered, and the best material in the stream.** Rubik Hub,
  InnovX-BCR, Techcelerator, Spherik and Orange Fab all publish named company
  lists. Techcelerator even has an explicit `NEXTFintech` alumni category.
- **Czechia: well covered but fintech-thin.** start it @ČSOB, JIC, StartupYard,
  xPORT and Nápad roku all publish. The Czech programmes skew deep tech,
  cybersecurity and hardware. The current start it @ČSOB cohort of 12 contains
  zero fintechs.
- **Hungary: moderate, and MBH FinTechLab carries it.** Hiventures (state VC) is
  large but its portfolio page shows descriptions without company names in the
  static HTML. OXO Labs publishes 15 companies, none fintech. BnL Start claims a
  24-company fintech-leaning portfolio but publishes no list and its TLS
  certificate has expired.
- **Poland: the weakest for published lists, despite being the biggest
  ecosystem.** Huge Thing, MIT EF CEE, PKO and Kozminski all run substantial
  programmes and all publish only a handful of showcase logos. The Polish signal
  is in the grant registry (`mapadotacji.gov.pl`) and the trade press
  (MamStartup, Cashless, Fintek), not on accelerator websites.

**Practical takeaway for TXN.** For first-hit discovery, scrape Rubik Hub,
Techcelerator, InnovX-BCR, Spherik, JIC and the Startup Wise Guys country
filters. For ongoing signal, monitor the annually-refreshed pages: Nápad roku
results, start it @ČSOB cohort page, Innovation Labs press coverage each May,
and Rubik Garage cohort announcements each autumn. For Poland, the accelerator
websites will not carry the signal; the grant register and the fintech press
will.

### What I could NOT verify

- **Elevator Lab (Raiffeisen Bank International).** `elevator-lab.com` returned
  HTTP 503 to both WebFetch and a browser-UA curl. This is the most obviously
  relevant bank programme in the region (RBI has subsidiaries in PL, CZ, RO and
  HU) and I could not confirm whether it is still running. Recorded Unverified.
  Someone should re-check on a residential connection.
- **RBL_START (Alior Bank).** Confirmed the subdomain redirects to the bank
  homepage and no accelerator page exists at the documented paths. Could not
  confirm whether a 2025 or 2026 edition ran. Recorded as likely dormant.
- **Startarium (Impact Hub Bucharest / ING).** `startarium.ro` 301s to
  `startarium.com`, which returned HTTP 403. Could not read the platform or
  confirm whether it publishes a business directory.
- **The Spinoff (Raiffeisen Bank Romania incubator).** Cited by Vestbee at
  `thespinoff.eu`. DNS does not resolve. Could not find a replacement domain.
- **Hiventures company names.** The portfolio page renders company descriptions
  but hides names behind "Bővebben" detail links that require per-company
  fetches. Portfolio size of 167 comes from a third party, not from Hiventures.
- **28DIGITAL cohort list.** Homepage verified, but no cohort or alumni listing
  URL exists on it. The 150-startup figure is from The Recursive, not from the
  programme.
- **Search coverage limitation.** This pass exhausted its web-search budget
  partway through and the remainder was done by direct URL probing, sitemap
  reading and following links from verified directory pages. Local-language
  searching (PL/CZ/RO/HU) was used for roughly the first two thirds. There are
  certainly more municipal and university programmes in all four countries that
  a fresh search budget would surface, particularly city-run incubators in
  Poland (Kraków, Wrocław, Gdańsk) and Hungarian county-level GINOP-funded
  incubators.

---

## Romania

### Rubik Hub (Piatra Neamț, ADR Nord-Est)

- **Type:** accelerator
- **Geography:** Romania, plus CEE-wide intake (Moldova, Bulgaria, Serbia, Slovenia, Estonia, Czechia, Italy, Greece, Spain, Austria seen in the list)
- **Homepage:** https://rubikhub.ro/
- **List page:** https://rubikhub.ro/startups/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, single flat page, no pagination
- **Update cadence:** Continuous. Programme labels on the list run to "WIPO IP Management Clinic Program 2026" and "Rubik Scale to UK 2025"; a Rubik Garage 8th edition ran October 2025 to February 2026. Expect meaningful refresh 2-3 times a year around cohort intake and demo day.
- **Why it surfaces card candidates:** Each entry carries a vertical tag including `# FinTech`, a country, the exact programme and cohort, and investment raised. Fintech entries seen include **Finergy** ("helps banks offer instant payment services to their customers", Rubik Scale to UK 2025), **DDD Invoices** (e-invoicing API, Slovenia), **Conta25**, **Signal Sigma**, **Equinox AI**. These are early-stage, pre-processor companies in a market TXN has named as MVP. The cohort labels also let you date the company, so you can filter to "accelerated in the last 12 months" and get a genuine greenfield list.
- **Approximate list size:** Page claims 600+ startups worked with since 2017; the rendered list is several hundred entries with 8 tagged FinTech.
- **Confidence:** Verified
- **Evidence:** WebFetch returned HTTP 403. Fetched successfully with `curl` and a desktop Chrome user-agent (HTTP 200, 1.35 MB HTML, 56 KB of extracted text). Confirmed the vertical and country filters, the per-entry "Program: <name>, Cohort N" labels, "Investment raised: EUR X" fields, and INACTIVE markers on dead companies.
- **Last checked:** 2026-08-25

### InnovX-BCR (Banca Comercială Română)

- **Type:** accelerator (bank-run)
- **Geography:** Romania (Bucharest, Cluj, Iași), with international intake
- **Homepage:** https://www.innovx.eu/
- **List page:** https://www.innovx.eu/startupsx/alumni
- **Publicly listed?** yes
- **Machine readable?** HTML cards (logo grid) with dropdown filters for year and industry
- **Update cadence:** Annual cohorts. Year filter offers 2019 through 2025, so the page is refreshed at least once per cohort.
- **Why it surfaces card candidates:** Bank-owned, explicitly fintech-focused alongside cyber and AI, and the alumni grid carries a fintech industry filter. Fintech alumni visible include MyMoney, SOLO, Coinscrap Finance, Lendox, Invoice Cash Group, Finqware, KidsFinance, Fagura. Romanian and Moldovan lending and money-management startups at exactly the stage where a card programme is a next-12-months decision.
- **Approximate list size:** Roughly 400 logos on the alumni page; homepage claims 487 innovators accelerated.
- **Confidence:** Verified
- **Evidence:** Fetched homepage (metrics: 487 innovators, 217 corporate partnerships, EUR 108.3M raised) and the alumni page. Confirmed the year filter (All / 2025 / 2024 / 2023 / 2022 / 2021 / 2020 / 2019) and a 40+ entry industry filter, and read fintech company names off the grid. Caveat: individual cohort years are not shown per logo, only reachable by filtering.
- **Last checked:** 2026-08-25

### Techcelerator

- **Type:** accelerator
- **Geography:** Romania (Bucharest), operating across 16 countries
- **Homepage:** https://techcelerator.co/
- **List page:** https://techcelerator.co/alumnis/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with dropdown filters for "Alumni Category" and "Alumni Year"
- **Update cadence:** Per-cohort. Year filter spans 2019-2024; four named programmes currently run (Advancing AI, CleanTech Nexus, Investment Readiness, Scale Match). The alumni page lags the programme page.
- **Why it surfaces card candidates:** It has an explicit **NEXTFintech** alumni category. Named fintech alumni include Tukana/Infin8 (finance management and transfers), Text'n Pay Me (banking keyboard for money transfers), Ocean Credit (online consumer lending via card transfers), Credia.store (point-of-sale consumer credit), Prime Dash, Bankspot, 22Trust Venture (AI pricing for lending), Finpathic. Lending and disbursement platforms of this shape are the exact greenfield profile in TXN's ICP.
- **Approximate list size:** Roughly 130 startups on the alumni page; site claims 148 companies since 2018.
- **Confidence:** Verified
- **Evidence:** Fetched homepage (148 companies, 33% raised capital, $120M portfolio value, 84% survival) and the alumni page, where I read the category list (Advancing AI, Batch #1-4, Investment Readiness, NEXTFintech), the year range and 12 named fintech companies with descriptions.
- **Last checked:** 2026-08-25

### Spherik Accelerator (Cluj-Napoca)

- **Type:** accelerator (NGO, university-linked to UTCN)
- **Geography:** Romania, with EU-wide intake through EIC and DMS programmes
- **Homepage:** https://spherikaccelerator.com/
- **List page:** https://spherikaccelerator.com/alumni/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with Sector, Year and Country filters
- **Update cadence:** Slow. Year filter spans 2015-2024, latest news item is 2 March 2025 ("DMS Accelerator opens its 3rd call"). Treat as a first-hit source, not an ongoing signal.
- **Why it surfaces card candidates:** Small but clean list with three named fintechs: **22TRUST VENTURE** (AI risk analysis and dynamic pricing for consumer credit), **bNesis** (fintech integration platform), **iFactor** (connects SMEs, investors and banks). Cluj is Romania's second tech hub and is under-covered by fintech press.
- **Approximate list size:** 27 companies (7 KPMG Startup Grow Pad alumni, 20 Spherik alumni)
- **Confidence:** Verified
- **Evidence:** Note the domain trap: `spherik.ro` does not resolve (DNS ENOTFOUND). The live site is `spherikaccelerator.com`. Fetched the homepage (confirmed nav and the 2 March 2025 news date) and the alumni page (counted 27 companies across two sections, confirmed Sector, Year and Country filters, read the three fintech descriptions).
- **Last checked:** 2026-08-25

### Orange Fab Romania

- **Type:** accelerator (corporate, Orange Romania)
- **Geography:** Romania, part of the Orange Fab network across 20 countries
- **Homepage:** https://www.orangefab.ro/
- **List page:** https://www.orangefab.ro/startup-uri/ (plus a digital catalogue at https://www.orangefab.ro/success-stories-digital-catalog/)
- **Publicly listed?** yes
- **Machine readable?** HTML, flat list of company names with year tabs (2017, 2018, 2019, 2020)
- **Update cadence:** The startup list's year tabs stop at 2020, but the news feed is current (Innovation Labs 2026 Demo Day, VivaTech 10 years, Rubik Garage 8th edition). 12-month programme, so cohorts are annual, but the public list is not being maintained in step.
- **Why it surfaces card candidates:** A telco accelerator is a strong non-financial-platform-adding-cards signal: these are companies with a distribution relationship to a carrier and a payments or loyalty problem coming. Named companies include PROCESIO, Nestor, FieldOS, Blugento, CityDock, Zevo Technologies, EmailTree.AI, Rastel.io. Offers PoC projects up to EUR 20,000, so participants are pre-revenue-scale.
- **Approximate list size:** Roughly 38 named companies
- **Confidence:** Verified
- **Evidence:** Fetched the homepage via curl (confirmed programme terms, 12-month duration, EUR 20k PoC, 5G Lab Iași and București), the `/startup-uri/` page (extracted the full list of about 38 company names and the 2017-2020 year tabs), and `/noutati/` (confirmed 2026-dated news items).
- **Last checked:** 2026-08-25

### Innovation Labs (Romania)

- **Type:** accelerator (university-anchored pre-accelerator, 5 cities)
- **Geography:** Romania (Bucharest, Cluj, Iași, Sibiu, Timișoara), 25 partner universities in 13 cities
- **Homepage:** https://www.innovationlabs.ro/
- **List page:** https://www.innovationlabs.ro/teams (SPA route, does not render server-side). Cohorts are reliably published in press, e.g. https://startupcafe.ro/lista-castigatori-competitie-idei-afaceri-innovation-labs-2026-100310
- **Publicly listed?** partial
- **Machine readable?** JS-rendered, no accessible API found. The press coverage is plain HTML.
- **Update cadence:** Strictly annual. Hackathon in spring, 10-week pre-acceleration March to May, Demo Day in May. 2026 edition: 640+ participants, 221 projects, 41 teams qualified. Cohort names hit the press within days of Demo Day.
- **Why it surfaces card candidates:** The largest student and young-professional pipeline in Romania, and Early Game Ventures put EUR 500,000 behind the 2026 cohort. These are pre-incorporation to pre-seed teams: too early for a card programme today, correct to be tracked so the signal fires when they raise. The 2026 cohort included **Money24**, a fintech-named team.
- **Approximate list size:** 809 supported teams cumulatively (figure taken from the site's own JS bundle text); 41 teams in the 2026 cohort.
- **Confidence:** Verified (programme and press list), Unverified (on-site machine-readable cohort list)
- **Evidence:** Homepage fetch returned only a loading shell. Downloaded the React bundle `/static/js/main.fcd0f76c.js` (328 KB) and confirmed the `/teams`, `/mentors`, `/juries` routes and the "809 supported teams" copy; team data is not in the bundle. Probed the backend at `il.calemis.org`: `wp-json/wp/v2/types` returns only `post`, `page`, `media` and a custom `mentor` type, no teams endpoint. Verified the press route instead by fetching the StartupCafe article (published 26 May 2026), which names AICoustic, DistriOS, Intrudify and Nabu as 2026 winners. Also fetched the government profile at https://accelerate.gov.ro/en/entities/innovation-labs.
- **Last checked:** 2026-08-25

### Impact Hub Bucharest / Startarium

- **Type:** incubator plus entrepreneurship platform
- **Geography:** Romania
- **Homepage:** https://www.impacthub.ro/
- **List page:** none found. Programmes at https://impacthub.ro/programe-pentru-antreprenori/ and https://impacthub.ro/startup-impact-lab/ ; Startarium at https://startarium.ro/ (301s to https://startarium.com/)
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Unknown. Programmes named on site (Romania ClimAccelerator, Innovators for Children) carry no dates.
- **Why it surfaces card candidates:** Startarium is ING Bank Romania's entrepreneurship platform and has historically been the largest funnel of Romanian first-time founders. If a business directory exists behind it, it would be a high-volume greenfield list. Impact Hub itself runs thematic accelerators (climate, agrifood) that are unlikely to be fintech-dense.
- **Approximate list size:** unknown
- **Confidence:** Reported
- **Evidence:** Fetched impacthub.ro and mapped the full nav; confirmed there is no alumni or startup directory page. `startarium.ro` 301-redirects to `startarium.com`, which returned HTTP 403 to WebFetch, so I could not read the platform or confirm a public directory.
- **Last checked:** 2026-08-25

### accelerate.gov.ro (Accelerate Romania)

- **Type:** register (government ecosystem portal)
- **Geography:** Romania
- **Homepage:** https://accelerate.gov.ro/en/
- **List page:** https://accelerate.gov.ro/en/pages/repository (a document library, not an entity list). Entity profiles exist at `/en/entities/<slug>`.
- **Publicly listed?** partial
- **Machine readable?** HTML pages per entity; the "repository" is PDF reports
- **Update cadence:** Unknown, appears static
- **Why it surfaces card candidates:** Useful only as a cross-check on which Romanian accelerators the government recognises, and for entity metadata (founders, cities, team size). It does not list startups.
- **Approximate list size:** unknown; individual entity pages confirmed to exist
- **Confidence:** Verified (that it is not the entity directory it appears to be)
- **Evidence:** Fetched the Innovation Labs entity page, which carried structured fields (organisation type, cities, founders, team size, contact channels). Fetched `/en/pages/repository` and found it contains research reports and academic papers (StartupBlink, OECD, EU Innovation Scoreboard links), with no searchable entity database.
- **Last checked:** 2026-08-25

### RomanianStartups.com

- **Type:** register (community-maintained directory)
- **Geography:** Romania
- **Homepage:** https://www.romanianstartups.com/
- **List page:** https://www.romanianstartups.com/accelerators-incubators/
- **Publicly listed?** yes
- **Machine readable?** HTML list with Launched / Project / Closed status filters, plus startup listings by 40+ industry categories and a "deadpool" section
- **Update cadence:** Stale. Footer reads 2012-2026 but the accelerator entries appear to date from around 2017.
- **Why it surfaces card candidates:** The industry-categorised startup listings and the deadpool are worth one pass for historical Romanian companies, but this is not an ongoing signal. Its accelerator list is materially out of date (7 entries, missing InnovX, Techcelerator, Rubik Hub and Orange Fab).
- **Approximate list size:** 7 accelerators listed; startup count unknown
- **Confidence:** Verified (including its staleness)
- **Evidence:** Fetched the accelerators page and enumerated all 7 entries (Risky Business, Transilvania START UP, Privacy Accelerator Program, Seed For Tech, Simplon Romania, Innovation Labs, Spherik). Confirmed the site structure and the absence of every major current Romanian programme.
- **Last checked:** 2026-08-25

---

## Czech Republic

### start it @ČSOB

- **Type:** accelerator (bank-run, ČSOB / KBC group)
- **Geography:** Czech Republic
- **Homepage:** https://startit.csob.cz/
- **List page:** https://startit.csob.cz/startupy-v-programu/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (image, description, link per startup)
- **Update cadence:** Twice-yearly cohorts, 5-month programme, currently on the 17th cohort. Applications for the next intake close **30 October 2026** (https://startit.csob.cz/prihlas-se/). The list page turns over with each cohort, so it must be snapshotted, not just diffed.
- **Why it surfaces card candidates:** The most fintech-adjacent bank accelerator in Czechia, run by one of the country's largest banks. The current cohort of 12 skews commerce and operations rather than pure fintech (Spiroq for vending machines, Reechable for restaurant loyalty cards, Rented for product sharing, Monomo for demand, supply and logistics), and several of those are exactly the non-financial-platform-adding-cards profile: vending payments, gastro loyalty, marketplace disbursement. A bank-backed startup that already has ČSOB's sandbox is a warm greenfield lead.
- **Approximate list size:** 12 companies in the current cohort; 130 startups accelerated in total out of 750+ applications over 7 years.
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (130 startups, 750+ applications, 7 years, 17th cohort, 30 October 2026 deadline) and the startups page, where I read all 12 current company names with descriptions. Confirmed there is no historical alumni archive: only the current cohort is shown, which is why snapshotting matters.
- **Last checked:** 2026-08-25

### Nápad roku

- **Type:** event / competition (Czechia's oldest national startup competition, 18 editions)
- **Geography:** Czech Republic
- **Homepage:** https://napadroku.cz/
- **List page:** One page per year, https://napadroku.cz/soutez/2025/ back to https://napadroku.cz/soutez/2007/ (a 2026 page exists at https://napadroku.cz/soutez/2026/)
- **Publicly listed?** yes
- **Machine readable?** HTML, one page per year, consistent structure
- **Update cadence:** Annual, one new results page per year, and the archive is never taken down. 2,652 projects entered across 18 editions.
- **Why it surfaces card candidates:** This is the deepest longitudinal Czech corpus of pre-launch companies I found, and it never appears on accelerator directories because it is a competition. Each entry carries founder name, project type (software, hardware, or a combination) and an industry tag, which makes filtering for finance and commerce projects straightforward. Entrants are typically pre-incorporation to seed: a card programme is 12-24 months out for most, which is precisely the window Ian wants.
- **Approximate list size:** 2,652 projects entered in total; each year's page carries the winners and placings (127 projects entered the 2025 edition).
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (18 editions, 2,652 projects, 476M CZK invested into projects), read the sitemap at https://napadroku.cz/sitemap.xml to recover the real URL pattern (`/soutez/<year>/`, not the `/vysledky-<year>/` the nav labels imply, which 404s), and fetched the 2025 results page in full: TROPIC01, CircuitNinja, Lightly and others with founder names, sector tags and descriptions.
- **Last checked:** 2026-08-25

### JIC (Jihomoravské inovační centrum, Brno)

- **Type:** incubator and accelerator (regional government backed, South Moravia)
- **Geography:** Czech Republic (Brno and South Moravia)
- **Homepage:** https://www.jic.cz/en/
- **List page:** https://www.jic.cz/en/about-us/our-clients
- **Publicly listed?** yes
- **Machine readable?** HTML logo cards with "Go to web" links and a "Load more" pagination control
- **Update cadence:** Continuous client intake rather than fixed cohorts. Site cites 300 clients in the last 10 years and 452 in the JIC+ network, so the page grows steadily.
- **Why it surfaces card candidates:** Largest regional incubator in Czechia (1,300+ companies supported over 20 years), runs JICbooster (early stage, market validation, seed access) and JIC STARCUBE (the country's longest-running accelerator). Fintech-adjacent clients visible include Tatum.io (blockchain infrastructure), Crypkit, Reservio (booking with payments) and SMS Ticket (ticketing payments). Brno companies are systematically under-covered by Prague-centric fintech press.
- **Approximate list size:** Roughly 400 logos rendered on the clients page; 1,300+ companies supported historically
- **Confidence:** Verified
- **Evidence:** Fetched the English homepage (nav structure, 1,300+ companies, JICbooster and JICplus programmes) and the clients page, where I confirmed the logo-grid structure, the "Load more" control, and read 15+ company names including the fintech-adjacent ones above.
- **Last checked:** 2026-08-25

### StartupYard (Prague)

- **Type:** accelerator
- **Geography:** Czech Republic, with international intake
- **Homepage:** https://startupyard.com/
- **List page:** No dedicated portfolio page. `https://startupyard.com/portfolio/` returns HTTP 404. Alumni are named on the homepage only.
- **Publicly listed?** partial
- **Machine readable?** HTML on the homepage, 17+ named companies plus "and many more…"
- **Update cadence:** Batch-based. Batch 15 announced 11 September 2025 via the blog at https://startupyard.com/blog/, which is where new cohorts appear first.
- **Why it surfaces card candidates:** Prague's longest-running accelerator, 70+ companies accelerated, EUR 30k investment per company. Named alumni include **BudgetBakers** (personal finance), **CityPay** and **Payowallet**, so there is a payments thread, though the programme's stated focus is deep tech, AI, IoT and cybersecurity rather than fintech. Worth watching the blog for batch announcements rather than scraping a list.
- **Approximate list size:** 17+ named on the homepage; 70+ accelerated in total
- **Confidence:** Verified
- **Evidence:** Fetched the homepage and confirmed the nav, the named alumni (Rossum, BudgetBakers, TeskaLabs, Gjirafa, Retino, CityPay, DishBoard), and the 11 September 2025 Batch 15 announcement. Separately confirmed `/portfolio/` returns HTTP 404, so the standard portfolio URL is a dead end.
- **Last checked:** 2026-08-25

### xPORT VŠE Business Accelerator (Prague University of Economics)

- **Type:** incubator (university)
- **Geography:** Czech Republic (Prague)
- **Homepage:** https://xport.cz/
- **List page:** https://xport.cz/tymy-v-xportu/
- **Publicly listed?** yes
- **Machine readable?** HTML, flat list of resident team names with paragraph descriptions
- **Update cadence:** Rolling. 3-month incubation cycles for student teams plus longer-term resident founders. The page sitemap (https://xport.cz/page-sitemap.xml) showed a `lastmod` of 2026-08-25, so the site is actively maintained.
- **Why it surfaces card candidates:** University incubators are the definition of the fringe here: no press coverage, no directory listings, real companies. The current resident list includes **ROIER**, a property-backed lending marketplace connecting individual investors with housing cooperatives, which is a lending platform with a plausible card need. Also runs an annual "Univerzitní startup" competition with funding.
- **Approximate list size:** Roughly 20 resident teams
- **Confidence:** Verified
- **Evidence:** The nav label "Naše týmy" points to a path that 404s; recovered the real URL from https://xport.cz/page-sitemap.xml. Fetched https://xport.cz/tymy-v-xportu/ (6.7 KB of text) and read the full team list with descriptions: ContextMinds, Scaleo, ShortPRO, ROIER, Quanda, Sentiscrape, TALENTDOCk, Future Sales, ATMT, SALESDOCk, Spectrasol, Competentia and others. Note one entry (Apexari) still carries lorem ipsum placeholder text, so the page is hand-maintained.
- **Last checked:** 2026-08-25

### czechstartups.gov.cz (CzechInvest)

- **Type:** register (government startup portal)
- **Geography:** Czech Republic
- **Homepage:** https://czechstartups.gov.cz/
- **List page:** https://czechstartups.gov.cz/startup-ekosystem/startupy/
- **Publicly listed?** partial
- **Machine readable?** HTML editorial page, no filters, no export, no API
- **Update cadence:** Unknown; content is editorial and appears infrequently refreshed. Copyright 2026.
- **Why it surfaces card candidates:** It does not, directly. This looked like a national startup register and is in fact a curated showcase of about 16 famous companies (Gen/Avast, Twisto, Liftago, STRV, Productboard, Kiwi.com). The homepage does cite 208 "startup infrastructure" entities and 44 investors, which suggests a fuller dataset exists behind the portal, but I could not reach a filterable list. Recorded so the next researcher does not repeat the effort.
- **Approximate list size:** 16 editorial profiles; 208 infrastructure entities claimed but not listed
- **Confidence:** Verified (that it is a showcase, not a register)
- **Evidence:** Fetched the homepage (CzechInvest branding, 44 investors, 208 startup infrastructure entities) and the startups page, which returned about 16 editorial success stories with no filtering, no export and no API. Only one fintech (Twisto).
- **Last checked:** 2026-08-25

### ITACA Business Incubator (Czech Republic): DEFUNCT

- **Type:** incubator
- **Geography:** Czech Republic
- **Homepage:** https://itaca.cz/ (dead)
- **List page:** none
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** not applicable
- **Why it surfaces card candidates:** It does not, and that is the point. Vestbee's current Czech accelerator roundup lists ITACA as one of only two Czech programmes with an explicit **FinTech** focus (alongside MedTech, CleanTech and AI, with 30+ mentors). It is dead. Anyone building a CEE fintech-accelerator target list from English-language roundups will pick this up as live.
- **Approximate list size:** none
- **Confidence:** Verified defunct
- **Evidence:** WebFetch failed with a TLS altname mismatch (the certificate covers `*.tilda.ws` only). Fetched with `curl -k`: HTTP 404 with the Tilda placeholder body "Domain has been assigned. Please go to the site settings and put the domain name in the Domain tab." The domain points at an unconfigured Tilda site.
- **Last checked:** 2026-08-25

---

## Hungary

### MBH FinTechLab (formerly MKB Fintechlab)

- **Type:** incubator and accelerator (bank-run, MBH Bank)
- **Geography:** Hungary, with CEE intake
- **Homepage:** https://fintechlab.hu/
- **List page:** https://fintechlab.hu/our-portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with one-line descriptions, split into active portfolio and exits
- **Update cadence:** Rolling investment plus a named early-stage programme, "Fintech Factory" (https://fintechlab.hu/fintech-factory/). Site copyright 2026.
- **Why it surfaces card candidates:** This is the highest-value Hungarian entry by a distance. Bank-owned, explicitly fintech, and the portfolio is dense with exactly TXN's greenfield profile: **Pastpay** (digital factoring and B2B BNPL for SMEs), **FintechX** (open banking and embedded finance), **hypomo** (online mortgage brokerage), **Space Invoices** (invoicing API for SaaS and e-commerce), **Tokeportal** (equity crowdfunding), **Limitless** (employee financial wellbeing), **Thinkout** (SME cash flow), **GeoFintech** (agricultural financing software), **Amon** (crypto debit card, already carded), **coinrule**. Embedded finance, factoring and financial-wellbeing platforms are the classic "about to add a card" segment.
- **Approximate list size:** Roughly 26 active companies listed plus 7 exits (Bookkeepie, Cloudent, complytron, compocity, ff.next, smapplab and one other). Treat the total as approximately 30 to 33.
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (confirmed the MKB to MBH rebrand, "Hungary's first incubator", the Fintech Factory programme, 2026 copyright) and the portfolio page, from which I read all active company names with descriptions and the exits section. Note the brand trap: English-language directories still list this as "MKB Fintechlab" and cite a 14-company portfolio from 2018.
- **Last checked:** 2026-08-25

### Hiventures (Hungarian state venture capital, MFB group)

- **Type:** VC portfolio plus incubation programmes (state-owned)
- **Geography:** Hungary
- **Homepage:** https://hiventures.hu/en/
- **List page:** https://hiventures.hu/portfolio-cegek/
- **Publicly listed?** partial
- **Machine readable?** HTML cards with Status (Active / Exited) and Industry filters, including a **FinTech/InsureTech** category. Company names sit behind per-company "Bővebben" detail links; the list page itself renders descriptions only.
- **Update cadence:** Continuous investment activity. The state's incubation and seed programmes make dozens of small investments a year, so the portfolio page grows steadily.
- **Why it surfaces card candidates:** The largest single source of early-stage Hungarian company names in existence, and state-run so it is exhaustive rather than curated. The FinTech/InsureTech filter is the entry point. Known portfolio companies include **PastPay** (B2B payments), and the visible descriptions include "Azonnal és bármikor lekérhető fizetés" (earned wage access) and Zeuss accounting software. A scraper would need to follow each detail link to recover company names.
- **Approximate list size:** 167 companies per VCBacked (third party, not confirmed on site); the rendered list page shows dozens of entries.
- **Confidence:** Verified (page and filters), Reported (portfolio count)
- **Evidence:** WebFetch failed twice with "unable to verify the first certificate". Fetched successfully with `curl -k` and a browser user-agent (HTTP 200). Confirmed the Status filter (Exitált / Aktív) and the full industry filter list including FinTech/InsureTech, and extracted the rendered company descriptions. Confirmed that company names are not present in the static list HTML.
- **Last checked:** 2026-08-25

### OXO Labs (Budapest)

- **Type:** incubator / early-stage venture programme
- **Geography:** Hungary and Central Europe
- **Homepage:** https://oxolabs.eu/
- **List page:** https://oxolabs.onlab.hu/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with Funded / Exited tabs
- **Update cadence:** Rolling. Site content dated to 2025 year-end activity.
- **Why it surfaces card candidates:** Honest answer: weakly. The 15-company portfolio contains **no fintech or payments companies** (IconicChain, zMed, GreenDrops/RotowerAI, TerraSky.ai, Medalyst, Appartman, EvolVeritas, Festivize, Vilhemp, Valley Leaves, Sharity Impact, Giggle, IC Events, Octopwn). Two are marketplace or gig-workforce plays (Giggle, Appartman) where disbursement is a plausible future need. Recorded because it is one of the few Hungarian programmes that publishes a complete named list, and because ruling it out saves the next researcher the trip.
- **Approximate list size:** 15 companies
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (confirmed the portfolio URL sits on a different host, `oxolabs.onlab.hu`) and the portfolio page, reading all 15 company names with descriptions and confirming the Funded / Exited tab structure.
- **Last checked:** 2026-08-25

### BnL Start Partners (Miskolc, North Hungary)

- **Type:** incubator (fintech-leaning, partnered with the University of Miskolc)
- **Geography:** Hungary (North Hungary region)
- **Homepage:** https://bnlstart.com/
- **List page:** none. Nav is Startup Factory, Mentoring, Funding, News, Team, FAQ, with no portfolio page.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Programme-driven and apparently slow: the visible programme is "GINOP-2.1.5 STARTUP FACTORY 2023" and the site describes its first acceleration programme as completed in 2020.
- **Why it surfaces card candidates:** Vestbee describes it as "Hungary's first B2B- and FinTech-focused startup incubator" with EUR 250k seed tickets and a EUR 2M fund. The site itself confirms the fintech bias in its own words: "As the founders of the incubator always highlighted their FinTech relations and network, most of the early-stage startups were selected from this field." A 24-company fintech-leaning portfolio in a Hungarian regional city is exactly the fringe TXN wants, but the names are not published. This is an outreach target, not a data source.
- **Approximate list size:** 24 companies claimed, none named publicly
- **Confidence:** Verified (site content), Unverified (portfolio composition)
- **Evidence:** WebFetch failed with "certificate has expired". Fetched with `curl -k` (HTTP 200) and read the About text confirming the 24-company portfolio, the fintech selection bias, 3 companies with follow-on external investment, 6 with next rounds totalling EUR 4M+, and one partial exit. Confirmed no portfolio or alumni page exists in the nav. The expired TLS certificate is itself a signal about how actively the site is maintained.
- **Last checked:** 2026-08-25

### Startup Campus (Budapest)

- **Type:** incubator
- **Geography:** Hungary
- **Homepage:** https://www.startupcampus.hu/
- **List page:** none found
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Latest named project launch is 1 January 2024 ("Startup Campus, Ötlettől a nemzetközi piacig! 2.0").
- **Why it surfaces card candidates:** Runs vertical programmes (HFDA for fashion and design, HUMDA for automotive and motorsport, TOKAJTECH for tourism and gastronomy, INNOGEN for youth) funded by Hungarian GINOP grants. The tourism, gastronomy and motorsport verticals are non-financial platforms where cards appear as a loyalty or disbursement need. But no participant list is published, so it can only be worked as a relationship.
- **Approximate list size:** unknown
- **Confidence:** Verified (that no list is published)
- **Evidence:** Fetched the homepage: confirmed founding year 2015, the four named vertical programmes, GINOP funding, the 1 January 2024 project launch, and the absence of any startup roster or alumni page.
- **Last checked:** 2026-08-25

### Design Terminal (Hungary): ABSORBED INTO CIVITTA

- **Type:** accelerator / mentoring programme (formerly)
- **Geography:** Hungary and CEE
- **Homepage:** https://designterminal.org/ (301 redirects to https://civitta.com/hu)
- **List page:** none. No alumni list survives at either domain.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Not applicable for the Design Terminal brand. The successor programmes at Civitta Hungary are active.
- **Why it surfaces card candidates:** It no longer does, and that is the finding. Design Terminal ran Hungary's best-known mentoring programme from 2014, putting 210+ startups through a 3-month intensive. Every English-language "accelerators in Hungary" list still cites it, including Vestbee (which points at `esabichu.designterminal.org` for ESA BIC Hungary). The brand's alumni corpus, 12 years of Hungarian founders, is no longer published anywhere I could find. The entity name survives as "Design Terminal Public Benefit Non-profit Ltd." in Civitta Hungary's footer. Successor programmes still live at Civitta Hungary: space-sector mentoring with up to EUR 60k, START Program Family (secondary and university students, 3-5M HUF grants), **V4 Startup Force** (Visegrád regional expansion, so PL, CZ, SK and HU intake), ESA BIC Hungary, NAK TechLab (agritech).
- **Approximate list size:** 210+ historical alumni, none published
- **Confidence:** Verified defunct as an independent brand
- **Evidence:** WebFetch on `designterminal.org` returned a 301 to a different host, `civitta.com/hu`. Fetched the redirect target and confirmed the Design Terminal entity name in the footer, the successor programme list, and the absence of any alumni directory. Separately confirmed `v4startupforce.com` does not resolve, so the V4 programme has no standalone site.
- **Last checked:** 2026-08-25

---

## Poland

### Huge Thing (Poznań)

- **Type:** accelerator
- **Geography:** Poland, with intake from 28 countries
- **Homepage:** https://hugething.vc/en/startups-and-innovations/
- **List page:** none. Four success stories on the main page, no portfolio directory.
- **Publicly listed?** partial
- **Machine readable?** HTML, showcase only
- **Update cadence:** Multiple live programmes with hard dates: Startup Booster by Huge Thing (18th edition, 2023-2026, equity-free grant), Female Fundraising Academy (3rd edition, 2026), Poznań Startup Contest (1st edition, applications closed **30 March 2026**).
- **Why it surfaces card candidates:** Huge Thing runs the startup recruitment for **PKO Bank Polski's Let's Fintech** programme, which makes it the practical front door to Poland's largest bank's fintech pipeline. Corporate partners include Alior Bank, PKO BP, PZU, Żabka, Rossmann and Veolia, so its cohorts are commerce and finance heavy. Named alumni include **Ramp Network** ($134M raised, crypto on-ramp payments) and Pergamin. But it publishes four logos, not a list.
- **Approximate list size:** 130 companies per Tracxn (third party); 41 startups to be accelerated in the current PARP-funded Startup Booster project across 9 rounds and 3 tracks.
- **Confidence:** Verified (programmes and dates), Reported (portfolio size)
- **Evidence:** Fetched https://hugething.vc/en/startups-and-innovations/ and confirmed the three live programmes with editions, the 30 March 2026 Poznań Startup Contest deadline, the four named success stories with funding figures, the additional testimonial companies (MY OVU, Tripso.ai, Space to Grow, Astrolayers, RIFFSEC), and the acceleration lead's contact. Confirmed no portfolio page exists in the nav.
- **Last checked:** 2026-08-25

### Let's Fintech with PKO Bank Polski

- **Type:** accelerator / corporate venturing (bank-run, PKO BP)
- **Geography:** Poland
- **Homepage:** https://fintech.pkobp.pl/ (English at https://fintech.pkobp.pl/eng)
- **List page:** none. Four partner companies shown on the English page.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Continuous recruitment ("rekrutacja prowadzona w trybie ciągłym"), no fixed cohort dates. Pilot and implementation announcements appear on the bank's press page at https://www.pkobp.pl/media/aktualnosci/.
- **Why it surfaces card candidates:** By volume this is the largest fintech screening funnel in Poland: **6,000+ companies analysed since 2015**, 5,000+ applications received, 1,000+ in 2025 alone, 100+ pilots run, 50+ converted to production implementations at the bank. The three-stage model (PoC pilot, commercial implementation, capital investment) means a company appearing in a PKO pilot announcement is a real, funded, pre-scale fintech. The catch: PKO publishes company names in press releases, not in a list. Named recent partners include 1Strike, Bright Technology, Settlemint, Agronet, XR Wizards, Travatar, WeGrant, vivaDrive, TerGO and Redigo Carbon.
- **Approximate list size:** 4 companies on the site; 100+ pilots historically, discoverable only via press releases
- **Confidence:** Verified
- **Evidence:** Note the URL trap: `https://www.pkobp.pl/fintech/let-s-fintech-with-pko-bank-polski/` returns HTTP 404. The live site is the `fintech.pkobp.pl` subdomain. Fetched the English page and confirmed the four partner companies, the 6,000-company screening figure, the 12M customer reach, and the absence of any portfolio listing or dated application window.
- **Last checked:** 2026-08-25

### MIT Enterprise Forum CEE

- **Type:** accelerator
- **Geography:** Poland-based, CEE-wide intake
- **Homepage:** https://mitefcee.org/
- **List page:** http://mitefcee.org/community/alumni-club/our-alumni (note: the HTTPS URL 301s to HTTP)
- **Publicly listed?** partial
- **Machine readable?** JS-rendered cards with industry filters including an explicit **Fintech & Insurtech** category and a "Show more" control. Only one company (Tamago) renders without JS.
- **Update cadence:** Cohort-based, with two named current tracks (Rethink Cohort, Pilot Ready Cohort). Historic editions ran roughly annually.
- **Why it surfaces card candidates:** 270+ accelerated startups with a dedicated Fintech & Insurtech filter, and the programme is CEE-wide rather than Polish-only, so it spans several MVP markets in one list. Corporate partners are Polish blue chips (Żabka, Rossmann, PZU). The "Pilot Ready" cohort framing means participants are at the stage of signing first commercial pilots, which is when a card programme decision gets made. Requires a headless browser to extract.
- **Approximate list size:** 270+ accelerated startups claimed
- **Confidence:** Verified (page and filters exist), Unverified (company names, which need JS rendering)
- **Evidence:** Fetched the homepage and mapped the nav to the alumni URL. Fetched the alumni page over HTTP after the HTTPS URL redirected. Confirmed the industry filter list (Energy, Enterprise Software, **Fintech & Insurtech**, FoodTech, Health, Industry 4.0, Martech and others), the card layout with a "Show more" control, and the 270+ figure. Only Tamago (tamago.software) was present in the server-rendered HTML.
- **Last checked:** 2026-08-25

### Kozminski Business Hub (Kozminski University, Warsaw)

- **Type:** incubator / university venture programme
- **Geography:** Poland
- **Homepage:** https://kozminskihub.com/
- **List page:** none
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Active, with upcoming webinars listed on the homepage.
- **Why it surfaces card candidates:** Kozminski is Poland's leading business school and the hub runs a Venture Lab (Fabryka Startupów, Akceleracja Startupów, Leothony business hackathons), an angel investor club, and the **Kozminski Impact Booster** grant programme worth up to 400,000 PLN per company. Named companies on site include **Incaso Group** (debt collection, an adjacent financial services play) and Plenti (electronics rental, a subscription-and-deposit model where cards matter). A university hub in Warsaw with a grant budget is a natural greenfield funnel, but no cohort roster is published.
- **Approximate list size:** 6 companies named; total unknown
- **Confidence:** Verified (that no list is published)
- **Evidence:** Fetched the homepage and confirmed the four programme pillars (Research & Consulting, Venture Lab, Angels, Impact Booster), the 400,000 PLN grant figure, the six named companies, and the absence of any startup directory page.
- **Last checked:** 2026-08-25

### Platformy startowe (PARP, Eastern Poland) and mapadotacji.gov.pl

- **Type:** scheme programme (EU and government) plus register
- **Geography:** Poland (Eastern Poland macroregion: lubelskie, podkarpackie, podlaskie, świętokrzyskie, warmińsko-mazurskie, and mazowieckie excluding metropolitan Warsaw)
- **Homepage:** https://www.parp.gov.pl/component/grants/grants/platformy-startowe
- **List page:** The programme pages publish no startup list. Beneficiary names are in the EU grant register at https://mapadotacji.gov.pl/projects/?lang=en, filterable by the "Platformy startowe dla nowych pomysłów" programme and by region.
- **Publicly listed?** partial (via the register, not the programme)
- **Machine readable?** Grant register is a filterable HTML search interface. No documented API or bulk export found.
- **Update cadence:** Rolling incubation rounds. One operator alone, Wschodni Akcelerator Biznesu 2 (https://wab.biz.pl/), is incubating 200 startups across 8 rounds, with round 8 closing **31 July 2026** and 279 applications received as of 3 August 2026. A separate PARP call ran 20 January to 17 March 2026 with a 30M PLN budget and up to 600,000 PLN per startup.
- **Why it surfaces card candidates:** This is the highest-volume greenfield funnel in Poland and it is invisible to fintech press because it is grant machinery, not a startup brand. Hundreds of newly-incorporated Polish companies pass through per year, each having just received an incubation grant, each about to build a product. Named operators include Unicorn Hub (Lublin), Wschodni Akcelerator Biznesu (Puławy), Start in Podkarpackie (Rzeszów, Mielec), Idealist (Lublin), Startup Heroes (Olsztyn, Ełk), Hub of Talents 2 (Białystok, Łomża) and HugeTECH Revolution. The grant register turns them into company names.
- **Approximate list size:** 200 startups per operator project; hundreds across the programme
- **Confidence:** Verified
- **Evidence:** Fetched the PARP programme page (enumerated the six named operators with cities, confirmed the "Nabór został zakończony" status for that call and the archive links). Fetched https://wab.biz.pl/ (confirmed the 200-startup target, roughly 40,000 PLN grants, round 8 closing 31 July 2026, 279 applications as of 3 August 2026, and that no startup list is published). Fetched the grant register at mapadotacji.gov.pl and confirmed filters by region, EU fund, and by the "Platformy startowe dla nowych pomysłów" programme specifically. Could not confirm an API or bulk download.
- **Last checked:** 2026-08-25

### FinTech Poland Foundation

- **Type:** community / industry association
- **Geography:** Poland
- **Homepage:** https://fintechpoland.com/en/home/
- **List page:** https://fintechpoland.com/en/ecosystem/ (member benefits page; member logos are displayed on the site but no structured member directory was found)
- **Publicly listed?** partial
- **Machine readable?** logos only, no structured list
- **Update cadence:** Active. Latest news item 31 July 2026. Publishes a recurring sector report, "How to do FinTech in Poland 3.0" (29 August 2025).
- **Why it surfaces card candidates:** Not a cohort source, but the reports and the BIK HUB sandbox programme are where Polish fintechs surface before they launch, and the foundation runs Supervision FinTech Talks with the regulator. The report series is the single best periodic census of the Polish fintech sector. Worth tracking for the annual report drop rather than scraping.
- **Approximate list size:** unknown
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (confirmed the report series with dates, the BIK HUB sandbox, the 31 July 2026 news item) and the ecosystem page (confirmed it describes membership benefits and a "join the network" flow, with no public structured member list).
- **Last checked:** 2026-08-25

### mAccelerator (mBank, Poland): DEFUNCT

- **Type:** accelerator (bank-run, formerly)
- **Geography:** Poland
- **Homepage:** https://maccelerator.pl/ (domain parked)
- **List page:** none
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** not applicable
- **Why it surfaces card candidates:** It does not. mBank's corporate venture and acceleration arm is still cited in CEE fintech-accelerator lists. The domain now serves a cyberfolks.pl hosting placeholder. If TXN is building a target list of Polish bank accelerators, this one is gone.
- **Approximate list size:** none
- **Confidence:** Verified defunct
- **Evidence:** Fetched https://maccelerator.pl/ with curl (HTTP 200) and got the Polish hosting-provider placeholder: "Domena jest aktywna, ale strona nie została jeszcze uruchomiona" (the domain is active but the site has not been launched), with a cyberfolks.pl support address.
- **Last checked:** 2026-08-25

### RBL_START (Alior Bank / PZU, Poland): LIKELY DORMANT

- **Type:** accelerator (bank-run)
- **Geography:** Poland
- **Homepage:** https://rbl.aliorbank.pl/ (301s to the Alior Bank retail homepage)
- **List page:** none found
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Unknown. Reported editions: 1st from September 2018, 5th reported around 2022 with a EUR 10,000 prize per winner. No evidence of a 2025 or 2026 edition.
- **Why it surfaces card candidates:** RBL_START was Poland's most fintech-specific bank accelerator and its cohorts are a good historical greenfield list: the first edition selected 8 from about 100 applicants, including **PayPo** (BNPL, later took a 4M PLN investment from Alior), Investsuite, Aazzur, Spendee, POSbistro and Bankzee. If the programme is genuinely dead, that is worth knowing before anyone builds outreach around it.
- **Approximate list size:** 8 companies in the first edition; total unknown
- **Confidence:** Unverified (status), Reported (historical cohorts)
- **Evidence:** `https://rbl.aliorbank.pl/` returns HTTP 200 but resolves to the Alior Bank retail homepage with no accelerator content. The documented bank path `https://www.aliorbank.pl/dodatkowe-informacje/o-banku/rbl.html` returns HTTP 404. Cohort details above come from Polish trade press (MamStartup, spidersweb.pl, bank.pl) surfaced in search, not from a fetched programme page. Not confirmed dead, only that no live programme page could be found.
- **Last checked:** 2026-08-25

### Google for Startups Campus Warsaw: CLOSED (global directory survives)

- **Type:** accelerator / campus (corporate)
- **Geography:** Poland (formerly), global directory
- **Homepage:** https://campus.co/warsaw/ (301s to https://startup.google.com/)
- **List page:** https://www.google.com/for-startups/alumni/directory/
- **Publicly listed?** yes (the global alumni directory)
- **Machine readable?** JS-rendered directory with **Region** filters (Poland, Romania, Hungary and Czechia all present) and **Industry** filters including Finance & Fintech
- **Update cadence:** Continuous as new Google for Startups programmes complete worldwide.
- **Why it surfaces card candidates:** The Warsaw campus is closed, but the alumni directory still lets you intersect country and fintech across all four MVP markets in one query. It is a modest-yield source for TXN because Google alumni skew later-stage and better-covered, but the country plus fintech filter combination is rare and cheap to run.
- **Approximate list size:** "thousands of startups" claimed; per-country counts not disclosed without filtering
- **Confidence:** Verified
- **Evidence:** `https://campus.co/warsaw/` redirects to `startup.google.com`, confirming the campus-specific site is gone. Fetched the alumni directory page and confirmed the Region filter includes Poland, Romania, Hungary and Czechia, and the Industry filter includes a Finance & Fintech category. No company count is published.
- **Last checked:** 2026-08-25

---

## Regional / CEE-wide

### Startup Wise Guys

- **Type:** accelerator (multi-vertical, with a dedicated Fintech track)
- **Geography:** Baltics-headquartered, CEE-wide intake including all four MVP markets
- **Homepage:** https://startupwiseguys.com/
- **List page:** https://startupwiseguys.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML with filters for Status, Batch, Vertical and **Headquarter location** (country)
- **Update cadence:** Multiple batches per year across verticals. Fintech batches 1 through 5 are separately listed, plus a live Fintech Accelerator Program at https://startupwiseguys.com/all-programs/fintech-accelerator-program/ offering up to EUR 150k convertible (120k cash plus 30k programme) with EUR 250k follow-on.
- **Why it surfaces card candidates:** The only programme in this stream with a dedicated, repeated fintech vertical **and** a country filter, so you can pull "fintech batch, headquartered in Poland" directly. Fintech alumni include Ondato (KYC), Okredo (credit data), JetBeep (mobile wallet and payments) and Partly. The MVP-market counts are small but real: Poland 8, Romania 3, Czechia 1, Hungary 1. Status filters (Active 286, Active/partial exit 4, Exit 23) let you drop dead companies before outreach.
- **Approximate list size:** 450+ startups claimed; 313 with status labels in the filter counts
- **Confidence:** Verified
- **Evidence:** Fetched the portfolio page and confirmed the four filter dimensions, the status counts (286 / 4 / 23), the vertical list (Cyber & Data, **Fintech**, Proptech, SaaS, Sustainability, Web3, XR/AR/VR), the per-country counts for Poland, Czechia, Romania and Hungary, and named fintech-batch companies with their countries.
- **Last checked:** 2026-08-25

### ReaktorX

- **Type:** accelerator (under-25 founders, CEE, with a San Francisco residency)
- **Geography:** Central and Eastern Europe, Romanian-led
- **Homepage:** https://reaktorx.com/
- **List page:** portfolio section on the homepage, with per-company pages
- **Publicly listed?** yes
- **Machine readable?** HTML cards
- **Update cadence:** Annual batches. Selection March to June, San Francisco residency in August. Batch #12 is the most recent referenced (Batch #11 and #12 Demo Days both listed).
- **Why it surfaces card candidates:** Small and very early ($50k SAFE for roughly 5%), so most participants are pre-product. Its value is timing: it catches CEE founders 18-24 months before a card decision, which is the earliest useful point in TXN's funnel. Named portfolio: 3DAPI, HAIP, DIMA AI, Grais, Vivid Mind, The Linghos (exited). No fintechs in the current portfolio.
- **Approximate list size:** About 6 named companies visible; 12 batches historically
- **Confidence:** Verified
- **Evidence:** Fetched the homepage: confirmed the $50k for 5% SAFE terms, the March to June selection and August SF residency cycle, the Batch #11 and #12 Demo Day references, the current application status, and the six named portfolio companies. Do not confuse this with the Polish "ReaktorX" fintech pre-accelerator formerly run by the FinTech Poland Foundation; they are different programmes.
- **Last checked:** 2026-08-25

### 28DIGITAL (EIT-initiated, CEE and Southern Europe)

- **Type:** scheme programme (EU-backed venture incubation)
- **Geography:** CEE and Southern Europe, with Poland, Romania and Bulgaria named as the highest-volume markets and Hungary at 11 teams across recent editions
- **Homepage:** https://28digital.eu/
- **List page:** none found on site. Cohort figures reported by The Recursive at https://www.therecursive.com/cee-startups-28digital-push-to-scale-regional-tech/
- **Publicly listed?** no (on the programme site)
- **Machine readable?** no list
- **Update cadence:** Cycle-based (14 startups in the most recent cycle reported).
- **Why it surfaces card candidates:** Up to EUR 250,000 per startup with **no co-investment required**, across a 270-partner European network, targeting exactly the CEE markets TXN cares about. A newly funded EUR 250k CEE startup is a prime greenfield candidate. The problem is that the programme does not publish who it funds, so the signal has to come from The Recursive's coverage or from EIT reporting.
- **Approximate list size:** 150+ startups supported across CEE (reported); 14 in the most recent cycle
- **Confidence:** Verified (programme exists, EIT-initiated, three pillars: Talent, Tech, Trust), Unverified (cohort list)
- **Evidence:** Fetched the homepage and confirmed the EIT origin and the programme structure (Co-Creation Accelerator, SpeedTech, Scale Smart among others). Confirmed there is no cohort, alumni or portfolio listing URL on the homepage. The 150-startup and EUR 250k figures come from The Recursive, not from the programme site.
- **Last checked:** 2026-08-25

### Elevator Lab (Raiffeisen Bank International): COULD NOT VERIFY

- **Type:** accelerator (bank-run, fintech partnership programme)
- **Geography:** Austria plus CEE. RBI has subsidiaries in all four MVP markets, and the programme has historically run local chapters.
- **Homepage:** https://elevator-lab.com/ (HTTP 503)
- **List page:** unknown
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** On paper this is the single most relevant bank programme in the region for TXN: an explicitly fintech partnership programme, run by a bank with retail operations in Poland (formerly), Czechia, Romania and Hungary, offering paid pilots with budgets reported up to EUR 200,000 and four months of work with RBI experts. Historical cohorts were payments-heavy (MishiPay in payments and transactions, SONECT in cash-as-a-service, Asteria in SME banking, Gauss Algorithmics in Czechia). Its sister entity, **Elevator Ventures**, is RBI's corporate VC focused on CEE fintech and may be the better live route.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** WebFetch on `https://www.elevator-lab.com/` returned HTTP 503. Retried with `curl` using a desktop Chrome user-agent and an Accept-Language header against `https://elevator-lab.com/`: also HTTP 503, 30-byte body ("Http/1.1 Service Unavailable"). Cohort details above are from third-party press surfaced in search, not from a fetched programme page. Do not treat this entry as live without re-checking.
- **Last checked:** 2026-08-25
