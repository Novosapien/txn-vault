---
description: "The Outbound Workforce delivery schedule: the session series, the technical deliverability build, domain warming and the platform setup sessions"
---

# Outbound Workforce: Delivery Schedule

> **Section:** [[outbound]] · **Index:** [[index]] · **Sibling engagement:** [[content-workforce]] · **Delivery:** [[delivery]]

Where [[outbound]] holds TXN's GTM corpus and the ICP and persona reconciliation, this page holds **the schedule**: what session happens when, the technical build behind the sending domains, and the channel decisions.

The Outbound Workforce is a **separate engagement** from the agentic AI layer, contracted under the GTM Workforces proposal and running in parallel with [[content-workforce]]. Brett was explicit at the first session that the two are not to be merged: *"I'm not going to use this as the content workforce session, we can do this in parallel."*

## What is being built

| Output | What it is | Status |
|--------|-----------|--------|
| **The offer** | Tagline, value proposition, pricing model, positioning guardrails. The factual-claims universe everything else draws on | **Closed** in session 1, 24 August. See [[2026-08-24-outbound-workforce-interview-1-offer]] |
| **The ICPs** | Tiered, signal-based company targets, doubling as the grading rubric for the lead database | **Held 25 August** and extracted in full: [[icp-definition]], [[prospecting-process]], [[qualification-matrix]], [[discovery-sources]] and the three persona scaffolds |
| **Buyer personas** | Who the agents speak to and how, per ICP | **Moved offline 2 September.** No longer a workshop: Brett runs the build as a heavy lift, roughly half an hour of processing per persona, delivered as one HTML artifact for asynchronous review |
| **Deliverability** | DKIM, DMARC and SPF on TXN's sending domains, then warming | **Still not started on 3 September**, against a w/c 1 September plan. Sizing settled at **four or five domains**; the blocker has moved from Jacob's contact details to **the domain hierarchy list George owes Brett** |
| **Five agents** | Configured on TXN's ICP and messaging. **Email and LinkedIn only**, no voice | Not started. The proposal calls week 2 the heavy week |

## Session schedule

| Date | Session | State |
|------|---------|-------|
| Mon 24 Aug | Interview 1: the offer | **Held.** George attended as it was the foundational session |
| Tue 25 Aug | Interview 2: ICPs | **Held and extracted.** Corpus loaded, 126-account register analysed at [[qualification-matrix]] |
| Thu 27 Aug | Interview 3: the offer, session 2 | **Held.** [[2026-08-27-outbound-workforce-offer-session-2]] |
| **Wed 2 Sep** | **Session 4: qualification and the ICPs** | **Held, did not finish.** [[2026-09-02-outbound-workforce-icp-qualification]]. Three ICP gating rules overturned; the session then degraded and Brett ended it to restart in a fresh context window |
| Thu 3 Sep | Session 5: the four statuses | **Held.** Took the Content Workforce slot. [[2026-09-03-outbound-workforce-icp-statuses]]. The ICPs are closed; personas run offline from here |
| **w/c 1 Sep** | **Technical: email domains and warming**, with Jacob | **Slipped.** Still unbooked on 3 September. Starts the two-week clock, so every day of delay is a day of elapsed time that cannot be recovered |
| **w/c 1 Sep** | **Team login and platform setup** | **To book** |

**The interview series is effectively closed.** Both sessions happened, on 2 and 3 September, and the second took the Content Workforce slot rather than a Friday one. What remains is offline: Brett builds the ICPs and personas as one artifact for asynchronous review. **The cost sits on the other engagement**, where the pillars and brand entity have now moved four times ([[content-workforce]]).

## The sending domains

Sizing settled on 2 September ([[2026-09-02-outbound-workforce-icp-qualification]]). Ownership did not.

| Item | Position |
|------|----------|
| Email addresses | **15 to 16**, carried forward from the earlier plan |
| Addresses per domain | **Three** |
| Domains needed | **Four or five** |
| Shape | Variations on the primary, *"things like um this is txn.com, those kind of domains"* |
| Who buys them | **Open.** Novosapien can create them, or TXN purchases directly |

**The blocker is inside Novosapien, not at TXN.** Brett, 2 September: *"I need to just chase George. He needs to send that to me."* **Still outstanding on 3 September**, and now explicitly late: *"George was meant to write it up last night for me, were all the various instructions around the domains"* ([[2026-09-03-outbound-workforce-icp-statuses]]). Three days lost on a two-week clock. Dorte has asked for the domain hierarchy twice and cannot make the buy-or-be-supplied decision without it: *"I just need to have the full picture till we can say we go either way and then we can talk to the other guys."*

So a two-week clock the vault has argued since 27 August should start immediately is waiting on a list one person owes another inside our own team. It is the cheapest item on the critical path and the one holding it up.

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
- **Warming has slipped and nothing has replaced the plan.** [[open-questions]] #64 counts eight working days to carry three engagements and an acceptance, and the domain session was the one item in it that runs unattended once started. It is now 3 September, the session is unbooked, and the clock has not begun.
- Register rows: [[open-questions]] #57 on the single committer, #63 on the September calendar, #64 on the September window.
