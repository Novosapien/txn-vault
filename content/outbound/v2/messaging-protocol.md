---
description: "The rules every outbound message follows, each with its source and status: what a message may claim, the language and channel rules, and sequence length by ICP"
status: draft, 20 Oct 2026. Not reviewed by Ian. Not loaded into the product
---

# TXN messaging protocol (v2)

> **Up:** [[market-profiles]] · [[questions-for-ian]] · the offer: [[txn-offer-v2]].
>
> **What this is.** The rules that bind every outbound message. The personas describe the buyer and give the angle that lands (§11). This file says what a message may and may not say. When a persona and this file disagree, this file wins.
>
> **Where the rules come from.** The rules that bind every persona in the 4 Sep [[buyer-personas]] (two rows changed on 20 Oct, see the end of this file); the message rules cut from the eleven v2 personas on 19 Oct (each persona's cut table lists them); the vocabulary doctrine of the 2 Sep [[offer]]; and George's decisions of 20 Oct.
>
> **Status key.** **Ian**: Ian said it, with the transcript line. **Ian (record)**: Novosapien's record of a session with no transcript; Ian has not confirmed the wording. **TXN document**: from TXN's own documents. **George**: decided by George, 20 Oct. **Novosapien**: our proposal, for Ian to confirm. **Open**: a question for Ian.
>
> **For the session with Ian.** Go through sections 1 and 2 with him. Every rule marked Novosapien or Ian (record) needs his yes.

> [!important] Rulings from the 21 October call with Ian
> ([[2026-10-21-icp-revision-outbound]])
>
> **M4 is confirmed by Ian, and sharpened.** Pricing stays out of every message. What is allowed is the shape: *"a headline of simple pricing structure"*. **Avoid "usage based fees"**, because *"people could say, well, is that APIs"*. The positioning is simplicity against opacity, never a number. **Q12 is closed.**
>
> **Three claims in §2 are resolved:**
>
> | Claim | Now |
> |---|---|
> | Card schemes | **Name none.** And never "Mastercard coming soon": *"we don't need to see Mastercard coming soon"* |
> | BIN sponsors | **"Existing BIN sponsor relationships."** No target market, and **no sponsor named**. Bring-your-own may be offered briefly |
> | AI capability not live at launch | **A capability gated behind client access may be described.** The per-feature list is unsettled, so every specific claim in §2 still waits. [[open-questions]] #121 |
>
> **A new rule, M13: sequence length is set by ICP and signal, not fixed.** Ian, on companies with a live card and no sign of moving: *"you wouldn't want to contact them on a six touch sequence, because in reality if they are unhappy, something lands in their inbox or on LinkedIn, it's opportunity... **if they do nothing with the first one or two, chances are they're just not interested. Full stop**... you don't want to go through a full sequence because you're literally just spamming people that are not going to move."* So **ICP 4 gets one or two touches**, and the full sequence is reserved for ICPs where intent is evidenced.
>
> **A new rule, M14: never lose a contact.** Ian: *"coming out of this we should never lose any single company or persona or contact, because outside of the outbound workforce there might be other stuff that we want to do with those people."* A company that is discounted, graded D or unresponsive stays on record and may enter another sequence later. One sequence is not one lifetime.
>
> **And a constraint on personas rather than messages: do not narrow by job title.** *"It's difficult to know, because you don't know who's doing what in these organisations despite what their title says... if you try to go too focused on that, you might miss somebody who's actually got the responsibility for it."*
>
> **Channel routing, as confirmed on the call.** Grade **A to LinkedIn**, *"because LinkedIn's the highest response rate. So you want the cream of the crop there"*. **B and C to email. D are not contacted at all**, because *"it's a waste of a message. It's going to harm deliverability"*.

## 1. Rules for every message

| # | Rule | Source | Status |
|---|---|---|---|
| M1 | **Never name a competitor of TXN.** Contrast only against categories (a first-wave modern processor, a legacy processor, building in-house), also when the prospect names a competitor first. | 2 Sep rulings (`R1`, no transcript line); [[offer]] vocabulary doctrine | Ian (record); [[questions-for-ian]] Q36 |
| M2 | **Never criticise the competition, named, implied or by category, and never the prospect's current processor.** State what TXN does, never what another platform cannot do. No "unlike your current processor", no "if your provider cannot". A buyer may criticise their processor; TXN does not. | Ian, 3 Sep L673-691: Brett offered to attack the incumbent or to state TXN's strengths, and Ian chose *"the latter"*; *"I just don't believe in criticizing the competition"*. It binds in all four ICPs | Ian. Whether messages may use the offer's §5 "why us" lines: Q41 |
| M3 | **Claim as available only what is live at launch.** Describe the rest as what TXN is building. Say which parts are proven and which are targets. | Ian, 10 Sep L471-475: *"for absolute sure when we launch this not everything that we're planning to do will be available"*; grand claims that are not there *"that's going to be really difficult"* | Ian. Which features are live at launch: Q10 |
| M4 | **No pricing.** No price figures, no price structure (the licence fee and volume fees), and no cost comparison with the current supplier. Figures are a conversation for a person. | Ian, 24 Aug L547-549: asked whether outbound may disclose prices, *"no"*. George, 20 Oct: the price structure is out too, because a message could carry it wrongly | **Ian, 21 Oct.** Confirmed: *"I don't think pricing in a message is necessary, as long as you go with a headline of simple pricing structure."* The structure stays out because it *"becomes quite wordy to explain"*. Avoid "usage based fees" too |
| M5 | **No cost figure that is not TXN's,** including Ian's estimate of the reissue cost per card. | George, 20 Oct | George. Q29 |
| M6 | **The ten-day figure only as a target.** "TXN targets under ten business days from contract signature to the first live transaction." Never describe how a launch happens: no test environment, no promotion to production, no steps. | [[txn-offer-v2]] §2 step 2: the mechanism is not written down. 4 Sep rules | Novosapien. Who does each launch step: Q27 |
| M7 | **Never lead with the owners.** Direct Transact and Paycorp do not appear in the first message or the follow-up sequence. A person introduces them later, when the prospect asks who is behind TXN. A sentence that mentions an owner ends on what TXN delivers. | 2 Sep rulings (`R1`); [[offer]] vocabulary doctrine and §6 | Ian (record); Q36 |
| M8 | **Never claim that TXN holds an accreditation.** If a buyer asks, the reply is: PCI is held by Direct Transact, our co-founding owner, and the platform is operated within that accredited environment. A reply only, never in a first message. | Ian, 3 Sep L417-429: *"DT hold the PCI accreditation"*; SOC 2 and ISO not known | Ian. SOC 2 and ISO 27001: Q35 |
| M9 | **Never describe how the platform was built.** No code lineage, in either direction. The claim is that the platform is TXN's. | 27 Aug session (`S2`): no upside, and it invites the question whether the code is legacy | Ian (record) |
| M10 | **Never name a peer company,** and never name the processor that a prospect or a peer uses. | George, 20 Oct: the workforce cannot confirm a peer's card, and a peer named from model memory can be wrong | George |
| M11 | **Never offer to share or pay part of a cost,** such as the reissue cost. | 27 Aug session: TXN "could consider" sharing the reissue cost; it is not an existing lever | Novosapien; Q29 |
| M12 | **Never say that TXN takes on the client's regulatory responsibility.** Compliance support is confidence, not replacement. | [[txn-offer-v2]] O8, the boundary (`AITO` 3.1.5) | TXN document |

## 2. Claims that wait for Ian

The offer states these claims, but the evidence does not support them yet. Until Ian answers, no message states them.

| Claim in the offer | Until Ian answers | Question |
|---|---|---|
| TXN settles "with Visa and Mastercard" (`txn-offer-v2.md:18`, `:188`). Ian, 9 Oct: "we don't support MC" | Name no card scheme as supported | Q2 (Mastercard: say it, or as coming soon), Q34 (Visa) |
| "Pre-integrated BIN sponsor relationships in each target market" (`txn-offer-v2.md:210`). Ian, 2 Sep L644: "getting the first one on board" | Make no claim about BIN sponsors | Q11 |
| O3, "the program runs without card experts on staff", and O8, "compliance requirements are surfaced and applied", as if they work today | Not as available today | Q10 |
| Authorising card spend against a balance that TXN holds | Not as available today | Q10 |
| Rewards and card-linked offers | Do not claim | Q23 |
| The §5 "why us" lines that say what other platforms cannot do | Do not use them | Q41 |

## 3. Language

From the vocabulary doctrine of the 2 Sep [[offer]] (line 27), which binds every message. Whether the list is complete: Q37.

- **Never use:** built on · powered by · provided by · runs on · inherit · partner, in the vendor sense, about Direct Transact · parent group · underlying infrastructure · bank-grade · "50 years combined experience" · built from the ground up · built new · solution, when platform is meant · ecosystem, when partners is meant · enterprise · revolutionary · game-changing · world-class · cutting-edge · disrupt · disruptor · transformative · seamless · best-in-class · synergies · leverage as a verb.
- **Two bans depend on the sense.** "Partner" is banned only about Direct Transact as a vendor; "BIN sponsor relationships" is fine. "Disrupt" is banned as a positioning claim; "disruption to the cardholder base" is TXN's own operational language.
- **Always use:** "Direct Transact, our co-founding owner" and "Paycorp, our co-founding owner". "program" and "programs", never "programme". British English. No em dashes.
- **Heritage.** The 25 years of processing heritage belongs to Direct Transact. Attribute it every time; never claim it for TXN.
- **Register: evolution, not disruption.** TXN does the existing job better; it does not replace the category.

## 4. Channels

| # | Rule | Source | Status |
|---|---|---|---|
| C1 | **Germany: LinkedIn only.** No cold email to German companies (UWG consent rules). | `prospecting-process.md:319` | TXN document |

## 5. Rules for one ICP

| # | ICP | Rule | Source | Status |
|---|---|---|---|---|
| I1 | ICP 2 | **Write the pains as what the new program needs,** never as what the current processor lacks. | Ian, 3 Sep L669-679 (*"it's the latter"*) | Ian |
| I2 | ICP 3 | **First the case for a card program, then the case for TXN,** also when a signal suggests the company is in the market. Speak about what card programs have done in the company's vertical, without naming a company (M10). | Ian, 2 Sep L862: *"you shouldn't assume that they've made a decision… you should talk about why they should launch a program"*; 2 Sep L580, L732 | Ian |
| I3 | ICP 4 | **Never describe the migration as painless,** and never say that the cardholder will notice no change. Reissue is the cleanest route. | 27 Aug session, line 31: Ian is sceptical of vendors who claim migration without reissue; [[txn-offer-v2]] step 12 | Ian (record) |
| I4 | ICP 4 | **The data extraction from the current processor is the client's work.** Do not imply that TXN does it. | 27 Aug session, line 30; [[txn-offer-v2]] step 12 | Ian (record) |

## 6. Rules for one persona

| # | Persona | Rule | Source | Status |
|---|---|---|---|---|
| P1 | ICP 1 founder, CEO or CFO | Do not open with the technology. | 4 Sep persona §11 | Novosapien |
| P2 | ICP 3 CPO or Head of Customer | Use no payments vocabulary that a product lead outside payments has to look up. | 4 Sep persona §11 | Novosapien |
| P3 | The CTO personas | Expect the accreditation question; answer it with the M8 reply when they ask. | 4 Sep personas §11 | Novosapien |

## 7. Open, for the session with Ian

| Question | Why it is open |
|---|---|
| **Pre-launch.** Should a message acknowledge that TXN has no live clients yet, before the buyer raises it? | The 4 Sep ICP 1 and ICP 4 CTO personas said yes. No line from Ian supports it. The usual answer to "you are pre-launch" is the owners' track record, which may not appear in a first message (M7) |
| **The 2 Sep rulings** (M1, M7, and "TXN sells nothing beyond this offer") | No transcript line exists for them (Q36) |
| **The price structure** (M4) | Q12 |
| **The banned-word list** (section 3) | Q37 |

## Changes from the 4 Sep rules

The 4 Sep [[buyer-personas]] held nine rules. All nine are here, with two changes:

| 4 Sep rule | Change, 20 Oct |
|---|---|
| "No pricing figures, ever. Ground on the shape" | The price structure is out too (M4, George) |
| "Naming a prospect's peer is not the same as naming a competitor" (ICP 3: the peer is the opening) | No peer company is named (M10, George) |
