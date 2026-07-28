# Reviewer Brief: Master Service Agreement (Novosapien x TXN)

**Prepared by:** Novosapien commercial-lawyer skill (dry run) · **Date:** 2026-07-03, updated 2026-07-22 · **Draft version:** v0.2
**Instrument:** Master Service Agreement + Statement of Work 2 (Agentic AI Layer); the pilot is the adopted Statement of Work 1
**Parties:** Novosapien and TXN
**Governing law:** England and Wales

> **CHANGELOG — 2026-07-22 (pilot separation).** The six-week pilot has been carved out into a standalone **Pilot Order** (see `txn-agentic-pilot-order.html` + its reviewer brief) so TXN's CEO could authorise it before going on leave, ahead of signing this MSA. This MSA is edited to match:
> - New **clause 2.1A** adopts the pilot, delivered under the Pilot Order, as the **completed Statement of Work 1** on MSA signature (its Deliverables and already-assigned Foreground IP become Deliverables/Foreground IP here; no further charge; nothing rebuilt).
> - The wider engagement (wire-in build + Phase 3) is now **Statement of Work 2** (Schedules 1 and 2); Schedule 1 heading and clause 2.1 updated.
> - **Clause 7.2** repriced: build £144,500 (4 months) → **wire-in £90,312.50** (~2.5 months); new note that the pilot (£54,187.50) was charged under the Pilot Order and is not re-charged. Clause 7.1 now cites the **22 July 2026 proposal (v1.2)**.
> - **Schedule 2** payment schedule and deliverable allocation rebuilt to the wire-in figures, with Sprint Zero and Pilot shown as reference rows. Month numbering "months 5 to 7" → "November to January".
> - **Total committed engagement unchanged at £270,375** (Sprint Zero £17,500 + Pilot £54,187.50 + wire-in £90,312.50 + Phase 3 £108,375). Support £4,250/mo after Phase 3, unchanged.
> - IP position is unchanged in substance: clause 6.3's present assignment now flows to the pilot via the Pilot Order (which lifts the same language) and the clause 2.1A adoption.
>
> Persona reviews below predate this change; re-check the charges and SoW-numbering sections against the current draft.

## 1. What this is and what it is not

A competent **first draft**, generated from Novosapien's standard house paper, with scope grounded in the TXN product vault (`txn-vault/content/**`) and commercials grounded in the latest proposal (`proposals/txn-agentic-layer-proposal_final.pdf`, v1.0, 17 June 2026). It is **not final legal advice** and needs a qualified solicitor's review before execution, particularly in a regulated payments context. This brief lists the positions, assumptions, negotiables, and open points so review is fast.

## 2. The deal in one paragraph

Novosapien builds the **agentic AI layer** across TXN's three surfaces (Core API, Console, Developer Portal) and its internal ops, delivered by a full-time team of three, bought by the month. Build phase is £144,500 over four months to the October 2026 launch (following a completed Sprint Zero), then an optional monthly retainer of £36,125 for Phase 3, plus £4,250/month managed support. TXN's platform is built by other partners (Direct Transact, Stackworkz, Super Ultra); Novosapien delivers the AI layer only.

## 3. Key positions taken (and why)

| Clause | Position taken | Rationale / source |
|--------|----------------|--------------------|
| Structure | MSA framework + SoW per engagement | Repeat/phased work (pilot → wire-in → Phase 3 menu); keeps legal terms stable |
| Charges (7.2-7.5) | £144,500 in 4 tranches of £36,125; retainer £36,125/mo; support £4,250/mo | Directly from the proposal's payment schedule and commercial terms |
| Late payment (7.4) | 4% above BoE base rate | Proposal (note: this is *below* the statutory 8%-above-base default under the Late Payment Act; it is a concession to TXN) |
| Liability cap (9.4) | Total charges paid; carve-outs for confidentiality breach + wilful misconduct (plus the statutory carve-outs) | Proposal ("capped at total fees paid; no indirect or consequential damages, except confidentiality or wilful misconduct") |
| Termination (10.2-10.3) | 30 days' notice; handover deployable + documented | Proposal |
| AI output (3.3-3.4) | Advise-not-decide; no accuracy warranty; approvals + permission model respected; no fraud auto-execution | Vault §6 non-negotiables + trust concepts |
| IP (6) | Three-way split: (6.2) Novosapien's delivery agents = Background IP, a build cost, excluded from what TXN gets; (6.3) the agents/AI/data built for the TXN platform = Deliverables, **exclusive to TXN and assigned to TXN on full payment** (full title guarantee, present assignment of future rights, embedded Background IP licensed as needed to use the Deliverables); (6.4) Novosapien's Content / Inbound / Outbound / Deal Lab Workforce products = **excluded**, available later only under a separate monthly consumption licence | Protects Novosapien's tooling and productised workforces while giving TXN clean ownership of its build. Assignment decided 6 July 2026: the 6.3 exclusivity promise had already removed the resale value of retaining ownership, and a regulated payments customer would demand ownership for exit/continuity anyway |
| Compliance (4.3) | TXN owns all compliance frameworks; Novosapien builds to respect them | Vault §6 + proposal warranties (PCI-DSS, GDPR, FCA) |
| Data (6.4, 8.2, Sch 3) | Novosapien = processor; Art 28 schedule; no training on TXN/client data; cardholder PII limited/redacted; UK/EU residency | Vault §6 (#16: limit + redact + EU residency) + ai-software-clauses |

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
- **Cardholder PII into LLM context** is a live risk (vault §8). Schedule 3 limits and redacts; confirm the data-residency mechanism if any personal data leaves the UK (model/hosting providers as sub-processors).
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
