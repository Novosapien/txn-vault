---
description: "Adversarial validation of stream 03: all 54 entries re-tested, the eight investment-date funds confirmed, eight corrections required"
---

> **Section:** [[research]]
> **File under test:** [[stream-03-investor-portfolios]]
> **Method:** independent agent, no contact with the authoring agent's notes, re-fetching with a different toolchain.

# Validation report: Stream 03, investor portfolio pages

Independent adversarial verification of `sources/03-investor-portfolios.md`.
Validation date: 2026-08-25. Validator: independent agent, no contact with the
authoring agent's working notes.

## Method

Every claim below was re-tested from scratch. Primary tool was `curl` with a
normal Chrome user agent, plus a local HTML-to-text extractor (strip `<script>`
and `<style>`, strip tags, unescape entities, collapse whitespace) so that byte
counts and character counts are directly comparable to the ones in the source
file. WebFetch was used where the source file claimed a WebFetch result, so that
the curl-vs-WebFetch discrepancy could itself be tested.

**All 54 entries in the file were checked.** Not a sample.

Note on tolerances: the source file quotes extracted-character counts. These are
live pages, so a 0.5-2% drift between the research pass and this validation pass
is expected and is treated as a match. A drift of that size in *both* directions
across dozens of independent pages is itself evidence the numbers were measured
rather than generated. Byte counts on static assets matched far more tightly.

---

## 1. The date-field claim (the most consequential claim in the file)

The file asserts eight funds expose a per-company investment date or year in
served HTML: Motive Partners, Seedcamp, Market One Capital, Inovo, Movens,
Hiventures, OTB, Underline Ventures. The brief asked for at least five verified.

**All eight verified. CONFIRMED.**

| Fund | Claimed bytes | Measured bytes | Date field found in served HTML |
|---|---|---|---|
| Motive Partners | 358 KB | 357,518 | `Investment date August 2022`, `Investment date February 2026` |
| Seedcamp | 449 KB | 449,513 | `Year of Investment` column header, literal |
| Market One Capital | 225 KB | 224,813 | `Year` column plus `Year of investment` filter 2026 to 2018 |
| Underline Ventures | 793 KB | 793,354 | `Date of partnership: August 24, 2026` |
| Inovo VC | not stated | 424,604 | year per row: `Handwave ... Fintech Latvia 2025` |
| Movens Capital | 249 KB | 249,575 | `Entry date: Q3 2020` per company |
| Hiventures | 59 KB | 59,287 | `February 17, 2026` per entry |
| OTB Ventures | 287 KB | 286,637 | `Invested: 2026` per company (34 instances) |

Verbatim extracts confirming the field, not just its presence:

- **Motive.** `Accordion Subsector Business services Strategy Growth & Buyout Location New York City, NY, United States Investment date August 2022 Accordion Not realized`. The file's sample rows for Accordion, Alchelyst (February 2026), Anchorage Digital (November 2021) and AMP (May 2023, Realized) are all exact. `Banking & payments` subsector confirmed present (Aufinity Group, Avaloq, Backbase).
- **Seedcamp.** Column headers read literally: `Company Name Year of Investment Description Link to Waniwani's website`. Filter list `All AI Climate Consumer Crypto Developer Tools Enterprise Fintech Health/Bio Marketplaces Security` is an exact match to the file.
- **Market One Capital.** Headers `Company Description HQ/Country Year Sector Co-Founders Status`. HQ country filter vocabulary matched the file's list verbatim, in order.
- **Movens.** `Sector Healthtech Voice AI Entry date: Q3 2020 Links: Talkie.ai`, an exact match to the file's sample.
- **OTB.** `Alta Ares ... Founded: 2024 Invested: 2026 Current stage: Series A`, an exact match.

**Verdict: CONFIRMED.** The date field is real on all eight. The new-deal feed the
file proposes is buildable. This is the claim the build decision rests on and it
holds.

---

## 2. Underline Ventures, company dated 24 August 2026

Fetched `https://underline.vc/portfolio`, 793,354 bytes, 23,183 characters of
extracted text (file claimed 793 KB / 23,243).

Verbatim from the served markup:

> `... Country: Ukraine, UK Sector: Embedded Software Date of partnership: August 24, 2026`

The company is **Embedd** ("developer tools ... helping semiconductor companies
make their hardware easier and faster for developers to build on"). Second-newest
is Uvionix, `Country: Bulgaria, US Sector: Retail and logistics Date of
partnership: February 10, 2025`, again an exact match to the file.

`Date of partnership` occurs 60 times, which at the file's stated 3x hover-state
repetition is exactly 20 companies, matching the file's "~20 companies".

**Verdict: CONFIRMED.** Including the triple-repetition parsing warning.

---

## 3. Seedcamp: 550+ companies with year of investment, including 2026 rows

Served text contains `550 + 550 + Portfolio companies` alongside `$100bn+
Portfolio enterprise value`, `12 $1bn+ companies`, `30+ $100m+ companies`.

Six 2026-vintage rows served: Waniwani (`2026 Revenue infrastructure for AI`),
Eversettled, Resolyst, Opereit, Lupin & Holmes, sherpa. The file cited Waniwani
and Eversettled by name with Waniwani's description verbatim. Both correct.

Profile-card date format also confirmed: `Revolut Our Companies 29.07.2024`. The
file cited `29.07.2024` as its example.

**Verdict: CONFIRMED.**

---

## 4. The empty-shell claim (drives the headless-browser spend)

| Target | Claimed | Measured | Result |
|---|---|---|---|
| Presto Ventures `/portfolio` | exactly 114 bytes | **114 bytes** | CONFIRMED |
| Cogito Capital `/portfolio` | exactly 114 bytes | **114 bytes** | CONFIRMED |
| Middlegame `/portfolio` | exactly 114 bytes | **114 bytes** | CONFIRMED |
| LAUNCHub `/portfolio` | 4,551-byte shell | 4,555 bytes | CONFIRMED |
| SMOK `/portfolio/` | Vue placeholders, 1,219 chars | 1,219 chars | CONFIRMED |
| Enterprise Investors | 346 chars | **346 chars** | CONFIRMED |
| MCI Capital | 385 chars | **385 chars** | CONFIRMED |
| Lead Ventures | 1,118 chars, zero companies | 1,079 chars, zero companies | CONFIRMED |
| Antler | byte-identical with/without `?location=` | **byte-identical, 254,245 both** | CONFIRMED |

The 114-byte body, identical on all three domains:

```
<!DOCTYPE html><html><head><script>window.onload=function(){window.location.href="/lander"}</script></head></html>
```

SMOK's served markup contains, verbatim, `{{item.title}}`, `#{{tag.name}}`,
`v-for="item in portfolio"` and `v-for="tag in item.tags"`. The Vue template ships
unevaluated, exactly as described.

Lead Ventures' full served text is nav, cookie banner, one boilerplate paragraph,
a Budapest address and a copyright line. Zero company names. Confirmed by reading
the entire 1,079 characters.

**Verdict: CONFIRMED.** The headless-browser tier is justified. No false positive
here. Note the byte counts on Presto, Cogito and Middlegame are identical because
all three are the same hosting platform's redirect stub, which is why the "exactly
114 bytes" coincidence is real rather than a copy-paste artefact.

---

## 5. Credo Ventures: WebFetch says empty, curl returns 2.3 MB

Both halves independently reproduced.

- `curl` returned **2,339,011 bytes** (file said 2.34 MB) yielding **2,426
  characters** of extracted text (file said 2,426 characters, exact).
- The served text contains `(Pre-seeds) 84 84 84 84 Selection Since 2009` and
  company names inline with status badges: Bugprove, Goodlegal, Assetario,
  Talkbase, Munch.so, Stock Story, Manta, Waymark, SignAll, GoAvio, Represent,
  Apiary, DataFeedWatch, Klick2Contact, Cognitive Security, Brainient. Every name
  the file listed is present.
- **WebFetch on the same URL returned, verbatim: "NO COMPANY NAMES FOUND ... the
  actual company names are not included in this content excerpt."**

**Verdict: CONFIRMED**, and this is the most operationally valuable finding in the
file. It is a reproducible tooling defect, not a one-off.

One correction below in section 11 on how many names Credo actually yields.

---

## 6. Elevator Ventures vs Elevator Lab: two vehicles, one alive

The file's careful distinction is correct, but its characterisation of the VC arm
contains a material error.

**The two vehicles are genuinely separate. CONFIRMED.**

- `elevator-ventures.com` returns HTTP 200, 212,803 bytes. Title: *"Elevator
  Ventures by Raiffeisen Bank International"*. Live.
- `elevatorlab.com` fails to connect (curl exit code 000, no response at all).
- `elevator-lab.com` returns **HTTP 503 Service Unavailable**, 62-byte body.

The accelerator's domains are dead; the VC's is not. Different registrable
domains, different sites, different status. The file was right to separate them.

**Portfolio page CONFIRMED:** `/en/portfolio.html` returned 237,369 bytes,
10,222 chars (file said 237 KB / 10,242). `Headquarters`, `Founded` and
`Selected Co-Investors` fields confirmed per company. Blockpit verbatim:
`Headquarters Linz, Austria Founded 2017 Selected Co-Investors Middlegame
Ventures, Venionaire Capital`, an exact match including both co-investor names.
QuoIntelligence, exnaton (Zurich) and Klim (Berlin) all confirmed.

**CEE fintech mandate CONFIRMED** from the homepage: *"manages funds of more than
EUR 100m to elevate the growth of technology companies in Fintech and Beyond
Banking ... wide sourcing and business development network in DACH and CEE"*.

**But two claims in the entry are wrong. See section 11, items 1 and 2.** The site
states `Series A & B Target stage`, not seed and Series A, and the portfolio page
serves 22 companies in a single EV II section, not "~15 ... more across vintages".

**Verdict: PARTLY CONFIRMED.**

---

## 7. Portfolion (OTP Bank): 46 companies, SEON and Finshape

Served text, verbatim: *"Since our founding, we've invested accross 46 companies
15 verticals 14 countries"* (the typo "accross" is theirs). 229,972 bytes,
2,491 chars against the file's 230 KB / 2,502.

Tier names served before `Show More`, all confirmed present:

- Venture Capital: Kodesage, **SEON**, Riptides, FLOWX.AI, Deskbird, Novakid, Uvionix, Deligo Vision
- Growth Equity: Mobilfox, GymBeam, **Finshape**, Pactum, Pepita.hu, VCC Live, Codecool, 4FIZJO

Both SEON and Finshape confirmed, in the tiers the file assigned them. `Show More`
truncation confirmed. `/portfolio/` and `/portfolio-companies/` 404 as stated.

**Verdict: CONFIRMED on the substance, with one URL correction. See section 11,
item 3.**

---

## 8. Advent: the `Carve-out` deal-type filter

Served verbatim from `adventinternational.com/investments/`:

> `Search by deal type All deal types Buyout Carve-out Expansion capital Growth buyout Growth equity Leveraged buyout Minority growth Other PIPE Privatization Public-to-private Recapitalization Secondary buyout`

`Carve-out` exists as a first-class filter value. The sector filter is also exactly
as claimed: `Business & financial services Consumer Healthcare Industrial
Aerospace, defense, and space Technology`. 238,495 bytes / 11,249 chars against
238 KB / 11,450.

**Verdict: CONFIRMED.** The file lists six of the thirteen deal types but does not
claim the list is exhaustive, so this is not an error.

---

## 9. The DEAD END claims

These were flagged in the brief as the most likely to be invented. **All three are
real, and all three matched verbatim.**

### Tera Ventures: Turkish SEO link spam. CONFIRMED

`https://www.tera.vc/portfolio` returns HTTP 404, 44,227 bytes (file said 44 KB),
2,713 characters (file said 2,713, exact).

Served text, first 200 characters verbatim:

> `Page not found : Tera Ventures Hacklink panel Hacklink panel Backlink paketleri Hacklink Hacklink Hacklink Hacklink Hacklink panel Hacklink panel Hacklink panel ...`

**105 occurrences of "Hacklink"** in the extracted text, plus `Hacklink satın al`
and `Hacklink giriş`. The file's description is accurate and its warning not to
scrape or follow links from the domain is sound.

### enern.com redirects to a Norwegian tourism site. CONFIRMED

`https://www.enern.com/` resolves to
`https://oppdal.com/utforsk/enern-er-avviklet/`, HTTP 404, 170,208 bytes.

Served text: `Page not found - Visit Oppdal Sesonger Vinter Påske Vår Sommer Høst
Jul Book Aktiviteter Mat og drikke Overnatting Bedrifter Hva skjer? ...`

The redirect target, the Norwegian language, the `Visit Oppdal` branding and the
`enern-er-avviklet` slug are all exactly as reported. The file's own caveat, that
the slug is on an unrelated site and is not evidence about the fund, is the right
call and should be kept.

### Catalyst Romania: lorem ipsum placeholder. CONFIRMED

`https://catalystromania.com/portfolio/` returns HTTP 200, 414,610 bytes (file
said 414 KB), 5,242 chars (file said 5,314).

Served text, verbatim:

> `Portfolio Catalyst Romania Portfolio 27 Jul 22 123 FORM BUILDER Catalyst Romania No Comments Lorem ipsum dolor sit amet Read More 03 Dec 19 Elefant.ro Catalyst Romania No Comments Portfolio Look how wonderful work we have done! At vero eos et accusamus et iusto odio digni goiku ssimos ducimus qui blanditiis praese. Ntium voluum deleniti atque corrupti quos. Business Growth ...`

Every specific in the file is present: the `At vero eos et accusamus et iusto odio
digni goiku ssimos` string including the mangled "digni goiku ssimos", the
`123 FORM BUILDER` title dated `27 Jul 22`, the generic `Digital Analysis` and
`Business Growth` titles, and the real names Elefant.ro and Avocatnet mixed in.

**Verdict on all three: CONFIRMED.** These are the vivid details the brief warned
would be invented. They were not invented.

---

## 10. PFR Ventures: did the agent give up too early?

**The 403 is real and fully reproducible. CONFIRMED.**

Tested every reasonable variation:

| Attempt | Result |
|---|---|
| `curl` plain | 403, 25,239 bytes |
| `curl` with Chrome UA plus `Accept-Language: pl-PL` | 403, 25,239 bytes |
| `pfrventures.pl/pl/portfolio.html` | 403 |
| `pfrventures.pl/portfolio.html` | 403 |
| `www.pfrventures.pl/en/portfolio.html` | 403 |
| `pfrventures.pl/` (bare domain) | 403 |
| `pfrventures.pl/robots.txt` | 403 |
| `pfrventures.pl/sitemap.xml` | 403 |
| **WebFetch** | **403 Forbidden** |

Block page text, verbatim: `Grupa PFR Dostęp został zablokowany Dostęp do strony
nie jest możliwy. Skontaktuj się z nami jeśli problem będzie się powtarzał. Ray
ID: ...`, matching the file's report including the Polish wording. The Ray ID
differs, as it must, being per-request.

The whole domain is blocked, not just the portfolio path. The file's account is
accurate and its `Unverified` label is correct.

**However, the agent stopped one step short on the source it itself called the
highest-leverage one. Two avenues were not tried, and both partially work:**

1. **Wayback Machine.** `web.archive.org` has six snapshots, most recent
   **28 May 2023**, retrievable at HTTP 200 (111,938 bytes). It yields the page's
   full filter taxonomy including `Fintech`, `InsurTech`, `RegTech`, a `Fund type`
   axis (`PE`, `VC with Business Angels`, `CVC`) and a `Fund status` axis
   (`Currently investing`, `Exit phase`, `Not active`). Useful for scoping the
   build before solving the block.
2. **PFR's own linked alternative.** The archived page carries: *"Together with
   dealroom and Polish Development Fund we launched a map of the Polish innovation
   ecosystem ... information about active investors on our market"*, linking to
   `poland.dealroom.co`. That is the same meta-source content by another route and
   was never tested by the research pass.

**A third finding matters more for the build than either.** In the archived HTML
both list panes read `No results for chosen filters. Try to clear filters or change
search criteria.` The fund list and the company list are **loaded by AJAX after
page load**. So even with a cookie-bearing browser session that defeats Cloudflare,
a static fetch of the HTML will still return an empty list. The file's remedy
("needs a browser session with cookies") is insufficient: this needs a headless
browser that executes JS, or the underlying XHR endpoint.

**Verdict: CONFIRMED that it is blocked. The file understates what remains to be
done and overlooks two live workarounds.**

---

## 11. Corrections required before this reaches the client

Ordered by how much they affect a build or a client-facing statement.

### 1. Elevator Ventures invests at Series A and B, not seed. MATERIAL.

The file states the fund "writes up to EUR 3M at seed and Series A" and concludes
"Any company it backs is financial-services adjacent, in a TXN market, and
**pre-scale**."

The fund's own homepage states, in its stats block:

> `Series A & B Target stage` · `1-3m EUR Initial ticket size` · `Fintech and
> Beyond Banking Industry` · `Companies in DACH & CEE Geography`

The ticket size is right. The stage is wrong by a full round, in the direction that
weakens the entry. A Series B company is not pre-scale and is materially less
likely to be greenfield on cards. Elevator Ventures is still a good source. It is
just a *later* source than the file claims, and the "pre-scale" sentence should go.

### 2. Elevator Ventures list size and structure. MINOR.

The file says "~15 companies in the EV II section, more across vintages". The
served page has **22 companies** (22 `Headquarters` field instances) under a
**single** heading, `EV II portfolio companies ... vintage starting from 2024`.
There are no other vintage sections on the page. The firm separately states it has
invested in 21 companies to date with seven exits, so the page is close to the full
book rather than a subset.

### 3. Portfolion's monitoring URL is wrong. MATERIAL for the crawler.

The file names `/investment-story/` as "the monitoring surface to poll". That path
**404s** as an index (108,863-byte 404 template).

The real index is **`https://www.portfolion.com/articles/`**, titled *"Investment
stories"*. It serves 11,783 chars with dated entries, and **the file's cited
`19-08-2026` entry is present there**, so the underlying observation was real and
only the URL was recorded wrong. `/investment-story/<slug>/` is the per-post prefix
and works for individual posts.

### 4. Kaya VC is not machine-readable in the way the entry implies. MATERIAL.

The file classes Kaya as "HTML cards (static)" with "~60 companies rendered" and
cites Finiata, Twisto and Bnext as fintech entries. What is actually served:

- **Company names do not appear in the text layer at all.** `Finiata`, `Twisto` and
  `Bnext` appear in the raw HTML only as lowercase strings inside CDN image
  filenames (`..._finiata-black.png`, `..._bnext-bg.png`). They are recoverable,
  but by image-path parsing, not text parsing.
- The descriptions the file quotes *are* served (`Instant SME Lending`,
  `BNPL Provider`, `Personal Finance Hub`), so the entry was written from a real
  fetch.
- **12 cards ship literal unfilled template copy:** `Startup on eline description
  Learn more`, repeated 12 times. The active portfolio is a broken template. Only
  the `Exited` cards carry real descriptions.

Kaya belongs in the same bucket the file correctly assigns to COBIN Angels and
Angel Invest ("names live in logo images"), not in the clean-static bucket. The
entry's own conclusion, that Kaya is the weakest of the Czech funds for monitoring,
survives. The machine-readability line does not.

### 5. SMOK Ventures: one unsupported sub-claim, two missed openings. MATERIAL.

The core claim is exact (1,219 chars, Vue placeholders verbatim). Three problems in
the surrounding recommendation:

- **Not reproducible:** the file asserts an `Investments (12)` blog category count
  and a tag cloud containing `fintech`, `payments` and `KYC`, and recommends that
  as "a perfectly good substitute feed". I could not find any of it.
  `smok.vc/blog/` (6,683 chars) carries **no category or tag links whatsoever**.
  `/blog/category/investments/` and `/blog/investments/` both 404. The strings
  `fintech`, `payments` and `KYC` do not appear in the blog page's raw HTML. The
  blog's dated posts are real and the file's two examples are exact
  (`Why We Invested in intoDNA January 12, 2026`, `Why We Invested In Juo June 27,
  2025`), so the feed exists, but the category and tag filtering that makes it
  "perfectly good" does not, and the recommendation should be softened.
- **Missed, and by the file's own rule:** the file says `smok.vc/angel-network/`
  404s "so that roster was not located". The correct path is
  **`/smok-angel-network/`**, HTTP 200, page title *"SMOK Angels, CEE Angel
  Investor Network | 220+ Founders Turned Investors"* (title punctuation normalised
  to house style). This is exactly the failure mode the file's own operational note
  1 warns about: the homepage href-extraction rule was applied to Movens, Portfolion
  and Innova but not to SMOK.
- **Missed:** SMOK serves **per-company static pages** at `/portfolios/<slug>/`
  (defguard, gemelo, intodna, letsdata, mos-health, principle, prox, pstryk,
  slicker, slickshift), each with the company name and a full description in
  server-rendered HTML. So "0 rendered statically" is true of the index page but
  overstates the problem. SMOK's portfolio *is* recoverable without a headless
  browser, via homepage href extraction.

### 6. Credo's usable name yield is overstated. MINOR.

"84 stated; dozens of names extracted from the HTML" is generous. The 2,426
characters of text yield **16 names**, and every one of them carries an `Exited` or
`RIP` badge. The active portfolio companies render as badge-only cards with the
names in logo images. The finding that curl beats WebFetch here stands. The
implication that the active book is text-parseable does not.

### 7. ING Ventures can now be partly resolved. MINOR, but closes a stated gap.

The file reports HTTP 403 from the Global Venturing article to both curl and
WebFetch. **On retry today the article returns HTTP 200** (189,729 bytes). It
confirms headline and byline: *"Dutch bank ING's ventures arm halts new
investments"*, **May 14, 2025**, by Maija Palmer. The body remains paywalled: the
visible text below the headline is unrelated filler, the standard content-swap. So
the date is now confirmable and the entry can be upgraded from "a headline exists"
to "headline dated 14 May 2025". The substance of the halt still is not readable
and should stay unasserted.

### 8. PFR: add the two untried routes and the AJAX caveat. See section 10.

### Not errors, listed so they are not re-raised

- Character counts drift 0.5-2% against the file across the board. Pages are live.
  Byte counts matched to within 0.01% where the asset is static.
- Market One Capital's column header is `HQ/Country`, the file writes `HQ Country`.
- LAUNCHub measured 4,555 bytes against a claimed 4,551; Antler 254,245 against
  254,212.
- The file lists 6 of Advent's 13 deal types but does not claim completeness.

---

## 12. Fabrication signatures: what I looked for and did not find

I actively hunted for the standard tells. None of them appeared.

- **Invented company names.** The Allianz X entry lists **39 company names**
  recovered from a 404 page's footer, the single most invitation-to-fabricate item
  in the file. I checked all 39 against the served text. **All 39 present. Zero
  fabricated.**
- **Invented funds.** Every one of the 54 entries resolves to a real fund at a real
  domain. No entry names an organisation that does not exist.
- **URLs that 404 where the file says they resolve.** None found. Every list page
  the file marks as working returned HTTP 200 at the URL given. Conversely, every
  404 and redirect the file *reports* was reproduced: GapMinder `/portfolio/` 404,
  `bvalue.vc/portfolio` resolving to `bvaluefund.com`, Allianz X `/our-companies`
  404, `uniqaventures.com/portfolio` 404, `smok.vc/angel-network/` 404,
  `techangels.ro/portfolio/` 404. The one exception is Portfolion's
  `/investment-story/`, which the file gave as a working stream and which 404s
  (correction 3).
- **Domains claimed not to resolve.** `genesiscapital.cz`, `genesiscapital.eu` and
  `depo.ventures` all fail to connect, exactly as reported.
- **Confident specifics that dissolve on inspection.** Repeatedly the opposite. The
  bValue date range "25/07/2024 through 02/11/2025" is precisely the first and last
  dated rows served. Hiventures "~44 companies" is exactly right: four pages of ten
  plus a fifth page of four, and page 5's four entries (BookrKids 17 Apr 2024,
  CX-Ray, Chameleon, DataInnovation, all Mar 2024) match name for name.
  Startup Wise Guys' batch counters read `Fintech 1 3 Fintech 2 4 Fintech 3 3
  Fintech 4 7 Fintech 5 6` and `Active 286 ... Exit 23`, every number correct.
  TechAngels' angel names reproduce with Romanian diacritics intact
  (`Marius Istrate, Felix Crișan, Sergiu Neguț, Ana Maria Andronic, Mihaela Matei`).
- **Round-number tells.** Absent. The file's counts are irregular
  (2,426 / 11,057 / 20,721 / 47,603 / 1,219) and match measurement.

The errors I did find (section 11) are all of one type: **misreading or
over-generalising from a page that was genuinely fetched.** None is an invention.
That is the signature of real work with imperfect note-taking, not fabrication.

---

## 13. Verdict

### Per-entry tally

**54 entries. 52 labelled `Verified`. 2 labelled `Unverified`. All 54 checked.**

| Verdict | Count | Entries |
|---|---|---|
| **CONFIRMED** | **47** | Inovo, Underline, Early Game, GapMinder, Movens, Market One, Day One, ZAKA, J&T, Innovation Nest, OTB, bValue, Hiventures, Lead Ventures, UNIQA, Illuminate, Anthemis, Seedcamp, Speedinvest, Target Global, Middlegame, Motive, Pollen Street, Advent, Hg, MidEuropa, Innova, Abris, FPE, Enterprise Investors, MCI, TechAngels, COBIN, Angel Invest, Superangel, Startup Wise Guys, Practica, Change Ventures, Eleven, Vestbee, SeedBlink, Allianz X, Antler, Tera Ventures, Enern, Catalyst Romania, Presto/Cogito/LAUNCHub |
| **PARTLY CONFIRMED** | **5** | Credo Ventures (name yield overstated), Kaya VC (names not in text layer, 12 placeholder cards), Elevator Ventures (stage wrong, count wrong), Portfolion (monitoring URL 404s), SMOK Ventures (blog category and tags not reproducible; two static routes missed) |
| **REFUTED** | **0** | none |
| **COULD NOT CHECK** | **0** | none |
| *Unverified entries, correctly labelled* | *2* | *PFR Ventures (block confirmed), ING Ventures (403 no longer reproduces; headline and date now confirmable)* |

**47 of 52 `Verified` entries survive validation intact. 5 need correction. None
is refuted.**

### Overall

**The research is sound and was not invented.** I attacked it from every angle the
brief specified and could not find a single fabricated fact.

The strongest evidence is the density of exact matches on things that would be
almost impossible to guess: three domains returning *precisely* 114 bytes with an
identical redirect stub; Enterprise Investors at *exactly* 346 characters and MCI
at *exactly* 385; Credo at *exactly* 2,426 characters; SMOK at *exactly* 1,219
with the literal Vue tokens; Startup Wise Guys at *exactly* 47,603 with five
correct fintech batch counts; Underline's `Date of partnership: August 24, 2026`
sitting one day before the research date exactly as claimed; 39 of 39 Allianz X
footer names; Antler's two URLs byte-identical at 254,245; TechAngels' angel names
with diacritics; and the Catalyst Romania lorem ipsum reproducing down to the
mangled `digni goiku ssimos`. Numbers of that kind come from measurement.

The single most useful claim in the file, that WebFetch reports Credo Ventures'
portfolio as empty while curl returns 2.3 MB with names inline, reproduced exactly,
in both directions, on this pass. It is a real and repeatable tooling defect and
the operational warning built on it is correct.

The two `Unverified` entries are honestly labelled and the reasons given are
accurate. PFR's block is total and reproducible. The file's only failing there is
stopping short of the Wayback and Dealroom routes, and not noticing that the list
is AJAX-loaded even behind the block.

**The load-bearing build decisions all hold:**

- The date field is real on all eight named funds. **A new-deal feed is buildable.**
- The empty-shell finding is real on all nine named targets. **The headless-browser
  tier is genuinely required and the money is not being wasted on a false positive.**

**Recommendation: fix the eight items in section 11, then this is client-ready.**
Corrections 1, 3, 4 and 5 change what a crawler would be built against and should
be made before anyone starts building. Correction 1 also changes a statement about
a fund's investment stage, which is the kind of thing a client will check.

---

*Every URL in this report was fetched during validation on 2026-08-25. Raw
responses retained in the validation scratch directory for this session.*
