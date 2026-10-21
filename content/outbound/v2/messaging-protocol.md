---
description: "TXN messaging protocol v2: the rules that every outbound message follows, for every ICP and persona. What a message may and may not say, the claims that wait for Ian, the language rules, the channel rules, and the rules for one ICP or one persona; each rule with its source and status. Updated for Ian's answers on the 21 October call"
status: draft, 20 Oct 2026; 21 Oct, M3, M4, §2 and I5 changed for Ian's call. Not reviewed by Ian as a whole. Not loaded into the product
---

# TXN messaging protocol (v2)

> **Up:** [[market-profiles]] · [[questions-for-ian]] · the offer: [[txn-offer-v2]].
>
> **What this is.** The rules that bind every outbound message. The personas describe the buyer and give the angle that lands (§11). This file says what a message may and may not say. When a persona and this file disagree, this file wins.
>
> **Where the rules come from.** The rules that bind every persona in the 4 Sep [[buyer-personas]] (two rows changed on 20 Oct, see the end of this file); the message rules cut from the eleven v2 personas on 19 Oct (each persona's cut table lists them); the vocabulary doctrine of the 2 Sep [[offer]]; George's decisions of 20 Oct; and Ian's answers on the 21 Oct call ([[2026-10-21-icp-revision-outbound]]; "21 Oct L617" is a line of its transcript).
>
> **Status key.** **Ian**: Ian said it, with the transcript line. **Ian (record)**: Novosapien's record of a session with no transcript; Ian has not confirmed the wording. **TXN document**: from TXN's own documents. **George**: decided by George, 20 or 21 Oct. **Novosapien**: our proposal, for Ian to confirm. **Open**: a question for Ian.
>
> **The 21 Oct call** did not walk through this file (George, L457: *"the messaging won't be today"*). It settled M4, changed M3 for the AI capabilities, changed three claims in §2, and gave the principle of I5. Every rule marked Novosapien or Ian (record) still needs his yes. Question numbers are those of [[questions-for-ian]].

## 1. Rules for every message

| # | Rule | Source | Status |
|---|---|---|---|
| M1 | **Never name a competitor of TXN.** Contrast only against categories (a first-wave modern processor, a legacy processor, building in-house), also when the prospect names a competitor first. | 2 Sep rulings (`R1`, no transcript line); [[offer]] vocabulary doctrine | Ian (record); [[questions-for-ian]] Q36 |
| M2 | **Never criticise the competition, named, implied or by category, and never the prospect's current processor.** State what TXN does, never what another platform cannot do. No "unlike your current processor", no "if your provider cannot". A buyer may criticise their processor; TXN does not. | Ian, 3 Sep L673-691: Brett offered to attack the incumbent or to state TXN's strengths, and Ian chose *"the latter"*; *"I just don't believe in criticizing the competition"*. It binds in all four ICPs | Ian. Whether messages may use the offer's §5 "why us" lines: Q41 |
| M3 | **Claim as available only what is live at launch, with one exception for the AI capabilities.** A prospect cannot reach TXN's AI capabilities before becoming a client. So an AI capability that is not live at launch may be described, if it will be live by the time the prospect becomes a client. In Ian's view, silence about it is wrong. Until Q46 says which AI capabilities pass this test, describe them as what TXN is building for its clients, never as live today, and give no date, percentage or target. Describe everything else that is not live in the same way, except Mastercard (§2). Say which parts are proven and which are targets. | Ian, 10 Sep L471-475: *"for absolute sure when we launch this not everything that we're planning to do will be available"*; grand claims that are not there *"that's going to be really difficult"*. Ian, 21 Oct L617: the website *"already describes some of the things that won't be there on the 16th, but those are not there on the 16th because you can't access those AI capabilities until you're a client. So not talking about them even though we know by the time that they be they would become a client they will be there would be the wrong thing to do"*. He called them *"what's coming"* (L621). The test is timing, and it covers the AI capabilities only | Ian. The interim form (until Q46) is Novosapien's. Which AI capabilities qualify, and the tense a message uses: Q46 |
| M4 | **No pricing.** No price figures, no price structure (no fee type, no fee name, no tiers), and no cost comparison with the current supplier. Do not write "usage based fees". **A message may say that TXN has a simple pricing structure.** It does not say that other platforms' pricing is opaque or complex (M2). Figures and the structure are a conversation for a person. | Ian, 24 Aug L547-549: asked whether outbound may disclose prices, *"no"*. George, 20 Oct: the price structure is out too, because a message could carry it wrongly. Ian, 21 Oct L855: *"I just don't think pricing in a message is necessary as long as you if you go with a headline of it simple uh pricing structure"*; *"even if you say usage based fees people could say a well is that APIs etc."*; L859: *"it's just better to try to limit what you say in this area"*. Ian framed TXN's position as *"selling against opaque and complex pricing structures"* (L831); under M2 a message does not say this (Novosapien). A pricing calculator on the website (Brett's idea, put by George, L861): rejected, *"there's more risk than there is benefit to it"* (L881) | Ian, 21 Oct. His own caveat has no reply line yet: *"you could argue that if you don't if you don't say it then you being opaque yourself"* (L831); see §7 |
| M5 | **No cost figure that is not TXN's,** including Ian's estimate of the reissue cost per card. | George, 20 Oct | George. Q29 |
| M6 | **The ten-day figure only as a target.** "TXN targets under ten business days from contract signature to the first live transaction." Never describe how a launch happens: no test environment, no promotion to production, no steps. | [[txn-offer-v2]] §2 step 2: the mechanism is not written down. 4 Sep rules | Novosapien. Who does each launch step: Q27 |
| M7 | **Never lead with the owners.** Direct Transact and Paycorp do not appear in the first message or the follow-up sequence. A person introduces them later, when the prospect asks who is behind TXN. A sentence that mentions an owner ends on what TXN delivers. | 2 Sep rulings (`R1`); [[offer]] vocabulary doctrine and §6 | Ian (record); Q36 |
| M8 | **Never claim that TXN holds an accreditation.** If a buyer asks, the reply is: PCI is held by Direct Transact, our co-founding owner, and the platform is operated within that accredited environment. A reply only, never in a first message. | Ian, 3 Sep L417-429: *"DT hold the PCI accreditation"*; SOC 2 and ISO not known | Ian. SOC 2 and ISO 27001: Q35 |
| M9 | **Never describe how the platform was built.** No code lineage, in either direction. The claim is that the platform is TXN's. | 27 Aug session (`S2`): no upside, and it invites the question whether the code is legacy | Ian (record) |
| M10 | **Never name a peer company,** and never name the processor that a prospect or a peer uses. | George, 20 Oct: the workforce cannot confirm a peer's card, and a peer named from model memory can be wrong | George |
| M11 | **Never offer to share or pay part of a cost,** such as the reissue cost. | 27 Aug session: TXN "could consider" sharing the reissue cost; it is not an existing lever | Novosapien; Q29 |
| M12 | **Never say that TXN takes on the client's regulatory responsibility.** Compliance support is confidence, not replacement. | [[txn-offer-v2]] O8, the boundary (`AITO` 3.1.5) | TXN document |

## 2. Claims that wait for Ian

The offer states these claims, but the evidence does not support them in full. The middle column says what a message may say now. The 21 Oct call changed the first three rows.

| Claim in the offer | What a message says now | Question |
|---|---|---|
| TXN settles "with Visa and Mastercard" ([[txn-offer-v2]] Section 1 and step 7). Ian, 9 Oct: "we don't support MC" | **Never "Mastercard coming soon"** (Ian, 21 Oct L609: *"We don't need to see Mastercard say Mastercard coming soon"*). Which scheme to name is not ruled. Name no card scheme as supported until Q34 (Novosapien default). On 24 Aug Ian was comfortable naming both ([[txn-offer-v2]] Section 1, Scheme) | Q34 (Visa; which scheme to name) |
| Was "pre-integrated BIN sponsor relationships in each target market". Since 21 Oct the offer says "existing BIN sponsor relationships" (step 11, the integrations line, D5, D6). Ian, 2 Sep L644: "getting the first one on board" | **Settled by Ian, 21 Oct.** Say **"existing BIN sponsor relationships"** (L781). Name no target market (L777). Name no sponsor in outbound: *"I wouldn't list the actual bin sponsors"* (L787). **No explicit bring-your-own line**: "existing" with no names makes the prospect ask, *"without having to say establish relationships willingness to work with you know additional bin sponsors"* (L793-797) | Q43 (which sponsors TXN has today, so whether the plural holds) |
| O3, "the program runs without card experts on staff", and O8, "compliance requirements are surfaced and applied", as if they work today | Not as live today. Under M3, describe the AI capabilities behind them as what TXN is building for its clients, with no date or figure, until Q46 (Novosapien interim reading of Ian, 21 Oct L617) | Q46 |
| Authorising card spend against a balance that TXN holds | Not as available today. It is not an AI capability, so the 21 Oct timing test does not cover it | Q46 (its last part) |
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
| I5 | ICP 4 | **Contact a company with a live card and no sign of moving on a short sequence, not the full six touches.** Ian did not set the number. It does not apply to ICP 1, 2 or 3. **Not built yet:** variable sequence length is George's proposal. | Ian, 21 Oct L753: *"you wouldn't want to contact them on a six touch sequence"*; L757: *"If they do nothing with the first one or two, I don't know what the exact what the right number is. Chances are they're just not interested. Full stop. It's not the only reason somebody might not respond. But in this specifically specific one, you don't want to go through a full sequence because you're literally just spamming people that are not going to move."* George, L761: *"an idea of maybe having a way to have variable sequences based on the ICP and the signals"* | Ian (principle); George (mechanism, not built). The number: Q45 |

## 6. Rules for one persona

| # | Persona | Rule | Source | Status |
|---|---|---|---|---|
| P1 | ICP 1 founder, CEO or CFO | Do not open with the technology. | 4 Sep persona §11 | Novosapien |
| P2 | ICP 3 CPO or Head of Customer | Use no payments vocabulary that a product lead outside payments has to look up. | 4 Sep persona §11 | Novosapien |
| P3 | The CTO personas | Expect the accreditation question; answer it with the M8 reply when they ask. | 4 Sep personas §11 | Novosapien |

## 7. Open

| Question | Why it is open |
|---|---|
| **Pre-launch.** Should a message acknowledge that TXN has no live clients yet, before the buyer raises it? | The 4 Sep ICP 1 and ICP 4 CTO personas said yes. No line from Ian supports it. The usual answer to "you are pre-launch" is the owners' track record, which may not appear in a first message (M7) |
| **The 2 Sep rulings** (M1, M7, and "TXN sells nothing beyond this offer") | No transcript line exists for them (Q36) |
| **A reply on pricing.** What a reply says when a prospect asks for pricing, or says that silence on price is itself opaque | Ian's own caveat, 21 Oct L831. M4 sends figures to a person. No reply line exists yet (Novosapien) |
| **The banned-word list** (section 3) | Q37 |

## Changes from the 4 Sep rules

The 4 Sep [[buyer-personas]] held nine rules. All nine are here, with two changes:

| 4 Sep rule | Change, 20 Oct |
|---|---|
| "No pricing figures, ever. Ground on the shape" | The price structure is out too (M4, George; confirmed by Ian on 21 Oct) |
| "Naming a prospect's peer is not the same as naming a competitor" (ICP 3: the peer is the opening) | No peer company is named (M10, George) |

## Changes on 21 October

From Ian's answers on the call ([[2026-10-21-icp-revision-outbound]]).

| Rule | Change |
|---|---|
| M3 | An exception for AI capabilities that will be live by the time a prospect becomes a client (Ian, L617). The question is now Q46 (was Q10) |
| M4 | Confirmed by Ian. "A simple pricing structure" is allowed; "usage based fees" is not; no fee type or name. The open question (Q12) is closed |
| §2, schemes | Never "Mastercard coming soon" (Ian, L609). "Name no scheme" stays as Novosapien's default, not Ian's ruling (Q34; was Q2) |
| §2, BIN sponsors | "Existing BIN sponsor relationships", no market, no names, no bring-your-own line (Ian, L777-797). Was "make no claim" (Q11) |
| §2, AI and balance rows | The question is now Q46 (was Q10) |
| I5 | New: ICP 4 on a short sequence (Ian, L753-757). Not built |
| §7 | The price-structure row is closed (Q12); a row for a pricing reply is added |
