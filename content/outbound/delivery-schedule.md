---
description: "The Outbound Workforce delivery schedule: the session series, the technical deliverability build, domain warming and the platform setup sessions"
---

# Outbound Workforce — Delivery Schedule

> **Section:** [[outbound]] · **Index:** [[index]] · **Sibling engagement:** [[content-workforce]] · **Delivery:** [[delivery]]

Where [[outbound]] holds TXN's GTM corpus and the ICP and persona reconciliation, this page holds **the schedule**: what session happens when, the technical build behind the sending domains, and the channel decisions.

The Outbound Workforce is a **separate engagement** from the agentic AI layer, contracted under the GTM Workforces proposal and running in parallel with [[content-workforce]]. Brett was explicit at the first session that the two are not to be merged: *"I'm not going to use this as the content workforce session, we can do this in parallel."*

## What is being built

| Output | What it is | Status |
|--------|-----------|--------|
| **The offer** | Tagline, value proposition, pricing model, positioning guardrails. The factual-claims universe everything else draws on | **Closed** in session 1, 24 August. See [[2026-08-24-outbound-workforce-interview-1-offer]] |
| **The ICPs** | Tiered, signal-based company targets, doubling as the grading rubric for the lead database | **Held 25 August** and extracted in full: [[icp-definition]], [[prospecting-process]], [[qualification-matrix]], [[discovery-sources]] and the three persona scaffolds |
| **Buyer personas** | Who the agents speak to and how, per ICP | **In progress**, two sessions on 27 August |
| **Deliverability** | DKIM, DMARC and SPF on TXN's sending domains, then warming | **Not started.** Next week, w/c 1 September. Blocked on Jacob's contact details |
| **Five agents** | Configured on TXN's ICP and messaging. **Email and LinkedIn only**, no voice | Not started. The proposal calls week 2 the heavy week |

## Session schedule

| Date | Session | State |
|------|---------|-------|
| Mon 24 Aug | Interview 1: the offer | **Held.** George attended as it was the foundational session |
| Tue 25 Aug | Interview 2: ICPs | **Held and extracted.** Corpus loaded, 126-account register analysed at [[qualification-matrix]] |
| Thu 27 Aug | Interview 3: the offer, session 2 | **Held.** [[2026-08-27-outbound-workforce-offer-session-2]] |
| **Wed 2 Sep** | **Session 4** | **Booked** |
| **Fri 4 Sep** | **Session 5** | **To book.** Brett has asked Dorte to try for Friday |
| **w/c 1 Sep** | **Technical: email domains and warming**, with Jacob | **To book.** Starts the two-week clock |
| **w/c 1 Sep** | **Team login and platform setup** | **To book** |

**Two more sessions are needed and one is booked.** Per Brett, 28 August: the Wednesday session is in the diary, and Friday would be the ideal slot for the second. That closes the interview series before the personal Content Workforce sessions start the following week.

## Channels: email and LinkedIn only, no voice

**TXN is not doing outbound calls.** Confirmed 27 August, and consistent with what Ian said on 24 August: he ruled out **AI outbound voice** on regulatory grounds, and Novosapien's **inbound** voice capability was declined in the same conversation, *"that inbound lead needs to be picked up by a human at TXN rather than any kind of voice call from AI"*. Recorded in [[commercial]] since 25 August; this section makes it the settled channel position rather than a note in a list.

The Workforce runs on **email and LinkedIn**. Emails send from **named individuals on a secondary domain** rather than a generic TXN address, initially all from Ian and later split by territory. LinkedIn is capped at **200 outreaches per week**.

> **Handled quietly on the client-facing flight plan, by decision (27-08).** Voice has been taken out of the schedule, the agent configuration step and the go-live definition without a change note. It was never something TXN asked for, so flagging its removal would invent a scope conversation rather than record one.

**Two loose ends this leaves in the paperwork**, neither urgent, both worth closing before signature:

| Where | What it says | Why it matters now |
|-------|-------------|--------------------|
| GTM Workforces Order, clause 8.2 | Novosapien is responsible for screening **UK voice calls against TPS and CTPS**, for the **voice agent disclosing at the start of each call** that it is an AI calling on behalf of TXN under Regulation (EU) 2024/1689, and for call recording rules by jurisdiction | The Order is not signed. These are obligations for a channel that will not run. Leaving them in creates a compliance surface with nothing behind it, and invites a reviewer question that has no good answer |
| [[commercial]], Outbound pricing | Usage pass-through is listed as Claude compute, Apollo lead data and **ElevenLabs voice**, at billed cost plus an administration fee | The ElevenLabs line is now obsolete. Small, but it is a stated cost component in a priced structure |

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
- **The AI layer is bundled into TXN's own licence fee**, per Ian on 24 August. Commercially material to Novosapien.
- Register rows: [[open-questions]] #57 on the single committer, #63 on the September calendar.
