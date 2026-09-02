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
| **Deliverability** | DKIM, DMARC and SPF on TXN's sending domains, then warming | **Still not started as of 2 September**, against a w/c 1 September plan. Sizing is now settled at **four or five domains**; the blocker moved from Jacob's contact details to **George owing Brett the domain hierarchy list** |
| **Five agents** | Configured on TXN's ICP and messaging. **Email and LinkedIn only**, no voice | Not started. The proposal calls week 2 the heavy week |

## Session schedule

| Date | Session | State |
|------|---------|-------|
| Mon 24 Aug | Interview 1: the offer | **Held.** George attended as it was the foundational session |
| Tue 25 Aug | Interview 2: ICPs | **Held and extracted.** TXN's own GTM corpus loaded, the 126-account scored register analysed at [[qualification-matrix]], and a discovery source research pass recorded at [[discovery-sources]] |
| Thu 27 Aug | Interview 3: buyer personas | **Booked** |
| **Thu 27 Aug** | **Interview 4: second block, same day** | **Booked.** Takes the slot vacated by the Content Workforce session that moved to 1 September. Most likely a continuation of the persona set, since every session in this series has over-run; **confirm the subject before the session** |
| Tue 2 Sep | Additional interview: qualification and the ICPs | **Held, did not finish.** Three ICP gating rules overturned. See [[2026-09-02-outbound-workforce-icp-qualification]] |
| **w/c 1 Sep** | **Technical: email domains and warming** | **Slipped.** Still unbooked on 2 September. With **Jacob**, who runs TXN's domains. Sets up the sending domains, DKIM, DMARC and SPF, and **starts the warming clock the same week**. Monday 31 August was the UK summer bank holiday, so the week runs Tuesday to Friday and half of it is already gone |
| **Next week, w/c 1 Sep** | **Team login and platform setup** | **To book.** Gets the TXN team into the Outbound Workforce platform and set up |

## The sending domains

Sizing settled on 2 September ([[2026-09-02-outbound-workforce-icp-qualification]]). Ownership did not.

| Item | Position |
|------|----------|
| Email addresses | **15 to 16**, carried forward from the earlier plan |
| Addresses per domain | **Three** |
| Domains needed | **Four or five** |
| Shape | Variations on the primary, *"things like um this is txn.com, those kind of domains"* |
| Who buys them | **Open.** Novosapien can create them, or TXN purchases directly |

**The blocker is internal to Novosapien.** Brett: *"I need to just chase George. He needs to send that to me."* Dorte has now asked for the domain hierarchy twice, on 1 and 2 September, and she cannot make the buy-or-be-supplied decision without it: *"I just need to have the full picture till we can say we go either way and then we can talk to the other guys."*

So a two-week clock that the vault has argued since 27 August should start immediately is waiting on a list one person owes another inside our own team. That is the cheapest item on the critical path and the one holding it up.

## Domain warming is the binding clock

**Warming takes roughly two weeks of elapsed time and cannot be compressed.** Sending too much too early damages deliverability on the domain permanently, so the only lever is when it starts.

Starting **next week** puts the domain live around **mid September**. That matters more than it looks: the Novosapien team flies on the evening of **10 September** for a three-week retreat, so warming started now runs its clock **during** the travel rather than after it. Held until after pilot acceptance closes, realistically it would not start until around 10 September and would finish around 24 September, roughly a week and a half later for no gain.

> **This supersedes the recommendation in the 25 and 26 August flight plans**, which was to hold domain setup and warming until after 7 September on capacity grounds. That recommendation was right about the capacity cost and wrong about the ordering, because it treated warming as work rather than as an unattended clock. **Decision taken 27 August: start it next week.**

**The one condition that keeps it safe.** The session lands five or six days before pilot completion, and it draws on George, who is the only person committing to any of the four pilot build repositories ([[open-questions]] #57). Scope it tightly: **Jacob owns the DNS records**, George specifies and verifies. It is a bounded session, not an open task that runs through acceptance week.

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
- **Warming has slipped and nothing has replaced the plan.** [[open-questions]] #64 counts eight working days to carry three engagements and an acceptance, and the domain session was the one item in it that runs unattended once started. It is now 2 September, the session is unbooked, and the clock has not begun.
- Register rows: [[open-questions]] #57 on the single committer, #63 on the September calendar, #64 on the September window.
