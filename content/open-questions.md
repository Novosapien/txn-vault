---
status: Living
---

# TXN — Open Questions

> **Index:** [[index]] · **Vision:** [[vision]] · **Components:** [[components]]

Central register of unresolved questions across the vault. Each links to the doc/section where the answer belongs. Docs carry a short inline marker — `[⚠ open — see [[open-questions]] #N]` — instead of burying the full question at the bottom of every file.

**Status:** `Open` (needs an answer) · `Answered` (resolved — keep the row, note where it landed) · `Parked` (deferred).

## Register

| # | Question | Area | Answer goes in | Raised in | Status |
|---|----------|------|----------------|-----------|--------|
| 1 | Product configuration — is it **~200 fields** or **50–60 properties**? (Two different figures from two calls.) | Co-pilot / Access Layer | [[vision]], [[co-pilot]], [[agent-access-layer]] | 13-05 / 01-06 | Open |
| 2 | MCP-server **permission model** — do we need both **program-defined** and **user-defined** permissions, with capabilities switchable on/off at each level? How do API keys/instances map to this? | Access Layer | [[mcp-server]], [[permission-scoping]] | 01-06 | Open |
| 3 | **Site-wide LLM ownership** — 29 May named **Teraflow** for the site-wide/agentic AI. **Resolved:** *Teraflow is Novosapien's former brand (since rebranded to Novosapien)* — the same party, not a distinct one. The site-wide / agentic LLM is **Novosapien's**. | Developer Support | [[developer-support]] | 29-05 | Answered |
| 4 | **System-defined alert corpus** — which alerts is TXN obliged to raise? (Specifics not defined; the focus so far is the *handling process*, not the catalogue.) | Inbox & Alerts | [[alert-detection]], [[agent-inbox-alerts]] | 02-06 | Open |
| 5 | **Idempotency** on mutating MCP calls — assumed, not discussed. Confirm the requirement. | Access Layer | [[mcp-server]] | (assumption) | Open |
| 6 | **Audit immutability / append-only + retention** — assumed immutable; retention window and storage location undecided. | Access Layer | [[audit-attribution]] | 01-06 | Open |
| 7 | **Notification delivery** — fallback/retry on failure and a default channel were assumed, not discussed. Confirm. | Inbox & Alerts | [[notification-routing]] | (assumption) | Open |
| 8 | **MCP-server ownership split** — docs/dev-portal MCP (Stackworkz wants it) vs card-acquiring-API MCP (owner unresolved, maybe DT). Who builds which; avoid duplicates. | Access Layer | [[agent-access-layer]] | 29-05 | Open |
| 9 | **AI-permission config** — TXN must build the org/user permission mirror for non-Console access (no API today). When, and owned by whom? | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 10 | **Product webhook** — will DT add it, and on what timeline? (Underpins change-impact alerts.) | Access Layer / Inbox & Alerts | [[agent-access-layer]], [[alert-detection]] | 01-06 | Open |
| 11 | **Core API stability + versioning policy** — when is it stable enough to build tools against; how are breaking changes managed? | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 12 | **Data-lake schema** — when does DT share it? | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 13 | **Alerting-system build ownership** — DT's role was narrowed (post-AI discussion) to a context-less "post an alert" API; nobody is currently scoped to build the alerting/detection system. Who owns it? | Inbox & Alerts | [[agent-inbox-alerts]], [[alert-detection]] | 02-06 | Open |
| 14 | **Scheduled-report failure handling** — are missed/failed runs retried, and is the user notified of a delay vs a silent drop? Assumed in [[scheduled-reporting]], not discussed. | Inbox & Alerts | [[scheduled-reporting]] | (assumption) | Open |
| 15 | **Alert priority field + multi-surface fan-out** — is there a `priority` field on the delivery payload, and do high-priority items fan out to multiple surfaces at once? Asserted in [[notification-routing]], not discussed. | Inbox & Alerts | [[notification-routing]] | (assumption) | Open |
| 16 | **AI-layer PII / data-residency / redaction** — may cardholder PII appear in chat/audit logs, and what residency + redaction policy applies? Asserted in [[audit-attribution]] beyond the grounded retention point (#6). | Access Layer | [[audit-attribution]] | (assumption) | Open |
| 17 | **AI-analysis consistency boundaries** — must the AI avoid analysing before a write settles (read-after-write guards)? Stated in [[ai-analysis-impact]] but flagged in [[vision]] §8 as a Novosapien inference. | Inbox & Alerts | [[ai-analysis-impact]] | (assumption) | Open |
| 18 | **User-defined optimization metric** — should the user set an objective the agent optimises toward, with the agent able to suggest additional objectives? Floated 13-05; not yet scoped. | Full Agentic Experience | [[full-agentic-experience]] | 13-05 | Open |
| 19 | **CRM ↔ Console data split** — exactly which client data items live only in the CRM vs are needed in the Console, and how they sync (Dorte raised). | Architecture / Internal Ops | [[architecture]], [[integrations]] | 10-06 | Open |
| 20 | **AI-ready downloadable doc file** — the Super-Ultra-designed `LLMS.txt`-style file (less than the MCP: "here's TXN, here are the endpoints"); who builds it (Stackworkz from portal data vs AI-generated) and on what release cadence. | Developer Support | [[developer-support]] | 09-06 | Open |

## Notes

- New open questions raised in any extraction go here (with a backlink), not at the bottom of a single doc.
- When a question is answered, set its status to `Answered` and record where the answer now lives.
