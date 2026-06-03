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
| 3 | **Site-wide LLM ownership** — 29 May named **Teraflow** (not Novosapien) for the site-wide/agentic AI. Is Teraflow a distinct party or an alias, and who provides this LLM? | Developer Support | [[developer-support]] | 29-05 | Open |
| 4 | **System-defined alert corpus** — which alerts is TXN obliged to raise? (Specifics not defined; the focus so far is the *handling process*, not the catalogue.) | Inbox & Alerts | [[alert-detection]], [[agent-inbox-alerts]] | 02-06 | Open |
| 5 | **Idempotency** on mutating MCP calls — assumed, not discussed. Confirm the requirement. | Access Layer | [[mcp-server]] | (assumption) | Open |
| 6 | **Audit immutability / append-only + retention** — assumed immutable; retention window and storage location undecided. | Access Layer | [[audit-attribution]] | 01-06 | Open |
| 7 | **Notification delivery** — fallback/retry on failure and a default channel were assumed, not discussed. Confirm. | Inbox & Alerts | [[notification-routing]] | (assumption) | Open |
| 8 | **MCP-server ownership split** — docs/dev-portal MCP (Stackworkz wants it) vs card-acquiring-API MCP (owner unresolved, maybe DT). Who builds which; avoid duplicates. | Access Layer | [[agent-access-layer]] | 29-05 | Open |
| 9 | **AI-permission config** — TXN must build the org/user permission mirror for non-Console access (no API today). When, and owned by whom? | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 10 | **Product webhook** — will DT add it, and on what timeline? (Underpins change-impact alerts.) | Access Layer / Inbox & Alerts | [[agent-access-layer]], [[alert-detection]] | 01-06 | Open |
| 11 | **Core API stability + versioning policy** — when is it stable enough to build tools against; how are breaking changes managed? | Access Layer | [[agent-access-layer]] | 01-06 | Open |
| 12 | **Data-lake schema** — when does DT share it? | Access Layer | [[agent-access-layer]] | 01-06 | Open |

## Notes

- New open questions raised in any extraction go here (with a backlink), not at the bottom of a single doc.
- When a question is answered, set its status to `Answered` and record where the answer now lives.
