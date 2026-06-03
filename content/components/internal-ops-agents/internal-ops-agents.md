---
component: "[[components]]"
status: Collecting
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[29-05-2026-stackworkz-meeting]]"
---

# TXN — Internal Ops Agents

> **Component map:** [[components]] · **Vision:** [[vision]]
> **Status:** Collecting
> **Owner:** _TBC_

> [!note] Stub — not yet scoped
> Surfaced in the [[vision]] but not yet deep-dived. The summary below is lifted from the vision and component map; there is no detailed scope, sub-components, or acceptance criteria yet. Open questions tracked in [[open-questions]].

## Overview

Running TXN itself agentically, so the business behind the agentic client experience isn't throttled by manual work. Ian Johnson (TXN's CEO) framed this as part of the vision, not a side-project — the worst outcome being an agentic client experience bottlenecked by humans doing manual work behind it.

Threads surfaced so far (from the vision, not deep-dived):

- **Release pipeline / change-logs** — release notes auto-drafted by an agent reading git + Linear, in business-readable English.
- **Documentation Engine (self-healing docs)** — production errors (e.g. via Sentry) route to an agent that navigates the knowledge graph, identifies the failing component, and opens a PR.
- **Ticket routing / triage** — support tickets pre-triaged and partially diagnosed before reaching a human queue; the human-resolved answer feeds back into the docs.
- **Process automation** — general internal-operations automation.

Receives classified feedback items (bug / enhancement / support) from [[developer-support]].

## Status

Not yet scoped to buildable depth — to be taken through a dedicated deep-dive. See [[open-questions]].
