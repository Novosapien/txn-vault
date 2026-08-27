---
description: "Adversarial validation of stream 06: no invented source found, but six of fourteen entries carried a wrong count and Deloitte Fast 50 CE excludes Hungary"
---

> **Section:** [[research]]
> **File under test:** [[stream-06-events-media-communities]]
> **Method:** independent agent, no contact with the authoring agent's notes, re-fetching with a different toolchain.

# Validation report: Stream 06, events / media / communities

Validator: independent adversarial pass
Validation date: 2026-08-25
File under test: `sources/06-events-media-communities.md`
Method: direct WebFetch plus `curl` with a full browser user agent. Web search
budget was already exhausted at session level, so every finding below rests on a
page actually retrieved, not on a search snippet.

## Headline verdict

**The research is real.** No invented source, no fabricated event, no fake
newsletter, no 404 among the entries marked `Verified`. Where I could count
companies off a page, the named companies matched the file, frequently
name-for-name across 20 to 55 entries. That is not a pattern a fabricating agent
produces.

**But the precise counts are unreliable, and there is one hard factual error that
must be fixed before this reaches Ian.** Six of the fourteen `Verified` entries I
tested carry a wrong number, and one carries a wrong market-coverage claim that
directly misleads on an MVP market.

Scoreboard for the fourteen `Verified` entries I tested end to end:

| Outcome | Count | Entries |
|---|---|---|
| CONFIRMED, no correction needed | 7 | Infoshare, South Summit, Web Summit, ROTSA, Cashless (awards), Czech Fintech Association, Copenhagen Fintech |
| PARTLY CONFIRMED, source real, number or claim wrong | 7 | Money Motion, Latitude59, Deloitte Fast 50 CE, The Hub, RoFintech, Vestbee, Swedish Tech Weekly |
| REFUTED (source does not exist or claim is invented) | 0 | none |

Separately, one `Unverified` blocked-source claim is **refuted**: Impact CEE is
not blocked. And two "blocked" sources including Sifted have an open,
machine-readable route the researcher did not find.

---

## 1. The load-bearing claims

### Money Motion (Zagreb): PARTLY CONFIRMED

**The accretion claim, which is the valuable part, is CONFIRMED.** This is the
single most important finding in the file and it holds up exactly as described.

I pulled `https://www.money-motion.eu/startups/` with curl (HTTP 200, 195KB) and
parsed the raw HTML rather than trusting a summariser. The page carries a live
cohort block followed by a section literally headed **"Check Out Previous Money
Motion Finalists"** with three further blocks headed `Startups 2025`,
`Startups 2024` and `Startups 2023`. Every company carries a country tag. The
page accretes. It does not reset.

Exact counts read off the HTML:

| Block | File claims | Actual | Verdict |
|---|---|---|---|
| MoMo2026 competition finalists | 19 | **18** | wrong by one |
| Startups 2025 | 20 | 20 | correct |
| Startups 2024 | 15 | 15 | correct |
| Startups 2023 | 10 | 10 | correct |
| Cumulative | 64 | **63** | wrong by one |

The 2026 block in full, 18 names: Coverally (SK), UNYX AI (UK), Creagen (UA),
Alerts Bar (US), eFrontiers (CH), Apeyron (IT), Cyber Quanta (TR), Sablier (IT),
aurea (IT), Streamflow (RS), Dexpiry (HR), Protokol.io (RS), Curvy Protocol (RS),
FraudShield (HU), Hobba (HR), Turing Space (NL), Inovat (UK), Bothub Trade (SE).

The four sample names the file quotes (Coverally, UNYX AI, Creagen, Alerts Bar)
are the first four on the page, in that order. The file was genuinely read off
the page.

Two additional corrections the file should absorb:
- **Cumulative unique is 61, not 63.** FraudShield and eFrontiers each appear in
  both the 2026 and 2025 cohorts. Anyone building a prospect list off this page
  needs to dedupe.
- The stale-text caveat is **confirmed and worth keeping**: the page really does
  still say "Applications closed January 28th, 2025" under a 2026 heading.
- Minor: the page footer says "over 700 companies and 3,500 professionals", where
  the file cites 3,000 attendees from the homepage. Low stakes, but 3,500 is what
  the startups page says.

**Correction required:** 19 to 18, 64 cumulative to 63 (61 unique).

### South Summit Madrid: CONFIRMED

Every element of this entry checks out. The article at the stated URL names all
100 finalists on the page itself, free, no gate. The ten verticals are real and I
read them off: Climate Tech & Sustainability, Consumer, Digital & Tech Solutions,
**Fintech & Insurtech**, Future of Work & Talent, Health, Industry 5.0, Mobility
& Smart Cities, Trust Tech & Data, Enterprise Solutions. The Fintech & Insurtech
vertical holds 10 startups. The applications figure is confirmed verbatim:
"selected from more than 4,500 applications across 110 countries", 80% of
submissions international.

No correction required. This entry is exactly as advertised.

### Romania Startup Awards (ROTSA): CONFIRMED, and the substitution is legitimate

This was the claim I most expected to break, and it did not.

The StartupCafe.ro article at the stated URL is real and carries the full nominee
list. I confirmed independently: organiser ROTSA (Romania Tech Startup
Association), gala 12 March 2026 in Bucharest, public voting closed 11 March
2026, the two-tier **Best Innovators** / **Best Performers** structure, and an
explicit **FinTech & InsurTech** category inside Best Innovators containing
exactly the five companies the file names: Fagura, Finergy, PayByFace, SOLO,
stock.estate. The article names approximately 157 startups, consistent with the
file's "150+" and with the reported 137 Romanian / 9 Moldovan / 11
Romanian-founded-abroad split.

**On the substitution.** The file says rotsa.ro 403s and that it used
StartupCafe.ro instead. I tested this hard and the substitution is honest, not a
cover for softer sourcing:
- `rotsa.ro/en/list-of-technology-startups-in-romania/` returns 403. Confirmed.
- I then found ROTSA's *real* list URLs by scraping its homepage (which does
  return 200): `/proiecte/lista_startup_tech/`,
  `/en/projects/listing-of-technology-startups-in-romania/`,
  `/harta-tech-startups-romania/` and `/rostartup-awards-ro/`. **All five return
  403.** ROTSA blocks every list route.
- The count did not come from somewhere softer. It came from a fetched article
  that names the companies in full.

One process note: the URL the researcher tried,
`/en/list-of-technology-startups-in-romania/`, does not exist on ROTSA's site.
The real path is `/en/projects/listing-of-technology-startups-in-romania/`. That
is a guessed URL, which brushes against README rule 1. It changes nothing here
because the real paths 403 too, but it is the one place I caught the researcher
inventing a URL rather than discovering one.

**No correction required to the finding.** Optionally add that ROTSA also
publishes a Romanian tech startup map and an investor list, both 403-blocked, so
a browser session against rotsa.ro is worth more than the file implies.

### Deloitte Technology Fast 50 Central Europe: PARTLY CONFIRMED, contains a hard error

The structural claims are **confirmed in full and were clearly read off the
page.** Four separate lists per year, not one, exactly as claimed:
1. **Fast 50** (main ranking)
2. **Companies to Watch**, described on-page as "companies that are too young to
   be listed in Fast 50, but are growing rapidly". This is the greenfield tier
   and the file characterises it correctly.
3. **AI Value Driver**, with Google Cloud. Confirmed.
4. **Impact Stars**, and the page confirms its scope covers "Fintech, Cyber, ESG,
   MedTech/BioTech, or Defence". Confirmed.

The three downloadable PDFs are confirmed at the exact sizes claimed: 2025 (17MB),
2024 (26MB), 2023 (25MB). Matching three file sizes to the megabyte is about as
strong an anti-fabrication signal as this exercise produces.

**But the country coverage claim is false.** The page's eligibility text
enumerates the programme's countries explicitly:

> "open to companies with headquarters based in the following countries: Estonia,
> Latvia, Lithuania, Poland, the Czech Republic, Slovakia, Romania, Croatia and
> Ukraine"

I grepped the entire page. The string "Hungar" appears **zero times**.

The file claims twice that it covers all four MVP markets:
- Summary, line 33: "covers 9 countries including all four MVP markets"
- Entry, line 560: "Covers all four TXN MVP markets."

It covers **three of four**. Hungary is excluded. This matters because the file
separately and correctly identifies Hungary as its weakest-covered MVP market,
and this error papers over exactly that hole. Note the entry's own **Geography**
field lists the nine countries correctly, without Hungary. So the file
contradicts itself: the analytical claim was never checked against the data field
printed two lines above it.

Also unsupported: "now in its 27th edition". The page contains no occurrence of
"edition", "27th" or "anniversary". The programme page presents itself as the
2026 edition with 2025 as the most recent completed ranking. The 27th-edition
claim should be dropped or downgraded to Reported.

**Corrections required:** remove "all four MVP markets" in both places, replace
with "three of the four MVP markets, Poland, Czech Republic and Romania. Hungary
is not covered." Drop or downgrade "27th edition".

### The Hub (thehub.io): PARTLY CONFIRMED, understated

The source is real, the filter claim is right, and the scale claim is wrong in
the client's favour.

- **Actual figure on the page today: "Showing: 11113 filtered startups".** The
  string "9,000" does not appear on the page. The file's "9,000+" is stale or
  came from a marketing headline elsewhere.
- **Per-country counts match the file exactly**: Denmark 5,233, Sweden 2,373,
  Norway 2,279, Finland 1,434, Iceland 24. Reading five numbers off correctly and
  then getting the headline total wrong suggests the total was taken from
  somewhere other than the page.
- **Fintech filter CONFIRMED**, and it is more useful than the file says: the
  filter carries a live count of **1,005 fintech companies**.
- Stage, size and funding filters confirmed (Idea / Product or prototype / Go to
  market / Growth and expansion; 1-10 through 200+; looking for funding 4,400 vs
  not looking 5,841). An Impact SDG filter also exists.
- Self-registration model confirmed.

**Correction required:** 9,000+ to 11,113. Add the 1,005 Fintech filter count,
which is the number that actually sizes the opportunity.

### Swedish Tech Weekly: PARTLY CONFIRMED, the "whole archive" claim is too strong

I tested the sequential URL claim directly, which is what the brief asked for.

Issue 368 fetched clean. Confirmed: issue number 368, published **24 August
2026** (a Monday, consistent with the claimed Monday cadence, and the day before
this validation), author **Martin Weigert**, free tier with a PRO tier marked by
"[PRO last week]" annotations and a "Request Invite to PRO" path, and the section
structure (M&A, funding, startup database, sector news, events, jobs). Company
density confirmed at roughly 28 named companies in the issue, inside the claimed
25 to 30 band.

**Sequential URL test, `/swedish-tech-weekly-<n>/`:**

| Issue | HTTP |
|---|---|
| 369 | 404 (not yet published) |
| 368 | 200 |
| 367 | 200 |
| 366 | 200 |
| 365 | 200 |
| 300 | 200 |
| 295, 290, 280, 270, 260, 250 | 200 |
| 230 | 404 |
| 210 | 404 |
| 200 | 404 |
| 100 | 404 |

**The mechanism works and is genuinely enumerable, but not for the whole
archive.** It breaks somewhere between issue 230 and 250. The file's claims that
"sequential issue numbers make the whole archive trivially enumerable" and that
there are "roughly seven years of continuous back issues" are both too strong.
Roughly 120 to 140 issues are reachable at this URL pattern, call it two and a
half years, not seven.

**Correction required:** soften to "issues from roughly 250 onward are reachable
at this pattern, about 120 back issues; earlier issues 404 at this URL form."

### Cashless.pl: CONFIRMED on awards, map figure remains Reported (correctly labelled)

The awards half is confirmed name-for-name. Three categories, 15 nominees:
**Projekt Fintech** (Comfino, FastTip, Allegro Klik, Leaselink Flex Limit,
SmartTerminal/mBank, WeSub Flex), **Osobowość Fintech 2026** (4 individuals),
**Fintech Roku 2026** (Lendi, PayPo, PragmaGO, Smartney Grupa Oney, Wealthon,
Zen). Matches the file.

On the map: `https://www.cashless.pl/fintechy/s` does host the **Mapa polskiego
fintechu** and describes itself as "the most comprehensive work for and about the
fintech industry on the Polish market". It is paginated and browsable. But
**neither "383" nor any edition number appears on that page.** The file already
labels the map contents `Reported` and states plainly that the 383 figure and the
18 June 2026 date came from article titles in search results. That labelling is
honest and I am not marking it as an error. It is simply still unverified, and
with the search budget gone I could not close it.

One small overreach: the file gives the Cashless Fintech Evening as "18 June".
The nominees page says only "w czerwcu 2026" (June 2026). The specific day is not
on the fetched page.

### Czech Fintech Association: CONFIRMED

Roughly 70 full members plus roughly 14 associate members, about 85 total. The
file said "roughly 70 full plus roughly 15 associate, about 85 total". Accurate.
I independently read back the member roster and it matches the file's list almost
name-for-name across more than 50 companies, including the long-tail small
companies the file highlights (Qerko, NFCtron, Flowpay, Fingood, Frenkee, Dobito,
Karstfin, Taxomat, WFlow, Corrency, Mo.one, Eterny, Unnits, Metada). Members are
rendered as linked logos with outbound URLs, so the enrichability claim holds.

I picked up two members the file missed (TipInc, Five Crafts) and two extra
associate members (Akschejbal, Martinik Legal). No correction needed; the file's
counts already absorb these.

### RoFintech: PARTLY CONFIRMED, minor count drift

Structure confirmed exactly: four sections, **Fintech Members**, **International
and Corporate Members**, **Strategic Partners**, **International Partners**.

Counts: I read **45** fintech members and **17** international/corporate, so 62.
The file says 47 and 17 for 64. A two-company drift on a linked-logo grid is
within normal counting tolerance and could be a genuine membership change since
the research pass, but the file should say "roughly 45" rather than a hard 47.

**The peer-association claim is confirmed and is undersold.** The International
Partners block names 25 peer fintech associations, and it is directly useful for
TXN's market roadmap: Fintech Poland (PL), Czech Fintech and APNU (CZ),
**Hungarian Fintech Association / Efisz (HU)**, Fintech Latvia, Fintech Lituania,
Finance Estonia, Fintech Bulgaria, AEFI (ES), Italia Fintech, Fintech Belgium,
Fintech Holland, France Fintech, Swedish Fintech Association, Fintech Norway,
UAFIC (UA), LHoFT (LU) and others.

Worth flagging to the client: **this block contains a Hungarian fintech
association**, which is a direct lead into the file's own worst-covered MVP
market. The file identifies the block's value in the abstract but does not spot
that it partly solves the Hungary gap.

### Copenhagen Fintech "Tech for Fin": CONFIRMED verbatim

This one mattered most because it was reported to the client as a literal
description of his target segment. It survives.

The programme description on `/startups` reads, word for word:

> "For future entrepreneurs and startups within other industries who would like to
> validate the problem-solution fit in fintech."

That is exactly what the file claims: founders from non-fintech industries moving
into fintech. The characterisation is accurate and the client-facing claim is
safe.

All five programmes confirmed (Mentor Program, Partnership Fast Track, Tech for
Fin, Incubation, Scaleup Partner). All four metrics confirmed: 630+ programme
alumni, 380+ Demo Day pitches, 90+ mentors, 5 programmes per year. No public
cohort roster confirmed.

Two small unsupported details: the page does **not** state a Lab capacity, so
"about 45 companies at a time" and "120+ cumulative Lab alumni" are not on this
page. And there are six case studies, not five (the file misses Safello, and
DoLand appears as DoLand/Valified).

---

## 2. Honesty of the blocked-source claims

Mostly honest, with one refutation and one significant miss.

| Source | File claims | My result | Verdict |
|---|---|---|---|
| Sifted `/leaderboards` | 403 | 403 | confirmed |
| Sifted `/rankings`, `/articles`, `/sitemap.xml`, article pages | (403) | 403, Cloudflare "Just a moment..." | confirmed |
| **Sifted homepage** | implied blocked | **200, 381KB** | overstated |
| **Sifted `/feed`** | not tried | **200, open RSS** | **significant miss** |
| EU-Startups `/directory/`, `/tag/weekly/`, `/` | 403 | 403 | confirmed |
| **EU-Startups `/feed/`** | not tried | **200, 104KB open RSS** | **significant miss** |
| StartupItalia | 403 | 403 on `/` and `/feed/` | confirmed |
| FinTech Futures | Cloudflare block | 403 on shortlist page and `/` | confirmed |
| MPE Berlin | 403 | 403 on both variants | confirmed |
| **Impact CEE** | "403 on both `/` and `/impact/2026`" | **200 on both, 287KB and 686KB** | **REFUTED** |
| ROTSA list page | 403 | 403 on all five list routes | confirmed |
| 4YFN `/exhibitors` | JS-rendered, zero names | zero names in static HTML | confirmed |
| paymentandbanking `/fintech-des-jahres/` | 404 | 404 | confirmed |
| therecursive `/podcast/` | 404 | 404 | confirmed |

### Sifted is reachable, by a route the researcher did not try

This is the finding the brief asked me to look hardest for, and it is real.

`https://sifted.eu/feed` returns **HTTP 200** and a well-formed RSS 2.0 feed. No
subscription, no browser session, no cookies. It carries titles, canonical URLs
and timestamps, and it was rebuilt at 14:42 GMT on the day of validation. The
items pulled today include exactly the artefact shape the client is asking for:

- "Serbian startups to watch, according to VCs"
- "The 10 robotics startups that raised the biggest rounds in H1 2026"
- "Lunar founders raise €8.2m to launch AI-native audit startup Repodo"

The first of those is a named-company CEE watch list, published the same day.

Caveat, stated plainly: the feed gives **titles and URLs, not article bodies**.
Individual article pages still 403 behind Cloudflare. So this is not full access
and it does not verify the leaderboard structure, the "Sifted 100" naming or the
paywall status, all of which remain search-snippet only and correctly marked
`Unverified`.

But it changes the operational conclusion materially. The file says Sifted "needs
an authenticated browser session or a Sifted Pro subscription" and should be "the
first thing re-verified in the next pass". In fact Sifted is already usable today
as a **monitoring signal**: poll `/feed`, match titles against list-shaped
patterns, and you get same-day notice of every Sifted list article. Against Ian's
stated design principle, that a deal should never be missed because nobody knew
it was on the street, a free polling feed on the client's own named reference
source is worth more than a note saying the site is blocked.

The identical pattern holds for **EU-Startups**: HTML 403 everywhere, `/feed/`
returns 200 with 104KB of live article titles.

### Impact CEE is not blocked

The file states 403 on both `https://impactcee.com/` and
`https://impactcee.com/impact/2026`. With a browser user agent both return **HTTP
200** with substantial content. The file's blocked-sources table does not claim a
curl attempt for this source (unlike Sifted and EU-Startups, where it explicitly
says curl was also tried), so this reads as an incomplete attempt rather than a
false statement. It is still a correctable gap.

Fetching it also corrects the entry's facts. The file reports Impact CEE as
"13-14 May 2026 at the Poznań Congress Center" from search snippets. The live
site shows **Impact'26 has already happened** ("thank you to every person who
participated in Impact'26") and advertises **Impact'27 on 12-13 May 2027**. The
forward-looking date in the file is wrong for outbound planning purposes.

---

## 3. Fabrication signatures: what I looked for and what I found

I checked specifically for the tells the brief named.

- **Invented events.** None. Every event in the entries I tested exists, ran, and
  has the URL claimed.
- **Fake newsletters.** None. Swedish Tech Weekly is real, weekly, correctly
  attributed to Martin Weigert, and issue 368 is dated the day before this
  validation.
- **URLs that 404.** None among the `Verified` entries. The only 404s in the file
  are ones it reports honestly as 404s, and I confirmed both
  (paymentandbanking.com/fintech-des-jahres/, therecursive.com/podcast/).
- **Counts that do not match the page.** **This is the real weakness.** Six
  wrong numbers across fourteen tested entries. See the correction list below.

**A note in the file's favour on honesty.** I stress-tested the file's own
self-reported caveats and they held every time:
- Infoshare: the file says the 2026 names (Beholder, Genotic, Green Sequest, SAY
  IT Labs, upLYFT) are Reported, not on the fetched page. Confirmed. Those names
  appear nowhere on that page. The file could easily have passed them off as
  verified and did not.
- Money Motion: the stale "Applications closed January 28th, 2025" caveat is real.
- Web Summit: pagination "1 2 3 4 5 … 27" confirmed exactly.
- Latitude59: 465 applicants from 53 countries and the €400k prize fund, both
  confirmed exactly.
- Finovate: the file says the fetched post named zero companies. Consistent with
  everything else I saw about its self-reporting.

An agent inventing research does not volunteer this many inconvenient caveats.
The pattern here is a researcher who fetched real pages and then got sloppy
counting and over-generalised from them, not one who made things up.

---

## 4. The error I found that nobody flagged: Latitude59

**PARTLY CONFIRMED, and the file understates the source by half.**

The file records "Approximate list size: 15-16 named in the TOP15 post" and adds
the observation "Note the post is titled TOP15 but lists 16."

That observation is wrong, and it is wrong in a traceable way. The page carries
**two** blocks: a TOP15 (15 companies) and a further **TOP30** block (15 more).
**The page names 30 companies, not 16.**

The 16 names the file lists are the 15 TOP15 companies plus **Pixit**, which
belongs to the TOP30 block. The researcher scooped one name across a block
boundary and then rationalised the off-by-one as a quirk of the page rather than
an error in the reading. The country tally in the file (Estonia 9, Lithuania 3,
Finland 2, Austria 1, Ukraine 1) is likewise inflated: the true TOP15 split is
Estonia 8, Lithuania 3, Finland 2, Austria 1, Ukraine 1.

The 15 companies the file misses entirely: Innoair, AtlasWiki, Snoika,
Polyatomic, B.O.R.I.S., AVEO TECH, Sort A Brick, Ennerio, RYTM, NeuroTech AI,
Supercomms, Monetily (LV), NoCFO (FI), Phishbite, Pixit.

This is an error that **costs the client**, because it halves a good source and
hides a Latvian entry that would have widened the country coverage.

---

## 5. Corrections required before this reaches the client

Ordered by how much they matter.

**Must fix, materially misleading:**

1. **Deloitte Fast 50 Central Europe does not cover Hungary.** Strike "all four
   MVP markets" at line 33-34 and line 560. It covers Poland, Czech Republic and
   Romania, three of four. This one would send Ian looking for Hungarian
   companies in a list that structurally cannot contain any.
2. **Latitude59 names 30 companies, not 15-16.** Remove the incorrect "titled
   TOP15 but lists 16" note, add the TOP30 tier, correct the country split to
   Estonia 8 / Lithuania 3 / Finland 2 / Austria 1 / Ukraine 1.
3. **Sifted is partly reachable now.** `https://sifted.eu/feed` returns an open
   RSS feed of titles and URLs, and the homepage returns 200 to a browser user
   agent. Reframe from "could not open, needs a subscription" to "article bodies
   are Cloudflare-blocked, but the RSS feed is open and is immediately usable as
   a same-day monitoring signal". Same correction applies to EU-Startups
   (`/feed/`, 200).
4. **Impact CEE is not blocked.** Both URLs return 200 to curl with a browser UA.
   Also correct the dates: Impact'26 has already run; the next edition is
   **12-13 May 2027**.

**Must fix, wrong numbers:**

5. **Money Motion:** 19 finalists to **18**; 64 cumulative to **63**. Add that
   unique cumulative is **61** because FraudShield and eFrontiers repeat across
   cohorts.
6. **The Hub:** 9,000+ to **11,113**. Add the Fintech filter count of **1,005**,
   which is the number that actually sizes the source.
7. **Swedish Tech Weekly:** drop "whole archive trivially enumerable" and "seven
   years of continuous back issues". The pattern works from roughly issue 250
   onward, about 120 issues. Issue 230 and below return 404.
8. **RoFintech:** 47 fintech members to **roughly 45** (62 total, not 64).
9. **Deloitte:** drop "27th edition", unsupported by the page.
10. **Vestbee:** "11 companies across 7 countries" should be **8 countries**. The
    file's own company list spans PL, EE, RO, CZ, LT, LV, SI, UA.

**Should fix, minor:**

11. **Cashless.pl:** the nominees page gives only "June 2026", not 18 June. Move
    the specific day to Reported alongside the map figures.
12. **Copenhagen Fintech:** the Lab capacity ("about 45 at a time", "120+ Lab
    alumni") is not on the fetched page. There are six case studies, not five.
13. **ROTSA:** the URL recorded as tried,
    `/en/list-of-technology-startups-in-romania/`, does not exist. The real paths
    are `/proiecte/lista_startup_tech/` and
    `/en/projects/listing-of-technology-startups-in-romania/`. All 403 anyway, so
    the finding stands, but the recorded evidence should cite a real URL.
14. **Money Motion:** the startups page says 700 companies / 3,500 professionals,
    where the file cites 3,000 attendees.

**Worth adding, found during validation:**

15. **RoFintech's International Partners block names a Hungarian fintech
    association (Efisz / Hungarian Fintech Association).** Given the file
    correctly identifies Hungary as its biggest hole, this is a concrete lead
    into that gap sitting inside a source the file already verified.

---

## 6. Overall trustworthiness

**Trust the sources. Check the numbers.**

Every source in this file that I tested is real, live, at the URL claimed, and
has the character described. Nothing was invented. The three claims the client is
most likely to act on, Money Motion's accreting archive, South Summit's free
100-name list, and Copenhagen Fintech's non-fintech-founder programme, all
survive validation, and the first and third survive it verbatim. The Romanian
awards find, which the file calls its best CEE result, is fully confirmed
including the exact five fintech nominees, and the StartupCafe substitution is
legitimate rather than a cover for weaker sourcing.

The file's self-reported failures are also genuine. I re-tested seven of them and
six were exactly as described. An agent fabricating research does not
volunteer that its own best-known reference source defeated it, nor flag five
company names as Reported when it could have quietly promoted them.

The failure mode here is arithmetic and over-generalisation, not invention. Six
wrong counts in fourteen entries is a high enough error rate that no specific
number in this file should be quoted to the client without a spot-check, and the
Deloitte Hungary claim and the Latitude59 undercount both need fixing before this
goes out. Fix the fourteen items above and this file is sound.

Fourteen `Verified` entries tested. Seven survived clean. Seven need a
correction. Zero were refuted as fabrications.
