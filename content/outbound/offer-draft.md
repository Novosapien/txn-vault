---
description: "Draft TXN offer: pains, outcomes and differentiation derived from TXN's own GTM corpus and the vault, for Ian to redline rather than answer from scratch"
---

# TXN Offer, draft for redline

> **Section:** [[outbound]]
> **Status:** **Draft. Derived, not elicited.** Every claim below traces to a document TXN wrote or to a decision recorded in a session. Nothing here has been confirmed by Ian in this shape.
> **How to read it:** this exists so Ian corrects a draft instead of answering questions from a blank page. Strike anything wrong, sharpen anything close, and the survivors become the fact base the outbound agents speak from.

**What this is not.** It is not marketing copy and no prospect reads it. It is the boundary of what the agents are permitted to state as fact. Judge it on whether every line is true and defensible.

**The one structural caution.** The offer method says facts that live only in someone's head must be elicited, not mined. This draft deliberately breaks that rule for the sections where TXN's own documents are unusually good, and marks every place where the document is the only source and Ian has never said it out loud. Those are the lines most likely to be wrong.

**Source key.** `CM` Core Messaging v2.5 · `AITO` AI Target Outcomes Framework v1.0 · `CL` Competitive Landscape v0.2 · `OH` Objection Handling v1.1 · `PO` Product Overview v1.0 · `S1` offer session 24-08 · `S2` offer session 27-08 · `S3` session 02-09

---

## Section 1, what it is: the four fields still missing

Agreed already: the anchor line, the literal description, the two negatives, the platform definition, the provenance ruling and the hosting sentence. These four were never asked.

**Mechanism arc** *(one sentence, input to output)*
A client brings a product idea and its own customers; TXN configures and certifies the card program, processes every scheme message those cards generate, and returns the client a running program with the settlement position, the cardholder data and the controls to change it. *(derived from PO and S1 transaction flow. Ian has not sharpened this.)*

**The surface the buyer touches**
Two, and which one leads depends on the buyer. The Console is the operator surface and the API is the engineering surface, with the agentic layer sitting across both (`CM` 8.2, three surfaces). **Unresolved:** for the buyer we write to first, which is *the* surface. `S2` settled that the CTO and engineering own the platform relationship day to day, which argues for the API, but the operator experience is the differentiator, which argues for the Console.

**Underlying problem** *(market level)*
Card programs are run on platforms that were designed before cloud, APIs and modern cardholder expectations, and the businesses that want to launch one are increasingly not banks and hold no card expertise. The platform layer therefore taxes two different groups: those who have a program and cannot change it quickly, and those who want one and cannot start. *(`CM` 5, `AITO` 3.1.1, `S3` two buyer types.)*

**What shifted**
Two things, on different clocks. Businesses outside financial services began treating a card as a product feature rather than a banking product, so the buyer stopped being a bank. And the first wave of modern processors proved that an API-first surface was possible, which moved the bar from "does it have an API" to what the platform does with the complexity underneath. `CL` market trends record the next move: from late 2026 buying committees expect an AI layer and ask what outcomes it delivers rather than whether it exists. **Needs Ian: the dates and the sequencing are ours, not his.**

**Prior answers, and why insufficient**
Three. Legacy issuer processors, which are proven and slow. First-wave modern processors, which fixed the developer surface and left the operator with the same complexity. And building in-house, which looks attractive at year one and painful at year three (`CL` 3.4). None of them removed the expertise requirement, which `AITO` 3.1.1 names as the primary reason businesses avoid adding card programs at all.

---

## Section 3, pain points

Eight, each distinct. `CM` 5 supplied four; the other four come from `AITO`, `CL` and the two-buyer-type split. Impact is written per the three roles settled in `S2`: CTO, CPO, CFO.

### P1. Every routine change goes through the processor's ticket queue

**Situation.** The operations team cannot change program configuration, card controls or scheme parameters themselves. Each change is raised as a ticket with the processor and waits. `CM` 5 records the effect as operational drag, long lead times and escalation fatigue, and the phrase it uses is that teams *"feel they are not in control"*.
**CTO.** Their team absorbs the escalations they cannot fix, and becomes an unwilling relay between operations and a vendor.
**CPO.** Every product change carries an invisible vendor dependency, so roadmap dates are estimates about someone else's queue.
**CFO.** Headcount is being spent on chasing rather than operating.
**Trigger events.** A launch date missed on a vendor lead time. A support backlog escalating to the executive team.
**Addressed by.** The Console as a self-serve operator surface (`CM` 6.5, `PO`).

### P2. The platform throttles product velocity

**Situation.** Running on a processor designed before cloud and APIs, every change is slow, costly and risky (`CM` 5). Iteration after launch is as expensive as the launch was, so programs get set once and left.
**CTO.** Engineering capacity is consumed by plumbing rather than proposition (`CM` 6.2).
**CPO.** Feels this most acutely. Competitors ship card features they cannot match, and the constraint is not their team.
**CFO.** Pays for engineering that produces no differentiated product.
**Trigger events.** A competitor launching a card feature. A re-platforming decision reaching the board.
**Addressed by.** Cloud-native, API-first platform with sandbox-to-production parity (`CM` 6.1).

### P3. Point vendors stitched together create debt and unclear accountability

**Situation.** Processing, fraud, data and tokenisation sit with different suppliers, integrated by the client. `CM` 5 records the consequence as integration debt, reconciliation cost, and unclear accountability when something breaks.
**CTO.** Owns an integration surface they did not design and cannot consolidate.
**CPO.** Any new product feature needs several vendors to agree.
**CFO.** Multiple contracts, multiple renewals, and a total cost nobody can state in one number.
**Trigger events.** An incident where no vendor accepts ownership. A renewal falling due on one component.
**Addressed by.** One platform owning processing, data and programmable controls (`CM` 5).

### P4. Program data is locked in the processor and arrives in batches

**Situation.** Cardholder behaviour is visible only through batch files and fixed reports. `CM` 5: product and risk teams cannot see behaviour in real time, so *"decisions lag reality"*.
**CTO.** Builds and maintains a data pipeline to work around the processor.
**CPO.** Cannot evidence whether a product change worked.
**CFO.** Fraud losses and program economics are understood after the period, not during it.
**Trigger events.** A fraud episode found late. A board asking for program metrics that take a week to assemble.
**Addressed by.** Real-time data via streaming and APIs with a query layer (`CM` 5).

### P5. Running a card program requires card experts you would have to hire

**Situation.** Card product configuration involves properties that, without domain knowledge, carry real risk of breaking compliance or disrupting cardholders (`AITO` 3.1.1). `AITO` names the expertise barrier as **the primary reason businesses avoid adding card programs, or are slow to migrate**.
**CTO.** Asked to own a domain their team has never worked in.
**CPO.** Cannot scope the product because nobody internally knows what is possible or what it costs.
**CFO.** A business case that requires hiring a function the company does not have.
**Trigger events.** A card program reaching a board agenda without an internal owner. A hire for a card role that stays open.
**Addressed by.** The AI layer wrapping card mechanics in business language and proposing configuration by program type (`AITO` 3.1.1).
**Note.** This is the dominant pain for the value-add buyer type identified in `S1` and `S3`. It is the one pain the incumbent-side buyer does not feel.

### P6. Configuration mistakes are expensive and surface after the fact

**Situation.** A misconfigured spend control, a compliance rule applied wrongly, or a program-wide setting changed without understanding its blast radius. `AITO` 3.1.3 records the consequences as regulatory exposure, financial loss and cardholder disruption.
**CTO.** Owns the incident.
**CPO.** Cardholder trust is damaged by something invisible until it fired.
**CFO.** Carries the loss and the remediation cost.
**Trigger events.** A change that reached live cards unintentionally. An audit finding.
**Addressed by.** Impact stated before a change is applied, `AITO`'s worked example being *"this change will affect 4,000 live cards and triggers a notification obligation"*.

### P7. Compliance obligations differ by market and product, and you need counsel at every step

**Situation.** Requirements vary by jurisdiction, scheme and product type, and a client in the UK faces different obligations from one launching across EU markets (`AITO` 3.1.5). `CL` market trends add PSD3 landing through 2026 and 2027 and continuing UK and EU divergence.
**CTO.** Multi-market means multi-integration unless the platform absorbs the difference.
**CPO.** Every new market is a legal project before it is a product one.
**CFO.** Ongoing external counsel cost with no ceiling.
**Trigger events.** A market expansion decision. A regulatory change landing.
**Addressed by.** Applicable requirements surfaced and explained in plain English, with the client confirming rather than configuring (`AITO` 3.1.5).
**Boundary, and it is load-bearing.** `AITO` states this is compliance confidence, **not compliance replacement**. TXN does not accept regulatory liability on the client's behalf. Agents must not blur this.

### P8. Building in-house looked cheap at year one and expensive at year three

**Situation.** Teams that built issuer capability between 2018 and 2023 are now carrying the maintenance cost, and `CL` market trends record the conversation moving from build versus buy to buying a platform that leaves control of the parts that matter.
**CTO.** Maintaining scheme mandates and certifications is permanent work that produces no product.
**CPO.** The roadmap competes with the platform's own upkeep.
**CFO.** A cost base that was capitalised as a project and became an operating line.
**Trigger events.** A scheme mandate cycle. An engineering lead leaving who held the card knowledge.
**Addressed by.** Three surfaces so a buyer keeps the control they associate with building without the maintenance (`CL` 3.4).

---

## Section 4, what changes

Seven outcomes. Five are `AITO` 3.1 converted into before-and-after pairs; two come from `CM` pillars 2 and 5.

### O1. Run a card program without employing card experts

**Before.** The program needs someone who has done it before, and that person has to be hired or borrowed.
**After.** Configuration, operations and compliance alignment are done by the team already there, with the platform proposing and the team confirming.
**Lever.** Headcount, and the barrier to starting at all.
**Pairs with.** P5.
**Evidence.** `AITO` 4.1 sets a target of 80 per cent of configurations completed without TXN support intervention within six months of launch. **This is a target TXN has set itself, not a measured result, and must be written as one.**
**Note.** `AITO` calls this **TXN's core positioning claim**, with every other outcome supporting it.

### O2. Launch in days, not months

**Before.** Weeks of configuration, compliance review and technical integration before the first cardholder can transact.
**After.** Pattern recognition applies the configuration and the client confirms rather than configures.
**Lever.** Time, and revenue recognition.
**Pairs with.** P2, P5.
**Evidence.** `AITO` targets **under ten business days from contract signature to first live transaction**. It is a target. `S2` established that what the ten days consist of is not yet documented, so **agents state it as TXN's target and never as an achieved result.**

### O3. Fewer costly errors

**Before.** Mistakes are found after they have reached live cards.
**After.** The impact of a change is stated before it is applied.
**Lever.** Risk.
**Pairs with.** P6.
**Evidence.** `AITO` 3.1.3 defines the measure as a reduction in post-launch configuration errors and support escalations. No baseline exists pre-launch.

### O4. A program that improves without being asked

**Before.** Reactive. Something goes wrong, or a periodic review happens, and only then does the client learn the program could perform better.
**After.** Optimisation opportunities surface automatically, benchmarked against comparable programs.
**Lever.** Money, through fraud rates and programme economics.
**Pairs with.** P4.
**Caution.** `AITO` 3.2.4 is explicit that cross-program benchmarking becomes credible only as transaction volume accumulates. **Pre-launch there is no benchmark set, so this is a designed capability, not a live one.** Agents must not imply otherwise.

### O5. Compliance confidence without regulatory expertise on staff

**Before.** External counsel at every market and product step.
**After.** Applicable requirements surfaced and explained, client confirms.
**Lever.** Risk and time.
**Pairs with.** P7.
**Boundary.** Confidence, not replacement. Liability stays with the client.

### O6. Operators act instead of raising tickets

**Before.** Routine changes queue with the processor.
**After.** Program configuration, card controls and scheme parameters are changed in the Console in real time.
**Lever.** Time, and internal control.
**Pairs with.** P1.
**Evidence.** `CM` 6.5 claims support load drops and internal satisfaction rises. Unquantified, and it should stay unquantified until there is a client.

### O7. Engineering capacity moves from plumbing to proposition

**Before.** Integrations, reconciliations and scheme administration absorb the team.
**After.** Scheme compliance, managed certifications and pre-integrated KYC, BIN sponsorship and card manufacturing are carried by the platform.
**Lever.** Headcount and growth.
**Pairs with.** P2, P3, P8.
**Needs Ian.** `CM` 6.2 lists those integrations as evidence. `S2` asked which partners are named and the answer is on the information request. Until it comes back, "pre-integrated" is a claim without a list behind it.

---

## Section 5, why us

### The alternatives, compressed from five to four

**1. Stay where they are.** `CL` 3.5 names this **the most common competitor**, especially where the pain has not reached a trigger.
*Why buyers choose it:* it is free, it is safe this quarter, and a migration is genuinely disruptive.
*Where it falls short:* every month is throttled velocity and accumulating integration debt, and the cost is invisible because it is never invoiced.

**2. A modern issuer processor.** Marqeta, Paymentology, Thredd, Enfuce, Episode Six, Pismo. **Naming is gated and unconfirmed.**
*Why buyers choose it:* a real reference base, a known brand, and a developer surface that already solved the API problem.
*Where it falls short:* `CL` records each of the six as thinner in Europe than its brand implies, and, on TXN's reading, all of them optimised the developer surface and left the operator carrying the same complexity.

**3. Build in-house.**
*Why buyers choose it:* total control, and at year one it looks cheaper.
*Where it falls short:* scheme mandates and certifications are permanent work, and `CL` records buyers now moving away from this as the maintenance cost lands.

**4. Stitch point solutions together.**
*Why buyers choose it:* each component is best in class and can be swapped.
*Where it falls short:* the client owns the integration and the accountability gap when something breaks.

### The differentiators

**D1. The operator experience is a product, not a report.**
*Versus* alternative 2. *Substance:* the Console lets operations change program configuration, card controls and scheme parameters directly, where the comparison is a ticket queue. `CL` records the operator surface as where Paymentology and Thredd under-invest. *Counters:* "we already have a modern API, why move."

**D2. Processing heritage without the architecture that usually comes with it.**
*Versus* alternatives 1 and 2. *Substance:* the platform is TXN's, hosted and managed by Direct Transact within their existing data governance and security frameworks, and Direct Transact does that for banks, large retailers and businesses with hundreds of thousands to millions of cardholders. *Counters:* "will you still be here in five years", which `CL` records as a question the first wave cannot answer cleanly. **`S2` ruling: no statement about code lineage in either direction.**

**D3. Scheme neutrality is structural.**
*Versus* alternative 2, Pismo specifically. *Substance:* TXN is not owned by a scheme, so BIN sponsor and scheme choice carry no conflict. *Counters:* the neutrality question `CL` says appears in most competitive procurements. **Naming gated.**

**D4. One platform, one accountable party.**
*Versus* alternative 4. *Substance:* processing, data and programmable controls sit together, so the reconciliation surface and the incident owner are the same organisation. *Counters:* "we have best of breed already."

**D5. The AI layer is defined by outcomes, and the outcomes are written down.**
*Versus* alternatives 1 and 2. *Substance:* `AITO` defines five client outcomes with metrics and states that any AI claim not traceable to one should be reconsidered. *Counters:* AI-washing, which `S1` recorded Ian naming in a competitor. **Care: this is a claim about TXN's discipline, and the outcomes are targets, not results.**

**D6. Control without the maintenance.**
*Versus* alternative 3. *Substance:* three surfaces, so a team keeps the parts that matter and does not carry scheme mandates or certification cycles. *Counters:* "we would rather own it."

**Falsifiability check, and one fails.** D1, D3, D4 and D6 name something a competitor cannot claim. D2 is structural and holds. **D5 is weak as written**, because every competitor would say their AI is outcome-driven. It survives only if the argument is that the outcomes are published and measured, and that needs Ian's view.

---

## What this draft cannot do

**Section 2 still has one hole.** The product mechanism is well covered across `PO`, [[architecture]], the seven components and sixteen user journeys. What is missing is the launch path from signature to first live transaction, which is with Dorte. It underpins O2 and nothing else.

**Every quantitative claim here is a target or is unsourced.** The ten days, the 80 per cent, the "weeks not quarters". All TXN's own targets, none measured, and the draft marks each one. If Ian wants any of them stated as fact, that needs evidence attached.

**Nothing in Section 6 changes.** No proof, and the draft does not pretend otherwise.
