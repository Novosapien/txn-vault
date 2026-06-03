# TXN — Components

> **Vision:** [[vision]]

## Overview

This is the component map for **Novosapien's deliverables within the TXN product** — the agentic AI layer embedded into TXN's three product surfaces (Core API, Console, Developer Portal). The platform itself is built by other partners (see [[vision#Scope boundary]]) and is not represented here as a Novosapien component.

The map is organised by **how the AI shows up**, not by technology. The three client-facing components are lanes along TXN's trust concepts — reactive co-pilot (C1), proactive inbox (C1→C2), and full agentic (C2→C3). Beneath them: a support component, a foundational tool layer every agent rides on (which also exposes the **A2A endpoint** — the inbound door for clients' own agents), a payment-stream component (stretch), and the internal-operations agents.

Components were first surfaced in the [[13-05-2026-txn-vision-meeting|vision meeting]], re-scoped on 2026-06-01, and deep-dived across the agentic-experience sessions ([[01-06-2026-component-1-Agent-Access-Layer|Agent Access Layer]], [[02-06-2026-component-2-alerts-agent-inbox|Alerts & Inbox]], [[29-05-2026-stackworkz-meeting|Stackworkz ways-of-working]]). Each is formalised through a dedicated deep-dive.

**Status legend:**
- **Collecting** — surfaced; details still being gathered
- **Defining** — deep-dive in progress; scope drafted, acceptance criteria pending
- **Defined** — document exists with scope, sub-components, and acceptance criteria
- **Ready for build** — defined, prioritised, queued
- **In build** / **Complete** — implementation states

## Components

| Component | What it does | Status | Link |
|-----------|-------------|--------|------|
| Co-pilot | *Client-facing, C1.* Reactive in-console assistant — Q&A, inline recommendations, impact preview, guided onboarding. You drive; AI augments. | Defining | [[co-pilot]] |
| Agent Inbox & Alerts | *Client-facing, proactive C1→C2.* Event → AI analyses → surfaces. C1 actionable alert; C2 investigated plan you approve, debate, or delegate. | Defined | [[agent-inbox-alerts]] |
| Full Agentic Experience | *Client-facing, C2→C3.* The agent is the interface — do-anything, renders UI in real time, acts on approval. | Defining | [[full-agentic-experience]] |
| Developer Support | Portal + docs chatbot, scoped Q&A, defensive triage layers, feedback routing (bug / enhancement / support); machine layer (MCP / LLMS.txt) for devs' own agents. | Defining | [[developer-support]] |
| Agent Access Layer | *Foundational.* The tool surface every agent calls, scoped to the acting user's Console permissions. Wraps the Core API as agent-callable tools; exposed via MCP. **Includes the A2A endpoint** (the inbound door for clients' own external agents). | Defined | [[agent-access-layer]] |
| Fraud & Risk Assist&ast; | *Payment stream.* Real-time enrichment of the approve/decline pass-through, plus a rules engine and rule recommendations. Advise, don't decide. Data-dependent (later phase). **&ast; Stretch — only if time permits.** | Collecting | [[fraud-risk-assist]] |
| Internal Ops Agents | *Internal.* Run TXN agentically — release pipeline, Documentation Engine (auto change-logs, self-healing), ticket routing, process automation. | Collecting | [[internal-ops-agents]] |

## Parked

| Item | Why parked |
|------|-----------|
| Simulation & Evaluation | Synthetic-persona test harness and cold-start data bridge (Dorte's no-data gap). Valuable but not a launch component — revisit once a client-facing slice exists to test. |

## Architecture, not components

Infrastructure the components depend on — tracked in [[architecture]] rather than as deliverables:

- **Data & insight layer** — data-lake query, pre-compute / memory store, scheduled analysis that feeds the alerts and the agents. *Scope open: ours / DT / shared.*
- **Cross-program benchmarking** — "five programmes in your sector do X" recommendations; surfaces through Co-pilot and the Inbox. Depends on data volume (the flywheel).

## Out of scope for Novosapien

These are part of the TXN product but built by other partners. They appear here as **context** — Novosapien's components integrate with them but do not deliver them.

| Component | Built by | Reference material |
|-----------|---------|--------------------|
| Core API / card-system backend | **Direct Transact (DT)** — TXN's internal dev partner | Core API documentation (from TXN) |
| TXN Console (frontend + back-end-for-frontend) | **Stackworkz** (frontend design by **Super Ultra**) | Console design prototype documentation |
| Developer Portal (site + Umbraco headless CMS) | **Stackworkz** | Developer portal site documentation |
| Data Lake | **Direct Transact (DT)** | _(schema input from Novosapien for AI consumption)_ |
