---
description: "Reviewer brief for the Novosapien x TXN MSA v0.3: positions taken, IP and liability decisions, EU regulatory addenda, and open points for counsel"
---

# Reviewer Brief: Master Service Agreement (Novosapien x TXN)

**Prepared by:** Novosapien commercial-lawyer skill · **Date:** 2026-07-03, updated 2026-07-22, updated 2026-10-07 · **Draft version:** v0.3
**Instrument:** Master Service Agreement + Statement of Work 2 (Phase 2 of the Agentic AI Layer); Phase 1, the pilot, is the adopted Statement of Work 1
**Parties:** Novosapien and TXN
**Governing law:** England and Wales

> **CHANGELOG, 2026-10-07 (v0.3: phase naming, Phase 1 completion, Phase 3 decommitted).** Read section 14 first. It is the current statement of the commercials and it supersedes anything below it that conflicts.

> **CHANGELOG, 2026-07-22 (pilot separation).** The six-week pilot has been carved out into a standalone **Pilot Order** (see `txn-agentic-pilot-order.html` + its reviewer brief) so TXN's CEO could authorise it before going on leave, ahead of signing this MSA. This MSA is edited to match:
> - New **clause 2.1A** adopts the pilot, delivered under the Pilot Order, as the **completed Statement of Work 1** on MSA signature (its Deliverables and already-assigned Foreground IP become Deliverables/Foreground IP here; no further charge; nothing rebuilt).
> - The wider engagement (wire-in build + Phase 3) is now **Statement of Work 2** (Schedules 1 and 2); Schedule 1 heading and clause 2.1 updated.
> - **Clause 7.2** repriced: build £144,500 (4 months) reduced to **wire-in £90,312.50** (~2.5 months); new note that the pilot (£54,187.50) was charged under the Pilot Order and is not re-charged. Clause 7.1 now cites the **22 July 2026 proposal (v1.2)**.
> - **Schedule 2** payment schedule and deliverable allocation rebuilt to the wire-in figures, with Sprint Zero and Pilot shown as reference rows. Month numbering changed from "months 5 to 7" to "November to January".
> - **Total committed engagement unchanged at £270,375** (Sprint Zero £17,500 + Pilot £54,187.50 + wire-in £90,312.50 + Phase 3 £108,375). Support £4,250/mo after Phase 3, unchanged.
> - IP position is unchanged in substance: clause 6.3's present assignment now flows to the pilot via the Pilot Order (which lifts the same language) and the clause 2.1A adoption.
>
> Persona reviews below predate this change; re-check the charges and SoW-numbering sections against the current draft.

## 1. What this is and what it is not

A competent **first draft**, generated from Novosapien's standard house paper, with scope grounded in the TXN product vault (`txn-vault/content/**`) and commercials grounded in the latest proposal (`proposals/txn-agentic-layer-proposal_final.pdf`, v1.0, 17 June 2026). It is **not final legal advice** and needs a qualified solicitor's review before execution, particularly in a regulated payments context. This brief lists the positions, assumptions, negotiables, and open points so review is fast.

## 2. The deal in one paragraph

Novosapien builds the **agentic AI layer** across TXN's three surfaces (Core API, Console, Developer Portal) and its internal ops, delivered by a full-time team of three, bought by the month. TXN's platform is built by other partners (Direct Transact, Stackworkz, Super Ultra); Novosapien delivers the AI layer only.

**The commercials in this section were superseded on 7 October 2026. See section 14.3 for the current position.** For the record, the figures this paragraph originally carried, a £144,500 four-month build to an October 2026 launch with a committed Phase 3 retainer, are no longer the deal. Phase 1 is delivered and accepted, Phase 2 is £90,312.50 over 28 September to 15 December 2026, and Phase 3 is not committed.

## 3. Key positions taken (and why)

| Clause | Position taken | Rationale / source |
|--------|----------------|--------------------|
| Structure | MSA framework + SoW per engagement | Repeat/phased work (Phase 1, then Phase 2, then Phase 3); keeps legal terms stable |
| Charges (7.2-7.5) | **Superseded, see section 14.3.** Phase 2 £90,312.50 in tranches of £36,125, £36,125 and £18,062.50; Phase 3 not committed; support £4,250/mo from 16 December 2026 | Phase Two proposal, 28 September 2026 |
| Late payment (7.4) | 4% above BoE base rate | Proposal (note: this is *below* the statutory 8%-above-base default under the Late Payment Act; it is a concession to TXN) |
| Liability cap (9.4) | Total charges paid; carve-outs for confidentiality breach + wilful misconduct (plus the statutory carve-outs) | Proposal ("capped at total fees paid; no indirect or consequential damages, except confidentiality or wilful misconduct") |
| Termination (10.2-10.3) | 30 days' notice; handover deployable + documented | Proposal |
| AI output (3.3-3.4) | Advise-not-decide; no accuracy warranty; approvals + permission model respected; no fraud auto-execution | Vault section 6 non-negotiables + trust concepts |
| IP (6) | Three-way split: (6.2) Novosapien's delivery agents = Background IP, a build cost, excluded from what TXN gets; (6.3) the agents/AI/data built for the TXN platform = Deliverables, **exclusive to TXN and assigned to TXN on full payment** (full title guarantee, present assignment of future rights, embedded Background IP licensed as needed to use the Deliverables); (6.4) Novosapien's Content / Inbound / Outbound / Deal Lab Workforce products = **excluded**, available later only under a separate monthly consumption licence | Protects Novosapien's tooling and productised workforces while giving TXN clean ownership of its build. Assignment decided 6 July 2026: the 6.3 exclusivity promise had already removed the resale value of retaining ownership, and a regulated payments customer would demand ownership for exit/continuity anyway |
| Compliance (4.3) | TXN owns all compliance frameworks; Novosapien builds to respect them | Vault section 6 + proposal warranties (PCI-DSS, GDPR, FCA) |
| Data (6.4, 8.2, Sch 3) | Novosapien = processor; Art 28 schedule; no training on TXN/client data; cardholder PII limited/redacted; UK/EU residency | Vault section 6 (#16: limit + redact + EU residency) + ai-software-clauses |

## 4. Assumptions made (confirm before execution)

- **Novosapien's legal entity: inserted (6 July 2026).** Novosapien Global Ltd, company no. 17308181, registered office Aldgate Tower, 2 Leman Street, London E1 8FA. The contracting entity is Novosapien, full stop: no Teraflow references anywhere in the paper, and no novation exercise for prior work; Sprint Zero is treated as delivered and paid, referenced only as a completed milestone.
- **TXN's legal entity: inserted (6 July 2026).** TXN Global Limited, registered office Office 303, 20 Iacovou Patatsou, Egkomi, 2408 Nicosia, Cyprus. The Cypriot company (HE) number is the one remaining TXN particular. Cyprus establishment confirms the EU counterparty analysis in section 9: EU GDPR governs TXN's processing, and the England & Wales governing-law enforcement note stands.
- Governing law England & Wales is correct for both parties.
- TXN is the contracting customer (not one of the build partners); DT, Stackworkz, and Super Ultra are TXN's responsibility, not Novosapien's subcontractors.
- The scope reflects the vault as at the June deep-dives and the 17 June proposal.
- ~~Payment period is 30 days (proposal gives the tranche timing but not the invoice payment window)~~ **Decided (6 July 2026): each invoice is payable on its date of issue (clause 7.4).** Counsel note: payable-on-issue means the late-payment interest clock starts immediately; a receiving finance team may push for 14 or 30 days, which is a concession Novosapien can trade.

## 5. Negotiable / decisions needed

- **IP: assignment vs licence: decided (6 July 2026).** Clause 6.3 now assigns the Foreground IP in the Deliverables to TXN on full payment of the relevant SoW, with an interim licence until payment and a use-licence to the Background IP embedded in the Deliverables. Counsel to check the assignment formalities, nothing commercial left to decide.
- **Liability carve-outs (9.4): decided (6 July 2026).** Confidentiality breach and wilful misconduct stay fully **uncapped**, as drafted. Counsel should still sanity-check the exposure, but the commercial decision is made.
- **Support & Maintenance: done.** Documented as a standalone Support & SLA agreement (`txn-agentic-ai-layer-support-sla.html`), with its own reviewer brief.
- Retainer "no minimum term, 30 days' notice" is generous to TXN; confirm that is intended.
- **AI Workforce product names (6.4).** Confirm the exact product names and that the list (Content, Inbound, Outbound, Deal Lab Workforce) is current. "Deal Lab Workforce" is taken from "Dill lab" in instructions; confirm spelling. The monthly consumption licence-fee terms are deliberately left to a future separate order, not priced here.

## 6. Risks and things to watch

- **Multi-tenancy is unresolved** (vault open question #48: ring-fenced per-client stacks vs central orchestration) and **infra separation** (#49). This affects the AI layer's architecture. **Partially resolved (6 July 2026): hosting responsibility is settled.** New clause 4.6 records that hosting, infrastructure, and the multi-tenancy architecture are provided and managed by TXN or its other partners in every model; Novosapien carries no liability for their failure, and downtime they cause is excluded from delivery obligations, service levels, and the liability cap (clause 9.5). The architectural choice itself remains a `[placeholder]` dependency in Schedule 1.
- **Dependency risk is high and partner-led.** Delivery dates depend on DT (Core API + YAML cadence, Data Lake schema) and Stackworkz (Console instrumentation, Portal plug-in points). Clause 4.2 gives relief for partner-caused delay; make sure TXN accepts that risk allocation.
- **Payments/FCA context.** The proposal warrants the architecture "supports and does not impede" TXN's PCI-DSS/GDPR/FCA obligations. Keep that as a design commitment, not a compliance guarantee; the draft (4.3, 9.1) does this. A solicitor should confirm the framing is tight enough.
- **Cardholder PII into LLM context** is a live risk (vault section 8). Schedule 3 limits and redacts; confirm the data-residency mechanism if any personal data leaves the UK (model/hosting providers as sub-processors).
- **Fraud & Risk Assist and Reconciliation** are excluded from SoW 1 (data-dependent). Keep them to a later SoW so they are not read as in-scope now.

## 7. Open questions for counsel

1. ~~Correct Novosapien contracting entity post-buyout, and any novation of prior (Teraflow) work?~~ **Resolved (6 July 2026): Novosapien contracts in its own name; no novation. Entity particulars still to insert.**
2. ~~Foreground IP: assignment or licence?~~ **Resolved (6 July 2026): assignment on full payment, per SoW. See sections 5 and 11.**
3. ~~Are the confidentiality / wilful-misconduct liability carve-outs uncapped, or subject to a separate cap?~~ **Resolved (6 July 2026): uncapped, as drafted.**
4. Is the 4%-above-base late-payment rate (below the statutory default) a deliberate, retained concession?
5. ~~Should support & maintenance be a separate Support & SLA agreement?~~ **Done: standalone Support & SLA agreement drafted.**
6. ~~Payment window (days from invoice) for each tranche and the monthly retainer?~~ **Resolved (6 July 2026): payable on the date of invoice.**

## 8. What is grounded vs assumed on scope

- **Grounded in the vault:** the six in-scope components and their sub-components, the advise-not-decide / approval-queue non-negotiables, the multi-vendor scope boundary, PII limit+redact+EU residency, and the later-phase status of Fraud and Reconciliation.
- **Grounded in the proposal:** all charges, payment schedule, retainer, support fee, day rates, liability position, termination, late-payment rate, and the four-month-to-launch phasing.
- **Assumed / to confirm:** both parties' legal entity details and the invoice payment window. (Previously listed here and since resolved: contracting entity, IP ownership, liability carve-outs, and hosting/infra responsibility.)

## 9. Addendum (2026-07-06): European regulatory review

TXN is a European card processor, so the draft was upgraded from UK-only to EU-aware. Changes made and points for counsel:

**Changes made to the draft:**
- **Dual-regime data protection.** Clause 8.2 now defines Data Protection Laws as EU GDPR + UK GDPR + DPA 2018; Schedule 3 is retitled to both regimes and gains rows for applicable regime, processing locations, transfer mechanism (EU SCCs and/or UK IDTA/Addendum with a transfer risk assessment), breach notification supporting TXN's 72-hour clock, and audit rights.
- **DORA (Reg (EU) 2022/2554).** New clause 4.4 (Regulatory cooperation) carries the Article 30(2) baseline: audit/regulator access, processing locations with change notice, incident assistance, exit plan and data return, and an agreed uplift to the Article 30(3) provisions (contingency testing, enhanced audit) if TXN designates the agentic layer as supporting a critical or important function. **Ask TXN for that designation; it decides the tier of obligations and should be priced.**
- **EU AI Act (Reg (EU) 2024/1689).** New clause 6.7 allocates roles (Novosapien develops/supplies, TXN deploys), commits transparency documentation, records the advise-not-decide human-oversight design, and gates any potentially high-risk use case (notably creditworthiness assessment) behind prior written agreement and a joint assessment. Relevant to the later-phase Fraud & Risk Assist component.
- **PCI-DSS.** New clause 4.5 states the design position: Novosapien does not store, process, or transmit cardholder data, and cardholder data stays out of AI model context; any future change triggers a PCI responsibility acknowledgment first.
- **Customer materials licence.** Clause 6.6 now grants Novosapien the limited licence to use TXN's data, materials, and branding solely to provide the Services (previously implied only).

**Remaining points for counsel (in addition to section 7):**
1. Confirm TXN's country of establishment; it determines the EU/UK GDPR split, the transfer mechanism, and whether an EU representative analysis is needed.
2. Obtain TXN's DORA position: is TXN in scope as a financial entity, and is the agentic layer designated critical/important? If yes, scope and price the Art 30(3) uplift (TLPT participation, contingency-plan testing, enhanced audit).
3. Governing law is England and Wales with an EU counterparty: enforcement post-Brexit is slower (no Lugano). Expect a request for the counterparty's law or arbitration; decide the fallback position before negotiation.
4. Insurance: an EU FS customer will likely ask for stated professional indemnity and cyber cover. Confirm Novosapien's actual policies before committing figures.
5. Verify the fraud-adjacent components against the AI Act high-risk list before Phase 3 scoping (fraud detection has a partial carve-out; creditworthiness does not).

## 10. Addendum (2026-07-06): liability cap repositioned (negotiation anchor)

**Change made on instruction:** clause 9.4's cap is now **30% of the total implementation fee (£43,350, based on the £144,500 build fee)**, replacing "total charges paid". The confidentiality / wilful-misconduct carve-outs are unchanged.

**This deliberately diverges from the proposal**, which stated *"Liability: capped at total fees paid."* It is an opening negotiation position, not the expected landing zone. Before sending:

1. **Decide the floor.** Anchor at £43,350; the proposal position (total fees paid, £162,000+ and growing) is the ceiling TXN already holds in writing. A realistic landing zone is somewhere between (e.g. 100% of fees paid in the prior 12 months). Do not let the negotiation start from the proposal number without getting something for the movement.
2. **Expect the pushback trio:** (a) "your proposal said fees paid"; (b) UCTA reasonableness, a cap at ~30% of the contract value invites scrutiny if we ever had to rely on it; (c) DORA/EU FS procurement standards, regulated customers often have minimum-cap policies. None of these are fatal to an opening position; all are reasons to know the floor in advance.
3. **Trade, don't gift.** If TXN pushes the cap up, take something back: a service-credit regime instead of a higher cap (see the SLA brief), a longer initial support term, or faster payment terms.

## 11. Addendum (2026-07-06, second session): commercial decisions applied

Decisions taken by Brett St Clair and applied to the draft:

- **Entity: Novosapien only.** No Teraflow references, no novation of prior work. Sprint Zero stays in Schedule 1 solely as a completed, paid milestone. Novosapien's particulars (legal name, company number, registered office) and TXN's particulars are the only entity gaps left; TXN's details are being obtained.
- **Liability carve-outs confirmed:** confidentiality breach and wilful misconduct are uncapped (clause 9.4 unchanged on this point). The 9.4 flag now covers only the cap-level negotiation posture.
- **Hosting and infrastructure risk pushed out (new clauses 4.6 and 9.5).** The TXN Platform's hosting, infrastructure, and multi-tenancy architecture are managed by TXN or its other partners, never by Novosapien. Failures they cause: are not Novosapien's breach, trigger clause 4.2 relief, sit outside every service level and availability measurement (here and in the Support & SLA agreement), and generate no Novosapien liability, so they cannot erode the clause 9.4 cap. The mirroring SLA changes are in the SLA brief.
- **DORA designation remains open.** Brett is unsure whether TXN designates the agentic layer as supporting a critical or important function; the clause 4.4(e) mechanism handles either answer. Ask TXN directly; it also drives the support-tier choice.

- **IP settled: assignment (clause 6.3).** On full payment of the relevant SoW, Novosapien assigns the Foreground IP in the Deliverables to TXN with full title guarantee (including a present assignment of future rights and a further-assurance obligation at TXN's cost). Until full payment, TXN holds a licence for the purposes of the SoW. The Background IP embedded in the Deliverables is licensed to TXN as needed to use them; the delivery agents, Workforce products, and generic reuse rights are unaffected. Rationale: the exclusivity promise already given in 6.3 removed the commercial value of retaining ownership, and a regulated payments customer needs ownership for exit and continuity.

With that, every commercial decision in this Agreement is taken.

## 12. Addendum (2026-07-06, third session): entity details and DPA particulars

- **TXN inserted:** TXN Global Limited, Office 303, 20 Iacovou Patatsou, Egkomi, 2408 Nicosia, Cyprus. HE number awaited. Cyprus establishment locks the EU GDPR analysis: clause 8.2 and Schedule 3 now state the regime split (EU GDPR for TXN as controller, UK GDPR for Novosapien's UK processing) and rest EEA-to-UK transfers on the Commission's UK adequacy decision, with a counsel flag to confirm adequacy remains in force at signature.
- **Payment: on invoice date** (clause 7.4), decided by Brett.
- **Novosapien's particulars inserted** (supplied by Brett after the Co-Founder folder came up empty): Novosapien Global Ltd, company no. 17308181, Aldgate Tower, 2 Leman Street, London E1 8FA. In both contracts.
- **Schedule 3 (DPA) substantially completed:** subject matter/duration, data types, data subjects, regime, transfers, and deletion/return are now filled from the vault's data posture (no cardholder data, redaction if ever in scope). Per Brett (6 July 2026): AI model sub-processors are **Anthropic (Claude) and Google (Gemini)**; hosting infrastructure sits in **European regions** (hosting provider name still to insert); processing locations are the UK (Novosapien operations) and the EEA (hosting). The **security-measures row is under Brett's review** and must match the actual posture before signature.
- **Counsel point on model endpoints:** naming Anthropic and Google as sub-processors does not by itself keep data in Europe; Claude and Gemini API calls route to US infrastructure unless EU/regional endpoints are pinned in the architecture. The Schedule's transfer mechanisms (adequacy, SCCs/IDTA) cover a US leg legally, but the "infrastructure in Europe" commitment and TXN's residency expectations argue for pinning EU endpoints and saying so in the final data-flow map.

What remains before sending: TXN's HE number, the effective date, TXN's DORA designation, the hosting provider name, Brett's sign-off on the security-measures row, and solicitor sign-off.

## 13. Addendum (2026-07-07): counterparty review incorporated

A red-team review from TXN's perspective (`txn-counterparty-review.md`) was run on 6 July and its recommendations incorporated on Brett's instruction:

**Credibility fixes (Part 1 of the review):**
- **Schedule 3 rebuilt as a real DPA:** new Part A carries the eight Article 28(3) processor obligations (documented instructions, personnel confidentiality, Article 32 security, sub-processor flow-down with notice and objection, data-subject assistance, breach notice supporting the 72-hour window, return/deletion, audit); the particulars table is now Part B.
- **Definitions (1.1):** Confidential Information defined with the four standard exclusions; Business Day defined as a London banking day.
- **Acceptance end-state (5.2):** after [2] failed re-submissions of the same Deliverable, TXN may accept at an agreed price reduction or terminate the SoW as to that Deliverable with a refund of its charges.
- **IP indemnity (new 9.6):** Novosapien defends third-party UK/EU IP infringement claims against the Deliverables, standard exclusions, procure/modify/replace remedy, Novosapien controls the defence, capped separately at [2x the general cap; figure to decide].
- **Insurance (new 9.7):** PI and cyber cover at [£1m/£1m] placeholders. **Do not send until the actual policies are confirmed; never state cover not in place.**
- **Notices (11):** email notice added; Novosapien's notice address is info@novosapien.ai; TXN's notice email to insert; deemed received next Business Day.
- **No-training mechanics (6.6):** Novosapien commits to configuring sub-processors with zero-data-retention or equivalent no-training options where offered.

**Pre-emptive concessions (Part 2 items worth giving before they are asked):**
- **10.2:** Novosapien cannot terminate a SoW for convenience during its build phase.

**CEO-level additions (Part 4):**
- **Working in the open (new 3.5):** work product lands in TXN-accessible repositories as built, deployable and documented. This is the continuity answer for a three-person supplier and should defuse any escrow demand.
- **Governance (Schedule 1):** named engagement leads, weekly during build, monthly after, founder/director escalation.
- **Removed:** "(numbering in the thousands)" from 6.2.

**New decisions needed:** the 9.6 IP-indemnity cap figure, the 9.7 insurance figures (and confirming cover exists), the [2] failed-acceptance count, and TXN's notice email address. Negotiation postures on the general cap, credits, payment days, the 4.6 causation carve, and LCIA fallback remain as documented in `txn-counterparty-review.md`.

## 14. Addendum (2026-10-07): v0.3, rebased on the Phase Two proposal and Phase 1 completion

This section is the current statement of the commercials. Where anything earlier in this brief conflicts with it, this section governs.

### 14.1 Why the draft moved

v0.2 was written on 22 July 2026 against the Agentic Layer proposal of the same date. Three things have happened since, and the MSA had drifted from all three:

1. **Phase 1, the pilot, finished and was accepted.** It ran from 27 July 2026, TXN accepted it **in writing on 16 September 2026**, and it was deemed complete at the end of the week commencing 14 September. The handover position is recorded in the Phase 1 handover document dated 24 September 2026.
2. **The phases were renamed and renumbered** by Brett on 25 September 2026. **Phase 1 is the pilot** (complete). **Phase 2 is the next stage** at £90,312.50. **Phase 3 follows** at an indicative £108,375. The earlier "wire-in build" and "phase one" labels are withdrawn. v0.2 used the old names throughout.
3. **A Phase Two proposal was issued** (v1.0, 28 September 2026), which scopes Phase 2 as six named components, fixes a single dated milestone, states the alerting boundary, and expressly declines to commit Phase 3. v0.2 contradicted the last of those.

### 14.2 What changed in the document

| Clause / Schedule | v0.2 | v0.3 |
|---|---|---|
| 2.1 | Schedules 1 and 2 = SoW 2, "the wire-in build and Phase 3" | Schedules 1 and 2 = SoW 2, **Phase 2 only** |
| 2.1A | Pilot adopted as SoW 1, no dates, no acceptance recited | Phase 1 adopted as SoW 1, **accepted in writing 16 September 2026**, handover document referenced, acceptance expressly not reopened |
| 2.1B (new) | Not present | Records the **four pieces of work delivered alongside Phase 1 at no charge** (Control Center build, Agent Inbox and Alerts front end, the workflow slate build to thirteen procedures and 43 tools, the speed and usability programme to production 22 September). TXN owns them; **no charge is or becomes due**; they do not extend Phase 2 scope |
| 2.1C (new) | Not present | The **four TXN items that complete the Phase 1 transfer** (destination environment, repository destination and push access, named technical recipient, model and framework list approval), each a clause 4.1 dependency, and expressly **not a shortfall in Phase 1 or a condition of any charge** |
| 4.1A (new) | Not present | **The alerting boundary.** Novosapien builds the inbox. Detection, monitoring and thresholds stay with Direct Transact and the Stackworkz Console. Alerts arrive on an agreed feed, which is a clause 4.1 dependency. TXN wanting Novosapien to own detection is a further SoW with a separate charge |
| 7.1, 7.2 | "Wire-in build" £90,312.50, 22 July proposal | **Phase 2** £90,312.50, 28 September proposal. Adds the team-rate basis: TXN buys the team for the period, TXN sets the weekly order of work, **the charge does not move with the mix**. Adds that if the start date moves the window and invoice dates move and the amounts do not |
| 7.3 | **TXN committed** to a 3-month Phase 3 at £36,125/mo (£108,375); neither party could exit | **Phase 3 is not committed.** Scope, duration and charge agreed in the **final fortnight of Phase 2**, under a further signed SoW. £36,125/mo stated as the indicative basis only |
| 7.5 | Support "after launch", tier fee £4,250/mo | Support **commences at the end of Phase 2 (15 December 2026)**. No support fee before that date. Defect correction during Phase 2 is inside the Phase 2 charge |
| 10.2 | No convenience termination during "build phase" or the committed Phase 3 term | No convenience termination of **Phase 2 before 15 December 2026**. Phase 3 carries no notice restriction unless its SoW says so. Clause 4.4A DORA rights expressly preserved |
| Schedule 1 | Six generic deliverables; A2A endpoint inside the Agent Access Layer; "alert detection" inside Agent Inbox; timeline to "the October 2026 launch"; Phase 3 committed | **The six Phase 2 components**, named as in the proposal. New **"Explicitly not in Phase 2"** list. **Term 28 September to 15 December 2026** with the **15 October knowledge hub milestone** and the **8 October** opening of the wire-in and Co-pilot. TXN dependencies rewritten to the proposal's list. Team, AI consumption, and weekly flight plan / fortnightly demo reporting added |
| Schedule 2 | One payment table mixing Phase 2 and a committed Phase 3; "deliverable price allocation" presented as prices | Four tables, separated by what is actually committed: **Phase 2 only** is charged here; Sprint Zero and Phase 1 shown for completeness; the **£270,375 plan marked indicative and not a committed spend**; the component allocation marked **indicative, for clauses 5.2 and 5.3 only** |

### 14.3 Commercial position, as it now stands

| Stage | Status under this Agreement | Charge |
|---|---|---|
| Sprint Zero | Delivered and invoiced, outside this Agreement | £17,500.00 |
| Phase 1, the agentic pilot | Delivered, accepted 16 September 2026, charged under the Pilot Order | £54,187.50 |
| Phase 2, SoW 2 | **Committed.** 28 September to 15 December 2026 | £90,312.50 |
| Phase 3 | **Not committed.** Scoped in the final fortnight of Phase 2 | £108,375.00 indicative |
| Support and maintenance | Separate agreement, commences 16 December 2026 | £4,250 / mo |

**TXN's committed spend under this Agreement is £90,312.50.** The £270,375 figure is retained in Schedule 2 because it is the figure every proposal has carried and removing it would read as a change of plan, but it is now labelled as the indicative route to version one rather than as a commitment. Counsel on either side should read it that way.

### 14.4 The decisions behind v0.3, and who made them

- **Phase 3 decommitted. Brett, 7 October 2026.** v0.2's committed 3-month Phase 3 contradicted the Phase Two proposal Ian will read alongside this Agreement. A contradiction a counterparty's lawyer finds costs more than the commitment is worth. The commercial consequence is real and should be understood: Novosapien has given up a contractual claim to £108,375 and now has to earn Phase 3 on the evidence of Phase 2. That is consistent with Ian's own position on 9 September, that the next phase of spend depends on an honest assessment of delivered value.
- **Phase 2 start date 28 September 2026. Brett, 7 October 2026.** The proposal said 1 October. The MSA now recites 28 September, which is the date the team actually started. Note the arithmetic: 28 September to 15 December is marginally over two and a half months, and the three invoice tranches are unchanged at £36,125, £36,125 and £18,062.50. **Counsel point:** if TXN's finance team reconciles the dates against the tranches, the half-month tranche is covering slightly more than half a month. This is in TXN's favour and is not worth reopening, but it should not come as a surprise.
- **Support commences at the end of Phase 2. Brett, 7 October 2026.** v0.2 hung support off a "Launch Date" that was never defined and a Phase 3 retainer that no longer exists. Support now commences 16 December 2026, which is a date both parties can diarise. Carried into the Support & SLA Agreement at its clause 2.1 (now v0.2 of that document).
- **The alerting boundary is now contractual, not just commercial.** It is in the proposal and it is now in clauses 4.1A and Schedule 1 of the MSA and in Schedule 1 of the SLA. This is deliberate and it will surface a conversation: TXN's open question #68 records Michael saying on 25 August 2026 that Direct Transact has **no** alerting system and that he wanted the AI to be the central one. If TXN's expectation is that Novosapien owns detection, the right place to discover that is before Phase 2 runs, not after.

### 14.4A Schedule 3, the data processing appendix, rebased on the 6 October 2026 standup

This was not in the original brief for this pass, and it is the most important change in v0.3. On **6 October 2026** Dorte asked Brett whether a data processing agreement had ever been signed. The answer was no. Her words: *"I need to gather all of the facts and then we go to external counsel. But for that I really need to have everything watertight that I can explain everything."* She intends to go to counsel **once**. That makes Schedule 3 the part of this pack most likely to be read by a lawyer who is not Novosapien's, and it had a false premise in it.

**The false premise.** v0.2's Schedule 3 opened by stating that the AI model services *"are engaged on TXN's own provider accounts; those providers are TXN's processors, not Novosapien's sub-processors"*. That is the **target** operating model. It is not the current one. On the same call Dorte said *"all of the LLMs are via your contracts"* and Brett confirmed: *"Correct."* The models run on **Novosapien's** accounts today.

**Why that mattered.** If the model providers run on Novosapien's accounts, they are Novosapien's **sub-processors** under Article 28, and every Part A obligation attaches to them: written flow-down, full responsibility for their performance, notice of change, and TXN's right to object. v0.2 disclaimed all of that on a factual basis that was wrong. A competent reviewer on TXN's side would have found it, and finding it in a document Novosapien drafted is worse than Novosapien raising it.

**What v0.3 does instead.** Schedule 3 now states **two operating models** and which one applies:

- **The current model (during Phase 2).** Models run on Novosapien's accounts. Those providers **are** Novosapien's sub-processors, are named in Part B, and Part A applies to them in full.
- **The target model.** On a date the parties confirm **in writing**, the accounts transfer to TXN and the providers become TXN's processors. Novosapien supplies the information TXN needs to make that appointment.
- A backstop sentence: until that transfer is confirmed in writing, the current model applies, and **nothing elsewhere in the Agreement about model usage running on TXN's accounts displaces it**. That is there because Schedule 1's AI-consumption paragraph and the Phase Two proposal both describe the target model, and a reader should not be able to use either to argue the point.

**The sub-processor list now names three providers, not two.** v0.2 named Anthropic and Google. The architecture has a third. George described the fallback chain on 29 September as Google, then Anthropic, then **OpenAI**, and confirmed on 1 October that the live model is Gemini 3.8 Flash through GCP. Part B now lists Google as primary, Anthropic as first failover and **OpenAI as second failover**, and Part A(d) carries a new sentence: **a provider used only as a failover is still a sub-processor**. Omitting OpenAI because it only appears when two other providers are down would have been the kind of omission that costs credibility in a single question.

**Hosting is named, because it is now settled.** Michael confirmed on 6 October that the AI layer gets *"another node for any central AI layer... alongside the API in that same sort of European Azure stack"*, inside Direct Transact's PCI-covered environment, and that it is already built. Part B carries a **Hosting** row saying exactly that, the processing-locations row now reads **European Union and United Kingdom** rather than deferring to TXN's configuration, and Part C's opening paragraph matches. The hosting-provider name that was a `[placeholder]` in earlier briefs is resolved.

**Two commitments that were engineering notes are now contractual.** EU or regional **endpoint pinning** and **zero-data-retention or no-training options** were previously a counsel note in the brief and an aspiration in the text. The international-transfers row now obliges Novosapien to pin them while the providers run on its accounts, and to **tell TXN before routing TXN personal data to any provider that offers no European endpoint**. Novosapien should be clear-eyed that this is a real obligation it now has to meet in the architecture, not a drafting flourish.

**The PCI point, raised rather than buried.** The AI node sits inside Direct Transact's PCI-covered environment. Schedule 3 says expressly that this does not change clause 4.5 (Novosapien does not store, process or transmit cardholder data, and cardholder data stays out of model context) and does not make Novosapien responsible for TXN's or Direct Transact's PCI-DSS compliance (clause 4.3). Counsel should confirm that framing is acceptable to TXN's compliance function, because a supplier operating inside a PCI environment is a question an auditor will ask.

**One genuine open item is now written down rather than left out.** George raised on 6 October that the agents write conversation history and execution traces to a datastore, and that its location is undecided. Part B carries a **Conversation history and traces** row recording that the location is to be confirmed in writing, that the intention is the same European Azure environment, and that in the meantime Novosapien will not write TXN personal data outside that environment and strips sensitive data before writing. **Counsel point:** this is an honest placeholder rather than a resolved position, and it should be closed before the pack goes to Dorte's external counsel, because an undecided storage location is exactly the thing she will be asked about.

**Carried into the SLA.** Schedule 4 of the Support & SLA Agreement mirrors all of the above, with a line saying the position confirmed under the MSA carries over so the parties do not have to confirm it twice.

### 14.4B The licensing handover, and why the data position has two stages rather than one

Added on Brett's instruction, 7 October 2026, after the first pass of 14.4A. It sharpens a trigger that was too vague to rely on.

**The operational fact.** Novosapien builds all the code and the environments, and runs dev and user-acceptance testing, **on its own models under its own licences**. That is deliberate: waiting for TXN to contract with Google, Anthropic and OpenAI before anyone can test would hold the build up for no benefit. **Once the Deliverables move into TXN's production environment, the processing and the AI model licensing hand over to TXN**, and from then on the layer runs on TXN's LLM contracts rather than Novosapien's.

**Why the first draft was not good enough.** 14.4A described two operating models separated by "a date the parties confirm in writing". That is a trigger with no content: it describes the paperwork without naming the event. A reviewer would reasonably ask what causes the confirmation, and neither party had an answer in the document.

**What v0.3 does now.**

- **New clause 1.2** defines four terms: **Non-Production Environment**, **TXN Production Environment** (the dedicated agentic AI layer node in TXN's European Azure environment managed by Direct Transact, rendering into the Stackworkz-provided Console and Developer Portal surfaces), **AI Model Services**, and **Production Cutover** (the date a Deliverable first operates in the TXN Production Environment, confirmed in writing by both parties).
- **New clause 3.7** carries the handover itself: before cutover Novosapien licenses and runs the models on its own accounts at its own cost; at cutover TXN takes over licensing, contracting and consumption on its own accounts; and the data-protection consequence of each stage points to Schedule 3.
- **Schedule 3** now presents the position as a **two-stage table**: where the Deliverables run, whose accounts the models run on, the status of the providers, who covers the transfer mechanism, and what Novosapien still processes, in each stage.

**Four drafting points a reviewer will test, and the answers.**

1. **Production Cutover is per Deliverable, not per engagement.** Phase 2 moves components across at different times; the wire-in and the knowledge hub will not cut over on the same day. Clause 1.2 says so, and clause 3.7(d) adds that a Deliverable which is partly live is treated as **before** cutover until the whole thing has moved. That resolves in favour of the stricter obligations, which is the right default.
2. **The handover is a two-sided obligation with a lead time.** Clause 3.7(c) requires Novosapien to give TXN, **20 Business Days before a planned cutover**, the list of models and fallbacks, the configuration it has been running (including regional endpoints and any zero-data-retention settings), and an expected-consumption estimate. TXN puts its accounts and credentials in place before the date. Without that lead time the handover becomes a scramble on the day.
3. **What happens if TXN's accounts are not ready.** Clause 3.7(c) says Novosapien keeps running on its own accounts if TXN asks in writing, the transitional period counts as pre-cutover for Schedule 3, and **Novosapien may recharge the model consumption at billed cost after telling TXN it intends to**. Novosapien should be comfortable with this: absorbing an open-ended production model bill because a counterparty's procurement was slow is a real commercial exposure, and this is the clause that closes it. It is also fair, because it only bites after notice.
4. **Data minimisation before cutover.** A new paragraph in Schedule 3 commits Novosapien to using synthetic or test data in preference to TXN personal data in Non-Production Environments, and not to use TXN personal data there except on TXN's instruction or where diagnosing a defect genuinely requires it. **This is the paragraph that answers Dorte's actual worry.** Her concern on 6 October was <em>"the LLM sends something to the US"</em>. If TXN personal data largely does not reach Novosapien's model accounts in the first place, the pre-cutover exposure is small, and the clause says so without overclaiming.

**One thing to confirm before this goes out.** Clause 3.7's data-minimisation commitment is drafted as a preference rather than an absolute. **If Phase 2 dev and UAT in fact run on synthetic data only, as the Pilot Order did, that should be stated as a flat prohibition instead**, which is both stronger for TXN and easier for Dorte to put in front of counsel. It is drafted as a preference because the vault does not record a Phase 2 decision on the point, and a flat prohibition that the team then breaches in a defect investigation is worse than an honest preference. **Confirm the Phase 2 test-data position and tighten the clause if it is synthetic-only.**

**A naming point, raised not buried.** Brett described the destination as the Stackworkz environment. Michael described it on 6 October as a dedicated node in Direct Transact's European Azure stack, alongside the Core API. The definition in clause 1.2 names the Azure environment as the production location and Stackworkz as the provider of the Console and Developer Portal surfaces the layer renders into, which covers both descriptions. If the destination is in fact a Stackworkz-operated environment rather than a DT-operated one, the definition needs one word changed, and Schedule 3's hosting row with it.

### 14.5 Open points for counsel, refreshed

Still open from earlier sections, and still blocking execution:

1. **TXN's Cyprus HE number** and the **effective date** are blank write-in lines.
2. **TXN's DORA designation** (clause 4.4B) is unconfirmed. If the Services support a critical or important function, clause 4.4B's obligations switch on automatically, including unrestricted audit rights and a maintained exit strategy with a 6-month transition.
3. **Insurance figures** (clause 9.7, £1m PI and £1m cyber) must match policies actually in force. Do not send otherwise.
4. **The IP indemnity cap** (clause 9.6) is drafted as capped separately at the SoW charges; the earlier intention was a 2x multiple. Confirm which.
5. **Schedule 3 security measures** need Brett's sign-off against the actual posture. The **hosting provider name is now resolved** (see 14.4A): a dedicated node in TXN's European Microsoft Azure environment, managed by Direct Transact.
6. **The EEA-to-UK transfer position** rests on the Commission's UK adequacy decision; confirm it is in force at signature.
7. **TXN's notice email address** is still to insert.

New with v0.3:

8. **The Phase 2 test-data position.** Confirm whether dev and UAT run on synthetic data only. If they do, tighten the Schedule 3 data-minimisation paragraph from a preference to a prohibition (see 14.4B).
9. **Phase 2 has already started.** The MSA recites a commencement date of 28 September 2026, which is before signature. Clause 2.1 says SoW 2 takes effect on signature. Counsel should confirm whether the parties want the Agreement to operate retrospectively from 28 September, which is the commercial reality, or whether a short recital should say so expressly. As drafted the position is workable but it is the kind of thing a careful reviewer will raise.
10. **The Phase Two proposal's status.** As at the last vault record (28 September 2026) it was with Brett for review and had not been sent to Ian. If it has since been issued and countersigned, this MSA should recite it. If it has not, the parties are signing an MSA whose SoW 2 scope has not been separately accepted. **Confirm before sending.**
11. **The 10 per cent pass-through administration fee** quoted by Brett on 4 September 2026 for the Outbound Workforce domains has never been put to TXN in writing, and it is unresolved whether 10 per cent is the general pass-through rate or specific to the domains. It is not in this Agreement. It belongs in the Workforce Order under clause 2.3 and should be settled before it is quoted again.
12. **The data processing appendix is the live commercial issue, not a background one.** There is no signed DPA, the MSA is not in play, and the current phase has only a proposal with no appendix (vault open question #103). Dorte has asked for the pack and intends one trip to external counsel. The drafting has been substantially complete since July and v0.3 has now corrected its premise, named the third model provider and resolved hosting. **What is missing is signature and an appendix for Phase 2, not drafting.** The practical sequence: close the conversation-history storage question, get Brett's sign-off on the Part C security row, then send the MSA, the SLA and both briefs as one pack.
13. **The GTM Workforces order is still unsigned** and still carries voice-calling obligations at its clause 8.2 and an ElevenLabs usage pass-through, both of which are now out of scope (Ian ruled out AI voice, inbound and outbound, on 24 August 2026). That document was not updated in this pass. It should be corrected before signature.

### 14.6 What this draft is still not

A competent first draft, now accurate to the delivery record and the latest proposal. **Not final legal advice.** It needs a qualified solicitor's review before execution, particularly on the DORA provisions, the IP assignment formalities, and the data-transfer position. The commercial positions in it are Novosapien's and have been taken deliberately; the legal mechanics have not been reviewed by a practising solicitor.
