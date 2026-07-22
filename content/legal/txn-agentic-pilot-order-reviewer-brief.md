# Reviewer Brief: Agentic Pilot Order (Novosapien & TXN)

**Prepared by:** Novosapien commercial-lawyer skill · **Date:** 22 July 2026 · **Draft version:** v0.1
**Instrument:** Standalone short-form Order (interim, self-sufficient; not contingent on the MSA)
**Parties:** Novosapien Global Ltd and TXN Global Limited
**Governing law:** England and Wales

## 1. What this is and what it is not

This is a competent **first draft** of a standalone Pilot Order, generated from Novosapien's house paper, aligned to the drafted Novosapien–TXN MSA, and grounded in the agentic-layer proposal v1.1 (Phase 1) and the TXN vault (`content/components/internal-ops-agents`, `full-agentic-experience`, `agent-access-layer`). It is **not final legal advice** and should be reviewed by a qualified solicitor before execution. Its job is to let TXN's CEO authorise the six-week pilot before he goes on leave (Friday 24 July COB), without waiting for the full MSA.

## 2. The deal in one paragraph

Novosapien delivers a six-week agentic pilot (Full Agentic Experience showcase, Agent Access Layer foundations, Internal Ops v1) on simulated tools and synthetic/test data, for **£54,187.50 exclusive of VAT** (1.5 months at the £36,125/month build rate). Payment is **50% on signature, 50% on completion/acceptance**. The Order stands entirely on its own; when the MSA is later signed, the pilot is carried into it as the completed Statement of Work 1, with the charge reconciled in the MSA's Schedule 2 and the pilot IP already vested in TXN.

## 3. Key positions taken (and why)

| Clause | Position taken | Rationale |
|--------|----------------|-----------|
| IP ownership (cl. 3) | Present assignment of all Foreground IP in the Pilot Deliverables to TXN as created; **not conditional on payment**; Novosapien's remedy for non-payment is suspension, not withholding title. Novosapien keeps its Background IP (delivery agents, frameworks, prompt libs, simulation tooling). | This is Ian's one hard, shareholder-driven requirement: pilot work belongs to TXN, unambiguously, even for the pilot. Lifted verbatim in substance from MSA §6.3 (assignment) and §6.2 (Background carve-out), so it holds before the MSA exists and carries over without change. |
| Standalone, not MSA-contingent (cl. 8.1) | The Order is a complete agreement for the pilot and survives even if the MSA is never signed. | Ian cannot sign the MSA before Friday; the pilot instrument must not depend on it. |
| Interim-then-absorbed (cl. 8.2–8.4) | On MSA signature, the pilot becomes the completed SoW 1, the £54,187.50 is recorded in MSA Schedule 2 (no double-charge), IP already assigned is preserved, nothing rebuilt. | Confirmed direction: recite AND adopt. Gives clean continuity with no IP/warranty gap. |
| Liability cap (cl. 6.4) | Greater of £150,000 and charges paid (general); greater of £250,000 and that for a data-protection breach. Carve-outs for confidentiality and wilful misconduct. | Matches MSA §9.4 exactly, so the cap does not shift when the pilot is absorbed. Note this exceeds the pilot fee, which is Novosapien accepting a fair, MSA-consistent cap. |
| Payment (cl. 2.2) | 50% on signature, 50% on completion; each invoice payable on issue; 6% over base late interest; suspend on 5 Business Days' notice for overdue undisputed sums. | Confirmed commercials; interest and suspension mirror MSA §7.4. |
| Acceptance (cl. 1.2) | Completion on demonstration + documented hand-over; 5 Business Day window for TXN to reject in writing with reasons for a material failure; deemed accepted otherwise. | Light, fair, and fast for a six-week demonstrator; avoids a payment stalling on silence. |
| AI output (cl. 6.1) | Provided with reasonable skill and care; not warranted error-free; the pilot is a demonstration on simulated tools, not a production system. | Honest about probabilistic/agentic output; consistent with MSA §9.1. |
| Data protection (cl. 5) | Prefer synthetic/test data; cardholder data out of scope; for any real personal data, Novosapien = processor on TXN's documented instructions and the parties adopt the MSA Schedule 3 (Art 28) terms for the pilot; no training on TXN data. | Covers the pilot either way. See open question Q1. |

## 4. Assumptions made

- Novosapien = Novosapien Global Ltd (no. 17308181, Aldgate Tower). TXN = TXN Global Limited, Cyprus (company number is a write-in; **still awaited**, per entity records).
- England & Wales governing law is correct. Note TXN is Cyprus-incorporated (EU), so EU GDPR applies alongside UK GDPR for any real personal data (handled via the MSA Schedule 3 hook in clause 5).
- Both parties are businesses, not consumers.
- Scope reflects the proposal v1.1 Phase 1 and the vault as at 22 July 2026.
- The £36,125/month build rate and the 50/50 split are as confirmed by Brett.
- Start date is a write-in (target week commencing 21 July 2026); "open for acceptance until 1 August 2026" is a placeholder to be aligned to Ian's availability before he leaves.

## 5. Negotiable points (where Novosapien can move)

- **Acceptance window:** 5 Business Days could flex to 10 if TXN wants more review time (weigh against the 6-week clock).
- **Payment split:** 50/50 is set; a 40/60 or milestone at week 3 is possible if TXN prefers to weight payment to completion.
- **Liability cap:** currently mirrors the MSA. TXN's counsel may probe a £150k cap on a £54k order; the answer is that it is deliberately MSA-consistent for clean carry-over, and is a ceiling not a floor.
- **DP clause:** can be simplified to "synthetic/test data only" if TXN confirms no real personal data (Q1).

## 6. Risks and things to watch

- **Data-processing (top risk).** The proposal says "synthetic data", but Internal Ops v1 (meeting capture, customer onboarding) can involve real personal data. If it does during the pilot, the Schedule 3 hook in clause 5 must be backed by the actual Schedule 3 text in the form last exchanged; confirm that text is settled enough to incorporate. Cross-border (Cyprus/EU + UK) transfer terms live in that schedule.
- **Schedule 3 dependency.** Clause 5.2 incorporates the MSA's Schedule 3 "in the form last exchanged". If that schedule is still moving, either freeze the version referenced or append a short interim processor annex to the Order so it is fully self-contained.
- **MSA divergence.** The drafted MSA still recites the 17 June proposal and a £144,500 build over four months. When the pilot is pulled out, the MSA's Schedule 1 (SoW 1) and Schedule 2 (Charges) need updating so SoW 1 = the pilot (delivered under this Order) and the build charge reflects the remaining wire-in (£90,312.50). That is a separate edit, not part of this Order, but flagged so the two documents stay consistent.
- **Entity number.** TXN Global Limited's Cyprus company number is blank in both this Order and the MSA; fill before signature.

## 7. Open questions for counsel / Brett

1. **Real personal data in the pilot?** Will Internal Ops v1 process any real personal data (CRM records, meeting attendees, prospect onboarding) in the six weeks, or synthetic/test only? This decides whether clause 5 stays as drafted (processor + Schedule 3) or simplifies to synthetic-only.
2. **Schedule 3 status.** Is the MSA Schedule 3 text stable enough to incorporate by reference for the pilot, or should we append a short interim processor annex here instead?
3. **Acceptance / validity dates.** Confirm the start date and the "open for acceptance until" date against Ian's leave (Friday 24 July COB), so he can sign in time.
4. **Signatory for Novosapien.** Who signs for Novosapien Global Ltd (Brett St Clair / George Westbrook), and is wet-ink or e-signature preferred (e-signature is currently accepted in clause 9)?

## 8. What is grounded vs assumed on scope

- **Grounded in the proposal/vault:** the three pilot deliverables and the synthetic-first, no-vendor-dependency basis (proposal v1.1 "Phase 1: the six-week agentic pilot"); Internal Ops v1 sub-scope (`content/components/internal-ops-agents`); the IP, liability, confidentiality, and DP positions (MSA §§6, 8, 9, Schedule 3).
- **Assumed / to confirm:** the DP data question (Q1), the two dates (Q3), the TXN company number, and the Novosapien signatory (Q4).
