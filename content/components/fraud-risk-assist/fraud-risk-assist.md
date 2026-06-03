---
component: "[[components]]"
status: Collecting
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[02-06-2026-component-2-alerts-agent-inbox]]"
---

# TXN — Fraud & Risk Assist&ast;

> **Component map:** [[components]] · **Vision:** [[vision]]
> **Status:** Collecting · **&ast; Stretch — only if time permits**
> **Owner:** _TBC_

> [!note] Stub — stretch component, not yet scoped
> Marked stretch (&ast;): in scope only if time allows. Surfaced in the [[vision]] but not deep-dived. The summary below is from the vision and component map; no detailed scope yet, and it is data-dependent (a later phase). Open questions tracked in [[open-questions]].

## Overview

Real-time enrichment of the approve/decline transaction pass-through, plus a rules engine and rule recommendations. The load-bearing principle from the [[vision]]: **advise, don't decide** — TXN signals, the client owns the fraud decision and tells TXN what was fraud after the fact.

Threads surfaced so far (from the vision, not deep-dived):

- **Real-time enrichment** of the approve/decline pass-through.
- **Rules engine + rule recommendations** — propose controls, don't enforce.
- **Data-dependent** — relies on transaction volume accumulating (the data flywheel); a later phase.

May surface a fraud flag *into* [[agent-inbox-alerts]], but services the action on its own dedicated page.

## Status

Stretch component — only if time permits. Not yet scoped. See [[open-questions]].
