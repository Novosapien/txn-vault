---
description: "TXN ICP 4 buyer persona v2: the CTO or Head of Engineering who must make moving a live card program survivable; technical veto, proposed lead. The 12-section persona, ready to load when ICP 4 is active, with its sources, gaps and cuts below"
status: draft, 19 Oct 2026, reworked from personas-icp-4.md (4 Sep), on hold with ICP 4
---

# ICP 4 persona: CTO or Head of Engineering

> **Up:** [[icp-4-full-switch|ICP 4]]. **On hold with ICP 4** (no reference customers, no migration tooling): the persona is ready and does not load until Ian decides whether ICP 4 gets outreach. The text between the two horizontal rules follows the 12-section persona standard (`cofounder: …/concepts/guidelines/buyer-persona.md`) and is what loads into the product's persona `definition`. Message rules live in the [[messaging-protocol|messaging protocol]], not here. Every quote is derived, not heard from a buyer.

---

### CTO or Head of Engineering (Approver, technical veto, proposed lead)

**1.0 Archetype Name** The Escape Planner

**2.0 Role & Functional Identity**
- **2.1 Primary Function:** Owns the question that decides this deal: not whether to move, but whether moving a live card program is survivable.
- **2.2 Core Responsibilities:**
  - Scoping a migration of live cardholders and live data off a platform they do not control and cannot fully inspect.
  - Establishing what the current contract permits on extracting the cardholder data, and what the extraction looks like in practice.
  - Owning the cutover: the sequencing, the rollback, the window, and what happens to a transaction in flight.
  - Running the existing program at full reliability throughout, because the customers do not know a migration is happening and must not find out.
  - Carrying the integration debt of the separate providers that have gathered around the program over the years.
- **2.3 Scope, Seniority & Authority:** Scope: business. Seniority: executive. Decision Authority: leads the evaluation; holds the technical veto; does not hold the commercial signature.

**3.0 Psychographic Profile**
- **Identity & Self-Image:** The person who argued for the move and is now responsible for making it not go wrong, which is a lonelier position than being right.
- **Core Values / What They Optimise For:** Reversibility. Any step they cannot undo is a step they will interrogate at length.
- **How They Measure Their Own Worth:** By whether the customers ever notice. A migration nobody noticed is the highest form of the craft.
- **Worldview & Biases Toward This Category:** Has lived with a card platform long enough to know what vendor promises are worth, and applies that scepticism to every vendor, including the one they want to move to. Reads confidence about migration as inexperience.

**4.0 A Day in the Life**
They have wanted this move for a long time. Now that it is real, they are the one listing the ways it could hurt the company. Their spreadsheet holds every integration that touches the current platform, and it keeps growing: a reporting job nobody remembers writing, a reconciliation script, a webhook consumer in a service that was deprecated but never turned off. Then there is the data: they have no clean answer on what the contract lets the company extract, or in what state it will arrive. Every cardholder has a card in their pocket that works today. That fact, more than the contract, is what keeps the project in the slow lane.

**5.0 Pains & Fears (Expanded Dossier)**
- **5.1 Operational Pains (Daily Fires):**
  - **"I keep finding another thing that touches the platform."** The migration scope keeps growing by something written years ago by somebody who has left.
  - **"I do not know what data we can get out, or in what state."** The contract is unclear, and the practical answer sits with the provider we are leaving.
  - **"There is no version of this plan without a moment of risk to live cards."** I can shrink that moment. I cannot remove it, and that is the sentence I have to say out loud.
- **5.2 Strategic & Political Pains:**
  - **"I argued for this, so if it goes wrong it is mine twice over."** Once for the choice and once for the execution.
  - **"Everyone above me is treating this as procurement."** They are comparing platforms. I am planning an operation on a live system, and those are different meetings.
  - **"The current set-up works, which is the strongest argument against doing anything."** Nobody gets fired for the platform they already have.
- **5.3 The Deepest Fear:** A cutover window where a meaningful number of cardholders cannot pay, it is visible to customers and then to the press, the rollback is slower than the runbook claimed, and the company's own name carries it. Not a failed migration: a public one.

**6.0 What They've Already Tried (and Why It Disappointed)**
- **Escalated their requirements with the current processor, repeatedly and at senior level:** it brought attention and some improvement, and it did not change the decision to move.
- **Built their own layers around the current set-up (retries, caching, reconciliation tooling, monitoring):** it works, it is now a system of its own, and maintaining it is part of the cost of staying.
- **Scoped a partial migration, moving one product first:** it modelled well, then failed on shared cardholder records and shared reporting, which is what made this a full switch.
- **Asked other engineering leaders how their migrations went:** each described a longer and messier process than planned, and each named reissue as the question that dominated everything.

**7.0 Decision Criteria & Objections**
- **What they weigh evaluating this category:**
  - What migration tooling exists today, as opposed to what the migration will be supported by.
  - How much of the cutover can be reversed, and how long a rollback takes in practice rather than in a document.
  - Whether the API covers every integration they must rebuild, without screen-based workarounds.
  - Whether the vendor is honest about the parts it does not own, in particular extracting the data from the current processor.
- **Objections / sources of resistance:**
  - "Tell me exactly which parts of this migration are ours and which are yours. Do not blur that."
  - "What does your migration tooling do today? Not the approach. The tooling."
  - "What happens to a transaction in flight during cutover?"
  - "Where does state live, and how is it reconciled between your system and ours?"
  - "Where does the intelligence layer sit relative to the transaction path?"
  - "You are pre-launch, and I am putting my whole live card base on you."
  - "Who holds the accreditations on the environment I am about to move my card base onto?"

**8.0 Trigger Events (Why Now)**
- A card payment incident visible on the company's own status page or to its customers.
- A payments or platform hire whose remit reads as migration or vendor consolidation, which means the move is being staffed.
- Joining the company as a new head of technology, which opens the platform to review.
- A scheme mandate with a deadline, which makes the dependency on the current set-up concrete rather than theoretical.

**9.0 Information Diet & Trusted Voices**
- Engineering leaders who have personally run a processor migration: the most valuable source they have, and a call they will take at any notice.
- Public status pages and incident histories, followed over long periods, for their current provider and for candidates.
- Developer portals and sandboxes, read as evidence about a vendor's engineering culture.
- Their own incident record, which is the argument they have already made internally.

**10.0 Success Metrics (What "Good" Looks Like)**
- From a cutover plan with a step that cannot be undone, to one that is rehearsed, timed and reversible.
- From separate providers that dispute ownership during an incident, to one platform with one accountable owner.
- From layers maintained on their own side to compensate, to behaviour they can rely on, with the workarounds deleted.
- From a migration scoped on assumption, to one scoped on a verified data extract and a measured cutover window.

**11.0 The Message That Lands**
This buyer has already decided to move, so the message lowers the risk of the move rather than creating desire for it. The angle is an exact line of ownership, stated before they ask: migration runs as a work stream inside the launch, the capture-and-configure work is the same as for a new program, and extracting the data from the current processor sits on the client's side of the line. They already know that last part is true, so saying it plainly earns more trust than a claim to handle it.

**12.0 Example Titles**
Chief Technology Officer · VP Engineering · Head of Payments Engineering · Director of Platform · Head of Card Operations Technology · Principal Architect, Payments

---

## Sources

| Part | Source |
|---|---|
| Role (approver, technical veto, proposed lead) | The ICP 4 buying group in [[icp-definition]] §10 (Novosapien drafting, 3–4 Sep): the CTO leads, proposed and **not confirmed by Ian**. The technical veto: the buying-group roles in [[offer]] Section 3 (`S2`) and Ian's primary-user scaffold ([[persona-primary-user]] §3.4) |
| Sections 2, 3, 4, 6, 9, 10 | Derived by Novosapien from ICP 4, the offer and the 4 Sep persona. No buyer was interviewed |
| Section 5 pains | Derived from the ICP 4 pain mapping and [[offer]] P10 (the CTO owns a migration risk they cannot fully scope from inside the current processor). The data question: [[offer]] step 12 (the client owns extracting its data). Every quote is derived |
| Section 7 objections | "Where does state live": Ian's primary-user scaffold ([[persona-primary-user]] §7). Migration tooling: Ian's gate, 3 Sep, *"they don't expect a 15 year old approach"* (recorded in [[icp-definition]] §10). The accreditation question: the answer is in [[messaging-protocol]] (M8). The rest: Novosapien, from the 4 Sep persona |
| Section 8 triggers | The hire whose remit reads as migration, and the new head of technology: the state modifiers in [[icp-4-full-switch]]. The rest derived |
| Section 11 | [[offer]]: step 12 (migration inside the launch; capture-and-configure the same as for a new program; the data extraction on the client's side of the line) |

## Gaps to settle

| Gap | Why it matters |
|---|---|
| The lead buyer: does the CTO lead in ICP 4? | Novosapien's proposal ([[icp-definition]] §10, [[buyer-personas]] gap P4); Ian has not confirmed it. It sets who gets the first message |
| What migration tooling will exist, and when | A gate on ICP 4, and the CTO's tooling objection has no answer until it is settled |
| "You are pre-launch" | True today; ICP 4 opens only after reference customers exist, so this objection may need a new form by then |
| Real buyer language for the quotes | Every quote is derived; Ian and Dorte should correct them |
| Triggers and information diet | Derived from the ICP signals and role conventions, not from real deals |

## What was cut from the 4 Sep version

| Where | What changed | Why |
|---|---|---|
| 4 Sep preamble | Not carried. The on-hold status and its two gates are in this file's header line. The two message bans (never criticise the current processor; never offer to share the reissue cost) stay in [[messaging-protocol]] | Status belongs in the header; message rules belong in the [[messaging-protocol|messaging protocol]] |
| Heading | "leads, weighting unconfirmed" replaced with "technical veto, proposed lead" | The CTO lead is Novosapien's proposal; it is now a gap |
| 2.2 | "the incumbent contract" and "a stitched vendor set that has accumulated around the incumbent" replaced with "the current contract" and "the separate providers that have gathered around the program" | The vocabulary of the revised ICP, with no judgement of the current processor |
| 2.3 | "holds the veto that most often stops it" replaced with "holds the technical veto" | "Most often" was never stated, and the 4 Sep CFO persona made the same claim for its own veto |
| 3.0 | "arguing for this for two years" and "interrogate for weeks" lose their durations | Invented specifics |
| 4.0 | Third person. Removed "for two years" and "I have asked twice" | Invented specifics |
| 4.0 | Removed "any plan I write has a moment in it where that stops being unconditionally true" and "My board thinks this is a vendor decision. It is a live-customer event with a vendor decision attached to it" | Repeated 5.1 (the moment of risk) and 5.2 (treated as procurement) |
| 5.1 | "Every week" removed | Invented frequency |
| 6.0 | "Pushed the incumbent hard on the specific failures ... no structural change, which is what converted frustration into a decision" replaced with an escalation that "did not change the decision to move" | TXN never criticises the current processor. The attempt and its result stay |
| 6.0 | "Two useful conversations" replaced with "each"; "than the vendor had described" replaced with "than planned" | Invented count; an implied criticism of another vendor |
| 7.0 | Added Ian's objection "Where does state live, and how is it reconciled between your system and ours?" | From Ian's primary-user scaffold §7; it fits a migration |
| 8.0 | Removed "Contract renewal approaching" and "An acquisition or a funding round that triggers a platform review" | Repeated across the three personas; kept in the CFO persona, where term, notice and funding sit |
| 8.0 | "A significant incident on the incumbent" replaced with an incident on the company's own status page; "A scheme mandate the incumbent handles slowly" replaced with "A scheme mandate with a deadline" | Framed as the buyer's own signals, not as the current processor's failings. The incident wording follows the ICP 4 signal |
| 8.0 | Added "Joining the company as a new head of technology" | A state modifier in the revised ICP 4 |
| 9.0 | Removed "Reachable by a message about migration mechanics specifically", and the line after it on which topics are noise | A message instruction that repeated 11.0 |
| 11.0 | Cut from seven sentences to three. Removed: the consolidation point (processing, controls, authentication and settlement in one platform); "say nothing about their incumbent"; the instruction to acknowledge the pre-launch position; the accreditation position; "never offer to share the reissue cost" | 11.0 holds the angle and one claim. The consolidation point stays in 10.0 and in the ICP 4 pain mapping. The rest are message rules, held in [[messaging-protocol]] |
