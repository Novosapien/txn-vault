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
description: "Index note for the DT-supplied TXN Global API OpenAPI spec (txn-api-spec.yaml) — 51 endpoints by resource group, and why the YAML grounds the portal"
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

## Why it matters to the vault

- **API Reference** in the Developer Portal is auto-rendered from the external YAML (see [[developer-support]] §1, §4).
- It **grounds the docs MCP server** ([[docs-mcp-server]]) and the **sandbox** ([[sandbox-assist]]) so answers stay current.
- The pilot's **mock API + MCP stubs** ([[agent-access-layer]], per the [[2026-07-28-agentic-pilot-kickoff]]) are built from the external spec; switching to the real API is a URL flip.
- It is one of the **two doc stores** (DT YAML for API reference; Umbraco for guides + changelog) noted in [[developer-support]] §9 and reflected in [[architecture]].
- Relates to the SuperUltra Code Block (OpenAPI mode) open question in [[umbraco-guide-content-model]]: TXN now definitively has **multiple specs**, so the operation picker needs scoping by spec.
