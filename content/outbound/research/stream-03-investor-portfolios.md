---
description: "Stream 03 raw research: 54 investor portfolio pages assessed as a new-deal feed rather than a company list"
---

> **Section:** [[research]]
> **Validation:** [[validation-03-investor-portfolios]]
> **Status:** raw research output, recorded verbatim. Read the validation report alongside it: several counts in this file were corrected.

# Stream 03: Investor portfolio pages as a discovery pipeline

Owner: investor-portfolio research stream. Research pass date: 2026-08-25.

## Summary

The thesis holds. A fund's portfolio page is frequently the earliest public record
of an investment, and several of the pages below carry a per-company **investment
date** in the markup, which converts a portfolio page from a static list into a
diffable feed. Underline Ventures (Romania) published a company dated **24 August
2026**, one day before this research pass. That is the signal Ian is describing.

I fetched 60+ URLs across CEE early-stage funds, European fintech-thesis VCs, bank
and insurer corporate venture arms, private equity firms with payments exposure,
and angel syndicates. Every `Verified` entry below was retrieved during this pass,
mostly with `curl` plus HTML-to-text extraction so that "static HTML vs JS-rendered"
is an observation about the actual bytes returned, not an inference.

### The seven best pages to scrape, in order

Ranked on: company names present in the served HTML, plus a per-company date or
year, plus a fintech/payments filter.

1. **Motive Partners.** `Investment date` to the month per company, plus a
   `Banking & Payments` subsector. Names in static HTML. PE/growth, so these are
   PE-owned businesses, exactly the "PE-owned business adding cards" pattern.
2. **Seedcamp.** Explicit `Company Name / Year of Investment / Description` table
   in static HTML, `Fintech` filter, 550+ companies, entries already dated 2026.
3. **Market One Capital (moc.vc).** Per-company `Year` and `Sector` including
   `FinTech`, plus HQ country. 2026 entries present. Small, clean, parseable.
4. **Underline Ventures.** Per-company `Date of partnership` to the exact day.
   Small portfolio but the freshest date stamps found anywhere in this pass.
5. **Inovo VC.** Per-company country, sector and investment year in static HTML,
   with three fintechs visible (Handwave 2025, Fiat Republic 2023, Symmetrical 2021).
6. **Movens Capital.** Per-company `Entry date` by quarter (e.g. `Q3 2025`).
7. **Illuminate Financial.** Has a literal `Payments & CFO Stack` theme filter.
   No dates, but the sector segmentation is the most TXN-relevant of any fund page.

Honourable mention for CEE coverage: **Portfolion** (OTP Bank's arm, 46 companies,
Hungary/CEE) and **Elevator Ventures** (Raiffeisen Bank International's arm,
explicitly CEE fintech). Both are bank corporate venture arms in TXN's MVP markets
and both publish readable static lists.

### The most useful negative finding

A large share of fund portfolio pages are **client-side rendered React/Vue/Webflow
shells that serve almost no HTML**. Confirmed empty or near-empty responses:
Presto Ventures (114 bytes), Middlegame Ventures (114 bytes), Cogito Capital
(114 bytes), SMOK Ventures (unrendered Vue `{{item.title}}` placeholders in the
served markup), LAUNCHub (4.5 KB shell, 81 characters of text), Enterprise
Investors (346 characters), MCI Capital (385 characters), Lead Ventures
(1.1 KB of text, zero companies), Antler and Angel Invest (descriptions render,
company names do not, because names live in logo images).

Operationally this means a headless-browser tier is required for roughly a third
of the target list. Budget for it. Do not assume `requests` plus BeautifulSoup
covers the corpus.

### What I could NOT verify

Recorded honestly, per the anti-fabrication rules:

- **ING Ventures wind-down.** A Global Venturing headline states ING's ventures arm
  halted new investments. The article returned **HTTP 403** to both `curl` and
  WebFetch, so I could not read the body. Status, date and portfolio treatment are
  all unconfirmed. Marked `Unverified` below.
- **PFR Ventures (Poland, state fund-of-funds).** `pfrventures.pl/en/portfolio.html`
  returned **HTTP 403** behind Cloudflare (Ray ID logged). This is potentially the
  single highest-leverage CEE meta-source, because it lists the VC funds the Polish
  state capitalises, and each of those funds has its own portfolio page. Needs a
  browser session with cookies. Not verified.
- **Genesis Capital (Czech PE)** and **Depo Ventures (Czech)**. `genesiscapital.cz`,
  `genesiscapital.eu` and `depo.ventures` all failed to resolve or connect from this
  environment. Domains not confirmed. Not verified.
- **ABN AMRO Ventures.** No portfolio list found on `abnamro.com`; the innovation
  page I fetched contains no company links. Reporting says the fund is now managed
  by Motive Ventures. Not verified.
- **neosfer (Commerzbank).** `neosfer.de` returned no extractable links to a
  portfolio page. Not verified.
- **Exact portfolio counts.** Where a page says "Show More" or paginates behind
  JS (Portfolion, Hiventures, FPE), the count below is what was actually served,
  not the fund's claimed total. Both numbers are given where they differ.
- **Update cadence.** Except where a per-company date field exists in the markup,
  cadence is an inference from the newest dated item on the page. I did not diff
  pages over time. Any entry whose cadence is stated without a date field should be
  treated as an estimate.
- **Portfolio pages behind auth** (LP logins on MidEuropa, Motive, Innova) were not
  attempted.

---

# Entries

## A. CEE early-stage funds (MVP markets: PL, CZ, RO, HU)

### Credo Ventures

- **Type:** VC portfolio
- **Geography:** Czech Republic, CEE, CEE diaspora
- **Homepage:** https://www.credoventures.com/
- **List page:** https://www.credoventures.com/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static; names present in served markup)
- **Update cadence:** No date field. Page counter reads "84 (Pre-seeds) Since 2009",
  so roughly 5-6 additions a year. Status badges (`Exited`, `RIP`) are maintained,
  which implies the page is actively edited.
- **Why it surfaces card candidates:** Prague-based pre-seed lead across CEE writing
  $1-5M first cheques. Companies appear here at pre-seed, years before any card
  program decision. Sits directly in a TXN MVP market.
- **Approximate list size:** 84 stated; dozens of names extracted from the HTML
  (Bugprove, Goodlegal, Assetario, Talkbase, Munch.so, Stock Story, Manta, Waymark,
  SignAll, GoAvio, Represent, Apiary, DataFeedWatch, Klick2Contact, Cognitive
  Security and more)
- **Confidence:** Verified
- **Evidence:** `curl` returned 2.34 MB of HTML, 2,426 characters of extracted
  visible text with company names and status badges inline. Note: a WebFetch of the
  same URL reported the page as empty/JS-rendered. That was wrong, and the raw
  bytes disprove it. Worth flagging as a general caution about WebFetch on
  logo-heavy pages.
- **Last checked:** 2026-08-25

### Kaya VC

- **Type:** VC portfolio
- **Geography:** Czech Republic, Poland, Slovakia, CEE
- **Homepage:** https://www.kaya.vc/
- **List page:** https://www.kaya.vc/companies
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static)
- **Update cadence:** No date or year field, and no sector filter. Cadence not
  determinable from the page. Weakest of the Czech funds for monitoring.
- **Why it surfaces card candidates:** Pre-seed to Series A, EUR 1-3M initial
  cheques, concentrated in Czechia, Poland and Slovakia. Already holds fintech
  (Twisto, Finiata, Bnext), so the fund understands the category and its new names
  are plausible card candidates.
- **Approximate list size:** ~60 companies rendered
- **Confidence:** Verified
- **Evidence:** WebFetch retrieved and read the page. Identical markup pattern per
  card with hardcoded logos and descriptions, no filter controls, fintech entries
  Finiata ("Instant SME Lending"), Twisto ("BNPL Provider"), Bnext ("Personal
  Finance Hub").
- **Last checked:** 2026-08-25

### Inovo VC

- **Type:** VC portfolio
- **Geography:** Poland, CEE
- **Homepage:** https://inovo.vc/
- **List page:** https://inovo.vc/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML table (static, with country, sector and year per row)
- **Update cadence:** Years run 2015 through 2025 continuously, so at least several
  additions per year and the page is kept current.
- **Why it surfaces card candidates:** Warsaw pre-seed/seed/Series A in a TXN MVP
  market, with fintech already in the book. Symmetrical (payroll fintech, PL, 2021)
  and Fiat Republic (PL, 2023) are the exact profile of a company that later needs
  issuing.
- **Approximate list size:** ~50 companies
- **Confidence:** Verified
- **Evidence:** WebFetch retrieved and read the page. Per-company rows carry
  sector, country and year. Fintech rows observed: Handwave (Fintech, Latvia, 2025),
  Fiat Republic (Fintech/Web3, Poland, 2023), Symmetrical (Fintech/HRtech/Payroll,
  Poland, 2021). Page states 7 portfolio companies above EUR 100m valuation.
- **Last checked:** 2026-08-25

### Underline Ventures

- **Type:** VC portfolio
- **Geography:** Romania, CEE (portfolio spans Bulgaria, Ukraine, UK)
- **Homepage:** https://underline.vc/
- **List page:** https://underline.vc/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with `Country`, `Sector` and
  `Date of partnership` fields per company
- **Update cadence:** **Fastest observed in this pass.** The newest entry carried
  `Date of partnership: August 24, 2026`, one day before this check. The date field
  makes new additions trivially diffable.
- **Why it surfaces card candidates:** Romania is a TXN MVP market and Underline is
  a solo-GP first-cheque fund, so companies appear here at their earliest funded
  moment. The explicit partnership date means TXN can detect a new name within days.
- **Approximate list size:** ~20 companies (23.2k characters of extracted text;
  each company repeated 3x in the markup for hover states, so parse with dedupe)
- **Confidence:** Verified
- **Evidence:** `curl` returned 793 KB HTML and 23,243 characters of text. Companies
  observed with dates: Embedd (Ukraine/UK, Embedded Software, 24 Aug 2026), Uvionix
  (Bulgaria, Retail and logistics, 10 Feb 2025).
- **Last checked:** 2026-08-25

### Early Game Ventures

- **Type:** VC portfolio
- **Geography:** Romania, CEE
- **Homepage:** https://earlygame.vc/
- **List page:** https://earlygame.vc/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with category filters including an
  explicit **FinTech** filter
- **Update cadence:** No date field on the index. Individual companies have dated
  "why we invested" posts under `/portfolio/<slug>`, which is a secondary dated feed.
- **Why it surfaces card candidates:** Bucharest fund, Fund II capitalised via the
  EIF-managed Recovery Equity Fund, leading pre-seed and seed in a TXN MVP market.
  Already holds Symphopay (payments) and Profluo (finance automation), which
  demonstrates it writes cheques into exactly TXN's adjacent space.
- **Approximate list size:** 37 named companies
- **Confidence:** Verified
- **Evidence:** WebFetch retrieved and read the page. Filter set is
  `All / B2C / B2B / AI / Cybersecurity / FinTech / DevTools / Edtech / Others`.
  Full name list extracted including Symphopay, Profluo, Milluu, Druid, Licenseware,
  Kinderpedia, Vatis Tech.
- **Last checked:** 2026-08-25

### GapMinder VC

- **Type:** VC portfolio
- **Geography:** Romania, CEE
- **Homepage:** https://gapminder.vc/
- **List page:** https://gapminder.vc/#portfolio (anchor on homepage)
- **Publicly listed?** partial
- **Machine readable?** JS-rendered. The detailed portfolio table loads dynamically;
  the static homepage carries only the highlight names.
- **Update cadence:** Unknown from the page. The site runs a dated news stream of
  individual investment announcements, which is the more reliable signal.
- **Why it surfaces card candidates:** The most fintech-weighted Romanian fund:
  FintechOS, TypingDNA and Finqware are all in the book. Fund II targets EUR 80m and
  is deploying. If GapMinder backs it, it is a financial-services company in a TXN
  MVP market.
- **Approximate list size:** ~20 names visible statically; full portfolio larger
- **Confidence:** Verified (page fetched) / Reported (portfolio size)
- **Evidence:** `https://gapminder.vc/portfolio/` returns **HTTP 404**. The homepage
  fetch surfaced the anchor and the highlight names above and the claim "85% of
  portfolio companies raised follow-on rounds", but the detailed table did not
  render statically.
- **Last checked:** 2026-08-25

### Movens Capital

- **Type:** VC portfolio
- **Geography:** Poland, CEE, Balkans, Baltics
- **Homepage:** https://movenscapital.com/
- **List page:** https://movenscapital.com/our-portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML table (static) with `Company / Description / Sector /
  Entry date` columns, plus Fund (Fund 1 / Fund 2 / Legacy) and Active/Exited filters
- **Update cadence:** `Entry date` is per-company by quarter. Entries observed from
  Q3 2020 to Q3 2025, so a diff on entry date reliably catches new names within a
  quarter.
- **Why it surfaces card candidates:** Warsaw, EUR 60m Fund 2, EUR 0.25-3M cheques
  from pre-seed to growth across Poland plus Czechia, Slovakia, Hungary and Romania:
  all four TXN MVP markets in one fund's mandate.
- **Approximate list size:** ~25-30 companies rendered (11,057 characters of text)
- **Confidence:** Verified
- **Evidence:** `curl` returned 249 KB and 11,057 characters. Note the obvious URL
  `movenscapital.com/portfolio` returns **404**; the real path is `/our-portfolio/`,
  found by extracting `href` attributes from the homepage. Sample rows: Talkie.ai
  (Healthtech Voice AI, Q3 2020), Certifier (Digital Credentialing SaaS, Q3 2024),
  Sun.Store (Solar Components Marketplace, Q3 2025), BeeSpeaker (EdTech, Q2 2025).
- **Last checked:** 2026-08-25

### Market One Capital

- **Type:** VC portfolio
- **Geography:** Poland (Warsaw) and Spain (Barcelona), investing across Europe
  including Bulgaria, Lithuania, Greece, Portugal
- **Homepage:** https://www.moc.vc/
- **List page:** https://www.moc.vc/portfolio
- **Publicly listed?** yes
- **Machine readable?** **HTML table (static)** with `Company / Description /
  HQ Country / Year / Sector / Co-Founders / Status` columns, plus filter vocabularies
  for HQ country, sector (including **`FinTech`**) and **`Year of investment`
  (2018 through 2026)**
- **Update cadence:** Year of investment is a first-class filter and **2026 entries
  are already present**, so the page is current. Annual granularity, but ordering is
  newest-first, which makes new names easy to spot.
- **Why it surfaces card candidates:** Warsaw-headquartered seed fund (EUR 45m)
  investing in marketplaces and network-effect platforms. **Marketplaces are a
  first-order card-issuing use case**: seller payouts, split payments, spend controls.
  Two 2025-2026 fintech rows are directly on-thesis: VINR (Bulgaria, FinTech, 2026,
  "a last mile multi-rail infrastructure for modern businesses") and Rizon (USA,
  FinTech, 2025, "dollar banking in the cloud"). Poland is a TXN MVP market.
- **Approximate list size:** 60+ investments reported; ~40 rows rendered
- **Confidence:** Verified
- **Evidence:** `curl` returned 225 KB and 12,396 characters. Filter values read
  verbatim from markup: HQ countries `Austria, Bulgaria, France, Germany, Greece,
  Lithuania, Netherlands, Palo Alto, Poland, Portugal, Spain, United Kingdom, USA`;
  sectors including `FinTech`, `E-commerce infra`, `Data infrastructure`, `PropTech`,
  `HRTech`; years `2026` down to `2018`. Sample rows: Kazimi (Germany, Cybersecurity,
  2026, Active), Stetig (Germany, Logistics, 2026), VINR (Bulgaria, FinTech, 2026),
  Rizon (USA, FinTech, 2025).
- **Last checked:** 2026-08-25

### Day One Capital

- **Type:** VC portfolio
- **Geography:** Hungary, CEE (portfolio spans HU, RO, CZ, HR, North Macedonia)
- **Homepage:** https://dayonecapital.com/
- **List page:** https://dayonecapital.com/#portfolio (same-page anchor, not a
  separate URL)
- **Publicly listed?** partial
- **Machine readable?** HTML cards (static / server-rendered), no filters, no dates
- **Update cadence:** Unknown. Small curated selection rather than a full list, so
  new investments may not appear promptly. Treat as low-signal for monitoring.
- **Why it surfaces card candidates:** Budapest-based, backs early-stage B2B software
  from CEE, states fintech among target sectors, launched a EUR 45m fund. Hungary is
  a TXN MVP market and the fund's earlier vehicle exited Tresorit and Gamee.
- **Approximate list size:** 6 companies shown on the homepage (Colossyan, Orqa,
  Veridion, Whalebone, HeyReach, Allonic); full portfolio is larger
- **Confidence:** Verified (page fetched) / Reported (full portfolio size)
- **Evidence:** WebFetch retrieved and read the homepage. The `Portfolio` nav item
  resolves to `#portfolio`, an in-page anchor, not a dedicated list page.
- **Last checked:** 2026-08-25

### ZAKA VC

- **Type:** VC portfolio
- **Geography:** Slovakia / CEE, with global (largely US) deal flow
- **Homepage:** https://zaka.vc/
- **List page:** https://zaka.vc/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static; names present as a delimited run in the
  served markup)
- **Update cadence:** No date field on the index. Site carries a dated News section.
- **Why it surfaces card candidates:** Slovak fund, heavily deeptech and biotech, but
  holds Mews (Czech hospitality PMS, an obvious embedded-payments profile) and
  Lunabill. Value here is more as a CEE-adjacent watchlist than as a fintech source.
- **Approximate list size:** ~27 named companies
- **Confidence:** Verified
- **Evidence:** `curl` returned 170 KB and 12,642 characters with the full name run:
  FinalDose, PerfectBit, Human Archive, AxionOrbital Space, CellType, Sygaldry,
  HexemBio, Ateios Systems, Mews, Zephyr Fusion, DeepSeq.AI, Lunabill, and others.
- **Last checked:** 2026-08-25

### J&T Ventures

- **Type:** VC portfolio
- **Geography:** Czech Republic, CEE
- **Homepage:** https://www.jtventures.cz/
- **List page:** https://www.jtventures.cz/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static names) with a client-side filter set that
  includes an explicit **FinTech** tag; counters render as `0` server-side
- **Update cadence:** Unknown from the page. Site has a blog but no per-company date.
- **Why it surfaces card candidates:** Prague, and notably the venture arm attached
  to **J&T Banka**, so this doubles as a bank-adjacent corporate venture source in
  a TXN MVP market. Portfolio includes Finlay (fintech).
- **Approximate list size:** ~20 named companies rendered
- **Confidence:** Verified
- **Evidence:** `curl` returned 80 KB and 1,984 characters. Names present
  (Supernova.io, Oddin.gg, Grid.online, XUND, Finlay, OutdoorVisit, Daytrip,
  Davinci Travel System, CodeNOW, Born Digital, Behavio). Sector tag list includes
  `FinTech`. Page is Czech-language by default with an `EN` toggle.
- **Last checked:** 2026-08-25

### Innovation Nest

- **Type:** VC portfolio
- **Geography:** Poland, Europe
- **Homepage:** https://innovationnest.com/
- **List page:** https://innovationnest.com/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML table plus gallery (static) with `Company / Country /
  Sector tags / Partner / Status / Website` per row
- **Update cadence:** No date column, but `Status` (Active/exited) is maintained and
  partner attribution is per-company, implying an actively edited table.
- **Why it surfaces card candidates:** Kraków B2B SaaS seed fund in a TXN MVP market.
  The row format is the most parseable of the Polish funds and includes the target
  company's own website URL, which shortens enrichment. Fintech rows present
  (Ember, UK, Fintech/Accounting; Sense Street, UK, Fintech/Capital Markets).
- **Approximate list size:** ~40+ rows
- **Confidence:** Verified
- **Evidence:** `curl` returned 480 KB and 3,921 characters in a Notion-style
  gallery plus table layout. Sample rows: uPacjenta (Poland, Health Care, Active),
  Cardiomatics (Poland, Health Care), Ember (UK, Fintech, Accounting).
- **Last checked:** 2026-08-25

### OTB Ventures

- **Type:** VC portfolio
- **Geography:** Poland / CEE origin, pan-European deeptech
- **Homepage:** https://otb.vc/
- **List page:** https://otb.vc/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with `Founded`, `Invested`, `Current
  stage`, `Founders` and `Investors` fields per company
- **Update cadence:** `Invested: <year>` per company, observed up to 2026. Annual
  granularity, but a genuine date field.
- **Why it surfaces card candidates:** Warsaw-founded, deeptech/spacetech/defence
  thesis, so **low direct fintech relevance**. Included because the per-company
  metadata block (founded, invested, stage, co-investors) is one of the richest
  structured formats found, and because it is a Polish fund whose new names are
  well-capitalised European companies. Rank it below the fintech-thesis funds.
- **Approximate list size:** ~30 companies (20,721 characters of text)
- **Confidence:** Verified
- **Evidence:** `curl` returned 287 KB and 20,721 characters. Note `www.otbvc.com`
  does not connect; the working domain is `otb.vc`. Sample: akirolabs (Invested
  2023), Alta Ares (Founded 2024, Invested 2026, Series A).
- **Last checked:** 2026-08-25

### bValue Fund

- **Type:** VC portfolio
- **Geography:** Poland, CEE
- **Homepage:** https://bvaluefund.com/
- **List page:** none. `bvalue.vc/portfolio` and `bvaluefund.com/investments/`
  both redirect to the homepage
- **Publicly listed?** partial
- **Machine readable?** The portfolio itself is not published as a list. What *is*
  published is a **dated content table** on the homepage:
  `Date / Title / Author`, with rows titled "Investing in <company>".
- **Update cadence:** Dated rows observed from 25/07/2024 through 02/11/2025. This
  is effectively an investment announcement feed with an explicit date column,
  arguably better for TXN than a portfolio grid, because each row *is* a new deal.
- **Why it surfaces card candidates:** Warsaw fund covering CEE tech. The "Investing
  in X" post pattern gives a clean, dated first-mention of each new holding.
- **Approximate list size:** 7 dated rows on the homepage; "All content" link for more
- **Confidence:** Verified
- **Evidence:** `curl` on both `bvalue.vc/portfolio` and `bvaluefund.com/investments/`
  resolved to `https://bvaluefund.com/` (56.7 KB, 937 characters). Dated rows read:
  "Investing in Solidstudio" (10/02/2025), "Investing in Fudo Security" (20/01/2025),
  "Investing in Xtreme Brands" (15/04/2025).
- **Last checked:** 2026-08-25

## B. Corporate venture arms and state funds in CEE

### Elevator Ventures (Raiffeisen Bank International)

- **Type:** VC portfolio (bank corporate venture arm)
- **Geography:** CEE and DACH, explicitly the RBI footprint (Poland, Czechia,
  Hungary, Romania, Austria)
- **Homepage:** https://www.elevator-ventures.com/
- **List page:** https://www.elevator-ventures.com/en/portfolio.html
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with `Headquarters`, `Founded` and
  `Selected Co-Investors` per company
- **Update cadence:** Portfolio is segmented by fund vintage ("EV II ... vintage
  starting from 2024"), so new-fund additions are identifiable by section. No
  per-company investment date.
- **Why it surfaces card candidates:** **The single most on-thesis corporate arm for
  TXN.** RBI's CVC exists to invest in fintech across CEE, writes up to EUR 3M at
  seed and Series A, and its co-investor field names the syndicate, which is itself
  a discovery vector for adjacent funds. Any company it backs is financial-services
  adjacent, in a TXN market, and pre-scale.
- **Approximate list size:** ~15 companies in the EV II section, more across vintages
- **Confidence:** Verified
- **Evidence:** `curl` returned 237 KB and 10,242 characters. `.com/portfolio`
  redirects to `/en/portfolio.html`. Sample: Blockpit (Linz, Austria, founded 2017,
  co-investors Middlegame Ventures and Venionaire Capital), QuoIntelligence
  (Frankfurt), exnaton (Zurich), Klim (Berlin).
- **Last checked:** 2026-08-25

### Portfolion Capital Partners (OTP Bank)

- **Type:** VC portfolio (bank corporate venture arm, multi-stage VC/growth/PE)
- **Geography:** Hungary and CEE (14 countries stated)
- **Homepage:** https://www.portfolion.com/
- **List page:** https://www.portfolion.com/companies/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static names) grouped by stage (Venture Capital,
  Growth Equity, Private Equity, Exit) with a JS `Show More` truncating each group
- **Update cadence:** No per-company date on the index, but the site runs a dated
  `/investment-story/` stream (an entry dated 19-08-2026 was observed), which is the
  monitoring surface to poll.
- **Why it surfaces card candidates:** OTP is Hungary's largest bank and a major CEE
  banking group; its venture arm invests EUR 500k-3M at pre-seed and seed across CEE.
  Two fintechs are already in the book (SEON, Finshape) plus FLOWX.AI. Hungary is a
  TXN MVP market. The growth and PE tiers additionally surface established CEE
  businesses, the PE-owned-adds-cards pattern.
- **Approximate list size:** "46 companies across 15 verticals and 14 countries"
  stated; 32 names served before `Show More`
- **Confidence:** Verified
- **Evidence:** `curl` returned 230 KB and 2,502 characters. Note `/portfolio/` and
  `/portfolio-companies/` both **404**; the real path `/companies/` was recovered by
  extracting `href` values from the homepage. VC tier names: Kodesage, SEON,
  Riptides, FLOWX.AI, Deskbird, Novakid, Uvionix, Deligo Vision. Growth tier:
  Mobilfox, GymBeam, Finshape, Pactum, Pepita.hu, VCC Live, Codecool, 4FIZJO.
- **Last checked:** 2026-08-25

### Hiventures

- **Type:** VC portfolio (Hungarian state-backed venture investor)
- **Geography:** Hungary
- **Homepage:** https://hiventures.hu/en/
- **List page:** https://hiventures.hu/en/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML list, **paginated**, with a **publication date per
  entry** (`/portfolio/page/2/` through `/page/5/`)
- **Update cadence:** Best-in-class for a state fund. Entries carry dates; the most
  recent English-side entries were dated 17 February 2026 and the oldest on page 5
  dated March/April 2024. Reverse-chronological ordering means page 1 is a new-deal
  feed.
- **Why it surfaces card candidates:** Hungary is a TXN MVP market and Hiventures is
  by volume one of the most prolific investors in it, funding very early and very
  broadly, including businesses the fintech press will never cover. This is the
  definition of the fringe source the brief asks for.
- **Approximate list size:** ~44 companies on the English site (5 pages of ~10). The
  Hungarian-language side is likely far larger. **Not verified.**
- **Confidence:** Verified
- **Evidence:** `curl` on `/en/portfolio/` returned 59 KB with dated entries
  (Biopesticide, Polcz, Zyntern, Horizont Brewing, 4D Interactive Anatomy, all
  17 Feb 2026; Oneminorder, Salarify, Merova, Vellab, RoyalPaté, 16 Feb 2026) and
  pagination "1 2 3 ... 5 Next". `/en/portfolio/page/5/` confirmed as the last page
  (BookrKids 17 Apr 2024, CX-Ray, Chameleon, DataInnovation, all Mar 2024).
- **Last checked:** 2026-08-25

### Lead Ventures (MOL Group)

- **Type:** VC portfolio (corporate venture arm of MOL Group)
- **Geography:** Hungary, Central Europe, Baltics
- **Homepage:** https://leadventures.eu/
- **List page:** https://leadventures.eu/portfolio/
- **Publicly listed?** no (page exists, list does not render)
- **Machine readable?** **JS-rendered.** Page returns navigation and boilerplate only,
  zero company names.
- **Update cadence:** Not determinable without a headless browser.
- **Why it surfaces card candidates:** Budapest, corporate-backed, EUR 150k-1.5M into
  Central European and Baltic scale-ups. Corporate arms sit adjacent to enterprise
  buyers, and MOL is a fuel retailer, a category with real card-program relevance.
  Worth the headless-browser cost to unlock.
- **Approximate list size:** unknown
- **Confidence:** Verified (that the page serves no list)
- **Evidence:** `curl` returned 86 KB of HTML but only 1,118 characters of visible
  text, consisting entirely of nav, cookie banner, address and boilerplate. No
  company names in the served markup.
- **Last checked:** 2026-08-25

### PFR Ventures

- **Type:** VC portfolio (Polish state fund-of-funds, lists *funds*, not companies)
- **Geography:** Poland
- **Homepage:** https://pfrventures.pl/
- **List page:** https://pfrventures.pl/en/portfolio.html
- **Publicly listed?** unknown
- **Machine readable?** unknown (blocked)
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Indirect but potentially the highest-leverage
  Polish source. PFR capitalises most of the Polish VC market; its portfolio page is
  a roster of the funds themselves. Resolving it would generate the complete list of
  Polish funds whose own portfolio pages TXN should then monitor. A meta-source.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** `curl` returned **HTTP 403** with a Polish-language Cloudflare block
  page ("Dostęp został zablokowany", Ray ID a30b46544b2bedf6). Needs a real browser
  session. **Recommend retrying this one first.**
- **Last checked:** 2026-08-25

### UNIQA Ventures

- **Type:** VC portfolio (insurer corporate venture arm)
- **Geography:** Austria, CEE
- **Homepage:** https://www.uniqaventures.com/ (resolves to the UNIQA group
  corporate site)
- **List page:** none found
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** n/a
- **Why it surfaces card candidates:** UNIQA is an Austrian insurer with a large CEE
  footprint, and its ventures arm co-invests in fintech (it is named as a partner in
  the Fintech Growth Fund Europe vehicle alongside Elevator Ventures and
  Speedinvest). Insurers adding cards is a real pattern. But there is no scrapeable
  surface.
- **Approximate list size:** unknown
- **Confidence:** Verified (that no standalone portfolio page is served)
- **Evidence:** `curl` on `uniqaventures.com/portfolio` returned **404**. Extracting
  `href` values from `uniqaventures.com` returned only UNIQA group corporate and
  investor-relations paths (`/grp/investor-relations/...`), i.e. the domain points at
  the parent insurer's site, not a VC microsite.
- **Last checked:** 2026-08-25

### ING Ventures

- **Type:** VC portfolio (bank corporate venture arm)
- **Geography:** Netherlands, Europe, global
- **Homepage:** not verified in this pass
- **List page:** not found
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** possibly zero (see below)
- **Why it surfaces card candidates:** Would be a strong Benelux (Phase 1b) source if
  live: a EUR 350m+ evergreen fintech and regtech vehicle.
- **Approximate list size:** unknown
- **Confidence:** **Unverified**
- **Evidence:** A Global Venturing headline reads "Dutch bank ING's ventures arm halts
  new investments". I attempted to read it at
  `https://globalventuring.com/corporate/europe/dutch-bank-ings-ventures-arm-halts-new-investments/`
  and received **HTTP 403** from both `curl` and WebFetch. I did not read the body,
  so I am not asserting the halt, its date, or what happens to the existing
  portfolio. **Recorded as an unconfirmed lead, not a finding.** Per the "defunct is
  a finding" rule this is worth resolving: if ING Ventures has stopped, it should be
  struck from any monitoring list rather than silently returning nothing.
- **Last checked:** 2026-08-25

## C. European fintech and payments-thesis VC

### Illuminate Financial

- **Type:** VC portfolio
- **Geography:** UK and Europe, North America, Asia
- **Homepage:** https://www.illuminatefinancial.com/
- **List page:** https://www.illuminatefinancial.com/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with `THEME`, `GEOGRAPHY` and `STATUS`
  filters
- **Update cadence:** No date field. Fund-count language ("47 Investments across four
  funds") suggests the page is revised per deal.
- **Why it surfaces card candidates:** Carries a literal **`Payments & CFO Stack`**
  theme filter alongside `Fintech` and `Financial Markets Infrastructure`. That is the
  most precisely TXN-shaped taxonomy encountered anywhere in this pass. LP base is
  JPMorgan, Barclays, Deutsche Börse and Citi, so its picks are institutionally
  validated B2B fintech: companies that will need issuing but have not built it.
- **Approximate list size:** 47 investments stated, 13 exits
- **Confidence:** Verified
- **Evidence:** `curl` returned 129 KB and 7,479 characters. Filter values read from
  the markup: themes `AI & Enterprise Tech`, `Digital Assets Infrastructure`,
  `Energy & Climate`, `Fintech`, `Financial Markets Infrastructure`,
  `Payments & CFO Stack`, `Private Markets, Wealth & Asset Management`. Note the
  domain: `illuminate.financial` **does not resolve**; the site is
  `illuminatefinancial.com`.
- **Last checked:** 2026-08-25

### Anthemis Group

- **Type:** VC portfolio
- **Geography:** UK, Europe, North America
- **Homepage:** https://www.anthemis.com/
- **List page:** https://www.anthemis.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static; alphabetical name run present in markup)
  with `Thesis`, `Strategy` and `Stage` filters
- **Update cadence:** No date field on the index. Site runs a dated "Why we invested"
  stream which is the better polling surface.
- **Why it surfaces card candidates:** Thesis filter includes **`Payments`**,
  **`Business & Corporate Banking`** and **`Retail Banking & Consumer Finance`**, and
  the `Stage` filter includes `Pre Seed`. A pre-seed company under the Payments thesis
  is close to a perfect TXN lead definition.
- **Approximate list size:** large (alphabetical run from Acre Homes onwards); exact
  count not served
- **Confidence:** Verified
- **Evidence:** `curl` returned 395 KB and 3,642 characters. Filter taxonomy extracted
  verbatim from markup. Names visible: Acre Homes, AcreTrader, Addition Wealth,
  AgentSync, Agreena, Alaffia Health, Hokodo, Kaiko, yulife, Diagon.
- **Last checked:** 2026-08-25

### Seedcamp

- **Type:** VC portfolio
- **Geography:** Europe (pan-European, incl. CEE)
- **Homepage:** https://seedcamp.com/
- **List page:** https://seedcamp.com/our-companies/ (`/companies/` redirects here)
- **Publicly listed?** yes
- **Machine readable?** **HTML table (static)** with explicit
  `Company Name / Year of Investment / Description / Link to website` columns, plus a
  `Fintech` filter
- **Update cadence:** **High and verifiable.** 2026-vintage rows were already present
  (Waniwani, "Revenue infrastructure for AI"; Eversettled). Profile cards additionally
  carry dates (e.g. `29.07.2024`). Year-of-investment is a first-class column, so a
  weekly diff surfaces new names cleanly.
- **Why it surfaces card candidates:** Europe's most prolific day-one investor
  (550+ companies) with a genuine fintech track record (Revolut, Wise, Pleo). Its new
  2026 names are, by construction, companies with no card program. Not a fringe fund,
  but the **page format** is the best-engineered discovery surface in this pass, and
  the target company's own website URL is in the row.
- **Approximate list size:** 550+ portfolio companies stated
- **Confidence:** Verified
- **Evidence:** `curl` returned 449 KB and 36,176 characters. Column headers read
  literally from markup: `Company Name`, `Year of Investment`, `Description`,
  `Link to <company>'s website`. Filters: `All, AI, Climate, Consumer, Crypto,
  Developer Tools, Enterprise, Fintech, Health/Bio, Marketplaces, Security`.
- **Last checked:** 2026-08-25

### Speedinvest

- **Type:** VC portfolio
- **Geography:** Austria, DACH, pan-European (incl. Hungary, Bulgaria, Estonia,
  Slovenia, Croatia, Greece)
- **Homepage:** https://www.speedinvest.com/
- **List page:** https://www.speedinvest.com/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static; company names and a parallel country list
  render server-side)
- **Update cadence:** No date field. Large portfolio, frequent additions.
- **Why it surfaces card candidates:** Speedinvest runs a dedicated fintech team and
  the portfolio already contains issuing-adjacent infrastructure (Upvest,
  "investment infrastructure powering modern financial products"; Gigs, embedded
  telecom; Tide, SME challenger bank; Wayflyer). Austria is Phase 1b and the
  portfolio country list confirms Hungary, Bulgaria, Estonia, Slovenia and Croatia
  exposure, so it reaches into CEE.
- **Approximate list size:** 400+ companies stated
- **Confidence:** Verified
- **Evidence:** `curl` returned 773 KB and 52,283 characters including a long
  server-rendered country sequence per card. Title tag reads "Speedinvest Portfolio:
  400+ Global Tech Companies & Unicorns".
- **Last checked:** 2026-08-25

### Target Global

- **Type:** VC portfolio
- **Geography:** Europe (Berlin/London), Israel, US
- **Homepage:** https://www.targetglobal.vc/
- **List page:** https://www.targetglobal.vc/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static names) with `Region` and `Industry`
  filters, industry list including **`Fintech`**
- **Update cadence:** No date field. Page carries two different counters ("Portfolio
  98" in the header, "42 investments" in the filter block), so counts on this page
  are not reliable.
- **Why it surfaces card candidates:** Deep payments track record (Rapyd, "the
  world's largest local payments network"; Revolut) plus CEE exposure via Docplanner.
  A Target Global Series A in payments adjacency is a strong TXN trigger, though the
  fund invests later than TXN's ideal entry point.
- **Approximate list size:** 42-98 (the page is internally inconsistent)
- **Confidence:** Verified
- **Evidence:** `curl` returned 326 KB and 37,817 characters. Names in markup include
  Gett, Fyber, DreamLines, Cybellum, Cryptofacilities, Zooz, Seekret, Minit, Kippa,
  Ermetic, Cobee, Rapyd, Delivery Hero, Flink, Copper, Reef. Note the markup contains
  a repeated `Rapyd` placeholder block, so naive parsing will over-count Rapyd.
- **Last checked:** 2026-08-25

### Middlegame Ventures

- **Type:** VC portfolio
- **Geography:** Europe and North America (Luxembourg-based, fintech thesis)
- **Homepage:** https://www.middlegame.vc/
- **List page:** https://www.middlegame.vc/portfolio
- **Publicly listed?** no (renders client-side only)
- **Machine readable?** **JS-rendered.** 114 bytes of HTML, zero text.
- **Update cadence:** not determinable statically
- **Why it surfaces card candidates:** A dedicated fintech fund that appears as a
  named co-investor on Elevator Ventures' portfolio (Blockpit), which puts it in the
  CEE/DACH fintech syndicate. Worth unlocking with a headless browser given the pure
  fintech thesis.
- **Approximate list size:** unknown
- **Confidence:** Verified (that the page serves no content statically)
- **Evidence:** `curl` returned exactly 114 bytes and 0 characters of extractable
  text, an empty SPA shell.
- **Last checked:** 2026-08-25

## D. Private equity with payments and fintech portfolios

### Motive Partners

- **Type:** VC portfolio (fintech-specialist PE: venture, growth and buyout)
- **Geography:** North America and Europe (New York, London, Berlin)
- **Homepage:** https://motivepartners.com/
- **List page:** https://motivepartners.com/portfolio
- **Publicly listed?** yes
- **Machine readable?** **HTML cards (static) with `Subsector`, `Strategy`,
  `Location`, `Investment date` (month plus year) and realised/unrealised status per
  company.** The richest structured format found in this pass.
- **Update cadence:** `Investment date` to the month, with entries observed through
  **February 2026**. Directly diffable.
- **Why it surfaces card candidates:** The `Banking & Payments` subsector filter plus
  a `Growth & Buyout` strategy tag identifies **PE-owned financial-services
  businesses**, precisely the "PE-owned business adding cards" pattern in the brief.
  A buyout-stage banking or payments company with a new sponsor is a company under
  pressure to launch new products, on a defined timeline.
- **Approximate list size:** ~40+ companies rendered
- **Confidence:** Verified
- **Evidence:** `curl` returned 358 KB and 10,887 characters. Sample rows: Accordion
  (Business services, Growth & Buyout, NYC, August 2022, Not realized); Alchelyst
  (Wealth & asset management, Growth & Buyout, NYC, February 2026); Anchorage Digital
  (Capital markets, Venture, San Francisco, November 2021); AMP (Venture, Boulder CO,
  May 2023, Realized). Subsector values include `Business services`, `Wealth & asset
  management`, `AI, data & analytics`, `Capital markets`.
- **Last checked:** 2026-08-25

### Pollen Street Capital

- **Type:** VC portfolio (financial-services-only PE and private credit)
- **Geography:** UK, Europe (Nordics, Benelux, Ireland)
- **Homepage:** https://www.pollenstreetgroup.com/
- **List page:** https://www.pollenstreetgroup.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static; name plus one-line description per card)
- **Update cadence:** No date field. Listed manager, so deals are also announced via
  RNS, a dated secondary feed.
- **Why it surfaces card candidates:** The portfolio is **wall-to-wall payments and
  banking**: Autopay ("digital payments platform"), Cashflows ("omni-channel payment
  services to SMEs"), bunq, Ding, Aryza. Sub-sectors stated as Lending, Insurance,
  Wealth, Payments, Tech-enabled Services. PE professionals here see European
  payments deal flow daily, which makes the firm itself a relationship target as
  well as a list.
- **Approximate list size:** ~20 named on the page; 64 companies reported elsewhere
  (not verified)
- **Confidence:** Verified
- **Evidence:** `curl` returned 156 KB and 4,627 characters with names and
  descriptions inline: Aryza, Assessio, Autopay, BidX1, bunq, Cashflows, Ding, etops.
- **Last checked:** 2026-08-25

### Advent International

- **Type:** VC portfolio (global PE with a Business & Financial Services vertical)
- **Geography:** Global, with a named European presence (UK, France, Germany, Italy,
  Spain, Luxembourg)
- **Homepage:** https://www.adventinternational.com/
- **List page:** https://www.adventinternational.com/investments/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with `Search by sector` and
  `Search by deal type` filters (`Buyout`, `Carve-out`, `Expansion capital`,
  `Growth buyout`, `Growth equity`, `Leveraged buyout`)
- **Update cadence:** No per-company date served. Site has a dated News section.
- **Why it surfaces card candidates:** The **`Carve-out`** deal type is the sharpest
  signal on this page. A financial-services or retail unit carved out of a corporate
  parent loses the parent's payment infrastructure and must rebuild it, often
  including issuing. Advent has a long payments history and a `Business & financial
  services` sector filter.
- **Approximate list size:** large; count not served
- **Confidence:** Verified
- **Evidence:** `curl` returned 238 KB and 11,450 characters. Sector filter values:
  `Business & financial services`, `Consumer`, `Healthcare`, `Industrial`,
  `Aerospace, defense, and space`, `Technology`. Deal-type filter values as listed
  above.
- **Last checked:** 2026-08-25

### Hg

- **Type:** VC portfolio (software and services PE)
- **Geography:** Europe and North America
- **Homepage:** https://hgcapital.com/
- **List page:** https://hgcapital.com/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static names and descriptions) with `Category`
  filters and an `A-Z` view
- **Update cadence:** No date field.
- **Why it surfaces card candidates:** Hg's thesis is **mission-critical SMB
  software**, which is the vertical-SaaS category the brief calls out: "a vertical
  SaaS business that will need cards and does not know it yet". Visma alone
  ("mission-critical business software to SMBs in Northern Europe") is a canonical
  embedded-payments candidate. Category filters observed include
  `Legal & Regulatory`, `Automation & Engineering`, `Insurance`.
- **Approximate list size:** large; count not served
- **Confidence:** Verified
- **Evidence:** `curl` returned 139 KB and 2,306 characters. Names in markup: A-LIGN,
  AMDT, Ascendia Gruppe, CINC, Trackunit, Visma.
- **Last checked:** 2026-08-25

### MidEuropa

- **Type:** VC portfolio (CEE-dedicated PE, ~EUR 5.3bn AUM)
- **Geography:** Central and Eastern Europe: Poland, Romania, Croatia, Baltics
- **Homepage:** https://mideuropa.com/
- **List page:** https://mideuropa.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static; name plus one-line description)
- **Update cadence:** No date field. `Portfolio Case Studies` sub-page and a News
  section provide dated context.
- **Why it surfaces card candidates:** The largest CEE-dedicated buyout house, and
  the portfolio is full of the exact profile: **Symfonia** (ERP and payroll software
  for Polish SMEs, an embedded-finance candidate with a captive SME base),
  **Pigu Group** (largest Baltic e-commerce platform), **Urgent Cargus** (Romanian
  courier). A PE-backed CEE platform with an SME customer base is a card program
  waiting to happen, and there is a sponsor with the capital to fund it.
- **Approximate list size:** ~15 named on the page
- **Confidence:** Verified
- **Evidence:** `curl` returned 97 KB and 1,805 characters. Names: OSHEE, RBC Romania,
  Optika Anda, MBL, FAMAR, Optegra, Pigu Group, Symfonia, Displate.
- **Last checked:** 2026-08-25

### Innova Capital

- **Type:** VC portfolio (CEE mid-market PE, founded 1994)
- **Geography:** Poland, Romania, Hungary, Slovakia, Bulgaria, Croatia, Slovenia,
  Baltics, Moldova
- **Homepage:** https://innovacap.com/
- **List page:** https://innovacap.com/our-investments/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with three filter axes: **`Fund`**
  (Innova/3 through Innova/7), **`Country`** and **`Sector`**. Sector values include
  **`Financial Services`**.
- **Update cadence:** No per-company date, but the `Fund` filter is a vintage proxy:
  anything tagged Innova/7 is current-fund and therefore recent.
- **Why it surfaces card candidates:** A `Financial Services` plus `In Portfolio` plus
  `Poland/Romania/Hungary` filter combination returns exactly TXN's target set of
  PE-owned CEE financial businesses. ProService Finteco (fund administration
  services) is already visible under that sector.
- **Approximate list size:** ~50 investments across 10 countries reported; ~30
  rendered
- **Confidence:** Verified
- **Evidence:** `curl` returned 73 KB and 9,871 characters. Note
  `innovacap.com/portfolio/` **404s**; the working path is
  `/our-investments/portfolio/`. Filter values read from markup, including country
  values `Poland`, `Romania`, `Hungary`, `Slovakia`, `Bulgaria`, `Croatia`, `CEE`,
  `Baltics`.
- **Last checked:** 2026-08-25

### Abris Capital Partners

- **Type:** VC portfolio (CEE mid-market PE)
- **Geography:** Poland, Romania and five other CEE countries
- **Homepage:** https://abris-capital.com/
- **List page:** https://abris-capital.com/investment/ (`/portfolio` redirects here)
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static; truncated descriptions with `Filter cases`)
- **Update cadence:** No date field. Some cards carry investment month and year inside
  the description text (e.g. "In March 2018 Abris invested in WDX SA"), which is
  parseable but inconsistent.
- **Why it surfaces card candidates:** 30 investments plus 50+ bolt-ons across seven
  CEE countries. **Alsendo** ("leader in technological shipping solutions for
  businesses") and **Urgent Cargus** are logistics platforms with merchant bases,
  a recurring embedded-card profile. Bolt-on acquisitions are themselves a trigger:
  a newly consolidated group has to unify payment infrastructure.
- **Approximate list size:** 30 investments stated; ~14 rendered
- **Confidence:** Verified
- **Evidence:** `curl` returned 107 KB and 2,882 characters. Names: CARGOUNIT,
  Hyperfy, Patent Co., Novago, Siodemka, Orbitvu, Scanmed, Urgent Cargus, Alsendo,
  WDX, Velvet Care, Pehart, MatexLab Group, Green Group.
- **Last checked:** 2026-08-25

### FPE Capital

- **Type:** VC portfolio (UK software and data growth PE)
- **Geography:** United Kingdom
- **Homepage:** https://www.fpecapital.com/
- **List page:** https://www.fpecapital.com/portfolio
- **Publicly listed?** partial
- **Machine readable?** Mostly **JS-rendered**. Pagination controls (`1 2 3`) render
  but company cards do not appear in the served text.
- **Update cadence:** not determinable statically
- **Why it surfaces card candidates:** "Over 35 investments (platform and bolt-on)"
  in profitable UK software and software-services businesses: vertical SaaS with
  existing revenue, i.e. companies with a customer base to monetise via cards.
  UK is Opportunistic tier for TXN, so this is lower priority.
- **Approximate list size:** 35+ investments stated; 0 rendered statically
- **Confidence:** Verified (that the list does not render statically)
- **Evidence:** `curl` returned 39 KB of HTML but only 918 characters of text, all
  boilerplate plus pagination.
- **Last checked:** 2026-08-25

### Enterprise Investors

- **Type:** VC portfolio (CEE PE and growth, EUR 20-75m equity cheques)
- **Geography:** Poland and CEE
- **Homepage:** https://www.ei.com.pl/
- **List page:** https://www.ei.com.pl/en/portfolio
- **Publicly listed?** no (page exists, list does not render)
- **Machine readable?** **JS-rendered.** 346 characters of text, zero companies.
- **Update cadence:** not determinable statically
- **Why it surfaces card candidates:** One of the oldest and largest Polish PE houses
  with a stated financial-services sector reach. High value if unlocked; Poland is a
  TXN MVP market.
- **Approximate list size:** unknown
- **Confidence:** Verified (that the page serves no list)
- **Evidence:** `curl` returned 18.9 KB of HTML, 346 characters of visible text
  consisting of nav, Warsaw address and footer only. Title tag reads
  "Investments Archive - Enterprise Investors".
- **Last checked:** 2026-08-25

### MCI Capital

- **Type:** VC portfolio (listed Polish PE, digital and tech)
- **Geography:** Poland and CEE
- **Homepage:** https://mci.pl/
- **List page:** https://mci.pl/en/portfolio
- **Publicly listed?** no (page exists, list does not render)
- **Machine readable?** **JS-rendered.** 385 characters of text, zero companies.
- **Update cadence:** not determinable statically. MCI is exchange-listed, so
  regulatory filings are a dated alternative feed.
- **Why it surfaces card candidates:** MCI is the most digital-focused Polish PE
  house and has historically owned payment and e-commerce assets. Poland is a TXN
  MVP market. Worth unlocking, but the listed-company filings route may be faster
  and more reliable than scraping.
- **Approximate list size:** unknown
- **Confidence:** Verified (that the page serves no list)
- **Evidence:** `curl` on `www.mci.pl/en/portfolio/` resolved to `mci.pl/en/portfolio`
  and returned 30 KB of HTML with 385 characters of text: navigation and copyright
  only.
- **Last checked:** 2026-08-25

## E. Angel syndicates and networks

### TechAngels (Romania)

- **Type:** community / angel syndicate portfolio
- **Geography:** Romania and South-Eastern Europe
- **Homepage:** https://techangels.ro/
- **List page:** https://techangels.ro/companies/
- **Publicly listed?** partial, deliberately so
- **Machine readable?** HTML cards (static) with sector tags, a
  **`first investment <year>`** field, and the **names of the backing angels** per row
- **Update cadence:** Opt-in. The page states "the directory grows as companies
  confirm their profiles", so it lags reality and undercounts badly.
- **Why it surfaces card candidates:** Romania is a TXN MVP market and angel rounds
  precede institutional rounds by 12-24 months, which is the earliest possible
  detection point. The listed backer names are also a warm-intro map. FilmChain is
  tagged `fintech, entertainment`. The honest caveat: only 7 companies are publicly
  confirmed against a claimed 270+ backed since 2013, so as a *list* it is thin.
  Its value is the named-angel graph, not the coverage.
- **Approximate list size:** 7 confirmed publicly; 270+ claimed
- **Confidence:** Verified
- **Evidence:** `curl` returned 54 KB and 2,262 characters. Rows: Anima Felix
  (healthtech, first investment 2024, backed by Marius Istrate, Felix Crișan, Sergiu
  Neguț, Ana Maria Andronic, Mihaela Matei), Bright Spaces (proptech, 2022),
  FilmChain (fintech, 2024), PROCESIO (2020), SalesOMMO (2024), SmartDreamers (2014),
  Veridion (2019). Note `techangels.ro/portfolio/` **404s** with a helpful migration
  notice; the correct path is `/companies/`.
- **Last checked:** 2026-08-25

### COBIN Angels (Poland)

- **Type:** community / angel syndicate portfolio
- **Geography:** Poland and CEE
- **Homepage:** https://www.cobinangels.com/
- **List page:** https://www.cobinangels.com/our-investments
- **Publicly listed?** partial
- **Machine readable?** HTML cards (static). **Descriptions render but company names
  do not**; names are carried in logo images.
- **Update cadence:** The homepage runs a dated Polish-language news feed
  ("Informator Anielski") with items through **5 August 2026**, which is a better
  monitoring surface than the investments page itself.
- **Why it surfaces card candidates:** The largest Polish business angel community,
  in a TXN MVP market, publishing annual market reports (2021-2025). Angel-stage
  companies are the deepest greenfield available. Caveat: the investments page as
  served requires OCR or image-alt parsing to recover names, and one visible holding
  is "Quantum computing software for the financial sector", so financial-services
  adjacency is present but the sample skews non-fintech.
- **Approximate list size:** ~10 cards rendered on the page
- **Confidence:** Verified
- **Evidence:** `curl` on `/our-investments` returned 123 KB and 2,958 characters of
  description-only text (e.g. "Loyalty and CRM platform for the hospitality and food
  industry", "Quantum computing software for the financial sector"). Note
  `cobinangels.com/en/` **404s**; the working paths are the bare domain and
  `/our-investments`.
- **Last checked:** 2026-08-25

### Angel Invest (Berlin)

- **Type:** VC portfolio (super-angel fund / rolling-fund model)
- **Geography:** Germany and Europe-wide
- **Homepage:** https://angelinvest.ventures/
- **List page:** https://angelinvest.ventures/portfolio
- **Publicly listed?** partial
- **Machine readable?** HTML cards (static) with **city, country and a one-line
  description per company, but company names largely absent from the text layer**
  (names are in logo images). Filters include an explicit **`Fintech`** tab.
- **Update cadence:** No date field. The fund states 75+ new investments per year,
  so the page changes constantly. High churn, which is good for discovery but means
  a diff must handle volume.
- **Why it surfaces card candidates:** Self-described as Europe's most active
  early-stage investor with 250+ portfolio companies and EUR 125k typical cheques,
  and it states AI, **fintech** and deep tech as focus areas. At EUR 125k first
  cheques these are the earliest-stage companies in this entire file. Germany is
  Opportunistic tier for TXN, which is the main knock against it.
- **Approximate list size:** 250+ claimed; a selection shown
- **Confidence:** Verified
- **Evidence:** `curl` returned 715 KB and 3,818 characters. Fintech-tagged
  descriptions read from markup: "Money, at Internet speed" (Berlin), "Finance for
  green hardware vendors" (Berlin), "Bling: Family fintech to understand, manage and
  grow money" (Berlin), "Financial operating system for healthcare". Only a handful
  of names (Bling) appear in text; the rest must be recovered from images.
- **Last checked:** 2026-08-25

### Superangel

- **Type:** VC portfolio (Baltic and Nordic early-stage)
- **Geography:** Estonia, Baltics, Nordics
- **Homepage:** https://superangel.io/
- **List page:** https://superangel.io/superangel-portfolio/
- **Publicly listed?** partial
- **Machine readable?** Mostly **JS-rendered**. Category tabs (`AI & Robotics`,
  `Data & Infrastructure`, `Deeptech & Science`, `SaaS`) render but the company grid
  does not appear in the served text.
- **Update cadence:** not determinable statically
- **Why it surfaces card candidates:** 100+ startups since 2012 across the Baltics.
  Notably, Superangel also publishes a separate **"Superangel 500" investor database**,
  a meta-source listing other investors, worth a look in its own right.
  Baltics are Opportunistic tier for TXN.
- **Approximate list size:** 100+ claimed; 0 rendered statically
- **Confidence:** Verified (that the grid does not render statically)
- **Evidence:** `curl` returned 66 KB of HTML with 1,113 characters of visible text:
  category tabs, three dated news blurbs (Kraken Technology / NATO, Labrys $20m,
  Pactum $20m) and a `SEE THE PORTFOLIO` call to action, but no company grid. Note
  `superangel.io/portfolio` **404s**; the real path is `/superangel-portfolio/`.
- **Last checked:** 2026-08-25

## F. Adjacent, meta and pre-seed sources

### Startup Wise Guys

- **Type:** accelerator / VC portfolio hybrid
- **Geography:** Estonia HQ, CEE, Baltics, Southern Europe, Africa
- **Homepage:** https://startupwiseguys.com/
- **List page:** https://startupwiseguys.com/portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with **status counts** (`Active 286`,
  `Active/Partial exit 4`, `Exit 23`) and **batch-level filters including five
  dedicated `Fintech` batches** (`Fintech 1` through `Fintech 5`, 3-7 companies each)
- **Update cadence:** Batch-driven. New cohorts append a new batch filter value, so
  a diff on the batch list detects a whole new cohort at once.
- **Why it surfaces card candidates:** Runs **named fintech accelerator batches** in
  CEE and the Baltics. An accelerator fintech cohort is the purest greenfield
  population available: companies at MVP stage, financial-services thesis, no card
  program, and the batch label tells you their vertical without any enrichment.
  Overlaps with the accelerator research stream but the portfolio page is a fund-side
  artefact worth listing here.
- **Approximate list size:** 450+ startups stated; 313 accounted for in the status
  counters
- **Confidence:** Verified
- **Evidence:** `curl` returned 1.35 MB and 47,603 characters. Batch filter values read
  from markup include `Fintech 1 (3)`, `Fintech 2 (4)`, `Fintech 3 (3)`,
  `Fintech 4 (7)`, `Fintech 5 (6)`, plus Cyber, SaaS, Growth and geographic batches.
  Vertical navigation lists `Fintech` as a named programme track.
- **Last checked:** 2026-08-25

### Practica Capital

- **Type:** VC portfolio
- **Geography:** Lithuania, Baltics
- **Homepage:** https://practica.vc/
- **List page:** https://practica.vc/en/investments
- **Publicly listed?** yes
- **Machine readable?** HTML list (static, **paginated** 1-5) with sector tags and a
  stage tag (`Seed`, `Early`, `Growth`) plus `Exited` status per row
- **Update cadence:** No date field. Pagination is stable, so a full crawl is 5
  requests.
- **Why it surfaces card candidates:** Baltic seed fund holding **AMLYZE** (tagged
  `RegTech`) and **HeavyFinance/Insoil**, financial-infrastructure companies.
  Baltics are Opportunistic tier, so treat as secondary. Included because the format
  is clean and the per-company URLs (`/en/investments/<slug>`) are predictable.
- **Approximate list size:** ~60 companies across 5 pages
- **Confidence:** Verified
- **Evidence:** `curl` returned 21.6 KB and 834 characters for page 1. Note
  `practica.vc/portfolio/` **404s**; the working path is `/en/investments`. Rows:
  AMLYZE (RegTech, Seed), Atrandi Biosciences (Early), Aurora Propulsion (Seed),
  Billo (Seed), CGTrader (Growth), Edurio (Seed).
- **Last checked:** 2026-08-25

### Change Ventures

- **Type:** VC portfolio
- **Geography:** Baltics (Estonia, Latvia, Lithuania)
- **Homepage:** https://www.changeventures.com/
- **List page:** https://www.changeventures.com/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML cards (static) with stage labels and slash-delimited
  sector tags (e.g. `Robotics / ClimateTech / B2B`)
- **Update cadence:** No date field.
- **Why it surfaces card candidates:** Baltic pre-seed and seed. Also publishes the
  **Baltic Startup Funding Report**, described on the page as "the only Baltic survey
  of investment transaction data with valuations". That report is arguably a better
  discovery artefact than the portfolio page itself, and is worth a separate fetch.
- **Approximate list size:** large (44,838 characters of extracted text)
- **Confidence:** Verified
- **Evidence:** `curl` returned 351 KB and 44,838 characters with per-company
  descriptions inline (e.g. Aerones, "world's leading robotic wind turbine blade
  inspection ... Latvian team graduated YCombinator").
- **Last checked:** 2026-08-25

### Eleven Ventures

- **Type:** VC portfolio
- **Geography:** Bulgaria and South-Eastern Europe
- **Homepage:** https://www.11.vc/
- **List page:** https://www.11.vc/portfolio-companies/
- **Publicly listed?** yes
- **Machine readable?** HTML (static, WordPress). 10.7k characters served, but the
  opening of the page is testimonial content and the company grid appears further
  down, so parse the whole document rather than the first screen.
- **Update cadence:** No date field.
- **Why it surfaces card candidates:** Backed **Payhawk** (Bulgarian spend-management
  and corporate cards) pre-product, which is direct proof this fund catches
  card-adjacent companies at their earliest stage. 150+ portfolio companies across
  SEE, a region the fintech press underweights. Bulgaria is not an MVP market but is
  in the wider EEA opportunistic tier.
- **Approximate list size:** 150+ reported
- **Confidence:** Verified
- **Evidence:** `curl` returned 441 KB and 10,723 characters. The correct domain is
  `11.vc`, not `eleven.vc` (which failed to connect). Named companies visible:
  Enhancv, SMSBump, Nitropack.
- **Last checked:** 2026-08-25

### Vestbee VC list

- **Type:** register / meta-directory
- **Geography:** CEE, Baltics, Europe
- **Homepage:** https://www.vestbee.com/
- **List page:** https://www.vestbee.com/vc-list
- **Publicly listed?** yes
- **Machine readable?** HTML with a **country-level HQ filter** exposing the full
  country vocabulary (Poland, Czech Republic, Hungary, Bulgaria, Estonia and 100+
  others) plus CEE/Baltics/Balkans/DACH regional groupings
- **Update cadence:** Continuously maintained as a commercial directory. Vestbee also
  publishes quarterly "VC funding in CEE" reports and monthly "Top CEE funding rounds"
  articles, both dated, structured secondary feeds.
- **Why it surfaces card candidates:** This is the **meta-source that generates the
  rest of this file**. Rather than TXN maintaining a hand-curated list of CEE funds,
  filter Vestbee by HQ = Poland/Czechia/Hungary/Romania, extract the fund list, then
  crawl each fund's own portfolio page. It also carries separate Accelerator and
  Startup directories and a business-angel-syndicate article that named COBIN Angels,
  SMOK Angels, Vestbee Angels (PL), TechAngels and Transylvania Angels Network (RO),
  HunBAN (HU), EstBAN/LatBAN/LitBAN and CBAN.
- **Approximate list size:** unknown (directory; some content behind a join wall)
- **Confidence:** Verified
- **Evidence:** `curl` returned 589 KB and 8,759 characters with the full filter
  taxonomy in the markup. The angel-syndicate article at
  `/insights/articles/business-angel-syndicates-in-europe` was separately fetched and
  read; it names the networks above but does **not** state whether any publish
  holdings, so syndicate-level portfolio availability had to be checked individually
  (see COBIN and TechAngels entries).
- **Last checked:** 2026-08-25

### SeedBlink

- **Type:** other (equity crowdfunding / syndicate execution platform)
- **Geography:** Romania HQ, pan-European
- **Homepage:** https://seedblink.com/
- **List page:** company profiles behind the platform ("Explore 100+ company
  profiles"); the public marketing site does not serve a flat list
- **Publicly listed?** partial
- **Machine readable?** HTML (static marketing shell). The deal and company data sits
  behind platform navigation and likely requires an account.
- **Update cadence:** Deal-driven and continuous by nature. This is a live
  fundraising marketplace, so a company appears here *while* it is raising, which is
  earlier than a portfolio page.
- **Why it surfaces card candidates:** Structurally the earliest signal in this file.
  A company raising on SeedBlink is mid-round, not post-round. Romanian-founded with
  strong CEE deal flow, and SeedBlink is itself a Catalyst Romania portfolio company.
  The catch: it is a platform, not a fund, so access terms need checking before
  building on it.
- **Approximate list size:** 100+ company profiles stated
- **Confidence:** Verified (homepage fetched and read) / Unverified (whether the
  company list is accessible without an account)
- **Evidence:** `curl` returned 192 KB and 13,772 characters of marketing navigation:
  "Build Your Pipeline, Explore 100+ company profiles, connect with founders",
  syndicate lead tooling, secondaries. No flat company list served publicly.
- **Last checked:** 2026-08-25

### Allianz X

- **Type:** VC portfolio (insurer corporate venture arm)
- **Geography:** Europe and global
- **Homepage:** https://allianzx.com/
- **List page:** `/our-companies` **404s**. The company list is rendered in the
  **site-wide footer/sitemap block**, which is served on every page including the
  404 page.
- **Publicly listed?** yes (by accident of template design)
- **Machine readable?** HTML links (static). The full name list is in the footer.
- **Update cadence:** No dates. Footer list changes when the site is redeployed.
- **Why it surfaces card candidates:** Insurer CVC with fintech and neobank exposure
  (N26, Wealthsimple, Fundbox, C2FO, Ualá, stripe, Clark). Germany-based, so
  Opportunistic tier for TXN. Included mainly as a **scraping technique note**: when
  a fund's portfolio route 404s, check the footer before concluding the list is
  unavailable.
- **Approximate list size:** ~38 companies in the footer list
- **Confidence:** Verified
- **Evidence:** `curl` on `allianzx.com/portfolio` and `allianzx.com/our-companies`
  both returned the 404 template (33 KB, 1,773 characters) whose footer nonetheless
  enumerated: ControlExpert, HeavenHR, Lemonade, N26, Nauto, Pie Insurance, SafeBoda,
  SDA SE, simplesurance, Urgent.ly, Wealthsimple, GT Motive, 1Qbit, 99co, American
  Well, OpenGamma, heycar, ESG Book, Coalition, Innovation Group, stripe, Purpose
  Unlimited, GoTo, C2FO, WeLab, BIMA, Wayhome, NEXT Insurance, Clark, AlTi, SandboxAQ,
  Fundbox, halodoc, Finanzen.de, Ualá, Openly, Coterie, Cambridge Mobile Telematics,
  EthiFinance.
- **Last checked:** 2026-08-25

### Antler

- **Type:** VC portfolio (global pre-seed / company builder, incl. Continental Europe)
- **Geography:** Global; Europe split into UK, Continental Europe and Nordics
- **Homepage:** https://www.antler.co/
- **List page:** https://www.antler.co/portfolio (accepts
  `?location=Continental+Europe`)
- **Publicly listed?** partial
- **Machine readable?** **JS-rendered for the company grid.** 11.5k characters served
  but they are navigation, location menus and resource links; no company names appear
  in the text layer, and the `?location=` query string returns byte-identical HTML
  (254,212 bytes both times), confirming filtering is entirely client-side.
- **Update cadence:** Cohort-driven. The site publishes a "Cohort Start dates" page,
  which is a dated forward-looking calendar and arguably more useful than the
  portfolio grid.
- **Why it surfaces card candidates:** Antler invests at day zero across Continental
  Europe including CEE. Cohort-based, so new companies arrive in waves on a published
  schedule. Requires a headless browser to extract.
- **Approximate list size:** large; 0 rendered statically
- **Confidence:** Verified (that the grid does not render statically, and that the
  location filter is client-side)
- **Evidence:** `curl` of both `/portfolio` and `/portfolio?location=Continental+Europe`
  returned identical 254,212-byte responses with 11,517 characters of nav-only text.
- **Last checked:** 2026-08-25

## G. Verified dead ends and broken pages

Recorded because "defunct is a finding" and because each one saves the next person
a wasted fetch.

### Tera Ventures: site compromised

- **Type:** VC portfolio (Estonian early-stage)
- **Geography:** Estonia, Baltics
- **Homepage:** https://www.tera.vc/
- **List page:** https://www.tera.vc/portfolio (**404**)
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** n/a
- **Why it surfaces card candidates:** It does not. The 404 page is not a normal 404.
  It serves a large block of SEO-spam link text ("Hacklink panel", "Hacklink satın
  al", "Backlink paketleri", Turkish-language spam). The site appears **compromised
  or abandoned to link injection**. Do not scrape it, do not follow links from it,
  and treat any Tera Ventures data sourced from the live site as untrustworthy.
- **Approximate list size:** n/a
- **Confidence:** Verified
- **Evidence:** `curl` returned 44 KB and 2,713 characters consisting almost entirely
  of repeated "Hacklink panel" spam anchors under a "Page not found : Tera Ventures"
  title.
- **Last checked:** 2026-08-25

### Enern: domain gone

- **Type:** VC portfolio (was a Prague/CEE fund)
- **Geography:** Czech Republic, CEE
- **Homepage:** https://www.enern.com/ (**redirects off-domain**)
- **List page:** none
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** n/a
- **Why it surfaces card candidates:** It does not any more. `enern.com` now redirects
  to `oppdal.com`, a Norwegian tourism site (`Visit Oppdal`), returning a
  Norwegian-language 404. The domain has changed hands. Any stored reference to
  `enern.com` in TXN's corpus is stale and should be purged. The fund itself may
  still operate under another domain. **Not verified.**
- **Approximate list size:** n/a
- **Confidence:** Verified (that the domain no longer serves the fund)
- **Evidence:** `curl` on `https://www.enern.com/` resolved to
  `https://oppdal.com/utforsk/enern-er-avviklet/` and returned "Page not found: Visit
  Oppdal". The Norwegian slug `enern-er-avviklet` translates as "enern has been wound
  up", which is suggestive but is a slug on an unrelated site, not evidence about the
  fund.
- **Last checked:** 2026-08-25

### Catalyst Romania: portfolio page is unfinished template content

- **Type:** VC portfolio (Romanian early-growth, EUR 50m Fund II)
- **Geography:** Romania, CEE
- **Homepage:** https://catalystromania.com/
- **List page:** https://catalystromania.com/portfolio/
- **Publicly listed?** no, in practice
- **Machine readable?** HTML (static) but the **content is placeholder text**
- **Update cadence:** Newest dated portfolio item is **27 Jul 2022**; most entries are
  dated Nov-Dec 2019. Effectively unmaintained.
- **Why it surfaces card candidates:** Catalyst Romania is a real, active fund in a
  TXN MVP market (portfolio reportedly includes SeedBlink, SmartBill, .lumen, Carfix,
  Footprints AI), but its published portfolio page **cannot be used as a source**.
  The entries carry Latin lorem ipsum body text ("At vero eos et accusamus et iusto
  odio...") and generic titles like "123 FORM BUILDER", "Digital Analysis" and
  "Business Growth" mixed with real names (Elefant.ro, Avocatnet). Note the domain:
  `catalyst-romania.com` with a hyphen **does not resolve**; the live site is
  `catalystromania.com`.
- **Approximate list size:** ~10 entries, most of them placeholders
- **Confidence:** Verified
- **Evidence:** `curl` returned 414 KB and 5,314 characters. Verbatim from the markup:
  "Portfolio Look how wonderful work we have done! At vero eos et accusamus et iusto
  odio digni goiku ssimos ducimus qui blanditiis praese." repeated across entries.
- **Last checked:** 2026-08-25

### SMOK Ventures: template not rendering server-side

- **Type:** VC portfolio (Warsaw, US-Polish, pre-seed and seed)
- **Geography:** Poland, CEE
- **Homepage:** https://www.smok.vc/
- **List page:** https://www.smok.vc/portfolio/
- **Publicly listed?** no (client-side only)
- **Machine readable?** **JS-rendered.** The served HTML contains raw, unevaluated
  Vue.js template syntax.
- **Update cadence:** The blog is the usable dated surface: "Why We Invested in
  intoDNA" (Jan 2026), "Why We Invested In Juo" (Jun 2025), plus a monthly archive
  dropdown and an `Investments (12)` category count. Tag cloud includes `fintech`,
  `payments` and `KYC`.
- **Why it surfaces card candidates:** Poland is a TXN MVP market and SMOK is one of
  the most active Polish pre-seed funds (47 investments reported, 23 Poland-HQ). The
  portfolio page is unusable statically, but the **blog category `Investments` plus
  the `payments`, `fintech` and `KYC` tags is a perfectly good substitute feed** and
  is dated. Also note SMOK runs "SMOK Angels", a 220+ member operator syndicate, but
  `smok.vc/angel-network/` **404s**, so that roster was not located.
- **Approximate list size:** 47 investments reported; 0 rendered statically
- **Confidence:** Verified
- **Evidence:** `curl` returned 53 KB and 1,219 characters including literal
  `{{item.title}}`, `#{{tag.name}}` and `v-for="item in portfolio"` in the output,
  i.e. the Vue template ships to the browser unrendered.
- **Last checked:** 2026-08-25

### Presto Ventures, Cogito Capital and LAUNCHub: empty SPA shells

- **Type:** VC portfolio (Presto: Czech; Cogito: Polish/CEE Series A+, EUR 125m
  Fund II reported; LAUNCHub: Bulgarian/SEE seed, EUR 74m, 90+ companies)
- **Geography:** Czech Republic, Poland, Bulgaria, wider CEE and SEE
- **Homepage:** https://presto.vc/ , https://cogitocapital.com/ , https://launchub.com/
- **List page:** https://presto.vc/portfolio , https://cogitocapital.com/portfolio ,
  https://launchub.com/portfolio
- **Publicly listed?** no (client-side only)
- **Machine readable?** **JS-rendered.** Presto and Cogito each return exactly 114
  bytes and zero text. LAUNCHub returns a 4,551-byte shell with 81 characters of nav
  text (`Portfolio Team Co-Investors Field Notes`) and no companies.
- **Update cadence:** not determinable statically
- **Why it surfaces card candidates:** All three are meaningful CEE funds in or
  adjacent to TXN MVP markets. Cogito explicitly targets Poland, Czechia, Slovakia,
  Hungary, Romania and the Baltics at Series A+ with an enterprise-software and
  fintech remit. All three are invisible to a static scraper. Grouped here so they
  are not silently dropped: they belong on the headless-browser list, not the discard
  pile.
- **Approximate list size:** unknown for Presto and Cogito; 90+ reported for LAUNCHub
- **Confidence:** Verified (that all three serve empty shells)
- **Evidence:** `curl` on each returned the byte counts above with no company names.
  Note `launchub.vc` does not connect; the live domain is `launchub.com`.
- **Last checked:** 2026-08-25

---

## Operational notes for whoever builds the crawler

1. **Guessed URLs fail often enough to matter.** In this pass the obvious
   `/portfolio` path was wrong for Movens (`/our-portfolio/`), Portfolion
   (`/companies/`), Innova (`/our-investments/portfolio/`), Practica
   (`/en/investments`), Superangel (`/superangel-portfolio/`), TechAngels
   (`/companies/`), Eleven (`11.vc/portfolio-companies/`) and Abris (`/investment/`).
   Extracting `href` values from the homepage and filtering for
   `portfolio|companies|investments` resolved every one of them. Do that first.

2. **Guessed domains fail too.** `illuminate.financial`, `smokvc.com`,
   `catalyst-romania.com`, `depo.ventures` and `eleven.vc` do not resolve;
   `launchub.vc`, `www.otbvc.com`, `genesiscapital.cz` and `genesiscapital.eu` do not
   connect. Always search for the domain before fetching it.

3. **WebFetch can be wrong about JS-rendering.** It reported Credo Ventures'
   portfolio as empty or JS-rendered; raw `curl` showed 2.3 MB of HTML with every
   company name inline. On logo-heavy pages, verify with raw bytes before writing off
   a source.

4. **Watch for duplicate blocks.** Underline repeats each company three times for
   hover states, and Target Global ships a repeated `Rapyd` placeholder block.
   Dedupe on company name or the crawl will over-report.

5. **The date field is the whole game.** Prioritise Motive Partners, Seedcamp,
   Market One Capital, Underline, Inovo, Movens, Hiventures and OTB. Every one of
   them exposes a per-company date or year in the served HTML, which turns a weekly
   crawl into a genuine new-deal feed rather than a full-list diff.
