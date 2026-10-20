---
description: "TXN ICP 2 buyer persona v2: the CTO or Head of Engineering who carries the cost of running two processors with one team; approver, weight in this buying group unconfirmed. The 12-section persona, ready to load, with its sources and gaps below"
status: draft, 19 Oct 2026, reworked from personas-icp-2.md (4 Sep)
---

# ICP 2 persona: CTO or Head of Engineering

> **Up:** [[icp-2-new-program-incumbent-stays|ICP 2]]. The text between the two horizontal rules follows the 12-section persona standard (`cofounder: …/concepts/guidelines/buyer-persona.md`) and is what loads into the product's persona `definition`. Message rules live in the [[messaging-protocol|messaging protocol]], not here. Every quote is derived, not heard from a buyer.

---

### CTO or Head of Engineering (Approver, weighting unconfirmed)

**1.0 Archetype Name** The Two-Stack Owner

**2.0 Role & Functional Identity**
- **2.1 Primary Function:** Owns the engineering consequence of a decision made on product grounds: two processors, two integrations, two reconciliations, one team.
- **2.2 Core Responsibilities:**
  - Integrating a second platform without destabilising the first, which is live and carrying real cardholders.
  - Deciding how much of the existing internal abstraction can be reused, and how much has to be rebuilt because it was written against one vendor's shape.
  - Owning two sets of reconciliation, two sets of scheme reporting and two escalation paths, permanently.
  - Judging whether the programs ever touch, because if they never do the cost is duplication, and if they do the cost is much larger.
  - Protecting a team that is being asked to learn a second platform while it operates the first.
- **2.3 Scope, Seniority & Authority:** Scope: department to business. Seniority: executive. Decision Authority: a technical veto; owns the integration estimate that shapes the business case; does not own the vendor selection.

**3.0 Psychographic Profile**
- **Identity & Self-Image:** The person who carries the operational reality of decisions taken elsewhere, and who has stopped being surprised by that.
- **Core Values / What They Optimise For:** Total system cost over time, not project cost. They are the only person in the room thinking about year three.
- **How They Measure Their Own Worth:** Whether the estate stays comprehensible. Two of anything is a comprehension cost, and they are the one who pays it.
- **Worldview & Biases Toward This Category:** Has integrated a processor before, so they know how long the last stretch of an integration takes and which parts of the documentation will turn out to be aspirational. Sceptical of anything described as easy by someone who has not maintained it.

**4.0 A Day in the Life**
Everyone else is discussing which platform; they are the only one costing what happens afterwards. The company will have two of everything: two integrations, two reconciliations, two sets of scheme reporting, two places to look when a number does not match, and the same people doing all of it. Nobody has asked them whether that is acceptable. They have been asked how long it takes, which is a different question with a much more comfortable answer. This afternoon they have to give product an estimate, and the honest version has a large number in it for work that is not integration at all: generalising the internal code the team wrote when there was only one program. They have been through a card integration before and know its shape; what they do not know is what running two feels like once both are live.

**5.0 Pains & Fears (Expanded Dossier)**
- **5.1 Operational Pains (Daily Fires):**
  - **"We are about to have two of everything and one team."** That is the real cost, and it does not appear in any business case.
  - **"Our internal abstraction was written against one vendor, and it shows."** Much of the integration work is not integration: it is undoing an assumption we made when we had one program.
  - **"I am being asked how long, not whether."** The decision arrives as a schedule question, which is how the ongoing cost gets skipped.
- **5.2 Strategic & Political Pains:**
  - **"The people making this call do not carry it."** Product wins a capability, engineering owns a permanent second estate, and those are not weighed against each other anywhere.
  - **"If either program has a bad month, it lands on me, and the first question will be whether the second platform caused it."** The new platform gets the blame for everything until it has a record.
  - **"I cannot argue against this without sounding like I am protecting the status quo."** Raising the cost of two reads as resistance rather than as accounting.
- **5.3 The Deepest Fear:** That the second program is integrated competently, the team then spends a growing share of its time reconciling across two platforms, the velocity everyone was promised quietly disappears into that, and nobody connects the two facts. Not a failed integration: a slow tax that nobody can trace.

**6.0 What They've Already Tried (and Why It Disappointed)**
- **Built an internal abstraction layer over the first processor:** it works, and it encoded that vendor's model so deeply that it is now an obstacle rather than an asset.
- **Estimated building the new program's processing in-house:** the build was plausible; the ongoing scheme mandate work was not, and that is what closed it.
- **Asked peers running two processors what it actually costs:** found very few people who had done it, and the ones who had gave answers more discouraging than the business case assumes.

**7.0 Decision Criteria & Objections**
- **What they weigh evaluating this category:**
  - Whether the API surface is complete enough that the second integration needs no screen-based workarounds.
  - Whether sandbox and production behave the same, because they will test against it while they run something else in production.
  - What the reconciliation and reporting surface looks like, since that is where the duplicated cost lives.
  - Whether operations can self-serve, because every configuration change that needs engineering doubles in a two-platform world.
- **Objections / sources of resistance:**
  - "The integration is not my concern. Running two for years is. Talk to me about that."
  - "Where does state live, and how is it reconciled between your system and ours?"
  - "Where does your intelligence layer sit relative to the transaction path?"
  - "You are pre-launch, and I am putting a live second program on you."
  - "Which certifications do you hold today, as opposed to building towards, and who holds them?"

**8.0 Trigger Events (Why Now)**
- A product decision that arrives as a schedule request, which is usually the first they hear of it.
- Multi-region infrastructure going live around a single-region card program, which makes the asymmetry structural rather than temporary.
- A second core banking or ledger instance being stood up, which is the moment the two-estate question becomes real.
- A distribution deal with a date, which removes the option of doing this slowly.
- Losing or failing to replace a payments engineer, which changes the capacity arithmetic entirely.

**9.0 Information Diet & Trusted Voices**
- Engineering peers who have run two processors.
- Developer portals and sandboxes, used as the primary evidence of a vendor's seriousness.
- Public status pages and incident histories, watched over months rather than checked once.
- Internal evidence above all: their own reconciliation breaks, their own on-call load, their own team's estimates.

**10.0 Success Metrics (What "Good" Looks Like)**
- From an internal abstraction that encodes one vendor, to one that holds two without leaking.
- From every configuration change needing engineering, to operations changing program settings themselves on both estates.
- From reconciliation as a recurring investigation, to reconciliation with mismatches flagged and a place to look.
- From an unquantified second-estate tax, to a running cost they measured, predicted and can defend.

**11.0 The Message That Lands**
Lead on the years after the integration, because that is where this buyer's cost sits. The claim that cuts through is that routine changes to the new program do not have to go through engineering: operators change program configuration, card controls and scheme parameters themselves, and everything is reachable through the API before it appears in any screen. Name reconciliation with mismatch flagging, because it is where the cost of running two programs lands.

**12.0 Example Titles**
Chief Technology Officer · VP Engineering · Head of Payments Engineering · Head of Platform Engineering · Director of Engineering, Cards · Principal Engineer, Payments

---

## Sources

| Part | Source |
|---|---|
| Role (approver, weighting unconfirmed) | [[icp-definition]] §10 (Novosapien drafting, 3–4 Sep): "CTO weighting is open", because this is the only status where the company runs two processors in parallel. **Not confirmed by Ian.** The technical veto comes from Ian's primary-user scaffold ([[persona-primary-user]] §3.4), which was written for a switch, not for this status |
| Experience from the first integration (§3, §4) | Ian, 2 Sep L764-768: they arrive *"with a bunch of knowns and experiences they've had that they're going to want to make sure they're not going to have with you again"*. The revised [[icp-2-new-program-incumbent-stays\|ICP 2]] core thesis |
| How the pains are framed | Ian, 3 Sep L669-679 (*"it's the latter"*): the current processor is never attacked. Every pain here is about running two, not about the first processor |
| Sections 2, 3, 4, 6, 8, 9, 10 | Derived by Novosapien from ICP 2, [[icp-definition]] §10, the offer and the 4 Sep persona. No buyer was interviewed |
| Section 5 pains | Derived from the two-processor cost in [[icp-definition]] §10 (two integrations, two reconciliations, two sets of scheme reporting, one team) and from Ian's primary-user scaffold ([[persona-primary-user]] §5: integration that becomes a long-term constraint; being trapped in a vendor-specific API shape). Every quote is derived |
| Section 7 objections | Ian's primary-user scaffold ([[persona-primary-user]] §7): where state lives and how it is reconciled. The intelligence layer, pre-launch and certification objections are from the 4 Sep persona; the offer's credentials section holds the certification answer |
| Section 11 | [[offer]]: O1 (operators change configuration, card controls and scheme parameters), step 8 (the Console), step 9 (API first), step 7 (reconciliation with mismatch flagging) |

## Gaps to settle

| Gap | Why it matters |
|---|---|
| **How much the CTO matters in ICP 2.** The company runs two processors in parallel, which either makes the CTO central or barely involves them if the programs never touch. Ian has not ruled | Sets whether this persona gets a message at all, and whether TXN raises the cost of running two or answers it only when asked |
| Does the CTO hold a technical veto in ICP 2? | The veto comes from a scaffold written for a switch |
| Real buyer language for the quotes | Every quote is derived; Ian and Dorte should correct them |
| Triggers and information diet | Derived from the ICP signals and role conventions, not from real deals |

## What was cut from the 4 Sep version

| 4 Sep item | Change | Why |
|---|---|---|
| The file's opening flag on the CTO's weight | Moved to Gaps to settle | The persona stays in full; the open question is a gap, not persona text |
| §3 "how long the last 20 per cent takes" | Now "the last stretch of an integration" | A number nobody stated |
| §4 first person | Third person | Agreed v2 layout |
| §4 "the internal abstraction we wrote against one vendor's model" | Now "the internal code the team wrote when there was only one program" | The vendor-shaped abstraction is already in §2.2, §5.1, §6 and §10 |
| §4 "what running two feels like in month nine" | Now "once both are live" | Invented duration |
| §4 "and neither does anyone I have asked" | Cut | Repeated §6 (asked peers) and §9 |
| §5.1 "Two reconciliations, two escalation paths, two mental models" | Cut from the expansion | Repeated §2.1, §2.2 and §4 |
| §5.1 "Half the integration work ... an assumption we made three years ago" | Now "Much of the integration work ... when we had one program" | Invented share and duration |
| §5.2 "The new thing gets blamed for everything for a year" | Now "until it has a record" | Invented duration |
| §5.3 "eighteen months later the team is spending a third of its time" | Now "a growing share of its time" | Invented duration and share |
| §6 "Pushed the capability request into the incumbent's roadmap process ... a queue position" | Cut | Described the current processor declining a request (Ian, 3 Sep L669-679) |
| §6 "Estimated building the missing capability in-house" | Now "the new program's processing"; the result is kept | "Missing capability" implied a deficiency |
| §7 "The next three years of running two is" | Now "Running two for years is" | A number nobody stated |
| §7 "Which of these do you hold today ..." | Now names certifications | "These" had no referent once §11 lost the accreditation text |
| §7, new objection | "Where does state live, and how is it reconciled ...?" | Ian's primary-user scaffold §7, which fits a two-processor estate |
| §8 trigger on a deal with a date | Now "A distribution deal with a date" | The 4 Sep wording used a word from the literal-check list; the new wording is the ICP's own term |
| §9 "who are rare enough that finding one is itself an event" | Cut | Repeated §6 and the CPO's information diet |
| §9 "Reachable only through technical specificity ..." | Cut | An outreach instruction, not an information source |
| §11 "Say nothing at all about their existing processor" | Cut | A message rule |
| §11 the accreditation paragraph (TXN holds none; PCI with the co-founding owner; the operated environment) | Cut | A message rule, and it names an owner; it lives in [[messaging-protocol]] (M8) |
| §11 "be equally direct about the pre-launch position" | Cut | A message instruction; the pre-launch objection stays in §7 |
| §11 the remaining message | Kept as the angle (the years after the integration) and the claim (operators self-serve, API first), with reconciliation named | Cut to three sentences |
