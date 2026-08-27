---
description: "Validated discovery sources for the greenfield segment: what survived adversarial checking, coverage by market, build requirements, and the miss-rate metric"
---

# Discovery Sources

Findings from the source research commissioned in the 25 August 2026 ICP interview, after adversarial validation. Routed from [[outbound]].

The working corpus this synthesises is held at [[research]]: all eight streams, all 299 source entries with the URL fetched and the evidence returned, and the seven independent validation reports that produced the corrections below. The client-facing version is the register at `research/txn-discovery-source-register.html`.

## The problem this addresses

TXN's prospecting corpus discovers companies through sources that observe **existing** card programs: registers of authorised entities, competitor case studies, scheme partner directories, fintech news. Ian's stated priority is the opposite segment, companies that have never launched a card program.

[[qualification-matrix]] shows the consequence: 126 accounts, 32 greenfield, holding 2 of the 22 Priority 1 places.

The organising insight from the research: **a company that has never issued a card emits no card signals.** Every source that worked finds companies doing something else, hiring, taking money, registering to recruit, filing for a legal status, entering a pitch competition. None of them is a card signal.

## Method and trustworthiness

Seven research streams, then seven independent validators told to attack the findings rather than confirm them. Roughly 254 source entries produced; every validator re-fetched claims with a different toolchain.

**No fabricated source was found in any stream.** The total fabrication yield across all seven checks was two company names attributed to lists they were not on. Validators confirmed the improbable details that would be easiest to invent: a leading space inside a JSON payload, byte counts matching to the digit, a fund's site serving link spam, another's portfolio page filled with mangled lorem ipsum.

Three systematic defects were found, all of which distort a real thing rather than conjure one:

| Defect | Example |
|--------|---------|
| **Counts estimated where counting was possible, usually high** | InnovX 400 to 287 · Rubik Hub 600 to 249 · Spain 2,394 to 1,960 · Czech Fintech Association 18 to 67 (that one low) |
| **Sources written off as blocked that were not** | Ten recovered, including NoFluffJobs, eJobs.ro, TMview, Sifted, three of five claimed 403 walls |
| **`Verified` applied per entry rather than per claim** | Five entries carried a memory-sourced sentence inside a verified stamp |

Treat entry counts as approximate until re-counted, and treat "blocked" as unproven unless `curl` with a browser user agent was tried.

## The strongest sources, validated

### Government and statutory registers

The best category found, and almost certainly unprospected. Free, official, structured, and defined by company age rather than sector.

| Source | Market | What it gives | State |
|--------|--------|---------------|-------|
| **Elevate Greece** | Greece, Phase 1a | 1,085 accredited startups in one unauthenticated POST (2.1 MB JSON) with industry, headcount, funding, region and website per company. **44 FinTech, 10 InsurTech, 9 LegalTech/RegTech** | Validated |
| **dados.gov.pt startup register** | Portugal, Phase 1a | 654 companies holding legal Startup/ScaleUp status under Law 21/2023, as JSON, with tax number, legal name and **date recognition was granted**. 143 granted in 2026. Refreshed the morning of the pass | Validated. No sector field, needs enrichment |
| **ENISA empresa emergente** | Spain, Phase 1a | **1,960 certifications in force** (2,415 issued). Named legal-entity table with tax number, company name, province and certification dates | Validated |
| **mapadotacji.gov.pl** | Poland, MVP | EU grant register filtered to the "Platformy startowe" programme returns **774 projects** with a beneficiary-name column | Validated |
| **Registro Imprese startup innovative** | Italy | 11,544 companies claimed, weekly refresh | **Gated.** The download path is an email request form with a reCAPTCHA challenge, not a file. Contents unverified |

**Correction on Spain.** This was initially described as greenfield "by construction". It is not. The criterion is *"antigüedad máxima de cinco o siete años desde su constitución"*, five **or** seven years by sector, and it is one of seven conditions. Nothing in the statute excludes a company that already runs a card programme. Greenfield by correlation.

### Hiring signals

The earliest credible signal identified, and the one that reaches non-financial companies.

- **Ashby** and **Greenhouse** both expose every customer's job board as unauthenticated JSON. Ashby carries `department` and `team` on 100% of records, so **a payments department being created** is detectable, not merely a role being filled.
- **NoFluffJobs** has a public unauthenticated API returning 20,889 postings with employer, title, category, seniority and salary band. Poland, an MVP market.
- Working per-market boards: justjoin.it (Poland), StartupJobs.cz, Profession.hu, eJobs.ro. **Profesia.sk has no industry filter**, recorded as a negative.

### Scheme and network

- **Visa Innovation Program Europe** publishes its full participant roster as an **open unauthenticated JSON API**: 154 fintechs, 2019 to 2026, each tagged with country, vertical and cohort year. Validated to the digit, including a 2026 cohort of exactly 22. Coverage is Phase 1a shaped: Greece/Cyprus/Malta 45, Türkiye 39, Spain/Portugal 34, Bulgaria 19, Italy 16.
- **Mastercard Lighthouse** runs on WordPress with an open REST API exposing 136 posts, naming its Nordic and Baltic cohorts.
- **Mastercard Start Path publishes nothing.** 500+ startups claimed, zero named, confirmed on adversarial retry.
- **BIN sponsors publish curated case studies, not client lists.** The leading signal is a sponsor's **news page**, where counterparties are named at signature. Only 2 of 14 sponsor sites had working RSS, so this needs HTML polling.

### Accelerators and venture builders

| Source | Market | Detail |
|--------|--------|--------|
| **start it @ČSOB** | Czech, MVP | Unauthenticated JSON API returns the full **132-company corpus with 130 URLs in one request** |
| **Rubik Hub** | Romania, MVP | 249 cards with FinTech and country filters, programme and cohort per entry. **Only yields to a browser user agent** |
| **InnovX-BCR** | Romania, MVP | 287 alumni, fintech-filterable |
| **MBH FinTechLab** | Hungary, MVP | ~26 companies with descriptions, dense with factoring, embedded finance and BNPL |
| **JIC** | Czech, MVP | 295 clients with a public one-click Excel export |
| **Nápad roku** | Czech, MVP | 18 years of published cohorts, 2,652 projects. Appears on no accelerator list |
| **Techstars, ABN AMRO Future of Finance** | Netherlands, Phase 1b | Fintech-only, 6th edition, every cohort named in a fetchable newsroom post. Best single-fit accelerator found |
| **Start it @KBC** | Belgium, Phase 1b | 1,700+ startups, server-rendered, Fintech/Insurtech/KYC-AML tags |
| **Startup Wise Guys** | CEE/Baltic | 50 fintech companies. Only 13 across the four MVP markets |

**Dead, with evidence:** mBank's mAccelerator, Alior's RBL_START, Design Terminal (absorbed into Civitta, alumni corpus gone), ITACA, Google Campus Warsaw, Barclays Rise, finleap, RBI's Elevator Lab accelerator, weXelerate, CaixaBank DayOne.

**Two vehicles, easily confused:** Raiffeisen's **Elevator Lab** accelerator ended in 2022. **Elevator Ventures**, the bank's VC arm, is live with 22 portfolio companies, but targets Series A and B, so it catches companies later than this segment. The unhyphenated domain is a parking page.

### Investor portfolios as a new-deal feed

**Eight funds expose a per-company investment date in served HTML**, confirmed on all eight: Motive, Seedcamp (550+ companies, literal `Year of Investment` column), Market One Capital, Inovo, Movens, Hiventures, OTB, Underline. That turns a crawl into a genuine new-deal feed rather than a full-list diff.

**Market One Capital** is the best fringe population found: a Warsaw marketplace fund with **exactly 46 companies of which exactly 5 are tagged FinTech**. The other 41 sit in logistics, travel, healthtech, agritech and mobility, invisible to any fintech filter while being exactly the companies that grow into card programs.

**Advent's `Carve-out` deal filter** is a trigger with a published list attached: a carved-out unit loses its parent's payment infrastructure.

### Awards, pitch shortlists and media

Exhibitor lists are mostly gated or resold. **Pitch shortlists and awards shortlists are the reliable artefact**, published by name in plain HTML weeks ahead because the organiser wants the coverage.

- **Romania Startup Awards**: ~157 Romanian and Moldovan startups on one free page with a FinTech category
- **Money Motion (Zagreb)**: the finalists page **accretes rather than resets**, holding 61 unique companies across four cohorts
- **South Summit Madrid**: 100 finalists, 10 verticals including Fintech and Insurtech, from 4,500+ applications
- **Deloitte Technology Fast 50 Central Europe**: four lists a year including a younger "Companies to Watch" tier. **Covers nine countries and Hungary is not one of them**
- **Sifted**: `sifted.eu/feed` is an open RSS feed, no auth, rebuilt daily. Article bodies remain paywalled. Same for EU-Startups
- **The Hub**: 11,113 Nordic startups, **1,005 tagged Fintech**, with a live "looking for funding" flag. Companies register in order to hire, so they appear before any funding database
- Local-language recurring lists: The Recursive (CEE weekly), Vestbee (CEE monthly), Swedish Tech Weekly (~120 enumerable issues), CzechCrunch, Cashless.pl (Polish fintech map, 383 companies), MamStartup.pl

### Associations with open member lists

Czech Fintech Association (~67 members: 55 full, 12 associate), The Payments Association (366 via open API), FinTech Belgium (Squarespace, so `?format=json` and `?format=rss` both work), Holland FinTech, RoFintech (~45, and it publishes a list of peer associations across Europe, which is a ready-made partnership map), EMA (~100 named EMIs, useful for confirming a sponsor is still authorised).

## Coverage by market, and an awkward finding

| Market | Phase | Coverage |
|--------|-------|----------|
| Greece | 1a | **Strong.** 1,085-company government API, plus heavy Visa Innovation Program presence |
| Spain | 1a | **Strong.** 1,960 certified companies with named legal entities |
| Portugal | 1a | **Strong.** 654-company open-data register with grant dates |
| Czech Republic | **MVP** | Good. ČSOB API, JIC export, Nápad roku, 67-member association |
| Romania | **MVP** | Good. Rubik Hub, InnovX, ROTSA, working job board |
| Poland | **MVP** | Moderate. 774 grant projects, NoFluffJobs API, justjoin.it. **Both bank accelerators dead**, PKO's 6,000-company funnel publishes four logos |
| Hungary | **MVP** | **Weakest.** MBH FinTechLab is close to the only thing standing. No recurring list source, no scheme programme, Design Terminal's corpus gone, excluded from Deloitte Fast 50 CE |
| Netherlands | 1b | Moderate. Techstars ABN AMRO is strong, but Techleap publishes no company database |

**The awkward part: the three Phase 1a markets are now better covered than three of the four MVP markets.** Southern Europe has national statutory registers and the Visa programme; CEE relies on scattered accelerators and one grant register. That is a finding about source availability, not about market attractiveness, and the phasing is Ian's call. But it is worth knowing that discovery in Greece, Spain and Portugal is currently cheaper and more complete than in Poland or Hungary.

## Build requirements this establishes

1. **A headless-browser tier is a precondition, not an optimisation.** Roughly a third of fund portfolio pages serve almost no HTML: three returned exactly 114 bytes each, others ship unrendered template placeholders. Rubik Hub, Sifted and PFR Ventures only yield to a browser session.
2. **`curl` with a browser user agent must be tried before a source is called blocked.** Ten sources were recovered this way. A fetch-tool 403 is not evidence of a wall.
3. **An empty JavaScript shell is not a 404.** Portugal Fintech's live 2025 microsite was written off this way.
4. **The rendered page can be more authoritative than the API.** The Czech Fintech Association's own endpoint returns a stale 18-member fragment while the page lists 67.

## The measure that makes this testable

Ian, 25-08:

> *"We're not going to win every deal, and if we lose because people have decided they want to go with somebody else, that's fine. But losing because you didn't know that a deal was on the street, that is the bit that in this age should never happen."*

Every source list is a guess at coverage. **Measure the miss rate instead.** Each time one of the named incumbents announces a client, check whether that company was already in the register. If not, log the company, the date, which scan should have caught it, and why it did not.

Over a quarter that produces a factual answer to "what are we missing", broken down by the source that failed. It costs nothing, since competitor announcements are already read for the contract-expiry trigger, and it should be the primary Phase A quality measure ahead of reply rate. Reply rate says whether the message works; miss rate says whether the engine works.

## Open decisions

| Decision | Note | Owner |
|----------|------|-------|
| Submit the Italian register's email request form | It mails from a government system, so it is a human action, not an agent one. Unlocks 11,544 companies if the file is what the page implies | Ian |
| Pursue Visa Fintech Fast Track enablement-partner status | Not a source. Visa's published eligibility is *"Not an existing Visa member"*, *"New to card issuance"*, *"raised at least $3M"*, and it undertakes to route applicants to processors. Verified verbatim. Borrowed credibility from the network rather than from the JV | Ian |
| Whether Route becomes a derived field on the account record | Already implicit in the Incumbent Processor column. See [[qualification-matrix]] | Ian |
| Attempt budget by route | Ian's own sequencing rule: do not spend all six attempts early on accounts unlikely to consider TXN yet | Both |

## Still open

Greek bank accelerators (Eurobank's egg domain is for sale, NBG paths 404) need a manual browser check, and Greece is Phase 1a. Barclays Eagle Labs publishes a directory of 4,610 founder profiles gated to attested investors, which is an access question. Sifted's article bodies remain paywalled. Hungary needs a dedicated pass. The class-36 trademark signal is now buildable, the TMview API having returned 2,926 results with the required fields, but no lead-time figure anywhere in this work has been measured.
