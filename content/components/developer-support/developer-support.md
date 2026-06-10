---
component: "[[components]]"
status: Defined
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[29-05-2026-stackworkz-meeting]]"
  - "[[09-06-2026-developer-support]]"
  - "[[10-06-2026-developer-support-and-internal-ops]]"
---

# TXN — Developer Support

> **Component map:** [[components]] · **Vision:** [[vision]]
> **User journeys:** [[ux-txn-intelligence-enhanced-documentation-discovery|Documentation Discovery]], [[ux-ai-user-stories-and-requirements|User Stories & Requirements]] — see [[user-journeys]]
> **Date:** 2026-06-10
> **Status:** Defined
> **Owner:** _TBC_
> **Sources:** [[13-05-2026-txn-vision-meeting]] (developer experience), [[29-05-2026-stackworkz-meeting]] (portal AI split, MCP / LLMS.txt), [[09-06-2026-developer-support]] (dedicated deep-dive — four-level access, hosted MCP strategy, support triage), [[10-06-2026-developer-support-and-internal-ops]] (wrap-up — docs hosting, Umbraco draft-API, cold-start)

---

## 1. What Does This Component Do?

**Functional purpose:**

Developer Support is the agentic AI experience in the **Developer Portal** — the surface where integrators (and increasingly their own AI agents) evaluate and build against the TXN API. Much of the portal is a traditional, auto-rendered developer portal (API reference from the YAML, change log from git/Linear, a public sandbox) and is therefore "light-touch" for AI; the deep-dive ([[09-06-2026-developer-support]]) focused on the *AI surfaces* and, decisively, on **where TXN should and shouldn't invest**.

**The access spine — four levels.** Ian Johnson (TXN's CEO) framed everything around how much AI/capability is unlocked at each stage, balancing a best-in-class evaluation experience against cost and abuse:

```
Level 1  Unknown visitor   — not registered; minimal AI, public docs only
Level 2  Signed up         — gave a (corporate) email; lead created; more unlocked
Level 3  Prospect          — recognised, in evaluation; broader access
Level 4  Client            — contracted; full developer AI experience
```

The end game (Ian): *"the best possible evaluation we can within a reasonable cost framework, and let clients integrate as quickly and as accurately as they can."* Each level is a **stage gate**; the cost-control question ("this is free — how do we stop bad actors / competitors swamping it") is answered by what's unlocked when.

**The strategic bet — MCP over chatbot.** The biggest shift from the deep-dive. The team reframed dev support as *more than a portal chatbot*: a **hosted documentation MCP server** that a developer plugs straight into Claude / Claude Code. George's own behaviour drove it — *"if a platform has an MCP server I'll just plug into that; I won't even look at the documentation."* The deliberate consequence (Ian): **don't over-invest in the portal co-pilot** — build a solid baseline, but put the weight behind MCP, on the belief that developers will increasingly arrive that way rather than via a portal chatbot. *"Meet them where they are, with one eye on the future."*

**Support is an entry point here; the brain is in [[internal-ops-agents]].** George was explicit that support *resolution* lives in Internal Ops; the portal provides the **entry point and first-line triage**: a logged-in developer describes an error, the agent queries *their* recent API logs, diagnoses it ("422 — you didn't pass the card ID"), and packages a **well-formed ticket** (user + the request in question + the issue) instead of a "help me, it's broken" message. A **swarm of agents pre-investigates** before the ticket reaches a human.

```
Developer Support  (AI surfaces of the portal)
├── Docs MCP server (hosted)      L1: agent queries the docs · L2: test the public sandbox  ← the strategic surface
├── Portal co-pilot               scoped docs Q&A (deliberately light); surfaces known tickets
├── Sandbox assist                explain a failed "try it now" request; pre-validation
├── Support triage & ticket pack  logged-in error diagnosis from API logs → well-formed ticket → swarm pre-triage (→ internal-ops)
└── Access gating & lead-gen      four-level stage gates; API-key issuance; rate-limiting; lead capture
```

_(Note: the session also confirmed, from the client side, that **A2A is not a standalone component** — it's bucketed into the [[agent-access-layer]], to revisit at the end. The vault already reflects this.)_

**Personas:**

| Persona | How they use this component | What they need from it |
|---------|---------------------------|----------------------|
| **Unknown visitor / evaluator** | Browses public docs; gets a feel for the platform; maybe asks the co-pilot a basic question | A compelling sense of "what it's like to build with TXN" without giving anything away yet |
| **Signed-up developer (lead)** | Gave a corporate email → got an API key; can use the MCP server / sandbox within limits | A fast, low-friction way to evaluate via their own tools (Claude/Claude Code) |
| **Integrator (prospect / client)** | Builds against the API; uses the hosted MCP server in their agent; raises diagnosed support tickets | Clean, current, machine-readable docs; accurate first-line diagnosis; a frictionless path to a human |
| **Integrators' own AI agents** | Consume TXN's docs (L1) and test the sandbox (L2) via the hosted MCP server | The integrator supplies the LLM; TXN supplies the MCP server + API key |
| **TXN's internal team** (downstream) | Receive pre-triaged, well-formed tickets | Pre-diagnosed items (handed to [[internal-ops-agents]]) |

---

## 2. What Needs to Happen?

**Functional requirements:**

- A **hosted MCP server** exposes the documentation to a developer's own agent: **Level 1** = query the docs; **Level 2** = test the public sandbox (API calls + responses) through the MCP.
- Using the MCP / sandbox requires an **API key**, obtained by giving a name + corporate email — which **creates a lead** and lets TXN **rate-limit per key** (and invalidate on abuse).
- A **portal co-pilot** answers integration questions strictly from TXN's documentation (deliberately scoped/light); it can **surface existing support tickets / known answers** so resolved questions aren't re-raised.
- **Sandbox assist:** a failed "try it now" request gets an AI explanation of the error (e.g. malformed JSON, trailing comma) and optional **pre-validation** before sending.
- **Support triage (entry point):** a logged-in developer describes an issue; the agent queries their recent API request logs, diagnoses the likely cause, and **packages a well-formed ticket** (user + request + issue). A **swarm pre-investigates** before it reaches a human.
- Answers stay **current** because docs are generated from live sources (API reference auto-rendered from the YAML; change log from git + Linear in business-readable English — per [[vision]]).
- Public/unknown access is **limited and metered**; more AI capability unlocks as the visitor moves up the four levels.

**Business rules and constraints:**

- **Access is staged** — the AI capability available is gated by the four levels (unknown → signed-up → prospect → client); the cost framework drives where each gate sits.
- **Public-facing means confidential-safe** — for prospects/unknowns, never leak internal specifics or other-tenant data; portal answers draw only on documentation + anonymised/known-answer knowledge.
- **Hosted MCP** is the chosen model (local MCP is a worse experience; most use Claude in-browser).
- **Documentation-scoped** co-pilot — not a general assistant; grounded in TXN docs.
- **No forced triage choice** — the developer describes the problem; the system classifies (bug / enhancement / support) and routes.
- **Don't over-build the co-pilot** — invest in MCP; ship a best-in-class but not "every conceivable feature" experience, then learn from real users.

**Edge cases and error states:**

- **Bad actor / competitor swamping** the free surface → rate-limit per API key; invalidate keys on repeated abuse.
- Docs out of date vs the live API → co-pilot/MCP answers wrongly and silently (see §10 — documentation drift).
- Question spans an undocumented capability → defensive route to support; flag for doc self-healing ([[internal-ops-agents]]).
- A developer raises a lazy "it's broken" ticket → the triage flow extracts context (logs + request) to make it actionable anyway.

---

## 3. How Should It Look and Feel?

**Design direction:** A self-serve, low-friction portal that lets a developer *evaluate fast* and *integrate accurately* — with the AI experience meeting developers in the tools they already use (Claude / Claude Code via MCP), not forcing them into a portal chatbot. A best-in-class experience that is **not a "me-too" version** of existing developer portals (Ian's repeated bar), but without over-engineering before real-user feedback.

**Reference products:**
- **Hosted MCP servers** (e.g. Linear's) — connect, add an API key, done; the experience the team wants to match.
- Modern docs assistants (Stripe-style inline docs search) — current, scoped, fast — as the *baseline* co-pilot, not the headline.
- `LLMS.txt` convention — machine-readable docs for external agents.

**Key UX principles for this component:**
- **Meet developers in their agent** — the MCP server is the primary AI experience; the co-pilot is the fallback.
- **Answer from the docs or route on** — confidence-gated, never a guess; surface known-ticket answers.
- **Invisible triage** — the developer describes the problem; the system diagnoses and packages it.
- **Stage-gate generosity** — give a great evaluation, but unlock capability as trust/identity grows.

---

## 4. How Are We Going to Solve It?

| Capability                        | Build / Buy / Access | Provider / Approach                                                                        | Rationale                                                                                                    |
| --------------------------------- | -------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Hosted docs MCP server**        | Build                | TXN-hosted MCP over the docs corpus; API-key gated; L1 docs query, L2 sandbox test         | The strategic surface — devs plug it into Claude/Claude Code; hosted beats local for the common browser case |
| Portal co-pilot (LLM)             | Build (light)        | Novosapien-integrated LLM over the docs corpus                                             | Baseline scoped Q&A; deliberately not over-invested                                                          |
| Docs source                       | Access               | Umbraco headless CMS APIs (Stackworkz)                                                     | Stackworkz exposes docs via API for AI search; same central knowledge as the Console                         |
| Sandbox assist                    | Build                | AI explanation / pre-validation over a failed sandbox request                              | Cheap, high-value "why did my call fail" help                                                                |
| Support triage & ticket packaging | Build                | Logged-in agent queries the user's API logs → diagnose → package ticket → swarm pre-triage | Entry point here; resolution handed to [[internal-ops-agents]]                                               |
| Access gating & lead-gen          | Build                | Four-level stage gates; API-key issuance on email capture; per-key rate limits             | Balances best-in-class evaluation against free-surface cost/abuse                                            |
| Currency of docs                  | Access               | Auto-rendered API ref (YAML) + change log (git/Linear)                                     | Keeps answers accurate (per [[vision]])                                                                      |

_Cost is a first-order constraint throughout: the surface is free, so AI capability is metered per level and per API key. Tier-2 **voice support** was discussed (call an AI assistant; ~18–30p/min) and **parked** as a possible later add-on — text first._

---

## 5. What Data Does It Need?

| Data | Direction | Source / Destination | Notes |
|------|-----------|---------------------|-------|
| Documentation corpus | In | Umbraco headless CMS (Stackworkz) | The central knowledge piece, shared with the Console |
| Live API reference | In | YAML spec (auto-rendered) | Always-current endpoint docs (also grounds the MCP) |
| Visitor identity + email | In / Stored | Sign-up form → API key issuance | Creates the lead; sets the access level |
| API key + usage | In / Stored | Per-key rate-limit + abuse tracking | Meters MCP / sandbox usage |
| Developer's API request logs | In | Core API logs (via [[agent-access-layer]]) | For logged-in error diagnosis |
| Existing support tickets | In | Support system | Surfaced to reuse known answers |
| Packaged / classified ticket | Out | Internal queues ([[internal-ops-agents]]) | Well-formed, pre-triaged; bug / enhancement / support |

---

## 6. Who Can Access It?

| Persona / Level | Access level | Notes |
|----------------|-------------|-------|
| **L1 — Unknown visitor** | Public docs; minimal/metered co-pilot | No MCP/sandbox until identified; protects the free surface |
| **L2 — Signed up** | API key → MCP (L1 docs query) + limited sandbox; rate-limited | Corporate email; lead created |
| **L3 — Prospect** | Broader MCP/sandbox + support triage | Recognised, in evaluation |
| **L4 — Client** | Full developer AI experience + support | Contracted |
| Integrators' own agents | Machine access via hosted MCP / `LLMS.txt`, scoped to the key's level | Read docs (L1), test sandbox (L2) |

_Sign-up/login is **not yet scoped in the MVP design** (docs are currently fully public) — introducing it is a flagged decision (see §9 / gaps)._

---

## 7. How Do We Know It's Working?

- [ ] _Developers connect and use the hosted MCP server to evaluate/build (adoption over the portal chatbot)_
- [ ] _Share of integration questions resolved by co-pilot/MCP without human escalation_
- [ ] _Sign-up → API-key conversion produces qualified leads_
- [ ] _Support tickets arrive pre-diagnosed and well-formed (lower human triage time)_
- [ ] _Free-surface cost stays within the model; abuse caught by per-key rate limits_
- [ ] _External agents successfully build against the docs via MCP / `LLMS.txt`_

---

## 8. Dependencies

**What this component needs:**

| Depends on | What we need | Blocking? |
|-----------|-------------|----------|
| Umbraco CMS (Stackworkz) | Docs exposed via API for search/grounding + MCP corpus | **Yes** |
| Public sandbox (DT) | The sandbox the MCP L2 / sandbox-assist tests against; **API-key model TBD** | **Yes** — gates the sign-up decision |
| [[agent-access-layer]] | API logs for diagnosis; the MCP exposure pattern | **Yes** |
| [[internal-ops-agents]] | Destination queues + swarm triage/resolution for packaged tickets | No — can stub queues |
| Live YAML spec + git/Linear change log | Current API reference and release notes | Partial |
| Lead/CRM destination | Where captured sign-up leads go | No — can stub |

**What other components need from this one:**
- Shares the central knowledge base with [[co-pilot]] (one knowledge piece, two surfaces).
- Feeds packaged, pre-triaged tickets to [[internal-ops-agents]] (support resolution / doc self-healing).
- Its MCP exposure pattern shares the "expose docs/agent, key-gated" thinking with the [[agent-access-layer]] external edge.

---

## 9. Priority

**Must-have at launch?** Partly — by Ian's GTM sequence (*win business → onboard → operate → analyse*), the portal/docs is the **first surface to hit the market**, so the docs + a baseline co-pilot + the evaluation MCP are early. The richer support-triage swarm and voice can follow.

**Open decisions flagged in the deep-dive:**
- **Sign-up/login not yet designed** — needed to gate MCP/sandbox and capture leads; depends on the sandbox API-key model.
- **Public sandbox API-key model (DT)** — unknown; *changes whether/when sign-up is required*.
- **Cost per level** — Ian wants the actual cost-per-1000-calls understood before finalising the gates.
- **Voice support (Tier 2)** — parked pending real-user feedback.

**Confirmed / added in the 10-Jun wrap-up ([[10-06-2026-developer-support-and-internal-ops]]):**
- **Docs hosted in two stores** — the **DT YAML** (API reference) + **Umbraco** (guides + change log, API-accessible). Umbraco supports **edit-via-API in draft mode**, so the [[internal-ops-agents]] knowledge engine can propose doc updates for human approval. Guides are kept stable/business-level (code specifics link to the API reference to avoid staleness).
- **Pre-launch cold-start** — the portal co-pilot / MCP are trained *before* launch via the [[internal-ops-agents]] simulation harness (auto-generated + ambiguous questions, 20+ developer personas) so day-zero isn't a "read the documentation" experience.
- **Open:** the Super-Ultra `LLMS.txt`-style downloadable doc file (a lighter-than-MCP "here's TXN + endpoints" file) — ownership + cadence undecided (see [[architecture]]).

---

## 10. Risks

**Abuse vectors:**
- **Free-surface swamping** by bad actors / competitors with no revenue line — mitigated by per-key rate limits + key invalidation + staged access.
- Prompt injection via questions/feedback; attempts to pull the co-pilot off-domain.

**Data risks:**
- **Documentation drift** — answers (co-pilot *and* MCP) only as accurate as the docs; a Core API change unreflected in the YAML breaks them silently.
- Surfacing a stale support-ticket answer that no longer applies.
- **Reputational risk** (Ian): tools that confidently tell developers the wrong thing to code against are worse than no tool — accuracy is non-negotiable.

**Compliance:**
- Public surface — must not leak internal or other-tenant information; prospect answers stay on documentation + anonymised knowledge.

**Controls needed:**
- Staged access + per-key rate limiting + abuse invalidation; confidence gating + defensive routing; doc self-healing loop ([[internal-ops-agents]]); grounding strictly in TXN docs; tenant/scope isolation.

---

## Sub-Components

| Sub-Component | Overview | Status | Link |
|--------------|----------|--------|------|
| Docs MCP server (hosted) | The strategic surface — L1 docs query, L2 sandbox test; API-key gated; plugs into the developer's own agent | Defined | [[docs-mcp-server]] |
| Portal co-pilot | Semantic doc discovery + conversational guidance (deliberately light); grounded, deterministic fallback; surfaces known-ticket answers | Defined | [[portal-co-pilot]] |
| Sandbox assist | Explain a failed "try it now" request; optional pre-validation | Defined | [[sandbox-assist]] |
| Support triage & ticket packaging | Logged-in error diagnosis from API logs → well-formed ticket → swarm pre-triage (entry point; resolution in [[internal-ops-agents]]) | Defined | [[support-triage]] |
| Access gating & lead-gen | Four-level stage gates; API-key issuance on email capture; rate-limiting; lead capture; entitlement source for the others | Defined | [[access-gating]] |
