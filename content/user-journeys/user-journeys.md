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
| [[ux-ai-user-stories-and-requirements\|AI User Stories & Requirements]] | [[developer-support]] | Read-only conversational doc/KB guidance across Portal, website + Console _(overlaps [[co-pilot]] for the in-Console slice)_ |
| [[ux-ai-user-stories-reporting\|AI User Stories Reporting]] | [[agent-inbox-alerts]] | NL reports in Console, saved + reusable (scheduled-reporting); conversational ask via [[co-pilot]] |
| [[ux-ai-driven-fraud-alerts\|AI Driven Fraud Alerts]] | [[fraud-risk-assist]] | AI detection of emerging fraud patterns + merchant risk signals |
| [[ux-ai-enhanced-authorisation-reconciliation\|AI Enhanced Authorisation Reconciliation]] | [[internal-ops-agents]] | Auth/clearing settlement reconciliation; finance/settlement personas _(candidate for its own payment-ops scope)_ |
| [[ux-ai-knowledge-base-updates\|AI Knowledge Base Updates]] | [[internal-ops-agents]] | AI-suggested doc improvements from recurring support patterns |
| [[ux-ai-knowledge-learning\|AI Knowledge Learning]] | [[internal-ops-agents]] | Knowledge improvement via governed support-case resolution feedback |
| [[ux-ai-cost-governance\|AI Cost Governance]] | [[architecture]] | Budget monitoring, model-tier routing, deterministic fallback (cross-cutting AI infra) |

## Coverage

| Component | Journeys |
|-----------|----------|
| [[co-pilot]] | 3 |
| [[agent-inbox-alerts]] | 4 |
| [[internal-ops-agents]] | 3 |
| [[a2a-endpoint]] (Access Layer edge) | 2 |
| [[developer-support]] | 2 |
| [[fraud-risk-assist]] | 1 |
| [[architecture]] (cross-cutting) | 1 |
| [[full-agentic-experience]] | 0 — scope from the deep-dive; no imported journey (reporting's co-work scheduling overlaps here) |

## Provenance & status

- **Author:** M. Moores (TXN); **dates:** 5–6 March 2026; **version:** all v1.0.
- **Status:** imported as-is. Original format (Document Control headers, prose preamble) retained; vault frontmatter + a component breadcrumb were added to each so the graph is bidirectional.
- **Mappings reconciled (9 Jun):** Reporting → [[agent-inbox-alerts]], Reconciliation → [[internal-ops-agents]], User Stories & Requirements confirmed [[developer-support]] (Co-pilot overlap). Reconciliation flagged as a candidate for its own payment-ops scope; Anomaly Detection stays in Alerts with Fraud as analytical source.
- **Next:** pull each journey's User Stories / acceptance criteria down into the relevant sub-component via `/product-sub-component`.
