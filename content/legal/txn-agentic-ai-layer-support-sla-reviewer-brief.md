---
description: "Reviewer brief for the Novosapien x TXN Support & SLA Agreement v0.2: tier selection, service-level targets, liability anchoring, and open points for counsel"
---

# Reviewer Brief: Support & SLA Agreement (Novosapien x TXN)

**Prepared by:** Novosapien commercial-lawyer skill · **Date:** 2026-07-05, updated 2026-10-07 · **Draft version:** v0.2
**Instrument:** Support & Service Level Agreement (standalone; sits under the MSA)
**Parties:** Novosapien and TXN
**Governing law:** England and Wales

> **CHANGELOG, 2026-10-07 (v0.2).** Commencement no longer hangs off an undefined Launch Date, and Schedule 1 is rebuilt to what Phase 1 and Phase 2 actually deliver. Read section 15 first.

## 1. What this is and what it is not

A competent **first draft** of the managed support and maintenance agreement for the agentic AI layer, for after launch. Scope is grounded in the TXN product vault; commercials are grounded in the proposal (`proposals/txn-agentic-layer-proposal_final.pdf`, section D, 17 June 2026). It is **not final legal advice** and needs a qualified solicitor's review before execution. Service-level targets marked `[placeholder]` are genuinely open: the proposal fixes the fee and what it covers, but not the priority targets, availability figure, or credit regime.

## 2. The deal in one paragraph

Novosapien runs, monitors, and maintains the agentic AI layer it built for TXN, as a **managed service** (not break-fix), for £4,250/month. The fee covers proactive run-and-monitor via the Agent Ops platform, up to **20 hours/month** of support and continuous improvement (prompt tuning, guardrail adjustments, small enhancements), and incident response to defined targets. Anything beyond that is a change request at standard day rates.

## 3. Key positions taken (and why)

| Clause | Position taken | Source |
|--------|----------------|--------|
| Fee (2.2) | £4,250/month in advance, ex-VAT; review at anniversary | Proposal section D (indicative annual £51,000) |
| Cover (3.1-3.3) | Run & monitor + keep-healthy + 20 hrs/month allocation | Proposal ("what the fee covers") |
| Change requests (3.5) | Beyond the allocation, charged at day rates (£950/£850/£750) | Proposal sections 9 and D |
| Late payment (2.2) | 4% above BoE base rate | Proposal (consistent with the MSA) |
| Liability (9.2) | Cap = total charges paid under this Agreement; carve-outs for confidentiality + wilful misconduct; no indirect loss | Proposal + consistent with the MSA |
| Termination (9.3) | 30 days' notice; transition assistance at day rates | Proposal |
| AI output (8.1-8.2) | Degraded output = an Incident; no accuracy warranty; model-provider failures excluded | Vault non-negotiables + ai-software-clauses |
| Model / partner dependency (7, 8.2) | Failures of third-party model providers, hosting, and other TXN partners are excluded from the SLA | Vault (multi-vendor build; advise-not-decide) |

## 4. Assumptions made (confirm before execution)

- Both parties' legal entity details are placeholders; the post-buyout contracting entity should match the MSA.
- The Agreement sits under, and is defined by reference to, the MSA (Supported System = the MSA Deliverables).
- Start date is the end of the build phase / after the Phase 3 retainer, per the proposal's "after the retainer" framing: **confirm the exact commencement trigger.**
- Service Hours assumed UK business hours: confirm whether TXN needs extended or 24/7 cover for P1 (payments context may warrant it).

## 5. Open points / decisions needed

- **Service-level targets (Schedule 2).** Priority response/resolution times, the availability percentage, and how availability is measured are placeholders. These are the core of an SLA and need TXN agreement. The payments context and the "advise-not-decide" design should shape what counts as P1 (total unavailability) vs P2 (degraded output).
- **Service credits (6.2, Schedule 2).** The proposal does not include a credit regime. Decide whether to offer credits at all for a £4,250 managed service, and if so, the levels and the cap. Credits as sole financial remedy is the standard protective position.
- **Availability carve-out for model providers.** Because the layer depends on third-party model providers whose uptime Novosapien does not control, the availability target should apply only to the parts within Novosapien's control (drafted that way in 4.1): confirm TXN accepts this.
- **Hours roll-over (3.3).** Drafted as no roll-over; confirm.
- **Initial term (2.1).** Drafted as 12 months then rolling monthly on 30 days' notice; the proposal says "no minimum term" for the retainer but is silent on the support term: confirm which applies here.

## 6. Risks and things to watch

- **Unbounded support scope.** The 20-hour allocation plus "small enhancements" can be stretched. The change-request gate (3.5) is the control; make sure "small enhancement" vs "change request" is applied in practice.
- **Payments-grade expectations.** TXN may expect faster P1 targets or out-of-hours cover than a standard business-hours SLA. Price and staff any uplift; do not agree tight targets the team cannot meet.
- **Dependency on TXN's changing API/docs.** The fee assumes a reasonable rate of change; a major Core API overhaul is a change request, not covered maintenance. Worth stating explicitly if the risk is real.

## 7. Open questions for counsel

1. Commencement trigger and initial term (end of build vs a fixed date; 12-month term vs no minimum)?
2. Confirm the P1-P4 targets, the availability figure and its measurement, and whether service credits apply and at what levels/cap?
3. Does TXN need out-of-hours / 24-7 cover for P1 given the payments context, and is the fee adjusted for it?
4. Is the availability carve-out for third-party model-provider and partner failures acceptable to TXN?
5. Should the liability cap be the fees paid under this Agreement, or aggregated with the MSA cap?

## 8. What is grounded vs assumed

- **Grounded in the proposal:** the £4,250/month fee, the run-and-monitor cover, the 20-hour allocation, change requests at the stated day rates, the late-payment rate, and the liability/termination posture.
- **Grounded in the vault:** the Supported System components, the advise-not-decide model, and the multi-vendor dependency exclusions.
- **Assumed / to confirm:** entity details, commencement and term, all service-level targets, the service-credit regime, out-of-hours cover, and roll-over.

## 9. Addendum (2026-07-06): support tiers and European regulatory review

**Tier structure added.** Schedule 2 is rebuilt around three selectable Support Tiers (no pricing yet, per instruction; tier charges go in Schedule 3 when agreed):

| | Business Hours | Extended | Mission Critical |
|---|---|---|---|
| Human cover | Mon-Fri 09:00-18:00, Business Days | 7 days 08:00-20:00, incl. weekends and holidays | 24/7/365 for P1/P2; 7 days 08:00-20:00 for P3/P4 |
| Availability | 99.5%/mo | 99.7%/mo | 99.9%/mo |
| P1 response / resolution | 2 SH / 8 SH | 1 SH / 6 SH | 30 min / 4 hrs (clock hours) |
| Escalation | Named contact | Duty engineer rota | On-call rota + escalation manager + wake-up channel |
| P1 comms | Each business day | Every 4 SH | Every 60 min |
| Reviews | Monthly report | + quarterly review | + monthly review + P1 post-incident reports |
| Credit cap | 15%/mo | 20%/mo | 30%/mo |

Automated monitoring runs 24/7 at every tier; the tier decides when humans respond. Out-of-hours P1 on the lower tiers is reasonable-endeavours only. Tier changes on 30 days' notice; chronic-failure termination at 3 consecutive missed months (2 at Mission Critical). House defaults live in the skill reference `sla-tiers.md`.

**Decisions needed on tiers:**
1. Which tier does the £4,250/month fee buy? The proposal predates the tier structure; the draft assumes Business Hours. If TXN's launch needs Extended or Mission Critical, price it separately.
2. **DORA drives the tier.** If TXN designates the agentic layer as supporting a critical or important function, Mission Critical is the defensible tier and full SLAs with quantitative targets are mandatory contract content (DORA Art 30(3)). Get the designation in writing either way.
3. Timezone (UK vs CET) and public-holiday calendar for the Service Hours definitions.
4. Do not sign Mission Critical wording before the on-call rota and wake-up channel actually exist; if needed, sell Extended now with a committed Mission Critical date.

**Regulatory changes made to the draft:**
- Clause 8.3 added: breach/security-incident notification without undue delay (feeding TXN's 72-hour GDPR clock) and assistance with TXN's DORA major-incident reporting.
- Clause 9.1 and Schedule 4 upgraded to dual-regime (EU GDPR + UK GDPR) with EU SCCs / UK IDTA transfer mechanics.
- Clause 3.7 added service reporting and reviews (monthly report; quarterly/monthly reviews by tier; P1 post-incident reports at Mission Critical), which also serves the DORA monitoring-and-reporting expectation.

## 10. Addendum (2026-07-06): agentic incident response (clause 3.2)

New clause 3.2 contracts the self-healing flow: monitoring agents observe error logs and telemetry 24/7 at every tier; on error, an agent first attempts automated remediation (known fix or rollback) within its authorised scope and without bypassing the MSA's approval/permission model; if unresolved, it escalates to a human via the shared messaging channel with a provisional auto-graded Priority and full diagnostics (error, affected components, remediation attempted, suspected cause). Humans can re-grade the Priority; automated remediations and escalations appear in the monthly service report.

**Points for counsel and the team:**
1. **Clock start (3.2(c)):** response targets run from the escalation notification (or TXN's report if earlier), not from the underlying error. This is deliberate and fair: it gives the agents room to self-heal without burning SLA time, but confirm TXN accepts it, as a strict customer might want the clock from detection.
2. **Authorised scope of automated remediation:** rollbacks are self-limiting, but "applying a known fix" must stay inside the agent-permission model. The clause says so; make sure the technical guardrails match the words.
3. **Shared messaging channel** is a placeholder: name it (shared Slack/Teams channel) and ensure both parties actually staff it, since escalation notices land there.
4. Vault note: self-healing of *code* in TXN's own repos is off the table (open question #47, DT owns the codebase); this clause covers the Supported System (the agentic layer) only, which is consistent.

## 11. Addendum (2026-07-06): service credits removed; liability anchored at 30% of implementation fee

**Supersedes the credit-regime content in sections 5, 6, and 9 above.** On instruction, the remedies architecture changed:

- **No service credits.** Clause 6 is now "Service performance": targets are monitored and reported monthly (clause 3.7); a missed month is not of itself material breach; TXN's protections are transparency, the chronic-failure termination right (3 consecutive missed months, 2 at Mission Critical), and the liability regime. The per-tier credit tables are gone from Schedule 2.
- **Liability cap (clause 9.2)** is now **30% of the total implementation fee under the MSA (£43,350)**, mirroring MSA clause 9.4, as a deliberate negotiation anchor. The proposal said "capped at total fees paid"; see the MSA brief section 10 for the negotiation posture and floor.
- **Concession path (agreed strategy):** if TXN insists on credits, concede a **capped, sole-remedy credit regime** (the shelved scaffold: credits on missed availability or P1/P2 resolution, monthly caps 15/20/30% by tier) **instead of raising the liability cap**. Credits are the cheaper concession: bounded, automatic, and they extinguish damages claims for the same miss.
- **Watch-point for counsel:** with no credits AND a low cap AND "missed month is not itself breach", TXN's lawyer may argue the SLA has no teeth. The honest answers: the chronic-failure termination right is real, the monthly reporting is contractual, and the credit regime is available in negotiation. If TXN is DORA-regulated and designates the layer critical/important, expect regulator-driven pressure for quantitative remedies; the concession path covers that.

## 12. Addendum (2026-07-06, second session): targets settled

Decisions taken by Brett St Clair and applied to the draft:

- **Timezone: UK.** Service Hours in Schedule 2 run on UK time; public holidays follow the England & Wales calendar.
- **Commencement: the Launch Date** (clause 2.1). The Agreement starts on the day the agentic AI layer is officially deemed launched under the MSA, confirmed in writing by the parties. The initial term (drafted 12 months) runs from that date.
- **Support Channels: a shared Slack channel plus a Novosapien support email address** (clause 3.2(b)); used for agent escalations, TXN incident reports, and incident response. The specific email address is the remaining placeholder.
- **Governing law: England and Wales, exclusive jurisdiction** (clause 9.4), matching the MSA.
- **Liability carve-outs confirmed:** confidentiality and wilful misconduct stay uncapped (clause 9.2).
- **Third-party hosting and infrastructure excluded outright (clauses 7.1-7.3, 9.2).** The TXN Platform's hosting, infrastructure, and multi-tenancy architecture are managed by TXN or its other partners (MSA clause 4.6). Failures they cause are not Novosapien Incidents; response, resolution, and Availability targets do not apply; the downtime is excluded from Availability measurement and chronic failure; and Novosapien has no liability for them, so they cannot erode the cap.

**Still open:** which Support Tier the £4,250 fee buys (draft assumes Business Hours); TXN's DORA designation (drives the tier); both parties' entity particulars (TXN's awaited); the support email address; and confirmation of the response/resolution matrix against the actual on-call rota before signature.

## 13. Addendum (2026-07-06, third session): entity details and DPA particulars

- **Both parties inserted.** TXN Global Limited, Office 303, 20 Iacovou Patatsou, Egkomi, 2408 Nicosia, Cyprus (HE number awaited). Novosapien Global Ltd, company no. 17308181, Aldgate Tower, 2 Leman Street, London E1 8FA.
- **Support email fixed: support@novosapien.ai** (clause 3.2(b)); the Support Channels are now fully defined.
- **Tier pricing deliberately omitted** on instruction: clause 2.2 states that Extended and Mission Critical are not priced in this Agreement and must be priced into Schedule 3 before selection. The open question is which tier the £4,250 buys (draft assumes Business Hours).
- **Schedule 4 (DPA) substantially completed**, mirroring MSA Schedule 3: data types, regime (EU GDPR for TXN as a Cyprus-established controller; UK GDPR for Novosapien's UK processing), EEA-to-UK transfers on the UK adequacy decision, and deletion/return on termination. Per Brett (6 July 2026): AI model sub-processors are **Anthropic (Claude) and Google (Gemini)**, hosting in **European regions** (provider name to insert, matching the MSA), and the **security-measures row is under Brett's review**. See the MSA brief on pinning EU model endpoints so the Europe commitment holds in practice.

## 14. Addendum (2026-07-07): counterparty review incorporated

Recommendations from the TXN-side red-team review (`txn-counterparty-review.md`) applied on Brett's instruction:

- **Schedule 4 rebuilt as a real DPA:** new Part A carries the eight Article 28(3) processor obligations, wired to clause 8.3 (breach notice) and clause 9.3 (return/deletion); the particulars table is now Part B.
- **Business Day defined** (clause 1.1) as a London banking day, so every response and resolution clock has one calendar.
- **Support Allocation disambiguated (3.4):** incident response to the Schedule 2 targets is part of the managed service and does not consume the 20 hours; the allocation covers keep-healthy and continuous improvement (3.1, 3.3); persistent incident patterns go to service reviews, not hourly billing. This resolves the ambiguity both sides would have tripped on.
- **Fee review capped (2.2):** annual increases limited to UK CPI plus [3]% (pre-empting the inevitable redline on an uncapped review right).
- **Notices and insurance (9.4):** email notice added (Novosapien: info@novosapien.ai; TXN's notice email to insert; deemed received next Business Day), and Novosapien commits to maintaining the MSA insurance for this Agreement's term.

**New decisions needed:** confirm the CPI+[3]% figure and TXN's notice email. Negotiation postures (credits concession path, chronic-failure trigger, Extended-tier pricing) remain as documented.

## 15. Addendum (2026-10-07): v0.2, commencement fixed and the Supported System rebuilt

### 15.1 Commencement: the Launch Date is gone

v0.1 started this Agreement on a **"Launch Date"**, defined as the day the agentic AI layer was "officially deemed launched under the Master Service Agreement, as confirmed in writing by the parties". Two problems with that, both now fixed:

1. **It was never going to be confirmed.** TXN's own launch sequencing has moved repeatedly (Dorte, 18 August 2026: pre-launch September, full launch October or November), and nothing in the MSA obliged either party to declare a launch date. A support agreement that cannot start is not a support agreement.
2. **It was coupled to a Phase 3 retainer that no longer exists.** v0.1's clause 2.1 said the support fee began "only when the Phase 3 team retainer under the Master Service Agreement ends". The MSA's committed Phase 3 retainer was removed on 7 October 2026 (MSA v0.3, clause 7.3). That made the trigger circular.

**New position, per Brett on 7 October 2026.** Clause 2.1: the **Commencement Date** is the day after Phase 2 under the MSA ends, being **16 December 2026**. If the Phase 2 window moves under MSA clause 7.2, the Commencement Date moves with it and the parties confirm it in writing. The 12-month initial term runs from that date.

New clause 2.1A states three things that follow:

- **No support fee before the Commencement Date.** During Phase 2, defect correction is inside the Phase 2 charge under the MSA, and no separate support fee is due. The same statement is in MSA clause 7.5 and Schedule 2, so the two documents agree.
- **If a Phase 3 retainer is later agreed** and runs past the Commencement Date, that retainer's monthly charge covers support for the months it runs, and no separate support fee is payable for those months. This preserves the original no-double-charging intent without depending on Phase 3 existing.
- **Support is not conditional on launch.** Stated expressly, so the Launch Date problem cannot return.

### 15.2 Schedule 1, the Supported System, rebuilt

v0.1's Schedule 1 listed the Agentic Layer proposal's full component set, written before anything was built. It included things Phase 2 is not building. Schedule 1 now lists what Phase 1 and Phase 2 actually deliver: the Agent Access Layer as wired to the live Core API, the Knowledge Hub, Co-pilot v1, Agent Inbox and Alerts v1, the Full Agentic Experience as wired to live data, and the Internal Ops agents (customer onboarding, knowledge engine, meeting capture).

A new **"Not in the Supported System"** paragraph names what is excluded until delivered under a later SoW and added by written agreement: the **A2A endpoint**, **Fraud & Risk Assist**, **Reconciliation**, and **authenticated developer features**. v0.1 had the A2A endpoint inside the supported Agent Access Layer and excluded only Fraud & Risk and Reconciliation. Supporting an endpoint nobody has built is not a position worth holding.

### 15.3 Detection and alerting are excluded, and that matters

A new paragraph in Schedule 1 states that Novosapien supports the **Agent Inbox**, being the surface that receives an alert, explains it, proposes an action and executes it on approval. **Detection, monitoring and thresholds sit with Direct Transact and the Stackworkz Console.** A failure of those systems, or of the feed that carries alerts into the Agent Inbox, is **not an Incident** and is excluded from every service level, availability measurement and response or resolution target.

This mirrors MSA clause 4.1A and the Phase Two proposal. It is deliberate and it is the single most important exclusion in this document, because it is the one most likely to be tested in a real incident: an alert that should have fired and did not is a detection failure, not an inbox failure, and the paper now says so.

**Counsel point, stated plainly.** Novosapien's own automated monitoring of the agent fleet under clauses 1.2 and 3.1 is unaffected and still runs 24/7 at every tier. A reviewer should be able to see the line between "we monitor our own software" and "we do not monitor your transaction estate". A final paragraph in Schedule 1 says that expressly.

### 15.3A Schedule 4, the data processing schedule, rebased

Schedule 4 mirrors MSA Schedule 3, and the same correction applies. **Read section 14.4A of the MSA reviewer brief for the full reasoning.** In short:

- v0.1 said the AI model services run on **TXN's** provider accounts and are therefore TXN's processors. On 6 October 2026 Dorte said *"all of the LLMs are via your contracts"* and Brett confirmed it. They run on **Novosapien's** accounts. Schedule 4 now states that **while that is the case the model providers are Novosapien's sub-processors**, and that the position confirmed under the MSA carries over to this Agreement so the parties do not confirm it twice.
- Part B now names **three** providers: **Google** (Gemini via GCP) as primary, **Anthropic** (Claude) as first failover, and **OpenAI** as second failover. Part A(d) adds that **a provider used only as a failover is still a sub-processor**.
- **Hosting is named and settled**: a dedicated node for the agentic AI layer in TXN's European Microsoft Azure environment, managed by Direct Transact alongside the Core API, inside Direct Transact's PCI-covered environment. The processing-locations row now reads European Union and United Kingdom, and Part C's opening paragraph matches.
- **EU or regional endpoint pinning** and zero-data-retention options are now obligations in the transfers row rather than aspirations.
- A **conversation history and traces** row records that the datastore location is still to be confirmed in writing, with sensitive data stripped before writing.

**Why this matters more here than in the MSA.** This Agreement is the one that runs for twelve months after the build stops, and it is the one under which Novosapien holds standing support access to a live card-issuing platform. If Dorte's external counsel reads one data schedule closely, it will be this one.

### 15.3B The licensing handover, and why it usually lands before this Agreement starts

Added 7 October 2026 on Brett's instruction. The Master Service Agreement now defines **Production Cutover**: the date a Deliverable first operates in the TXN Production Environment, confirmed in writing by both parties. **Before cutover** Novosapien licenses and runs the AI Model Services on its own accounts, so build and UAT are not held up waiting for TXN to contract with a model provider. **At cutover** the processing and the model licensing transfer to TXN, and the layer runs on TXN's LLM contracts. Full reasoning in section 14.4B of the MSA reviewer brief.

**What that means for this Agreement specifically.** Support commences on **16 December 2026**, and the Deliverables are expected to be in the production environment by then. So the **normal position under this Agreement is that the model providers are TXN's processors, not Novosapien's sub-processors**, which is a materially lighter position for Novosapien than the MSA carries during Phase 2.

Schedule 4 still lists the three providers in Part B, and that is deliberate. If any component of the Supported System has not cut over at the Commencement Date, the pre-cutover position applies to that component until it does. Listing them costs nothing and removes an argument. Part A(d) carries the same rule as the MSA: a provider used only as a failover is still a sub-processor.

**The point for counsel.** Do not read Part B as a statement that Novosapien holds the model contracts during the support term. It is a fallback for an incomplete cutover. Clause 1.1 now imports the MSA's defined terms so the two documents cannot drift on this.

### 15.4 Open points for counsel, refreshed

Carried forward and still open:

1. **The tier selection is unticked.** Schedule 2 offers Business Hours, Extended and Mission Critical. The £4,250/month figure in Schedule 3 and in MSA clause 7.5 is the Business Hours price. TXN has not selected a tier. A payments business running live card programs may well need Extended or Mission Critical, which is a different price.
2. **The entity particulars** mirror the MSA: TXN's Cyprus HE number, the effective date, and TXN's notice email are blank.
3. **TXN's DORA designation** is unconfirmed, as in the MSA.
4. **The security-measures Part C** still needs Brett's sign-off against the actual posture. The **hosting provider name is now resolved** (section 15.3A). Part C(h) commits that documented security-awareness onboarding will be in place before this Agreement commences; that date is now a real date, **16 December 2026**, so the commitment is now testable. Make sure it is met.
5. **Insurance** figures must match policies in force.

New with v0.2:

6. **The 12-month initial term now runs from 16 December 2026 to 15 December 2027.** Clause 9.3 permits termination during the initial term only for uncured material breach. Confirm TXN will accept a 12-month commitment to support on a system it has not yet run in production, or whether a shorter initial term closes faster. This is the most likely redline in the document.
7. **Availability measurement starts on a system wired to the live platform for the first time.** Phase 2 wires the Agent Access Layer and the Full Agentic Experience onto the real Core API. The availability target begins to bite on 16 December 2026, within days of that wire-in completing. Consider whether a short ramp period, for example the first full calendar month measured but not credited, is worth proposing before TXN asks for it.
8. **Section 11 above is stale on the liability cap and should be read with care.** It records a cap of 30 per cent of the MSA implementation fee (£43,350). The document does not say that. **Clause 9.2 as drafted caps each party's liability at the greater of £50,000 and the total charges paid under this Agreement in the 12 months before the claim**, separately from the MSA caps. That is the operative position. Counsel should note the practical effect of the commencement change: in the first 12 months the 12-month charges figure cannot exceed about £51,000 at the Business Hours tier, so the £50,000 floor is doing almost all the work early on. The strategy in section 11 for conceding a capped, sole-remedy credit regime instead of raising the cap still stands.

### 15.5 What this draft is still not

**Not final legal advice.** It needs a qualified solicitor's review before execution. The service-level targets and the exclusions are Novosapien's commercial positions and have been taken deliberately; the legal mechanics have not been reviewed by a practising solicitor.

9. **Confirm Production Cutover happens before 16 December 2026.** If it does not, Novosapien is supporting a live service while still holding the model contracts, which is the heaviest combination of obligations in either document. It is also a commercial exposure: Novosapien would be paying for production model consumption under clause 3.7(c) of the MSA while charging a fixed support fee.
10. **There is still no signed data processing agreement anywhere in this engagement** (vault open question #103). Dorte raised it on 6 October 2026 with the launch in view, and she intends a single trip to external counsel. This Agreement's Schedule 4 and the MSA's Schedule 3 should go to her as one pack, with the conversation-history storage question closed first.
