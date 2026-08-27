---
description: "Delivery hub for the TXN engagement: flight plans carrying pilot status, workflow implementation state, the module ledger and the evidence behind each claim"
---

# TXN — Delivery

> **Index:** [[index]] · **Commercial:** [[commercial]] · **Components:** [[components]]

Delivery status for the engagement. Where [[commercial]] records what was sold and [[components]] records what is being built, this records **what is actually delivered**, reconciled from three independent sources: the code in the repositories, the promises in the proposals, and the decisions in this vault.

## Flight plans

**One file per date**, named `flightplan-txn-YYYY-MM-DD.html`. Revisions on the same day update that day's file in place. Previous **dates** stay in place: they are the audit trail and the diff baseline for the weekly review. _(Convention set 25-08. Files dated before then carry a time suffix and are left as they are, since renaming would collide on 14 August and rewrite the audit trail.)_

| Flight plan | Scope | Generated |
|-------------|-------|-----------|
| [flightplan-txn-2026-08-27.html](flightplan-txn-2026-08-27.html) | **Six pages.** Carries the **workflow-slate build** (13 SOPs, 43 tools, 19 gated writes), the corrected Content Workforce schedule, and the **Stackworkz code-sharing** session | **27 Aug 2026, current** |
| [flightplan-txn-2026-08-26.html](flightplan-txn-2026-08-26.html) | Superseded. First six-page issue: the four pilot pages plus **Content Workforce** and **Outbound Workforce**. Its commit cut-off was 21 August, so it predates the slate build | 26 Aug 2026 |
| [flightplan-txn-2026-08-25.html](flightplan-txn-2026-08-25.html) | Superseded. The six-week pilot to 7 September. Four pages: Home, Pilot Release, **Workflow Status** (carrying TXN's ranked slate decision), Module Ledger | 25 Aug 2026 |
| [flightplan-txn-2026-08-21-1110.html](flightplan-txn-2026-08-21-1110.html) | Superseded. Issued before TXN's slate decision arrived | 21 Aug 2026 |
| [flightplan-txn-2026-08-19-1540.html](flightplan-txn-2026-08-19-1540.html) | Superseded. Added the parked-candidates section | 19 Aug 2026 15:40 |
| [flightplan-txn-2026-08-19-1305.html](flightplan-txn-2026-08-19-1305.html) | Superseded the same day | 19 Aug 2026 13:05 |
| [flightplan-txn-2026-08-18-1935.html](flightplan-txn-2026-08-18-1935.html) | Superseded. The six-week agentic pilot only | 18 Aug 2026 |
| [flightplan-txn-2026-08-14-1615.html](flightplan-txn-2026-08-14-1615.html) | Superseded | 14 Aug 2026 16:15 |
| [flightplan-txn-2026-08-14-1220.html](flightplan-txn-2026-08-14-1220.html) | Superseded the same day | 14 Aug 2026 12:20 |
| [flightplan-txn-2026-08-13-1640.html](flightplan-txn-2026-08-13-1640.html) | First issue | 13 Aug 2026 |

## Scope of the flight plan

From 26 August the plan covers **three engagements**, not one. The four pilot pages remain the agentic layer only. Two further pages track the GTM workforces, which are contracted separately and run in parallel:

| Page | Engagement | How progress is measured |
|------|-----------|-------------------------|
| Content Workforce | GTM Workforces proposal | Interview sets closed, against the four-week plan in the proposal. Week one is the gate: everything downstream waits on the workshops |
| Outbound Workforce | GTM Workforces proposal | Same shape. Week one is the ICP workshop and the deliverability build |

**How "what is left" is tracked**, since it had no method before: each page carries the delivery schedule drawn up in its own proposal, and progress is measured as **interview sets closed** rather than days elapsed. The workshops became a series of refinement sessions rather than a single day, so calendar weeks stopped being a useful measure while the sessions run long.

## Decisions

Decision records that sit outside the meeting series, kept here so the flight plan and the vault agree.

| Decision | Date | Record |
|----------|------|--------|
| **Workflow slate: TXN's ranked order and flagship pick.** Depth before breadth; decline investigation with the fix attached is the flagship. Clears the item that blocked forward workflow planning | 25 Aug 2026 | [[2026-08-25-workflow-slate-decision]] |
| **The workflow-slate build.** Seven new SOPs, ten new MCP tools, nineteen gated writes, merged to `main` across four repositories. Ranks 1 to 6 of TXN's order now have running SOPs | 25 to 26 Aug 2026 | [[2026-08-26-workflow-slate-build]] |

## What the current plan says

### The headline, 27 August

- **The biggest code drop of the pilot landed, and the buffer still narrowed.** **78%** of scope complete (range 74 to 82) against **76%** of the window elapsed, day 32 of 42, 11 days to completion. Scope moved 4 points in two days, which is fast; the clock moved 5. The margin was **+23 on 14 August, +16 on 18 August, +3 on 25 August, +2 today**. This is the asymmetry stated as plainly as it can be stated: a very large, well-tested build, and it bought back one day of comfort out of five.
- **The workflow-slate build landed on 26 August.** Full record at [[2026-08-26-workflow-slate-build]]. The SOP library went from **6 to 13**, the MCP catalogue from **33 to 43 tools**, and the HITL gate now covers **19 record-changing tools** with a boot-time assertion that every gate is reachable. **Ranks 1 to 6 of TXN's slate all have running SOPs**, including card service actions, which was 0 of 6 on tool coverage two days earlier.
- **Two of the flight plan's own "not in this build" items are now built.** `onboard-cardholder` and `lost-stolen-card` were written on 12 August, sat on an unmerged branch for a fortnight, and reached `main` on 26 August. Every issue since 13 August has told TXN that cardholder onboarding is not implemented and that no create operations exist. That statement is now wrong and is corrected on this issue.
- **The slate alignment action has inverted, and it is still urgent.** The slate over-claimed on 25 August; it now **under**-claims, and TXN is writing thirteen journey documents against it. The correction has to reach them before their documents are finished.
- **The 25 August commit-velocity note was wrong and is withdrawn.** It counted `main` and the work was on branches. Count all branches. The part of [[open-questions]] #57 that stands is that every commit on all four repositories is still George's, these included.
- **Content Workforce has slipped a second time, and the slip is the method's known trade-off.** Session 2 on **21 August** was booked as the brand entity and spent its hour completing the manifesto. The manifesto is **closed and loaded into the platform**; the pillars and the brand entity are both booked for **27 August**. See [[2026-08-21-content-workforce-interview-2]].
- **A Stackworkz session on 26 August demonstrated the agent interface and opened the code-sharing plan.** First time the built surface has been shown to the partner who owns the production Console. Recorded at [[2026-08-26-stackworkz-agent-demo]]; it is the first mechanism against register rows #33 and #35, which have been theoretical since May.
- **The acceptance date is still not fixed in writing.** Carried from 18 August, now nine days overdue and unchanged by any of the above ([[open-questions]] #54).

### The headline, 25 August

_Superseded by the entry above. Kept because the flight plan diff is read against it._

- **The pilot has run out of buffer.** **74%** of scope complete (range 70 to 78) against **71%** of the window elapsed, day 30 of 42, 13 days to completion. The margin was **+23 points on 14 August, +16 on 18 August, +3 today**. The pilot is not late and nothing contracted has been missed, but the comfort has gone, and it went in one week. This is the asymmetry behaving exactly as the last two issues predicted.
- **Commit activity has consolidated.** _Internal note, not carried on the client-facing flight plan by decision (25-08)._ Across the four build repositories there were **two substantive commits in the seven days to 25 August**: `txn-agentic-agent` last moved 17 August, `txn-mcp-server` 11 August, `txn-mock-api` one lint fix. Recorded here as evidence for the completion estimate rather than as a reported risk.
- **Approval stacking has landed**, and it was the main open item in the last issue. Two commits did it: 20 August *"HITL hand-off: the next gate arrives, answered cards stay answered"* and 24 August *"Acknowledge the click, hold the answer, and a browser harness that watches"*. The second also adds a browser test harness, which is the right instinct this close to UAT.
- **Capacity concentration.** _Internal note, not carried on the client-facing flight plan by decision (25-08)._ Every commit on all four build repositories since kickoff is George's, and the 24 August outbound session additionally assigned him email configuration and domain warming. Tracked at [[open-questions]] #57 so it stays visible internally.
- **The TXN customer onboarding agent still has no code**, re-verified 25 August across all eight repositories: no repo, no branch, no module, zero open GitHub issues anywhere in the estate. It has been unstarted for the full six weeks. **This issue moves it into the post-pilot plan as the first build after acceptance** and recommends agreeing its landing point with TXN rather than discovering the gap at acceptance.
- **The acceptance date is still not fixed in writing.** Carried from 18 August, now the single most overdue item ([[open-questions]] #54).

### The forward frame

The frame is **launch anchored**: it opens 8 September 2026, the day after pilot completion, and runs in three-month blocks. Set on 25 August, to hold stable, and not to move without TXN agreeing it in a weekly review.

**It is planned here rather than on the flight plan.** The 10:07 issue carried four quarter pages; the client-facing report has been returned to its established four-page structure (Home, Pilot Release, Workflow Status, Module Ledger). The forward pipeline below remains the working plan.

| Quarter | Window | Character |
|---------|--------|-----------|
| Block 1 | 8 Sep to 7 Dec 2026 | Delivery: acceptance closeout, the customer onboarding agent, the wire-in build, the permission model |
| Block 2 | 8 Dec 2026 to 7 Mar 2027 | Scale: Phase 3 team, first client onboarding, hardening from real use |
| Block 3 | 8 Mar to 7 Jun 2027 | Planning surface, no commitments by design |
| Block 4 | 8 Jun to 7 Sep 2027 | Planning surface, a horizon rather than a plan |

**A commercial precondition on every commitment beyond the pilot.** Only the pilot is papered, under a standalone Pilot Order. Everything beyond the pilot sits under the MSA, which [[commercial]] records as **drafted and under persona review, not signed**. If signature slips, the forward plan slips with it, and that is a TXN-side action rather than a delivery risk.

### Carried forward, still true

- **All three Pilot Order deliverables are in scope.** The Full Agentic Experience and the Agent Access Layer are operational on simulation, with **thirteen workflow SOPs** running end to end. The MCP surface is at **43 tools** since 26 August, of which **19 are gated as record-changing writes**.
- **[[internal-ops-agents|Internal Ops v1]] is three line items**: knowledge engine **delivered** and in active client use, meeting capture **delivered** and running on this project (**18 meeting records**, most recent 24 August), and the **[[customer-onboarding|TXN customer onboarding agent]] not started**.
- **Note on the word onboarding.** Three different things carry the name. Internal Ops part 3 is **onboarding a customer onto TXN**, the commercial process run when a client commits. It is not [[guided-onboarding]] (the in-product co-pilot journey), and not cardholder onboarding on the workflow slate.
- **Two pieces of work are routinely confused.** Sprint Zero (£17,500, delivered) is the requirements effort for the whole project and produced this vault. The **Control Center React build** is separate, and appears in **no priced stage of any proposal**.
- **The candidate slate decision has come back (25-08).** Recorded in full at [[2026-08-25-workflow-slate-decision]]. Michael has ranked all ten with the principle **depth before breadth**, and named **decline investigation with the fix attached** as the flagship build: highest daily volume, half of it already runs as `investigate-declines`, no external dependency, and the fix half reuses the spend-control workflow. TXN has written **journey documents for all thirteen workflows** and will confirm endpoints and approval gates through the following week. **Candidates 8, 9 and 10, previously Novosapien concepts TXN had not asked for, are now TXN-ranked work.** Two things remain open: TXN ranked all ten and parked none, so there is no cut line, and Michael frames the work as being *"in the pilot"*, which needs the landing point confirming since the pilot definition is frozen and completes 7 September.
- **Workflow slate alignment is now more pressing, and it has reversed direction (27-08).** The slate describes three workflows as operational. The implemented set is **thirteen SOPs**, and it now includes both of the workflows the slate was said to over-claim: cardholder onboarding and lost or stolen card are both implemented as of 26 August. **TXN is writing journey documents against the slate's descriptions**, so the correction still has to reach them before their documents are finished; it is simply a different correction from the one that was planned. See [[2026-08-26-workflow-slate-build]].
- **Permission model still deferred.** Named in Pilot Order deliverable 2. The 26 August build hardened the **gate**, 19 record-changing tools with a boot-time reachability assertion, but did not add a **permission model**: nothing yet decides who may call what. The distinction matters at acceptance and is worth putting to Michael in those words.

### Scope added inside the launch window

**The workflow-slate build, 25 to 26 August.** Five of the seven new SOPs are TXN's ranked post-pilot build, written and merged inside the frozen window. Assessed under the scope-add protocol:

- **Broken code shipped.** The pilot's safety mechanism was reworked twelve days from acceptance: the HITL gate went from a handful of tools to 19, and the console's approval chain gained a collapse ladder and a third render state. Highest-exposure change of the pilot, and **the best mitigated one**: a boot-time gate-reachability assertion that turns a renamed tool into a boot failure rather than an ungated destructive tool, 344 lines pinning the SOP prose, 245 tests plus 105 live oracle checks on the MCP server, a Playwright geometry test, and a browser sign-off loop whose numbered defects were fixed in the same commit.
- **Whole-codebase breakage.** The catalogue regenerated 33 to 43 with three measured overrides, and the console's label map, the mock's coverage pin and the agent's facets all had to move together. Cross-repo invariant tests carry it.
- **Cloud environment.** All four services deploy on push to `main`, so all four redeployed on 26 August.
- **The displacement, named.** Nothing on the must-land list moved while this was built. The acceptance date is still unwritten, the customer-onboarding agent still has no landing point, and TXN still has not been inside the build.
- **It does not raise pilot completion.** Five of the seven SOPs are post-pilot scope ([[open-questions]] #59). They are counted as delivered work, not as pilot progress.
- **Recommendation.** Freeze `main` on the four build repositories until the regression pass on all thirteen SOPs is done against the exact release build. No further slate SOPs before acceptance.

**The 24 August outbound session** assigned **George** email configuration and domain warming for the Outbound Workforce, plus a session with Jacob. It carries no direct structural risk to the pilot codebase, but it costs attention at the point attention is scarcest. **Recommendation: take the discovery session with Jacob now, hold the domain setup and warming until after 7 September.** Nothing in the agreed launch sequence needs it sooner, since outbound cannot send before the market announcement.

## Corrections this plan makes to the vault

| Vault record | What the code shows | Action |
|--------------|--------------------|--------|
| [[open-questions]] #32 said the pilot mock API runs on the 29 May YAML | The mock moved to the **External contract on 10 August** and now carries `api-specification_10Aug2026.yaml`, 67 paths and 98 operations, with a spec-pull pipeline | **Done 25-08.** Flagged on 18-08 and left uncorrected for a week; register row now carries the correction and is narrowed to the partner question |
| [[vision]] states in five places that TXN does not hold balances in MVP and every authorisation is a pass-through | Ian, 24-08: *"it's both, not an either or"*. There are occasions where TXN authorises against a balance it holds | **Open.** New register row #55. Load bearing: it is the stated premise for scoping [[fraud-risk-assist]] as advise, don't decide. Confirm with Ian before correcting [[vision]] |
| [[architecture]] does not record the multi-tenancy risk | Shared architectural components mean one client flooding the system can affect others. Ian, 24-08: *"Yes, we believe there still is a risk"* | **Open.** New register row #56 |
| [[commercial]] records the Outbound Workforce as deferred to a later phase (13-08) | It is actively starting: domains being scoped, 126 accounts in play, George assigned | **Done 25-08.** [[commercial]] corrected |
| **New.** Every flight plan since 13-08 told TXN that **cardholder onboarding is not implemented** and that no create operations exist for a cardholder, account, card or PIN | `onboard-cardholder` runs the full five-record chain with read-back verification, on `main` since 26-08. `lost-stolen-card` likewise covers block, replace and re-provision | **Done 27-08.** Corrected on this issue and recorded at [[2026-08-26-workflow-slate-build]]. It was true when written; the code was on an unmerged branch |
| **New.** [[delivery]] recorded on 25-08 that build velocity had fallen to **two substantive commits in seven days**, and [[open-questions]] #57 carried it as evidence | The count was taken on `main`. The work was on three build branches and merged 26-08: roughly 5,000 lines across four repositories | **Done 27-08.** The velocity conclusion is withdrawn. Method corrected: **count all branches, not `main`**. The single-committer half of #57 stands |
| **New.** No vault record carried a mechanism for getting the agentic surface into the **Stackworkz Console**. [[open-questions]] #33 and #35 have been theoretical since May | A 26-08 session demonstrated the agent interface to Stackworkz and opened a code-sharing plan | **Open.** New register row #61, recorded at [[2026-08-26-stackworkz-agent-demo]]. No transcript was captured; get the follow-up recorded |
| **New.** [[content-workforce]] had session 2 on **20 August** as the brand entity | It ran on **21 August** and did not reach the brand entity. The hour completed the manifesto | **Done 27-08.** Schedule corrected; both the pillars and the brand entity are booked for 27 August |

## Reporting cadence

Agreed with Dorte on 18 August: **the flight plan goes to TXN at the end of each week**, not every couple of days, since little changes across two days. Novosapien runs it daily internally to watch percentage completion against duration and catch stuck line items.

## Sources

Reconciled at generation from: nine GitHub repositories (`txn-vault` 109 commits, `txn-console-react` 277, `txn-mock-api` 49, `txn-agentic-agent` 43, `txn-mcp-server` 27, `txn-admin-panel` 25, `txn-admin-api` 11, `txn-vault-mcp` 2, and `ICP-site` 3, which carries the Content Workforce ICP walkthrough; 546 commits in total), the proposals in [[commercial]], and this vault. The workflow candidate slate lives in the shared folder as `txn-workflow-candidates.pdf`.

**Method note, set 27-08.** Repository evidence is gathered with `git fetch --all` and read across **every branch**, not `origin/main`. The 25 August issue counted `main` only and reported a velocity fall that had not happened; roughly 5,000 lines were sitting on three unmerged build branches at the time. Branch state is now part of the ledger, and unmerged work is reported as unmerged rather than as absent.
