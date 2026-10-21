---
description: "TXN ICP 1 v2, first program where the card is essential: the full ICP definition, Ian's rewrite of its dominant pain, and its sources and gaps"
status: draft, 19 Oct 2026, revised after the source audit
---

# ICP 1: First program, card is essential (v2)

> **Up:** [[market-profiles]]. **Personas:** [[cpo-the-promised-launcher|CPO]] · [[cto-the-reluctant-first-mover|CTO]] · [[founder-ceo-cfo-the-funder-of-an-unpriced-line|Founder, CEO or CFO]] (in `personas/`).
>
> **How to read this file.** The block between the two horizontal rules is the ICP definition. It follows the guideline structure exactly (`cofounder: …/concepts/guidelines/icp.md`), and it is the text that loads into the product's `definition` field. Everything after the second rule stays in the vault: the source of each part and the gaps to settle.
>
> **Principle.** Observable facts define this ICP. Signals that are hard to find add weight when the research finds them; their absence never blocks a lead. An anti-signal fires only on evidence, never on missing evidence.
>
> **Rules applied to the definition text.** No competitor named or criticised. No claim that TXN holds an accreditation. No pricing. The ten-day launch figure appears only as a target, and nothing describes how a launch happens. No word from TXN's banned list. "program", British English, no em dashes.

---

### ICP Definition: First Program, Card Is Essential

**1. ICP Archetype Name:** `First-Program Card-Essential - The Committed Newcomer`

**2. Core Thesis:** A fintech building a product that does not work without a card, with no card that customers can use yet. The decision to have a card program was made when they chose what to build, so the open question is who they launch with. They have no current processor to compare against and no card spend to model, and often nobody in the building has run a card program before, so they may not be able to test a vendor's answers. They will launch; the risk they carry is choosing without a reference point. Their single dominant pain is **exposure**.

**3. Rubric-Aligned Profile**

- **Tier 1: Specific Business Type (50% Weight)**
    - **Primary Industry:** `FinTech`, `Financial Services`
    - **Ideal Verticals:** `Digital banking for consumers (neobanks)`, `Digital banking for businesses (SME accounts)`, `Expense management and corporate cards`, `Crypto platforms with fiat rails`.
    - **Defining Characteristics & Offerings (The "Idiot's Guide"):**
        - **Core Identity:** A company whose product needs a card to work (an account, a spend platform, or crypto converted into money to spend), and that has no card customers can order or use today. The test: if the product went without a card, would it look incomplete?
        - **Website Evidence:** A card, wallet or spend feature described in the product pages, with no card that customers can order yet. "Waitlist", "coming soon" or "beta" language attached to the card. A pricing page that assumes a card. App store screenshots of a card that cannot be ordered yet.
    - **State Modifiers (Observable Signals of this Archetype):**
        - **GTM Motion:** The careers page lists card, payments, issuing or scheme roles while no card is live.
        - **Marketing Motion:** Launch content for the card on the website: waitlist campaigns, "be the first to get your card", founder posts about why they are building it.
        - **Growth Signal:** The website or its news page mentions an e-money or payment institution licence in progress, a funding round that names a card or payments product, or an incubator or accelerator cohort.
- **Tier 2: Business Model Category (30% Weight)**
    - **Primary Model:** `Product-led` or `Sales-assisted`, selling a financial product directly to its own customers.
    - **Target Customer:** `Consumers`, `SMBs` or `Corporates`, by vertical. A descriptor, not a qualifier.
    - **Tech Stack Signal:** The website's integrations or careers pages name a core banking or ledger platform (`Mambu`, `Thought Machine`, `10x`, `Tuum`) and no card issuer processor, or name a KYC vendor (`Onfido`, `Sumsub`, `Veriff`).
- **Tier 3: Firmographics (20% Weight)**
    - **Employee Count (Range):** `Any`. Headcount does not rank this ICP: a company of any size is in scope, including companies with fewer than 10 people.
    - **Geography (Ideal):** `EEA` and `United Kingdom`, with `Poland`, `Czech Republic`, `Romania` and `Hungary` first.

**4. Disqualification Criteria (Anti-Signals)**

- **Customers can already order or use the card (a live card):** a card page with an order or sign-up flow, live cardholder terms that name an issuer, a usable card in the app store listing, or a help page about using or replacing the card. Card art, a waitlist, "coming soon" or "beta" on its own is not a live card. The company is then a new-program, full-switch or static case.
- **The product is not an account, a spend platform or crypto converted into money to spend:** for example a loan, an investment or trading app, a payout service or a shop. A card would not look missing from it. The company is then an industry-inference case.
- **Crypto only, with no fiat rails:** there is no money to spend, so there is no card use case.
- **A card program for the company's own staff only:** outside TXN's sub-sectors.
- **A BIN sponsor:** a bank or e-money institution that issues cards for other companies' programs under its own licence. TXN works with BIN sponsors directly, as a separate channel, outside outreach.
- **The card is planned on Mastercard only:** TXN does not support Mastercard today.
- **The card is planned for markets in Asia or for Ukraine:** TXN does not support them.
- **Petrol retail, a government body, a state-owned company, or a Tier 1 bank itself:** outside TXN's scope. A Tier 1 bank's digital subsidiary is not disqualified here.
- **In administration, insolvency or wind-down, or reported for regulator difficulty or sanctions:** the company cannot commit to a launch.

**5. Archetype-to-Pain Mapping (Sharpened for EXPOSURE)**
Connects observable signals to the exposure of a company that launches its first card program without a processor it has used before.

| Observable Signal (from Tiers 1 & 2) | Primary Inferred Pain (The Core Problem) | Relevance to the Offer (Why We Win) |
|---|---|---|
| The website names a core banking or ledger platform, and no card processor | **`They have built the account and cannot yet build the card.`** The product is visibly incomplete, and the missing piece is one that few people in the building have done before. Every week without the card is a week the product is half-launched. | TXN sets up the card program as configuration rather than bespoke code. The specialist knowledge of running a card program sits in the platform, so the decision to launch does not need a card expert on the payroll. |
| The card is on a waitlist or "coming soon", and customers cannot order it | **`They have announced a date they cannot yet defend.`** The launch is public and the processor is not chosen. Each week of vendor selection eats into a date that customers can already see. | TXN targets under ten business days from contract signature to the first live transaction. After launch, a change to the card product is a setting, not a new release. |
| Card, payments or issuing roles on the careers page, with no card live | **`They are buying the expertise they lack, one person at a time.`** The first specialist hire becomes a single point of dependency before anything is built. If that person leaves, the knowledge leaves with them. | The core job of TXN is to let a company run a card program without employing card experts. Guided setup, an assistant in the Console and documentation generated from the API carry knowledge that would otherwise sit in one person. |
| An e-money or payment institution licence in progress, and no processor named | **`The licence will arrive before the platform does.`** A regulatory clock is running against a decision nobody has made. When the licence lands, the business case expects cards soon after. | Scheme and regulatory requirements arrive as delivered outcomes. PSD2 strong customer authentication and 3DS sit inside the platform, and clearing and settlement are reconciled in the Console. |
| An incubator or accelerator cohort, with the card named in the proposition | **`Nobody has told them what a card program costs in time, money or risk.`** They have not chosen a vendor, and they do not know the domain yet. They will learn it from whichever vendor reaches them first. | Their engineers can integrate through the API and a sandbox that behaves like production, with no sales conversation in the way. Program changes later are settings in the Console, not a new project. |

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
> **Specific to this ICP: the dominant pain is wrong, and Ian rewrote it.**
>
> This document leads on **exposure**. Ian replaced it. The worry is **the fear of getting an irreversible decision wrong**, by a team with no experience to judge the answer by:
>
> > *"If you're launching a first card program and a card is essential to your product, for me that is the one where you need to be working with somebody who takes some of the complexity out of it. I've seen it firsthand at Marqeta where **people just can't make a decision because they don't want to get the decision wrong because it's so important**, and they've got no background or experience in doing this necessarily, and because it's core to their business, get it wrong and their concern is things go awry. So they can spend an overly extended period of time trying to make a selection. So I don't know if that's risk of failure, or fear to make a decision, or fear of the unknown, whatever it is. **I realise it's not one word, but ultimately that's kind of their biggest worry.**"*
>
> **The condition underneath it:** *"often they don't know what they don't know. So they come to this green and not really understand it."*
>
> **Note the failure mode is the opposite of what exposure implies.** Exposure suggests a company moving fast and carrying risk. Ian describes a company that **stalls**: an extended selection process driven by fear. A message that leads on risk may reinforce the stall. One that removes the need to be a card expert addresses it, which is his own standard: *"if a client feels that they need to have card expertise to be able to launch a card program on TXN, then we failed."*
>
> **Still to do:** the §5 pain mapping and the core thesis both say "exposure" and need rewriting against this. Section 5's underlying signal-to-pain pairs survive; the heading does not.

## Sources

**Who wrote what.** Section 10 of [[icp-definition]] (the four ICPs) is **Novosapien's drafting of 3–4 Sep 2026**, built from Ian's rulings and shown to him on 3 Sep. The 3 Sep transcript shows Ian reacting to drafts, not dictating them. Where this file takes from section 10, it is Novosapien's work unless a transcript line is cited.

| Part | Source |
|---|---|
| Archetype name, dominant pain "exposure" | Novosapien, section 10. Ian never uses the word "exposure" in a transcript. Question for Ian |
| Core thesis | Novosapien, section 10, softened after the audit: on 24 Aug Ian said card-core companies "probably know more" than card-adjacent ones (24 Aug L669-673), and on 2 Sep he raised the case of a company that already has someone who launched a card program (2 Sep L628) |
| Verticals | Ian, 3 Sep L901: *"banking, digital banking, expense management, and crypto are the ones that if you went without a card, your product would look odd."* The split of digital banking into consumer and business is ours. Whether "banking" means a fourth group is a question for Ian |
| Core identity and its test | Ian's test, 3 Sep L901. "Customers can order or use" is ours, after the audit found that card art on a waitlist page would block a real ICP 1 |
| Website evidence, state modifiers | Novosapien, section 10, rewritten to what the company's own website shows (the workforce reads only that site) |
| Tech stack signal | Novosapien, section 10, rewritten to what the website names |
| Employee count `Any` | Ian, 3 Sep L909 (size "doesn't warrant a significant score") and 2 Sep L852 (size rules no one out) |
| Geography | Ian's phases, [[icp-definition]] §4.4 (his v0.4 document) |
| Anti-signals | Ian's anti-profile, §7, and his 3 Sep ruling that it is the same for all statuses (3 Sep L991). Staff-card-only: his §8.1.2. State-owned enterprises: TXN's Core Messaging v2.5 §3.2. Mastercard, Asia and Ukraine: his 9 Oct email. "The product is not an account, a spend platform or crypto converted into money to spend": ours (20 Oct), from Ian's test (3 Sep L901), so a card-adjacent company is not ranked here; it replaces "the product works fully without a card", which every company without a card met. The live-card evidence list: ours (20 Oct), the same in all four ICPs. BIN sponsors out of outreach: Ian, 2 Sep L642-645 |
| Pain mapping: signals and pains | Novosapien, section 10, with the expansions lengthened and the signals rewritten to what the website shows |
| Pain mapping: relevance | [[offer]]: the primary job, step 1 (configuration; a change is a setting), step 2 (the ten-day target, stated only as a target), steps 6 and 7, steps 9 and 10 |

## Gaps to settle

| Gap | Why it matters |
|---|---|
| **Mastercard.** Not supported today (9 Oct); certification is the first priority after MVP (24 Aug L573-577). Remove a Mastercard-only card, or schedule it later? When is certification expected? | Decides whether the anti-signal stays |
| **Markets** besides Asia and Ukraine. His v0.4 calls MENA and Africa later-phase, not disqualified (`icp-definition.md:224`) | Decides whether more markets join the anti-signal |
| **"Banking" as a fourth card-essential group** (3 Sep L901) | A bank with no card would be ICP 1, not ICP 3 |
| **"Exposure" as the dominant pain** | Our label. The writer leads every message on it |
| **The economic buyer** (founder or CFO) | Not part of the ICP structure. It goes to the personas |
