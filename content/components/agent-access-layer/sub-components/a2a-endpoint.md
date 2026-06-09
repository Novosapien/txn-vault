---
component: "[[agent-access-layer]]"
status: Defined
sources:
  - "[[13-05-2026-txn-vision-meeting]]"
  - "[[01-06-2026-component-1-Agent-Access-Layer]]"
  - "[[29-05-2026-stackworkz-meeting]]"
  - "[[05-06-2026-component-4-full-agentic-experience]]"
---

# TXN — A2A Endpoint (external edge)

> **Component:** [[agent-access-layer]] · **Vision:** [[vision]]
> **User journeys:** [[ux-ai-transaction-query|Transaction Query (read)]], [[ux-ai-user-stories-mapping|API Actions (write)]] — see [[user-journeys]]
> **Date:** 2026-06-05
> **Status:** Defined
> **Owner:** _TBC_
> **Sources:** [[13-05-2026-txn-vision-meeting]] (Concept 3 / A2A), [[01-06-2026-component-1-Agent-Access-Layer]] (permission scoping, approval, audit), [[29-05-2026-stackworkz-meeting]] (external agents), [[05-06-2026-component-4-full-agentic-experience]] (expose-the-agent mechanism)

---

## 1. What Does This Sub-Component Do?

**Functional purpose:**

The A2A Endpoint is the **external edge of the [[agent-access-layer]]** — its agent-to-agent face. Where the rest of the access layer is the *internal* core that TXN's own agents ([[co-pilot]], [[agent-inbox-alerts]], [[full-agentic-experience]]) call directly, this sub-component is the *inbound* door through which a client's *own* agent (or an LLM like Claude in the client team's hands) reaches the same capabilities on behalf of a human user, over standard agent-to-agent protocols. It is the destination end of the trust spine (Concept 3). It matters because it is how a whole class of clients will prefer to integrate — TXN's CEO Ian Johnson noted that many clients will run their own AI over the data TXN gives them, and Mike Moores (TXN's CTO) raised the explicit case of *"what if I want my whole business to work with your agent, agent-to-agent."* It is the most security-critical line in the access layer: the boundary where traffic crosses in from *outside* the tenant.

The endpoint exposes the same capabilities the rest of the AI layer uses — it rides on the tool surface and MCP server of the [[agent-access-layer]] — but adds the agent-to-agent protocol, identity, and scoping needed for an external agent to be trusted. The load-bearing rule is that an external agent **gets exactly the permissions of the human user it represents, and no more**. Because TXN's permission model was designed around the Console, an external/agent-to-agent consumer needs an **AI-specific permission configuration** that mirrors the granular Console permissions (there is no such API today — see [[agent-access-layer]]).

**Expose the agent, not the tools.** This is the core architecture decision the deep-dive resolved ([[05-06-2026-component-4-full-agentic-experience]]). The common approach — hand the client a raw MCP server and let their Claude call the tools directly — is **deliberately rejected** for TXN. George Westbrook's reasoning: raw tool exposure carries none of the context that makes TXN safe — "how things should be done, what the impacts are" — so "just exposing MCP tools is not going to be good enough." Instead, TXN exposes its **agent**, which carries the skills, ways-of-working, approval layers, and impact-awareness, and the external agent talks *to that agent*. Two mechanisms deliver this:

- **Preferred — A2A:** the client's agent (e.g. Claude) speaks to the **TXN agent over A2A**; the TXN agent executes the [[agent-access-layer]] MCP tools behind its own guard rails and replies. This depends on providers shipping direct A2A connections (assumed to be coming for the major providers).
- **Fallback — MCP-as-message (available today):** TXN's agent is wrapped and exposed to the client's Claude *as MCP tools*. When Claude wants to (say) update a setting, it sends a payload to the MCP server, which is passed as a **user message into the TXN agent** — the agent (not Claude) does the work and replies back. The client agent never touches raw tools directly.

Ian's mental model for the target is the agentic e-commerce / travel-booking experience inside Claude (find hotel → "best price, shall I book?" → complete) — "something similar, of a TXN flavour." Rendering generative UI back into the client's Claude is *possible* but "not in exactly the same way" as TXN's own [[full-agentic-experience]] surface — the rich rendering is for TXN-hosted surfaces.

Critically, **the agentic shortcut does not bypass TXN's safeguards**. Ian was firm that "if it's agent-to-agent we don't care, we'll just do whatever's asked" is *not* the model — the same **prompted-trust** confirmation, impact information, **approval queue**, and **audit trail** that protect a Console user apply to an external agent. The whole proposition is that TXN helps non-experts avoid costly mistakes; abandoning that for A2A would undermine it. Approvals can themselves be **agent-mediated**: where an action needs sign-off, the request routes to the named approver (or their agent), who confirms, and only then does it execute. Because the request lands as a message to the *TXN agent*, those safeguards are enforced agent-side regardless of which mechanism (A2A or MCP-as-message) the client uses.

```
A2A Endpoint
├── Agent-to-agent protocol     (external agent → TXN agent: A2A preferred, MCP-as-message fallback)
├── Identity & scoping           (maps the agent to its human user's permissions)
├── Prompted-trust + approval    (confirm / impact / approval-queue still enforced, agent-side)
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
| Agent exposure (preferred) | Build / Access | External agent → **TXN agent over A2A** → TXN agent executes [[agent-access-layer]] MCP tools → replies | Expose the agent (with skills, approval layers, impact-awareness), not raw tools; depends on provider A2A enablement |
| Agent exposure (fallback, today) | Build | Wrap TXN agent **as MCP tools**; client Claude's payload passed as a **user message** to the TXN agent | Works now without provider A2A support; client agent never calls raw tools directly |
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
| Provider A2A enablement | Major providers (e.g. Anthropic) shipping direct A2A connections | No — MCP-as-message fallback carries it until then |
| TXN agent | The agent that gets exposed (shared with [[full-agentic-experience]]) | **Yes** — A2A exposes the agent, not raw tools |

**What other components need from this one:**
- [[full-agentic-experience]] relies on this edge as the external door to the same capabilities — it and this edge share the **"expose the agent, not the tools"** mechanism (TXN's own agent surface and the inbound external door, one mechanism).

---

## 9. Priority

_Phasing out of scope for this exercise — full scope captured. (Concept 3 is the destination of the trust spine per [[vision]]; included in full.)_

---

## 10. Risks

**Abuse vectors:**
- **Permission escalation / scope abuse** — an external agent sending misleading framing to act beyond its user's rights; mitigated by server-side validation + least privilege.
- **Approval-queue bypass** — the endpoint must not let an agent self-approve or impersonate an approver.
- **Cross-tenant leakage** — an agent for Client A must never reach Client B's data.
- **Raw-tool exposure temptation** — shipping a plain MCP tool server (skipping the TXN agent) would strip the impact-awareness and approval layers; explicitly rejected in favour of exposing the agent.

**Delivery risks:**
- **Provider A2A enablement** — the preferred path depends on providers supporting A2A; the MCP-as-message fallback must carry the experience until that lands.

**Data risks:**
- Acting on stale state; impact estimates computed before a write settles.

**Compliance:**
- Audit sufficiency for agent-initiated actions; PII handling in agent context; data residency for external agent traffic (see [[vision]] §8).

**Controls needed:**
- Least-privilege identity mapping; prompted-trust + approval enforcement; server-side validation; full attribution/audit; tenant isolation.

---

## Shared machinery

This edge does not own its own copies of identity, approval, or audit — those are the [[agent-access-layer]]'s sub-components, reused. What is *distinct* to this edge is only the **agent-to-agent protocol surface** (A2A-preferred, MCP-as-message fallback) and the **external trust boundary**. Everything else is shared:

| Concern | Where it lives | This edge adds |
|---------|---------------|----------------|
| Tool execution & validation | [[mcp-server]] | The external agent talks to the *TXN agent*, which calls the MCP server — it never touches raw tools |
| Identity & permission scoping | [[permission-scoping]] | Maps an *external* agent → its represented user's permissions (same AI-permission config) |
| Prompted-trust & approval | [[approval-queue-integration]] | Same confirmation + approval-queue, enforced agent-side regardless of A2A vs MCP-as-message |
| Audit & attribution | [[audit-attribution]] | Attributes the action to the external agent *and* the user it represents |
