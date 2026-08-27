---
date: 2026-08-26
type: general
description: "Record of the 2026-08-26 session with Stackworkz: a demonstration of the agent interface and the opening of the code-sharing plan between the two build teams"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-access-layer]]"
  - "[[integrations]]"
status: partially-extracted
extracted-to:
  - "[[delivery]]"
  - "[[open-questions]]"
---

# TXN: Stackworkz agent interface demonstration (2026-08-26)

> **Source:** Brett's account, 27 August 2026. **No transcript was captured for this session**, so this record is a note rather than an extraction, and the detail below is deliberately thin. It is filed because the session opens a dependency that nothing else in the vault carries.
> **Parties:** Novosapien and **Stackworkz**. Prior ways-of-working session: [[29-05-2026-stackworkz-meeting]].
> **Delivery:** [[delivery]]

## What happened

Two things.

1. **The agent interface was demonstrated to the Stackworkz team.** This is the first time the built agentic surface has been shown to the partner who owns the Console it eventually has to live inside.
2. **A plan was opened for how code is shared between Novosapien and Stackworkz.** How the agentic experience moves out of Novosapien's own React build and into the Stackworkz Console.

## Why this matters more than it looks

The pilot has always run on Novosapien's own surface. `txn-console-react` is a full React build of the Control Center that Novosapien produced so the agentic experiment had something real to drive. **Stackworkz builds the production Console and the Developer Portal**, in C#/.NET with React and Material UI on their own infrastructure, as recorded in [[29-05-2026-stackworkz-meeting]] and [[integrations]].

Every previous plan has treated the wire-in as a **Direct Transact problem**: real APIs, the data lake, the architecture decision. It is also a **Stackworkz problem**, and that half has had no named mechanism until now. Two long-standing register rows depend on it:

- **[[open-questions]] #33**, Console instrumentation depth. Stackworkz has to expose page state, component identifiers and action handlers before the co-pilot can drive the Console, and no caching requirements have ever been given to them.
- **[[open-questions]] #35**, the component library handle. The agent renders by passing arguments to Stackworkz's pre-built components rather than generating component code, so the two component sets have to agree.

A code-sharing plan is the first thing that makes either of those actionable rather than theoretical.

## What is not yet decided

Recorded as unknown rather than guessed:

- Whether the agentic surface is **handed over as code** for Stackworkz to absorb into the Console, **consumed as a service** by the Console, or **kept as a separate surface** that the Console links to.
- Which repository the shared code lives in, and who merges to it.
- How the two release cadences reconcile. Novosapien deploys on push to `main`; Stackworkz run a DevOps pipeline onto VMs.
- Whether any of this lands before or after pilot acceptance on 7 September.

## Post-call analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Agent interface demonstrated to Stackworkz, first time | [[delivery]] | Recorded |
| Code-sharing plan opened, mechanism undecided | [[open-questions]] | New row #61 |
| Partially de-risks the wire-in phase on the Stackworkz side | [[delivery]] | Recorded in the forward plan |
| No transcript captured | this record | Get the follow-up session recorded so it can be digested properly |
