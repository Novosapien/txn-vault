---
description: "TXN ICP 4 v2, full switch (a live card, no visible new program, a short sequence): the loadable ICP definition, with its sources, questions and gaps"
status: draft, 19 Oct 2026, revised after the source audit; revised 21 Oct 2026, active on a short sequence
---

# ICP 4: Full switch (v2)

> **Up:** [[market-profiles]]. **Personas:** [[cto-the-escape-planner|CTO]] · [[cpo-the-keeper-of-the-cardholder|CPO]] · [[cfo-the-reissue-signatory|CFO]] (in `personas/`).
>
> **Status: active on a short sequence (21 Oct).** Ian ranked full switch last (3 Sep L547-551), compared its pursuit cost to a Tier 1 bank (3 Sep L591-599), and named two gates: reference customers and migration tooling (*"they don't expect a 15 year old approach"*). On 21 Oct he ruled that companies with a live card and no sign of moving are contacted, but not on a full sequence: *"if you don't contact them, they'll never know necessarily you exist"* (L753); *"If they do nothing with the first one or two, I don't know what the exact what the right number is. Chances are they're just not interested"* (L757). A sequence length by ICP is not built yet. The gates were put to him again (Q9) and are still unanswered: [[questions-for-ian]] Q45.
>
> **How to read this file.** The block between the two horizontal rules is the ICP definition. It follows the guideline structure exactly (`cofounder: …/concepts/guidelines/icp.md`), and it is the text that loads into the product's `definition` field. Everything after the second rule stays in the vault: the source of each part, the questions for the first conversation, and the gaps to settle.
>
> **Principle (George's decision D2, 21 Oct).** A live card is observable; the intent to move is hard to find. So this ICP takes every company with a live card and no visible new program. Intent to move, a processor that TXN rates as legacy, or published problems with the current processor raise the grade; their absence never blocks a lead. An anti-signal fires only on evidence, never on missing evidence. The 20 Oct exception to the ICP principle is removed: this ICP now rests on observable facts.
>
> **Dominant pain.** "The risk of the move" is Novosapien's interim word (21 Oct). Ian said "entrapment" needs changing and gave no replacement: [[questions-for-ian]] Q44.
>
> **Rules applied to the definition text.** No competitor named or criticised. TXN's own strengths are stated; the current processor is never attacked, even when this buyer is unhappy with it: they may say it, TXN does not. No claim that TXN holds an accreditation. No pricing. No offer to share the reissue cost. No word from TXN's banned list. "program", British English, no em dashes.

---

### ICP Definition: Full Switch

**1. ICP Archetype Name:** `Full-Switch Candidate - The Established Program Owner`

**2. Core Thesis:** A company that runs a live card program and shows no new program, so the existing program is the subject, and the sale is a full switch of that program, its cardholders and data, to a new processor. Most such companies are not looking to move, because moving processor is a large step; a few are, often because they need something the current setup does not give them. Those that look arrive with clear requirements and with experiences they do not want to repeat. The question they weigh is whether a move is survivable for a live cardholder base: the cardholders, the reissue question and a route that keeps live customers' cards working. Their single dominant pain is **the risk of the move**.

**3. Rubric-Aligned Profile**

- **Tier 1: Specific Business Type (50% Weight)**
    - **Primary Industry:** `FinTech`, `Financial Services`, `Banking`, `Retail`, `E-commerce`
    - **Ideal Verticals:** `Digital banking for consumers (neobanks)`, `Digital banking for businesses (SME accounts)`, `Crypto platforms with fiat rails`, `Expense management and corporate cards`, `Travel and expense`, `Accounts payable`, `SMB lending`, `Consumer lending`, `FX payments and multi-currency accounts`, `Payments`, `Banking as a service (BaaS)`, `Investment management and trading apps`, `Disbursement and payouts`, `Retail`, `E-commerce and marketplaces`. Every vertical carries this ICP. The Core Identity decides the fit, not the vertical.
    - **Defining Characteristics & Offerings (The "Idiot's Guide"):**
        - **Core Identity:** A live card program, and no visible new product, customer segment or market that would make it a new-program case. Evidence that the whole current program is moving to a new processor also places a company here, even when a new program is visible. A signal that the company intends to replace its processor raises the grade; it is not required.
        - **Website Evidence:** A live card, meaning customers can order or use a card today: a card page with an order or sign-up flow, live cardholder terms that name an issuer, a usable card in the app store listing, or a help page about using or replacing the card. Card art, a waitlist, "coming soon" or "beta" on its own is not a live card. The intent to move is rarely published. When the careers page or the news page shows it, it raises the grade.
    - **State Modifiers (Observable Signals of this Archetype):**
        - **GTM Motion:** The careers page lists a payments or platform role whose remit reads as a processor migration or vendor consolidation.
        - **Marketing Motion:** The news page or a public statement from an executive refers to a change of card platform, or to migration activity.
        - **Growth Signal:** A public reference to a multi-year processor contract nearing its anniversary. A new head of product or technology.
- **Tier 2: Business Model Category (30% Weight)**
    - **Primary Model:** `Any`. How the company sells to its own customers does not rank this ICP.
    - **Target Customer:** Whoever the current program already serves, which the live product shows. A descriptor, not a qualifier.
    - **Tech Stack Signal:** A card issuer processor in place for the live program. Several separate providers visible around the program (processing, authentication, controls, settlement). Where the research can identify the processor: a processor that TXN rates as legacy raises the fit, even with no other trigger, and published problems with it raise the fit further. A processor that TXN rates as top tier, with no published problem, lowers the fit. These add weight only; their absence never blocks a lead. They are for ranking only: a message never names or criticises the current processor.
- **Tier 3: Firmographics (20% Weight)**
    - **Employee Count (Range):** `Any`. Headcount does not rank this ICP: a company of any size is in scope.
    - **Geography (Ideal):** `EEA` and `United Kingdom`, with `Poland`, `Czech Republic`, `Romania` and `Hungary` first. TXN contracts only with companies in Europe (Switzerland included) or the UK. Where the cards may be issued is the BIN sponsor's decision, not TXN's. A company that publishes card issuance for markets outside Europe and the UK (for example Asia, the Middle East or Africa), or for Ukraine, ranks lower here. It is not disqualified. Do not try to identify the licensed issuer.

**4. Disqualification Criteria (Anti-Signals)**

- **The card is not live:** the website shows card art, a waitlist, "coming soon" or "beta" for the card, or the product pages list the features and no card is among them. There is nothing to move. The company is then a first-program or card-adjacent case.
- **A visible new product, customer segment or market, with no sign that the whole current program is moving:** a new program is in view. The company is then a new-program case, and the migration conversation does not apply.
- **A card program for the company's own staff only:** outside TXN's sub-sectors.
- **A BIN sponsor:** a bank or e-money institution that issues cards for other companies' programs under its own licence. TXN works with BIN sponsors directly, as a separate channel, outside outreach.
- **No company in Europe or the UK to contract with:** the website shows the company and its group registered only outside Europe and the UK. TXN can contract only with companies in Europe or the UK. A European or UK subsidiary of a group based elsewhere is not disqualified, and a website that does not say where the company is registered is not evidence.
- **Petrol retail, including fuel card programs, a government body, a state-owned company, or a Tier 1 bank itself:** outside TXN's scope. A Tier 1 bank's digital subsidiary is not disqualified here.
- **A traditional bank (a retail, savings, cooperative or regional bank), not a digital bank or neobank:** a low priority for later. TXN needs reference clients and credibility before it can win banks. The company stays on record and is revisited later.
- **In administration, insolvency or wind-down, or reported for regulator difficulty or sanctions:** the company cannot commit to a migration.

**5. Archetype-to-Pain Mapping (Sharpened for THE RISK OF THE MOVE)**
Connects observable signals to what a company needs before it can move a live card program, stated as the needs of the move, never as the failings of the current processor.

| Observable Signal (from Tiers 1 & 2) | Primary Inferred Pain (The Core Problem) | Relevance to the Offer (Why We Win) |
|---|---|---|
| A live card program, with no visible new program and no sign of a move | **`Staying is easier than moving.`** The program works well enough, and a move would touch every live cardholder. They are unlikely to look unless the current setup stops them doing something they need. | Migration runs as a work stream inside the launch, not as a separate engagement, and the capture-and-configure work is the same as for a new program. After the move, a change to the card product is a setting, not a new release. |
| Card payment incidents reported on the company's own status page or help centre | **`They answer to cardholders for every failed payment.`** When a payment fails, cardholders blame the company whose name is on the card. Reliability is their brand problem, whoever does the processing. | TXN is the issuer processor and does not outsource its processing. The intelligence layer runs alongside the platform, not inside the real-time transaction path, a design choice that protects stability and latency. |
| A payments or platform role on the careers page whose remit reads as migration or consolidation | **`They have decided to move and are staffing the move.`** The decision is made; the route is not. The question they cannot answer yet is whether the move is survivable for a live cardholder base. | Migration runs as a work stream inside the launch, not as a separate engagement, and the capture-and-configure work is the same as for a new program. The first conversation is about the risk of the move, and a person leads it. |
| A public reference to a processor contract near its anniversary | **`A window is opening that closes again for years.`** If they miss it, they are held for another term. Term and notice decide the timing of everything else. | Because migration sits inside the launch, the move can be planned against the renewal date from the first conversation. After the move, a change to the card product is a setting, not a new release. |
| Several separate providers visible around a live program | **`Nobody owns the whole chain when something fails.`** Processing, authentication, controls and settlement sit with different providers. Moving means untangling several relationships at once, which is why they have not moved yet. | Issuing, authorisation, spend controls, PSD2 authentication, and clearing and settlement sit in one platform, with pre-integrated KYC and card manufacturing relationships. The move reduces the number of providers rather than moving the same tangle. |

---

## Sources

**Who wrote what.** Section 10 of [[icp-definition]] is **Novosapien's drafting of 3–4 Sep 2026**, shown to Ian on 3 Sep. On the ICP 4 messaging, the 3 Sep transcript shows Ian saying only *"Yeah, seemed okay to me"* (L683). Where this file takes from section 10, it is Novosapien's work unless a transcript line is cited. "21 Oct" lines are from the raw transcript in [[2026-10-21-icp-revision-outbound]].

| Part | Source |
|---|---|
| The status itself | Ian, 3 Sep L489: *"a full switch"*. Widened on 21 Oct by George's decision D2: every company with a live card and no visible new program. Ian ruled that companies *"with a live card and no sign of moving"* are contacted on a short sequence (L753-757) |
| Status and gates | Ian's ranking and the Tier 1 comparison (3 Sep); the gates as recorded in [[outbound]] and [[open-questions]] #78. No longer on hold from 21 Oct (L753-757). The gates were put to Ian on 21 Oct (Q9) and not answered: [[questions-for-ian]] Q45 |
| Archetype name | Novosapien. Renamed on 21 Oct from `Full-Switch Migrator - The Blocked Escapee`, which carried "entrapment" and assumed a decision to move |
| Dominant pain | Novosapien's interim word (21 Oct), because Ian said the last of the four words, "entrapment", needs changing (L703) and gave no replacement. It rests on his *"it's not a small thing to to move processor"* (L601) and *"people really don't want to move... processes"* (L591-597). [[questions-for-ian]] Q44 |
| Core thesis | Ian, 2 Sep L764-768 (*"a bunch of knowns and experiences"*). Ian, 21 Oct: moving processor is a large step (L601); a company is in market when *"there's something that they've identified that they need"* that its processor *"doesn't give them"* (L613). The rest is Novosapien |
| Primary industry and verticals | Ian, 21 Oct L681-691: every vertical carries every ICP. Earlier: 2 Sep L824, L830. The list is the union of the four market profiles, without traditional banks; `Travel and expense` and `Accounts payable` are still our inference |
| Core identity, website evidence | Novosapien, section 10, rewritten to what the company's own website shows. "A public procurement notice" is removed. On 21 Oct the intent to move left the Core Identity and became weight (D2), after George's finding that a signal a website cannot show *"should be a signal but shouldn't be the signal that defines"* (L725), which Ian agreed with (L727) |
| State modifiers | Ian's own triggers in his v0.4 §5 (`icp-definition.md:87-88`: contract expiry, executive remarks, migration activity) and his prospecting process (a new executive in product or tech). The earlier "the card goes quiet" signal was ours and is removed |
| Tier 2 | Novosapien, section 10. The processor is described, not named. Primary model `Any`: George dropped sales-led on 21 Oct (L701); Ian could not remember the distinction (L699) |
| Incumbent weight (tech stack signal) | Ian's score order, 21 Oct L563-573, and the weak-incumbent signal (L597), as in [[icp-2-new-program-incumbent-stays|ICP 2]]. A top-tier incumbent with no published problem lowers the fit, with no cap: George's decision D5, from Ian's L567 and L591. The ratings stay out of the definition: [[questions-for-ian]] Q47 |
| Employee count `Any` | Ian, 3 Sep L909 and 2 Sep L852 |
| Geography | Ian's phases, §4.4. The two layers: Ian, 21 Oct L637 (contracting in Europe or the UK only), L641-657 (issuance is the BIN sponsor's decision; mark down published issuance elsewhere; do not find the licensed issuer). Naming Ukraine in the mark-down is ours, from his 9 Oct email |
| Anti-signals | Ian's anti-profile §7, the same for all statuses (3 Sep L991); staff-card-only §8.1.2; state-owned enterprises (Core Messaging v2.5 §3.2); BIN sponsors out of outreach (Ian, 2 Sep L642-645); the live-card evidence list and "the card is not live" (ours, 20 Oct, the same in all four ICPs; it replaces "the website shows no live card", which fired on missing evidence). A recent multi-year contract is **not** an anti-signal: Ian ruled it moves a company down the list (2 Sep L636) |
| Anti-signals: changes of 21 Oct | "The current processor stays for the existing book" is now "a visible new program, with no sign that the whole program is moving", so that it fires on evidence (D2). Mastercard removed (L609, L613). Asia and Ukraine: now the Tier 3 mark-down (L653). No company in Europe or the UK: George's decision D4, from Ian's L637; it fires only on evidence. Traditional bank: George's decision D1, from Ian's *"They are definitely low priority... for later"* (L669); MagNet Bank and Attica Bank on the 6 Oct list now take a D |
| Pain mapping | Novosapien, section 10, rewritten to the needs of the move. Row 1 (a live card and nothing else) is ours, 21 Oct, for the widened ICP |
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
| **Sequence length.** Ian: *"the first one or two"*, with *"I don't know what the exact what the right number is"* (21 Oct L757). A sequence length by ICP is not built yet | Novosapien's to build. Until it is, this ICP has no short sequence to run on |
| **What clears each gate?** How many reference customers; which migration tooling, owned by whom, by when. Not answered on 21 Oct: [[questions-for-ian]] Q45 | The ICP now runs without them. Decides what a full-switch conversation can promise |
| **Which public signals of intent to move does Ian accept?** [[questions-for-ian]] Q25 | Intent now adds weight only. The answer sets how much |
| **"The risk of the move" as the dominant pain.** Novosapien's interim word. [[questions-for-ian]] Q44 | The writer leads every message on it |
| **The processor ratings:** which processors TXN rates as legacy and which as top tier. Ian gave one legacy example on 21 Oct (L597). [[questions-for-ian]] Q47 | The incumbent weight works only when TXN supplies the ratings and the research can find who the company is live with. Not checked: whether the workforce can take such a list today |
| **Ian's score order, layer 2:** a company with no live card *"should score higher"* (21 Oct L573), and a live program is *"not... the highest level of ICP"* (L601) | A grade is set within one ICP, so this definition cannot rank ICP 4 below the others. The short sequence carries part of it. Open for George |
| **The lead buyer** (the CTO lead is our proposal) | Not part of the ICP structure. It goes to the personas |
