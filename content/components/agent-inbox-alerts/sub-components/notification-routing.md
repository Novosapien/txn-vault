---
component: "[[agent-inbox-alerts]]"
status: Defined
sources:
  - "[[02-06-2026-component-2-alerts-agent-inbox]]"
  - "[[2026-09-08-agentic-standup]]"
description: "Spec for the alert delivery last mile — routing composed items to the Stackworkz central hub, channel preferences and in-context dashboard-dot surfacing"
---

# TXN — Notification Routing

> **Component:** [[agent-inbox-alerts]] · **Journey source:** [[ux-ai-configurable-operational-alerting|Operational Alerting]]
> **Date:** 2026-06-02
> **Status:** Defined
> **Owner:** _TBC_
> **Sources:** [[02-06-2026-component-2-alerts-agent-inbox]]

---

## 1. What Does This Sub-Component Do?

**Functional purpose:**

Notification routing is the last mile — it takes a composed alert, report, or insight and gets it to the user **where they are**. Mike Moores (TXN's CTO) was firm that TXN wants a **central notification hub**: one place where *anything* can raise something for a user — the AI, DT, or the Console — delivered to the user's **preferred channel** (in-console, Slack, Teams, email). The principle is *meet people where they are.*

The ownership split: **Stackworkz owns notification preferences and the actual sending**; this sub-component is the AI side that **routes** an already-composed item (from [[ai-analysis-impact]] / [[scheduled-reporting]]) to the hub with the right channel. Beyond push channels, surfacing can also be **in-context** — Brett's idea of an AI recommendation as a "dot" on a dashboard metric, explaining *why* it spiked or dropped. As the deep-dive put it, the job is delivering *"insight packaged at the right time"* — sometimes an alert, sometimes a notification, sometimes an embedded annotation.

**Entities that interact with it:**

- **Agent** — composes and routes the item
- **The central notification hub / Stackworkz delivery** — sends to the channel
- **The user** — receives in their preferred channel or sees it embedded in the UI
- **Other sources** — DT and the Console can also feed the hub

---

> [!important] The true agent inbox, proposed 8 September 2026
> The answer to *"how does a silent agent tell you anything?"* ([[open-questions]] #84), proposed by George and refined by Dorte on the same call ([[2026-09-08-agentic-standup]]).
>
> **Two surfaces, not one.** The existing **alerts inbox** carries things the system noticed. A new **true agent inbox** carries work the user asked for: *"I've done this piece of work for you, this is what I've done"*, or *"I need this help here."*
>
> The framing is a positioning statement as much as a design one: *"rather than everything being like what everyone else is doing, where here's this chat interface and this is the only way you can interface with the agents, is having that kind of **true digital worker experience**... it's just a bit easier to see rather than having to click into a chat and read it."*
>
> **That is the direct answer to Ian's objection** ([[process-surfacing]]): the alternative to narrating every step is not silence, it is reporting on completion.
>
> **Dorte's addition, and her own guard on it.** She proposed a popup while the user is already in the console, flashing done or needs help with a link through to detail. George extended it to separate system and agent notification streams with an unread count. She then constrained it immediately: *"we just need to be mindful that we're not over complicating it, because it might be a number of different things coming in. It's like you lose the plot where you actually are. What is really important?"*
>
> **So the requirement is not "notify me", it is "tell me what matters."** Read with her 03-09 rule, *"I get really impatient if nothing explains why I'm waiting"*, her position is consistent across both sessions: **explain a block, report a completion, narrate nothing else.**
>
> **Sequencing.** The notification is one event and its placement is a separate decision: *"all it needs to do is emit a message when it's done. It's just a matter of where we're going to put it. If it's in the chat, it's just sending the chat message back. In the agent inbox, same thing."* So the backend can be built before the routing is settled.

## 2. What Needs to Happen?

**Functional requirements:**

- Take the already-composed item (alert / report / insight) and prepare it for delivery.
- Resolve the user's **preferred channel** from Stackworkz notification preferences.
- Hand off to the **central hub** for delivery (console / Slack / Teams / email).
- Support **in-context surfacing** — e.g. a dashboard "dot" with an explanation — as an alternative to a push.
- Accept items from **any source** (AI / DT / Console) into the same hub.

**Business rules:**

- **Meet people where they are** — deliver to the chosen channel, not only in-console.
- **Action or silence** — only route items that carry an action or insight.
- **Stackworkz delivers; we route** — respect the ownership split.

**Edge cases:**

- No channel preference set → sensible default (in-console).
- An item surfaces in-context (dashboard dot) **or** as a push — chosen per item. _[⚠ open — see [[open-questions]] #15]_
- Delivery failure on a channel → fall back / retry; don't silently drop.

---

## 3. Entity Journeys

### 3b. Cross-Component Journeys

#### Journey 1: Route a surfaced item to the user's channel

**Entity:** Agent → central notification hub (Stackworkz delivery)

**Input:** A composed alert, report, or insight from [[ai-analysis-impact]] / [[scheduled-reporting]].

**Handoff point:** Crosses into the **central notification hub / Stackworkz delivery** — state passed: the composed item + resolved channel. Stackworkz performs the actual send.

**Components involved:** Agent Inbox & Alerts → central hub (Stackworkz) → user channel

**Outcome:** The right item reaches the user in their preferred channel (or is embedded in the UI), at the right time.

**Steps:**

```mermaid
graph TD
    A[Composed item: alert / report / insight] --> B[Resolve preferred channel - Stackworkz prefs]
    B --> C{Surfacing mode}
    C -->|push| D[HANDOFF: central hub delivers to channel]
    C -->|in-context| E[Embed as dashboard dot + explanation]
    D --> F[Delivered: console / Slack / Teams / email]
    E --> F
    F --> G[RETURN: delivery status]
    G --> H{Delivered?}
    H -->|no| I[Fallback / retry — not silently dropped]
    H -->|yes| J[Done]
```

**Acceptance criteria:**
- [ ] An item is delivered to the user's preferred channel.
- [ ] The hub accepts items from any source (AI / DT / Console).
- [ ] In-context surfacing (dashboard dot + explanation) is available as an alternative to a push.
- [ ] Delivery failures fall back / retry rather than dropping silently. _[⚠ open — see [[open-questions]] #7]_
- [ ] Only items carrying an action or insight are routed.

---

## 5. Data Requirements

| What | Direction | Description | Source / Destination |
|------|-----------|------------|---------------------|
| Composed item | In | Alert / report / insight to deliver | [[ai-analysis-impact]] / [[scheduled-reporting]] |
| Channel preference | In | The user's preferred channel | Stackworkz notification preferences |
| Delivery payload | Out | Item + channel | → central hub (Stackworkz) |
| Delivery status | In | Success / failure for fallback | Central hub |

---

## 6. Dependencies

| Depends on | What we need | Blocking? |
|-----------|-------------|----------|
| Stackworkz notification system | Preferences + actual delivery to channels | **Yes** (cross-component) |
| Central notification hub | A single intake any source can feed | **Yes** |
| Console dashboard | Surface for in-context "dot" insights | No — push-only fallback |

**What siblings/other components need from this one:**
- [[ai-analysis-impact]] and [[scheduled-reporting]] deliver through here.

---

## 7. Risks

**Specific risks:**
- Alert fatigue if too much is routed (counter with the action-or-silence bar).
- Silent delivery failure — user misses a critical item.
- Inconsistent experience across channels.

**Controls to build into the journeys:**
- Action-or-insight gate before routing.
- Delivery-status check with fallback/retry.
- Honour user channel preferences; sensible default.

---

## 8. Priority

_Phasing out of scope. Relative note: depends on the Stackworkz notification system + the central-hub contract; in-console delivery is a viable first surface while other channels mature._

---

## Sub-Sub-Components

Leaf node — no further decomposition needed.
