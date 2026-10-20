---
description: "Router for TXN's market profiles v2: the firmographic account selection criteria (geography, industries, verticals, company types, headcount, funding stage, keywords), split by sector into four profiles in their own files, with the ICPs each feeds and the gaps to settle"
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
