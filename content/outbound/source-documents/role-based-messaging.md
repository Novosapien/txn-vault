---
description: "TXN Role-Based Messaging v1: the deck mapping message to buying-group role, each persona framed by the type of risk they are trying to eliminate"
---

# Role-Based Messaging v1

> **Section:** [[source-documents]]
> **Author:** Ian Johnson, TXN Global. Delivered 24 August 2026.
> **Original:** `originals/TXN_Role_Based_Messaging_(V1).pptx`
> **Status:** verbatim conversion of the file as delivered. Not edited, not summarised. Where the conversion and the original disagree, the original governs.

Ten slides, extracted from the original PowerPoint. Carries the company-level decision criteria table that assigns DACI role, veto power and explicit criteria per pillar. Slide 1 labels it DRAFT V0.1.

---

## Slide 1

Role based messaging overview

DRAFT V0.1

Ian Johnson


## Slide 2

Framework overview

Each persona is trying to eliminate a different type of risk — our messaging and content should map exactly to that risk.
Decision Making Process Role (DACI) – Driver Approver Contributor Informed
What do they need to de-risk
What do they need to know (not what we want to tell them)
What they will challenge us on
Messaging pillars
Language to use / avoid
Content they expect
Example copy



## Slide 3

Company Level Decision Criteria

| Pillar |  | Owner | DACI Role | Decision Outcomes | Veto / Stage |  | Explicit Criteria |
|---|---|---|---|---|---|---|---|
| Technical Control | Ability to control auth, integrate cleanly, scale reliably | CTO | Approver (A) | CTO validates 
“This will work” | Yes | Early Stage
If we fail technically, nothing else matters | Can we control authorisation logic?
Can we integrate without workarounds?
Is API behaviour predictable?
What happens under failure? |
| Product Enablement | Ability to build differentiated products quickly | Product | Contributor (C) | Product validates 
“We can build what we need” | No | Early Stage
Whilst this role is unlikely to have veto power, they are a significant voice in the room | Can we support our use cases (BNPL, expense)?
How configurable is the platform?
How fast can we launch? |
| Operational Viability | Ability to run programmes without friction | Payments | Driver (D) | Payments validates 
“We can operate this” | Yes | Pre-Approval Stage
Runs evaluation, shortlists vendors, shapes internal narrative, if we lose them, we never reach approval stage | Can we reconcile transactions easily?
How are disputes handled?
What visibility do we have?
How much manual effort is required?
How much support will we need for set up / integration? |
| Commercial Model | Sustainable, scalable economics | CFO | Approver (A) | CFO validates 
“This makes financial sense” | Yes | Late Stage
Most deals fail here due to unclear pricing and / or unit economics not fitting client business model | Cost per transaction / card
Pricing transparency
Scalability of cost
Hidden fees (scheme, tokenisation, 3DS) |
| Risk & Compliance | No regulatory or operational exposure | COO / Risk | Contributor (C) | Risk validates 
“This won’t expose us” | Yes | Late Stage
Most deals fail here due to compliance ambiguity or concerns on supplier risk | Who owns compliance?
Fraud capability
Data handling, residency & privacy (GDPR)
Scheme alignment
Compliance (PCI, DORA, PSD2, GDPR) |



## Slide 4

DACI + Decision Criteria Table

| Role | DACI Role | Real Role in DMP | Decision Criteria |  |
|---|---|---|---|---|
| Head of Payments
Programme Lead | Driver (D) | Runs evaluation
Coordinates stakeholders
Owns vendor selection process | Operational feasibility (reconciliation, disputes)
Ease of programme management
Vendor responsiveness / support model | Implementation complexity |
| CTO
Head of Engineering | Approver (A) | Veto power on architecture, APIs, and scalability | Authorisation control (can we own decisioning?) 
API quality (consistency, idempotency)
Latency + uptime | Architecture (scalability, resilience & security)
Failure handling
Stand-in processing, retries |
| CFO | Approver (A) | Signs off on commercial viability | Unit economics (cost per txn / card)
Pricing transparency
Cost scalability (volume tiers) | Total cost of ownership
ROI vs alternatives |
| COO
Risk & Compliance | Contributor (C) | Ensures regulatory + operational risk is acceptable | Compliance coverage (PCI, PSD2, DORA, scheme rules)
Fraud controls
Operational resilience | Data security & hosting
Liability model |
| Head of Product
CPO | Contributor (C) | Shapes requirements
Validates product fit | Product flexibility (controls, wallets, features)
Speed to market
Ability to differentiate | Roadmap dependency on processor |
| Procurement
Legal | Contributor (C) | Structures deal
Removes contractual risk | SLA strength
Liability & indemnities
Exit terms / lock-in | Pricing clarity in contract |
| CEO / Founder | Informed (I) /Approver (A) | Steps in for strategic deals or large commitments – Approver (A) | Strategic alignment
Speed vs Risk - brand / vendor credibility |  |



## Slide 5

Role-based messaging / content

| 1. CTO / Head of Engineering |  |  |  |
|---|---|---|---|
| DACI Role | Approver (A)
Veto power on architecture, APIs, and scalability | Language to use | Latency
Idempotency
Webhook retries
Event-driven architecture
Deterministic behaviour |
| What do they need to de-risk | Will this platform break at scale?
Will we lose control of the authorisation logic?
Will integration become a long-term constraint? | Language to avoid | Flexible
Scalable
Robust
All of the above where no proof points exist |
| What do they need to know | Authorisation control model
API integrity
Latency & Reliability
Architecture | Content they expect | API docs (Swagger / OpenAPI)
Sequence diagrams
Failure scenarios
Sandbox access |
| What will they challenge us on | Can I control auth decisions in real time?
What happens if my system is down?
Show me your retry logic
What’s your webhook failure model?
Where does state live? | Messaging Pillars | Define and execute your own authorisation logic in real time using configurable rule layers or direct API decisioning
Every API is versioned, idempotent, and designed for predictable behaviour at scale]
Authorisation responses consistently delivered in sub-100ms with 99.99% platform availability
Built in stand-in processing ensures continuity when your systems are unavailable |
| Copy Example | Intercept every authorisation request, apply your own decision logic, and respond in real time — or rely on configurable stand-in rules when your systems are unavailable. |  |  |



## Slide 6

Role-based messaging / content

| 2. CPO / Head of Product |  |  |  |
|---|---|---|---|
| DACI Role | Contributor (C)
Shapes requirements
Validates product fit | Language to use | Launch
Configure
Control
Build |
| What do they need to de-risk | Can I build differentiated products?
Will this slow down roadmap delivery?
Will I be constrained by the processor? | Language to avoid | Platform capabilities |
| What do they need to know | What can they build
How quickly
Where flexibility does / does exist
What engineering effort will be required | Content they expect | Use case breakdowns
Product configuration examples
Time-to-launch benchmarks
Customer / partner testimonials (where available) |
| What will they challenge us on | Can I support multiple wallets?
Can I configure spend controls per account / cardholder / card?
Can I launch in multiple countries / regions?
How much effort / engineering is required to launch initial and future products / expand into new markets? | Messaging Pillars | Design card products around your business model – not platform limitations
Launch new programmes in weeks, not months, using pre-built components and APIs
Configure spend controls, limits, and behaviours at account, cardholder, and card level
Evolve your product without re-platforming |
| Copy Example | Launch a multi-wallet card product with real-time spend controls and embedded approval logic – without building issuing infrastructure from scratch |  |  |



## Slide 7

Role-based messaging / content

| 3. Head of Payments / Programme Lead (Operational Owner) |  |  |  |
|---|---|---|---|
| DACI Role | Driver (D)
Runs evaluation
Coordinates stakeholders
Owns vendor selection process | Language to use | Reconciliation
Settlement
Disputes |
| What do they need to de-risk | Will this create operation chaos?
How do I manage reconciliation, disputes, and scheme processes? | Language to avoid | Statements without concrete workflow examples
Complex technical jargon without operational context |
| What do they need to know | Operational workflows
Visibility into transactions
Exception Handling | Content they expect | Workflow diagrams
Dashboard screenshots
Video demo links |
| What will they challenge us on | How does reconciliation work?
How are disputes handled?
What tooling do I get? | Messaging Pillars | Full visibility into every transaction, balance, and event in real time
Automated reconciliation, dispute management, and settlement processes
Seamless connectivity with Visa and Mastercard processes |
| Copy Example | Manage transactions, disputes, and settlement from a single operational view – with no manual reconciliation required |  |  |



## Slide 8

Role-based messaging / content

| 4. CFO / Commercial Controller |  |  |  |
|---|---|---|---|
| DACI Role | Approver (A)
Signs off on commercial viability | Language to use | Cost per transaction
Unit economics
Margin impact |
| What do they need to de-risk | Will this destroy my unit economics?
Are there hidden costs? | Language to avoid | Cost effective
Competitive pricing
Simplified and transparent pricing without pricing construct |
| What do they need to know | Pricing model
Cost predictability
Impact on margins | Content they expect | Pricing scenarios
ROI examples |
| What will they challenge us on | What is my cost per average active account / cardholder / card?
How does pricing scale?
What are hidden costs? | Messaging Pillars | Clear, predictable pricing aligned to your growth
Reduce costs per transaction through automation and scale
Pricing models designed to support differentiated business models |
| Copy Example | Reduce processing costs as you scale, with transparent pricing and no hidden scheme or infrastructure fees |  |  |



## Slide 9

Role-based messaging / content

| 5. Risk & Compliance / Legal |  |  |  |
|---|---|---|---|
| DACI Role | Contributor (C)
Ensures regulatory + operational risk is acceptable
Structures deal
Removes contractual risk | Language to use | Compliance
Risk
Controls |
| What do they need to de-risk | Regulatory exposure
Fraud risk
Operational failure
Contractual exposure
Vendor lock-in | Language to avoid | Minimising regulatory complexity without examples |
| What do they need to know | Compliance ownership
Fraud controls
Certifications
3rd party partner compliance and audit
Exit options | Content they expect | SLA
DPA
Contract summaries
Schedules supporting regulatory compliance requirements |
| What will they challenge us on | Liability and penalties for failures | Messaging Pillars | Built to meet PCI DSS, PSD2, DORA and scheme requirements
Integrated fraud monitoring and transaction controls
Designed for high availability and secure processing
Clear SLAs, pricing, and responsibilities
Transparent operating model |
| Copy Example | Reduce regulatory burden with built-in compliance and fraud controls designed for card issuing at scale |  |  |



## Slide 10

