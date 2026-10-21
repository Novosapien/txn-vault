---
description: "TXN ICP 2 v2, new program where the incumbent stays: the full ICP definition, Ian's ruling that expansion not unhappiness is the signal, and its gaps"
status: draft, 19 Oct 2026, revised after the source audit
---

# ICP 2: New program, incumbent stays (v2)

> **Up:** [[market-profiles]]. **Personas:** [[cpo-the-boxed-in-roadmap-owner|CPO]] · [[cto-the-two-stack-owner|CTO]] · [[cfo-the-second-supplier-approver|CFO or Finance Director]] (in `personas/`).
>
> **How to read this file.** The block between the two horizontal rules is the ICP definition. It follows the guideline structure exactly (`cofounder: …/concepts/guidelines/icp.md`), and it is the text that loads into the product's `definition` field. Everything after the second rule stays in the vault: the source of each part and the gaps to settle.
>
> **Principle.** Observable facts define this ICP: a live card, and a visible new product, market or segment. Signals that are hard to find (for example, that the new program will go to a different processor) add weight when the research finds them; their absence never blocks a lead. An anti-signal fires only on evidence, never on missing evidence.
>
> **Rules applied to the definition text.** No competitor named or criticised. TXN's own strengths are stated; the current processor is never attacked (Ian, 3 Sep L673-677). No claim that TXN holds an accreditation. No pricing. The ten-day launch figure appears only as a target, and nothing describes how a launch happens. No word from TXN's banned list. "program", British English, no em dashes.

---

### ICP Definition: New Program, Incumbent Stays

**1. ICP Archetype Name:** `Second-Program Builder - The Constrained Operator`

**2. Core Thesis:** A company that already runs a card program and is launching another program, product or market, while its current program stays where it is. They know the domain and have integrated a processor before, so they arrive with clear requirements and with experiences they do not want to repeat. They can walk away at no cost, because the current program keeps working if the new one never launches. Their single dominant pain is **constraint**: specific needs of the new program that have to be met.

**3. Rubric-Aligned Profile**

- **Tier 1: Specific Business Type (50% Weight)**
    - **Primary Industry:** `FinTech`, `Banking`, `Financial Services`
    - **Ideal Verticals:** `Digital banking (neobanks)`, `Banking as a service (BaaS)`, `FX payments and multi-currency accounts`, `Lending (SMB and consumer)`, `Expense management and corporate cards`.
    - **Defining Characteristics & Offerings (The "Idiot's Guide"):**
        - **Core Identity:** A company with a live card program **and** a visible new product, customer segment or market that the current card does not cover yet.
        - **Website Evidence:** A live card, meaning customers can order or use a card today: a card page with an order or sign-up flow, live cardholder terms that name an issuer, a usable card in the app store listing, or a help page about using or replacing the card. Card art, a waitlist, "coming soon" or "beta" on its own is not a live card. Then, separately, a landing page for a new market, a second product line, a regional domain, or localised pricing that the current card does not serve.
    - **State Modifiers (Observable Signals of this Archetype):**
        - **GTM Motion:** The careers page lists roles for a named new market or product line, or a second program manager or payments lead. Roles to integrate a new card processor are a strong signal that the next program goes elsewhere.
        - **Marketing Motion:** Launch messaging for a new customer segment. A licence or regulatory announcement for a market they do not serve yet.
        - **Growth Signal:** A funding announcement earmarked for expansion. A distribution or co-brand deal that implies a card the current program does not issue.
- **Tier 2: Business Model Category (30% Weight)**
    - **Primary Model:** `Sales-led` or `Sales-assisted`.
    - **Target Customer:** Whoever the new product serves, which is often not who the current program serves. A descriptor, not a qualifier.
    - **Tech Stack Signal:** A card issuer processor in place for the live program. Infrastructure across several regions. Localisation tooling.
- **Tier 3: Firmographics (20% Weight)**
    - **Employee Count (Range):** `Any`. Headcount does not rank this ICP: a company of any size is in scope.
    - **Geography (Ideal):** `EEA` and `United Kingdom`, with `Poland`, `Czech Republic`, `Romania` and `Hungary` first. The company's own location decides the order, even when the new market sits elsewhere.

**4. Disqualification Criteria (Anti-Signals)**

- **The card is not live:** the website shows card art, a waitlist, "coming soon" or "beta" for the card, or the product pages list the features and no card is among them. The company is then a first-program or card-adjacent case.
- **The whole current program is moving too:** cardholders and data migrate. The company is then a full-switch case, where the conversation is about migration risk.
- **The new program is planned on Mastercard only:** TXN does not support Mastercard today.
- **The new program is planned for markets in Asia or for Ukraine:** TXN does not support them.
- **A card program for the company's own staff only:** outside TXN's sub-sectors.
- **A BIN sponsor:** a bank or e-money institution that issues cards for other companies' programs under its own licence. TXN works with BIN sponsors directly, as a separate channel, outside outreach.
- **Petrol retail, a government body, a state-owned company, or a Tier 1 bank itself:** outside TXN's scope. A Tier 1 bank's digital subsidiary is not disqualified here.
- **In administration, insolvency or wind-down, or reported for regulator difficulty or sanctions:** the company cannot commit to a launch.

**5. Archetype-to-Pain Mapping (Sharpened for CONSTRAINT)**
Connects observable signals to the specific needs of a new program, stated as what the new program needs, never as what the current processor lacks.

| Observable Signal (from Tiers 1 & 2) | Primary Inferred Pain (The Core Problem) | Relevance to the Offer (Why We Win) |
|---|---|---|
| A live card program, plus a landing page or localised pricing for a new market | **`The new market needs a program of its own, on a date already set.`** They chose the market first, and the card setup for it is still open. Local rules, BIN allocation and routing have to be ready before customers there can use a card. | TXN sets up a program per market as configuration. BINs are allocated across the sponsor, program owner and processor roles, and each transaction is routed to the right program. |
| A live program, plus a second product line announced | **`The second product needs controls the first one never needed.`** A new product brings new spend rules, merchant limits or customer segments. The team has to design them before launch, while it keeps the first program running. | Spend and merchant controls are set by amount, frequency, merchant category, geography and transaction type, and cascade down the entity model. Everything is reachable through the API first, with events and webhooks into their own systems. |
| A second program manager or a market-specific payments lead on the careers page | **`Every new program adds people to run it.`** Each program and market brings its own servicing, reconciliation and scheme reporting. Headcount grows with each launch, and the few specialists become the bottleneck. | The core job of TXN is to let a company run a card program without employing card experts. The Console gives operators one role-aware place for servicing, reconciliation and approvals, so a routine change does not wait on a specialist. |
| A distribution or co-brand deal that implies a new card | **`A commercial commitment is running ahead of the card.`** The deal has a date, and the card it depends on does not exist yet. A missed date puts the deal at risk. | TXN targets under ten business days from contract signature to the first live transaction. After launch, a change to the card product is a setting, not a new release. |
| Infrastructure across several regions, with the card live in one | **`The company is multi-market and its card is not yet.`** The rest of the business already runs across markets. The card has to catch up before customers in the new markets can use it. | Each new market starts from configuration. PSD2 strong customer authentication and 3DS sit inside the platform, and clearing and settlement are reconciled in the Console for every program. |

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
> **Specific to this ICP: the premise was wrong.**
>
> **"Constraint" is confirmed** as the dominant pain. Ian was comfortable with it.
>
> **But a second program does not imply unhappiness with the first processor.**
>
> > *"You could be perfectly happy with a processor for doing what the program you've got today needs them to do, but then you're launching a new card program that has got a set of requirements, whether that be where they can serve regionally, the type of cards they can serve, the functionality they've got, that they wouldn't book with that processor."*
>
> **The public signal is expansion, not dissatisfaction.** *"It's incredibly difficult to find where that would be. I think the signal that you get is **if they announce that they've got investment to launch into new markets or to launch a new product**. It doesn't mean they're unhappy with a processor and it doesn't mean they won't do it with that processor, but at least it's an indication of there might be some opportunity because they're doing something new."*
>
> **And the default where nothing is published:** *"you have to assume they're not doing anything, because you wouldn't know any alternative."*
>
> **Drop the sales-led and product-led distinction.** Ian: *"I can't even remember the distinguishing between sales-led and product-led in the whole ICP piece."* It is also hard to read off a website. Remove it from Tier 2 and from the anti-signals.
>
> **A correction to this document's method, raised by George and agreed by Ian.** Several of this ICP's defining signals are not publicly observable. *"We need to investigate if these signals that are not necessarily going to be public are holding too much weight in the ICPs... they should be a signal but shouldn't be **the** signal that defines this is either this or that."* See [[open-questions]] #122.

## Sources

**Who wrote what.** Section 10 of [[icp-definition]] is **Novosapien's drafting of 3–4 Sep 2026**, shown to Ian on 3 Sep. Where this file takes from section 10, it is Novosapien's work unless a transcript line is cited.

| Part | Source |
|---|---|
| The status itself | Ian, 3 Sep L489: *"launch the next product with somebody else"*. The "somebody else" part cannot be seen on a website, so it adds weight when found and does not define the ICP |
| Archetype name, dominant pain "constraint" | Novosapien, section 10. "Constraint" appears in the transcript only where Brett reads the draft aloud (3 Sep L669, L681). Question for Ian |
| Core thesis | Ian, 2 Sep L764-768: they come in *"with a bunch of knowns and experiences they've had that they're going to want to make sure they're not going to have with you again."* Ian, 3 Sep L583: ranked second, discounted for reversibility. The earlier v2 wording ("not unhappiness", "not on reassurance") contradicted Ian and is removed |
| Verticals | Novosapien, section 10 weighting. Ian ruled that verticals are the same for every status (2 Sep L824, L830) |
| Core identity, website evidence, state modifiers | Novosapien, section 10, rewritten to what the company's own website shows |
| Primary model, target customer, tech stack signal | Novosapien, section 10. The processor is described, not named |
| Employee count `Any` | Ian, 3 Sep L909 and 2 Sep L852 |
| Geography | Ian's phases, §4.4. "The company's location decides" is Novosapien's |
| Anti-signals | Ian's anti-profile §7, the same for all statuses (3 Sep L991); staff-card-only §8.1.2; state-owned enterprises (Core Messaging v2.5 §3.2); BIN sponsors out of outreach (Ian, 2 Sep L642-645); the live-card evidence list and "the card is not live" (ours, 20 Oct, the same in all four ICPs; it replaces "the website shows no card at all", which fired on missing evidence); Mastercard, Asia and Ukraine (9 Oct email). "No sign of a second program" is removed as an anti-signal, because it would fire on missing evidence |
| How the pains are framed | Ian, 3 Sep L673-677: state TXN's strengths, never attack the incumbent ("it's the latter") |
| Pain mapping: relevance | [[offer]]: the primary job, step 1, step 2 (the ten-day target only), step 5, steps 6 and 7, step 8, step 9, step 11 (BIN allocation and routing). The claim of "pre-integrated BIN sponsor relationships in each target market" is removed: Ian said on 2 Sep that TXN is "getting the first one on board" (L644) |

## Gaps to settle

| Gap | Why it matters |
|---|---|
| **Marqeta clients.** All of them, or only the seven removed on 9 Oct? Why? His prospecting process calls a published Marqeta customer "a proven ICP fit by definition" (`prospecting-process.md:90`) | It may remove a large part of this ICP. Not in the definition until Ian answers |
| **Mastercard.** Not supported today; certification is the first priority after MVP. Remove or schedule later? | Decides the Mastercard anti-signal |
| **Markets** besides Asia and Ukraine | Decides whether more markets join the anti-signal |
| **What sign from outside shows the next program goes to a different processor?** | The status is defined by it, but no website shows it |
| **Is the buyer unhappy with the current processor?** His 2 Sep words suggest yes | Sets the dominant pain the writer leads on |
| **BIN sponsors today, and where** | Decides what relevance row 1 may claim |
| **A recently signed incumbent contract:** does it delay this ICP? (2 Sep L636: "move them down the list") | Decides when to contact |
| **How much the CTO matters** | Not part of the ICP structure. It goes to the personas |
| **Five ideal verticals, against Ian's ruling that verticals are the same for every status** (2 Sep L824). The market profiles feed this ICP with more. Discussion point with Ian, [[questions-for-ian]] Q5 | A fitting company outside the five ranks lower on Tier 1. Unchanged until Ian answers |
| **"Sales-led or Sales-assisted"** (Novosapien's). The workforce rejects a product-led company when the ICP requires sales-led. Discussion point with Ian, Q6 | A product-led neobank with a live card can be rejected. Unchanged until Ian answers |
