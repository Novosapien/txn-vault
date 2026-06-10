# TXN — Architecture

> **Project:** [[index]]
> **User journeys:** [[ux-ai-cost-governance|AI Cost Governance]] (cross-cutting AI-infra concern) — see [[user-journeys]]

Cross-cutting technical decisions that affect the whole product. This directory covers tech stack choices, infrastructure, and third-party integrations.

## Sections

| Section | What it covers | Status | Link |
|---------|---------------|--------|------|
| Integrations | Third-party services, APIs, data feeds, build-partner environments | Collecting | [[integrations]] |

## Decisions

_Cross-cutting calls made in client sessions._

- **CRM (Freshsales) is the system of record for client data** _(Ian, [[10-06-2026-developer-support-and-internal-ops]])._ Everything client-related lives in the CRM; the Console receives the data it needs *sent* to it, rather than context being split across systems or written directly to the Console. Flat documents are avoided — they limit how the data items can be reused. Shapes what [[internal-ops-agents]] (customer onboarding) writes to, and what [[agent-access-layer]] / the Console read.
- **TXN runs its own operations through the agentic experience + Teams, not bespoke Console admin UI** _(Ian, same session)._ TXN-as-user accesses AI-driven information through the Claude-like experience ([[full-agentic-experience]]) and receives alerts in Teams; do **not** build more AI-management software into the Console. Affects where internal alerts/reviews surface and keeps the Console from bloating.
- **Documentation is hosted in two stores** _(Mike, same session)._ The **DT YAML** is the source for the API reference (the same API the portal renders); **guides + change log live in Umbraco** (headless CMS, API-accessible). The AI reads both; Umbraco supports **edit-via-API in draft mode** for the [[internal-ops-agents]] knowledge engine.

## Open Questions

Tracked centrally in the [[open-questions]] register. Architecture-level items currently open include the site-wide LLM owner (#3), the MCP-ownership split (#8), the CRM ↔ Console data split (#19), the AI-ready downloadable doc file (#20), and AI data-access / dev-environment questions (see [[integrations]]).
