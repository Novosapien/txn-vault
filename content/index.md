# TXN

> **Client:** TXN
> **Status:** Discovery
> **Date started:** 2026-05-17

## Overview

TXN is a card issuing platform (issuer processor) delivered through three product surfaces — Core API, TXN Console, and Developer Portal. **Novosapien's scope** is the agentic AI layer that powers every human and agent-facing interaction across all three surfaces. TXN's platform itself is built by other partners; see [[vision#Scope boundary]] for the delivery split. Current phase: **discovery** — vision fully drafted from the 13 May 2026 workshop; component deep-dives next.

___

## Documents

| Document | Description | Status |
|----------|------------|--------|
| [[vision]] | Product vision — what we're building and why | Draft complete (all 8 §§); per-section gaps inline |
| [[architecture]] | Cross-cutting technical decisions — tech stack, infrastructure, integrations | Integrations collecting (build-partner stack) |
| [[components]] | Component map — Novosapien's deliverables within the TXN product | 7 top-level components; Access Layer, Alerts, Co-pilot, Full Agentic, Developer Support **defined**; Internal Ops **defining**; Fraud collecting; A2A folded into the Access Layer as its external edge |
| [[user-journeys]] | Behavioural UX journeys (M. Moores, Mar 2026) routed to the components they exercise | 16 journeys imported + cross-linked; provisional mappings to reconcile |

## External Resources

_Client-provided materials, design artifacts, research, and data that live outside the vault. Link to Google Drive folders or other external locations._

| Resource | Location | Notes |
|----------|----------|-------|
| | | |

## Recent Activity

_Updated as work progresses. Most recent first._

| Date | What happened |
|------|--------------|
| 2026-06-10 | [[developer-support]] taken to buildable sub-component depth — **all 5 Defined** with entity journeys + acceptance criteria: [[docs-mcp-server]], [[portal-co-pilot]], [[sandbox-assist]], [[support-triage]], [[access-gating]]. Sourced from the deep-dive + the Documentation Discovery / User Stories journeys. |
| 2026-06-10 | [[internal-ops-agents]] built out from the vision + the Developer Support hand-off + its 3 journeys → **Defining**. Centrepiece is the **knowledge engine** (self-healing docs, reactive capture from unresolved cases, proactive pattern-mining — all human-approved, re-indexed); plus release pipeline, support triage/resolution, process automation, simulation, and (provisional) settlement reconciliation. No dedicated deep-dive yet — a session must confirm the dev-support boundary, reconciliation's home, and simulation timing. |
| 2026-06-09 | [[developer-support]] deep-dive ([[09-06-2026-developer-support]]) processed → **Defined**. Four-level access spine (unknown → signed-up → prospect → client); the strategic bet is a **hosted docs MCP server** over the portal co-pilot; support triage packages well-formed tickets (resolution in [[internal-ops-agents]]); API-key lead-gen + per-key rate limits. Session also confirmed, client-side, that A2A folds into [[agent-access-layer]]. |
| 2026-06-09 | [[agent-inbox-alerts]] swept against its 4 UX journeys — all covered by the existing 5 sub-components; journey-source cross-links added; [[scheduled-reporting]] enriched with on-demand NL reports + reusable templates (the one genuine gap). |
| 2026-06-09 | [[co-pilot]] fully decomposed — **all 6 sub-components Defined** to buildable depth with entity journeys + acceptance criteria: [[conversational-qa]], [[impact-preview]], [[guided-configuration]], [[guided-onboarding]], [[action-on-confirmation]], [[process-surfacing]]. First three from their UX journeys; latter three from the deep-dive. |
| 2026-06-09 | 16 UX [[user-journeys]] integrated + cross-linked; provisional mappings reconciled (Reporting→Alerts, Reconciliation→Internal Ops). Collecting stubs created for [[fraud-risk-assist]] and [[internal-ops-agents]] (repaired dangling links). |
| 2026-06-09 | [[co-pilot]] and [[full-agentic-experience]] deep-dives processed — both now **Defined**. Co-pilot gains the four-level graduation model + page-scoped-execution / hand-off boundary; Full Agentic gains the specialised multi-agent core, merged-journey value, and the "expose the agent, not the tools" A2A/MCP mechanism. **A2A Endpoint folded into [[agent-access-layer]]** as its external edge ([[a2a-endpoint]] relocated from a top-level component to a sub-component) — map now **7 top-level components**. Sources: [[04-06-2026-component-3-co-pilot]], [[05-06-2026-component-4-full-agentic-experience]]. |
| 2026-06-02 | [[agent-inbox-alerts]] taken to buildable depth — 5 sub-components with entity journeys + acceptance criteria: [[alert-detection]], [[ai-analysis-impact]], [[plan-and-execute]], [[scheduled-reporting]], [[notification-routing]]. Component now **Defined**. |
| 2026-06-02 | [[agent-access-layer]] taken to buildable depth — 5 sub-components with entity journeys + acceptance criteria: [[mcp-server]], [[permission-scoping]], [[approval-queue-integration]], [[audit-attribution]] (new 5th), [[tool-catalogue]] (gated on full API docs). Component now **Defined**. |
| 2026-06-02 | Full agentic-experience scope captured across Console, Developer Portal, and A2A (phasing deliberately excluded). New component docs: [[co-pilot]], [[agent-inbox-alerts]], [[developer-support]], [[a2a-endpoint]] (promoted from a sub-component); [[full-agentic-experience]] and [[agent-access-layer]] enriched. Sources: [[01-06-2026-component-1-Agent-Access-Layer]], [[02-06-2026-component-2-alerts-agent-inbox]]. Map now 8 components. |
| 2026-06-02 | Digested [[29-05-2026-stackworkz-meeting]]: build partners named — **Stackworkz** (Console + Dev Portal), **Super Ultra** (design), **Direct Transact** (Core API + Data Lake). Stack/infra captured in [[integrations]]; MCP-ownership split logged on [[agent-access-layer]]. Timeline: **Dev Portal + API target October**, Console a fast-follow. |
| 2026-06-01 | Component map re-scoped 6 → 7 along the trust-concept spine ([[components]]); Agent Access Layer deep-dive started. Transaction primer added to [[vision]] §1. |
| 2026-05-17 | Vision draft complete across all 8 sections — extracted from [[13-05-2026-txn-vision-meeting]]. 6 Novosapien-scope components surfaced in [[components]]. Per-section gap lists ready for the next TXN conversation. |
| 2026-05-17 | Vault created |
