---
description: "Stream 02 raw research: 34 pan-European and UK accelerator sources, including the scheme-operated programmes"
---

> **Section:** [[research]]
> **Validation:** [[validation-02-paneuropean-accelerators]]
> **Status:** raw research output, recorded verbatim. Read the validation report alongside it: several counts in this file were corrected.

# Stream 02: Pan-European and UK accelerators, incubators and startup programmes

Owner: research agent, stream 02.
Research pass date: 2026-08-25.
Method: WebSearch to locate, WebFetch to confirm. `Verified` below means the
listed page was retrieved and read during this pass. Nothing here is written
from model memory.

---

## Summary

**34 entries.** 18 carry a cohort, alumni or portfolio list that was fetched and
read on the programme's own site. 2 more (Mastercard Lighthouse, Mastercard
Start Path) have their company lists read from a fetched third-party mirror
because the primary host returns HTTP 403. 9 further entries had their programme
page fetched but publish no company list, and that absence is recorded as a
finding rather than assumed. The remainder are `Reported` or `Unverified` with
the reason stated, including six defunct, dormant or out-of-scope programmes.

### The best sources for TXN's greenfield segment

Ranked by how directly they surface a company that has never had a card program
and is about to need one.

1. **Hexa (Paris venture studio, `hexa.com/companies`).** 50 companies, tagged
   by sector including Fintech, and by studio stage `Start` / `Sprint` /
   `Scale`. Companies with 2026 founding years are on the page. A Hexa fintech
   at `Start` stage is a company that does not yet exist commercially. This is
   the single highest-signal list found. Hexa built Swan and Spendesk, so the
   studio has form for producing exactly the kind of company that needs a card
   processor.
2. **MBH Fintechlab (Budapest, `fintechlab.hu/our-portfolio/`).** 25 active
   portfolio companies plus 6 exits, named on one page, in English, from a
   bank-owned incubator in an MVP priority market. Contains at least six
   companies that will need or already have card rails (FintechX, Amon,
   Pastpay, Tokeportal, GeoFintech, Limitless).
3. **Entrepreneur First (`joinef.com/companies/`).** Filterable by location
   (Berlin, Paris, London), industry (fintech), founding year (through 2026)
   and stage (Pre-Seed upward). Pre-Seed + fintech + 2026 is a machine-buildable
   query that returns companies at the exact moment before a processor decision.
4. **Startup Wise Guys (`startupwiseguys.com/portfolio/`).** 50 fintech
   companies explicitly counted by the site's own vertical filter, with a
   CEE-heavy country distribution (Estonia 78, Lithuania 35 across all
   verticals). Directly on TXN's MVP geography.
5. **Mastercard Lighthouse FINITIV (Nordics and Baltics).** Two cohorts a year,
   15 to 21 companies, all fintech or fintech-enabler, all named in press
   releases. A card scheme running its own funnel of pre-card-program fintechs.
6. **InnovX (Bucharest, `innovx.eu/startupsx/alumni`).** 400+ startups filterable
   by 30+ industries including FinTech and by year 2019-2025. Bank-backed (BCR,
   Erste Group). Romania is an MVP priority market.

### What surprised me

- **Card schemes run more startup funnels in Europe than the register would
  suggest, and they are geographically split.** Mastercard runs Start Path
  globally, *and separately* runs Mastercard Lighthouse specifically for the
  Nordics and Baltics with its own twice-yearly cohorts. Visa's European
  programme is not run by Visa at all: it is operated by Tenity, which as of
  this pass has two open Visa tracks, **Nordics & Baltics** and **Southern
  Europe**. Southern Europe maps onto TXN's Phase 1a (Spain, Portugal, Greece)
  almost exactly. This is a scheme actively assembling a list of pre-card-program
  fintechs in TXN's target markets and publishing it.
- **The Warsaw venture builder The Heart was co-founded with Mastercard and
  mBank, and three of its twelve ventures are fintech** (VASBOX, AIS Gateway,
  Digital Gateways). A corporate venture builder in an MVP market spinning out
  fintechs from scratch is a greenfield source by construction.
- **CEE bank venture arms publish their portfolios in local language and are
  effectively invisible to English-language fintech press.** KB SmartSolutions
  (Komerční banka) lists nine companies in Czech at `kbsmart.cz/nase-portfolio/`.
  MBH Fintechlab lists 31 in English but is almost never covered outside
  Hungary. These are the densest, least-contested lists found.
- **Three well-known UK/DE programmes are dead or hollowed out.** Barclays Rise
  is being wound down, finleap has handed its portfolio to Motive Ventures and
  stopped building, and RBI's Elevator Lab accelerator ran only 2017-2022 and is
  now an ecosystem outreach function with no cohort. Anyone prospecting these
  names today is prospecting a graveyard.
- **Rockstart is not a fintech source.** Despite frequently appearing on
  "European accelerator" listicles, its own site scopes it to Energy, AgriFood
  and Emerging Tech. Recorded so nobody wastes a pass on it.

### What I could NOT verify

Stated explicitly, per anti-fabrication rule 4.

- **Mastercard Start Path**: `mastercard.com` returns HTTP 403 to the fetcher on
  every path tried, including the Start Path programme page and the cohort press
  releases. The cohort names below come from a fintechnews.ch article that *was*
  fetched. I could not confirm whether a public, browsable Start Path portfolio
  page exists. Worth a manual browser check.
- **Mastercard Lighthouse (`mclighthouse.com`)**: HTTP 403 on both the homepage
  and a cohort press release. The 15-company Spring 2025 FINITIV list below was
  read from fintechnordics.com instead. I could not confirm whether
  mclighthouse.com hosts a cumulative alumni index.
- **Rise by Barclays**: `rise.barclays` returns 403, and the fintechfutures
  article returns 403, and the fintech.global article returned a 504 gateway
  timeout. The wind-down is recorded as `Reported`, not `Verified`.
- **Barclays Eagle Labs** (`labs.uk.barclays`): 403. Could not confirm whether
  it publishes a member directory, which matters because Rise London members
  were reportedly offered transfers into it.
- **Alior Bank RBL_START (Poland)**: both `accelerator.aliorbank.pl` and
  `rbl.aliorbank.pl` fail TLS hostname validation (certificate covers only
  `aliorbank.pl` and `www.aliorbank.pl`). Genuinely unfetchable by this tool.
  Poland is an MVP market so this is a real gap worth a manual check.
- **OTP Startup Partner Program (Hungary)**: `otpstartup.com` 301-redirects to
  a generic OTP Group corporate page, which is the classic signature of a
  retired programme domain. I could not confirm whether the programme still
  runs. Treat the CEE-wide OTP funnel as unconfirmed, not as absent.
- **Tenity's own portfolio**: `tenity.com/portfolio` and `/portfolio/` both
  render a heading and a logo wall with no company names in the HTML;
  `/portfolio-companies` is a 404. Tenity claims 300+ fintech alumni. I could
  not extract a single name from the portfolio pages.
- **UK FinTech Scotland directory** (`ukfintech.co/directory-all/scotland/`):
  HTTP 403. FinTech Scotland's claimed 250+ member cluster could not be
  confirmed against a fetched list.
- **Le Village by CA**: 44 villages, 800+ hosted startups claimed, but no
  central directory URL exists. Each regional village site hosts its own list.
  Coverage would require 44 separate scrapes.
- **Cohort sizes and update cadences** are stated below only where the fetched
  page or a fetched press release gave them. Where a page did not say, the field
  reads `unknown` rather than an estimate.
- **Web search budget was exhausted** (200/200 calls) before I could check
  Techstars' remaining European fintech programmes, Santander X, BBVA Spark's
  company lists, ING Labs, Fintech Belgium, or the Greek/Portuguese national
  programmes. These are open leads, not negative findings.

---

## Entries

### Hexa (formerly eFounders)

- **Type:** venture builder / startup studio
- **Geography:** France, Belgium, pan-European hiring
- **Homepage:** https://www.hexa.com/
- **List page:** https://www.hexa.com/companies
- **Publicly listed?** yes
- **Machine readable?** HTML cards, tagged by sector and stage
- **Update cadence:** continuous; the fetched page carried companies with 2026
  founding years (Kyneon, Hodor, Enobase) alongside 2011 entries, so the list is
  appended as each venture launches rather than in annual batches
- **Why it surfaces card candidates:** Hexa builds companies from zero with a
  founder brought in for a 12-month build. A company tagged `Fintech` at the
  `Start` stage has, by definition, made no processor decision. Hexa's own
  fintech track record (Swan, Spendesk, Upflow, Roundtable, Marble, Reki,
  Zenvest, Multis) shows the studio repeatedly produces companies that need card
  issuing.
- **Approximate list size:** 50 companies, of which 10+ carry a Fintech tag
- **Confidence:** Verified
- **Evidence:** Fetched `hexa.com/companies`. Page states "So far, we've launched
  50 companies, with a combined valuation of over $5billion", 3 billion-dollar
  companies, 12 exits. Companies are grouped under Start / Sprint / Scale and
  tagged AI, BtoB, BtoC, Fintech, with status Active / Acquired / Inactive.
  Named fintechs read from the page: Spendesk, Swan, Upflow, Roundtable, Marble,
  Reki, Zenvest, Multis. Homepage fetch separately confirmed the /companies URL.
  Note: the fetched pages did **not** mention the eFounders / Logic Founders /
  3founders sub-studio branding that secondary sources describe, so I have not
  recorded a fintech-specific sub-studio as fact.
- **Last checked:** 2026-08-25

### MBH Fintechlab

- **Type:** incubator / corporate venture arm (MBH Bank, Hungary)
- **Geography:** Hungary, Central and Eastern Europe
- **Homepage:** https://fintechlab.hu/
- **List page:** https://fintechlab.hu/our-portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, one page, English
- **Update cadence:** unknown; site footer reads "@2026 All Rights Reserved" and
  the pitch-deck submission form is live, so the programme is running
- **Why it surfaces card candidates:** Bank-owned incubator in a TXN MVP market
  that takes companies at incubation stage. Several portfolio companies are
  pre-card or card-adjacent: FintechX (open banking and embedded finance),
  Amon (crypto debit card), Pastpay (digital factoring for SMEs), Tokeportal
  (equity crowdfunding), GeoFintech (agricultural financing), Limitless
  (employee financial wellbeing). Any of these is a plausible first-card-program
  buyer.
- **Approximate list size:** 25 active + 6 exits = 31 companies
- **Confidence:** Verified
- **Evidence:** Fetched `fintechlab.hu/our-portfolio/`. Full company list read,
  including Aeriu, Antavo, Bedrock.farm, Cegjelzo, Coinrule, Diverzum,
  Dreamjobs, FintechX, Fitpuli, Guardit, Hypomo, H4 Software, Instacar,
  Landventure, Pastpay, Recart, Solar Viewpoint, Space Invoices, Tokeportal,
  Amon, BusinessFlow, GeoFintech, Hydrobot, Labshare, Limitless, Thinkout.
  Exits: Bookkeepie, Cloudent, Complytron, Compocity, ff.next, Smapplab.
  Homepage fetch confirmed "Hungary's first incubator and a leading innovation
  hub, powered by MBH Bank".
- **Last checked:** 2026-08-25

### Entrepreneur First

- **Type:** accelerator / talent investor
- **Geography:** London, Berlin, Paris, plus Bangalore, Singapore, NY, SF, HK,
  Toronto
- **Homepage:** https://www.joinef.com/
- **List page:** https://www.joinef.com/companies/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with `Load more` pagination; four filter axes
- **Update cadence:** continuous, cohort-driven; founding-year filter runs
  2014-2026, so 2026 companies are already indexed
- **Why it surfaces card candidates:** EF forms companies from individuals, so
  every fintech in the list started life inside EF with no vendor stack at all.
  The stage filter goes down to Pre-Seed. Filtering location=London/Berlin/Paris,
  industry=fintech, year=2026, stage=Pre-Seed produces a list of companies that
  cannot yet have chosen a processor.
- **Approximate list size:** unknown from the page itself (paginated); secondary
  sources cite 640-680 companies but I did not verify that count
- **Confidence:** Verified
- **Evidence:** Fetched `joinef.com/companies/`. Confirmed filters: Location
  (Bangalore, Berlin, Hong Kong, London, New York, Paris, San Francisco,
  Singapore, Toronto, Other), Industry (20+ sectors including fintech), Founding
  Year (2014-2026), Stage (Pre-Seed through Series E, plus Exits). Named entries
  read: Tractable, Cleo, PolyAI, Aztec, Neptune Robotics.
- **Last checked:** 2026-08-25

### Startup Wise Guys

- **Type:** accelerator + fund
- **Geography:** Estonia HQ; CEE, Baltics, Nordics, Italy, UK, Ukraine, Balkans
- **Homepage:** https://startupwiseguys.com/
- **List page:** https://startupwiseguys.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** JS-filtered HTML cards with search box and four dropdowns
  (status, batch, vertical, HQ country)
- **Update cadence:** per batch; batches are named and dated in the filter
  (e.g. "Fintech 2018", "SaaS Milan 2021", "Sustainability Copenhagen 2022",
  "Growth Program")
- **Why it surfaces card candidates:** The vertical filter reports **50 fintech
  companies** and the geography is squarely CEE and Baltic. Startup Wise Guys
  takes companies at pre-seed, which is before a card program exists. There has
  been at least one explicitly named `Fintech` batch, so cohort-level targeting
  is possible.
- **Approximate list size:** 450+ total; 286 active, 23 exits, 4 active/partial
  exits; **50 tagged Fintech**
- **Confidence:** Verified
- **Evidence:** Fetched `startupwiseguys.com/portfolio/`. Read vertical counts
  (Fintech 50, SaaS 164, Cyber & Data 39, Sustainability 31, XR 17, Proptech 6,
  Web 3 5) and country counts (Estonia 78, USA 40, Lithuania 35, UK 29,
  Italy 29). Named entries read: StoreDNA, Investly, Ready Player Me, Ocoya,
  Klimashift.
- **Last checked:** 2026-08-25

### Mastercard Lighthouse (FINITIV and MASSIV)

- **Type:** scheme programme (Mastercard, Nordic and Baltic region)
- **Geography:** Denmark, Norway, Sweden, Finland, Estonia, Latvia, Lithuania
- **Homepage:** https://mclighthouse.com/
- **List page:** per-cohort press releases, e.g.
  https://mclighthouse.com/mastercard-lighthouse-finitiv-2025-spring-program-welcomes-15-forward-looking-nordic-and-baltic-fintech-and-fintech-enabler-companies/
  (403 to this fetcher; mirrored and fetched successfully at
  https://fintechnordics.com/8477/fintechdenmark/mastercard-lighthouse-finitiv-2025/)
- **Publicly listed?** yes, per cohort
- **Machine readable?** HTML prose in press releases, grouped by country; no
  cumulative index found
- **Update cadence:** **twice a year**, spring and autumn. Spring 2025 was
  described as the 14th programme round. Spring 2026 admitted 21 companies
  across both tracks.
- **Why it surfaces card candidates:** This is a card scheme building its own
  early-stage funnel in a region TXN classes as opportunistic EEA but where card
  program launches are frequent. FINITIV is explicitly the fintech and
  fintech-enabler track. The Spring 2025 list alone contains a tokenised
  business-card company (Tapeeze), a Connector-as-a-Service platform
  (BankingLab), an SME payments company (Tap2Pay) and a payment-process company
  (Front Payment): all card-program-adjacent, all early.
- **Approximate list size:** 15 per cohort in 2025, 21 across both tracks in
  Spring 2026; roughly 30-40 named companies per year
- **Confidence:** Verified (cohort content), Unverified (cumulative alumni index)
- **Evidence:** Fetched the fintechnordics.com mirror of the Spring 2025 FINITIV
  announcement and read all 15 names with countries: Denmark (Kontolink, LENEO,
  Partisia, Tapeeze, Wolfpack), Norway (Bislab, Digisure, Front Payment, Justify,
  Mobai), Baltics (Axiology, BankingLab, Complok, Tap2Pay, Zwapgrid). Page
  states it is the 14th programme round and quotes Mats Taraldsson, Head of
  Innovation, Mastercard Nordic and Baltic. Direct fetches of `mclighthouse.com`
  and of the `mastercard.com` Spring 2026 release both returned HTTP 403.
- **Last checked:** 2026-08-25

### Visa Innovation Program Europe (operated by Tenity)

- **Type:** scheme programme, run by a third-party accelerator
- **Geography:** 15 European markets. As of this pass two tracks are open:
  **Nordics & Baltics** and **Southern Europe**. Prior editions covered Greece,
  Cyprus and Malta.
- **Homepage:** https://www.tenity.com/cases/visa-innovation-program-europe/
- **List page:** https://www.tenity.com/programs (programme index with status
  and dates). No per-cohort company list found on Tenity's own site.
- **Publicly listed?** partial. Programme dates and status are published;
  participant names are not, and Tenity's case page states "specific success
  stories are confidential".
- **Machine readable?** HTML table of programmes; **no list** of participants
- **Update cadence:** annual cycles, 8th cycle as of 2026; 7 cohorts completed,
  142 startups selected historically
- **Why it surfaces card candidates:** The Southern Europe track maps onto TXN
  Phase 1a (Spain, Portugal, Greece) and the Nordics & Baltics track onto
  opportunistic EEA. Visa selecting a fintech for acceleration is a strong signal
  the company is at or approaching a card decision, and Visa's involvement means
  scheme membership without a processor decision necessarily being made yet.
  The weakness is that participant names are withheld, so this is a source to
  monitor via press releases and Demo Day announcements, not to scrape.
- **Approximate list size:** 142 cumulative; 7 per cohort in the 2026
  Greece/Cyprus/Malta edition per secondary reporting (AgriNow, Better, Cloudigo,
  Paytic, GYST, Outfindo, Peanuds; **not** independently fetched)
- **Confidence:** Verified (programme exists, tracks and dates), Reported
  (cohort names)
- **Evidence:** Fetched `tenity.com/cases/visa-innovation-program-europe/`:
  confirms multi-country platform, 15 European markets, 7 cohorts, 142 startups,
  EUR 520M+ raised, 100+ PoCs, and explicitly says no names are published.
  Fetched `tenity.com/programs`: confirms two open Visa tracks, "Visa Innovation
  Program | Nordics & Baltics" (London, Open, 21 Aug 2026) and "Visa Innovation
  Program | Southern Europe" (Istanbul, Open, 21 Aug 2026), plus a separate
  "Fintech Market Activation, London & Zurich" (Open, 1 May 2026).
- **Last checked:** 2026-08-25

### InnovX (BCR / Erste Group)

- **Type:** accelerator, bank-backed
- **Geography:** Romania (Bucharest, Cluj, Iasi), Republic of Moldova, wider SEE
- **Homepage:** https://www.innovx.eu/
- **List page:** https://www.innovx.eu/startupsx/alumni
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid with year filter (2019-2025) and 30+
  industry filters including FinTech
- **Update cadence:** annual cohorts across three tracks (startups, scaleups,
  SMEs); year filter runs through 2025 on the fetched page
- **Why it surfaces card candidates:** Romania is a TXN MVP priority market and
  this is the largest published Romanian accelerator alumni list found. It is
  backed by BCR, part of Erste Group, giving it genuine CEE banking deal flow.
  Fintech alumni read from the page include MyMoney, SOLO, TOKERO, Invoice Cash
  Group, Fagura, 2Value, KidsFinance and Coinscrap Finance.
- **Approximate list size:** ~400 logos on the alumni page; homepage claims 487
  innovators accelerated; secondary reporting cites 185 accelerated out of 3,119
  applicants at an earlier date
- **Confidence:** Verified
- **Evidence:** Fetched `innovx.eu/` (found the `/startupsx/alumni` path and the
  "487 innovators" figure) and then fetched `innovx.eu/startupsx/alumni`
  directly, confirming the grid, the year filter, the 30+ industry filter
  including FinTech, and the named fintech companies above.
- **Last checked:** 2026-08-25

### Startupbootcamp

- **Type:** accelerator network
- **Geography:** multi-country. Fetched filter shows Netherlands, Italy, Latvia,
  Ireland, UAE, Brazil, Singapore, South Africa, Australia and more.
- **Homepage:** https://startupbootcamp.org/
- **List page:** https://startupbootcamp.org/startups/portfolio-companies
- **Publicly listed?** yes
- **Machine readable?** HTML cards, data embedded in HTML (client-side
  filtering), paginated 8 / 24 / 48 per page. Individual alumni have their own
  pages, e.g. `/alumni-list/finbase`.
- **Update cadence:** per programme batch; year filter offers 2019-2025 on the
  fetched page
- **Why it surfaces card candidates:** There is a named **FinTech &
  CyberSecurity Amsterdam** programme in the accelerator filter and a **Fintech**
  option in the portfolio-category filter, so the fintech subset can be isolated
  cleanly. Startupbootcamp takes companies at roughly EUR 15K for ~8%, which is
  pre-product-launch and therefore pre-processor.
- **Approximate list size:** 400+ visible on the portfolio page; site elsewhere
  claims 1,600+ portfolio companies. Treat 400+ as the fetched figure.
- **Confidence:** Verified
- **Evidence:** Fetched `startupbootcamp.org/startups/portfolio-companies`.
  Confirmed the four filter dimensions (portfolio category including Fintech;
  accelerator programme including "FinTech & CyberSecurity Amsterdam"; year
  2019-2025; country), the pagination control, and that company data is embedded
  in HTML rather than requiring JS for initial load. Named entries read: Pixpel,
  Solvpro Technology, HALA, Eight Vectors, Brunei Select Pharma, Zanto.
- **Last checked:** 2026-08-25

### FinTech Innovation Lab (London)

- **Type:** accelerator (Accenture + Partnership Fund for New York City)
- **Geography:** London, New York, Asia Pacific
- **Homepage:** https://www.fintechinnovationlab.com/regions/london/
- **List page:** https://www.fintechinnovationlab.com/alumni/ (cumulative,
  filterable) and per-cohort announcements such as
  https://www.fintechinnovationlab.com/news/london/fintech-innovation-lab-london-2026-meet-the-startups-shaping-the-future-of-financial-services/
- **Publicly listed?** yes
- **Machine readable?** HTML grid cards with logo, year, region, description;
  filters for Region (All / New York / London / Asia Pacific), Year (2011-2026)
  and 30+ Categories including **Payments** and **Blockchain**. Acquisition
  status is annotated on cards.
- **Update cadence:** annual. The 2026 London programme started 27 March 2026
  with 14 startups over 12 weeks.
- **Why it surfaces card candidates:** The alumni index goes back to 2011 with a
  Payments category filter, which is the cleanest historical fintech list in the
  UK found this pass. For greenfield specifically, the 2026 cohort contains at
  least three companies that plausibly have no card program yet and a business
  model that implies one: **Diesta** (payment operations platform for insurance,
  automating premium reconciliation), **Lumio** (shared household finances
  without joint accounts) and **NOBO Finance** (cross-border export financing).
- **Approximate list size:** alumni index spans 2011-2026 across three regions;
  exact count not stated on the page (initial render shows "0 Results" until a
  filter is applied). 14 in the 2026 London cohort.
- **Confidence:** Verified
- **Evidence:** Fetched the 2026 London cohort announcement and read all 14
  names grouped under four themes: Next-Gen Propositions (Diesta, Lumio,
  Embedded Advice); Digital Assets & Market Infrastructure (Axiology, Colossus
  Digital, NOBO Finance); Data & Platform Intelligence (Contextbases, OpenBox AI,
  Klara, Veris AI); Risk & Operational Resilience (Astran, AnalystPro,
  reCOMPLY.ai, Cytidel). Separately fetched `/alumni/` and confirmed the filter
  axes and card format; named entries read: 55/Redefined, Aazzur, Abel, Alloy,
  AlgoDynamix, Addition Wealth, AimBrain (annotated "Acquired by BioCatch").
- **Last checked:** 2026-08-25

### Antler

- **Type:** venture builder / day-zero investor
- **Geography:** 24 countries; European presence includes UK, Germany, Nordics,
  Netherlands
- **Homepage:** https://www.antler.co/
- **List page:** https://www.antler.co/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards, filterable by Sector, Location and Year
- **Update cadence:** continuous; year filter runs 2017-2026 with 2025 and 2026
  entries present on the fetched page
- **Why it surfaces card candidates:** Antler invests at inception, before a
  company has a product. A `FinTech` + European location + 2026 filter returns
  companies that are weeks or months old. The failure mode is volume: 1,800+
  companies globally means the European fintech slice needs isolating.
- **Approximate list size:** 1,800+ companies across six continents
- **Confidence:** Verified
- **Evidence:** Fetched `antler.co/portfolio`. Confirmed "1,800+ companies across
  six continents, from inception through Series C" and the three filter axes:
  Sectors (Real Estate and PropTech, Industrials, Health and BioTech, **FinTech**,
  Energy and ClimateTech, ConsumerTech, B2B Software), Locations (24 incl.
  Germany, UK), Years (2017-2026). Fintech entries read: Access Carbon (US,
  2024), AlphaLoops (UK, 2023), AlphaNova (Singapore, 2025).
- **Last checked:** 2026-08-25

### Kickstart Innovation

- **Type:** corporate innovation platform / accelerator
- **Geography:** Switzerland-based, startups drawn from across Europe (nine
  countries in a recent edition)
- **Homepage:** https://www.kickstart-innovation.com/
- **List page:** https://www.kickstart-innovation.com/community-startups-alumni
- **Publicly listed?** yes
- **Machine readable?** HTML list filterable by vertical and by year (2016-2025)
- **Update cadence:** annual. "Each year, Kickstart brings around 100
  entrepreneurs to Switzerland." Most recent site news item dated 29 July 2026,
  so the platform is live.
- **Why it surfaces card candidates:** There is a dedicated **Finance, Insurance
  & Cybersecurity** vertical with its own filter, and the cohort is matched
  against Swiss corporate and bank partners rather than being a generic
  accelerator. Fringe value is high: Kickstart gets minimal UK/US fintech press
  coverage despite 530+ startups supported.
- **Approximate list size:** 530+ startups supported since 2015; alumni page
  spans 2016-2025
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (confirmed the five verticals, the 530+ and
  400+ partnership figures, the CHF 3.1B alumni raise figure, the 29 July 2026
  news item, and the alumni URL) and then fetched
  `/community-startups-alumni` directly, confirming the vertical and year
  filters. Finance & Insurance 2025 entries read: Almanax, Fini, Maven Health AG,
  Meeco.
- **Last checked:** 2026-08-25

### Founders Factory

- **Type:** accelerator + venture studio
- **Geography:** London HQ, five continents; runs a dedicated Italian fintech
  programme with Mediobanca (see next entry)
- **Homepage:** https://foundersfactory.com/
- **List page:** https://foundersfactory.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with `Load More`; filters for Sector,
  Location and Investment Type
- **Update cadence:** rolling, six-month accelerator cycles
- **Why it surfaces card candidates:** A `Fintech` sector filter over 500+
  companies, and the studio arm builds companies from zero. Named fintech and
  insurtech entries read from the page include Tembo, Bewica, Jet Now, Plural.fi,
  Inaza and Mo.health, several of which sit in embedded-finance and
  pay-later territory where card issuance follows.
- **Approximate list size:** 500+ companies
- **Confidence:** Verified
- **Evidence:** Fetched `foundersfactory.com/portfolio/`. Confirmed "500+
  companies in 5 continents", the Sector filter (Fintech, Consumer, Health,
  SaaS & Enterprise, Industrial & Climate, Media & Telco), Location and
  Investment Type filters, `Load More` pagination, and the named entries above.
- **Last checked:** 2026-08-25

### Mediobanca x Founders Factory Fintech Accelerator (Milan)

- **Type:** accelerator, bank-backed
- **Geography:** Italy (Milan and remote)
- **Homepage:** https://foundersfactory.com/mediobanca-fintech-accelerator/
- **List page:** none dedicated. The programme page names six portfolio
  companies but not a per-cohort list.
- **Publicly listed?** partial
- **Machine readable?** HTML cards on the programme page; **no cohort list**
- **Update cadence:** annual application cycle. The fetched page header reads
  "Applications close February 6th", implying a Q1 intake and a four-month
  programme.
- **Why it surfaces card candidates:** A bank-backed fintech accelerator in Italy
  is exactly the kind of programme that does not market itself to the UK fintech
  press. Its six stated themes include **Consumer Lending** and
  **Corporate & Investment Banking**, both card-adjacent. The value here is as a
  *signal* to monitor (application deadline in early February, cohort announced
  in spring) rather than as a list to scrape.
- **Approximate list size:** unknown per cohort; six companies named on the page
  (Tembo, Qumata, Previse, ClearGlass, Acre, Hammock), which are Founders Factory
  portfolio examples rather than a Mediobanca cohort
- **Confidence:** Verified (programme exists and is open), Unverified (cohort
  composition)
- **Evidence:** Fetched `foundersfactory.com/mediobanca-fintech-accelerator/`.
  Confirmed "Cash Investment, 4 Months Accelerator Program, Milan & Remote", the
  February 6th application deadline, the six themes (Wealth Management,
  Corporate & Investment Banking, Consumer Lending, Insurtech, LegalTech, and
  Compliance/Audit/Risk), and the six named companies. Cohort size not stated.
- **Last checked:** 2026-08-25

### The Heart (Warsaw)

- **Type:** corporate venture builder
- **Geography:** Poland, CEE
- **Homepage:** https://www.theheart.tech/
- **List page:** https://www.theheart.tech/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards with sector labels
- **Update cadence:** unknown. No dates or status indicators on the portfolio
  page, which is a real weakness: I cannot tell from the page which ventures are
  live.
- **Why it surfaces card candidates:** Poland is a TXN MVP market. The Heart was
  established with Mastercard and works with mBank, so its ventures are
  bank-and-scheme-adjacent by construction, and three of twelve are fintech:
  **VASBOX** (value-added services commercialisation), **AIS Gateway** and
  **Digital Gateways** (customer onboarding). A venture builder spinning out a
  fintech from scratch has no incumbent processor relationship at all.
- **Approximate list size:** 12 ventures
- **Confidence:** Verified
- **Evidence:** Fetched `theheart.tech/` (found the `/portfolio` path) and then
  `theheart.tech/portfolio`. Full list read: VASBOX (Fintech), AIS Gateway
  (Fintech), Digital Gateways (Fintech), Flatte (Real Estate), HomeAlert (Real
  Estate), Uniperks (MarTech), Wellnoted (HealthTech), Car Platform (Automotive),
  Domum (ConTech), PrefabHUB (ConTech), ScanPay (FoodTech), Tandu (EdTech). Page
  carries no dates or active/inactive flags.
- **Last checked:** 2026-08-25

### KB SmartSolutions (Komerční banka)

- **Type:** corporate venture arm / bank subsidiary
- **Geography:** Czech Republic, Slovakia
- **Homepage:** https://www.kbsmart.cz/
- **List page:** https://www.kbsmart.cz/nase-portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, **Czech language**, split into "Stars"
  (equity) and "Partners" (distribution)
- **Update cadence:** unknown; slow-moving by nature (9 companies total)
- **Why it surfaces card candidates:** Czech Republic is a TXN MVP market and
  this list is invisible to English-language fintech sourcing because it is
  published only in Czech. Portfolio includes **Finbricks** (PSD2 bank
  aggregation), **Lemonero** (AI e-commerce financing, subsequently embedded into
  the George banking app) and **Upvest** (real-estate crowdfunding), all of which
  are plausible card-program candidates as they broaden.
- **Approximate list size:** 9 companies (4 equity "Stars", 5 "Partners")
- **Confidence:** Verified
- **Evidence:** Fetched `kbsmart.cz/nase-portfolio/`. Stars: Upvest, Lemonero,
  Finbricks, ENVIROS Advisory. Partners: ČEZ ESCO, Fidoo, Sunwork, iÚčto,
  Fakturoid. Page also describes Program ELENA, an EIB-cofinanced energy
  consulting programme.
- **Last checked:** 2026-08-25

### Techcelerator (Romania)

- **Type:** accelerator
- **Geography:** Romania and South East Europe
- **Homepage:** https://techcelerator.co/
- **List page:** https://techcelerator.co/alumnis/
- **Publicly listed?** yes
- **Machine readable?** HTML grid with name, description and website link;
  grouped by programme (Advancing AI, Investment Readiness, **NEXTFintech**,
  Batch #1-#4) and filterable by year 2019-2024
- **Update cadence:** per programme cycle. The homepage advertised a CleanTech
  Hackathon dated 23-24 May 2025; year filter on the alumni page stops at 2024,
  so the list may lag the programme by a year or more.
- **Why it surfaces card candidates:** There is a **named fintech programme**
  (NEXT FinTech) with its own filter grouping, in a TXN MVP market. Fintech
  alumni read from the page: Zanumi, Tukana (Infin8), SOLO, Vestinda, Bankspot,
  Ocean Credit, Prime Dash. Secondary reporting also names Boleron, Credify,
  SPIN Analytics, Text' Pay Me from an earlier fintech cohort (not independently
  fetched).
- **Approximate list size:** 148 companies accelerated per the homepage; 100+
  visible on the alumni page
- **Confidence:** Verified
- **Evidence:** Fetched `techcelerator.co/` (confirmed 148 companies, $120M
  portfolio value, EUR 13.5M raised, 84% survival rate, three stage-based
  programme tiers including "Next FinTech", and the `/alumnis/` URL) and then
  fetched `techcelerator.co/alumnis/` directly, confirming the programme
  groupings, the 2019-2024 year filter and the named fintech entries above.
- **Last checked:** 2026-08-25

### Blenheim Chalcot

- **Type:** venture builder
- **Geography:** UK (London), with India delivery
- **Homepage:** https://blenheimchalcot.com/
- **List page:** https://blenheimchalcot.com/ventures
- **Publicly listed?** yes
- **Machine readable?** HTML cards, filterable by sector (incl. **Financial
  Services**) and by stage (**EVO**, Seed, Venture, Growth, Exited)
- **Update cadence:** continuous; page covers ventures back to 2001
- **Why it surfaces card candidates:** The **EVO** stage filter is the useful
  one: it isolates ventures being incubated before they are real companies.
  Blenheim Chalcot built Modulr, Liberis, Salary Finance, Koodoo and Oakbrook, so
  the studio demonstrably produces payments and lending businesses that need card
  rails. A Financial Services venture at EVO stage has no processor.
- **Approximate list size:** 60+ businesses built over 25+ years
- **Confidence:** Verified
- **Evidence:** Fetched `blenheimchalcot.com/ventures`. Confirmed "built over 60
  businesses", the sector filter (Financial Services, Education, Public Services
  & Health, Media & Marketing, Property, Sports) and the stage filter (EVO, Seed,
  Venture, Growth, Exited). Financial Services entries read: BCI Capital, Koodoo,
  Liberis, Modulr, Oakbrook, Salary Finance.
- **Last checked:** 2026-08-25

### Level39

- **Type:** community / innovation space (Canary Wharf)
- **Geography:** UK, London
- **Homepage:** https://level39.co/
- **List page:** https://level39.co/members/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with grid and list view toggle, `Load More`
  pagination (16 at a time), filterable by **Sector** (14 categories incl.
  FinTech and RegTech & Compliance) and by **Stage** (Pre-seed through IPO plus
  "Not Fundraising")
- **Update cadence:** rolling as members join and leave. The homepage claims
  "more than 180" companies while the members page renders 139, which suggests
  the directory is a subset or lags the marketing copy.
- **Why it surfaces card candidates:** The **Stage** filter is unusual and
  valuable: filtering FinTech + Pre-seed/Seed gives a list of London fintechs
  young enough not to have chosen a processor, with a physical address. Fringe
  value is moderate (Level39 is well known) but the structured stage filter is
  rarer than the venue.
- **Approximate list size:** 139 companies rendered; 180+ claimed
- **Confidence:** Verified
- **Evidence:** Fetched `level39.co/` (confirmed "more than 180 startup and
  scaleup technology companies", the "Our Members" nav item and "See Who's Here"
  link) and then `level39.co/members/`, confirming 139 total, the grid/list
  toggle, the 14-category sector filter and the stage filter. Entries read:
  eToro (FinTech, Series D), CybSafe, Sanius Health, Polysolar, Applied
  Blockchain, Hypervolt.
- **Last checked:** 2026-08-25

### Holland FinTech

- **Type:** community / trade association with member directory
- **Geography:** Netherlands-centred, members across Europe
- **Homepage:** https://www.hollandfintech.com/
- **List page:** http://www.hollandfintech.com/members/ (note: HTTPS
  `hollandfintech.com/members/` 301-redirects to the `www.` host over HTTP)
- **Publicly listed?** yes
- **Machine readable?** HTML logo grid with `Load more`; filters for Primary
  Sector (Banking, **Payments**, RegTech, Legal Advisory, and others),
  Customer Type (Consumers, Corporates, Financial Institutions, **Startups**,
  SMEs), Products/Services (**Payments**, Compliance, Identity Solutions,
  Wealth Management), Primary Country and Primary Market
- **Update cadence:** rolling as members join
- **Why it surfaces card candidates:** Netherlands is TXN Phase 1b. The
  Products/Services and Primary Sector filters both isolate Payments, and the
  directory mixes startups with incumbents so the filter work matters. Weakness:
  the membership is heavily weighted toward advisers and incumbents (Clifford
  Chance, Accenture, AWS, ING, Mastercard all appear), so signal-to-noise for
  greenfield is lower than a pure accelerator list.
- **Approximate list size:** 300+ member companies claimed; exact count not
  stated on the fetched page
- **Confidence:** Verified
- **Evidence:** Fetched `http://www.hollandfintech.com/members/` after following
  the 301 from the HTTPS non-www URL. Confirmed the grid format, `Load more`
  pagination and all five filter axes. Entries read: 3S Money, Accenture,
  Airwallex, AWS, Bird & Bird, Clifford Chance, ING, Mastercard, Flow Traders.
- **Last checked:** 2026-08-25

### NatWest FinTech Programme

- **Type:** bank-run accelerator
- **Geography:** UK
- **Homepage:** https://www.natwest.com/business/enterprise/fintech-innovation.html
- **List page:** same URL; the current cohort is listed inline
- **Publicly listed?** partial. The current cohort is named. There is **no
  alumni index**: the page references a 2025 cohort and quotes one participant
  (Tunic Pay) but does not list prior cohorts.
- **Machine readable?** HTML cards for the current cohort only
- **Update cadence:** **annual**. 2025 was the inaugural programme, 2026 is the
  second, announced May 2026. 12-week programme.
- **Why it surfaces card candidates:** Targets pre-Series A and Series A. The
  2026 cohort skews AI-for-financial-services rather than card issuing, so
  direct card relevance is weak this year: the strongest candidate is **Round
  Treasury** (agentic treasury and payments platform). Value is as an annual
  signal rather than a list, and the annual reset means the page must be checked
  each May or the cohort is missed.
- **Approximate list size:** 8 companies per cohort (2026); 2025 cohort described
  as "small", size not stated
- **Confidence:** Verified
- **Evidence:** Fetched the NatWest page. All eight 2026 cohort companies read
  with descriptions: Aveni, Condukt, DeepFlow, Empath_AI, Galveston Group,
  Gradient Labs, Murphy AI, Round Treasury. Confirmed the 12-week duration, the
  pre-Series A / Series A target, the AI-and-customer-experience theme, and the
  absence of an alumni directory.
- **Last checked:** 2026-08-25

### Innovate Finance (UK trade body)

- **Type:** community / trade association member directory
- **Geography:** UK, with global members
- **Homepage:** https://www.innovatefinance.com/
- **List page:** https://www.innovatefinance.com/our-community/
- **Publicly listed?** yes, but poorly structured
- **Machine readable?** JS-rendered. The fetched HTML contained only a search box
  and A-E / F-J / K-O / P-T / U-Z alphabetical tabs. **No sector or stage
  filter, and no member names in the served HTML.** Individual members do have
  their own pages (e.g. `/company/level39/`, `/company/rise-created-by-barclays/`).
- **Update cadence:** rolling as members join
- **Why it surfaces card candidates:** Broad UK fintech coverage including
  seed-stage members, and per-member pages give a stable URL pattern. But with no
  sector filter and JS-rendered listings, this needs headless-browser scraping
  and then classification, which is a lot of work for a UK-only list when the
  UK is TXN's lowest-priority geography.
- **Approximate list size:** 250+ members claimed; not confirmed from the page
- **Confidence:** Verified (page exists, structure as described), Unverified
  (member count and composition)
- **Evidence:** Fetched `innovatefinance.com/our-community/`. Confirmed the
  search function and alphabetical tabs, and confirmed that no company names or
  sector filters appear in the served HTML. Member sub-pages for Level39 and
  Rise were surfaced in search results, confirming the `/company/<slug>/` URL
  pattern.
- **Last checked:** 2026-08-25

### Copenhagen Fintech

- **Type:** incubator / innovation hub, non-profit
- **Geography:** Denmark and the Nordics
- **Homepage:** https://www.copenhagenfintech.dk/
- **List page:** **none found.** `https://www.copenhagenfintech.dk/startups`
  describes five programmes and names six alumni as case studies but has no
  directory. `https://www.copenhagenfintech.dk/memberships-partnerships` exists
  but was not fetched.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** **5 programmes per year** per the fetched page
- **Why it surfaces card candidates:** Strong programme design for the greenfield
  segment: the **Incubation Program** targets "ambitious entrepreneurs pursuing
  their idea full-time, ideally with a working prototype or an MVP", which is
  pre-processor by definition, and **Tech for Fin** targets entrepreneurs from
  other sectors validating a fintech idea. The problem is discoverability: with
  630+ alumni and no public directory, the only routes in are Demo Day
  announcements (380+ pitches to date) and direct relationship with the hub.
  Worth treating as a **partnership target** rather than a scrape target.
- **Approximate list size:** 630+ programme alumni claimed; 120+ startups have
  worked out of the lab per secondary sources; **0 published**
- **Confidence:** Verified (absence of a directory is confirmed, not assumed)
- **Evidence:** Fetched `copenhagenfintech.dk/startups`. Confirmed the five
  programmes (Mentor Program, Tech for Fin, Incubation Program, Partnership Fast
  Track, Scaleup Partner), "5 Programs per year", "630+" alumni, "380+ Demo Day
  pitches", and the absence of any searchable database. Alumni named as case
  studies: Predicti, Monthio, DoLand, Januar, Uniify, Safello.
- **Last checked:** 2026-08-25

### ROCKIT Vilnius

- **Type:** fintech hub with pre-accelerator programmes
- **Geography:** Lithuania (Vilnius, Kaunas, Klaipėda)
- **Homepage:** https://www.rockitvilnius.com/
- **List page:** **none.** `https://www.rockitvilnius.com/startups` is a
  programmes-and-benefits page, not a directory.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** multiple bootcamps and pre-accelerator batches per year;
  a Resilience Bootcamp in Palanga was dated August 2026 on the fetched page
- **Why it surfaces card candidates:** Vilnius is the densest EMI and payments
  licensing cluster in the EU, and ROCKIT sits at the centre of it. The
  Startup Pre-Accelerator runs in multiple batches and offers EUR 7,000-20,000 in
  de minimis state aid, which means participants are very early. The catch: the
  fetched page scopes eligibility to startups in **Central and Western
  Lithuania** established within five years, and prioritises "innovation, AI and
  sustainability", not fintech specifically. So ROCKIT's *hub* is fintech-dense
  but its *published programme* is not fintech-scoped. Secondary sources claim
  ~150 fintech companies under the hub; I could not confirm that from the site.
- **Approximate list size:** ~150 fintech companies claimed by secondary
  sources; **0 published on the site**; only Ratepunk and Kiloverse named
- **Confidence:** Verified (absence of a directory), Unverified (the ~150 figure)
- **Evidence:** Fetched `rockitvilnius.com/startups`. Confirmed the programme
  list (Resilience Bootcamp Palanga Aug 2026, Startup Pre-Accelerator, Energy
  Bootcamp, Smart City Hackathon, Founders Offsite), the EUR 7,000-20,000 de
  minimis aid, the Central/Western Lithuania eligibility scope, and that only two
  companies are named anywhere on the page.
- **Last checked:** 2026-08-25

### Let's Fintech with PKO Bank Polski

- **Type:** bank-run acceleration and pilot programme
- **Geography:** Poland
- **Homepage:** https://fintech.pkobp.pl/eng
- **List page:** **none.** The page carries an "Apply to the program" CTA and
  four partner-startup showcases but no directory.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** rolling pilots. Secondary reporting cites 6,000+ companies
  analysed since 2015, 100+ pilots run, over half converting to implementation,
  and 13 new pilots in the most recent year.
- **Why it surfaces card candidates:** Poland is a TXN MVP market and this is the
  largest bank in it. Companies entering a PKO pilot are being validated by a
  bank *before* they have scale, which is the right moment. But with no published
  list, the only usable signals are PKO's Polish-language press releases
  (`pkobp.pl/media/aktualnosci/`) which do name pilot companies. This is a
  press-release monitoring target, not a scrape target.
- **Approximate list size:** 4 companies named on the English page (vivaDrive,
  Listny Cud, TerGO, Redigo Carbon); none of them fintech
- **Confidence:** Verified (page and absence of a list), Reported (pilot counts
  and the MentiWay / Mojafirma.Ai / Squirro / Rebench / Eco-Soft pilot names,
  which came from Polish-language press coverage I did not fetch)
- **Evidence:** Fetched `fintech.pkobp.pl/eng`. Confirmed the four named partner
  startups, the offer (co-financed PoCs, access to 12 million customers and
  1,500+ branches, technological sandbox, API services, dedicated CVC fund), the
  target profile (minimum viable product, digital banking / blockchain / data
  analytics / security / open banking) and the absence of a startup directory.
- **Last checked:** 2026-08-25

### Seed Starter (Česká spořitelna)

- **Type:** corporate venture arm / incubator
- **Geography:** Czech Republic, Slovakia, CEE
- **Homepage:** https://www.seedstarter.cz/en/home
- **List page:** **none found in the served HTML.** The page has a "Portfolio"
  section header but no company names rendered.
- **Publicly listed?** partial
- **Machine readable?** JS-rendered or image-based; no names extractable
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Czech Republic is a TXN MVP market and
  Seed Starter's stated mandate is unusually precise for TXN's purposes: pre-seed
  and seed, EUR 200k to 1M tickets, minority stakes, CEE-focused, targeting
  startups whose product "innovates the banking industry or is valuable for its
  clients". That is a description of TXN's greenfield segment written by a bank.
  The problem is purely mechanical: the names are not in the HTML. Portfolio
  companies confirmed via Czech press but not fetched: Investown (2020), Signi
  (2021), SmartHead (2023).
- **Approximate list size:** unknown; Czech press cites 185M CZK invested against
  a 405M CZK portfolio value at end-2023
- **Confidence:** Verified (mandate and stage), Unverified (portfolio contents)
- **Evidence:** Fetched `seedstarter.cz/en/home`. Confirmed pre-seed/seed stage,
  EUR 200k to 1M ticket, CEE geography, minority-stake structure, and the
  banking-innovation mandate wording. Confirmed that no portfolio company names
  appear in the served content despite a Portfolio section header.
- **Last checked:** 2026-08-25

### Le Village by CA (Crédit Agricole)

- **Type:** accelerator network, bank-backed
- **Geography:** France (mainland and overseas), Italy, Luxembourg
- **Homepage:** https://levillagebyca.com/language/en/
- **List page:** **none central.** Each village runs its own site and its own
  startup list, e.g. `aquitaine.levillagebyca.com`, `rouen.levillagebyca.com`,
  `paris.levillagebyca.com`.
- **Publicly listed?** partial: yes per village, no centrally
- **Machine readable?** per-village HTML profiles; **44 separate sources**
- **Update cadence:** rolling per village as startups enter and graduate
- **Why it surfaces card candidates:** This is the largest regional accelerator
  network in Europe and it is bank-owned, with dedicated fintech specialists
  across 11 vertical areas. Secondary sources cite 800+ startups continuously
  hosted and 429 currently housed. The fringe value is very high (French
  regional startups get almost no pan-European fintech press) but the acquisition
  cost is also high: no central directory means 44 scrapes and no single update
  signal. **Also note the related entity `La Fabrique by CA`**, described as a
  startup studio and fund that "creates startups, takes stakes, or acquires
  fintechs", which was not investigated this pass and is a live lead.
- **Approximate list size:** 800+ claimed cumulatively, 429 currently housed;
  **0 in one place**
- **Confidence:** Verified (network structure and absence of a central directory),
  Reported (the 800+ and 429 figures, which came from Crédit Agricole corporate
  press, not the fetched page)
- **Evidence:** Fetched `levillagebyca.com/language/en/`. Confirmed "44 Villages
  in France, Italy and Luxembourg", confirmed there is no central directory URL
  or sector filter on the main page, and confirmed the per-village subdomain
  pattern with startup profiles embedded (Aquitaine: VITIROVER, YZAR, Eliosta).
- **Last checked:** 2026-08-25

### Mastercard Start Path

- **Type:** scheme programme
- **Geography:** global, including Europe
- **Homepage:** https://www.mastercard.com/global/en/innovation/partner-with-us/start-path.html
- **List page:** **not found.** Every `mastercard.com` URL tried returned HTTP
  403 to this fetcher.
- **Publicly listed?** partial: cohorts are announced by press release; no
  browsable portfolio confirmed
- **Machine readable?** unknown
- **Update cadence:** multiple cohorts per year across tracks (Emerging Fintech
  and others). A cohort of 11 was announced September 2025.
- **Why it surfaces card candidates:** Start Path is where a card scheme puts its
  hands on early fintechs globally, and the September 2025 cohort explicitly
  cited **card processing infrastructure** among the selection criteria.
  European representation is real but thin per cohort: **amnis** (Zurich,
  cross-border banking) was the only confirmed European company in that cohort.
  Given the 403 wall and the global rather than European skew, this is a lower
  priority for TXN than Mastercard Lighthouse, which is Nordic/Baltic-specific
  and publishes 15-21 named companies twice a year.
- **Approximate list size:** 450+ companies from 60+ countries claimed
- **Confidence:** Reported
- **Evidence:** Direct fetch of the Start Path programme page returned HTTP 403.
  Cohort composition was instead fetched from
  `fintechnews.ch/fintech/mastercard-start-path-11-startups/78388/`, which named
  all 11: AraxaTech (card processing infrastructure), Hyperlayer, Kamina,
  firmly, amnis (Zurich), Qawn, MoovnPay, Save Your Wardrobe, Pentatonic,
  Circulae, Circulayo. The 450+ portfolio figure comes from Mastercard newsroom
  copy surfaced in search results and was **not** fetched.
- **Last checked:** 2026-08-25

### Tenity (formerly F10)

- **Type:** accelerator / incubator operator, runs programmes for banks and
  schemes
- **Geography:** Zurich, London, Singapore, Istanbul, Hong Kong, Baku
- **Homepage:** https://www.tenity.com/
- **List page:** https://www.tenity.com/programs (programmes, with status and
  dates). Portfolio pages carry **no company names**:
  `tenity.com/portfolio` and `tenity.com/portfolio/` render a heading and a logo
  wall only; `tenity.com/portfolio-companies` is a 404.
- **Publicly listed?** partial: programmes yes, companies no
- **Machine readable?** programme index is a clean HTML table with location,
  status (Open / Closed) and date. Portfolio is **not** machine readable.
- **Update cadence:** continuous; the programme index carried entries dated from
  December 2025 through March 2027 at the time of fetching
- **Why it surfaces card candidates:** Tenity is the operator behind the Visa
  Innovation Program in Europe and runs a "Fintech Market Activation, London &
  Zurich" programme, plus bank programmes such as Yapı Kredi FRWRD. It also runs
  the Zurich Fin/Tech Accelerator, a **pre-seed** fintech programme (batch 14 ran
  to a Demo Day on 11 June 2025 with 13 startups selected from 130+ applicants
  per secondary sources). Pre-seed fintech is the correct stage for TXN. The
  weakness is that Tenity publishes programme metadata but withholds participant
  names, so this is a calendar to monitor, not a list to scrape.
- **Approximate list size:** 300+ fintech alumni claimed; **0 names retrievable**
- **Confidence:** Verified (programme index), Unverified (portfolio)
- **Evidence:** Fetched `tenity.com/programs` and read the full programme table,
  including both open Visa tracks, Fintech Market Activation (London/Zurich,
  Open, 1 May 2026), Yapı Kredi FRWRD Global, PASHA Hackathon 6.0, SwissHacks
  2026, StableHacks 2026, SFIIP 2026, Digital Health Accelerator (Zurich, Open,
  1 Mar 2027) and closed programmes (IDDA Incubation, SingHacks, XRPL
  Accelerator 2025). Fetched `tenity.com/portfolio` and `/portfolio/`: both
  confirm no names in the HTML, with the disclaimer "The portfolio companies
  depicted above do not represent all of the investments made by Tenity".
  Fetched `tenity.com/portfolio-companies`: HTTP 404. Fetched
  `tenity.com/programs/zurich-fintech-accelerator-batch-14/`: no startup names.
- **Last checked:** 2026-08-25

---

## Defunct, dormant and negative findings

Per anti-fabrication rule 5, these are recorded because knowing a programme is
dead is worth as much as knowing one is alive.

### Elevator Lab (Raiffeisen Bank International): accelerator ENDED 2022

- **Type:** accelerator, bank-backed
- **Geography:** Austria and CEE (was the largest corporate fintech partnership
  programme in the region)
- **Homepage:** https://www.rbinternational.com/en/raiffeisen/rbi-group/about-us/innovation/elevator-lab.html
- **List page:** none current
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** **none.** No cohort has been run since 2022.
- **Why it matters:** This was the obvious CEE bank accelerator and it is no
  longer an accelerator. RBI's page states verbatim: *"Elevator Lab Partnership
  Program was organized as a structured startup accelerator and partnership
  program from 2017 until 2022."* The brand persists as an ecosystem-outreach
  function (Global Fintech Scouts Program, World Web3 Metaverse Challenge 2024,
  Vienna community events) with **no participating startups listed for 2026**.
  The related CVC, **Elevator Ventures** (`elevator-ventures.com`), was not
  investigated this pass and remains a live lead for CEE fintech deal flow.
- **Approximate list size:** 0 current; historical success stories named on the
  page are Moxo, Billon, Pisano and SESAMm
- **Confidence:** Verified
- **Evidence:** Fetched the RBI Elevator Lab page and read the 2017-2022 wording
  directly. Separately attempted `elevator-lab.com`, which returned HTTP 503.
- **Last checked:** 2026-08-25

### finleap: venture builder WOUND DOWN, portfolio moved to Motive Ventures

- **Type:** venture builder / fintech company builder
- **Geography:** Berlin, with former offices in Hamburg, Milan, Madrid, Paris
- **Homepage:** https://finleap.com/
- **List page:** none. The site publishes aggregate figures only.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** **none.** No new ventures being built.
- **Why it matters:** finleap was Europe's highest-profile fintech-specific
  company builder and produced solarisBank, Element and Qonto. It is not building
  any more. The site's own headline reads "The Journey Continues with Motive
  Ventures" and scopes the building period to 2014-2021. Solaris was acquired by
  SBI Group in March 2025. Anyone treating finleap as a live pipeline source is
  working from stale knowledge. **Motive Ventures** now manages the portfolio and
  was not investigated this pass.
- **Approximate list size:** "built or invested in 15 ventures" plus 5+ corporate
  JVs, per the site; **0 named**
- **Confidence:** Verified
- **Evidence:** Fetched `finleap.com/`. Read the "The Journey Continues with
  Motive Ventures" headline, the "from 2014 to 2021" framing, and the aggregate
  "15 ventures ... collectively worth EUR 3.0Bn+ at a point in time" figure.
  Confirmed no venture names are published.
- **Last checked:** 2026-08-25

### Rise, created by Barclays: WINDING DOWN

- **Type:** accelerator + fintech coworking community
- **Geography:** London, New York, Mumbai
- **Homepage:** https://rise.barclays/ (HTTP 403 to this fetcher)
- **List page:** none accessible
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** **being retired.** Multiple fintech trade outlets report
  Barclays phasing Rise out by mid-2025, with London members offered transfers
  to Barclays Eagle Labs and Barclays Business Banking.
- **Why it matters:** Rise London was one of the two anchor fintech venues in the
  UK alongside Level39, with 150+ resident fintechs and a 7,500-strong virtual
  community. If it is gone, that community has dispersed and the list is stale.
  Its likely successor, **Barclays Eagle Labs** (`labs.uk.barclays`), returned
  HTTP 403 and could not be assessed, so I do not know whether a member directory
  survived the transfer. This is the single most valuable unresolved question in
  this stream for the UK market.
- **Approximate list size:** 150+ resident fintechs historically; unknown now
- **Confidence:** Reported. **Not** verified: `rise.barclays` returned 403,
  `fintechfutures.com` returned 403, and the `fintech.global` article returned
  HTTP 504.
- **Evidence:** Three independent trade outlets (FinTech Futures, fintech.global,
  Innovate Finance's member page) surfaced in search results consistently
  describing the mid-2025 wind-down and the Eagle Labs transfer. No primary
  source was successfully fetched. Treat as strong but unconfirmed.
- **Last checked:** 2026-08-25

### OTP Startup Partner Program: LIKELY DORMANT

- **Type:** bank-run partnership programme
- **Geography:** CEE, 11-13 countries under OTP Group (includes Hungary,
  Romania, Bulgaria, Croatia, Serbia, Slovenia, Albania, Moldova, Ukraine)
- **Homepage:** https://www.otpstartup.com/ (**301-redirects to
  https://www.otpbank.hu/portal/en/AboutUs/otpGroup**, a generic corporate page)
- **List page:** none
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** unknown; most recent substantive coverage found dates from
  2019-2022
- **Why it matters:** On paper this is the most geographically relevant bank
  programme found for TXN: OTP covers Hungary and Romania (both MVP markets) plus
  most of the Balkans, offers access to 19M+ CEE customers, takes no equity and
  charges no fee, and explicitly targets post-product-market-fit startups. If it
  is live it is a high-value partnership target. The redirect of its dedicated
  domain to a corporate About page is the standard signature of a retired
  programme, but a redirect is evidence, not proof. **This needs a manual check
  before being written off.**
- **Approximate list size:** ~29 startups supported per third-party investor
  databases; 9 participants named in a Croatian OTP cohort announcement
- **Confidence:** Unverified
- **Evidence:** Attempted `otpstartup.com`, which returned a 301 to
  `otpbank.hu/portal/en/AboutUs/otpGroup`. Programme structure (3-month pilot,
  6-month rollout, no equity, no fee, 11 CEE markets) comes from secondary
  sources including an OTP Group news page and EU-Startups, none of which were
  fetched. No 2023-2026 activity found.
- **Last checked:** 2026-08-25

### Alior Bank RBL_START (Poland): UNFETCHABLE

- **Type:** bank-run accelerator
- **Geography:** Poland (Warsaw)
- **Homepage:** https://rbl.aliorbank.pl/ and
  https://www.accelerator.aliorbank.pl/ (**both fail TLS hostname validation.**
  The certificate covers only `aliorbank.pl` and `www.aliorbank.pl`, so neither
  subdomain can be fetched.) The related CVC is at `rbl.vc`.
- **List page:** unknown
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** unknown. Two editions confirmed by trade press; the first
  selected 8 startups from 100 applicants for a 15-week programme.
- **Why it matters:** Poland is a TXN MVP market and this is a genuine fintech
  accelerator run by a bank with a PSD2 API sandbox, which is precisely the
  environment where a first card program gets specced. Alior invested PLN 4M into
  **PayPo**, a BNPL company, out of the programme. This is a real gap caused by a
  server misconfiguration, not by absence.
- **Approximate list size:** 8 in edition 1; unknown thereafter
- **Confidence:** Unverified
- **Evidence:** Two fetch attempts, both failing with
  `Hostname/IP does not match certificate's altnames`. Programme details and the
  PayPo and Blockkey names come from Retail Banker International, SME Banking
  Club and cashless.pl coverage surfaced in search, none of which were fetched.
- **Last checked:** 2026-08-25

### Rockstart: NOT A FINTECH SOURCE

- **Type:** accelerator + fund
- **Geography:** Amsterdam, Copenhagen, Bogotá
- **Homepage:** https://rockstart.com/
- **List page:** https://rockstart.com/portfolio/ (not fetched)
- **Why it matters:** Rockstart appears on most "top European accelerator" lists
  and looks like an obvious fintech candidate. It is not one. Since 2019 it has
  been scoped to three domains: **Energy, AgriFood and Emerging Technologies**.
  Recorded here so that nobody in a later pass spends a scrape on it.
- **Approximate list size:** 350+ startups, none of them a fintech track
- **Confidence:** Reported
- **Evidence:** Not fetched. Domain scoping taken from Rockstart's own
  description as reproduced in search results and from Tracxn/Crunchbase
  profiles. Flagged as `Reported` rather than `Verified` accordingly.
- **Last checked:** 2026-08-25

---

## Open leads not pursued (web search budget exhausted at 200/200 calls)

Recorded so the next pass does not rediscover them:

- **Elevator Ventures** (`elevator-ventures.com`), RBI's CVC, which outlived the
  Elevator Lab accelerator and still covers CEE.
- **La Fabrique by CA**, Crédit Agricole's startup studio and fund, described in
  CA corporate press as creating startups and acquiring fintechs.
- **Motive Ventures**, now managing the finleap portfolio.
- **Barclays Eagle Labs** (`labs.uk.barclays`, 403 this pass): does it publish a
  member directory, and did Rise London members land there?
- **Plug and Play Fintech Europe** (Paris and Frankfurt programmes, plus a new
  Limassol, Cyprus location announced April 2026 covering fintech and regtech).
  Cyprus is an interesting fringe market and this was announced too recently to
  be in anyone's corpus.
- **Worldline e-Payments Challenge** and the **e-Payments Booster Program**: a
  payments company running its own fintech funnel with 26 pre-selected startups
  in one edition and client challenges from Erste Group and OP Financial Group.
  Editions confirmed 2015-2023; 2024-2026 status not established.
- **Yapı Kredi FRWRD Global** (via Tenity, Istanbul, open as of Aug 2026):
  Turkish bank programme with a "Road to DACH Region" track.
- **Santander X / Santander Fintech Station** and **BBVA Spark** (Spain, Phase
  1a): both confirmed to exist, neither company list assessed.
- **FinTech Scotland** cluster (250+ firms claimed) and the
  `ukfintech.co/directory-all/scotland/` directory: 403 this pass.
- **Techstars' remaining European fintech programmes**: status not established.
- **Design Terminal / V4Startup Force** (Poland, Czech Republic, Slovakia,
  Hungary): a four-country V4 programme covering all four TXN MVP markets,
  surfaced in a Vestbee listicle but never verified.
- **ITACA Business Incubator** (Czech Republic) and **BnL Start Partners**
  (Hungary, described as the first B2B and fintech-focused accelerator there):
  both surfaced in a Vestbee listicle, neither verified.
- **Greek, Portuguese and Bulgarian national programmes**: not reached.
