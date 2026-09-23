---
title: "TXN Global API - OpenAPI Specs (index)"
type: reference-artifact
source: "DirectTransact (DT)"
received-from: Michael
date: 2026-07-28
status: reference
artifact: "txn-api-spec-external.yaml + txn-api-spec-internal.yaml"
maps-to:
  - "[[architecture]]"
  - "[[integrations]]"
  - "[[developer-support]]"
  - "[[docs-mcp-server]]"
  - "[[sandbox-assist]]"
  - "[[agent-access-layer]]"
description: "Index note for DT's TXN Global API specs: the external and internal split, the 21 September drop to 46 operations, the gateway move, and the key state"
---

# TXN Global API - OpenAPI Specs (index)

> **Reference artifact (placed):** Index note for the DirectTransact OpenAPI specs, received from Michael. This is the **"DT YAML"** referenced throughout [[developer-support]]: the API reference is auto-rendered from it, and it grounds the docs MCP server, the sandbox, and the [[agent-access-layer]] mock-API stubs. Routed from [[integrations]].

> **These are the latest specs and the ones to build against going forward.** Shared by Michael at the [[2026-07-28-agentic-pilot-kickoff]] ("the latest one from Friday"); placed in the vault 2026-07-29. They supersede the single spec of 29 May 2026 (`txn-api-spec.yaml`, removed; recoverable from git history).

## What changed vs the May spec

The single **51-endpoint** spec has been **split into two APIs**:

- **External** (`TxnGlobal.API`): the public, client-facing surface integrators build against. This is the spec for the dev portal API reference, the sandbox, and the pilot's mock API.
- **Internal** (`TxnInternalGlobal.API`): platform-management resources (BINs, BIN ranges, BIN sponsors, card programs, program managers). Not client-facing.

Also note: paths are now **pluralised** (`/accounts`, `/cards`, `/pins/set`), a naming change consistent with the "field/name changes expected" warning in [[open-questions]] #32. The split maps onto the single-vs-separate API instance architecture discussion (#48); known issue per Michael (28-07): **YAML quality, e.g. missing limits**, is still being worked by DT.

## The two specs

| Property | External | Internal |
|----------|----------|----------|
| Title | `TxnGlobal.API` | `TxnInternalGlobal.API` |
| Raw file | `txn-api-spec-external.yaml` | `txn-api-spec-internal.yaml` |
| Spec date | 2026-07-08 | 2026-07-07 |
| Version / OpenAPI | `v1` / 3.0.4 | `v1` / 3.0.4 |
| Size | 30 paths, 99 operations, ~325 schemas | 7 paths, 23 operations, ~71 schemas |
| Owner / source | Direct Transact (directtransact.co.za) | Direct Transact |

The specs are kept as raw `.yaml` artifacts rather than inlined here: they are auto-rendered into the portal's API Reference and consumed by tooling, so the YAML is the canonical form. This note exists so the artifacts are discoverable and wikilinked inside the vault.

## Resource groups

**External** (`txn-api-spec-external.yaml`), 30 paths:

| Area | Endpoints |
|------|-----------|
| Account | `/accounts` |
| Alerts | `/alerts` |
| Cardholder / Group | `/cardholders`, `/cardholdergroups` |
| Card | `/cards` |
| Delegated Approval | `/delegatedapprovals`, `/delegatedapprovals/health`, `/delegatedapprovalsources`, `/delegatedapprovalstandins` |
| Digital Wallet | `/digitalwallettokens`, `/digitalwallettokens/pushprovision` |
| Fees | `/fees` |
| Transactions / Simulation | `/transactions`, `/simulations/transactions` |
| Merchant Control | `/binsponsors/merchantcontrols`, `/merchantcontrolgroups` |
| Spend Control / Override | `/binsponsors/spendcontrols`, `/spendoverrides` |
| Webhooks | `/webhooks`, `/webhooks/health`, `/webhookinbounds` |
| PIN | `/pins/authenticate`, `/pins/set`, `/pins/unblock`, `/pins/view` |
| Product | `/products` |
| 3DS | `/3ds/bulk/enroll`, `/3ds/bulk/unenroll` |
| Health / Meta | `/healths`, `/api-specification.yml` |

**Internal** (`txn-api-spec-internal.yaml`), 7 paths:

| Area | Endpoints |
|------|-----------|
| BIN management | `/bins`, `/binranges`, `/binsponsors` |
| Card Program | `/cardprograms` |
| Program Manager | `/programmanagers` |
| Health / Meta | `/healths`, `/api-specification.yml` |

> For the full request/response schemas, parameters, and examples, open the YAML files directly.

## The 21 September spec, and why the surface shrank

**Sources:** [[2026-09-22-agentic-standup]], and the delta George ran the same day (`specs/2026-09-22-txn-api-spec-refresh/reference/api-delta.md`).

| Spec | Paths | Operations | Schemas |
|---|---|---|---|
| Build pin, 10 Aug 2026 | 67 | 98 | 327 |
| 25 Aug 2026 | 22 | 35 | 177 |
| 21 Sep 2026 | 30 | 46 | 223 |

George put the drop to Michael on the call: about 96 operations in August against *"40 48 or 46"* now. The areas he named as missing were transactions, spend control creates and updates, spend overrides, alerts, PIN, 3DS and digital wallets.

**Michael's explanation is that the spec now shows only what DT has built.** *"They've moved now to a new open API spec service they've built. So before they've just uploaded everything. So you had everything that wasn't even built... now you're actually seeing the true live reflected."* The missing areas *"will be coming in in one way shape or the other"*, and the remaining build, mostly FDS, transactions and spend controls, is *"around there"* for October, because TXN needs it to go live.

**There is no target spec to build against, which is the finding that matters.** Michael: *"there isn't one sort of one defined spec that keeps rotating. Basically we just have these small user stories unfortunately that that they're sort of building from... we have sort of documentation for it but not specifically you know a design YAML if you will."* He will ask DT what changed and why, because TXN follows the same YAML and its own test suite carries the same risk. **No endpoint is signed off yet.**

**Two changes he named:** the spend control identifier moves **out of the URL and into the body**, and the rest are mostly **extra fields** that come out of the Visa mandates.

> [!note] The mock API rule, agreed on the call (22-09-2026)
> George proposed it and Michael accepted, *"Yeah. Yeah, definitely. I appreciate that."*
>
> - **The endpoint exists in both versions** → update the mock API to the new fields.
> - **The endpoint is absent from the 21 September spec** → keep the 10 August version until DT confirms the drop, then update or remove it.
>
> **Why it matters:** the live API misses at least one tool call in **8 of 13 agent workflows** (George, on the call), so building against the live surface alone would stall most of the slate.

**What the same-day delta found.** Of the 43 MCP tools, **20 keep their path and change shape**, **3 merchant-control tools move path**, and **20 are absent** (transactions, webhooks, alerts and fees, spend control writes, PIN, 3DS, digital wallet, spend overrides). The shape changes are not all field additions: spend control limits nest as `limits.amount`, the account transition `reason` and `fundingType` become enums that reject the values our SOPs send, and no card row carries `cardNumberMasked`, which the last-four targeting depends on. The impact analysis verdict is **STOP** until the paired SOP, prompt and code changes exist. Ian asked on the call how far away a settled MVP API is, because of rework cost; that question and this gap are tracked at [[open-questions]] #94.

### Routing: program manager ID becomes card program ID

Michael, 22 September: *"the program manager ID is what we pass in. We've switched that to car[d] program ID just so you don't have to give both IDs."* The internal API holds the full list of card programs, a user is assigned to one, and the identifier lets DT route the call to the right infrastructure. It is the last piece before Stackworkz start external UAT. Related: [[open-questions]] #48, the single-instance-versus-per-client question this routing serves.

### Stackworkz hit the same schema gap

Michael on their progress: the core work such as permissions is done, but *"we have now hit a point where they need to know the APIs, they need to know the schemas"*, so the build slowed. One gap is structural rather than a schema detail: listing **all cards** for a drop-down needs multiple calls and *"it's not sort of built for a public API, because obviously you don't normally search all cards."* DT and TXN are agreeing how to do it. Their focus is the internal side, program creation and setup, before the external API.

## Where the specs are served from (UAT)

**Updated 27 August 2026.** Source: email from **Michael Moores** to Brett and George.

Direct Transact **launched a new OpenAPI service** to deliver better documentation, and had to move the specs to a new URL in UAT as a result. Michael's assurance: *"no further changes have been made and everything you were running before should work with the new URL."*

| Spec | URL |
|------|-----|
| **External** | `https://development.txn.global/api/stg/Txn/feApiTxnOpenSpecification/api-specification.yml` |
| **Internal** | `https://development.txn.global/api/stg/Txn/feApiTxnOpenSpecification/internal-api-specification.yml` |

Both are served with the subscription key in the header; the key never appears in the URL.

### The shape of the URLs changed, not just their location

This is the part that matters operationally and it is easy to miss. Under the old scheme the two specs sat at **different base paths under the same filename**, `api-specification.yml`. Under the new scheme they sit at the **same base path and differ by filename**:

- external → `.../feApiTxnOpenSpecification/**api-specification.yml**`
- internal → `.../feApiTxnOpenSpecification/**internal-api-specification.yml**`

`txn-mock-api/scripts/fetch_spec.py` assumes the old shape. It holds a single constant, `SPEC_ENDPOINT = "api-specification.yml"`, and builds the request as `{base_url}/{SPEC_ENDPOINT}`, choosing between `TXN_EXTERNAL_BASE_URL` and `TXN_INTERNAL_BASE_URL` on the `--internal` flag.

**Consequence: pointing both base URLs at the new path makes `--internal` fetch the external spec, and it fails silently.** The request succeeds, the YAML parses, and the file is written under whatever name was asked for. Nothing errors. Michael's *"everything should work"* is true for the external spec and not true for the internal one, through no fault of his: it is our assumption that broke, not his service.

The fix is a one-line change, making the filename depend on the flag rather than being a constant. Tracked at [[open-questions]] #67.

**Nothing is broken right now.** The pilot builds from the committed `spec/api-specification_10Aug2026.yaml`, pinned by sha, so no live fetch sits on the critical path. This bites the next time someone regenerates from the internal spec.

### Updated 22 September 2026: the prefix moved again, and the key is rejected

Michael sent the new spec URL by email on 21 September. DT moved the gateway prefix from `/api/stg/` to `/api/staging/`, so **every `/api/stg/...` route now returns 404**.

| Route under `https://development.txn.global/api/staging/Txn/` | Result |
|---|---|
| `feApiTxnOpenSpecification/external/api-specification.yml` | 200, with or without a key |
| `feApiTxnOpenSpecification/internal/api-specification.yml` | 401, invalid subscription key |
| `feapiTxnGlobal/accounts`, `/cardholders`, `/products`, `/healths` | 401, invalid subscription key |
| `feapiTxnInternalGlobal/bins` | 401, invalid subscription key |

**The subscription key is rejected on every route that checks one.** George raised it on the call as *"not urgent"*, because the schemas and payloads are what the build needs today, *"but obviously when we get to testing on live APIs, I think that'd be something we might need to get sorted."* Michael's account: DT rebuilt the environment in **Azure API Management**, he received a new key that morning, and he will send it once he has tested it. Later there will be a **dedicated key per application**, production separated, and the authentication method itself will change. Tracked at [[open-questions]] #95.

**The spec route does not check the key**, so a successful spec download proves nothing about the key.

**The URL shape returns to what the script expects.** The two specs now sit at **different base paths under the same filename**, `external/api-specification.yml` and `internal/api-specification.yml`, which is the shape `fetch_spec.py` was written for. Point `TXN_EXTERNAL_BASE_URL` and `TXN_INTERNAL_BASE_URL` at the two new paths and the `--internal` flag is correct again, so the one-line fix at [[open-questions]] #67 may no longer be needed. Every URL in `txn/.env` still carries the old `/api/stg/` prefix. (Source: `specs/2026-09-22-txn-api-spec-refresh/reference/api-delta.md`, not the call.)

## Spend controls: the hierarchy, and a live gap

Described by Michael on 15 September 2026 ([[2026-09-15-agentic-standup]]), after the agent gave a false answer about them ([[open-questions]] #89).

| Rule | Detail |
|------|--------|
| **Depth** | A **nine-level hierarchy**, from BIN sponsor (strictly, BIN range) down to card |
| **Ownership by URL** | Separate endpoints per level with the same request schema, *"to make that ownership clear"* |
| **Access** | A program manager cannot act at BIN sponsor level; the agent should offer only reachable levels |
| **Ceilings** | A lower level cannot exceed its parent: *"you couldn't go and say put £1,000 on this card if the program was set to 500"* |
| **Guidance before refusal** | *"The API will just tell you to go away anyway, but if we can frontload that ahead, so we're guiding them properly"* |
| **Merchant controls** | Same hierarchy, **yes or no** rather than an amount |

**The endpoints are not built.** Michael: *"we haven't approved the user stories of spend controls yet. That's what they've automatically built"*, and DT's API is *"pretty broke right now for that."* **The agent is also on an out-of-date version of this spec** because of the URL change at [[open-questions]] #67, which is why it reasoned from what it had and reported the gap as architecture.

**Incoming:** Michael holds around **twenty DT specification documents** on the hierarchy and will send them once his DT questions are answered. He expects spend controls to be *"one of the most used"* areas, with analytical questions like *"if I did a transaction of £500 at this merchant, would it go through?"* checked across every level.

## Why it matters to the vault

- **API Reference** in the Developer Portal is auto-rendered from the external YAML (see [[developer-support]] §1, §4).
- It **grounds the docs MCP server** ([[docs-mcp-server]]) and the **sandbox** ([[sandbox-assist]]) so answers stay current.
- The pilot's **mock API + MCP stubs** ([[agent-access-layer]], per the [[2026-07-28-agentic-pilot-kickoff]]) are built from the external spec; switching to the real API is a URL flip.
- It is one of the **two doc stores** (DT YAML for API reference; Umbraco for guides + changelog) noted in [[developer-support]] §9 and reflected in [[architecture]].
- Relates to the SuperUltra Code Block (OpenAPI mode) open question in [[umbraco-guide-content-model]]: TXN now definitively has **multiple specs**, so the operation picker needs scoping by spec.
