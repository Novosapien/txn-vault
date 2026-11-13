---
description: "Reviewer brief for Support & SLA v0.3: the two operating modes, the commencement restructure off 16 December, the availability defect fixed, and the pass-through at cost plus 10%"
---

# Reviewer brief: Support & SLA Agreement v0.3

**Instrument:** [[txn-agentic-ai-layer-support-sla]] · **Draft v0.3, 13 November 2026.** For Brett's review, then TXN's counsel.
**Supersedes** the v0.2 brief of 7 October. Read with [[txn-dpa-interim-hosting-reviewer-brief]], because the two documents divide the data protection work between them.

---

## 1. Why v0.2 had to be rebased

Ian asked on 11 November ([[2026-11-11-personal-data-alignment]]) for support and maintenance papered
immediately after the hosting arrangement. v0.2 could not simply be signed, for three reasons.

**One: it commenced on a date that no longer exists.** v0.2 hard-coded commencement at **16 December
2026**, the day after Phase 2. That was built on the assumption that the Console components would be
live by then. They will not be, and TXN has not set a date for them. Meanwhile the Knowledge Hub
*does* have a date and is live from launch. A single fixed commencement date is the wrong shape.

**Two: it left a live, Novosapien-hosted public service uncovered.** The Knowledge Hub goes live on
16 or 17 November and Novosapien hosts it. Under v0.2, support began a month later. Clause 2.1A said
the Phase 2 charge covered "correction of defects", which is not the same thing as running a
production service with availability and incident obligations.

**Three, and this is the real defect: it committed Novosapien to availability it does not control.**
v0.2 Schedule 2 stated a hard 99.5% monthly availability target and hung the chronic-failure
**termination** right off missing it three months in six. After Production Cutover, Direct Transact
hosts the Console components, controls all access, and **is the only party that may deploy to them**.
Clause 4.1's "for the parts within its control" hedge does not survive a Schedule that states a
number and attaches a termination right to it. Novosapien could have been terminated for Direct
Transact's downtime.

## 2. The structural answer: two operating modes

v0.3 states, for every component, who hosts it and what follows. This is the centrepiece and it is
new (clause 4).

| | **Hosted Mode** | **Supplier Mode** |
|---|---|---|
| Who hosts | **Novosapien**, in its own Azure subscription | **TXN and Direct Transact**, in the TXN Production Environment |
| Who deploys | Novosapien | **Direct Transact only** |
| Components today | The Knowledge Hub AI Assistant, and only that | Agent Access Layer, Co-pilot, Agent Inbox & Alerts, Full Agentic Experience, Internal Ops Agents |
| Availability | **Novosapien commits** 99.5% / month | **No availability target at all** (clause 5.2) |
| Backup and recovery | Novosapien's | TXN's (clause 6.2) |
| Resolution means | Service restored | **A tested fix delivered to TXN's release process** (clause 4.3) |
| Data protection role | **Processor**, continuously | **Not a processor** (clause 10.2) |

A component moves from Hosted to Supplier at its Production Cutover, confirmed in writing, and stays
in Hosted Mode until the parties confirm it (clause 4.2). That mirrors the per-Deliverable cutover
mechanism already in MSA clause 1.2, so the two documents move together.

## 3. The three positions that matter most

### Commencement now follows what is actually live (clauses 2.1, 2.2)

- **The Agreement commences on the Knowledge Hub go-live date.** That is the only date anyone can
  currently confirm, and it is the component Novosapien is accountable for.
- **Each other component enters support on its own Service Commencement Date**, confirmed in writing
  when it goes live. **Schedule 1 Part B deliberately leaves those dates blank.** A component carries
  no service level before its date.
- The confirmed dates are recorded in the monthly service report, which becomes the agreed record of
  what is in support. No side letter needed each time.

**This is better for Novosapien than v0.2.** Novosapien stops owing service levels on components TXN
has not taken live, and stops owing them from an arbitrary calendar date.

### Resolution, when Novosapien cannot deploy (clauses 4.3, 4.4)

This is the single most important protection in the document. In Supplier Mode, resolution is
**delivering a tested fix or workaround to TXN's release process**, with the release notes and test
evidence that process requires. The target is met on delivery. **Deployment, and the time Direct
Transact takes to deploy, are not counted against Novosapien.**

Clause 4.4 adds the pause: the clock stops while Novosapien waits on information, a decision, access,
or a release slot, and each pause is recorded in the monthly report so the measurement is auditable
rather than asserted.

Without these two clauses, a 4-hour P1 resolution target on a system Novosapien cannot deploy to is
unmeetable by construction.

### Break-glass access, and the honest answer on the processor role (clauses 4.5, 10)

Brett's instruction was to cater for the case where Novosapien is *not* a data processor. v0.3 does
that, but it does not overclaim, because "Novosapien is never a processor" stops being true the
moment an engineer opens a production log to debug a P1.

So there are three states, not two:

1. **Hosted Mode: processor, continuously.** For the Knowledge Hub this is governed by the
   [[txn-novosapien-dpa-interim-hosting]], which prevails over this Agreement for it. No duplication,
   no risk of the two drifting.
2. **Supplier Mode: not a processor.** Novosapien has no standing access, does not need TXN personal
   data, and TXN undertakes not to send it any. Only confidentiality applies. If TXN sends personal
   data anyway, Novosapien says so and the parties decide whether to delete it.
3. **Break-glass: a processor for the window only.** Access is requested in writing naming the
   individual, the systems, the purpose and the period; granted for a defined period; withdrawn;
   logged by both sides. Schedule 4 applies in full for the duration. Data extracted for the
   diagnosis is deleted when the Incident closes, confirmed in the monthly report. The written grant
   is TXN's Article 28 documented instruction.

Breach notification at 24 hours applies **in every mode** (clause 9.3), including Supplier Mode, so
there is no gap if Novosapien learns of something through its own monitoring.

## 4. Charges

| Item | Position | Note |
|---|---|---|
| Support tier | **Business Hours, £4,250 / month** | Unchanged from v0.2. A documentation assistant down overnight is an embarrassment, not an outage |
| When the fee starts | The first month in which **neither** the Phase 2 team charge **nor** a Phase 3 retainer is payable (clause 2.3) | The Agreement commences at Knowledge Hub go-live, so all the obligations bite from day one, but TXN is not charged twice for the same month. This applies v0.2's existing Phase 3 principle consistently to Phase 2 |
| **Pass-through, new** | Cloud hosting, AI model consumption and observability for Hosted Mode components, at **cost plus a 10% administration fee** (clause 2.4, Schedule 3) | Monthly in arrears, with the provider statements attached. None of this applies in Supplier Mode, where TXN holds the accounts |
| Day rates | £950 / £850 / £750 | Unchanged |
| Service credits | **None** | House position held |

> [!warning] The pass-through contradicts the MSA, and the MSA is the document that is wrong
> **MSA clause 3.7(c) says model consumption is recharged "at billed cost".** MSA Schedule 2 says "AI
> model usage is not charged by Novosapien" and "cloud and observability hosting are excluded". The
> 10% administration fee contradicts all three.
>
> SLA clause 2.4 resolves it by expressly prevailing over MSA 3.7(c). That works, but it leaves the
> MSA stating something untrue. **MSA clause 3.7(c) and Schedule 2 should be corrected when the MSA
> next moves**, and the correction should be flagged to TXN rather than left for their counsel to
> find. A supplier whose two agreements disagree about money is the one thing that will slow this
> down.

## 5. Negotiables and floors

| Term | Hold | Floor / trade |
|---|---|---|
| **No availability target in Supplier Mode** (5.2) | **Hold absolutely** | This is the v0.2 defect. Do not accept a redline restoring a blended target. If TXN insists on a number for DT-hosted components, the answer is that TXN should take it from Direct Transact, who hosts and deploys |
| **Resolution = delivery to the release process** (4.3) | **Hold absolutely** | Non-negotiable while Novosapien cannot deploy. If TXN wants resolution measured to live, the trade is Novosapien getting deploy rights, which Direct Transact has refused |
| Clock pauses (4.4) | Hold | Accept a cap on cumulative pause time per Incident if pushed, but keep the mechanism |
| Commencement per component (2.2) | Hold | TXN may want one date for simplicity. Resist: it puts Novosapien back on the hook for components TXN has not launched |
| Pass-through at cost + 10% (2.4) | 10% | Cost-only is the floor, and it is what the MSA currently says, so expect the challenge. Below cost is never acceptable |
| Support fee £4,250 | Hold | The Extended tier at £6,750 is the upsell if the Knowledge Hub proves to need weekend cover |
| Break-glass logging and time-boxing (4.5) | Hold | This protects both sides. TXN's security team should welcome it |
| P1 15 min response | Hold | Tighter than the house default of 2 Service Hours. It is staffable inside Service Hours with the shared Slack channel and the monitoring agents. Do not extend it to out-of-hours without a rota |
| Liability cap, greater of £50,000 and trailing 12-month charges (11.2) | Hold | Separate pool from the MSA and the DPA, expressly. Do not let it be merged |
| ISO 27001 / SOC 2 (Schedule 4 Part C(a)) | **Claim nothing** | Novosapien holds neither. v0.3 removes v0.2's forward commitment to "pursue alignment", which was an obligation with no funding behind it |

## 6. Open before signature

| Item | Owner |
|---|---|
| TXN's Cypriot company (HE) number, and the notice address | TXN |
| Confirm the Knowledge Hub go-live date, 16 or 17 November, as the Commencement Date | TXN (Ian), [[open-questions]] #130 |
| Confirm the support fee start month, on the clause 2.3 no-double-charge rule | Brett and TXN |
| Agree the named contact for break-glass requests, on both sides | Both |
| Correct MSA clause 3.7(c) and Schedule 2 for the pass-through uplift | Novosapien |
| Confirm Direct Transact will accept fixes through a defined release process, so clause 4.3 has something to deliver into | TXN, with Direct Transact |

## 7. Honest limitations

- A competent draft, not a solicitor's sign-off. It should be reviewed by a qualified solicitor before
  execution.
- **Clause 4.3 depends on a release process that does not yet exist in agreed form.** Direct Transact's
  Q05 asks Novosapien to define the release pack; that work is outstanding. Until there is a defined
  process to deliver a fix into, "delivered to TXN's release process" is harder to measure than it
  reads. This is worth saying to TXN plainly, because it is a shared dependency, not a Novosapien gap.
- Schedule 4 Part C states the measures Novosapien operates today. It makes no certification claim and
  should not be edited to imply one.
- The agentic components that will carry real client data are not yet in support and have no date. When
  they arrive, the Support Tier should be revisited: a Business Hours tier is the right answer for a
  documentation assistant and probably not for a component in the payment path.
