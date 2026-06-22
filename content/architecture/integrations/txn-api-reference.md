---
title: "TXN Global API - OpenAPI Spec (index)"
type: reference-artifact
source: "DirectTransact (DT)"
received-from: Michael
date: 2026-05-29
status: reference
artifact: "txn-api-spec.yaml"
maps-to:
  - "[[architecture]]"
  - "[[integrations]]"
  - "[[developer-support]]"
  - "[[docs-mcp-server]]"
  - "[[sandbox-assist]]"
---

# TXN Global API - OpenAPI Spec (index)

> **Reference artifact (placed):** Index note for the DirectTransact OpenAPI spec, received from Michael. The raw artifact is `txn-api-spec.yaml` (in this same `integrations/` directory). This is the **"DT YAML"** referenced throughout [[developer-support]]: the API reference is auto-rendered from it, and it grounds the docs MCP server and sandbox. Routed from [[integrations]].

## What this is

The OpenAPI definition for the **TXN Global API**, the source of truth for the public API surface that integrators build against.

| Property | Value |
|----------|-------|
| Title | `DirectTransact.TxnGlobal.API` |
| Description | "This is the global APIs for the TXN system" |
| Version | `v1` |
| OpenAPI | 3.0.4 |
| Owner / source | Direct Transact (directtransact.co.za) |
| Spec date | 29 May 2026 |
| Size | ~17,400 lines · 51 endpoints · ~464 schemas |
| Raw file | `txn-api-spec.yaml` |

The spec is kept as the raw `.yaml` artifact rather than inlined here: it is auto-rendered into the portal's API Reference and consumed by tooling, so the YAML is the canonical form. This note exists so the artifact is discoverable and wikilinked inside the vault.

## Resource groups (endpoints)

The 51 endpoints cluster into these resource areas:

| Area | Example endpoints |
|------|-------------------|
| Account | `/account`, `/account/accounts` |
| Alerts | `/alerts` |
| Bin / Bin Range / Bin Sponsor | `/bin`, `/bins`, `/binrange`, `/binranges`, `/binsponsor`, `/binsponsors` |
| Cardholder / Cardholder Group | `/cardholder`, `/cardholders`, `/cardholdergroup` |
| Card / Card Program | `/card`, `/cardprogram`, `/cardprograms` |
| Delegated Approval | `/delegatedapproval`, `/delegatedapproval/health`, `/delegatedapprovalsource(s)`, `/delegatedapprovalstandin(s)` |
| Digital Wallet | `/digitalwallettoken/pushprovision`, `/digitalwallettokens` |
| Fees | `/fee`, `/fees` |
| Transactions / Simulation | `/transactions`, `/simulation/transaction` |
| Merchant Control | `/binsponsor/merchantcontrol`, `/merchantcontrolgroup(s)` |
| Spend Control / Override | `/binsponsor/spendcontrol(s)`, `/spendoverride(s)` |
| Webhooks | `/webhook`, `/webhooks`, `/webhook/health`, `/webhookinbound` |
| PIN | `/pin/authenticate`, `/pin/set`, `/pin/unblock`, `/pin/view` |
| Product | `/product`, `/products` |
| Program Manager | `/programmanager`, `/programmanagers` |
| 3DS | `/3ds/bulk/enroll`, `/3ds/bulk/unenroll` |
| Health / Meta | `/health`, `/healths`, `/api-specification.yml` |

> For the full request/response schemas, parameters, and examples, open `txn-api-spec.yaml` directly.

## Why it matters to the vault

- **API Reference** in the Developer Portal is auto-rendered from this YAML (see [[developer-support]] §1, §4).
- It **grounds the docs MCP server** ([[docs-mcp-server]]) and the **sandbox** ([[sandbox-assist]]) so answers stay current.
- It is one of the **two doc stores** (DT YAML for API reference; Umbraco for guides + changelog) noted in [[developer-support]] §9 and to be reflected in [[architecture]].
- Relates to the SuperUltra Code Block (OpenAPI mode) open question in [[umbraco-guide-content-model]]: TXN has multiple specs, so the operation picker may need scoping by spec.
