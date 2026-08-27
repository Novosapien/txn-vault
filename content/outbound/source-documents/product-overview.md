---
description: "TXN GTM Product Overview v1.0: what the platform is, what is live at MVP across API, Console, Intelligence and Developer Portal, and what comes later"
---

# Product Overview v1.0

> **Section:** [[source-documents]]
> **Author:** Ian Johnson, TXN Global. Delivered 24 August 2026.
> **Original:** `originals/TXN_GTM_Product_Overview_v1.0.docx`
> **Status:** verbatim conversion of the file as delivered. Not edited, not summarised. Where the conversion and the original disagree, the original governs.

Capabilities are marked as live at MVP or as later phases. Performance and availability figures are engineered targets, not production-proven, and must be presented as such.

---

TXN GLOBAL

Product Overview

The TXN issuer-processing platform: what it is, what clients achieve, and what is live at launch

Version: v1.0 (first populated release, supersedes the v0.1 scaffold)

Owner: Ian Johnson (ianj@txn.global) · Prepared 16 July 2026

Sources: 02_Product (Platform Vision MVP to Phase 2, AI Adoption Framework, and the TXN API, Console, Developer Portal and Intelligence product briefs and visions) and 07_GTM Core Messaging v2.5.

Claim discipline: *TXN is pre-launch. Capabilities are marked as live at MVP or as later phases. Performance and availability figures are engineered platform targets, not yet production-proven, and should be presented as such until validated.*

## 1. What TXN is

TXN is a next-generation issuer-processing platform. It is the infrastructure behind card programs: card issuance, real-time transaction processing and decisioning, authentication and settlement, and card and account lifecycle management. TXN gives European fintechs, digital banks, embedded finance companies and other card program owners the control, speed and resilience to launch and scale card programs without the usual trade-off between flexibility and reliability.

TXN is a platform, not a single product. It is designed for multiple programs, multiple tenants and multiple regions from the start, and it removes the complexity of running a card program so teams do not need card experts on staff to operate one.

The anchor: *“Intelligence built in. Complexity taken out.”*

Processing reliability comes from 25 years of proven heritage held through ownership: Direct Transact, our co-founding owner, contributes the processing track record and scheme certifications, and Paycorp, our co-founding owner, contributes international payments experience and market reach.

### What TXN is not

Being clear on the boundary keeps the proposition sharp. TXN is not a consumer-facing banking application, not an acquiring or merchant platform, and not a one-size-fits-all issuer product. It enables others to build, operate and scale card products; it does not compete with them for the end customer.

## 2. The platform at a glance

TXN is built as four decoupled components. Each is a first-class product surface, and each can evolve without forcing change on the others. Clients choose the mix that suits them, from full API automation to a self-serve operator console.

| Component | What it is |
|---|---|
| TXN API | The machine-to-machine surface and the stable contract layer of the platform. All core functionality is available through the API before it appears in any screen. Behaviour is deterministic: the same inputs always produce the same outcome. |
| TXN Console | The self-serve operator console: the human-facing surface for onboarding, program configuration, card and cardholder servicing, monitoring, approvals and audit, with role-aware access throughout. |
| TXN Intelligence | The cross-cutting intelligence layer. AI assists people and automates routine work under governance and audit, running alongside the platform rather than inside the real-time transaction path. Intelligence is the mechanism that removes complexity; it is not the identity of the product. |
| TXN Developer Portal | The self-service surface where developers discover, test and integrate the TXN API: live documentation generated from the API itself, an interactive explorer, and sandbox testing. |

### What clients achieve

The proposition leads with outcomes, not technology. With TXN a client can:

- Run a card program without employing card experts, because the platform and its intelligence layer remove the specialist work.
- Launch in weeks rather than quarters, and scale without rewrites.
- Keep full control of authorisation and spend, with transparency into why every transaction was approved, declined or controlled.
- Protect unit economics as volume grows, with clear and predictable pricing.
- Meet scheme and regulatory requirements as a delivered outcome rather than a burden carried in-house.

## 3. What is live at launch (MVP)

This section sets out the demonstrable day-one capability set, by component. It is the basis for what Sales can show and commit at launch. Items beyond this scope are covered in section 4 and must be treated as directional, not day-one.

### 3.1 Platform and API

The API delivers end-to-end issuer processing programmatically, so a client can run a program without relying on manual steps.

| Capability | What it does |
|---|---|
| Program configuration and lifecycle | Set up and operate card programs through the API, with configuration rather than bespoke code driving behaviour. |
| Card issuance and lifecycle | Create, activate and manage virtual, tokenised and physical cards across their full lifecycle. |
| Cardholder, account and business entities | Create and manage cardholders, funding accounts and business (cardholder group) structures, with KYC and KYB. |
| Real-time authorisation and decisioning | Authorise, clear, settle and reconcile transactions, with the client able to apply their own decision logic in real time. |
| Spend and merchant controls | Apply policy-driven limits by amount, frequency, merchant category, geography and transaction type during authorisation. |
| Tokenisation and digital wallets | Manage tokenised card credentials in digital wallets as first-class entities with their own lifecycle and risk context. |
| 3DS authentication | Deliver 3DS 2.x authentication and PSD2 SCA through an integrated access control server. |
| Fee management | Configure and apply issuer-side fees across the card lifecycle. |
| BIN and program routing | Structure and allocate BINs and BIN ranges across BIN sponsor, program owner and issuer-processor roles, and route transactions to the correct program. |
| Physical card fulfilment | Coordinate card production, provider integration, shipment tracking and delivery confirmation. |
| Secure data display | Let cardholders view sensitive data such as PAN, CVV and PIN without bringing client systems into PCI scope. |
| Multi-tenant, multi-program isolation | Run many programs across many owners with strict isolation on shared, scalable infrastructure. |
| Events, webhooks and reporting hooks | Event-driven integration, reconciliation and reporting for downstream systems. |
| Secure access | OAuth 2.0 client-credentials with scoped tokens, and mutual TLS for high-assurance integrations, with full audit logging. |

### 3.2 TXN Console (operator console)

The Console gives operators a single, role-aware place to run and oversee programs, replacing fragmented tools and spreadsheets. The MVP is organised around program owner, BIN sponsor, customer service and TXN internal views.

| Area | What is live at MVP |
|---|---|
| Dashboards and search | Overview dashboards with KPI tiles, universal search, alerts and actions, recent activity, and an editable dashboard. |
| Program configuration | View, edit and add program controls; suspend, terminate or reactivate; add spend limits. |
| Card products | Build card products manually or with AI-assisted (agentic) setup, promote from UAT to production, and manage the product library. |
| BINs and ranges | Manage BINs and ranges with capacity indicators and alerts. |
| Servicing | Manage cardholder groups (KYB), cardholders (KYC), and cards: issue physical or virtual, reset PIN, replace, release holds, view inherited controls and wallet tokens; manage accounts. |
| Monitoring | Live transaction feed with volume charts and export, reconciliation with mismatch flagging, and fraud monitoring KPIs. |
| Approvals and audit | Approval workflows for sensitive actions, and a full audit trail with before and after values and rollback. |
| Reports and support | Standard, custom and AI-generated reports; support tickets with escalation to TXN. |
| Roles and access | System and custom roles, per-environment permission matrices, user lifecycle and delegated provisioning. |
| AI assistant | A persistent assistant for summaries, guided setup, natural-language queries and report generation, with the person always in the decision loop. |

Not in the Console MVP: self-registration by email and password (SSO only at launch), creating and editing fraud rules and the AI fraud copilot, digital wallet token management actions, audit-trail and disputes export, and several production reconciliation exports. Developer-facing integration tools (API keys, webhooks) sit in the Developer Portal, not the Console.

### 3.3 TXN Intelligence

At MVP the intelligence layer establishes its foundations: natural-language interaction, retrieval over TXN documentation, and core orchestration for internal use, with audit and governance controls built in from day one. AI assists and automates routine work; it does not replace deterministic system logic, and it runs outside the real-time transaction path to protect stability and latency. Early agentic workflows execute only under explicit human approval, and every AI action is logged, attributable and reversible where the underlying action allows.

### 3.4 TXN Developer Portal

The Developer Portal turns API capability into adoption. At MVP it provides live documentation generated from the API (so documentation does not drift from the live contract), an interactive explorer with real request and response handling, sandbox access, and quick-start guides and code examples. The aim is time-to-first-successful-integration measured in minutes, not days. AI supports discovery, but the portal stays developer-led.

## 4. Beyond MVP (directional)

The phases below describe direction, not delivery commitments. Use them to show where the platform is heading, not as dated promises. Anything past MVP needs Product sign-off before it is committed to a client.

| Phase | Platform and operations | Intelligence and developer experience |
|---|---|---|
| Phase 1 | Expanded configurability and controls, deeper reporting and automation, richer cross-program views, and support for more complex client models. | Triage and recommendations for support and operations, predictive analytics, and the first agentic workflows executed under human approval; expanded SDK coverage and richer integration guides. |
| Phase 2 | Greater self-service and scale, client and partner self-service operations, and optimisation across regions and client tiers. | Advanced intelligence and insights, opening the orchestration layer to clients and partners, more autonomous workflows under cost governance, and deeper AI-assisted developer guidance. |

## 5. Platform targets, standards and proof

Two things need to stay separate: what is proven and citeable today, and the platform targets the build is engineered to meet at launch. Do not present the latter as achieved until validated in production.

### 5.1 Proven heritage (citeable today)

| Source | Proof |
|---|---|
| Direct Transact, our co-founding owner | 25 years of processing heritage, over R50bn processed monthly, 99.99% uptime, Visa and Mastercard certification, PASA System Operator status, PCI DSS and ISAE 3402. |
| Paycorp, our co-founding owner | 25 years of international payments experience and over $9bn processed annually, with long-standing bank, scheme and regulator relationships. |

### 5.2 Platform design targets (engineered for launch)

| Target | Detail |
|---|---|
| Availability | 99.99% monthly for production core; 99.5% for AI-assisted features and for UAT. |
| API performance | Critical calls P95 under 300ms and P99 under 1s; standard calls P95 under 500ms; complex reporting P95 under 2s. |
| Console and AI responsiveness | Console page load P95 under 2 seconds; AI responses under 100ms, 500ms and 1s by task complexity. |
| Speed to deploy | New programs or environments deployed within 15 minutes under standard conditions, with a maximum of one business day for more complex clients. |
| Resilience | Recovery time objective of 4 hours, recovery point objective of zero data loss for transactional writes, and regional failover. |
| Scale | Load-tested at twice expected peak before each release, scaling horizontally without code change. |

### 5.3 Standards and compliance

| Area | Standard |
|---|---|
| Card data security | PCI DSS Level 1, TLS 1.2 minimum, no regulated card data in standard responses. |
| Access and authentication | OAuth 2.0 with scoped tokens, mutual TLS for high-assurance integrations, SSO for console users with mandatory two-factor where password sign-in is used. |
| Regulatory | PSD2 and SCA, 3DS 2.x step-up authentication. |
| Auditability | Immutable audit logging with a minimum seven-year retention, actor, action, timestamp and outcome on every event. |
| Accessibility | WCAG 2.1 AA across interactive surfaces. |
| Hosting | Cloud-native on Microsoft Azure, delivered as software as a service. |

## 6. Scheme, BIN sponsorship and ownership

Launch certifies one card scheme first, currently expected to be Visa, with Visa due diligence already under way; further schemes follow by region. TXN treats BIN sponsorship as a first-class role in the platform and works with pre-integrated BIN sponsor relationships in each target region to simplify and speed up how clients launch programs. TXN is the issuer processor; it does not outsource its processing.

On ownership, TXN is a 50/50 joint venture, equally co-founded by Direct Transact and Paycorp. Both are described only as “our co-founding owner”. TXN’s reliability is rooted in Direct Transact’s track record through ownership, not as an outsourced service. Do not describe TXN as built on, powered by, or a version of either owner’s platform, and attribute each owner’s heritage separately.
