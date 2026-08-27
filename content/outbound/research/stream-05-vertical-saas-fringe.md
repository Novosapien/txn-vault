---
description: "Stream 05 raw research: 30 hiring-signal, vertical SaaS, trademark and regulatory-register sources reaching non-financial companies"
---

> **Section:** [[research]]
> **Validation:** [[validation-05-vertical-saas-fringe]]
> **Status:** raw research output, recorded verbatim. Read the validation report alongside it: several counts in this file were corrected.

# 05: Vertical SaaS and marketplace fringe

**Stream owner:** exploratory / fringe
**Research pass:** 25 August 2026
**Target segment:** non-financial companies that will need a card program and do not
appear in any fintech filter.

---

## 1. Summary

TXN's discovery filters on financial-services sub-sectors. The companies this stream
covers are, by definition, tagged as something else: logistics, healthtech, proptech,
agritech, foodtech, leisure, e-commerce. They become card issuers anyway, because their
business model forces money through them before they ever call themselves a fintech.

The research found three usable classes of source, ranked by how early they fire:

| Class | Lead time before launch | Best sources found |
|---|---|---|
| **Hiring signal** | 6-18 months | ATS board APIs (Greenhouse, Ashby), justjoin.it, StartupJobs.cz, Profession.hu, Profesia.sk |
| **Regulatory / IP footprint** | 1-12 months (unquantified, see §6) | EBA PSD2 register download, KNF MIP register + cashless.pl, EUIPO eSearch class 36 |
| **Population sources** (who exists at all) | n/a, this is the "first hit" job | Market One Capital portfolio, EIT Urban Mobility portfolio, Dealroom taxonomy, Capterra category directories, CLECAT / Ecommerce Europe member lists |
| **Partner announcements** | 0 months (launch day) | Enfuce newsroom, Swan customers, Weavr case studies, Visa Fleet 2.0, Mastercard Product Express |

The single most important finding for the brief: **the strongest pre-announcement signal
is not a news source, it is an HTTP endpoint.** Greenhouse and Ashby expose every
customer's live job board as unauthenticated JSON. Both were called successfully during
this pass. A sweep of those endpoints for `payments`, `embedded finance`, `card`, or
`fintech` in the job title, cross-referenced against a company whose Dealroom sector tag
is *not* financial services, is a repeatable monthly job that costs nothing and fires
long before any press release.

The second most important finding is the inverse: **the sources that name these companies
loudly (BaaS newsrooms, scheme programme lists) all fire on launch day.** Enfuce, Swan,
Weavr and Visa Fleet 2.0 name the vertical platform in the announcement, which is
excellent for building a comparables library and for displacement targeting, but by
Ian's own test it is exactly the moment that is already too late. They are recorded here
as valuable, and explicitly labelled as late.

---

## 2. What I could NOT verify

Read this before trusting anything below.

1. **eJobs.ro** blocks our user agent outright (`400: domain not accessible to our user
   agent`). Romania's largest job board could not be reached at all. BestJobs.eu was used
   as a partial substitute and is a weaker source.
2. **NoFluffJobs** could not be fetched (`Claude Code is unable to fetch from
   nofluffjobs.com`). Everything recorded about it is from search-result snippets, marked
   `Reported`. It is potentially the single best CEE job board for this purpose (five
   markets, mandatory salary disclosure) and someone with browser access should verify it.
3. **PhocusWire** returned HTTP 403. Its travel-payments coverage is real per search
   snippets but the page was not read. Marked `Reported`.
4. **EUIPO eSearch plus**: the FAQ page and the search UI both returned 403 to WebFetch.
   A raw `curl` to `https://euipo.europa.eu/eSearch/` returned HTTP 200 with
   `<title>EUIPO - eSearch</title>`, which proves the tool exists and is publicly
   reachable, but **I did not run a class-36 search and did not confirm the filter
   behaviour, record count, export limit, or API**. The claim that class-36 filings are a
   detectable signal is therefore a PROPOSAL resting on an unverified mechanism.
5. **TMview API**: `POST https://www.tmdn.org/tmview/api/search/results` returned HTTP 000
   (connection failed) with several header/body variants. The TMview front end returns 200.
   No programmatic access confirmed.
6. **Recruitee public offers API**: the documented pattern is
   `https://{tenant}.recruitee.com/api/offers/`. Of 25 tenant names probed, 24 returned
   404 and one (`vinted`) returned HTTP 200 with `offers: []`. The endpoint shape is real;
   **broad availability is not demonstrated**. Do not rely on the tenant-guessing approach.
7. **Teamtailor** requires a per-tenant `X-Api-Key` minted inside each customer's admin,
   so it is not sweepable the way Greenhouse and Ashby are. `Reported`, from search results.
8. **LinkedIn Jobs** was never fetched. It is gated and its terms prohibit scraping.
   Everything about LinkedIn in this document is inference, not evidence.
9. **Dealroom's actual filter URLs** (`app.dealroom.co/...`) are behind login. Only the
   public taxonomy documentation was read. Whether a paid seat can export "non-financial
   + marketplace + Series A+ + CEE" as a list was not tested.
10. **KNF's own MIP register page** was not fetched. Only a cashless.pl article reporting
    on it was read. The register URL was not confirmed.
11. **HOTREC and FIEC member lists** were not fetched, only described in search snippets.
12. **Update cadence** is unverified for almost every source here. Where a cadence is
    stated below it is either printed on the page or clearly marked as an estimate.
13. **No claim in §6 (puzzle-piece patterns) about lead time has been measured.** Those
    numbers are reasoned estimates and are labelled as such. Nobody backtested them.

---

## 3. Sources: hiring signal

This is the section the brief asked for most directly. Findings first, then the
technique in §3.9.

### Greenhouse Job Board API

- **Type:** other (unauthenticated data endpoint)
- **Geography:** global, heavily used by European scale-ups
- **Homepage:** https://developers.greenhouse.io/job-board.html
- **List page:** `https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs`
- **Publicly listed?** yes
- **Machine readable?** JSON, no authentication
- **Update cadence:** live, reflects the company's published board in real time
- **Why it surfaces card candidates:** a non-financial company's first payments hire
  appears here months before anything is announced. The job description usually states
  the intent explicitly ("launch our embedded payments offering", "own the card product").
  This is the earliest credible signal identified in this pass.
- **Approximate list size:** one board per customer; thousands of European customers
- **Confidence:** Verified
- **Evidence:** `curl https://boards-api.greenhouse.io/v1/boards/gocardless/jobs` returned
  HTTP 200 and a JSON body beginning
  `{"jobs":[{"absolute_url":"https://job-boards.greenhouse.io/gocardless/jobs/8141651", ...
  "location":{"name":"Leeds, UK"} ... "updated_at":"2026-08-20T06:33:26 ...`
  No API key, no signup. Board token is discoverable from any company's careers page URL.
- **Last checked:** 2026-08-25

### Ashby Job Board Posting API

- **Type:** other (unauthenticated data endpoint)
- **Geography:** global
- **Homepage:** https://developers.ashbyhq.com/
- **List page:** `https://api.ashbyhq.com/posting-api/job-board/{board_name}`
- **Publicly listed?** yes
- **Machine readable?** JSON, no authentication
- **Update cadence:** live
- **Why it surfaces card candidates:** same mechanism as Greenhouse. Ashby skews younger
  and more startup-heavy, which matches the greenfield segment better than Greenhouse does.
- **Approximate list size:** one board per customer
- **Confidence:** Verified
- **Evidence:** `curl https://api.ashbyhq.com/posting-api/job-board/ramp` returned HTTP 200
  and JSON containing `{"jobs":[{"id":"34413f8d-...","title":" Security Engineer, Cloud",
  "department":"Engineering","team":"Backend","employmentType":"FullTime","location":"New
  York, NY (HQ)" ...`. Fields include `department` and `team`, which lets you detect
  whether a *payments team* is being created rather than a single role being backfilled.
- **Last checked:** 2026-08-25

### justjoin.it

- **Type:** other (job board)
- **Geography:** Poland primarily, plus other European cities (Copenhagen listings observed)
- **Homepage:** https://justjoin.it
- **List page:** https://justjoin.it/all-locations/pm
- **Publicly listed?** yes
- **Machine readable?** HTML cards, JS-assisted but server-rendered enough to fetch
- **Update cadence:** continuous; the board offers publication-date filters of yesterday,
  last week, last 2 weeks, last month, which is exactly the cadence control needed for a
  monthly sweep
- **Why it surfaces card candidates:** Poland is the MVP market and justjoin.it is the
  default IT board there. Its search box is explicitly "Job title, company, keyword", so a
  keyword sweep for `payments` returns roles across all employer types, not just fintechs.
- **Approximate list size:** 1,435 offers in the PM category alone at time of check
- **Confidence:** Verified
- **Evidence:** Fetched https://justjoin.it/all-locations/pm. Confirmed filter set
  (location, category, seniority incl. C-level, salary, publication date, working mode,
  contract type) and confirmed the search box label "Search: Job title, company, keyword".
  Separately ran a domain-restricted search against justjoin.it for `"payments" product
  manager OR "head of payments"`, which returned a live
  **Payments Operation Manager** posting at **Code and Pepper** (a software house, not a
  licensed financial institution) at
  https://justjoin.it/job-offer/code-and-pepper-payments-operation-manager-krakow-analytics
  and a Head of Product, Central Europe posting at eService. The technique demonstrably
  returns non-fintech employers.
- **Last checked:** 2026-08-25

### StartupJobs.cz

- **Type:** other (job board)
- **Geography:** Czech Republic
- **Homepage:** https://www.startupjobs.com
- **List page:** https://www.startupjobs.com/jobs
- **Publicly listed?** yes
- **Machine readable?** HTML cards
- **Update cadence:** continuous (not stated on page; estimate)
- **Why it surfaces card candidates:** the only Czech board found with an explicit
  **Companies** filter alongside a "Search by industry, job title, or keyword" field. That
  combination is what lets you separate "fintech hiring a payments PM" from "logistics
  platform hiring a payments PM", which is the entire distinction this stream cares about.
- **Approximate list size:** not disclosed on the page
- **Confidence:** Verified
- **Evidence:** Fetched https://www.startupjobs.com/jobs. Filter list read directly from
  the page: Location, Work Mode, Seniority, Salary, Employment Type, Type of Contract,
  Technology, **Companies**, Benefits, Languages, plus "Search by industry, job title, or
  keyword".
- **Last checked:** 2026-08-25

### Profession.hu

- **Type:** other (job board)
- **Geography:** Hungary
- **Homepage:** https://www.profession.hu
- **List page:** https://www.profession.hu (category listings linked from home)
- **Publicly listed?** yes
- **Machine readable?** HTML
- **Update cadence:** continuous
- **Why it surfaces card candidates:** Hungary is an MVP market with thin English-language
  startup coverage. Profession.hu is the mainstream national board, which matters here
  because a *non-tech* company hiring its first payments person will post to the
  mainstream board, not to a startup board.
- **Approximate list size:** 17,656 ads from 4,395 employers at time of check; 24 job
  categories from Adminisztráció to Vendéglátás
- **Confidence:** Verified
- **Evidence:** Fetched https://www.profession.hu. Read the counter "4395 hirdető, 17656
  hirdetés" and the category list with per-category counts (54 to 3,909). English version
  available via language selector.
- **Last checked:** 2026-08-25

### Profesia.sk

- **Type:** other (job board)
- **Geography:** Slovakia
- **Homepage:** https://www.profesia.sk/en/
- **List page:** https://www.profesia.sk/en/ (regional and company listings linked)
- **Publicly listed?** yes
- **Machine readable?** HTML
- **Update cadence:** continuous
- **Why it surfaces card candidates:** carries a browsable **list of 5,050 employers**
  advertising jobs. That employer list is itself a company population source for Slovakia,
  independent of the job content.
- **Approximate list size:** ~16,000 active positions; 5,050 employers
- **Confidence:** Verified
- **Evidence:** Fetched https://www.profesia.sk/en/. Counts read from page (Bratislava
  region alone 4,860). **Negative finding worth recording: there is no employer-industry
  filter.** You can browse companies but not slice them by sector, so the non-financial
  cross-reference has to be done externally.
- **Last checked:** 2026-08-25

### NoFluffJobs

- **Type:** other (job board)
- **Geography:** Poland, Hungary, Czech Republic, Slovakia, Ukraine
- **Homepage:** https://nofluffjobs.com
- **List page:** https://nofluffjobs.com/jobs (not reached)
- **Publicly listed?** yes
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** the only board found covering four of the four MVP
  and near-MVP CEE markets under one search. Mandatory salary disclosure since 2014 adds a
  usable secondary signal: an unusually high band for a first payments hire indicates a
  senior, mandate-carrying role rather than an operations backfill.
- **Approximate list size:** unknown
- **Confidence:** Reported
- **Evidence:** WebFetch to nofluffjobs.com was blocked at the tool level. Search-result
  snippets confirm the five-market footprint, keyword search, and filters for category,
  seniority, region, city, remote. **Not read directly. Needs browser verification.**
- **Last checked:** 2026-08-25

### BestJobs.eu

- **Type:** other (job board)
- **Geography:** Romania (plus remote)
- **Homepage:** https://www.bestjobs.eu/en/jobs
- **List page:** https://www.bestjobs.eu/en/jobs
- **Publicly listed?** yes
- **Machine readable?** HTML cards
- **Update cadence:** continuous
- **Why it surfaces card candidates:** stand-in for eJobs.ro, which is unreachable.
  Romania is an MVP market and currently the weakest-covered one in this stream.
- **Approximate list size:** ~25 per page, total not disclosed
- **Confidence:** Verified (weakly)
- **Evidence:** Fetched https://www.bestjobs.eu/en/jobs. Listings are predominantly in
  Romanian ("Inginer CFDP", "Consultant Asigurari, Credite & Turism"). Employer names and
  salaries displayed. Filter set is thin compared with the Polish and Czech boards.
- **Last checked:** 2026-08-25

### Arbeitnow Job Board API

- **Type:** other (job board with free API)
- **Geography:** Germany
- **Homepage:** https://www.arbeitnow.com/api/job-board-api
- **List page:** https://www.arbeitnow.com/api/job-board-api
- **Publicly listed?** yes
- **Machine readable?** JSON, no authentication
- **Update cadence:** live
- **Why it surfaces card candidates:** Germany is not an MVP market, but this is the only
  *aggregated* free job API found in Europe (as opposed to per-company ATS endpoints). It
  is the right place to prototype and tune the keyword classifier before pointing it at
  the CEE boards, which have no API and will need scraping.
- **Approximate list size:** unknown, paginated
- **Confidence:** Verified
- **Evidence:** Fetched the API page. Response shape `{"data":[{...}]}` with fields
  `slug, company_name, title, description, remote, url, tags, job_types, location,
  created_at`. No auth observed. `tags` includes categories such as Finance, which gives a
  crude sector cross-reference inside the same payload.
- **Last checked:** 2026-08-25

### 3.9 The technique, stated concretely

This is a PROPOSAL for how to operate the sources above. The sources are verified; the
operating procedure is not, because nobody has run it yet.

**Step 1, build the board-token list.** For every company already in the corpus and every
company harvested from the population sources in §4, resolve its careers page and extract
the ATS token. Greenhouse tokens appear as `boards.greenhouse.io/{token}` or
`job-boards.greenhouse.io/{token}`; Ashby as `jobs.ashbyhq.com/{name}`. This is a one-off
enrichment that then runs forever.

**Step 2, sweep monthly.** Hit each token's JSON endpoint. Match job titles against:

```
payments | payment | embedded finance | embedded payments | fintech |
card | issuing | banking | treasury | money movement | payouts | wallet |
"platform finance" | "financial products"
```

plus the local-language equivalents for the CEE boards, which are the part that will
actually take work: `płatności` (PL), `platby` (CZ/SK), `fizetés` / `fizetési` (HU),
`plăți` (RO).

**Step 3, apply the negative filter.** This is the step that makes it this stream's
technique rather than a generic fintech sweep. **Discard the hit if the company's own
sector classification is financial services.** Use the Dealroom taxonomy (§4) or the
company's own about page. What remains is a non-financial company hiring for payments,
which is the target.

**Step 4, score for firstness.** A single payments role in a company with no other
payments staff is a launch signal. A payments role in a company that already has a
payments team is a backfill. Ashby's payload exposes `department` and `team` directly,
so a *new* department name appearing is a strong version of this. Greenhouse exposes
department via the `content=true` variant of the endpoint.

**Step 5, for boards with no API**, run domain-restricted search instead. This was tested
and works: a search scoped to `justjoin.it` for `"payments" product manager OR "head of
payments"` returned live non-fintech postings. It is lower fidelity than the API sweep and
depends on the search index being fresh, so treat it as a supplement.

**Known weakness, stated plainly.** Companies that recruit via LinkedIn only, via
Personio/SmartRecruiters/Workday, or through headhunters are invisible to this method.
Workday boards are enumerable but per-tenant and messy; SmartRecruiters and Personio were
not tested in this pass. The method has a real and unmeasured coverage hole.

---

## 4. Sources: where non-financial vertical companies are catalogued

### Dealroom tech sector taxonomy

- **Type:** register (private-market database)
- **Geography:** global, strong European coverage
- **Homepage:** https://dealroom.co
- **List page:** https://dealroom.co/guides/taxonomy (taxonomy documentation; the queryable
  lists are behind login at app.dealroom.co)
- **Publicly listed?** partial (taxonomy public, data gated)
- **Machine readable?** gated
- **Update cadence:** continuous
- **Why it surfaces card candidates:** this is the **negative filter** that makes the whole
  stream work. Dealroom carries business model as a first-class dimension ("Marketplace &
  eCommerce", "SaaS") *separately* from industry, and separately again from income stream
  (Advertising / Commission / Selling own inventory / Subscription). That means you can
  express the actual target query: business model = marketplace, income stream = commission,
  industry ≠ fintech, geography = CEE. No other source found expresses that shape.
- **Approximate list size:** 31 industries with nested sub-industries, 18 derived sectors,
  2,783 free-form tags including "Vertical SaaS" and "Logistics"
- **Confidence:** Verified (taxonomy only)
- **Evidence:** Fetched https://dealroom.co/guides/taxonomy. Confirmed the 31-industry
  structure, multi-industry membership, the separate business-model and income-stream
  dimensions, the 18 algorithmically derived sectors, and the 2,783-tag free-form layer.
  **Did not verify** that a seat can export the resulting list, or at what cost.
- **Last checked:** 2026-08-25

### Market One Capital, portfolio

- **Type:** VC portfolio
- **Geography:** Europe, headquartered Warsaw with offices in Spain and Luxembourg
- **Homepage:** https://www.moc.vc/
- **List page:** https://www.moc.vc/portfolio
- **Publicly listed?** yes
- **Machine readable?** HTML table with inline sector tags, not JS-rendered
- **Update cadence:** on new investment; the fund is actively deploying from a €80m Fund II
- **Why it surfaces card candidates:** this is the best single find in the stream. It is a
  **CEE-headquartered fund whose entire thesis is marketplaces and network-effect
  platforms**, which is precisely the business model that ends up needing to move money to
  third parties. Every company is pre-tagged with its vertical, and the verticals are the
  ones that issue cards: Logistics (Stetig, Magaloop, Linker Cloud), Travel (Arise,
  Welcome Pickups, Nautal), HealthTech (Jutro Medical, Petsapp, Mindgram), FoodTech (Kitch,
  Lunching), AgriTech (Vosbor), PropTech (SonarHome), Automotive (Dobry Mechanik), Leisure
  (Eversports, Convious), Micromobility (TIER). Only five of 46 are tagged FinTech, meaning
  **41 of 46 companies would be invisible to a fintech filter**.
- **Approximate list size:** 46 companies with sector tags (fund reports 60+ total
  investments; the public page shows 46)
- **Confidence:** Verified
- **Evidence:** Fetched https://www.moc.vc/portfolio and read the full list with sector
  labels. Plain HTML table markup with company logos, descriptions and metadata in the DOM,
  so it is directly scrapeable. Note: my first guess at the domain (`mocap.vc`) did not
  resolve; the correct domain is `moc.vc`, found via search.
- **Last checked:** 2026-08-25

### EIT Urban Mobility, startup portfolio

- **Type:** accelerator / public investor portfolio
- **Geography:** EU and associated countries, explicit CEE representation
- **Homepage:** https://www.eiturbanmobility.eu
- **List page:** https://www.eiturbanmobility.eu/our-impact/startup-portfolio/
- **Publicly listed?** yes
- **Machine readable?** HTML cards with a "load more" control
- **Update cadence:** per investment round and per cohort; the fund runs an annual
  Startup Investments Open Call
- **Why it surfaces card candidates:** mobility is a card-native vertical (fuel, charging,
  tolls, parking, driver expenses) and this is an EU-funded body that publishes its whole
  portfolio for free with country labels. It sits entirely outside the fintech press. Also
  worth noting: EIT Health, EIT Food and the wider EIT community publish comparable
  portfolios, and the EIT community's aggregate portfolio is published on Dealroom.
- **Approximate list size:** 140+ in the investment portfolio; 350+ supported since 2020;
  127 companies from 29+ countries per the fund's own framing
- **Confidence:** Verified
- **Evidence:** Fetched https://www.eiturbanmobility.eu/our-impact/startup-portfolio/.
  Company names, logos, countries and mobility topics displayed. CEE presence confirmed by
  name: AgeVolt (Slovakia), Delivery Couple (Poland), Bruntor and DIGAS (Latvia), .lumen
  (Romania), plus Czech and Estonian entries. Other names read: A.D. Knight, Arxax, Beev,
  Blike, Blowind.
- **Last checked:** 2026-08-25

### Capterra category directories (country editions)

- **Type:** media / directory
- **Geography:** country editions including UK, and other European locales
- **Homepage:** https://www.capterra.co.uk
- **List page:** https://www.capterra.co.uk/directory/10009/field-service-management/software
  (example category)
- **Publicly listed?** yes
- **Machine readable?** HTML cards, paginated
- **Update cadence:** continuous
- **Why it surfaces card candidates:** Capterra catalogues software **by the industry it
  serves**, which is the exact axis a fintech filter lacks. Categories such as Field Service
  Management, Dental, Construction Management and Medical Practice Management are lists of
  vertical SaaS companies, most of which will never be in a startup database because many
  are bootstrapped, old, and profitable. Capterra states it lists all vendors, not only
  paying ones. Field Service Management in particular is the classic card-program vertical:
  mobile workers buying parts and fuel on the company's account.
- **Approximate list size:** 900+ categories; the field service category alone runs 44 pages
  at 25 products per page (~1,100 products)
- **Confidence:** Verified
- **Evidence:** Fetched
  https://www.capterra.co.uk/directory/10009/field-service-management/software. Confirmed
  25 products on page 1 of 44, vendor names and review counts displayed (Connecteam,
  Housecall Pro, Jobber, Infraspeak, Odoo), filters advertised on-page. **Not verified:**
  whether vendor country of origin is exposed as a filter, which matters a lot for a CEE
  focus. G2 was not tested at all this pass.
- **Last checked:** 2026-08-25

### Vestbee, CEE startup and VC database

- **Type:** media / register
- **Geography:** Central and Eastern Europe
- **Homepage:** https://www.vestbee.com
- **List page:** not confirmed
- **Publicly listed?** partial
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** the main CEE-native ecosystem publisher, with
  country-level scaleup counts (Poland 60, Estonia 54, Czechia 38, Romania 21) and
  industry breakdowns that include transportation, energy and enterprise software as
  separate lines from fintech.
- **Approximate list size:** unknown
- **Confidence:** Reported
- **Evidence:** Search-result snippets only, including a Dealroom-sourced CEE report.
  **The database itself was not fetched and its filter capability is unverified.**
- **Last checked:** 2026-08-25

### EU-Startups directory

- **Type:** media / register
- **Geography:** Europe
- **Homepage:** https://www.eu-startups.com/directory/
- **List page:** https://www.eu-startups.com/directory/
- **Publicly listed?** yes (per snippets)
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** industry-and-country filterable, free, and covers
  smaller companies that Dealroom under-indexes.
- **Approximate list size:** unknown
- **Confidence:** Reported
- **Evidence:** Search snippets only; the directory page was not fetched. Also surfaced:
  startupeurope.net, europe-startup-guide.com/directory and startupmap.one, none of which
  were verified. Recording them as leads, not as sources.
- **Last checked:** 2026-08-25

---

## 5. Sources: regulatory and IP footprint

These are the fringe of the fringe. They do not describe companies, they describe
*paperwork companies file before they launch*. The mechanism is verified for the EBA
register; the lead-time claim is not verified for any of them.

### EBA central register of payment and e-money institutions (PSD2)

- **Type:** register
- **Geography:** EU / EEA
- **Homepage:** https://www.eba.europa.eu/risk-and-data-analysis/data/registers/payment-institutions-register
- **List page:** search https://euclid.eba.europa.eu/register/pir/disclaimer ,
  bulk download https://euclid.eba.europa.eu/register/pir/registerDownload
- **Publicly listed?** yes
- **Machine readable?** yes, full-register download with a published JSON file specification
- **Update cadence:** national competent authorities update at least once per day
- **Why it surfaces card candidates:** the register contains nine entity categories, and
  the one that matters here is **agents** as defined in PSD2 Article 4(38). When a vertical
  SaaS platform embeds a card product, it very often appears first as an agent or
  distributor of a licensed EMI, before it has a product page, a press release, or a
  fintech tag. Diffing the download month over month and filtering new agent entries for
  companies whose name and website are non-financial is a fully automatable greenfield
  detector across the entire EEA in one file.
- **Approximate list size:** several thousand institutions and ~150,000 agents
- **Confidence:** Verified
- **Evidence:** Fetched the EBA register page and confirmed the nine categories (payment
  institutions, exempted PIs, AISPs, EMIs, exempted EMIs, **agents**, EEA branches,
  nationally entitled providers, excluded providers), the daily update commitment, the
  availability of a full machine-readable download, and the JSON specification document.
  `curl` to https://euclid.eba.europa.eu/register/pir/disclaimer returned HTTP 200.
  **Not verified:** the actual file format and field set of the download, and whether agent
  records carry enough identifying data (company number, website) to classify sector
  automatically. That needs testing before anyone builds on it.
- **Last checked:** 2026-08-25

### KNF register of small payment institutions (MIP), Poland, plus cashless.pl as a feed

- **Type:** register (plus media wrapper)
- **Geography:** Poland
- **Homepage:** https://www.knf.gov.pl (register URL not confirmed)
- **List page:** https://www.cashless.pl (cashless.pl publishes each batch of new entries
  by name; example read: https://www.cashless.pl/8684-6-nowych-mip)
- **Publicly listed?** yes
- **Machine readable?** unknown for the register; HTML articles for cashless.pl
- **Update cadence:** irregular but frequent; entries are added and removed in small
  batches and cashless.pl reports each batch
- **Why it surfaces card candidates:** the MIP route is the cheap Polish on-ramp. No
  licence application, just a filing, capped at €1.5m monthly turnover, Poland-only. It is
  therefore what a **non-financial Polish company experiments with first**. Watching the
  MIP register in the MVP market is a low-cost, high-specificity greenfield signal, and
  cashless.pl does the monitoring work for free.
- **Approximate list size:** 75+ entities as of the article read; the register is actively
  pruned (seven delistings reported in one October period)
- **Confidence:** Reported (media) / Unverified (register itself)
- **Evidence:** Fetched https://www.cashless.pl/8684-6-nowych-mip. The article names six
  newly registered MIPs (Benefitia, Gerlipay, IXPLAT, Inkaso Finanse, Titan PL, MV Brands
  Kacperczyk) and confirms the outlet reports these routinely. **Honest caveat: on this
  sample, all six read as payments-native names, so I have no evidence yet that
  non-financial companies show up in the MIP register.** That is the assumption the source
  rests on and it is currently untested. The KNF register page itself was not fetched and
  its URL is not confirmed. **Defunct check not performed.**
- **Last checked:** 2026-08-25

### EUIPO eSearch plus, Nice class 36 filings

- **Type:** register
- **Geography:** EU (EUTM), with TMview extending to national offices
- **Homepage:** https://euipo.europa.eu/eSearch/
- **List page:** https://euipo.europa.eu/eSearch/ (search UI; not exercised, see caveat)
- **Publicly listed?** yes
- **Machine readable?** partial (Excel export reported at up to 1,000 results; API reported
  but not confirmed)
- **Update cadence:** reported as daily
- **Why it surfaces card candidates:** Nice class 36 covers "financial transaction and
  payment services ... electronic funds transfer, processing of credit card and debit card
  payments". A company files a trademark **before** it launches the product the trademark
  protects. A vertical SaaS company whose existing marks are all class 9 and class 42
  suddenly filing a class 36 mark is declaring an intention in a public register, months
  ahead, for €850. I have not found this technique described anywhere in a sales-prospecting
  context, which is why it is in this stream.
- **Approximate list size:** 2.5m+ EUTM records since 1996 (reported)
- **Confidence:** Unverified as a working search; the tool's existence is Verified
- **Evidence:** WebFetch to both the eSearch UI and the EUIPO eSearch FAQ returned HTTP 403.
  A raw curl with a browser user agent to https://euipo.europa.eu/eSearch/ returned
  **HTTP 200 with `<title>EUIPO - eSearch</title>`**, confirming the tool is live and
  publicly reachable. Search snippets report free access, daily updates, 2.5m+ records,
  advanced search combining owner + Nice class + filing number + legal status, and Excel
  export capped at 1,000 results. **None of that was confirmed on-page. No class-36 search
  was run. The whole signal is a PROPOSAL until someone executes a real query.**
  TMview (the multi-office front end, tmdn.org/tmview) returned HTTP 200 at the root but
  its search API returned HTTP 000 on every POST variant tried.
- **Last checked:** 2026-08-25

---

## 6. Sources: partner and scheme announcements (late signal, still valuable)

Everything in this section fires **at or after launch**. It is recorded because it names
the vertical platform explicitly and is therefore the best available training set for the
patterns in §7, and the right list for displacement targeting. It is not an early warning.

### Enfuce newsroom

- **Type:** other (BaaS / issuer-processor newsroom)
- **Geography:** Nordics, UK, Ireland, Belgium, Luxembourg, expanding
- **Homepage:** https://enfuce.com
- **List page:** https://enfuce.com/newsroom/
- **Publicly listed?** yes
- **Machine readable?** HTML cards, paginated (5 pages)
- **Update cadence:** frequent; 54 posts in the archive
- **Why it surfaces card candidates:** Enfuce announcements consistently name a
  **non-financial** partner and describe the card program. Read directly from the newsroom:
  **Circle K** (fuel retail, 400,000+ consumer cards migrated across Sweden, Norway,
  Denmark), **Monizze** (employee benefits, Belgium and Luxembourg), **Swile** (employee
  benefits, Latin America entry), plus **Octopus Energy Electroverse** (EV fleet payments
  card, UK) and **FLEET220** (Italian fleet services, open-loop mobility card on Visa Fleet
  2.0) from adjacent search results. This is the shape of company this stream targets, and
  Enfuce is naming them one at a time for free.
- **Approximate list size:** 54 news posts
- **Confidence:** Verified
- **Evidence:** Fetched https://enfuce.com/newsroom/ and read 12 items on page 1 with the
  counter "All news posts (54)" and pagination 1-5. Note: https://enfuce.com/press-releases/
  returns HTTP 404 as an index; individual press releases live under that path but the
  browsable index is /newsroom/. Dates were not shown on the listing page. No RSS link
  found in the fetched content.
- **Last checked:** 2026-08-25

### Swan, customers page

- **Type:** other (BaaS customer directory)
- **Geography:** France, Germany, Netherlands, Spain, Italy
- **Homepage:** https://www.swan.io
- **List page:** https://www.swan.io/customers
- **Publicly listed?** yes
- **Machine readable?** HTML cards with a working industry filter
- **Update cadence:** on new case study (estimate)
- **Why it surfaces card candidates:** the page has an **industry filter** built in, with
  values Accounting & Bookkeeping, Treasury & Cash Flow, PropTech, HR Tech, Travel, Health
  & Insurance, and a product filter that includes **Expense Cards**. Filtering that page by
  product = Expense Cards gives you a ready-made list of vertical software companies that
  have already shipped a card, sorted by vertical. That is the best available reference set
  for pattern-building.
- **Approximate list size:** 13 published customer stories (Pennylane, MyUnisoft, Sibill,
  fulll.io, Betterfly, Accountable, Axonaut, Libeo, Lucca, Indy, Expensya, Syndic Yourself,
  Agicap)
- **Confidence:** Verified
- **Evidence:** Fetched https://www.swan.io/customers. Read all 13 names, their industry
  labels, and both filter dimensions (industry and product type).
- **Last checked:** 2026-08-25

### Weavr, embedded finance case studies

- **Type:** other (embedded finance provider case studies)
- **Geography:** UK and Europe
- **Homepage:** https://www.weavr.io
- **List page:** https://www.weavr.io/embedded-finance-case-studies/
- **Publicly listed?** yes
- **Machine readable?** HTML, static, no filter
- **Update cadence:** infrequent (5 studies published; estimate)
- **Why it surfaces card candidates:** Weavr's whole positioning is B2B SaaS rather than
  fintech, and it partnered with Visa to target ERP, HR management and B2B commerce
  platforms specifically. Its use-case taxonomy (expense management, employee benefits,
  payroll, B2B payments, AP/AR, credit disbursement, salary advance, claims payments) is a
  useful list of the *jobs* that trigger a card program, independent of vertical.
- **Approximate list size:** 5 case studies (Ben, Club Employés, Peanuds, Finway, NUMARQE)
- **Confidence:** Verified
- **Evidence:** Fetched https://www.weavr.io/embedded-finance-case-studies/ and read all
  five with their verticals. Note https://www.weavr.io/customers returns HTTP 404; the
  case-studies path is the correct one.
- **Last checked:** 2026-08-25

### Visa Fleet 2.0 and Mastercard Product Express partner announcements

- **Type:** scheme programme
- **Geography:** Europe
- **Homepage:** Visa Fleet & Mobility Partner Programme / Mastercard Europe newsroom
  https://www.mastercard.com/news/europe/en/newsroom/press-releases/
- **List page:** no single consolidated partner list found
- **Publicly listed?** partial
- **Machine readable?** no list
- **Update cadence:** per announcement
- **Why it surfaces card candidates:** these programmes exist specifically to onboard
  **non-financial** vertical platforms into card issuance, and each announcement names one.
  Examples surfaced this pass: **ryd** (Munich mobility app, launched ryd fleet with
  Mastercard as a payment operating system for European fleet operators), **Corpay**
  (Visa Fleet 2.0 rollout across its 800,000-customer network), **FLEET220** (Italy, ODOS
  open-loop mobility card), **Cubic³ + CarPay-Diem** (FleetWallet³, 12 European countries,
  5,300+ fuel retailers), **ReceiptHero** (Visa Ready for Fleet). Visa reportedly launched
  Fleet 2.0 with 15 partners; the full list was not found.
- **Approximate list size:** unknown; 15 initial Visa Fleet 2.0 partners reported
- **Confidence:** Reported
- **Evidence:** All from search-result snippets across Mastercard newsroom, PYMNTS,
  Finextra, The Paypers, ffnews and carpay-diem.com. **No partner-list page was fetched
  and no consolidated directory was found to exist.** If one exists it is a strong source;
  I could not confirm it does.
- **Last checked:** 2026-08-25

### Mangopay, marketplace client base

- **Type:** other (marketplace PSP)
- **Geography:** Europe, 22 countries
- **Homepage:** https://mangopay.com
- **List page:** https://blog.mangopay.com/category/clients (not fetched)
- **Publicly listed?** partial
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** Mangopay is marketplace-only and reports 2,500+
  European platform customers. Its named clients (Vinted, Wallapop, Malt, ManoMano,
  Chrono24, Leboncoin, Rakuten France, Carrefour) are the population that graduates into
  issuing. **The commercial insight is that Mangopay solves the collect-and-split problem
  but is not primarily a card issuer**, so its customer base is a pool of platforms that
  have already proven they move third-party money and have not yet solved the outbound
  card side. That is the greenfield definition.
- **Approximate list size:** 2,500+ customers claimed; only a handful named publicly
- **Confidence:** Reported
- **Evidence:** Search snippets only. **The clients page was not fetched and no public
  full customer list was found.** The 2,500 figure is the company's own claim, unverified.
- **Last checked:** 2026-08-25

### Verestro

- **Type:** other (CEE BaaS / issuing platform)
- **Geography:** Poland-headquartered, active across CEE, Balkans, Middle East, US, SE Asia
- **Homepage:** https://www.verestro.com
- **List page:** none found
- **Publicly listed?** no
- **Machine readable?** no list
- **Update cadence:** n/a
- **Why it surfaces card candidates:** relevant as **competitive intelligence in the MVP
  market rather than as a source of names**. Verestro is Mastercard-backed, Polish, and
  explicitly bundles issuing for "non-bank entities", serving e-commerce platforms and
  insurers alongside banks. Any CEE vertical platform that has already gone to Verestro is
  no longer greenfield. Named partners found: Austriacard, Fidor Bank, MBK (Hungary), OTP
  Banka (Serbia), Komercijalna Banka (Macedonia), all financial institutions.
- **Approximate list size:** unknown
- **Confidence:** Reported
- **Evidence:** Search snippets only. **No customer or partner list page was located.**
- **Last checked:** 2026-08-25

---

## 7. Sources: vertical trade media and associations

### trans.info

- **Type:** media
- **Geography:** Europe with strong CEE focus; editions in English, Polish, Hungarian,
  Romanian, Lithuanian, Ukrainian, Spanish, German, French, Italian, Russian
- **Homepage:** https://trans.info/en
- **List page:** n/a (news feed)
- **Publicly listed?** yes
- **Machine readable?** HTML articles; RSS not confirmed
- **Update cadence:** daily
- **Why it surfaces card candidates:** road transport and logistics is the highest-density
  card vertical (fuel, tolls, driver expenses, ferry, parking) and CEE is where European
  haulage actually operates from. trans.info reports company technology launches for that
  sector in the local languages of three of the four MVP markets. A logistics platform's
  card launch would be covered here before it reached any fintech outlet, and a company's
  *funding or expansion* story here is an earlier signal still.
- **Approximate list size:** n/a
- **Confidence:** Verified
- **Evidence:** Fetched https://trans.info/en. Confirmed the 10+ language editions, the
  topic coverage (road transport, logistics infrastructure, shipping, EV/autonomous,
  regulation, company developments and M&A), and CEE-specific coverage of Polish hauliers,
  Czech operations, Romanian logistics and Hungarian market developments. **RSS not
  confirmed on the fetched page.**
- **Last checked:** 2026-08-25

### Hospitality Net

- **Type:** media
- **Geography:** global with European editorial base
- **Homepage:** https://www.hospitalitynet.org/
- **List page:** Supplier News section (URL not captured separately)
- **Publicly listed?** yes
- **Machine readable?** HTML; **RSS confirmed present in footer**
- **Update cadence:** daily
- **Why it surfaces card candidates:** hospitality tech vendors (PMS, booking, F&B) push
  press releases here that never reach the fintech press. Running since 1994, it has a
  dedicated Technology section and an explicit Supplier News channel that accepts vendor
  announcements. A PMS vendor adding payouts or cards to its stack announces it here first.
- **Approximate list size:** n/a
- **Confidence:** Verified
- **Evidence:** Fetched https://www.hospitalitynet.org/. Confirmed the Supplier News
  section, the Technology section, the press-release acceptance model, and an RSS option in
  the footer. **No dedicated payments subsection exists**, so a keyword monitor on the RSS
  feed is the practical approach rather than a section subscription.
- **Last checked:** 2026-08-25

### PhocusWire

- **Type:** media
- **Geography:** global travel technology
- **Homepage:** https://www.phocuswire.com/
- **List page:** payments topic pages exist (e.g.
  https://www.phocuswire.com/travel-agencies-embrace-virtual-future-b2b-payments)
- **Publicly listed?** yes
- **Machine readable?** unknown
- **Update cadence:** daily
- **Why it surfaces card candidates:** travel is a virtual-card-native vertical. OTAs issue
  virtual cards to settle with hotels and airlines, reportedly ~40% of OTA-to-hotel payments
  by end-2022, and PhocusWire covers this as a standing beat. An OTA or travel management
  company moving from a third-party virtual card supplier to its own program is a
  displacement opportunity that appears here first.
- **Approximate list size:** n/a
- **Confidence:** Reported
- **Evidence:** **HTTP 403 on fetch.** Article titles and payments-beat coverage confirmed
  only from search results. Not read.
- **Last checked:** 2026-08-25

### Ecommerce Europe, national association members

- **Type:** community / trade association
- **Geography:** EU, EFTA and candidate countries
- **Homepage:** https://ecommerce-europe.eu/
- **List page:** https://ecommerce-europe.eu/members-of-ecommerce-europe/national-ecommerce-associations/
- **Publicly listed?** yes
- **Machine readable?** HTML list with association names and websites
- **Update cadence:** on membership change; slow (estimate)
- **Why it surfaces card candidates:** this is a **directory of directories**. Each national
  association below has its own member list of merchants and marketplaces in that country,
  which is a company population no startup database contains. Ecommerce Europe reports
  representing 150,000+ companies through them.
- **Approximate list size:** 22 national associations
- **Confidence:** Verified
- **Evidence:** Fetched the page and read all 22 with countries and websites. MVP and
  Phase 1a coverage confirmed: **Poland (eIZBA, eizba.pl), Czech Republic (APEK, apek.cz),
  Romania (ARMO, armo.org.ro), Greece (GRECA), Portugal (ACEPI), Spain (Adigital)**.
  **Negative finding: Hungary is not a member.** Company members named include Vinted and
  Whatnot. Individual national association member lists were **not** fetched; whether each
  publishes its own member directory is unverified.
- **Last checked:** 2026-08-25

### CLECAT, full members

- **Type:** community / trade association
- **Geography:** EU
- **Homepage:** https://www.clecat.org
- **List page:** https://www.clecat.org/members/full-members
- **Publicly listed?** yes
- **Machine readable?** plain text blocks with addresses, contacts and websites, not
  semantic list markup
- **Update cadence:** slow, on membership change
- **Why it surfaces card candidates:** same directory-of-directories logic for freight
  forwarding, logistics and customs. Each national association (e.g. PIFFA in Poland) holds
  a member list of forwarders, which is the customer base a logistics platform issues driver
  and fuel cards to.
- **Approximate list size:** members from 24 countries
- **Confidence:** Verified
- **Evidence:** Fetched https://www.clecat.org/members/full-members. **Poland (PIFFA),
  Romania (ROUBROKER and USER, two associations), Hungary (HLLC) confirmed present.
  Negative finding: Czechia is not a full member.** Format is plain text with line breaks,
  so parsing will need work.
- **Last checked:** 2026-08-25

### HOTREC (hospitality) and FIEC (construction)

- **Type:** community / trade association
- **Geography:** Europe
- **Homepage:** https://www.hotrec.eu/en/ and https://www.fiec.eu
- **List page:** https://www.hotrec.eu/en/membership.html ,
  https://www.fiec.eu/fiec/fiec-members
- **Publicly listed?** yes (per snippets)
- **Machine readable?** unknown
- **Update cadence:** unknown
- **Why it surfaces card candidates:** same pattern as CLECAT for two more card-heavy
  verticals. HOTREC reportedly represents 47 member associations across 36 countries; FIEC
  reportedly 33 national federations across 28 countries.
- **Approximate list size:** HOTREC 47 associations, FIEC 33 federations (both reported)
- **Confidence:** Reported
- **Evidence:** Search snippets only. **Neither members page was fetched.** Country
  coverage for the MVP markets is unconfirmed for both.
- **Last checked:** 2026-08-25

---

## 8. Puzzle-piece patterns

Everything in this section is a **PROPOSAL**. Each pattern is built only from attributes
that are observable in a source named above, and each states which source detects it. None
has been backtested. The lead-time figures are reasoned estimates, not measurements, and
should be treated as hypotheses to be validated against the register's existing 32
greenfield accounts before anyone acts on them.

### Pattern A: money already moves through it, but it does not own the instrument

**Observable pieces**

1. Business model is marketplace or SaaS-with-payouts, not pure subscription.
   *Detected by:* Dealroom business-model + income-stream filters (§4); Market One Capital
   portfolio sector tags.
2. A platform PSP is already integrated. Visible in the checkout flow, in the terms of
   service, or in the PSP's own customer page.
   *Detected by:* Swan customers page, Mangopay client references, Adyen for Platforms and
   Stripe Connect case studies; or by fetching the target's own `/terms` page and grepping
   for the PSP name.
3. The platform has a **payout obligation to third parties** it does not employ:
   subcontractors, drivers, hosts, practices, suppliers.
   *Detected by:* the company's own product page language ("get paid", "payouts",
   "settlement"), plus the vertical taxonomy in Capterra.
4. Series A or later.
   *Detected by:* Dealroom / Vestbee.

**Why it predicts a card program:** the platform has already accepted that money flows
through it and has already paid an integration cost to make that happen. The next
unsolved problem is outbound spend control, which is a card. The three pieces together
distinguish this company from a subscription SaaS that will never need issuing.

**Evidence this shape is real:** every one of the 13 Swan customers and 5 Weavr case
studies fits it, and none of them is a fintech by sector tag. That is corroboration, not
proof, because it is selected on the outcome.

**Estimated lead time:** 12-18 months from PSP integration to card launch. **Unmeasured.**

### Pattern B: the first payments hire in a non-financial company

**Observable pieces**

1. A job title containing payments / embedded finance / card / issuing / payouts.
   *Detected by:* Greenhouse and Ashby board API sweep (§3); justjoin.it, StartupJobs.cz,
   Profession.hu, NoFluffJobs keyword search.
2. The company's own sector classification is **not** financial services.
   *Detected by:* Dealroom taxonomy as the negative filter.
3. It is the **first** such role. No existing payments team, no prior payments postings.
   *Detected by:* Ashby's `department` and `team` fields, which reveal a new department
   being created; Greenhouse's `content=true` variant for department; posting history.
4. Seniority is mandate-carrying, Head of / Lead / Principal rather than analyst.
   *Detected by:* justjoin.it seniority filter (includes C-level); NoFluffJobs salary band.

**Why it predicts a card program:** companies hire a payments owner when payments has been
promoted from an integration to a product line. Nobody hires a Head of Payments to keep
using Stripe Checkout.

**Evidence the detection works:** a domain-restricted search of justjoin.it during this
pass returned a live Payments Operation Manager role at Code and Pepper, a software house
rather than a licensed institution. One example, and it happens to be an agency, so it is
a weak positive. The mechanism fired; the precision is unknown.

**Estimated lead time:** 6-18 months. **Unmeasured.** This is the pattern with the
strongest theoretical lead time and the one most worth backtesting first, because the
backtest is cheap: take the 32 known greenfield accounts and any recent European card
launch, and check whether a payments role appeared on their ATS board 6-18 months prior.

### Pattern C: regulatory footprint before product footprint

**Observable pieces**

1. The company appears as a **PSD2 agent or distributor** in the EBA register, or in the
   KNF MIP register in Poland, while its primary business is non-financial.
   *Detected by:* EBA register monthly download diff; cashless.pl for Poland.
2. It files a **Nice class 36 trademark** when its prior filings are class 9 / 42 only.
   *Detected by:* EUIPO eSearch plus (mechanism unverified, see §5).
3. Its corporate registry record adds a payments-related activity code.
   *Detected by:* national business registers. **Not researched this pass.**

**Why it predicts a card program:** all three are filings a company makes because it has
already decided, and they are all cheap, public and boring enough that nobody watches them.
This is the closest thing found to Ian's "a deal on the street that we didn't know about".

**Confidence:** the EBA register mechanism is Verified as an accessible daily-updated
machine-readable file containing agents. **The lead-time claim is pure inference.** The
class-36 mechanism is unverified. The MIP sample I looked at contained no obviously
non-financial companies, so piece 1's Polish variant is currently unsupported.

**Estimated lead time:** 1-6 months for agent registration, 3-12 months for a trademark
filing. **Both unmeasured.**

### Pattern D: captive spend with a compliance problem

**Observable pieces**

1. The vertical has a fragmented supplier base that must be paid **at the point of
   service**: fuel, tolls, charging, parking, hotel, parts, materials.
   *Detected by:* trade association member directories (CLECAT, HOTREC, FIEC) and trade
   media (trans.info, Hospitality Net, PhocusWire).
2. An existing closed-loop or manual mechanism is in place: a fuel card, a petty cash
   float, a reimbursement process, a company credit card handed around.
   *Detected by:* the platform's own help documentation and trade media.
3. There is a tax or regulatory reporting duty on that spend (VAT reclaim, fuel duty,
   per-diem rules, driver hours).
   *Detected by:* trade media and association policy pages.

**Why it predicts a card program:** the incumbent closed-loop instrument is what gets
displaced, and the compliance duty is what makes a switch worth the effort. This is the
Circle K, Octopus Electroverse, ryd and FLEET220 shape, all four of which were confirmed
this pass as real launches by non-financial companies.

**Note on use:** this pattern selects **verticals**, not companies. Use it to decide which
Capterra categories and which association directories to enumerate, then apply Patterns A
and B inside them.

### Pattern E: the marketplace hitting its take-rate ceiling

**Observable pieces**

1. Marketplace with growing GMV but a take rate that cannot go up without churn.
   *Detected by:* rarely public. Proxy: the company publicly discusses "monetisation" or
   "new revenue streams", or an investor page describes it as expanding into services.
2. Its investor's portfolio-page description changes to mention financial services.
   *Detected by:* Market One Capital portfolio page diff (plain HTML, easily diffed).
3. Pattern B fires at the same company.

**Why it predicts a card program:** financial services is the standard answer to a
take-rate ceiling, and issuing is the highest-margin part of it.

**Confidence:** weakest pattern here. Piece 1 is largely unobservable from public sources,
which is exactly the honesty this document is supposed to carry. **Recorded because piece
2 is genuinely cheap: diffing a 46-row HTML table monthly costs nothing and the brief
explicitly asked for "a fund whose portfolio page updates before the funding is
announced".** Whether MOC's page actually updates ahead of announcements was not tested.

### Pattern F: composite score

**PROPOSAL for operationalising the above.** Score each candidate on seven binary pieces:

| # | Piece | Source |
|---|---|---|
| 1 | Sector tag is non-financial | Dealroom |
| 2 | Business model is marketplace or SaaS-with-payouts | Dealroom, MOC portfolio |
| 3 | Platform PSP already integrated | Swan / Mangopay / Stripe / Adyen customer pages, target's own T&Cs |
| 4 | Series A or later | Dealroom, Vestbee |
| 5 | First payments hire posted | Greenhouse / Ashby API, CEE job boards |
| 6 | Nice class 36 trademark filed | EUIPO eSearch (unverified) |
| 7 | Appears as PSD2 agent in a national register | EBA register download |

Pieces 1-4 are **static** and answer "who is out there right now that the register misses",
the brief's first-hit job. Pieces 5-7 are **event-driven** and answer "what fires when a
new candidate appears", the ongoing job. A candidate scoring 1-4 belongs in the corpus at
low priority. A candidate scoring 1-4 **plus any of 5, 6 or 7** is the one that should
trigger an alert inside the month.

**This threshold is asserted, not derived.** It needs calibrating against the 32 existing
greenfield accounts before it is trusted.

---

## 9. Recommended next actions for whoever picks this up

1. **Backtest Pattern B first.** It is the cheapest test with the highest claimed value.
   Take 20 known European card launches by non-financial companies from the Enfuce
   newsroom, Swan customers page and the Visa Fleet 2.0 announcements, resolve each
   company's ATS, and check whether a payments role appeared 6-18 months before launch.
   That single experiment either validates or kills the strongest claim in this document.
2. **Download the EBA register once** and inspect the agent records. If agents carry a
   website or company number, Pattern C piece 1 is buildable this quarter. If they carry
   only a name, it is much weaker.
3. **Get a browser onto the four blocked sources**: eJobs.ro, NoFluffJobs, PhocusWire,
   EUIPO eSearch. All four are potentially significant and all four are unread.
4. **Run one real EUIPO class-36 query** against a company known to have launched a card,
   and check whether the filing predates the launch. That converts the most original idea
   here from a proposal into a source, or kills it.
5. **Enumerate the national e-commerce associations** behind Ecommerce Europe (eIZBA, APEK,
   ARMO) and check whether each publishes a member directory. If they do, that is a
   merchant and marketplace population for three of four MVP markets that exists in no
   startup database.
