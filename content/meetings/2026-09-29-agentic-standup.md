---
date: 2026-09-29
type: standup
description: "Speed work shipped and Ian approves, DT's rate limit threatens it, alerting scope settled, and phase two framed as what TXN launches with"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-inbox-alerts]]"
  - "[[developer-support]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[agent-orchestration]]"
  - "[[alert-detection]]"
  - "[[agent-inbox-alerts]]"
  - "[[portal-co-pilot]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-09-29)

> **Source:** Fathom transcript, 29 September 2026, 09:00 BST, 44m. **Brett StClair**, **George Westbrook**, **Max Kingaby**, **Hasan Ahmed** and **Lily St. Clair** with **Ian Johnson**, **Dorte Dye** and **Michael Moores**. Full attendance on both sides, the first since the team returned.
>
> **Two demos and a proposal.** The speed rebuild, shown as recordings sent ahead; the knowledge hub co-pilot, demonstrated live by Hasan; and the phase two proposal, which Ian had not yet read.

## The speed work shipped, and Ian accepts it

Brett sent two recordings ahead of the call, both of suspending a card, chosen deliberately: *"they are the simplest and quickest actions... which I think was where the complaints were, that it's a two or three-click thing in the console, and it's taking 40, 50 seconds to do in there."*

**Ian's verdict:** *"I did have a look at those. **It seemed to be closer to what we'd hoped for.**"*

That is the first positive response to the build since his 15 September verdict, and it came unprompted.

### What changed

| Change | Detail |
|---|---|
| **Front-loaded form** | The agent now collects last four digits, cardholder name **and a reason** before acting. *"It's not going to let you do it until there's a reason"* |
| **Parallel investigation** | Where 40 declines were investigated one after another, they now run **in parallel**. *"A lot, a lot quicker, even for those longer time horizon tasks"* |
| **Less verbose** | *"So it's not chewing your ear off and having to spend 20 minutes reading its response"* |
| **Deployed** | All of it is on the production instance, the one TXN tests against |

George was candid that it is not finished: *"there's still definitely more tweaks to be made in the way that it responds as well."*

### The reason field came from Ian's own question

Ian had spotted something in the recording: a card was suspended with a label like *"suspicious activity"*, and *"there didn't seem to be anything in the flow to indicate how we'd arrived at the fact it was suspicious activity."*

George had already fixed it: *"you've got to put in the reason now. Whereas before, it was just put it in."* The reason is now a mandatory field on the form rather than something the agent infers.

**That is the right correction and it is worth naming.** An agent that invents a justification for a write is the same failure class as [[open-questions]] #89, where it invented an architectural explanation. Making the human supply the reason removes the inference entirely.

## The rate limit could undo all of it

Ian's question, and it is the sharpest thing on the call:

> *"How are we handling the AI calling into the APIs? Because theoretically there could be a lot more of those happening over a sustained period of time than there might be through just normal activity... speed is fine in terms of what you're trying to do on the AI side, George, but then if you hit the API and you've got some kind of rate limiting in there, then **the experience could be particularly poor**."*

**Michael's answer sets out the constraint:**

| | Position |
|---|---|
| **Scope** | **Per IP**, blanket across all endpoints |
| **Limit** | **15 requests per second** |
| **Purpose** | Built for external clients, *"purely just to make sure we're not getting hammered"* |
| **Precedent** | *"At Marqeta we hit 15 per second easily"* |
| **Mechanism** | **Azure Front Door**. DT and the Console both use the same approach |
| **Customisation** | DT have said limits can be raised per endpoint. Whether they can be raised **per IP** is unknown, and Michael is **waiting on documentation** |

**The problem is structural, not incidental.** The agent's whole speed strategy is to do more in parallel: 40 declines at once rather than in sequence. That is precisely the pattern a per-IP limit punishes, so the work that made the agent faster is the work most likely to hit the ceiling.

**George's proposed fix:** give the agent a **static IP** and whitelist it. Today it runs on Cloud Run, moving to the Azure equivalent, and *"I don't think it's got a static IP."*

**Michael's framing is better than a bypass:** *"it's a different question being an internal service, and we know all of that's legitimate... there's a conversation there we can have to not bypass it, but almost have a separate avenue for that."*

Ian closed it: *"I'll leave that with you, Mike."* Raised at [[open-questions]] #97.

## Identifying the right card, without over-exposing the cardholder

Ian asked whether cardholder name plus last four digits could match the wrong card. Michael's answer is that it can, and more easily than expected.

| Fact | Consequence |
|---|---|
| Last four repeats **70 to 80 times per million cards** | Not distinctive on its own |
| Cardholder names are **not enforced as unique** | Two cardholders may share a name |
| Cardholder name is **optional**; some clients give no cardholder detail at all | *"You could get 60 or 70 cards back on the last four"* |
| The only certain identifier is the **card ID** | *"Not everyone will know the ID"*, and a console user almost never would |

Michael described it as a *"logical waterfall"* down to the ID, and named the gap it exposes: **DT has no card search endpoint.** There is cardholder search, and cardholder groups, but *"we don't have one for cards at the moment specifically, so you can't get the cardholder first, then get the card."* He has emailed DT about it and will report back.

### Two constraints pulling against each other

**Show enough to decide.** George's proposal is to surface more on the approval card when there are multiple matches, cardholder group being the obvious discriminator: *"this is other information, click approve before you do it, because this is a sensitive action."* He named the human failure mode too: *"sometimes you might get users who are just, yeah, done, click approve. And then they're like, I didn't mean to do that."*

**Show no more than necessary.** Ian raised GDPR unprompted:

> *"Is there anything from a GDPR perspective about what data gets displayed back in order for somebody to make a decision?... if you included postcode and the cardholder name and the last four digits, that would seem to be a bit more information and probably a bit more connectivity between a card and address and a person than we might ideally like."*

> *"We just need to think through making sure that we pull back sufficient data for somebody to make a decision, but that also we're just conscious of not looking to pull back information that can necessarily connect a card to a cardholder to an address."*

**The agreed approach:** mirror what the Console already shows when a human searches, since that set has presumably been reasoned about, then decide which fields the agent needs as a minimum. Michael: *"we just need to be careful what's optional, what's mandatory, whether we put in some sort of mandatory fields in the AI."*

Raised at [[open-questions]] #98. It sits alongside [[open-questions]] #69, which asks where agent data is stored and on which side of the GDPR line; this is the same question about what is **displayed** rather than what is kept.

## What happens when the model is unavailable

Ian's second structural question, prompted by press coverage:

> *"All of this is built around existing LLMs... my concern is are we at risk for, whether it be safety, performance and cost, being things that make whatever the LLM that's being used not viable for the task that it's performing? And therefore would that essentially mean that AI just would not work?"*

**George's first answer was about swapping models** and it was not quite the answer to the question: *"it's a couple of lines of code and it's changed... the frameworks and packages we use allow us to very quickly, a matter of minutes, change from one LLM to another."* He added that models improve and cheapen over time, so the direction of travel is favourable.

**Ian pushed back, correctly:**

> *"How you describe it, George, is there's a couple of lines of code, but then there's some testing. Well, that is pretty significant for a business like us, into one that's basically supposed to be **always on**."*

And he made it concrete with alerts, which is the right example because it is the one with a duty attached:

> *"If a user is reliant on the alerts that we bring back, and then those alerts [are] not there, and therefore no action is taken, **I can see us being in hot water over that**, because people become reliant on it. We can word everything however we want, but if you offer an alert service, the fact that it's being powered by AI, I wouldn't care less as the client. I don't care. I expect this scenario happened, I expect an alert, you didn't deliver an alert, and this has been the impact to my business."*

> *"I don't see it as any difference to one failover from one data centre to another data centre in our business. It's just like, well, that's not working, something else has to start working straight away."*

### George's answer, and it is a good one

Two layers, and the second is the important one.

**A provider hierarchy.** *"There'll be level 1 LLM that is by one provider, level 2 LLM, level 3 LLM. We can go as deep as we want. So if Google's LLMs are down, then we switch to Anthropic. If Anthropic's down, we'd switch to OpenAI."*

**And the alert path degrades to no AI at all:**

> *"There's level one alerts, which is just, here you go, here's the alert. **Without any AI, that can still be delivered.** The request would be consumed, alerted to the user... In the worst case, if every single LLM in the world is out, [we] can still make sure that that alert is delivered. It might not have all of the AI niceties with it, but at least it's still notifying the user that you've had 50 declines today, it's over your threshold of 10. It's not going to go in and do the deep investigation if there's no LLMs."*

**That is the design principle worth keeping: the alert is a plain delivery obligation, and the AI is an enhancement layered on top of it.** It answers Ian's duty-of-care objection without promising that models never fail. Recorded against [[agent-inbox-alerts]], and it advances [[open-questions]] #85, which has carried the fallback chain as a gap since 3 September.

## Alerting scope is settled: DT detects, Novosapien consumes and acts

Ian, reading the phase two proposal live: *"I've just read the six components for Phase 2, and I've noticed that in bold it says **not an alerting system, so detection stays with DT**. It's a question mark, right? Because what is an alerting system?"*

**Brett's answer draws the line:**

> *"The originating source of the alert, so whether it's DT firing it up, that this is an alert that we need to take care of. It's going to be difficult for us to build that. But **taking the alerts, putting it into an inbox, making sure it's delivered, and allowing it to take action, happy days.**"*

> *"I want to just use the standard stuff that comes with Azure"*, rather than rebuild it. *"Anything that we spot where we think we're going to be reinventing a wheel, there's already a product, we're going to push back on you guys."*

**This substantially answers [[open-questions]] #68**, open since 25 August, which recorded that DT has no alerting system and inverted the assumption in [[alert-detection]]. The resolution is that DT does not need to build one, because **Azure's native logging and alerting is the detection layer**, and Novosapien consumes it.

### Two distinct alert classes, and they need different machinery

Michael separated them clearly, and this is new detail the vault did not have.

| | **Technical errors** | **Anomalies** |
|---|---|---|
| **Source** | Azure's built-in logging. *"They'll have specific alerts: this has failed, this is broken"* | The **data lake** |
| **Example** | An API call fails | *"You make a change and declines go down by 20%. That's for us an alert"* |
| **Nature** | Something is broken | *"It's not an error, really, but it's a known configuration [change]"* |
| **Delivery** | *"I assume with these systems you have webhooks"*, with TXN setting baseline alerts | Scheduled jobs or agent routines looking for variance |
| **Status** | DT logging exists; Michael is *"waiting to be able to see them and make sure they're of appropriate quality"* | **Blocked.** DT has not returned the data lake architecture |

**Detection must be variance-based, not threshold-based**, and Michael brought the Marqeta precedent: *"not just 11 over 10, because maybe there's nine all the time. But it's the percentage difference. So if there was none and then we had 20, then obviously that was an issue, versus going from 20 to 21."*

**Severity follows business impact, not error volume.** Michael's ranking: **transaction availability is highest**, *"that's a purchase from a cardholder that doesn't work."* Then the main APIs, grouped by whether failure breaks a user flow: *"you may not be able to create a card in that flow and result in an app failure, whereas not being able to load one transaction in the app, often you can just retry and it's fine."*

**George named the remaining gap**: scheduled checks are straightforward, *"maybe a user says check every hour or check every day."* Catching something **the instant it happens** is the hard part, *"something needs to ping us that this has happened so we can investigate, plan, and then potentially take action."* That is the webhook dependency, and [[open-questions]] #10 records that DT deprioritised product webhooks behind Visa certification, which has now been granted.

**Still open on DT:** the data lake architecture, which Novosapien will review *"to make sure that at least the foundation is right for pulling that data"*, with an API in front of it.

## Phase two, and Ian's framing of it

Brett has sent the proposal. **Ian had not read it** and left before the walkthrough, so Michael took it.

| | Detail |
|---|---|
| **Duration** | **Two and a half months**, *"which takes us through to effectively the end of the year"* |
| **Structure** | **Six components** |
| **Contents** | Stitching everything in; co-pilots and MCP servers on the dev portal; the agentic AI layers; **a first version of the co-pilot in the Console**; alerting |
| **Scale** | *"There's like **50, 60 workflows** that we're managing and building out"* |
| **Deliberately loose** | Brett left areas vague *"so we can add some more bits into it"*, to allow pivoting |

### The framing that matters

> Ian: *"**Phase 2 is that that's what we will go to market with.** Then there will be no diving into Phase 3, because we need to understand what the feedback is. **We need to have actual people using this thing** before we set an agreement."*

**His instruction to Michael for reviewing it** is the right test and worth quoting in full:

> *"Is there anything that is not in Phase 2 that we think we absolutely have to have at the point that we start servicing our clients, for it to meet what we've envisaged, **but also the message that we're giving to the market**, because that's how we need to set the scope."*

**That last clause connects phase two directly to [[open-questions]] #96.** On 23 September Nicola and Bron agreed to announce the full proposition at launch. Ian has now said scope should be set by the market message. If the message is bullish and the scope is not, the gap lands inside phase two, and Ian is the person who will have to reconcile them. **He has not yet seen the messaging position taken on 23 September, and he had not yet read the proposal.**

Brett's own reason for the shape: *"If I was in your shoes, what would we need to do? What could we hold back?"*

## Build for how developers work now

Ian's parting point before dropping off, and it is a product principle rather than a feature request:

> *"When it comes to the developer portal, one of the things that we want to make sure is that we are really building that capability to service **how people are building today**... we are building a platform knowing that the people who build and connect to that platform will be building in a different way than they traditionally have, and therefore we need to make sure that we're fit for purpose."*

His example is Marqeta's developer portal, which offers per-page export into a model.

**Michael listed what that means concretely**, from what he is specifying for Stackworkz:

- Copy page
- Copy as LLM text
- View as markdown
- **Open in ChatGPT**
- **Open in Claude**
- Ask a question about this page in **Perplexity**
- **Connect with Cursor**
- **Connect with VS Code**

**The split:** *"Stackworkz is going to build the top couple, and asking questions just opens a window. So I think they can do most of that by just diverting. Obviously when it comes to installing the MCP, I think that comes later when you've got yourselves sorted."* Michael is writing it up formally for Stackworkz and **copying Novosapien in**.

## Hasan's knowledge hub co-pilot, demonstrated

Built ahead of schedule. Brett: *"we've been a little bit cheeky just because we're worried about the timeline, and we've started building the co-pilot because we had some spare capacity."*

**What it does today**, from Hasan's demo on the cardholder page, reached through a small **Ask AI** icon:

- Answers a question such as *"how do I issue a card"* with the required headers, key fields and optional fields
- **Cites the source** and links straight to that documentation page
- Produces an **example payload**, expandable into a larger window for copy and paste

**Planned next:** chat history, export, one-click copy of the payload *"if you just want to paste it anywhere, into Claude, into ChatGPT"*, and navigating the user to the relevant page from the answer. Hasan: *"over the coming weeks we are going to extend it and make it a lot more feature-rich."*

**Michael's response:** *"It looks fantastic so far. **Exactly what we're thinking** in terms of being there, asking the AI, using the guides, using the reference."*

**And it has content to work with: 51 documents** are in the CMS.

> This is [[portal-co-pilot]] running rather than specified, and it arrived before the MCP server that was prioritised ahead of it on 16 September. Worth noting the order changed in practice, because spare capacity landed on the co-pilot first.

## The CMS handover, which closes an ask

Michael, on the call: **"The CMS one is over in five minutes."**

**Three webhook events** come with it:

- `content published`
- `content unpublished`
- `content deleted`

*"If you want to parse a document, you'll get given the web app with the specific API to call for that document. So at least you'll get that constant: we've published new documentation, if you want to parse it through, update, whatever, it's there."* Plus **a public URL that pulls down the content**. Currently the UAT instance.

**That answers the Umbraco access request made on 17 September** and left unanswered at the time ([[open-questions]] #92). It also delivers the continuous-pull mechanism that row needs, since publication events can now drive a refresh rather than a poll.

**Still outstanding for Novosapien:** infrastructure access for hosting. Brett: *"the only outstanding issues are around getting access to the content, to the CMS, and to the infrastructure, so we can start looking at how we get it hosted, get it up and running. I'll keep on just tapping on your door on that one."*

## Findings and where they landed

### The agent

| Finding | Destination | Action |
|---|---|---|
| **Speed work shipped, and Ian accepts it**: *"closer to what we'd hoped for"* | [[agent-orchestration]], [[open-questions]] | Added to **#87** and **#83** |
| Front-loaded form, parallel investigation, less verbose output | [[agent-orchestration]] | Recorded |
| **Reason is now a mandatory field**, not something the agent infers | [[agent-orchestration]], [[open-questions]] | Recorded; related to **#89** |
| **DT's 15 per second per-IP rate limit** threatens the parallelism | [[open-questions]] | New row **#97** |
| **Identifying the right card, against GDPR minimisation** | [[open-questions]] | New row **#98** |
| DT has **no card search endpoint**; Michael has raised it | [[txn-api-reference]], [[open-questions]] | Recorded in **#98** |

### Alerting

| Finding | Destination | Action |
|---|---|---|
| **Detection stays with DT via native Azure tooling**; Novosapien consumes, routes, investigates and acts | [[alert-detection]], [[agent-inbox-alerts]] | **#68** substantially answered |
| **Two classes**: technical errors from logs, anomalies from the data lake | [[alert-detection]] | Recorded |
| **Variance-based detection**, not absolute thresholds | [[alert-detection]] | Recorded, with the Marqeta precedent |
| Severity by business impact, transaction availability highest | [[alert-detection]] | Recorded |
| **Alerts must deliver with no AI at all**; AI is a layer on top | [[agent-inbox-alerts]], [[open-questions]] | Recorded; advances **#85** |
| Provider hierarchy confirmed: Google, then Anthropic, then OpenAI | [[open-questions]] | Added to **#85** |
| Instant detection still needs a push mechanism | [[open-questions]] | Ties to **#10**, now unblocked by Visa certification |
| Data lake architecture still not returned by DT | [[open-questions]] | Recorded |

### Delivery and the portal

| Finding | Destination | Action |
|---|---|---|
| **Phase two: six components, two and a half months, 50 to 60 workflows** | [[delivery]], [[open-questions]] | New row **#99** |
| **Ian: phase two is what TXN goes to market with**, and scope is set by the market message | [[delivery]], [[open-questions]] | Recorded in **#99**, tied to **#96** |
| No phase three planning until real users have used it | [[delivery]] | Recorded |
| **Build the portal for how developers work now**: open in Claude, ChatGPT, Cursor, VS Code | [[developer-support]], [[docs-mcp-server]] | Recorded; Stackworkz builds the first few |
| **Knowledge hub co-pilot demonstrated and endorsed** | [[portal-co-pilot]] | Recorded; built ahead of the MCP server |
| **CMS handed over with three content webhooks** | [[open-questions]] | **#92** answered |
| Infrastructure access for hosting still outstanding | [[delivery]] | Recorded |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Get DT's documentation on customising rate limits | Michael | Per endpoint is possible; per IP unknown |
| Give the agent a static IP so it can be whitelisted | Novosapien | Currently Cloud Run, moving to the Azure equivalent |
| Resolve card lookup with DT, since there is no card search endpoint | Michael | Emailed; will report back |
| Decide the minimum fields shown to disambiguate a card | Both | Mirror the Console, then cut to what is needed |
| Read the phase two proposal | Ian, Michael | Ian had not; test is what must exist to service clients |
| Send the portal AI export spec to Stackworkz | Michael | Copying Novosapien in |
| Send the CMS access and webhook details | Michael | *"Over in five minutes"* |
| Grant infrastructure access for hosting | Michael | Brett: *"I'll keep tapping on your door"* |
| Book a session to show Ian the co-pilot build | Novosapien | Offered on the call |

---

## Transcript

# **TXN \- Agentic AI SU \- September 29**

[**VIEW RECORDING \- 44 mins (No highlights)**](https://fathom.video/share/RYssggvX9GuG_ftZtCQxpyCqEAjypq7-?tab=summary&utm_campaign=postmeetingsummary&utm_content=view_recording_button&utm_medium=email)

[@0:00](https://fathom.video/calls/839476988?timestamp=0.0) \- **Dörte Dye (Paycorp)**

Everyone else looks chill, and you're like, it's not my country.

[@0:06](https://fathom.video/calls/839476988?timestamp=6.15) \- **Brett StClair (Novosapien)**

I'm looking forward to being back in cool weather, this constant heat. Self-inflicted. It's been good. It's been good. We've got a big table.

Everyone just grafts around that table, hammering it out. How have you been, Ian? I'm very well.

[@0:30](https://fathom.video/calls/839476988?timestamp=30.6) \- **Ian Johnson**

You look very red, Brett. That's how I started the conversation. This is the, this is the Bali look.

[@0:38](https://fathom.video/calls/839476988?timestamp=38.33) \- **Brett StClair (Novosapien)**

Brett is constantly sweating. Is it because of us being your client, or is it because of the climber?

[@0:50](https://fathom.video/calls/839476988?timestamp=50.75) \- **Dörte Dye (Paycorp)**

You've got some pleasure to work with.

[@0:53](https://fathom.video/calls/839476988?timestamp=53.15) \- **Ian Johnson**

This climate is killer.

[@0:58](https://fathom.video/calls/839476988?timestamp=58.97) \- **Brett StClair (Novosapien)**

Hi, George. Mike joining. How are we doing?

[@1:03](https://fathom.video/calls/839476988?timestamp=63.3) \- **Ian Johnson**

He sure will be. There he is. There we go.

[@1:07](https://fathom.video/calls/839476988?timestamp=67.21) \- **Dörte Dye (Paycorp)**

Hello, can you hear me? Yeah, we can hear you.

[@1:10](https://fathom.video/calls/839476988?timestamp=70.99) \- **Ian Johnson**

What's missing from the call? Yeah. I have myself through Max's computer.

[@1:19](https://fathom.video/calls/839476988?timestamp=79.18) \- **George Westbrook (Novosapien)**

There we go. There's Michael's Fathom.

[@1:23](https://fathom.video/calls/839476988?timestamp=83.58) \- **Brett StClair (Novosapien)**

I was thinking I'm missing that.

[@1:29](https://fathom.video/calls/839476988?timestamp=89.54) \- **Ian Johnson**

Awesome. I think that's everybody. Shall we kick off?

[@1:34](https://fathom.video/calls/839476988?timestamp=94.05) \- **Brett StClair (Novosapien)**

Yes, go for it. So there's a couple of demos we want to do today. The first one being in, I'm keen to, George, to take you through the speed and kind of different steps that we've narrowed down on so you can have a look at how that flows.

I'm not too sure if those loops came out very well. I was struggling a little bit with them, but I think.

If you did have a chance, we kind of recorded that to give you a sense.

[@2:04](https://fathom.video/calls/839476988?timestamp=124.99) \- **Ian Johnson**

Yeah, I did have a look at those. It seemed to be closer to what we'd hoped for. I had one question on it, that they were both around suspending the card, and then one was where the last four digits were entered.

And that was a really quick process, because it just pulled back the only card that obviously ended in those four digits.

And then the other one was pulling back, from memory, was pulling back a number of different cards, you know, the four digits.

Different options.

[@2:43](https://fathom.video/calls/839476988?timestamp=163.56) \- **Brett StClair (Novosapien)**

So, both looks okay. The only thing I didn't quite understand was, there seemed to be a reason for the card being suspended.

[@2:53](https://fathom.video/calls/839476988?timestamp=173.09) \- **Ian Johnson**

That was, I didn't see how that was actually, I don't know, Mike, if you've seen it, but I didn't, I couldn't see and understand how.

Thank you. Thank That had got there, that label had got there. I think it was something like suspicious activity or something.

[@3:06](https://fathom.video/calls/839476988?timestamp=186.92) \- **George Westbrook (Novosapien)**

But it didn't seem be anything in the flow to indicate how we'd arrived at the fact it was suspicious activity.

[@3:16](https://fathom.video/calls/839476988?timestamp=196.02) \- **Ian Johnson**

Yes, and I've changed that in a new one.

[@3:18](https://fathom.video/calls/839476988?timestamp=198.5) \- **George Westbrook (Novosapien)**

Literally, you've got to put in the reason now. Whereas before, it was just put it in. It's, yeah, now there's the form where it's, you put it in, the number, last four digits, or the last four digits, name of the cardholder, the reason, and then it's not going to let you do it until there's a reason.

Okay.

[@3:40](https://fathom.video/calls/839476988?timestamp=220.51) \- **Ian Johnson**

And then on the last four digits and the name of the cardholder, this might be my ignorance, Mike, but is there any risk, is there, I know the risk would be slight.

But is there any risk that that would pull back or that would pick up the wrong? So is there any risk that a cardholder with the same name would have the same last four digits?

You're on mute, think, mate.

[@4:11](https://fathom.video/calls/839476988?timestamp=251.1) \- **Michael Moores**

Obviously, like, last four would probably repeat 70 or 80 times in, you know, a million cards or something like that.

So it does happen commonly last four. Now, obviously, the cardholder name in last four would be, you know, much rarer.

Obviously, we don't stop two cardholders having the same name. That's not a sort of distinctness we've got in. So it is possible that, you know, you could potentially have that.

Yeah, I think the risk would be quite low in that situation. I've never seen it personally. Obviously, the more possible risk would be if a client didn't give us any cardholder name.

So obviously, clients don't have to give us any detail about the cardholder. It could just be a card with some details.

So in that case, you could get, you know, 60 or 70 cards back on the last four, basically. So I guess it depends on how many is returned in terms of that lookup.

Obviously, in that situation alone, I guess the lookup for the agent would be difficult anyway, because obviously we've got nothing to search for.

So I think that whole flow would be potentially different anyway, because you have to find the ID of the cardholder first, because you wouldn't find any cardholder names.

So I think in a generic, let's say normal use case, would be quite rare to have same cardholder names, same last form outside of that.

Yeah, famous lad, but it's possible.

[@5:36](https://fathom.video/calls/839476988?timestamp=336.44) \- **Ian Johnson**

So we should definitely make sure that we think it through to make sure that we are, in that scenario, it's what we'd present back for the user to then make a decision as to which one was to card.

That's the only point to me. So if the agent found multiple matches, and I agree, Mike, the chances are very slim.

But, you know, it's not completely impossible. So if we pull those back, we just have to think about what additional data items were displayed for them to then be able to make a decision about which one it was they were suspended.

[@6:17](https://fathom.video/calls/839476988?timestamp=377.36) \- **George Westbrook (Novosapien)**

Yeah, I suppose as well with things like the cardholder group, that's just making that even more unlikely as well, isn't it?

I'm just trying to think how we could, yeah, just providing all the information we can to the user before, I suppose on the approval card, we can display that information as well.

So let's say the agent thinks it's a match and it isn't, we'll be like, cardholder group is this, this is other information, click approve before you do it, because this is sensitive action.

I suppose it's just with the user, sometimes you might get users who are just, yeah, damn, done, click approve.

And then they're like, , , , I didn't mean to do that. Yeah.

[@7:05](https://fathom.video/calls/839476988?timestamp=425.32) \- **Ian Johnson**

I also, I'm just, I guess the only other question is just, is there anything from a GDPR perspective about what data gets displayed back in order for somebody to make a decision that you are connecting the last four numbers of a card?

So what's brought to mind is like, say, let's say, for example, postcode, but if you included postcode and the cardholder name and the last four digits, that would seem to be a bit more information and probably a bit more connectivity between a card and address and a person that we might ideally like.

So it's just something to muse on, really, just to think about scenario, because obviously, if I understand rightly, correctly, Mike, every single card has got its own unique code.

Within our system, but if I think about it from a user experience point of view, am I going to know what the actual code is, and what does that look like, then, so I'm in, and we're saying, we'll meet you wherever you are, but then, essentially, you wouldn't know, it would be very unlikely you'd know which code that related to which card.

So it's, it's a very, it's a, definitely an edge case, but we just need to think through making sure that we pull back sufficient data for somebody to make a decision, but that also we're just conscious of not looking to pull back information that can necessarily connect a card to a cardholder to an address.

Okay, yeah, so I suppose from there, what we could do, we could just look at how someone would identify on the console, and then provide.

[@9:00](https://fathom.video/calls/839476988?timestamp=540.0) \- **George Westbrook (Novosapien)**

They're saying more similar information for them to be able to make their decision. I'm assuming if they went through the console, they'll be able to click through, find the right card that they want, and then we just show that information that's there.

[@9:14](https://fathom.video/calls/839476988?timestamp=554.7) \- **Michael Moores**

Yeah, we've got a sort of searching capability, which is first name, last name, last father card, a couple of other bits, obviously ID being the simplest, but as Ian said, not everyone will know the ID.

So I think we need to have a look at what we need to make a match, and then at some point, like I say, some of these fields are optional, so obviously first name, last name is optional in our system, because we may not keep that data.

So then you're down to the last four, which then becomes very difficult to condense that down. The only thing to condense it down after the last four, if you don't have any cardholder needed names, would be the ID.

So these are that logical sort of waterfall, if you will, and at some point, we are going to have to revert back to the ID if we don't have any data.

So we just need to be careful. What's optional, what's mandatory, whether we put in some sort of mandatory fields in the AI to, you know, knowing who's going to use this, there are most likely not going to be people with, you know, identifiers, basically.

They'll be looking for certain details.

[@10:14](https://fathom.video/calls/839476988?timestamp=614.301) \- **George Westbrook (Novosapien)**

So maybe we just say, right, we need to find possible matches, we need these things in the object, basically, and we can do that.

[@10:21](https://fathom.video/calls/839476988?timestamp=621.801) \- **Michael Moores**

And a lot of our services are sort of hinged off the back of, if you want other services, you need to provide the details.

So it's only going to be those sort of complex clients that want to build a lot themselves that won't give us that detail.

I'd say 90% of them, you know, our clients will give that detail, and we will be the source of truth for that.

It's just those are the ones that may be not sort of supportive, but sort of making sure we say, you know, there's no details that we need.

You know, here are the IDs, or, you know, can you add it or something like that, basically. So I'll have a look.

I sent an email to DT about this, actually, about searching, because we have... Ability to search by cardholder, cardholder groups, you've got all that endpoint where you can pull them back and search.

We don't have one for cards at the moment specifically, so it's sort of can't get the cardholder first, then get the card.

So we're just working through some sort of solutions there to how we can pull back the specific card. So if you didn't just have the last four, for example, you can just pull back everything in the last four.

So we are still working through that as a solution for if you don't have the cardholder. So I'll keep you updated on that as well.

Thanks.

[@11:38](https://fathom.video/calls/839476988?timestamp=698.321) \- **George Westbrook (Novosapien)**

Yes, I suppose that I think the two videos we sent over was all related to suspending a card, which, yeah, all related to suspending a card.

So there's been speed changes all throughout. And the reason we sent those over because they are the, it takes me like, the simplest and quickest actions.

That is most likely going to take, which obviously I think that was where the complaints were, that it's a two-click thing, two or three-click thing in the console, and it's taking 40, 50 seconds to do in there.

So like other things, for example, I think investigating declines, whereas before what might happen is, let's say there was 40 declines that you wanted to investigate.

It would be, like, let me investigate one, then another, then another, then another, then another. Now it's 40 in parallel, so it's a lot, a lot quicker, even for those longer, longer time horizon tasks.

It should be, should be a bit more concise as well, so it's not chewing your ear off and having to spend 20, 20 minutes reading its response.

But there's still definitely more, more tweaks to be made in the way that it responds as well. So I think everything, everything's been pushed onto the, the production version, or let's call it that.

The main test version, which we're calling production. So whenever you've got a chance to play around, just let us know if there's any issues, any bits of feedback, and then we'll get on to them.

I think, was there any questions, any feedback on that before we move on? I just wanted to ask one question, Mike, just in terms of the conversation that's going on with DT about the whole rate limiting piece.

[@13:31](https://fathom.video/calls/839476988?timestamp=811.201) \- **Ian Johnson**

Is there a, how are we handling the AI calling into the APIs? Because theoretically, there could be a lot more of those happening over a sustained period of time than there might be through just normal activity.

I don't know, I might be completely wrong, but I just want to make sure that we think about speed is fine in terms of...

of what you're trying to do on the AI side, George, but then if you hit the API, and then you've got some kind of rate limiting in there, then the experience could be particularly poor.

[@14:16](https://fathom.video/calls/839476988?timestamp=856.772) \- **George Westbrook (Novosapien)**

Is the rate limiting per logged in user, is it just an overall rate limit from TXN interacting with any DT APIs?

So per IP. Okay. Could there be a potential that we could whitelist? I'm sorry. Sorry, I think there's a, I think there's like a two second delay.

So, yeah, I was just going to ask, is there a way that maybe like we could, the IP, could get a static IP for the agent?

And then, because at the moment, because we're using, well, Cloud Run, we will use the Azure version of Cloud Run.

I don't think it's got a static IP. Okay. Okay. So, So, So potentially is there a way if we create it, so it's got a static IP, could basically whitelist that IP so that it bypasses the user rate limit, but does have some sort of rate limiting in there as well.

[@15:16](https://fathom.video/calls/839476988?timestamp=916.062) \- **Michael Moores**

Yeah, I think obviously the rate limiting was very much external clients, so there's a conversation that we had with it being pulled in internally as an internal function.

Obviously it's not a resource thing, but the way it's limited, it's purely just to make sure we're not getting hammered by our external clients, so that's one avenue.

The second avenue we're waiting for documentation on is how do we customize this, so at the moment it's a blanket per IP across all endpoints.

They have mentioned we can increase it for certain API endpoints, and I want to know if we can increase it for certain IPs as well, because we are going to have larger customers.

I think it's set to 15 per second at the moment, but at Marquette we add 15 per second easily, so we need to have a look at that, we're waiting for documentation on that.

I think it's a different question being an internal service, and we know all of that's legitimate, and we need to make those calls to pull the stuff back.

So I think there's a conversation there we can have to not bypass it, but almost have a separate avenue for that as well.

So I think it is Azure front door they're using to do that. So it may just be, say, the IP to allow that through or something like that.

So DT using the same thing, the console's using the same approach as well. So there must be something that they've already done.

We're just waiting for documentation on how it is done specifically, and then obviously make sure we won't be sort of blocked or barred from doing things.

Okay, so I'll leave that with you, Mike.

[@16:45](https://fathom.video/calls/839476988?timestamp=1005.89) \- **Ian Johnson**

So the other thing that's been on my mind, want to get, I also want to, as I said in my email, Brett, I just want to pick up on phase two, just so we can kind of make sure we're aligned on what the scope of it is.

But the other thing that's just playing on my mind slightly is obviously all of this is built around kind of existing LLMs, so whether it's Claw, ChatGBT, whatever else might be being used.

I guess that my concern is are we at risk for whether it be safety, which obviously raised because there's a lot of about that in the press at the moment, pardon my French, Lily, performance and cost being things that make whatever the LLM that's being used not viable for the task that it's performing.

And therefore, would that essentially mean that AI just would not work? I think if, let's say, the LLM were currently...

[@18:00](https://fathom.video/calls/839476988?timestamp=1080.0) \- **George Westbrook (Novosapien)**

We're is out of date in comparison to why it is too expensive or too slow. It's a couple of lines of code and it's changed.

It's very, very easy to switch it out. It's not as if we're building everything around one LLM. The frameworks and packages we use allow us to very, very quickly, like a matter of minutes, change from one LLM to another.

Another LLM. I'd be alive if said that you wouldn't need to do a bit more testing, but all it would be is you just run a few tests and see acceptance criteria met for these workflows.

Yep, okay, let's get this model out there. We're constantly changing models because a new one will come out every other week and we want to test to see if it gets better performance.

But it's one of those, it's never really going to degrade. It's only really... really going to ever improve in terms of functionality because they get more intelligent and usually cheaper as well over time.

So, yeah, I don't think there's anything, so there's no risk, but I think the risk is pretty low.

[@19:18](https://fathom.video/calls/839476988?timestamp=1158.46) \- **Ian Johnson**

I think we just need to think about what the critical capabilities are that are being delivered with AI, and what happens, because how you describe it, George, is there's a couple of lines of code, but then there's some testing.

Well, that is pretty significant for a business like us into one that's basically supposed to be always on. Now, that wouldn't apply to everything, Mike, in my mind.

If there were things, for example, let's talk about alerts, where if a user is reliant on the alerts that we bring back, and then those alerts...

not there, and therefore no action is taken, I can see us being in hot water over that because people become reliant on it.

Now we can word everything however we want, but if you offer an alert service, the fact that it's being powered by AI, I wouldn't care less of the client on that.

I don't care, I expect this scenario happened, I expect an alert, you didn't deliver an alert, and this has been the impact to my business.

So I think we just need to think that area through, because I don't see it as any difference to one failover from one data centre to another data centre in our business.

It's just like, well, we don't care. So that's not working, something else has to start working straight away.

[@20:53](https://fathom.video/calls/839476988?timestamp=1253.34) \- **George Westbrook (Novosapien)**

So on that point, say taking alerts as the example, I suppose there's level one alerts. Which is just, here you go.

Here's the alert. Without any AI, that can still be delivered. The request would be consumed, alerted to the user.

Let's say there's a flag which says, write AI down, which probably wouldn't happen because, I think I mentioned it before, what we'll do is there'll be level 1 LLM that is by one provider, level 2 LLM, level 3 LLM.

We can go as deep as we want. So that if, say for example, Google's LLMs are down for a random reason, then we switch to Anthropik.

If Anthropik's down, we'd switch to OpenAI or could switch to another one and another one. So that there's always going to be an LLM that is going to respond to the user.

In the worst case, if every single LLM in the world is out, can still make sure that that alert is delivered.

It might not have all of the AI niceties with it, but at least it's still notifying the user that, say, at the

You've had 50 declines today. It's over your threshold of 10, for example. It's not going to go in and do the deep investigation if there's no LLMs, but 99.99999% of the time, there's going to be an LLM available that's going to respond to the user.

Okay.

[@22:23](https://fathom.video/calls/839476988?timestamp=1343.83) \- **Brett StClair (Novosapien)**

On the point of alerts, I know we've had various discussions and you guys talk about AI-powered alerts. I want to get into a little bit more of that detail as we're trying to build out the requirements for what we can deliver, when we can deliver.

There are various layers to this, right? Who's generating the alert? Why it's being generated? If it's infrastructure, network, DT, how are you guys seeing that?

And then there's how we deliver the alerts, how we take action on those alerts. What alerts should be floated up?

What alerts should be logged and stored in a system? So it gets quite complicated. Mike, you mentioned that you're thinking AI powered everything.

Where's your headspace, on that? Yeah, still a lot of stuff going around, obviously, for us to sort of confirm.

[@23:20](https://fathom.video/calls/839476988?timestamp=1400.79) \- **Michael Moores**

So we still don't know where the log is sitting with DT or what the structure of data lake is.

But obviously, I think having connections into the whatever logging platform it is and, you know, those errors there would be the first one.

Obviously, pushing that into there. Then obviously, the data lake would be sort of the anomaly side. So you're not everything is like an error in such as, you know, a logging error.

It may be that you make a change and declines go down by 20%. So that's for us to like an alert.

[@23:51](https://fathom.video/calls/839476988?timestamp=1431.29) \- **Brett StClair (Novosapien)**

So, again, that sort of looks at the data structure we're trying to have with DT as well. So we're still trying to build that out for us to know exactly.

[@24:00](https://fathom.video/calls/839476988?timestamp=1440.0) \- **Michael Moores**

What it is, obviously the main focus would be on sort of transaction availability, I think is the highest one for me, because that's a purchase from a cardholder that doesn't work.

And then you have sort of main APIs, really. So, you know, getting a transaction, the impact of that is much lower than if you can't create a card, for example.

So, we have some sort of high availability APIs that we consider is, you know, they interrupt the flow, and a lot of them may, you know, may break or may not be able to create a card in that flow and result in an app failure.

Whereas not being able to load one transaction in the app, often you can just retry and it's fine. So, there are sort of groupings there that we'd say that this is key, high, you know, alert, whereas the others are, you if there's a small amount of errors in the get transactions, for example, it's much lower.

So, a lot of stuff we did at Marquetta was sort of variance. So, obviously, not just 11 over 10, because maybe there's...

You know, nine all the time, for example. But it's the percentage difference. So if there was none and then we had 20, then obviously that was an issue versus going from 20 to 21\.

You know, that could trigger a static alert that we've had in the past. But it should be sort of a sizable gain that it's not just increased from being really bad, but it's actually a noticeable percentage shift.

So obviously we get that from logging and also we are building out sort of transaction availability and decline reports in DT as well.

But obviously you'll work with yourself to see what data you may want to pull or in what format as well.

But that's still very much open with DT about that. And again, we'll get together on that piece as well with DT.

And we're waiting for their data lake sort of architecture back again still, which obviously will get you to review and make sure that at least the foundation is right for pulling that data.

Obviously there'll be an API in front of that as well. So we're just trying to make sure we get all that data into you first.

To have that basis.

[@26:01](https://fathom.video/calls/839476988?timestamp=1561.1) \- **Ian Johnson**

Okay, so I've just read the six components for Phase 2, and I've just noticed that it's in bold, it says not an alerting system, so detection stays with DT.

It's a question mark, right? I've just flagged that there, because what is an alerting system?

[@26:20](https://fathom.video/calls/839476988?timestamp=1580.78) \- **Brett StClair (Novosapien)**

So the originating source of the alert, so whether it's DT firing it up, that this is an alert that we need to take care of.

It's going to be difficult for us to build that, right? But taking the alerts, putting it into an inbox, making sure it's delivered, and allow it to take action, happy days.

So I was struggling with the definition, and so we look at a lot of our alerts if there's a problem with the code or a problem with the database.

We've also got a bunch of alerts that are firing up into our backends, and we've got these kind of...

Self-healing, human-augmented systems that also go, this is done. The AI is going to make an attempt to fire it up, fix it, fire it up, get it stood up again.

And, you know, we'll use alerting platforms to initiate the log and track the log. But perfectly comfortable consuming a bunch of APIs, consuming those alerts, putting the rule sets around it, allowing it to take action, especially around the user kind of interfaces.

George, is there anything you want to jump in there on that?

[@27:36](https://fathom.video/calls/839476988?timestamp=1656.1) \- **George Westbrook (Novosapien)**

Yeah, yeah, I think it's just as long as we're getting the alert, like this has happened, then we can send that to an agent which can do further investigation, build a bit more context, build up a plan, build an impact analysis, send the plan and the impact analysis to a user in order for the agent to go execute.

Make a change. Yeah, it's just the originating of that alert system, right?

[@28:08](https://fathom.video/calls/839476988?timestamp=1688.0) \- **Brett StClair (Novosapien)**

Yeah, I think for any, with any failures, obviously, DT will be logging it somewhere.

[@28:13](https://fathom.video/calls/839476988?timestamp=1693.56) \- **Michael Moores**

I think it's all Azure built in.

[@28:15](https://fathom.video/calls/839476988?timestamp=1695.66) \- **George Westbrook (Novosapien)**

We're still working on the access and where that's going to sit and stuff like that anyway.

[@28:19](https://fathom.video/calls/839476988?timestamp=1699.8) \- **Michael Moores**

So they'll have specific alerts. This has failed, this is broken. So obviously that will be, I assume with these systems, you have webhooks or whatever it may be, and we can set our own baseline alerts there.

Yeah, the sort of data lake one would be more anomaly checking, more running those jobs with an agent or a routine in the background to say, we're looking for this variance of this change.

And then you have something like that. So I think there's a split there in terms of that. But yeah, for just error tracking, there will be logging the error for transactions, APIs, stuff like that.

you know what mean? Azure does have those standard logging features and error alerting. And so we were kind of… of… a big

So these are pretty standard tools.

[@29:02](https://fathom.video/calls/839476988?timestamp=1742.87) \- **Brett StClair (Novosapien)**

Rather than us recreating them, let's make sure that your guys are making use of them. We pull a hook into it.

I get on the data lake, that makes sense, right? It's going to be very specific to the user journey and what they're trying to achieve, and we can do a lot with that.

That's very cool stuff. Perfectly happy with that. But generally, I want to just use the standard stuff that comes with Azure.

Yeah. Perfect.

[@29:29](https://fathom.video/calls/839476988?timestamp=1769.23) \- **George Westbrook (Novosapien)**

Yeah, because I think with the, let's say, if it was pure, like the agent looking for anomalies, if it was done on, say, like a regular cadence, regular time cadence, then that would be fine for the agents.

Maybe a user says, check every hour or check every day for this, blah, blah. It's just where the difficulty would be with the data lake is catching something the instant it happens.

Because then it would be, right, this has literally just happened. And that's That's where we'd need to be like, right, something needs to ping us that this has happened so we can investigate, plan, and then potentially take actions.

But the one that's more routine on that regular time cadence is I. Yeah, I think we'll know more once we speak to DT.

Naturally, there's two ways to find out if transactions are failing, obviously.

[@30:22](https://fathom.video/calls/839476988?timestamp=1822.77) \- **Michael Moores**

So I guess it depends if it's functionally broken. Let's say that the back end is broke. You're going to get errors in the logs.

But let's say you've changed something that technically is working, but then obviously reduces the sort of passing rate. So it's not an error, really, but it's a known configuration.

[@30:41](https://fathom.video/calls/839476988?timestamp=1841.47) \- **Brett StClair (Novosapien)**

I guess obviously we can, through the console and through the AI, we'll know that's happened.

[@30:45](https://fathom.video/calls/839476988?timestamp=1845.03) \- **Michael Moores**

So there'll be a log of what's happened. And then there'll also be an output and outcome. So I think we just need to think of how we hang that together.

Obviously, make sure we've got the right reporting with DT and we're still doing the timelines on what we can do.

So I think the day-to-day stuff won't be immediate. But obviously, certainly, you could have some sort of set schedule to look at that as well.

So I it's more like BAU errors versus actual, you know, specific API technical errors as well.

[@31:11](https://fathom.video/calls/839476988?timestamp=1871.08) \- **George Westbrook (Novosapien)**

So just trying to bridge the gap with both of those.

[@31:13](https://fathom.video/calls/839476988?timestamp=1873.48) \- **Michael Moores**

But yeah, the API errors should be fully covered from DT in terms of login and stuff like that. I'm just waiting to be able to see them and make sure they're of appropriate quality.

But naturally, they should be easy to read and interpret from there as well. Okay, so just conscious of time.

[@31:34](https://fathom.video/calls/839476988?timestamp=1894.43) \- **Brett StClair (Novosapien)**

So, have you read the Phase 2 proposal?

[@31:42](https://fathom.video/calls/839476988?timestamp=1902.25) \- **Ian Johnson**

I haven't yet, no. Okay. So shall I give you a quick walkthrough on it? Talk through it? I've got to be on a call at 22, so you can talk the guys through it by all means.

I just want to double check something. So I understand there's a bunch of stuff that's... Leftover, I guess the thing that we need to be clear about as we finish Phase 2, which to me, Mike, Phase 2 is that that's what we will go to market with.

then there will be no diving into, at the moment in my head, there's no diving into Phase 3 because we need to understand what the feedback is.

We need to have actual people using this thing before we set an agreement. And you're going to pivot a lot, right?

I've tried to keep it kind of open enough to help you pivot as we get closer and closer to it.

So I think when you read it, Mike, it's just looking at it and saying, is there anything that is not in Phase 2 that we think we absolutely have to have at the point that we start servicing our clients for it to meet?

Okay, what we've envisaged, but also the message that we're giving to the market, because that's how we need to set the scope.

Yes. We've literally taken a stab at it, and I can't make those judgment calls for you guys.

[@33:15](https://fathom.video/calls/839476988?timestamp=1995.2) \- **Brett StClair (Novosapien)**

So that's the perfect way to read it. Yeah, take a look.

[@33:20](https://fathom.video/calls/839476988?timestamp=2000.86) \- **Michael Moores**

Okay, and that's two and a half months, which takes us through to the end of, well, effectively the end of the year, right?

[@33:28](https://fathom.video/calls/839476988?timestamp=2008.08) \- **Ian Johnson**

Yeah, yeah. So there's a lot there. It's stitching in everything. It's building out the copilots and MCPs on your dev portal.

[@33:39](https://fathom.video/calls/839476988?timestamp=2019.34) \- **Brett StClair (Novosapien)**

It's getting all the agentic AI layers in. It's getting a first version of the copilot into the console. You know, the amount of tooling and workflows are large.

There's like 50, 60 workflows that we're managing and kind of building out. So I kind of looked at it and thought, about about it and and and and you.

If I was in your shoes, what would we need to do? What could we hold back? Most of the time we can get a bit ahead on some stuff.

So I've kind of left some areas where, you know, it's a little bit vaguer and we can add some more bits into it.

But there's a lot. There's a lot. The alerting and all that kind of stuff, that's a big chunk, but we're comfortable that we can do it.

We're just worried that, you know, we'd end up building up, I mean, we could build a full alerting system, but I think as you, what you're planning to do using the Azure Stack and DT stuff and we consuming it, perfect.

You just don't want to reinvent the wheel there. Anything that we spot where we think, , we're going to be reinventing a wheel.

There's already a product. We're going to push back on you guys just to kind of make sure that you've, that you're aware of it and that you're happy with the approach.

But I think at the moment, it's very much, we've packaged it to be exactly what you kind of need.

That isn't wheelhouse stuff. Okay.

[@35:04](https://fathom.video/calls/839476988?timestamp=2104.97) \- **Ian Johnson**

I'm going to have to jump off, but one final thing on it is just bear in mind that when it comes to the developer portal, one of the things that we want to make sure is that we are really building that capability to service how people are building today.

So we've had lots of conversations about that, but if you go to the Marketa developer portal, I think it is Mike who just noticed that there's the options to, I think, download directly into a certain model, but on a page basis.

So it's not everything, it's I'm on this page, download this, some things like that we need to really think about because we are building a platform, knowing that the people who build and connect.

And that platform will be building in a different way than they traditionally have, and therefore we need to make sure that we're fit for purchase.

[@36:07](https://fathom.video/calls/839476988?timestamp=2167.79) \- **Brett StClair (Novosapien)**

So we've been a little bit cheeky just because we're worried about the timeline, and we've started building the co-pilot because there's a bunch of stuff like that already, and we had some spec capacity.

Can we set up maybe some time this week just so you can have a look and see where we're heading in that right?

Those same features, we're really building that out.

[@36:34](https://fathom.video/calls/839476988?timestamp=2194.31) \- **Ian Johnson**

So just so you can see it. I'm interested, but I'm by far the least qualified to comment on how we develop.

So Mike's a lot closer than I am to that. But then equally, I think, Mike, it might be something where we give DTs, developers, a window into what we're thinking about sometime appropriately in the same way we have with the kind of knowledge hub.

Yeah. All right, we'll get you on phase two, Brett, but I need to jump, I've got a call, so.

Awesome, all the best. Mike, if you're available, do you want us to quickly take you through that? Yeah, sure.

[@37:13](https://fathom.video/calls/839476988?timestamp=2233.75) \- **Michael Moores**

Yeah, I think it would be nice just to get your kind of feedback on that in the early stages.

[@37:20](https://fathom.video/calls/839476988?timestamp=2240.47) \- **Brett StClair (Novosapien)**

And, yeah, and then I guess the only kind of outstanding issues are around getting access to the content, to the CMS, and to the infrastructure, so we can start looking at how we get it on there, get it hosted, get it up and running.

I'm going to be the first kind of pressing things as soon as we kick off, so I'll keep on just tapping on your door on that one.

Yep, the CMS one is over in five minutes.

[@37:52](https://fathom.video/calls/839476988?timestamp=2272.74) \- **Michael Moores**

So, if you want some, there's some notes here, but public API, short, if you want some webhooks, you can.

And we just need to set them up. For you and you need to go as a URL. Sourcing that across to you and you've got that and let me know if any questions.

Perfect. I'm going to hand over to Hasan, who's been getting a crack on this.

[@38:12](https://fathom.video/calls/839476988?timestamp=2292.17) \- **Brett StClair (Novosapien)**

Are ready? Yeah, I should be already.

[@38:19](https://fathom.video/calls/839476988?timestamp=2299.03) \- **Hasan Ahmed (Novosapien)**

So let me share my screen. So how is, at the moment, this is the existing R\&O caseholder page? I don't know if this has been updated recently, but this is just starting standard APRs.

So if you had to access the actual AI agent, it would just be this small icon here. And it says, ask AI when you hover over it.

At the moment, it's, I'll say, it's quite, I'll say, it's a bit basic. So it's just more going to be like a Q\&A sort of agent.

this one... shouldn't be... We are planning on extending onto it, adding on like a bit of Latin chat history, adding on like if you want to export as well, but at the moment if I do a quick test such as how do I issue a card, if we give it a second, it should hand you all of the key, actually the headers, the key individuals and fields as well, and then also the optional fields, and then it will give you the actual source as well.

So if you want to go to that specific page, if you had to click on that, it will take you straight to that page, and so if you want to take like a Fathom and look into it, and so yeah, if I just, let's say, can you give me an example payload?

Like, it will sort of give you the exact, like, I mean, the exact, like, I mean, I'll say body of it, and all of the, like, I mean, existing headers.

If you want to expand it out, and so it's a bit hard to read here, I mean, you can expand it out into, like, I mean, like, into a sort of, like, bigger window, and so it's easier to read, easier to just copy-paste it, so just do that.

But, um, I mean, I do, like, also have, like, plan on extending it where, like, um, like, all, like, it will be is you have to just, like, click an icon, and then it will just, like, copy the entire payload, and then if you just want to paste it anywhere, into Claude, into the chat GPT, for example, and, and so, yeah, I think, that's all it is at the moment, but, yeah, um, I mean, are there any, like, sort of, other questions?

I mean, I mean, at the moment, is quite, I'll say, basic. So, I mean, as we do extend on, I mean, as we do extend on to it, improve on it, then I mean, there are going to be a lot more features.

And so I do have a plan on if you were to ask a certain question, it will also take you on to that specific page as well.

And so that's just, I mean, like, I would say, like, in, like, a few other weeks or so, like, over the coming weeks, we are going to extend on to it and make it a lot more feature-rich and a lot easier to use.

And so, yeah, like, any questions on this or? Yeah, it looks fantastic so far.

[@41:47](https://fathom.video/calls/839476988?timestamp=2507.0) \- **Michael Moores**

I exactly what we're thinking in terms of being there, asking the AI, obviously, yeah, using the guise, using the reference.

So I think, you know, once we give you the TMS as well, we've got, I think, 51 documents up there.

Now, so plenty for you to use.

[@42:03](https://fathom.video/calls/839476988?timestamp=2523.65) \- **Hasan Ahmed (Novosapien)**

Yeah, I think that looks great so far. So, yeah, thank you.

[@42:08](https://fathom.video/calls/839476988?timestamp=2528.51) \- **Michael Moores**

But, yeah, I think I'm just looking at what Ian mentioned as well in terms of the thing we were sort of passing to Stackworx.

So on each of the guide pages, basically, there's a copy page. So I'm just sort of looking now. So they've got sort of copies, LLM, view is marked down, open in chat, GVT, open in Claude.

So, and then I think the further down, ask question about this page in perplexity. Connect with Cursor, connect with VS Code.

So actually pushing our MCP server into those places. So that's what you sort of mentioned. Stackworx is going build the top couple and obviously ask questions just opens a window.

So I think they can do most of that by just diverting. Obviously, when it comes to installing the MCP, I think that comes later when you've got yourselves sorted as well.

So I am going to write that up properly and send that to Stackworx to start looking at. But I'll copy you in as well, because I think some of the options will be when you guys get ready with this bit as well.

No, I think it looks great so far. Thank you. Yeah, if there's any questions on this, what I'll send you now, I'll that there's three core events, content published, content unpublished, and content deleted.

So you have those. If you want to sort of learn or parse a document, you'll get given the web app with the specific API to call for that document.

So at least you'll get in that constant. We've published new documentation. If you want to sort of parse it through, update, whatever, it's there.

But it's also a, well, this is UAT we're sending you, but a public URL that just pulls down our content.

So that's there as well. Perfect. Thank you. Awesome.

[@43:50](https://fathom.video/calls/839476988?timestamp=2630.06) \- **Brett StClair (Novosapien)**

Thank you very much, everybody. Thank you.

[@43:53](https://fathom.video/calls/839476988?timestamp=2633.92) \- **Michael Moores**

Happy days. Cheers. Take see you guys soon.

[@43:56](https://fathom.video/calls/839476988?timestamp=2636.82) \- **Brett StClair (Novosapien)**

Take care. Have a good way. Thanks very much. Bye-bye.

