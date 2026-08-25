---
description: "Delivery hub for the TXN engagement: flight plans carrying pilot status, workflow implementation state, the module ledger and the evidence behind each claim"
---

# TXN — Delivery

> **Index:** [[index]] · **Commercial:** [[commercial]] · **Components:** [[components]]

Delivery status for the engagement. Where [[commercial]] records what was sold and [[components]] records what is being built, this records **what is actually delivered**, reconciled from three independent sources: the code in the repositories, the promises in the proposals, and the decisions in this vault.

## Flight plans

New timestamped file every run. Previous versions stay in place: they are the audit trail and the diff baseline for the weekly review.

| Flight plan | Scope | Generated |
|-------------|-------|-----------|
| [flightplan-txn-2026-08-25-1007.html](flightplan-txn-2026-08-25-1007.html) | The pilot to 7 September, **plus four quarters of forward pipeline** (first issue to carry the quarter frame) | **25 Aug 2026, current** |
| [flightplan-txn-2026-08-18-1935.html](flightplan-txn-2026-08-18-1935.html) | Superseded. The six-week agentic pilot only | 18 Aug 2026 |
| [flightplan-txn-2026-08-14-1615.html](flightplan-txn-2026-08-14-1615.html) | Superseded | 14 Aug 2026 16:15 |
| [flightplan-txn-2026-08-14-1220.html](flightplan-txn-2026-08-14-1220.html) | Superseded the same day | 14 Aug 2026 12:20 |
| [flightplan-txn-2026-08-13-1640.html](flightplan-txn-2026-08-13-1640.html) | First issue | 13 Aug 2026 |

## Decisions

Decision records that sit outside the meeting series, kept here so the flight plan and the vault agree.

| Decision | Date | Record |
|----------|------|--------|
| **Workflow slate: TXN's ranked order and flagship pick.** Depth before breadth; decline investigation with the fix attached is the flagship. Clears the item that blocked forward workflow planning | 25 Aug 2026 | [[2026-08-25-workflow-slate-decision]] |

## What the current plan says

### The headline, 25 August

- **The pilot has run out of buffer.** **74%** of scope complete (range 70 to 78) against **71%** of the window elapsed, day 30 of 42, 13 days to completion. The margin was **+23 points on 14 August, +16 on 18 August, +3 today**. The pilot is not late and nothing contracted has been missed, but the comfort has gone, and it went in one week. This is the asymmetry behaving exactly as the last two issues predicted.
- **Build velocity has dropped sharply.** Across the four build repositories there have been **two substantive commits in seven days**. `txn-agentic-agent` has had no commit since 17 August, `txn-mcp-server` none since 11 August, `txn-mock-api` one lint fix. Against a mid-August week producing fifteen or more. Needs confirming as deliberate consolidation before UAT rather than capacity drawn elsewhere.
- **Approval stacking has landed**, and it was the main open item in the last issue. Two commits did it: 20 August *"HITL hand-off: the next gate arrives, answered cards stay answered"* and 24 August *"Acknowledge the click, hold the answer, and a browser harness that watches"*. The second also adds a browser test harness, which is the right instinct this close to UAT.
- **New risk: one engineer, now split across two engagements.** Every commit on all four build repositories since kickoff is George's. The 24 August outbound session additionally assigned him email configuration and domain warming for the Outbound Workforce ([[open-questions]] #57).
- **The TXN customer onboarding agent still has no code**, re-verified 25 August across all eight repositories: no repo, no branch, no module, zero open GitHub issues anywhere in the estate. It has been unstarted for the full six weeks. **This issue moves it into Q1 P1 position 2** and recommends agreeing its landing point with TXN rather than discovering the gap at acceptance.
- **The acceptance date is still not fixed in writing.** Carried from 18 August, now the single most overdue item ([[open-questions]] #54).

### The quarter frame, set this issue

Quarters are **launch anchored**: Q1 opens 8 September 2026, the day after pilot completion, and each runs three months. Set on 25 August, to hold stable, and not to move without TXN agreeing it in a weekly review.

| Quarter | Window | Character |
|---------|--------|-----------|
| Q1 | 8 Sep to 7 Dec 2026 | Delivery quarter: acceptance closeout, the customer onboarding agent, the wire-in build, the permission model |
| Q2 | 8 Dec 2026 to 7 Mar 2027 | Scale quarter: Phase 3 team, first client onboarding, hardening from real use |
| Q3 | 8 Mar to 7 Jun 2027 | Planning surface, no P1s by design |
| Q4 | 8 Jun to 7 Sep 2027 | Planning surface, a horizon rather than a plan |

**A commercial precondition on every Q1 commitment.** Only the pilot is papered, under a standalone Pilot Order. Everything in Q1 and beyond sits under the MSA, which [[commercial]] records as **drafted and under persona review, not signed**. If signature slips, the quarter slips with it, and that is a TXN-side action rather than a delivery risk.

### Carried forward, still true

- **All three Pilot Order deliverables are in scope.** The Full Agentic Experience and the Agent Access Layer are operational on simulation, with **six workflow SOPs** running end to end. The MCP surface is at **33 tools** since 11 August.
- **[[internal-ops-agents|Internal Ops v1]] is three line items**: knowledge engine **delivered** and in active client use, meeting capture **delivered** and running on this project (**18 meeting records**, most recent 24 August), and the **[[customer-onboarding|TXN customer onboarding agent]] not started**.
- **Note on the word onboarding.** Three different things carry the name. Internal Ops part 3 is **onboarding a customer onto TXN**, the commercial process run when a client commits. It is not [[guided-onboarding]] (the in-product co-pilot journey), and not cardholder onboarding on the workflow slate.
- **Two pieces of work are routinely confused.** Sprint Zero (£17,500, delivered) is the requirements effort for the whole project and produced this vault. The **Control Center React build** is separate, and appears in **no priced stage of any proposal**.
- **The candidate slate decision has come back (25-08).** Recorded in full at [[2026-08-25-workflow-slate-decision]]. Michael has ranked all ten with the principle **depth before breadth**, and named **decline investigation with the fix attached** as the flagship build: highest daily volume, half of it already runs as `investigate-declines`, no external dependency, and the fix half reuses the spend-control workflow. TXN has written **journey documents for all thirteen workflows** and will confirm endpoints and approval gates through the following week. **Candidates 8, 9 and 10, previously Novosapien concepts TXN had not asked for, are now TXN-ranked work.** Two things remain open: TXN ranked all ten and parked none, so there is no cut line, and Michael frames the work as being *"in the pilot"*, which needs the landing point confirming since the pilot definition is frozen and completes 7 September.
- **Workflow slate alignment is now more pressing.** The slate describes three workflows as operational; the implemented set is six SOPs and differs (cardholder onboarding is not implemented at all, lost or stolen is partial). **TXN is writing journey documents against those descriptions**, so the alignment action has moved from tidy-up to something that should happen before their documents are finished.
- **Permission model still deferred.** Named in Pilot Order deliverable 2, no commit on `txn-mcp-server` since 11 August. Moved to Q1 P1 position 4.

### Scope added inside the launch window

The 24 August outbound session assigned **George** email configuration and domain warming for the Outbound Workforce, plus a session with Jacob. Assessed under the scope-add protocol in the current flight plan: it carries no direct structural risk to the pilot codebase, but it costs attention at the point attention is scarcest. **Recommendation: take the discovery session with Jacob now, hold the domain setup and warming until after 7 September.** Nothing in the agreed launch sequence needs it sooner, since outbound cannot send before the market announcement.

## Corrections this plan makes to the vault

| Vault record | What the code shows | Action |
|--------------|--------------------|--------|
| [[open-questions]] #32 said the pilot mock API runs on the 29 May YAML | The mock moved to the **External contract on 10 August** and now carries `api-specification_10Aug2026.yaml`, 67 paths and 98 operations, with a spec-pull pipeline | **Done 25-08.** Flagged on 18-08 and left uncorrected for a week; register row now carries the correction and is narrowed to the partner question |
| [[vision]] states in five places that TXN does not hold balances in MVP and every authorisation is a pass-through | Ian, 24-08: *"it's both, not an either or"*. There are occasions where TXN authorises against a balance it holds | **Open.** New register row #55. Load bearing: it is the stated premise for scoping [[fraud-risk-assist]] as advise, don't decide. Confirm with Ian before correcting [[vision]] |
| [[architecture]] does not record the multi-tenancy risk | Shared architectural components mean one client flooding the system can affect others. Ian, 24-08: *"Yes, we believe there still is a risk"* | **Open.** New register row #56 |
| [[commercial]] records the Outbound Workforce as deferred to a later phase (13-08) | It is actively starting: domains being scoped, 126 accounts in play, George assigned | **Done 25-08.** [[commercial]] corrected |

## Reporting cadence

Agreed with Dorte on 18 August: **the flight plan goes to TXN at the end of each week**, not every couple of days, since little changes across two days. Novosapien runs it daily internally to watch percentage completion against duration and catch stuck line items.

## Sources

Reconciled at generation from: nine GitHub repositories (`txn-vault` 101 commits, `txn-console-react` 260, `txn-mock-api` 47, `txn-agentic-agent` 41, `txn-mcp-server` 25, `txn-admin-panel` 25, `txn-admin-api` 11, `txn-vault-mcp` 2, and `ICP-site` 3, which carries the Content Workforce ICP walkthrough; 515 commits in total), the proposals in [[commercial]], and this vault. The workflow candidate slate lives in the shared folder as `txn-workflow-candidates.pdf`.
