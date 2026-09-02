---
description: "Analysis of TXN's scored register v0.7: 126 accounts, tier and route distribution, and the maturity bias its own author confirmed and part-corrected on 02-09"
---

# Qualification Matrix (v0.7)

Analysis of `TXN_GTM_Qualification_Matrix_v0.7.xlsx`, delivered 25 August 2026. This is the register named in [[icp-definition]] §9.5, and the source of the "126 accounts" Ian referred to in [[2026-08-24-outbound-workforce-interview-1-offer|interview 1]]. The count is exactly 126.

> **Source of truth:** the workbook in the outbound folder. This page is analysis, not a mirror. Routed from [[outbound]].

## Structure

Fifteen tabs. `02_Scoring_Register` carries one row per account across 43 columns: 19 input columns, 10 auto-scored parameter columns matching [[icp-definition]] §8.1, then total, gating flag, anti-profile hit, tier and rationale. Scoring is formula-driven, not hand-entered.

`04_Triggers` holds 101 trigger events, `10_Watch_List` holds 21 pre-scoring early-stage candidates, and `09_Freshsales_Field_Map` carries 91 field mappings. Contacts, activities, meetings, suppression and audit tabs are scaffolded but empty.

## The workbook is ahead of the documents

Three input columns exist in v0.7 that [[icp-definition]] v0.4 does not describe: **Card Program Target Date**, **Timing Fit** (OK / Watch / Deferred) and **Card Program Category** (Consumer / Commercial and B2B / Disbursement and Payout / Vertical-specialist).

More significant: parameter **P7 Incumbent Processor now carries a "Planning to Launch (No Incumbent Yet)" band scoring 4 points**. ICP v0.4 §8.1.8 has no such band, and its DQ definition ("no card program and no stated plan to launch one") would place a greenfield company at zero. The workbook has already closed that gap. **ICP v0.4 is the document that is now stale, not the matrix.**

## What the register contains

| Tier | Accounts | Action per [[icp-definition]] §8.4 |
|------|----------|-----------------------------------|
| Priority 1 | 22 | ABM plus sustained tailored outbound |
| Priority 2 | 64 | LinkedIn and direct email |
| Priority 3 | 31 | No proactive campaigns |
| Disqualified | 9 | No activity |

Geography tracks the §4.4 phasing: 76 of 126 sit in the MVP markets (Poland 29, Romania 20, Czech Republic 18, Hungary 9), with the United Kingdom next at 18.

## Route distribution, and the effort mismatch

Route is not a column, but it is derivable from the Incumbent Processor input.

| Route | Accounts | P1 | P2 | P3 | DQ | Average score | P7 points |
|-------|---------:|---:|---:|---:|---:|--------------:|----------:|
| **1, greenfield** ("Planning to Launch") | 32 | 2 | 14 | 13 | 3 | **61.7** | 4 |
| **2 and 3, migration** (named or in-house incumbent) | 44 | 17 | 25 | 2 | 0 | **74.4** | 6 to 8 |
| Incumbent unknown | 32 | 3 | 24 | 5 | 0 | 67.3 | 3 |
| No card program, no plan | 18 | 0 | 1 | 11 | 6 | 46.4 | 0 |

**Migration accounts score 12.7 points higher on average than greenfield accounts, and take 17 of the 22 Tier 1 places.** Only 2 Tier 1 accounts are greenfield: PragmaGO (82) and BanqUP (89), both Polish.

Ian's position, established in the 25 August ICP interview, is that route 1 is where TXN wins first, because a company changing or adding a processor is unlikely to choose a platform with no market track record. Tier 1 receives ABM plus sustained tailored outbound. So **the most expensive motion is pointed at the accounts TXN is least likely to convert at launch**, and the route Ian named as first place holds 2 of 22 Tier 1 slots.

### Why it is not a one-parameter fix

P7 accounts for at most 4 points of the 12.7-point gap. The rest accumulates across P4 licence status, P9 scheme and BIN sponsor signal, and P10 card program scale, all of which reward a company that already runs a program at scale.

The scoring framework is, structurally, **a measure of card program maturity**. That is the correct thing to measure for fit, and it is exactly what makes it a poor proxy for near-term winnability, because maturity implies an incumbent and an incumbent implies the track record objection. See [[persona-champion]] §7, which lists that objection verbatim.

This does not make [[icp-definition]] wrong. Ian's distinction holds: an ICP states who the ideal customer is, and Trade Republic is an ideal customer whether or not TXN wins it this year. The gap is that tier drives effort allocation with no sequencing overlay, so a fit score is doing a job it was never meant to do.

## Ian reached the same conclusion independently

Prospecting v0.6 §4.1.5, dated 19 August, adds an early-stage watch list for pre-Series-A fintechs, with this rationale:

> *"...that would otherwise be missed by discovery weighted toward existing card programs."*

That is the same bias, named by its author six days before this session. The watch list is a partial answer: it catches pre-product companies before they reach the register at all (21 candidates, no auto-scoring, promoted on a defined trigger). It does not address the 32 greenfield companies already scored and sitting in Tier 2 and Tier 3.

## Confirmed by its author, 2 September 2026

The finding above was Novosapien's reading of a client document. It is not any more. On [[2026-09-02-outbound-workforce-icp-qualification]] Ian read back his own disqualification bands, without reference to this analysis, and rejected the one that produces the bias:

> *"it can't be a disqualifier that there's no signal that somebody is planning to launch a car[d] program."*

> *"green field companies often there are no public signals... How would we know? There's a could be a bunch of people planning to launch a car[d] program. We have absolutely no idea they're going to do it, but they fit squarely in verticals that we believe are use cases that are applicable."*

He also named the behaviour the framework produces, in the same terms this page used a week earlier:

> *"if the assumption is everybody that could ever launch a... card program or is considering launching a car[d] program has already... has a processor, that's obviously not correct."*

**And he inverted the ranking this register produces.** His one correction to the target matrix on that call:

> *"in a target vertical no evidence of a program no evidence in market is higher than has a program contract position open or or unknown."*

Against the v0.7 distribution above, that is a straight reversal. Greenfield averages 61.7 and holds 2 of 22 Priority 1 places; migration averages 74.4 and holds 17. Ian is asking for the first group to rank above at least part of the second.

**What this does not settle.** The gap is not one parameter, so withdrawing the P7 band does not close it: P7 is worth at most 4 points of the 12.7-point spread, and the remainder sits in licence status, scheme and BIN sponsor signal, and program scale, all of which still reward maturity. Ian withdrew the licence-status **gate**, not its points. So the register will still rank migration above greenfield after a straight application of his rulings, and the sequencing overlay this page proposed is still the thing that actually fixes it.

## Open questions this raises

| Question | Note |
|----------|------|
| Does sequencing get expressed as a Route field, or stay a judgement when working the list? | Route is derivable from Incumbent Processor today. It is not surfaced, and tier actions cannot see it |
| ~~Should the 18 "no card program, no plan" accounts be on the register?~~ | **Answered 02-09: yes, and none of them should have been scored DQ.** Ian rejected the §8.1.8 band outright. All 18 stay, and the 6 currently disqualified return to the working list |
| Does Timing Fit already carry the sequencing role? | 102 OK, 22 Watch, 2 Deferred. It sequences by *when* a program is due, not by which route the account arrives on |
| Should ICP v0.4 be reissued to match the workbook? | **Now overdue on two counts.** The P7 band, Timing Fit, Card Program Category and Card Program Target Date are live in v0.7 and undocumented in v0.4; and as of 02-09 three of v0.4's gating rules are withdrawn. Ian has said he will feed the session output back into the GTM documents. Tracked at [[open-questions]] #75 |
