---
component: "[[components]]"
status: Defining
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[09-06-2026-developer-support]]"
  - "[[ux-ai-knowledge-base-updates]]"
  - "[[ux-ai-knowledge-learning]]"
---

# TXN — Internal Ops Agents

> **Component map:** [[components]] · **Vision:** [[vision]]
> **User journeys:** [[ux-ai-knowledge-base-updates|KB Updates]], [[ux-ai-knowledge-learning|Knowledge Learning]], [[ux-ai-enhanced-authorisation-reconciliation|Reconciliation]] — see [[user-journeys]]
> **Date:** 2026-06-10
> **Status:** Defining
> **Owner:** _TBC_
> **Sources:** [[13-05-2026-txn-vision-meeting]] (internal-operations vision), [[09-06-2026-developer-support]] (support-triage hand-off), [[ux-ai-knowledge-base-updates]] + [[ux-ai-knowledge-learning]] (the knowledge loop)

---

## 1. What Does This Component Do?

**Functional purpose:**

Internal Ops Agents is the **inward-facing** component — running the TXN business *itself* agentically, rather than the client-facing surfaces. Ian Johnson (TXN's CEO) was explicit that this is part of the vision, not a side-project, and named the risk directly: *"You are the single point of failure."* The worst outcome is delivering an agentic *client* experience while the business behind it is throttled by humans doing manual work — release notes, support triage, doc maintenance. The same agentic philosophy that powers the client surfaces must power the business that runs them, or the client experience can't keep up.

It also carries a **data-flywheel advantage**: ticket triage and the knowledge loop deliver value **from day one with no transaction data** — exactly the kind of AI TXN can ship before the data lake matures.

The component groups four established workstreams plus two it inherits from adjacent sessions:

```
Internal Ops Agents
├── Release pipeline          git + Linear → business-readable release notes
├── Knowledge engine          self-improving docs/KB loop (3 inputs → human-approved → re-indexed)
│     ├── self-healing docs   Sentry production error → navigate knowledge graph → open PR
│     ├── reactive capture    AI can't answer → support case → human resolves → validated answer → KB
│     └── proactive mining    recurring ticket pattern → suggested KB article → human approves → publish
├── Support triage & resolution  pre-triage + partial diagnosis + swarm investigation before a human
├── Process automation        general internal-workflow automation
├── Simulation & evaluation   synthetic-persona testing/training (parked as a launch component)
└── Settlement reconciliation  auth/clearing matching — provisional home, candidate for its own scope
```

The **knowledge engine** is the heart of it, and the two imported journeys are its two halves: *reactive capture* ([[ux-ai-knowledge-learning]]) turns questions the AI *couldn't* answer into validated knowledge, and *proactive mining* ([[ux-ai-knowledge-base-updates]]) turns recurring ticket *patterns* into new documentation. Both feed the same knowledge base, both are human-approved, version-controlled, and audited, and both close the loop by re-indexing so the next identical question is answered automatically — "the next ticket of that shape never escalates." **Support triage** ([[09-06-2026-developer-support]]) is the upstream feeder: the Developer Portal packages a well-formed, diagnosed ticket, and resolution + the knowledge loop happen here.

**Personas:**

| Persona | How they use this component | What they need from it |
|---------|---------------------------|----------------------|
| **TXN Support Specialist** | Reviews/approves AI-suggested KB articles; resolves escalated support cases; the human in the knowledge loop | Pre-triaged, well-contextualised cases; suggestions with their supporting evidence; final approval authority |
| **TXN Ops / Product Specialist** | Reviews documentation accuracy and operational guidance | Confidence the published docs are correct and version-controlled |
| **TXN Dev / Release team** | Receives auto-drafted release notes; receives self-healing-doc PRs | Business-readable notes; correct, reviewable PRs against the right component |
| **Finance & Settlement Analyst** | _(provisional)_ monitors reconciliation accuracy, investigates unmatched records | Higher match accuracy; fewer unresolved exceptions |
| **Client Programme User** (indirect trigger) | Asks a question the AI can't answer → escalation that seeds the knowledge loop | A reliable answer (even if via a human) rather than a speculative one |

---

## 2. What Needs to Happen?

**Functional requirements:**

- **Release pipeline** — an agent reads git + Linear and drafts **business-readable** release notes (not commit messages).
- **Self-healing docs** — a production error caught by Sentry routes to an agent that navigates the knowledge graph, identifies the failing component, and **opens a PR**.
- **Reactive knowledge capture** — when the AI cannot confidently answer (confidence below threshold), it **does not guess**: it gathers context (question, conversation history, entity/system context) into a **structured support case**, a human resolves it, the resolution is **validated**, and only then incorporated into the knowledge base.
- **Proactive knowledge mining** — the system continuously analyses support interactions, detects **recurring patterns** above a defined threshold (e.g. "high volume of Visa partial-approval tickets"), and **suggests** a new/updated KB article with its supporting evidence, for human approval.
- **Publish + re-index** — approved articles are published (Console / Portal / support) with **version control + audit**, and indexed so future AI answers retrieve them automatically.
- **Support triage & resolution** — consume the diagnosed tickets from [[developer-support]]; a **swarm** pre-investigates before a human; route to the correct internal queue (bug / enhancement / support).
- **Process automation** — automate general internal workflows so humans aren't the bottleneck.
- **Simulation & evaluation** — drive synthetic personas through tens of thousands of flows to test/train the agents and surface gaps in docs and product.

**Business rules:**

- **Human-in-the-loop, always** — AI must **never auto-publish** documentation or modify knowledge sources without human review and approval.
- **No speculative answers** — below the confidence threshold, escalate rather than answer.
- **Validated-only inclusion** — only human-verified resolutions enter the knowledge base, to prevent knowledge corruption.
- **Version-controlled + auditable** — every documentation change and every suggestion/approval is logged.
- **Pattern-thresholded** — don't propose docs off a small/noisy sample.

**Edge cases:**

- False pattern from a small sample → threshold gating before any suggestion.
- AI-generated article incomplete/inaccurate → human approval gate; suggestions show supporting evidence.
- Self-healing PR targets the wrong component → it's a PR (reviewed), not a direct commit.
- Knowledge update introduces inconsistency → validation + version control before it goes live.

---

## 3. How Should It Look and Feel?

_Mostly agent-facing / back-office, with human **review surfaces** where approval is required._

**Design direction:** Low-touch for humans — the agents do the gathering, drafting, and triage; the human sees a **clean review queue** (suggested article + its evidence; resolved case ready to promote to KB; release-note draft) and approves/edits/rejects. The bar is "turn the tap off at source" (Ian) — stop work reaching humans unless it genuinely needs them.

**Key UX principles:**
- **Evidence-attached** — every suggestion shows the support patterns / errors that triggered it.
- **Approve, don't author** — humans curate AI drafts rather than write from scratch.
- **Closed loop visible** — show that a resolved case has fed back into the KB.

---

## 4. How Are We Going to Solve It?

| Capability | Build / Buy / Access | Provider / Approach | Rationale |
|-----------|---------------------|-------------------|-----------|
| Release-note generation | Build | Agent over git + Linear → business-readable draft | Reads the same sources the change log uses ([[vision]]) |
| Self-healing docs | Build | Sentry webhook → agent navigates the knowledge graph → opens PR | Error-driven; PR keeps a human in the loop |
| Knowledge engine (capture + mining) | Build | Orchestrator + analysis agents over support interactions; threshold detection; draft generation; human-approval gate; re-index | The day-one, no-data-needed value; both journeys share this engine |
| Support triage swarm | Build | Multiple agents pre-investigate a packaged ticket before a human | Consumes [[developer-support]] tickets; "swarm" pre-triage |
| Process automation | Build | Agentic automation of internal workflows | Removes the human bottleneck Ian flagged |
| Simulation & evaluation | Build | Synthetic-persona harness running many flows | Tests/trains agents; surfaces doc/product gaps (also used in build/test) |
| Settlement reconciliation _(provisional)_ | Build | AI enhancement layer over the reconciliation engine | Improves auth/clearing match accuracy beyond rules — confirm home in a session |

---

## 5. What Data Does It Need?

| Data | Direction | Source / Destination | Notes |
|------|-----------|---------------------|-------|
| Commits + issues | In | git + Linear | Release-note source |
| Production errors | In | Sentry | Self-healing-doc trigger |
| Support interactions / tickets | In | Support system (fed by [[developer-support]]) | Pattern mining + triage + capture |
| Conversation context | In | AI assistant ([[co-pilot]] / portal) | Context for an escalated case |
| Documentation / knowledge base | In / Out | Umbraco CMS + the knowledge graph | Read for grounding; write (PR/article) on approval |
| Validated resolutions | Stored | Knowledge base (version-controlled) | Only after human validation |
| Auth/clearing records _(reconciliation)_ | In | Core API / Data Lake | Settlement matching |

---

## 6. Who Can Access It?

| Persona / Role | Access level | Notes |
|---------------|-------------|-------|
| TXN internal staff (support / ops / product / dev) | Internal — review/approve queues | The humans in each loop |
| Internal agents | Agent access via [[agent-access-layer]] | Scoped to internal-ops tools; PRs and KB writes gated by human approval |

_Internal-facing; not exposed to clients. Approval authority stays with TXN staff._

---

## 7. How Do We Know It's Working?

- [ ] _Recurring-ticket volume falls after a KB article ships (the "never escalates again" test)_
- [ ] _Share of escalated cases whose resolution is captured back into the KB_
- [ ] _Release notes are shipped business-readable with minimal human editing_
- [ ] _Self-healing PRs target the correct failing component (low false-PR rate)_
- [ ] _Support tickets reach humans pre-triaged/diagnosed — reduced human handling time_
- [ ] _Internal headcount does not scale linearly with client volume (the core thesis)_

---

## 8. Dependencies

**What this component needs:**

| Depends on | What we need | Blocking? |
|-----------|-------------|----------|
| [[developer-support]] | The packaged, diagnosed support tickets it resolves; the knowledge loop's upstream | **Yes** (for triage/knowledge) |
| [[agent-access-layer]] | Tools the internal agents act through; audit | **Yes** |
| git + Linear | Release-note source | No |
| Sentry | Production-error trigger | No |
| Umbraco CMS + knowledge graph | Docs to read and write (PR/article) | **Yes** (for the knowledge engine) |
| Data Lake (DT) | Settlement/analytical data (reconciliation) | No — later phase |

**What other components need from this one:**
- [[developer-support]] hands off tickets here and benefits from the improved KB (its co-pilot/MCP answers get better).
- [[co-pilot]] and the client surfaces improve as the knowledge base self-heals.

---

## 9. Priority

**Must-have at launch?** Partly. The **knowledge loop + support triage + release notes** are **day-one, no-data-needed** value (the data flywheel) and directly address Ian's "single point of failure" risk — high priority. **Settlement reconciliation** and **simulation-at-scale** are later-phase (reconciliation needs settlement data; simulation is parked as a launch component — revisit once a client-facing slice exists to test).

**Status note — `Defining`, not `Defined`:** assembled from the vision, the Developer Support session, and three UX journeys — **no dedicated Internal Ops deep-dive yet.** A focused session should confirm: the [[developer-support]] ↔ Internal Ops triage boundary; whether **reconciliation** belongs here or becomes its own payment-ops component; and the **simulation** scope/timing (it's also parked in [[components]]).

---

## 10. Risks

**Abuse vectors:**
- Prompt injection via ticket/support content steering a suggested article or PR.

**Data risks:**
- **Knowledge corruption** — an unvalidated/incorrect resolution entering the KB and propagating to client answers (mitigated by validated-only inclusion + version control).
- **False patterns** from sparse early data driving spurious doc suggestions (threshold gating).
- **Documentation drift** — a self-healing PR or article that lags the live API.

**Compliance:**
- Documentation changes version-controlled + auditable; support-case context may carry PII — handle per [[vision]] §8.

**Controls needed:**
- Human-approval gates on all publishing; confidence-gated escalation (no speculative answers); validated-only KB inclusion; pattern thresholds; version control + audit on every change; PRs (reviewed) rather than direct commits for self-healing.

---

## Sub-Components

| Sub-Component | Overview | Status | Link |
|--------------|----------|--------|------|
| Release pipeline | git + Linear → business-readable release notes | Collecting | _[[sub-components/release-pipeline]]_ |
| Knowledge engine | Self-improving docs/KB loop — self-healing (Sentry→PR), reactive capture, proactive mining; human-approved, re-indexed | Collecting | _[[sub-components/knowledge-engine]]_ |
| Support triage & resolution | Swarm pre-triage of packaged tickets; route + resolve; feeds the knowledge engine | Collecting | _[[sub-components/support-triage-resolution]]_ |
| Process automation | Agentic automation of internal workflows | Collecting | _[[sub-components/process-automation]]_ |
| Simulation & evaluation | Synthetic-persona testing/training harness (parked as a launch component) | Collecting | _[[sub-components/simulation-evaluation]]_ |
| Settlement reconciliation | AI-assisted auth/clearing matching _(provisional — candidate for its own payment-ops scope)_ | Collecting | _[[sub-components/settlement-reconciliation]]_ |
