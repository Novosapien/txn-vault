---
description: "Adversarial validation of stream 05: 18 of 20 Verified entries intact, the EBA register twice the claimed size, NoFluffJobs promoted to an open API"
---

> **Section:** [[research]]
> **File under test:** [[stream-05-vertical-saas-fringe]]
> **Method:** independent agent, no contact with the authoring agent's notes, re-fetching with a different toolchain.

# Validation: 05 Vertical SaaS and marketplace fringe

**Validator:** independent adversarial check
**File under test:** `sources/05-vertical-saas-fringe.md`
**Date of validation:** 2026-08-25
**Method:** every entry marked `Verified` was re-fetched independently, by `curl`
with a browser user agent and/or WebFetch. Counts stated in the file were
recounted from raw HTML/JSON rather than taken on trust. Load-bearing API claims
were called directly. The "could not verify" section was spot-checked for
premature surrender.

---

## 1. Headline verdict

**The file is trustworthy. It was not invented.**

Twenty entries carry the `Verified` label. **Eighteen survive fully intact.
Two are partly confirmed. None is refuted.** Not a single fabricated URL, company
or programme was found. Every specific number I recounted either matched exactly
or differed only by live-counter drift in the expected direction.

The evidence that the research pass was genuinely executed is unusually strong,
because the file quotes artefacts that cannot be guessed:

- It quotes the Ashby payload as `"title":" Security Engineer, Cloud"` **with the
  leading space**. That leading space is really in Ramp's data. Nobody invents that.
- It quotes the Greenhouse response for GoCardless down to
  `"updated_at":"2026-08-20T06:33:26"` and job id `8141651`. Both are exact.
- It quotes Profession.hu's counter as `4395 hirdető, 17656 hirdetés`. The
  advertiser count is still exactly 4395 today; the ad count has moved to 17,662.
- It reports Profesia.sk's Bratislava figure as 4,860. It reads 4,861 today.
- It reports five negative findings (four dead URLs, one absent country) that I
  independently reproduced. A fabricating agent does not go looking for 404s.

The failures I did find are of one specific kind: claims imported from model
memory or search snippets that were attached to entries the file then labelled
`Verified` on the strength of a different, genuinely-fetched claim. That is a
real defect and four items must be corrected before this reaches the client. But
it is a labelling discipline problem, not invention.

Separately, and more usefully: **the file gave up too early on three sources in
its own honesty section, and one of them is its single most original idea.** All
three work. Details in §5.

---

## 2. The load-bearing claims

### 2.1 Greenhouse job board JSON endpoint: CONFIRMED

```
curl https://boards-api.greenhouse.io/v1/boards/gocardless/jobs
→ HTTP 200, application/json, 26 jobs, no auth, no signup
```

First record returned:
`absolute_url: https://job-boards.greenhouse.io/gocardless/jobs/8141651`,
`id: 8141651`, `location: {"name":"Leeds, UK"}`,
`updated_at: 2026-08-20T06:33:26-04:00`.

Every element the file quoted is present and identical. The claim is exact.

I additionally tested the `content=true` variant the file relies on in §3.9 step 4
("Greenhouse exposes department via the `content=true` variant"). **Also confirmed.**
The expanded payload adds `content`, `departments`, `offices`,
`ai_disclaimer`, `include_ai_disclaimer`, `ai_opt_out_request_url`. Departments come
back structured with parent/child ids:
`departments: [{"id":965,"name":"Sales","child_ids":[],"parent_id":null}]`.
`/v1/boards/{token}/departments` is also a live 200 endpoint, which the file did not
mention and which is a cleaner way to do step 4.

### 2.2 Ashby posting API and its `department` / `team` fields: CONFIRMED

```
curl https://api.ashbyhq.com/posting-api/job-board/ramp
→ HTTP 200, application/json, 137 jobs, no auth
```

Top-level keys `jobs`, `apiVersion`. Per-job fields:

```
id, title, department, team, employmentType, location, secondaryLocations,
publishedAt, isListed, isRemote, workplaceType, address, jobUrl, applyUrl,
descriptionHtml, descriptionPlain
```

`department` and `team` are both present on 100% of records. The file's specific
operational claim, that these fields let you distinguish a *new payments team*
from a backfill, is mechanically supported. The quoted first record matches
verbatim including the leading space in the title.

Board-name portability spot-check: `deel` 200, `notion` 200, `vinted` 404. The
endpoint shape generalises; token discovery is the real constraint, which the file
correctly identifies as a one-off enrichment step.

### 2.3 Market One Capital: PARTLY CONFIRMED

**The two numbers the client would act on are exactly right.** I downloaded
`https://www.moc.vc/portfolio` (HTTP 200, 224,813 bytes, static HTML) and parsed
the sector column myself:

```
TOTAL PORTFOLIO ROWS: 46      ← file says 46, correct
FinTech:                5      ← file says 5, correct
```

Full sector distribution I counted: FinTech 5, Ecommerce 4, Logistics 3,
HealthTech 3, Travel 3, Content Creation 2, Gaming 2, EdTech 2, Circular economy 2,
Quick Commerce 2, Leisure 2, FoodTech 2, and one each of Cybersecurity, AI
infrastructure, Energy, Data infrastructure, Productivity, HRTech, Infrastructure
Provider, CleanTech, AgriTech, PropTech, Micromobility, Beauty, Business Services,
Automotive.

Every vertical count the file asserts checks out: Logistics 3, Travel 3, HealthTech 3,
FoodTech 2, AgriTech 1, PropTech 1, Automotive 1, Leisure 2, Micromobility 1.
**The "41 of 46 invisible to a fintech filter" claim is correct.**

"Machine readable? HTML table with inline sector tags, not JS-rendered" is
confirmed. I parsed it with a regex against raw curl output; no browser needed.

Warsaw base is **confirmed, but not from the page the file cites.** The moc.vc
FAQ states the majority of the team is based in Warsaw, Poland. The team page lists
nine people, all with Polish names.

**Three sub-claims on this entry are wrong or unsupported:**

| File says | Site says |
|---|---|
| "offices in Spain and Luxembourg" | Only one office is listed anywhere on moc.vc: 28 boulevard d'Avranches, L-1160 Luxembourg. The FAQ explicitly names no Spanish office. (Two portfolio companies, Genially and Nautal, are Spanish, which is the likely source of the confusion.) |
| "actively deploying from a €80m Fund II" | No fund size appears anywhere on the site. The investment-profile page states **€140m AUM across funds**. "Market One Capital II SCSp" exists as a named vehicle; its size is not disclosed. |
| "fund reports 60+ total investments" | The investment-profile page states **"80+ Companies"** and "3 unicorns". |

None of these came from the portfolio page the Evidence line cites. They should be
struck or re-sourced.

**One curiosity, not an error.** The file lists "Arise" under Travel and "Petsapp"
under HealthTech; the rendered page shows those rows as "Asap.work" and "Routine".
MOC's own markup is internally inconsistent: the row slugs are `/portfolio/arise`
and `/portfolio/petsapp`, the logo files are `arise_logo_400x240.webp` and
`petsapp.png`, and the outbound links are `arise.travel` and `petsapp.com`, while
the display name has been changed. The file read the underlying identity. That is
the source page being messy, not the agent being wrong.

### 2.4 EBA central register: PARTLY CONFIRMED, and the scale figure is wrong

Everything mechanical the file claims is true, and the source is **better** than
the file says. The one specific number is off by more than 2x.

I traced the download properly, which the file did not do. The path is:

```
GET https://euclid.eba.europa.eu/register/api/filemetadata   → HTTP 200, JSON:
{
 "latest_version_relative_zip_path":"20260824/download-PSDMD-202608241600.zip",
 "latest_version_relative_zip_size":"19828208",
 "sha256_hash":"59c49826ad71...",
 "timestamp":"Mon Aug 24 16:00:29 UTC 2026",
 "golden_copy_path_context":"https://euclid.eba.europa.eu/register/downloads/PSDMD/"
}
```

Concatenating those two fields gives the file. I downloaded it: **HTTP 200,
19,828,208 bytes, no authentication, no cookie, no disclaimer acceptance
enforced server-side.** It unzips to a single 218 MB JSON plus a SHA-256 sidecar.

- **Downloadable without authentication: CONFIRMED.**
- **Machine readable: CONFIRMED** (single JSON array, no scraping).
- **Daily update: CONFIRMED.** The golden copy is stamped yesterday, 24 Aug 2026
  16:00 UTC, and individual records carry `__EBA_EntityVersion` timestamps.
- **Nine entity categories: CONFIRMED, exactly nine**, and they map one-to-one
  onto the nine the file listed.

Now the count. I parsed all 329,149 records:

| EntityType | Count | Meaning |
|---|---:|---|
| PSD_AG | **322,494** | **agents** |
| PSD_EPI | 2,758 | exempted payment institutions |
| PSD_EXC | 1,659 | excluded providers |
| PSD_PI | 1,014 | payment institutions |
| PSD_EMI | 427 | e-money institutions |
| PSD_ENL | 336 | nationally entitled providers |
| PSD_BR | 244 | EEA branches |
| PSD_AISP | 129 | account information service providers |
| PSD_EEMI | 88 | exempted EMIs |
| **Total** | **329,149** | |

**The file says "~150,000 agents". The register holds 322,494 agent records.**
Of those, 126,288 are `Active` and 196,206 are `Inactive`. So neither the total nor
the active subset is 150,000. The figure was not derived from the file, since the
entry admits the download was never opened, and it should be replaced.

**Three findings the file wanted and could not get.** §9 action 2 asks whether agent
records carry a website or company number. They answer as follows, from 322,494
records at 100% field coverage:

```
ENT_NAT_REF_COD  100.0%   national reference / company number (e.g. IT104749184)
ENT_NAM          100.0%   name
ENT_ADD          100.0%   street address
ENT_TOW_CIT_RES  100.0%   town
ENT_POS_COD      100.0%   postcode
ENT_COU_RES      100.0%   country
ENT_TYP_PAR_ENT  100.0%   parent entity type
ENT_COD_PAR_ENT  100.0%   parent entity code
DER_CHI_ENT_AUT  100.0%   Active / Inactive
```

1. **There is no website field anywhere in the register**, for any entity type. I
   checked the full property vocabulary across all 329,149 records; the only fields
   that exist are the nine above plus `ENT_AUT`, `ENT_EXC`, `ENT_DES_ACT_EXC_SCP`
   and `ENT_NAM_COM`. So the automatic sector classification the file hopes for
   must be done by name-and-company-number matching against an external source, not
   by URL. Pattern C piece 1 is buildable, but it needs an entity-resolution step
   the file has not budgeted for.
2. **`DER_CHI_ENT_AUT` gives you the diff for free.** Active/Inactive is carried
   per record, so a month-over-month diff does not even need a stored baseline to
   detect status flips.
3. **The agent population is not what the file assumes, and this is the material
   correction.** Agents by country of residence: Spain 72,511, France 66,962,
   **Poland 66,168**, Italy 50,965, Germany 14,334, Greece 7,727, **Czechia 6,620**,
   **Romania 4,300**, **Hungary 151**. A random sample of Polish agent names reads:
   *BANK SPOLDZIELCZY W TARNOGRODZIE*, *WACHOWICZ, NADIA*, *SEWERYN BAJRAMOW*,
   *Ubezpieczenia Ap Agnieszka Poroslo*, *Kantor Trust Sp. z o.o.*,
   *P.H.U. CB KOM Paweł Syczak*. This population is overwhelmingly sole traders,
   natural persons, currency-exchange kiosks and insurance agencies acting as
   money-remittance agents. The file's premise, that "when a vertical SaaS platform
   embeds a card product, it very often appears first as an agent", is not
   supported by what is actually in the file. The signal-to-noise is far worse than
   the entry implies, and Hungary at 151 records is effectively empty for an MVP
   market. This does not kill the source, but the entry must say so.

### 2.5 Dealroom business model and income stream as separate dimensions: CONFIRMED

All five numbers on the taxonomy page are exact:

- "31 industries, each with nested sub-industries", correct
- **"Business Models"** as a distinct dimension, with "Marketplace & eCommerce" and
  "SaaS" among the values, correct
- **"Income Streams"** as a further distinct dimension, values exactly
  *Advertising / Commission / Selling own inventory / Subscription*, correct
- "18 mutually exclusive sectors", algorithmically derived, correct
- "2,783 unique tags", correct

The central architectural claim, that Dealroom carries business model and income
stream **separately from industry**, which is what makes the file's target query
expressible, is correct. This is the load-bearing part and it holds.

Minor: the file says the tag layer includes "Vertical SaaS" and "Logistics".
"Logistics" appears on the page; **"Vertical SaaS" does not.** The page shows only
50 example tags out of 2,783, so the tag may well exist, but it was not on the
page that was read, and the entry presents it as though it was.

The gating caveat the file states (queryable lists behind login at
app.dealroom.co, export capability untested) is accurate.

### 2.6 The CEE job boards: ALL CONFIRMED

| Board | Claim | Result |
|---|---|---|
| justjoin.it | search box labelled "Job title, company, keyword" | **Exact.** Raw HTML: `placeholder="Search: Job title, company, keyword"` |
| justjoin.it | publication-date filter: yesterday / last week / last 2 weeks / last month | **Exact.** All four values present in the filter markup |
| justjoin.it | seniority filter includes C-level | **Confirmed**, 13 occurrences of `C-level` |
| justjoin.it | "1,435 offers in the PM category" | Reads **1 441** today. Live counter, correct order |
| justjoin.it | server-rendered enough to fetch | **Confirmed**, 1.9 MB of static HTML with content |
| justjoin.it | the Code and Pepper posting exists at the cited URL | **Confirmed.** HTTP 200, `<title>Payments Operation Manager - Code and Pepper` |
| StartupJobs.cz | filters: Location, Work Mode, Seniority, Salary, Employment Type, Type of Contract, Technology, Companies, Benefits, Languages | **All ten present**, in that order (page reads "Technologie") |
| StartupJobs.cz | "Search by industry, job title, or keyword" | **Exact string match** |
| Profession.hu | counter "4395 hirdető, 17656 hirdetés" | **4395 exact**; ad count now 17,662 (drift) |
| Profession.hu | 24 job categories, Adminisztráció to Vendéglátás | **23 categories.** First and last names exact, per-category range 54 to 3,906 vs the file's 54 to 3,909 |
| Profesia.sk | "5,050 employers" | Reads **5 054** today on the English homepage ("List of all companies 5 054"). Confirmed |
| Profesia.sk | ~16,000 active positions | Region counts sum to **16,476**. Confirmed |
| Profesia.sk | Bratislava region 4,860 | Reads **4 861** today. Confirmed |
| Profesia.sk | **no employer-industry filter** | **Confirmed with a nuance**, see below |
| BestJobs.eu | reachable, HTML cards | HTTP 200, 847 KB |
| Arbeitnow | unauthenticated JSON, fields as listed, `tags` includes Finance | **Exact.** 175 records, field list matches character for character, `Finance` appears 7 times in tags |

**On the Profesia.sk negative finding.** The file's claim is right in the sense that
matters. I checked every occurrence of "industry" on the homepage: all eight are the
company name "IKEA Industry Slovakia". There is a **"Pracovná oblasť"** (work-field)
facet on the Slovak listing page with values like Obchod 2,349, Výroba 1,811,
Administratíva 1,744, Doprava/špedícia/logistika 1,587, but that classifies the
**job**, not the **employer**, which is precisely the distinction the file's stream
depends on. The negative finding stands. It would be stronger if it named the
Pracovná oblasť facet and explained why it does not substitute.

**One interpretive overreach.** The StartupJobs.cz entry claims its **Companies**
filter is "what lets you separate 'fintech hiring a payments PM' from 'logistics
platform hiring a payments PM'". The Companies filter is a company-name picker, not
a sector classifier. It does not do that job. The "Search by industry" placeholder is
real, but a placeholder is not a proven facet. Soften this.

---

## 3. Every remaining `Verified` entry

| Entry | Verdict | What I obtained |
|---|---|---|
| EIT Urban Mobility portfolio | **CONFIRMED** | Page states "140+ startups in our investment portfolio". AgeVolt, Delivery Couple, Bruntor, DIGAS, .lumen all present with country labels. A.D. Knight, Arxax, Beev, Blike, Blowind all present. "Load more" control present. (The "350+ since 2020" and "127 from 29+ countries" figures were not visible on this page.) |
| Capterra field service directory | **CONFIRMED** | Page 1 of 44, exactly 25 products. Connecteam, Housecall Pro, Jobber, Infraspeak and Odoo all present with review counts. No country-of-origin filter, so the file's own caveat is correct. Not confirmed: that Capterra "states it lists all vendors, not only paying ones". That sentence is not on the page. |
| Enfuce newsroom | **CONFIRMED** | Counter reads exactly "All news posts (54)". Pagination 1 to 5. 12 items on page 1. Circle K, Monizze and Swile all named in page-1 headlines. No dates on the listing, correct. No RSS link, correct. `enfuce.com/press-releases/` returns **404**, correct. |
| Swan customers | **CONFIRMED** | Exactly 13 stories. All 13 names correct: Pennylane, MyUnisoft, Sibill, fulll.io, Betterfly, Accountable, Axonaut, Libeo, Lucca, Indy, Expensya, Syndic Yourself, Agicap. Industry filter present with the exact values listed. Product filter includes **Expense Cards**, correct (plus Local Accounts, Send/Accept Payments, Employee Benefits, Transfers, Tap to Pay, Online Cards). |
| Weavr case studies | **CONFIRMED** | Exactly 5: Ben, Club Employés, Peanuds, Finway, NUMARQE. `weavr.io/customers` returns **404**, correct, and the case-studies path is the right one. |
| trans.info | **CONFIRMED** | 11 language editions in the markup: en, pl, hu, ro, lt, ua, es, de, fr, it, ru. That is exactly the eleven the file lists. No RSS link found, so the file's caveat is correct. |
| Hospitality Net | **CONFIRMED** | Supplier News section, Technology section, "Publish your news on HN" press-release model, **RSS link in footer**, **no dedicated payments section**, "Online since 1994". Every element including both negatives. |
| Ecommerce Europe | **CONFIRMED** | Exactly **22** national associations. Poland eIZBA, Czech Republic APEK, Romania ARMO, Greece GRECA, Portugal ACEPI, Spain Adigital, all present. **Hungary absent**, so the negative finding is correct. Not on the page: the "150,000+ companies" figure. |
| CLECAT full members | **CONFIRMED** | Members across **24 countries**. PIFFA (Poland), ROUBROKER and USER (Romania, two associations), HLLC (Hungary) all present. **No Czech full member**, so the negative finding is correct. Format is unstructured plain text with addresses, phone, fax, email, website, not semantic list markup. |

---

## 4. Fabrication signatures: none found

I looked specifically for the things that give invented research away.

- **Dead URLs presented as live:** none. Every URL in a `Verified` entry resolved.
- **Invented companies:** none. Every company name I spot-checked exists: all 13
  Swan customers, all 5 Weavr studies, all 46 MOC portfolio rows, all six MIP
  entities in the cashless.pl article, all ten EIT Urban Mobility names.
- **Invented programmes:** none. Mastercard Product Express appears in an Enfuce
  page-1 headline, independently corroborating a §6 claim.
- **Untraceable statistics:** one, the EBA 150,000 (§2.4). Three more are
  attributed to pages that do not carry them: MOC's €80m and 60+, Ecommerce
  Europe's 150,000+ companies, Capterra's all-vendors statement.
- **The dead-URL findings are real, which is the strongest signal of all.**
  `enfuce.com/press-releases/` returns 404. `weavr.io/customers` returns 404.
  `mocap.vc` does not resolve. All three reproduced exactly. An agent writing
  from memory does not record its own failed domain guess.

I also reproduced the file's Recruitee finding independently. Probing nine
plausible tenant names (`recruitee`, `bolt`, `wise`, `pipedrive`, `dashlane`,
`trengo`, `teamleader`, `silverfin`, `showpad`) returned **404 on all nine**. The
file's warning "do not rely on the tenant-guessing approach" is correct and
well-judged.

---

## 5. Is the honesty section honest? Mostly, but it surrendered too early three times

The brief asked me to check both failure modes. I found no case of the file
claiming something was unverifiable to hide a weak claim. I found three cases of
**giving up on something that works**, and one of them matters a great deal.

### 5.1 NoFluffJobs (§2 item 2): REFUTED. It works, and it has a public API.

The file says WebFetch was blocked at the tool level, marks the source `Reported`,
and calls it "potentially the single best CEE job board for this purpose". The agent
used `curl` elsewhere in the same pass (Greenhouse, Ashby, EUIPO, EBA) but did not
try it here.

```
curl -A "<browser UA>" https://nofluffjobs.com/pl/jobs   → HTTP 200, 712,996 bytes
```

It is not blocked. It is a WebFetch limitation, not a site limitation. And it is
better than the file hoped:

```
GET https://nofluffjobs.com/api/joboffers/main?salaryCurrency=PLN&salaryPeriod=month&region=pl
→ HTTP 200, application/json, 2,087,133 bytes
  totalCount: 20,889 postings
  per-posting fields: id, name (employer), location, posted, renewed, title,
  technology, logo, category, seniority, url, regions, fullyRemote, salary, ...
```

**NoFluffJobs exposes an unauthenticated JSON job API carrying employer name, job
title, category, seniority, salary band and posting date across 20,889 live
postings.** By the file's own ranking logic that puts it alongside Greenhouse and
Ashby in the top tier, not in the "could not verify" list. It should be promoted to
`Verified`, moved into §3 as an API source rather than a scrape target, and the
"needs browser verification" note deleted. The mandatory-salary-band secondary
signal the file theorised about is a first-class field in the payload.

I ran the file's own technique against it as a sanity check: a keyword sweep over
page 1 (283 postings) returned one payments hit, at ING Bank, which is a bank and
therefore a true negative for this stream. Small sample, but the mechanism runs.

### 5.2 eJobs.ro (§2 item 1): REFUTED. Reachable, with keyword search.

The file says Romania's largest job board "could not be reached at all" and
substitutes the weaker BestJobs.eu, calling Romania "currently the weakest-covered"
MVP market in the stream.

```
curl -A "<browser UA>" https://www.ejobs.ro                          → HTTP 200, 1,184,901 bytes
curl -A "<browser UA>" https://www.ejobs.ro/locuri-de-munca/payments → HTTP 200, 979,677 bytes
  <title>Locuri de Munca Payments • 104 Joburi • August 2026 - eJobs
```

Not only reachable, but the keyword-search URL pattern is trivially predictable
(`/locuri-de-munca/{keyword}`) and it returns a live count: 104 payments jobs in
Romania right now. Again, WebFetch was blocked and curl was not tried. Romania is
not the weakest-covered MVP market; it just was not checked properly.

### 5.3 TMview API (§2 item 5): REFUTED. The POST works.

This is the most consequential of the three, because the class-36 trademark idea is
the file's most original contribution and it is currently shelved as a proposal.
The file states the TMview search API "returned HTTP 000 (connection failed) with
several header/body variants" and concludes "no programmatic access confirmed".

```
POST https://www.tmdn.org/tmview/api/search/results
Content-Type: application/json
{"page":"1","pageSize":"10","criteria":"C","basicSearch":"pay",
 "fOffices":["EM"],"fNiceClass":["36"]}

→ HTTP 200, application/json
  {"tradeMarks":[...], "page":1, "totalPages":..., "totalResults":2926}
```

**2,926 results, unauthenticated, filtered on EUIPO office and Nice class 36.**
Per-trademark fields returned:

```
ST13, tmName, tmOffice, applicationNumber, registrationNumber, tradeMarkStatus,
niceClass, applicantName, applicationDate, registrationDate, tradeMarkType,
viennaCodes, oppositionPeriodStart, oppositionPeriodEnd, oppositionDeadLine
```

`niceClass` comes back as an array per mark (e.g. `[9,16,35,36,37,38,41,42,45]`),
and `applicantName` and `applicationDate` are both carried. **That is exactly the
field set Pattern C piece 2 requires**: filter by applicant, read their class list,
watch for a class-36 mark appearing where prior filings were class 9 and 42 only,
and date it against launch.

The EUIPO's own `copla` endpoint also returns unauthenticated JSON per mark
(`https://euipo.europa.eu/copla/trademark/data/{number}` returns HTTP 200 and
17.9 KB of JSON).

So the file's most interesting idea is **not** "a PROPOSAL resting on an unverified
mechanism". The mechanism is live and machine-readable today. §5 and §9 action 4
both need rewriting to reflect that. This is a genuine upgrade to the document, and
the only reason it was missed is that the POST was tried against a blocked path or
with a malformed body and then abandoned.

### 5.4 The honesty items that hold up

| Item | Verdict |
|---|---|
| §2.3 PhocusWire returns 403 | **CONFIRMED.** Still 403 with a full browser user agent. Genuinely blocked. |
| §2.4 EUIPO eSearch UI: 403 to WebFetch, 200 to curl | **CONFIRMED.** `https://euipo.europa.eu/eSearch/` returns HTTP 200, 12,989 bytes. |
| §2.6 Recruitee tenant guessing unreliable | **CONFIRMED.** 9 of 9 probes 404. |
| §2.9 Dealroom filter URLs behind login | **CONFIRMED.** Only the public taxonomy is readable. |
| §2.10 KNF register URL not confirmed | **CONFIRMED, and I could not confirm it either.** `knf.gov.pl/podmioty/wyszukiwarka_podmiotow` returns 200 but is a JS shell containing no MIP register; `rpu.knf.gov.pl` is the insurance-intermediary register, not payments. The file is right to leave this open. |
| §2 general: cashless.pl article | **CONFIRMED.** `cashless.pl/8684-6-nowych-mip` returns HTTP 200, title *"Sześć nowych małych instytucji płatniczych w rejestrze KNF-u. Na liście jest już 75 podmiotów"*. All six named entities present. The "75+" figure is on the page. The file's self-criticism, that all six read as payments-native names so the non-financial premise is untested, is accurate and creditable. |

---

## 6. Must be corrected before this reaches the client

Ordered by cost of being wrong.

1. **EBA agent count.** Replace "~150,000 agents" with **322,494 agent records
   (126,288 Active, 196,206 Inactive), of 329,149 total records** in the 24 Aug 2026
   golden copy. Cite the `filemetadata` endpoint and the download path, both given
   in §2.4 above.
2. **EBA composition caveat.** Add that the agent population is dominated by sole
   traders, natural persons and small local businesses acting as money-remittance
   agents, and that Hungary carries only 151 agent records. Pattern C piece 1 needs
   this or it will be built on a false expectation of signal density.
3. **EBA field set.** Replace the "not verified" note with the actual answer:
   agents carry a national reference/company number at 100% coverage and an
   Active/Inactive flag, but **there is no website field anywhere in the register**.
   §9 action 2 is now answered and can be struck.
4. **Promote NoFluffJobs to `Verified`** and move it into §3 as an unauthenticated
   JSON API source (`/api/joboffers/main`), not a blocked scrape target. This
   materially strengthens the file's strongest recommendation.
5. **Correct the eJobs.ro finding.** It is reachable via curl and supports
   predictable keyword-search URLs. Remove the claim that Romania is the
   weakest-covered MVP market on that basis, and demote BestJobs.eu to a supplement.
6. **Rewrite the EUIPO and TMview section.** The class-36 mechanism is verified and
   programmatically accessible. Move it out of "PROPOSAL" status, record the working
   POST body and the returned field set, and rewrite §9 action 4 from "run one real
   query to see if this works" to "backtest known launches against filing dates".
7. **Fix the three Market One Capital sub-claims:** office footprint (Luxembourg
   only on-site, team in Warsaw per the FAQ, no Spanish office), fund size (site
   says €140m AUM across funds, not €80m Fund II), investment count (site says
   80+ companies, not 60+). The 46 and 5 portfolio numbers are correct and stay.
8. **Minor factual fixes:** Profession.hu has 23 categories, not 24. "Vertical SaaS"
   is not among the tags shown on the Dealroom taxonomy page. The Ecommerce Europe
   "150,000+ companies" figure is not on the cited page. The Capterra
   "lists all vendors, not only paying ones" statement is not on the cited page.
9. **Two framing softenings:** the StartupJobs.cz **Companies** filter is a
   company-name picker, not a sector classifier, and cannot do the fintech versus
   logistics separation the entry credits it with. And Enfuce does not
   "consistently" name a non-financial partner: page 1 includes Payac (Irish credit
   unions) and Avida (a lender). The pattern is real but it is not consistent.

**None of the above changes a conclusion in the file.** The three top-line findings
survive intact and two of them get stronger: the ATS endpoints are real and
unauthenticated (and NoFluffJobs joins them), Market One Capital's 41-of-46
non-fintech split is exactly right, and the EBA register is a genuinely downloadable
daily machine-readable file that is twice the size the file claimed, with a
signal-density caveat that must be stated.

---

## 7. Score

| | Count |
|---|---:|
| Entries labelled `Verified` | 20 |
| **Fully confirmed** | **18** |
| **Partly confirmed** | **2** (Market One Capital, EBA register) |
| Refuted | **0** |
| Fabricated URLs found | **0** |
| Fabricated companies or programmes found | **0** |
| Negative findings independently reproduced | 8 of 8 |
| Items in §2 "could not verify" that actually work | **3 of 13** (NoFluffJobs, eJobs.ro, TMview API) |
| Items in §2 that are genuinely blocked | confirmed for PhocusWire, EUIPO WebFetch, Recruitee, Dealroom, KNF |

**Trustworthiness: high.** The research was performed, not invented. The
verification discipline the README asked for was largely followed, and the file's
self-criticism is real self-criticism rather than decoration: it repeatedly
undercuts its own best ideas where the evidence is thin.

The one systematic weakness to feed back: the `Verified` label was applied at
**entry** level when the underlying fetch only supported **some** of the entry's
claims. Market One Capital, the EBA register, Capterra, Dealroom and Ecommerce
Europe each carry at least one sentence sourced from memory or a snippet sitting
inside an entry stamped `Verified`. The fix is per-claim rather than per-entry
marking, or a stricter rule that anything not on the fetched page goes in a
separate `Reported` line.

And the one opportunity: **the file underrates itself in three places.** NoFluffJobs,
eJobs.ro and the TMview class-36 API all work. The agent hit a tool limitation and
recorded it honestly, which is right, but it had `curl` in hand and did not reach
for it. Two of those three are in the MVP markets, and the third is the most
original idea in the document.
