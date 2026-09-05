---
description: "Three buyer personas for ICP 4, the full switch: the engineer who owns migration survivability, the product lead who owns cardholder disruption, and the CFO holding the reissue bill"
---

# Buyer Personas: ICP 4, full switch

> **Up:** [[buyer-personas]]
> **Parent ICP:** [[icp-definition]] Section 10, ICP 4. Archetype `Full-Switch Migrator, the Blocked Escapee`.
> **Dominant pain inherited by all three:** **entrapment.** Cumulative dissatisfaction blocked by migration risk. The blocker is rarely the contract. It is the cardholder base, the reissue question, and the absence of a route that does not disrupt live customers.
> **Buying group as the ICP defines it:** CTO leads (**proposed, not yet confirmed by Ian**), CPO carries the cardholder disruption question, CFO carries the reissue cost.
> **Grounded on:** [[offer]] Section 2 step 12 for the migration mechanism, Section 7 for the commercial shape, Section 4 for what may be promised.

**These three personas are built and not yet usable, and that is deliberate.** ICP 4 is last in priority and gated on two things rather than one. Nobody moves a full suite to a company with no track record, so reference customers are the first gate. The second is a product dependency: Ian, 3 September, on buyers expecting migration tooling, *"they don't expect a 15 year old approach"*. ICP 4 therefore waits on something being built as well as something being won. The personas exist so that the moment both gates clear, the work is done rather than started.

**Two things must never appear in a message to any of them.** TXN must not criticise the incumbent, even here, where the buyer has already decided the incumbent failed them: state what TXN does and let the buyer say the rest. And the idea that TXN might share or subsidise the reissue cost is **not an existing lever** and must not be offered, hinted at, or used to open a conversation.

---

## Persona 4.1: CTO or Head of Engineering (Approver, leads, weighting unconfirmed)

**1.0 Archetype Name** The Escape Planner

**2.0 Role & Functional Identity**
- **2.1 Primary Function:** Owns the question that decides this deal, which is not whether to move but whether moving is survivable.
- **2.2 Core Responsibilities:**
  - Scoping a migration of live cardholders and live data off a platform they do not control and cannot fully inspect.
  - Establishing what the incumbent contract permits regarding data extraction, and what the extraction actually looks like in practice.
  - Owning the cutover: the sequencing, the rollback, the window, and what happens to a transaction in flight.
  - Running the existing program at full reliability throughout, because the customers do not know a migration is happening and must not find out.
  - Carrying the integration debt of a stitched vendor set that has accumulated around the incumbent over years.
- **2.3 Scope, Seniority & Authority:** Scope: business. Seniority: Executive. Decision Authority: leads the evaluation in this ICP, holds the veto that most often stops it, does not hold the commercial signature.

**3.0 Psychographic Profile**
- **Identity & Self-Image:** The person who has been arguing for this for two years and is now responsible for making it not go wrong, which is a lonelier position than being right.
- **Core Values / What They Optimise For:** Reversibility. Any step they cannot undo is a step they will interrogate for weeks.
- **How They Measure Their Own Worth:** By whether the customers ever notice. A migration nobody noticed is the highest form of the craft.
- **Worldview & Biases Toward This Category:** Has lived with a platform long enough to know exactly what vendor promises are worth, and applies that scepticism uniformly, including to the vendor they want to move to. Reads confidence about migration as inexperience.

**4.0 A Day in the Life**
I have wanted to move for two years and now that it is real I am the person listing the ways it kills us. There is a spreadsheet with every integration that touches the current platform and I keep finding new rows: a reporting job nobody remembers writing, a reconciliation script, a webhook consumer in a service we deprecated but did not turn off. Then there is the data. I do not have a clean answer on what we are contractually able to extract or what state it comes out in, and I have asked twice. And underneath all of it, the thing that actually keeps this in the slow lane: every one of our cardholders has a card in their pocket that works today, and any plan I write has a moment in it where that stops being unconditionally true. My board thinks this is a vendor decision. It is a live-customer event with a vendor decision attached to it.

**5.0 Pains & Fears (Expanded Dossier)**

**5.1 Operational Pains (Daily Fires)**
- **"I keep finding another thing that touches the platform."** Every week the migration scope grows by something written years ago by somebody who has left.
- **"I do not know what data we can actually get out, or in what state."** The contract is ambiguous and the practical answer is in the hands of the people we are leaving.
- **"There is no version of this plan without a moment of risk to live cards."** I can shrink that moment. I cannot remove it, and that is the sentence I have to say out loud.

**5.2 Strategic & Political Pains**
- **"I argued for this, so if it goes wrong it is mine twice over."** Once for the choice and once for the execution.
- **"Everyone above me is treating this as procurement."** They are comparing platforms. I am planning an operation on a live system, and those are different meetings.
- **"The current setup works, which is the strongest argument against doing anything."** Nobody gets fired for the platform they already have.

**5.3 The Deepest Fear:** A cutover window where a meaningful number of cardholders cannot transact, it is visible to customers and then to the press, the rollback is slower than the runbook claimed, and the company's own name carries it. Not a failed migration. A public one.

**6.0 What They've Already Tried (and Why It Disappointed)**
- **Pushed the incumbent hard on the specific failures, repeatedly and at senior level.** Got attention, some improvement, and no structural change, which is what converted frustration into a decision.
- **Built compensating layers on their own side: retries, caching, reconciliation tooling, monitoring the vendor.** It works, it is now a system of its own, and maintaining it is part of the cost of staying.
- **Scoped a partial migration, moving one product first.** Modelled well, then collapsed on shared cardholder records and shared reporting, which is what made this a full switch.
- **Asked other engineering leaders how their migration went.** Two useful conversations, both of which described a longer and messier process than the vendor had described, and both of which raised reissue as the thing that dominated everything.

**7.0 Decision Criteria & Objections**
- **What they weigh evaluating this category:**
  - What migration tooling actually exists, as opposed to what the migration will be supported by.
  - How much of the cutover is reversible, and how long a rollback takes in practice rather than in a document.
  - Whether the new platform's API surface is complete enough to rebuild every integration without screen-based workarounds.
  - Whether the vendor is honest about the parts they do not own, particularly the extraction from the incumbent.
- **Objections / sources of resistance:**
  - "Tell me exactly which parts of this migration are ours and which are yours. Do not blur that."
  - "You are pre-launch, and I am putting my entire live card base on you."
  - "What does your migration tooling actually do today? Not the approach. The tooling."
  - "Where does the intelligence layer sit relative to the transaction path?"
  - "What happens to a transaction in flight during cutover?"
  - "Who holds the accreditations on the environment I am about to move my entire card base onto?"

**8.0 Trigger Events (Why Now)**
- A significant incident on the incumbent, particularly one visible on a public status page or to their own customers.
- A payments or platform hire whose remit reads as migration or vendor consolidation, which means the escape is being staffed.
- Contract renewal approaching, which is the only moment the whole position is genuinely open.
- An acquisition or a funding round that triggers a platform review with an external sponsor behind it.
- A scheme mandate the incumbent handles slowly, which makes the dependency concrete rather than theoretical.

**9.0 Information Diet & Trusted Voices**
- Engineering leaders who have personally run a processor migration. This is the highest-value source available to them and they will take that call at any notice.
- Public status pages and incident histories, tracked over long periods, for their own vendor and for candidates.
- Developer portals and sandboxes, evaluated as evidence about the vendor's engineering culture.
- Their own incident record, which is the argument they have already made internally.
- Reachable by a message about migration mechanics specifically. Anything about velocity or transformation is noise to a person planning an operation.

**10.0 Success Metrics (What "Good" Looks Like)**
- From a cutover plan with an irreversible step in it, to one that is rehearsed, timed and reversible.
- From a stitched vendor set with disputed ownership at incident time, to one platform with one accountable owner.
- From compensating layers maintained on their own side, to behaviour they can rely on and delete their workarounds.
- From a migration scoped on assumption, to one scoped on a verified extract and a measured cutover window.

**11.0 The Message That Lands**
This buyer has already decided; the message has to reduce risk, not create desire. Be exact about the line of ownership, because that is what earns their attention: migration is a work stream inside the launch mechanism, the configure-and-capture work is identical to a greenfield launch, and **the data extraction from the incumbent sits on their side of the line**. Saying that plainly is more persuasive than claiming to handle it, because they already know it is true and every vendor who implies otherwise loses them. Then the consolidation point, that processing, controls, authentication and settlement sit in one platform, so the migration reduces the vendor count rather than moving it. Say nothing about their incumbent, in any register: this buyer has decided the incumbent failed them and may say so freely, and TXN still does not. Acknowledge the pre-launch position before they raise it, and give the accreditation position straight: TXN holds none of its own, PCI sits with Direct Transact, our co-founding owner, and the platform is operated within that accredited environment. Never offer to share the reissue cost.

**12.0 Example Titles**
Chief Technology Officer · VP Engineering · Head of Payments Engineering · Director of Platform · Head of Card Operations Technology · Principal Architect, Payments

---

## Persona 4.2: CPO or Head of Product (Champion, owns the cardholder consequence)

**1.0 Archetype Name** The Keeper of the Cardholder

**2.0 Role & Functional Identity**
- **2.1 Primary Function:** Owns what the migration feels like to the person holding the card, which in this ICP is the difference between a technical project and a customer event.
- **2.2 Core Responsibilities:**
  - Deciding, with the CTO, between reissuing every card and running the existing base to expiry, and owning the customer consequence of either.
  - Designing the communication: what cardholders are told, when, and how many times before their card changes.
  - Protecting activation and spend through a period where a customer is being asked to do something they did not ask for.
  - Holding the product roadmap still while the migration runs, and defending that pause internally.
  - Judging which cohorts can absorb disruption and which cannot, because the base is not uniform.
- **2.3 Scope, Seniority & Authority:** Scope: business. Seniority: Executive. Decision Authority: owns the customer experience and the reissue approach, does not own the technical decision or the commercial signature, and can stall the deal by refusing the disruption.

**3.0 Psychographic Profile**
- **Identity & Self-Image:** The advocate for the person who never asked for any of this. They see themselves as the only one in the room representing someone who is not in it.
- **Core Values / What They Optimise For:** Trust, measured over years rather than quarters. A customer who stops trusting the card stops using it and does not tell you why.
- **How They Measure Their Own Worth:** By retention and by active card usage through and after a change. Flat is a win.
- **Worldview & Biases Toward This Category:** Understands that infrastructure decisions become customer experiences, and has watched a previous technical change land badly on customers who were not considered until late.

**4.0 A Day in the Life**
Everyone else is discussing platforms and I am discussing a letter. If we reissue, several thousand people receive a card they did not ask for, with instructions, and some proportion of them will not activate it, and some proportion of those were our best customers and are now not customers at all. If we run to expiry instead, we operate two platforms for years and I have cards that renewed last month sitting outside the window for another three or four, which someone will have to mop up separately and which will be my problem then too. I have spent this morning segmenting the base by how much disruption each cohort can absorb, which is not something the engineering conversation has any interest in, and it is the single largest variable in the outcome. Nobody in the migration meeting has asked me what happens to activation. They have asked me when I can approve.

**5.0 Pains & Fears (Expanded Dossier)**

**5.1 Operational Pains (Daily Fires)**
- **"Every migration option puts a task on the customer, and every task loses a percentage."** Activation is the number that decides whether this was worth it and nobody upstream is tracking it.
- **"Cards that renewed recently are stranded outside any run-to-expiry window."** Three to five more years, then a second exercise, and it lands on my team.
- **"I am being asked to approve a date, not a plan."** The migration timeline arrives as a fact and the customer communication is expected to fit inside it.

**5.2 Strategic & Political Pains**
- **"The roadmap stops for this and I have to defend that to people who did not choose it."** A quarter or more of no new product, in exchange for a platform nobody outside this building will see.
- **"If activation drops, it will be read as a product failure rather than a migration cost."** The attribution will not survive the quarter.
- **"I did not ask for this migration and I carry its most visible consequence."** Engineering wanted it, finance sized it, I explain it to customers.

**5.3 The Deepest Fear:** That a segment of long-standing, high-value cardholders quietly stop using the card during the reissue, never say why, and the company discovers eight months later that it traded a chunk of its best cohort for a platform change. Not a bad launch. An invisible loss they could have prevented if anyone had asked them earlier.

**6.0 What They've Already Tried (and Why It Disappointed)**
- **Run a smaller card change before: new art, a new range, a re-brand.** Learned exactly what activation drop looks like, which is why they are the most cautious person in this process.
- **Modelled a phased reissue by cohort.** Better on paper, much worse operationally, because it means the base is in two states for a long period and support has to hold both.
- **Asked the incumbent what a managed migration would look like.** The answer was unhelpful for obvious reasons, and it removed the last hope of a route with no customer impact.
- **Pushed for the migration to wait until after a major product release.** Granted once, and the delay cost the company its renewal window, which is why nobody will grant it again.

**7.0 Decision Criteria & Objections**
- **What they weigh evaluating this category:**
  - Whether the migration approach genuinely allows a choice between reissue and running to expiry, or whether one is being assumed.
  - How much of the disruption can be absorbed by the platform rather than passed to the cardholder.
  - Whether the new platform lets them keep the card product identical, so nothing changes for the customer beyond the plastic.
  - How much control they retain over timing, because customer communication has to lead the technical schedule.
- **Objections / sources of resistance:**
  - "What does the cardholder actually have to do? Give me the exact steps."
  - "How do I explain this to someone whose card works perfectly well today?"
  - "If we run to expiry, what happens to the cards that renewed last month?"
  - "Who is accountable if activation drops, and what is the plan if it does?"

**8.0 Trigger Events (Why Now)**
- A migration decision reaching a date, which converts a debate into a customer communication deadline.
- An incident on the incumbent that customers noticed, which changes the internal balance because doing nothing is no longer free.
- Contract renewal, which makes the timing somebody else's decision rather than theirs.
- A card range approaching mass expiry, which is the one moment a run-to-expiry approach is genuinely cheap.
- A brand or product refresh already planned, which is the only situation where reissue costs the customer relationship almost nothing.

**9.0 Information Diet & Trusted Voices**
- Product leaders who have run a reissue, sought out specifically for the activation numbers nobody publishes.
- Their own customer research, support tickets and churn analysis, which is the evidence they trust above all.
- Customer experience and lifecycle communities rather than payments ones.
- Their own base, segmented, which is the argument they will bring to every meeting.
- Reachable by a message that treats the migration as a customer event, which almost nobody does, and which distinguishes the sender immediately.

**10.0 Success Metrics (What "Good" Looks Like)**
- From an activation cliff at reissue, to activation flat through the change.
- From a base in two states for years, to a single platform on a timeline they set.
- From customer communication squeezed into a technical schedule, to the schedule built around the communication.
- From a card product that changes because the platform changed, to one where the customer experience is identical either side.

**11.0 The Message That Lands**
Almost nobody talks to this persona at all, so speaking to them directly is itself the differentiator. Lead on the choice rather than on the platform: the reissue-or-run-to-expiry decision is theirs, it depends on why the company is moving, and there is no single right answer. Name the trap they already know about, that running to expiry strands recently renewed cards outside the window for another three to five years and produces a second exercise later. Then the claim that matters to them, which is that program behaviour is configuration, so the card product can be reproduced as it stands and the customer experience does not have to change because the platform did. Do not describe the migration as painless, because they have done this before and will stop reading. Never offer to share the reissue cost, and say nothing about the incumbent.

**12.0 Example Titles**
Chief Product Officer · Head of Product, Cards · Director of Customer Experience · Head of Card Portfolio · VP Product, Consumer · Head of Lifecycle Marketing

---

## Persona 4.3: CFO or Finance Director (Economic Buyer, holds the reissue bill)

**1.0 Archetype Name** The Reissue Arithmetic

**2.0 Role & Functional Identity**
- **2.1 Primary Function:** Owns the one number in this deal that is real rather than modelled: what it costs to put a new card in the hand of every cardholder they have.
- **2.2 Core Responsibilities:**
  - Sizing the migration cost, of which reissue is the dominant and least avoidable component.
  - Weighing that one-off against the ongoing saving, and establishing over how many years it pays back.
  - Owning the exit from the incumbent contract: notice, term, early termination, and what is still owed.
  - Funding a period where the company pays two platforms at once, which is short, certain and rarely modelled.
  - Answering for a large, visible, one-off cost that produces no new revenue.
- **2.3 Scope, Seniority & Authority:** Scope: business. Seniority: Executive. Decision Authority: final commercial signature, owns the exit negotiation, and holds the veto that most often postpones this deal by a year.

**3.0 Psychographic Profile**
- **Identity & Self-Image:** The person who insists the full cost is on the table before anyone commits, and who has been proved right often enough to be unembarrassed about it.
- **Core Values / What They Optimise For:** Completeness of the number. A cheap decision with a missing line is worse than an expensive one that is fully stated.
- **How They Measure Their Own Worth:** By whether the actual cost matched the approved cost. Payback discipline is the professional standard they hold themselves to.
- **Worldview & Biases Toward This Category:** Knows the ongoing saving is real and knows the one-off is what kills these projects. Has seen a migration business case resting on the run rate with the transition cost added late, and does not intend to approve another.

**4.0 A Day in the Life**
The saving is not the hard part. I believe the run rate improves, I can see the argument, and I could defend it. The hard part is a one-off number that buys nothing new: two pounds a card, near enough, all in, and we have a lot of cards. That is a line that produces no revenue, delivers no feature, and exists solely to arrive at a position we could describe as the same place with a different supplier. Then there is a period where we pay both, which is certain and which nobody has put in the model. Then there is the exit: notice, term, whatever is still owed, and a negotiation with a company that has no reason to help us. I asked for a payback period this morning and got a range, and I sent it back. If I approve this, I am approving a number that will be discussed at every board meeting for four quarters, so it needs to be complete before it is presented, not after.

**5.0 Pains & Fears (Expanded Dossier)**

**5.1 Operational Pains (Daily Fires)**
- **"The reissue is a large cash cost that buys nothing new."** Plastic, personalisation, chip, postage, per card, and we have a lot of cards.
- **"There is a period where we pay two platforms and it is not in anybody's model."** Certain, short, and always missing.
- **"Every business case I get back leads with the run rate and buries the transition."** I keep sending them back and they keep coming back the same way.

**5.2 Strategic & Political Pains**
- **"Approving this makes it mine at every board meeting for a year."** A visible one-off cost has an owner in a way an ongoing saving never does.
- **"The exit negotiation is with a counterparty who benefits from us being slow."** They know we are leaving and they hold the notice period.
- **"If activation drops after reissue, the saving evaporates and the cost does not."** The downside is asymmetric and it lands after I have signed.

**5.3 The Deepest Fear:** That they approve a migration on a payback case, the transition costs run over, the ongoing saving arrives later and smaller than modelled, and the company spends three years on a platform that is better in ways nobody can see and was expensive in ways everyone remembers. Not the cost. Being the person who approved a number that turned out to be wrong.

**6.0 What They've Already Tried (and Why It Disappointed)**
- **Used the migration threat as leverage at the last renewal.** It worked on price and changed nothing about the service, which is what turned a negotiating position into a genuine intention.
- **Asked for a business case that includes the full transition cost.** Received three, each of which underweighted reissue, which is why they now build the reissue line themselves.
- **Explored running to expiry to avoid the reissue cost.** Cheaper in cash and longer in duration, which means paying two platforms for years rather than months, and the arithmetic did not clearly favour it.
- **Asked the incumbent what leaving costs contractually.** Got an answer that was accurate, unhelpful and slow, and which established that the exit is a negotiation rather than a clause.

**7.0 Decision Criteria & Objections**
- **What they weigh evaluating this category:**
  - The total transition cost, with reissue, dual-running and internal effort all stated, before anything else is discussed.
  - The payback period on the ongoing saving, as a number rather than a range.
  - Term, minimums and notice on the new arrangement, since they are about to be reminded what those cost.
  - Whether unit costs improve with volume, which is the only mechanism by which the saving grows rather than erodes.
- **Objections / sources of resistance:**
  - "The reissue cost is the whole conversation. Everything else is a rounding error against it."
  - "You will not give me numbers, and I am pricing a migration."
  - "You are pre-launch, and I am being asked to fund a one-off cost to get onto you."
  - "What are your term and notice? I have just spent six months learning what those are worth."

**8.0 Trigger Events (Why Now)**
- Contract renewal or notice date on the incumbent, which is the only window where the exit cost is bounded.
- An acquisition or funding round that both triggers a platform review and funds the transition.
- A quarter with the balance sheet capacity to absorb a one-off, which is genuinely what decides the timing.
- A price increase or a material incident on the incumbent, which changes the cost of staying.
- A card range approaching mass expiry, which is the one circumstance where the reissue cost largely disappears.

**9.0 Information Diet & Trusted Voices**
- Finance peers who have funded a processor migration, for the transition numbers that no vendor and no case study provides.
- Their own invoices and their own card base data, which is the only fully trusted evidence in the room.
- Card manufacturing and fulfilment quotes, obtained directly, because that is the largest line and they will not take it from a platform vendor.
- Board members with payments experience, whose view on timing carries more weight than any analysis.
- Reachable by a short message that opens on the transition cost rather than the run rate, which is the opposite of what they normally receive.

**10.0 Success Metrics (What "Good" Looks Like)**
- From a business case that leads with the run rate, to one where the transition cost is stated first and completely.
- From a payback expressed as a range, to a payback as a date they will stand behind.
- From dual-running as an unmodelled surprise, to a bounded, funded period with an end.
- From unit costs that stay flat, to a cost per active card that falls as volume rises.

**11.0 The Message That Lands**
Open where every other vendor closes, which is the transition cost. Acknowledge that the reissue is the dominant line, that it is roughly two pounds or two euros a card all in covering plastic, branding, personalisation, production and postage, and that at their card count it is material. Presenting that number before being asked establishes more credibility with this persona than any capability claim, and it is honest, because it is an industry estimate rather than a TXN price and must be stated as such. Then the ongoing side, in TXN's own words: a fixed monthly licence fee plus volume-tiered fees that step down as monthly volume rises, so cost per active card falls as the program grows, with figures in a conversation rather than in a message. **Never offer to share or subsidise the reissue cost.** It is not an existing lever, and offering it would be a commitment TXN has not made. Say nothing about the incumbent.

**12.0 Example Titles**
Chief Financial Officer · Finance Director · VP Finance · Head of Commercial Finance · Group Financial Controller · Chief Operating Officer, finance-owning
