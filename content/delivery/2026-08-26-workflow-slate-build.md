---
description: "The 25 to 26 August workflow-slate build: seven new SOPs, ten new MCP tools, nineteen gated writes, and what it means for pilot scope and the frozen build definition"
---

# TXN: the workflow-slate build (2026-08-25 to 26)

> **Index:** [[index]] · **Delivery:** [[delivery]] · **Decision it implements:** [[2026-08-25-workflow-slate-decision]] · **Components:** [[full-agentic-experience]], [[agent-access-layer]]

## What landed

The largest single code drop of the pilot, merged to `main` across four repositories on **26 August**, one day after TXN's ranked slate decision arrived.

| Repository | Commit | What it carries |
|-----------|--------|-----------------|
| `txn-mcp-server` | `548ef0f`, merged `8b5c6d1` | **Ten new tools, catalogue 33 to 43.** Three measured overrides, ten contract notes. 245 tests plus 105 live oracle checks |
| `txn-agentic-agent` | `5a6d79c`, merged `27982b5` | **Six workflow SOPs**, `hitl.py` gating **19 record-changing tools** and leaving 24 reads open, a `merchant_controls` facet. 1,840 lines added |
| `txn-mock-api` | `3624009`, merged `5f48776` | Tool coverage pin follows the 43-tool catalogue, 43 of 55 operations |
| `txn-console-react` | `ae43b94`, merged `84afdbc` | Ten tool labels, a named held-render placeholder, and the **approval-chain collapse** with a Playwright browser harness. 3,270 lines added |

The same merge also brought **`onboard-cardholder` and `lost-stolen-card`** onto `main`. Both were written on 12 August on `build/three-production-workflows` and sat unmerged for a fortnight.

## The SOP library is 13, not 6

| SOP | State before 26 Aug | Now |
|-----|--------------------|-----|
| `spend-control-impact` | on `main` | on `main` |
| `suspend-card` | on `main` | on `main` |
| `review-alerts` | on `main` | on `main` |
| `investigate-declines` | on `main`, investigation only | **rewritten**, with `diagnosis.md` and `fix.md`: the fix half is attached |
| `cardholder-overview` | on `main` | on `main` |
| `release-hold` | on `main` | on `main` |
| `onboard-cardholder` | written 12 Aug, unmerged | **on `main`** |
| `lost-stolen-card` | written 12 Aug, unmerged | **on `main`** |
| `vip-spend-exception` | did not exist | **new** |
| `card-service-actions` | did not exist | **new** |
| `merchant-control-change` | did not exist | **new** |
| `offboard-cardholder` | did not exist | **new** |
| `bulk-change` | did not exist | **new** |

## Two vault claims this falsifies

Both were true when written and are now wrong. They are corrected here and in [[delivery]] because they appear in the client-facing flight plan.

| Claim, as at 25 August | What the code shows |
|-----------------------|--------------------|
| **"Cardholder onboarding is not implemented, and the tool surface does not support it: there is no create operation for a cardholder, account, card or PIN."** Carried in every flight plan since 13 August, and in [[2026-08-25-workflow-slate-decision]] as a live alignment risk | `onboard-cardholder` runs the full chain: duplicate check, product choice, then cardholder, account, card, PIN and 3-D Secure enrolment, five approval cards announced up front, every id verified by read-back. On `main` since 26 August |
| **"Lost or stolen card is only partially implemented; replace and re-provision are outstanding."** | `lost-stolen-card` confirms the card by last four and expiry, blocks first, then takes a replacement through PIN, 3-D Secure and wallet provisioning. Five approval cards on a confirmed report, one on an unconfirmed one |

**The alignment action described in [[2026-08-25-workflow-slate-decision]] has therefore inverted.** The slate described three workflows as operational and the vault's position was that the slate over-claimed. The slate is now the document that **under**-claims, and TXN is writing thirteen journey documents against it. The alignment job is unchanged in urgency and reversed in direction.

## Tool coverage against TXN's ranked order

The ten new tools are `create_merchant_control`, `create_spend_override`, `get_cardholder_group`, `get_merchant_control`, `get_spend_override`, `list_cardholder_groups`, `list_spend_overrides`, `unblock_pin`, `update_cardholder`, `update_merchant_control`.

They were chosen against TXN's ranking, and they close it:

| TXN rank | Workflow | Coverage on 25 Aug | Coverage now | SOP |
|---|---|---|---|---|
| **1** | Decline investigation with the fix attached | 5 of 6 | **6 of 6** | `investigate-declines`, fix half attached |
| 2 | VIP spend exception | 2 of 4 | **4 of 4** | `vip-spend-exception` |
| 3 | Card service actions | **0 of 6** | **6 of 6** | `card-service-actions` |
| 4 | Merchant control change with impact | 2 of 5 | **5 of 5** | `merchant-control-change` |
| 5 | Cardholder offboarding | 5 of 6 | **6 of 6** | `offboard-cardholder` |
| 6 | Bulk change with a scaled confirmation | 3 of 5 | **5 of 5** | `bulk-change` |
| 7 to 10 | Alert to plan, monitoring alert, scheduled report, guided product launch | unchanged | unchanged | not built |

**Ranks 1 to 6 all have running SOPs on the simulation.** The "full tool-building round" that rank 3 was said to need has been done.

## The honest qualifications

The build is real. Four things stop it being a finished answer.

1. **Stood up, not delivered.** All thirteen run against the mock. None has been driven by TXN, and TXN has still not been into the build at all.
2. **Built ahead of TXN's own confirmation.** Michael's 25 August email said TXN would confirm *"the endpoints, the approval gates and the rest through next week"* and would write thirteen journey documents. The SOPs were written before any of that arrived. Where TXN's journey documents disagree with the implemented approval gates, the implementation moves, not the documents.
3. **This is post-pilot scope arriving inside the frozen window.** [[open-questions]] #59 records that the ranked build lands after acceptance because the pilot definition is frozen and completes 7 September. Five of the seven new SOPs are that ranked build. **They do not raise pilot completion**, and they must not be counted as though they do.
4. **The approval surface was reworked again.** The HITL gate now covers 19 tools rather than a handful, and the console's approval chain gained a collapse ladder and a third render state. That is the pilot's safety mechanism, changed twelve days from acceptance.

## Why the mitigation is better than usual

Recorded because it is the strongest test discipline the engagement has produced, and it is what makes point 4 tolerable:

- `assert_gates_are_reachable` turns a renamed tool into a **boot failure** rather than a silently ungated destructive tool.
- The gate is maintained by name, not derived from the catalogue's `kind`, because the two disagree on `pin_authenticate`: a POST that mints a token and changes no record. Deriving it would have been right 42 times and wrong on the one that matters.
- `test_slate_skill_bodies.py`, 344 lines, pins the SOP prose itself.
- `NO_UNEXPECTED_SHIFT`, a Playwright test that measures the collapse geometry in a real browser.
- A **browser sign-off feedback loop**: `feedback/browser-signoff-2026-08-25.md` records numbered defects found by driving the build, and the fixes are folded into the same commit.

## A method correction for the flight plan

[[delivery]] recorded on 25 August that there had been **"two substantive commits in the seven days to 25 August"** across the four build repositories, and used it as evidence for the completion estimate. That was measured on `main`.

It was wrong. The work existed on `build/three-production-workflows`, `build/workflow-slate` and `build/agentic-experience`, and `main` saw none of it until the merges. **Count all branches, not `main`.** Every subsequent flight plan does.

The related conclusion in [[open-questions]] #57, that build velocity had fallen, is withdrawn. The part of #57 that stands is that **every commit is still George's**, on all four repositories, including these.
