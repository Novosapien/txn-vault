---
status: Living
---

# TXN — Open Questions

> **Index:** [[index]] · **Vision:** [[vision]] · **Components:** [[components]]

Central register of unresolved questions across the vault. Each links to the doc/section where the answer belongs. Docs carry a short inline marker — `[⚠ open — see [[open-questions]] #N]` — instead of burying the full question at the bottom of every file.

This is the **single source of truth** for open questions. The branded **[gap register](drafts/txn-gap-register.html)** (HTML, for partners) is generated *from* this table — regenerate it when this changes.

**Status:** `Open` (needs an answer) · `Answered` (resolved — keep the row, note where it landed) · `Parked` (deferred).
**Type:** `Build` (build-blocking — ours to build, blocks the dependent piece) · `Client` (TXN product / commercial / risk decision) · `Partner` (needed from DT / Stackworkz / Super Ultra / a provider) · `Design` (our design work — land &amp; iterate).

## Register

| # | Question | Type | Area | Answer goes in | Raised in | Status |
|---|----------|------|------|----------------|-----------|--------|
| 1 | Product configuration — is it **~200 fields** or **50–60 properties**? (Two different figures from two calls.) | Client | Co-pilot / Access Layer | [[vision]], [[co-pilot]], [[agent-access-layer]] | 13-05 / 01-06 | Open |
| 2 | MCP-server **permission model** — do we need both **program-defined** and **user-defined** permissions, with capabilities switchable on/off at each level? How do API keys/instances map to this? | Design | Access Layer | [[mcp-server]], [[permission-scoping]] | 01-06 | Open |
| 3 | **Site-wide LLM ownership** — 29 May named **Teraflow** for the site-wide/agentic AI. **Resolved:** *Teraflow is Novosapien's former brand (since rebranded to Novosapien)* — the same party. The site-wide / agentic LLM is **Novosapien's**. | Client | Developer Support | [[developer-support]] | 29-05 | Answered |
| 4 | **System-defined alert corpus** — which alerts is TXN obliged to raise? (Specifics not defined; the focus so far is the *handling process*, not the catalogue.) | Client | Inbox & Alerts | [[alert-detection]], [[agent-inbox-alerts]] | 02-06 | Open |
| 5 | **Idempotency** on mutating MCP calls — assumed, not discussed. Confirm the requirement. | Design | Access Layer | [[mcp-server]] | (assumption) | Open |
| 6 | **Audit immutability / append-only + retention** — assumed immutable; retention window and storage location undecided. | Build | Access Layer | [[audit-attribution]] | 01-06 | Open |
| 7 | **Notification delivery** — fallback/retry on failure and a default channel were assumed, not discussed. Confirm. | Design | Inbox & Alerts | [[notification-routing]] | (assumption) | Open |
| 8 | **MCP-server ownership split** — docs/dev-portal MCP (Stackworkz wants it) vs card-acquiring-API MCP (owner unresolved, maybe DT). Who builds which; avoid duplicates. | Partner | Access Layer | [[agent-access-layer]] | 29-05 | Open |
| 9 | **AI-permission config** — TXN must build the org/user permission mirror for non-Console access (no API today). When, and owned by whom? | Build | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 10 | **Product webhook** — will DT add it, and on what timeline? (Underpins change-impact alerts.) | Partner | Access Layer / Inbox & Alerts | [[agent-access-layer]], [[alert-detection]] | 01-06 | Open |
| 11 | **Core API stability + versioning policy** — when is it stable enough to build tools against; how are breaking changes managed? | Partner | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 12 | **Data-lake schema** — when does DT share it? | Partner | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 13 | **Alerting-system build ownership** — DT's role was narrowed (post-AI discussion) to a context-less "post an alert" API; nobody is currently scoped to build the alerting/detection system. Who owns it? | Partner | Inbox & Alerts | [[agent-inbox-alerts]], [[alert-detection]] | 02-06 | Open |
| 14 | **Scheduled-report failure handling** — are missed/failed runs retried, and is the user notified of a delay vs a silent drop? Assumed in [[scheduled-reporting]], not discussed. | Design | Inbox & Alerts | [[scheduled-reporting]] | (assumption) | Open |
| 15 | **Alert priority field + multi-surface fan-out** — is there a `priority` field on the delivery payload, and do high-priority items fan out to multiple surfaces at once? Asserted in [[notification-routing]], not discussed. | Design | Inbox & Alerts | [[notification-routing]] | (assumption) | Open |
| 16 | **AI-layer PII / data-residency / redaction** — may cardholder PII appear in chat/audit logs, and what residency + redaction policy applies? Asserted in [[audit-attribution]] beyond the grounded retention point (#6). | Client | Access Layer | [[audit-attribution]] | (assumption) | Open |
| 17 | **AI-analysis consistency boundaries** — must the AI avoid analysing before a write settles (read-after-write guards)? Stated in [[ai-analysis-impact]] but flagged in [[vision]] §8 as a Novosapien inference. | Design | Inbox & Alerts | [[ai-analysis-impact]] | (assumption) | Open |
| 18 | **User-defined optimization metric** — should the user set an objective the agent optimises toward, with the agent able to suggest additional objectives? Floated 13-05; not yet scoped. | Client | Full Agentic Experience | [[full-agentic-experience]] | 13-05 | Open |
| 19 | **CRM ↔ Console data split** — exactly which client data items live only in the CRM vs are needed in the Console, and how they sync (Dorte raised). | Client | Architecture / Internal Ops | [[architecture]], [[integrations]] | 10-06 | Open |
| 20 | **AI-ready downloadable doc file** — the Super-Ultra-designed `LLMS.txt`-style file (less than the MCP: "here's TXN, here are the endpoints"); who builds it (Stackworkz from portal data vs AI-generated) and on what release cadence. | Partner | Developer Support | [[developer-support]] | 09-06 | Open |
| 21 | **Sign-up / login design** — not scoped in the portal MVP (docs are public). Needed to gate the MCP/sandbox and capture leads. Depends on #31. | Build | Developer Support | [[access-gating]], [[developer-support]] | 09-06 | Open |
| 22 | **Persistence store** — where do saved rendered views + recurring-task definitions live (state model for revisitable dashboards)? | Build | Full Agentic Experience | [[session-persistence]] | 05-06 | Open |
| 23 | **External name for "Co-pilot"** — "Co-pilot" is a Microsoft trademark (Dorte). Internally it needn't be named; decide the external/market name before launch collateral. | Client | Co-pilot | [[co-pilot]] | 04-06 | Open |
| 24 | **Per-level cost / token model** — the free surfaces (portal, MCP, sandbox) need a cost-per-1000-calls understanding to set the access gates (Ian). | Client | Developer Support / Alerts | [[developer-support]], [[agent-inbox-alerts]] | 09-06 / 02-06 | Open |
| 25 | **Reconciliation's home** — auth/clearing settlement reconciliation fits neither the client lanes nor fraud cleanly. Own payment-ops component, or stays in Internal Ops? | Client | Internal Ops | [[internal-ops-agents]] | 06-03 / journeys | Open |
| 26 | **AI risk-tolerance boundaries** — what AI actions are *never* allowed even with approval? What blast radius forces a human override regardless of trust level? | Client | Cross-cutting | [[vision]], [[agent-access-layer]] | 13-05 §8 | Open |
| 27 | **Cross-program benchmarking consent** — with few clients per use case, "anonymised" comparisons can still identify a client. Consent model + identification thresholds (later phase). | Client | Inbox & Alerts | [[agent-inbox-alerts]] | 02-06 | Open |
| 28 | **In-product pricing transparency** — is pricing surfaced inside the Console (so the co-pilot can reference it) or held externally? | Client | Co-pilot | [[co-pilot]] | 13-05 §8 | Open |
| 29 | **Corporate-email gating policy** — preferred to avoid junk signups (the Marqeta lesson), but don't block genuine startups without a corporate email. | Client | Developer Support | [[access-gating]] | 09-06 | Open |
| 30 | **Voice support (Tier 2)** — a voice support agent (~18–30p/min) vs text-first. Validate with a user group post-launch. | Client | Developer Support | [[support-triage]] | 09-06 | Parked |
| 31 | **Public sandbox API-key model** — does the sandbox need a per-user API key? This *changes whether/when sign-up (#21) is required*. | Partner | Developer Support | [[developer-support]], [[sandbox-assist]] | 09-06 | Open |
| 32 | **Endpoint QA / test status** — ~80 endpoints, ~80–90% untested; affects mock-API fidelity for early build. When are they QA'd? | Partner | Access Layer | [[agent-access-layer]] | 05-06 | Open |
| 33 | **Console instrumentation depth** — page state, component identifiers, action handlers. Michael flagged additional work may be needed to "plug in the AI." | Partner | Co-pilot / Full Agentic | [[co-pilot]], [[full-agentic-experience]] | 13-05 | Open |
| 34 | **Umbraco doc APIs + vector index** — docs exposed via API for AI search, embedded for semantic retrieval; draft-API for the knowledge engine. | Partner | Developer Support | [[developer-support]], [[knowledge-engine]] | 09-06 / 10-06 | Open |
| 35 | **Console component library handle** — addressable React/MUI components for the agent to render (generative UI). | Partner | Full Agentic Experience | [[generative-ui-rendering]] | 29-05 / 05-06 | Open |
| 36 | **A2A provider enablement** — direct A2A connections from the big providers (e.g. Anthropic). MCP-as-message fallback carries it until then. | Partner | Access Layer (A2A edge) | [[a2a-endpoint]] | 05-06 | Open |
| 37 | **Process-surfacing altitude** — how much of the multi-agent work to show. "Won't know until tested in the wild" — land one universal level &amp; iterate. | Design | Co-pilot / Full Agentic | [[process-surfacing]], [[full-agentic-experience]] | 04-06 / 05-06 | Open |
| 38 | **Real-time vs cached writes** — console-wide principle: fire each call live, or cache &amp; commit on review? (Mike: depends on action type — confirm console-wide.) | Design | Co-pilot | [[co-pilot]] | 04-06 | Open |
| 39 | **Stuck-user replay mechanism** — restate goal → replay completed steps → correct. Agreed in principle, undesigned. | Design | Co-pilot | [[conversational-qa]] | 04-06 | Open |
| 40 | **Bounding open-ended composition** — the agent "starts with all the data but doesn't know where it's going" (Stackworkz). Guard rails on what it may compose — the hardest problem. | Design | Full Agentic Experience | [[generative-ui-rendering]], [[agent-orchestration]] | 05-06 / 29-05 | Open |
| 41 | **Generative UI inside the client's Claude** — "probably could, but not exactly the same way." How much renders through the A2A path vs the TXN surface? | Design | Full Agentic / A2A | [[full-agentic-experience]], [[a2a-endpoint]] | 05-06 | Open |
| 42 | **One MCP server vs several** — leaning to a single "monolith" with per-turn tool gating; confirm as the tool count grows. | Design | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 43 | **Simulation scope &amp; timing** — vision puts the synthetic-persona harness in Internal Ops scope; the map parks it as a launch component. When is it built / used (incl. pre-launch cold-start)? | Design | Internal Ops | [[internal-ops-agents]] | 10-06 | Open |
| 44 | **Dev-Support ↔ Internal-Ops boundary** — triage entry point (portal) vs resolution + knowledge loop (internal ops). Confirm the hand-off contract. | Design | Developer Support / Internal Ops | [[developer-support]], [[internal-ops-agents]] | 10-06 | Open |
| 45 | **Component success metrics** — several §7 sections are placeholder-quality; quantify the evals per component with TXN. | Design | Cross-cutting | [[components]] | (multiple) | Open |
| 46 | **Internal Ops vision / dedicated session** — the component is assembled from the vision + adjacent sessions + journeys; Ian said it needs its own vision (resolves #25, #43, #44). | Design | Internal Ops | [[internal-ops-agents]] | 10-06 | Open |

## Notes

- New open questions raised in any extraction go here (with a backlink), not at the bottom of a single doc.
- When a question is answered, set its status to `Answered` and record where the answer now lives.
- The HTML gap register ([drafts/txn-gap-register.html](drafts/txn-gap-register.html)) is a generated view of this table — keep it in sync when rows change.
