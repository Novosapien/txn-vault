---
description: "Router for TXN's four market profiles v2: the firmographic sourcing criteria, the ICPs each feeds, the exclusions and the gaps, revised after the 21 Oct call"
status: draft, 19 Oct 2026, split by sector; revised 21 Oct 2026 after the call with Ian
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
| **Feeds** | ICP 1, ICP 2, ICP 4 | ICP 1, ICP 2, ICP 4 | ICP 2, ICP 3, ICP 4 | ICP 3, ICP 2, ICP 4 |
| **Card relevance (Ian)** | Card-essential | Card-essential | Card-adjacent | Card-adjacent |
| **Geography** | EEA + UK, MVP countries first | Same | Same | Same |
| **Industries** | Banking, Financial Services | Financial Services, Software Development, Software Products | Financial Services, Credit Intermediation, Banking | Investment Management, Capital Markets, Financial Services, General Retail, Online and Mail Order Retail |
| **Verticals** | Consumer and business digital banking, crypto with fiat rails, banks (low priority for later) | Expense management, corporate and commercial cards, travel and expense, accounts payable | SMB lending, consumer lending, FX payments, payments, BaaS | Investment and trading apps, disbursement and payouts, retail, e-commerce and marketplaces |
| **Company types** | Private, Public; FinTech | Private, Public; FinTech, SaaS; b2b | Private, Public; FinTech | Private, Public; Marketplace, E-commerce, Retail, FinTech; b2c, b2b2c |
| **Headcount** | Any | Any | Any | Any |
| **Funding stage** | Any | Any | Any | Any |
| **Keywords** | 4 vertical groups | 4 vertical groups | 5 vertical groups | 4 vertical groups |

**Feeds.** Every vertical carries every ICP (Ian, 21 Oct L681-691: *"they are the same for every vertical"*). So each profile's search serves every ICP, and the ranking stage decides the ICP after the research. The Feeds row shows where each ICP can appear: ICP 1 only where the product needs a card (*"some verticals there'll be no ICP1s"*, L687), and ICP 3 only where it does not. All four ICPs carry the same vertical list, the union of the four profiles without traditional banks.

## Rulings of 21 October that land here

From the raw transcript in [[2026-10-21-icp-revision-outbound]].

- **The first pass is firmographic.** George described it (*"a neo bank that's based in um Bulgaria not based in Ukraine is between this size and that size"*, L461), and Ian restated it as *"very very very top of the potential funnel"* (L463).
- **Banks are a low priority for later.** Ian: *"They are definitely low priority... for later... we we need to get some scores on the board and some credibility before you're going to win with banks"* (L669). Every ICP carries the same bank line (George's decision D1): a traditional bank, not a digital bank or neobank, is graded D and kept on record.
- **Markets: two layers.** TXN can contract only with companies in Europe or the UK (L637). Every ICP carries this as an anti-signal that fires only on evidence (George's decision D4). Where the cards are issued is the BIN sponsor's decision (L641): published issuance outside Europe and the UK is a mark-down in each ICP's Tier 3, not an exclusion (L653), and the workforce does not try to identify the licensed issuer (L657).
- **Mastercard is not an exclusion** (L609, L613).
- **Marqeta clients are not all excluded.** Ian scores a company on its propensity to launch a card program, whether a card is live, who it is live with, and published problems with that incumbent (L563-573). His seven stay out as his own judgement (L573); other Marqeta clients are sourced and scored, with the incumbent weight in ICP 2 and ICP 4.
- **Early-stage companies.** Ian asked that sourcing not miss start-ups: funding rounds that the company or its investors announce, incubators, and companies talking to a card scheme (L519-533). Novosapien's reading: no scheme publishes who it talks to, so scheme leads come through TXN's own scheme relationships (*"we do have other channels for it"*, L523), not through the workforce, unless TXN passes the names in. Bootstrapped companies are *"pretty difficult"* to find, because *"it tends not to be too visible"* (L529).
- **Never lose a company.** *"As long as we don't lose anything that's been discounted... it's always a record there"* (L661-665).
- **Competitor LinkedIn tracking** was raised and parked by George (L509-513: *"that's a different conversation"*).

## Exclusions

Each profile ends with the same **Exclusions** section (decided by George, 19 Oct): the company types and named companies that a sourcing run leaves out, including the 15 companies Ian removed on 9 October. The seven Marqeta clients among them stay out as Ian's own judgement (21 Oct L573: *"I've discounted them as a human intervention"*) and stay on record. Other Marqeta clients are sourced and scored. Exclusions that need research (a staff-only card, insolvency, no company in Europe or the UK to contract with) stay in every ICP's anti-signals, so the ranking grades them D after the research and keeps them on record. Mastercard is no longer an exclusion. Published card issuance outside Europe and the UK is a mark-down in each ICP's Tier 3, not an exclusion.

## Gaps to settle

| Gap | Profile | Where |
|---|---|---|
| A bank with no card: ICP 1 or ICP 3? The priority is answered: low priority for later (Ian, 21 Oct L669) | P-1, P-3 | [[questions-for-ian]] Q4, answered in part. Matters when banks are revisited |
| The UK's place in the order | All | Q13 |
| Use cases beyond the twelve sub-sectors | P-3, P-4 | Q14 |
| BaaS: prospect or competitor category | P-3 | Q24 |
| Closed-loop cards | P-4 | Q22 |
| The extra verticals in P-2 (travel and expense, accounts payable), now in every ICP's verticals, and the software industries | P-2 | Our inference |
| Every keyword list | All | Not tested yet: run a free Prospeo search through Nova for each keyword before the first sourcing run |
