---
component: "[[components]]"
status: Defining
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[29-05-2026-stackworkz-meeting]]"
---

# TXN — Developer Support

> **Component map:** [[components]] · **Vision:** [[vision]]
> **Date:** 2026-06-02
> **Status:** Defining
> **Owner:** _TBC_
> **Sources:** [[13-05-2026-txn-vision-meeting]] (developer experience), [[29-05-2026-stackworkz-meeting]] (portal AI split, MCP / LLMS.txt)

---

## 1. What Does This Component Do?

**Functional purpose:**

Developer Support is the agentic AI experience in the **Developer Portal** — the surface where integrators (and their own AI assistants) build against the TXN API. It buckets everything AI-facing for the portal: a **documentation-scoped chatbot** that answers integration questions grounded in TXN's docs; a **defensive triage stack** that catches anything the chatbot can't confidently answer and routes it onward rather than guessing; a **feedback path** on every interaction that classifies an input as bug, product enhancement, or support request and drops it into the right internal queue *without the developer having to choose*; and a **machine-facing layer** (an MCP server over the docs plus an `LLMS.txt`) so a developer's own coding agent can consume TXN's documentation directly.

The portal serves two distinct AI consumers, and the call drew a clear line between them. The **site-wide chatbot** is operational — it has access to the relevant documentation, guides the user on what to click, and in some cases performs actions; this is where Novosapien integrates the LLM. The **developer-facing machine layer** is different: many developers will use their *own* agent / LLM, so what they need from TXN is a clean MCP server and `LLMS.txt` — the LLM is theirs, not TXN's. Stackworkz indicated they are happy to own the docs MCP / `LLMS.txt` piece "regardless of scope," since it sits naturally in their domain (the [[agent-access-layer]] notes this ownership split as an open question).

The knowledge the chatbot answers from is the **same central knowledge piece** that serves the Console — Mike Moores (TXN's CTO) described portal AI as *knowledge-base-centred*: searching documentation, helping developers understand it, and surfacing existing support-case tickets so a known answer is reused rather than re-raised. The docs themselves come from the portal's **Umbraco (headless) CMS**, which Stackworkz can expose via API for AI search.

```
Developer Support
├── Docs chatbot                (scoped Q&A grounded in documentation)
├── Defensive triage            (catch low-confidence answers → route on, don't guess)
├── Feedback routing            (bug / enhancement / support → right internal queue)
├── Support-ticket surfacing    (reuse known answers from existing tickets)
└── Machine layer (MCP/LLMS.txt) (developer's own agent consumes the docs — ownership split)
```

**Personas:**

| Persona | How they use this component | What they need from it |
|---------|---------------------------|----------------------|
| **Integrators** (Developer Portal) | Ask the chatbot integration questions; get answers from the docs; raise feedback/bugs without leaving the flow | Fast, accurate, doc-grounded answers; a frictionless path to a human when needed |
| **Integrators' own AI agents** | Consume TXN's docs via MCP / `LLMS.txt` to help build the integration | Clean, current, machine-readable documentation; the integrator supplies their own LLM |
| **TXN's internal team** (downstream) | Receive correctly-routed feedback/support items | Pre-classified, pre-triaged items (handed to [[internal-ops-agents]]) |

---

## 2. What Needs to Happen?

**Functional requirements:**

- A **scoped chatbot** answers integration questions strictly from TXN's documentation (no open-domain answers).
- When the chatbot can't answer confidently, a **defensive layer routes the query onward** to the support stack rather than hallucinating.
- Every interaction offers a **feedback path** classified automatically as **bug / product enhancement / support request** and routed to the correct internal queue.
- The chatbot can **surface existing support tickets / known answers** so resolved questions aren't re-worked.
- A **machine-facing MCP server + `LLMS.txt`** exposes the documentation for developers' own agents.
- Answers stay **current** because the docs are generated from live sources (API reference auto-rendered from the YAML spec; change log from git + Linear in business-readable English — per [[vision]]).

**Business rules and constraints:**

- **Documentation-scoped** — not a general assistant; grounded in TXN's docs.
- **Defensive by default** — uncertain → route to a human/queue, never guess.
- **No forced triage choice** — the developer never has to pick a queue; the AI classifies.

**Edge cases and error states:**

- Docs out of date vs. the live API → chatbot answers wrongly and silently (see §10 — documentation drift).
- Question spans an undocumented capability → defensive route to support; flag for doc self-healing ([[internal-ops-agents]]).

---

## 3. How Should It Look and Feel?

**Design direction:** A self-serve, low-friction support surface embedded in the portal — answers in-place, with an obvious, non-bureaucratic path to a human when the AI is unsure.

**Reference products:**
- Modern docs assistants (e.g. Stripe-style developer docs with inline search/answers) — current, scoped, fast.
- `LLMS.txt` convention — machine-readable docs for external agents.

**Key UX principles for this component:**
- **Answer from the docs or route on** — confidence-gated, never a guess.
- **Invisible triage** — the developer describes the problem; the system decides where it goes.
- **Always current** — answers reflect the live spec, not a stale copy.

---

## 4. How Are We Going to Solve It?

| Capability | Build / Buy / Access | Provider / Approach | Rationale |
|-----------|---------------------|-------------------|-----------|
| Docs chatbot (LLM) | Build | Novosapien-integrated LLM over the docs corpus | The site-wide operational AI — Novosapien provides the LLM |
| Docs source | Access | Umbraco headless CMS APIs (Stackworkz) | Stackworkz can expose docs via API for AI search |
| Docs MCP / `LLMS.txt` | Access / **ownership TBD** | Likely **Stackworkz** ("happy to own, regardless of scope") | Developers bring their own LLM; this is the machine-readable doc layer — see [[agent-access-layer]] MCP split |
| Defensive triage + routing | Build | Confidence gating → classify (bug/enhancement/support) → internal queue | Hands off to [[internal-ops-agents]] for triage/resolution |
| Currency of docs | Access | Auto-rendered API ref (YAML) + change log (git/Linear) | Keeps answers accurate (per [[vision]]) |

---

## 5. What Data Does It Need?

| Data | Direction | Source / Destination | Notes |
|------|-----------|---------------------|-------|
| Documentation corpus | In | Umbraco headless CMS (Stackworkz) | The central knowledge piece, shared with the Console |
| Live API reference | In | YAML spec (auto-rendered) | Always-current endpoint docs |
| Existing support tickets | In | Support system | Surfaced to reuse known answers |
| Classified feedback | Out | Internal queues ([[internal-ops-agents]]) | bug / enhancement / support |

---

## 6. Who Can Access It?

| Persona / Role | Access level | Notes |
|---------------|-------------|-------|
| Integrators (authenticated + public) | Public docs + chatbot; deeper context when signed in | Portal is part public marketing, part authed integration hub |
| Integrators' own agents | Machine access via MCP / `LLMS.txt` | Read-only docs consumption |

---

## 7. How Do We Know It's Working?

- [ ] _Share of integration questions resolved by the chatbot without human escalation_
- [ ] _Correct auto-routing of feedback (bug/enhancement/support) — low mis-route rate_
- [ ] _Reduced duplicate tickets (known answers surfaced)_
- [ ] _External agents successfully build against the docs via MCP / `LLMS.txt`_

---

## 8. Dependencies

**What this component needs:**

| Depends on | What we need | Blocking? |
|-----------|-------------|----------|
| Umbraco CMS (Stackworkz) | Docs exposed via API for search/grounding | **Yes** |
| Docs MCP / `LLMS.txt` (Stackworkz?) | The machine-readable doc layer — ownership to confirm | No — coordinate with Stackworkz |
| [[internal-ops-agents]] | Destination queues + triage for routed feedback | No — can stub queues |
| Live YAML spec + git/Linear change log | Current API reference and release notes | Partial |

**What other components need from this one:**
- Shares the central knowledge base with [[co-pilot]] (one knowledge piece, two surfaces).
- Feeds classified items to [[internal-ops-agents]] (support triage / doc self-healing).

---

## 9. Priority

_Phasing out of scope for this exercise — full scope captured. (Noted: Mike scoped portal AI as knowledge-base-centred; the broader portal is being built first per the partner timeline — a sequencing input, not a scope cut.)_

---

## 10. Risks

**Abuse vectors:**
- Prompt injection via questions/feedback content; attempts to pull the chatbot off-domain.

**Data risks:**
- **Documentation drift** — answers only as accurate as the docs; a Core API change unreflected in the YAML breaks the chatbot silently.
- Surfacing a stale support-ticket answer that no longer applies.

**Compliance:**
- Public surface — must not leak internal or other-tenant information in answers.

**Controls needed:**
- Confidence gating + defensive routing; doc self-healing loop ([[internal-ops-agents]]); grounding strictly in TXN docs; tenant/scope isolation.

---

## Sub-Components

| Sub-Component | Overview | Status | Link |
|--------------|----------|--------|------|
| Docs chatbot | Scoped Q&A grounded in documentation | Collecting | _[[sub-components/docs-chatbot]]_ |
| Defensive triage | Confidence-gated routing of low-confidence queries | Collecting | _[[sub-components/defensive-triage]]_ |
| Feedback routing | Auto-classify bug/enhancement/support → internal queue | Collecting | _[[sub-components/feedback-routing]]_ |
| Support-ticket surfacing | Reuse known answers from existing tickets | Collecting | _[[sub-components/support-ticket-surfacing]]_ |
| Machine layer (MCP / LLMS.txt) | Docs exposed for developers' own agents — ownership split with Stackworkz | Collecting | _[[sub-components/docs-machine-layer]]_ |
