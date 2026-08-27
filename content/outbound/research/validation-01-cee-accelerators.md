---
description: "Adversarial validation of stream 01: 35 entries checked, 23 intact, 9 corrected, none refuted, plus the eight fixes required before client use"
---

> **Section:** [[research]]
> **File under test:** [[stream-01-cee-accelerators]]
> **Method:** independent agent, no contact with the authoring agent's notes, re-fetching with a different toolchain.

# Validation report: Stream 01, CEE accelerators, incubators and startup programmes

Independent adversarial check of `sources/01-cee-accelerators.md`.

Validated 2026-08-25. Method: direct URL fetching with `curl` and a desktop
Chrome user-agent (the technique the source file itself documents), plus
`openssl s_client` for certificate checks, XML sitemap reads, JS bundle reads
and one WebFetch where the origin sits behind Incapsula. No claim in this report
rests on a search-engine snippet.

## Headline verdict

**The file is sound. It was not invented.**

Every one of the 35 entries points at a real programme. Every death and
absorption claim is true. The three highest-risk numeric claims (Rubik Hub's
600+ startups, start it @ČSOB's 130 over 17 cohorts, Nápad roku's 2,652 projects
over 18 editions) reproduce **verbatim** off the live pages. Several evidence
notes are precise to the byte, which is not something a fabricating agent
produces: the source says Rubik Hub returned "1.35 MB HTML" and it returns
1,351,698 bytes; it says Wschodni Akcelerator Biznesu had "279 applications as
of 3 August 2026" and the page reads "03 sierpnia 2026 / Do 8 rundy wpłynęło 279
wniosków".

**32 entries carry a `Verified` component. 23 survive intact. 9 need a
correction. 0 are refuted outright.** Three specific claims inside otherwise
sound entries are wrong and must be fixed before this reaches Ian. Two of the
three corrections make the source *better*, not worse.

The file's own self-accounting is accurate: 35 entries, 32 with a `Verified`
component, 1 `Reported`, 2 `Unverified`. I counted them and the arithmetic holds.

---

## 1. Rubik Hub, the load-bearing claim

**Verdict: PARTLY CONFIRMED. The substance is right. Four details are wrong.**

This is the claim the whole stream is sold on, so I attacked it hardest.

What reproduces exactly:

- `curl` with a full Chrome UA returns **HTTP 200, 1,351,698 bytes**. The source
  claimed 1.35 MB. Exact.
- The page's own meta description and body copy: *"Since 2017, we've worked with
  over 600 startups that build solutions the world really needs."* Confirmed.
- **FinTech vertical filter: confirmed.** Elementor `e-filter` buttons,
  `data-filter="fintech"`, plus a `.startup-vertical-select` dropdown.
- **Country filter: confirmed.** `.startup-country-select` plus per-card
  taxonomy classes. 22 countries present: Romania 181, Moldova 10, Italy 10,
  Ukraine 8, Bulgaria 7, Poland 4, Czech Republic 2, Hungary 1.
- **Programme and cohort per company: confirmed.** 240 of 249 cards carry a
  `Program: <name>, Cohort N` line. Labels seen include "Rubik Garage
  Accelerator, HealthTech Edition 2025-2026", "Rubik Scale to USA 2024, Cohort
  2", "WIPO IP Management Clinic Program 2026", "Rubik Scale to UK 2025". The
  source's cohort-dating use case works.
- **INACTIVE markers: confirmed**, 86 occurrences.
- **All three named fintechs exist on the page**, with the exact descriptions
  quoted:
  - **Finergy:** "Finergy helps banks offer instant payment services to their
    customers." `Program: Rubik Scale to UK 2025`. Country: **Republic of
    Moldova** (the source's write-up does not say Romania, so this is fine, but
    it is worth knowing the best-named fintech on the page is Moldovan).
  - **DDD Invoices:** Slovenia, `# FinTech`, "a single API for global
    e-invoicing compliance", `Rubik Garage Accelerator, CEE Edition 2023, Cohort
    5`, `Investment raised: €1.31 million`.
  - **Conta25:** Romania, `# FinTech`, SaaS for accountants, same cohort.
  - Signal Sigma and Equinox AI also present and correctly described.

What is wrong:

1. **The URL redirects to a different domain.** `https://rubikhub.ro/startups/`
   301s cross-host to `https://rubikhub.com/startups/`. The file records the
   `.ro` URL as the list page. Not fatal, but a scraper config built off the file
   will take an unnecessary redirect hop, and WebFetch refuses cross-host
   redirects, which is a plausible partial explanation for the reported 403.
2. **"Several hundred entries" is 249.** I counted the loop items precisely:
   **249 cards**. The 600+ figure is the site's cumulative since-2017 claim, and
   the file does correctly separate the two, but "several hundred" reads as ~500
   and it is 249.
3. **7 FinTech-tagged cards, not 8.** The string "FinTech" appears 8 times in the
   HTML; only 7 of those are card labels.
4. **"Investment raised" is not on every entry.** It appears on **69 of 249**
   cards (28%). The write-up says "Each entry carries a vertical tag ..., a
   country, the exact programme and cohort, and investment raised." Three of
   those four are near-universal. Investment raised is not.

One claim I could not reproduce and will not hold against the file: the 403. A
plain no-UA `curl` also gets HTTP 200 today. The 403 is specific to WebFetch's
user-agent, or was transient. The practical advice (use a browser UA) is right
either way.

**Net:** this is still the best source in the four MVP markets, and the reasons
given for that are all true. The scale needs restating.

---

## 2. The other named-figure claims

### MBH FinTechLab: PARTLY CONFIRMED, with a scraping trap the file missed

- Portfolio page: HTTP 200, 279,985 bytes.
- **Count: 26 active plus 6 exits = 32.** The file says "roughly 26 active plus 7
  exits ... treat the total as approximately 30 to 33". The active count is
  exact. The exits count is 6, not 7 (the file hedged with "and one other",
  which is the one it invented). Total lands inside its own stated range.
- **Pastpay, FintechX and Space Invoices are all present**, with descriptions
  matching the file exactly: "Digital factoring platform providing fast, flexible
  financing solutions for SMEs" (Pastpay), "Provides open banking and open
  finance solutions, including embedded finance apps" (FintechX), "Invoicing API
  for global SaaS and e-commerce companies" (Space Invoices). hypomo, Tokeportal,
  Limitless, Thinkout, GeoFintech, Amon and coinrule also all present. Exits
  Bookkeepie, Cloudent, complytron, compocity, ff.next and smapplab all present.
- **The trap.** Company names are **not in the page text**. Only Amon is named in
  prose. Every other name is recoverable solely from logo image filenames
  (`Pastpay-e1770758611288.png`, `FintechX-logo-...png`,
  `space-invoices-300x150-1-...jpg`). All `alt` attributes are empty. The file
  says "HTML cards with one-line descriptions" and "I read all active company
  names with descriptions", which overstates what the page hands you. This is the
  identical trap the same file correctly flagged for Hiventures. It should be
  flagged here too, because a naive scraper gets 32 descriptions and zero names.
- Homepage claims confirmed: "Hungary's first incubator", Fintech Factory
  programme (`/fintech-factory/` returns 200), 2026 copyright. The string "MKB"
  does **not** appear on the homepage, so "confirmed the MKB to MBH rebrand" is
  not supported by the page fetched.

### start it @ČSOB: CONFIRMED on every number, but one claim is REFUTED and the source is better than described

Everything the file asserts about scale and dates is exact, in Czech, on the
page:

- **"130 akcelerovaných / 750+ přihlášených startupů / 7 let fungování"**:
  confirmed verbatim.
- **17th cohort**: confirmed, *"Start it @ČSOB zahájil již 17. vlnu akcelerace"*.
- **Applications close 30 October 2026**: confirmed, *"Přihlaste se do 30.10.
  2026"*, on both the homepage and the list page.
- **12 companies in the current cohort**: confirmed, 12 cards. Spiroq (vending
  machine OS), Reechable (gastro digital loyalty cards), Rented (product
  sharing) and Monomo (demand, supply, logistics) all present and correctly
  characterised. The news item says the 17th wave launched with nine startups, so
  the 12 on the list page span more than one wave.

**REFUTED:** *"Confirmed there is no historical alumni archive: only the current
cohort is shown, which is why snapshotting matters."*

There is an archive, and it is trivially reachable. The list page carries a
`load-more-startupy` control (`data-page="2"`, `data-numposts="12"`). The theme
bundle at `/wp-content/themes/startit2025/js/app.js` routes it to an
unauthenticated JSON endpoint. One request:

```
POST https://startit.csob.cz/wp-json/api/startupy
page=1&numposts=500&section=%23startupy-all
```

returns `{"lastpage": true, "numposts": 132, "html": ...}`, that is **132
startups with descriptions and 130 outbound company URLs in a single call.**
That is the whole alumni corpus behind the "130 accelerated" headline, and it
matches the headline figure.

This is a correction that *upgrades* the entry: start it @ČSOB moves from
"snapshot the current 12 each cohort" to "one HTTP call for the full 132-company
Czech bank-accelerator corpus".

### mapadotacji.gov.pl: CONFIRMED, and stronger than claimed

The Poland workaround holds completely.

- Register is public, no login, HTTP 200.
- The programme filter exists. `search-number-name-activity` contains the option
  **`1.1. Platformy startowe dla nowych pomysłów`, value `28509`**.
- Running it (`https://mapadotacji.gov.pl/projects/?lang=en&search-number-name-activity=28509`)
  returns **"Found: 774 Projects"** in a results table with columns: project
  title, **Name of the beneficiary**, project value, EU co-financing,
  voivodeship, category.
- It yields real startup names, not just operator projects. Sampled beneficiaries
  include `4MAT SP. Z O.O.`, `MAGLY SP. Z O.O.`, `BUSBUS sp. z o.o.`,
  `WINOPASJA.PL SP Z O.O.` alongside the platform operators (Kielecki Park
  Technologiczny, Białystok Science and Technology Park, Lubelski Park
  Naukowo-Technologiczny).
- Voivodeship and county filters confirmed.

The PARP programme page is behind Incapsula and refuses `curl`; via WebFetch it
returns exactly the six operators the file names (Unicorn Hub Lublin, Wschodni
Akcelerator Biznesu Puławy, Start in Podkarpackie Rzeszów/Mielec, Idealist
Lublin, Startup Heroes Olsztyn/Ełk, Hub of Talents 2 Białystok/Łomża) and the
status "Nabór został zakończony". The page states a combined budget of 108.4M
PLN; the file's "30M PLN / 600,000 PLN per startup" figures are from a different
call page and should be sourced. "HugeTECH Revolution" is named in the file as an
operator but is not on the PARP list.

`wab.biz.pl` confirms the file to the day: *"Do 31.07.2026 r. Runda 8"* and
*"03 sierpnia 2026, Do 8 rundy wpłynęło 279 wniosků"*.

### Nápad roku: CONFIRMED, no material error

- Homepage, verbatim: **"18 ročníků"**, **"2652 projektů"**, **"476 milionů Kč"**.
- The URL pattern claim is right and the nav trap is real: `/soutez/<year>/`
  returns 200 for 2007, 2010, 2015, 2020, 2024, 2025 and 2026; `/vysledky-2025/`
  returns **404**, exactly as the file warns.
- Sitemap lists 19 year pages. **2008 has no page** (404), so the archive is
  2007 then 2009-2026, not "every year from 2007 to 2026". One-line fix.
- 2025 results page: *"Do 18. ročníku soutěže se celkem přihlásilo 127
  projektů"*, the file's 127 figure, exact. TROPIC01 (Jan Pleskač, "Kombinace
  software a hardware", "IoT/IoE & Sensors"), CircuitNinja and Lightly all
  present with founder name, project type and industry tag as described.

### InnovX-BCR: PARTLY CONFIRMED, the count is materially high

- Alumni page HTTP 200. Year filter: All / 2025 / 2024 / 2023 / 2022 / 2021 /
  2020 / 2019, exactly as described.
- Industry filter present and includes **FinTech**. The file says "40+ entry
  industry filter"; it is **34 industries** (36 options including the header and
  "All industries").
- All eight named fintechs present: MyMoney, SOLO, Coinscrap Finance, Lendox,
  Invoice Cash Group, Finqware, KidsFinance, Fagura.
- **Count is wrong. 287 alumni cards, not "roughly 400".** That is a ~39%
  overstatement and it matters, because 400 was used to rank this as a
  first-hit scrape target.
- Homepage metrics confirmed exactly: 487 innovators accelerated, 217 corporate
  partnerships, €108.3 million raised.
- Two upgrades the file missed: every card carries `data-year` and
  `data-industry` attributes, so per-company cohort year **is** in the DOM (the
  file says it is "only reachable by filtering"); and there are **15 cards tagged
  2026** that the year dropdown does not offer, so the filter UI lags the data.
  Year distribution: 2019:26, 2020:31, 2021:56, 2022:38, 2023:47, 2024:43,
  2025:31, 2026:15. FinTech: **17 companies**.

---

## 3. The death and absorption claims

**All five confirmed. None should be reinstated.** This is the strongest section
of the file.

| Claim | Verdict | Evidence |
|---|---|---|
| **Design Terminal** absorbed into Civitta | **CONFIRMED** | `designterminal.org` redirects to `civitta.com/hu`. Footer carries "Design Terminal Public Benefit Non-profit Ltd. VAT HU25717002". Successor programmes present and named: ESA BIC Hungary, **V4 Startup Force**, NAK TechLab, START programcsalád, Womenture, ESERO Hungary. **No alumni directory anywhere on the page.** The 210+ alumni corpus is genuinely gone. `v4startupforce.com` does not resolve, as claimed. |
| **ITACA** dead Tilda domain | **CONFIRMED** | `itaca.cz` returns **HTTP 404** with the Tilda body "Domain has been assigned. Please go to the site settings and put the domain name in the Domain tab." Certificate covers `*.tilda.ws` only. Vestbee is indeed citing a dead programme as one of two fintech-focused Czech incubators. |
| **mAccelerator** parked | **CONFIRMED** | `maccelerator.pl` HTTP 200, 9,358 bytes, cyberfolks.pl placeholder: *"Domena jest aktywna, ale strona nie została jeszcze uruchomiona"*, support address `wsparcie@cyberfolks.pl`. Verbatim match to the file. |
| **RBL_START** subdomain redirects to retail | **CONFIRMED** | `rbl.aliorbank.pl` resolves to `https://www.aliorbank.pl/` (246 KB retail homepage). `aliorbank.pl/dodatkowe-informacje/o-banku/rbl.html` returns **404**. The file's "Unverified (status)" grading is the correct grading: I also cannot prove it is dead, only that no programme page exists. |
| **Google Campus Warsaw** closed | **CONFIRMED** | `campus.co/warsaw/` redirects to `startup.google.com`. The campus-specific site is gone. |

Three further negative findings, checked and confirmed: `spherik.ro`,
`thespinoff.eu` and `v4startupforce.com` all fail DNS resolution exactly as
recorded. **BnL Start's TLS certificate expired on 6 August 2018**, eight years
ago, which is a stronger signal than the file's "has expired".

---

## 4. The Raiffeisen three-way conflict: SETTLED

**They are two separate vehicles. The client was told correctly. Confirm, do not
correct.**

| | Elevator **Lab** | Elevator **Ventures** |
|---|---|---|
| What it is | RBI ecosystem-outreach initiative | RBI corporate venture capital arm |
| Accelerator status | **Ended 2022** | n/a, still investing |
| Live URL | `rbinternational.com/.../elevator-lab.html` (200) | `www.elevator-ventures.com/en/portfolio.html` (200, 237 KB) |
| Publishes | 4 historical success stories, no current cohort | **22 portfolio companies**, static HTML, with Headquarters / Founded / Selected Co-Investors |
| Use to TXN | relationship only | scrapeable list |

Findings:

- **`sources/02` is correct and its quotation is genuine.** The RBI page contains
  the exact string *"Elevator Lab Partnership Program was organized as a
  structured startup accelerator and partnership program from 2017 until 2022."*
  I checked for it character by character. It is on the page. The brand survives
  as an outreach function with three pillars (Ecosystem, Partnerships, Insights)
  and names Moxo, Billon, Pisano and SESAMm as historical success stories, again
  as `02` records.
- **`sources/03` is correct.** `www.elevator-ventures.com/en/portfolio.html` is
  live and static. 22 companies with 19 `Selected Co-Investors` fields and 19
  `Founded` fields. Blockpit, QuoIntelligence, exnaton and Klim are all there as
  `03` samples them, plus **Finqware (Romania), Twisto (CEE BNPL), Tarfin,
  Autenti (Poland), Wultra, Trustfull, Tangany, Elucidate, FinCompare, vestr,
  kompany, Agro.Club, Cloudcart, Bob W, byrd, goUrban, Pisano, SESAMm**. `03`'s
  "237 KB" is exact.
- **`sources/01` is not wrong, it is stale, and it should be resolved.**
  `elevator-lab.com` and `www.elevator-lab.com` both still return **HTTP 503**
  from a fresh connection with a Chrome UA (62-byte body; the file said 30 bytes,
  which is the only discrepancy and is immaterial). The standalone domain is
  genuinely dead. But the answer was reachable at the RBI corporate URL that
  `02` used, and `01` did not try it.
- **Domain trap worth recording:** `elevatorventures.com` (no hyphen) is a
  **HugeDomains parking page**. The live CVC is `elevator-ventures.com`
  (hyphenated). `02` cites the unhyphenated form twice. Anyone following `02`'s
  URL lands on a domain squatter.

**Action:** replace `01`'s "COULD NOT VERIFY" entry with `02`'s finding
(accelerator ended 2022, brand persists as outreach, standalone domain dead) and
cross-reference `03` for the live CVC. Nothing about the two-vehicle framing
needs walking back to the client.

---

## 5. Fabrication signatures found

I looked specifically for the four tells: counts that do not match, programmes
that do not exist, URLs that 404, named companies absent from the lists they are
claimed to be on. **No programme in this file is invented.** Three real errors:

### 5.1 A `Verified` URL that returns 404: Google for Startups

The file records, under `Confidence: Verified`:

> **List page:** `https://www.google.com/for-startups/alumni/directory/`
> **Evidence:** Fetched the alumni directory page and confirmed the Region filter
> includes Poland, Romania, Hungary and Czechia...

**That URL returns HTTP 404.** Both with and without the trailing slash.

The described content is entirely real, at a different address:
`https://startup.google.com/alumni/directory/` (HTTP 200, 256 KB). I confirmed
there that the Region filter lists Czech Republic, Czechia, Hungary, Poland and
Romania under Europe, that the Industry filter includes Fintech, and that
"thousands" is the published figure.

So the finding stands and the URL does not. This is the only breach of
anti-fabrication rule 1 in the file, and it is a stale-URL breach rather than a
guessed one.

### 5.2 Two company names not on the lists they are attributed to

- **Payowallet (StartupYard).** The file's prose says "Named alumni include
  **BudgetBakers** (personal finance), **CityPay** and **Payowallet**". The
  homepage contains BudgetBakers, CityPay, TeskaLabs, Rossum, Gjirafa, Retino
  and DishBoard. It contains **no** "Payowallet" and exactly one instance of the
  string "wallet", inside a CityPay.io description. The "payments thread" framing
  is right; the third company is not there. Also not on the homepage: the "70+
  accelerated" and "EUR 30k per company" figures the entry cites.
- **Money24 (Innovation Labs 2026).** The file says "The 2026 cohort included
  **Money24**, a fintech-named team." The cited StartupCafe article (fetched,
  239 KB, published 26 May 2026) contains no "Money24" and no fintech or finance
  reference at all. The four named winners (**AICoustic, DistriOS, Intrudify,
  Nabu**) are exactly as the file records them, as are 221 projects, 41 teams
  into the 10-week programme and the EUR 500,000 Early Game Ventures prize. But
  the article names **4 winners, not the 41-team qualified list**, so the claim
  that the press "publishes the full qualified list every May" is not evidenced
  by the source cited for it.

### 5.3 Two list sizes materially inflated

- **InnovX alumni: 287, stated as "roughly 400".**
- **JIC clients: 295, stated as "roughly 400".** I counted
  `class="company-item"` = 295, and 294 unique outbound client URLs.

Both round in the same direction, which is worth naming as a pattern: where the
file estimated rather than counted, it estimated high. Rubik Hub ("several
hundred" for 249) is the third instance.

---

## 6. Corrections that make the source better

Three things I found that upgrade entries rather than damage them. These should
go into the file.

1. **start it @ČSOB has a public 132-company API.** See section 2. Single
   unauthenticated POST to `https://startit.csob.cz/wp-json/api/startupy`.
2. **JIC publishes a one-click Excel export of its entire client list.** The
   clients page carries
   `/Kentico.PageBuilder/Widgets/en-US/JIC.Content.Companies/GetClientsDownloads`,
   which returns a 33 KB `application/vnd.ms-excel` file, HTTP 200, no auth.
   Further, client names **are** in the HTML, as `data-title` legal-entity names
   on each `company-item` div: "Tatum Technology s.r.o.", "Reservio, s.r.o.",
   "smsticket s.r.o.", "Devmons s.r.o." (which is Crypkit: the file lists
   "Crypkit" as a visible client name, but the visible name is Devmons and the
   Crypkit brand appears only in the URL). JIC is therefore the most
   machine-readable Czech source in the stream, not a "Load more" logo grid.
3. **Startarium is readable.** The file records `startarium.com` as HTTP 403 to
   WebFetch and drops it as `Reported`. `curl` with a Chrome UA returns **HTTP
   200, 560 KB**, the same workaround the file applies to Rubik Hub but did not
   apply here. The substantive conclusion survives (nav is Începe / Administrează
   / Crește / Învață, an education and resource platform, no public business
   directory visible), but the entry can be upgraded from `Reported` and the
   "could not read the platform" note removed.

---

## 7. Per-entry verdicts

### Fully confirmed, no correction needed (23)

**Techcelerator** (NEXTFintech confirmed as one of 7 alumni categories; year
filter 2019-2024; 123 alumni cards vs "roughly 130"; Tukana/Infin8, Ocean Credit,
Credia, Prime Dash, Bankspot, 22Trust, Finpathic and Text'n Pay Me all present.
Note the filters are JetSmartFilters **checkboxes**, not dropdowns) ·
**Spherik** (Sector/Year/Country filters confirmed including FinTech; 22TRUST
VENTURE, bNesis and iFactor present with the quoted descriptions; **26**
companies, 7 KPMG plus 19 Spherik, not 27) · **Orange Fab** (36 named companies
and the 2017-2020 year tabs; PROCESIO, Nestor, FieldOS, Blugento, CityDock, Zevo,
EmailTree.AI, Rastel.io all present) · **accelerate.gov.ro** (the Innovation Labs
entity page carries Category, Main domain, Founded by, Team: structured as
described) · **RomanianStartups.com** (7 accelerators exactly as enumerated;
InnovX, Techcelerator and Rubik Hub all absent, confirming the staleness
finding) · **Nápad roku** (2008 nit only) · **xPORT** (ROIER, ContextMinds,
Scaleo, ShortPRO, Quanda, Sentiscrape, TALENTDOCk, SALESDOCk, Spectrasol,
Competentia present; the Apexari lorem ipsum is confirmed; sitemap `lastmod` for
`/tymy-v-xportu/` is 2026-07-01, and the 2026-08-25 the file quotes is the
sitemap maximum from another page) · **czechstartups.gov.cz** (15 editorial
profiles. Note **FTMO** is a second fintech alongside Twisto, so "only one
fintech" is slightly off) · **ITACA** · **Hiventures** (Státusz Exitált/Aktív and
Iparág filter incl. FinTech/InsureTech confirmed; 44 "Bővebben" links; names
genuinely absent from the list HTML, exactly as flagged) · **BnL Start** ·
**Startup Campus** (HFDA, HUMDA, TOKAJTECH, INNOGEN, GINOP, 1 January 2024
launch, no roster) · **Design Terminal** · **Huge Thing** ("Applications are due
by March 30, 2026" confirmed verbatim; Ramp Network, Pergamin, MY OVU,
Tripso.ai, RIFFSEC present) · **Let's Fintech PKO** (6000 companies analysed and
12 million customers verbatim; **exactly four** partner companies, vivaDrive,
Listny Cud, TerGO and Redigo Carbon, confirming "publishes almost nothing".
Caveat: the other partner names the entry lists, 1Strike, Bright Technology,
Settlemint, Agronet, XR Wizards, Travatar, WeGrant, are press-sourced and appear
nowhere on the fetched page, which the Evidence field should say) · **MIT EF
CEE** (Fintech & Insurtech filter, Tamago, 270+ all confirmed, but the HTTPS URL
does **not** 301 to HTTP, it serves 200 over HTTPS, so use
`https://mitefcee.org/community/alumni-club/our-alumni`) · **Kozminski** ("do 400
tysięcy złotych", Impact Booster, Venture Lab, Fabryka Startupów, Incaso Group
and Plenti all confirmed) · **Platformy startowe / mapadotacji** · **FinTech
Poland** (the 31.07.2026 news item and the "How to do FinTech in Poland" series
confirmed; "Supervision FinTech Talks" not found on the homepage) ·
**mAccelerator** · **RBL_START** · **Startup Wise Guys** · **ReaktorX**
(confirmed: $50K cash via SAFE, 5% equity, 1 month in San Francisco, 15 teams per
batch, Batch #11 and #12 Demo Days, and the six named portfolio companies) ·
**28DIGITAL** (EIT origin, Talent/Tech/Trust pillars, Co-Creation Accelerator
2026-2027 all confirmed; no cohort list on site, as recorded).

**Startup Wise Guys deserves a special note: it reproduces perfectly.** Status
counts Active **286** / Active-Partial exit **4** / Exit **23** (=313, as the
file computes). Headquarter location counts **Poland 8, Romania 3, Czech Republic
1, Hungary 1**, all four exact. Fintech batches 1 through 5 present. Verticals
Cyber & Data, Fintech, Proptech, SaaS, Sustainability, Web3, XR/AR/VR. "+450
startups" claimed on page. Ondato, Okredo, JetBeep and Partly all present. Zero
errors.

### Partly confirmed, correction required (9)

| Entry | Correction |
|---|---|
| Rubik Hub | URL should be `rubikhub.com`; 249 cards not "several hundred"; 7 FinTech not 8; investment raised on 69 of 249 |
| InnovX-BCR | 287 alumni not ~400; 34 industries not 40+; per-card year IS in the DOM; the dropdown misses 2026 |
| JIC | 295 clients not ~400; add the XLS export and the `data-title` names; "Crypkit" is listed as "Devmons s.r.o." |
| start it @ČSOB | Remove "no historical alumni archive"; add the 132-company API |
| MBH FinTechLab | 6 exits not 7; company names are **not** in page text, only in logo filenames; "MKB to MBH rebrand" is not on the homepage |
| StartupYard | Drop **Payowallet**; the 70+ and EUR 30k figures are not on the homepage |
| OXO Labs | 4 of the 15 names given (IconicChain, GreenDrops, RotowerAI, Valley Leaves) do not appear on the page; the other 11 do. The substantive finding (15 companies, no fintech) holds |
| Google for Startups | List page URL **404s**; replace with `https://startup.google.com/alumni/directory/` |
| Innovation Labs | Drop **Money24**; the cited StartupCafe article names 4 winners, not the 41-team list |

### Correctly graded as not-verified (3)

**Impact Hub / Startarium** (`Reported`, but `startarium.com` is now readable and
the entry can be upgraded) · **RBL_START** (`Unverified (status)`, correct, I
also could not prove it dead) · **Elevator Lab** (`Unverified`, now resolvable,
see section 4).

---

## 8. Must be corrected before this reaches the client

Ranked by how much damage each does if it ships as-is.

1. **Delete "start it @ČSOB has no historical alumni archive."** It is false and
   it downgrades a source that turns out to be the most extractable Czech
   programme in the stream. Replace with the 132-company API.
2. **Fix the Google for Startups list-page URL.** It 404s, and the file is being
   read as a scrape spec. Use `https://startup.google.com/alumni/directory/`.
3. **Correct the three inflated counts:** Rubik Hub 249, InnovX 287, JIC 295.
   All three are cited as first-hit scrape targets and all three are smaller than
   stated. The corpus-planning arithmetic downstream depends on them.
4. **Remove Payowallet and Money24.** Two company names attributed to lists they
   are not on. These are the only two claims in the file that would fail a
   client's own spot-check, and they are exactly the kind of thing Ian asked to
   be checked for.
5. **Resolve the Elevator Lab entry** against `sources/02` and cross-reference
   `sources/03`. Also fix `sources/02`'s `elevatorventures.com` to the hyphenated
   `elevator-ventures.com`; the unhyphenated domain is a HugeDomains parking page.
6. **Add the MBH FinTechLab name-extraction caveat.** Names live in logo
   filenames, not text. Without this, the scrape returns 32 anonymous
   descriptions.
7. **Change Rubik Hub's list URL to `rubikhub.com`** and note the cross-host
   redirect as the likely cause of the WebFetch failure.
8. Minor: Nápad roku has no 2008 page · MIT EF CEE serves HTTPS fine ·
   czechstartups has two fintechs (Twisto and FTMO) · PARP does not list HugeTECH
   Revolution · Techcelerator filters are checkboxes · Spherik is 26 not 27 ·
   upgrade Startarium from `Reported`.

## 9. Trustworthiness assessment

I went in assuming fabrication and did not find it. What I found instead is a
file written by something that fetched a lot of pages, recorded byte counts and
Czech and Polish source strings accurately, correctly identified five dead
programmes, correctly identified three separate URL traps (`spherik.ro`,
`/vysledky-2025/`, `pkobp.pl/fintech/...`), and was honest in its "What I could
NOT verify" section about a search budget it had exhausted.

Its failure mode is not invention. It is **estimating list sizes upward when it
did not count, and not re-testing a page after a first fetch failed**. Three
counts are 30-40% high. Two company names drifted in from model knowledge or
press rather than the page. One URL went stale between whenever it was learned
and this pass. And in three cases (Startarium, Elevator Lab, the ČSOB archive) it
stopped one step short of an answer that was available.

That is a normal-quality research artefact with fixable defects, not a
hallucination. **Recommend: correct the nine items in section 8, then ship.**
The Rubik Hub recommendation, the mapadotacji.gov.pl workaround for Poland, the
Startup Wise Guys country filter, the five death findings and the Raiffeisen
two-vehicle framing are all safe to put in front of the client today.

**Last checked: 2026-08-25**
