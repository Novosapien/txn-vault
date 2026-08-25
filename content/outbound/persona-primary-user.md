---
description: "TXN's Primary User persona scaffold: the engineering leader who holds technical veto and owns the Technical Control decision pillar"
---

# Persona: Primary User (CTO)

> **Source of truth:** `TXN_GTM_Persona_Primary_User_v0.1.docx` in the outbound folder (`programming/txn/outbound`, mirrored at `shared/clients/txn/outbound`), delivered by Ian Johnson on 24 August 2026. This page is a readable mirror. Edit the source document, then re-mirror. Routed from [[outbound]].

---

Version: 0.1Author: I. JohnsonDate: 22/04/2026
Chief Technology Officer. The engineering leader whose team lives with the platform.Chief Technology Officer. The engineering leader whose team lives with the platform.Persona: Primary UserPersona: Primary User

# 1. Document Control
| Version | 0.1 |
| Date | 22/04/2026 |
| Author | I. Johnson |
| Owner | I. Johnson |
| Description | Initial scaffold. Primary User persona maps to CTO / Head of Engineering. Content drawn from TXN_Role_Based_Messaging_(V1).pptx and aligned to ICP v0.3. |

# 2. Purpose
Define the Primary User persona for TXN's Named Account List. The Primary User is the engineering leader whose team integrates and operates against TXN's APIs day in and day out. They hold veto power on architecture, API quality, and platform resilience, and they are the persona whose experience most determines whether TXN becomes a long-term partner or a migration target.

# 3. Persona Overview

## 3.1 Role Mapping
The Primary User persona maps to the Chief Technology Officer or Head of Engineering. Equivalent titles include VP Engineering, Platform Lead, Principal Engineer in smaller organisations, and in very large organisations a dedicated Head of Payments Engineering.

## 3.2 Background
Technical leaders at fintechs accountable for platform stability, API integration quality, and engineering team velocity. Reports to CEO or CTO-equivalent. Typically 10 to 20 years of engineering experience, with at least 3 to 5 years in payments, fintech, or scale-up technical environments. Holds veto on architecture decisions.

## 3.3 Why They Are the Primary User
TXN is an API-first product. The daily interaction that determines product satisfaction happens through the APIs, not through the console. The engineering team is therefore the primary operator of the platform post-go-live, and the CTO speaks for that group. If the CTO does not respect the platform, the team's frustrations build over time and the account drifts towards churn regardless of how happy Product or Payments are.

## 3.4 DACI Role
Approver (A) with technical veto. The CTO holds veto power on architecture, APIs, and scalability. If the CTO says no, nothing else matters in the deal. This differs from the Economic Buyer veto (which fails the deal on commercial grounds) because the technical veto often kills evaluations at the early stage, before commercial conversation begins.

## 3.5 Company Decision Pillar
The Primary User owns the Technical Control pillar in the client's evaluation framework. The questions they drive are: can we control authorization logic; can we integrate without workarounds; is API behaviour predictable; what happens under failure. If TXN fails technically, nothing else matters per the pptx framework.

# 4. Goals and Success Criteria
Stable, predictable platform that scales with the business without architectural surprise.
Engineering team productivity. Clean APIs, complete documentation, minimal integration workarounds.
Control over authorization logic and decisioning in real time.
Resilience under failure conditions. Clear behaviour during vendor outages and during client-side outages.
A future-proof technical architecture that does not become the next constraint.
Success is measured by platform uptime, authorization latency, API error rates, incident frequency and resolution time, and the engineering team's satisfaction with integration quality.

# 5. Pains and What They Need to De-risk
Will this platform break at scale? Concern that the vendor has not been proven at the volumes the client is planning for.
Will we lose control of the authorization logic? Fear of being locked into the processor's decisioning rather than owning it.
Will integration become a long-term constraint? Fear that early integration decisions calcify into architecture debt.
Vendor lock-in at the architectural level. Concerns about exit cost and about being trapped in a vendor-specific API shape.
Poor API documentation forcing workarounds. An unambiguous signal of poor engineering hygiene.

# 6. Information Needs
Authorization control model. Can decisions be made in real time by the client, and how are the fallback and stand-in modes configured.
API integrity. Versioning policy, idempotency guarantees, consistency between documentation and behaviour, backwards compatibility.
Latency and reliability. Concrete numbers, not adjectives. p50, p95, p99 latencies. Uptime SLA with penalties, not targets.
Architecture. Scalability, resilience, security, multi-region strategy, deployment model.
Failure handling. Retry logic, stand-in processing, webhook backoff, dead letter handling, state recovery.

# 7. Common Objections and Challenges
Can I control authorization decisions in real time? If so, under what latency budget and with what fallback behaviour?
What happens if my system is down? Walk me through stand-in processing.
Show me your retry logic. What is the backoff curve and maximum retry window?
What is your webhook failure model? How do I know I have received every event?
Where does state live, and how is it reconciled between your system and ours?
What is your platform uptime SLA, with penalties rather than targets?
Show me your sandbox. If I cannot get a working integration in an afternoon, I am not interested.

# 8. Language

## 8.1 Language to Use
Latency, idempotency, webhook retries.
Event-driven architecture, deterministic behaviour.
Stand-in processing, retry logic, authorization control.
Sub-100 millisecond response, 99.99 percent availability, numbers with context.
Sandbox, SDK, OpenAPI specification, webhook signature verification.

## 8.2 Language to Avoid
Flexible, scalable, robust, as standalone claims without proof points.
Any claim without concrete numbers or demonstrable evidence.
Marketing language without technical substance. This persona discounts it heavily.
Presenting the console as the integration surface. The API is the surface.

# 9. Messaging Pillars
The four messaging pillars for the Primary User, in priority order:
Define and execute your own authorization logic in real time using configurable rule layers or direct API decisioning.
Every API is versioned, idempotent, and designed for predictable behaviour at scale.
Authorization responses consistently delivered in sub-100 millisecond latency with 99.99 percent platform availability.
Built-in stand-in processing ensures continuity when your systems are unavailable.

# 10. Content They Expect
API documentation in Swagger or OpenAPI format. Complete, accurate, versioned.
Sequence diagrams for key flows. Authorization, settlement, reconciliation, dispute.
Failure scenario documentation. What happens when the client is down, when TXN is down, when the scheme is down.
Sandbox access, self-serve, with realistic test data. No sales gating to sandbox access.
Architecture diagrams at the level the CTO can evaluate. Multi-region deployment, database architecture, scheme connectivity topology.
Security certifications. PCI DSS, SOC 2 Type II, ISO 27001, DORA readiness, GDPR posture.

# 11. Example Copy
Intercept every authorization request, apply your own decision logic, and respond in real time; or rely on configurable stand-in rules when your systems are unavailable.

# 12. Relationship to Other Personas
The Primary User works closely with the Champion (CPO). The Champion brings use cases and desired product behaviour; the Primary User validates technical feasibility. A Champion cannot win a deal without Primary User sign-off.
The Primary User gates the Economic Buyer (CFO). The CFO will not commit commercially if the CTO has not signed off technically. Sequence evaluations to secure technical validation first.
The Primary User works with Risk and Compliance (profiled in Role-Based Messaging) on security, data handling, PCI and DORA compliance, and incident response. Architecture decisions must survive compliance review.
The CTO's day-to-day interaction with TXN is through the APIs and through engineering dashboards, not through the console. The console is the Head of Payments' surface (Role-Based Messaging), not the Primary User's.

# 13. Alignment with ICP and Role-Based Messaging
Section 6 of the ICP (Technographic Signals) directly aligns with this persona. The expectation that the ICP-fit company's tech stack is cloud-based on AWS, Azure, or GCP, that an API-first architecture is a strong positive signal, and that the company has its own in-house engineering team, implies that the Primary User persona assumes a technical maturity baseline. Do not pitch this persona at a company that fails the Section 6 signals.
Section 4.3 Company Size (20 to 2,000 employees) has implications for who the Primary User actually is. At the lower end of the band (20 to 100 employees), the CTO is typically the Primary User personally, hands on with integration. At the upper end (1,000 to 2,000 employees), the CTO is abstracting and has a VP Engineering or Platform Lead who is the hands-on Primary User. Calibrate the material accordingly. Senior titles get strategic content; hands-on roles get technical depth.
Cross-reference to the Role-Based Messaging document (V1) for the full DACI framework. The Primary User maps to the Technical Control pillar there. The operational counterpart (Head of Payments running reconciliation, disputes, and settlement) is profiled separately in Role-Based Messaging and is a critical supporting persona for any deal that reaches technical sign-off.
