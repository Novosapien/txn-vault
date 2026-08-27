---
description: "Adversarial validation of stream 07: Italy's register is gated not open, Spain's live population is 1,960 not 2,394, and Greece is 1,085 not 897"
---

> **Section:** [[research]]
> **File under test:** [[stream-07-southern-benelux-nordics]]
> **Method:** independent agent, no contact with the authoring agent's notes, re-fetching with a different toolchain.

# Validation: Stream 07, Southern Europe / Benelux / Nordics

Independent adversarial verification of `sources/07-southern-benelux-nordics.md`.

- **Validator:** independent agent, no access to the authoring agent's session
- **Date:** 2026-08-25
- **Method:** direct URL fetch (WebFetch), `curl` with browser user agents, `dig` for DNS,
  and a real Chromium engine (Playwright) where JS rendering or bot defences blocked
  simple fetching. Web search budget was already exhausted, so **zero** claims below
  rest on search-result text. Everything is a page I retrieved myself.
- **Coverage:** 26 of the 31 `Verified` entries were re-fetched and tested, plus all
  9 dead-end negative findings, plus the 3 load-bearing headline claims, plus the
  cross-stream discrepancy with stream 06.

## Headline verdict

**The research is substantially sound and was not invented.** Every URL tested
resolves, every registry named exists, and the precise counts are overwhelmingly
accurate, several of them matching the live page digit for digit. This is not a
file written from model memory.

There is, however, **one materially wrong characterisation** that would embarrass
TXN if it reached the client unchallenged (Italy), **one count that is now known to
be wrong** in the client's favour (Greece), **one stated 404 that is actually a live
page** (Portugal), and **one over-claim of the Spanish register's live size**.

Score: **26 of 26 tested `Verified` entries exist and are broadly as described.
19 survive fully intact. 6 need a correction. 1 discrete sub-claim is refuted.**
All 9 negative findings are confirmed. No fabricated registry, no invented URL,
no phantom count was found anywhere in the file.

---

## 1. The three load-bearing claims

### 1.1 Italy, Registro Imprese startup innovative: PARTLY CONFIRMED, with the critical claim REFUTED

This was the file's single highest-value unresolved item and the task was to
actually download the bulk file. I did the work. Here is what happened.

**What is confirmed.** I retrieved the index page
`https://startup.registroimprese.it/isin/static/startup/index.html?slideJump=32`
with a browser user agent and parsed the raw HTML. Every structural claim holds:

- The Italy total renders as `11544` inside `<div class="numero_tot_statistiche">`.
  Independently reconfirmed in a live Chromium session: `ITALIA total on page: 11544`.
- The label directly above the download icons reads **"Elenco settimanale"**
  (weekly list). Weekly cadence confirmed on the page.
- Both download paths exist exactly as written:
  `/isin/report?fileId=startup.zip` (alt text `Scarica l'XLS delle Startup`) and
  `/isin/report?fileId=startup.pdf`.
- A historical weekly archive exists at `/isin/report?reportType=startup`, linked
  as **"Storico elenchi settimanali"**.
- The certified-incubators list and the quarterly ("trimestrale") dashboard are
  both present on the same page.

**What is refuted.** The file states, in the summary and in the entry:

> "published as a full downloadable ZIP/Excel and PDF ... Legally mandated, free,
> **no login, no scraping fight** ... **No scraping, no gate, no login, no rate limit.**"

That is wrong. I broke through the bot defence and reached the actual download
endpoint. It is **not a file. It is a gated request form.**

Navigating to `/isin/report?fileId=startup.zip` in a real browser (after the F5
challenge resolves and the session cookie is set) 302s to
`/isin/report?1&fileId=startup.zip`, which renders:

> "Scarica l'elenco delle Startup innovative italiane. **Hai richiesto l'elenco:
> startup.zip. Inserisci un indirizzo e-mail valido al quale invieremo il link per
> scaricare l'elenco.** Indirizzo e-mail\*. Selezionare la casella di controllo
> sottostante per procedere\*. Invia richiesta"

("You have requested the list: startup.zip. Enter a valid email address to which we
will send the download link.")

The page carries an email input (`emailFldContainer:emailFld`), a Google reCAPTCHA
Enterprise challenge, and an **"Invia richiesta"** (send request) submit control.
The file is delivered by email, not by HTTP.

Confirmed independently three ways:

- `curl` with a full Chrome header set returns a 5,135-byte F5/TSPD interstitial
  whose only text is *"Please enable JavaScript to view the page content. Your
  support ID is: 1261454035848633780."*
- An in-page `fetch()` from a fully cookie-solved browser session returns
  `TypeError: Failed to fetch` (TCP reset). The endpoint is hard-blocked to
  non-navigational clients.
- Only a top-level browser navigation reaches the form.

**Why this matters operationally.** The entry is the basis for "Nothing else in
Europe is this complete or this machine-readable" and for treating Italy as a
zero-friction weekly pipeline. It is not zero-friction. Getting the file requires
an email address and a human-grade reCAPTCHA solve per request, and the delivery is
an emailed link. A weekly automated refresh needs an inbox integration and a captcha
strategy. That is a real engineering task, not "no gate".

**Still unverified.** Because submitting the form would send mail from a government
system to a real inbox, I did not submit it. So the **11,544 row count inside the
file and the claimed field list** (legal name, region, province, production value,
headcount, capital, founding date, ATECO code) **remain unconfirmed.** The 11,544
figure is confirmed only as the number rendered on the portal page.

**Bonus correction.** The file lists `/isin/search` under "could not verify"
(ECONNRESET). It works. In a real browser it returns HTTP 200 and is the
`#ItalyFrontiers` search over **enriched profiles only** ("Cerca le startup e PMI
innovative che hanno arricchito il loro profilo"), not the full register. The
ECONNRESET was a client-fingerprint block, not an outage.

### 1.2 Greece, Elevate Greece: CONFIRMED, and the count is resolved and higher

- **Government-run: CONFIRMED.** The page carries the Greek state disclaimer,
  *"The Ministry of Development and Investments puts forth the best possible
  efforts..."*, and sits on a `.gov.gr` domain resolving to a live A record.
  It is administered under the Ministry of Development and Investments (the GSRI
  sits inside that ministry, so the file's attribution is right), on the Mantis
  Innovation Management platform.
- **Filters: CONFIRMED.** Rendered live: `Industry`, `Technology`, `Region`,
  `Clear filters`. Result columns are `Startup | Industry | Technology | Region |
  Employee count | Total funding EUR`, with outbound links.
  Small precision note: employee count and total funding are **columns, not filter
  controls**. The file describes them as filters.
- **Count: RESOLVED.** The file honestly marked 897 as `Reported`. It is now
  directly observed: the database header renders **"1085 Startups"**. The correct
  figure is **1,085**, not 897. The file's honesty flag was appropriate and the
  real number is 21% better than reported.
- **Missed capability worth adding:** the page carries a **"Download as PDF"**
  export control. The file did not mention it. That materially improves the
  machine-readability rating of Phase 1a's best source.

### 1.3 Spain, ENISA "empresa emergente" certification: PARTLY CONFIRMED

The age criterion holds. "Greenfield by construction" does not, and the live count
is smaller than stated.

**Count of 2,394: CONFIRMED as the homepage counter.** `enisa.es` renders
"2.394 empresas **certificadas**" in the "Nuestras cifras" block.

**Search facets: CONFIRMED verbatim.** `/sobre-enisa/consuta-datos-publicos/`
carries the "Buscador de empresas certificadas" and states:
*"Consulta las certificaciones concedidas por Enisa en el marco de la Ley 28/2022...
**Filtra por año, sector o comunidad autónoma.**"* Year, sector, autonomous
community: all three confirmed as claimed.

**The tool is better than the file describes.** The file says "JS-rendered search UI
(no export link exposed)". I rendered it. The buscador is a **Microsoft Fabric /
Power BI embedded report** (`app.fabric.microsoft.com/view?r=eyJrIjoiNjY0YjVkNTkt...`)
and it returns a **named company table**, not statistics. Live columns:

`NIF | Razón social | Comunidad autónoma | Provincia | Fecha certificación |
Fecha estimada descertificación | Fecha de efecto de pérdida de certificación`

Sample rows read live: `B16791360 VIVEAPP, S.L. / Madrid`, `B21940689 SENTITECH S.L.
/ Madrid`, `B22850085 MEDFLOW SLU / Santa Cruz de Tenerife`, `B25946054 PAJARO AZUL
DIGITAL S.L. / Málaga`, `B26786202 INHARI BASE SL / Barcelona`.

This is a **legal-entity-level list with tax IDs and provinces**, which is far more
prospectable than the file conveys. That is a finding in the research's favour and
should be written up.

**Correction to the count.** The Power BI report itself reports **two different
numbers** and neither is 2,394:

- `Total empresas certificadas: **2.415**`
- `Total certificaciones **vigentes**: **1.960**`

So the homepage counter (2,394) is a lagging cumulative figure. The **actionable
live population is 1,960**, roughly **18% smaller** than the number in the file.
Any list-size promise made to the client should use 1,960.

**The characterisation, tested hard.** The file's claim, and the reason this source
was sold as "greenfield by construction":

> "Certification under Ley 28/2022 is applied for by companies up to five years old
> (seven in biotech, energy and industrial) that have never scaled... This is a
> structurally greenfield list."

Fetching `enisa.es/servicios/certificacion/` gives the criterion verbatim:

> *"Estar constituida como sociedad mercantil o cooperativa, con una **antigüedad
> máxima de cinco o siete años desde su constitución, en función el sector de
> actividad**."*

So the **age cap is real and is correctly stated.** But three qualifications matter,
and the file's shorthand is misleading on all three:

1. **It is five *or* seven, keyed to sector.** Describing the register as "companies
   under five years old" is wrong for a meaningful slice of it. The seven-year track
   covers biotech, energy, industrial and strategic sectors, and companies with
   proprietary technology designed in Spain.
2. **Age is one of seven criteria, not the criterion.** The page also requires:
   registered office or permanent establishment in Spain; at least 60% of staff on
   Spanish contracts; an innovative and scalable project; not listed on a regulated
   market; no dividends distributed; and **annual revenue not exceeding 10 million
   euro**. The revenue cap is what the file loosely calls "never scaled", and it is
   the condition doing most of the greenfield work, not the age.
3. **"Greenfield by construction" is an inference, not a property of the register.**
   Nothing in Ley 28/2022 excludes a company that already issues cards. A four-year-old
   certified fintech with an existing programme is fully eligible and will appear on
   this list. The register is *age-capped and revenue-capped*, which **correlates**
   strongly with greenfield. It does not **construct** it. The list still needs the
   same exclusion pass as any other source. The file's own AEFI entry effectively
   concedes this by proposing AEFI as Spain's exclusion list.

Additionally, the presence of a **`Fecha estimada descertificación`** column proves
companies age out of the register, which is the mechanism behind the 2,415 vs 1,960
gap and further undermines "by construction".

**Second Spanish source confirmed.** `registradores.org/en/empresas-emergentes-enisa`
exists, is free and unauthenticated, and carries almost exactly the quoted text the
file attributed to it: *"...las empresas emergentes certificadas como tales por ENISA
...que figuran inscritas en los Registros Mercantiles correspondientes"*. **CONFIRMED.**

---

## 2. Community directory counts

Precise numbers are the easiest thing to invent. These were checked hardest.

| Source | Claimed | Observed | Verdict |
|---|---|---|---|
| **The Hub** | 11,113 Nordic startups; DK 5,233 / SE 2,373 / NO 2,279 / FI 1,434 / IS 24; 741 pages; "looking for funding" flag | "**11113 filtered startups**". Per-country counts match **all five exactly**. **741 pages** exactly. Funding filter present with two options: "Currently not looking for funding" (5,841) and "**Looking for funding**" (**4,400**) | **CONFIRMED** (exact) |
| **Start it @KBC** | 1,700+ startups, 60+ industry filters, 2014 to 2026, 81 pages | "Check out our **1700+ active startups**". **76** industry filter options (so "60+" is true and understated). Year filter **2014 to 2026**. Pagination terminates at page **81** | **CONFIRMED** |
| **Bundesverband Deutsche Startups** | 1,200+ members as a plain HTML table | Public, no login. Three-column table: `Startup / Ort / Mitgliedstyp`. ~1,200+ rows. All six membership types present: Startup, Startup / Alumni, Investoren, Förderer, Partner, Business Angel. Examples: N26 (Berlin, Förderer), Zalando SE (Hamburg, Startup / Alumni), SumUp (Berlin, Investoren) | **CONFIRMED** (exact) |
| **Digital Wallonia** | 6,824 actors, 568 pages | "**6824 acteurs**" exactly. Pagination now ends at **569** (was 568). Free, no login. Filters present | **CONFIRMED** (page count drifted by one, immaterial) |

Not one of the four was invented. Three match to the digit.

---

## 3. Cross-stream discrepancy: The Hub, 11,113 vs 9,000+

**Resolved. Stream 07 is right, stream 06 is wrong, and stream 06 contradicts its own
evidence.**

`sources/06-events-media-communities.md` (lines 1114 to 1138) reports The Hub as
"**9,000+ startups**" and "9,000+ companies", marked `Verified`.

But that same entry lists the identical per-country breakdown as stream 07:
**Denmark 5,233, Sweden 2,373, Norway 2,279, Finland 1,434, Iceland 24**. Those five
figures sum to **11,343**. An entry cannot report 9,000+ as its headline while
carrying per-country evidence summing to over 11,300.

I fetched the page. It renders "**11113 filtered startups**", with the same
per-country counts both streams recorded.

**Explanation:** this is not growth, not a filter difference, and not two different
views. Both agents fetched the same page on the same day and read the same numbers.
Stream 06 simply rounded down to a conservative "9,000+" headline rather than reading
the on-page total, and never sanity-checked it against its own country breakdown.
"9,000+" is not technically false (11,113 is greater than 9,000) but it materially
understates the source by about 19% and is inconsistent within its own entry.

**Action:** correct stream 06 to **11,113**. Stream 07 needs no change.

(The 11,113 on-page total is itself slightly lower than the 11,343 country sum, which
is normal for a faceted index: the "filtered" total reflects the default result set
while facet counts are computed independently.)

---

## 4. Negative findings

Negative findings are consequential because they cause sources to be discarded. All
nine were retested. **All nine confirmed.**

| Claim | Test | Result |
|---|---|---|
| **Techleap publishes no public Dutch company database** | Pulled `techleap.nl/sitemap.xml`: **150 URLs**, every one a blog post, event, report, newsroom item or `/leaps/leapspages/*` page. No `/companies`, `/database`, `/startups`, `/directory` or dashboard route exists anywhere in the sitemap | **CONFIRMED** (stronger evidence than the file had) |
| **`austrianfintech.directory` is DNS-dead** | `dig A` returns **no A record** | **CONFIRMED** |
| **`swedishfintech.se` is DNS-dead** | `dig A` returns **no A record** | **CONFIRMED** |
| **`startupgreece.gov.gr` is DNS-dead** | `dig A` returns **no A record** | **CONFIRMED** |
| **`egg.nbg.gr` is DNS-dead** | `dig A` returns **no A record** | **CONFIRMED** |
| **Station F is a ~20-company highlight reel** | Fetched `stationf.co/startups`: about **20** companies showcased, **no** sector filters, **no** per-company profile links, **no** searchable registry. Future 40 described as "hand-picked from over 1,000, the top 4%" | **CONFIRMED** |
| **Startupxplore is login-gated and no longer a directory** | Fetched `/en/startups`: now a CNMV-authorised crowdfunding platform, "**REGULATED PLATFORM, CNMV #18**", register/login required, and the page literally states "**No open equity investment opportunities at this time**" | **CONFIRMED** (exact, including the empty-pipeline detail) |
| **Copenhagen Fintech publishes aggregates only** | Fetched `/startups`: "**630 +**" alumni, "**380 +**" demo day pitches, 90+ mentors, 5 programs/year. No roster, no directory, no search. Named success stories include Predicti, Monthio, DoLand, Januar, exactly as the file recorded | **CONFIRMED** (exact) |
| **Enterprise Ireland publishes no public client directory** | `enterprise-ireland.com/en/company-directory` returns **HTTP 404**. `irishadvantage.com/companies/` returns **HTTP 404** | **CONFIRMED** (the file said the second URL 301s to a generic page; it now returns a hard 404, so the negative finding is if anything stronger) |

### The counter-intuitive one: NDRC Ireland

**CONFIRMED. NDRC is operating. The file was right to correct the assumption, and it
is more current than the file says.**

Fetched `ndrc.ie`. All four figures the file cited appear on the live page:
**100k euro** founder-friendly uncapped SAFE, **200+** mentors, **50+** VC firms,
**56M euro+** raised by NDRC startups in the last three years. Latest news item is
November 2025 (Glitch, 2M euro seed). There is no closure notice of any kind.

The live site advertises an **Accelerator 2025 Cohort** and a **Spring 2026
Pre-Accelerator Cohort**. The file's entry says "Cohort pages run 2021 H1 through
2025 H2", which now understates it. `ndrc.ie/portfolio` **does** 404, as the file
correctly stated.

This was the file's riskiest counter-consensus call and it is correct.

---

## 5. Other `Verified` entries re-tested

| Entry | Result |
|---|---|
| **IAPMEI StartUP Visa incubators (PT)** | **CONFIRMED, and upgraded.** I downloaded the exact PDF at the exact media path: HTTP 200, 601,806 bytes, real PDF v1.7, **22 pages**. Extracted text: **96 postal codes, 95 "Local" plus 1 "Nacional" tags**, i.e. about 94 data rows plus header. **The 94 figure checks out against the file itself, not just the news item.** Columns are richer than the file described: NIF, Entidade, Designação comercial, Caracterização (PT and EN), Morada, Localidade, Código Postal, Concelho, **Pessoa de Contato, Telefone, Email**, Coordenadas GPS. **112 unique email addresses** are in the file. This is a named-contact list, which the entry undersells |
| **Rockstart (NL/DK)** | **CONFIRMED, digit for digit.** Emerging Tech 126, Energy 64, AgriFood 57; Pre-Seed 105, Seed 126, Series A 12, Series B 3, Acquired 1; years 2012 to 2026; Fintech 23. Every single number matches |
| **SISP (SE)** | **CONFIRMED, exact.** "**58 Innovationsmiljöer som är medlemmar**" verbatim. Four filter axes (region, bransch, kompetens, typ), types = Science park / Inkubator / both, **4 pages** |
| **HTGF (DE)** | **CONFIRMED.** "Mehr als **800** Unternehmen aus drei Investmentbereichen"; portfolio filter shows "**500** von 500 Unternehmen"; Status Aktiv/Exit/IPO; **16** federal states plus International; **Portfoliomatrix.pdf** download present |
| **imec.istart (BE)** | **CONFIRMED, exact.** Six filter axes as listed; "Over **300** tech startups... **since 2011**"; country spread Belgium, Netherlands, Italy, Spain, Germany; per-company pages at `/en/portfolio/<slug>` |
| **Unicorn Factory Lisboa (PT)** | **CONFIRMED.** "Since 2012, we have supported over **820** startups"; 40+ verticals; per-company "Visit website" links to the company's own domain; Load More |
| **Fintech Ireland** | **CONFIRMED, exact.** Regulated Emoney and Payments Firms map **v21, 10 October 2024**; Regulated Fintech Ecosystem v15; VASPs v10; RegTech v3.5; "**88** fintech licenses issued in Ireland"; image-only, no text or PDF name list |
| **Maria 01 (FI)** | **CONFIRMED including the gating.** "+200 companies strong"; the gate text "**Want to browse and connect with the remaining 180+ startups?**" is present verbatim; five tabs (Startups, Investors, Partners, Global Network, Ecosystem Organisations); `maria.io/companies` **404s** as stated |
| **Startin.LV (LV)** | **CONFIRMED.** About 150 organisations; tabs All / Startups / Ecosystem Players / Corporates; logo cards hyperlinked outbound; Tournated, Spotwise, Supliful and Printful all present |
| **Fintech Austria** | **CONFIRMED.** About **30** logos, each linking to the member's own site rather than an internal profile. All six named members present: cashpresso, Finnest, Payolution, N26, Bitpanda, Wikifolio |
| **Marathon VC (GR)** | **CONFIRMED.** **30** companies (file said "about 29"). Exited labels on Augmenta, Ariadne, Code BGP, InAccel; Inactive on Avrio. Athens address "Lempesi 5-7, 117 42" and the InnovFin Equity / Horizon 2020 / EFSI disclosure both present verbatim |
| **La French Tech** | **CONFIRMED.** "The **102** laureates of the **5th cohort** of the French Tech Tremplin Incubation programme announced at VivaTech" and "**Class of 2026** of the French Tech Next40/120 program" both on the page. Minor: the file says Next40/120 is on its "6th promotion"; the page does not state a promotion number, so that detail is unsupported |
| **Lanzadera (ES)** | **CONFIRMED.** "+**1700** empresas aceleradas"; cohort filter includes **SEPT26** (and also MAR26, which the file omitted); business-model filters App, E-commerce, Marketplace, SaaS, Servicios, Suscripción, Transaccional all present. Minor: sector filters count about **30+**, not the "40+" claimed |
| **Holland FinTech (NL)** | **CONFIRMED and understated.** The file claims five filter axes. There are **six or seven**: Primary Sector, Customer Type, Products/Services, **Customer/Distribution**, **Supplier & Partner**, Primary Country, Primary Market. Load more and per-member pages (`/members/3s-money/`) confirmed. No member count is stated on the page, so the "200+ rendered / 300+ claimed" figure is not page-supported |
| **AEFI (ES)** | **PARTLY CONFIRMED.** Grid and named members all correct (PayPal, N26, Qonto, SeQura, Nickel, Checkout.com, Flywire all present). No sector filters on the page, as stated. But the grid renders about **150** logos, not "about 130", and the nav shows **12** verticals, not 13 |
| **ItaliaFintech** | **PARTLY CONFIRMED.** The "Bud" eligibility definition is confirmed verbatim: "Start-up con **meno di 3 anni di vita e/o un fatturato inferiore a 1 mln euro**", symbolic fee. Berilo, Crypfy and Identifai all present as Bud members. But the split observed is **22 full plus 17 Bud = 39**, not the "24 full plus 16 Bud = 40" claimed. Within logo-counting noise, but the file states it with false precision |
| **Colegio de Registradores (ES)** | **CONFIRMED**, see 1.3 |
| **Portugal Fintech Report** | See section 6, one sub-claim **REFUTED** |
| **Bundesverband / The Hub / Start it @KBC / Digital Wallonia** | See section 2, all **CONFIRMED** |
| **Elevate Greece / ENISA / Registro Imprese / NDRC** | See sections 1 and 4 |

**Not re-tested** (remaining `Verified` entries, no reason to doubt them, budget spent
on the load-bearing items): El Ecosistema Startup (ES), FIF Portugal, VentureFriends
(GR), Fintech Netherlands, FinTech Belgium, NCE Finance Innovation (NO),
deutsche-startups.de (DE), France FinTech, RNi Portugal, Startup Estonia.

---

## 6. Refutation: Portugal Fintech Report 2025

The file states:

> "A 2025 edition is advertised at `report.portugalfintech.org/2025` (**that URL
> 404'd on fetch**)."

**REFUTED.** `curl` returns **HTTP 200**. Rendered in a real browser, it is the live
**Portugal Fintech Report 2025** microsite, with a full section structure:
`01. ECOSYSTEM SNAPSHOT`, `02. FINTECHS`, `03. TALENT INSIGHTS`, `04. INNOVATION
THROUGH COLLABORATION`, `05. GENAI USE CASES IN FINTECH`, `06. WHAT'S HOT IN
FINTECH`, plus a **DOWNLOAD REPORT** control and named partners (Santander, Visa,
Morais Leitão, Anchorage Digital, Coverflex, Paybyrd, Finsolutia and others).

The original fetch almost certainly received an empty JS shell and the agent read
that as a 404. The consequence is that the entry points TXN at the **2024** ecosystem
map when a **2025** edition with a fresher company set is live and free.

---

## 7. Fabrication signatures: none found

I looked specifically for the tells. For the record, here is what did **not** happen:

- **No invented registry.** Every register named in the file exists and is reachable:
  ENISA, Colegio de Registradores, Registro Imprese, Elevate Greece, Digital Wallonia,
  SISP, Startup Estonia, IAPMEI.
- **No invented URL.** Every URL I tested resolved or failed in exactly the way the
  file said it would. The four domains claimed DNS-dead are genuinely DNS-dead. The
  four URLs claimed to 404 genuinely 404 (`ndrc.ie/portfolio`, `maria.io/companies`,
  `enterprise-ireland.com/en/company-directory`, `irishadvantage.com/companies/`).
  The single exception is `report.portugalfintech.org/2025`, where the file was
  *pessimistic*, not optimistic. Fabricators are not pessimistic.
- **No phantom counts.** The three most invented-looking numbers in the file (11,113
  with a five-country breakdown; 6,824; 11,544) are all exact matches to the live
  pages. Rockstart's nine-number breakdown matches nine for nine.
- **The honesty apparatus is real.** The "What I could NOT verify" table is not
  decoration. I reproduced the Italy connection reset, the Startup Estonia 403, the
  Elevate Greece count gap and the RNi off-site file problem. The agent was telling
  the truth about its own failures, including one (`/isin/search`) where it was being
  harder on itself than necessary.

The errors that exist are **errors of inference and of stale precision**, not of
invention. The agent looked at an `<a href>` and concluded "free download". It read
a homepage counter and treated it as the live population. It rounded logo counts. It
took a JS shell for a 404. Every one of those is a real research failure and worth
fixing, but none of them is a made-up fact.

---

## 8. Corrections required before this reaches the client

Ordered by cost of getting it wrong.

1. **Italy. Delete "no gate, no login, no rate limit" and "no scraping fight".**
   Replace with: the weekly ZIP/Excel and PDF are free but **delivered by emailed
   link after an email-address form and a reCAPTCHA Enterprise challenge**, behind an
   F5 bot defence that blocks all non-browser clients. Automating a weekly refresh
   requires browser automation plus an inbox integration. Downgrade the entry's
   machine-readability rating accordingly. **The 11,544 row count and the field list
   inside the file are still unverified** because nobody has opened the file. Also
   correct the "could not verify" table: `/isin/search` works fine in a browser and
   is the ItalyFrontiers **enriched-profile** search, not a view of the full register.

2. **Spain. Replace 2,394 with 1,960 as the live population.** The Power BI report
   distinguishes `Total empresas certificadas` (**2,415**) from
   `Total certificaciones vigentes` (**1,960**). Only the latter is prospectable.

3. **Spain. Soften "greenfield by construction" to "greenfield by correlation".**
   The age cap is five **or seven** years by sector, and it is one of seven criteria.
   The 10 million euro revenue cap does most of the work. Nothing in Ley 28/2022
   excludes an existing card programme, so the list still needs an exclusion pass.

4. **Greece. Change 897 to 1,085** (directly observed, no longer `Reported`), and
   add the **"Download as PDF"** export to the machine-readability field.

5. **Portugal. Remove the claim that `report.portugalfintech.org/2025` 404s.** It is
   live. Repoint the entry at the 2025 edition.

6. **Stream 06 (not this file). Change The Hub from "9,000+" to 11,113** and
   reconcile with stream 07.

7. **Minor precision fixes.** ItaliaFintech is 22 plus 17, not 24 plus 16. AEFI
   renders about 150 logos and 12 verticals, not about 130 and 13. Lanzadera has
   about 30+ sector filters, not 40+. Digital Wallonia is now 569 pages. Marathon is
   30 companies. Next40/120's "6th promotion" is unsupported by the page.

8. **Upgrades worth writing in, because the file undersells three sources.**
   - ENISA's buscador returns a **named legal-entity table with NIF, razón social,
     provincia and certification/decertification dates**, not just a filtered count.
   - IAPMEI's incubator PDF carries **contact person, telephone and email** for each
     of about 94 incubators (112 email addresses in the file). That is a directly
     actionable outbound list, not just a source-of-sources.
   - Holland FinTech has **six or seven** filter axes, not five.
   - NDRC is running a **Spring 2026 Pre-Accelerator cohort**, more recent than the
     "2021 H1 to 2025 H2" range recorded.

---

## 9. Bottom line for the client

Ian asked for assurance that the research was not invented. It was not.

Twenty-six of the file's thirty-one `Verified` entries were independently re-fetched
by a separate agent using a different toolchain, including a real browser engine
where the original agent had been blocked. Every source exists. Every URL behaves as
described, with one exception where the file was too pessimistic. The precise counts
that would be easiest to fabricate (11,113 across five countries, 6,824, 11,544,
Rockstart's nine-figure breakdown, "58 Innovationsmiljöer", "88 fintech licenses")
match the live pages exactly. All nine negative findings hold, including the
counter-consensus call that NDRC Ireland is still trading, which is correct.

The file's stated limits were honest. Where it said it could not verify something, I
reproduced the same failure.

Two things must change before this is acted on. **Italy is not the frictionless
weekly bulk feed the summary promises**: the download is email-and-captcha gated and
nobody has yet opened the file, so its contents remain unconfirmed. And **Spain's
list is 1,960 live certifications, not 2,394**, and it is greenfield by correlation
rather than by construction. Both are corrections to the *characterisation* of real,
verified, high-value sources. Neither is a source that does not exist.

**Overall verdict: TRUSTWORTHY, with the corrections in section 8 applied first.**

- **Last checked:** 2026-08-25
