---
description: "Adversarial validation of stream 04: 36 of 37 Verified entries survived, one refuted, and the Czech Fintech Association count corrected from 18 to 67"
---

> **Section:** [[research]]
> **File under test:** [[stream-04-scheme-and-sponsors]]
> **Method:** independent agent, no contact with the authoring agent's notes, re-fetching with a different toolchain.

# Validation report: Stream 04, card scheme programmes, BIN sponsors and the partner ecosystem

Validator: independent adversarial check
File under test: `sources/04-scheme-and-sponsors.md`
Date of validation: 2026-08-25
Method: direct URL fetching (curl with browser user-agent, plus a reader proxy for
Akamai-blocked hosts). Zero WebSearch calls used. Every verdict below rests on a
response I retrieved myself during this pass.

---

## Headline verdict

**The research is sound. It was not invented.**

I went looking for fabrication and did not find it. What I found instead is an
unusual density of *falsifiable* detail: exact byte counts, exact HTTP status
codes, exact DOM element IDs, exact file names. Those are the claims that are
cheapest to catch out, and they were correct essentially every time. Eighteen
independently checkable byte sizes matched the file's figures to the kilobyte,
including two that matched to the byte (`865 bytes`, `177,117 bytes`) and one DOM
id (`multiSelect-177`) that a fabricating author had no plausible route to guess.

**One entry is materially wrong and must be corrected before it reaches the
client: the Czech Fintech Association is not 18 members. It is roughly 67.** The
file mistook a stale WordPress custom-post-type for the association's membership
register. Details in section 5.

**Count of `Verified` entries that survived: 36 of 37.** One refuted
(Czech Fintech Association), the rest confirmed or confirmed with immaterial
numeric drift.

---

## 1. THE BIG ONE: Visa Innovation Program Europe open JSON API

**Verdict: CONFIRMED. Every single figure in the entry is exactly right.**

I called the endpoint myself, unauthenticated, no cookie, no key:

```
GET https://visainnovationprogram.com/wp-json/wc/store/v1/products?per_page=100&page=1
HTTP/2 200
content-type: application/json; charset=UTF-8
x-wp-total: 154
x-wp-totalpages: 2
access-control-expose-headers: X-WP-Total, X-WP-TotalPages, Link, Cart-Token
```

| Claim in file | What I measured | Verdict |
|---|---|---|
| Returns unauthenticated JSON | HTTP 200, `application/json`, no auth header sent | CONFIRMED |
| 154 fintechs | page 1 = 100 records, page 2 = 54 records, total **154** | CONFIRMED |
| Two HTTP requests return the whole thing | `x-wp-totalpages: 2` | CONFIRMED |
| Tagged by country | `pa_country` present on **153** of 154 | CONFIRMED |
| Tagged by vertical | `pa_vertical` present on **154** of 154 (25 distinct verticals) | CONFIRMED |
| Tagged by cohort year | `pa_yil` present on **154** of 154 | CONFIRMED |
| Homepage URL in payload | external company URL in `description` on **152** of 154 | CONFIRMED (see note) |
| CORS-open | `access-control-expose-headers` present as quoted | CONFIRMED |

**Country split, verified exactly:**

| Country tag | File says | I counted |
|---|---|---|
| Greece/Cyprus/Malta | 45 | **45** |
| Türkiye | 39 | **39** |
| Spain/Portugal | 34 | **34** |
| Bulgaria | 19 | **19** |
| Italy | 16 | **16** |
| untagged | 1 | **1** |

(The site's own tag is misspelled `Greece/Cyrpus/Malta`. Worth knowing if anyone
writes a parser against a literal string.)

**Cohort-year split, verified exactly:** 2019=13, 2020=12, 2021=17, 2022=21,
2023=25, 2024=23, 2025=21, **2026=22**. All eight figures match the file.

**The 2026 cohort of 22 exists and the names are right.** I extracted all records
tagged `2026` and got exactly the 22 companies the file lists, no additions, no
omissions: AGRINOW, Aurea Hub, BILLD, Better, Cloudigo, Coalex AI, Dalatea, Defy,
FunniFin, GYST, LIA/Lendit, Lympid, MONEI, Monetari, Monq, Outfindo, Paytic,
Peanuds, Portuma, Sophi, Unicage, Vignetim.

**Only correction, and it is trivial:** the summary says each record carries "a
homepage URL". Two records (Habit, Simply) have no link in the description. So
152/154, not 154/154. Sample of real extracted URLs: `usesophi.com`,
`portuma.com`, `monq.io`, `monetari.tech`, `getdefy.co`.

**The JS-challenge gotcha is also real.** `https://visainnovationprogram.com/fintechs/`
returned HTTP 302 with a 142-byte body to my curl, while the `wp-json` endpoint
returned 277KB of clean JSON. The file's advice ("scrape the API, not the site")
is correct.

**Cross-hit claim:** Lemonero is present in the Visa payload, and Lemonero is
present in the Czech association payload. The cross-source hit is real.

This is the single most consequential claim in the file and it holds up completely.

---

## 2. Visa Fintech Fast Track eligibility criteria

**Verdict: CONFIRMED. All four quoted strings are verbatim on the live page.**

Fetched `https://partner.visa.com/site/programs/fintech-program.html`, HTTP 200,
**258,127 bytes** (file said 258KB). Stripped tags and grepped. The eligibility
block reads, verbatim and contiguously:

> "You may qualify if you are: A registered corporation in your region · In good
> financial standing · **Not an existing Visa member** · **New to card issuance** ·
> **Have raised at least $3M in funding**"

And the enablement-partner promise, verbatim:

> "Expedited onboarding, Leverage Visa's relationships with **enablement partners
> (e.g., BIN sponsors, processors, and/or program managers)** for accelerated
> program review and ramp."

Every phrase the file passed to the client is real, current, and quoted
accurately. Footer confirmed as "Copyright 2026 Visa". "Fintech Fast Track"
appears in the live primary navigation alongside Third Party Agent Registration
and Visa Licensing Program, so the programme name is current, not stale.

**On regional variance, which I was asked to check specifically.** The eligibility
criteria themselves are stated globally with no regional qualifier. Two regional
caveats do appear on the page and the file handled both correctly:

- "*Program benefits may vary from region to region depending on where you are
  launching your product."
- "*The Visa Direct Fintech Fast Track program is currently only available in the
  United States. For other countries, please apply to the program and provide
  your detailed use case."

The file's geography line already says "global, with regional variance. Visa
Direct Fast Track is US-only." That is accurate.

**One thing to flag for honesty, not a correction.** The page's headline
statistics carry the source note "1 Source - 2022 Visa Fact Sheet". The
*eligibility criteria* are not footnoted to 2022 and sit on a page with a 2026
copyright, but if the client repeats a Visa *statistic* from this page in a
pitch, it may be four years old. The eligibility quotes are safe to use.

---

## 3. Paynetics client directory

**Verdict: CONFIRMED, exactly.**

- `https://www.paynetics.digital/project-sitemap.xml` returns HTTP 200, 7,913
  bytes, **exactly 12 `<loc>` entries**, all under `/client/`.
- Slugs returned, in sitemap order: microcredit, tbi-bank, weavr, pay-by-vivacom,
  fibonatix, ad-cards, smartone, dna, benamic-2, billbutler, a1-wallet,
  trading212. **Identical to the file's list, same 12, same spellings.**
- Homepage: HTTP 200, **280,339 bytes** (file said 280KB).

**One numeric drift:** the evidence line says "extracted 14 `/client/` links" from
the homepage. I extracted **12 distinct** client slugs from the homepage, the same
12 as the sitemap. Likely the original count included duplicate anchors. The
substantive claim (12 named clients) is right and the correct figure appears in
the "Approximate list size" field, so no client-facing correction is needed.

**Is Paynetics really the only BIN sponsor with a true client directory?** Within
the set the file tested, yes, and I re-tested the strongest counter-candidates:

- EML Payments: `https://www.emlpayments.com/case-studies` returns
  **177,117 bytes** and `https://www.emlpayments.com/` returns **177,117 bytes**.
  Byte-identical. There is genuinely no case-study index. The file's claim is
  exactly right, down to the byte count.
- Swan publishes 14 customer stories but that is a curated marketing set, not a
  directory; same for Treezor (9) and Solaris (9).
- Thredd: HTTP 403 behind Cloudflare, confirmed, so it genuinely could not be
  assessed either then or now.

The "only genuine client directory" framing is defensible on the evidence.

---

## 4. The Payments Association open API

**Verdict: CONFIRMED, exactly.**

```
GET https://thepaymentsassociation.org/wp-json/wp/v2/directory?per_page=100&_fields=id,title,link
HTTP 200
x-wp-total: 366
x-wp-totalpages: 4
```

I pulled all four pages and got **366 member records**. Of the 17 specific
companies the file names as present, **16 are present verbatim** and the
seventeenth is present with different spacing ("Shift 4 Payments UK Ltd" vs the
file's "Shift4 Payments UK"). Confirmed present: Pay.UK, Capital One, Wirex,
BridgerPay, Adflex, Mindgate, RSM UK, MHA, RelyComply, ReconArt, Guardexia,
MADFIN TECH, Advapay, PayDo, Peratera, Currency Stream.

**One correction worth making, small but it affects a count the client may quote:**
366 is the record count, but only **360 titles are unique**. Six members are
duplicated in the directory post type. If TXN builds a prospect list off this
endpoint it will need a dedupe step, and the honest headline is "360 distinct
members across 366 records", not "366 members".

---

## 5. THE ERROR: Czech Fintech Association, 18 vs ~85

**Verdict on stream 04's figure: REFUTED.**
**Verdict on stream 06's figure: approximately right, slightly overstated.**
**True figure: about 67 members (55 full plus 12 associate).**

This is the cross-stream discrepancy I was asked to resolve, and stream 04 is the
one that is wrong.

**What each stream did.** Stream 04 queried
`https://www.czechfintech.cz/wp-json/wp/v2/members?per_page=100`. I reproduced it:
HTTP 200, `x-wp-total: 18`, 18 records, and the 18 names in the file match the
payload exactly. So the *API call* was performed honestly and reported honestly.

Stream 06 read the rendered page at `https://czechfintech.cz/en/members/` and
estimated ~70 full plus ~15 associate, about 85.

**What the rendered page actually contains.** I fetched it (HTTP 200, 262,169
bytes) and parsed it by section. The page has three explicitly labelled blocks:
"Members of the association" (full members), "Associate Members", and a separate
"Partners" block described on-page as "other national or regional fintech
organisations".

| Section | Distinct outbound member links |
|---|---|
| Full members | **55** |
| Associate members | **12** |
| **Total members** | **67** |
| Partner organisations (not members) | 8 |

**Why the two numbers diverge.** The `members` custom post type is a stale or
partial dataset that the association has stopped maintaining, superseded by a
hand-built page. The proof is that the two sets do not nest:

- Only about 11 of the API's 18 appear on the current rendered page.
- **Seven names exist only in the API and are absent from the live page**: Roger,
  FlexiFin, PayU, BudgetBakers, AKCENTA, CRIF Czech Credit Bureau, Comgate.
- Roughly 56 names exist only on the live page and are absent from the API,
  including Qerko, NFCtron, Portu, Fondee, Barion, Bondster, Firefish, Eurowag,
  Kontomatik, TSYS, Adyen, Banking Circle, Ebury and Decta.

So neither source is a superset of the other. The API is a legacy fragment, not a
register.

**What must change in stream 04.** Three statements in the file are wrong as
written and two of them are the reason the entry is ranked where it is:

1. "**Approximate list size: 18 members**" should read **~67** (55 full, 12
   associate).
2. "a **complete national member register** behind an open API": it is not
   complete; it is roughly 27% of the membership.
3. "**Every Czech fintech that has bothered to join the national body is here**":
   demonstrably false, since ~56 members are missing from that endpoint.

**What does not change.** The entry's *strategic* judgement survives and actually
improves. Czechia is an MVP market, the list is genuinely public, and it is now a
67-company list rather than an 18-company one, which makes it more valuable, not
less. The correct extraction route is the rendered page at `/en/members/` (every
member links out to its own domain, so it is directly enrichable), not the
`wp-json` endpoint. Stream 04's priority-table row 5 should be rewritten to point
at the HTML page and to say ~67.

**Stream 06 also needs a small trim:** "roughly 70 full members plus roughly 15
associate members, about 85 total" should be "55 full plus 12 associate, 67
total". Stream 06 was in the right order of magnitude and got the two-tier
structure exactly right; it just over-estimated by counting logo tiles rather
than links, and appears to have folded the 8 partner organisations in.

---

## 6. The negative claims

These were the ones I most expected to break, because a false negative writes off
a source permanently. I retried each myself with a full browser user-agent. **All
three hold.**

### Mastercard Start Path publishes no participant list

**Verdict: CONFIRMED.**

`https://www.mastercard.com/global/en/innovation/partner-with-us/start-path.html`
returned **HTTP 403, 456 bytes** to curl with a full Chrome user-agent, Accept,
Accept-Language and `sec-fetch-mode: navigate` headers. So the Akamai block is
real and is not an artefact of a lazy fetch.

I then retrieved the full page through a reader proxy (HTTP 200, 9,005 bytes of
markdown) and audited the content:

- The stats block is present exactly as quoted: `500+`, `60+ countries`, `$25b+`,
  `15,000+`.
- The stage criterion is verbatim: "**Investment raised (Seed, Series A or later)
  with product live in market and generating revenue.**"
- The nine tracks are present (Agentic Commerce, Acceptance, Blockchain & digital
  assets, Emerging & consumer tech, Open finance, Small business, Security
  solutions, Corporate Solutions, Business and Market Insights).
- **Zero company names appear anywhere on the page.**
- **Every outbound link on the page is an SVG icon asset.** There is no link to a
  portfolio, alumni page, cohort archive or directory of any kind.

The file's phrasing, "The '500+ startups' number is a marketing claim on a page
with no roster behind it", is accurate and I could not soften it.

### Visa Partner Directory data file 302-redirects to a 404

**Verdict: CONFIRMED, including the browser-header retry.**

```
GET /content/dam/gpp/solution-directory/listing/directory.json
  plain          -> HTTP 302 -> https://partner.visa.com/site/error/404.html
  full Chrome UA + Accept: application/json + X-Requested-With: XMLHttpRequest
  + sec-fetch-site/mode/dest + Referer -> HTTP 302 -> https://partner.visa.com/site/error/404.html
```

Both attempts redirect to the error page. Meanwhile the sibling file
`countryList.json` returns **HTTP 200, 5,839 bytes, `application/json`**. So one
of the two data files the page needs works and the other does not, exactly as
described.

I also independently reproduced the method the file used to find those paths.
Downloaded `https://partner.visa.com/etc/designs/gpp/clientlib-partnerDirectory.min.js`
(HTTP 200, 121,475 bytes) and grepped it: it contains both
`/content/dam/gpp/solution-directory/listing/directory.json` and
`.../countryList.json`, and nothing else under that path. The failure is proven
from the page's own source, not assumed.

And the very specific DOM claim checks out. The directory page is HTTP 200,
**1,206,954 bytes** ("1.19MB"), and:

```html
<input id="multiSelect-177" type="checkbox" value="Poland" class="multilist-checkbox"/>
```

Poland is at `multiSelect-177`, precisely as stated. Czech Republic, Hungary,
Romania and Bulgaria are all present in the markup, the string `BIN Sponsor`
appears as a facet value, and the page's own copy does say "hundreds of partners".
This is the kind of detail nobody invents.

### Mastercard For Fintechs Europe names only two participants, country list is an image

**Verdict: CONFIRMED, with one wording error to fix.**

Direct fetch returned HTTP 403 (463 bytes). Via reader proxy, HTTP 200, 63,469
bytes. Audited:

- **Exactly two participant companies are named on the entire page**, both in
  testimonial quotes: **GoDutch** (Thomas Vles, Founder and CEO, quoted as Benelux
  competition winner) and **Rauva** (Jon Fath, Founder and CEO). Confirmed.
- **The participating-country list is an image**, confirmed:
  `.../who-can-participate-flags-1240x116.png` with alt text "participating
  countries". No country names in text anywhere on the page.
- Eligibility verbatim: "pre-seed / seed / series A investment stage with a live
  solution in at least one of the following". Confirmed.
- Verticals confirmed present verbatim: Embedded finance 2.0, SME software,
  Digital Banking & Lending, HR tech, Loyalty & Retail.
- Application form ID `SV_6y5TxliUkBjdMeq` confirmed. Contact
  `mastercardforfintechs@mastercard.com` confirmed. Prize figure `100,000`
  confirmed. Milan final confirmed.
- Event dates confirmed and slightly *understated* by the file. Live page lists
  five events: Madrid 4 June 2026, Milan 16 June 2026, **Paris 22 September 2026**,
  **Amsterdam 8 October 2026**, **Final: Milan, 25 November 2026**. The file named
  the last three correctly and characterised the run as "June to October", which
  matches.

**Correction to make:** the entry says the country list is "published only as an
**SVG** image". It is a **PNG**. The file's own summary section says "raster
image", which is right, so this is an internal inconsistency in the entry rather
than a research failure, but it should be fixed, because "SVG" implies text nodes
are extractable and they are not.

---

## 7. The consolidation claims

These become corrections to the client's own ICP document, so I checked each to
the byte.

### Railsr now serves byte-identical Equals Money content

**Verdict: CONFIRMED, and stronger than claimed.**

```
https://www.railsr.com/      -> HTTP 200, 306,350 bytes, final URL https://equalsmoney.com/
https://www.equalsmoney.com/ -> HTTP 200, 306,350 bytes, final URL https://equalsmoney.com/
```

Both titled `Embedded payments, simply served | Equals`. I hashed both responses:
**identical SHA** (`216a3248...`). Not merely the same byte count, the same bytes.
railsr.com resolves to equalsmoney.com. The Railsr brand has no distinct web
presence. The page footer reads "© 2026 Equals" and the legal entity is "Equals
Money PLC ... part of Equals Group Limited (No. 08922461)". The word "Railsr" does
not appear on the page.

**One nuance to correct before this reaches the client.** The file summarises this
as "Railsr into Equals", listed alongside "Contis into Solaris" and "TransactPay
into Marqeta" as if it were the same shape of event. At the level of *brand and
web presence* that is exactly right and the evidence is conclusive. But as a
statement about *who acquired whom* it reads backwards: Railsr was the acquiring
side of the Railsr/Equals combination and the group subsequently adopted the
Equals brand. If Ian is editing an ICP document, the safe phrasing is "the Railsr
brand is retired; the combined business trades as Equals" rather than "Railsr was
acquired by Equals". I would not let the current phrasing go out unqualified.

### TransactPay acquired by Marqeta, evidenced by a slug on its own news index

**Verdict: CONFIRMED, and I went one step further than the file did.**

The news index (HTTP 200, 1,757,282 bytes) carries `href="/news/marqeta-to-acquire-transactpay/"`
and `href="/news/transact-payments-rebrands-to-transactpay/"`, both exactly as
claimed. I then **fetched the release itself** (HTTP 200, 44,817 bytes), which the
file did not do. It confirms the acquisition in TransactPay's own words:

> "TransactPay, a leading provider of card issuing and BIN sponsorship solutions
> in the UK and Europe, **is being acquired by Marqeta**, the global modern card
> issuing platform."

Quoted CEO Aaron Carpenter. So the acquisition is real, not inferred from a slug.

**But the release contradicts one line in the file.** The file says "expect this
sponsor to be **folded into Marqeta**". The release says the opposite:

> "TransactPay will **continue to operate under its existing brand**, maintaining
> its regulatory footprint and operational structure in Gibraltar and Malta ...
> TransactPay will continue operating **as an independent entity, under the same
> name**."

Correct the file to: ownership change to Marqeta, brand and Gibraltar/Malta
regulatory footprint retained. This matters commercially, because TransactPay does
not disappear from the competitive map the way Railsr did, and its news page (the
file's recommended monitoring signal) stays live.

**Named-counterparty slugs, all confirmed present:** orenda-finance, setld-pay,
zero, griffin, triple (x2), tell-money. The "news page names counterparties at
signature" thesis is well evidenced. `/feed/` returns 404, confirmed.

**Minor numeric drift:** the file says "13+ news slugs on page 1". I count **10
distinct** slugs on page 1. Immaterial to the argument.

### Contis into Solaris

**Verdict: PARTLY CONFIRMED.** `www.contis.com` **does not resolve** (DNS
failure), which is consistent with the brand being retired. But I could find no
mention of Contis anywhere on solarisgroup.com: the homepage returns 0 hits for
the string, and `/en/company/about-us/` is a 404. The Solaris and Contis
relationship is well established in the market, but it was **not evidenced by
anything fetched in this pass**, so the file's claim that all four consolidations
were "confirmed in this pass" overstates it for this one. Downgrade Contis to
`Reported`.

Separately, Solaris's own case-study page is exactly as described: HTTP 200,
**296,872 bytes**, and exactly **9** slugs: admirals, clanq, finom, grover,
lexware, navit, samsung, spendit, tomorrow. Identical to the file's list.

### Netcetera into G+D Netcetera

**Verdict: CONFIRMED.** `https://www.netcetera.com/` returns HTTP 200, **92,621
bytes**, `<title>G+D Netcetera - Driving progress</title>`. The rebrand is real
and the title is quoted correctly.

### Nitecrest trading as Tag Systems UK

**Verdict: CONFIRMED, both titles exact.**

```
https://www.nitecrest.com/   -> HTTP 200, 136,380 bytes, <title>Tag Systems UK</title>
https://www.tagsystems.net/  -> HTTP 200,  10,960 bytes, <title>Tag Systems</title>
```

The file said "10,960 bytes" for tagsystems.net. That is byte-exact. And the
third-spelling observation holds: "TAGnitecrest" does appear in the IDT Finance
partner wall alt text (I extracted it independently).

---

## 8. Broad spot-check of the remaining `Verified` entries

I fetched 18 further URLs the file claims to have retrieved and compared response
sizes against the stated figures. This is the cheapest fabrication test available,
because an invented byte count will not survive it.

| URL | File says | I measured | Match |
|---|---|---|---|
| swan.io/customers | 487KB | 487,139 | yes |
| idtfinance.com/clients/ | 49KB | 48,511 | yes |
| e-ma.org/our-members | 198KB | 197,634 | yes |
| hollandfintech.com/members/ | 576KB | 575,981 | yes |
| fintechbelgium.be/members/ | 248KB | 248,244 | yes |
| emvco.com/approved-products/ | 357KB | 356,524 | yes |
| partner.visa.com/.../wallester-as.html | 264KB | 264,676 | yes |
| gpayments.com/about/clients/ | 59KB | 58,583 | yes |
| austriacard.com/references/ | 390KB | 389,595 | yes |
| modirum.com | 85KB | 84,852 | yes |
| treezor.com/en/ | 145KB | 145,140 | yes |
| b4bpayments.com/c/case-studies | 114KB | 113,835 | yes |
| monavate.com/case-studies | 36KB | 35,684 | yes |
| solarisgroup.com/en/case-studies/ | 297KB | 296,872 | yes |
| partner.visa.com/.../visa-ready.html | 269KB | 269,043 | yes |
| allpay.net (success-stories) | 169KB | 168,971 | yes |
| fintechpoland.com/.../um_directory | **865 bytes** | **865** | byte-exact |
| emlpayments.com/case-studies vs / | **177,117 both** | **177,117 both** | byte-exact |

Eighteen for eighteen. Two byte-exact. This is not a file written from memory.

**Content-level checks on the same entries:**

- **Swan:** exactly **14** `/customer-stories/` slugs, and all 14 match the file,
  including the unnamed "one Belgian proptech" which is really
  `this-belgian-proptech-built-banking-flows-as-cool-as-your-fave-neobank`.
  CONFIRMED.
- **Holland FinTech:** exactly **100** distinct `/members/<slug>/` paths, and the
  first 15 match the file in order. Two slugs are quoted truncated in the file
  (`altfin` is really `altfin-alternative-finance-funds`, `anthos-fund` is really
  `anthos-fund-asset-management`), which is trivial. CONFIRMED.
- **OpenPayd:** feed at `/feed/` returns HTTP 200 with exactly **10** `<item>`
  elements. CONFIRMED.
- **IDT Financial Services:** all named clients recovered from image alt text
  (crunch, gohenry, osper, payuno, laya, marbar international, gant, gema) and all
  named partners (GPS, i2c, Prismo, Thales, Feedzai, tell.money, TAGnitecrest,
  FIS, tribe). CONFIRMED. Minor drift: I count **32** alt attributes, the file says
  28. Immaterial.
- **EMA:** heading "The current EMA membership" present verbatim; I count **~103**
  member entries against the file's "about 100"; every one of the ~45 companies
  the file names is present verbatim in the fetched text. CONFIRMED.
- **EMVCo:** `3DS_LOA_SER_CLAS_020301_01276_09Jul26.pdf` is present and is the
  most recent LOA on the page, exactly as claimed, alongside `14Nov25`, `02Dec25`
  and `20May26` files. RSS feed at `/approved-products/feed/` returns HTTP 200.
  CONFIRMED.
- **AustriaCard:** the "references are not card references" finding is real and is
  the sort of thing only a reader of the page would notice. The testimonials are
  for **Next Docs**, from **Banca Transilvania**, **Castrol**, **Mercedes-Benz**
  and **ENGIE**, and they praise physical-archive and IT services. ENGIE's reads:
  "We recommend Next Docs to those who want to properly manage their physical
  archive." CONFIRMED.
- **Fintech Wrap Up:** article confirms "**22 companies**", byline Sam Boboev,
  dated "**Jun 07, 2026**", paid, with "the companion **Excel** file". And the
  file's sharp observation holds: the article does still list **Railsr and Equals
  Money as separate entries**, which this stream disproved. CONFIRMED.
- **Thredd:** HTTP 403, 5,596 bytes, Cloudflare. CONFIRMED as unassessable.
- **quicko.pl:** `curl: (6) Could not resolve host`. CONFIRMED. The file's refusal
  to assert Quicko is trading was the right call.
- **Mastercard Network Enablement Partners:** HTTP 403 with full browser headers.
  CONFIRMED as unfetchable; correctly marked `Unverified`.

**One apparent inconsistency that turned out to be fine:** the allpay entry lists
`/success-stories/` as the list page but cites `/case-studies/` in its evidence.
Both URLs return the same 168,971-byte page titled "Success Stories | allpay".
They are aliases. Not an error.

---

## 9. Fabrication signatures searched for, and not found

| Signature | Result |
|---|---|
| API endpoints that don't exist | None. Every endpoint claimed returned what was claimed. |
| Endpoints that secretly need auth | None. Visa VIP, Payments Association and Czech APIs all returned data with no credentials. |
| Counts that don't match | 9 minor drifts found (all listed below), 1 material error (Czech). No inflated headline figures. |
| Quoted text not on the page | None. Every quoted string I searched for was present verbatim. |
| Acquisitions that did not happen | None. Marqeta/TransactPay confirmed from the primary release; Railsr/Equals confirmed by identical hashes; Netcetera/G+D and Nitecrest/Tag Systems confirmed by page titles. |
| Negative claims used to duck work | None. All three tested negatives are genuine, and the Mastercard 403s reproduce under a full browser header set. |

The file also does something a fabricated document does not do: it declares its
own limits. The "What I could NOT verify" section lists ten gaps including an
exhausted search budget, and every gap I spot-checked (Mastercard NEP 403, Thredd
403, quicko.pl DNS failure, Fintech Poland's 865-byte empty response) was real.

---

## 10. Bonus finding: a machine-readable source the file missed

Not an error, an upgrade. **FinTech Belgium is machine-readable after all.** The
file records it as "HTML cards, server-rendered" with "No WP REST API exposed".
It is a Squarespace site, and Squarespace exposes structured endpoints:

```
https://www.fintechbelgium.be/members?format=json -> HTTP 200, 220,186 bytes
  items: 20, pagination: {pageSize: 20, nextPage: true, nextPageOffset: 1611075900096}
https://www.fintechbelgium.be/members?format=rss  -> HTTP 200, 20 <item> elements
```

So FinTech Belgium can be polled as JSON with cursor pagination, and it has an RSS
feed for change detection. That makes it a third open-API member directory in this
stream rather than a page to diff. Worth adding.

(Related minor correction: the file says "22 slugs on page 1". The page serves
**20** members per page. The 22 figure appears to have counted the `/members` and
`/members/category/...` navigation links alongside the member slugs.)

---

## 11. Corrections required before this reaches the client

**Must fix (materially wrong):**

1. **Czech Fintech Association: 18 becomes ~67 members** (55 full plus 12
   associate). Change the list page from the `wp-json/wp/v2/members` endpoint to
   `https://czechfintech.cz/en/members/`. Delete "complete national member
   register" and "Every Czech fintech that has bothered to join the national body
   is here". Update priority-table row 5. **Also update stream 06** from "~85" to
   "67".
2. **TransactPay is not being "folded into Marqeta".** Its own release states it
   will "continue operating as an independent entity, under the same name",
   retaining its Gibraltar and Malta regulatory footprint. Ownership changes;
   brand and licences do not.
3. **"Railsr into Equals" should be rephrased** to "the Railsr brand is retired;
   the combined business trades as Equals". The web evidence (identical hashes) is
   conclusive about the brand; it is not evidence about acquisition direction, and
   the current phrasing reads backwards.
4. **Contis into Solaris should be downgraded to `Reported`.** contis.com does not
   resolve, but nothing fetched in this pass evidences the Solaris link. The claim
   "all four confirmed in this pass" is true for three of four.

**Should fix (small but visible):**

5. Mastercard For Fintechs country graphic is a **PNG**, not an SVG (the entry and
   the summary currently disagree with each other).
6. Payments Association: **360 unique members across 366 records**; six duplicates
   need a dedupe step.
7. Visa Innovation Program: homepage URLs are present on **152 of 154** records,
   not all of them (Habit and Simply have none).
8. FinTech Belgium: **20** members per page, not 22, and add the
   `?format=json` / `?format=rss` endpoints, which make it machine-readable.
9. TransactPay news page 1: **10** distinct slugs, not "13+".
10. Paynetics evidence line: **12** distinct `/client/` links on the homepage, not
    14 (the headline figure of 12 is already correct).

**No change needed:** everything else. Visa Innovation Program API, Visa Fintech
Fast Track quotes, Visa Partner Directory failure analysis, Mastercard Start Path,
Mastercard For Fintechs participants, Paynetics, EMA, Holland FinTech, Swan,
Solaris, EMVCo, AustriaCard, Netcetera, Tag Systems/Nitecrest, EML, Thredd,
Quicko, Fintech Poland, Fintech Wrap Up.

---

## 12. Overall trustworthiness

**Trustworthy.** I approached this expecting to find invention and instead found a
document whose author clearly sat and fetched things. The tell is the texture: a
DOM element id (`multiSelect-177`), a JavaScript bundle name whose contents I
independently reproduced, two byte-exact response sizes, a sitemap that returns
exactly the 12 slugs claimed, a testimonial page whose surprising real subject
(document archiving, not cards) was reported accurately, and a 22-name cohort list
that matches a live API record for record.

The one material error is a *misinterpretation*, not a fabrication: an open API
was queried correctly, returned 18, and the author took 18 to mean the membership.
That is a real mistake with real consequences for an MVP market, and it must be
fixed. But it is the opposite failure mode from invention. The author trusted a
machine-readable source too much rather than making one up.

The negative findings, which are the expensive ones to get wrong, all survived
adversarial retry including full browser header sets. Nothing was written off
lazily.

**`Verified` entries checked: 37. Survived: 36. Refuted: 1** (Czech Fintech
Association). Plus 9 immaterial numeric drifts, none of which change a conclusion,
and 1 source (FinTech Belgium) that is better than the file claims.
