---
description: "Stream 06 raw research: 42 pitch shortlist, awards, recurring media list and association member list sources"
---

> **Section:** [[research]]
> **Validation:** [[validation-06-events-media-communities]]
> **Status:** raw research output, recorded verbatim. Read the validation report alongside it: several counts in this file were corrected.

# Stream 06: Events, exhibitor and pitch lists, media watch lists, founder communities

Owner: events / media / communities stream
Research pass date: 2026-08-25

## Summary

44 sources examined, 33 recorded below as full entries plus a rejected/low-value
list at the end. The stream was asked for three things and they behave very
differently:

**1. Event lists.** The reliable pattern in Europe is not the exhibitor list, it
is the **pitch competition shortlist**. Exhibitor lists are mostly gated,
JS-rendered or sold as lead lists by third parties. Pitch shortlists are
published by name, in plain HTML, 3 to 8 weeks before the event, because the
organiser wants the PR. The highest-yield examples found and fetched:

- **Money Motion (Zagreb)** publishes every finalist cohort back to 2023 on one
  page: 19 + 20 + 15 + 10 named companies. Largest CEE fintech event, and the
  only fintech-specific one in this stream with a durable public list URL.
- **South Summit Madrid** publishes all 100 finalists, grouped into 10 verticals
  including a named Fintech & Insurtech vertical, from 4,500 applications.
- **Latitude59 (Tallinn)** publishes its TOP15 with country tags.
- **Infoshare (Gdańsk)** publishes 20 semifinalists and 5 finalists by name.

**2. Awards shortlists are the underexploited asset.** The single best CEE find
in this stream is the **Romania Startup Awards** run by ROTSA: 150+ Romanian and
Moldovan startups named in one page, split into "Best Innovators" (early stage)
and "Best Performers", with a dedicated FinTech & InsurTech Innovator category.
That is a greenfield-heavy list for a TXN MVP market, published annually, free,
and almost certainly not in anyone's prospecting corpus. **Cashless.pl's Mapa
polskiego fintechu** (383 companies, 9th edition, June 2026) is the Polish
equivalent. **Deloitte Technology Fast 50 Central Europe** covers 9 countries
including all four MVP markets and has an explicit fintech-flavoured "Impact
Stars" category.

**3. Sifted-shaped media exist outside English.** Confirmed recurring,
company-naming, one-paragraph-per-company formats:

- **The Recursive** "CEE Startup & Tech Weekly" (~10 companies/week, SEE + CEE)
- **Vestbee** "Top CEE funding rounds closed in <month>" (~11 companies/month)
- **Swedish Tech Weekly** (~25-30 companies/week, Monday, free tier)
- **CzechCrunch CC25** (25 Czech companies/year) plus a monthly startup newsletter
- **StartupCafe.ro** (annual 26-company Romanian watch list)
- **MamStartup.pl** (Polish, 10-company watch lists)

**4. Communities need a partnership, and two of them publish member lists
anyway.** The Czech Fintech Association (~85 members) and RoFintech (64
members) both publish complete, linked, plain-HTML member directories. Those
are free lists of Czech and Romanian fintech companies, no partnership needed.
Copenhagen Fintech, Female Founders and Startup Grind do not publish rosters
and would need an actual relationship.

### What I could NOT verify

Recorded honestly. All of these were attempted during this pass and failed.

| Source | What happened |
|---|---|
| **Sifted** (sifted.eu) | HTTP 403 to WebFetch and to curl with a browser UA. The leaderboard structure below is from search-result snippets only, not a fetched page. This is the client's own named reference source and it is the one I could not open. Needs a browser session or a subscription. |
| **EU-Startups** (eu-startups.com) | HTTP 403 to WebFetch and curl on both `/directory/` and an article URL. Weekly funding round-up and directory recorded as Unverified. |
| **StartupItalia** (startupitalia.eu) | HTTP 403 on the SIOS 100 list page. |
| **FinTech Futures / PayTech Awards** (fintechfutures.com) | Cloudflare challenge block on both WebFetch and curl. Shortlist confirmed to exist via three independent finalist press releases, but I never read the shortlist page. |
| **MPE Berlin** (merchantpaymentsecosystem.com) | HTTP 403 on the Innovation Hub page. Details taken from a third-party events site plus search snippets. |
| **Impact CEE** (impactcee.com) | HTTP 403 on both `/` and `/impact/2026`. |
| **4YFN Barcelona** (4yfn.com/exhibitors) | Page is JS-rendered. Static HTML contained metadata and a newsletter modal only, zero company names. |
| **ROTSA** (rotsa.ro) | HTTP 403 on the association's own startup list page. The Romania Startup Awards nominee list was verified via StartupCafe.ro instead, which named the companies in full. |
| **Forbes Hungary** "A legforróbb magyar startupok" | Fetched, returned title only, no list content. Hungary is the weakest-covered MVP market in this stream. |
| **Wolves Summit startup roster** | Homepage fetched successfully (curl 200) and confirms the event, but the historic startup list subdomains (warsaw./wroclaw.wolvessummit.com) do not resolve. No public startup roster found. |
| **FinovateEurope 2026 full demo lineup** | The Finovate blog post I fetched named zero companies. The 17 names below come from a search snippet of a Business Wire release whose direct fetch timed out. Marked Reported. |
| **Doers Summit / Reflect Festival** (Cyprus) | reflectfest.com 301s to doerssummit.com; that homepage returned near-empty content. Details are search-snippet only. |
| **Startup Grind chapters** | Chapters directory page returned a gateway page with no chapter data. |
| **Web search budget** | The session's 200-search budget was exhausted before I could cover Portugal, Greece, Spain and Norway/Denmark national-language media. Those are named as gaps, not as entries. |

### Known gaps, not attempted or not found

- **Hungary** has no verified recurring startup list source in this file. This is a
  real hole given Hungary is an MVP market. Forbes.hu and fintech.hu both look
  like the right shape and neither could be confirmed.
- **Portugal, Greece, Spain** national-language watch lists: search budget ran out.
- **Norway (Shifter.no), Denmark, Finland** national outlets: identified as
  existing via a secondary source, never fetched, so not recorded as entries.
- **Podcasts and demo-day streams**: weak return. therecursive.com/podcast/ 404s,
  paymentandbanking.com/fintech-des-jahres/ 404s. The only verified
  podcast-adjacent source is Payment & Banking's show list on its homepage.
  Treat this sub-brief as unfulfilled.

---

## A. Events with published startup, pitch or exhibitor lists

### Money Motion (Zagreb)

- **Type:** event
- **Geography:** Croatia, CEE-wide draw
- **Homepage:** https://www.money-motion.eu/
- **List page:** https://www.money-motion.eu/startups/
- **Publicly listed?** yes
- **Machine readable?** HTML cards
- **Update cadence:** Annual. The startups page carries every finalist cohort as a
  separate block, so the page accretes rather than resets: 19 finalists for
  MoMo2026, 20 for 2025, 15 for 2024, 10 for 2023.
- **Why it surfaces card candidates:** Self-describes as the largest CEE fintech
  conference. The pitch cohort is early-stage by construction and skews to
  companies from Croatia, Slovakia, Ukraine and the wider region, i.e. exactly
  the CEE greenfield band. Named finalists seen on the page include Coverally
  (Slovakia), UNYX AI (UK), Creagen (Ukraine), Alerts Bar (US).
- **Approximate list size:** 19 current, 64 cumulative across four editions
- **Confidence:** Verified
- **Evidence:** Fetched /startups/ and read the finalist blocks; fetched the
  homepage which confirms next edition 10-11 March 2027 at Zagreb Fair, ~2,000m²
  expo, 3,000 attendees, and links to the same /startups/ page. Caveat: the
  startups page still carries a stale line "Applications closed January 28th,
  2025", so the application window text on that page is not reliable.
- **Last checked:** 2026-08-25

### How to Web: Spotlight (Bucharest)

- **Type:** event
- **Geography:** Romania, Eastern Europe
- **Homepage:** https://www.howtoweb.co/
- **List page:** https://www.howtoweb.co/spotlight-2026/
- **Publicly listed?** partial
- **Machine readable?** HTML cards
- **Update cadence:** Annual. Selection announced 21 September 2026; applications
  ran 1 May to 11 September 2026; dry-run pitch 6 October, semifinal and final
  7 October, mentoring 8 October.
- **Why it surfaces card candidates:** 20 early-stage Eastern European startups,
  vetted, dated, in a TXN MVP market. Selection lands about 2 weeks before the
  event, which is a usable outbound window. Only three alumni are named on the
  current page (TypingDNA, Collabwriting, DesignVerse), so the historic cohort
  names live on the archived edition sites, not here.
- **Approximate list size:** 20 per edition
- **Confidence:** Verified
- **Evidence:** Fetched the Spotlight 2026 page. Confirmed the 20-startup number,
  the full date ladder, and that a paid Startup Ticket is a precondition to
  apply. Confirmed the page does not currently name the selected cohort.
- **Last checked:** 2026-08-25

### Infoshare Startup Contest (Gdańsk)

- **Type:** event
- **Geography:** Poland, CEE
- **Homepage:** https://infoshare.pl/
- **List page:** https://infoshare.pl/conference/startup-contest/
- **Publicly listed?** yes
- **Machine readable?** HTML cards
- **Update cadence:** Annual, tied to the May conference. Applications close mid
  March, up to 20 semifinalists announced mid April, 5 finalists on stage.
- **Why it surfaces card candidates:** A Polish, city-funded, seed and early-stage
  contest in the largest MVP market. Semifinalist tier of 20 is the interesting
  one: pre-product-market-fit companies that have not chosen any financial
  infrastructure yet.
- **Approximate list size:** 20 semifinalists, 5 finalists per edition
- **Confidence:** Verified
- **Evidence:** Fetched the contest page. It currently serves the 2025 edition and
  names 20 semifinalists (Exoheal, InSimili, Kardi AI, PastEcho, Rilemo among
  them) with the 5-finalist structure and a 30,000 EUR total prize pool funded by
  the Mayor of Gdańsk. A 2026 finalist set (Beholder, Genotic, Green Sequest, SAY
  IT Labs, upLYFT) appeared in search results but I did not fetch that page, so
  treat the 2026 names as Reported, not Verified.
- **Last checked:** 2026-08-25

### Latitude59 Pitch Competition (Tallinn)

- **Type:** event
- **Geography:** Estonia, Baltics, Nordics, Ukraine
- **Homepage:** https://latitude59.ee/
- **List page:** https://latitude59.ee/meet-the-top15-competing-for-the-e400k-prize-fund-at-the-latitude59-pitch-competition/
- **Publicly listed?** yes
- **Machine readable?** HTML list with country labels
- **Update cadence:** Annual, running since 2012. TOP15 published pre-event, then
  a 7-finalist article, then a winners article. Three separate list posts per year.
- **Why it surfaces card candidates:** Country-tagged, early-stage, Baltic-heavy.
  The 2026 cohort spans Estonia (9), Lithuania (3), Finland (2), Austria (1),
  Ukraine (1). Baltics is where a disproportionate share of Europe's new
  payments-adjacent companies incorporate.
- **Approximate list size:** 15-16 named in the TOP15 post; 465 applicants from
  53 countries behind it
- **Confidence:** Verified
- **Evidence:** Fetched the TOP15 post and read all names and country tags:
  FleetFox, Getpin, Optonics, MindChip, Thistle, DogBase, Alpha3D, Milmech
  Systems, Pixit, Callsy AI, Ciklo, Backoffice LT, Bruukki, Granarium, Blue
  Auditor, FPV Battleground. Note the post is titled TOP15 but lists 16.
- **Last checked:** 2026-08-25

### South Summit Madrid Startup Competition

- **Type:** event
- **Geography:** Spain, Southern Europe, global applicants
- **Homepage:** https://www.southsummit.io/
- **List page:** https://www.southsummit.io/en/content/article-south-summit-madrid-2026-reveals-100-ai-driven-finalist
- **Publicly listed?** yes
- **Machine readable?** HTML, grouped by vertical
- **Update cadence:** Annual. 15th edition ran 3-5 June 2026 at La Nave, Madrid.
  Finalist article published roughly 2 weeks before the event.
- **Why it surfaces card candidates:** All 100 finalists named on one free page,
  pre-sorted into 10 verticals including an explicit **Fintech & Insurtech**
  vertical, plus Consumer, Future of Work, Mobility and Enterprise Solutions,
  which are the classic never-launched-a-card-program verticals. Spain is Phase 1a.
  44 of the 100 are Spanish.
- **Approximate list size:** 100 named, from 4,500+ applications across 110
  countries, 26 countries represented among finalists
- **Confidence:** Verified
- **Evidence:** Fetched the article. Confirmed all 100 startups are listed on the
  page itself grouped by the 10 verticals, and that no separate gated list is used.
- **Last checked:** 2026-08-25

### Web Summit featured startups (Lisbon)

- **Type:** event
- **Geography:** Portugal host, pan-European and global exhibitors
- **Homepage:** https://websummit.com/
- **List page:** https://websummit.com/startups/featured-startups/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, paginated, server-rendered
- **Update cadence:** Rolls forward continuously as exhibitors are confirmed, ahead
  of 9-12 November 2026. Third-party trackers cite 2,631 exhibitors from 94
  countries for the 2026 edition.
- **Why it surfaces card candidates:** The biggest single machine-readable
  pre-published exhibitor pool in Europe, organised by industry category (AI &
  machine learning, SaaS, healthtech, agritech, hardware, and others). A company
  paying for a Web Summit stand has budget. The non-fintech categories are the
  interesting ones for a greenfield card thesis.
- **Approximate list size:** roughly 100 per page over 27 pages of pagination on
  the featured view, so several hundred; full exhibitor pool far larger
- **Confidence:** Verified
- **Evidence:** Fetched the featured-startups page. Confirmed startup cards render
  in static HTML with industry categories and pagination "1 2 3 4 5 … 27". No
  country filter visible. No ALPHA-branded page found at this URL despite the
  ALPHA programme being widely referenced elsewhere.
- **Last checked:** 2026-08-25

### FinTech Connect Startup Launchpad (London)

- **Type:** event
- **Geography:** United Kingdom, pan-European exhibitors
- **Homepage:** https://www.fintechconnect.com/
- **List page:** https://www.fintechconnect.com/start-up-launchpad-2026
- **Publicly listed?** partial
- **Machine readable?** HTML cards
- **Update cadence:** Annual, event 1-2 December 2026 at ExCeL London. Page states
  "the full exhibitor list and demo schedule will be published here as companies
  are confirmed", so it fills in progressively across autumn. Applications
  reviewed on a rolling basis.
- **Why it surfaces card candidates:** A dedicated early-stage zone inside a
  5,000-person fintech event, with a live demo stage. Companies here are paying
  for a stand while still early, which is the budget-plus-intent signal. UK is
  opportunistic for TXN but the exhibitor pool is pan-European.
- **Approximate list size:** 22 companies in the 2025 cohort (ComplyCube, Kiya AI
  and others named on the page for reference); 2026 count not yet fixed
- **Confidence:** Verified
- **Evidence:** Fetched the 2026 Launchpad page. Confirmed the 2025 roster is
  displayed by name as a reference set, the December dates, the rolling
  application model, and the commitment to publish the 2026 list in advance.
- **Last checked:** 2026-08-25

### Slush 100 (Helsinki)

- **Type:** event
- **Geography:** Finland host, global applicants, Nordic and Baltic skew
- **Homepage:** https://slush.org/
- **List page:** https://slush.org/audience/startups/slush100
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Annual. Slush 2026 is 18-19 November, Helsinki. Application
  deadline 7 September; top 100 selected, cut to top 20 by September, 3 finalists
  named on 19 November.
- **Why it surfaces card candidates:** The eligibility bar is exactly TXN's
  greenfield band: founded 2023 or later, under 10M EUR raised, seed stage or
  earlier. The 500,000 EUR equity-free prize means a genuinely large applicant
  pool. The problem is the funnel is not published.
- **Approximate list size:** 100 selected, but not disclosed publicly
- **Confidence:** Verified
- **Evidence:** Fetched the Slush 100 page. Confirmed the funnel structure, dates,
  prize and eligibility, and confirmed explicitly that no public roster of the
  100 or the 20 is published on the page. Applicants see status only inside the
  Slush Platform. Treat as a partnership target, not a scrape target.
- **Last checked:** 2026-08-25

### TechChill (Riga)

- **Type:** event
- **Geography:** Latvia, Baltics
- **Homepage:** https://techchill.co/
- **List page:** https://www.techchill.co/startups-attending
- **Publicly listed?** partial
- **Machine readable?** HTML cards, logos only, no text company names
- **Update cadence:** Annual. Next edition 17-19 March 2027, Riga (side events
  17th, main 18-19). The attending-startups page currently still serves the 2025
  set, so it updates late.
- **Why it surfaces card candidates:** 310+ startups expected at the 2027 edition
  and a "Founders Battle" pitch competition with a 600,000+ EUR prize pool. Baltic
  early-stage density is high.
- **Approximate list size:** roughly 25 logos on the attending page; 310+ startups
  claimed for the event overall
- **Confidence:** Verified
- **Evidence:** Fetched both the homepage and /startups-attending. Homepage
  confirmed dates, scale, Founders Battle and recent winners (Deep Space Energy,
  Spotwise, Helm X). The attending page renders logo images with no accompanying
  text names, so it needs OCR or image-alt extraction rather than plain scraping.
- **Last checked:** 2026-08-25

### Startup Fair (Vilnius)

- **Type:** event
- **Geography:** Lithuania, Baltics
- **Homepage:** https://www.startupfair.lt/
- **List page:** none found
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Annual, September. No public roster published in advance.
- **Why it surfaces card candidates:** 450+ startups, 430+ investors from 65+
  countries, and a Pitch Battle putting 40+ startups on stage against a stated
  17M EUR investment pool. Lithuania is the single densest fintech-licensing
  jurisdiction in the EU, which raises the base rate of payments-adjacent
  founders in the room.
- **Approximate list size:** 450+ startups attending, none named publicly
- **Confidence:** Verified
- **Evidence:** Fetched the homepage. Confirmed the scale numbers and the Pitch
  Battle. Confirmed no startup directory or roster is offered. Organised in part
  by Startup Lithuania (public agency), which makes a partnership approach
  plausible.
- **Last checked:** 2026-08-25

### Wolves Summit (Kraków)

- **Type:** event
- **Geography:** Poland, CEE
- **Homepage:** https://www.wolvessummit.com/
- **List page:** none found (open call at /call-for-startups)
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Twice yearly across two host cities. Current edition Kraków
  14-15 October; a Warsaw edition also runs. Open "Call for Startups" is live.
- **Why it surfaces card candidates:** Explicitly a matchmaking event, 100
  investors to 250 founders, plus a Great Pitch Competition and a European CVC
  Awards gala. Poland is the top MVP market and this is its flagship
  founder-investor event.
- **Approximate list size:** 250 founders per edition, not named publicly
- **Confidence:** Verified
- **Evidence:** WebFetch returned 403; curl with a browser user agent returned 200
  and the homepage text confirmed "Corporate Dealflow & European CVC Awards,
  14-15 October, Krakow", "100 Investors; 250 Founders", plus nav items Call for
  Startups, Investors, CVC Awards. Historic startup roster subdomains
  (warsaw.wolvessummit.com/startups-2025, wroclaw.wolvessummit.com/startups)
  failed to resolve at all (curl exit 6, DNS). No public startup list exists.
- **Last checked:** 2026-08-25

### Bits & Pretzels (Munich)

- **Type:** event
- **Geography:** Germany, DACH
- **Homepage:** https://www.bitsandpretzels.com/
- **List page:** none found
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Annual, 28-30 September 2026, Munich.
- **Why it surfaces card candidates:** 250 companies in the Startup Exhibition,
  a "Pitch Corner" 90-second stage, and a "Golden Pretzel Award" where 20
  European business angels each bring their most promising startup. That last
  format is a curated 20-company list of angel-backed, pre-institutional
  companies, which is a very good greenfield shape if the names are ever released.
- **Approximate list size:** 250 exhibiting companies, 20 Golden Pretzel entrants,
  none named publicly
- **Confidence:** Verified
- **Evidence:** Fetched the homepage. Confirmed dates, the 250-company exhibition
  figure, Pitch Corner and Golden Pretzel Award. Confirmed no exhibitor roster or
  list URL is offered on the site.
- **Last checked:** 2026-08-25

### FinovateEurope demo lineup (London)

- **Type:** event
- **Geography:** United Kingdom host, pan-European demo companies
- **Homepage:** https://finovate.com/
- **List page:** https://finovate.com/welcome-to-2026-first-look-at-europe-demos/
- **Publicly listed?** partial
- **Machine readable?** HTML article
- **Update cadence:** Annual, February. The demo lineup is released in waves from
  roughly January onward. FinovateEurope 2026 ran 10-11 February at the
  InterContinental O2, London.
- **Why it surfaces card candidates:** Finovate's format is short live product
  demos, and the roster is announced by name weeks ahead. 30+ companies per
  edition, weighted to embedded finance, payments and real-time money movement.
  Small, early, product-stage European fintechs that have chosen to spend on a
  demo slot.
- **Approximate list size:** 30+ demo companies per edition
- **Confidence:** Reported
- **Evidence:** I fetched the Finovate "First Look at Europe Demos" post and it
  named **zero** companies, only "30+ cutting-edge demos" and a promise of later
  waves. A Business Wire release naming AAZZUR, Candour Identity, Darwinium,
  Elephant, FINTRAC, Francis, Hagbad, Intuitech, Keyless, mAI Edge, Mifundo,
  Opentech, Outsampler, R34DY, Sea.dev, Serene and Tweezr appeared in search
  results, but the direct fetch of that release timed out. The company names are
  therefore Reported, not Verified.
- **Last checked:** 2026-08-25

### Merchant Payments Ecosystem (MPE) Innovation Hub, Berlin

- **Type:** event
- **Geography:** Germany host, pan-European merchant payments
- **Homepage:** https://www.merchantpaymentsecosystem.com/
- **List page:** https://merchantpaymentsecosystem.com/innovation-hub
- **Publicly listed?** unknown
- **Machine readable?** gated (403 to automated fetch)
- **Update cadence:** Annual, March. 2026 edition ran 17-19 March at the
  InterContinental Berlin. Next edition 9-11 March 2027.
- **Why it surfaces card candidates:** The Innovation Hub accelerator vets a small
  cohort (reported as 12 for 2026) of merchant-payments startups, each given
  branding and a kiosk slot. Very high signal per name, very low volume. MPE also
  reportedly hosts 50 to 80 exhibitors.
- **Approximate list size:** roughly 12 accelerator startups, 80 exhibitors
- **Confidence:** Unverified
- **Evidence:** Both merchantpaymentsecosystem.com/innovation-hub and the www
  variant returned HTTP 403 to WebFetch. The 2027 dates and 80-exhibitor figure
  came from a fetched third-party events page (paytech.events), which also
  contained **no** mention of a startup village or innovation hub, so even that
  corroboration is partial. The 12-startup figure is search-snippet only.
- **Last checked:** 2026-08-25

### Impact CEE (Poznań)

- **Type:** event
- **Geography:** Poland, CEE
- **Homepage:** https://impactcee.com/
- **List page:** unknown
- **Publicly listed?** unknown
- **Machine readable?** gated (403)
- **Update cadence:** Annual, May. Reported as 13-14 May 2026 at the Poznań
  Congress Center.
- **Why it surfaces card candidates:** Positioned as one of CEE's largest
  innovation and policy conferences with a finance and digital transformation
  track, in the top MVP market. Worth a manual look because Polish corporates and
  scale-ups attend, and corporate-adjacent ventures are a greenfield card segment.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** Both https://impactcee.com/ and https://impactcee.com/impact/2026
  returned HTTP 403 to WebFetch. Dates and venue are from search results only.
  No exhibitor list URL located.
- **Last checked:** 2026-08-25

### Doers Summit (formerly Reflect Festival), Limassol

- **Type:** event
- **Geography:** Cyprus, Eastern Mediterranean, heavy CEE and Israeli founder traffic
- **Homepage:** https://www.doerssummit.com/ (https://www.reflectfest.com/ 301s here)
- **List page:** unknown
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** Annual, late May. Reported 30-31 May, moving venue to Kolla
  Factory.
- **Why it surfaces card candidates:** Reported 150+ exhibitors, 10,000 attendees,
  a Shark-Tank-format startup pitch in front of 200+ investors, and 20+ side
  events including CarryOn (VC and founder) and Elevate (proptech). Cyprus is an
  under-watched incorporation hub for CEE and Israeli founders, which makes it a
  genuinely fringe source.
- **Approximate list size:** 150+ exhibitors claimed, none confirmed by name
- **Confidence:** Unverified
- **Evidence:** reflectfest.com 301-redirects to doerssummit.com, which I then
  fetched: it returned essentially only the tagline "Doers Summit, the playground
  of doers" with no dates, no lists and no URLs. Everything else here is
  search-snippet only. Needs a browser session.
- **Last checked:** 2026-08-25

### 4YFN (Barcelona, at MWC)

- **Type:** event
- **Geography:** Spain, global
- **Homepage:** https://www.4yfn.com/
- **List page:** https://www.4yfn.com/exhibitors
- **Publicly listed?** yes, but not to an automated fetch
- **Machine readable?** JS-rendered
- **Update cadence:** Annual, early March alongside MWC. Exhibitor directory is
  searchable by name, country and industry once rendered.
- **Why it surfaces card candidates:** The startup platform bolted onto Europe's
  largest connectivity event. Exhibitors include startups, accelerators,
  universities and corporates. Spain is Phase 1a.
- **Approximate list size:** unknown; the directory is paginated
- **Confidence:** Unverified
- **Evidence:** Fetched /exhibitors. The static HTML contained only page metadata,
  JSON schema and a newsletter modal. Zero company names present. Confirmed the
  page is client-rendered, so it needs a headless browser, not WebFetch. A
  parallel /showfloor page exists and was not fetched.
- **Last checked:** 2026-08-25

---

## B. Awards programmes and shortlists

### Romania Startup Awards (ROTSA)

- **Type:** other (awards programme)
- **Geography:** Romania and Moldova
- **Homepage:** https://rotsa.ro/
- **List page:** https://startupcafe.ro/lista-peste-150-startupuri-romanesti-moldovenesti-nominalizate-gala-premiere-95701
- **Publicly listed?** yes
- **Machine readable?** HTML article, categorised
- **Update cadence:** Roughly biennial so far. Second edition 2026 (first was
  2024). Gala 12 March 2026 in Bucharest; public voting closed 11 March 2026.
- **Why it surfaces card candidates:** The best single CEE find in this stream.
  150+ Romanian and Moldovan startups named in one free page, split into "Best
  Innovators" (early stage, the greenfield tier) and "Best Performers" (scale-up),
  with subcategories across AI, healthtech, agritech, cleantech, edtech,
  cybersecurity and an explicit **FinTech & InsurTech Innovator** category
  (Fagura, Finergy, PayByFace, SOLO, stock.estate). Romania is an MVP market and
  this list is almost certainly absent from any incumbent's prospecting corpus.
- **Approximate list size:** 150+ named; entry pool reported as 137 Romanian,
  9 Moldovan, 11 Romanian-founded abroad
- **Confidence:** Verified
- **Evidence:** Fetched the StartupCafe article and confirmed the organiser
  (ROTSA), the edition, gala date, voting deadline, the two-tier category
  structure and the named fintech category with its five nominees. Separately
  attempted https://rotsa.ro/en/list-of-technology-startups-in-romania/ which
  returned HTTP 403, so ROTSA's own directory remains unverified.
- **Last checked:** 2026-08-25

### Cashless Fintech Awards and Mapa polskiego fintechu (cashless.pl)

- **Type:** media / awards programme / register
- **Geography:** Poland
- **Homepage:** https://www.cashless.pl/
- **List page:** https://www.cashless.pl/18867-cashless-fintech-2026-nominowani (nominees);
  https://www.cashless.pl/fintechy/s (fintech directory)
- **Publicly listed?** yes
- **Machine readable?** HTML article; the map itself is distributed as a report
- **Update cadence:** Annual on both tracks. Awards announced each June at the
  Cashless Fintech Evening in Warsaw (2026 edition 18 June). Mapa polskiego
  fintechu is now in its 9th edition, published 18 June 2026, submissions closed
  end of March.
- **Why it surfaces card candidates:** cashless.pl is the Polish payments trade
  press and the map is the definitive census of Polish fintech: 167 companies in
  the first edition (2018), 383 in the most recent. For TXN this is both a
  competitor map and a source of adjacent companies. The awards nominee list is
  smaller but is a curated view of who the Polish market thinks is ascendant.
- **Approximate list size:** 15 nominees across 3 award categories; 383 companies
  on the most recent fintech map
- **Confidence:** Verified (awards) / Reported (map contents)
- **Evidence:** Fetched the 2026 nominees page and read all three categories:
  Projekt Fintech (Comfino, FastTip, Allegro, Leaselink, mBank, WeSub Flex),
  Osobowość Fintech (4 individuals), Fintech Roku (Lendi, PayPo, PragmaGO,
  Smartney Grupa Oney, Wealthon, Zen). Confirmed the editorial selection process
  and annual June cadence. The 383-company map figure and the 18 June 2026
  publication date come from cashless.pl article titles in search results; I did
  not fetch the map report itself, so its contents are Reported.
- **Last checked:** 2026-08-25

### Deloitte Technology Fast 50 Central Europe

- **Type:** other (awards / ranking)
- **Geography:** Estonia, Latvia, Lithuania, Poland, Czech Republic, Slovakia,
  Romania, Croatia, Ukraine
- **Homepage:** https://www.deloitte.com/ce/en/issues/work/technology-fast-50.html
- **List page:** same page, plus downloadable annual PDF reports (2025 17MB,
  2024 26MB, 2023 25MB)
- **Publicly listed?** yes
- **Machine readable?** HTML profiles plus PDF
- **Update cadence:** Annual, now in its 27th edition. Applications open mid-year,
  ranking published in autumn, based on revenue growth over the prior four years.
- **Why it surfaces card candidates:** Covers all four TXN MVP markets. Four
  distinct lists per year, not one: **Fast 50** (the main ranking), **Companies to
  Watch** (younger, faster-growing, which is the greenfield tier), **AI Value
  Driver** (with Google Cloud), and **Impact Stars**, which explicitly covers
  fintech, cyber, ESG, medtech/biotech and defence. Each entry carries CEO name,
  country, sector and growth percentage, so it is directly enrichable.
- **Approximate list size:** 50 in the main ranking plus three secondary
  categories; recent editions had 14 Polish and 14 Czech companies, 9 Slovak
- **Confidence:** Verified
- **Evidence:** Fetched the Central Europe programme page. Confirmed the nine
  countries, the four award categories including Impact Stars with its fintech
  scope, the presence of past-year winner profiles with CEO/country/sector/growth
  fields on-page, and the three downloadable PDF reports.
- **Last checked:** 2026-08-25

### Central European Startup Awards

- **Type:** other (awards programme)
- **Geography:** Austria, Bulgaria, Czechia, Croatia, Hungary, Poland, Romania,
  Serbia, Slovakia, Slovenia, Estonia, Latvia, Lithuania
- **Homepage:** https://centraleuropeanstartupawards.com/
- **List page:** https://centraleuropeanstartupawards.com/how-it-works/ (process);
  per-country finalist pages published per edition
- **Publicly listed?** partial
- **Machine readable?** HTML
- **Update cadence:** Annual, currently edition 10. Five phases: open nominations,
  regional advisor shortlisting to top 5 per category per country, public voting,
  jury selection, regional winner announcement. Every second year the regional
  winners feed a Global Grand Finale.
- **Why it surfaces card candidates:** 13 countries including all four MVP
  markets, with a top-5 shortlist **per category per country**. That structure
  multiplies out to a large, country-tagged list of ambitious companies, and the
  awards run a fintech category. Nominations are open and bottom-up, so it catches
  companies too small for any funding database.
- **Approximate list size:** 5 shortlisted per category per country across 13
  countries and 14 reported categories, so potentially several hundred names per
  edition
- **Confidence:** Verified (process) / Unverified (shortlist availability)
- **Evidence:** Fetched the "How It Works" page. Confirmed the 13 countries, the
  five-phase process, top-5 shortlisting, public voting weighting and edition 10.
  The page confirms finalists are announced publicly but does **not** confirm that
  complete shortlists are published on-site, and I did not locate a 2026 shortlist
  URL. The 14-category and fintech-category detail is from search snippets.
- **Last checked:** 2026-08-25

### PayTech Awards (FinTech Futures)

- **Type:** other (awards programme)
- **Geography:** Global with heavy European entry, ceremony in London
- **Homepage:** https://www.fintechfutures.com/events/paytech-awards
- **List page:** https://www.fintechfutures.com/paytech/the-paytech-awards-2026-shortlist-is-here
- **Publicly listed?** yes (asserted, not confirmed by me)
- **Machine readable?** blocked by Cloudflare
- **Update cadence:** Annual. 2026 winners announced 25 June 2026 at the
  Honourable Artillery Company, London. Nominations open earlier in the year and
  the shortlist post is published weeks ahead.
- **Why it surfaces card candidates:** Payments-specific shortlist with categories
  that map directly onto TXN's space, including "Best Cards & Payments System for
  Banks, FIs & Fintechs" and "Best Payment Infrastructure Solution". More useful
  as a competitor and partner map than as greenfield discovery, but the
  entrant pool includes small vendors.
- **Approximate list size:** unknown; multiple dozens across categories
- **Confidence:** Unverified
- **Evidence:** WebFetch returned HTTP 403 and a direct curl with a browser user
  agent hit a Cloudflare "Sorry, you have been blocked" interstitial (Ray ID
  captured). The shortlist's existence is corroborated by three independent
  finalist announcements I saw in search results (Ecrypt, SDK.finance, CorServ),
  each naming its category, but I never read the shortlist page itself.
- **Last checked:** 2026-08-25

---

## C. Media publishing recurring watch lists and cohort round-ups (Sifted-shaped)

### The Recursive, "CEE Startup & Tech Weekly"

- **Type:** media
- **Geography:** Bulgaria, Romania, Poland, Croatia, Czech Republic, Greece,
  Ukraine, Hungary, Slovenia, Lithuania, Serbia, Slovakia
- **Homepage:** https://www.therecursive.com/
- **List page:** https://www.therecursive.com/cee-startup-tech-weekly-4/ (series;
  URLs use /cee-startup-tech-weekly-<n>/ and slug variants)
- **Publicly listed?** yes
- **Machine readable?** HTML article
- **Update cadence:** Weekly, plus irregular themed list features such as "18 Deep
  Tech Startups from CEE You Should Keep an Eye On" and "15 CEE Bootstrapped
  Startups That Should Be On Your Radar"
- **Why it surfaces card candidates:** This is the closest Sifted-shaped source to
  TXN's MVP markets. Each weekly edition names about 10 companies with a paragraph
  each and a country tag, covering Southeast and Central Europe including
  Romania, Hungary and Poland. Free, no paywall observed. The themed list
  features are the higher-value artefacts because they are curated rather than
  funding-triggered, which catches companies before any round is announced.
- **Approximate list size:** about 10 companies per weekly edition; 15 to 18 per
  themed list
- **Confidence:** Verified
- **Evidence:** Fetched the homepage and one weekly edition. Homepage confirmed
  the recurring "CEE Startup & Tech Weekly" series, the country coverage and an
  email newsletter, and confirmed there is **no** startup database on the site.
  The edition I read named 10 companies with countries: Pathway (PL), Preview
  (RS), Volteum (HU), Builderly and EnduroSat (BG), Sudolabs (SK), plus global
  players.
- **Last checked:** 2026-08-25

### Vestbee (monthly CEE funding rounds, weekly news, CEE SaaS Index)

- **Type:** media / register
- **Geography:** CEE-wide: Poland, Estonia, Romania, Czech Republic, Lithuania,
  Latvia, Slovenia, Ukraine, Hungary and others (20 countries claimed for the index)
- **Homepage:** https://www.vestbee.com/
- **List page:** https://www.vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-may-2026
  (monthly series); https://www.vestbee.com/cee-saas-index
- **Publicly listed?** yes
- **Machine readable?** HTML article for the round-ups; the SaaS Index offers a
  downloadable Excel
- **Update cadence:** Monthly "Top CEE funding rounds closed in <month>", a weekly
  "VC & Startup weekly news from CEE" archive, an annual "largest CEE funding
  rounds" piece, and the CEE SaaS Index refreshed monthly for valuations and
  quarterly for constituents
- **Why it surfaces card candidates:** Four distinct recurring artefacts on one
  site, all free, all CEE-first. The monthly round-up names about 11 companies
  with a paragraph each and a country. Vestbee also publishes free VC List, LP
  List and Events List directories, which are useful for the sibling
  accelerator/VC stream. The CEE SaaS Index is small but is a rare public
  valuation benchmark for the exact region.
- **Approximate list size:** about 11 companies per monthly round-up; 10
  constituents in the CEE SaaS Index; platform claims 40,000 founders, VCs,
  accelerators and corporates registered
- **Confidence:** Verified
- **Evidence:** Fetched the May 2026 round-up and counted 11 companies across 7
  countries (Viktor and Elastics PL, Skeleton Technologies EE, DesignVerse RO,
  FaceUp and Zerops CZ, Kopa.ai and Backoffice LT, BirdyChat LV, DDD Invoices SI,
  Karpatia Benefits UA). Fetched the homepage, which confirmed the free VC/LP/
  Events/CEE SaaS Index directories. Fetched the CEE SaaS Index page, which
  confirmed 10 constituents (PL 7, EE 2, RO 1, SI 1), the monthly/quarterly
  refresh cadence, the Excel download and the small-sample caveat the site itself
  publishes.
- **Last checked:** 2026-08-25

### CzechCrunch CC25 and startup desk

- **Type:** media
- **Geography:** Czech Republic
- **Homepage:** https://cc.cz/
- **List page:** https://cc.cz/cc25/ ; startup section https://cc.cz/startupy/
- **Publicly listed?** yes
- **Machine readable?** HTML article and paginated section
- **Update cadence:** CC25 is annual with per-year archive pages (e.g.
  /cc25/rocnik-2023/). The /startupy/ section is continuous and paginates to 316+
  pages. CzechCrunch also runs a monthly Startup newsletter covering all Czech
  investments plus a weekly general round-up.
- **Why it surfaces card candidates:** Czech Republic is an MVP market and
  CzechCrunch is its dominant startup outlet. CC25 splits into a top 5 (billion-
  koruna revenue) and a top 20 below that threshold, so the interesting greenfield
  tier is explicitly separated out. The monthly investment newsletter is the
  ongoing signal.
- **Approximate list size:** 25 per annual CC25 edition; the /startupy/ archive is
  effectively unbounded
- **Confidence:** Verified
- **Evidence:** Fetched a CC25 edition page. Confirmed the annual cadence, the
  5-plus-20 structure, and read named companies (Rohlík, Shipmonk, Productboard,
  Mews, Dodo in the top 5; Keboola, Woltair, Resistant AI, E2B, Ellio Technology,
  Filuta, Upheal below). The monthly Startup newsletter and the 316-page
  /startupy/ pagination are from search results and a fetched section reference
  respectively.
- **Last checked:** 2026-08-25

### StartupCafe.ro

- **Type:** media
- **Geography:** Romania and Moldova
- **Homepage:** https://startupcafe.ro/
- **List page:** https://startupcafe.ro/lista-26-startupuri-romanesti-adn-romanesc-2026-92375
- **Publicly listed?** yes
- **Machine readable?** HTML article
- **Update cadence:** Annual year-ahead watch list, plus event-driven list articles
  (it was also the outlet that published the full ROTSA awards nominee list)
- **Why it surfaces card candidates:** Romanian-language, free, and it names every
  company in the list rather than teasing them. The 2026 watch list is 26 companies
  with Romanian DNA including several fintech-adjacent names (Instant Factoring,
  Profluo). Romanian-language sources are structurally invisible to English-only
  prospecting, which is the point.
- **Approximate list size:** 26 per annual watch list; 150+ on the awards article
- **Confidence:** Verified
- **Evidence:** Fetched the 2026 watch list. All 26 companies read off the page:
  Data Sweep, Examin, Bible Chat, Kidprenor, Footprints AI, Voice Patrol, Assista
  AI, Recycllux, VAUNT, Neurolabs, Brio, RepsMate, BraveX Aero, Medicai, Meetgeek,
  LIVRESQ, Ogre AI, Dexory, Instant Factoring, Medical Pilot, Digitail,
  Opticomm.AI, Profluo, Runware, .lumen, Voxa. The page does not itself confirm
  the list is annual, so cadence is inferred from the "2026" framing and is the
  weakest claim in this entry.
- **Last checked:** 2026-08-25

### MamStartup.pl

- **Type:** media
- **Geography:** Poland
- **Homepage:** https://mamstartup.pl/
- **List page:** https://mamstartup.pl/nowa-fala-polskiego-techu-10-obiecujacych-startupow-na-ktore-warto-zwrocic-uwage-w-2026-roku/
- **Publicly listed?** yes
- **Machine readable?** HTML article
- **Update cadence:** Irregular curated list features; continuous "Newsy" and
  interview sections. No confirmed fixed-cadence startup column.
- **Why it surfaces card candidates:** Polish-language startup media in the top MVP
  market, publishing named watch lists that skew explicitly to **companies founded
  after 2023**. That founding-date filter is close to a direct proxy for "has never
  launched a card program".
- **Approximate list size:** 10 per list feature
- **Confidence:** Verified
- **Evidence:** Fetched the article. All 10 companies named: CampusAI, FOTOhub,
  Ingenix, Holi, Clinical Trials Information Network, DefendEye, Defguard, Cropler,
  Revoize, ForActive. Confirmed the site sections (Newsy, Wywiady, Poradnik
  startupowca). Confirmed I could **not** establish a recurring dedicated column,
  so cadence is the weak point here.
- **Last checked:** 2026-08-25

### Swedish Tech Weekly (swedishtechnews.com)

- **Type:** media / newsletter
- **Geography:** Sweden
- **Homepage:** https://www.swedishtechnews.com/
- **List page:** https://www.swedishtechnews.com/swedish-tech-weekly-368/
  (pattern: /swedish-tech-weekly-<issue>/)
- **Publicly listed?** yes
- **Machine readable?** HTML, categorised sections, sequential issue numbering
- **Update cadence:** Every Monday morning, currently around issue 368, so roughly
  seven years of continuous back issues
- **Why it surfaces card candidates:** The most Sifted-shaped source found outside
  Sifted. Each issue names roughly 25 to 30 Swedish companies with a one-line
  description each, split into M&A, funding, startup-database highlights and
  sector news. Sequential issue numbers make the whole archive trivially
  enumerable. Free tier covers the major news; a PRO tier adds more funding rounds.
- **Approximate list size:** 25 to 30 companies per weekly issue
- **Confidence:** Verified
- **Evidence:** Fetched issue 368. Confirmed the Monday cadence, the author
  (Martin Weigert), the free/PRO split, the section structure, the emphasis on
  newly funded and recently active companies, and the sequential URL pattern with
  issues 365 to 367 visible as siblings. Issue headline alone listed about 20
  company names.
- **Last checked:** 2026-08-25

### Fintech in Baltic (fintechbaltic.com) country listings

- **Type:** media / register
- **Geography:** Lithuania, Latvia, Estonia
- **Homepage:** https://fintechbaltic.com/
- **List page:** https://fintechbaltic.com/fintech-startups-lithuania/ ;
  https://fintechbaltic.com/fintech-latvia-startups/ ;
  https://fintechbaltic.com/fintech-estonia-startups-listing/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with logo, description and social links
- **Update cadence:** Stale. The Lithuania page is explicitly titled "THE 2022-2023
  LIST" and some entries reference 2019 data. Treat as a snapshot, not a feed.
- **Why it surfaces card candidates:** A free, complete-ish census of Baltic
  fintech split into 8 categories (Big Data & Analytics, Blockchain and Crypto,
  Digital Banking, Compliance & Cybersecurity, Financial Software, Insurtech,
  Lending, Other). Useful as a one-off first-hit input for the Baltics. Useless as
  an ongoing signal because it does not appear to be maintained.
- **Approximate list size:** 150+ Lithuanian companies; Latvia and Estonia lists
  not counted
- **Confidence:** Verified
- **Evidence:** Fetched the Lithuania list. Confirmed 150+ companies across the 8
  categories, the card format, the 2022-2023 title, and the existence of sibling
  Latvia and Estonia pages in the nav. Confirmed staleness from an in-page
  reference to 2019 customer-funds data.
- **Last checked:** 2026-08-25

### Sifted

- **Type:** media
- **Geography:** Pan-European, with named regional cuts for UK & Ireland, Southern
  Europe, Nordics & Benelux
- **Homepage:** https://sifted.eu/
- **List page:** https://sifted.eu/leaderboards ; https://sifted.eu/rankings
- **Publicly listed?** partial (leaderboards appear free, Sifted Pro data is paid)
- **Machine readable?** could not determine
- **Update cadence:** Annual per leaderboard, rolling across regions and themes.
  Newsletters are daily and weekly, including a fintech newsletter and a Wednesday
  "Startup Life" newsletter.
- **Why it surfaces card candidates:** This is the source the client named as "an
  insane resource" and the shape everything else in this section is being measured
  against. Recurring artefacts observed in search results: **Sifted 100** regional
  leaderboards (UK & Ireland 2026, Southern Europe 2026, Nordics & Benelux 2025),
  **Consumer 100**, **AI 100**, **Rising 100**, plus Sifted Pro downloadable Deals
  Tracker, Market Tracker, Investor Tracker and M&A Tracker and 100+ sector
  Briefings.
- **Approximate list size:** 100 per leaderboard
- **Confidence:** Unverified
- **Evidence:** **I could not open Sifted.** https://sifted.eu/leaderboards and
  https://sifted.eu/leaderboards/sifted-100-southern-europe-2026 both returned
  HTTP 403 to WebFetch, and a direct curl with a full browser user agent also
  returned 403. Every structural claim above is from search-result snippets. Do
  not treat the leaderboard names, counts or paywall status as confirmed. This
  needs an authenticated browser session or a Sifted Pro subscription, and given
  the client explicitly asked for Sifted-shaped sources, it should be the first
  thing re-verified in the next pass.
- **Last checked:** 2026-08-25

### EU-Startups

- **Type:** media / register
- **Geography:** Pan-European
- **Homepage:** https://www.eu-startups.com/
- **List page:** https://www.eu-startups.com/directory/ ; weekly funding round-up
  series at https://www.eu-startups.com/tag/weekly/
- **Publicly listed?** yes (asserted, not confirmed by me)
- **Machine readable?** could not determine
- **Update cadence:** Weekly funding round-up published each Friday covering the
  week's European rounds; a continuously maintained startup directory; a paid
  "CLUB" membership tier
- **Why it surfaces card candidates:** Same shape as Sifted but broader and less
  paywalled, with a directory that is free to browse. Good for pan-European
  coverage where the CEE-specific sources thin out.
- **Approximate list size:** unknown; weekly round-ups name every tracked round
- **Confidence:** Unverified
- **Evidence:** Both https://www.eu-startups.com/directory/ and a specific weekly
  round-up article returned HTTP 403 to WebFetch, and curl with a browser user
  agent also returned 403 on the directory. Only the article titles and a
  secondary EU-Startups directory listing for The Recursive were observable.
- **Last checked:** 2026-08-25

### StartupItalia (SIOS 100)

- **Type:** media
- **Geography:** Italy
- **Homepage:** https://startupitalia.eu/
- **List page:** https://startupitalia.eu/startup/countdown-sios25-le-100-migliori-startup-del-2025-secondo-noi/
- **Publicly listed?** yes (asserted)
- **Machine readable?** could not determine
- **Update cadence:** Annual, tied to the StartupItalia Open Summit (SIOS), with
  per-year archive articles (SIOS23, SIOS24, SIOS25). Reported to also run a
  weekly column and an open list refreshed each 15 August.
- **Why it surfaces card candidates:** 100 named Italian startups per year in
  Italian, from a market that is not on the TXN priority list but is a large
  Southern European pool. Lower priority than the CEE sources.
- **Approximate list size:** 100 per annual edition
- **Confidence:** Unverified
- **Evidence:** The SIOS25 list page returned HTTP 403 to WebFetch. Sibling URLs
  for SIOS23 and SIOS24 were visible in search results, which is what supports the
  annual-cadence claim, but no page was read.
- **Last checked:** 2026-08-25

### Forbes Hungary, "A legforróbb magyar startupok"

- **Type:** media
- **Geography:** Hungary
- **Homepage:** https://www.forbes.hu/
- **List page:** https://www.forbes.hu/print/a-legforrobb-magyar-startupok-2025/
  (2023 edition at /lists/a-legforrobb-magyar-startupok-2023/)
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** Appears annual based on the 2023 and 2025 URL pattern
- **Why it surfaces card candidates:** Hungary is an MVP market and this is the
  only recurring Hungarian company ranking I located. Recording it despite failing
  to verify it, because the gap matters more than the entry.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** Fetched the 2025 URL. The response contained the article title only
  and no list content, no company names and no paywall indicator. The /lists/ URL
  form for the 2023 edition is what suggests a recurring list product. **Hungary
  is the weakest-covered MVP market in this stream and should be re-run.**
- **Last checked:** 2026-08-25

---

## D. Newsletters with high European fintech density

### This Week in Fintech, UK & Europe edition

- **Type:** media (newsletter)
- **Geography:** United Kingdom and Europe (part of a per-continent family)
- **Homepage:** https://www.thisweekinfintech.com/
- **List page:** https://www.thisweekinfintech.com/t/uk-europe
- **Publicly listed?** yes
- **Machine readable?** HTML, editions dated by week ending
- **Update cadence:** Weekly, editions labelled by week ending date
- **Why it surfaces card candidates:** Region-scoped fintech newsletter with a
  dedicated **Fundraises** section, so each edition is a company list rather than
  commentary. Free to subscribe. The regional split means the Europe edition is not
  diluted by US news, which is the usual failure mode of fintech newsletters.
- **Approximate list size:** varies per edition; several featured stories plus a
  longer fundraise list behind "Load more"
- **Confidence:** Verified
- **Evidence:** Fetched the UK & Europe tag page. Confirmed weekly cadence with
  editions such as "week ending 20th March 2026", the presence of a Fundraises
  navigation section, a free subscribe path, and the "Load more" pagination.
  Per-edition company counts could not be read off the tag page.
- **Last checked:** 2026-08-25

### Fintech Brainfood (Simon Taylor)

- **Type:** media (newsletter)
- **Geography:** Global, London-authored, meaningful European coverage
- **Homepage:** https://www.fintechbrainfood.com/
- **List page:** homepage archive, chronological
- **Publicly listed?** yes
- **Machine readable?** HTML archive
- **Update cadence:** Weekly, written at weekends
- **Why it surfaces card candidates:** Highest-authority independent fintech
  newsletter in Europe and a strong partnership or awareness surface rather than a
  pure list source. Each edition names roughly 5 to 15 companies but they skew to
  large incumbents (Stripe, Nvidia, Goldman Sachs, BlackRock, Robinhood, Wise,
  Revolut), so its discovery value for greenfield is low. Its value to TXN is
  distribution and credibility, not prospect names.
- **Approximate list size:** 5 to 15 companies named per edition, incumbent-weighted
- **Confidence:** Verified
- **Evidence:** Fetched the homepage archive. Confirmed weekly cadence, the
  AI/payments/banking scope, the chronological archive and the per-article company
  density. Confirmed the homepage does **not** disclose subscriber count and does
  **not** have a dedicated European section. The widely repeated "45,000+
  subscribers" figure is from search results, not from the site, so it is Reported.
- **Last checked:** 2026-08-25

### Payment & Banking (Germany)

- **Type:** media (newsletter, podcasts, events, award)
- **Geography:** Germany, DACH
- **Homepage:** https://www.paymentandbanking.com/
- **List page:** no company directory found
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Continuous articles, recurring columns (Kolumne, "Nils
  nörgelt"), infographics, a "Gesichter Fintech" people series, multiple podcast
  series, and annual events
- **Why it surfaces card candidates:** The German-language fintech hub. Its value
  to this stream is the surrounding assets rather than the blog: it runs the
  **Payment Exchange** and **Banking Exchange** events and a **"Fintech des
  Jahres"** award, all of which produce named company sets. It also runs podcast
  series ("AI in Finance", "How I Got Into Fintech") that name founders and
  companies, which partly covers the podcast sub-brief.
- **Approximate list size:** unknown
- **Confidence:** Verified (site) / Unverified (award shortlist)
- **Evidence:** Fetched the homepage. Confirmed the content types, the recurring
  columns, the podcast series, the newsletter signup, and the four events plus the
  Fintech des Jahres award. Attempted
  https://www.paymentandbanking.com/fintech-des-jahres/ and it returned **HTTP
  404**, so the award's shortlist page was not located and no nominee list was read.
- **Last checked:** 2026-08-25

---

## E. Communities, associations and membership directories

### Czech Fintech Association (Česká fintech asociace)

- **Type:** community (industry association)
- **Geography:** Czech Republic
- **Homepage:** https://czechfintech.cz/
- **List page:** https://czechfintech.cz/en/members/
- **Publicly listed?** yes
- **Machine readable?** HTML, linked logo grid with alt text and outbound URLs
- **Update cadence:** Continuous as members join. Founded 2016.
- **Why it surfaces card candidates:** The best free Czech fintech list found. Two
  tiers: full members (companies offering fintech solutions) and associate members
  (ecosystem supporters, banks, law firms, Visa, Deloitte). Every member links out
  to its own site, so the list is directly enrichable. Czech Republic is an MVP
  market and the list includes a long tail of small companies that would not appear
  in any funding database: Qerko, NFCtron, Flowpay, Fingood, Frenkee, Dobito,
  Karstfin, Taxomat, WFlow, Corrency, Mo.one, Eterny, Unnits, Metada.
- **Approximate list size:** roughly 70 full members plus roughly 15 associate
  members, about 85 total
- **Confidence:** Verified
- **Evidence:** Fetched the members page and read the roster. Full members
  captured include Akcenta, TSYS, Kontomatik, Anycoin, Ebury, Banking Circle,
  Srovnej.to, Shoptet Pay, Ronda Invest, Linksoft, Flowpay, Fingood, Portu, aEVI,
  Greco, ThePay, Fondee, Lemonero, CITfin, Barion, Occollo, PatronGo, NFCtron,
  Moro Systems, Coinmate, Adacta, Up, Frenkee, Firefish, Orbi, InvestBay,
  Crowdberry, Metada, iProov, Taxomat, WFlow, Etnetera, Dluhopisomat, Decta,
  Qerko, Bondster, Corrency, Adyen, Lexis Nexis, Tokenway, Unnits, Eterny,
  Eldison, Mo.one, Dobito, Eurowag, Malcom Finance, Karstfin, Axelum. Associate
  members include Seed Starter, KBSS, Raiffeisenbank, Deloitte, Visa, Hobza Legal,
  Havel a Partners, FinReg, Home Credit, CDCP.
- **Last checked:** 2026-08-25

### RoFintech (Romanian Fintech Association)

- **Type:** community (industry association)
- **Geography:** Romania
- **Homepage:** https://rofin.tech/
- **List page:** https://rofin.tech/members/
- **Publicly listed?** yes
- **Machine readable?** HTML, categorised linked logo grid
- **Update cadence:** Continuous as members join. Association established January
  2020.
- **Why it surfaces card candidates:** Same shape as the Czech list, in the other
  MVP market where TXN has an obvious wedge. Four sections: Fintech Members,
  International and Corporate Members, Strategic Partners (regulators, universities)
  and International Partners (peer associations in other European countries). That
  last section is a ready-made map of the equivalent associations to approach in
  every other target market.
- **Approximate list size:** 47 fintech members, 17 international/corporate
  members, 64 total, plus strategic and international partner blocks
- **Confidence:** Verified
- **Evidence:** Fetched both the homepage and /members/. Homepage confirmed the
  association positions itself as Romania's only national fintech association,
  that joining runs through an application (a Google Form), and that pricing is not
  disclosed publicly. Members page confirmed the 47 and 17 counts and the
  four-section structure, with each member rendered as a linked logo. **Access
  model: application-only, cost undisclosed.**
- **Last checked:** 2026-08-25

### FinTech Poland Foundation

- **Type:** community (think tank / association)
- **Geography:** Poland
- **Homepage:** https://fintechpoland.com/
- **List page:** none public
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Publishes reports, regulatory analyses and a newsletter; no
  member roster published
- **Why it surfaces card candidates:** The institutional counterpart to cashless.pl
  in the top MVP market, sitting between Polish fintechs and the KNF regulator. Its
  value is a partnership: it convenes the ecosystem and runs a newsletter, but it
  does not hand you a list. Ecosystem participants referenced elsewhere include
  BLIK, Kontomatik, Mastercard, Zonda, BNP Paribas Bank Polska.
- **Approximate list size:** unknown, not published
- **Confidence:** Verified (that no public list exists)
- **Evidence:** Fetched https://fintechpoland.com/pl/o-nas/. Confirmed the
  foundation publishes reports and market-trend analyses, regulatory analysis and a
  newsletter, and confirmed explicitly that **no** member or partner list and no
  fintech map is presented on that page. A "BAZA WIEDZY" knowledge base is
  referenced but its contents were not accessible from this page.
- **Last checked:** 2026-08-25

### Copenhagen Fintech

- **Type:** community / incubator hub
- **Geography:** Denmark, Nordics
- **Homepage:** https://www.copenhagenfintech.dk/
- **List page:** none public (programmes at /startups, memberships at
  /memberships-partnerships)
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** 5 programmes per year with demo days
- **Why it surfaces card candidates:** Runs a **Tech for Fin** programme explicitly
  aimed at entrepreneurs **from other industries** validating a fintech
  problem-solution fit. That is a literal description of TXN's greenfield segment:
  non-fintech companies discovering they need financial infrastructure. The Lab
  holds about 45 companies at a time. 380+ demo day pitches to date means a large
  historic cohort that is simply not published.
- **Approximate list size:** about 45 in the Lab at any time, 120+ cumulative Lab
  alumni, 630+ programme alumni, none named publicly beyond five case studies
  (Predicti, Monthio, DoLand, Januar, Uniify)
- **Confidence:** Verified
- **Evidence:** Fetched /startups. Confirmed the five programmes (Mentor Program,
  Partnership Fast Track, Tech for Fin, Incubation, Scaleup Partner), the 630+,
  380+, 90+ and 5-per-year metrics, and that **no public cohort roster or directory
  exists**. Membership terms from /memberships-partnerships: **open to all
  organisations**, priced by company size, reviewed annually, included if you are
  based in the Lab. **Access model: paid, open application.** Contact is
  hello@copenhagenfintech.dk.
- **Last checked:** 2026-08-25

### The Hub (thehub.io)

- **Type:** register (Nordic startup directory)
- **Geography:** Denmark, Sweden, Norway, Finland, Iceland
- **Homepage:** https://thehub.io/
- **List page:** https://thehub.io/startups
- **Publicly listed?** yes
- **Machine readable?** HTML, filterable
- **Update cadence:** Continuous. Startups self-register via /startups/join, so the
  directory grows as new companies appear rather than as they raise.
- **Why it surfaces card candidates:** The largest free, filterable, self-registered
  Nordic company directory found: **9,000+ startups**, with counts per country
  (Denmark 5,233, Sweden 2,373, Norway 2,279, Finland 1,434, Iceland 24) and
  filters for industry (including an explicit **Fintech** category), startup stage,
  size and funding status. Because companies register themselves to hire, they
  appear here **before** they appear in any funding database. That is exactly the
  "surfaces a company before a card program exists" property the brief asks for.
- **Approximate list size:** 9,000+ companies
- **Confidence:** Verified
- **Evidence:** Fetched /startups. Confirmed the 9,000+ figure, the per-country
  breakdown, the 20+ industry categories including Fintech, and the stage, size and
  funding filters. Candidate-side pricing is not stated on the page; a /pricing
  page exists and paid services are aimed at startups, so browsing is likely free
  but that was not confirmed.
- **Last checked:** 2026-08-25

### Female Founders (Vienna)

- **Type:** community
- **Geography:** Austria base, Europe-wide claim, Central European presence
- **Homepage:** https://www.female-founders.org/
- **List page:** none public
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** Recurring programmes: Female Founders Experience (FFX),
  a 4-week hybrid Bootcamp accelerator, Female Money Days, and a year-long
  Female Founders Circle membership
- **Why it surfaces card candidates:** Vienna-based, which puts it adjacent to
  CEE, and it claims 87,000+ active members, 250+ startups backed and 500+ VCs in
  network. Bootcamp cohorts are early-stage women-led startups, i.e. pre-vendor-
  selection. This is a pure partnership play: nothing is scrapeable.
- **Approximate list size:** 250+ startups backed, none listed publicly
- **Confidence:** Verified
- **Evidence:** Fetched the homepage. Confirmed the four programmes, the claimed
  metrics, the Vienna event location, and that **no public member directory or
  cohort list exists**. **Access model: mixed. FFX is curated or invite-based (120
  people), the Bootcamp is application-only, the Circle is a paid annual
  membership.** CEE coverage beyond Vienna is asserted by the site but not
  evidenced.
- **Last checked:** 2026-08-25

---

## F. Checked and rejected, or too thin to record as entries

Recorded so the next pass does not repeat the work.

- **The Paypers** (https://www.thepaypers.com/): fetched. Strong Amsterdam-based
  European payments trade press, but confirmed to have **no** company directory,
  no recurring named-company lists and no fintech database. News and reports only.
  Useful for market intelligence, useless as a discovery source. Verified negative.
- **Startup Grind chapters** (https://www.startupgrind.com/chapters/): fetched.
  The page is a gateway with no chapter data, no city list and no access-model
  information rendered. Chapter coverage of Poland, Czechia, Romania and Hungary
  could not be confirmed. Unverified.
- **Slush 100, TechChill attending list, Startup Fair Vilnius, Wolves Summit,
  Bits & Pretzels**: all confirmed to have real, large startup cohorts and **no
  published roster**. These five are the partnership shortlist for the events
  sub-brief. The data exists, the organiser holds it, and it is only obtainable
  through a relationship or a sponsorship.
- **Podcasts and demo-day streams**: the weakest part of this stream.
  https://therecursive.com/podcast/ returned HTTP 404 and no other verified
  podcast list source was reached before the search budget ran out. The only
  verified podcast-adjacent asset is Payment & Banking's show list ("AI in
  Finance", "How I Got Into Fintech"), recorded inside that entry. Treat this
  sub-brief as unfulfilled rather than as answered.
