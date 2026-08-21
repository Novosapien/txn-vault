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
| [flightplan-txn-2026-08-21-1110.html](flightplan-txn-2026-08-21-1110.html) | The six-week agentic pilot, 27 July to 7 September 2026 | **21 Aug 2026, current** |
| [flightplan-txn-2026-08-19-1540.html](flightplan-txn-2026-08-19-1540.html) | Superseded | 19 Aug 2026 15:40 |
| [flightplan-txn-2026-08-19-1305.html](flightplan-txn-2026-08-19-1305.html) | Superseded the same day | 19 Aug 2026 13:05 |
| [flightplan-txn-2026-08-18-1935.html](flightplan-txn-2026-08-18-1935.html) | Superseded | 18 Aug 2026 |
| [flightplan-txn-2026-08-14-1615.html](flightplan-txn-2026-08-14-1615.html) | Superseded | 14 Aug 2026 16:15 |
| [flightplan-txn-2026-08-14-1220.html](flightplan-txn-2026-08-14-1220.html) | Superseded the same day | 14 Aug 2026 12:20 |
| [flightplan-txn-2026-08-13-1640.html](flightplan-txn-2026-08-13-1640.html) | First issue | 13 Aug 2026 |

## What the current plan says

- **Pilot completion: 68%** of scope against **45%** of the window elapsed, so the pilot is ahead of its window. 24 days remained at generation.
- **The dominant risk is now calendar, not build** (18 Aug). The pilot completes 7 September, Michael is away 10 days from early September, and the Novosapien team travels on the evening of 10 September for three weeks. Acceptance, the 5 business day shortfall window and any remedial work must fit into three days ([[open-questions]] #54).
- **Earlier risks, now partly resolved** (14 Aug): **Michael is on holiday 10 days from early September**, landing on the UAT fortnight and the acceptance review, and he is TXN's only technical reviewer ([[open-questions]] #50). **Neither Michael nor Dorte has used the deployed build**, which is how three open items were meant to be settled ([[open-questions]] #51).
- **Five items were added to the build on 13 August**, the day the definition froze: per-run tool and endpoint audit, Sentry linked to feedback, collapsible approval cards, approval regrouping, and a UI rebuild against the final wireframes. Each carries a risk statement in the plan; the recommendation is to hold the UI rebuild until after acceptance.
- **All three Pilot Order deliverables are in scope.** The Full Agentic Experience and the Agent Access Layer are operational on simulation, with **six workflow SOPs** running end to end.
- **[[internal-ops-agents|Internal Ops v1]] is tracked as three line items** (14 August), all inside Internal Ops:
  1. **Knowledge engine** — delivered, as a remote MCP connector over this vault plus the docs portal.
  2. **Meeting capture** — delivered, and running on this project now.
  3. **[[customer-onboarding|TXN customer onboarding agent]]** — specified to build depth across four stages, **not started, no code in any repository**.
- **Note on the word onboarding.** Three different things carry the name. Internal Ops part 3 is **onboarding a customer onto TXN**, the commercial process run when a client commits. It is not [[guided-onboarding]] (the in-product co-pilot journey), and not cardholder onboarding on the workflow slate (creating a person, account, card and PIN).
- **Two pieces of work are routinely confused.** Sprint Zero (£17,500, delivered) is the requirements effort for the whole project and produced this vault. The **Control Center React build** is separate: a full React build of the GUI environments, done for the agentic experiment, appearing in **no priced stage of any proposal**.
- **The workflow scope is resolving** (20-08). Michael has reviewed the slate and is aligned; he met Ian to agree the priority order and will return the list. **Target: six or seven workflows for the pilot**, floor of three, and additions need not come from the slate. See [[open-questions]] #55.
- **The pilot's workflow scope was never confirmed, and it was the gating decision** ([[open-questions]] #55). The three operational workflows were Novosapien's choice to prove the pattern, not TXN's selection. Novosapien is close to complete on everything achievable without the answer; the remaining workflows are ready to start the moment TXN picks. **The gap in the plan is a decision, not delivery.** Narrowed on 19 August from ten candidates to seven: #9 and #7 are not proceeding, #10 is leaning out. All three are **parked and shown**, not dropped, since they were Novosapien's own suggestions.
- **Nothing on the candidate slate is agreed.** It was sent to TXN for a decision on every card (build next, park, not this) and **that confirmation has not come back**. Every candidate is a Novosapien proposal, not a commitment, and none of it is pilot scope. **Candidates 8 (alert, investigation, proposed plan), 9 (scheduled performance report) and 10 (guided product launch) are Novosapien concepts TXN did not ask for** and are marked as such.
- **Workflow slate alignment needed.** The Novosapien candidate slate describes three workflows as operational. The implemented set is six SOPs and differs: spend-control change matches, lost or stolen card is partially implemented, cardholder onboarding is not implemented.

## Corrections this plan makes to the vault

| Vault record | What the code shows | Action |
|--------------|--------------------|--------|
| [[open-questions]] #32 says the pilot mock API runs on the 29 May YAML | The mock moved to the **External contract on 10 August** and now carries `api-specification_10Aug2026.yaml`, 67 paths and 98 operations, with a spec-pull pipeline | Register row and [[integrations]] timeline to be updated |

## Reporting cadence

Agreed with Dorte on 18 August: **the flight plan goes to TXN at the end of each week**, not every couple of days, since little changes across two days. Novosapien runs it daily internally to watch percentage completion against duration and catch stuck line items.

## Sources

Reconciled at generation from: eight GitHub repositories (`txn-vault`, `txn-console-react`, `txn-agentic-agent`, `txn-mcp-server`, `txn-mock-api`, `txn-admin-panel`, `txn-admin-api`, `txn-vault-mcp`), the proposals in [[commercial]], and this vault. The workflow candidate slate lives in the shared folder as `txn-workflow-candidates.pdf`.
