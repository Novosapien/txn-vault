---
component: "[[components]]"
status: Defined
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[01-06-2026-component-1-Agent-Access-Layer]]"
  - "[[29-05-2026-stackworkz-meeting]]"
---

# Agent Access Layer

> **Component map:** [[components]] · **Vision:** [[vision]]

## Overview

The Agent Access Layer is the **foundational tool surface** that lets any agent act on TXN's capabilities. It wraps the Core API as agent-callable tools, scoped to the acting user's permissions, and exposes them via the Model Context Protocol (MCP). It is not an experience the client sees — it is the substrate every experience rides on.

Every other client-facing component consumes it:

- **[[co-pilot]]** — to answer questions and, later, take actions.
- **[[agent-inbox-alerts]]** — to investigate triggers and execute approved plans.
- **[[full-agentic-experience]]** — to do anything the user asks; its A2A endpoint lets a client's *own* agent reach the same tools.
- **[[fraud-risk-assist]]** — to read transaction state and write rule changes.

If the Agent Access Layer is wrong, every agent is wrong. That is why it is the first deep-dive — but note it is also the component most dependent on materials and decisions that sit with TXN (see Dependencies).

## Scope

**The Agent Access Layer IS:**

- The catalogue of agent-callable tools mapped from the Core API (issue card, suspend card, configure product, query transactions, etc.)
- The permission model that scopes each tool call to what the acting user is allowed to do in the Console
- The MCP server that exposes those tools to TXN's own agents and to external LLMs (Claude, etc.)
- The routing of any action that requires sign-off into the Console's existing approval queue

**The Agent Access Layer IS NOT:**

- The **Core API** itself — built by TXN's dev team; we wrap it, we don't build it
- The **agent that decides which tools to call** — that intelligence lives in the consuming components ([[co-pilot]], [[agent-inbox-alerts]], [[full-agentic-experience]])
- The **A2A protocol surface** — the external agent-to-agent face lives in [[full-agentic-experience]]; this layer only provides the tools it exposes
- The **data lake** — built by DT; the layer reads from it but does not own it

## Sub-components

| Sub-component | What it does | Status | Link |
|---------------|-------------|--------|------|
| MCP server (validation & execution) | Single monolith MCP server; per-turn tool gating, server-side validation, Core API execution with self-correcting errors | Defined | [[mcp-server]] |
| Permission & authorization scoping | Resolves identity and computes the per-turn exposed tool set; mirrors the Console's granular permission model | Defined | [[permission-scoping]] |
| Approval-queue integration | Prompted-trust + two-person approval for product/multi-card changes; privileged single-card actions execute directly | Defined | [[approval-queue-integration]] |
| Audit & attribution | Combined console + API + chat trail that makes "prompted trust" provable; dispute reconstruction | Defined | [[audit-attribution]] |
| Tool catalogue | Business-language tools mapped from the Core API endpoints; exact list gated on full API docs | Collecting | [[tool-catalogue]] |

## Dependencies — what we need from TXN

This component cannot be fully specced without:

- **Core API documentation + YAML spec** — the source for the tool catalogue
- **API stability + breaking-change / versioning policy** — when is it stable enough to build tools against, and how are breaking changes managed?
- **The Console's granular permission model** (from **Stackworkz** — it lives in their back-end-for-frontend, not the Core API) — to mirror role → tool-permission mapping
- **Approval-queue mechanics** (from **Stackworkz**) — so AI-initiated actions route correctly
- **Data-lake schema** (from DT) — what the tools can read for grounding

## Decisions from the 01-06 deep-dive

**DT Core API shape (Mike Moores, TXN CTO).** The endpoints to wrap as tools: **card holder** (the person), **card holder groups** (logical grouping — business / tier / rewards), **account** (the balance that drives approve/decline; may or may not sit on TXN), **card** (linked to an account; PAN + security; per-card overrides like contactless/online off), **product** (the configuration template — *~200 fields* controlling look, expiry, what can transact), plus **reporting** endpoints (extent still TBC). Split into **platform-management** (infrequent, e.g. product — "once per country per year") vs **day-to-day operational** (e.g. issue/suspend a card, hit by a banking app). The product/configuration layer is the **highest-value AI target** — "how can we say, this is what 90% of people do."

**Permission architecture (three stores).** (1) **DT API keys** at *program* level — `read` / `write` / `program-manager` (config); read+write always granted, program-manager sometimes withheld contractually. (2) **Stackworkz Console back-end** holds the *granular user* permissions (role-based, very flexible; e.g. suspend-a-card vs terminate-a-card). (3) For AI **outside** the Console (MCP / Claude / A2A) there is **no permission API today** — TXN will build an **AI-specific permission config** (Super Ultra designed a screen) that mirrors the Console model at org + user level. The **client is always a super-user**; sub-users get subsets — so the layer only ever needs to check the **user ID**.

**Validation — three layers, server authoritative.** Agent → **MCP server-side validation** (a single "monolith" MCP server gates which tools are exposed per user/turn, via a universal API key + user-ID + the user's permissions passed in the payload — "functional", not "the agent decides") → **Core API** as the authoritative backstop (rejects unpermitted calls with fully-formatted errors the agent reads and self-corrects). The 1-in-1,000 bad call must fail at the server, not rely on agent context.

**Approval queue — approval is itself a permission.** Two-person rule: even an approver needs someone else to approve. Cut line: **anything product-level / affecting multiple cards needs approval**; terminating a single card is *privileged* but not approval-gated (one-card blast radius). The agent routes an approval request to the **named approver**, including the note that an AI agent recommended it (Dorte Dye's point — keeps the audit trail consistent); the approver becomes the initiator of the action.

**Audit — combined and provable.** A single trail across **Console** (clicked/navigated/read), **Core API** (executed this, by this identity — AI gets its own attributed identity), and **AI chat** (the user said "yes"). Entity **transitions** (card/account/holder state changes) are logged with their lifecycle. This is what makes "**prompted trust**" provable when a client later disputes a change ("we prompted, you confirmed"). Brett proposed pushing it into the data warehouse / knowledge-graph audit store. Retention/size TBD.

**Product webhook (to request from DT).** DT to add a product/config webhook so that **any** change — Console, API, or AI — emits an event the AI can react to and pull back into one place. Underpins [[agent-inbox-alerts]] change-impact.

## Open questions — raise with TXN

- **MCP-server ownership split** (from [[29-05-2026-stackworkz-meeting]]) — two distinct MCP servers are in play with different likely owners:
  - a **docs / dev-portal MCP** (consumes documentation, `LLMS.txt`) that **Stackworkz wants to own**, "regardless of scope" — this may *remove* surface area from Novosapien here;
  - a **card-acquiring-API MCP** (exposes/executes against the production Core API) whose ownership is **unresolved** — possibly Direct Transact (DT).
  Resolve who builds which, and avoid building duplicate MCP servers that do the same thing (one reusable server should serve internal + external agents).
- **One MCP server or several?** Leaning toward a single "monolith" MCP with per-turn tool gating (see Decisions) rather than semantically-bucketed servers — to confirm as tool count grows.
- **AI-permission config** — TXN needs to build the org/user permission mirror for non-Console access (no API today; Super Ultra designed a screen). When, and owned by whom?
- **Product webhook** — will DT add it, and on what timeline?
- **API stability + versioning policy** — when is the Core API stable enough to build tools against; how are breaking changes managed? *(Open.)*
- **Data-lake schema availability** — when does DT share it? *(Open.)*
- **Audit retention & storage** — how much chat/transition history is kept, where, and for how long?

_Resolved in the 01-06 deep-dive (see Decisions): permission source of truth (universal key + user-ID + payload permissions, server-validated); role→tool mapping (Console/Stackworkz is the source, mirrored by the AI permission config)._

## Acceptance criteria

_Pending sub-component deep-dives. To be defined per sub-component (tool-catalogue coverage, permission-parity tests, approval-queue routing tests)._

## Sources

- [[13-05-2026-txn-vision-meeting]] — MCP / permission-scoping discussion (~00:57–01:06); approval-queue (~01:35–01:37)
- [[01-06-2026-component-1-Agent-Access-Layer]] — DT API shape; permission architecture; three-layer validation; approval-as-permission + two-person rule; combined audit; product webhook (full session)
- [[29-05-2026-stackworkz-meeting]] — MCP-server ownership split (~00:13–00:16); permissions live in Stackworkz BFF (~00:10)
