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
| [flightplan-txn-2026-08-13-1640.html](flightplan-txn-2026-08-13-1640.html) | The six-week agentic pilot, 27 July to 7 September 2026 | 13 Aug 2026 |

## What the current plan says

- **Pilot completion: 67%** of scope against **43%** of the window elapsed, so the pilot is ahead of its window. 25 days remained at generation.
- **All three Pilot Order deliverables are in scope.** The Full Agentic Experience and the Agent Access Layer are operational on simulation, with **six workflow SOPs** running end to end.
- **[[internal-ops-agents|Internal Ops v1]] is tracked as three line items** (14 August), all inside Internal Ops:
  1. **Knowledge engine** — delivered, as a remote MCP connector over this vault plus the docs portal.
  2. **Meeting capture** — delivered, and running on this project now.
  3. **[[customer-onboarding|TXN customer onboarding agent]]** — specified to build depth across four stages, **not started, no code in any repository**.
- **Note on the word onboarding.** Three different things carry the name. Internal Ops part 3 is **onboarding a customer onto TXN**, the commercial process run when a client commits. It is not [[guided-onboarding]] (the in-product co-pilot journey), and not cardholder onboarding on the workflow slate (creating a person, account, card and PIN).
- **Two pieces of work are routinely confused.** Sprint Zero (£17,500, delivered) is the requirements effort for the whole project and produced this vault. The **Control Center React build** is separate: a full React build of the GUI environments, done for the agentic experiment, appearing in **no priced stage of any proposal**.
- **Workflow slate alignment needed.** The Novosapien candidate slate describes three workflows as operational. The implemented set is six SOPs and differs: spend-control change matches, lost or stolen card is partially implemented, cardholder onboarding is not implemented.

## Corrections this plan makes to the vault

| Vault record | What the code shows | Action |
|--------------|--------------------|--------|
| [[open-questions]] #32 says the pilot mock API runs on the 29 May YAML | The mock moved to the **External contract on 10 August** and now carries `api-specification_10Aug2026.yaml`, 67 paths and 98 operations, with a spec-pull pipeline | Register row and [[integrations]] timeline to be updated |

## Sources

Reconciled at generation from: eight GitHub repositories (`txn-vault`, `txn-console-react`, `txn-agentic-agent`, `txn-mcp-server`, `txn-mock-api`, `txn-admin-panel`, `txn-admin-api`, `txn-vault-mcp`), the proposals in [[commercial]], and this vault. The workflow candidate slate lives in the shared folder as `txn-workflow-candidates.pdf`.
