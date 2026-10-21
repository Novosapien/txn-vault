---
description: "Router for TXN's four market profiles v2: the firmographic criteria for the first sourcing pass, the ICPs each feeds, and Ian's rulings of 21 October"
status: draft, 19 Oct 2026, split by sector
---

# TXN market profiles (v2)

> **What this is.** The firmographic criteria that we source leads with: our answer to Ian's question of 9 October, *"What are the criteria used for each of the categories to search for matching accounts?"* The workforce then researches each company and ranks it against the ICPs (the categories). Card program status (no card yet, live card, switching) is not here: no lead source holds it, so the ICPs decide it after the research.
>
> **The split.** By sector only, following TXN's own Core Messaging: *"the primary segmentation axis is sub-sector, not company stage"* (`source-documents/core-messaging.md:68`). Each sector sits in one profile. No profile filters on funding stage or company size, so a company that fits is never dropped for missing data. (The first v2 draft split by funding stage; that split had no source and was removed on 19 Oct.)
>
> **The attributes.** Each profile uses the same seven: geography, industries, verticals, company types, headcount, funding stage, keywords. They are provider-neutral. The industry and company-type values are written as Prospeo values, because Nova sources from Prospeo. The product does not hold market profiles yet (IDEA-0003-CO in the Outbound Workforce vault), so today Nova reads the ICP text.
>
> **Guides, not strict filters (George, 20 Oct).** Geography, company types and keywords guide the sourcing agent: it may drop, add or change terms, search by where a company operates rather than only by its HQ, and widen a search that returns too few fitting companies. Headcount and funding stage are Any. Only the Exclusions are strict. Nova today applies every stated dimension as a strict filter, so a profile must say this in words.
>
> **Tags.** `[Ian]` = Ian ruled it, with the place. `[TXN]` = TXN's own documents. `[Derived]` = our inference, for Ian to confirm. `[Gap]` = not known yet.

> [!important] Ian confirmed the sourcing role, and two rulings land here (21-10-2026)
> **The split these profiles exist for is now confirmed by Ian** ([[2026-10-21-icp-revision-outbound]]). The first pass is firmographic only, *"a neobank that's based in Bulgaria, not based in Ukraine, is between this size and that size"*, which Ian restated as *"very very very top of the potential funnel"*. The ICPs are applied afterwards, when a researched company is sorted and graded.
>
> **Every vertical carries every ICP.** *"If the ICP and status are the same thing, then my argument is they are the same for every vertical."* The consequence is a property of the data, not a rule to encode: *"some verticals there'll be no ICP 1s, because that vertical doesn't contain any companies where a card program is essential. Meaning that you then go down and follow the list through two, three, four."* So the same search criteria run for every profile, and the ranking stage decides the ICP.
>
> **Geography is two separate layers.** TXN *"can only contract with companies that are in Europe or the UK"*. Where cards may be issued is not TXN's to decide: *"it's determined by a BIN sponsor"*. A company publishing that it issues for the Middle East, Africa or Asia is **marked down, not excluded**, and nobody chases the licensed issuer: *"for the level of complexity that might be involved... I think we can pass on that"*.
>
> **Banks are sourced but not loaded.** *"They are definitely low priority for later... we need to get some scores on the board and some credibility before you're going to win with banks."*
>
> **Early-stage sourcing, answering his own 9 October ask.** *"If you're a startup, the first thing you do is you go and get money."* So the channels are **funding rounds** announced by the company or its investors, **incubators**, and **the card schemes**, since *"somebody's talking to a card scheme if they're thinking about launching a card program"*. Bootstrapped companies are effectively out of reach: *"it tends not to be too visible."* See [[discovery-sources]].
>
> **Two new sources were raised and parked:** competitor LinkedIn tracking, pulling in the people who like and comment on a competitor's posts as warmer leads, and **job postings**, with Brett suggesting a commercial arrangement with a job board for API access. George framed the second as a test of Novosapien's own progression, *"we start pure human, then human with AI, then just AI"*.
>
> **Still to do, and the biggest piece of work from the call.** George expects *"only minor minor tweaks"* to the ICPs and personas, but *"the market profiles might be the ones where that's worth looking at a little bit more... just picking out some things that might be key red flags."*

## The profiles

- [[market-profile-1-digital-banking|P-1 Digital banking]]
- [[market-profile-2-commercial-card-expense|P-2 Commercial card and expense management]]
- [[market-profile-3-lending-fx-embedded-finance|P-3 Lending, FX and embedded finance]]
- [[market-profile-4-card-adjacent|P-4 Card-adjacent businesses]]

## Summary

| | P-1 Digital banking | P-2 Commercial card and expense | P-3 Lending, FX and embedded finance | P-4 Card-adjacent |
|---|---|---|---|---|
| **Feeds** | ICP 1, ICP 2 (ICP 4) | ICP 1, ICP 2 (ICP 4) | ICP 2, ICP 3 (ICP 4) | ICP 3 (ICP 2 if a card is live) |
| **Card relevance (Ian)** | Card-essential | Card-essential | Card-adjacent | Card-adjacent |
| **Geography** | EEA + UK, MVP countries first | Same | Same | Same |
| **Industries** | Banking, Financial Services | Financial Services, Software Development, Software Products | Financial Services, Credit Intermediation, Banking | Investment Management, Capital Markets, Financial Services, General Retail, Online and Mail Order Retail |
| **Verticals** | Consumer and business digital banking, crypto with fiat rails, banks (pending Ian) | Expense management, corporate and commercial cards, travel and expense, accounts payable | SMB lending, consumer lending, FX payments, payments, BaaS | Investment and trading apps, disbursement and payouts, retail, e-commerce and marketplaces |
| **Company types** | Private, Public; FinTech | Private, Public; FinTech, SaaS; b2b | Private, Public; FinTech | Private, Public; Marketplace, E-commerce, Retail, FinTech; b2c, b2b2c |
| **Headcount** | Any | Any | Any | Any |
| **Funding stage** | Any | Any | Any | Any |
| **Keywords** | 4 vertical groups | 4 vertical groups | 5 vertical groups | 4 vertical groups |

## Exclusions

Each profile ends with the same **Exclusions** section (decided by George, 19 Oct): the company types and named companies that a sourcing run leaves out, including the 15 companies Ian removed on 9 October. Exclusions that need research (Mastercard-only programs, programs that serve Asia or Ukraine, staff-only cards, insolvency) stay in every ICP's anti-signals, so the ranking blocks them after the research.

## Gaps to settle

| Gap | Profile | Where |
|---|---|---|
| Banks as targets; is a bank with no card a first-program target? | P-1, P-3 | [[questions-for-ian]] Q4 |
| The UK's place in the order | All | Q13 |
| Markets besides Asia and Ukraine that TXN does not support | All | Q3 |
| Use cases beyond the twelve sub-sectors | P-3, P-4 | Q14 |
| BaaS: prospect or competitor category | P-3 | Q24 |
| Closed-loop cards | P-4 | Q22 |
| The extra verticals in P-2 (travel and expense, accounts payable) and the software industries | P-2 | Our inference |
| Every keyword list | All | Not tested yet: run a free Prospeo search through Nova for each keyword before the first sourcing run |
