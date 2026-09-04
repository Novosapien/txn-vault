---
description: "TXN's Ideal Customer Profile: one fit definition and four ICPs, with Card Program Status as the top parameter, firmographics, anti-profile and tiering"
---

# TXN ICP Definition (v0.4)

> **Source of truth:** `TXN_GTM_ICP_Definition_v0.4.docx` in the outbound folder (`programming/txn/outbound`, mirrored at `shared/clients/txn/outbound`), delivered by Ian Johnson on 24 August 2026. This page is a readable mirror. Edit the source document, then re-mirror. Routed from [[outbound]].

---

TXN Global
Ideal Customer Profile
Who TXN sells to, and who to deprioritise
Version 0.4   |   Author: I. Johnson   |   13/07/2026

## 1. Document Control
| Version | Date | Author | Owner | Description |
| 0.1 | 22/04/2026 | I. Johnson | I. Johnson | Initial version. |
| 0.2 | 01/05/2026 | I. Johnson | I. Johnson | Section 8 (Tiering) and scoring framework. |
| 0.3 | 22/04/2026 | I. Johnson | I. Johnson | Completed Section 9 (Named Account List Method) covering selection criteria, sources, Claude's role in discovery and refresh, storage and format, refresh cadence, governance, and review. Single-owner, monthly refresh. |
| 0.4 | 13/07/2026 | I. Johnson | I. Johnson | Firmographic reconciliation. (1) Section 3 ICP Statement widened to 10-5,000 employees with 20-2,000 as ideal band; "planning to launch" clarified as equal weight to "migrating" in trigger detection. (2) Section 4.3 Company Size expanded to 10-5,000 with rationale for the range. (3) Section 5 adds equal-weight note for launch versus migrate. (4) Section 7 sub-scale operator anti-profile reframed as judgement pattern (small program in small market with no scale ambition), not a headcount threshold. (5) Section 8.1.3 adds reconciliation note tying scoring bands to Section 4.3 range. (6) Section 8.2 adds explicit clarification that P2 Company Size DQ does not disqualify. (7) Spelling standardised: "programme/programmes" replaced with "program/programs" throughout per Core Messaging v2.5 tone rules. |

## 2. Purpose
Define the Ideal Customer Profile for TXN. The ICP is the filter used by Marketing to target, by Sales to qualify, and by Product to prioritise. It is the anchor document for downstream GTM work including personas, messaging, qualification, campaign targeting, and the Named Account List. Everything downstream must be consistent with this document.

## 3. ICP Statement
TXN sells to companies providing, or looking to provide, payment card programs with 10 to 5,000 employees in the EEA plus the United Kingdom. The ideal band is 20 to 2,000 employees where the account scores Priority 1 or Priority 2 on the Section 8.1.3 sizing framework; smaller companies (10 to 19 employees) and larger companies (2,001 to 5,000 employees) remain in scope as Priority 3 candidates where sub-sector fit and triggers are strong. Companies fewer than 10 or more than 5,000 receive zero points on parameter P2 but are not, on that basis alone, disqualified per Section 8.2.
The company is either looking to launch a new payment card program to its customer base or is looking to migrate an existing payment card program from a competitor. Both intents are weighted equally in trigger detection, discovery, and outbound prioritisation. Launching and migrating are treated as parallel workstreams, not sequential.
These companies value the ability to self-serve their card programs by building to a comprehensive API suite and by using intuitive, comprehensive web applications provided by an issuer processor. They are seeking to move quickly with product launches, product evolution, and market expansion.
Currently, they look to issuer processors such as Marqeta, Paymentology, Thredd, Enfuce, Episode Six, and Pismo to provide these services. These competitors have significant gaps in their offerings and often drive clients to build more capabilities themselves to maximise efficiency in managing their card programs.

## 4. Firmographic Criteria

### 4.1 Sectors
FinTech, Banking, Financial Services, Retail.

### 4.2 Sub-sectors
Digital Banking, Expense Management, Lending (SMB), Lending (Consumer), FX Payments, Investment Management, Disbursement, Payments, BaaS, Retail, Ecommerce, Crypto.

#### 4.2.1 Card-essential or card-adjacent

Tagged by Ian, 3 September 2026. **This tagging is what separates ICP 1 from ICP 3** (see 8.1.12), so it is load-bearing rather than descriptive. The operational test is Ian's own: **if you went without a card, would the product look odd?**

| Sub-sector | Card is | Note |
| Digital Banking | **Essential** | The account without the card is an incomplete product |
| Expense Management | **Essential** | The card is the instrument the control and reporting act on |
| Crypto | **Essential, conditionally** | Essential where the proposition is converting crypto to spendable fiat. Crypto-only with no fiat rails remains DQ under 8.1.3, so the same line is drawn from both directions |
| Lending, SMB | Adjacent | Demonstrable use case, optional to the product |
| Lending, Consumer | Adjacent | As above |
| FX Payments | Adjacent | As above |
| Investment Management | Adjacent | As above |
| Disbursement | Adjacent | As above |
| Payments | Adjacent | As above |
| BaaS | Adjacent | **Flagged as the likeliest misclassification.** A BaaS platform bundling issuer functions sits close to card-essential. A researcher in doubt should record the ambiguity rather than pick |
| Retail | Adjacent | As above |
| Ecommerce | Adjacent | As above |

**Note that only three sub-sectors are card-essential.** ICP 1 is the highest-priority ICP and has the narrowest vertical base of the four. That is a real property of the target market, not a gap in the research.

### 4.3 Company Size

> **Ruled 3 September 2026: do not use employee count as a core ranking.** Ian's reasoning, which is the part that matters: in ICP 1 a company where the card is essential may have scaled elsewhere first and have ten people, or may be a startup building cards from day one with fewer than ten. Both are exactly who TXN wants, and ranking on headcount penalises both. *"There are too many different sized businesses that could capitalise on this. Don't use this as a core ranking."*
>
> **Consequences.** The parameter weight drops from 10 to 3 at 8.1.3, enough to register that a 4,000-person company is a different sale without letting size drive the order. **Sub-10 is now explicitly in scope**, which is wider than either ICP v0.4 or Core Messaging v2.5 allowed, so the 10-to-5,000 versus 20-to-2,000 disagreement is not resolved in favour of either: the scope widens and the weight falls. Gap G9 in [[offer]] closes on this basis.

10 to 5,000 employees. The ideal band is 20 to 2,000 employees, where the account scores Priority 1 (50 to 1,000 employees) or Priority 2 (20 to 49 or 1,001 to 2,000 employees) on the Section 8.1.3 sizing framework.
Sub-20 employees remains in scope as Priority 3, particularly for seed and Series A fintechs planning card launches where sub-sector fit and triggers are strong. Above 2,000 up to 5,000 remains in scope as Priority 3, subject to the Tier 1 bank anti-profile exclusion at Section 7. Fewer than 10 or more than 5,000 receives zero points on parameter P2 but does not, on that basis alone, disqualify the account per Section 8.2.

### 4.4 Geography
EEA plus the United Kingdom. Phased outbound priority:
MVP: Poland, Czech Republic, Romania, Hungary.
Phase 1a: Spain, Portugal, Greece.
Phase 1b: Netherlands, Belgium, Austria.
Opportunistic: the remaining EEA plus United Kingdom markets. No EEA plus UK company is excluded from consideration; phasing governs outbound prioritisation and ABM targeting only. Inbound enquiries from anywhere in scope are accepted and qualified normally.

### 4.5 Regulatory Regime
EEA plus the United Kingdom.

### 4.6 Ownership Model
Private companies, listed companies, VC-backed, PE-controlled.

## 5. Behavioural and Situational Triggers
Triggers are the signal that an ICP-fit company is active now. Each trigger has observable signals used for detection and scoring. Companies planning to launch a new card program are weighted equally to companies migrating from an existing incumbent; discovery and outbound treat both as parallel workstreams.
New market entry: public announcement of geographic expansion, licence application filings, hiring in the target country, partner search signals.
Incumbent contract expiry: public reference to a multi-year contract with a named incumbent nearing its anniversary; RFP-like activity; executive remarks on platform change.
Incumbent service performance issues: public incident posts, press coverage of outages, customer complaints on social channels, reports of migration activity.
New product launch: roadmap announcements, funding round press releases referencing card products, hiring for card program roles, beta program invitations. Applies equally to first-time launches by companies with no existing program.

## 6. Technographic Signals
Processor: any incumbent processor is deemed a legitimate target. Named competitors include Marqeta, Paymentology, Thredd, Enfuce, Episode Six, Pismo, Carta, Visa DPS, HPS, i2C, Minisait, Thales, and Tribe, along with in-house legacy processors.
Tech stack: expectation is that the company's tech stack is cloud-based, most likely using AWS, Azure, or Google Cloud. API-first architecture is a strong positive signal.
Engineering capability: in almost all instances the company will have its own in-house engineering team, and will more than likely be utilising AI tools to accelerate development cycles.
Scheme and BIN sponsor signals: existing BIN sponsor relationship (for example Paynetics, DiPocket, Modulr, Transact Payments, Enfuce as sponsor, or Railsr), direct scheme principal membership, Apple Pay and Google Pay integration, named 3DS partner.

## 7. Anti-Profile
Any match on the anti-profile is an automatic disqualification regardless of aggregate score. **The anti-profile is the only disqualification in the framework** (see 8.2), and it applies identically to all four ICPs. Ruled 3 September 2026.

> **Removed 3 September 2026: "companies with limited capital available for investment and operational expenses".** Deleted rather than relocated. Ian's reasoning is an observability test and it is worth keeping: raises are frequently undisclosed, and even when announced you cannot know how much is directed at this, what the next raise depends on, or what triggers send them back for it. Keeping it would mean *"an endless loop analysing data that we really still won't know the story on"*. A criterion that can never be resolved should not be written down, because someone will try to resolve it anyway.

> **Not every item below applies at research time.** Five can be verified from public sources and a research agent applies them. Three cannot be seen from outside and surface only in conversation: bespoke build with client-held IP, on-premises hosting, and the sub-scale operator pattern. They are real reasons to walk away, and they are marked so an agent does not guess. **They must be carried explicitly into the qualification conversation**, or they get missed precisely because they are no longer scored.
**[Conversation only]** Sub-scale operators, defined by a specific pattern rather than a headcount threshold: a card program with limited scale ambition (fewer than 10,000 cards projected within 18 months), confined to a small single-market audience, with no engineering or product capacity to grow. Early-stage companies with clear scale ambition (Series A or later, or seed-stage with a defined product roadmap and hiring plan) do not match this pattern regardless of current headcount.
**[Observable]** Governments and local governments.
**[Observable]** Tier 1 banks (for example Barclays, BNP Paribas).
**[Observable]** Petrol retail companies.
**[Conversation only]** Companies looking for bespoke, non-platform-based solutions where the IP developed rests with the company.
**[Conversation only]** Companies looking for on-premises hosting of an issuer processor solution.
**[Observable]** Companies reported in the press as having difficulties with any local regulator, or under sanctions exposure.
**[Observable]** Companies in active administration, insolvency, or pending wind-down.

## 8. Tiering
Tiering governs how an account is treated across Marketing and Sales. Each account is assigned a tier based on a scoring framework (Section 8.1), subject to gating rules (Section 8.2), with the resulting tier defined in Section 8.3 and the associated actions in Section 8.4.

### 8.1 Scoring Framework
Each account is scored across ten parameters to a total of 100 points. **Card Program Status carries the largest single weight**, because Ian ruled on 3 September 2026 that where a company sits relative to having a card program is the top-level determinant, though not a single determining factor on its own. Geography is weighted above the standard firmographic fields because the GTM phasing governs outbound effort.

> **Rebalance provisional, Ian to confirm.** Card Program Status replaces the retired Incumbent Processor Signal, which freed 8 points and needed 20. The remaining 12 were taken from Triggers, on the reasoning that Status now encodes most of what Triggers was measuring, so leaving Triggers at 20 paid an account twice for the same fact. The total still reaches 100. Any other split of the 12 is Ian's to make.

### 8.1.1 Weight Summary
| # | Parameter | Source Section | Max |
| **1** | **Card Program Status** | **Section 8.1.12** | **20** |
| 2 | Sub-sector / Use Case Fit | Section 4.2 | 17 |
| 3 | Company Size (employees) | Section 4.3 | 3 |
| 4 | Geography / Region Phase | Section 4.4 | 12 |
| 5 | Regulatory Licence Status | Section 4.5 | 8 |
| 6 | Ownership and Funding Stage | Section 4.6 | 8 |
| 7 | Behavioural / Situational Triggers | Section 5 | 8 |
| 8 | Tech Stack and Engineering | Section 6 | 6 |
| 9 | Scheme / BIN Sponsor Signal | Section 6 | 8 |
| 10 | Card Program Scale and Ambition | Sections 3 and 4 | 10 |

*Retired 3 September 2026: **Incumbent Processor Signal**, formerly parameter 7 at 8 points. It scored 8 for a confirmed named incumbent and 0 for "no card program and no stated plan", which ranked the four ICPs in exactly the reverse of Ian's stated priority. It is replaced by Card Program Status rather than sitting alongside it.*

### 8.1.12 Card Program Status (max 20)

> **The number is deliberately out of sequence.** This is parameter 1 by weight and sits first for reading, but it takes the next free number rather than 8.1.2, because [[offer]], [[qualification-matrix]] and the cohort research all cite the existing 8.1.x numbers and renumbering would silently break every one of them.

The top-level parameter. Ruled by Ian on 3 September 2026: where a company sits relative to having a card program is the highest-order determinant, though **not a single determining factor**, so it scores heavily and gates nothing.

**There is no DQ band.** Every company in a target vertical lands in one of the five, consistent with the 2 September ruling that qualification inside a chosen vertical is near-universal and that timing, not exclusion, is what the framework should express.

| Band | Status | Points | Definition |
| A | **ICP 1, first program, card is essential** | 20 | No card program today, and a card is essential to the product they are building or selling. |
| B | **ICP 2, new program, incumbent stays** | 16 | Has a program with an incumbent, and is launching an additional program, product or region. Nothing migrates. |
| C | **ICP 3, industry inference** | 10 | No card program and no stated plan, in a vertical where a named peer runs a program against a use case that would work here. |
| D | **ICP 4, full switch** | 5 | Has a program and is moving all of it. Cardholders and data migrate. |
| E | **Not an ICP: static incumbent** | 3 | Has a program and shows no evidence of any change in motion. |

**Why this order**, recorded because a ranking without its reasoning gets re-litigated:

- **ICP 1 leads on certainty.** Ian: *"you're 100 per cent sure they're going to do it. The only way they don't do it is if the company just doesn't exist."* It is also the exact proposition, which is running a card program without employing card experts.
- **ICP 2 is second** because the decision is made and it is a vendor selection, discounted only because they can change their mind at no cost: they already have a working program and nothing breaks if the new one never launches.
- **ICP 3 is third** because it is a different sale rather than a different message. There is a period of convincing on the value of a card program at all before the conversation reaches why TXN.
- **ICP 4 is last** because nobody moves a full suite to a company with no track record. Ian added a second gate that is not about reputation: buyers now expect migration tooling, and *"they don't expect a 15 year old approach"*. ICP 4 therefore depends on something being built, not only on reference customers being won. Tracked in [[delivery]], not here.

**This inverts the retired parameter 7**, which paid 8 points for a named incumbent and nothing for greenfield. That was scoring card program maturity, which is a reasonable proxy for fit and a poor one for near-term winnability, because maturity implies an incumbent and an incumbent implies the track-record objection.

#### Observable signals

Every signal below must be verifiable from a website, a job post, a named tool or press, or a research agent cannot apply the band.

**Band A.** Product pages describe a card, wallet or spend feature as part of the proposition with nothing live. Waitlist or coming-soon language against a card. Hiring for card, payments or issuing roles with no live program. An EMI or payment institution authorisation in progress. A funding announcement naming a card or payments product. Or the company is structurally a type that requires one: a neobank, an expense platform, a lending product.

**Band B.** A live card evidenced by a BIN, card art, cardholder terms or app store screenshots, **plus** a separate announcement of a new market, segment or product. Hiring for a second program or a new region.

**Band C.** No card evidence anywhere, but the company sits in a vertical where a named peer runs a relevant program, and holds both a customer relationship and a payment flow a card could attach to. **The evidence is about the vertical, not the company**, which is a deliberate departure from the observability rule and is recorded as one below.

**Band D.** A live program plus a change signal: a public service incident with the incumbent, a procurement notice, a contract at renewal age, or a payments hire whose remit reads as migration.

**Band E.** A live program and none of the above.

#### Three limits, recorded rather than hidden

**Band D is the least observable of the five.** Contract position, incumbent identity and card base size are precisely what cannot be seen from outside, and the cohort research confirmed it. ICP 4 will carry the largest gaps list. That is tolerable only because ICP 4 is also last in priority.

**Band C's evidence is an absence plus an inference**, not a signal. The ICP guideline requires every signal to be publicly observable and this one is not, strictly. It is kept because excluding these companies would remove the population Ian ruled on 2 September must never be disqualified for lack of signal, and because a company that has never issued a card emits no card signals by definition.

**Band A, B and D overlap Triggers.** Being in market is itself a trigger. The 12-point reduction to parameter 7 at 8.1.7 is the correction; without it an account is paid twice for one fact.

#### Dominant pain and messaging by ICP

| ICP | Dominant pain | What the message has to do |
| ICP 1 | **Exposure.** Never done this, no incumbent to compare against, no internal experience to sense-check a vendor | Why TXN. They have decided; the job is to de-risk the not-knowing |
| ICP 2 | **Constraint.** Not unhappy, specifically unable | Why TXN. Name the capability, never the incumbent's gap |
| ICP 3 | **Falling behind**, and they may not have registered it | Two jobs. Why a card program at all, carried by the named peer in their vertical, then why TXN |
| ICP 4 | **Entrapment.** Wants out, blocked by migration rather than by the contract | Why TXN, and why the migration will not hurt |

#### Binding rule: never criticise the competition

Ruled by Ian, 3 September 2026, and it applies **in every ICP, not only where an incumbent stays in place.** His position: *"I just don't believe in criticising the competition, it's more important to emphasise your differentiators as you understand them."*

- **Never go after the incumbent or a competitor.** Not named, not implied, not by category. This is stricter than the 2 September ruling that competitors are never named, which governs naming only.
- **Position on what TXN does, as capability rather than comparison.** State what TXN does. Never state what the other cannot. No "unlike your current processor", no "if your provider can't", no implied deficiency.
- **The gap does the work.** Where a capability is genuinely absent on the incumbent, the buyer draws the comparison themselves, and a comparison the buyer makes is worth more than one an agent makes for them.
- **Consequence for the offer.** The `where_it_falls_short` material in [[offer]] Section 5 stays as internal grounding and becomes **context-not-quotable**, the same treatment Section 7 already carries. Agents ground on it; they never voice it.
- **It binds hardest in ICP 2**, where the incumbent stays and the buyer is standing behind a live decision they are not reversing. It binds in ICP 4 too, where the buyer will raise the incumbent themselves and the restraint is what keeps the conversation about TXN.

### 8.1.2 Sub-sector / Use Case Fit (max 17)

> **Raised from 10 to 17 on 3 September 2026**, provisional, Ian to confirm. The seven points come from Company Size. Sub-sector now carries the card-essential versus card-adjacent tagging at 4.2.1, which is what places a company into ICP 1 or ICP 3, so it tells you materially more than it did. Band points below still read to the old maximum and are rescaled on confirmation.
| Band | Points | Definition |
| P1 | 10 | Digital Banking, Neobank. |
| P2 | 7 | Expense Management, Lending (SMB or Consumer), BaaS, FX Payments. |
| P3 | 4 | Investment Management, Disbursement, Payments, Ecommerce, Retail, Gift Card. |
| DQ | 0 | Outside the listed sub-sectors; crypto-only with no fiat rails; staff-card-only use. |

### 8.1.3 Company Size, Employees (max 3)

> **Reduced from 10 to 3 on 3 September 2026.** Ruled by Ian: headcount must not drive the ranking, and sub-10 is in scope. See 4.3. Band points below still read to the old maximum and are rescaled on confirmation.
| Band | Points | Definition |
| P1 | 10 | 50 to 1,000 employees. |
| P2 | 7 | 20 to 49, or 1,001 to 2,000 employees. |
| P3 | 4 | 10 to 19, or 2,001 to 5,000 employees. |
| DQ | 0 | Fewer than 10, or more than 5,000 employees. |

Section 4.3 defines the firmographic range as 10 to 5,000 employees. The scoring bands above allocate points across that range: sub-20 (10 to 19) and 2,001-plus (up to 5,000) score 4 points (Priority 3); fewer than 10 and more than 5,000 score 0. Per Section 8.2, a DQ band on parameter P2 (Company Size) contributes zero points but does not, on its own, disqualify the account. A small start-up with strong sub-sector fit, geography fit, licence fit, and active triggers can still qualify as Priority 3 or higher.

### 8.1.4 Geography / Region Phase (max 12)
| Band | Points | Definition |
| P1 | 12 | MVP markets: Poland, Czech Republic, Romania, Hungary. |
| P2 | 8 | Phase 1a and 1b markets: Spain, Portugal, Greece, Netherlands, Belgium, Austria, United Kingdom. |
| P3 | 5 | Rest of EEA, including France, Germany, Italy, Ireland, the Baltics, and the Nordics (Norway and Sweden are flagged price-sensitive but remain P3). |
| DQ | 0 | Outside EEA plus UK. MENA and Africa markets are handled as later-phase and are not disqualified on geography alone. |

### 8.1.5 Regulatory Licence Status (max 8)
| Band | Points | Definition |
| P1 | 8 | Holds an EMI or credit institution licence in EEA or UK; scheme principal member. |
| P2 | 6 | Holds a PI licence; EMI licence in application; active BIN sponsor agreement in place. |
| P3 | 3 | No licence but engaged with a BIN sponsor; regulated under a secondary regime. |
| DQ | 0 | Unlicensed with no sponsor route; licence revoked; sanctions exposure. |

### 8.1.6 Ownership and Funding Stage (max 8)
| Band | Points | Definition |
| P1 | 8 | VC-backed Series B to D with last raise within 24 months; PE-backed with a growth mandate; listed with a growth profile. |
| P2 | 6 | VC Series A; bootstrapped but profitable; PE-backed with a stable mandate. |
| P3 | 3 | Seed stage with strong investors; established private with flat growth. |
| DQ | 0 | In administration, insolvency, or pending wind-down; sanctions exposure. |

### 8.1.7 Behavioural / Situational Triggers (max 8)

> **Reduced from 20 to 8 on 3 September 2026**, provisional, Ian to confirm. Card Program Status now encodes most of what this was measuring, so leaving it at 20 paid an account twice for being in market. The band points below still read to the old maximum and are rescaled on Ian's confirmation.
| Band | Points | Definition |
| P1 | 20 | Two or more active triggers within 12 months (for example new funding round plus incumbent contract expiry window, or announced product launch plus hiring signals). |
| P2 | 14 | One strong active trigger (announced product launch, funding round within 12 months, public incumbent service issue, executive change in product or tech). |
| P3 | 7 | Weak or historical trigger (incumbent contract signed 2 to 3 years ago, early roadmap hints, low-signal hiring). |
| DQ | 0 | Recently signed a multi-year incumbent contract within the last 12 months with no offsetting trigger. **Scores zero. Does not disqualify** (8.2, ruled 2 September 2026). |
| NE | 0 | **No trigger evidenced.** Added 3 September 2026. Research found nothing either way. Distinct from DQ, which is an adverse fact rather than an absence. Scores zero, never disqualifies, and must not be recorded as DQ: three passes resolved this hole three different ways and each time it removed greenfield accounts on absence of evidence. |

### 8.1.8 Incumbent Processor Signal (retired 3 September 2026)

Replaced by **Card Program Status** at 8.1.12. Kept as a stub rather than deleted, because the register and the scored workbook still carry columns that reference it, and a parameter that vanishes without trace gets re-added by the next person who notices the gap.

The retired bands scored 8 for a confirmed named incumbent and 0 for "no card program and no stated plan". That is the reverse of the priority Ian set on 3 September, and it is the mechanical cause of the bias the register analysis measured: greenfield accounts averaged 61.7 points against 74.4 for migration accounts, and migration took 17 of the 22 Priority 1 places. Incumbent identity is still worth capturing as an attribute; it is no longer worth scoring.

### 8.1.9 Tech Stack and Engineering (max 6)
| Band | Points | Definition |
| P1 | 6 | Cloud-native (AWS, Azure, or GCP), API-first architecture visible, AI tooling adoption signals. |
| P2 | 4 | Cloud-based with a modern stack but not API-first. |
| P3 | 2 | Hybrid stack; limited public technology signals. |
| DQ | 0 | On-premises requirement; no in-house engineering team. |

### 8.1.10 Scheme / BIN Sponsor Signal (max 8)
| Band | Points | Definition |
| P1 | 8 | Existing BIN sponsor relationship (for example Paynetics, DiPocket, Modulr, Transact Payments, Enfuce as sponsor, Railsr), or scheme principal. |
| P2 | 6 | Scheme participation visible (Apple Pay and Google Pay live, named 3DS partner). |
| P3 | 3 | No visible BIN sponsor but licensing signals suggest one is imminent. |
| DQ | 0 | No scheme participation path. |
| UD | 3 | **Live scheme issuer, sponsor undisclosed.** Added 3 September 2026. The company is visibly issuing, so a sponsor exists and is simply not published. This is not "no path". It was every Hungarian issuer in the cohort research without exception. |

### 8.1.11 Card Program Scale and Ambition (max 10)
| Band | Points | Definition |
| P1 | 10 | More than 500,000 cards in issue today or projected within 18 months, or a multi-product card roadmap. |
| P2 | 7 | 100,000 to 500,000 cards in issue or projected. |
| P3 | 4 | 10,000 to 100,000 cards in issue or projected. |
| DQ | 0 | Fewer than 10,000 cards projected; single staff-card use case only. |

### 8.2 Gating Rules

**Rewritten 3 September 2026 to carry Ian's rulings of 2 September.** The previous version gated on four parameters. Three of those gates are withdrawn.

**The anti-profile at Section 7 is now the only disqualification.** Everything else scores zero and stays on the register.

The governing principle, in Ian's words: qualification inside a chosen vertical is near-universal, the exclusion list is very small, and *"everything else shouldn't be treated with anything different than a priority. That is your target market."* A company that scores badly is scheduled later; it is not removed.

| Former gate | Ruling, 2 September 2026 |
|---|---|
| **Triggers (8.1.7)** | **Withdrawn.** Absence of an evidenced trigger must never disqualify. Greenfield companies rarely emit a public trigger, so gating on it silently removed the population that ranks first in priority. |
| **Regulatory Licence Status (8.1.5)** | **Withdrawn.** Ruled directly by Ian: it no longer gates. |
| **Incumbent Processor (8.1.8)** | **Moot.** The parameter is retired. Its DQ band was "no card program and no stated plan", which described exactly the highest-priority ICP. |
| **Sub-sector (8.1.2)** | **Retained.** The one genuine fit exclusion. Outside the listed sub-sectors there is no use case to sell against. |

A DQ band on any other parameter contributes zero points and does not disqualify. In particular, a DQ on Company Size (fewer than 10 or more than 5,000 employees) is not a disqualifier: the account can still reach Priority 3 or higher.

**Two anti-profile carve-outs**, both ruled 2 September:

- **A Tier 1 bank's digital subsidiary is not automatically excluded.** It turns on how operationally independent the subsidiary really is. Ian's reason for the exclusion is not the parent's size but that a small company cannot absorb a large bank's documentation and process load. A subsidiary given capital and loose oversight is in scope; one carrying the parent's full due diligence and process expectations is not. **No early observable proxy for this exists yet, and finding one is open work.**
- **A subsidiary of a non-EEA parent is not excluded on geography.** It depends on which entity the contract is with, and that only surfaces in conversation. Include and find out.

### 8.3 Tier Definitions
| Tier | Total Score | Additional Rules |
| Priority 1 (Tier 1) | 80 to 100 | No DQ on any parameter; no anti-profile match. |
| Priority 2 (Tier 2) | 60 to 79 | No DQ on gating parameters; no anti-profile match. |
| Priority 3 (Tier 3) | 40 to 59 | No DQ on gating parameters; no anti-profile match. |
| Disqualified | Below 40 | Or any gating DQ, or any anti-profile match. |

### 8.4 Tier Actions
Tier 1: accounts are identified and an Account-Based Marketing campaign is executed alongside a sustained, highly tailored outbound sales campaign. Any inbound lead is treated with high importance and urgency.
Tier 2: accounts are identified and LinkedIn marketing approaches are used alongside direct email marketing campaigns. Any inbound lead is handled by Sales and treated with high importance and urgency.
Tier 3: no LinkedIn or direct email marketing campaigns. Any inbound lead is handled by Sales and treated with medium importance and urgency.
Disqualified: no proactive activity. Inbound leads are politely declined or deferred, with a record kept in case qualification changes materially.

## 9. Named Account List Method
This section sets out how named accounts are selected, maintained, refreshed, and retired. The Named Account List is the operating register of ICP-fit companies under active consideration, and it is the single starting point for all Marketing and Sales motion across tiers.

### 9.1 Purpose and Scope
The Named Account List is the register of companies identified as ICP-fit and considered candidates for proactive engagement. Every record carries a score against Section 8, a derived tier, and a set of attached contacts and trigger events. The list is the single operating view of TXN's addressable market at any point in time, and drives the tiered activity defined in Section 8.4.
The list is not a marketing contact database. It is deliberately narrow: only companies that pass firmographic, anti-profile, and minimum-score thresholds appear. Companies evaluated and disqualified are retained on the register with a Disqualified status for audit, re-qualification, and lookback.

### 9.2 Selection Criteria
A company is added to the Named Account List when it meets all of the following:
Passes the firmographic criteria of Section 4 (sector, sub-sector, size, geography, regulatory regime, ownership).
Clears the Section 7 anti-profile with no matches.
Scores 40 or above against the Section 8 scoring framework and is assigned Tier 1, 2, or 3.
Operates in EEA plus UK territory with a registered entity or a documented intent to register.
Has at least one identified contact or a clear path to discovering one within 30 days of addition.

### 9.3 Sources
Candidates are surfaced from two tiers of source.

### 9.3.1 Primary (authoritative, structured)
Regulatory registers: EBA public register of Payment Institutions and Electronic Money Institutions, plus national equivalents (FCA in the UK, BaFin in Germany, KNF in Poland, CNB in the Czech Republic, ANAF in Romania, MNB in Hungary, and equivalents across remaining EEA jurisdictions). These are the single highest-quality feeds because they pre-filter to licensed entities.
Scheme and BIN Sponsor directories: Visa's published partner directory, Mastercard Connect, and the public client pages of Paynetics, DiPocket, Modulr, Transact Payments, Enfuce as sponsor, and Railsr.
Competitor case study pages: Marqeta, Paymentology, Thredd, Enfuce, Episode Six, and Pismo all publish client references on their websites. These are companies currently under contract with an incumbent and are the highest-fit targets for contract-expiry plays.

### 9.3.2 Secondary (signal-rich, unstructured)
Fintech databases: Dealroom.co (European focus, generous free tier, prioritised for Europe), Crunchbase, Pitchbook, Sifted database.
News and trigger feeds: Sifted, Finextra, The Paypers, FinTech Futures, Finovate. Used to detect funding rounds, product launches, executive moves, incumbent churn.
Job posting signals: LinkedIn, Welcome to the Jungle (EU). Keyword searches such as Marqeta, card issuing, BIN Sponsor, Apple Pay integration surface companies hiring for card program roles.
Contact enrichment: Apollo.io or ZoomInfo for contact data; LinkedIn Sales Navigator for verification. Treated as a separate refresh layer given paid tooling and independent update cycles.

### 9.4 Claude's Role in Discovery and Refresh
Claude operates as the orchestration layer above the list. It is responsible for discovery, initial classification, and scheduled refresh; the owner retains decision authority on list composition.

### 9.4.1 What Claude does
Runs a monthly scheduled task (see Section 9.6) to scan the primary and secondary sources for new candidate companies.
Applies Section 4 firmographic filters and Section 7 anti-profile exclusions to each candidate before surfacing.
Drafts a provisional score against the Section 8 framework using publicly available data, with a provisional tier recommendation and rationale.
Produces a shortlist of new candidates with score drafts for owner review, alongside a refreshed view of existing records where any attribute has changed (employee count, funding stage, regulatory status, new trigger events).
Writes every refresh run to the Audit Log tab of the workbook, capturing records checked, records changed, new accounts added, tier changes, and triggers detected.

### 9.4.2 What Claude does not do autonomously
Pull personal contact email addresses at scale. Contact enrichment remains a human-initiated action through Apollo, ZoomInfo, or LinkedIn Sales Navigator.
Send outbound messages. Claude may draft tailored outbound copy on request, but sending remains a human action.
Promote an account between tiers. Claude surfaces proposed changes; the owner approves or rejects.
Archive or retire records without owner approval.

### 9.5 Storage and Format
The Named Account List is held in a single Excel workbook, TXN_GTM_Qualification_Matrix, in 07_GTM/04_Sales_Motion/. Despite the legacy filename, this workbook is both the scoring engine and the Named Account List register. Sheet layout:
02_Scoring_Register: one row per account. Carries firmographic attributes, Section 8 scoring, derived tier, recommended action, status, and workflow fields.
03_Contacts: one row per contact, with foreign key to Account ID. Carries name, title, role category (Champion, Economic Buyer, Primary User, Influencer), contact details, and engagement history.
04_Triggers: one row per detected trigger event, with foreign key to Account ID. Carries date, trigger type, description, source URL, priority, and action taken.
05_Audit_Log: one row per refresh run. Captures what Claude or the owner did and what changed.
Reference tabs (Parameter Reference, Anti-Profile Reference, Tier Definitions, Lookups) hold band definitions, validated values, and dropdown sources.
The data model is CRM-ready. When a CRM is in place, every column translates column-for-column: Account ID becomes the CRM record identifier, Contacts becomes the CRM contacts object with Account ID as the relationship key, Triggers becomes activities or events, and the Audit Log becomes the system audit trail. The workbook is a staging layer until the CRM is in place, after which the workbook is archived.

### 9.6 Refresh Cadence
| Cadence | Activity | Who |
| Monthly (full-list) | Claude scans primary and secondary sources, produces a shortlist of new candidates and a refresh delta on existing records. Owner reviews and approves within one working week. | Claude + Owner |
| 90-day rolling | Every record is re-scored and re-checked on a rolling 90-day basis (one third of the list each month), so no record goes stale. | Claude |
| Event-driven | When Claude detects a high-priority trigger (new funding round, incumbent announcement, executive change), it surfaces it inside the month regardless of the rolling review window. | Claude |
| Ad-hoc | New candidates discovered by the owner or team are added immediately with a provisional score, then validated at the next monthly refresh. | Owner |

### 9.7 Governance
Ian Johnson is the Named Account List owner. Owner approval is required for the following:
Adding a new account to the list.
Any tier change, whether an upgrade or a downgrade.
Archiving or retiring an account (moving to Dormant status).
Any structural change to the workbook schema (new tab, new column, new validated value).
Day-to-day data entry does not require approval. Adding contacts to the Contacts tab, recording activities and notes, and logging triggers in the Triggers tab are free actions.
When an SDR or sales hire joins, this owner role can be delegated. Structural changes remain an owner-approved action.

### 9.8 Review and Retirement
An account is archived (moved to Dormant status) when any of the following apply:
A deprioritisation trigger is hit: the account signs a new multi-year contract with an incumbent, is acquired by a Tier 1 bank, or loses its regulatory licence.
Twelve months pass with no engagement and no new triggers of any kind.
A re-scoring pass puts the account below the 40-point threshold.
An anti-profile match is newly discovered that was not visible at the time of original scoring.
Archived accounts remain in the workbook for audit and for re-qualification if circumstances materially change. A Dormant account is re-activated by a new scoring pass and owner approval.

---

## 10. The Four ICPs

**One fit definition, four buying situations within it.** Sections 3 to 7 define who is in the market at all, and every ICP below inherits that definition unchanged: the same verticals, the same geography, the same firmographics, the same anti-profile. What separates them is **where a company sits relative to having a card program**, which is parameter 1 at 8.1.12.

So a company cannot fail one ICP's criteria and pass another's. It qualifies once, then falls into exactly one of these four, and that placement decides the dominant pain, the message, the buying group and when to call.

Numbered in priority order, ICP 1 highest. **The anti-profile at Section 7 applies identically to all four**, ruled 3 September 2026. Only the observable items are applied at research time; the three marked conversation-only are carried into the qualification conversation instead.

### ICP 1. First program, card is essential

**Priority 1 of 4.** Band A at 8.1.12, 20 points, the heaviest in the framework.

**Archetype name:** `First-Program Card-Essential, the Committed Newcomer`

**Core thesis.** A company building a product that does not work without a card, which has not yet issued one. They are not weighing up whether to have a card program; that decision was made when they chose what to build. What they lack is an incumbent to compare against, current spend to model, internal card expertise, and any way to sense-check a vendor's answers. They will launch, and the only real question is with whom, which is why this ICP carries the heaviest weight. Ian: *"you're 100 per cent sure they're going to do it. The only way they don't do it is if the company just doesn't exist."* Their dominant pain is **exposure**.

**The card is essential to the product, not the product itself.** Ian's correction, 3 September, and it governs the messaging. A neobank's product is the account and the app; expense management's product is control and reporting. The card is how each of them works. Telling either that the card is their product is wrong and they will know it. Telling them their product does not work without one is right.

#### Tier 1: business type

**Primary industry.** FinTech and Financial Services.

**Ideal verticals.** Only three, because only three sub-sectors are card-essential at 4.2.1:
Digital banking and neobanks.
Expense management and spend control, including corporate card and travel-and-expense programs.
Crypto platforms with fiat rails, where the proposition is converting crypto to spendable money.

**Not padded to a minimum.** The guideline asks for four to five verticals. There are three. ICP 1 is the highest-priority ICP and has the narrowest vertical base of the four, and that is a property of the market rather than a gap in the research.

**Core identity, what a researcher must confirm.** The product proposition requires a card to function, and no card is live.

**Website evidence.** A card, wallet or spend feature described in the product pages with nothing issued. Waitlist, coming-soon or beta language attached to the card specifically. A pricing page that assumes a card. Cardholder terms drafted with no BIN. App store screenshots showing a card that cannot yet be ordered.

**State modifiers.**
**Go to market:** hiring for card, payments, issuing or scheme roles with no live program. A first payments hire at a company that has never processed.
**Marketing:** launch-sequence content, waitlist campaigns, a founder writing publicly about why they are building it.
**Growth:** an EMI or payment institution authorisation in progress. A funding announcement naming a card or payments product. Incubator or accelerator cohort membership, which is where these companies exist before they announce themselves.

#### Tier 2: business model

**Primary model.** Product-led or sales-assisted, selling a financial product directly.

**Target customer.** Consumers, SMBs or corporates by vertical. A descriptor, not a qualifier.

**Tech stack signal.** The strongest single signal in this record: **a core banking or ledger platform in place with no issuer processor named.** Thought Machine, Mambu, 10x, Tuum. That is a company building a bank that has not chosen how the cards work. Supporting signals: cloud-native on AWS, GCP or Azure; a named KYC vendor such as Onfido, Sumsub or Veriff; an acquirer handling payments in, with nothing handling payments out.

#### Tier 3: firmographics

**Employee count.** No band and no meaningful score, per the 3 September ruling at 4.3. Sub-10 is in scope.

**Geography.** The EEA plus the United Kingdom, phased per 4.4. Phasing orders effort; it excludes nobody.

#### Disqualifiers

Research-time only. Everything here is verifiable from outside.

**A card is already live.** Then the company is ICP 2, ICP 4 or a static incumbent. This is the single most important separation in the record.
**Crypto-only with no fiat rails.** Already DQ at 8.1.3, and the mirror of why crypto is card-essential when the fiat conversion is the offer.
**Government or local government.** Anti-profile.
**Tier 1 bank**, subject to the subsidiary carve-out at 8.2. Anti-profile.
**In administration, insolvency or pending wind-down**, or reported regulator difficulty or sanctions exposure. Anti-profile.

**Deliberately not listed:** on-premises hosting, bespoke build with client-held IP, and the sub-scale operator pattern. All three are real reasons to walk away and none is observable from outside, so they are qualification questions rather than research disqualifiers. This matters most for ICP 1, where the companies are earliest and a researcher is most tempted to infer.

#### Buying group

Re-derived for this ICP rather than carried over from [[offer]].

**CPO leads.** The card is essential to the product they are building, so it is a product decision before it is a technical one.
**CTO validates feasibility**, and holds the technical veto. In this ICP they are validating something nobody in the building has done before, which is the exposure pain in its most concrete form.
**CFO** funds it as part of the product build rather than as a separate platform decision.

#### Signal to pain mapping

| Observable signal | Primary inferred pain | Relevance to the offer |
| Core banking or ledger platform live, no issuer processor named | **They have built the account and cannot yet build the card.** The product is visibly incomplete and the missing piece is the one nobody in the building has done before | Section 2 steps 1 and 2 configure and certify the program. Step 10 wraps the mechanics in business language, so the decision does not require a card expert on staff |
| Card described in the product, waitlist or coming-soon, nothing issued | **They have committed publicly to a date they cannot yet defend.** The launch is announced and the mechanism is not chosen | Step 2 is the launch path. The under-ten-days figure is TXN's target for exactly this position, and is stated as a target and never as a result |
| First payments or card hire at a company that has never processed | **They are buying the expertise they lack one person at a time**, and that person becomes a single point of dependency before they have written anything | The primary job at Section 1: run a card program without employing card experts |
| EMI or payment institution authorisation in progress, no processor named | **The licence will arrive before the platform does.** A regulatory clock is running against a decision nobody has made | Steps 6 and 10 carry scheme and regulatory obligations as delivered outcomes rather than research the client begins from nothing |
| Incubator or accelerator cohort membership, card named in the proposition | **Nobody has told them what this costs in time, money or risk.** Pre-decision on the vendor and pre-informed on the domain | The whole of Section 2. This population is also the target of the incubator monitoring instruction at 4.3 |

### ICP 2. New program, incumbent stays

**Priority 2 of 4.** Band B at 8.1.12, 16 points.

**Archetype name:** `Second-Program Builder, the Constrained Operator`

**Core thesis.** A company already running a card program with an incumbent, launching an additional program, product or region somewhere else. Nothing migrates and nobody is leaving; the incumbent stays in place and keeps the original book. These buyers know the domain, have integrated a processor before, and can tell you precisely what their current one cannot do, because they have already asked and been told no. The discount against ICP 1 is that they can walk away at no cost: they have a working program and nothing breaks if the new one never launches. Their dominant pain is **constraint**, which is not unhappiness but specific inability.

**The binding rule applies hardest here.** Never go after the incumbent, named, implied or by category (7 and 8.1.12). The incumbent stays, so the buyer is standing behind a live decision they are not reversing, and criticising it criticises them. State what TXN does, never what the other cannot, and let the buyer draw the comparison.

#### Tier 1: business type

**Primary industry.** FinTech, Banking, Financial Services and Retail.

**Ideal verticals.** All twelve at 4.2 are eligible, because a live program already proves the use case works for them. Weighted towards those with multi-product roadmaps or multi-region ambitions: digital banking and neobanks, BaaS, FX payments, lending, expense management.

**Core identity, what a researcher must confirm.** A live card program **and** a separate, dated commitment to a new product, segment or geography.

**Website evidence.** A live card evidenced by a BIN, card art, cardholder terms or app store screenshots. Then, separately, a new market landing page, a second product line, a regional domain or a localised pricing page that the existing program does not cover.

**State modifiers.**
**Go to market:** hiring for a named new market or product line. A second payments or program manager rather than a first.
**Marketing:** launch messaging for a new segment. Regulatory or licence announcements in a market they do not yet serve.
**Growth:** a funding round earmarked for expansion. A partnership or distribution agreement that implies a card the current program does not issue.

#### Tier 2: business model

**Primary model.** Sales-led or sales-assisted, usually further along than ICP 1.

**Target customer.** Whoever the new product serves, which is frequently not who the existing program serves. That gap is the opportunity.

**Tech stack signal.** An identifiable incumbent processor, captured as an attribute and no longer scored since 8.1.8 was retired. Multi-region infrastructure. A second core banking or ledger instance. Localisation tooling.

#### Tier 3: firmographics

**Employee count.** Not ranked, per 4.3. In practice larger than ICP 1, because running one program and launching another takes capacity.

**Geography.** EEA plus the United Kingdom, phased per 4.4. Note the new market may sit outside the phase order while the company sits inside it, and the company's location governs.

#### Disqualifiers

**No card program at all.** Then it is ICP 1 or ICP 3.
**Moving the existing program too.** Then it is ICP 4, and the migration conversation dominates.
**No evidence of a second program, product or region.** Then it is a static incumbent at band E.
Plus the five observable anti-profile items at 7.

#### Buying group

**CPO leads.** Ruled by Ian, 3 September: a new product or a new region is a product decision.
**CTO weighting is open**, and it is a genuine question rather than a detail. This is the only ICP where the client ends up **running two processors in parallel**: two integrations, two reconciliations, two sets of scheme reporting, one team. That either makes the CTO more central than in any other ICP, because the ongoing cost is theirs, or barely registers because the programs never touch. Ian's experience decides it, and it also decides whether TXN raises the cost of running two or answers it before being asked.
**CFO** approves on commercial grounds, comparing against a price they already pay.

#### Signal to pain mapping

| Observable signal | Primary inferred pain | Relevance to the offer |
| Live card program plus a new market landing page or localised pricing | **The existing platform does not reach where they are going.** They have chosen the market and discovered the constraint afterwards | Section 2 steps 1, 6 and 11 configure a program and its BIN and routing per market, so a new geography is configuration rather than a second vendor relationship |
| Live program plus a second product line the current card cannot support | **The platform decides what they are allowed to build.** The roadmap is being shaped by a vendor's limits | Steps 5 and 9 carry programmable controls and the extension surface, which is where a product that the incumbent cannot express becomes buildable |
| Hiring a second program manager or a market-specific payments lead | **They are adding people to work around a platform**, which is the cost of the constraint made visible on a payroll | The primary job: run a card program without employing card experts. Step 10 removes the headcount the workaround needs |
| Partnership or distribution deal implying a card the current program does not issue | **A commercial commitment is running ahead of the platform.** There is a date attached and the current vendor is not the answer | Step 2 is the launch path, and the ten-day figure is TXN's target, stated as a target |
| Multi-region infrastructure with a single-region card program | **The company is multi-market and the card is not.** The asymmetry is visible from outside and is felt internally as a ceiling | Steps 6 and 11 handle multi-jurisdiction obligation and BIN structure, so the card catches up with the rest of the business |


### ICP 3. Industry inference

**Priority 3 of 4.** Band C at 8.1.12, 10 points.

**Archetype name:** `Card-Adjacent Unaware, the Peer-Shadowed Operator`

**Core thesis.** A company with no card program and no stated plan for one, operating in a vertical where a named peer already runs a card program against a use case that would work here. They may never have considered it. The qualification is an inference drawn from the vertical rather than a signal emitted by the company, which makes this the only ICP where the evidence is about somebody else. It is also a different sale rather than a different message: there is a period of convincing on the value of a card program at all before the conversation reaches which vendor. Their dominant pain is **falling behind**, and they may not have registered it yet.

**This is the population that must never be disqualified for lack of signal.** Ruled 2 September. A company that has never issued a card emits no card signals by definition, and the old framework scored exactly that condition at zero and gated on it.

#### Tier 1: business type

**Primary industry.** Retail, Ecommerce, Financial Services and the adjacent operating verticals.

**Ideal verticals.** The nine card-adjacent sub-sectors at 4.2.1: lending SMB and consumer, FX payments, investment management, disbursement, payments, BaaS, retail, ecommerce. Not the three card-essential ones, because a card-essential company with no card is ICP 1.

**Core identity, what a researcher must confirm.** Three things together. No card evidence anywhere. A **named peer** in the same vertical running a card program against a use case that transfers. And the two preconditions that make a card possible at all: they hold a **direct customer relationship** and they already move **money to or from** those customers.

**Website evidence.** This is the inverse of every other ICP, because the company-level evidence is an absence. What is present instead: a customer account or login, a stored balance, wallet, store credit or loyalty scheme, a payout or disbursement flow, a subscription or recurring billing relationship. Any of those is a card waiting to happen.

**State modifiers.**
**Go to market:** none card-related, by definition. Look instead for a company investing in its own customer relationship, which is where a card becomes rational.
**Marketing:** loyalty, rewards, membership or wallet propositions.
**Growth:** funding or expansion that increases the customer base a card would serve.

**The peer map is a prerequisite, not a nicety.** ICP 3 cannot be operated without a maintained list of named companies per vertical who have launched a relevant program, because the peer is both the qualification evidence and the opening of the message. That list does not exist yet and building it is the largest outstanding piece of work on this ICP.

#### Tier 2: business model

**Primary model.** Any model with a recurring or account-based customer relationship. Marketplaces, subscription businesses, platforms with a payout side.

**Target customer.** Consumers or SMBs held as accounts rather than as transactions.

**Tech stack signal.** A payments-in acquirer with no payments-out capability. A loyalty or rewards platform. A customer identity or account system. Notably absent: anything issuing-related.

#### Tier 3: firmographics

**Employee count.** Not ranked, per 4.3.

**Geography.** EEA plus the United Kingdom, phased per 4.4.

#### Disqualifiers

**Any card evidence at all.** Then it is ICP 4, ICP 2 or a static incumbent.
**A card-essential vertical.** Then it is ICP 1, which outranks this.
**No direct customer relationship**, for example pure wholesale or B2B2B with no end user.
**No money movement to or from customers**, which removes the use case entirely.
**No named peer in the vertical.** Without one there is no evidence, and inventing a peer is fabrication.
Plus the five observable anti-profile items at 7.

#### Buying group

**CPO and CFO together**, confirmed by Ian on 3 September. Somebody has to fund a thing the business has lived without, so the product case and the business case are made in the same conversation rather than in sequence.
**CTO is not in the buying group at this stage.** They arrive once the decision to have a card program has been taken, which is after the sale this ICP is running.

#### Signal to pain mapping

| Observable signal | Primary inferred pain | Relevance to the offer |
| A named peer in the same vertical launched a card program in the last 24 months | **A competitor has built a revenue and engagement line they have not.** The gap is visible to their market before it is visible to them | The whole of Section 2, framed as what the peer did rather than what TXN sells. This is the only ICP where a competitor's success is the opening |
| Stored balance, wallet, store credit or loyalty scheme, no card | **Money is already sitting with them and cannot be spent anywhere else.** The customer relationship is being under-monetised in a way the balance sheet shows | Steps 3, 4 and 5 turn a held balance into a spendable instrument with controls, which is the shortest path from what they have to what the peer built |
| Payout or disbursement flow to customers or suppliers, paid by transfer | **Every payout is a cost and a delay rather than a product.** They are moving money without owning the moment it is spent | Steps 3 and 4 make the payout an issued card, which changes a cost line into a retained relationship |
| Subscription or account-based relationship with no payment instrument of their own | **They own the customer and rent the payment.** The most valuable part of the relationship belongs to someone else | The primary job at Section 1, and step 10, because this buyer has nobody who could run a card program today |
| Investment in loyalty, rewards or membership without a card | **They are buying engagement the hard way.** They have already decided the customer relationship is worth spending on, and reached for the weaker instrument | Step 5's programmable controls and step 9's extension surface, where rewards and offers attach to spend rather than to a points ledger |


### ICP 4. Full switch

**Priority 4 of 4.** Band D at 8.1.12, 5 points.

**Archetype name:** `Full-Switch Migrator, the Blocked Escapee`

**Core thesis.** A company running a live card program that intends to move all of it to another processor. Cardholders and data migrate, and that single fact governs everything: the qualification questions, the risk conversation, the commercial shape and the timeline. They have usually decided the incumbent has failed them, so the sale is not about whether to move but about whether moving is survivable. Their dominant pain is **entrapment**: cumulative dissatisfaction blocked by migration risk, where the blocker is rarely the contract but the cardholder base, the reissue question, and the absence of a route that does not disrupt live customers.

**Last in priority, and gated on two things rather than one.** Nobody moves a full suite to a company with no track record, so reference customers are the first gate. The second is a product dependency: Ian, 3 September, on buyers now expecting migration tooling, *"they don't expect a 15 year old approach"*. ICP 4 therefore waits on something being built as well as something being won. Tracked in [[delivery]], not here.

#### Tier 1: business type

**Primary industry.** FinTech, Banking and Financial Services.

**Ideal verticals.** All twelve at 4.2 are eligible; a live program proves the use case. Weighted towards those where the incumbent set is known to underperform.

**Core identity, what a researcher must confirm.** A live card program **and** evidence of intent to replace the processor entirely, as opposed to adding one.

**Website evidence.** Weakest of the four ICPs. A live card is easy to confirm; the intent to move is rarely published. Occasionally visible through a status page history of incidents, a public procurement notice, or a careers page describing a migration.

**State modifiers.**
**Go to market:** a payments or platform hire whose remit reads as migration or vendor consolidation.
**Marketing:** unusually quiet on the card while the rest of the business is loud, which sometimes precedes a replatform.
**Growth:** a funding round or acquisition that triggers a platform review. A contract at renewal age, where known.

**Observability is the structural weakness of this record.** Contract position, incumbent identity and card base size are exactly what cannot be seen from outside, and the cohort research confirmed it. ICP 4 will carry the largest gaps list of the four. That is tolerable only because it is also last in priority.

#### Tier 2: business model

**Primary model.** Established, revenue-generating, usually sales-led.

**Target customer.** Whoever the existing program already serves, which is knowable from the live product.

**Tech stack signal.** An identifiable incumbent processor, held as an attribute rather than scored. Public incident history. Integration surfaces that suggest a stitched vendor set.

#### Tier 3: firmographics

**Employee count.** Not ranked, per 4.3. In practice the largest of the four, because a migratable book implies scale.

**Geography.** EEA plus the United Kingdom, phased per 4.4.

#### Disqualifiers

**No live card program.** Then it is ICP 1 or ICP 3.
**Keeping the incumbent for the existing book.** Then it is ICP 2, and the migration conversation does not apply.
Plus the five observable anti-profile items at 7.

#### The qualification set that exists in no other ICP

Not scored, because none of it is observable. It is the first conversation, and it is written here so it is not improvised.

**Who owns the cardholder data today**, and what the incumbent contract says about extracting it.
**Reissue or run to expiry.** Reissuing is cleanest, and Ian's caution applies: running to expiry leaves recently renewed cards stranded outside the window for another three to five years, so those get mopped up separately.
**What the reissue costs at their card count.** Ian's estimate is roughly two pounds or two euros per card, all in, covering plastic, branding, personalisation, production including the chip, and postage. At 100,000 cards that is material, and it is recorded as his industry estimate rather than a TXN price.
**Why they are moving**, because it changes the reissue appetite. Service-level dissatisfaction means they want the path of least resistance and will resist reissuing. Moving to launch something new usually brings new branding anyway, so reissue matters less.
**Whether TXN shares any of the reissue cost.** Ian has described this as something TXN could consider for a program already at scale, and it is **not an existing lever**. It must not be offered.

#### Buying group

**CTO leads**, proposed and **not yet confirmed by Ian**. The reasoning is that migration risk is technical risk, engineering owns the existing integration, and the decision that stops this deal is whether the move is survivable.
**CPO** carries the cardholder disruption question, since reissue is a customer-experience event before it is a technical one.
**CFO** carries the reissue cost, which in this ICP is a real number on a real card base rather than a modelling exercise.

#### Signal to pain mapping

| Observable signal | Primary inferred pain | Relevance to the offer |
| Live program with a public incident history on the incumbent | **They are carrying someone else's reliability as their own reputation.** Every outage is theirs to explain to cardholders | Section 2 step 12 is the migration path, and step 7 the clearing and settlement chain they would be moving onto |
| A payments or platform hire whose remit reads as migration or consolidation | **They have already decided and are staffing the escape.** The decision is made and the route is not | Step 12, and the qualification set above. This is the one ICP where the first conversation is about risk rather than capability |
| Live program at a contract renewal age, where knowable | **A window is opening that closes again for years.** If they miss it they are held for another term | Step 12, plus the commercial shape at Section 7, since term and notice are the whole conversation at this moment |
| Stitched vendor set visible around a live program | **Nobody owns the failure.** Moving means untangling several relationships at once, which is why they have not | Steps 4 to 7 and 11 consolidate processing, controls, authentication and settlement, so the migration reduces the vendor count rather than moving it |


