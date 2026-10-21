---
description: "TXN ICP 4 v2, full switch: the full ICP definition, Ian's ruling that it runs on one or two touches, incumbent tiering, and the two things he left open"
status: draft, 19 Oct 2026, revised after the source audit, on hold
---

# ICP 4: Full switch (v2)

> **Up:** [[market-profiles]]. **Personas:** [[cto-the-escape-planner|CTO]] · [[cpo-the-keeper-of-the-cardholder|CPO]] · [[cfo-the-reissue-signatory|CFO]] (in `personas/`).
>
> **Status: on hold, pending Ian.** Ian ranked full switch last (3 Sep L547-551) and compared its pursuit cost to a Tier 1 bank (3 Sep L591-599). He named two gates: reference customers and migration tooling (*"they don't expect a 15 year old approach"*). On 9 Oct he still asked for a sample message for each category, and the 6 Oct list had three full-switch companies that he did not remove. Whether this ICP gets any outreach now is a question for Ian.
>
> **How to read this file.** The block between the two horizontal rules is the ICP definition. It follows the guideline structure exactly (`cofounder: …/concepts/guidelines/icp.md`), and it is the text that loads into the product's `definition` field. Everything after the second rule stays in the vault: the source of each part, the questions for the first conversation, and the gaps to settle.
>
> **Principle.** A live card is observable; the intent to move is hard to find. So a company is assigned to this ICP only when the research finds an intent signal. Without one, it goes to the new-program ICP or the static group. An anti-signal fires only on evidence, never on missing evidence.
>
> **Exception to the ICP principle (George, 20 Oct).** Every other ICP is defined by observable facts. This one is defined by the intent to move, which a website rarely shows: it is there, but it has to be discovered in the outreach. The exception is recorded here, and the definition is revisited when Ian answers [[questions-for-ian]] Q9 and Q25.
>
> **Rules applied to the definition text.** No competitor named or criticised. TXN's own strengths are stated; the current processor is never attacked, even though this buyer is leaving it: they may say it, TXN does not. No claim that TXN holds an accreditation. No pricing. No offer to share the reissue cost. No word from TXN's banned list. "program", British English, no em dashes.

---

### ICP Definition: Full Switch

**1. ICP Archetype Name:** `Full-Switch Migrator - The Blocked Escapee`

**2. Core Thesis:** A company that runs a live card program and intends to move all of it to another processor, with its cardholders and data. They arrive with clear requirements and with experiences they do not want to repeat. The sale is not about whether to move but about whether the move is survivable for a live cardholder base: the cardholders, the reissue question and a route that keeps live customers' cards working. Their single dominant pain is **entrapment**.

**3. Rubric-Aligned Profile**

- **Tier 1: Specific Business Type (50% Weight)**
    - **Primary Industry:** `FinTech`, `Banking`, `Financial Services`
    - **Ideal Verticals:** `Digital banking (neobanks)`, `Expense management and corporate cards`, `Banking as a service (BaaS)`, `FX payments and multi-currency accounts`, `Lending (SMB and consumer)`.
    - **Defining Characteristics & Offerings (The "Idiot's Guide"):**
        - **Core Identity:** A live card program **and** a signal that the company intends to replace its processor entirely, as opposed to adding a second one.
        - **Website Evidence:** A live card, meaning customers can order or use a card today: a card page with an order or sign-up flow, live cardholder terms that name an issuer, a usable card in the app store listing, or a help page about using or replacing the card. Card art, a waitlist, "coming soon" or "beta" on its own is not a live card. The intent to move is rarely published; it shows occasionally on the careers page or the news page.
    - **State Modifiers (Observable Signals of this Archetype):**
        - **GTM Motion:** The careers page lists a payments or platform role whose remit reads as a processor migration or vendor consolidation.
        - **Marketing Motion:** The news page or a public statement from an executive refers to a change of card platform, or to migration activity.
        - **Growth Signal:** A public reference to a multi-year processor contract nearing its anniversary. A new head of product or technology.
- **Tier 2: Business Model Category (30% Weight)**
    - **Primary Model:** `Sales-led`; an established, revenue-generating business.
    - **Target Customer:** Whoever the current program already serves, which the live product shows. A descriptor, not a qualifier.
    - **Tech Stack Signal:** A card issuer processor in place for the live program. Several separate providers visible around the program (processing, authentication, controls, settlement).
- **Tier 3: Firmographics (20% Weight)**
    - **Employee Count (Range):** `Any`. Headcount does not rank this ICP: a company of any size is in scope.
    - **Geography (Ideal):** `EEA` and `United Kingdom`, with `Poland`, `Czech Republic`, `Romania` and `Hungary` first.

**4. Disqualification Criteria (Anti-Signals)**

- **The card is not live:** the website shows card art, a waitlist, "coming soon" or "beta" for the card, or the product pages list the features and no card is among them. There is nothing to move. The company is then a first-program or card-adjacent case.
- **The current processor stays for the existing book:** only a new program moves. The company is then a new-program case, and the migration conversation does not apply.
- **The program uses Mastercard only:** TXN does not support Mastercard today.
- **The program serves markets in Asia or Ukraine:** TXN does not support them.
- **A card program for the company's own staff only:** outside TXN's sub-sectors.
- **A BIN sponsor:** a bank or e-money institution that issues cards for other companies' programs under its own licence. TXN works with BIN sponsors directly, as a separate channel, outside outreach.
- **Petrol retail, including fuel card programs, a government body, a state-owned company, or a Tier 1 bank itself:** outside TXN's scope. A Tier 1 bank's digital subsidiary is not disqualified here.
- **In administration, insolvency or wind-down, or reported for regulator difficulty or sanctions:** the company cannot commit to a migration.

**5. Archetype-to-Pain Mapping (Sharpened for ENTRAPMENT)**
Connects observable signals to what a company needs before it can move a live card program, stated as the needs of the move, never as the failings of the current processor.

| Observable Signal (from Tiers 1 & 2) | Primary Inferred Pain (The Core Problem) | Relevance to the Offer (Why We Win) |
|---|---|---|
| Card payment incidents reported on the company's own status page or help centre | **`They answer to cardholders for every failed payment.`** When a payment fails, cardholders blame the company whose name is on the card. Reliability is their brand problem, whoever does the processing. | TXN is the issuer processor and does not outsource its processing. The intelligence layer runs alongside the platform, not inside the real-time transaction path, a design choice that protects stability and latency. |
| A payments or platform role on the careers page whose remit reads as migration or consolidation | **`They have decided to move and are staffing the move.`** The decision is made; the route is not. The question they cannot answer yet is whether the move is survivable for a live cardholder base. | Migration runs as a work stream inside the launch, not as a separate engagement, and the capture-and-configure work is the same as for a new program. The first conversation is about the risk of the move, and a person leads it. |
| A public reference to a processor contract near its anniversary | **`A window is opening that closes again for years.`** If they miss it, they are held for another term. Term and notice decide the timing of everything else. | Because migration sits inside the launch, the move can be planned against the renewal date from the first conversation. After the move, a change to the card product is a setting, not a new release. |
| Several separate providers visible around a live program | **`Nobody owns the whole chain when something fails.`** Processing, authentication, controls and settlement sit with different providers. Moving means untangling several relationships at once, which is why they have not moved yet. | Issuing, authorisation, spend controls, PSD2 authentication, and clearing and settlement sit in one platform, with pre-integrated KYC and card manufacturing relationships. The move reduces the number of providers rather than moving the same tangle. |

---

> [!important] Rulings from Ian, 21 October 2026
> From the ICP revision call ([[2026-10-21-icp-revision-outbound]]). These bind this ICP. The rulings that apply to every ICP are repeated in each file so that a writer loading one file alone is not misled.
>
> **Applies to every ICP:**
>
> | Ruling | Effect here |
> |---|---|
> | **Mastercard is not a disqualifier** | *"We shouldn't really care too much if it's Mastercard... by the time somebody's made a decision that they're going to move, the chances are we'll have Mastercard certification anyway."* **Remove the Mastercard anti-signal.** And no message says "Mastercard coming soon": *"we don't need to see Mastercard coming soon"* |
> | **Geography is two layers** | TXN *"can only contract with companies that are in Europe or the UK"*. Where cards may be issued *"is not something that we can determine. It's determined by a BIN sponsor."* **So: mark down on published non-European issuance, do not disqualify, and do not try to identify the licensed issuer.** *"For the level of complexity that might be involved... I think we can pass on that"* |
> | **Every vertical carries every ICP** | *"If the ICP and status are the same thing, then my argument is they are the same for every vertical."* Some verticals will simply contain no ICP 1s, and those companies fall through to 2, 3 or 4 |
> | **Lose nothing** | *"Coming out of this we should never lose any single company or persona or contact."* A discounted company stays on record and may be contacted later |
> | **Do not narrow by job title** | *"Chief product officer, head of payments, possibly the founder. It's difficult to know, because you don't know who's doing what in these organisations despite what their title says."* And: *"if you try to go too focused on that, you might miss somebody who's actually got the responsibility for it"* |
>
> **Specific to this ICP: it loads, but on a short sequence.**
>
> **The question asked was whether ICP 4 gets outreach at all. Ian answered a different and more useful question: how much.**
>
> > *"My question is whether or not the sequencing and approach can be flexed. So for example, these with a live card and no sign of moving, no sign of moving, but we don't know. There might be a chance, but **if you don't contact them, they'll never know you exist**. But you wouldn't want to contact them on a six touch sequence, because in reality if they are unhappy, something lands in their inbox or on LinkedIn, it's opportunity. It's the right timing and they're more likely to do something about it. **If they do nothing with the first one or two, chances are they're just not interested. Full stop**... you don't want to go through a full sequence because you're literally just spamming people that are not going to move."*
>
> **So: one or two touches, not six.** Sequence length becomes a variable set by ICP and signal, not a constant. See [[messaging-protocol]].
>
> **Marqeta clients are deprioritised, not removed**, and the score is layered: what the company does and its propensity to launch; then whether a card is live; then who it is live with; then whether anything published suggests that incumbent has problems. *"It's not about removing them. It's about understanding that it's highly unlikely that we'll get any traction with them unless there's another proof point."*
>
> **A weak incumbent is itself a signal, with no public trigger needed.** This is new.
>
> > *"I was talking to somebody in Bulgaria last week... they've gone with I2C, which **I immediately know is legacy and known not to be very good**. So if you did a list of people that have got an incumbent, and the incumbent matched this particular type of incumbent, even without any kind of trigger or proof point in the market, **they might be higher up the list**... we know they've probably got some gripes. Maybe the technology is not as flexible as they wanted it to be."*
>
> The workforce cannot know which processors those are. Ian holds it as working knowledge: [[open-questions]] #122, and question 30 in [[questions-for-ian]].
>
> **Where a proof point surfaces:** *"the place that it floats up most is LinkedIn."* Only a major outage reaches the press. The mechanism is the competitor-tracking idea pointed the other way, at people posting negative things about a competitor. Ian's own weighting: *"it's not the highest priority thing."*
>
> **Drop the sales-led and product-led distinction**, as in ICP 2.
>
> **Two things Ian did not settle.** The dominant pain: he said the last of the four words needed changing and never replaced it, so **"entrapment" is unendorsed**. And the two gates he set in September, reference customers and migration tooling, were never answered. [[open-questions]] #120.

## Sources

**Who wrote what.** Section 10 of [[icp-definition]] is **Novosapien's drafting of 3–4 Sep 2026**, shown to Ian on 3 Sep. On the ICP 4 messaging, the 3 Sep transcript shows Ian saying only *"Yeah, seemed okay to me"* (L683). Where this file takes from section 10, it is Novosapien's work unless a transcript line is cited.

| Part | Source |
|---|---|
| The status itself | Ian, 3 Sep L489: *"a full switch"* |
| Status and gates | Ian's ranking and the Tier 1 comparison (3 Sep); the gates as recorded in [[outbound]] and [[open-questions]] #78 |
| Archetype name, dominant pain "entrapment" | Novosapien (section 10 and the 25 Aug record, which has no transcript). Ian never uses the word in a transcript |
| Core thesis | Ian, 2 Sep L764-768 (*"a bunch of knowns and experiences"*); the rest is Novosapien, section 10 |
| Verticals | Novosapien. Ian ruled that verticals are the same for every status (2 Sep L824, L830) |
| Core identity, website evidence | Novosapien, section 10, rewritten to what the company's own website shows. "A public procurement notice" is removed |
| State modifiers | Ian's own triggers in his v0.4 §5 (`icp-definition.md:87-88`: contract expiry, executive remarks, migration activity) and his prospecting process (a new executive in product or tech). The earlier "the card goes quiet" signal was ours and is removed |
| Tier 2 | Novosapien, section 10. The processor is described, not named |
| Employee count `Any` | Ian, 3 Sep L909 and 2 Sep L852 |
| Anti-signals | Ian's anti-profile §7, the same for all statuses (3 Sep L991); staff-card-only §8.1.2; state-owned enterprises (Core Messaging v2.5 §3.2); Mastercard, Asia and Ukraine (9 Oct email); BIN sponsors out of outreach (Ian, 2 Sep L642-645); the live-card evidence list and "the card is not live" (ours, 20 Oct, the same in all four ICPs; it replaces "the website shows no live card", which fired on missing evidence). A recent multi-year contract is **not** an anti-signal: Ian ruled it moves a company down the list (2 Sep L636) |
| Pain mapping | Novosapien, section 10, rewritten to the needs of the move |
| Relevance | [[offer]]: step 10 (intelligence layer outside the transaction path), step 11 (TXN does not outsource its processing), step 12 (migration inside the launch), steps 3 to 7, step 1 (a change is a setting), the pre-integrated relationships. "BIN sponsor" is removed from the pre-integrated list: Ian said on 2 Sep that TXN is "getting the first one on board" (L644) |

## Questions for the first conversation

From the 27 Aug offer session record (no transcript) and the offer's step 12. None of it is observable from outside, so it is not in the definition. A person asks these, not an agent.

- Who owns the cardholder data today, and what does the current contract say about extracting it?
- Reissue, or run to expiry? Reissue is cleanest. Running to expiry strands recently renewed cards outside the window for another three to five years.
- What does a reissue cost at their card count? Ian's industry estimate is about £2 or €2 per card, all in. It is his estimate, not a TXN price.
- Why are they moving? Service-level dissatisfaction makes them resist a reissue; a move to launch something new usually brings new branding anyway.
- TXN does not offer to share the reissue cost. It is not an existing lever and must not be offered.

## Gaps to settle

| Gap | Why it matters |
|---|---|
| **Outreach now?** No outreach, light touch, or normal outreach at the lowest priority | Decides whether this ICP loads at all, and whether we owe Ian a full-switch sample message |
| **What clears each gate?** How many reference customers; which migration tooling, owned by whom, by when | The hold has no test today |
| **Which public signals of intent to move does Ian accept?** | Without one, this ICP cannot be told apart from a static live program |
| **Marqeta clients:** all of them, or only the seven? Why? | If all, it removes much of this ICP |
| **Mastercard:** not supported today; first priority after MVP. Remove or schedule later? | This ICP opens after MVP, when Mastercard may be live |
| **Markets** besides Asia and Ukraine | Decides whether more markets join the anti-signal |
| **Banks that are not Tier 1** (MagNet Bank and Attica Bank were on the 6 Oct list) | Decides whether retail banks belong here |
| **"Entrapment" as the dominant pain** | Our label |
| **The lead buyer** (the CTO lead is our proposal) | Not part of the ICP structure. It goes to the personas |
| **Five ideal verticals, against Ian's ruling that verticals are the same for every status** (2 Sep L824). The market profiles feed this ICP with more. Discussion point with Ian, [[questions-for-ian]] Q5 | A fitting company outside the five ranks lower on Tier 1. Unchanged until Ian answers |
| **"Sales-led"** (Novosapien's). The workforce rejects a product-led company when the ICP requires sales-led. Discussion point with Ian, Q6 | Most full-switch targets (neobanks, FX apps, consumer lenders) are product-led. Unchanged until Ian answers |
