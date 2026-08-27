---
description: "Stream 04 raw research: 37 card scheme, BIN sponsor, programme manager and trade association sources"
---

> **Section:** [[research]]
> **Validation:** [[validation-04-scheme-and-sponsors]]
> **Status:** raw research output, recorded verbatim. Read the validation report alongside it: several counts in this file were corrected.

# Stream 04: card scheme programmes, BIN sponsors, and the partner ecosystem

Owner: scheme-and-sponsors research stream
Last checked: 2026-08-25
Scope exclusion honoured: no BIN range registrations, no public BIN lookup
databases. Ruled out by the client as a post-decision signal.

---

## Summary

The stream was commissioned on the hypothesis that the card schemes list their
own fintech onboarding cohorts, and that BIN sponsors list their clients. Both
halves of that hypothesis were tested by fetching the pages. One survives, one
mostly does not.

**What survives, and it is the single best find in this stream:**

The **Visa Innovation Program Europe** publishes its entire participant roster
as an open, unauthenticated JSON API. 154 fintechs, tagged by country, vertical
and cohort year, 2019 through 2026, with company description and homepage URL in
the payload. No key, no login, no scraping. Two HTTP requests return the whole
thing. It covers Greece/Cyprus/Malta, Spain/Portugal, Italy, Bulgaria and
Türkiye, which maps directly onto TXN's Phase 1a markets and reaches one CEE
country. The 2026 cohort of 22 companies was published within the last four
months. This is a list of companies that applied to a card scheme's growth
programme, which is a far earlier signal than a launch announcement.

**What does not survive:**

- **Mastercard does not publish a Start Path participant list.** The Start Path
  page states 500+ startups in 60+ countries and offers no directory, no alumni
  page, and no filter. Cohorts are announced only as press releases on a
  JavaScript-rendered newsroom that returns 403 to every non-browser fetch
  method tried. The "500+ startups" number is a marketing claim on a page with
  no roster behind it.
- **The Visa Partner Directory list is broken or gated for anonymous users.**
  The page renders, the country filter contains every European market including
  Poland, Czechia, Hungary and Romania, and there is a documented filter value
  for `BIN Sponsor`. But the data file the page loads,
  `/content/dam/gpp/solution-directory/listing/directory.json`, 302-redirects to
  a 404 page. Individual partner pages ARE public and server-rendered. The
  aggregate list is not retrievable without a real browser session, and possibly
  not even then.
- **Mastercard For Fintechs Europe publishes no participant list either.** Its
  participating-country graphic is a raster image, not text. Named companies
  appear only as two testimonial quotes.
- **BIN sponsors almost never publish a client list.** They publish curated case
  studies: 2 to 17 logos, hand-picked, months to years old. The one genuine
  client directory found was **Paynetics** (Bulgaria), with 12 named clients at
  stable URLs under `/client/` and a WordPress sitemap that enumerates them.
  Everyone else publishes a marketing subset.

**The load-bearing correction to the brief's premise:** a BIN sponsor's *client
page* is a lagging signal, same as a competitor case study. The leading signal
in this ecosystem is a BIN sponsor's *news page*, where partnership
announcements name a counterparty at the moment of signature. TransactPay names
new partners by name in its news slugs. That is a monthly-cadence signal. The
client logo wall is not.

**Second correction:** the highest-value scheme page in this stream is not a
list at all. Visa's Fintech Fast Track eligibility criteria are, verbatim,
"New to card issuance" and "Have raised at least $3M in funding". That is TXN's
ICP written by Visa. Visa is running an intake funnel for exactly TXN's segment
and publishing the qualification bar but not the queue. Worth a partnership
conversation, not a scrape.

---

## What I could NOT verify

Recorded honestly rather than guessed:

1. **Mastercard Lighthouse (Nordics/Baltics).** Appeared in search results with a
   2026 Spring cohort of 21 companies. Every attempt to fetch the press release
   failed (mastercard.com returns 403 to WebFetch and curl; the reader-proxy
   route returns only the logo alt-text because the newsroom is JS-rendered).
   Recorded as `Reported`, not `Verified`.
2. **Mastercard Network Enablement Partners directory.** Linked from the
   Mastercard Europe navigation, which I did read. The page itself returned 403
   on every method. Cannot confirm whether it is a public list.
3. **Mastercard Engage partner directory.** The directory page loads (430KB) but
   partner records come from an Impartner PRM backend over JS. The solutions
   marketplace confirms 14 solution categories. Partner count and whether it can
   be filtered to European issuers: unknown.
4. **Whether the Visa Partner Directory is enumerable with a real browser.**
   The underlying JSON 404s even with full browser headers. It may be broken for
   everyone, or gated behind login. A headless-browser check would settle it and
   was out of budget here.
5. **AEFI (Spain), Portugal Fintech, Fintech Bulgaria member directories.** All
   three homepages load. The obvious member-list paths 404. The real paths were
   not found before the search budget was exhausted.
6. **Quicko (Poland)**, named as Verestro's EU BIN sponsor. Neither `quicko.pl`
   nor `www.quicko.pl` resolved. Cannot confirm the company is currently trading
   under that domain.
7. **Hungary.** No Hungarian fintech association member directory was located.
   `fintechzone.hu` loads but is an analysis/media site, not a member body.
8. **Romania.** `fintechromania.ro` loads but is a news site. `/membri/` 404s.
   No Romanian association member directory found.
9. **Enfuce customer-stories and partners pages.** Both return HTTP 200 but the
   card grids are JS-rendered; only chrome and navigation are in the HTML. I can
   confirm the pages exist, not what is on them.
10. **The WebSearch budget for this session was exhausted mid-stream** (200/200).
    The later half of the research was done by probing candidate URLs directly
    and keeping only those that returned real content. Several categories,
    notably CEE industry bodies and card fulfilment bureaux, are thinner than
    they should be as a direct result.

---

## Priority ranking for the corpus

| Rank | Source | Why |
|------|--------|-----|
| 1 | Visa Innovation Program Europe JSON API | Open API, 154 companies, country and year tagged, annual refresh, covers ES/PT/GR/BG |
| 2 | The Payments Association member API | Open WP REST, 366 members, continuous churn |
| 3 | TransactPay / OpenPayd / Monavate news pages | Partnership announcements name the counterparty at signature |
| 4 | Paynetics client directory | Only true BIN sponsor client list found; Bulgaria is CEE |
| 5 | Czech Fintech Association member API | Small (18) but it is a CEE priority market with an open API |
| 6 | Holland FinTech / FinTech Belgium member lists | Phase 1b markets, server-rendered, 100+ and 22+ |
| 7 | Visa Fintech Fast Track | Not a list. A partnership target. Eligibility equals TXN's ICP verbatim |

---

# Entries

## Scheme programmes

### Visa Innovation Program Europe

- **Type:** scheme programme
- **Geography:** Greece, Cyprus, Malta, Spain, Portugal, Italy, Bulgaria, Türkiye
- **Homepage:** https://visainnovationprogram.com/
- **List page:** https://visainnovationprogram.com/wp-json/wc/store/v1/products?per_page=100&page=1 (open JSON API, 2 pages). Human-facing equivalent at https://visainnovationprogram.com/fintechs/
- **Publicly listed?** yes
- **Machine readable?** JSON API (WooCommerce Store API v1, unauthenticated, CORS-open, `X-WP-Total` header gives the count)
- **Update cadence:** annual cohort. Year attribute `pa_yil` runs 2019 (13), 2020 (12), 2021 (17), 2022 (21), 2023 (25), 2024 (23), 2025 (21), 2026 (22). The 2026 cohort logos carry `wp-content/uploads/2026/04/` paths, so the 2026 intake was published around April 2026.
- **Why it surfaces card candidates:** Companies in a Visa growth programme are pre-qualified as wanting to work with Visa but are, at cohort entry, generally pre-card. The vertical tag separates the ones that will need issuing (Mobility, Payments, Lending, SME) from the ones that will not. Countries covered include Spain, Portugal and Greece (Phase 1a) and Bulgaria (CEE-adjacent). No Poland, Czechia, Romania or Hungary.
- **Approximate list size:** 154 companies. Country split: Greece/Cyprus/Malta 45, Türkiye 39, Spain/Portugal 34, Bulgaria 19, Italy 16, untagged 1.
- **Confidence:** Verified
- **Evidence:** Fetched the sitemap index, then `wp-sitemap-posts-product-1.xml` (154 URLs), then the Store API for both pages. Response header `x-wp-total: 154`, `x-wp-totalpages: 2`. Each record returns `name`, `description` (with an embedded `<a href>` to the company's own website), `images`, and an `attributes` array carrying `pa_country`, `pa_vertical` and `pa_yil` terms. Confirmed the 2026 cohort as: Vignetim, Sophi, Portuma, Monq, Monetari, Defy, FunniFin, BILLD, Aurea Hub, Unicage, MONEI, Lympid, LIA/Lendit, Dalatea, Coalex AI, Peanuds, Outfindo, GYST, Paytic, Cloudigo, Better, AGRINOW.
- **Notes / gotcha:** The rendered HTML pages sit behind a "SuperJS" JavaScript challenge and return a 364-byte stub to any non-browser client. The XML sitemaps and the `wp-json` API are NOT behind that challenge. Scrape the API, not the site. The same site also exposes an `avada_portfolio` sitemap listing about 80 programme *partners* (Akbank, CaixaBank, Santander, Nexi, Worldline, Intesa Sanpaolo, Bank of Cyprus, Piraeus, Eurobank, TBI Bank, JCC, Cardlink, plus Marqeta, Solaris, Stripe, Adyen, Checkout, N26). That is an ecosystem map, not a lead list.
- **Last checked:** 2026-08-25

### Visa Fintech Fast Track

- **Type:** scheme programme
- **Geography:** global, with regional variance. Visa Direct Fast Track is US-only.
- **Homepage:** https://partner.visa.com/site/programs/fintech-program.html
- **List page:** none. No participant roster is published anywhere on the programme site.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** not applicable (rolling application intake, no published cohort)
- **Why it surfaces card candidates:** It does not surface them as a list. It matters because Visa has written TXN's ICP into its own eligibility criteria. The published qualification bar is: registered corporation in region, good financial standing, **"Not an existing Visa member"**, **"New to card issuance"**, **"Have raised at least $3M in funding"**. Visa is therefore operating an intake funnel for precisely the greenfield segment Ian is targeting, and explicitly promises applicants access to "Visa's relationships with enablement partners (e.g., BIN sponsors, processors, and/or program managers)". The commercial move is to be one of those enablement partners, not to scrape the page.
- **Approximate list size:** unknown, not published
- **Confidence:** Verified
- **Evidence:** Fetched the page (258KB, HTTP 200) and extracted the body text. Confirmed the programme is live under this name as of 2026: it appears in the site's primary navigation alongside Third Party Agent Registration, Visa Licensing Program, Visa Ready Certification and Visa Sensory Branding. Footer reads "Copyright 2026 Visa". The eligibility bullets and the enablement-partner language above are verbatim from the fetched page. The programme name "Fintech Fast Track" is current, not a stale memory: earlier press coverage from 2020-2023 uses the same name and the 2026 nav confirms it.
- **Last checked:** 2026-08-25

### Visa Partner Directory

- **Type:** scheme programme (partner/vendor directory)
- **Geography:** global, filterable by operating country including Poland, Czech Republic, Hungary, Romania and every other EEA market
- **Homepage:** https://partner.visa.com/
- **List page:** https://partner.visa.com/site/partner-directory.html . Filtered example: https://partner.visa.com/site/partner-directory.html?Visa_Ready_Certified_Partners=BIN+Sponsor
- **Publicly listed?** partial
- **Machine readable?** gated (aggregate JSON 404s). Individual partner pages are server-rendered HTML.
- **Update cadence:** unknown. No dated records exposed.
- **Why it surfaces card candidates:** It does not surface buyers. It surfaces the *supply side*: who is certified as a BIN Sponsor or Program Manager in which countries. Useful as a competitive and channel map, i.e. which BIN sponsors to build referral relationships with in CEE, and which processors are already certified there. The `Visa_Ready_Certified_Partners` facet accepts `BIN Sponsor` and `Program Manager` values.
- **Approximate list size:** "hundreds of partners" per the page's own copy. Exact count not retrievable.
- **Confidence:** Verified (with a documented failure)
- **Evidence:** Fetched the directory page (1.19MB, HTTP 200). The country filter is server-rendered as `<input type="checkbox">` elements: confirmed Poland at `multiSelect-177`, plus Czech Republic, Hungary, Romania, Bulgaria, Croatia, Estonia, Latvia, Lithuania, Greece, Portugal, Spain and the rest of the EEA. Partner *records* are not in the HTML. Downloaded the page's own script, `/etc/designs/gpp/clientlib-partnerDirectory.min.js`, and read the two data paths out of it: `/content/dam/gpp/solution-directory/listing/directory.json` and `.../countryList.json`. `countryList.json` returns 200 with `application/json` (5,820 bytes). `directory.json` returns **302 to https://partner.visa.com/site/error/404.html**, with plain headers, with XHR headers, and with a full Chrome header set including `sec-fetch-*`. The directory payload is therefore not publicly retrievable. Individual partner pages ARE public and fully server-rendered: fetched https://partner.visa.com/site/partner-directory/wallester-as.html (264KB, HTTP 200) and read the body, which carries the tag string "White-Label Solutions, B2B Expense, Virtual, Consumer, Business, Crypto Cards, Mobile App, Co-Brand, **BIN Sponsorship**" and the Visa Ready certifications "Wallester - Card Issuer" and "Wallester - Digital Issuance".
- **Notes / gotcha:** partner.visa.com serves an AEM error page for `/robots.txt` and `/sitemap.xml`, so there is no cheap way to enumerate the per-partner URLs. Enumeration would need either a headless browser against the directory page or discovery of partner slugs from elsewhere.
- **Last checked:** 2026-08-25

### Visa Ready certification programme

- **Type:** scheme programme
- **Geography:** global
- **Homepage:** https://partner.visa.com/site/programs/visa-ready.html
- **List page:** none of its own. Certified partners surface through the Visa Partner Directory facet above.
- **Publicly listed?** partial
- **Machine readable?** gated
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Visa Ready certification categories include Card Issuer and Digital Issuance, which is how a processor or BIN sponsor signals capability to the market. Relevant to TXN as a certification path and as a way to read who else is certified in a given market, not as a lead source.
- **Approximate list size:** unknown
- **Confidence:** Verified (page exists and loads, HTTP 200, 269KB)
- **Evidence:** Fetched. Appears in the partner.visa.com primary navigation as a live 2026 programme.
- **Last checked:** 2026-08-25

### Mastercard Start Path

- **Type:** scheme programme
- **Geography:** global, 60+ countries claimed
- **Homepage:** https://www.mastercard.com/global/en/innovation/partner-with-us/start-path.html
- **List page:** **none exists.** There is no portfolio page, no alumni directory, no cohort archive.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** cohorts announced ad hoc via press release, roughly two to three per year based on the release titles seen in search results
- **Why it surfaces card candidates:** In principle a Start Path cohort is a strong greenfield signal. In practice you cannot get the cohort from Mastercard in list form. The stage criterion published on the page is "Investment raised (Seed, Series A or later) with product live in market and generating revenue", which skews later than Visa's programme and therefore slightly later than TXN's ideal entry point.
- **Approximate list size:** "500+ startups in 60+ countries" claimed on the page. Zero of them named on it.
- **Confidence:** Verified (verified that the list does not exist)
- **Evidence:** Full page text retrieved via a reader proxy after mastercard.com returned 403 to both WebFetch and curl. The page carries the stats block (500+ startups, $25b+ capital raised post-program, 15,000+ brokered connections), the four selection criteria, the four-step process, nine programme tracks (Agentic Commerce & Services, Acceptance, Blockchain & digital assets, Emerging & consumer tech, Open finance, Small business, Security solutions, Corporate Solutions, Business and Market Insights), a "For corporates" block and an FAQ. It contains no company names and no link to any roster. Third-party aggregators (Crunchbase hub, CB Insights investor profile) reconstruct the portfolio; Mastercard itself does not publish it.
- **Notes / gotcha:** mastercard.com is behind Akamai and returns 403 to WebFetch, to curl with a full Chrome header set, and to the archive-availability path for the newsroom. A reader proxy got the marketing pages but returned only logo alt-text for newsroom press releases, which are JS-rendered. Any ongoing monitoring of Start Path cohorts needs a real browser or a third-party feed.
- **Last checked:** 2026-08-25

### Mastercard For Fintechs (Europe), third edition 2026

- **Type:** scheme programme
- **Geography:** France, Belgium, Luxembourg, Netherlands, Spain, Portugal, Italy
- **Homepage:** https://www.mastercard.com/europe/en/innovation/partner-with-us/mastercardforfintechs.html
- **List page:** no participant list. Per-event pages exist: `/iberia-event-details.html`, `/italy-event-details.html`, `/france-event-details.html`, `/netherlands-event-details.html`, `/final-event-details.html`
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** annual, with local competition events June to October and the final in Milan on 25 November 2026
- **Why it surfaces card candidates:** Eligibility is "pre-seed / seed / Series A fintechs with a live solution" in one of seven Western European markets, and the target verticals named on the page include Embedded finance 2.0, SME software & B2B automation, Digital Banking & Lending, HR tech & employee benefits and Loyalty & Retail tech. Every one of those is a card-issuing candidate. The winner is fast-tracked into Start Path. The geography overlaps TXN Phase 1a (Spain, Portugal) and Phase 1b (Netherlands, Belgium) but reaches no CEE market.
- **Approximate list size:** "over 100 European startups engaged and more than 20 fintechs competing" across the first two editions, per the launch press release seen in search results. Not enumerable.
- **Confidence:** Verified (page), Reported (the 100/20 figures)
- **Evidence:** Full page text retrieved via reader proxy (63KB). Confirmed: 2026 third edition is live; local events at Paris 22 Sep 2026, Amsterdam 8 Oct 2026, final Milan 25 Nov 2026; prize is 100,000 EUR marketing support plus Start Path fast-track; application form at `https://form.mastercard.com/jfe/form/SV_6y5TxliUkBjdMeq`; contact `mastercardforfintechs@mastercard.com`. The nine target verticals are listed verbatim on the page. **The participating-countries list is published only as an SVG image**, so the country set above comes from the press-release summary, not from page text. Only two participant companies are named anywhere on the page, both as testimonial quotes: **GoDutch** (winner, Benelux) and **Rauva** (Portugal). The page also names about 40 programme partners as SVG filenames, which is a usable adjacent list: Seaya, Kfund, Samaipata, Draper B1, Adara Ventures, Truffle Capital, Lumen Ventures, Armilar, Easo Ventures, Kibo Ventures, Proximity Capital, Cardumen Capital, Actyus, GoHub, Plug and Play, Seedstars, Wayra, Lanzadera, Endeavor, Google for Startups, Startup Valencia, Barcelona Finance Hub, Unicorn Factory, 4YFN, South Summit, AEFI, Fintech Belgium, Finance Innovation, CaixaBank, Santander, BBVA, Sabadell BStartup, Unicaja, Skaleet, Square, Herbert Smith, Andersen, Asensi Abogados, ICDICO, IAG.
- **Notes / gotcha:** The event-detail pages were identified but not fetched. If any of them publish a finalist shortlist, that is the participant list this programme otherwise lacks. Worth 20 minutes of follow-up before the Milan final in November.
- **Last checked:** 2026-08-25

### Mastercard Engage partner directory

- **Type:** scheme programme (partner/vendor directory)
- **Geography:** global, with an explicit Europe region facet
- **Homepage:** https://engagepartners.mastercard.com/
- **List page:** https://engagepartners.mastercard.com/English/directory/ and https://engagepartners.mastercard.com/English/solutions/
- **Publicly listed?** partial
- **Machine readable?** JS-rendered (Impartner PRM backend served from `prod.prmcdn.io`)
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Same shape as the Visa Partner Directory: this is the supply side, not the buyer. Its value to TXN is as a certification and channel map, and as a way to see which enablement partners Mastercard is steering fintechs toward in Europe.
- **Approximate list size:** unknown. The adjacent solutions marketplace returns exactly 14 solution categories including Acceptance, Authentication, Commercial and Crypto.
- **Confidence:** Verified (pages load), Unverified (partner records)
- **Evidence:** Fetched `/English/directory/` (430KB, HTTP 200) and `/English/solutions/` (180KB, HTTP 200). The solutions page is server-rendered and states "1-14 (14 results)". The directory page contains facet scaffolding and a filter UI but no partner records in the HTML. Downloaded `/js/marketplace.js` (104KB) and found no data endpoint in it. A direct search URL with `pageSize=100` returned HTTP 406. Extracting the partner list needs a headless browser.
- **Last checked:** 2026-08-25

### Mastercard Lighthouse (Nordics and Baltics)

- **Type:** scheme programme
- **Geography:** Nordic and Baltic markets
- **Homepage:** unknown. Announcements appear under https://www.mastercard.com/news/europe/en/newsroom/press-releases/
- **List page:** https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2026/nordic-startups-named-winners-of-mastercard-lighthouse-spring-2026/
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** appears to run Spring and Autumn programmes
- **Why it surfaces card candidates:** A regional Mastercard fintech programme naming a full cohort would be a direct greenfield signal. Baltic markets (Estonia, Latvia, Lithuania) are EEA and are where a large share of European EMI licences sit.
- **Approximate list size:** 21 companies in the Spring 2026 programme, per the press-release headline
- **Confidence:** Reported
- **Evidence:** The URL and the headline "Mastercard Lighthouse 2026 Spring program welcomes 21 forward-looking Nordic and Baltic fintech and impact companies" came from a web search result. **The page itself could not be fetched.** curl returns 403, WebFetch returns 403, and the reader proxy returns only the Mastercard logo alt-text because the newsroom is JS-rendered. `lighthouse.mastercard.com` and `mastercardlighthouse.com` both fail DNS resolution. I have not read this page and am not claiming its contents.
- **Last checked:** 2026-08-25

### Mastercard Network Enablement Partners directory (Europe)

- **Type:** scheme programme (partner directory)
- **Geography:** Europe
- **Homepage:** https://www.mastercard.com/europe/en/business/support/network-enablement-partners.html
- **List page:** same URL
- **Publicly listed?** unknown
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** NEPs are the Mastercard-side equivalent of Visa Ready enablers, i.e. processors, programme managers and BIN sponsors. If the directory is public and filterable it is the Mastercard counterpart to the Visa Partner Directory entry above.
- **Approximate list size:** unknown
- **Confidence:** Unverified
- **Evidence:** The link was extracted from the fetched Mastercard Europe navigation (it sits under "For business, Partner programs" and again under "For business, Support"), so the page definitely exists. Every attempt to fetch it returned HTTP 403, including curl with full Chrome headers and the `/us/en/` variant of the same path. Not read.
- **Last checked:** 2026-08-25

### EMVCo Approved Products and Solutions (3-D Secure)

- **Type:** register
- **Geography:** global
- **Homepage:** https://www.emvco.com/approved-products/
- **List page:** https://www.emvco.com/approved-products/?type=3-d_secure . RSS at https://www.emvco.com/approved-products/feed/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with a type facet, plus an RSS feed. Each approval also has a Letter of Approval PDF at `wp-content/uploads/loa/`.
- **Update cadence:** continuous. LOA filenames carry approval dates: the most recent seen in the fetched page is `3DS_LOA_SER_CLAS_020301_01276_09Jul26.pdf` (9 July 2026), with others from Nov and Dec 2025 and May 2026.
- **Why it surfaces card candidates:** Weakly, and honestly this is the lowest-value entry in the stream. EMVCo approves *products* (3DS Servers, ACS, SDKs) held by *vendors*, not card programmes held by issuers. A new ACS approval tells you a vendor shipped a version, not that a fintech is launching a card. Recorded because the brief asked for 3DS providers, and because the RSS feed is a genuine zero-cost change signal for the vendor layer.
- **Approximate list size:** unknown. Paginated (page/2/ exists).
- **Confidence:** Verified
- **Evidence:** Fetched `/approved-products/` (357KB, HTTP 200), read the navigation and extracted the facet URLs and LOA PDF links listed above. Note that `/approvals/`, `/registered-products/` and `/3ds-product-registration/` all 404. The current path is `/approved-products/`.
- **Last checked:** 2026-08-25

---

## BIN sponsors and programme managers

### Paynetics (Bulgaria)

- **Type:** BIN sponsor
- **Geography:** Bulgaria, UK, EEA passporting
- **Homepage:** https://paynetics.digital/
- **List page:** https://www.paynetics.digital/project-sitemap.xml (12 client URLs). Individual pages at `https://www.paynetics.digital/client/<slug>/`
- **Publicly listed?** yes
- **Machine readable?** XML sitemap plus HTML cards
- **Update cadence:** slow. 12 entries total, so this is a curated reference set rather than a live client register. The sitemap gives `lastmod` per entry, which makes new additions detectable without diffing the HTML.
- **Why it surfaces card candidates:** The only genuine client *directory* found across every BIN sponsor checked in this stream. Bulgaria is the closest thing to a CEE anchor in the sponsor layer, and Paynetics sponsors both its own market and UK/EEA programmes. Reading the list tells you which programme types Paynetics wins, which tells you which ones it is losing.
- **Approximate list size:** 12 named clients: microcredit, tbi-bank, weavr, pay-by-vivacom, fibonatix, ad-cards, smartone, dna, benamic-2, billbutler, a1-wallet, trading212.
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (280KB, HTTP 200) and extracted 14 `/client/` links from it. `/clients/` itself 404s, so the index page is elsewhere. The sitemap index at `/sitemap_index.xml` lists a `project-sitemap.xml` which I fetched and which returns exactly 12 client URLs. Note the client set is a mix of true fintechs (Trading 212, Weavr, Fibonatix) and telco/retail programmes (A1 Wallet, Vivacom, TBI Bank).
- **Last checked:** 2026-08-25

### TransactPay (Gibraltar / UK / EEA), being acquired by Marqeta

- **Type:** BIN sponsor
- **Geography:** UK and EEA
- **Homepage:** https://transactpay.com/
- **List page:** https://transactpay.com/case-studies/ (2 entries) and, more usefully, https://transactpay.com/news/
- **Publicly listed?** partial
- **Machine readable?** HTML cards. No RSS (`/feed/` 404s).
- **Update cadence:** the news page is the live one. Slugs fetched include `transactpay-and-orenda-finance-partner-to-accelerate-embedded-finance-across-europe`, `transactpay-and-setld-pay-partner-to-simplify-payment-solutions`, `transactpay-and-zero-partner-to-launch-game-changing-sustainable-payment-card`, `transactpay-partners-with-griffin-to-strengthen-its-uk-banking-infrastructure`, `transactpay-joins-forces-with-triple`, `tell-money-to-enable-seamless-open-banking-for-clients`.
- **Why it surfaces card candidates:** This is the pattern worth generalising across the whole sponsor layer. A BIN sponsor's *case studies* are a lagging marketing artefact (2 entries, curated). Its *news page* names a new counterparty at the moment the partnership is signed, months before the card launches. Orenda Finance, Setld Pay and Zero all appear in slugs as named counterparties. That is a monthly-cadence, name-bearing signal available from a single HTML page.
- **Approximate list size:** 2 case studies (payac, tymit). 13+ news slugs on page 1, paginated.
- **Confidence:** Verified
- **Evidence:** Fetched `/services/bin-sponsorship/` (248KB), `/case-studies/` (246KB) and `/news/` (1.76MB), all HTTP 200, and extracted the slugs above. **Ownership change:** the news index carries the slug `marqeta-to-acquire-transactpay`, and the company also carries `transact-payments-rebrands-to-transactpay`. Treat "Transact Payments Limited / TPML" and "TransactPay" as the same entity, and expect this sponsor to be folded into Marqeta.
- **Last checked:** 2026-08-25

### Solaris (Germany)

- **Type:** BIN sponsor / BaaS
- **Geography:** Germany, EEA
- **Homepage:** https://www.solarisgroup.com/en/
- **List page:** https://www.solarisgroup.com/en/case-studies/ and https://www.solarisgroup.com/en/ecosystem-partners/
- **Publicly listed?** partial
- **Machine readable?** HTML cards (case studies). The ecosystem-partners page yielded no extractable slugs.
- **Update cadence:** slow, curated
- **Why it surfaces card candidates:** Solaris clients are the archetype of the segment TXN wants to displace *after* it exists, not before. Its value here is as a competitive read on the German and DACH programme layer. Also relevant: Solaris absorbed Contis, so historic Contis programmes now sit here.
- **Approximate list size:** 9 case studies: admirals, clanq, finom, grover, lexware, navit, samsung, spendit, tomorrow
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (326KB) and `/en/case-studies/` (297KB), both HTTP 200, and extracted the 9 slugs. `/en/ecosystem-partners/` returns HTTP 200 (217KB) but the partner grid is not in the HTML.
- **Last checked:** 2026-08-25

### Swan (France)

- **Type:** BaaS / programme manager
- **Geography:** France, Germany, Spain, Italy, Netherlands, Belgium
- **Homepage:** https://swan.io/
- **List page:** https://swan.io/customers
- **Publicly listed?** yes
- **Machine readable?** HTML cards, server-rendered
- **Update cadence:** slow, curated. No RSS (`/rss.xml` 404s).
- **Why it surfaces card candidates:** Swan's client base is almost entirely **vertical SaaS companies that added embedded finance**: accounting software (Pennylane, MyUnisoft, Fulll), HR software (Lucca), expense tools (Expensya, Libeo), cashflow tools (Agicap), invoicing (Axonaut, Sibill), insurtech (Betterfly). That is exactly the "vertical SaaS business that will need cards and does not know it yet" archetype the brief asks for. Read this list not as prospects (they have already chosen) but as a **taxonomy**: it tells you which vertical-SaaS categories in France, Italy, Spain and Belgium convert to card programmes, so the same categories can be prospected in Poland, Czechia, Romania and Hungary where no Swan equivalent has reached yet.
- **Approximate list size:** 14 customer stories
- **Confidence:** Verified
- **Evidence:** Fetched https://swan.io/customers (487KB, HTTP 200) and extracted 14 `/customer-stories/` slugs: accountable-partnership, agicap, axonaut-partnership, betterfly-partner-story, indy, expensya, fulll-partnership, libeo, lucca, myunisoft-partnership, pennylane-partnership, pennylane-wallet, sibill-partner-story, and one Belgian proptech.
- **Last checked:** 2026-08-25

### Treezor (France, Societe Generale)

- **Type:** BIN sponsor / BaaS
- **Geography:** France, EEA
- **Homepage:** https://www.treezor.com/en/
- **List page:** https://www.treezor.com/en/insights/success-stories/
- **Publicly listed?** yes
- **Machine readable?** HTML cards
- **Update cadence:** slow, curated
- **Why it surfaces card candidates:** Same taxonomy value as Swan, one tier more mature. The named programmes (Qonto, Lydia, Shine, Swile, Skipr, Cashbee, Coinhouse, VeraCash, Tiime) map the French embedded-finance categories that reached card issuance.
- **Approximate list size:** 9 success stories
- **Confidence:** Verified
- **Evidence:** Fetched the site (145KB, HTTP 200) and extracted 9 `/insights/success-stories/` slugs: cashbee, coinhouse-and-treezor-cryptoassets, lydia, qonto, shine, skipr, swile, tiime-and-treezor-modernizing-sme-accounting, veracash-treezor-precious-metals-payment-innovation.
- **Last checked:** 2026-08-25

### B4B Payments (UK, Banking Circle group)

- **Type:** BIN sponsor / programme manager
- **Geography:** UK, EEA, with a dedicated France presence
- **Homepage:** https://www.b4bpayments.com/
- **List page:** https://www.b4bpayments.com/c/case-studies
- **Publicly listed?** yes
- **Machine readable?** HTML cards (HubSpot CMS)
- **Update cadence:** slow, curated
- **Why it surfaces card candidates:** The client mix is instructive and mostly *not* fintech: charities, NGOs, media agencies, temporary-staffing payouts, travel, churches, a cricket World Cup. This is the disbursement and prepaid corner of the market. Relevant to TXN as a reminder that a meaningful slice of greenfield card issuance is bought by non-financial organisations that would never appear in a fintech register or an accelerator cohort.
- **Approximate list size:** 17 case-study slugs
- **Confidence:** Verified
- **Evidence:** Fetched the homepage (158KB) and `/c/case-studies` (114KB), both HTTP 200, and extracted 17 slugs including `b4b-in-france`, `bunzl-case-study`, `education-first-simplified-travel-payment-process`, `idee-per-viaggiare-case-study`, `alpha-contract-solutions...unbanked-workers`, `b4b-payments-has-partnered-with-hps-to-deliver-streamlined-and-efficient-payroll-services`.
- **Last checked:** 2026-08-25

### Monavate (UK)

- **Type:** BIN sponsor / issuer
- **Geography:** UK, EEA
- **Homepage:** https://www.monavate.com/
- **List page:** https://www.monavate.com/case-studies plus https://www.monavate.com/newsroom
- **Publicly listed?** yes
- **Machine readable?** HTML cards. No RSS (`/feed/` 404s).
- **Update cadence:** slow. Most recent case study on the fetched page is dated 3 November 2024.
- **Why it surfaces card candidates:** Small but clean client list with sector labels (Fintech, Web3, Travel, Insurance, Media Buyers, Fleet). The sector taxonomy is more useful than the four logos: it is Monavate telling you which verticals are currently buying card programmes.
- **Approximate list size:** 4 case studies: Baanx (blockchain), HyperJar (consumer spending), a responsible-lending programme, a healthcare payments programme
- **Confidence:** Verified
- **Evidence:** Fetched https://www.monavate.com/ (101KB) and `/case-studies` (36KB), both HTTP 200, and read the body text and slugs.
- **Last checked:** 2026-08-25

### IDT Financial Services (Gibraltar)

- **Type:** BIN sponsor
- **Geography:** Gibraltar, EEA, UK. Visa Europe principal member and Mastercard licensee.
- **Homepage:** https://www.idtfinance.com/
- **List page:** https://www.idtfinance.com/clients/
- **Publicly listed?** yes
- **Machine readable?** HTML logo wall (client names recoverable from image `alt` attributes)
- **Update cadence:** slow, curated
- **Why it surfaces card candidates:** Publishes both a client wall and a partner wall on the same page, which is unusual and useful. Clients read as consumer and youth prepaid and benefit programmes (gohenry, Osper, Crunch, Laya, Gant, Gema, PayUno, Marbar International). Partners name the processor layer the sponsor works with (GPS, i2c, Prismo, Thales, Feedzai, Tell.money, TAGnitecrest, FIS). That partner wall is effectively a map of who TXN would be displacing on a given programme.
- **Approximate list size:** about 10 clients and about 10 partners
- **Confidence:** Verified
- **Evidence:** Fetched https://www.idtfinance.com/clients/ (49KB, HTTP 200), read the body text ("Partnerships are in our DNA and we collaborate with a wide range of both clients and partners... Our clients / Case studies / Our partners") and extracted 28 image alt attributes, from which the names above are taken.
- **Last checked:** 2026-08-25

### Wallester (Estonia)

- **Type:** BIN sponsor / issuer-processor
- **Geography:** EEA and UK. Visa principal member.
- **Homepage:** https://wallester.com/
- **List page:** none found on wallester.com. The best public record of its capability is its Visa Partner page: https://partner.visa.com/site/partner-directory/wallester-as.html
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** not applicable
- **Why it surfaces card candidates:** As a Visa Ready certified Card Issuer and Digital Issuance partner offering BIN sponsorship out of Estonia, Wallester is a direct competitor to TXN in the Baltic and CEE corridor rather than a lead source. Its Visa Partner page is the cleanest single-page statement of a competitor's positioning found in this stream.
- **Approximate list size:** not applicable
- **Confidence:** Verified
- **Evidence:** Fetched https://wallester.com/ (293KB, HTTP 200) and read the body: the homepage sells business and freelancer IBAN accounts and white-label issuing, with no customer list, no case studies and no press page in the navigation. Separately fetched the Visa partner page (264KB, HTTP 200) which carries the BIN Sponsorship tag and the two Visa Ready certifications.
- **Last checked:** 2026-08-25

### Verestro (Poland)

- **Type:** programme manager / issuing technology, BIN sponsorship via a partner payment institution
- **Geography:** Poland and EU
- **Homepage:** https://www.verestro.com/card-issuing
- **List page:** https://www.verestro.com/blog/categories/case-studies
- **Publicly listed?** partial
- **Machine readable?** HTML cards. A blog feed exists at https://www.verestro.com/blog-feed.xml but returned only one item when fetched.
- **Update cadence:** unknown
- **Why it surfaces card candidates:** The most significant Polish name in the issuing supply chain, and Poland is TXN's top MVP market. Verestro provides the technology. Per its own materials the EU BIN sponsorship is supplied by **Quicko**, a licensed Polish payment institution. That two-party structure matters: a Polish fintech buying Verestro has taken a technology decision that TXN would need to displace, whereas one that has only signed Quicko may still be processor-shopping.
- **Approximate list size:** unknown. The case-studies category page loads (1.12MB) but individual client slugs were not extracted.
- **Confidence:** Verified (Verestro pages), Unverified (Quicko)
- **Evidence:** Fetched https://www.verestro.com/card-issuing (2.09MB, HTTP 200) and the case-studies category page (1.12MB, HTTP 200). **Quicko could not be verified:** neither `https://quicko.pl/` nor `https://www.quicko.pl/` resolved (curl exit, no HTTP response). The Verestro and Quicko relationship is `Reported` from a search-result summary, not from a fetched page.
- **Last checked:** 2026-08-25

### Equals Money, and the disappearance of Railsr

- **Type:** BIN sponsor / programme manager
- **Geography:** UK, EEA
- **Homepage:** https://www.equalsmoney.com/
- **List page:** https://www.equalsmoney.com/case-studies and https://www.equalsmoney.com/newsroom
- **Publicly listed?** yes
- **Machine readable?** HTML cards
- **Update cadence:** slow, curated
- **Why it surfaces card candidates:** **Defunct-is-a-finding entry.** `https://www.railsr.com/` now returns the Equals Money site: byte-identical response size (306,350 bytes) and identical `<title>` ("Embedded payments, simply served | Equals") to `https://www.equalsmoney.com/`. Railsr, formerly Railsbank, one of the most-referenced European BaaS and BIN-sponsor names, no longer exists as a distinct web presence. Any corpus entry, competitor list or ICP note that still treats Railsr as a live independent sponsor is stale. Consolidation in this layer is fast: Railsr into Equals, Contis into Solaris, TransactPay into Marqeta, Netcetera into G+D, all four confirmed in this pass.
- **Approximate list size:** case studies include equals-money-ahmad-tea, sargasso-grey, team-evolution
- **Confidence:** Verified
- **Evidence:** Fetched both `https://www.railsr.com/` and `https://www.equalsmoney.com/` in the same batch. Both HTTP 200, both 306,350 bytes, both titled "Embedded payments, simply served | Equals". Extracted `/case-studies` and `/newsroom` link paths from the response body.
- **Last checked:** 2026-08-25

### OpenPayd

- **Type:** BaaS / programme manager
- **Geography:** UK, EEA
- **Homepage:** https://openpayd.com/
- **List page:** no client list. https://openpayd.com/feed/ is a **working RSS feed with 10 items**.
- **Publicly listed?** no (clients), yes (news)
- **Machine readable?** RSS
- **Update cadence:** live. This was one of only two working RSS feeds found across fourteen sponsor and programme-manager sites tested.
- **Why it surfaces card candidates:** No client list, but a functioning feed. For the "ongoing" job in the brief, a working RSS feed on a sponsor's newsroom is worth more than a static client wall, because partnership announcements name counterparties. Cheap to poll.
- **Approximate list size:** 10 items in the current feed window
- **Confidence:** Verified
- **Evidence:** Fetched https://openpayd.com/ (90KB, HTTP 200). No customers or case-studies link in the navigation, only `/blog/`. Fetched `https://openpayd.com/feed/`, HTTP 200, 10 `<item>` elements.
- **Last checked:** 2026-08-25

### Other BIN sponsors and programme managers checked

Recorded as one entry rather than fifteen thin ones, because the finding for each
is the same: the site is live, and it does not publish a client list.

- **Type:** BIN sponsor / programme manager
- **Geography:** UK, EEA, various
- **Publicly listed?** no
- **Machine readable?** no list
- **Confidence:** Verified (each URL fetched, HTTP 200, navigation and link structure read)
- **Evidence and per-company finding:**
  - **Enfuce** (Finland/UK): https://enfuce.com/payment-solutions/bin-sponsorship/ 200. `/solutions/customer-stories` and `/who-we-are/partners` both exist and return 200, but the card grids are JS-rendered and only navigation chrome is in the HTML. Enfuce publishes customer stories; they are **not extractable without a browser**. `/customers/` 404s. No RSS.
  - **Modulr** (UK/Netherlands): https://www.modulrfinance.com/ 200. Case studies exist at `/case-studies` with 7+ named slugs (Teya, Motorway, Martin Aitken & Co, Makars Mash Bar, Accountability Edinburgh). SME and accountancy adjacent, same taxonomy value as Swan.
  - **Vodeno** (Belgium/Poland): https://vodeno.com/ 200. No client list. `/feed/` returns 200 but zero items. Notable for Poland exposure; nothing published.
  - **Paynovate** (Belgium): https://paynovate.com/ 200. Only `/partner/pos` and `/partner/reseller` channel pages. No client list, no RSS.
  - **Weavr** (UK): https://www.weavr.io/ 200 and `/embedded-finance-case-studies/` 200, but no case-study slugs in the HTML. Also appears as a *client* on the Paynetics list, which is a useful reminder that this layer is recursive.
  - **DiPocket**: https://dipocket.org/en/bin-sponsorship-explained-the-complete-guide/ 200. Content-marketing guide only, no client list at that URL.
  - **EML Payments**: https://www.emlpayments.com/ 200. `/case-studies` returns the homepage (same 177,117 bytes), i.e. **no case-study index exists**.
  - **Moorwand**: https://www.moorwand.com/ 200, still trading. Navigation includes About Us, Partners, Issuing Services, News & Insights Hub. No client list extracted. Recorded because Moorwand has been widely reported as troubled; the site is live as of this check.
  - **Unlimit**, **Satchel** (Lithuania), **iCard** (Bulgaria), **Decta** (Latvia), **Tribe Payments**, **Paymentology**, **Pannovate**: all fetched, all HTTP 200, none publish an enumerable client list. Decta `/case-studies` 404s. Paymentology `/customers` 404s. Tribe `/customers` 404s but `/case-studies` and `/news` exist. Pannovate returns a 1.7KB placeholder page.
  - **Thredd** (UK): https://www.thredd.com/ returns **HTTP 403 behind a Cloudflare interstitial** ("Just a moment..."). Could not be assessed.
  - **FINCI**: `https://finci.io/` did not resolve. Correct domain not established.
- **Last checked:** 2026-08-25

---

## Industry bodies and member directories

### The Payments Association

- **Type:** community / trade association
- **Geography:** UK primarily, with a separate EU arm
- **Homepage:** https://thepaymentsassociation.org/
- **List page:** https://thepaymentsassociation.org/members/ . **Open API at** https://thepaymentsassociation.org/wp-json/wp/v2/directory?per_page=100&_fields=id,title,link
- **Publicly listed?** yes
- **Machine readable?** JSON (WordPress REST API, unauthenticated, `X-WP-Total` header exposed)
- **Update cadence:** continuous. Membership churns as companies join and lapse. The REST API exposes post dates for diffing.
- **Why it surfaces card candidates:** 366 members spanning issuers, PSPs, processors, law firms, auditors and, critically, a long tail of small UK payments companies that have joined a trade body *before* launching a product. Joining a payments trade association is a commitment signal that precedes a card programme. The membership also includes many companies that are not yet card issuers but are adjacent (RelyComply, ReconArt, Guardexia, MADFIN TECH, Advapay, PayDo, Peratera, Currency Stream). UK is "opportunistic" in TXN's market tiering, so this is volume rather than priority, but it is the highest-volume open API found in this stream.
- **Approximate list size:** 366 members
- **Confidence:** Verified
- **Evidence:** Fetched `/members/` (272KB, HTTP 200) and found it JavaScript-rendered via Elementor and JetEngine, with no member records in the HTML. Fetched `/wp-json/wp/v2/types` and identified the custom post type `directory` with label "Members". Fetched `/wp-json/wp/v2/directory?per_page=100`. Response header `x-wp-total: 366`, `x-wp-totalpages: 4`. First 30 titles confirmed, including Pay.UK, Capital One, Shift4 Payments UK, Wirex, BridgerPay, Adflex, Mindgate Solutions, RSM UK, MHA Baker Tilly.
- **Last checked:** 2026-08-25

### Electronic Money Association (EMA)

- **Type:** community / trade association
- **Geography:** UK and EU, with local branches in Belgium, Ireland, Lithuania, Luxembourg, Malta and the Netherlands
- **Homepage:** https://www.e-ma.org/
- **List page:** https://www.e-ma.org/our-members
- **Publicly listed?** yes
- **Machine readable?** HTML, fully server-rendered as a plain text list
- **Update cadence:** unknown. No dates exposed.
- **Why it surfaces card candidates:** This is the EMI layer, i.e. the companies that hold or are pursuing e-money authorisation across the EEA, which is the regulatory prerequisite for many card programmes. Membership is heavily skewed to companies that already issue, so it is a competitor and incumbent map more than a greenfield list. Its real value is the **local branches**: EMA Lithuania, EMA Malta, EMA Belgium and EMA Ireland are where newly-authorised EMIs cluster.
- **Approximate list size:** about 100 named members. Confirmed present in the fetched text: 3S Money, Aircash, Airwallex UK, Aplauz NL, Banked, BCB Digital, Blackhawk Network EMEA, Boku, BVNK, Cardaq, CashFlows, Currenxie, Decta, ECOMMPAY, emerchantpay, EML Payments, EPG Financial Services, Finance Incorporated, Financial House, FinXP, Globepay, IDT Financial Services, iFAST Global Bank, Imagor, Loodapay LU, Modulr Finance B.V., MONAVATE, MONETLEY, Moorwand, MuchBetter, myPOS Payments, Navro, Newrails UAB, Nium Solutions, Nuvei Financial Services, OpenPayd, Owl Payments Europe, pay.cetera, Papaya Global/Azimo, Park Card Services, Payhawk Financial Services, Paysend EU DAC, Peratera, Pleo Financial Services, PPS, Push Labs, Satispay Europe, plus the large platforms (Amazon, Airbnb, eBay, Etsy, Google Payment, PayPal, Revolut, Ripple, Coinbase, Kraken, Circle, Crypto.com, OKX, Bitstamp).
- **Confidence:** Verified
- **Evidence:** Fetched https://www.e-ma.org/our-members (198KB, HTTP 200) and stripped tags to recover the member list as plain text under the heading "The current EMA membership". `/members` and `/membership` both 404. `/our-members` is the correct path. Cross-check value: **Moorwand, Monavate, IDT Financial Services, Decta, PPS, Modulr and OpenPayd all appear here and in the BIN-sponsor entries above**, which is a cheap way to confirm a sponsor is still authorised and trading.
- **Last checked:** 2026-08-25

### Holland FinTech

- **Type:** community / trade association
- **Geography:** Netherlands (TXN Phase 1b)
- **Homepage:** https://hollandfintech.com/
- **List page:** https://hollandfintech.com/members/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, server-rendered, one page per member at `/members/<slug>/`
- **Update cadence:** unknown. No sitemap (`sitemap_index.xml` returns empty) and no WordPress REST API, so change detection means diffing the members page.
- **Why it surfaces card candidates:** Largest member directory found in a Phase 1b market. The membership is broad, spanning startups, banks, consultancies and infrastructure vendors, so it needs filtering, but Dutch fintechs that have joined the national body and not yet launched a card are exactly the greenfield profile.
- **Approximate list size:** 100 member slugs recovered from page 1. Pagination is not at `/members/page/2/` (404), so the full count is higher and the mechanism is likely AJAX. First slugs confirmed: 3s-money, accenture, ace-company, adup, aera-payment-identification, afs-group, airwallex, allshare-b-v, altfin, alveo-technology, amazon-web-services-aws, amrop-executive-search, anthos-fund, apg, aurus.
- **Confidence:** Verified
- **Evidence:** Fetched https://hollandfintech.com/members/ (576KB, HTTP 200) and extracted 100 unique `/members/<slug>/` paths from the HTML. Confirmed no WP REST API and no working sitemap.
- **Last checked:** 2026-08-25

### FinTech Belgium

- **Type:** community / trade association
- **Geography:** Belgium (TXN Phase 1b)
- **Homepage:** https://fintechbelgium.be/
- **List page:** https://fintechbelgium.be/members/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, server-rendered, paginated
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Belgian national body, Phase 1b market. Also appears as a named programme partner on Mastercard For Fintechs, which means its member list and the Mastercard Benelux competition pool substantially overlap. A cheap cross-reference.
- **Approximate list size:** 22 slugs on page 1 (a-cube, abbove, aerapayment, aguilonius, almaxtech, area42, bancontact, basikon, byqwest, cerrix, coeo, contractfit, copla, craft and others). Paginated, so total is higher.
- **Confidence:** Verified
- **Evidence:** Fetched https://fintechbelgium.be/members/ (248KB, HTTP 200), title "FinTech Belgium's members", and extracted 22 `/members/<slug>` paths. No WP REST API exposed.
- **Last checked:** 2026-08-25

### Czech Fintech Association (Fintech asociace)

- **Type:** community / trade association
- **Geography:** Czech Republic (TXN **MVP market**)
- **Homepage:** https://www.czechfintech.cz/
- **List page:** **open API at** https://www.czechfintech.cz/wp-json/wp/v2/members?per_page=100
- **Publicly listed?** yes
- **Machine readable?** JSON (WordPress REST API, custom post type `members`, label "Členové", unauthenticated)
- **Update cadence:** slow, given the size. The REST API exposes post dates, so additions are trivially detectable.
- **Why it surfaces card candidates:** Small, but this is one of the four MVP markets and it is a complete national member register behind an open API. Every Czech fintech that has bothered to join the national body is here. At 18 members it is short enough to review by hand and long enough to be worth reviewing.
- **Approximate list size:** 18 members: Hobza Legal, Platební instituce Roger a.s., Lemonero, CITFIN, FINREG PARTNERS, FlexiFin, PayU, Five Crafts, Coinmate, Flowpay, ADACTA, Patron GO, Metada, BudgetBakers, AKCENTA, CRIF Czech Credit Bureau, SCHEJBAL & PARTNERS, Comgate.
- **Confidence:** Verified
- **Evidence:** Fetched `/wp-json/wp/v2/types`, identified the `members` post type with Czech label "Členové", then fetched `/wp-json/wp/v2/members?per_page=100`. Response header `x-wp-total: 18`, `x-wp-totalpages: 1`. All 18 titles listed above are from the fetched payload. Note **Lemonero also appears in the Visa Innovation Program Europe participant list**, the first confirmed cross-hit between two independent sources in this stream, and a template for scoring.
- **Last checked:** 2026-08-25

### Fintech Poland

- **Type:** community / trade association
- **Geography:** Poland (TXN **MVP market**, highest priority)
- **Homepage:** https://fintechpoland.com/
- **List page:** none retrievable. A custom post type `um_directory` labelled "Member Directories" exists but https://fintechpoland.com/wp-json/wp/v2/um_directory?per_page=100 returned only 865 bytes, i.e. effectively empty.
- **Publicly listed?** no (as far as could be established)
- **Machine readable?** no usable list
- **Update cadence:** not applicable
- **Why it surfaces card candidates:** It would be the single most valuable industry body in this stream if it published members, because Poland is the top MVP market. It appears not to, or to gate the directory behind Ultimate Member login (the `um_` prefix is the Ultimate Member plugin, which supports members-only directories).
- **Approximate list size:** unknown
- **Confidence:** Verified (that the public API returns nothing usable), Unverified (whether a member list exists elsewhere on the site)
- **Evidence:** Fetched https://fintechpoland.com/ (172KB, HTTP 200). Fetched `/wp-json/wp/v2/types` and found `um_directory` labelled "Member Directories". Fetched that endpoint: HTTP 200, 865 bytes. **Follow-up worth doing:** the Ultimate Member plugin usually renders its directory on a normal page; that page was not located before the search budget ran out.
- **Last checked:** 2026-08-25

### CEE and Southern Europe industry bodies: negative results

Recorded because the brief asked, and because a documented dead end saves the
next researcher the same hour.

- **Type:** community / trade association
- **Geography:** Romania, Hungary, Bulgaria, Spain, Portugal
- **Publicly listed?** no member directory located for any of the five
- **Confidence:** Verified (each URL fetched). The conclusion is "not found", not "does not exist".
- **Evidence:**
  - **Romania**: https://fintechromania.ro/ HTTP 200 (104KB), but it is a **news and analysis publication**, not a member association. Title translates as "News and analysis on technology, artificial intelligence". `https://www.fintechromania.ro/membri/` returns HTTP 404 with title "Page Not Found". No Romanian fintech association member directory located.
  - **Hungary**: https://fintechzone.hu/ HTTP 200 (303KB), title "FinTechZone, Elemzés-műhely" ("analysis workshop"). A media and analysis site, not a member body. No Hungarian association directory located.
  - **Bulgaria**: https://www.fintechbulgaria.org/ HTTP 200 (454KB). `/members/` returns HTTP 404. The only membership-related link in the homepage HTML is `/become-a-member/`, i.e. a join page with no roster behind it.
  - **Spain (AEFI)**: both https://asociacionfintech.es/socios/ and `/asociados/` return HTTP 404 ("Página no encontrada"). AEFI is confirmed to exist as an organisation (it appears as a named programme partner on the Mastercard For Fintechs page), but its member-list URL was not found.
  - **Portugal Fintech**: https://portugalfintech.org/ HTTP 200 (756KB). `/members/` returns HTTP 404. No REST API exposed. Portugal Fintech is known to publish an annual report and ecosystem map; neither was located from the homepage before the budget ran out.
- **Why this matters:** Three of the four MVP markets (Poland, Romania, Hungary) yielded **no** usable association member directory, and the fourth (Czechia) yielded 18 companies. The scheme programmes reach none of the four. **The supply-side and trade-body angle does not cover TXN's priority markets.** That is the single most important negative result in this stream and it should be fed back into the source strategy: for Poland, Romania and Hungary, the discovery route has to come from a different stream, most likely national registers, accelerators, or funding data.
- **Last checked:** 2026-08-25

---

## Card bureaux, fulfilment and 3DS vendors

### G+D Netcetera

- **Type:** other (3DS and digital payments vendor)
- **Geography:** Switzerland, DACH, Europe
- **Homepage:** https://www.netcetera.com/
- **List page:** https://www.netcetera.com/company/success-stories.html plus individual reference pages at `/references/<client>.html`
- **Publicly listed?** yes
- **Machine readable?** HTML, one page per reference
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Marginal for greenfield discovery, since 3DS is bought after the card programme exists. Recorded for two reasons. First, **name change confirmed**: the site now titles itself "G+D Netcetera", i.e. Netcetera is now branded under Giesecke+Devrient. Any corpus entry using the standalone name is stale. Second, the reference pages name specific European banks (BLT, SIX, Valiant), which is issuer-side intelligence.
- **Approximate list size:** small. 3 reference pages found in the homepage HTML.
- **Confidence:** Verified
- **Evidence:** Fetched https://www.netcetera.com/ (93KB, HTTP 200), title "G+D Netcetera - Driving progress". Extracted `/company/success-stories.html`, `/references/BLT.html`, `/references/SIX.html`, `/references/valiant.html`. Note `/en/payment` and `/en/solutions/payment.html` both 404: the site structure changed with the rebrand.
- **Last checked:** 2026-08-25

### GPayments

- **Type:** other (3DS ACS and 3DS Server vendor)
- **Geography:** global, with UK presence
- **Homepage:** https://www.gpayments.com/
- **List page:** https://www.gpayments.com/about/clients/
- **Publicly listed?** yes
- **Machine readable?** HTML logo wall (names in image `alt` attributes)
- **Update cadence:** unknown
- **Why it surfaces card candidates:** A 3DS ACS vendor's client list names **card issuers**, because the ACS is the issuer's authentication component. That is a more issuer-proximate list than a 3DS Server vendor's (which names acquirers and gateways). Small, but the mechanism is right: an issuer appearing on an ACS vendor's wall has a live card programme. That makes it a competitor map, not a greenfield source.
- **Approximate list size:** about 6 named clients recoverable from alt text: Fibonatix, Clydeston, DaftCode, Neurocom, Active Access, "ana company". Also carries an "EMVCO Approved" badge.
- **Confidence:** Verified
- **Evidence:** Fetched https://www.gpayments.com/about/clients/ (59KB, HTTP 200), title "Payment Fraud Prevention Tools | GPayments", read the body ("Meet Our Clients. We provide Fraud Prevention services to some of the most cutting-edge bank and payment service providers across the globe") and extracted 41 image alt attributes. Note **Fibonatix appears both here and on the Paynetics client list**, a second confirmed cross-source hit.
- **Last checked:** 2026-08-25

### allpay Limited

- **Type:** other (card bureau, fulfilment and prepaid programme provider)
- **Geography:** United Kingdom
- **Homepage:** https://www.allpay.net/
- **List page:** https://www.allpay.net/success-stories/ and https://www.allpay.net/about/partners/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, server-rendered, one page per story
- **Update cadence:** unknown. No RSS found.
- **Why it surfaces card candidates:** The client base is **UK public sector and social housing**: Edinburgh City Council, North East Lincolnshire Council, NHS Wales prepaid, Great Places Housing Group. These organisations run prepaid disbursement card programmes and are almost entirely invisible to fintech-oriented sources. It is a real greenfield-adjacent segment that no accelerator, VC portfolio or scheme programme would ever surface. UK-only, so opportunistic tier for TXN, but the *category* (municipal and social-housing disbursement programmes) is replicable in CEE and is worth flagging to whoever owns the register strategy.
- **Approximate list size:** about 8 named success stories on the index page
- **Confidence:** Verified
- **Evidence:** Fetched https://www.allpay.net/case-studies/ (169KB, HTTP 200, title "Success Stories | allpay") and read the body and link structure, recovering the named slugs above plus `/about/partners/` and `/news/`.
- **Last checked:** 2026-08-25

### AustriaCard Holdings

- **Type:** other (card manufacturing, personalisation and fulfilment bureau)
- **Geography:** Austria, Greece, Romania, Bulgaria, Poland, Czech Republic and wider CEE
- **Homepage:** https://www.austriacard.com/
- **List page:** https://www.austriacard.com/references/ , but see evidence, it does not contain card clients
- **Publicly listed?** no (for card issuing clients)
- **Machine readable?** no usable list
- **Update cadence:** not applicable
- **Why it surfaces card candidates:** It *should* be one of the best sources in this stream. AustriaCard is a listed CEE card bureau operating in exactly TXN's MVP markets, and a bureau knows about a card programme early because someone has to manufacture the plastic. It does not publish that client list.
- **Approximate list size:** not applicable
- **Confidence:** Verified (that the references page is not what it appears to be)
- **Evidence:** Fetched https://www.austriacard.com/references/ (390KB, HTTP 200, title "References - AUSTRIACARD") and read the body. **The page's testimonials are for "Next Docs", a physical-archiving and document-management subsidiary.** The quoted organisations are Banca Transilvania, Castrol, Mercedes-Benz and ENGIE, praising archive management, not card issuance. There is no card-issuing client list on this page. The site carries `/news/` and `/investor-relations-ac/press-releases-ac/`, and as a listed company its regulatory announcements are the realistic monitoring route for contract wins.
- **Last checked:** 2026-08-25

### Tag Systems and Nitecrest

- **Type:** other (card bureau and fulfilment)
- **Geography:** Andorra, UK, Europe
- **Homepage:** https://www.tagsystems.net/ and https://www.nitecrest.com/
- **List page:** none. `https://www.tagsystems.net/references` returns HTTP 404.
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** not applicable
- **Why it surfaces card candidates:** It does not, directly. Recorded for the **consolidation finding**: `nitecrest.com` returns HTTP 200 with the title "**Tag Systems UK**", i.e. Nitecrest now trades as Tag Systems UK. The two names are one entity. The same combined entity appears as "TAGnitecrest" on IDT Finance's partner wall, which is a third spelling of the same company and a good illustration of why entity resolution matters in this layer.
- **Approximate list size:** not applicable. `tagsystems.net` returns only an 11KB page.
- **Confidence:** Verified
- **Evidence:** Fetched https://www.tagsystems.net/ (10,960 bytes, HTTP 200, title "Tag Systems") and https://www.nitecrest.com/ (136KB, HTTP 200, title "**Tag Systems UK**"). `/references` on tagsystems.net returns HTTP 404 "Page Not Found". Neither site exposes a client list.
- **Last checked:** 2026-08-25

### Modirum

- **Type:** other (3DS vendor)
- **Geography:** Finland, Europe, global
- **Homepage:** https://www.modirum.com/
- **List page:** none. `/customers` returns HTTP 404. News index at https://www.modirum.com/news
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** news page is live. Recent items concern a Finnish public-safety network contract and a Brazilian defence-electronics acquisition.
- **Why it surfaces card candidates:** Minimal. Recorded to close out the 3DS vendor category honestly: of the four 3DS vendors checked (G+D Netcetera, GPayments, Modirum, plus EMVCo's approval register), only GPayments publishes a client list, and it is six logos. **3DS vendor client lists are not a viable discovery channel for greenfield card issuance.** The category can be deprioritised.
- **Approximate list size:** not applicable
- **Confidence:** Verified
- **Evidence:** Fetched https://www.modirum.com/ (85KB, HTTP 200) and extracted news slugs. `/customers` returns HTTP 404 with title "Modirum | Page Not Found (404)". One news item, `maksu-joins-payments-association-eu`, incidentally confirms that a **Payments Association EU** exists as a distinct body from the UK Payments Association. Worth a follow-up that budget did not allow.
- **Last checked:** 2026-08-25

---

## Meta-source

### Fintech Wrap Up: directory of UK and European card issuing and programme management platforms

- **Type:** media
- **Geography:** United Kingdom and Europe
- **Homepage:** https://www.fintechwrapup.com/
- **List page:** https://www.fintechwrapup.com/p/deep-dive-the-directory-of-the-uk
- **Publicly listed?** partial (preview free, full profiles paywalled)
- **Machine readable?** gated. Subscribers get a downloadable Excel file.
- **Update cadence:** one-off deep dive, published **7 June 2026**
- **Why it surfaces card candidates:** Supply-side map, not a lead list, but it is the most complete single artefact found for the European card issuing and programme management layer, it is recent (three months old), and it ships as a spreadsheet. For competitive positioning and for building the referral-partner target list it is worth the subscription cost, which is trivially small relative to the analyst time it replaces. It independently corroborates most of the sponsor entries above.
- **Approximate list size:** 22 companies across five categories: Marqeta, Thredd, Enfuce, Paymentology, Wallester, Solaris, Swan, Railsr, Modulr, Equals Money, Paynetics, Adyen, Stripe, Airwallex, Nium, Pismo, Worldline, Openway, Nexi, Nuvei, SDK Finance, Decta.
- **Confidence:** Verified (page fetched and read. The 22 names and the structure are from the fetched preview, not from the paywalled body.)
- **Evidence:** Fetched the article. Confirmed: 22 companies, five categories, published 7 June 2026, paywalled with a 7-day free trial, subscribers receive "the full structured profile for each of the 22 companies" plus an Excel download. Note it still lists **Railsr and Equals Money as separate entities**, which this stream disproved by fetching both domains. A useful reminder that even a well-maintained three-month-old directory decays fast in this layer.
- **Last checked:** 2026-08-25

---

## Method notes for whoever validates this

Three technical patterns did most of the work and are worth reusing:

1. **When the rendered page is blocked, try the sitemap and the REST API.**
   visainnovationprogram.com serves a 364-byte JavaScript challenge to every
   non-browser client, but its XML sitemaps and its WooCommerce Store API are
   wide open. Same shape at thepaymentsassociation.org (Elementor front end,
   open `wp-json`) and czechfintech.cz. Checking `/wp-json/wp/v2/types` for a
   members-shaped custom post type took seconds and cracked two directories.
2. **Read the page's own JavaScript for its data endpoint.** The Visa Partner
   Directory's data paths were recovered by downloading
   `clientlib-partnerDirectory.min.js` and grepping for quoted paths. That is
   also how the failure was proven rather than assumed: the endpoint exists in
   the code and 302s to a 404 in production.
3. **Byte-identical responses reveal consolidation.** railsr.com and
   equalsmoney.com returning the same 306,350 bytes with the same title is
   conclusive without needing a press release.

Blocked domains, for the record: `mastercard.com` (403 to curl and WebFetch; a
reader proxy works for marketing pages but not the JS-rendered newsroom),
`thredd.com` (Cloudflare interstitial), `partner.visa.com` directory JSON
(302 to 404). `quicko.pl` and `finci.io` did not resolve at all.
