---
component: "[[components]]"
status: Collecting
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
---

# TXN — Fraud & Risk Assist

> **Component map:** [[components]] · **Vision:** [[vision]]
> **Status:** Collecting
> **Owner:** _TBC_

---

## 1. What Does This Component Do?

The **payment-stream** component: real-time enrichment of the approve/decline pass-through, plus a rules engine and AI **rule recommendations**. The guiding principle is **advise, don't decide** — the AI surfaces risk signals, emerging fraud patterns, and recommended controls, but the authoritative approve/decline decision stays in the payment rail. It is **data-dependent** and therefore a **later phase**: it needs accumulated transaction history before it can detect patterns (the data flywheel in [[vision]] §"data flywheel"). At launch there is nothing to analyse.

It surfaces its findings through the proactive [[agent-inbox-alerts]] surface rather than being a screen of its own, and reads transaction state through the [[agent-access-layer]].

> **Status: Collecting** — surfaced at the vision level and through imported UX journeys; no dedicated deep-dive yet. Scope, sub-components, and acceptance criteria are pending a focused session.

---

## Related user journeys

Imported UX journeys ([[user-journeys]]) that exercise this component:

| Journey | What it covers |
|---------|----------------|
| [[ux-ai-driven-fraud-alerts\|AI Driven Fraud Alerts]] | AI detection of emerging fraud patterns and merchant risk signals across programmes |
| [[ux-ai-enhanced-authorisation-reconciliation\|AI Enhanced Authorisation Reconciliation]] | AI-assisted reconciliation improving match accuracy beyond rule-based matching _(mapping provisional — could sit with internal ops)_ |

---

## Dependencies

- [[agent-access-layer]] — read transaction state, write rule changes
- [[agent-inbox-alerts]] — the surface that delivers risk signals to the user
- Data Lake (DT) — transaction history the analysis depends on (not available until volume accumulates)

---

## Sources

- [[13-05-2026-txn-vision-meeting]] — payment-stream / advise-don't-decide framing
