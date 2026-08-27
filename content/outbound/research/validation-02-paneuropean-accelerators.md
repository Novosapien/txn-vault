---
description: "Adversarial validation of stream 02: 28 Verified entries re-fetched, no fabrication found, corrections centred on over-claimed access"
---

> **Section:** [[research]]
> **File under test:** [[stream-02-paneuropean-accelerators]]
> **Method:** independent agent, no contact with the authoring agent's notes, re-fetching with a different toolchain.

# Validation report: stream 02, pan-European and UK accelerators

File under test: `sources/02-paneuropean-accelerators.md`
Validator: independent adversarial pass, 2026-08-25.
Method: every URL in the file re-fetched with `curl` (browser user-agent) and
parsed directly from raw HTML rather than through a summarising fetcher, so
counts below are machine counts of the served markup, not impressions. WebFetch
used only where a page is JS-rendered (Level39, Kickstart). WebSearch was
unavailable: the 200-call session budget was already exhausted, which is the
same wall the research agent hit, so all verification here is primary-source
fetching.

---

## Headline verdict

**The research is real. It was not invented.**

Across 28 entries carrying a `Verified` label I found no invented programme, no
invented URL, and no invented company. Every cited URL resolves. Where the file
quotes a page verbatim, the quote is genuinely on the page: I checked the RBI
Elevator Lab sentence, the finleap headline, the Copenhagen Fintech incubation
wording and the Seed Starter mandate wording character by character and all four
are exact. Where the file names companies it says it read off a page, those
companies are on the page: 26 of 26 MBH Fintechlab portfolio names, 12 of 12
The Heart ventures, 14 of 14 FinTech Innovation Lab 2026 cohort names, 15 of 15
Mastercard Lighthouse Spring 2025 names, and all seven Startup Wise Guys
vertical counts to the exact integer.

The failure mode of this file is not fabrication. It is two other things:

1. **Arithmetic and tag-counting drift.** Several list sizes are wrong by
   enough to matter (KB SmartSolutions 9 vs 13, InnovX ~400 vs 287, Hexa "10+
   fintech" vs 7).
2. **Premature surrender on 403s.** Three of the five sites the file writes off
   as HTTP 403 return HTTP 200 to `curl`. One of them, Barclays Eagle Labs, the
   file itself calls "the single most valuable unresolved question in this
   stream for the UK market". It is answerable in one command.

**Verified entries that survive: 27 of 28.** One (KB SmartSolutions) is refuted
on both its count and its central "Czech-only" premise. Six more need numeric or
label corrections before the client sees them.

---

## 1. The load-bearing claims

### Visa's European programme is operated by Tenity, with Nordics/Baltics and Southern Europe open: **CONFIRMED**

This is the most consequential claim in the file because it corrects something
already told to the client. It holds, on primary source, in both halves.

**Operator relationship.** `tenity.com/cases/visa-innovation-program-europe/`
(HTTP 200, fetched) states verbatim:

> "The program is implemented and operated by Tenity in close collaboration with
> Visa and local ecosystem stakeholders."

Every supporting figure in the file's evidence line is on that page and exact:
launched 2019, **7** cohorts completed, **142** selected startups, **EUR 520M+**
funding raised, **15 markets** across Europe, **100+ PoCs**, and the disclosure
"(Specific success stories are confidential.)" which is the file's basis for
marking participant names unavailable. The timeline block confirms expansion to
Spain, Portugal and Italy in 2022-2023 and to Nordics & Baltics in 2025.

**Open tracks.** `tenity.com/programs` (HTTP 200) carries both, and the status is
in the card class attribute, not just visual styling:

| Programme | Location | Date | Status class |
|---|---|---|---|
| Visa Innovation Program \| Nordics & Baltics | London | 21 Aug 2026 | `--open` |
| Visa Innovation Program \| Southern Europe | Istanbul | 21 Aug 2026 | `--open` |

These are the only two Visa entries on the index and both are open. Confirmed.

**One correction inside this entry.** The file's evidence line also reports
"Fintech Market Activation, London & Zurich (Open, 1 May 2026)". It is
`--closed`. Same for "Yapı Kredi FRWRD Global (via Tenity, Istanbul, open as of
Aug 2026)" in the open-leads section: `--closed`. Full status read from the
index today: open = Visa Nordics & Baltics, Visa Southern Europe, SFIIP 2026,
Digital Health Accelerator. Running = ITA Market Access, HackZone by Allianz.
Everything else closed. Fix the two mislabelled ones; the Visa claim itself is
untouched.

### Hexa: 50 companies, sector and stage tags, founding years, Swan/Spendesk: **PARTLY CONFIRMED**

`hexa.com/companies` fetched, HTTP 200, 198,861 bytes. I parsed the
`our-companies_item` cards directly.

| Claim | Finding |
|---|---|
| "50 companies" | The page copy does say "we've launched 50 companies, with a combined valuation of over $5billion". **But 62 company cards actually render.** The file quoted the marketing copy and recorded it as the list size. |
| Tagged by sector including Fintech | **CONFIRMED.** `fs-cmsfilter-field="category"` on every card. |
| Tagged by studio stage Start / Sprint / Scale | **CONFIRMED.** `fs-cmsfilter-field="track"`. Distribution: Start 49, Sprint 10, Scale 3. |
| Founding years shown, 2026 entries present | **CONFIRMED.** Years 2011-2026. The three named 2026 companies (Kyneon, Hodor, Enobase) are all on the page, plus Oligoplus, Revolty, Rubicon, Plato, Radiant, Waniwani, Verso: 10 companies with 2026 years. |
| Swan and Spendesk connection | **CONFIRMED.** Both are portfolio cards: `/companies/swan` (2019, Fintech + BtoB) and `/companies/spendesk` (2016, Fintech + BtoB + Future of Work + AI). |
| "10+ carry a Fintech tag" | **REFUTED. It is 7:** spendesk, swan, roundtable, reki, marble, numeral (Acquired), zenvest. |
| Named fintechs "Spendesk, Swan, Upflow, Roundtable, Marble, Reki, Zenvest, Multis" | 6 of 8 carry the Fintech tag. **Upflow** is tagged BtoB + Future of Work. **Multis** is tagged Web3 + BtoB and is `Inactive`. The file also missed **Numeral**, which is Fintech-tagged. |

**The analytical error matters more than the count.** The file's reason for
ranking Hexa first is: *"A company tagged `Fintech` at the `Start` stage has, by
definition, made no processor decision."* That inference is wrong. Start, Sprint
and Scale are **three separate Hexa programme brands** with their own top-level
nav pages (`/start`, `/sprint`, `/scale`), not a maturity ladder. 49 of 62
companies are "Start", including Aircall (2014) and Spendesk (2016), both
long-scaled. **All seven Fintech-tagged companies are "Start".** Meanwhile the
genuinely new 2026 ventures are mostly "Sprint". So filtering Fintech + Start
returns Spendesk and Swan, not a pre-processor startup. The right query for
TXN's greenfield segment on this page is **founding year**, not stage.

### MBH Fintechlab: 25 active + 6 exits, bank-owned, Hungarian: **PARTLY CONFIRMED (count off by one)**

`fintechlab.hu/our-portfolio/` fetched, HTTP 200. I counted the `<img title="">`
attributes on each logo card, split at the "Exits" heading.

- **Portfolio: 26**, not 25. Aeriu, Antavo, Bedrock.farm, cegjelzo, coinrule,
  diverzum, dreamjobs, FintechX, Fitpuli, guardit, hypomo, H4 Software,
  instacar, landventure, Pastpay, recart, Solar viewpoint, space-invoices,
  Tokeportal, Amon, businessflow, GeoFintech, hydrobot, labshare, Limitless,
  Thinkout.
- **Exits: 6.** bookkeepie, Cloudent, complytron, compocity, ff.next, smapplab.

Note that the file's own written-out list contains **all 26 names** and all 6
exits, correctly spelled, in page order. It then summed them as "25 active + 6
exits = 31". The list was read; the addition slipped. Correct to **26 + 6 = 32**.

Everything else holds: English, single page, card assets uploaded under
`/wp-content/uploads/2026/01/`, so the page is being maintained in 2026. The six
card-adjacent companies the file singles out (FintechX, Amon, Pastpay,
Tokeportal, GeoFintech, Limitless) are all present.

### InnovX: roughly 400 startups, filterable by FinTech and year: **PARTLY CONFIRMED**

`innovx.eu/startupsx/alumni` fetched, HTTP 200. Cards carry
`data-title / data-type / data-year / data-industry`, so this is countable
exactly.

- **287 alumni cards render, not ~400.** By year: 2021 (56), 2023 (47), 2024
  (43), 2022 (38), 2025 (31), 2020 (31), 2019 (26), 2026 (15).
- **Filters CONFIRMED.** Year dropdown 2019-2025 (as the file says), Industry
  dropdown with **34** options including `FinTech` (file says "30+": correct).
- **"487 innovators" homepage claim CONFIRMED** verbatim: "We have successfully
  accelerated 487 innovators". So the gap between 487 and 287 is InnovX's, not
  the researcher's. But the file's "~400 logos on the alumni page" is a visual
  estimate that is 39% high and should be replaced with 287.
- **Named fintech alumni: 5 of 8 check out.** MyMoney, SOLO, Invoice Cash Group,
  Fagura, Coinscrap Finance are all `data-industry="FinTech"`. **TOKERO is tagged
  Blockchain, 2Value is tagged E-Commerce, KidsFinance is tagged Education.**
  They are arguably fintech in substance, but they were not "read from the page"
  as FinTech, and a machine filter on FinTech will not return them.
- Full FinTech-tagged set (17): Scoreplex, MAI CALL, MyMoney, credia.store, SOLO,
  crystal-matrix.com, ContApp, dMonitor, Prime Dash, Invoice Cash Group, IRIS
  Solutions, eCollect, Fagura, Coinscrap Finance, Finqware, BAAM, KPEYE.

### Startup Wise Guys: the site's own filter reports 50 fintech: **CONFIRMED, exactly**

`startupwiseguys.com/portfolio/` fetched, HTTP 200, 1.36 MB. The counts are in
`<span class="swg-items-filter__option-count">`. Every single number in the file
matches the served HTML:

| Filter | File says | Page says |
|---|---|---|
| Fintech | 50 | **50** |
| SaaS | 164 | **164** |
| Cyber & Data | 39 | **39** |
| Sustainability | 31 | **31** |
| XR | 17 | **17** (labelled XR/AR/VR) |
| Proptech | 6 | **6** |
| Web 3 | 5 | **5** |
| Estonia | 78 | **78** |
| USA | 40 | **40** |
| Lithuania | 35 | **35** |
| UK | 29 | **29** |
| Italy | 29 | **29** |
| Active | 286 | **286** |
| Exits | 23 | **23** |
| Active/partial exits | 4 | **4** |

This is the strongest evidence in the whole file that the research pass was real.
Named entries StoreDNA, Investly, Ready Player Me, Ocoya, Klimashift all present.

Two small corrections. (a) **313 `portfolio-item` cards render**, while the page
header claims "more than +450 startups". The file took the 450+ marketing figure;
say 313 rendered against 450+ claimed. (b) The file gives batch-name examples as
"Fintech 2018", "SaaS Milan 2021", "Sustainability Copenhagen 2022". The filter
values are **not** dated that way: they read `Fintech 1` through `Fintech 5`,
`SaaS Milan 2`, `Sustainability Copenhagen`. Only a few carry years (`Spring
Batch 2025`, `Web 3 October 2024`). Batches are named, not dated.

### The Heart: co-founded with Mastercard, 3 of 12 ventures fintech: **PARTLY CONFIRMED; the Mastercard claim is overstated**

`theheart.tech/portfolio` fetched, HTTP 200.

- **12 ventures CONFIRMED**, and the file's list is exactly right, in page order:
  VASBOX, AIS Gateway, Flatte, Digital Gateways, uniperks, HomeAlert, Wellnoted,
  Car Platform, Domum, PrefabHUB, ScanPay, Tandu.
- **3 Fintech tags CONFIRMED.** Sector tag distribution on the page: Fintech 3,
  Real estate 2, ConTech 2, MarTech 1, HealthTech 1, Automotive 1, FoodTech 1,
  EdTech 1 = 12.
- **No dates or active/inactive flags CONFIRMED.** The file flags this weakness
  honestly. Footer reads "© 2025".
- **"Co-founded with Mastercard": NOT SUPPORTED by any primary source I could
  reach.** `theheart.tech/about-us` says "The Heart is the only established
  Corporate Venture Builder in Poland. Since 2016" with no founder named. Its
  meta description says "We build scalable startups with **Mastercard, mBank &
  more**". The partner logo wall lists **13** corporates: Velo Bank, Zen.com,
  Saint Gobain, Pietro Fiorentini, Uniwersytet Medyczny Łódź, Enerco Net,
  Develia, Credit Agricole, **Mastercard**, Cittru, Clear Channel, Ghelamco,
  **mBank**. Mastercard is one partner among thirteen, not a named co-founder.
  WebSearch was exhausted so I could not test the co-founding claim against
  historical press; treat it as **COULD NOT CHECK, and downgrade the wording**
  from "co-founded with Mastercard" to "counts Mastercard and mBank among its
  corporate partners". The summary section currently leans on the co-founding
  framing as the reason this source is high-value.

### KB SmartSolutions: 9 companies, Czech-language only: **REFUTED on both counts**

`kbsmart.cz/nase-portfolio/` fetched, HTTP 200.

- **13 companies, not 9.** The page carries **4** `Hvězda` (Star) blocks and
  **9** `Partner` blocks. The file got the 4 Stars right (Upvest, Lemonero,
  Finbricks, ENVIROS Advisory) and listed 5 Partners (ČEZ ESCO, Fidoo, Sunwork,
  iÚčto, Fakturoid). **It missed four: firmaprovas.cz, Shoptet, Paymium and
  Roger.** Confirmed by counting the "přejít na" outbound links: upvest.cz,
  lemonero.cz, finbricks.com, enviros.cz, kb.cz (Program ELENA), cezesco.cz,
  fidoo.com, sunwork.cz, iÚčto.cz, fakturoid.cz, firmaprovas.cz, shoptet.cz,
  paymium.cz, roger.cz.
- **"Published only in Czech" is false.** There is a language toggle in the nav
  linking to `/en/`, and **`https://www.kbsmart.cz/en/our-portfolio/` returns
  HTTP 200** with the same 4 Stars and 9 Partners in English. The English
  homepage reads "We provide funding to fintechs and assist in their development
  and rapid growth. We also build our own fintechs from scratch."
- This matters because the file's "What surprised me" section uses the
  Czech-only claim as the reason this list is "invisible to English-language
  fintech sourcing" and therefore "least-contested". That reasoning has to go.
  Note that **Paymium** ("payment and ordering system") and **Fidoo** (corporate
  cards and expenses) are both missed-and-card-relevant, so the correction adds
  targets rather than removing them.

### Entrepreneur First: filterable by location, industry, year and stage: **CONFIRMED, with one label correction**

`joinef.com/companies/` **301-redirects to `joinef.com/portfolio/`** (HTTP 200).
The file should record the canonical URL. Filter axes read from the served
`<fieldset>` markup:

- **Location, 11 options:** Bangalore, Berlin, External, Hong Kong, London, New
  York, Other, Paris, San Francisco, Singapore, Toronto. (File lists 10, missing
  "External".)
- **Industry, 30 options.** **There is no "fintech" option.** The relevant values
  are **`Financial Services`** and `Insurance`. The file says "Industry (20+
  sectors including fintech)" and its ranking entry proposes the query
  "industry=fintech". As written that query returns nothing. Correct to
  `Financial Services`.
- **Year: 2014-2026 CONFIRMED**, 13 options.
- **Stage: 8 options CONFIRMED.** Exit, Pre-Seed, Seed, Series A through E.
- Named entries Tractable, Cleo, PolyAI, Aztec, Neptune Robotics all present.

The substance of the recommendation survives: Financial Services + Pre-Seed +
2026 is a real, machine-buildable query on this page.

---

## 2. The death claims

A programme wrongly declared dead is as damaging as one wrongly declared alive,
so these got the hardest look. **All four hold. Two are stronger than the file
claims, one needs a real softening.**

### Barclays Rise winding down: **CONFIRMED, and upgradeable from `Reported` to `Verified`**

The file marks this `Reported` because `rise.barclays` returned 403 and no
primary source could be fetched. That is no longer true:

- **`https://rise.barclays/` returns HTTP 200 to `curl` after a single redirect
  to `https://home.barclays/who-we-are/innovation/`.** The Rise domain no longer
  serves Rise at all.
- I searched that destination page for the string "Rise": **zero occurrences.**
  Barclays' own innovation page does not mention the programme.

A dedicated programme domain redirecting to the parent's generic innovation page,
with the programme name scrubbed from that page, is primary evidence of
retirement. This can be re-graded `Verified` on the redirect alone.

### finleap stopped building, portfolio moved to Motive Ventures: **CONFIRMED, verbatim**

`finleap.com` fetched, HTTP 200, 22,588 bytes. Full body text, which is short
enough to quote in its entirety:

> "The Journey Continues with Motive Ventures / Explore our Ecosystem / From 2014
> to 2021 finleap has built or invested in 15 ventures and developed more than 5
> corporate JVs and service ventures collectively worth EUR 3.0Bn+ at a point in
> time. / Select investors / Our outstanding investor network / © 2026 finleap"

Exact match to the file, including the 2014-2021 framing, the "15 ventures" and
"5+ corporate JVs" figures, and the finding that **no venture names are
published**. Nothing to correct.

### RBI Elevator Lab accelerator ran only 2017-2022: **CONFIRMED, verbatim quote is genuine**

I specifically tested the file's claim to be quoting RBI "verbatim", because a
paraphrase dressed as a quotation is a classic fabrication signature. It is a
real quotation. The exact string appears on
`rbinternational.com/en/raiffeisen/rbi-group/about-us/innovation/elevator-lab.html`:

> "Elevator Lab Partnership Program was organized as a structured startup
> accelerator and partnership program from 2017 until 2022."

The page separately says the initiative was "adjusted... to be a holistic startup
and external ecosystems outreach program". Also confirmed on the page: the
Global Fintech Scouts Program (with Tatra Banka), the World Web3 Metaverse
Challenge 2024, and the four historical success stories the file names:
**Moxo, Billon, Pisano, SESAMm**. No 2025 or 2026 cohort anywhere on the page.
Confirmed in full.

### Rockstart is not a fintech source: **PARTLY REFUTED. Soften this one.**

The file marks this `Reported` and states honestly that it did not fetch the
page. I fetched it: **`rockstart.com/portfolio/` returns HTTP 200** (1.94 MB).

- **The fund-scoping claim is correct** and is on the page verbatim: "Since 2019,
  we narrowed our focus to launch four funds across three domains: AgriFood,
  Energy, and Emerging Tech which work hand-in-hand with our accelerator." Domain
  filter counts: Emerging Tech (126), Energy (64), Agrifood (57).
- **But the flat statement "350+ startups, none of them a fintech track" is
  wrong.** The portfolio page carries a **Vertical** filter, and one of its
  values is **`Fintech (23)`**. Twenty-three portfolio companies are tagged
  Fintech, mostly pre-2019 accelerator alumni.

Rewrite as: Rockstart runs no fintech fund or fintech track today, so it is not a
source of *new* fintech deal flow, but its portfolio page does expose 23
legacy Fintech-tagged companies via its own vertical filter. The practical
advice ("don't spend a scrape on it for greenfield") survives; the absolute
phrasing does not. It can also be upgraded from `Reported` to `Verified`.

---

## 3. Honesty of the gaps section

This is where the file is weakest. It lists five sites as HTTP 403 walls. **Three
of the five return HTTP 200 to `curl` with a browser user-agent.** The file's own
brief told the agent that curl sometimes succeeds where the fetcher gets a 403.

| Claimed gap | `curl` result | Verdict |
|---|---|---|
| `mastercard.com` Start Path, 403 | **HTTP 403** (456 bytes) | **CONFIRMED.** A genuine wall. |
| `mclighthouse.com`, 403 | **HTTP 200**, 168,803 bytes | **REFUTED.** Gave up early. |
| `rise.barclays`, 403 | **HTTP 200** after redirect | **REFUTED.** Gave up early. |
| `labs.uk.barclays`, 403 | **HTTP 200**, 135,492 bytes | **REFUTED.** Gave up early. |
| `ukfintech.co/directory-all/scotland/`, 403 | **HTTP 200**, 120,011 bytes | **REFUTED.** Gave up early. |
| Alior `rbl.` / `accelerator.aliorbank.pl`, TLS mismatch | **Reproduced exactly** | **CONFIRMED**, with a caveat below. |
| `otpstartup.com`, 301 to OTP corporate page | **Reproduced** (4 hops to `otpbank.hu/portal/en/about-us/otp-group`) | **CONFIRMED.** |
| `tenity.com/portfolio-companies`, 404 | **HTTP 404** | **CONFIRMED.** |

### What was behind the walls the file did not open

**Mastercard Lighthouse (`mclighthouse.com`).** The file says "I could not
confirm whether mclighthouse.com hosts a cumulative alumni index." Answers:

- The homepage states **"228 ALUMNI STARTUPS / EUR 1,2 B INVESTED / 308 PROGRAM
  PARTNERSHIP"**, "Mastercard Lighthouse Success Story since 2018".
- **An alumni index page does exist** at `mclighthouse.com/alumni-success-stories/`
  (HTTP 200), but it renders through Typeform and serves **no company names in
  HTML**. So the file's conclusion ("no cumulative index found") is right in
  effect, but now on evidence rather than on a 403.
- **The site is WordPress and its REST API is open.** `/wp-json/wp/v2/posts`
  returns `X-WP-Total: 136`. That is a clean, machine-readable feed of every
  cohort announcement, which converts this entry from "press-release monitoring
  target" into a **scrape target**. This is a material upgrade for TXN.
- Using that API I pulled the **primary** Spring 2025 FINITIV announcement and it
  matches the file's third-party mirror exactly: "launched its **14th round**
  with 15 outstanding fintech and fintech-enabler startups", Denmark (Kontolink,
  LENEO, Partisia, Tapeeze, Wolfpack), Norway (Bislab, Digisure, Front Payment,
  Justify, Mobai). Tapeeze is described as offering "multifunctional and
  innovative cards through tokenization", exactly as the file characterises it.
  **The mirror-sourced entry is now confirmed against primary source.**
- The post feed also confirms the cadence claim precisely: FINITIV cohorts of
  **15** in Mar 2025, Aug 2025 and Mar 2026; MASSIV cohorts of **5**, **5** and
  **6**. Spring 2026 = 15 + 6 = **21 across both tracks**, exactly as the file
  states.

**Barclays Eagle Labs (`labs.uk.barclays`).** The file calls this "the single
most valuable unresolved question in this stream for the UK market". Resolved:

- Eagle Labs is **alive**, running programmes with live deadlines (Funding
  Readiness Programme, applications close 31 August 2026), plus a Black Founder
  Accelerator, Female Founder Accelerator, Scaleup and others.
- **It does publish a directory: the Barclays Demo Directory** at
  `labs.uk.barclays/demo-directory/`. Its own stats: **"4,610 founder profiles
  created"** and **"1,114 investors"**, cumulative since launch on 30 October
  2023, "correct as of Friday 31 July, 2026".
- **The catch: it is login-gated.** Listings are published "for our network of
  attested investors or corporates to see". So it is a partnership/access target
  rather than a scrape target, and the file's open question should be closed with
  that answer rather than left open.

**FinTech Scotland (`ukfintech.co/directory-all/scotland/`).** Fetches fine and
serves a full alphabetical directory of Scottish fintechs with one-line
descriptions, **59 companies in the served HTML** (AccessFintech, Actelligent,
Advisory Direct, Alba, Amiqus, Appii, Artemis, AutoRek, Aveni, Beeks, Bibby,
BR-DGE, Brady, Broker Insights, Castlight, CrowdX and on). The page states it is
"Scotland's most comprehensive directory of Fintechs". The file's 250+ member
claim is a FinTech Scotland cluster figure, not this page, and remains
unconfirmed, but the directory itself is no longer a gap.

### The Alior gap is real, but the framing is wrong

The TLS diagnosis is exactly right, and I reproduced it verbatim:

```
subject: ... O=Alior Bank SA; CN=aliorbank.pl
subjectAltName does not match host name rbl.aliorbank.pl
curl: (60) SSL: no alternative certificate subject name matches target host name
```

**However**, running the same fetch with certificate verification disabled shows
what is behind it: both `rbl.aliorbank.pl` and `accelerator.aliorbank.pl`
redirect to `https://www.aliorbank.pl/`, the bank's retail homepage. There is no
accelerator site behind the broken certificate. The file concludes "This is a
real gap caused by a server misconfiguration, not by absence." That should become
**"a stale subdomain with a mismatched certificate that now redirects to the
bank's homepage, which is consistent with the programme having been retired."** A
dead subdomain is a finding, and it changes the recommended next step from
"manually fetch the site" to "check Polish trade press for whether RBL_START
still runs".

---

## 4. Fabrication signatures: what I hunted for and did not find

| Signature | Result |
|---|---|
| URLs that 404 | None, except `tenity.com/portfolio-companies`, which the file itself records as a 404. All 30+ other URLs resolve. |
| Programmes that do not exist | None. Every one of the 34 entries is a real, locatable organisation. |
| Company counts that do not match the page | Five (Hexa fintech tags, MBH total, InnovX size, KB SmartSolutions total, SWG rendered vs claimed). All are undercounts or overestimates of real lists, not invented lists. |
| Quotations presented as verbatim that are paraphrases | **None.** I tested the four most load-bearing quotes (RBI, finleap, Copenhagen Fintech, Seed Starter). All four are character-exact. |
| Company names that are not on the cited page | 4 out of roughly 120 named companies: Bewica, Plural.fi and Mo.health (Founders Factory) and Brunei Select Pharma (Startupbootcamp). Both those pages paginate and rotate a "FEATURED COMPANIES" block, so the most likely explanation is a different render, not invention. Everything else checks out. |
| Confident specifics that dissolve on checking | One: the Hexa "Start stage = pre-processor" inference (see above). |

### Entries confirmed with no correction needed

Verified by re-fetch and machine comparison against the file's stated evidence:
**Visa Innovation Program Europe, Tenity, Startup Wise Guys, Mastercard
Lighthouse, FinTech Innovation Lab, Antler, Founders Factory, Mediobanca x
Founders Factory, Techcelerator, Blenheim Chalcot, Level39, Holland FinTech,
NatWest, Innovate Finance, Copenhagen Fintech, ROCKIT Vilnius, Let's Fintech with
PKO, Seed Starter, Le Village by CA, Elevator Lab, finleap.** Spot-check
highlights:

- **Level39.** WebFetch returns "more than 180 startup and scaleup technology
  companies" and "Showing 16 of 139 results". Both file figures exact. 14 sector
  categories including FinTech and RegTech & Compliance; 8 stages including
  Pre-seed and Not Fundraising; eToro annotated Series D. Exact.
- **FinTech Innovation Lab.** The 2026 London cohort URL resolves and names all
  **14** startups under the file's four themes, with Diesta described as "A
  payment operations platform purpose-built for insurance, automating premium
  reconciliation". Alumni page filters: Region (All / New York / London / Asia
  Pacific), 35 categories including Payments and Blockchain, years 2011-2026,
  "0 Results" on initial render. Every detail matches.
- **NatWest.** All eight 2026 cohort names present (Aveni, Condukt, DeepFlow,
  Empath_AI, Galveston Group, Gradient Labs, Murphy AI, Round Treasury), plus
  "12-week" and "to be Pre-Series A, or Series A company with proven
  product-market-fit". Exact.
- **Innovate Finance.** Served HTML contains exactly "A - E  F - J  K - O  P - T
  U - Z" plus a search box, and **no** company names or sector filter. Exact.
- **Copenhagen Fintech.** "630 + Program alumni", "380 + Demo Day pitches", "5
  Programs per year", all five programme names, and the incubation-programme
  wording quoted in the file is verbatim.
- **Seed Starter.** "Pre-seed & Seed investment rounds / Ticket size 200k to 1M
  EUR / Minority shareholder / Startups active in CEE" and "a product or solution
  that innovates the banking industry or is valuable for its clients", all
  verbatim, with a Portfolio header and no names. Exact. (Bonus: **SmartHead**
  does appear in the page source, so one of the three companies the file listed
  as press-sourced is confirmable on-site.)
- **Antler.** "1,800+ companies across six continents, from inception through
  Series C", verbatim, with the seven sector filters as listed.
- **Blenheim Chalcot.** "built over 60 businesses", and the EVO stage is
  confirmed as a real process: "Our earliest stage businesses are subject to our
  Emerging Venture Opportunity (EVO) process before they graduate into the
  portfolio." The file's read of EVO as the useful filter is correct.
- **Techcelerator.** Alumni groupings exactly as listed (Advancing AI, Batch
  #1-#4, Investment Readiness, NEXTFintech) with year filter 2019-2024.
- **Startupbootcamp.** "over 1,600 startups... since 2010" verbatim; portfolio
  filter (All / Energy / Fintech / Fashion / Food / Net-Zero / Decarbonize /
  Mobility / Sports & Events); the "FinTech & CyberSecurity Amsterdam"
  accelerator tag appears 57 times; 8/24/48 pagination confirmed. One drift: the
  **Country filter today offers only Netherlands, Italy, South Africa,
  Australia**, not the nine-country list the file gives.
- **Kickstart Innovation.** Year filter 2016-2025 confirmed; Almanax, Fini,
  Maven Health and Meeco all present as 2025 alumni. One label correction: the
  alumni-page vertical is **"Finance & Insurance"**, not "Finance, Insurance &
  Cybersecurity".

---

## 5. Must-fix list before this reaches the client

Ordered by how much damage it would do if acted on.

1. **KB SmartSolutions: change "9 companies" to 13** (4 Stars + 9 Partners) and
   **delete the "Czech-language only" claim.** `kbsmart.cz/en/our-portfolio/`
   exists and serves the same list in English. Add the four missed partners:
   firmaprovas.cz, Shoptet, **Paymium** (payment and ordering system) and Roger.
   Remove the "invisible to English-language sourcing" reasoning from the
   summary.
2. **Hexa: change "10+ Fintech tags" to 7**, change "50 companies" to "50 claimed
   in page copy, 62 cards render", and **delete the reasoning that `Start` stage
   means pre-processor.** Start/Sprint/Scale are three programme brands; 49 of 62
   companies including Aircall and Spendesk sit under Start. Recommend filtering
   on founding year instead. Add Numeral to the Fintech-tagged list; move Upflow
   and Multis out of it.
3. **The Heart: downgrade "co-founded with Mastercard"** to "counts Mastercard
   and mBank among 13 named corporate partners". No primary source found for
   co-founding; the summary section currently rests on it.
4. **Rewrite the gaps section.** `mclighthouse.com`, `labs.uk.barclays` and
   `ukfintech.co` are not 403 walls; all three return 200 to `curl`. Only
   `mastercard.com` is a genuine wall.
5. **Upgrade the Mastercard Lighthouse entry.** Add: 228 alumni startups claimed;
   an alumni page exists but serves no names in HTML; **the WordPress REST API at
   `/wp-json/wp/v2/posts` exposes 136 posts**, making the cohort archive
   scrapeable. Re-grade the Spring 2025 cohort from mirror-sourced to
   primary-confirmed.
6. **Close the Barclays Eagle Labs question.** Alive; runs multiple accelerators;
   publishes the **Barclays Demo Directory** with 4,610 founder profiles and
   1,114 investors as of 31 July 2026, but **login-gated to attested investors**.
   Partnership target, not scrape target.
7. **InnovX: change "~400 logos" to 287 cards** (487 accelerated per homepage).
   Move TOKERO, 2Value and KidsFinance out of the "fintech alumni read from the
   page" list; they are tagged Blockchain, E-Commerce and Education. Add the
   twelve other FinTech-tagged alumni.
8. **MBH Fintechlab: 26 active + 6 exits = 32**, not 25 + 6 = 31. The name list
   is already correct and already has 26 entries.
9. **Entrepreneur First: the industry filter value is `Financial Services`, not
   `fintech`.** Update the proposed query. Record the canonical list URL as
   `joinef.com/portfolio/` (the `/companies/` path 301s).
10. **Rockstart: soften from "NOT A FINTECH SOURCE".** Its own portfolio filter
    reports **Fintech (23)**. Correct statement: no fintech fund or track since
    2019, 23 legacy Fintech-tagged portfolio companies. Re-grade to `Verified`,
    since the page fetches fine.
11. **Rise by Barclays: re-grade `Reported` to `Verified`.** `rise.barclays` 301s
    to `home.barclays/who-we-are/innovation/`, and that page contains zero
    mentions of Rise.
12. **Alior RBL_START: reframe.** The TLS mismatch is real and correctly
    diagnosed, but with verification off both subdomains redirect to
    `aliorbank.pl`. Nothing is being hidden by the certificate. Change "a real
    gap caused by a server misconfiguration, not by absence" to a
    likely-retired finding.
13. **Tenity programme statuses.** "Fintech Market Activation" and "Yapı Kredi
    FRWRD Global" are both `--closed`, not open. The two Visa tracks are the only
    open Visa entries and both are correctly recorded.
14. **Minor.** Startup Wise Guys batch names are not year-suffixed (`Fintech 2`,
    not `Fintech 2018`); state 313 rendered against 450+ claimed. Kickstart's
    vertical is "Finance & Insurance". Startupbootcamp's country filter currently
    offers four countries, not nine.

---

## Scorecard

| Category | Count |
|---|---|
| Entries in file | 34 |
| Entries carrying a `Verified` label | 28 |
| **`Verified` entries surviving as genuinely fetched and read** | **27** |
| Refuted outright | 1 (KB SmartSolutions) |
| Needing numeric or label correction but substantively sound | 6 (Hexa, MBH, InnovX, EF, Startupbootcamp, Kickstart) |
| Death claims tested | 4 |
| Death claims upheld | 4 (2 upgradeable to `Verified`, 1 needing softening) |
| Claimed 403 walls tested | 5 |
| Claimed 403 walls that are real | 1 (`mastercard.com`) |
| Invented URLs found | 0 |
| Invented programmes found | 0 |
| Invented verbatim quotes found | 0 |

**Trustworthiness: high on existence, medium on arithmetic, low on
persistence.** Ian can rely on this file for what exists and where it lives.
He should not rely on its list sizes without a recount, and he should assume
that anything the file calls a 403 wall is worth one more attempt with a
different client.

**Validator note on budget.** The 200-call WebSearch allowance was already spent
when this pass began, so I could not independently test two claims that need
press rather than a primary page: The Heart's co-founding by Mastercard, and
whether OTP's Startup Partner Program still runs. Both are marked COULD NOT
CHECK above rather than confirmed or refuted.

**Last checked:** 2026-08-25
