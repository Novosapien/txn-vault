---
component: "[[components]]"
status: Defining
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[01-06-2026-component-1-Agent-Access-Layer]]"
  - "[[29-05-2026-stackworkz-meeting]]"
---

# TXN — Co-pilot

> **Component map:** [[components]] · **Vision:** [[vision]]
> **Date:** 2026-06-02
> **Status:** Defining
> **Owner:** _TBC_
> **Sources:** [[13-05-2026-txn-vision-meeting]], [[01-06-2026-component-1-Agent-Access-Layer]] (co-pilot scope + permissions), [[29-05-2026-stackworkz-meeting]]

---

## 1. What Does This Component Do?

**Functional purpose:**

The Co-pilot is the **reactive** entry point on TXN's trust spine — Concept 1. The user is in the driving seat, clicking through the Console (or Developer Portal), and the AI rides alongside as an assistant they can turn to: a panel, typically down the right-hand side, that they *open and ask*. It answers questions, explains what's on the screen, recommends actions, previews the impact of a change before it's made, and — with confirmation — can take the action on the user's behalf. It does **not** proactively interrupt (that is [[agent-inbox-alerts]]) and it is **not** the agent-as-interface (that is [[full-agentic-experience]]); it augments a human who is still doing the driving.

Two behaviours define its value. First, **impact explanation**: the user is not a card expert and doesn't want to be one, so before they change a setting the co-pilot tells them what it means — *"if you make this change, X,000 cards will be affected."* Second, **guided configuration / onboarding**: a card product carries ~200 fields and most users don't know what they do. The co-pilot collapses that into a guided conversation — it recognises the shape of the program ("you're a travel programme; here's what most clients in your shape do") and applies the right configuration with the user *confirming, not configuring*. Mike Moores (TXN's CTO) framed the product step as the highest-value target: *"how can we say, this is what 90% of people do — you're probably going to want to follow this."*

Crucially, the co-pilot is **scoped to everything, not just the current page**. Mike was clear that the user shouldn't need to know where to click — they can be on the Products page and ask about cards, and the co-pilot guides them to the right place and surfaces the right information. On the Console most of the relevant data is already on the screen, so the co-pilot leans on **analytical data from the wider set** and on on-screen context, rather than re-pulling individual records from the API. To keep tool use tractable, **page state scopes which tools are exposed** at a given moment (the page tells the co-pilot where the user is), with a set of holistic tools always available.

```
Co-pilot
├── Conversational Q&A         (ask about anything; guided to the right place)
├── Impact preview              ("if you change this, X cards affected")
├── Guided configuration        (pattern-recognised onboarding; confirm-not-configure)
└── Action-on-confirmation       (execute via Agent Access Layer, prompted-trust)
```

**Personas:**

| Persona | How they use this component | What they need from it |
|---------|---------------------------|----------------------|
| **Card Program Operators** (Console) | Open the co-pilot to ask, understand a screen, get a recommendation, preview an impact, or have it perform an action | Plain-language guidance; the AI as their card expert; confidence that an action is what they intended |
| **Integrators** (Developer Portal) | The co-pilot also renders in the Portal alongside [[developer-support]] — help understanding the product/console while integrating | Context-aware help that doesn't require leaving the page |

---

## 2. What Needs to Happen?

**Functional requirements:**

- User can open a conversational co-pilot in the Console (and Portal) and ask questions in natural language about anything in their program — not just the current page.
- Co-pilot **guides navigation** — points the user to the right place / surfaces the right information without them knowing where to click.
- Before a change, co-pilot **previews impact** using data-lake/analytical data ("this affects N cards / ~X% of transactions").
- Co-pilot offers **guided configuration**: recognises the program pattern and proposes the standard configuration ("90% of travel clients do this") for the user to confirm.
- Co-pilot can **execute an action on confirmation** via [[agent-access-layer]], honouring the user's permissions and the approval queue.
- **Prompted-trust confirmation**: the co-pilot always confirms what it is about to do before doing it ("this is the change I'll make — happy?"), surfacing recommendations at that step. Many actions need no second step beyond the confirmation.

**Business rules and constraints:**

- **Permission parity** — the co-pilot can never let a user do something they couldn't do in the Console; it respects the granular user permission model (see [[agent-access-layer]]).
- **Scoped to TXN's domain** — not a general-purpose assistant.
- **Bounded, not open-ended** — semi-structured (slash commands / predefined workflows) to keep queries built-for-success and cost controlled (shared design principle with [[agent-inbox-alerts]]).

**Edge cases and error states:**

- User asks about something outside their permissions → co-pilot advises they lack permission *early* (before attempting), and where relevant routes to the approval queue.
- Action irrelevant to the program type (e.g. an MCC change that doesn't apply) → surfaced as "not applicable here," even if the user has the permission.
- Permission rejection from the Core API → the descriptive error is surfaced/auto-corrected (see [[agent-access-layer]] validation layers).

---

## 3. How Should It Look and Feel?

**Design direction:** A quiet assistant panel, typically the right-hand rail of the Console — present, not intrusive. It feels like asking a knowledgeable colleague, in the user's language, not querying a database.

**Reference products:**
- **Claude / ChatGPT side-assistant** — the conversational model; Ian referenced Claude's *"before I do this, do you want me to do that?"* confirmation behaviour as the bar.
- **Super Ultra Console designs** — the co-pilot renders inside those screens; impact pop-ups already appear in the prototype.

**Key UX principles for this component:**
- **Confirm before acting** — short steps, but always "here's what I'll do."
- **Speak business, not config** — wrap the ~200-field reality in plain language.
- **Guide, don't gatekeep** — answer about anything; lead the user to the right screen.

---

## 4. How Are We Going to Solve It?

| Capability | Build / Buy / Access | Provider / Approach | Rationale |
|-----------|---------------------|-------------------|-----------|
| Conversational assistant | Build | Co-pilot agent rendered inside Console/Portal; page state sets exposed tools | Reuses [[agent-access-layer]] tools; page context keeps tool surface small/static |
| Impact preview | Build / Access | Query Data Lake + analytical set for the estimate | Most screen data is already present; co-pilot adds the wider analytical view |
| Guided configuration | Build | Pattern recognition over client-category data ("travel → these settings") | Collapses ~200 config fields into confirm-not-configure |
| Action execution | Access | [[agent-access-layer]] tools, prompted-trust confirmation, approval queue | Permission-scoped; server-side validated |

---

## 5. What Data Does It Need?

| Data | Direction | Source / Destination | Notes |
|------|-----------|---------------------|-------|
| On-screen / page context | In | Console (Stackworkz) | Sets state and exposed tools per page |
| Analytical / program data | In | Data Lake + Core API (via [[agent-access-layer]]) | Co-pilot favours the analytical set over re-pulling records |
| Client-category patterns | In | Data Lake (category tags: travel, lending, rewards…) | Powers guided configuration recommendations |
| Config changes | Out | Core API (via [[agent-access-layer]]) | On confirmation, permission-scoped, audited |

---

## 6. Who Can Access It?

| Persona / Role | Access level | Notes |
|---------------|-------------|-------|
| Card Program Operators | Scoped to their Console permissions | Co-pilot mirrors exactly what the user may do in the Console |
| Integrators (Portal) | Portal-scoped | Co-pilot in the Portal context; deeper integration help via [[developer-support]] |

_Inherits the permission model from [[agent-access-layer]]._

---

## 7. How Do We Know It's Working?

- [ ] _Users complete configuration/onboarding via the co-pilot without dropping to manual config_
- [ ] _Impact previews reduce "I didn't realise that would happen" support contacts_
- [ ] _Co-pilot answers resolve in-session without the user hunting for the screen_

---

## 8. Dependencies

**What this component needs:**

| Depends on | What we need | Blocking? |
|-----------|-------------|----------|
| [[agent-access-layer]] | Tools, permission scoping, server-side validation, approval routing | **Yes** |
| Console (Stackworkz) | Page state / on-screen context; render surface (right-hand panel) | **Yes** |
| Data Lake (DT) | Analytical data + client-category patterns for impact + guided config | Partial — can mock early |

**What other components need from this one:**
- The impact-explanation logic is shared with [[agent-inbox-alerts]] (same information source, different delivery — Ian's point).

---

## 9. Priority

_Phasing out of scope for this exercise — full scope captured. (Noted: the Console co-pilot is on TXN's critical path per Ian/Mike — a design input, not a scope cut.)_

---

## 10. Risks

**Abuse vectors:**
- Permission escalation — coaxing the co-pilot to act beyond the user's rights (mitigated by server-side validation in [[agent-access-layer]]).
- Prompt injection via user-controlled fields in context.

**Data risks:**
- Hallucinated card-domain guidance — must be grounded in TXN docs/data, not generic LLM knowledge (high-cost wrong answers).
- Stale analytical data leading to a wrong impact preview.

**Compliance:**
- Audit of co-pilot-initiated actions; PII handling in context (see [[agent-access-layer]] / [[vision]] §8).

**Controls needed:**
- Prompted-trust confirmation; permission-parity enforcement; grounding in TXN documentation; bounded-query framework.

---

## Sub-Components

| Sub-Component | Overview | Status | Link |
|--------------|----------|--------|------|
| Conversational Q&A | Ask-anything assistant, guided to the right screen | Collecting | _[[sub-components/conversational-qa]]_ |
| Impact preview | Pre-change "this affects N cards / X% of transactions" | Collecting | _[[sub-components/impact-preview]]_ |
| Guided configuration | Pattern-recognised onboarding; confirm-not-configure over ~200 fields | Collecting | _[[sub-components/guided-configuration]]_ |
| Action-on-confirmation | Execute via Agent Access Layer with prompted-trust | Collecting | _[[sub-components/action-on-confirmation]]_ |
