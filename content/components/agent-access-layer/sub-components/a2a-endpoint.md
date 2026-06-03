---
component: "[[agent-access-layer]]"
status: Collecting
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[01-06-2026-component-1-Agent-Access-Layer]]"
  - "[[29-05-2026-stackworkz-meeting]]"
---

# TXN — A2A Endpoint

> **Parent component:** [[agent-access-layer]] · **Vision:** [[vision]]
> **Date:** 2026-06-02
> **Status:** Collecting
> **Owner:** _TBC_
> **Sources:** [[13-05-2026-txn-vision-meeting]] (Concept 3 / A2A), [[01-06-2026-component-1-Agent-Access-Layer]] (permission scoping, approval, audit), [[29-05-2026-stackworkz-meeting]] (external agents)

> [!warning] Sub-component of the Agent Access Layer — not yet deep-dived
> The A2A endpoint is the inbound door for external agents and rides on the access layer's tool surface, so it lives **inside** [[agent-access-layer]] rather than as a standalone component. It has not had its own deep-dive — detail below reflects the vision and the access-layer session plus inference. Treat scope and acceptance criteria as **proposals to confirm**. Open questions tracked in [[open-questions]].

---

## 1. What Does This Component Do?

**Functional purpose:**

The A2A Endpoint is TXN's **agent-to-agent face** — the surface through which a client's *own* agent (or an LLM like Claude in the client team's hands) acts on TXN's capabilities on behalf of a human user, over standard agent-to-agent protocols. It is the destination end of the trust spine (Concept 3): where the [[full-agentic-experience]] is TXN's *own* agent as the interface, the A2A Endpoint is the *inbound* door for *external* agents the client controls. It is treated as a co-equal surface alongside the Console and Developer Portal because it is how a whole class of clients will prefer to integrate — TXN's CEO Ian Johnson noted that many clients will run their own AI over the data TXN gives them, and Mike Moores (TXN's CTO) raised the explicit case of *"what if I want my whole business to work with your agent, agent-to-agent."*

The endpoint exposes the same capabilities the rest of the AI layer uses — it rides on the tool surface and MCP server of the [[agent-access-layer]] — but adds the agent-to-agent protocol, identity, and scoping needed for an external agent to be trusted. The load-bearing rule is that an external agent **gets exactly the permissions of the human user it represents, and no more**. Because TXN's permission model was designed around the Console, an external/agent-to-agent consumer needs an **AI-specific permission configuration** that mirrors the granular Console permissions (there is no such API today — see [[agent-access-layer]]).

Critically, **the agentic shortcut does not bypass TXN's safeguards**. Ian was firm that "if it's agent-to-agent we don't care, we'll just do whatever's asked" is *not* the model — the same **prompted-trust** confirmation, impact information, **approval queue**, and **audit trail** that protect a Console user apply to an external agent. The whole proposition is that TXN helps non-experts avoid costly mistakes; abandoning that for A2A would undermine it. Approvals can themselves be **agent-mediated**: where an action needs sign-off, the request routes to the named approver (or their agent), who confirms, and only then does it execute.

```
A2A Endpoint
├── Agent-to-agent protocol     (external/client agent connects, over A2A standards)
├── Identity & scoping           (maps the agent to its human user's permissions)
├── Prompted-trust + approval    (confirm / impact / approval-queue still enforced)
└── Audit                         (every A2A-initiated action attributed and logged)
```

**Personas:**

| Persona | How they use this component | What they need from it |
|---------|---------------------------|----------------------|
| **The client's own agents** (A2A) | A client-built agent / Claude acts on TXN on behalf of a human user — querying data, requesting changes | Permission parity with the human; a stable A2A contract; clear impact + confirmation before acting |
| **The client business** (whole-business A2A) | A business wires its operations to TXN agent-to-agent | Business-scoped identity; governance that mirrors what they'd set in the Console |
| **The named approver** (or their agent) | Receives and approves agent-initiated high-impact changes | The request + context (incl. that an AI agent recommended it) to make an informed approval |

---

## 2. What Needs to Happen?

**Functional requirements:**

- An external/client agent can connect over **agent-to-agent protocol(s)** and invoke TXN capabilities (the [[agent-access-layer]] tools).
- The endpoint **maps the agent to a human user identity** and enforces **exactly that user's permissions** — never more.
- **Prompted-trust applies**: before a state change, the endpoint surfaces what will happen + estimated impact and obtains confirmation (the external agent can decline detail, but the action is still confirmed).
- **Approval queue applies**: actions affecting multiple cards (product/spend-control level) route to a named approver, who can approve via their own channel/agent; the *approver* becomes the initiator of the action.
- Every A2A-initiated action is **audited** — attributed to the agent + the user it represents, captured alongside the API and chat audit (see [[agent-access-layer]]).
- Supports **business-level** and **individual-user-level** scoping (the "client as super-user" model from [[agent-access-layer]]).

**Business rules and constraints:**

- **No safeguard bypass** — A2A does not skip confirmation, impact, approval, or audit.
- **Permission parity** — an agent can only do what its represented user can do in the Console.
- **Server-side authoritative rejection** — unpermitted calls are rejected by the Core API with formatted errors the agent can self-correct (see [[agent-access-layer]] validation layers).

**Edge cases and error states:**

- A client with **no Console users** ("I'll just use AI to do everything") → treated as a single super-user client (all permissions TXN makes available); needs an identity to attribute to.
- Approver unavailable → action waits in the approval queue; agent informed.
- Protocol/version drift → see §10 (A2A immaturity).

---

## 3. How Should It Look and Feel?

**Design direction:** This is a protocol/contract surface, not a visual one — its "feel" is reliability, predictable scoping, and transparent confirmation/audit. The experience is felt by the *client's* agent and, at approval time, by a human approver.

**Reference products:**
- Emerging **A2A** / agent-to-agent protocol standards (tracked; still maturing).
- **MCP** as the underlying tool-exposure mechanism (via [[agent-access-layer]]).

**Key UX principles for this component:**
- **Same trust model as humans** — confirm, show impact, route approvals, audit everything.
- **Least privilege** — represented-user permissions, nothing broader.
- **Self-correcting** — descriptive, machine-readable errors so the external agent can retry correctly.

---

## 4. How Are We Going to Solve It?

| Capability | Build / Buy / Access | Provider / Approach | Rationale |
|-----------|---------------------|-------------------|-----------|
| Agent-to-agent protocol surface | Build / Access | A2A standard(s) on top of the [[agent-access-layer]] MCP server | Reuse the tool surface; add the agent-to-agent face |
| Identity & permission scoping | Build | AI-specific permission config mirroring Console permissions (user + org) | No API exists today; must mirror granular Console model |
| Prompted-trust + approval | Access | Reuse confirmation + Console approval queue (via [[agent-access-layer]]) | Same safeguards as Console/Co-pilot |
| Audit | Access | Combined console/API/chat audit (see [[agent-access-layer]]) | Attribute agent + user; provable "prompted + confirmed" |

---

## 5. What Data Does It Need?

| Data | Direction | Source / Destination | Notes |
|------|-----------|---------------------|-------|
| Agent ↔ user identity mapping | In | AI permission config (to be built) | Mirrors Console user/org permissions |
| Capability/tool calls | In/Out | [[agent-access-layer]] tools / Core API | Permission-scoped, server-validated |
| Impact estimates | Out | Data Lake (via [[agent-access-layer]]) | For prompted-trust before changes |
| Action + approval audit | Out | Combined audit store / data warehouse | Attributed to agent + represented user |

---

## 6. Who Can Access It?

| Persona / Role | Access level | Notes |
|---------------|-------------|-------|
| Client's own agent (representing a user) | Exactly the represented user's permissions | Least privilege; server-validated |
| Client business (whole-business A2A) | Business/super-user scope, as configured | Mirrors Console governance |
| External agent without a mapped user | Denied / must map to an identity | No anonymous capability access |

_Inherits and extends the permission model from [[agent-access-layer]]._

---

## 7. How Do We Know It's Working?

- [ ] _External agents complete tasks within the represented user's permissions, with zero privilege escalation_
- [ ] _100% of A2A-initiated state changes are confirmed + audited_
- [ ] _Approval-required actions correctly route to and execute only via the approver_

---

## 8. Dependencies

**What this component needs:**

| Depends on | What we need | Blocking? |
|-----------|-------------|----------|
| [[agent-access-layer]] | Tool surface, MCP server, server-side validation, approval routing | **Yes** |
| AI-specific permission config | Org/user permission mirror for non-Console access (new build) | **Yes** |
| Combined audit store | Attribution of agent + user actions | No — extends existing audit |
| A2A protocol standard | A stable protocol to implement against | No — track and adopt |

**What other components need from this one:**
- [[full-agentic-experience]] references the A2A endpoint as the external door to the same capabilities; the A2A endpoint is a sub-component of [[agent-access-layer]] (not of the full agentic experience).

---

## 9. Priority

_Phasing out of scope. Scope here is inferred from the vision + access-layer session (not a dedicated deep-dive); Concept 3 is the destination of the trust spine per [[vision]]._

---

## 10. Risks

**Abuse vectors:**
- **Permission escalation / scope abuse** — an external agent sending misleading framing to act beyond its user's rights; mitigated by server-side validation + least privilege.
- **Approval-queue bypass** — the endpoint must not let an agent self-approve or impersonate an approver.
- **Cross-tenant leakage** — an agent for Client A must never reach Client B's data.

**Data risks:**
- Acting on stale state; impact estimates computed before a write settles.

**Compliance:**
- Audit sufficiency for agent-initiated actions; PII handling in agent context; data residency for external agent traffic (see [[vision]] §8).

**Controls needed:**
- Least-privilege identity mapping; prompted-trust + approval enforcement; server-side validation; full attribution/audit; tenant isolation.

---

## Sub-Components

_Not separately documented — the A2A endpoint hasn't been deep-dived. The aspects surfaced so far (agent-to-agent protocol surface, identity/permission scoping, prompted-trust + approval routing, audit) are described inline above and inherit the [[agent-access-layer]] mechanisms. They'll be decomposed if/when A2A gets its own session._
