---
description: "TXN's offer under Offer Structure v2: the factual-claims universe the Cold Outreach Workforce is permitted to speak from, rebuilt clean on 2 September 2026"
---

# TXN Offer

> **Up:** [[outbound]]
> **Status:** Rebuilt clean, 2 September 2026, then revised the same day against five rulings (`R1`). Supersedes [[offer-draft]]. **Nothing blocks the offer.** Fourteen gaps remain, none of them load-bearing, and one factual check sits with Ian. Reconciled against the 3 September session on 5 September, which closed the credentials and employee-band gaps. Still to be read end to end and signed off by Ian.
> **What this is:** the factual-claims universe. Everything written here is permitted truth that the outbound agents may state and the critic will pass. **No prospect ever reads this document.** It is not marketing copy and it is not a brochure. Judge it only on whether every line is true and defensible.
> **The markdown is the source of truth.** A generated JSON appendix is added once the gaps list below is closed and Ian has signed the document off. It is not written by hand.
> **Readable HTML version:** `~/shared/clients/txn/outbound/txn-offer-<timestamp>.html`, generated from this file by `python3 scripts/render-html.py offer`. It is a rendering, not a second copy. Edit this document, then regenerate; never edit the HTML.

## How this version was built, and where that limits it

This is a rebuild from source, not an edit of the previous draft. Two kinds of material went into it and they are not equally strong.

**Elicited from Ian Johnson and Dorte Dye in session.** The tagline, the value proposition in Ian's own words, the balance-holding correction, the platform provenance ruling, the buying group, the migration ruling, the pricing model, the proof position, the disclosure rules. These are the strongest lines in the document because they came out of someone's head rather than out of a file.

**Derived from TXN's own written corpus.** Product Overview v1.0, Core Messaging v2.5, AI Target Outcomes Framework v1.0, Objection Handling v1.1, Competitive Landscape v0.2. These are unusually good internal documents, but they are documents: they say what TXN says about itself, and the offer method is explicit that this is orientation rather than answer.

**Every derived line that Ian has never said out loud is marked.** Those are the lines most likely to be wrong, and they are the ones to put in front of him first. Fields nobody has answered are written `unknown` and collected in the gaps list at the foot. A visible gap is a correct gap.

**Source key.** `S1` offer session 24-08-2026 · `S2` offer session 27-08-2026 · `ICP2` ICP session 25-08-2026 · `S3` ICP statuses session 03-09-2026 · `R1` rulings taken 02-09-2026 · `PO` Product Overview v1.0 · `CM` Core Messaging v2.5 · `AITO` AI Target Outcomes Framework v1.0 · `OH` Objection Handling v1.1 · `CL` Competitive Landscape v0.2 · `JV` JV Messaging Framework v2.3

---

## Vocabulary doctrine, binding on this document

A word TXN bans externally must not appear in this fact base, because this fact base is what feeds messages. A banned word sitting here is a banned word the critic will happily pass into client-facing copy.

**Never use.** built on · powered by · provided by · runs on · inherit · partner, in the vendor or service-provider sense, when referring to Direct Transact · parent group · underlying infrastructure · bank-grade · "50 years combined experience" · built from the ground up · built new · solution, when platform is meant · ecosystem, when partners is meant · enterprise · revolutionary · game-changing · world-class · cutting-edge · disrupt · disruptor · transformative · seamless · best-in-class · synergies · leverage as a verb.

**Always use.** "Direct Transact, our co-founding owner" and "Paycorp, our co-founding owner" as the canonical external designations. "program" and "programs", never "programme", because TXN's platform uses that spelling. British English otherwise. No em dashes.

**Two standing rules.** The 25 years of processing heritage belongs to Direct Transact and must be attributed every time it is used; it is never claimed for TXN. Any sentence that references an owner ends on what TXN delivers, not on the owner.

**Positioning register: evolution, not disruption.** (`S2`.) Differentiation is framed as doing the existing job better, never as replacing the category.

**Never stated, in any channel: how the platform was built.** (`S2`.) The external claim is that the platform is TXN's. Nothing about code lineage, in either direction. Ian's reasoning is that there is no upside and one clear downside, which is inviting the question "they have been in place for 25 years, so was that code legacy in the first place."

**Two bans are sense-specific, and a literal string match will over-fire on them.** *Partner* is banned only when applied to Direct Transact in a vendor or service-provider sense; "BIN sponsor relationships" and "pre-integrated partners" are fine. *Disrupt* is banned as a positioning register, the disruptor claim; "disruption to the cardholder base" is TXN's own operational language and appears in their documents. Anything else on the list is banned outright.

**Never name a competitor.** (`R1`.) Not Marqeta, Paymentology, Thredd, Enfuce, Episode Six or Pismo, and not any other. Contrast against the categories in Section 5, including when a prospect names a competitor first. TXN's per-competitor counters exist and stay with the humans.

**Never criticise the competition, and this is stricter than the naming ban.** (`S3`.) Ian, asked whether the restraint applies even where a buyer is actively leaving somebody: *"The answer to that question is yes. I just don't believe in criticizing the competition. It's more important to emphasize all differentiators as you understand them."* **Binding in all four ICPs**, not only where an incumbent stays. State what TXN does, never what the other cannot. No "unlike your current processor", no "if your provider cannot", no implied deficiency. Where a capability is genuinely absent on the alternative, the buyer draws the comparison themselves, and a comparison the buyer makes is worth more than one an agent makes for them.

**Consequence, and it changes how Section 5 is read.** The **Where it falls short** material under each alternative in Section 5 is **context-not-quotable**: agents ground on it, and never voice it. It is internal grounding for choosing which TXN capability to lead with, the same treatment Section 7 already carries.

**Never lead with the owners.** (`R1`.) Direct Transact and Paycorp do not appear in first touch or in the follow-up sequence. They carry real credibility and it is deployed further down the sales process, by a person, once the prospect is engaged and asking who is behind this. Full placement rule in Section 6.

**Open:** whether this ban list is complete, or whether bans exist that were never written into a document. Ian to confirm.

---

## Section 1: What it is

TXN is an issuer-processing platform: the infrastructure that sits between a business that wants to give its own customers cards and the card schemes those cards run on. It does two things. It lets a client manage cardholder accounts so that cards, physical or digital including Apple Pay and Google Pay, can be requested and run. And it does the processing itself, handling the messages from Visa and Mastercard every time one of those cards is presented at a merchant anywhere in the world. The client touches it through three surfaces: an API for machine-to-machine integration, a Console for the people who operate the program day to day, and an intelligence layer running across both. It is delivered as software as a service, cloud-native on Microsoft Azure, and it is multi-tenant and multi-region by design.

The anchor line, used verbatim and never paraphrased: **"Intelligence built in. Complexity taken out."**

The tagline, agreed in `S1`: **"TXN is the platform for any company launching and operating a card program."** The load-bearing word is *any*. Ian: *"doesn't have to be a bank... you can be a trade platform, you can be a marketplace, you can be whatever."* A tagline and a plain description of what the company does are two different sentences with two different jobs, and both are held here.

### Literal description

**Category**
Issuer-processing platform.

**Form factor**
Multi-tenant cloud software, four decoupled component surfaces, each able to change without forcing change on the others. (`PO` 2.)

**Surface**
Three, and which one leads depends on the buyer. The **TXN API** is the machine-to-machine surface and the stable contract layer: all core functionality is available through it before it appears on any screen, and behaviour is deterministic, so the same inputs always produce the same outcome. The **TXN Console** is the operator surface for onboarding, configuration, servicing, monitoring, approvals and audit, role-aware throughout. **TXN Intelligence** runs across both. A fourth surface, the **TXN Developer Portal**, is where developers discover, test and integrate.

**Delivery model**
Software as a service, cloud-native on Microsoft Azure. (`PO` 5.3.)

**Operating model**
The client operates their own program; TXN operates the platform. The platform is hosted and managed by Direct Transact within their existing data governance and security frameworks. (`S2`, and this sentence is the approved confidence line.)

**Buying model**
A fixed monthly licence fee per client to access the platform, plus volume-tiered variable fees. Shape only; the economics are in Section 7.

**Mechanism arc**
A client brings a card product idea and its own customers; TXN configures and certifies the card program, processes every scheme message those cards generate, and returns a running program with the settlement position, the cardholder data, and the controls to change it. *(Derived from `PO` and the `S1` transaction-flow description. Ian has never said this sentence.)*

### Why it exists

**Underlying problem**
Card programs run on platforms designed before cloud, APIs and modern cardholder expectations, and the businesses that now want to launch one are increasingly not banks and hold no card expertise. So the platform layer taxes two different groups: those who already have a program and cannot change it quickly, and those who want one and cannot start. (`CM` 5, `AITO` 3.1.1.)

**What shifted**
Two things, on different clocks. Businesses outside financial services began treating a card as a feature of their product rather than as a banking product, so the buyer stopped being a bank. And the first wave of modern processors proved an API-first surface was possible, which moved the bar from whether a platform has an API to what it does with the complexity underneath. *(Derived. The framing is ours and the dates and sequencing have never been confirmed by Ian. Marked as a question in the gaps list.)*

**Prior answers**
Three, and none of them removed the expertise requirement, which `AITO` 3.1.1 names as the primary reason businesses avoid adding card programs at all. Legacy issuer processors are proven and slow. First-wave modern processors fixed the developer surface and left the operator with the same complexity. Building in-house looks attractive at year one and painful at year three, because scheme mandates never stop. (`OH` 4.2, `CL` 3.4.)

### What it is not

**Not a** consumer-facing banking application.
**Confused because** it manages cardholder accounts and card lifecycles.
**Differs in** that the cardholder relationship belongs to the client. TXN enables others to build, operate and scale card products; it does not compete with them for the end customer. (`PO` 1.)

**Not an** acquiring or merchant platform.
**Confused because** both sit in card payments and both process scheme messages.
**Differs in** which side of the transaction it stands on: TXN is on the issuing side, acting for the business that gives out the card, not for the merchant that accepts it.

**Not a** one-size-fits-all issuer product.
**Confused because** it is a platform with a standard shape rather than a bespoke build.
**Differs in** that behaviour is driven by configuration rather than bespoke code, across many programs, many owners and many regions. (`PO` 1, 3.1.)

**Not a** legacy platform repackaged for export.
**Confused because** the processing heritage cited belongs to a 25-year-old business, and because that business is South African.
**Differs in** two sentences and no more: the platform is TXN's, and it is hosted and managed by Direct Transact within their existing data governance and security frameworks. **Code lineage is never discussed, in either direction.** (`S2`. This replaces the `S1` answer, which asserted the technology was new; that claim is withdrawn.)

### The job it does

**Primary job**
Run a card program without employing card experts. (`AITO` 3.1.1: *"This is TXN's core positioning claim. Every other outcome in this section supports it."*)

**Secondary jobs**
Launch a program in weeks rather than quarters, and keep changing it afterwards without re-platforming.
Keep control of authorisation and spend, with transparency into why every transaction was approved, declined or controlled.
Meet scheme and regulatory requirements as a delivered outcome rather than a burden carried in-house.

### Identity block

**Founded**
`unknown`

**HQ**
`unknown`. The contracting entity recorded in the commercial work is TXN Global Limited, registered in Cyprus, but that has not been confirmed as the fact base's answer to "where is TXN".

**Geographies served**
The EEA plus the United Kingdom. Outbound priority is phased: MVP markets are Poland, the Czech Republic, Romania and Hungary; Phase 1a is Southern Europe; Phase 1b is Western Europe; the rest of the EEA and the UK are opportunistic. (`CM` 3.1.)
**The phasing orders effort. It excludes nobody.** Ruled by Ian on 2 September, because the phase list was being read as a filter: *"we are not limiting our efforts even in the early outreach to just Eastern Europe... we're not restricting ourselves to that by any stretch of imagination."* A company outside the MVP markets is a target that is scheduled later, never a company that is out of scope.

**Team size**
`unknown`

**Type**
`product`. **Provisional.** Ian's own framing is emphatically a platform, and the commercial shape is a licence plus usage fees, which is a product shape. The signal pointing the other way is that TXN people perform real work in the launch path: program configuration, scheme certification, BIN sponsor arrangement. If that work turns out to be commercially distinct rather than absorbed into the licence, the routing is `both` and Section 2 steps get actor labels. **Ian to rule.**

**Built for**
European fintechs, digital banks, embedded finance companies, and other card program owners that are either launching a new card program or migrating one from an incumbent processor. Three segment clusters carry most of the addressable market: digital banking and neobanks; commercial card and expense management; lending, FX and embedded finance. (`CM` 3.1.) The full fit definition lives in [[icp-definition]].
**Employee band: ruled 3 September, and the ruling is that there is no band.** (`S3`.) Ian: *"the number of employees to a certain degree it's relevant but it doesn't warrant a significant score."* Headcount and card-readiness are uncorrelated in both directions: a scaled business may have built everything except the card and have ten people, and a startup may build cards from day one with fewer than ten. **Sub-10 is explicitly in scope**, which is wider than either ICP v0.4 or `CM` 2.5 allowed, so the 10-to-5,000 versus 20-to-2,000 disagreement is not resolved in favour of either. The scope widens and the weight falls, to 3 points at [[icp-definition]] 8.1.3. Closes G9.

**Covers**
The TXN issuer-processing platform in full: the API, the Console, the Developer Portal and the intelligence layer, for both greenfield launches and migrations from an incumbent.

**Not covered**
**Nothing.** TXN sells nothing that this offer does not describe, so there is no second offering to disambiguate against and no adjacent product an agent should be steering a lead towards. (`R1`. Closes G2.)

**Scale facts**
**TXN has none. TXN is pre-launch and has no clients, no case studies, no testimonials and no track record in its own name.** That is the correct entry and it is written here deliberately, so that no agent invents one. The only citeable figures belong to the co-founding owners and must be attributed to them (see Section 6).

**Credentials**
**Two different things live here and conflating them is the single most dangerous error in this document.** What TXN holds, and what the platform is engineered to. Settled on 3 September (`S3`).

*What is held, and by whom.*
**TXN holds no accreditation of its own.** Ian, unprompted and for the record: *"we definitely don't have it just for that record."*
**PCI is held by Direct Transact, our co-founding owner, not by TXN.** Ian: *"DT hold the PCI accreditation because essentially they're the ones that are managing our card infrastructure."*
**SOC 2: `unknown`.** Ian was not sure; Dorte believes Direct Transact holds it. Ian owns the check.
**ISO 27001: `unknown`.** Ian: *"I'm pretty sure they do. We'll just have to double check that."* Ian owns the check.

**The only permitted form of the claim.** The platform is operated within Direct Transact's accredited environment, and Direct Transact is a co-founding owner rather than a supplier. **Never "TXN is PCI compliant", never "TXN is certified", never "our certifications".** This is the same distinction Ian drew on 27 August between the platform and the environment it is operated in, and getting it wrong in a regulated procurement is unrecoverable.

*What the platform is engineered to*, per `PO` 5.3. These are design standards, not held accreditations, and they are stated as such or not at all.
Card data security: PCI DSS Level 1 as the design standard, TLS 1.2 minimum, no regulated card data in standard responses.
Access: OAuth 2.0 with scoped tokens, mutual TLS for high-assurance integrations, SSO for console users with mandatory two-factor where password sign-in is used.
Regulatory: PSD2 and SCA, 3DS 2.x step-up authentication.
Auditability: immutable audit logging with a minimum seven-year retention, carrying actor, action, timestamp and outcome on every event.
Accessibility: WCAG 2.1 AA across interactive surfaces.
Scheme: launch certifies one scheme first, currently expected to be Visa, with Visa due diligence under way. Mastercard follows and is the number one priority once MVP launch completes. Ian is comfortable naming both schemes in outbound because the sequencing can be handled in conversation. (`S1`, `PO` 6.)

**Notable names**
None. Permission-gated field, and there is nothing in it.

**Provenance**
TXN is a 50/50 joint venture, equally co-founded by Direct Transact and Paycorp. The joint venture is **not the lead message**. Ian: *"I don't see why anybody in Europe would really have any knowledge of a South African payment business."* In targeted outbound the joint venture is a reason to believe, brought in second, never the opening. (`S1`.)

**Delivery surface**
Web console, HTTP API, developer portal.

---

## Section 2: How it works

**Overview.** A client decides what card product they want; TXN configures and certifies the program against a scheme and a BIN sponsor; cards are issued to the client's own customers; every scheme message those cards generate is authorised, authenticated, cleared, settled and reconciled by TXN in real time; and the client changes any of it afterwards through the Console or the API without waiting on anyone.

This is the longest section in the document by design, and one step in it is a hole. It is named as a hole rather than filled.

### Step 1. Configure the program

**What happens.** The client's intent, what they want the card product to do, for whom, in which markets, is captured and turned into program configuration rather than bespoke code. Programs, card products, spend rules, fee structures and entity models are all set as configuration. Card products can be built manually in the Console or through AI-assisted setup, then promoted from UAT to production and held in a product library for reuse.
**Contributes.** So that what a client wants changed later is a setting rather than a release.

### Step 2. Get from signature to a live program

**What happens.** `unknown`, and **parked by decision on 2 September 2026** (`R1`) rather than left open. Dorte's write-up of the signature-to-first-live-transaction sequence is no longer being waited on. Ian confirmed the sequence is materially the same for a greenfield launch and for a migration, and that the capture-and-configure part is identical either way, which is recorded at step 12.
**What is known about the target.** `AITO` 3.1.2 sets the target at under ten business days from contract signature to first live transaction, and 4.1 carries it as a measured metric. **That is a target TXN has set itself, not an achievement, and it must be presented as a target until a client has been through it.**
**What parking this costs, stated so it is a decision rather than a hole.** The primary job, running a card program without employing card experts, is carried by steps 1 and 10 and does not depend on this step. What loses its mechanism is the launch-speed secondary job. So the ten-day figure stays quotable as a stated target and **must never be described as a process**: an agent may say TXN targets under ten business days, and may not say how that is achieved, because nobody has written it down. A prospect asking how is a conversation for a human.
**Contributes.** So that the time between deciding and transacting is measured in days.

### Step 3. Issue and manage cards, cardholders and accounts

**What happens.** Cardholders, funding accounts and business entities, which are cardholder groups, are created and managed with KYC and KYB. Virtual, tokenised and physical cards are created, activated and run across their full lifecycle. Tokenised credentials in digital wallets are first-class entities with their own lifecycle and risk context. Physical fulfilment is coordinated end to end: production, provider integration, shipment tracking, delivery confirmation. Cardholders can view sensitive data such as PAN, CVV and PIN without bringing the client's systems into PCI scope.
**Contributes.** So that the client owns the cardholder relationship without owning the card mechanics or the PCI burden that normally comes with it.

### Step 4. Authorise in real time

**What happens.** When a card is presented at any merchant worldwide, TXN receives the scheme message and decides. There are two shapes and Ian was explicit that it is both, not either. TXN can authorise against a balance it holds on behalf of the client, and TXN can route the decision to the client for them to make. Ian, `S1`: *"there are occasions where we can authorize a transaction based on a balance that we hold on behalf of the client... increasingly in this market it typically is that the authorization gets rooted to the customer for them to make a decision... But it's an either or. Sorry, it's it's both, not an either or."* Where the client decides, they apply their own logic in real time.
**Contributes.** So that the client keeps the authorisation decision if they want it, and does not have to build the plumbing around it if they do not.
**Note.** This corrects the pass-through-only model stated in [[vision]]. The correction is `S1` and is the reason [[fraud-risk-assist]] was scoped as advise-not-decide.

### Step 5. Apply spend and merchant controls

**What happens.** Policy-driven limits are applied during authorisation, by amount, frequency, merchant category, geography and transaction type. Controls cascade down the entity model, so a rule set at a cardholder group reaches the cards beneath it, and that cascade is visible in the Console when servicing a single card.
**Contributes.** So that a control change is made once at the right level and takes effect on the next transaction, rather than being reapplied card by card.

### Step 6. Authenticate under PSD2

**What happens.** 3DS 2.x authentication and PSD2 strong customer authentication are delivered through an integrated access control server, so the step-up sits inside the platform rather than being wired in from outside.
**Contributes.** So that the regulatory authentication requirement is met as a delivered outcome rather than an integration the client owns.

### Step 7. Clear, settle and reconcile

**What happens.** TXN receives clearing confirmations from the schemes, aggregates the day's authorised and cleared transactions, and tells the client what is owed to Visa and Mastercard. Reconciliation runs in the Console with mismatch flagging, and issuer-side fees are configured and applied across the card lifecycle. (`S1` for the settlement description in Ian's words; `PO` 3.1 and 3.2 for the surfaces.)
**Contributes.** So that the client knows their settlement position without assembling it from files.

### Step 8. Operate the program day to day

**What happens.** The Console gives operators one role-aware place to run and oversee programs, in place of fragmented tools and spreadsheets. It carries dashboards with KPI tiles and universal search; program configuration including suspend, terminate, reactivate and spend limits; BIN and range management with capacity indicators; cardholder and card servicing including PIN reset, replacement and hold release; a live transaction feed with volume charts and export; approval workflows for sensitive actions; and a full audit trail with before and after values and rollback. Roles are system or custom, with per-environment permission matrices and delegated provisioning.
**Contributes.** So that a routine change is made by the person who wants it made, rather than raised as a ticket with the processor and waited on.
**Not in the Console at MVP**, and this list is part of the fact base because agents must not imply otherwise: self-registration by email and password, so SSO only at launch; creating and editing fraud rules, and the AI fraud copilot; digital wallet token management actions; audit-trail and disputes export; several production reconciliation exports. Developer-facing tools, API keys and webhooks, sit in the Developer Portal rather than the Console. (`PO` 3.2.)

### Step 9. Integrate and extend

**What happens.** All core functionality is reachable through the API before it appears in any screen, with event-driven integration through events, webhooks and reporting hooks for downstream systems. The Developer Portal carries documentation generated from the API itself, so it cannot drift from the live contract, an interactive explorer with real request and response handling, sandbox access, quick-start guides and code examples. The stated aim is time-to-first-successful-integration measured in minutes.
**Contributes.** So that the client's engineering team can integrate without a sales conversation in the way, and so that sandbox behaviour matches production behaviour.

### Step 10. Assist and automate under governance

**What happens.** The intelligence layer runs alongside the platform, **not inside the real-time transaction path**, which is the design choice that protects stability and latency. At MVP it establishes foundations: natural-language interaction, retrieval over TXN documentation, core orchestration for internal use, and a persistent Console assistant for summaries, guided setup, natural-language queries and report generation. Early agentic workflows execute only under explicit human approval. Every AI action is logged, attributable, and reversible where the underlying action allows.
**Contributes.** So that the specialist knowledge a card program normally requires sits in the platform rather than in a person the client has to hire.
**The rule that governs how this is described.** AI is the mechanism that delivers outcomes; it is never TXN's identity claim, and messages never lead with the technology. Ian, `S1`, on a competitor who *"suddenly announced themselves as the AI issuer. No, no, they're not. It's absolute nonsense."*

### Step 11. Structure BINs and program routing

**What happens.** BINs and BIN ranges are structured and allocated across the BIN sponsor, program owner and issuer-processor roles, and transactions are routed to the correct program. TXN treats BIN sponsorship as a first-class role in the platform and works with pre-integrated BIN sponsor relationships in each target market. TXN is the issuer processor and does not outsource its processing. (`PO` 3.1, 6.)
**Contributes.** So that a client does not have to assemble a sponsor relationship and a routing model before they can start.

### Step 12. Migrate an existing program

**What happens.** Migration is a work stream inside the launch mechanism, not a separate kind of engagement. (`S2` ruling: it is neither mechanically nor commercially distinct enough to be its own component track.) The capture-and-configure work is identical to a greenfield launch. **The large piece is the data migration and it sits on the client's side of the line:** the client requests the accounts and cards on TXN's platform, and the client owns extracting their data from the incumbent. Ian: *"There's work to be done that's not that much different from a TXN point of view."* The cleanest route in Ian's experience is reissuing new cards to every cardholder; he is sceptical of vendors who claim migration without reissue. Which route a client takes depends on why they are leaving: service-level dissatisfaction makes them resist reissue because everything else works, while leaving in order to launch a new product usually brings new branding anyway.
**Contributes.** So that a client with a live program can move without the move being a different product.
**Two client-side considerations, named because they decide the shape.** Disruption to the existing cardholder base, where reissuing as cards expire avoids a big-bang but strands recently renewed cards outside the window for another three to five years, so those are mopped up separately. And cost: Ian's industry estimate is roughly £2 or €2 per card all-in, covering plastic, branding, personalisation, production including the chip, and postage. **That is Ian's estimate from experience, not a TXN price, and it carries no source beyond him.**
**Not a claim.** Ian raised the idea that TXN could share or subsidise part of a reissue cost, because a scaled program with tens of thousands of already-spending cardholders is worth materially more than a greenfield one. He described it as something TXN *could* consider. **It is not an existing TXN lever and must not be offered.**

### Integrations and onboarding path

**Pre-integrated.** KYC, BIN sponsor and card manufacturing relationships, with scheme certifications managed by TXN. (`CM` 6.2, `OH` 3.)
**Multi-tenancy, stated honestly.** The standard shape is shared platform components with segregated databases per client. A client that needs it can stand up a completely separate environment. Ian, `S1`, asked whether one client flooding the system with bad API calls could affect others: *"Yes, we believe there still is a risk that it could impact other clients."* This is an active conversation between TXN and Direct Transact about the architecture. **It is in the fact base because it will be asked in procurement, and a denial would be false.**
**Onboarding path.** `unknown`, pending Dorte's write-up. See step 2.

---

## Section 3: Pain points

The buyer is a business that has decided a card is part of what it offers its own customers, and has discovered that the card is the easy part. What is hard is everything underneath it: the scheme relationships, the authorisation logic, the compliance obligations that differ by market, and the platform that either lets them change their mind or does not. Some of them are already live on a processor and cannot move at the speed their product needs. Some of them have never issued a card and do not know what they do not know. The pains below are shared, but they land on three different desks in three different ways.

### Buying-group roles

Ruled by Ian in `S2`, on the criterion of whose problem it is rather than who holds a veto.

**CTO**, primary user, approver with technical veto.
Optimises for clean integration, control of authorisation logic, and predictable behaviour under failure.

**CPO**, champion, contributor.
Optimises for building the product they want without the platform constraining them. Where a company puts product ownership somewhere other than a CPO, that is a note on this role rather than a fourth role.

**CFO**, economic buyer, approver with commercial veto.
Optimises for unit economics that work and pricing that stays predictable as volume scales.

**Not one of the three, deliberately.** Head of Payments is the DACI Driver who runs the evaluation, and Ian was clear that *"if we lose them, we never reach approval stage."* They remain a targeting persona in [[prospecting-process]]; the offer simply does not write pains against them.

### P1. Every routine change goes through the processor's ticket queue

**Situation.** The operations team cannot change program configuration, card controls or scheme parameters themselves. Each change is raised as a ticket with the processor and waits. `CM` 5 records the effect as operational drag, long lead times and escalation fatigue, and its own phrase is that teams *"feel they are not in control."*
**CTO.** Their team absorbs escalations it cannot fix and becomes an unwilling relay between operations and a vendor.
**CPO.** Every product change carries an invisible vendor dependency, so roadmap dates are estimates about somebody else's queue.
**CFO.** Headcount is being spent chasing rather than operating.
**Trigger events.** A launch date missed on a vendor lead time. A support backlog escalating to the executive team.
**Addressed by.** Section 2 step 8, and outcome O1.

### P2. The platform throttles product velocity

**Situation.** Running on a processor designed before cloud and APIs, every change is slow, costly and risky. (`CM` 5.) Iteration after launch costs as much as the launch did, so programs get set once and left alone.
**CTO.** Engineering capacity is consumed by plumbing rather than by proposition.
**CPO.** Feels this most acutely. Competitors ship card features they cannot match, and the constraint is not their own team.
**CFO.** Paying for engineering that produces no differentiated product.
**Trigger events.** A competitor launching a card feature. A re-platforming decision reaching the board.
**Addressed by.** Section 2 steps 1, 9, and outcomes O2, O4.

### P3. Running a card program needs card experts the business does not have and does not want to hire

**Situation.** Card product configuration involves properties that, without domain knowledge, carry real risk of breaking compliance or disrupting cardholders. `AITO` 3.1.1 names this expertise barrier as the primary reason businesses avoid adding card programs at all, or migrate slowly when they have one. The buyer is increasingly not a bank and has no card people to redeploy.
**CTO.** Asked to own a domain their team has never worked in, with the failure modes landing on them.
**CPO.** The product they want requires knowledge the company would have to buy before it could even scope the work.
**CFO.** Specialist hires with narrow, expensive skills, needed permanently to run something that is not the core business.
**Trigger events.** A card specialist resigning. A board asking why a card feature needs three new hires.
**Addressed by.** Section 2 steps 1, 10, and outcome O3.

### P4. Point vendors stitched together leave nobody accountable when it breaks

**Situation.** Processing, fraud, data and tokenisation bought from different vendors and wired together. `CM` 5 records the result as integration debt, reconciliation cost and unclear accountability when something goes wrong. The question that exposes it is who owns the problem at two in the morning when three vendors point at each other. (`OH` 4.2.)
**CTO.** Owns the integration surface between every vendor, and owns the incident when they disagree.
**CPO.** Changes that touch more than one vendor become projects rather than releases.
**CFO.** Multiple contracts, multiple renewals, and a total cost nobody can state in one number.
**Trigger events.** An incident where the vendors disagree on cause. A renewal cycle where the stack is re-tendered.
**Addressed by.** Section 2 steps 4, 5, 6, 7, 11, and outcome O5.

### P5. Program data is locked inside the processor

**Situation.** Data reachable only through batch files and limited reports. Product and risk teams cannot see cardholder behaviour in real time, so decisions lag reality. (`CM` 5.)
**CTO.** Builds and maintains an extraction layer to get at data the client already owns.
**CPO.** Iterates on the product without evidence of how the last change landed.
**CFO.** Cannot see program unit economics until the reporting cycle catches up.
**Trigger events.** A fraud pattern found late. A pricing decision taken without current data.
**Addressed by.** Section 2 steps 8, 9, and outcome O6.

### P6. Launching a first card program means committing before you know what you do not know

**Situation.** The greenfield buyer has never issued a card. There is no incumbent to compare against, no current spend to model, and no internal experience to sense-check a vendor's answers. `ICP2` established this as route 1, and its dominant pain as **exposure**. The register quantifies how invisible these companies are to a card-signal filter: greenfield accounts average 61.7 points against 74.4 for migration accounts, because the scoring framework measures card program maturity.
**CTO.** Being asked to approve an architecture in a domain where they cannot yet tell a good answer from a plausible one.
**CPO.** Building a business case on a cost base and a timeline they have no way to validate.
**CFO.** Signing for something whose real total cost only becomes visible after launch.
**Trigger events.** A board approving a card product in principle. A competitor in an adjacent category launching a card.
**Addressed by.** Section 2 steps 1, 2, 10, and outcomes O3, O4.

### P7. Card operations and engineering carry the same failure differently

**Situation.** Two distinct populations sit at a client and they are routinely conflated. **Card operations run the card program**, and they are not the technical team. **Engineering own the relationship with the platform**, because the platform is a technology product: they integrate it, keep it working, and own the connection into the client's own product and internal systems. The escalation path proves the split. Ian, `S2`, on what card ops says to their own tech team: *"we've got a problem with whatever's happening with the processing and you guys selected this, sort it out."*
**CTO.** Receives operational failures they did not cause, in a system they chose, from a team that cannot self-serve.
**CPO.** Operational friction shows up as roadmap slippage without ever being logged as a product problem.
**CFO.** Two teams spending time on one failure.
**Trigger events.** A processing incident escalating internally rather than to the vendor.
**Addressed by.** Section 2 step 8, and outcome O1.

### P8. Compliance obligations differ by market and knowing where to start is the work

**Situation.** Requirements vary by jurisdiction, scheme and product type. A client operating in the UK faces different obligations from one launching across EU markets, and UK and EU rules have been drifting apart since Brexit. (`AITO` 3.1.5, `OH` 3.) Without regulatory expertise on staff, every new market or product type starts with research rather than with building.
**CTO.** Implements requirements they had to discover first.
**CPO.** Market entry timelines set by legal review rather than by build effort.
**CFO.** Regulatory counsel engaged at every step, and exposure carried if a step is missed.
**Trigger events.** A decision to enter a second market. A new product type inside an existing program.
**Addressed by.** Section 2 steps 6, 10, and outcome O8.

### P9. Unit economics do not improve as the program scales

**Situation.** Cost per active card stays flat or worsens as volume grows, because the operational load grows with it and the fee structure does not step down. `CM` 6.5 places this on the CFO and on the day-to-day operational role.
**CTO.** Scale means more infrastructure work rather than less.
**CPO.** Growth in the program does not produce headroom to invest in it.
**CFO.** Feels this directly. The program gets bigger without getting more profitable.
**Trigger events.** A volume milestone passed with no change in unit cost. A margin review on the card line.
**Addressed by.** Section 2 step 10 and Section 7, and outcome O7.

### P10. Mid-contract with an incumbent, and moving feels impossible even when the case is clear

**Situation.** `ICP2` established this as route 3, full switch, with **entrapment** as its dominant pain: cumulative dissatisfaction blocked by migration risk. The blocker is rarely the contract alone. It is the cardholder base, the reissue question, and the absence of a route that does not disrupt live customers.
**CTO.** Owns a migration risk they cannot fully scope from inside the incumbent.
**CPO.** Every quarter of delay is a quarter of the roadmap they do not control.
**CFO.** Paying for a platform they have already decided to leave.
**Trigger events.** A contract renewal window opening. An incumbent incident or price increase.
**Addressed by.** Section 2 step 12, and outcome O5.

---

## Section 4: What changes

Before: the program is something the business owns commercially and does not control operationally. Changes are requests. Data arrives late. The specialist knowledge needed to run it either sits in expensive hires or does not exist in the building, and the cost of both is paid every month. After: the operations team makes changes themselves and sees them take effect, engineering integrates once and stays out of the operational path, and the platform carries the domain knowledge that used to have to be hired.

### O1. Routine changes are made by the team that wants them, the same day

**Before state.** Configuration, card controls and scheme parameters change by raising a ticket with the processor and waiting.
**After state.** An operator opens the Console, changes the setting, and the change is live, with the approval workflow and the audit trail recording who did it and what it replaced.
**Value lever.** Time, and control.
**Produced by.** Section 2 step 8.
**Pairs with pain.** P1, P7.

### O2. Product ships card features on its own release cycle

**Before state.** Product changes carry an invisible vendor dependency, so roadmap dates are estimates about someone else's queue.
**After state.** The product team scopes a card change against configuration and the API, and dates it against their own release cycle.
**Value lever.** Growth, and speed.
**Produced by.** Section 2 steps 1, 9.
**Pairs with pain.** P2.

### O3. The program runs without card experts on staff

**Before state.** Running the program requires domain knowledge the business does not have, so it either hires it or moves slowly and carefully around it.
**After state.** The team configures and operates the program in business language, with the platform explaining the effect of a change before it is made.
**Value lever.** Headcount, and risk.
**Produced by.** Section 2 steps 1, 10.
**Pairs with pain.** P3, P6.
**Evidence.** `AITO` 4.1 sets a target of 80 per cent of program configurations completed without TXN support intervention within six months of launch. **A target, not a result.**

### O4. Launch takes weeks rather than quarters, and changing it afterwards stays cheap

**Before state.** Launching a program is a project. Iterating on it after launch costs about as much as launching did, so programs get set once and left.
**After state.** The program goes live inside the launch window, and the changes after it are configuration rather than release cycles.
**Value lever.** Time, and money.
**Produced by.** Section 2 steps 1, 2, 9.
**Pairs with pain.** P2, P6.
**Evidence.** `AITO` 3.1.2 and 4.1 set a target of under ten business days from contract signature to first live transaction. **A target TXN set itself, unproven, and it must be presented that way until a client has been through it.**

### O5. One accountable platform replaces a stitched vendor set

**Before state.** Processing, fraud, data and tokenisation bought separately, with integration debt between them and an argument about cause whenever something breaks.
**After state.** Processing, data and programmable controls sit in one platform with one accountable owner, and incidents have one place to go.
**Value lever.** Risk, and money.
**Produced by.** Section 2 steps 4, 5, 6, 7, 11, 12.
**Pairs with pain.** P4, P10.

### O6. Program data is available as it happens

**Before state.** Data reachable through batch files and limited reports, so product and risk decisions lag reality.
**After state.** A live transaction feed, event-driven integration into the client's own systems, and reporting the operator can run without asking anyone.
**Value lever.** Time, and risk.
**Produced by.** Section 2 steps 8, 9.
**Pairs with pain.** P5.

### O7. Cost per active card falls as the program grows

**Before state.** Volume grows and the unit cost does not move, so scale does not produce headroom.
**After state.** Per-transaction rates step down as monthly volume rises, and the operational load that normally grows with volume is absorbed by the platform rather than by hires.
**Value lever.** Money.
**Produced by.** Section 2 step 10, and the fee structure in Section 7.
**Pairs with pain.** P9.

### O8. Compliance obligations are surfaced and applied rather than researched

**Before state.** Every new market or product type begins with finding out what the rules are.
**After state.** Applicable requirements are surfaced in plain English and offered for application; the client confirms rather than configures. A client operating in both the UK and the EEA runs both on one platform.
**Value lever.** Time, and risk.
**Produced by.** Section 2 steps 6, 10.
**Pairs with pain.** P8.
**The boundary, and it is not optional.** This is compliance confidence, not compliance replacement. TXN does not accept regulatory liability on the client's behalf. (`AITO` 3.1.5.)

---

## Section 5: Why us versus the status quo

A business that needs a card program today has four realistic moves, and three of them are chosen for good reasons. The legacy processors are chosen because they work and everybody knows they work. The first-wave modern platforms are chosen because they made integration possible for a normal engineering team. Building is chosen because it looks like control. And staying put is chosen more often than any of them, because moving is genuinely hard. TXN's argument is not that these are bad choices. It is that each of them makes the buyer accept a specific compromise, and that the compromise is structural rather than a matter of vendor quality.

**Two rules govern this section, and they are different rules.**

**One: competitors are never named in outbound. Settled, not pending.** (`R1`. Closes G4.) TXN's own documents name Marqeta, Paymentology, Thredd, Enfuce, Episode Six and Pismo freely and carry a specific counter for each, and that material stays where it is: `CL` and `OH` 4.1, for a human in a live conversation. **Agents contrast against the categories below and never against a company name**, including when a prospect names one first. A prospect naming a competitor is a conversation for a person, not a line for an agent to answer.

**Two: the Where it falls short lines below are context-not-quotable.** (`S3`.) They exist so an agent knows which TXN capability to lead with against a buyer in that situation. **They are never voiced, in any form.** An agent that states what the alternative cannot do has broken the rule even if it named nobody. What may be voiced is the differentiator claim and its substance, which are statements about TXN.

### The alternatives

**Legacy issuer processors.**
**Why buyers choose it.** They are proven, they hold deep scheme and licence coverage, and they carry customer bases that have run on them for years. Nobody is fired for choosing one.
**Where it falls short.** They were designed before cloud, APIs and modern cardholder expectations, so every change is slow, costly and risky, and routine configuration goes through the vendor rather than the operator.

**First-wave modern issuer processors.**
**Why buyers choose it.** They solved the developer surface. An API-first platform with real documentation and a sandbox made card issuing reachable for a normal engineering team, and that was the genuine breakthrough of the last decade.
**Where it falls short.** The operator was left where they started. The developer experience improved; the person running the program day to day still works through tickets, spreadsheets and fragmented tools, and still needs card expertise to do it safely.

**Building in-house.**
**Why buyers choose it.** Total control, no vendor dependency, and at year one the engineering looks tractable.
**Where it falls short.** Scheme compliance is not a one-off. Visa and Mastercard issue mandates periodically that every issuer processor must implement, and that engineering never stops. The cost profile is attractive in year one and painful in year three. (`OH` 4.2.)

**Staying on the incumbent.**
**Why buyers choose it.** It is the lowest-risk decision available on any given day, and it is often genuinely correct while a contract has years to run.
**Where it falls short.** It is a decision with a running cost: throttled product velocity and accumulating integration debt, paid for in customer value that goes elsewhere. `OH` 4.2 records it as the most common answer and the most expensive.

### D1. Control, speed and resilience in one platform, so the team does not pick a compromise

**Versus.** Legacy processors, first-wave modern processors.
**Substance.** The compromise is structural in both alternatives: legacy platforms hold reliability and cannot give velocity because of when they were built, and first-wave platforms gave velocity at the developer surface without taking the complexity out from underneath the operator. TXN carries three surfaces at once, the API, the Console and the intelligence layer, so the client chooses their mix rather than accepting the vendor's.
**Barrier countered.** "We already looked at modern processors and the operations problem did not go away."

### D2. The operator surface is a first-class product, not a reporting screen

**Versus.** First-wave modern processors, legacy processors.
**Substance.** Everything an operator needs is in one role-aware place: program configuration, card and cardholder servicing, live monitoring, approval workflows, and a full audit trail with before and after values and rollback. The competitive gap is specific and named in `CM` 12.2 as under-investment in the operator side by the modern cohort, and as legacy roots in the older one.
**Barrier countered.** "Our ops team will still be raising tickets, whatever the API looks like."

### D3. The intelligence layer runs outside the real-time transaction path, with a person in the decision loop

**Versus.** First-wave modern processors.
**Substance.** This is an architectural choice, not a positioning one: AI assists and automates routine work alongside the platform rather than inside authorisation, which is what protects stability and latency in the path where they matter. Early agentic workflows execute only under explicit human approval, and every AI action is logged, attributable and reversible where the underlying action allows.
**Barrier countered.** "We are not putting a language model in our authorisation path", and separately, "every processor is claiming AI this year."

### D4. Processing reliability comes through ownership, not a vendor contract

**Versus.** All four alternatives, and specifically against the objection that TXN is new.
**Substance.** Direct Transact, our co-founding owner, holds 25 years of processing operation, and the TXN platform is hosted and managed by Direct Transact within their existing data governance and security frameworks: the same frameworks that serve a client base of large South African retailers and banks. It is a 50 per cent co-founding ownership relationship, not an outsourcing arrangement, and TXN is the issuer processor rather than a reseller of anyone's processing.
**Barrier countered.** "You are pre-launch and unproven."
**Where this claim may be used, and it is the only differentiator with a placement rule.** (`R1`.) **Not in first touch, and not in the follow-up sequence.** The owners give credibility further down the sales process, once a prospect is engaged and asking who is behind this. They are never the reason the prospect opens the conversation. This sharpens the `S1` position that the joint venture is a reason to believe rather than the lead message: the reason-to-believe is now placed as well as ranked. D4 is objection-handling material, deployed in reply, not opening material.
**The honest half, and it stays attached.** Ian named this as one of the biggest risks in the whole proposition. Some buyers will have less appetite for the perceived risk of a new company, whether on personal comfort or on internal compliance policy. That cannot be argued away and TXN accepts it.

### D5. Europe is the whole business, not a region of a larger home market

**Versus.** First-wave modern processors.
**Substance.** A processor headquartered elsewhere prioritises its own larger home market for roadmap, budget and support. TXN's markets, phasing and scheme and BIN sponsor relationships are European, and the sub-sector coverage is built around European fintech categories rather than adapted to them.
**Barrier countered.** "We will just use the platform the US market uses."

### D6. Scheme neutrality on BIN sponsorship

**Versus.** First-wave modern processors, specifically any owned by a scheme.
**Substance.** TXN treats BIN sponsorship as a first-class role in the platform and works with pre-integrated sponsor relationships in each target market, with no scheme ownership sitting behind the recommendation. A processor owned by a scheme cannot demonstrate the same neutrality on sponsor choice.
**Barrier countered.** "Whose interest is being served when they pick our sponsor?"

### D7. The scheme mandate treadmill is absorbed rather than passed on

**Versus.** Building in-house.
**Substance.** Visa and Mastercard issue mandates periodically that every issuer processor must implement. A business that builds carries that engineering forever, on a schedule it does not set. TXN carries it, and the three surfaces give the control that building is usually chosen for, without the maintenance.
**Barrier countered.** "We would rather own it ourselves."

### D8. The competitive ground is deliberately not price

**Versus.** All four alternatives.
**Substance.** Ian, `S1`: *"they can compete on price but we're not going to do that, no one's interested in doing that."* The chosen ground is how easy it is for the client to do what they want to do, specifically not needing deep card expertise and not needing large teams to run a program. `OH` 2 makes this an operating rule for the sales motion: never lead on price, reframe on the cost of running the program, and offer narrower scope at the same rate before moving on fees.
**Barrier countered.** "You are more expensive than X."

---

## Section 6: Proof

**No verified TXN proof is available.** TXN is pre-launch: no clients, no case studies, no testimonials, no metrics from live operation, and no track record in its own name. Ian stated this plainly in `S2`: until TXN has its first client there are no TXN proof points, and there is no way around it. **This section stays empty of TXN claims until that changes.** Any agent that produces a TXN case study, a TXN uptime figure, or a TXN customer outcome is fabricating.

### What may be cited, with attribution, and where

Owner heritage only, attributed separately to each owner every time, with the sentence ending on what TXN delivers rather than on the owner.

**The placement rule, which binds harder than the wording rule.** (`R1`. Closes G5.) Direct Transact and Paycorp are owners and they carry real credibility, **but they do not appear in outbound first touch and they do not appear in the follow-up sequence.** They belong further down the sales process, in the conversation where a prospect has engaged and is asking who is behind this. An agent leading with the owners is answering a question nobody has asked yet, and it puts a South African payments business in front of a European fintech that has no reason to recognise either name. Ian's own framing in `S1`: *"I don't see why anybody in Europe would really have any knowledge of a South African payment business."*

**What that means operationally.** These figures ground the fact base and they are what a human reaches for when the credibility question arrives. They are not message material for a cold email or a LinkedIn message, and the critic should treat an owner claim appearing in first-touch copy as a fault rather than as colour.

**Direct Transact, our co-founding owner.**
25 years of processing heritage. Over R50bn processed monthly. 99.99 per cent uptime. Visa and Mastercard certification. PASA System Operator status. PCI DSS and ISAE 3402.
**Evidences.** D4.

**Paycorp, our co-founding owner.**
25 years of international payments experience. Over $9bn processed annually. Operations across Southern Africa, Central and Eastern Europe and the UK, with long-standing bank, scheme and regulator relationships.
**Evidences.** D4.

**The operational construct, as a claim in its own right.** The TXN platform is operated within an infrastructure and the associated processes that support Direct Transact's client base, which is large South African retailers and banks. Ian's framing of why this matters: it is not three people standing up a cloud environment, writing the security policies and chasing PCI DSS and GDPR from scratch. Some buyers read that as a strength and some as a weakness, and both readings are legitimate.

### Gate on the owner figures

**These figures are not yet cleared for market use.** Ian's instruction in `S2` is a process, not a list: Novosapien sources what is publicly available on Direct Transact and Paycorp, ranks it by what actually lands with a European fintech buyer, and brings a shortlist. The two shareholders then confirm what they are comfortable having in the market. **Until that confirmation lands, treat the figures above as candidates rather than as permitted claims.**

**No longer blocking the workforce, and this is why.** The placement rule above takes owner material out of every message the workforce sends, so an uncleared figure can no longer reach a prospect through outbound. The clearance exercise still matters, because the figures are what a human reaches for later in the same deal, and because the joint press release needs them. It is now a parallel workstream rather than a gate on the offer.

### Targets, which are not proof

`AITO` 4 carries a metrics register, and `PO` 5.2 carries platform design targets: availability, API latency percentiles, speed to deploy, recovery objectives, load testing. **Every one of them is engineered for launch and not production-proven.** They may be described as what the platform is built to, never as what it has done. `PO` states this discipline itself.

---

## Section 7: Commercial shape

Buying TXN is a licence plus usage. There is a fixed monthly fee for access to the platform, and then variable fees that track what the program actually does, falling per unit as the program grows. Ian's stated position on disclosure is unambiguous and it governs everything below: **no pricing numbers go into outbound, at all.**

**Pricing**
Two core principles. A **fixed monthly licence fee per client** to access the platform, covering the Control Center, the Knowledge Hub and unlimited API calls. Plus **volume-tiered variable fees**: one fee per settled transaction and one fee per 3D Secure authentication, with the unit fee falling as monthly volume rises. The intelligence layer is currently included in the licence fee. (`S1`. Ian noted that the pricing language as currently written has issues, so the wording here is his description of the model rather than a quotable rate card.)

**Price points**
**Not disclosed.** Ian, asked directly whether to disclose prices: *"no."* Brett confirmed the rule for the workforce: *"For balances and disclosure, definitely no. Do not name numbers."* Agents ground on the shape and never state a figure. A prospect asking for pricing is a conversation for a human.

**Commitment**
`unknown`. Term, minimums and notice have not been given.

**Entry path**
Sandbox access through the Developer Portal, or a working session with the solutions team. (`CM` 8.3.) For early customers there is a **first-client program with reference-friendly terms**; Ian's answer on what those terms are is **case by case**, and that is the complete answer rather than a gap.

**Risk reversal**
None offered. There is no guarantee to quote, and none should be implied.

**A live commercial rule that binds messages.** `OH` 2: never lead on price. Reframe on the cost of running the program and on total cost of ownership first, and offer a narrower scope at the same rate before moving on fees.

---

## The gaps list

Every field this document could not answer, as an explicit collection list. This is a deliverable, not an apology.

### The five that were blocking: resolved 2 September 2026

**Nothing blocks the offer now.** Four were ruled and one was parked, all on 2 September (`R1`). Recorded here rather than deleted, because a ruling that leaves no trace gets re-litigated.

| # | What it was | Ruling | Where it landed |
|---|-------------|--------|-----------------|
| G1 | The signature-to-first-live-transaction mechanism | **Parked.** No longer waiting on Dorte's write-up | Section 2 step 2, with the cost of parking it stated: the ten-day figure stays quotable as a target and may never be described as a process |
| G2 | What TXN sells that this offer does not cover | **Nothing.** The offer covers everything TXN sells | Section 1, `not_covered` |
| G3 | Which credentials are certified today as against engineered for | **Answered on 3 September, and it had already been answered when this gap was written.** TXN holds nothing of its own; PCI sits with Direct Transact; SOC 2 and ISO remain unknown and Ian owns the check | Section 1 credentials, rewritten 5 September. The residual unknowns are carried below |
| G4 | Competitor naming permission | **Never name a competitor in outbound.** Categories only, including when a prospect names one first | Section 5, settled rather than pending |
| G5 | Owner proof point shortlist | **The owners are credibility, placed late.** Not in first touch, not in the follow-up sequence; they belong further down the sales process | Section 6 placement rule, and the D4 placement rule |

### Carried to the next meeting with Ian and Dorte

| Item | What is needed |
|------|----------------|
| **Direct Transact's SOC 2 and ISO 27001 status** | The only part of the credentials question still open. Ian owns the check and said so on 3 September: *"We'll just have to double check that."* Everything else is settled and written into Section 1: TXN holds no accreditation of its own, PCI sits with Direct Transact, and the only permitted claim form is that the platform is operated within Direct Transact's accredited environment |
| **The owner proof clearance** | Still worth doing, no longer a gate. Novosapien sources and ranks what is public on Direct Transact and Paycorp for a European fintech buyer; the shareholders confirm what may go to market. It feeds the joint press release and the later-stage sales conversation, not the outbound messages |

### Company facts, cheap to answer, currently blank

| # | What is missing | Who |
|---|-----------------|-----|
| G6 | Founded date | Ian |
| G7 | Headquarters, and whether TXN Global Limited in Cyprus is the answer the fact base should give | Ian |
| G8 | Team size | Ian |
| ~~G9~~ | ~~The employee band ruling for `built_for`~~ | **Closed 3 September.** There is no band. Headcount is not a core ranking, sub-10 is explicitly in scope, and the parameter weight falls to 3 |
| G10 | Commitment terms: term, minimums, notice | Ian |

### Rulings needed on things this document had to guess

| # | What is missing | Who |
|---|-----------------|-----|
| G11 | **Offering type.** Routed `product` on Ian's own framing. If the launch-path work TXN's people perform is commercially distinct, the routing is `both` and every Section 2 step needs an actor label | Ian |
| G12 | **The `what_shifted` narrative.** The two-clock framing in Section 1 is ours, not his. The dates and the sequencing have never been confirmed | Ian |
| G13 | **The mechanism arc sentence** in Section 1. Derived from `PO` and the `S1` flow description; Ian has never sharpened it | Ian |
| G14 | **Which surface leads for the buyer we write to first.** `S2` settled that engineering owns the platform relationship day to day, which argues for the API; the operator experience is the differentiator, which argues for the Console | Ian |
| G15 | **Whether the banned-word list is complete**, or whether bans exist that never made it into a document | Ian |

### Known-unknown, tracked elsewhere

| # | What is missing | Where it lives |
|---|-----------------|----------------|
| G16 | TXN Data Residency Messaging Framework v1.0. Referenced by `JV` v2.3, never supplied | [[open-questions]] #56 |
| G17 | The boundary between queries the workforce answers and queries that always escalate to a human. Ian ruled that platform-origin questions are not automation territory; no general boundary exists | [[open-questions]] #65 |
| G18 | The Knowledge Hub content, which will be the first externally-facing material TXN has written in the register it actually uses with the market. Every document feeding this offer is internally focused | `S1` open action, chase Ian |

---

## Self-review gate

Run mechanically, 2 September 2026. Recorded so the next reader knows what was and was not checked.

| # | Check | Result |
|---|-------|--------|
| 1 | **Classification test.** Does Section 1 alone reveal the offering type? | **Pass, with a caveat.** Section 1 reads as a product. The caveat is G11: the routing is provisional pending Ian |
| 2 | **Adjective scan.** Any unverifiable quality adjective anywhere? | **Pass.** "Proven" survives only where attached to Direct Transact's 25 years, which is TXN's own approved formulation. Every inherited superlative from the source corpus was cut |
| 3 | **Fabrication scan.** Every claim traceable to something stated or confirmed? | **Pass, with five marked exceptions.** The mechanism arc, the `what_shifted` narrative, the underlying-problem framing, and the two-clock sequencing are derived and marked as such. Every performance figure is labelled a target |
| 4 | **Cross-ref audit.** | **Pass.** All ten pains resolve to a Section 2 step and a Section 4 outcome. All eight outcomes carry `produced_by` and `pairs_with_pain`. All eight differentiators ground in a Section 2 step. Section 6 entries evidence D4 |
| 5 | **Depth contract.** Section 2 longest; steps ≥2 sentences; 6 to 10 pains; 5 to 8 outcomes; 4 to 8 differentiators; 2 to 4 alternatives | **Pass on count** (12 steps, 10 pains, 8 outcomes, 8 differentiators, 4 alternatives). **Fails on one step by decision:** step 2 carries no mechanism, parked on 2 September, with the consequence written into the step rather than left implicit. Section 2 is the longest section |
| 6 | **Boundary sweep.** No steps in Section 1; no outcomes in Section 2 `contributes`; no comparisons in Section 4; no campaign objectives; no voice or audience profiles | **Pass.** Conversion rates, channel caps, domain warming and the 126-account list were all present in the source sessions and are deliberately excluded: they are campaign-layer configuration, and they live in [[commercial]] and [[delivery-schedule]] |
| 7 | **Own-words check.** Does Section 7 sound like the client? | **Pass.** The pricing description and the disclosure rule are Ian's wording |
| 8 | **Gaps list.** | **Pass, and the count is now auditable.** Fourteen open: 2 carried to the next meeting, 4 company facts, 5 rulings this document had to guess, 3 tracked elsewhere. Seven resolved: the five that were blocking, plus G3 and G9. Earlier versions of this row said thirteen and then eleven; both were wrong, because closed rows were subtracted twice. Counted row by row on 5 September |
| 9 | **Vocabulary check.** No banned word anywhere | **Pass.** Swept for all 24 banned terms, the em dash, and "programme". One deliberate retention: "partner" appears only as "BIN sponsor relationships", never applied to Direct Transact |
| 10 | **Presentation check.** Bold human labels, one field per line, JSON appendix | **Partial.** Labels and line discipline pass. **The JSON appendix is deliberately not generated**, because generating it before Ian has gated the document would create a stale machine artefact that the workforce would then read as truth |
| 11 | **Compound offers, track wiring** | **Not applicable.** No component tracks. Migration is a step, per the `S2` ruling |

**Two failures carried, both by choice rather than by omission.** Step 2 has no mechanism, parked on 2 September, and the offer states what that costs instead of pretending otherwise. Check 10 is deliberately incomplete: the machine-readable appendix is generated once Ian signs the document off, because generating it earlier would create a stale artefact the workforce would read as truth.

**Reconciled 5 September 2026 against the 3 September session**, which had already answered two gaps this document was still carrying as open. Two findings, both corrections rather than additions:

- **The credentials block was wrong, not merely incomplete.** It listed PCI DSS Level 1 among TXN's credentials with the status marked unknown. TXN holds no accreditation of its own; PCI is held by Direct Transact. A regulated procurement would have tested that claim first and it would not have survived. Rewritten to separate what is held, and by whom, from what the platform is engineered to.
- **The competition rule was under-stated.** The document banned naming a competitor. Ian's ruling is wider: never criticise the competition at all, in any of the four ICPs, and the Where it falls short material in Section 5 is grounding that agents must never voice.

Two gaps closed on the same reconciliation, G3 and G9, both of which had been answered in the room before this document recorded them as open.

**Revised 2 September 2026** against five rulings. Section 1 `not_covered`, Section 2 step 2, Section 5 competitor naming, Section 6 owner placement, D4 placement, the vocabulary doctrine, and the gaps list all changed. Checks 2, 3, 4, 6 and 9 were re-run over the changed passages and still pass.
