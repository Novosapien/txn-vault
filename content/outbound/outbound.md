---
description: "Outbound Workforce engagement: TXN's own GTM corpus, the three routes to a client, the ICP and persona reconciliation, and the interview series"
---

# Outbound Workforce

Novosapien's Cold Outreach Workforce configuration for TXN, and the home for TXN's own go-to-market corpus that it grounds on.

The distinguishing fact of this engagement: **TXN arrived with GTM material already written.** Ian Johnson authored an ICP definition, a prospecting process, and three persona scaffolds between April and July 2026. The onboarding work is therefore reconciliation and enhancement, not authoring from scratch.

## Documents

| Document | Description | Status |
|----------|------------|--------|
| [[icp-definition]] | TXN's ICP v0.4: firmographics, triggers, anti-profile, ten-parameter scoring, tiering, Named Account List method | Client-authored, 13-07-2026. The fit authority, but **now behind the workbook** |
| [[prospecting-process]] | TXN's seven-stage prospecting process, four discovery sub-scans, the early-stage watch list, Freshsales model, phased rollout | Client-authored, **v0.6**, 19-08-2026 |
| [[qualification-matrix]] | Analysis of the scored register v0.7: 126 accounts, tier and route distribution, and the maturity bias in the scoring | Novosapien analysis, 25-08-2026 |
| [[discovery-sources]] | Validated discovery sources for the greenfield segment: what survived adversarial checking, coverage by market, build requirements | Novosapien research, 25-08-2026 |
| [[persona-champion]] | CPO. Contributor, no veto. Owns Product Enablement | Client-authored scaffold, v0.1 |
| [[persona-primary-user]] | CTO. Approver with technical veto. Owns Technical Control | Client-authored scaffold, v0.1 |
| [[persona-economic-buyer]] | CFO primary, CEO or Founder secondary. Owns Commercial Model | Client-authored scaffold, v0.1 |

## Sub-sections

| Section | Contents |
|---------|----------|
| [[source-documents]] | TXN's own GTM corpus as Ian delivered it on 24 August 2026. Every original file, plus verbatim markdown mirrors of the eight documents that had no other home in the vault: Core Messaging v2.5, JV Messaging Framework v2.2, Competitive Landscape v0.2, Objection Handling v1.1, Product Overview v1.0, Outbound Content Playbook v1.0, AI Target Outcomes Framework v1.0, and the Role-Based Messaging deck |
| [[research]] | The working corpus behind [[discovery-sources]]: eight research streams holding 299 source entries, seven independent adversarial validation reports, and the client-facing register |

The seven documents previously recorded here as unmirrored are now mirrored, and every original Ian sent is held under [[source-documents]]. That directory is the source of truth for what the client actually delivered; the documents in the table above are the vault's working versions.

**Original source folder:** `programming/txn/outbound`, mirrored at `shared/clients/txn/outbound`. Delivered by Ian 24 August 2026.

## The three routes to a client

Established by Ian in the ICP interview on 25 August 2026. Every prospect arrives by one of three routes, and they are not variations of one motion.

| Route | Description | Dominant pain |
|-------|-------------|---------------|
| **1. No incumbent** | Has never issued a card program. Splits underneath into card-as-core-product and card-as-value-add | **Exposure.** Never done this, does not know what it does not know |
| **2. Next product elsewhere** | Already live with an incumbent, deliberately placing its *next* product with someone else. Drivers: regional coverage, product capability | **Constraint.** Not unhappy, specifically unable |
| **3. Full switch** | Moving every product across to a new processor | **Entrapment.** Cumulative dissatisfaction, blocked by migration risk |

### Route 1 leads, and the reason is track record

Ian, 25-08: *"Changing or adding a processor is not a small undertaking. So if you're going to do that, it's highly unlikely that you're going to do that with somebody that has no market track record. You're much more likely to do that if you are launching a card programme for the very first time."* Asked which route TXN wins first: *"undoubtedly number 1."*

Note the wording covers *changing or adding*, so route 2 takes the same hit as route 3, only softer. Routes 2 and 3 become winnable as a function of reference customers, not product capability. That is a sequencing rule, not a preference.

### Sequencing is not fit

Ian, 25-08, correcting an earlier framing in this engagement: an ICP is who the ideal customer is; targeting order is who you go after first. They are different questions. Trade Republic, currently with Marqeta, is an ideal customer on fit and Ian would want to win it. It is not a first-wave target. ICP v0.4 weights launching and migrating equally, and that is **correct as a fit statement**. It does not conflict with route 1 leading.

## The reconciliation

Two models are in play and they use the same words for different objects.

| | TXN's model | Cold Outreach Workforce model |
|---|---|---|
| **ICP** | A fit definition. One ICP, scored on ten parameters to 100 points | The messaging and grading unit. Each carries one dominant pain distinct from the others |
| **Personas** | A DACI buying group spanning the whole ICP | Children of exactly one ICP, 1 to 5 each, weighted to the economic buyer |
| **Grading** | Ten parameters, 100 points, Tier 1 at 80+ | Tier 1 business type 50%, Tier 2 business model 30%, Tier 3 firmographics 20%, grade A at 70%+ |

**Proposed resolution.** [[icp-definition]] stays the single fit authority and scoring engine, untouched. Two workforce ICP records sit beneath it, one greenfield and one migration, both inheriting v0.4's firmographics, anti-profile and scoring, differing only in dominant pain, messaging and which persona leads. Sequencing is expressed as an overlay rather than a score.

### The gap that needs closing

Discovery separates the routes: [[prospecting-process]] §4.1.3 runs four sub-scans, where sub-scan 2 (use-case-primary) surfaces greenfield companies and sub-scan 3 (incumbent-customer) surfaces migration candidates. The use-case lens was added precisely for this, citing **Trade Republic pre-Marqeta** as the canonical case of a fit company invisible to a card-signal filter.

Scoring then merges the routes back together, and tier actions cannot distinguish them. So a Tier 1 greenfield launch and a Tier 1 Trade Republic receive the same ABM treatment, and the sequencing decision has nowhere to live.

**The register quantifies the effect.** Greenfield accounts average 61.7 points against 74.4 for migration accounts, and migration takes 17 of the 22 Tier 1 places. Full working at [[qualification-matrix]]. The gap is not one parameter: P7 accounts for at most 4 points of the 12.7, with the rest spread across licence status, BIN sponsor signal and program scale. The framework measures **card program maturity**, which is right for fit and a poor proxy for near-term winnability, because maturity implies an incumbent and an incumbent implies the track record objection.

**Proposed fix:** surface Route as a derived attribute (launch / new product / full switch). It already exists implicitly in the Incumbent Processor input, so this is derivation and exposure rather than new data capture. Carry it into Freshsales and use it to order outreach *within* tier. The score is untouched and fit is untouched.

Ian named this bias himself in [[prospecting-process]] §4.1.5, dated 19 August, when adding the early-stage watch list for companies *"that would otherwise be missed by discovery weighted toward existing card programs."* The watch list catches pre-product companies before they reach the register; it does not reach the 32 greenfield accounts already scored into Tier 2 and Tier 3.

## Persona scaffolds: what carries and what is missing

All three documents describe themselves as *"Initial scaffold"* in their own Document Control. They are the base layer, to be enhanced into the workforce's 12-section structure rather than replaced.

**Carries across:** role mapping, the DACI authority model (cleaner than the workforce template's own), pains already written in first-person question form, objections (the strongest section in all three), messaging pillars, example copy, equivalent job titles.

**Missing, to be built:** archetype name, psychographic profile, day in the life, the deepest fear, what they have already tried and why it disappointed, persona-level trigger events, and information diet and trusted voices. That last one is the operationally expensive gap, because it decides channel, timing and which publication to cite.

**Not yet documented:** Head of Payments (operational viability) and Risk & Compliance. Both are profiled in Role-Based Messaging and all three scaffolds lean on them, so they are load-bearing absences.

### The incumbent assumption

Every persona scaffold is written assuming an incumbent exists. [[persona-champion]] §3.3: *"They have the most to gain from moving off an incumbent processor."* [[persona-economic-buyer]] §4 seeks *"a competitive total cost of ownership versus the incumbent"* and §6 asks for margin impact *"compared like-for-like to the incumbent."* [[persona-primary-user]] §2 frames the outcome as *"a long-term partner or a migration target."*

For route 1 there is no incumbent, no current spend, and no like-for-like comparison, so the Economic Buyer's evaluation frame has nothing to sit on. The scaffolds need a greenfield variant before route 1 outbound can run.

Related: [[persona-champion]] §7 lists the objection *"What is your track record with similar products and use cases? Show me three references in our vertical."* That is the objection TXN cannot currently answer, and it is the same constraint that puts route 1 first.

## Interview series

| Date | Session | Record | Status |
|------|---------|--------|--------|
| 24-08-2026 | Interview 1, the Offer | [[2026-08-24-outbound-workforce-interview-1-offer]] | Partially extracted; positioning held |
| 25-08-2026 | Interview 2, the ICPs | This page | In progress |
| 27-08-2026 | Interview 3, the Personas | Not yet held | Scheduled |

Positioning material from interview 1 (tagline, value proposition) is deliberately held until the series closes, so it lands as one piece rather than in fragments.

## Open items

| Item | Needs | Who |
|------|-------|-----|
| ~~The scored register of the 126 accounts~~ | **Delivered 25-08 as v0.7.** Analysis at [[qualification-matrix]] | Closed |
| Reissue [[icp-definition]] to match the workbook: the P7 "Planning to Launch" band, Timing Fit, Card Program Category, Card Program Target Date are all live in v0.7 and undocumented in v0.4 | A version bump | Ian |
| Route attribute decision: is sequencing carried as a derived field | A decision | Ian |
| Whether the 18 "no card program, no plan" accounts belong on the register at all | A decision. [[icp-definition]] §8.1.8 scores them DQ but P7 is not a gating parameter, so 12 survive as Priority 2 and 3 | Ian |
| Greenfield variants of the three persona scaffolds | Interview 3 | Both |
| Head of Payments and Risk & Compliance personas | Decision on whether they get standalone documents | Ian |
| Route 2 worked examples: who moved a next product, and what the incumbent could not do | Ian's recall or records | Ian |
| Whether BIN lookup resolves reliably across Europe as a research signal | Research | Novosapien |
| Reconciling this corpus's sequencing rules with [[commercial]], which records outbound as sequenced behind the launch | Both, once the series closes | Both |
