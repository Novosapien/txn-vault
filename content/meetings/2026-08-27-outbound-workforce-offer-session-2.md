---
date: 2026-08-27
type: general
description: "Offer track session 2 with Ian: migration is a step not a track, the platform provenance ruling, evolution over disruptor, and the buying group settled as CTO, CPO, CFO"
scope:
  - "[[outbound]]"
  - "[[commercial]]"
  - "[[vision]]"
status: extracted
extracted-to:
  - "[[outbound]]"
  - "[[open-questions]]"
---

# TXN: Outbound Workforce, Offer Session 2 (2026-08-27)

> **Source:** working session run live against the offer question bank, Brett relaying to Ian Johnson. No Gemini transcript; the record is the working exchange itself. Continues [[2026-08-24-outbound-workforce-interview-1-offer]] and runs alongside the ICP work held on [[outbound]].
>
> **Shape of the session.** The mechanism block was moved offline: Dorte is writing up the signature-to-first-live-transaction sequence and sending it through. The live time went on the questions only Ian can answer, and eight of them closed.

## Decisions taken

### Migration is a step, not a component track

The offer schema promotes something to its own component track only if it is **mechanically distinct and commercially distinct**. Migration passes neither cleanly, so it is written as a work stream inside the launch mechanism.

Ian's reasoning, in full, because the nuance matters more than the ruling:

- **Same as greenfield:** understanding what the client wants to achieve and capturing it, so the program can be configured. That part is identical either way and sits in Dorte's write-up.
- **The big exercise is the data migration**, and it sits on the client's side of the line. The client requests the accounts and cards on TXN's platform, and the client owns extracting their data from the incumbent. *"There's work to be done that's not that much different from a TXN point of view."*
- **The cleanest route in Ian's experience is reissuing new cards to all cardholders.** Vendors who claim migration without reissue exist; Ian is sceptical of the claim.
- **Which route a client picks depends on why they are leaving.** Service-level dissatisfaction means everything else works and they want the path of least resistance, so they resist reissue. Leaving in order to launch a new product usually brings new branding anyway, so reissue matters less. No one-size-fits-all.
- **Two considerations, both landing on the client.** First, disruption to the existing cardholder base: reissuing as cards expire avoids a big-bang, but leaves recently renewed cards stranded outside the window for another three to five years, so those get mopped up separately. Second, cost.

> **Reissue cost, Ian's estimate:** roughly **£2 / €2 per card** all-in, covering the physical plastic, branding, personalisation, production including the chip, and postage. At 100,000 cards that is material. **Recorded as Ian's industry estimate, not a TXN price**, and it carries no source beyond his experience.

**The commercial lever, and why it did not flip the ruling.** Ian raised the idea that TXN could share or subsidise part of the reissue cost, on the reasoning that a scaled program with tens of thousands of already-spending cardholders is worth materially more to TXN than a greenfield program that must first attract cardholders and then wait for spend to ramp. He described it as something he has done before and as something **TXN could consider**, not as an existing TXN lever. That is the second half of the promotion test failing: without a confirmed commercial difference, migration stays a step.

### The platform provenance ruling

This resolves a contradiction between what [[2026-08-24-outbound-workforce-interview-1-offer]] recorded and what Ian stated today, and it is the most load-bearing item in the session.

Session 1 recorded that TXN's technology is its own, built now, and that the owners contribute know-how, heritage and capital but **not the platform**. Today Ian said elements did start from the DT code base.

**Ian's ruling, and the distinction he drew:** there is the context and the reality, and separately there is what gets positioned. They are not the same document.

- **The external claim is simply: the platform is TXN's.** Nothing about how it was built. Not "built new", not "built from the ground up".
- **What "the platform" means**, as the definition agents work from: the core card management capability, plus the knowledge hub, the Control Center, the API layer, and the agentic AI layer. Ian: *"the knowledge of all of that is our IP that we're building."*
- **The hosting sentence, to be used as the confidence line:** the platform is hosted and managed by Direct Transact within their existing data governance and security frameworks. The confidence comes from DT doing exactly that for companies that insist on it, meaning banks, large retailers, and businesses with hundreds of thousands to millions of cardholders.
- **Code lineage is never stated.** Ian's reasoning: no upside, and one clear downside, which is inviting *"they've been in place for 25 years, so was that code legacy in the first place that you built from?"*
- **For internal context only**, and deliberately kept out of the fact base: where existing code already met requirements it was taken; where requirements were new it was built from scratch; where existing code needed enhancing and modernising it was enhanced.

**Banned list additions from this ruling:** `built from the ground up`, `built new`.

**Effect on the session 1 negatives.** "Not a legacy platform repackaged for export" survives as a risk to head off, but the answer to it changes. It is no longer a claim that TXN's technology is new. It is the two sentences above, and no engagement on lineage.

### Positioning: evolution, not disruptor

Open since the content workshop on 19 August. Ian: **evolution.**

Consistent with the existing vocabulary doctrine, which already bans *disrupt*, *revolutionary*, *transformative* and *game-changing*. Differentiation claims are therefore framed as doing the existing job better, never as replacing the category.

### The buying group: CTO, CPO, CFO

The offer takes one to three roles, and the five-role DACI framework in Role-Based Messaging V1 has more than that. Ian's ruling is **CTO, CPO, CFO**.

Novosapien proposed CTO, Head of Payments, CFO on the basis of who holds a veto that stops the deal. Ian corrected the criterion: the question is not who blocks, it is **whose problem it is**, which is the right test because the offer field is how the same pain lands differently on each role.

| Role | Optimises for |
|------|---------------|
| **CTO** | Clean integration, control of authorisation logic, predictable behaviour under failure |
| **CPO** | Building the product they want without the platform constraining them |
| **CFO** | Unit economics that work, and pricing that stays predictable as volume scales |

**On the product function.** Ian's first framing was that it is the function rather than the title: whoever drives product strategy and product delivery, the people who start with what they want to build and work back to what has to be in place, whose test is that the platform lets them build without constraint. He then corrected the attempt to make that a fourth abstract label: *"keep the three as CTO, CPO and CFO. And then there'll be the product function lying across one of those."* Where a company puts product ownership elsewhere, that is a note on the CPO role, not a separate role.

**Head of Payments does not disappear.** Role-Based Messaging has them as the DACI Driver who runs the evaluation, and *"if we lose them, we never reach approval stage."* They remain a targeting persona in [[prospecting-process]]; they are simply not one of the three the offer writes pains against.

### Why the Primary User is engineering, not card operations

Ian explained the reasoning behind [[persona-primary-user]], and it is worth recording because "primary user" reads as "the person using it most" and that is not what it means here.

There are two distinct day-to-day populations at a client:

- **Card operations run the card program.** Not engineering, not the technical team. An operations team, card ops, or whatever it is called locally.
- **Engineering own the relationship with TXN's platform**, because TXN is a technology product. They integrate it, they keep it working, and they own the connection into the client's own product and internal management systems.

The escalation path is the proof: card ops hits a processing problem and goes to their own tech team, *"we've got a problem with whatever's happening with the processing and you guys selected this, sort it out."*

Strong material for the pain points section, because it is observable and it shows the same problem landing differently on two roles. Also relevant to the persona track, where whether card operations earns its own persona is now an open shape rather than an oversight.

## The proof position, stated plainly

Ian on what TXN can and cannot claim before its first client. Recorded close to verbatim because the wording threads the banned-word list and any paraphrase risks putting a banned phrase back in.

- Until TXN has its first client there are **no TXN proof points**, and there is no way around it.
- What TXN can say: **the TXN platform is operated within an infrastructure and the associated processes that support Direct Transact's client base.** That client base is large South African retailers and banks.
- Ian named this as **one of the biggest potential risks**. Some buyers will have less appetite for the perceived risk of a new company, on personal comfort or on internal compliance. Others will not. Nothing can be done about it and it is accepted.
- **The mitigation is two-part.** The strength of the co-founding owners, and the operational construct: it is not three people standing up Azure, writing the security policies and chasing PCI DSS and GDPR from scratch. The platform is operated within an environment that already manages all of that. Some buyers read that as a plus, some as a negative.

**First-client program terms: case by case.** That is the complete answer and it is written as such.

**Owner proof points are a process, not a list.** Ian's instruction: Novosapien sources what is publicly available on Direct Transact and Paycorp, ranks it by what actually lands with a European fintech buyer, and brings a shortlist. The two shareholders then confirm what they are comfortable having in the market. Ian also thinks that exercise feeds the joint press release, which he, Bronwyn and Steve are starting.

**Incoming: JV Messaging Framework v2.3.** Built off work done on 26 August covering exactly this ground. Ian is sending it. Now that hosting, data residency and team ownership are settled, the messaging can describe the real position rather than an intended one.

## Flagged for the workforce build, not the offer

Ian made a point that sits outside the offer and matters more than the question that prompted it.

Asked how an agent should handle a buyer digging into the platform's origins, his answer was that this is **not automation territory at all**: *"we've got to be careful about the type of automation that we're comfortable handling, the type of queries we're comfortable handling with automation, and those that will never be handled by it."* His own move would be to say it is a TXN platform and then work out what is actually behind the question. Is the concern technical debt? You cannot know without asking, and you cannot script it.

**There is no defined boundary today** between the queries the Cold Outreach Workforce answers and the ones that always escalate to a human. Raised as [[open-questions]] #65.

## Method notes

- **A correction to our own framing.** Novosapien recorded a three-way conflict between the Role-Based Messaging deck, the persona scaffolds and the 21 August workshop over the buying group. On review there is no conflict: the deck, [[persona-champion]], [[persona-primary-user]] and [[persona-economic-buyer]] describe one consistent five-role DACI framework. The framing was wrong and is withdrawn.
- **Session 1's balances question is not reopened here.** [[open-questions]] #55 stands as filed.
- The offer's mechanism section remains the largest gap in the fact base and is now with Dorte.

## Still open for Ian

| Item | Needs |
|------|-------|
| What TXN sells that this offer does not cover | One line. "Nothing" is a complete answer |
| The employee band ruling | ICP v0.4 says 10 to 5,000 with 20 to 2,000 ideal; Core Messaging v2.5 and [[persona-primary-user]] still say 20 to 2,000 |
| Competitor naming in outbound | Named, or categories only. TXN's own documents name all six freely |
| Whether the banned-word list is complete | Or whether bans exist that never made it into a document |
