---
component: "[[components]]"
status: Collecting
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
---

# TXN — Internal Ops Agents

> **Component map:** [[components]] · **Vision:** [[vision]]
> **Status:** Collecting
> **Owner:** _TBC_

---

## 1. What Does This Component Do?

The **internal** component — running the TXN business itself agentically, not the client-facing surfaces. Ian Johnson (TXN's CEO) was explicit that this is part of the vision, not a side-project: the worst outcome is delivering an agentic *client* experience while the business behind it is throttled by humans doing manual work ([[vision]] §"internal operations").

Scope surfaced so far:

- **Release pipeline** — agent-drafted, business-readable release notes generated from git + Linear.
- **Documentation Engine** — auto change-logs and **self-healing docs**: production errors (Sentry) route to an agent that navigates the knowledge graph, finds the failing component, and opens a PR.
- **Ticket routing & triage** — support tickets pre-triaged and partially diagnosed before reaching a human; the human-resolved answer **feeds back into the documentation** so the next ticket of that shape never escalates.
- **Process automation** — general agentic automation of internal workflows.

> **Status: Collecting** — surfaced at the vision level and through imported UX journeys; no dedicated deep-dive yet. Scope, sub-components, and acceptance criteria are pending a focused session.

---

## Related user journeys

Imported UX journeys ([[user-journeys]]) that exercise this component:

| Journey | What it covers |
|---------|----------------|
| [[ux-ai-knowledge-base-updates\|AI Knowledge Base Updates]] | AI-suggested documentation improvements based on recurring support patterns |
| [[ux-ai-knowledge-learning\|AI Knowledge Learning]] | AI knowledge improvement through governed support-case resolution feedback |
| [[ux-ai-enhanced-authorisation-reconciliation\|AI Enhanced Authorisation Reconciliation]] | AI-assisted auth/clearing settlement reconciliation — finance/settlement analysts _(candidate for its own payment-ops scope; moved here from Fraud)_ |

_The knowledge-base / learning loop overlaps with [[developer-support]] (where the support tickets originate) — confirm the boundary in a focused session._

---

## Dependencies

- git + Linear — source for release notes
- Sentry — production-error trigger for self-healing docs
- [[developer-support]] — the support-ticket feed that powers triage and the knowledge loop

---

## Sources

- [[13-05-2026-txn-vision-meeting]] — internal-operations vision; release notes, self-healing docs, ticket triage
