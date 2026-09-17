---
date: 2026-09-16
type: general
description: "Phase two set: acceptance follows UAT, the knowledge hub is next with MCP first, demo data becomes a sales requirement, and messaging gates all content"
scope:
  - "[[developer-support]]"
  - "[[delivery]]"
  - "[[content-workforce]]"
  - "[[outbound]]"
status: extracted
extracted-to:
  - "[[developer-support]]"
  - "[[docs-mcp-server]]"
  - "[[portal-co-pilot]]"
  - "[[access-gating]]"
  - "[[support-triage]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Next Phase Discussion (2026-09-16)

> **Source:** Fathom transcript, 16 September 2026, 11:00 CEST, 1h 15m. **Brett StClair**, **George Westbrook**, **Max Kingaby**, **Tyler Thompson**, **Hasan Ahmed**, **Vineth Siriwardana** and **Lily St. Clair** with **Ian Johnson**, **Dorte Dye** and **Michael Moores**.
>
> **The agenda Brett set:** where the pilot landed, a fast start on the developer portal, the next phase of work, and a status on both GTM workforces. Ian added one item: read the flight plan together *"in just plain English."*
>
> **This is the call flagged the day before** as the natural place to answer Ian's value question ([[open-questions]] #88). It was not answered directly. What happened instead is that **the next phase got defined**, and the definition is an answer of a different kind.

## The flight plan said the wrong thing about acceptance

Ian read it back rather than accepting it, which is the useful thing he does:

> *"I can see that the pilot acceptance is down to be confirmed in writing on the 18th, so Friday. And then the assertion is that it's complete, because what was asked to be built is complete, and the fact that the speed we talked about yesterday is something that's going to be corrected but it doesn't delay the acceptance of the pilot. So just explain the logic behind that for me."*

**Brett withdrew the wording:**

> *"It's poor articulation of our discussion. Essentially, when you guys are finished with the UAT, then we can send an invoice, and based on that, anything still outstanding we'll still make sure we fix... **We just didn't get to a date.** Tried to articulate that poorly."*

So the position is:

| | Position |
|---|---|
| **Trigger** | **TXN finishing UAT**, not a calendar date. The 18 September date is withdrawn |
| **Invoice** | Follows UAT completion |
| **Outstanding items** | Still fixed afterwards, including the speed work |
| **Date** | **Still none.** Both sides acknowledged that explicitly |

Ian: *"Okay, understood."*

**This is the fourth time acceptance has failed to acquire a date** ([[open-questions]] #54). It is no longer a collision of calendars, because the retreat and Michael's leave are both past; it is simply that TXN's UAT is unfinished and nobody has said when it will be. The difference now is that the trigger is agreed even though the date is not.

## Speed first, and Ian added a reason nobody had raised

George set out the speed work, confirming what was agreed on 15 September and adding detail:

- **Rewrite the SOPs again** so the agent asks up front: *"who do you want to suspend? Things like that"*, rather than doing ten tool calls to find out.
- **Composite tools.** Not one tool per API call: *"there might be three or four API calls within one tool call."* The point is turns, not calls: *"even though it's making the same amount of API calls, from the agent perspective it's a lot less turns."*
- **Concentrate effort where the value is**, the long-horizon tasks that would take five or six Console pages, *"and make people go, hell yeah, this is very good."*

Ian accepted the direction and then raised the thing that makes it harder.

### The demo data problem

> *"Some other stuff will have no value until there's a large number of transactions in the platform. But equally, if we don't have that capability, we can't demonstrate it, then it lessens the sales proposition, because you're asking [people to] buy something on a belief that this feature functionality is going to be there."*

> *"We've got to figure out a way of somehow getting enough dummy transactional data into somewhere on the platform that we can actually demo the AI features in action. **Otherwise that whole ethos of show, not tell, goes out the window**, which to tech-focused buyers would seem a bit strange, that we'd be going back to 'just trust us, this is how it'll work' and then not being able to show it."*

> *"If we build something, and I agree we should be focusing on where the value is, then we have to have a mentality of being able to demo it, otherwise there's no point."*

**This creates a requirement that sits across delivery and sales**: every AI feature built for the launch needs a demonstrable state, with enough synthetic transaction data behind it to show the feature doing something real.

**George's answer, and it turns an accident into an asset.** The Console Novosapien built for the pilot becomes the demo surface: *"it feels and acts like the real thing"*, Stackworkz said it looks exactly like their prototype, and *"we've got loads and loads of test data that's matching up to what you would have in the API."* He added **recorded demos**: Loom explainers for the moment a prospect says *"okay, show me"*, and videos on the website. Ian agreed.

That is a second use for `txn-console-react`, which until now has been described as scaffolding for the experiment. It is now also the demo environment and the source of sales collateral.

## The knowledge hub is the next build, and the priorities are set

The largest part of the session, and it produced a clear order.

### Why it comes first

Michael: *"if you look at the order we're putting things in, people integrating and getting on there would be first in the flow. The pilot is very much console... in the natural order of things, when a client reaches a console it's going to be much later than when they start integrating."*

Ian's framing is the engagement's own theme, applied to developers: *"the stuff we've done in the content workforce is about not needing to have card expertise to be able to build a card program."* His worry is the web of relationships between accounts, cardholders, card products, and the answer *"go and read the guides"*:

> *"If the answer is you can go and read the guides, that could be the same answer for all AI. It's all there. If you want to go and find the answer to something, you can do it the really long way, or you can do it the super simple way."*

George on why that matters now: *"a lot of developers are getting more inherently lazy, in that they're like, I don't want to read the documentation. I just want to speak to my AI which is going to find the page, which is going to tell me the payload, what I need to do on my end."*

### The order

| Priority | Surface | Reason |
|---|---|---|
| **1** | **MCP server**, exposed externally so a developer's own Claude or ChatGPT can query TXN's docs | Michael: *"having that MCP so they can not only navigate but start building towards the APIs... that'll really help speed up the integration with our clients. That for me is a number one."* Developers *"are going to know how to connect an MCP server"* |
| **2** | **Unauthenticated co-pilot** in the knowledge hub | Question and answer over the docs, with links out. *"It provides a good base to push off of"* for later authenticated features |
| **Dropped** | `llms.txt` | *"All that really is is one long text file... having a 20,000 line file is just going to bloat the context for their AI and potentially decrease the quality of the answer"* |

**George's MCP design is a deliberate departure from the usual pattern**, and it mirrors how Novosapien's own vault MCP works:

> *"When it comes to searching, some people put it in a vector database. I just don't think it's the best way any more. What we do with the MCP server is expose effectively like a bash tool, which will tell their Claude, write bash commands in here, which will execute and search through it in exactly the same way Claude Code did if it was a local file system, but it would all be in the cloud. So from their perspective, their Claude thinks they're searching a local file system."*

With the obvious caveat handled: *"you don't really want an agent executing random bash commands on a server, so all we do is severely limit the amount of commands that could be done. It'd be tightly scoped, it'd be all isolated."*

**He also separated the AI surfaces cleanly**, which the vault has held loosely until now: the **co-pilot in the knowledge hub or dev portal**, the **co-pilot in the Console**, and the **full agentic experience** with alerts alongside. MCP servers are portable microservices, so the knowledge MCP is a different server from the one the agentic experience uses, and either co-pilot could consume either.

### What TXN wants it to do, in Michael's words

> *"Where we start for MVP, it will be very much ease of integration with both of those two things... how quickly can we get live for them."*

He described the documentation structure it sits on: *"a logical get your first request done, here's everything that's in order."* The guides deliberately do not repeat the payload, *"because we don't want to update it all the time"*, so they reference the API reference instead. **The AI's job is to merge the two layers back together:**

> *"The agent layer or the co-pilot layer would be potentially merging those two things back together into one interface, where you can ask a simple question and it'll be, okay, you can see this account does this, and this is a field you need to do X, Y and Z. I think that's the benefit there, of pulling those two layers which are purposely separate into one context."*

## Cost exposure, and the email gate

The knowledge hub MVP has **no sign-in**: *"purely here's information, how to connect to us."* Ian raised the consequence.

> *"How do we cap the amount of stuff that somebody can do?... How many people are going to come and try out the knowledge hub where we have no revenue line, and how much is that going to cost us? At the moment that's completely unlimited, because we're not putting any stops in there."*

His worst case: *"a competitor comes in, we've got no way of blocking them because we're not asking them for an email address, and they can just keep messing with us for as long as they like."*

**Brett's answer, accepted:**

> *"If you do want to use agentic AI, that's the prompt for an email address. **All these functions should be triggers to gather more information, but at the same time you're using that information to protect yourself.**"*

> *"Here's a knowledge hub, it's like a website. You want to browse and use some really good features on here? Please log in with an email address and your company details."*

**Ian's condition, and it is a real one:**

> *"We then have to make sure that we've got some kind of video on the website where people can see what that would be like. Otherwise it's saying, give us your email address and then we'll open up some tools for you... people are going to be like, I don't know what I'm going to get if I do give you my email address."*

So the email gate **depends on the demo videos** from the earlier section. The two requirements are the same requirement.

**Corporate email only.** Ian wants Gmail and the like blocked; Brett: *"it's becoming a norm, please submit your work email, and all we do is block Gmail, Yahoo, and in Max's case AOL."* Ian's own caveat from Marqeta: a genuine early startup may not have a corporate address, so there must be a contact route for them. His reason for the gate is not cost alone: *"we're interested in businesses, and we don't want to expose a bunch of capability to people that aren't a business."*

**Where he landed**, after Brett's point about disposable code:

> *"As long as we know there's a way, that there are mechanisms to cap our exposure, then I'm okay with that."*

> Brett's framing: *"you're in a world where code is throwaway-able... very quickly we can change and amend it if it's not working in a direction. Test something, it doesn't work, fail it, kill it. Those cost elements are small, and it opens you to a world where you can take a different level of risk."*

Ian's own read on the real risk is that it is small: nobody spends serious time in a new company's knowledge hub without intent, and the likely visitors are competitors checking whether the ease-of-integration claim is true, *"which I would do the same thing as well."*

Michael's framing of the trade-off is the one to carry into the decision: **"Will you win sales with the AI, versus how much does it actually cost to run that if people don't sign up with us?"**

### Session continuity without a login

George: an unauthenticated user has no history, *"let's say yesterday they asked 20 questions, they come in the next day, that chat's not going to be there."* A cookie might work, *"but I don't know if that would be durable enough."*

Michael wants at least a cached session ID for MVP: *"if I come back tomorrow and just want to add on to an additional question, that would be beneficial."* Full history is a later phase.

**And he set out why the history matters commercially**, which is the strongest argument for the gate:

> *"As they're looking at us and as they're investigating, if they want to be with us, we have a lot of context. By the time they decide they want to go with us, we know what they want to build, who they are... you've given them something that might be 95% fit. It just means they've got the core set up and they might make a few tweaks, and that really cuts down the time."*

That connects the knowledge hub directly to **program onboarding** in the Console: the context gathered before signature becomes the configuration after it.

## Two requirements Ian made non-negotiable

### 1. Sandbox error diagnosis, from day one

George proposed it: if a developer is logged in and hitting the sandbox, the agent can read their request logs. *"Let's say they're pinging one endpoint and they keep getting a 422 error. The documentation says it is issuer ID with a capital I, but they're putting in [something else]... when it can look at the logs, it's a lot better than a user looking at their request, looking at the response."* Then the fork: *"is it a them issue"*, in which case tell them, *"or if it's an us issue, ping Michael."*

**Ian made it a must-have:**

> *"That to me, Mike, must-have. It's a priority, because otherwise I don't really see that we're making that much of a dramatic effort to streamline integration."*

> *"If I think about your role when you were helping on those project calls at Marqeta, a lot of it was that people don't know why they've got an error... and you're able to say, this should be this, you've set the parameter incorrectly. **That to me is something that shouldn't be done by a human any more.** So I think we need to think about that being there from day one."*

**His fallback if logs are not available**, and it is a sensible phase one: *"they could just paste what they're putting in into the co-pilot, say this is what I'm getting, and we can then tell them where the error is, which ultimately does the same thing."*

**Michael's constraint is the blocker, and it is not ours.** There is no per-user sandbox today: *"it's just an authentication from the knowledge hub to the sandbox. So the knowledge hub will be that authenticated entity."* Per-user private sandboxes, the Marqeta model he described, depend on DT and a public sandbox that does not exist yet.

**So the phased answer is already visible:**

| Phase | Mechanism | Depends on |
|---|---|---|
| **Now** | The *try it now* panel is browser-only and shows errors on screen; the AI reads that screen context, *"similar to what it does in console"* | Nothing outside TXN |
| **Next** | Paste the request and response into the co-pilot for diagnosis | Nothing outside TXN |
| **Later** | Read the user's own sandbox logs, diagnose, and escalate to TXN when it is a platform fault | DT, plus per-user sandboxes |

George added a commercial consequence: an authenticated developer hitting the sandbox is also a **lead**, and the endpoints they call and the errors they hit could feed the outbound message. Ian: *"super interesting."*

### 2. The anomaly loop

Ian raised the case nobody had: what happens when the guides and the API reference disagree, which they will.

> *"There were anomalies. There were things at Marqeta that people found: that's not right, it says this and it's actually this. And I can imagine those being exposed in a co-pilot, because the AI wouldn't know what else to say. It would basically call them out."*

Michael confirmed the exposure plainly: **"At MVP the main knowledge is going to be the YAML and the guides. So if the guides are wrong, the AI may be wrong."**

**Ian's requirement is about the interaction, not the fix:**

> *"If we don't know about it, the only other person that can tell us is the user. So if I'm the user, okay, there's an anomaly. What is the AI going to tell me about what action is being taken about that anomaly? And it should be as simple as, we've advised the platform team, this will be fixed shortly."*

**George's design:** the co-pilot offers to report it, with the whole conversation as context, into an email or a support ticket. His description of how these loops mature internally: *"first maybe an agent will analyse and then give us a ticket, then we'll go in and do the fix. But over time it progresses to the point where the agent creates a support ticket, the agent updates. But the first step is always just finding an easy way to get it down. **The co-pilot would be one of the perfect surfaces to do that.**"*

Michael's longer arc: **self-healing documentation**, comparing Freshdesk tickets against the docs, *"you're saying this thing to customers, but your guides say something else."* Later phase.

George also named a hygiene requirement that makes all of this work: pull the documentation from **Umbraco** continuously, *"so that there's not a point where the MCP server or the co-pilot is pulling in documentation that's a month old."*

## Most of this was already specified in June

Worth stating plainly, because it is the strongest evidence the discovery work was sound.

| What TXN asked for on 16 September | Already specified |
|---|---|
| An MCP server a developer's own agent can query | [[docs-mcp-server]], with L1 docs and L2 sandbox access, API-key gated |
| A light co-pilot over the docs, grounded with source links | [[portal-co-pilot]] |
| An email gate that protects cost and captures leads | [[access-gating]], a four-level gate with L2 as *name plus corporate email* |
| Plain-language help on failed sandbox requests | [[sandbox-assist]] |
| Diagnose from the user's own API logs and package a ticket | [[support-triage]], which uses **the same 422 example** |

**So this session is a prioritisation of existing scope, not an expansion of it.** The genuinely new material is the demo-data requirement, the bash-style MCP search design, the anomaly-reporting interaction, and Michael's constraint that per-user sandbox logs do not exist yet.

## Developer portal status

| Item | State |
|---|---|
| Build | Stackworkz say it is done. **In staging, not production** |
| Access | The website is not up yet, and that is how it will be reached |
| Environment | Needs end-to-end testing after moving from Stackworkz to **DT's European instance**. *"There shouldn't be any functional changes"* |
| Umbraco | Set up |
| Freshdesk | Set up and integrating now |
| Michael's own list | Writing the documentation |
| **The blocker** | **The guides and the accuracy of the YAML.** Michael: *"that's the last lever that's on DT... obviously there's been quite a lot of errors there. So that's what we're waiting for"* |

**Decision: prototype the AI first.** Brett proposed building a demo version of the knowledge hub AI the way the agent Console was built, *"so you can get a feel, and it gives you an idea on that requirement."* Ian agreed: **"Mike, I'm happy that we go with that as the next priority."**

Ian also set the order for the DT conversation: *"let's be clear on what it is that we're going to deliver before that conversation takes place, so that we're concrete in what we're actually asking."*

Michael offered the material to build against: the Stackworkz dev environment, the latest prototype, and a **UAT URL**, *"that's the one we're testing against as well."*

## Content Workforce

**Tyler has drafted.** One article each for Ian and Dorte, plus **a corresponding TXN article for each**, sent for review: *"give me approval or any feedback so that I can then refine the model."*

**Ian blocked publication on one thing, and was unambiguous about it:**

> *"The first thing is we need to get the output of the various interviews and where you've arrived at for the positioning and messaging of the company. **That's the number one thing, because everything essentially needs to flow from there.**"*

> *"Before we start producing and exposing content, we need to make sure that the manifesto and the core messaging, positioning and brand and tone of voice document is there, and that's the basis of everything that gets used."*

It has to go to **Bronwyn** and the **independent PR consultant** for alignment first. Ian expects it to be close: *"I don't think we're a million miles off, because I haven't said anything any different since I joined the company."*

**And he confirmed what [[open-questions]] #63 was chasing:** *"the tone of voice and the brand document was actually fed in directly from work we did last year with Bronwyn."* So Bronwyn's material did reach the platform, through Ian's own onboarding.

**Format: PDF, not HTML.** Brett offered branded HTML; Ian: *"it's just easier for sharing, people reading on various devices."* His framing of the ask is worth keeping: **"I know you're working in an AI world, but I need this in a human world that can be shared."**

**LinkedIn.** The TXN page exists but is unbranded; **Bronwyn is setting up the imagery** and Ian needs a completion date. No objection to giving Tyler access; Dorte will send the details, and Tyler must follow the page before she can grant it.

**Ian wants a separate session on strategy**, and gave a fair criticism of the proposal: *"the proposal is pretty high level, Brett. It's not a criticism, but it's pretty high level about a number of pieces of content that get produced. So we just need a bit more detail."* He also wants to understand **how readership is maximised** for a company nobody knows yet.

**Booked: a content session on 17 September, 11:00 to 12:00.** Max and Tyler had already prepared for it.

## Outbound Workforce

**Ian's priority is the list, and he thinks it is too small:**

> *"The number one thing before we do anything is, who are we doing it to? So how are we building this target list of accounts? I've obviously submitted something to you guys. **My initial assertion is it doesn't seem to be big enough.**"*

He also asked how the list stays current, and named the segment the vault has worried about since 25 August: *"how are we sourcing target companies? They might be in incubators, they might be very early stage startups... to make sure that we're not missing out on companies that might be in stealth, or they might not be in market yet."*

> **Note:** Ian recalled *"five categories"* from the ICP work. The framework settled on 3 September has **four** card program statuses ([[icp-definition]]). Probably a slip, but worth confirming rather than assuming, since he is the author.

**Domains: George reported approval, Dorte corrected him.**

> George: *"we started yesterday and the day before, but put it on hold till we'd spoken to Alex and got everything approved. Now we've got the approval."*
>
> Dorte: *"**Maybe just a step back. There wasn't an approval.** We just discussed the approach, how we split it. Alex is going back to run it via Gavin to get Kevin's sign-off."*

**And the domains already bought may be wrong:** *"the URLs are another one. What George and the team has already purchased might not fit in what your thinking is. So I made sure that you are in the loop of which ones we actually want to purchase."*

Three names appear here for the first time: **Alex**, **Gavin** and **Kevin**, on TXN's side of the domain approval.

**Ian is not rushing it:** *"it's not like we want to start the outbound stuff tomorrow. The most important thing is what are the lead lists we're targeting."* Content can go earlier, because a LinkedIn post *"is not being sent specifically to somebody."* But: *"we just need to get it right rather than move super fast."*

## Findings and where they landed

### Delivery and acceptance

| Finding | Destination | Action |
|---|---|---|
| **Acceptance follows UAT completion, not the 18 September date** on the flight plan | [[delivery]], [[open-questions]] | **#54** updated; the date is withdrawn |
| Invoice follows UAT; outstanding items including speed still fixed afterwards | [[delivery]] | Recorded |
| Composite tools: three or four API calls per tool call, to cut agent turns | [[agent-orchestration]], [[tool-catalogue]] | Recorded |
| **Demo data: every AI feature needs a demonstrable state** | [[open-questions]] | New row **#90** |
| `txn-console-react` becomes the demo surface and the source of sales videos | [[delivery]], [[full-agentic-experience]] | Recorded |

### The knowledge hub

| Finding | Destination | Action |
|---|---|---|
| **Knowledge hub is the next build, and MCP is priority one** | [[developer-support]], [[docs-mcp-server]] | Priority order recorded |
| Unauthenticated co-pilot second; `llms.txt` dropped | [[portal-co-pilot]] | Recorded |
| **Bash-style scoped search over cloud docs, not a vector database** | [[docs-mcp-server]] | New design detail |
| Three AI surfaces named, MCP servers portable between them | [[developer-support]] | Recorded |
| The AI merges the guides and the API reference, which are deliberately separate | [[portal-co-pilot]] | Recorded |
| **Email gate on AI features, corporate addresses only** | [[access-gating]], [[open-questions]] | New row **#91** |
| Session continuity without login, by cached session ID | [[access-gating]] | Recorded |
| Pre-signature context feeds program onboarding after signature | [[developer-support]] | Recorded |
| **Sandbox error diagnosis is a day one must-have** | [[sandbox-assist]], [[support-triage]] | Recorded with the three phases |
| **No per-user sandbox exists**; the hub authenticates as one entity | [[open-questions]] | Recorded in **#91**; DT dependency |
| **The anomaly loop: the AI must report doc errors back to TXN** | [[support-triage]], [[open-questions]] | New row **#92** |
| Pull documentation continuously from Umbraco | [[docs-mcp-server]] | Recorded |
| **Most of this was specified in June** | [[developer-support]] | Recorded as confirmation |
| Portal in staging; blocked on guide and YAML accuracy at DT | [[open-questions]] | Added to **#32** |
| **Prototype the knowledge hub AI first**, as with the agent Console | [[developer-support]] | Agreed next priority |

### The workforces

| Finding | Destination | Action |
|---|---|---|
| **Messaging output gates all content**, and must be a PDF for humans | [[content-workforce]], [[open-questions]] | **#63** answered, new gate recorded |
| Bronwyn's brand and tone work did reach the platform, via Ian's onboarding | [[open-questions]] | **#63** answered |
| Tyler has drafted four articles for review | [[content-workforce]] | Recorded |
| LinkedIn page unbranded; Bronwyn setting up imagery; Tyler needs access | [[content-workforce]] | Recorded |
| Ian: the proposal is high level, and readership strategy is undefined | [[content-workforce]] | Recorded |
| **Ian: the target list "doesn't seem to be big enough"** | [[outbound]], [[qualification-matrix]] | Recorded |
| **The domain approach was not approved**, contrary to George's report | [[delivery-schedule]] | Corrected |
| Domains already purchased may not match Ian's intent | [[delivery-schedule]] | Recorded |
| Ian recalled five ICP categories; the framework has four | [[outbound]] | Flagged to confirm |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Send the messaging and positioning output **as a PDF** | Brett | Ian's number one item; gates all content |
| Review Tyler's four draft articles | Ian, Dorte | Sent during the call |
| Content workforce session | All | **17 September, 11:00 to 12:00** |
| Send Tyler the LinkedIn page details, after he follows the page | Dorte | |
| Confirm when Bronwyn finishes the LinkedIn branding | Ian | |
| Prototype the knowledge hub AI, MCP first | Novosapien | Agreed as the next priority |
| Confirm the domain names with Ian before purchase | Dorte | Kevin's sign-off still pending via Alex and Gavin |
| Build and review sample lead lists | Novosapien | In parallel with domain warming |
| Test the portal end to end in DT's European instance | Michael | After the move from Stackworkz |
| Fix the guides and YAML accuracy | DT, via Michael | The blocker on going live |

---

## Transcript

## **TXN Next Phase discussion \- 2026/09/16 11:00 CEST – Transcript**

# **Attendees**

Brett StClair, Dorte Dye, Dörte's Fathom Notetaker, George Westbrook, George's Fathom Notetaker, Hasan Ahmed, Ian Johnson, Lily StClair, Max Kingaby, Michael Moores, Michael's Fathom Notetaker, Tyler Thompson, Vineth Siriwardana

# **Transcript**

George Westbrook: Hello.

Dorte Dye: You look like you're sitting in a cell with a wooden ceiling. You always have to show off. Thank you very much.

Brett StClair: I'm in one of those old Tuscan farmhouses.

Brett StClair: It's not actually in Tuscan. Morning.

Dorte Dye: I mean, Mike at least looks like you got a good tongue compared to me.

Dorte Dye: I'm just being back in old England.

Ian Johnson: Honey flakes.

Brett StClair: I'm trying to see if we can load more Fathom notetakers than people.

George Westbrook: What's the ratio at the moment?

George Westbrook: There's three. we prefer the API for Fathom actually.

Brett StClair: 

Dorte Dye: I think that's just…

Dorte Dye: George, because you don't trust Google to transcribe it correctly.

George Westbrook: The Google one you can do it. It's just the Fathom one's a lot better.

Brett StClair: I'm going to test if the pushto talk feature on Google works whether I can just use that.

George Westbrook: We can't hear you.

Brett StClair: Okay, you can't hear me.

George Westbrook: When you push,…

George Westbrook: we can obviously. Yeah.

Brett StClair: …

Brett StClair: shall we kick off? so a couple of things we need to cover in this call is the status on …

George Westbrook: Yeah.

Brett StClair: we covered quite a bit yesterday, but let's just do a recap on where we landing with the pilot. Then let's talk about your fast kickoff on the dev portal and what can be done there and some of the ideas that we've got going there. Then let's talk about the next phase of work that needs to be put together, what's outstanding, where all the different players are and then do a cover on where we are with the work forces. So that's Sorry, the kitchen is right by me. I'm just going to go find a quieter spot.

George Westbrook: I don't think we had that last part, right?

Brett StClair: 

Brett StClair: My apologies. for the content and work forces for the outbound give you a status on where we are and what our thinking is on all those positions. to want to cover you.

Brett StClair: So the workforce is on content and outbound. And then Ian, is there anything else that we want to cover through this?

Ian Johnson: No, I think it'd be worth just sent across the flight plan. I think it's worthwhile just making sure that we're all aligned on that, having a quick read through it. but let's talk in just plain English about where we are, I think. So, I can see that the pilot acceptance is down to be confirmed in writing on the 18th, so Friday.

Ian Johnson: And then I think what the assertion is that it's complete because what was asked to be built is complete and the fact that the speed that we talked about yesterday something that's going to be corrected but it doesn't delay the acceptance of the pilot proposal. So just explain the logic behind that for me.

Brett StClair: it's poor articulation of our discussion in so essentially when you guys are finished with the UAT and then when we can send an invoice and based on that anything still outstanding we'll still make sure we fix anything that might still be outstanding after the UAT.

### 00:05:00

Brett StClair: We just didn't get to a date. It's tried to articulate that poorly.

Ian Johnson: Okay, understood. so…

Brett StClair: Mike, have you got the flight plan as well? Shall I forward that?

Michael Moores: Yes,…

Michael Moores: please. There is heat.

Dorte Dye: I sent it.

Brett StClair: Okay. …

Dorte Dye: No, I sent it this morning.

Brett StClair: you've sent it.

Dorte Dye: As I got it in for bread,…

Brett StClair: Okay. Okay. Cool.

Dorte Dye: I sent it on to you

Ian Johnson: then there's a point that says what is being done about it? Decide what belongs in the agent by Fix speed first then decide and do not push simple actions out the agent prematurely. So that says state 16th September call. So what does that mean?

Brett StClair: So that's just putting a priority on getting all your speed issues worked on ASAP.

Ian Johnson: But then until that's done, we can't decide what's going to go in the agent. So, what's the plan in terms of you guys moving forward?

Brett StClair: George, do you want to walk through what you're currently working on and how we're addressing speed issues?

George Westbrook: Yeah. Yeah.

George Westbrook: So, I think it's first of all, rewriting the SOPs again. so that like we were saying yesterday, it's rather than it be I'm going to suspend a card. then it will do some investigation and be like, I've read all your card holders, read that, blah. Which ones do you want it to be? Just up front. Just ask as much detail as possible. who do you want to suspend? Things like that. Obviously, all of the other ones as well.

George Westbrook: So more upfront questioning so that rather than it going away doing 10 tool calls it's just going to solve a lot of those problems earlier in the instance where it has got to do a lot of tool calls is they call them the special tools. So rather than it being one kind of a onetoone mapping to the API it's not quite that but rather than it being something like that they're more kind of composite. So there might be three or four API calls within one tool call. So it's limiting the terms that the agent's having. So when I say a turn of the agent, it's user response or a tool call execution and the result return. cutting them down as well. so even though it's making the same amount of API calls, from the agent perspective, it's a lot less terms. so that should speed it up a lot as well.

George Westbrook: But where we are thinking I know it seems premature but if we can focus on certain areas of the agent where it's actually going to add loads of value and where do we want to put that effort? So those longer time horizon things where it's maybe five or six pages in the console just sitting down and thinking right okay these are going to be the things which are going to actually add a lot of value to users making sure that some of those trick actions are quicker as well but maybe putting more eggs in the basket of the things that's going to add more value and…

George Westbrook: make people go f\*\*\*\* hell yeah this is very very You keep it.

Ian Johnson: Okay, understood.

Ian Johnson: So I suppose in thinking about there's a combination of what's going to add the most value and…

George Westbrook: What's different.

Ian Johnson: a timing piece from my perspective might some other stuff will I have no value until there's a large number of transactions in the platform but equally if we don't have that capability we can't demonstrate it then it lessens the sales proposition because you're asking buy something on a belief that this feature functionality is going to be there so I do think finding the value items is the right thing to do. But then Mike, I think we've got to figure out a way of somehow getting enough dummy transactional data into somewhere on the platform that we can actually demo the AI features in action. Otherwise, that whole ethos of show not goes out the window, which would seem

Ian Johnson: I think to tech focused buyers would seem a bit strange that we'd be going back to the thing of just trust us this is how it'll work and then not being able to show it. So if we build something and…

### 00:10:00

Ian Johnson: And I agree we should be focusing on where the value is then we have to have a mentality of being able to demo it otherwise there's no point

George Westbrook: So, is it worth us keeping Well,…

George Westbrook: I mean, we're going to do it anyway, but the kind of console that we've built becomes that demo part for a lot of the AI features. obviously there'll be a point in time where the real console will be the thing that is being demoed on. but for the time being, and correct me if I'm wrong on this, but the console that we've got feels, and acts like the real thing. maybe there's a bit of alignment needed with stack work, but when we spoke to them before,…

Ian Johnson: Yeah.

George Westbrook: they said it looks exactly like what the prototype they had.

George Westbrook: And because that's what we've got at the moment. we've got loads and loads of test data that's matching up to what you would have in the API. so hope that that should suffice. and I think as well maybe what we could do is get some videos as well. Maybe some Loom videos so that maybe with the cold outreach and when it's reaching a point in time where somebody's "Okay, brilliant. Yeah, you're telling me all about this AI functionality you have you got any evidence of it for a call?" Maybe packaging in some demos of it or maybe adding it to a website as well. because We haven't done it yet. I know there's kind of a video we've got on our website that we did ages and ages ago for the contact of

George Westbrook: which we created with which basically uses the raw components from the actual content workforce to create a video AI voice everything so as well as in person on a call where using the actual console there's recorded loom videos that are explainers and then also videos that go onto the website as well because I agree with you in when you've got somebody who said a company that says yeah AI does this amazing thing and…

George Westbrook: you're like, "Okay, show me." And it's like, " we'll book a demo." you're a bit hesitant.

Ian Johnson: Yeah, agreed.

Ian Johnson: Okay, cool. That's sounds good. the No,…

George Westbrook: Sorry. Go.

Ian Johnson: go ahead.

George Westbrook: Because I think the second part that we wanted to talk about was the knowledge slash developer portal.

George Westbrook: because obviously there's still loads of work that needs to be done with the agent. but in parallel obviously starting to make some progress on the knowledge Obviously that's going to be the first thing that's going to be released. I think for us it'd be really good to talk about you guys in terms of that AI functionality. Where do you what needs to be there at launch? What needs to be there slightly after launch and…

George Westbrook: maybe setting some priorities there. and then given that we can kind of discuss we might need to do xyz before we focus on that as well.

Ian Johnson: Yeah. …

Ian Johnson: conscious might you and I haven't had chance to catch up. but obviously from a sequencing point of view, the knowledge hub is the first thing that's actually in the wild. and there's not as much with the knowledge of George that we can do that adds meaningful value, but my mind is pretty much on the fact that when we spoke to Stack Works and we got feedback from kind of some of the developers that it's difficult because they're in it and they have this thing of we'd be okay with the documentation's is pretty clear etc.

Ian Johnson: I just got this thing there's so many inter relationships Mike with different entities on our platform whether it's account card holder card products whatever it might be and that the guides are being produced understood that they're going to be I think the plan was to scale back some of the detail might because of the issues with changing field names from DT as they build but the plan ultimately would be to have the guides specifically referencing field names in the API. But in my mind as a non-developer if I

Ian Johnson: don't know this stuff. And if you bear in mind the stuff we've done in the content workforce stuff which is about not needing to have card expertise to be able to build a card program. That's one of the themes. if you don't have it then the inter relationship between these different entities on the platform. how would and understand them? If the answer is where you can go and read the guides, that could be the same answer for all AI. It's all there. if you want to go and find the answer to something, you can do it the really long way or you can do it the super simple way.

### 00:15:00

George Westbrook: Wait, stop.

Ian Johnson: And I guess what's in my head is people might know some of it and then start building and then they come across something that they're not quite sure of. And yes, they can go to the guide or they can just ask AI the question and we produce the guides and the information. So we've got the source. Its just can we add value by giving somebody an answer without to go and troll through documentation. However good the documentation is I mean what are your thoughts on it as a kind of tech team?

George Westbrook: So I think a lot of developers are getting more inherently lazy in that they're like I don't want to read the documentation.

George Westbrook: I just want to speak to my AI which is going to find the page which is going to tell me the payload what I need to do on my end blah blah blah that's me. I can imagine Mike as well obviously you're quite AI first so it's never let me scout through each and every page. there's a time and a place for that. 100%. I think it's just now a lot of developers are maybe going more AI first. which I so given that I think the two point points of the two parts when it comes to the knowledge hub that I think would genuinely add value are the MCP server and the co-pilot both which kind of build on top of each other so I think me and Han were having a discussion about this this morning so I think the MCP server one that can be exposed to people exter

George Westbrook: externally so that if they want to chat with it with their claw their chat DPT I mean they're developers at the end of the day so they're going to know how to connect an MCP server but there can be a page in there as well and the way in which we do it is similar to how we do with the vault MCP servers wherein so when it comes to searching some people putting it in a vector database doing it like that I just don't think it's the best way anymore for example with us we have a lot of things on our local file

George Westbrook: system which store code would then execute bash commands in order to search through it. so what we do with the MTP server is expose effectively like a bash tool which will tell their claw write bash commands in here which will execute and search through it in exactly the same way code did if it was a local file system but it would all be in the cloud. so from their perspective, their claw thinks they're searching for a local file system. but they're inherent issues with that, which are not issues, are you don't really want an agent executing random bash commands on a server. so all we do is severely limit the amount of commands that could be done. so it'd be tightly scoped. It'd be all isolated.

George Westbrook: So one that's for exposing it to their agent, but also the second point, the piloter. so having that co-pilot in the corner that's got access to that knowledge so when somebody's reading through, it can be like I want help integrating with TXM platform. This is not what I'm doing. This is what I'm unsure of. And it's going to search through that knowledge base. and give them links to external pages. could do some other stuff as well like sending an implementation plan given the question questions that they've asked to their email. I think that's later down the line. but I think there's a lot of value that we could add to the so if I'd say co-pilot and MCP server would be the two biggest things. because there's the LLM.txt

George Westbrook: txt as well, but all that really is just one long text file which the LLM pulls in can add some value. it's just usually somebody's going in with a query about one thing or one or…

Ian Johnson: Mike thoughts.

George Westbrook: two things. So having a 20,000 line file is just going to bloat the context for their AI and potentially not decrease the quality of the answer.

### 00:20:00

Michael Moores: Yeah. Yeah. Obviously I think if you look at the order we sort of putting things in I think potentially if you're looking at people integrating and getting on there first would be the first in the flow. I'd say obviously the pilot is very much sort of console I find at the end. So obviously in the natural order of things when a client reaches a console it's going to be much later than I think when they start integrating. So for me having that MTP so they can not only navigate but start building towards the APIs I think is the initial first one for me that'll really help speed up the integration with our clients and obviously we've also got that pilot one which is equally important but I think that's going to require a program to go Eyes.

Michael Moores: then they're going to start using it through the console to actually drive, customer service and stuff like that as well. So, I think for me the MCP were the biggest hit to start with, especially as we're trying to get people to show what we can do, how easy it is to integrate. I think that for me is a number one

George Westbrook: I think in terms of the co-pilot, I wasn't meaning the co-pilot in the console. I meant kind of like a co-pilot within the actual knowledge so it' be a lot simpler where it's not really taking actions. it's more just that kind of knowledge retrieval. there is scope to allow it to take actions for example first line support. So they could go in there maybe there's a button submit a ticket and then it's going to maybe do a bit of investigation given the documentation obviously not touching anything on their system but I suppose it's the different AI surfaces are the co-pilot in the dev portal or knowledge hub the co-pilot in the console and obviously what we're calling the full aent experience along with obviously the other bits of the AI workforces like the alerts but I suppose

George Westbrook: Let's call them the main three. and when I say MCP servers as well, there's the MCP server that the bullet genic experience is currently using. and then it's going to be a completely different MCP server for the knowledge. the good thing is they're like microser so they're portable. So that MCP server could be used by the co-pilot or could be used by the pogenic experience.

Ian Johnson: Yeah.

George Westbrook: In the same way that if we wanted to get the developer console to be able to take actions…

George Westbrook: if somebody's authenticated, we could do as well.

Michael Moores: Yeah, I think obviously from the way we are with the knowledge hub is I think very much going to be sort of in integration is the main thing.

Michael Moores: Obviously we're not any sign in to start with. It's purely here's information how to connect to us. So I think any copilot MCC MCP will be pushing to do that. Obviously we've functionality in the knowledge hub. So that's all very much a try and have a play rather than a full begin your integration type thing. So it's literally to get them in the door see what we can do and then quickly progress them to a commercial contract and stuff like that and then obviously we build that for now as we look to the future obviously automations we can and the transition of that data from sandbox to production we'll probably look at on boarding them signing up as early as possible and taking that context all the way through.

Michael Moores: So I think where we start for MVP for me it will be very much ease of integration with both of those two things and that should be where the focus should be especially for the knowledge hub and obviously then when we get to the console we expanded to actually doing things and helping them set up. So I think in both aspects it would be how quickly can we live for them. Whether or not the biggest win or the biggest wow to start with and as we get that data in obviously we can build those alerts transactions on top as well but I think yeah for the first one it'll just be ease of getting through that documentation and getting that first API call basically and…

George Westbrook: Yes.

Michael Moores: that's the sort way we structure the documentation already as sort of a logical get your first request done here's everything that's in order and stuff like that so we will have some detailed documentation that can be helpful but then obviously the more we can build off the back of that as well. Obviously, the agent will have the YML as well. So, …

Michael Moores: if it's missing something, it's got the API reference as well to add further context or color to the guys. So, it's not going to be a full copy of the payload…

George Westbrook: It is.

Michael Moores: because we don't want to update it all the time. It might reference a few fields where the context is needed, but it'll be most of the time here's what it does, go and see API reference for more. So I think the agent layer there or the co-pilot layer would be potentially merging those two things back together into one interface where you can ask a simple question. It'll be okay you can see this accounts do this and this is a field you need to do x y and zed. I think that's the benefit there of sort of maybe pulling those two layers which are purposely separate into one sort of context. if someone's asking the question

### 00:25:00

George Westbrook: So in terms of priorities, it' be 100% I think I agree with the MCP first. and then an unauthenticated co-piloter.

Michael Moores: What happened?

George Westbrook: So for that quick question answer and then that it provides a good base to push off of as so obviously pilot for the knowledge hub so that if later down the line like you said want to add some support stuff want to add something for an authenticated user. the only thing with an unauthenticated user is history. there wouldn't really be any history. So, let's say yesterday they asked 20 questions, they come in the next day that chat's not going to be there.

George Westbrook: There might be a way we could do that by dropping a cookie, but I don't know if that would be durable enough.

Michael Moores: Yeah, I think…

Michael Moores: if we can have this I think for me for MVP obviously ideally future state would be full history really push it into production but obviously that requires a lot more in the later phases. So I think if we can if it's a session ID that's cashed or something like that, that'll be ideal. So at least we can…

George Westbrook: It's good. Hey.

Michael Moores: if I come back tomorrow and just want to add on to an additional question I had, that would be beneficial. But I think in a later phase where we string orders together where we've got our automation and maybe our CRM tools and all the data, we'll probably look at that entire flow and then look at how early we can on board. Obviously, the initial MVP was always get let them come in, let them try it, see for themselves. Then the next step is what should we put behind a signup gate if you will. So right now we don't have anything for them really to put behind the signup gate. I know we discussed about AI and costing as well but I think right now as it stands there's nothing we would put behind the gate. So we need some sort of incentive for them to sign up or something to gather information. And then also a lot of them will just use a Gmail account.

George Westbrook: Yeah. This is Yes.

Michael Moores: So how do we transition that from email to a full company? there's a few other things we need to consider to make that end to end journey basically. So that's why for MVP it's sort of fully public for now and then the idea is to capture that history. but if we can have that sort of seemingly capturing that history for them just for their purposes so far and I think the next benefit will be capturing it for our purposes as a individual company organization level so we can build up the idea for me is that as they're looking at us and as they're investigating if they want to be with us we have a lot of context by the time they decide they want to go with us we know what they want to build who they are and we build that very quick and that goes into that sort of program on boarding

Michael Moores: phase that we're doing for the console. So the more information we can pull in to start with will make that program on boarding a lot easier or…

George Westbrook: Yeah. Yes.

Michael Moores: least have a lot more context. And that's the idea sort of similar to how you do as we have these conversations. You sort of know what we want to build by the time we get there. And that's the aim for us that without them realizing it, you've gathered all this information and then you've given them something that might be 95% fit or as close to 100 as you can get it. It just means that they've got the core set up and they might make a few, tweaks or changes and that really cuts down the time. Obviously, we need the full automation, deployment, all that before we can get there, but that's the sort of end goal I think for this and…

Michael Moores: just make sure we don't lose that context as we go through, but obviously build on that as we go through MVP and the later phases of knowledge and stuff like that as well.

Ian Johnson: So I've got a couple of points,…

Ian Johnson: a couple of questions. all of this is ultimately your call. One thing for me with no sign up which I'm agreed that's what we've said how do we cap the amount of stuff that somebody can do not so notwithstanding that we won't have a history but I guess within a session Mike almost what I'm just slightly conscious of is and again it comes down to a costing we've got to basically look at this and say how many people are going to come and try out the knowledge

Michael Moores: Yeah.

Ian Johnson: where we have no revenue line and how much is it is that going to cost us and at the moment that's completely ended because at the moment we're not putting any stops in there to say okay that's gone far off. and really to a certain degree what we're really wanting to do in the knowledge hub with AI is showing people who are looking at stuff what the experience would be like to work with TXN. That's The next stage is okay, I want to basically sign up with these guys so that I can start to build something.

### 00:30:00

Ian Johnson: In reality how that normally works George is people might have made a decision in the background that they're going to go with TXN and the tech team want to get started on building against the APIs. So essentially they want to start building and we had it all the time right where people from their side they've got the code that was already built to the sandbox so they built the stuff whilst the commercial conversation are continuing. I mean, we never minded that because the reality is the more the tech team built to the APIs, the less negotiation power the commercial team had because they built the thing.

Ian Johnson: So to a certain degree we're happy for them to do it, but there has to be something where we've got some way of not allowing people just to keep constantly asking questions and…

Ian Johnson: using the co-pilot, the MCP server without getting to a point where they're actually signed up. And I don't know how you do that or if we can do it.

George Westbrook: What would be…

George Westbrook: what would be like a pound amount per user? a month's time where you'd be like okay I'm worried that they're consuming this amount of resources.

George Westbrook: Would it be a pound a a month? yeah. But yeah.

Ian Johnson: Obviously I'll say a pound a month.

Ian Johnson: 10 10p. No, I don't know what. because I have no real concept of how much this stuff costs. Brett kind of gave us some rough estimates and we had the conversation to say, what you're actually doing is not going to be very costly at all. And I have factored some stuff into the budget to assume a number of people come to the knowledge hub and they spend whatever per month. but I think it goes the other I'm trying to understand the mechanism, Let's say the amount was 100, But there's still a point where you don't want to just carry on spending 100 quid with somebody who's not committed to actually doing anything. Trying to understand the mechanism.

Ian Johnson: I mean, I don't think in reality that anyone would do that,…

George Westbrook: All right.

Ian Johnson: but equally, if I think about the worst case scenario that a competitor comes in, we've got no way of blocking them because we're not asking them for an email address and they can just keep f\*\*\* pardon the French lady but just f\*\*\*\*\*\* with us for as long as they like

Brett StClair: So that can be protected, So you take that scenario if you do want to use Aentic AI, that's the prompt for an email address. And so all these functions should be triggers to gather more information, but at the same time, you're using that information to protect yourself.

Ian Johnson: Okay. Don't say Brett.

Brett StClair: So I would go with that approach. I'd be like, here's a knowledge ub. It's like a website.

Brett StClair: You want to browse and use some really sexy features on here?

George Westbrook: You've got excuse me the boomer.

Brett StClair: Please log in with an email address and your company details. Yeah.

Ian Johnson: Don't say sexy. There's only people of roughly my age that describe everything technology wise as sexy. It's sexy. it never will but I think it's a legitimate option. but we then have to make sure that we've got some kind of video on the website where people can see what that would be like. Otherwise it's saying give us your email address and then we'll open up some tools for you. And it's the same thing. So if we don't let them play with it for a short time and then stop them without an email address, then there's got to be another way of showing them what the experience would be like.

Ian Johnson: Otherwise, people are going to be like, I don't know what I'm going to get if I do give you my email address.

Brett StClair: I want to caveat that quickly. Sorry, you're in this world where code is throw awayable as well,…

George Westbrook: Okay. I'm

Brett StClair: So, very quickly we can change and amend it if it's not working in a direction. So what I'd like you to get in your head is you've got an idea, you want to test it, let's test it. But then if it's not working, we throw it away. We change it immediately. And so those cost elements are small and what it does is it opens you to a world where you can take a different level of risks.

### 00:35:00

Brett StClair: Test something, it doesn't work, fail it, kill it. Whereas in the past, it wasn't really like that. I just want you to factor that It's a different way to think, but it al helps you risk things differently or…

Ian Johnson: Okay. …

Ian Johnson: as long as it's a mechanism,…

Brett StClair: gauge the risk differently.

Ian Johnson: I'm okay with it because I think we can just be of the mindset of let's just wait and see what happens knowing that this thing is not going to break the bank even if loads of people go and start using it. I mean, you'd have to be practically to ask a bunch of questions and to access the MCP server a lot. You're either serious or you're messing with nobody's got enough time or interest to come to a brand new company's knowledge hub and start spending tons of time in there when they don't really mean to do anything. and only route is because of what our likely go to market message is about ease of integration, managing card programs without being card experts, etc.

George Westbrook: Yeah. Easy. Yes.

Ian Johnson: competitors will go and see whether or not what we're actually offering is remotely true because I would do the same thing as well. In fact, I've gone to plenty of them and looked at said that's rubbish. So, people do it, but I can't think of too many scenarios, Mike, where people would do it. The only other one one I can see is, bots that are accessing for nefarious purposes of building stuff that's at the end of the day is going to be fraudulent. I mean, they're never live. There's nothing they can do with it.

Ian Johnson: But I can't see too many way. So maybe as long as we know there's a way that there are mechanisms to cap our exposure, then I'm okay with that. I think.

Michael Moores: Yeah, I think obviously the later phases it's always I think for MVP the knowledge we assume this would be the very first thing no AI obviously we've got to this point here you a lot quicker I think so we've always intended signing would be sort of a later phase for the knowledge hub So obviously we had the discussion in that we had personalization part of the design we taken out as well that there are certain things we wanted to make sure we had that bundle and…

Michael Moores: at what point did we want to capture that email so I think there's always a consideration that we will be gauging something and…

Ian Johnson: I think we've got to put something out there day one that is AI based to help integration.

Michael Moores: I say whether that's the right move now or we just sort of put a sort of a softer limit for early MVP and then look how it goes and go from there.

Michael Moores: Obviously, the benefit of that, will that win sales? I think that's what I'm thinking out doing publicly. Will you win sales with the AI versus how much does it actually cost to run that if people don't sign up with us? I think there's a consideration there, isn't it?

Ian Johnson: I think Mike you raised I think just on the personalization and other pieces I' just become more of the mindset of for example the MCP stuff and what you said earlier about having the full context etc which is useful to us but equally from their perspective if they've got access to MCP server I would expect them to be doing the same thing that you guys are doing of likely building a vault or whatever it might be and then building out their own internal specifications and whatever else it might be. So I think

Ian Johnson: I think the whole thing about the personalization and…

George Westbrook: Thank you.

Ian Johnson: the ideas we've got Mike is they're valid but I think we would need to see some people using the thing in the wild and the two things for me in the wild are the MCP server and a pilot because if we don't provide those two things then what are we're only competing on we've got cleaner API documentation and it's just not enough because that is mistakes. So I think that's the one thing I would say about the knowledge of the other part to it was I'm just thinking about anomalies right where let's say something in the guides and I know that I'm assuming this won't happen Mike right but I'm just thinking about the worst case scenario where the guide don't match the API reference I know you're doing a bunch of stuff to make sure that's not the

Ian Johnson: But more generally speaking, there were anomalies. There were things that PE at Marqueta that people found, that's not right. It says this and it's actually this.

### 00:40:00

Ian Johnson: And I can imagine those being exposed in a co-pilot because the AI wouldn't know what else to say. It would basically call them out, right? I'm imagining

Michael Moores: Yeah, I think especially at MVP that the main knowledge of it is going to be the YAML and…

Michael Moores: the knowledge So obviously if the guys are wrong, the AI may be wrong. Obviously as we build it up, we'll have some of the later ideas of self-healing documentation and all that. you pile on the tickets from Fresh Desk, you start getting a sort of comparison there. what is correct? What am I saying versus…

Michael Moores: what the documentation saying? I think when we get that level, you get that sort of comparative and analysis to say, you're saying this thing to customers, but your guys say something else obviously. So, I think adding those three layers sort of bring it in later on as well. But yeah, ultimately you're correct.

Ian Johnson: This is…

Ian Johnson: this is where I'm going to. I'm not sure that is a later stage and I don't think it's a big thing. My question, George, is if I'm the user and the AI comes back and basically correctly identifies there's an anomaly, which I'm assuming that it would and…

Michael Moores: That's Yeah.

George Westbrook: Last question.

Ian Johnson: we don't want it want to because if something's wrong, it's wrong. I think we've got to think about what that interaction is then because we need to know that. And the only way we're going to know it is if somebody something tells us. There's self documentation. Mike, you're absolutely right. But for me, that's not really That's more a function of getting that information into I guess your own automated agentic flow. I

Ian Johnson: to then go and correct the documentation so that it can be published. So the anomaly is gone. but if we don't know about it, the only other person that can tell us is the user. So to me in thinking about it, it's like if I'm the user, okay, there's an anomaly. What is the AI going to tell me about…

George Westbrook: Awesome. what we…

Ian Johnson: what action is being taken about that anomaly? And it should be as simple as we've advised the platform team or wherever else it is. this will be fixed shortly and we get it fixed very quickly. And I don't know how that would work, in terms of us getting that notification that this anomaly has been identified.

George Westbrook: what we could do and this would work quite nicely with a support is let's say there's a conversation back and forth there is an anomaly Mr. user would or Mr. or Mrs.

George Westbrook: user would we're going to report an anomaly. Is there anything else you'd like to say on this? It's obviously going to have the full context of the conversation. and then what it could do is send you an email. or there could be a platform or something which is going to add that support ticket. because I suppose a lot of the say how some of the stuff we do internally is it's always first maybe an ap will analyze and then give us a ticket. then given that we'll go in and do the fix. but over time it progresses to the point where agent creates a sport ticket, agent updates and then that loop starts. But the first step is always just finding an easy way to get it down. And I think the co-pilot would be one of the perfect surfaces to do that.

George Westbrook: Because I suppose you're getting the agents context of the documentation on top of real-time user feedback I tried this this didn't work this is what happened with a logged in user as well one of the things we could potentially do which I don't know if this be possible Mike is if they're logged in and they're currently making real API requests be it in the sandbox or something else we could have the logs of the API. let's say they're pinging one endpoint and they keep on getting a 422 error. The documentation says it is issuer ID with a capital I. but they're putting in basically when it can look at the logs, it's a lot better than say maybe a user looking at their request, looking at the response.

George Westbrook: And then that way we can work out is it a them issue and if it's them issue we can say right you keep on putting in the wrong field name but if it's an us issue ping Mike can speak to a relevant person and fix it and in time it goes in and automatically updates it. because we'd obviously be pulling in the stuff for the knowledge. not obviously, but what we'd aim to do is pull in the documentation from Umbraco to make sure that it's constantly being updated so that there's not a point where the MCP server or…

### 00:45:00

George Westbrook: the co-pilot is pulling in documentation that's a month old and there's been loads and loads of changes. So

Ian Johnson: Yeah, agreed.

Ian Johnson: So just I understand the piece about identifying why something is failing within the sandbox. That to me, Mike, must have. it's a priority because otherwise I don't really see that we're making that much of a dramatic effort to streamline integration

Michael Moores: Yeah. Yeah.

George Westbrook: and…

George Westbrook: I suppose that could be the first point in which you get that user information. so I know for me if I'm trying something and I'm pinging a real sandbox, if I want to be able to either see logs or have something be able to see my logs, I'd expect that there'd be some sort of authentication.

George Westbrook: And then I suppose once you've got that authenticated user, they're also a lead which could mean you can start doing outreach to them as well.

George Westbrook: and then potentially going down a bit of a rabbit hole, but you can see the end points that they're hitting. You can see all of the queries that they're telling you about which could be included in the outreach message that you both that you send for them.

Ian Johnson: Okay.

Ian Johnson: But when you say getting to see their logs, to

George Westbrook: If they're logged in and they're hitting the sandbox. I don't know if there's any authentication in the sandbox already, but if they were authenticated users and we're tracking the requests that are hitting the sandbox, they well could or should be associated with a user ID.

George Westbrook: And then given that logged in the agent will know the user's ID and then can then write queries in order to get those logs back. So it'll be select requests where there was an error. then it's going to pull that into its context when it answered any questions and then could lead into the support tickets as well where it's like this user keeps on getting this error on this thing. is it a go to mic for documentation support or…

George Westbrook: is it something that gets put to a documentation agent that selfs? Yes, call

Ian Johnson: So yeah, I think that's super interesting. And I think if the only gate to being able to do that is making people lot give an email address.

Ian Johnson: 

George Westbrook: There you go.

Ian Johnson: Mike, I think to Brett's point, that's the point. if you want to use these features, then we need your email address. I think something about people will just use a Gmail address but again not interested in that in the sense that if you're not a business and the argument of Marqueta was they had this viewpoint George of they honestly because Mike you will undoubtly have seen it but you see the people that are accessing it with email addresses and there's a bunch of them were at Barclay University and whatever else it's just a bunch

George Westbrook: Thanks.

Ian Johnson: whacking away and that's, fine, whatever. But ultimately, we're interested in businesses and we don't want to expose a bunch of capability to people that aren't a business. And the only argument ever came back is, if they're really a true startup, they probably don't even have a corporate email address at the moment. It's like, okay, I'll get that. So we might have a situation but in that case they can contact there should be a way of them being able to contact us and then we can have a conversation to understand where they are with it otherwise we're just because then if we did have that and depending on what the cost of it is I do think that log checking and error arbitrage is a super interesting

Ian Johnson: in the important parts. The only other way I can see of doing it, George, is they could just paste what they're putting in, copy what they're putting in, put it into the co-pilot, say this is what I'm getting, and we can then tell them where the error is, which ultimately does the same thing. And maybe that's the first phase, Mike. But I do think that that's an important part of So if I think about your role when you were helping on those project calls at Mark and stuff from memory, a lot of it was that people don't know why they've got an error or whether they're emailing you or whatever else it might be and they haven't figured it out and you're able to say, this should be this and you set it to the wrong you've set the parameter incorrectly.

### 00:50:00

Ian Johnson: That to me is something that shouldn't be done by a human anymore. So I think we need to think about that being there from day one.

Michael Moores: Yeah, obviously there's loads of different places you sort of improved obviously guides the login the errors that come back from the API already huge amount we've done towards that.

Michael Moores: So I think where the AI just pulls that all together. Obviously there's quite a lot of moving pieces with fully getting it logged in. So this is where we're still looking at DT and public sandbox. So ideally we would have public sandbox where each user would have their own sort of private section logged in and stuff like that. Obviously we don't have that today. It's just a authentication from the knowledge hub to the sandbox basically. So the knowledge hub will be that authenticated entity basically.

Michael Moores: So I think end to end would be ideal all the way to DT but I think where we are with DT you're probably looking at potentially login in the knowledge hub capture it there and then we won't have that full history but obviously if we do have that enter end enter to end history you can then start pulling stuff in a public sandbox the sandbox in production if you start pulling all this information into an entering an organization then the AI obviously gets more powerful across the board so I think firstly We need to decide do we let them So logging in we can then gate the AI and those behaviors as well. Obviously the try it now functionality will be browser only for now. So you will get that response back. You will get all the errors shown on the screen. So the AI could ultimately do what it does in console and read the context on that specific screen if you will. So it can do the similar thing. It can see what's happening and try and help.

Michael Moores: I think to your point George later on if we can actually get a full end to end solution where DT's got a specific user logged in we can have access to the logs it can do sort of user queries as well that will get much more tighter across the board so if they use the API or any other avenue we can see that across the board it ultimately doesn't matter which service you use we know you're having an error this is how we can help so I think for initial phase it would be how can we help you in browser testing I think that's achievable without touching sort of DT's world. And then when we get to this end to end thing that we always planned, they'll be having the fully public sandbox where you have that private sort of section for them on there individual personalized, sandboxes. That's what Marqueta started offering. So you sign up, you get your own little mini sandbox where it's just your data.

Michael Moores: That's where you can get that quite deep, integration that people are getting at Marquetta where I've already built half of it. You could do that in a public sandbox, but obviously you're always cautious because data is shared with everybody. So, Marqueta took that up the next level and started off those personal sandboxes, which is something they did about a year before I left. So, offering that little and then you have your own sort of demo console and stuff like that. I think that's always the plan obviously where we are that sort of a large build for the MVP considering we haven't even built recovery sandbox.

Michael Moores: So that's why we've not done that with DT but there's so much we can do beforehand. and I think that will just nice and bring it all together. when we get back

Ian Johnson: …

Ian Johnson: it sounds like on the knowledge that we've got some good ideas. I think remember the philosophy is people don't need to be experts. and to speed of integration and when they do hit speed bumps that we're able to give them quick guidance on how to rectify where they've gone wrong and then if the issues on our end that we have a mechanism of of getting that fed back so that it can be corrected in the first place.

Ian Johnson: I think I don't like that seems to be the kind of embodiment following Brett's comment as well.

George Westbrook: Oops. But at least you're using your email that you made when you're about 5 years old still.

Ian Johnson: If you want to use AI features, there's an expectation that you give us an email. For me, that needs to be a corporate email. I accept the fact that some people might be wary of doing that. but there's got to be some way of Yeah.

Brett StClair: I think it's also becoming a norm, Please submit your work email, and all we do is we blocking Gmail, Yahoo, and in Max's case, AOL. And that's a real story.

### 00:55:00

Max Kingaby: There's a time and a place where I sorry I'm not showing my face guys.

Ian Johnson: It was 19 Okay.

Max Kingaby: The bad end I think of the barley that I'm not tired.

George Westbrook: I can see him sat down. he looks rougher than usual.

Max Kingaby: I just feel a bit rough right now. I

George Westbrook: Yeah, I think that's an important caveat…

Ian Johnson: What? we don't need any of that information's face.

George Westbrook: because I think everyone thought Max is currently on the toilet. Heat.

Ian Johnson: So, conscious of the fact we're nearly at time. I guess did so couple of things just quickly on there because I saw that Tyler had joined. So on the content workforce what I saw on the flight plan was content plan and trial content. So, I think what it says in the text is that we're at a point now where you guys can start to build some content and…

Ian Johnson: we can have a look at it, review it, and approve it. Is that right?

Brett StClair: Yeah. …

Brett StClair: we're at that phase where Tyler's actually started generating and got some ideas that he's coming up with. But I think it's important for you guys to just start sharing some ideas of what you want to talk about and let Tyler start putting together the content so you can have a read, see if it feels right, and then let's start putting it out there. And we can always edit once it's out there as well. So, want you to bear in mind it's not like when on the internet it's on the internet forever. It's not. you can then go tweak and change it. Tyler, do you want to have a quick jump in and…

Brett StClair: discuss what you've been working on?

Tyler Thompson: Yeah. …

Tyler Thompson: I've just worked on a couple of ideas that I've set up in a document I'll attach for Ian, Dota, and I did an article for each of you guys and then a corresponding TXN article for each. Obviously, I just want you guys to go through it, give me approval on any feedback so that I can then refine the model so that it just works in your favor. another big thing is access or LinkedIn credentials. Has anybody started a TXN LinkedIn account that I can get access to it?

Dorte Dye: So we discussed that you said that we set up on the platform that everything is done by the platform then rather me giving you personally access right?

Tyler Thompson: Yeah but you'll have to give my personal profile access to the company through there.

Dorte Dye: So you need to follow the page and only then I can give you access to it.

Tyler Thompson: Is it not TXM global?

Dorte Dye: I can send you the details.

Tyler Thompson: Perfect. Thank you.

Ian Johnson: Okay, I just want to bring you guys up to speed on a few things that are happening.

Dorte Dye: We just need to be ego.

Ian Johnson: So the first thing is we need to get the output of the various interviews that we've had and where you've arrived at for the positioning and messaging of the company. That's the number one thing because that everything essentially needs to flow from there when it comes from company content and we need to make sure that that is the basis of what we want to go forward with. And with that in mind obviously Bronwin has a role in that. we are talking to an independent consultant to help around PR and all those different things. but we need to make sure that everybody's aligned.

Ian Johnson: So before we start producing and exposing content, we need to make sure that this kind of the manifesto and whatever it was they referred to in here as the core messaging, positioning and brand and tone voice document is there and that's the basis of everything that gets used. I don't think we're a million miles off because I haven't said anything any different since I joined the company. The tone of voice and the brand document was actually fed in directly from work we did last year with Bronwin. and yet another agency because as marketing people don't do any work themselves. They get agencies to do it all.

### 01:00:00

Ian Johnson: So I'm convinced we won't be a million miles away, but we need to get some the output in a suitable format that it can be shared with other people to say this is where we've arrived at get comments and feedback and then be able to feed it back into you Tyler and say okay this is what we've landed on. so that's the first thing just to mention with respect to that. the LinkedIn profile piece no major issue but at the moment it's not branded or anything. So Bronwin has taken an action to go and actually get things set up. So it's got some imagery etc. I just need to know when that's going to be completed. No issue with giving you guys access to it.

Ian Johnson: And then I think just an understanding of what the strategy is to try to maximize the kind of the readership of some of these documents. how do we make sure that we're getting seen as much as you can be expected for a new company?

Ian Johnson: So I think we probably need a separate session on the content workforce about making sure we're aligned first and then understanding okay are we what happens moving forward because I think the proposal is pretty high level Brett it's not a criticism but it's pretty high level about a number of pieces of content that get produced so we just need a bit more detail around Yeah. Yeah.

Max Kingaby: So if I may, Tyler and I have spent some time talking about exactly that yesterday. We've got a list of things we'd like to discuss with you, and when you are ready, we would love to organize that call. However, daughter said you guys want to catch up with Brett beforehand and then move on to start doing the content stuff. So, if you want to do the content stuff tomorrow, boom, we're ready to go. If you guys want to wait and speak to Brett first then likewise do that.

Dorte Dye: Is that all this call I'm…

Dorte Dye: and Tyler Max. We're ready to book session in.

Max Kingaby: Great. we'll get it in tomorrow then.

Dorte Dye: Yeah. Heat.

Ian Johnson: But…

Ian Johnson: what I need from you guys is and I know you're working in an AI world, but I need this in a human world that can be shared with essentially for the company? That's the priority. The core messaging, the tone of voice, etc. you've got to make sure that that's the starting point and it gets reviewed and then before we get started it's all aligned. I mean I think PDF might be better.

Brett StClair: That'll come to you in an HTML format with your branding. Would that suit or would you like it in a PDF? As I said, I was like, " that's silly, Brett. Still too AI." Yeah.

Ian Johnson: it's just easier for sharing people reading on various devices etc. If you could send that across as the first step, it doesn't stop us from having that conversation, Max, in terms of the mechanics and ideas and things you've got or reviewing what you've drafted already, Tyler. Happy to do that.

Tyler Thompson: Thank

Ian Johnson: But I do want to make sure that we're all aligned. so that's the step we need to take there on the outbound workforce. Brett, I guess my question is…

George Westbrook: All right.

Ian Johnson: how far are we from being able to start that process? Because I see the content workforce and the outbound workforce being very very similar.

Dorte Dye: You're on mute.

Ian Johnson: it's not just a delivery method. I understand it's more than that. You're on mute.

George Westbrook: Did you see your wonderful hand gestures?

Brett StClair: One's pull,…

Brett StClair: one's push. No.

Ian Johnson: Yeah, indeed. So, the number one thing before we do anything is who are we doing it to? So, how are we building this target list of accounts? So, I've obviously submitted something to you guys. My initial assertion is it doesn't seem to be big enough. But that's the first starting point is who are the companies that we're going to go and target. And if you remember when we talked, I think it was in the outbound workforce, we bucketed them into I think it was five categories. The car product is core and…

### 01:05:00

Brett StClair: 

Ian Johnson: they have no vendor etc. those different categories. So that's the first thing for me. Do we know who it is we're going to go out and target? And that's just company names because my understanding is part of the outbound workforce is that you guys will go and find the relevant target contact information.

Dorte Dye: Was that nice? Mhm.

Ian Johnson: That right.

George Westbrook: Yeah. Yeah. So in terms of the outbound workforce, I think me and daughter had a call with what's his name? Alex this morning So it's basically we need to buy the domain to get the email set up. good thing is I think in terms of access with emails. he didn't seem too concerned. which is good. I think the only issue with domains and I think obviously you mentioned daughter might need to be a bit more alignment on the names of the domains we're going to use. and then once we've got that it's a process of getting…

Dorte Dye: sleep.

George Westbrook: because we started yesterday and the day before but thought put it on hold till we spoken to Alex and got everything approved.

George Westbrook: what now we've got the approval. It's just getting the names of the domains getting the emails warmed up and then once that's all done it's getting the messages fired out. Obviously in parallel to doing that is let's get some list of leads. let's look through some samples to make sure that it's in the right direction. which is good because we've got a bit of time before the emails are going to be warmed anyway.

George Westbrook: So, it's not as if by tomorrow we need to make sure that we've got the lists, they're all approved, and everybody's running around rushing to try and get them sorted.

Dorte Dye: Maybe just a step back.

Dorte Dye: There wasn't an approval. We just discussed the approach how we split it. Alex is going back to run it via Gavin to get Kevin sign off and then I wanted to bring it back to you Ian to present what we agreed. but the URLs it's another one. What George and the team has already purchased might not fit in what your thinking is.

Dorte Dye: So I made sure that you are in the loop of which ones we actually want to purchase. So you will get everything as soon as I hear back from Kevin.

Ian Johnson: I'm totally comfortable with that and…

Ian Johnson: It's not like we want to start the outbound stuff tomorrow. The most important thing is what are the lead list that we're targeting. B what is the process for ensuring that that list is kept up to date. So what I mean by that is how are we sourcing target companies they might be in incubators they might be very early stage startup companies.

Ian Johnson: So, it's understanding how do we get that data to make sure that we're not missing out on companies to a certain degree might be in stealth or they might not be in market yet to make sure that we're there from the outset. So, I'm not overly concerned about the timing because again, number one, got to get this content ign. We got to get this messaging alignment because everything's going to flow from that. Obviously, there's the email domain stuff you've talked about, but then aside from the content piece actually can go earlier because we're just saying that to everybody to a certain degree when it goes onto our link.

Ian Johnson: LinkedIn page then,…

Ian Johnson: it's not being sent specifically to somebody. but we just need to get it right rather than move super fast is my …

Brett StClair: Just on timings,…

Brett StClair: I wanted to check with the developer portal and getting that work done. What are your guys timings around there?

Ian Johnson: I've been told it done. And the sandbox is there, Mike, but they think they said in the project meeting yesterday. I couldn't really guess. I didn't fully understand what their answer was.

Ian Johnson: They said it was in staging, but it's not in production. It's certainly not available to anybody because the website's not up yet, and that's how you'll access it. But I think we've got to test it end to end, Mike, once it's in the European in your instance.

Michael Moores: Yep. No,…

Ian Johnson: So it's pretty close. I don't think there's much more left to do on it, Mike. Right.

### 01:10:00

Michael Moores: just test it end to end with obviously there shouldn't be any functional changes. It's just moving to a DTowned environment versus stat works and then obviously just sort of testing that writing the documentation is on my list. and obviously sort of making sure it looks okay before we publish that as a whole basically. But yeah, we've got the Umbrau set up.

Michael Moores: we have the fresh test set up integrating with that as well now. So both those entities are set up ready. It's just the end to end testing with the public sandbox YAML sources all again all functionally the same just making sure all the infrastructure works together and everything looks okay. I think the biggest one really before we go live will be the guides and the consistency and…

Michael Moores: the accuracy of the YAML. I think that's the last sort of lever that's on sort of DT to make sure it looks good that we can publish it. obviously there's been quite a lot of errors there. So, that's what we're sort of waiting for. Yeah.

Brett StClair: If we need to get some of those AI features in,…

Brett StClair: we're going to need to figure out where and how we going to fit into that architecture.

Michael Moores: Yeah, we can set that up and…

Michael Moores: speak with DT and see how we want to work with them. and go from there.

Ian Johnson: I think let's be clear on…

Ian Johnson: what it is that we're going to deliver before that conversation takes place so that we're concrete in what we're actually asking.

Brett StClair: Should we get cracking on a demo pilot version that's similar to what we did with the agent stack just so you can get a feel look and…

Brett StClair: feel and it kind of gives you an idea on that requirement. cuz that's something we can move fairly quickly with

George Westbrook: Okay. We…

George Westbrook: because it might be an older version of the knowledge hub. but we've got access to all the UI stuff for that and it with the console look acts like the real thing.

Ian Johnson: Mike, I'm happy that we go with that as the next priority.

George Westbrook: The only thing might be is certain changes to the YAML and some of the actual content. which is for us just updating a few things and it would be all fine.

Michael Moores: Yeah, obviously we've got the actual stat works dev as well for you to look at the actual Very similar to the console that I gave You got the prototype which is the latest one. Obviously at some point we stop that and go to the UI wireframes.

Michael Moores: Same process and we've also got that live the UAT URL that we can give you as well. Then you just see how it looks.

Michael Moores: And that's because that's the one we're testing against as well. So that's all that ready.

George Westbrook: Okay, perfect. Lovely.

Brett StClair: Happy days.

Ian Johnson: Okay, sounds good. We got a plan moving forward.

Dorte Dye: Yep.

Ian Johnson: Somebody can get me the kind of messaging positioning in a kind of PDF.

George Westbrook: Oops.

Ian Johnson: Brett, then I can get that alignment exercise kicked off. and then obviously Tyler, I see that you sent some stuff across, so I'll take a look at that as well.

Michael Moores: Perfect. Okay,…

Brett StClair: Perfect. We're on it.

Max Kingaby: What time works for you guys tomorrow for that content call?

Ian Johnson: Anytime from 10 through…

Ian Johnson: till 1 and any time from 3 to 4 Okay,…

Max Kingaby: Too close. Yep.

Dorte Dye: I have 11 there.

Dorte Dye: We've all free 11 to 12\. Awesome. Thanks, Max.

Ian Johnson: folks. Thanks. Bye.

Brett StClair: Well done.

George Westbrook: Perfect. Thanks very much.

Brett StClair: Thank you everybody.

Michael Moores: thank you.

George Westbrook: Have a good rest of your day.

Michael Moores: Cheers to Kevin.

Brett StClair: Enjoy. cha.

George Westbrook: Cheers. Tonight I

### Meeting ended after 01:14:43 👋

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*

