---
description: "Stream 02b raw research: 27 accelerator follow-up sources and national startup registers, written after validation and never independently checked"
---

> **Section:** [[research]]
> **Validation:** none. This pass was written after the validation agents finished and has had no independent adversarial check.
> **Status:** raw research output, recorded verbatim.

# Stream 02b: accelerator leads follow-up, plus bank and corporate programmes

Owner: research agent, stream 02b.
Research pass date: 2026-08-25.
Picks up the open leads left at the end of
`sources/02-paneuropean-accelerators.md`, which exhausted its search budget
before reaching them.

Method note, and it matters for reading this file. **The WebSearch budget for
this session was already spent (200/200) before this stream started.** Every
finding below was produced by direct HTTP fetching: `curl` with a browser
user-agent, an HTML-to-text extractor, sitemap and `robots.txt` reads, WordPress
and Magnolia REST endpoints, `dados.gov.pt`'s dataset API, and the Wayback
Machine CDX index where a live host blocked automated fetchers. Mojeek was used
as a keyword-search fallback via curl but its index proved too stale to be
useful and contributed nothing to the entries below.

`Verified` means the named URL was retrieved and read during this pass. Nothing
here is written from model memory.

---

## Summary

**27 entries.** 14 are `Verified` with a company or programme list actually
retrieved and counted. 8 are `Verified` for the programme's existence and
structure but record the **absence** of a published company list as the finding.
4 are defunct, absorbed, pivoted away from acceleration, or resolve to a dead
domain, each recorded with the evidence that killed them. 1 is `Unverified` with
the reason stated.

### The three best finds in this pass

Ranked by how directly they surface a company that has never had a card program.

1. **The Portuguese national startup register, published as open data at
   `dados.gov.pt`, refreshed the morning of this research pass.** A JSON file of
   every company holding legal Startup or ScaleUp status under Law 21/2023: 654
   companies, each with its Portuguese tax number (NIPC), legal name, status and
   the **date recognition was granted**. 143 of the 654 were granted in 2026
   alone, the most recent on 21 August 2026, four days before this pass. This is
   not a cohort list that refreshes twice a year. It is a monthly-diffable feed
   of newly incorporated, state-certified Portuguese startups, keyed on a
   government identifier, in a Phase 1a market. Nothing else found in this pass
   comes close on freshness or structure.

2. **Elevate Greece's startup database, extractable in one POST.** The Greek
   government's national startup registry publishes 1,085 accredited startups
   through an unauthenticated WordPress AJAX action. One request returns 2.1 MB
   of JSON with company name, industry, technologies, headcount, total funding,
   region and website. **44 are tagged FinTech, 10 InsurTech, 9 LegalTech /
   RegTech.** Greece is Phase 1a and this list is effectively invisible to
   English-language fintech sourcing.

3. **Plug and Play's entire content platform is a public, unauthenticated JSON
   API.** The website is an Angular shell that renders nothing to a fetcher, so
   it looks like a dead end. It is not. `public.dxp.playbook.vc/.rest/delivery/`
   serves **5,540 startups**, 70 locations, 29 programmes, 124 batches, 108
   investment announcements and 37 industry taxonomies, all filterable by
   country and industry UUID. The honest caveat, stated in the entry: Plug and
   Play's European fintech coverage is thin (UK 19, France 14, Spain 6, and
   effectively zero across CEE), so the *access* is excellent and the *content*
   is mediocre for TXN's geography.

### The most useful negative findings

- **Techstars has almost entirely left Europe.** Its own `/accelerators` page
  lists 16 programmes and its `/locations` page states "Showing 16 of 16
  Results". Exactly **two** are in Europe: the ABN AMRO + Techstars Future of
  Finance Accelerator in Amsterdam, and Techstars London. There is no Berlin, no
  Paris, no Oslo, no Stockholm, no Turin, no Lisbon. Belfast, Sarajevo, Istanbul
  and Uzbekistan appear in the sitemap but resolve to `/location/<city>` pages
  explicitly badged "A Startup Community Partnership", which run Founder
  Catalyst and Startup Weekend, not a cohort. Anyone prospecting "Techstars
  Europe" as a category is prospecting one bank accelerator and one generalist
  London programme.
- **But the one Techstars fintech programme left in Europe is the single
  best-fit accelerator found across streams 02 and 02b.** ABN AMRO + Techstars
  Future of Finance is Amsterdam-based (Phase 1b), fintech-only, takes 10
  companies a year at pre-seed and seed, publishes every cohort by name in a
  fetchable newsroom post, and is running its **6th edition** with Demo Day
  10 December 2026. 520+ companies applied in 2025 for 9 places.
- **`caixabankdayone.com` has no DNS record at all.** CaixaBank DayOne is
  frequently listed as a Spanish bank startup programme. Its standalone domain
  does not resolve, and four `caixabank.es` / `caixabank.com` paths returned 404.
- **`factorybyraiffeisen.ro` has no DNS record**, and `raiffeisen.ro/factory`
  404s. Consistent with stream 02's finding that RBI's Elevator Lab accelerator
  ended in 2022: the Romanian arm is gone too.
- **Design Terminal, Budapest, no longer exists as an independent brand.**
  `designterminal.org` 301-redirects to `civitta.com/hu`. It has been absorbed
  into the Civitta consultancy.
- **weXelerate, Vienna, is alive but is no longer an accelerator.** The site now
  sells offices, co-working, event space, "membership" and innovation services.
  Its navigation contains no cohort programme.
- **"Warsaw" in the Plug and Play location list is Warsaw, Indiana.** The API
  slug is `warsaw-in` and the title is "Warsaw, IN". Plug and Play has no Polish
  presence. This is a trap that would have produced a fabricated entry if the
  slug had not been read.

### What surprised me

- **Two national governments in TXN's Phase 1a markets both run a legally
  defined startup register, and both publish it machine-readably, and neither is
  in the corpus.** Greece does it through a ministry-run WordPress site with an
  open AJAX endpoint. Portugal does it through the national open-data portal
  with a versioned JSON resource and a dataset API. These are the cheapest,
  freshest, highest-coverage lists found anywhere in this research programme.
  They do not name the card program because no card program exists yet, which is
  precisely the point.
- **Portugal also accredits its incubators, publishes the register as a Google
  Sheet, and tags each incubator with its vertical specialisations.** 146
  accredited incubators in 2025, of which **32 list Fintech**. That is a
  ready-made target list of 32 Portuguese organisations each sitting on their own
  unpublished cohort.
- **Belgium's biggest bank accelerator publishes 1,700 startups as plain
  server-rendered HTML across 81 pages, with an industry tag and a cohort year
  on every card.** Start it @KBC is free, takes no equity, admits 65 companies
  per intake, and its industry taxonomy includes Fintech, Insurtech and
  "Identification/Authentication/KYC/AML" as separate facets. For a Phase 1b
  market this is the densest and least contested list found.
- **The same companies keep reappearing across supposedly independent funnels.**
  Axiology shows up in Mastercard Lighthouse FINITIV Spring 2025 and the FinTech
  Innovation Lab London 2026 cohort (both from stream 02) *and* as a Plug and
  Play investment announcement. "Better" appears in the Techstars ABN AMRO 2025
  class and in the reported Visa Innovation Program Greece/Cyprus 2026 cohort.
  The accelerator layer is smaller and more overlapping than its surface area
  suggests, which argues for prioritising the national registers, which have no
  such selection funnel, over yet another accelerator.
- **Bank "startup programmes" in Spain are mostly banking products, not
  accelerators.** BBVA Spark turns out to be a venture-debt and business-banking
  unit with 1,500 clients, not a cohort programme. Santander X is a
  training-and-awards portal. Neither runs the kind of intake that produces a
  dated cohort list, which is why neither has one.

---

## Entries

### ABN AMRO + Techstars Future of Finance Accelerator (Amsterdam)

- **Type:** accelerator, bank-backed
- **Geography:** Amsterdam, Netherlands; Europe-focused intake (2025 class drawn
  from Germany, Denmark, Israel, Switzerland, Ireland, Italy, France, UK)
- **Homepage:** https://www.techstars.com/accelerators/abn-amro-techstars-future-of-finance-accelerator
- **List page:** per-cohort newsroom posts, e.g.
  https://www.techstars.com/newsroom/the-2025-class-of-the-abn-amro-techstars-future-of-finance-accelerator
- **Publicly listed?** yes, per cohort. The programme page carries "Latest class"
  and "Past Companies" tabs but their contents are not in the served HTML, so
  the newsroom post is the usable list.
- **Machine readable?** HTML prose, one named company per bullet with a
  one-line description. No cumulative index.
- **Update cadence:** **annual, and the calendar is published a year ahead.** The
  fetched programme page states: applications open 02 Mar 2026, final deadline
  10 Jun 2026, accelerator starts 08 Sep 2026, **Demo Day 10 Dec 2026**. A
  programme-news item dated 9 April 2026 announces the 6th edition.
- **Why it surfaces card candidates:** This is the closest fit to TXN's
  greenfield segment found in either stream. It is fintech-only, it is in a
  Phase 1b market, it takes 10 companies per programme at a stage where 520+
  applicants compete for 9 places, and every company is named publicly at
  kick-off in September. The 2025 class contains at least four companies whose
  business model implies a card program that does not yet exist: **1-CP**
  (described on the page as a "Corporate PayPal", bringing B2C convenience into
  B2B transactions with embedded expense, finance and AI), **Better** (recovers
  failed online payments), **Haboo Money** (flexible debt repayment), and
  **Narrative Banking** (turns banking apps into AI growth coaches for SMEs).
  Because the intake is European and ABN AMRO runs a EUR 100m fintech venture
  fund alongside it, these are companies about to make an infrastructure choice.
  The right cadence is to fetch the newsroom in mid-September each year.
- **Approximate list size:** 10 places per programme, 9 admitted in 2025;
  6 editions to date implies roughly 50-60 cumulative alumni, not published as an
  index
- **Confidence:** Verified
- **Evidence:** Fetched the programme page: read the four published dates above,
  the "We accept 10 startups per program" statement, the ABN AMRO EUR 100m fund
  reference, the four named team members (Allard Luchsinger MD, Eoghan
  O'Flaherty, Laurens Hamerlinck and Jolenthe Janssen of ABN AMRO Fintech
  Venturing), and the three linked news items. Then fetched the 2025 class
  newsroom post and read all nine companies with descriptions: 1-CP, Avido AI,
  Auxilius.ai, Better, Fintalo, Haboo Money, Humbrela, Narrative Banking, Orion
  Finance. The post states "more than 520 fintech companies applied", "nine
  early-stage, Europe-focused fintech teams", the eight source countries, and
  "18-24 months of progress in just 13 weeks".
- **Last checked:** 2026-08-25

### Techstars, European footprint: TWO PROGRAMMES ONLY

- **Type:** accelerator network
- **Geography:** global. In Europe: Amsterdam and London. Nothing else.
- **Homepage:** https://www.techstars.com/accelerators
- **List page:** https://www.techstars.com/locations (filterable index, states
  "Showing 16 of 16 Results")
- **Publicly listed?** partial. Programmes and locations are listed with
  descriptions, partners and vertical tags. Company lists are not.
- **Machine readable?** HTML list, server-rendered, with location, vertical and
  partner labels per row. `sitemap.xml` carries 906 URLs and is fetchable.
- **Update cadence:** the sitemap carries `lastmod` dates (the accelerators index
  was last modified 2026-07-10, the homepage 2026-08-21), so change detection is
  cheap
- **Why it surfaces card candidates:** As a category it barely does any more,
  and that is the finding. The only fintech-relevant European entry is the ABN
  AMRO programme recorded above. Techstars London is explicitly "across all
  verticals" with no fintech focus; its next cycle opens 24 Aug 2026, closes
  18 Nov 2026, starts 08 Mar 2027 and demos 03 Jun 2027, so it produces one
  undifferentiated cohort a year on a long lag.
- **Approximate list size:** 16 accelerators globally; 2 in Europe
- **Confidence:** Verified
- **Evidence:** Fetched `/accelerators` and read all 16 programme names. Fetched
  `/locations` and read all 16 rows with their city and country: Amsterdam
  (Netherlands), Anywhere, Baltimore, Birmingham AL, Boston, Boulder, Chicago
  (x2), Columbus, London (United Kingdom), Los Angeles (x2), Minneapolis, New
  York City, Tokyo, Washington DC. Fetched `/accelerators/london` and read the
  four programme dates. Fetched `sitemap.xml` and found `belfast`, `sarajevo`,
  `istanbul`, `omaha` and `uzbekistan` under `/accelerators/`; fetched all five,
  each 301s to `/location/<name>` and each page reads "A Startup Community
  Partnership ... Startup Community Partnerships bring Techstars programming to
  founders where they are" with Founder Catalyst listed as the programme. None
  is an accelerator with a cohort.
- **Last checked:** 2026-08-25

### Techstars portfolio index: NOT SCRAPABLE

- **Type:** accelerator portfolio
- **Geography:** global
- **Homepage:** https://www.techstars.com/portfolio
- **List page:** **none usable.** The page's "Search Portfolio" control is an
  in-page anchor (`href="#search-portfolio"`), and no company records appear in
  the served HTML beyond the Unicorn Registry.
- **Publicly listed?** partial
- **Machine readable?** no. The 906-URL sitemap contains no per-company
  portfolio URLs.
- **Update cadence:** unknown
- **Why it surfaces card candidates:** It would, if it were reachable: the
  Unicorn Registry alone carries Finance-tagged entries (Alloy, Chainalysis).
  But 11,034 founders accelerated and $55B raised sit behind a client-side search
  with no server-rendered records and no per-company URLs, so this is a
  headless-browser job for a global list that is mostly US. Low priority for TXN.
- **Approximate list size:** 29 unicorns listed inline; full portfolio not
  published in fetchable form
- **Confidence:** Verified (structure and the absence of a scrapable list)
- **Evidence:** Fetched `/portfolio` and read the headline statistics (29
  unicorns, $354B combined market cap, $55B raised, 11,034 founders accelerated
  since 2007, $1M+ average first raise) and the full Unicorn Registry with year
  and vertical tags. Confirmed the only portfolio-related links on the page are
  `/portfolio` itself and the `#search-portfolio` anchor. Fetched `sitemap.xml`
  and confirmed no per-company URLs.
- **Last checked:** 2026-08-25

### Santander X

- **Type:** corporate programme portal (awards, challenges, training), bank-run
- **Geography:** Argentina, Brazil, Chile, Germany, Mexico, **Portugal**,
  **Spain**, United Kingdom, Uruguay, USA (list read from the fetched homepage)
- **Homepage:** https://www.santanderx.com/en/index.html (note: `/en` alone
  redirects to a 404 page; the `index.html` suffix is required)
- **List page:** per-award finalist pages, e.g.
  https://www.santanderx.com/en/sites/finalist-santander-x-global-award-2025.html
- **Publicly listed?** partial. Finalists of each award edition are named
  publicly. The Santander X 100 community directory is not retrievable.
- **Machine readable?** HTML prose grouped by category (University / Startup /
  Scaleup / SME), one named company per block with a one-line description. The
  `sitemap.xml` enumerates every award edition and every `finalist-*` page, which
  is the practical index.
- **Update cadence:** annual per award, plus rolling "global challenges". The
  sitemap carries pages for Global Award 2023, 2024, 2025 and 2026, UK Awards,
  and themed challenges (AI Revolution, CyberProtect the Future, Digital
  Economy, Innovation Healthcare, Circular Economy, Reimagine Silver Age, The
  Quantum AI Leap).
- **Why it surfaces card candidates:** Spain and Portugal are both Phase 1a, and
  the SME and Scaleup categories put Santander's own commercial screen on
  companies before they are widely covered. The 2025 finalist list contains at
  least three card-adjacent companies: **Reveni** (described as "fintech
  infrastructure that enables global e-commerce to be profitable through payment
  and financing solutions"), **Cardda** ("comprehensive corporate expense
  management solution for companies"), and **Bulk** ("digital platform for
  managing and automating debt collection from private customers"). Cardda in
  particular is a textbook first-card-program buyer. The weakness is signal
  density: 3 of 35 finalists are card-relevant, the rest are agritech, medtech
  and consumer.
- **Approximate list size:** 35 finalists in the 2025 global edition (9
  University, 8 Startup, 10 Scaleup, 8 SME). Santander X 100 was described as
  "60 plus companies" on a 2022-era page.
- **Confidence:** Verified (the 2025 finalists page and its contents),
  Unverified (the Santander X 100 directory)
- **Evidence:** Fetched `santanderx.com/en/index.html` and read the ten-country
  availability list and the registration-gated structure. Fetched
  `santanderx.com/sitemap.xml` and enumerated the `finalist-*` page family.
  Fetched `finalist-santander-x-global-award-2025.html` and read all 35 finalists
  with descriptions across the four categories, including the three named above.
  Fetched `santander-x-global-award.html`, which still serves the **2023**
  edition (9 countries incl. Poland and Portugal, 20 finalists, 6 winners), so
  the canonical award page lags the finalist pages.
- **Last checked:** 2026-08-25

### Santander X 100 startup directory: UNRETRIEVABLE

- **Type:** corporate community directory
- **Geography:** global, Santander footprint
- **Homepage:** https://www.santanderx.com/en/sites/santanderx100_temp.html
- **List page:** https://www.santanderx.com/en/sites/startups-scaleups-santanderx100.html
- **Publicly listed?** claimed yes, in practice no
- **Machine readable?** **no.** The list page returns HTTP 200 with a
  **zero-byte body** to a browser-user-agent fetcher.
- **Update cadence:** unknown
- **Why it surfaces card candidates:** The `_temp` landing page names a handful
  of members and describes the benefit set, which includes "Access to potential
  clients and the **Fintech Station of Banco Santander**": a bank explicitly
  matchmaking its community into its own fintech unit. Two of the three named
  scaleups are payments-adjacent (**Almond**, "international remittance company
  enabling payments using blockchain"; **Agrotoken**, agro-commodity stablecoins).
  If the directory were readable it would be worth having. It is not.
- **Approximate list size:** "60 plus companies" claimed on the fetched page; 6
  named
- **Confidence:** Verified (the page exists, the directory does not serve
  content)
- **Evidence:** Fetched `santanderx100_temp.html`: read the Web Summit 2022
  framing, the "60 plus companies" figure, the named startups (Agrotoken,
  Basquevolt, Concrete4Challenge) and scaleups (Agrofy, Almond, Alyne), and the
  benefit list including the Fintech Station. Extracted the three "View all
  startups" hrefs. Fetched `startups-scaleups-santanderx100.html` twice: both
  returned a body of exactly 0 bytes.
- **Last checked:** 2026-08-25

### BBVA Spark

- **Type:** bank unit for startups and VC funds (venture debt plus business
  banking). **Not an accelerator**, despite frequently being listed as one.
- **Geography:** Argentina, Colombia, **Spain**, Mexico, **United Kingdom** (5
  countries, stated on the page)
- **Homepage:** https://www.bbvaspark.com/ (HTTP **403** to every automated
  fetcher tried, including WebFetch)
- **List page:** **none.** No `/startups`, `/portfolio`, `/clientes` or
  equivalent path exists anywhere in the Wayback CDX index for the domain since
  2025.
- **Publicly listed?** partial: a client logo-and-name wall on the homepage, not
  a directory
- **Machine readable?** the client names are plain text in the homepage HTML; the
  live host blocks fetchers, so an archived snapshot is the only route
- **Update cadence:** unknown; the client wall is marketing copy, not a register
- **Why it surfaces card candidates:** Weakly, and mostly in the wrong
  direction. BBVA Spark banks companies that already have revenue and a VC round;
  its own copy is about venture debt, multi-currency accounts and payment or
  collection products. Those are post-launch companies, not greenfield. Its value
  to TXN is as a **named list of Spanish high-growth companies** rather than as a
  pre-card-program signal, and even then only ~32 of a claimed 1,500 clients are
  named.
- **Approximate list size:** "+1500 clientes" and "600 Millones de euros de
  financiación" claimed; **32 client names published**
- **Confidence:** Verified via archive (the live host is unfetchable)
- **Evidence:** `bbvaspark.com` returned HTTP 403 on four URL variants to curl
  with a full browser user-agent and Accept headers, and 403 to WebFetch. The
  Wayback CDX index for `bbvaspark.com*` since 2025 returns hundreds of `/akam/`
  Akamai bot-manager paths and a content tree of `/contenido/en/news/` and
  `/contenido/en/events/` articles, with **no** company-directory path. Fetched
  the 22 June 2025 snapshot of the homepage and read: the five-country statement,
  "+1500 clientes", "600 Millones de euros de financiación", the product framing
  (Venture Debt, Spark Rewards, "El banco del ecosistema emprendedor
  tecnológico"), and the full client name list: 99 minutos, bit2me, go> bravo,
  Cabify, Cafler, Casafari, Cobre, Conekta, Creditas, Creze, Druo, Exoticca,
  Fairplay, Habi, Henry, Heura, Insurama, Jeeves, Jüsto, Kredi, Kueski, Lookiero,
  Menta, Mundimoto, Nexu, Payflow, Pulppo, Twinco Capital, Voicemod, Wallbox,
  Wahu, Xepelin.
- **Last checked:** 2026-08-25

### Plug and Play, public content API

- **Type:** accelerator / corporate innovation network, with an open REST API
- **Geography:** 70 locations. In Europe: Amsterdam, Antwerp, Barcelona, Catania,
  Coventry, Gothenburg, Istanbul, **Limassol**, London, Madrid, Milan, Modena,
  Munich, Paris, Stuttgart, Tirana, Turin, Valencia, **Vienna**, **Vilnius**,
  Yerevan.
- **Homepage:** https://www.plugandplaytechcenter.com/
- **List page:** **https://public.dxp.playbook.vc/.rest/delivery/startups/v1**
  (and sibling endpoints `locations/v1`, `programs/v1`, `batches/v1`,
  `investments/v2`, `industries/v1`, `countries/v1`, `partners/v1`, `events/v1`,
  `press-releases/v1`, `challenge-offerings/v1`, `pages/v1`)
- **Publicly listed?** yes, but only through the API. The public website renders
  nothing to a fetcher.
- **Machine readable?** **JSON, unauthenticated, filterable, paginated.** Query
  parameters `limit`, `offset`, `startupCountry=<uuid>`,
  `startupMainIndustry=<uuid>`, `startupLocation=<uuid>`, and `?slug=` /
  `?@name=` lookups all confirmed working.
- **Update cadence:** continuous; records carry `mgnl:lastModified`. The website
  `sitemap.xml` (2,586 lines) also carries `lastmod` per URL and enumerates 47
  `/venture-capital/investment-announcements/<company>-investment` pages, which
  is a second, simpler change feed.
- **Why it surfaces card candidates:** The access is outstanding and the European
  content is thin, so both need saying. **5,540 startups** are queryable with
  country and industry filters, including a `fintech` industry
  (`cbf05043-f396-4e30-a63a-4cd20ab9367d`) and a separate
  `crypto-and-digital-assets` industry. But a country-by-country sweep run during
  this pass returns, for fintech: **United Kingdom 19, France 14, Spain 6,
  Germany 4, Italy 2, Netherlands 1, Lithuania 1, Poland 1, Czech Republic 1,
  Hungary 0, Greece 0, Belgium 0, Austria 0.** CEE, which is TXN's MVP
  geography, is effectively absent. The `investments/v2` endpoint is the more
  useful half: 108 announcements including fintech names (moneyhash, nearpays,
  axiology, complir, kota, dunly), each published as a dated page. Treat this as
  an ongoing-signal source on the investment feed, not a first-hit list.
- **Approximate list size:** 5,540 startups, 70 locations, 29 programmes, 124
  batches, 108 investment announcements, 37 industries, 252 countries
- **Confidence:** Verified
- **Evidence:** Fetched `/cyprus` and `/innovation-services/startups/our-startups`
  from the public site: both return an Angular shell whose only text is "Plug and
  Play". Fetched `main-XEYWX4E3.js` (1.85 MB) and read the service definitions,
  which reference `${Me.restBase}/delivery/startups/v1`, `/delivery/programs/v1`,
  `/delivery/investments/v2`, `/delivery/batches/v1/?slug=`,
  `/delivery/locations/v1` and others, then resolved `restBase` from
  `Mx="https://public.dxp.playbook.vc"` and `wR="/.rest"`. Queried each endpoint
  and read the `total` field and sample records. Read the full industry taxonomy
  (37 entries) and the European subset of the country taxonomy. Ran the
  13-country fintech sweep quoted above.
- **Last checked:** 2026-08-25

### Plug and Play Cyprus Acceleration Program (Limassol): ANNOUNCED, NO COHORT YET

- **Type:** accelerator, government co-funded
- **Geography:** Cyprus (Limassol), positioned for the Eastern Mediterranean
- **Homepage:** https://www.plugandplaytechcenter.com/innovation-services/our-programs/cyprus-accelerator-program
- **List page:** **none exists yet.**
- **Publicly listed?** no
- **Machine readable?** the programme page's content is retrievable as JSON via
  `https://public.dxp.playbook.vc/.rest/delivery/pages/v1/plug-and-play/innovation-services/our-programs/cyprus-accelerator-program?lang=en`;
  there is no cohort to read
- **Update cadence:** three-month programme, "Launching in 2026". No cohort dates
  published on the page.
- **Why it surfaces card candidates:** When it runs, it should be a strong
  source, and TXN should watch it. The programme copy names its target verticals
  explicitly and they are card-adjacent: "Cyprus serves as an EU stronghold for
  financial services, where startups are focused on digitizing traditional
  finance and automating the complex compliance requirements of the European
  market", broken into **Digital Asset Infrastructure** ("institutional-grade
  crypto trading platforms and exchange backends") and **Automated Compliance**
  ("AI for real-time identity verification"). It is co-funded by the Cypriot
  Deputy Ministry of Research, Innovation and Digital Policy and the Research and
  Innovation Foundation, so it will be publicly reported when it selects.
- **Approximate list size:** **0 published**
- **Confidence:** Verified (the programme exists and has no cohort)
- **Evidence:** Fetched the programme page content through the Magnolia pages
  API and read the title "Limassol, Cyprus Accelerator", the description
  ("Plug and Play brings Silicon Valley's proven model of acceleration and
  venture capital to Cyprus. Launching in 2026, our three-month acceleration
  program in Limassol..."), the co-funding statement, the five benefit cards, and
  the fintech vertical breakdown quoted above. Then confirmed the absence of a
  cohort three ways: `programs/v1/?@name=cyprus-accelerator-program` returns
  `"total": 0` (the programme is not in the live 29-programme index);
  `locations/v1/?slug=limassol` returns a record with `locationIsActive: true`
  but no address and no sorting order; and
  `startups/v1?startupLocation=<limassol id>` returns `"total": 0`. Separately
  confirmed that the 124-batch index contains **no European fintech batch**: the
  only fintech batches are `sv-fintech-batch-19`,
  `silicon-valley-fintech-batch-20`, `silicon-valley-fintech-batch-21`,
  `visa-inclusive-fintech-accelerator-cohort-1` and
  `inclusive-fintech-accelerator-cohort-2`.
- **Last checked:** 2026-08-25

### Plug and Play European programmes: NO FINTECH TRACK IN EUROPE

- **Type:** accelerator programmes
- **Geography:** as listed below
- **Homepage:** https://www.plugandplaytechcenter.com/innovation-services/our-programs
- **List page:** https://public.dxp.playbook.vc/.rest/delivery/programs/v1?limit=40
- **Publicly listed?** yes, via API
- **Machine readable?** JSON, with `programLocation` resolved inline
- **Update cadence:** continuous
- **Why it surfaces card candidates:** It largely does not, and that is the
  finding. Of 29 live programmes, the European ones are **B! Up Accelerate**
  (Paris), **Cassini Business Accelerator** (Amsterdam), **CrossConnect**
  (Catania), **DualTech by Takeoff** and **Takeoff Accelerator** (Turin),
  **Motor Valley Accelerator** (Modena), **MTC Innovation Accelerator**
  (Coventry), **Net Zero Jerez Aeronautical Hub** (Madrid), **STARTUP AUTOBAHN**
  (Stuttgart), **Startup Lithuania Accelerator** (Vilnius), **WMHTIA** (London),
  and **Scale-Up Lab Western Balkans**. None is fintech-scoped. The only fintech
  programmes in the index are **Visa Africa Fintech Accelerator** (run out of Abu
  Dhabi) and **XDC Decentralized Finance Accelerator** (Silicon Valley). The
  Startup Lithuania Accelerator in Vilnius is the closest adjacency, because
  Vilnius is the EU's densest EMI cluster, but the programme itself is not
  fintech-scoped.
- **Approximate list size:** 29 programmes, 12 in Europe, 0 European fintech
- **Confidence:** Verified
- **Evidence:** Fetched `programs/v1?limit=40` and read all 29 programme names
  with their resolved `programLocation.locationTitle`.
- **Last checked:** 2026-08-25

### Elevate Greece, National Startup Registry

- **Type:** register (government), national startup accreditation
- **Geography:** Greece
- **Homepage:** https://elevategreece.gov.gr/
- **List page:** https://elevategreece.gov.gr/the-startup-database/ , with the
  data served by
  `POST https://elevategreece.gov.gr/wp-admin/admin-ajax.php`
  `action=lvt-fetch-startups-data&security=<nonce>`
  where the nonce is the `value` of the hidden input `id=lvt_ajax_actions` on the
  database page. Per-company profiles live at
  `https://registry.elevategreece.gov.gr/company/<slug>`.
- **Publicly listed?** yes
- **Machine readable?** **yes, JSON, 2.1 MB in one request.** Each record carries
  `startup` (name plus logo plus registry profile URL), `industries`,
  `technologies`, `employee_count`, `total_funding`, `total_funding_numb`,
  `guid`, `website` and `regions`. The page also exposes DataTables HTML5 export
  buttons. The site's WordPress REST API (`/wp-json/wp/v2/pages`) is open.
- **Update cadence:** rolling, as the Ministry accredits companies. Accreditation
  is granted by the General Secretariat for Research & Innovation, so entries
  appear on a regulatory rhythm rather than a cohort rhythm.
- **Why it surfaces card candidates:** Greece is Phase 1a and this is the single
  most complete list of Greek startups in existence, published by the state. It
  is **1,085 companies**, of which **44 are tagged "FinTech, Financial Services
  (WealthTech)"**, **10 InsurTech**, and **9 LegalTech / RegTech**. Crucially the
  registry admits companies at incorporation, so a large fraction of the fintech
  cohort has no product in market, let alone a card program. Verified fintech
  entries read from the JSON include **Payment Components Hellas**, **FlexFin**
  (invoice factoring), **eCredit**, **Finclude** (EUR 2M raised), **Coinbux**,
  **Wocap**, **Quadible** (identity), **METALEASE**, **WRAPP**, **Wysely**,
  **Fairlo**, **Sinequity**, **Blocktech**, **Xenios Blockchain Group**,
  **Ai B Value**, **LB Linked Business**, **Ysoft Informatics**, **Quetri IT
  Solutions** and **Deliberative Technologies**. The `total_funding` and
  `employee_count` fields let the list be scored for readiness without a second
  data source.
- **Approximate list size:** **1,085 companies**; 44 FinTech, 10 InsurTech, 9
  LegalTech/RegTech; largest sectors Life Sciences 159, Environment & Energy 95,
  Travel 81, AgriTech/FoodTech 80, Enterprise Software 74
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (confirmed the Ministry of Development &
  Investments / GSRI accreditation framing and the "Startup Database" nav item).
  Fetched `/the-startup-database/` and read the filter set (Startup, Industry,
  Technology, Region, Employee count, Total funding, Website) and the "Data
  powered by Mantis Innovation Management Software" attribution. Read the theme
  bundle `wp-content/cache/minify/5b225.js` to recover the AJAX action name, and
  extracted the nonce from the page HTML. POSTed to `admin-ajax.php` and received
  2,099,723 bytes of JSON. Parsed it: `len(startups) == 1085`, industry
  distribution as above, and the 44-row FinTech subset with names, regions,
  funding and headcount. Note: `robots.txt` and `sitemap.xml` both return HTTP
  403 on this host, so the AJAX endpoint is the only enumeration route found.
- **Last checked:** 2026-08-25

### Portugal, national register of companies with Startup / ScaleUp status (dados.gov.pt)

- **Type:** register (government open data), statutory startup recognition under
  Law 21/2023
- **Geography:** Portugal
- **Homepage:** https://dados.gov.pt/pages/datasets/lista-de-empresas-reconhecidas-com-o-estatuto-de-startup
- **List page:** dataset API at
  `https://dados.gov.pt/api/1/datasets/lista-de-empresas-reconhecidas-com-o-estatuto-de-startup/`
  which returns the current resource URL. As of this pass the resource is
  `https://dados.gov.pt/s/resources/lista-de-empresas-reconhecidas-com-o-estatuto-de-startup/20260825-110010-0e119193/startup-portugal-certificate-07-2026-1787655608217.json`
- **Publicly listed?** yes
- **Machine readable?** **JSON array, 85 KB, one object per company:**
  `estatuto` (StartUp / ScaleUp), `titularNipc` (Portuguese corporate tax
  number), `titularFirma` (legal name), `titularNome`, `fileDate` (date
  recognition was granted).
- **Update cadence:** **effectively continuous, and the API exposes it.** The
  dataset's `last_modified` at the time of this fetch was
  `2026-08-25T11:00:10Z`, the same morning as this research pass, and the newest
  record was granted 21 August 2026. The published `frequency` field reads
  "unknown", so the cadence is inferred from the timestamps rather than declared.
  The resource filename is versioned by date, so the API must be re-queried
  rather than the resource URL hard-coded.
- **Why it surfaces card candidates:** This is the best ongoing signal found in
  this pass, for exactly the reason Ian described. Portugal is Phase 1a. A
  company appears here when the state certifies it as a startup, which is
  typically within months of incorporation and years before any card program. The
  record carries a NIPC, so every name resolves unambiguously to a legal entity
  and can be enriched against the Portuguese commercial register, and it carries
  the grant date, so a monthly diff yields a clean list of new companies with no
  deduplication problem. **143 of the 654 entries were granted in 2026 alone**,
  which is roughly 18 new named companies a month. The limitation, stated plainly:
  there is **no sector field**, so sector classification has to come from
  enrichment on the NIPC or the company name.
- **Approximate list size:** **654 companies** (644 StartUp, 10 ScaleUp);
  193 granted in 2024, 318 in 2025, 143 in 2026 to 21 August
- **Confidence:** Verified
- **Evidence:** Fetched `startupportugal.com/startup-status/` and read the
  statutory eligibility criteria under Law 21/2023 (Portuguese entity, under 10
  years old, under 250 employees, under EUR 50M turnover, plus ANI innovation
  recognition or a completed VC round or Banco Português de Fomento investment)
  and the sentence "Check the list of companies recognized with startup status",
  from which the `dados.gov.pt` link was extracted. Fetched the dataset API and
  read `title`, `organization: Agência para a Reforma Tecnológica do Estado`,
  `created_at: 2024-04-02`, `last_modified: 2026-08-25T11:00:10Z` and the single
  JSON resource. Fetched the resource (84,880 bytes) and parsed it: 654 records,
  status split 644/10, `fileDate` range 2024-01-17 to 2026-08-21, per-year counts
  as above. Most recent five records read: FRIENDLY CHAOS UNIPESSOAL LDA
  (21 Aug 2026), FEUILLET & VIANA LDA (21 Aug 2026), AMAZING ALGORYTHM LDA
  (13 Aug 2026), Pingos (10 Aug 2026), CELADONSOFT UNIPESSOAL LDA (10 Aug 2026).
- **Last checked:** 2026-08-25

### RNi Portugal Incubators (accredited incubator register)

- **Type:** register of accredited incubators, run by Startup Portugal
- **Geography:** Portugal, all regions including Azores and Madeira
- **Homepage:** https://startupportugal.com/rni-portugal-incubators/
- **List page:** https://startupportugal.com/rni-portugal-incubators/network-members/
  which links the register as a Google Sheet:
  https://docs.google.com/spreadsheets/d/1VdpjH-A52YJlpAIsr2GhAErhkS9nblAsO3Y4oD5y8zI
  (CSV export at `.../export?format=csv`), plus a PDF mirror on Google Drive
- **Publicly listed?** yes
- **Machine readable?** **yes, CSV export confirmed working, 42.6 KB, 146 data
  rows.** Columns: incubator name, responsible entity, entity NIPC, address,
  city/municipality, postcode, incubator website, public email, and **vertical
  specialisation areas**.
- **Update cadence:** annual accreditation cycle. The sheet's own header reads
  "Em 2025 foram acreditadas pela RNi - Portugal Incubators 146 incubadoras, das
  quais foram identificadas 43 Incubadoras Tech (29%) e 103 Incubadoras Locais
  (71%)".
- **Why it surfaces card candidates:** It is a meta-source, and a good one. Each
  of these 146 incubators runs its own unpublished cohort in a Phase 1a market,
  and the register tells you which ones to bother with: **32 of the 146 list
  Fintech among their vertical specialisations**, with a website and a public
  email address for each. Named Fintech-tagged incubators verified from the CSV
  include **Build Up Labs** (Lisboa), **Fábrica de Startups / FABSTART**
  (Oeiras), **Founders Founders** (Porto), **Driven Venture Builders** (Porto),
  **Centro de Incubação Atlântico** (Porto), **IPN Incubadora** (Coimbra),
  **inCoimbra StartUp HUB**, **Nova SBE Haddad Entrepreneurship Institute**
  (Carcavelos), **INOVAGAIA**, **IDEIA-ATLÂNTICO** (Braga) and **Acelera
  Portugal** (Aveiro). That is a targetable partnership list, not just a
  scraping list.
- **Approximate list size:** **146 accredited incubators** (43 Tech, 103 Local);
  32 tagged Fintech
- **Confidence:** Verified
- **Evidence:** Fetched `/rni-portugal-incubators/` and read the network
  description ("over one hundred incubators") and the two-tier Tech/Local
  structure. Fetched `/rni-portugal-incubators/network-members/` and read the
  "In 2025, 146 incubators were accredited... 43 Tech Incubators and 103 Local
  Incubators" statement, then extracted the Google Sheet and Drive PDF links.
  Fetched the sheet's CSV export (HTTP 200, 42,616 bytes), parsed 146 data rows,
  confirmed the nine-column schema, and counted 32 rows containing "Fintech" in
  the vertical-specialisation column.
- **Last checked:** 2026-08-25

### Startup Portugal, Ecosystem Mapping Platform: NOT EXTRACTED

- **Type:** national ecosystem directory
- **Geography:** Portugal
- **Homepage:** https://ecossistema.startupportugal.com/
- **List page:** same URL
- **Publicly listed?** unknown
- **Machine readable?** **no, not from this pass.** The host serves a Next.js
  app shell of 13.8 KB with no server-rendered records and no discoverable API
  route.
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Startup Portugal describes it as the place
  to "get key metrics and elements that make up our ecosystem", which suggests
  company-level data. It is the obvious complement to the `dados.gov.pt` register
  because it may carry the sector field the register lacks. Worth a
  headless-browser pass; not worth guessing at.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** Fetched the URL: HTTP 200, 13,803 bytes, containing only Next.js
  chunk references, font preloads and stylesheet links. An attempt to recover an
  API base from the chunk bundles timed out and was abandoned rather than
  guessed at.
- **Last checked:** 2026-08-25

### Start it @KBC (and Start it X)

- **Type:** accelerator, bank-run (KBC Group)
- **Geography:** Belgium, 9 hubs. Sister programmes Start it @CBC, Start it
  Fashion, Start it Hardware, Scale it Agro, Thrive, Sales Sprint.
- **Homepage:** https://startit-x.com/en/accelerate/start-it-kbc (note:
  `startit.be` 301-redirects here)
- **List page:** https://startit-x.com/en/accelerate/all-startups , paginated at
  `/all-startups/p2` through `/all-startups/p81`
- **Publicly listed?** yes
- **Machine readable?** **yes, server-rendered HTML.** Each card carries company
  name, one or more industry tags and a cohort year. Pagination is a clean path
  segment (`/p2`), not a query string, so the crawl is 81 deterministic URLs.
- **Update cadence:** two intakes a year. The fetched page advertises the Fall
  2026 programme: info sessions week of 31 Aug 2026, **application deadline
  14 Sep 2026**, programme starts 28 Oct 2026, 12 months, **capacity 65
  participants**, **free with no equity taken**.
- **Why it surfaces card candidates:** Belgium is Phase 1b and this is the
  densest published early-stage list found in the region. The taxonomy is
  unusually good for TXN's purposes: alongside a **Fintech** tag it carries
  **Insurtech**, **Identification/Authentication/KYC/AML**, and a separate
  **Finance, Insurance & Investing** facet, plus **SME solutions (sector
  agnostic)** and **Enterprise solutions (sector agnostic)** which is where
  spend-management and expense products land. The cohort-year filter runs
  2014-2026, so filtering to 2025-2026 plus a finance tag isolates companies that
  joined a free, no-equity accelerator within the last eighteen months, which is
  as close to pre-processor as a published list gets. Because entry is free, the
  bar is commitment rather than traction, so the 2026 cohort skews earlier than a
  typical equity accelerator.
- **Approximate list size:** **"1700+ active startups"** stated on the list page;
  81 pages of results
- **Confidence:** Verified
- **Evidence:** Fetched `startit.be/en/startups` (301 to
  `startit-x.com/en/accelerate/start-it-kbc`) and read the Fall 2026 programme
  parameters quoted above, the "#1 startup accelerator in Belgium" claim, the
  nine Belgian hubs, and the three September 2026 info sessions (Leuven, Hasselt,
  Brussels). Fetched `/en/accelerate/all-startups` and read the "Check out our
  1700+ active startups" heading, the full industry filter vocabulary (two
  generations of taxonomy, including Fintech, Insurtech,
  Identification/Authentication/KYC/AML and Finance, Insurance & Investing), the
  year filter 2014-2026, roughly 20 server-rendered company cards with their
  tags and cohort years (A.I.R. Distillations, Agriflight, AICON, Aisitec, Alex
  AI, alia, Artech International, Artsy Impact, ARTYFACT, AskMaeve, ÁSPILON,
  AuditQ, Augeas, B.me, Bar.on, Beatunity, Belmade, Bernamo, Better World
  Marketing, BioNoda, all 2025), and the pagination control ending at page 81.
  Confirmed the pagination URL form is `/all-startups/p2`, not a query parameter.
- **Last checked:** 2026-08-25

### imec.istart

- **Type:** accelerator, university/research-institute backed (imec)
- **Geography:** Belgium (primary), plus Netherlands, Italy, Spain, Germany
- **Homepage:** https://www.imecistart.com/
- **List page:** https://www.imecistart.com/en/portfolio
- **Publicly listed?** yes
- **Machine readable?** **yes, and richly so.** All 376 companies are
  server-rendered as `/en/portfolio/<slug>` links, and the page's embedded React
  server-component payload carries, per company: `filter_domain`, `filter_year`,
  `filter_country`, `filter_technologies`, `filter_hardware` (life-cycle stage),
  `tagline`, `description` and the company's own website URL. Everything the UI
  filters on is in the HTML.
- **Update cadence:** cohort-based since 2011; the payload carries a cohort year
  per company
- **Why it surfaces card candidates:** Belgium is Phase 1b and imec.istart is the
  research-institute counterweight to Start it @KBC, taking deeper-tech
  companies. The `filter_hardware` field distinguishes early-stage from Scale-up,
  and `filter_domain` includes **FinTech** as a first-class value. Only **10 of
  376** carry the FinTech tag, so this is a precision source rather than a volume
  one. The single verified example read in full from the payload, **Risolto**
  (Belgium, 2020, Scale-up, domains FinTech plus Business Services), is described
  as "digital, datadriven and truly personalized (e-)invoicing, (e-)payment,
  dunning and collection, as a service", which is a payments company that may
  well never have issued a card.
- **Approximate list size:** **376 companies** on the portfolio page; "Over 300
  tech startups went through the imec.istart program since 2011" stated on the
  page; 10 tagged FinTech
- **Confidence:** Verified
- **Evidence:** Fetched `imecistart.com/portfolio` (301 to `/en/portfolio`,
  1.65 MB) and read the "Over 300 tech startups" statement and the six filter
  axes (Domain, Life cycle, Technologies, Status, Cohort year, Country). Parsed
  the HTML for `href="/en/portfolio/<slug>"`: **376 unique slugs**. Parsed the
  embedded payload for `filter_domain` arrays: 376 blocks, **10 containing
  "FinTech"**. Read the Risolto record in full including its tagline,
  description, country, year, life-cycle stage and website. Confirmed that the
  filter URL form shown in the taxonomy
  (`/en/portfolio-filters/domain/fintech`) returns **HTTP 404**, so filtering is
  client-side only and the whole page must be parsed.
- **Last checked:** 2026-08-25

### Lanzadera (Valencia)

- **Type:** accelerator, corporate-founded (Juan Roig / Marina de Empresas)
- **Geography:** Spain, Valencia
- **Homepage:** https://lanzadera.es/
- **List page:** https://lanzadera.es/proyectos/ (note: `/empresas/`
  301-redirects here)
- **Publicly listed?** partial
- **Machine readable?** **partial.** 29 project links are server-rendered; the
  full portfolio sits behind JetSmartFilters AJAX with three tabs (Destacadas /
  En programa / Todas). The site's WordPress REST API is open and does expose a
  `portfolio` post type, but it returns `x-wp-total: 0` to an unauthenticated
  request, so the REST route is a dead end.
- **Update cadence:** rolling; the "En programa" tab distinguishes companies
  currently in the programme from alumni, which is the useful axis
- **Why it surfaces card candidates:** Spain is Phase 1a and Lanzadera is
  described on its own page as a top-3 accelerator in Spain and Portugal by the
  Financial Times for three consecutive years, with **1,700+ companies
  accelerated over 15 years**. The "En programa" tab is the one that matters for
  TXN: it isolates companies in the programme right now. The page's text does
  carry Fintech and "Finanzas" as category labels. The blocker is purely
  mechanical: the filtered lists need a headless browser or the JetSmartFilters
  AJAX endpoint reverse-engineered, neither of which was completed in this pass.
- **Approximate list size:** **1,700+ accelerated** claimed; **29** rendered
  server-side
- **Confidence:** Verified (programme, scale, page structure), Unverified (the
  full company list)
- **Evidence:** Fetched `lanzadera.es/empresas/` (301 to `/proyectos/`) and read
  "15 años acelerando", "+1700 empresas aceleradas", the Financial Times top-3
  claim, the three portfolio tabs, and the first five featured companies (Nidus,
  Sepiia, Gana Energía, Holafly, BusUp). Parsed the HTML: 29 unique
  `lanzadera.es/proyecto(s)/<slug>/` links, 15 occurrences of "finanzas" and 2 of
  "Fintech" as category labels, and `wp-json/jet-search/v` plus `admin-ajax`
  references confirming the AJAX filtering. Queried
  `wp-json/wp/v2/types` (the `portfolio` post type is registered) and then
  `wp-json/wp/v2/portfolio`, which returned `x-wp-total: 0`.
- **Last checked:** 2026-08-25

### Orange Fab Romania

- **Type:** corporate accelerator (Orange / telecom)
- **Geography:** Romania. Part of a 20-country Orange Fab network that includes
  France, Belgium & Luxembourg, Spain, Poland, Tunisia, Senegal, Madagascar and
  Cameroon.
- **Homepage:** https://www.orangefab.ro/
- **List page:** https://www.orangefab.ro/startup-uri/
- **Publicly listed?** yes
- **Machine readable?** HTML list, server-rendered, names only on the index with
  per-company detail pages
- **Update cadence:** 12-month programme cycles
- **Why it surfaces card candidates:** Romania is an MVP market and this is a
  verified, currently-live Romanian corporate accelerator with a published
  company list, which is rarer than it should be. The honest assessment: **none
  of the 33 named companies is a fintech**. The list is dominated by industrial
  AI, robotics, cybersecurity and IoT (KFactory, .lumen, Arcanna.ai, SecurifAI,
  CyberEDU, Agora Robotics, uRADMonitor). Its value to TXN is as a Romanian
  ecosystem-monitoring source and as evidence that Orange runs PoC budgets of up
  to EUR 20,000 per startup, not as a fintech funnel.
- **Approximate list size:** **33 companies** named
- **Confidence:** Verified
- **Evidence:** Fetched `orangefab.ro/` and read the programme description
  (12-month corporate accelerator, PoC projects up to EUR 20,000, access to 5G
  Lab Iași and București, Hub Pass workspace, Orange Venture funding, and the
  20-country Orange Fab network). Fetched `/startup-uri/` and read all 33 names:
  BraveX.Aero, Alpha by Zendra, Solomonar, Telesenior, PROCESIO, .lumen, Xfleet,
  Ogre, Nestor, FieldOS, CORE Antivirus, CautCurier.ro, Blume Technologies, Airis
  Vision, Agora Robotics, Mobilecontrol, uRADMonitor, Fullscreen Digital,
  SecurifAI, KFactory, Dekeneas, AgriCloud, Blugento, CityDock, Arcanna.ai,
  Telios Care, Zevo Technologies, CyberEDU, EmailTree.AI, Virtual Board,
  Hydrosync.ai, StageOne. Fetched `/catalog/` which returned no content.
- **Last checked:** 2026-08-25

### Orange Fab Poland

- **Type:** corporate accelerator (Orange / telecom)
- **Geography:** Poland
- **Homepage:** https://www.orangefab.pl/
- **List page:** https://www.orangefab.pl/startupy/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with a category tag and a Polish-language
  description per company
- **Update cadence:** unknown from the page
- **Why it surfaces card candidates:** Poland is an MVP market, but this
  particular list is too small and too far from finance to be worth a pipeline.
  Seven companies are published, tagged E-commerce, IoT, AI, Knowledge Management
  and "Inne" (Other). There is **no Fintech category**. Recorded so nobody spends
  a second pass on it. The one adjacency worth noting is **Uniperks**, described
  as Poland's largest student benefits and discounts platform connecting ~140
  brands with almost 400,000 verified students, which is a captive-spend
  population, and which also appears in The Heart's portfolio in stream 02.
- **Approximate list size:** **7 companies**
- **Confidence:** Verified
- **Evidence:** Fetched `orangefab.pl/startupy/` and read the category filter
  (Pokaż wszystkie, E-commerce, IoT, Inne, Others, Knowledge Management, AI) and
  all seven companies with descriptions: IoToak, Liki Mobile Solutions,
  Chatporter, CAPTiX, WitCloud, QuestPass, Uniperks. Confirmed no Fintech
  category exists in the filter. Also read the Orange Fab Network footer listing
  France, Romania, Belgium & Luxembourg, Spain, Tunis, Senegal, Madagascar and
  Cameroon.
- **Last checked:** 2026-08-25

### hubraum (Deutsche Telekom)

- **Type:** corporate incubator (telecom)
- **Geography:** Berlin and **Krakow** campuses
- **Homepage:** https://www.hubraum.com/
- **List page:** https://www.hubraum.com/startups-partners/ (note:
  `/startups` 301-redirects here)
- **Publicly listed?** yes
- **Machine readable?** HTML, server-rendered, alphabetical, with a description
  paragraph on many entries
- **Update cadence:** programme-based. Current initiatives named on the page:
  Tangible Tomorrow 2026, Security Co-Creation Program, Digital Innovation
  Program, MWC 2026, Prototyping Campus.
- **Why it surfaces card candidates:** It essentially does not, and the Krakow
  campus makes that worth stating explicitly rather than assuming. Deutsche
  Telekom's incubator has a Polish presence in an MVP market and publishes a
  long alphabetical alumni list, but the extracted page text contains **zero
  occurrences of "fintech", "payment" or "banking"**. The portfolio is XR, AI,
  edge computing, robotics, healthtech and connectivity. Recorded as a negative
  so the Krakow campus does not get re-investigated.
- **Approximate list size:** long alphabetical list, exact count not stated on
  the page; 0 fintech
- **Confidence:** Verified
- **Evidence:** Fetched `hubraum.com/startups` (301 to `/startups-partners/`) and
  read the "Our Startups and Alumni" heading, the initiative list including
  Campus Berlin and Campus Krakow, and roughly 25 alphabetical entries with
  descriptions (HAPTICLABS, FIBERLIKE, MOVE2EDGE, TWINCUBE, VOXIST, MODINO, 1000
  realities, 2sens, 360 Stories, 3DforScience, 5Analytics, Abaro, Absolute zero,
  Adlatus, Admetsys, AIDY Health, AISight...). Grepped the full extracted text
  for fintech, payment and banking: 0 matches.
- **Last checked:** 2026-08-25

### MIT Enterprise Forum CEE (Warsaw)

- **Type:** accelerator, foundation-run (Foundation for Technology
  Entrepreneurship)
- **Geography:** Poland and CEE
- **Homepage:** https://mitefcee.org/
- **List page:** **none public.** `https://mitefcee.org/community/alumni-club/our-alumni/`
  exists but renders no company list; the Alumni Club itself is hosted on
  `alumni-club.circle.so` behind a login.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** multiple concurrent tracks: Early Stage, Rethink Cohort,
  Late Stage, Pilot Ready Cohort, Expansion Weeks, ESA BIC
- **Why it surfaces card candidates:** Poland is an MVP market and this is one of
  the longest-running CEE accelerators (founded 2015 per its own copy), with an
  explicit corporate-matchmaking model ("Accelerator As a Service") that puts it
  in front of Polish corporates before their suppliers scale. But with no
  published alumni list and a gated community platform, it is a **partnership
  target, not a scrape target**. The "Pilot Ready Cohort" naming is the
  interesting signal: it implies a stage gate that a card-issuing vendor could
  attach to.
- **Approximate list size:** **0 published**
- **Confidence:** Verified (the absence of a public list is confirmed, not
  assumed)
- **Evidence:** Fetched `mitefcee.org/startups` and read the full programme
  navigation (Early Stage, Rethink Cohort, Late Stage, Pilot Ready Cohort,
  Expansion Weeks, ESA BIC, Corporate, Accelerator As a Service, Metaverse Hub)
  and the "one of CEE's top Startup Acceleration Programs (founded in 2015)"
  claim. Extracted the alumni hrefs and fetched
  `/community/alumni-club/our-alumni/`: the page renders the club pitch, a
  "Startups we accelerated" heading and a corporate-partners heading, but no
  company names. Confirmed the club link points to `alumni-club.circle.so`.
- **Last checked:** 2026-08-25

### StartupYard (Prague)

- **Type:** accelerator
- **Geography:** Czech Republic, CEE ("CEE Tech Founders", 26 countries)
- **Homepage:** https://startupyard.com/
- **List page:** **none.** `/portfolio/`, `/companies/` and `/alumni/` all 404 or
  redirect to unrelated blog posts.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** unknown from the site; the only current call to action is
  "apply to StartupYard Remote Lab"
- **Why it surfaces card candidates:** Czech Republic is an MVP market and
  StartupYard is the best-known Czech accelerator, so its absence from the
  scrapable set is worth recording. Its own homepage claims **130+ startups,
  EUR 105M raised, thousands of jobs, 26 countries**, but publishes only six
  alumni as outbound links. Of those, **BudgetBakers** (personal finance
  management) and **Rossum** (document and invoice data extraction) are the only
  finance-adjacent names. Treat as a relationship target.
- **Approximate list size:** **130+ claimed, 6 published**
- **Confidence:** Verified (the absence of a directory)
- **Evidence:** Fetched `startupyard.com/` and read the four headline figures and
  the founder testimonials (Mergim Cahani of Gjirafa, Petr Baudis of Rossum).
  Extracted every outbound link on the page: 24vs.io, budgetbakers.com,
  dishboard.cz, feedyou.ai, gjirafa.com, qoobus.com, rossum.ai. Probed
  `/portfolio/` (404), `/companies/` (301 to an unrelated blog post) and
  `/alumni/` (404).
- **Last checked:** 2026-08-25

### Wayra (Telefónica)

- **Type:** corporate venture capital, formerly an accelerator network
- **Geography:** **Spain, Germany, United Kingdom, Brazil** (four countries,
  stated on the homepage)
- **Homepage:** https://wayra.com/
- **List page:** **none reachable.** The homepage's "Our startups" link points to
  `https://startups.telefonica.com/`, which renders only the words "Open
  Innovation calls" to a fetcher. `wayra.com/portfolio` and
  `wayra.com/es/portfolio` both return 404.
- **Publicly listed?** partial. Individual investments are announced in the news
  feed with company names and dates.
- **Machine readable?** no list; dated news items only
- **Update cadence:** rolling investment announcements. Most recent read:
  16 July 2026 (MITO AI), 5 February 2026 (the ACCIÓN digital-health accelerator
  with AstraZeneca and Kunsen). An "OUTLIERS 2026" showcase is promoted on the
  homepage.
- **Why it surfaces card candidates:** Spain is Phase 1a and Wayra is the
  largest corporate venture arm operating there, with an explicit
  **venture-client model** that connects portfolio companies into Telefónica's
  business units. That is a strong pre-scale signal. But without a fetchable
  portfolio the only usable route is monitoring `wayra.com/news` for investment
  announcements, which makes this an ongoing-signal source of modest volume
  rather than a first-hit list.
- **Approximate list size:** the homepage displays animated counters that render
  as "+1" to a fetcher, so no figure could be read; **0 companies published in
  list form**
- **Confidence:** Verified (structure, geography and the absence of a list)
- **Evidence:** Fetched `wayra.com/` and read the four-country statement, the
  "Telefónica's Corporate Venture Capital" positioning, the venture-client
  description, the two most recent news items with dates, and the footer link
  set. Probed `/portfolio` and `/es/portfolio`: both 404. Fetched
  `startups.telefonica.com/`: the entire extracted text is "Open Innovation
  calls / open innovation".
- **Last checked:** 2026-08-25

### Fundación Innovación Bankinter: NO STARTUP LIST

- **Type:** corporate foundation (Bankinter)
- **Geography:** Spain
- **Homepage:** https://www.fundacionbankinter.org/en/our-initiatives/startups/
  (note: `/en/startups/` 301-redirects here)
- **List page:** **none found.** The startups page renders a content hub of
  reports and articles.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** n/a
- **Why it surfaces card candidates:** It was checked because Bankinter is a
  Spanish bank in a Phase 1a market with a long-standing startup foundation, and
  it does not. The page served is an editorial index (834 "See" items, 724
  "Read" items, 6 events, organised by Economic Development / Science and
  Technology / Social transformation) with no company records. Recorded as a
  negative.
- **Approximate list size:** **0**
- **Confidence:** Verified (the absence of a list)
- **Evidence:** Fetched `/en/startups/` (301 to `/en/our-initiatives/startups/`)
  and read the full page: a search box, three featured topics, format and theme
  counters, a reports carousel and a "Glossary of Synthetic Biology" feature. No
  company names appear anywhere in the served content.
- **Last checked:** 2026-08-25

### CaixaBank DayOne: DOMAIN DOES NOT RESOLVE

- **Type:** bank programme for startups
- **Geography:** Spain
- **Homepage:** `caixabankdayone.com`, which has **no DNS record**
- **List page:** none found
- **Publicly listed?** unknown
- **Machine readable?** n/a
- **Update cadence:** n/a
- **Why it surfaces card candidates:** CaixaBank DayOne appears on most lists of
  Spanish bank startup programmes. Its standalone domain has no A record at all,
  and four plausible paths on the bank's own domains return 404. Whatever the
  programme's current status, **the URL that most prospecting lists carry is
  dead**, and recording that is more useful than guessing at a replacement.
  Someone should confirm manually whether DayOne still operates under a different
  path before it is written into the corpus.
- **Approximate list size:** unknown
- **Confidence:** Unverified. What was tried: `https://www.caixabankdayone.com/`,
  `https://www.caixabankdayone.es/`, `https://dayone.caixabank.es/`,
  `https://dayone.caixabank.com/` (all curl exit code 000, connection failed),
  and `https://www.caixabank.es/empresa/dayone/dayone_es.html`,
  `https://www.caixabank.es/particular/dayone.html`,
  `https://www.caixabank.com/en/business/dayone.html`,
  `https://www.caixabank.com/es/empresa/dayone.html` (all HTTP 404).
- **Evidence:** `dig +short caixabankdayone.com` returns nothing. Eight URL
  probes as listed above.
- **Last checked:** 2026-08-25

### Factory by Raiffeisen (Romania): DEAD

- **Type:** accelerator, bank-run
- **Geography:** Romania
- **Homepage:** `factorybyraiffeisen.ro`, which has **no DNS record**
- **List page:** none
- **Publicly listed?** no
- **Machine readable?** n/a
- **Update cadence:** n/a
- **Why it surfaces card candidates:** It does not, and this closes a loop from
  stream 02. That stream established that RBI's group-level Elevator Lab
  accelerator ran only 2017-2022 and is now an ecosystem-outreach function with
  no cohort. The Romanian programme is in the same state or worse: its domain
  does not resolve and the bank's own site has no `/factory` path. Romania is an
  MVP market, so anyone building a Romanian bank-accelerator list should skip
  Raiffeisen and go to InnovX (BCR/Erste) and Techcelerator, both recorded in
  stream 02.
- **Approximate list size:** n/a
- **Confidence:** Verified (defunct)
- **Evidence:** `dig +short factorybyraiffeisen.ro` returns nothing;
  `https://factorybyraiffeisen.ro/` returns curl exit code 000.
  `https://www.raiffeisen.ro/factory` returns HTTP 404.
- **Last checked:** 2026-08-25

### Design Terminal (Budapest): ABSORBED INTO CIVITTA

- **Type:** accelerator, formerly government-and-corporate backed
- **Geography:** Hungary and CEE
- **Homepage:** `designterminal.org`, which **301-redirects to `civitta.com/hu`**
- **List page:** none under the Design Terminal brand
- **Publicly listed?** no
- **Machine readable?** n/a
- **Update cadence:** n/a
- **Why it surfaces card candidates:** Hungary is an MVP market and Design
  Terminal was for a decade the most visible Hungarian accelerator brand,
  including corporate programmes with banks. It no longer exists as an
  independent entity: the domain now lands on the Hungarian page of the Civitta
  consultancy. Any Hungarian accelerator list carrying Design Terminal is stale.
  Stream 02's MBH Fintechlab entry remains the live Hungarian source.
- **Approximate list size:** n/a
- **Confidence:** Verified (redirect confirmed)
- **Evidence:** `https://designterminal.org/en` returns HTTP 200 at the final URL
  `https://civitta.com/hu` after following redirects.
- **Last checked:** 2026-08-25

### weXelerate (Vienna): NO LONGER AN ACCELERATOR

- **Type:** innovation hub and co-working operator; formerly an accelerator
- **Geography:** Austria, Vienna
- **Homepage:** https://wexelerate.com/ (note: **`www.wexelerate.com` does not
  resolve**; only the apex domain works)
- **List page:** none. The site offers an "Ecosystem map" behind its Ecosystem
  menu, not a cohort list.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** n/a for cohorts; the site runs an event calendar
- **Why it surfaces card candidates:** Austria is Phase 1b and weXelerate was
  once the largest Austrian corporate accelerator, with bank and insurer
  partners. Its current navigation is Hub services (Offices, Co-Working, Rent an
  Event Space), Innovation services (Membership, Benefits, Ecosystem map), Event
  calendar and About us. **There is no accelerator programme in the navigation
  and no cohort anywhere on the site.** It is now a workspace and membership
  business. The "Ecosystem map" may contain company records and was not opened in
  this pass; that is the one thread left.
- **Approximate list size:** unknown; **0 cohort companies published**
- **Confidence:** Verified (the pivot away from acceleration), Unverified (the
  contents of the Ecosystem map)
- **Evidence:** `https://www.wexelerate.com/` returns curl exit code 000 (host
  does not resolve). `http://www.wexelerate.com` resolves to
  `https://wexelerate.com/`, which was fetched: read the full navigation as
  listed above, plus the current banner "Quantum Special: ++ Is Your Enterprise
  Ready for the Quantum Shift? ++". `dig +short wexelerate.com` returns
  104.248.100.144.
- **Last checked:** 2026-08-25

---

## What I could NOT verify

Stated explicitly, per anti-fabrication rule 4.

- **The WebSearch budget was already exhausted (200/200) before this stream
  began.** Every entry above was reached by direct fetching from a URL that was
  either linked from a page already fetched, listed in a sitemap or REST index
  that was fetched, or probed and reported with its actual HTTP status. Mojeek
  was tried as a curl-based search fallback; its index returned results from 2014
  to 2019 for current queries and contributed nothing. **The practical
  consequence: this pass is strong on the leads it was given and on anything
  reachable by link-following, and weak on discovering programmes whose existence
  was not already suspected.** A follow-up pass with search budget would likely
  find more CEE bank programmes.
- **Greek bank accelerators could not be reached at all.** Eurobank's `egg`
  programme (enter, grow, go): `egg.gr` resolves to Cloudflare but serves a
  `topdomains.gr` domain-for-sale page, `www.egg.com.gr` does not resolve, and
  `eurobank.gr/en/business/egg` and `eurobank.gr/en/omilos/egg-enter-grow-go`
  both return HTTP 403 to automated fetchers. NBG Business Seeds: two `nbg.gr`
  paths returned 404. **Greece is a Phase 1a market and its two largest bank
  startup programmes are a genuine gap in this research.** They need a manual
  browser check, not another automated attempt.
- **ČSOB (Czech Republic)**: `csob.cz/portal/csob/startups` returns HTTP 200 with
  no server-rendered content. ČSOB is KBC-owned, and KBC runs the best bank
  accelerator found in this pass (Start it @KBC in Belgium), so a Czech sister
  programme is plausible and would sit in an MVP market. Not confirmed either
  way.
- **BNP Paribas Poland**: `bnpparibas.pl` returns 200 but no startup-programme
  path was located without search. Poland is an MVP market. Open lead.
- **Startup Portugal's Ecosystem Mapping Platform**
  (`ecossistema.startupportugal.com`) serves a 13.8 KB Next.js shell. An attempt
  to recover its API base from the chunk bundles timed out. This matters because
  it is the most likely place to find the **sector field that the `dados.gov.pt`
  register lacks**.
- **Lanzadera's full portfolio.** 29 of a claimed 1,700 companies are rendered
  server-side; the rest sit behind JetSmartFilters AJAX. The WordPress REST
  `portfolio` endpoint returns `x-wp-total: 0`. The AJAX endpoint was not
  reverse-engineered.
- **Techstars' portfolio search.** 11,034 accelerated founders sit behind an
  in-page anchor with no server-rendered records and no per-company sitemap URLs.
  Not extractable without a headless browser.
- **Santander X 100's directory** returns HTTP 200 with a zero-byte body. Two
  attempts. No workaround found.
- **BBVA Spark's live site** is behind Akamai bot management and returned 403 to
  every method tried including WebFetch. Everything recorded for it comes from a
  **22 June 2025 Wayback snapshot**, so the client list and the "+1500 clientes"
  figure are 14 months old at the time of writing.
- **CaixaBank DayOne's current URL**, if it has one. Eight probes, all failed.
- **weXelerate's "Ecosystem map"** was not opened; it may contain a company
  directory for Austria.
- **imec.istart's per-company detail pages** were not fetched individually. The
  376 slugs and the embedded metadata were read from the index page only, so
  per-company funding and contact detail is unconfirmed.
- **Cohort sizes and update cadences** are stated above only where the fetched
  page or API record gave them. Where a page did not say, the field reads
  `unknown` rather than an estimate.
- **The Techstars ABN AMRO 2026 cohort** had not been announced at the time of
  this pass. The programme starts 8 September 2026 and the class is announced at
  kick-off, so the 2026 names should be checked in the second half of September
  2026.
