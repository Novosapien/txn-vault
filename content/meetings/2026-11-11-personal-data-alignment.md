---
date: 2026-11-11
type: general
description: "Personal data on the Knowledge Hub and the AI layer: the random ID is dropped beyond 72 hours, IP stays in Front Door only, and Ian needs two agreements signed"
scope:
  - "[[developer-support]]"
  - "[[architecture]]"
  - "[[commercial]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[portal-co-pilot]]"
  - "[[architecture]]"
  - "[[commercial]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Personal data on the Knowledge Hub and the AI layer (2026-11-11)

> **Source:** transcript, 11 November 2026, a Wednesday. **Novosapien:** Brett StClair, George Westbrook. **Stackworx:** Ruan Sunkel, Armand Pretorius. **TXN:** Ian Johnson, Michael Moores, Dörte Dye.
>
> **The call that settles the data position five days before launch.** It was called to work through a long email from TXN's lawyers about what personal data the Knowledge Hub and the AI layer touch. Ian ran it, set a risk-based posture, and closed the open design question on the chat identifier. It ends with the commercial conversation: there is still no signed agreement and no data processing agreement, and he now wants two of them in place.

## The data map, as it actually is

| Data | Where it lives | How long | Who can reach it |
|---|---|---|---|
| **Visitor IP address** | Azure Front Door logs only | **30 days** | Hosted in Europe. Novosapien could reach the Front Door logs if it chose to; there is no reason to |
| **Random ID** | The visitor's browser, linking them to their chat history | Session-length, once the change below lands | Nobody outside the browser |
| **Chat content** | The agent's own store | **72 hours** | Europe |
| **Sanitised chat content** | The long-term store | As long as it is useful | Europe, with the random ID stripped |

**The IP address never reaches the model.** George confirmed it directly: the only reason the IP exists at all is Azure Front Door. It is not submitted to any model and no model provider sees it.

**Why Novosapien would ever want the IP:** rate limiting per visitor on a surface with no sign-in. That is code reading the value, not a person reading a log.

## Ian's test, and his posture

**The test he applies throughout:** for GDPR there are two questions, **where is it stored** and **can anyone outside Europe access it**. Once someone outside Europe can reach it, the storage location stops mattering. Everything here is stored in Europe.

**His posture on the lawyers' email is a ruling, not a mood.** Personal data is not asked for anywhere, the acceptable use policy will say so, and if someone enters it anyway nothing is done with it. He will push back rather than engineer around a hypothetical:

- Finding out who an IP belongs to would mean approaching the internet provider, with no business reason to do it.
- Nobody can promise that no one could ever access anything. The control is what access is granted, and a breach of that is handled by the agreement that governs it.
- He described the wider exercise as a sledgehammer to crack a nut, and asked for a **risk-based approach**.

**And a practical point that lowers the risk on the sandbox:** the APIs do not require cardholder name or address. A completely blank cardholder can be created, so a visitor testing the sandbox need never enter a personal detail.

## The decision: the random ID is dropped from anything kept beyond 72 hours

**Ian settled it in one line.** Retaining chat history beyond 72 hours is fine in isolation **as long as the random ID attached to that chat is dropped**. The random ID exists only to let a visitor return to their own chat; it adds nothing to the purpose the long-term store exists for.

**That purpose, as George described it:** run a model across the stored chats to read the sentiment and the recurring questions, and use it to find where the documentation needs to change. The chat identifier matters for that. The identifier that links a chat to a browser does not.

> This is the mechanism [[open-questions]] #92 has been asking for since September, now with a legal shape around it as well as a technical one.

### A correction that happened live on the call

George checked while the call ran: **the random ID is in local storage, not session storage.** Local storage persists until it is manually cleared; session storage dies when the tab closes.

**Three changes follow, all Novosapien's:**

1. Move the random ID to **session storage**, so it is gone when the visitor closes the tab.
2. Strip the random ID when a chat is written to the long-term store, so a visitor who leaves a tab open for a week still has no persistent link.
3. George to consider whether a random ID is needed at all, or whether the chat can carry its own identifier with no browser link.

**Net effect:** the implicit chain of browser to random ID to chat content to IP address in the Front Door logs is broken in the one place it could have been joined.

## The legal basis, in plain terms

Ian ran the question through his own research during the call and read the result back:

- **Security logs sit under legitimate interest.** Recital 49 names network and information security as a legitimate interest, which is the normal basis for firewall and access logs. Thirty days is unremarkable.
- **Chat history and the random ID are also legitimate interest**, because the visitor is asking for the service.
- **A short written legitimate interest assessment is good practice**, and does not exist yet. New [[open-questions]] #129.
- With 30-day security logs and 72-hour chat deletion, the position is comfortably inside the bounds, and a visitor cannot be identified from what is held.

He was appropriately sceptical of his own source, noting it tends to present every issue as a crisis.

## Where 72 hours actually came from

Asked directly whether 72 hours is a regulatory number: **no**. Michael set it on functional grounds. Most comparable services use 24 hours; TXN went to 72 to keep the value of returning to a chat the next day while holding the risk down. It is also the number TXN has been pushing Direct Transact to apply to the public sandbox.

> **And it is not documented with Direct Transact.** Michael: 72 hours is what was stated to them, and it has never been confirmed in any official documentation. He will check. Armand recalled the original sandbox discussion with Direct Transact, where periodic clearing was the agreed strategy. See [[open-questions]] #119.

## Who supports what, and who can touch production

**The support split, stated plainly by Ian:** Novosapien support and maintain **the AI layer**. Stackworx support and maintain **the Knowledge Hub**.

**Production access took a few passes and landed in the right place.** The distinction is between the source code and the running service:

| | Position |
|---|---|
| **Source code in GitHub** | Novosapien and Stackworx can see it, pull it and push to branches. A new developer could pull down what is currently deployed |
| **The running production service** | **Only Direct Transact can deploy.** There are multiple gates and nobody can change code and change the live site |
| **Why** | Ruan: it is like that on purpose |

**Ian's underlying concern**, which the answer satisfies, was that nobody can go into the code that is operating right now and start changing it.

**The one honest admission on the call**, from George: if Novosapien had the intent, it could open the Azure Front Door logs and read an IP address. Ian's answer is that this is true of everything in IT, the question is what anyone would use it for, and the control is the agreement rather than a claim that access is impossible.

## Cloud providers in privacy policies

Ian has **never seen a cloud provider named** in a privacy policy or a data processing agreement, and neither has the room. He will check TXN's samples, including the Paymentology policy, before deciding whether Azure needs to be called out at all. He noted that the questions arriving are themselves shaped by what people's AI assistants tell them to look for.

**YouTube and Vimeo embedding:** a non-issue at this stage.

**Stackworx:** Ruan confirmed there is nothing he needs to put in place from a Stackworx perspective.

## The commercial close, which is the part with a deadline

**Ian, directly: there is no signed agreement and no data processing agreement.** Brett's account: an MSA was put together, linked back to the initial deal, and structured so each piece of work could be added as an appendix.

**Why it matters now and did not two months ago.** Ian: the GDPR position was not a live issue then because Novosapien was not storing or hosting any data. It is now.

**The structure both sides agreed on the call:** standard terms, with an appendix per service bought, the newest being the hosting service.

| What Ian wants | By when |
|---|---|
| **The hosting arrangement papered** | **Before launch.** He called this one absolutely necessary, and does not expect it to be large |
| **The support and maintenance agreement** | Immediately. He believes there is no agreement for it either |
| The whole agreement signed | Before launch, which he acknowledged is a big ask because launch is Tuesday |
| **Spreading the Phase 2 work into a monthly retainer** | Raised by Ian, unprompted. He is <em>pretty open-minded</em> and wants it discussed properly |

**Direct Transact have sent TXN a list of requirements.** Ian will forward it for Novosapien to turn around. His own view is that it is overkill for what is actually happening, which is a hosted Knowledge Hub making an API call out to a model and getting an answer back.

> [!warning] Ian said Tuesday again, which is the 17th
> He said the whole agreement before launch is a big ask **because that is Tuesday**. The call was Wednesday 11 November, so Tuesday is **17 November**. Every delivery record says **16 November**, a Monday. **This is the second time Ian has named the 17th**, after [[2026-11-03-dt-demo-and-infrastructure]]. The vault keeps 16 November until it is confirmed, and it now needs confirming rather than flagging. [[open-questions]] #130.

## The 24 November session

A working session at Novosapien's offices in Aldgate East from **16:00**, moving to dinner in Soho around 18:30. Ian is at a conference at Billingsgate that day and can arrive earlier than first planned. **The agenda he named himself:** the arrangement that lets the work keep moving, the support and maintenance agreement, and spreading Phase 2 into a retainer.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| IP held in Azure Front Door only, 30 days, Europe, never sent to the model | [[architecture]], [[portal-co-pilot]] | Callout added |
| **Random ID dropped from anything retained beyond 72 hours**, Ian's decision | [[portal-co-pilot]], [[open-questions]] #92 | Callout added; row updated |
| **Random ID is in local storage, not session storage.** Move it, strip it on write, consider removing it | [[portal-co-pilot]] | **Three build items, Novosapien** |
| Long-term sanitised store approved in principle, for sentiment and documentation improvement | [[portal-co-pilot]], [[open-questions]] #92 | Callout added |
| Legal basis: legitimate interest, Recital 49 for security logs | [[architecture]] | Callout added |
| **A written legitimate interest assessment does not exist** | [[open-questions]] | **New row #129** |
| 72 hours is functional, not regulatory, and is undocumented with Direct Transact | [[open-questions]] #119 | Row updated; action on Michael |
| Personal data in chat and sandbox: not asked for, policy to say so, nothing done with it | [[commercial]], [[portal-co-pilot]] | Callout; acceptable use policy action on Dörte |
| APIs require no cardholder personal details; a blank cardholder can be created | [[portal-co-pilot]] | Recorded, it lowers the sandbox risk |
| Support split: Novosapien the AI layer, Stackworx the Knowledge Hub | [[commercial]], [[delivery]] | Callout added |
| Only Direct Transact can deploy to the running production service | [[architecture]], [[delivery]] | Callout added |
| Cloud providers are not normally named in privacy policies; Ian to check the samples | [[commercial]] | Action on Ian |
| **No signed agreement and no DPA.** Standard terms plus an appendix per service | [[commercial]], [[open-questions]] #103 | Callout added; row updated |
| **Hosting arrangement to be papered before launch** | [[commercial]], [[delivery]] | **The commercial critical path** |
| Support and maintenance agreement needed immediately | [[commercial]] | Recorded |
| **Ian raised spreading Phase 2 into a monthly retainer** | [[commercial]] | Recorded for 24 November |
| Direct Transact's requirements list to come to Novosapien | [[delivery]] | Action on Ian, then Novosapien |
| **Ian said Tuesday, which is the 17th**, for the second time | [[delivery]], [[open-questions]] | **New row #130** |
| 24 November session, Aldgate East 16:00 then Soho | [[delivery]] | Recorded |

### Context, no action

| Finding | Note |
|---|---|
| Questions are being shaped by AI assistants | Ian noted that the queries arriving are what people's assistants tell them to look for, and treated his own research with the same scepticism |
| YouTube and Vimeo embedding | A non-issue at this stage |
| Stackworx have nothing to put in place | Ruan, on the call |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Move the random ID to session storage | Novosapien | Before launch |
| Strip the random ID when a chat is written to the long-term store | Novosapien | Before launch |
| Decide whether a random ID is needed at all | George | Not dated |
| Write the legitimate interest assessment | Both | Before the privacy policy is finalised |
| Put personal data out of scope in the acceptable use policy | Dörte | Before launch |
| Confirm the 72-hour sandbox clearing with Direct Transact in writing | Michael | Not dated |
| Check whether cloud providers are named in TXN's sample privacy policies | Ian | Not dated |
| Send Direct Transact's requirements list to Novosapien | Ian | After the call |
| **Paper the hosting arrangement** | Both | **Before launch** |
| Paper the support and maintenance agreement | Both | Immediately after |
| **Confirm the launch date: 16 or 17 November** | Ian | Now |
