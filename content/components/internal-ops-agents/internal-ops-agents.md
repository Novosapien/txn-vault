---
component: "[[components]]"
status: Defining
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[09-06-2026-developer-support]]"
  - "[[10-06-2026-developer-support-and-internal-ops]]"
  - "[[ux-ai-knowledge-base-updates]]"
  - "[[ux-ai-knowledge-learning]]"
---

# TXN — Internal Ops Agents

> **Component map:** [[components]] · **Vision:** [[vision]]
> **User journeys:** [[ux-ai-knowledge-base-updates|KB Updates]], [[ux-ai-knowledge-learning|Knowledge Learning]], [[ux-ai-enhanced-authorisation-reconciliation|Reconciliation]] — see [[user-journeys]]
> **Date:** 2026-06-10
> **Status:** Defining
> **Owner:** _TBC_
> **Sources:** [[13-05-2026-txn-vision-meeting]] (internal-operations vision), [[09-06-2026-developer-support]] (support-triage hand-off), [[10-06-2026-developer-support-and-internal-ops]] (customer-onboarding workstream, CRM-as-record, cold-start simulation), [[ux-ai-knowledge-base-updates]] + [[ux-ai-knowledge-learning]] (the knowledge loop)

---

## 1. What Does This Component Do?

**Functional purpose:**

Internal Ops Agents is the **inward-facing** component — running the TXN business *itself* agentically, rather than the client-facing surfaces. Ian Johnson (TXN's CEO) was explicit that this is part of the vision, not a side-project, and named the risk directly: *"You are the single point of failure."* The worst outcome is delivering an agentic *client* experience while the business behind it is throttled by humans doing manual work. The same agentic philosophy that powers the client surfaces must power the business that runs them, or the client experience can't keep up. The thesis is simple: **internal headcount must not scale linearly with clients** — much of what a Customer Success Manager does is an AI target.

It carries a **data-flywheel advantage**: ticket triage, the knowledge loop, and onboarding deliver value **from day one with no transaction data** — exactly the kind of AI TXN can ship before the data lake matures.

```
Internal Ops Agents
├── Customer onboarding       client commits → due diligence → SoW/contract → scheme project → CIQ → project plan
│     ├── Due diligence        application form → research (Companies House, DORA, ownership, red flags) → report
│     ├── Meeting capture       notetaker → CRM-aware meeting-analysis agent teams → notes + actions, looped across meetings
│     └── SoW + drift           onboarding-interview agent captures intent; SoW changes auto-flagged
├── Release pipeline          git + Linear → business-readable release notes
├── Knowledge engine          self-improving docs/KB loop (3 inputs → human-approved → re-indexed)
│     ├── self-healing docs   Sentry production error → navigate knowledge graph → open PR
│     ├── reactive capture    AI can't answer → support case → human resolves → validated answer → KB
│     └── proactive mining    recurring ticket pattern → suggested KB article → human approves → publish
├── Support triage & resolution  pre-triage + partial diagnosis + swarm investigation before a human
├── Process automation        general internal-workflow automation
├── Simulation & evaluation   synthetic-persona testing/training — incl. pre-launch cold-start training
└── Settlement reconciliation  auth/clearing matching — provisional home, candidate for its own scope
```

**Customer onboarding** is the **first thing that happens after a client commits**, and Ian named it the place to start (park go-to-market; keep the scope thin). It runs from due diligence through to the client being live: due diligence (from the application form), Statement of Work + contract, raising the scheme project, providing the data for the Visa **CIQ**, and a realistic project plan (Visa's ~12-week lead time vs "go live tomorrow"). The guiding rule throughout: **assume a human (especially Mike) is *not* required on the call** — whoever is on it should be able to answer almost any question via AI; if the AI can't, that's a documentation gap to fix, not a reason to fetch "another Mike." A **notetaker + meeting-analysis** agent captures every call (reading the **Freshsales CRM** to infer the pipeline stage and analyse in the right context), and an **onboarding-interview agent** (à la Novosapien's content-workforce interview) guides the client, surfaces the painful realities up front (Visa = 12 weeks), captures what TXN and Visa need, and **flags when a client wants to change standard terms** so it routes to a human.

The **knowledge engine** remains the heart of the day-one value: *reactive capture* ([[ux-ai-knowledge-learning]]) turns questions the AI *couldn't* answer into validated knowledge, *proactive mining* ([[ux-ai-knowledge-base-updates]]) turns recurring ticket *patterns* into new documentation, and *self-healing* fixes docs from production errors. Mike confirmed the mechanism is buildable: **Umbraco supports edit-via-API in draft mode**, so the AI proposes and a human approves before publish — "the worst thing is answering the same question the next day." **Support triage** ([[09-06-2026-developer-support]]) is the upstream feeder.

**Where TXN itself works (architecture note):** Ian was firm that TXN should run its own operations through the **Claude-like agentic experience + Teams**, *not* by building more AI-management software into the Console; and that the **CRM (Freshsales) is the central source of truth** for everything client-related — the Console receives the data it needs *sent* to it, rather than context being split across systems. Both are recorded in [[architecture]].

**Personas:**

| Persona | How they use this component | What they need from it |
|---------|---------------------------|----------------------|
| **Customer Success Manager** | Runs project onboarding + the ongoing relationship; the role whose headcount AI must keep flat against client growth | Pre-done due diligence, drafted SoWs, captured meeting notes/actions, flagged drift — so they approve and relate, not administer |
| **Operations lead (Dorte)** | Owns customer operations, due diligence, legal/contract; defines the onboarding gates | A mapped gated process; AI to fire off checks and suggest the next step; a single source of truth |
| **TXN CTO (Mike)** | Product/tech; ideally *not* required on onboarding calls | Not to be the bottleneck; questions answered by AI; only genuine exceptions routed to him |
| **TXN Support Specialist** | The human in the knowledge loop; resolves escalations; approves KB articles | Pre-triaged cases; suggestions with evidence; final approval authority |
| **TXN Dev / Release team** | Receives auto-drafted release notes + self-healing-doc PRs | Business-readable notes; correct, reviewable PRs |
| **Client (onboarding)** | Submits the application form; is interviewed by the onboarding agent; provides CIQ inputs | A guided, supported onboarding that doesn't feel like form-filling; clarity on real timelines |

---

## 2. What Needs to Happen?

**Customer onboarding requirements:**

- **Due diligence** triggered by the **application form**: research ownership (25% threshold), negative press / red flags, DORA-driven checks; use sources like **Companies House** + plug-in data providers; produce a **due-diligence report with sources** for human validation. Light-to-detailed depending on the customer.
- **Statement of Work + contract** — capture the client's intended build as a **snapshot** (to keep them accountable — "customers want more, deliver less"); meetings for productivity, email/forms for the record.
- **Meeting capture & analysis** — a notetaker agent records calls, reads the **Freshsales CRM** to identify attendees + pipeline stage, routes to the right **meeting-analysis agent team**, and produces notes + actions, **looping across multiple meetings** to build the full picture.
- **Onboarding-interview agent** — guides the client through what's needed, surfaces hard realities up front (timelines, dependencies), and **flags requested changes to standard terms** to a human.
- **CIQ support** — know what goes into the Visa CIQ; **tick off what's been captured vs still missing** across the calls; provide the processor-side data TXN is responsible for; a **template** for TXN's standard settings (fixed info + the few changeable fields). TXN does **not** own/complete the whole CIQ.
- **Scheme project** — raise it for implementation; handle the triparty case (unregulated customer needs a third party); scope with the scheme; the BIN phase.
- **Project plan** — realistic dates anchored on real lead times (Visa ~12 weeks).
- **SoW-drift detection** — a change agreed in a conversation (even one Mike wasn't on) that affects the SoW is **automatically identified and flagged**, so TXN always knows what it's meant to deliver.

**Knowledge / support / release requirements:** _(carried from the established scope)_

- **Release pipeline** — agent reads git + Linear → **business-readable** release notes.
- **Self-healing docs** — Sentry error → agent navigates the knowledge graph → identifies the failing component → **opens a PR**.
- **Reactive knowledge capture** — below the confidence threshold the AI **does not guess**; it builds a structured support case → human resolves → validated → into the KB.
- **Proactive knowledge mining** — detect recurring patterns above a threshold → suggest a KB article (with evidence) for approval; consider **separate agent-facing vs user-facing doc versions**; a daily/weekly **cron job** consolidates support queries into a report with suggested snippets.
- **Publish + re-index** via Umbraco draft-API → human approval → live; indexed for future retrieval.
- **Support triage & resolution** — consume diagnosed tickets from [[developer-support]]; swarm pre-investigates; route by type.
- **Process automation** — automate internal workflows so humans aren't the bottleneck.
- **Simulation & evaluation** — drive synthetic personas through many flows to test/train agents; **pre-launch cold-start training** (below).

**Business rules:**

- **Human-in-the-loop, always** — AI never auto-publishes docs or commits CIQ/SoW changes without human approval; PRs/drafts only.
- **No human bottleneck** — onboarding proceeds without requiring a specific person; exceptions are captured by the notetaker and routed.
- **CRM is the source of truth** — client context lives in the CRM ([[architecture]]); flat documents limit data-item reuse.
- **No speculative answers**; **validated-only** KB inclusion; **version-controlled + auditable**; **pattern-thresholded**.
- **Trends, not one-offs** (Mike) — clients build differently; only raise a doc change when it's a genuine trend, not a single client's pattern.

**Edge cases:**

- A client builds in the platform without telling TXN their intent → TXN knows *what* was built but not *why*; the SoW/interview exists precisely to capture intent.
- SoW drift in a call no one logged → drift detection + notetaker capture.
- Due-diligence data source unavailable → flag for manual check; never fabricate a clearance.
- Same as before: false patterns (threshold), inaccurate AI article (approval gate), wrong-component PR (reviewed).

---

## 3. How Should It Look and Feel?

_Mostly agent-facing / back-office, with human **review surfaces** where approval is required, and a **conversational onboarding** surface for clients._

**Design direction:** Low-touch for TXN humans — agents gather, draft, triage; the human sees a **clean review queue** (due-diligence report + sources, drafted SoW, suggested KB article + evidence, release-note draft) and approves/edits/rejects. TXN works through the **agentic experience + Teams**, not bespoke Console admin UI. For clients, onboarding feels like a **guided interview**, not a form. Bar: "turn the tap off at source" (Ian).

**Key UX principles:**
- **Evidence-attached** — every suggestion/report shows its sources.
- **Approve, don't author** — humans curate AI drafts.
- **Provenance + status** — a shared onboarding form view can show, per field, who/what filled it (AI / client / TXN) and its review status.
- **Closed loop visible** — a resolved case visibly feeds the KB.

---

## 4. How Are We Going to Solve It?

| Capability | Build / Buy / Access | Provider / Approach | Rationale |
|-----------|---------------------|-------------------|-----------|
| Due-diligence research | Build / Access | Agent over Companies House + plug-in data providers → report with sources | Automates the manual, labour-intensive DD checks (Dorte) |
| Meeting capture & analysis | Build / Access | Custom notetaker (meeting API) → reads **Freshsales** for stage/attendees → routes to meeting-analysis agent teams → loops across meetings | Removes manual note-taking; analyses in the right pipeline context |
| Onboarding-interview agent | Build | Conversational agent (content-workforce pattern) capturing intent, surfacing timelines, flagging term changes | Replaces form-filling with a guided, supported experience |
| CIQ assembly | Build | Template of TXN's processor-side settings + capture-and-tick-off of what's covered vs missing | TXN provides its data; doesn't own the whole doc |
| CRM as source of truth | Integrate | **Freshsales** (has an API) holds all client context; Console gets data sent to it | One source of truth; avoids split context ([[architecture]]) |
| Release-note generation | Build | Agent over git + Linear → business-readable draft | Same sources as the change log |
| Knowledge engine | Build | Orchestrator + analysis agents; threshold detection; Umbraco **draft-API** writes; human approval; re-index; daily/weekly consolidation cron | Day-one value; buildable on Umbraco's API |
| Self-healing docs | Build | Sentry webhook → navigate knowledge graph → open PR | Error-driven; human-reviewed |
| Support triage swarm | Build | Agents pre-investigate a packaged ticket before a human | Consumes [[developer-support]] tickets |
| Simulation & evaluation | Build | Synthetic-persona harness — incl. **pre-launch cold-start** (below) | Tests/trains; bridges the no-data cold start |
| Settlement reconciliation _(provisional)_ | Build | AI enhancement over the reconciliation engine | Confirm home in a session |

**Pre-launch cold-start training (simulation):** before the knowledge hub has any real usage, the agent **teaches itself** — generate a raft of likely questions from the docs and answer them; generate deliberately **ambiguous/incomplete** questions to train the clarify-then-answer behaviour; and run **20+ developer/customer personas** (varying proficiency and background) through a multi-phase background workflow — read the docs → if insufficient, talk to the support agent → repeated hundreds/thousands of times → a sample dataset run daily for weeks pre-launch, continuing periodically once live. This is both the **Simulation & evaluation** capability and Dorte's cold-start bridge for the data-sparse launch.

---

## 5. What Data Does It Need?

| Data | Direction | Source / Destination | Notes |
|------|-----------|---------------------|-------|
| Application form | In | Client submission | Triggers due diligence |
| Due-diligence sources | In | Companies House + plug-in providers | Ownership, red flags, DORA checks |
| Meeting transcripts + attendees | In | Notetaker (meeting API) + Freshsales | Stage-aware meeting analysis |
| Client context / pipeline | In / Out / Stored | **Freshsales CRM** (source of truth) | All client-related data; sends what the Console needs |
| SoW + intent snapshot | In / Stored | Onboarding-interview agent → CRM | Keeps the client accountable; basis for drift detection |
| CIQ data items | In / Out | TXN template + client inputs → Visa CIQ | TXN provides processor-side data; doesn't own the doc |
| Commits + issues | In | git + Linear | Release notes |
| Production errors | In | Sentry | Self-healing-doc trigger |
| Support interactions / tickets | In | Support system (fed by [[developer-support]]) | Pattern mining, triage, capture |
| Documentation / knowledge base | In / Out | Umbraco CMS (draft-API) + knowledge graph | Read for grounding; write on approval |
| Auth/clearing records _(reconciliation)_ | In | Core API / Data Lake | Settlement matching |

---

## 6. Who Can Access It?

| Persona / Role | Access level | Notes |
|---------------|-------------|-------|
| TXN internal staff (CSM / ops / support / product / dev) | Internal — review/approve queues, via the agentic experience + Teams | The humans in each loop; approval authority |
| Client (onboarding only) | Conversational onboarding + shared form | Provides application/CIQ inputs; sees guided onboarding, not internal ops |
| Internal agents | Agent access via [[agent-access-layer]] | Scoped to internal-ops tools; PRs, KB writes, CIQ/SoW changes gated by human approval |

_Internal-facing. Approval authority stays with TXN staff; clients touch only the onboarding surface._

---

## 7. How Do We Know It's Working?

- [ ] _Internal headcount (esp. CSMs) does not scale linearly with client volume — the core thesis_
- [ ] _Onboarding calls proceed without requiring a specific person (e.g. Mike) on the line_
- [ ] _Due-diligence reports are produced with sources and accepted with minimal rework_
- [ ] _SoW drift is caught automatically (no "we built the wrong thing" surprises)_
- [ ] _Recurring-ticket volume falls after a KB article ships ("never escalates again")_
- [ ] _Release notes ship business-readable with minimal human editing_
- [ ] _Pre-launch simulation lifts day-one answer quality (no "read the documentation" failures)_

---

## 8. Dependencies

**What this component needs:**

| Depends on | What we need | Blocking? |
|-----------|-------------|----------|
| **Freshsales CRM** | The system of record + API to read/write client context | **Yes** (onboarding) |
| Companies House + DD data providers | Sources for due-diligence checks | No — incremental |
| Card scheme (Visa) | CIQ structure, BIN phase, lead times | No — known externally |
| [[developer-support]] | Packaged, diagnosed tickets; the knowledge loop's upstream | **Yes** (triage/knowledge) |
| [[agent-access-layer]] | Tools internal agents act through; audit | **Yes** |
| Umbraco CMS (draft-API) + knowledge graph | Docs to read + write on approval | **Yes** (knowledge engine) |
| Meeting-capture API | The notetaker surface | No — known API |
| git + Linear, Sentry | Release notes; self-healing trigger | No |
| Data Lake (DT) | Settlement/analytical data (reconciliation) | No — later phase |

**What other components need from this one:**
- [[developer-support]] hands off tickets here and benefits from the improved KB.
- [[co-pilot]] and the client surfaces improve as the knowledge base self-heals.
- The CRM-as-source-of-truth decision shapes what [[agent-access-layer]] / the Console read.

---

## 9. Priority

**Must-have at launch?** **Customer onboarding is the first internal-ops thing to build** (Ian — it's the first thing that happens after a client commits; park go-to-market). The **knowledge loop + support triage + release notes** are day-one, no-data-needed value. **Settlement reconciliation** and **simulation-at-scale** are later, though **pre-launch cold-start simulation** is needed *before* launch to avoid a day-zero "read the documentation" experience.

**Status note — `Defining`, not `Defined`:** the customer-onboarding workstream was opened in [[10-06-2026-developer-support-and-internal-ops]] but Ian explicitly said internal ops needs its **own vision** and shouldn't "boil the ocean." A focused session should confirm: the onboarding scope + gates (Dorte to map); the **CRM-vs-Console data split**; the [[developer-support]] ↔ Internal Ops boundary; reconciliation's home; and simulation scope/timing.

---

## 10. Risks

**Abuse vectors:**
- Prompt injection via ticket/support/meeting content steering a suggested article, PR, or CIQ field.

**Process / data risks:**
- **SoW drift** — a change agreed off-record leaving TXN building the wrong thing (mitigated by drift detection + notetaker capture).
- **CIQ responsibility boundary** — confusion over what TXN owns vs the client/sponsor; TXN provides its data, not the whole document.
- **Due-diligence accuracy / compliance** — DORA and ownership checks must be correct and sourced; never fabricate a clearance.
- **Knowledge corruption** — unvalidated resolution entering the KB (validated-only inclusion + version control).
- **One-off vs trend** — editing docs for a single client's pattern (Mike) — require a genuine trend.
- **Documentation drift** — a self-healing PR/article lagging the live API.

**Compliance:**
- Onboarding handles PII + regulated checks (DORA); documentation + CIQ data version-controlled and auditable (see [[vision]] §8).

**Controls needed:**
- Human-approval gates on all publishing + CIQ/SoW changes; SoW-drift flagging; sourced due-diligence with manual fallback; confidence-gated escalation; validated-only KB inclusion; trend thresholds; version control + audit; CRM as the single source of truth.

---

## Sub-Components

| Sub-Component | Overview | Status | Link |
|--------------|----------|--------|------|
| Customer onboarding | Client-commit → due diligence → SoW/contract → scheme project → CIQ → project plan; the first internal-ops build target (decomposes further into stage units) | Defined | [[customer-onboarding]] |
| Meeting capture & analysis | Notetaker + CRM-aware meeting-analysis agent teams; notes + actions looped across meetings | Defined | [[meeting-capture-analysis]] |
| Release pipeline | git + Linear → business-readable release notes | Collecting | _[[sub-components/release-pipeline]]_ |
| Knowledge engine | Self-improving docs/KB loop — self-healing (Sentry→PR), reactive capture, proactive mining; Umbraco draft-API; human-approved, re-indexed | Collecting | _[[sub-components/knowledge-engine]]_ |
| Support triage & resolution | Swarm pre-triage of packaged tickets; route + resolve; feeds the knowledge engine | Collecting | _[[sub-components/support-triage-resolution]]_ |
| Process automation | Agentic automation of internal workflows | Collecting | _[[sub-components/process-automation]]_ |
| Simulation & evaluation | Synthetic-persona testing/training, incl. pre-launch cold-start; the no-data bridge | Collecting | _[[sub-components/simulation-evaluation]]_ |
| Settlement reconciliation | AI-assisted auth/clearing matching _(provisional — candidate for its own payment-ops scope)_ | Collecting | _[[sub-components/settlement-reconciliation]]_ |
