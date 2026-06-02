---
component: "[[components]]"
status: Defining
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
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

| Sub-component | What it does | Status |
|---------------|-------------|--------|
| Tool catalogue | Maps Core API endpoints into agent-callable tools with business-language descriptions | Collecting |
| Permission & authorization scoping | Mirrors the Console's granular permission model so an agent can only do what its user can | Collecting |
| MCP server | The Model Context Protocol server exposing the tools to internal and external agents | Collecting |
| Approval-queue integration | Routes sign-off-required actions through the Console's existing multi-user approval flow | Collecting |

## Dependencies — what we need from TXN

This component cannot be fully specced without:

- **Core API documentation + YAML spec** — the source for the tool catalogue
- **API stability + breaking-change / versioning policy** — when is it stable enough to build tools against, and how are breaking changes managed?
- **The Console's granular permission model** (from the console build team) — to mirror role → tool-permission mapping
- **Approval-queue mechanics** (from the console build team) — so AI-initiated actions route correctly
- **Data-lake schema** (from DT) — what the tools can read for grounding

## Open questions — raise with TXN

- **One layer or two?** Do TXN's own agents call the same MCP server, or call the Core API tools directly, with MCP only for external consumers?
- **Who owns the role → tool-permission mapping?** (Dorte's question in the vision call — aligning our model with theirs.)
- **Permission source of truth** — does the layer read live Console permissions per call, or hold its own copy?
- **API stability timeline** — gates when build can start.
- **Data-lake schema availability** — when does DT share it?

## Acceptance criteria

_Pending sub-component deep-dives. To be defined per sub-component (tool-catalogue coverage, permission-parity tests, approval-queue routing tests)._

## Sources

- [[13-05-2026-txn-vision-meeting]] — MCP / permission-scoping discussion (~00:57–01:06); approval-queue (~01:35–01:37)
