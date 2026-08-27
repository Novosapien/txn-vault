---
description: "Hub for the TXN Outbound Workforce engagement: the interview schedule, the technical deliverability build, domain warming and the platform setup sessions"
---

# TXN — Outbound Workforce

> **Index:** [[index]] · **Commercial:** [[commercial]] · **Sibling engagement:** [[content-workforce]] · **Delivery:** [[delivery]]

The Outbound Workforce is a **separate engagement** from the agentic AI layer, contracted under the GTM Workforces proposal and running in parallel with [[content-workforce]]. Brett was explicit at the first session that the two are not to be merged: *"I'm not going to use this as the content workforce session, we can do this in parallel."*

This section tracks the configuration work and the technical build behind it.

## What is being built

| Output | What it is | Status |
|--------|-----------|--------|
| **The offer** | Tagline, value proposition, pricing model, positioning guardrails. The factual-claims universe everything else draws on | **Closed** in session 1, 24 August. See [[2026-08-24-outbound-workforce-interview-1-offer]] |
| **The ICPs** | Tiered, signal-based company targets, doubling as the grading rubric for the lead database | **Held 25 August**, no record in the vault yet |
| **Buyer personas** | Who the agents speak to and how, per ICP | **In progress**, two sessions on 27 August |
| **Deliverability** | DKIM, DMARC and SPF on TXN's sending domains, then warming | **Not started.** Next week, w/c 1 September. Blocked on Jacob's contact details |
| **Five agents** | Configured on TXN's ICP and messaging, custom voice trained | Not started. The proposal calls week 2 the heavy week |

## Session schedule

| Date | Session | State |
|------|---------|-------|
| Mon 24 Aug | Interview 1: the offer | **Held.** George attended as it was the foundational session |
| Tue 25 Aug | Interview 2: ICPs | **Held.** No transcript in the vault yet |
| Thu 27 Aug | Interview 3: buyer personas | **Booked** |
| **Thu 27 Aug** | **Interview 4: second block, same day** | **Booked.** Takes the slot vacated by the Content Workforce session that moved to 1 September. Most likely a continuation of the persona set, since every session in this series has over-run; **confirm the subject before the session** |
| **Next week, w/c 1 Sep** | **Technical: email domains and warming** | **To book.** With **Jacob**, who runs TXN's domains. Sets up the sending domains, DKIM, DMARC and SPF, and **starts the warming clock the same week**. Monday 31 August is the UK summer bank holiday, so the week runs Tuesday to Friday |
| **Next week, w/c 1 Sep** | **Team login and platform setup** | **To book.** Gets the TXN team into the Outbound Workforce platform and set up |

## Domain warming is the binding clock

**Warming takes roughly two weeks of elapsed time and cannot be compressed.** Sending too much too early damages deliverability on the domain permanently, so the only lever is when it starts.

Starting **next week** puts the domain live around **mid September**. That matters more than it looks: the Novosapien team flies on the evening of **10 September** for a three-week retreat, so warming started now runs its clock **during** the travel rather than after it. Held until after pilot acceptance closes, realistically it would not start until around 10 September and would finish around 24 September, roughly a week and a half later for no gain.

> **This supersedes the recommendation in the 25 and 26 August flight plans**, which was to hold domain setup and warming until after 7 September on capacity grounds. That recommendation was right about the capacity cost and wrong about the ordering, because it treated warming as work rather than as an unattended clock. **Decision taken 27 August: start it next week.**

**The one condition that keeps it safe.** The session lands five or six days before pilot completion, and it draws on George, who is the only person committing to any of the four pilot build repositories ([[open-questions]] #57). Scope it tightly: **Jacob owns the DNS records**, George specifies and verifies. It is a bounded session, not an open task that runs through acceptance week.

## Nothing sends before the market announcement

The agreed launch sequence puts Direct Transact and Pay Corp channels first, then the personal networks of Ian, Michael and Dorte, and only then TXN's own outbound. Warming is preparation for that sequence, not a start to it. There is no scenario in which an email goes to a prospect during the pilot's acceptance window.

## People

| Who | Role in this engagement |
|-----|------------------------|
| Ian Johnson | The voice on the offer, positioning and pricing |
| Dorte Dye | Coordinates scheduling and inputs |
| Jacob | Runs TXN's domains. Needed for the deliverability build. **Surname, contact and employer all unknown**, see below |
| Max Kingaby | Runs the configuration sessions |
| George Westbrook | Email configuration and domain warming, assigned 24 August. Also the sole committer on the pilot build |

## Open

- **When does the 30-day go-live clock start?** Both GTM proposals carry a 30-day go-live guarantee and neither engagement has a stated start date on the record. The interviews have been running ahead of one.
- **Who is Jacob?** He is named once, in the 24 August session, when Brett asked *"who runs your domains?"* and Dorte answered *"Jacob."* That is the entire record. **No surname, no email, and no confirmation of whether he sits inside TXN, at Pay Corp, or with an outsourced IT provider.** The domain session cannot be booked without it, and it is the gating step on a two-week clock that is meant to start next week. Ask Dorte.
- **The ICP session has no vault record.** Held 25 August, nothing captured.
- **The AI layer is bundled into TXN's own licence fee**, per Ian on 24 August. Commercially material to Novosapien.
- Register rows: [[open-questions]] #57 on the single committer, #63 on the September calendar.
