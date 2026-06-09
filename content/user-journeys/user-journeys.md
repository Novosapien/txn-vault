---
type: index
status: imported
---

# TXN — User Journeys

> **Vision:** [[vision]] · **Components:** [[components]]

A library of **behavioural UX journeys** authored by **M. Moores (TXN)**, 5–6 March 2026, imported into the vault. Each journey describes how a persona moves through an AI-assisted experience end-to-end, and feeds the User Stories & Requirements that sit beneath the components.

These are **source UX material**, not component definitions — they are routed here to the components they exercise. A single journey can touch more than one component; the **Component** column gives its primary home. Mappings marked _provisional_ need confirming in a focused session.

## Journeys by component

| Journey | Component | Notes |
|---------|-----------|-------|
| [[ux-ai-guided-product-onboarding\|AI Guided Product Onboarding]] | [[co-pilot]] | Guided configuration for launching/maintaining card programmes |
| [[ux-ai-configuration-validation\|AI Configuration Validation]] | [[co-pilot]] | Real-time validation + conflict detection on config changes |
| [[ux-ai-assisted-customer-service-resolution\|AI Assisted Customer Service Resolution]] | [[co-pilot]] | In-console assistant: support explanations + recommended actions (CS persona) |
| [[ux-ai-configurable-operational-alerting\|AI Configurable Operational Alerting]] | [[agent-inbox-alerts]] | User-defined monitoring conditions → AI signal analysis → Console alerts |
| [[ux-entity-performance-insights\|Entity Performance Insights]] | [[agent-inbox-alerts]] | Automated health + behavioural insights for business / payment entities |
| [[ux-txn-Intelligence-ai-autonomous-anomaly-detection\|TXN Intelligence — Autonomous Anomaly Detection]] | [[agent-inbox-alerts]] | Anomaly detection across programmes/merchants _(overlaps [[fraud-risk-assist]])_ |
| [[ux-ai-transaction-query\|AI Transaction Query]] | [[a2a-endpoint]] | External client AI reads transaction/entity data via MCP (read path) |
| [[ux-ai-user-stories-mapping\|AI User Stories Mapping]] | [[a2a-endpoint]] | External client AI executes operational API actions via MCP governance (write path) |
| [[ux-txn-intelligence-enhanced-documentation-discovery\|Enhanced Documentation Discovery]] | [[developer-support]] | Semantic understanding + contextual ranking of Dev Portal docs |
| [[ux-ai-user-stories-and-requirements\|AI User Stories & Requirements]] | [[developer-support]] | Conversational guidance over TXN docs/KB/platform context _(provisional — could be [[co-pilot]])_ |
| [[ux-ai-user-stories-reporting\|AI User Stories Reporting]] | [[full-agentic-experience]] | AI-generated reports from conversational queries _(provisional — could be Alerts scheduled-reporting)_ |
| [[ux-ai-driven-fraud-alerts\|AI Driven Fraud Alerts]] | [[fraud-risk-assist]] | AI detection of emerging fraud patterns + merchant risk signals |
| [[ux-ai-enhanced-authorisation-reconciliation\|AI Enhanced Authorisation Reconciliation]] | [[fraud-risk-assist]] | AI-assisted reconciliation beyond rule-based matching _(provisional — could be internal ops)_ |
| [[ux-ai-knowledge-base-updates\|AI Knowledge Base Updates]] | [[internal-ops-agents]] | AI-suggested doc improvements from recurring support patterns |
| [[ux-ai-knowledge-learning\|AI Knowledge Learning]] | [[internal-ops-agents]] | Knowledge improvement via governed support-case resolution feedback |
| [[ux-ai-cost-governance\|AI Cost Governance]] | [[architecture]] | Budget monitoring, model-tier routing, deterministic fallback (cross-cutting AI infra) |

## Coverage

| Component | Journeys |
|-----------|----------|
| [[co-pilot]] | 3 |
| [[agent-inbox-alerts]] | 3 |
| [[a2a-endpoint]] (Access Layer edge) | 2 |
| [[developer-support]] | 2 |
| [[fraud-risk-assist]] | 2 |
| [[internal-ops-agents]] | 2 |
| [[full-agentic-experience]] | 1 |
| [[architecture]] (cross-cutting) | 1 |

## Provenance & status

- **Author:** M. Moores (TXN); **dates:** 5–6 March 2026; **version:** all v1.0.
- **Status:** imported as-is. Original format (Document Control headers, prose preamble) retained; vault frontmatter + a component breadcrumb were added to each so the graph is bidirectional.
- **Next:** reconcile the _provisional_ mappings, and pull each journey's User Stories / acceptance criteria down into the relevant sub-component via `/product-sub-component`.
