---
date: 2026-10-06
type: standup
description: "No signed data agreement and an MSA still not in play, rate limiting resolved, hosting settled in DT's Azure stack, and Marqeta now leads with a co-pilot"
scope:
  - "[[commercial]]"
  - "[[architecture]]"
  - "[[developer-support]]"
  - "[[full-agentic-experience]]"
status: extracted
extracted-to:
  - "[[commercial]]"
  - "[[architecture]]"
  - "[[docs-mcp-server]]"
  - "[[portal-co-pilot]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-06)

> **Source:** Gemini transcript, 6 October 2026, 15:30 BST, 38m. **George Westbrook**, **Brett StClair**, **Max Kingaby** and **Vineth Siriwardana**, now back in the UK, with **Michael Moores** and **Dorte Dye**. **Ian absent**, travelling.
>
> **The call ran as a working session**, mostly George and Michael, and closed with the most commercially significant exchange on this engagement in weeks: Dorte asking whether a data processing agreement had ever been signed.

## The paperwork gap, and what already exists

Dorte, near the end, with the launch in view: **"Did we sign a data processing agreement with you guys?"**

Brett: **"No."**

Then the fuller position, in his words:

> *"On the agreement side we put an agreement together. We then did an appendix to the agreement for the first two bits of work, and then the second work we've just got a proposal but **no appendix to that agreement, and the agreement still needs to be in play**. In that agreement I put a very lightweight data components, because I know you were working a whole lot of data compliance components that need to be added."*

### Where that leaves things

| Item | State |
|---|---|
| **MSA** | Drafted, **not in play** |
| **First two pieces of work** | Covered by an appendix |
| **The current phase** | **Proposal only, no appendix** |
| **Data processing agreement** | **Not signed** |

**Dorte's position is the one to act on.** She has no in-house specialist, has to assemble the facts herself before going to external counsel, and wants to go once:

> *"I need to gather all of the facts and then we go to external counsel. But for that I really need to have everything watertight that I can explain everything."*

And on the privacy policies, said earlier in the call:

> *"While I might have a slim down version for launch, I want to just go once to that. So we both might need to just work out a timeline."*

Her reaction to the gap was plain: *"This is the shit that really ruins my life."*

### The good news Brett undersold

**Brett described the data framework in the MSA as *"very lightweight."* The vault says otherwise.**

[[txn-agentic-ai-layer-support-sla-reviewer-brief]] records, on **6 July**, that **Schedule 4 was substantially completed**, mirroring MSA Schedule 3: data types, the regime (EU GDPR for TXN as a Cyprus-established controller, UK GDPR for Novosapien's UK processing), EEA-to-UK transfers on the UK adequacy decision, and deletion or return on termination.

And on **7 July**, after TXN's own red-team review, **Schedule 4 was rebuilt as a real DPA**: Part A carries the eight Article 28(3) processor obligations, wired to the breach-notice and return-or-deletion clauses, with the particulars table moved to Part B.

**So the facts Dorte needs for counsel largely exist, and have since July.** What is missing is signature and an appendix for the current phase, not the drafting. Brett undertook to send her what he has; the vault is the better starting point.

### Her actual worry is already a known open item

> *"While you're building this stuff you still would be running it, right? Because **all of the LLMs are via your contracts**. And for as, so it's like, I think that's where the joy always goes when **the LLM sends something to the US**."*

Brett: *"Correct. At the moment I'll build. So this is going to be the slight complication. So got two components."* Then he took it offline.

**That exact risk was identified in July.** The reviewer brief names the AI model sub-processors as **Anthropic (Claude) and Google (Gemini)**, hosting in **European regions**, and carries an explicit note: *"see the MSA brief on **pinning EU model endpoints so the Europe commitment holds in practice**."*

So the drafted answer is: European hosting, named sub-processors, and the open engineering task is making sure the endpoints are actually pinned to EU regions. That is a verifiable thing rather than a legal unknown.

### And one gap the July draft does not cover

**The sub-processor list names Anthropic and Google. The architecture now includes OpenAI.**

On 29 September George described the fallback chain as *"if Google's LLMs are down, then we switch to Anthropic. If Anthropic's down, we'd switch to OpenAI"* ([[2026-09-29-agentic-standup]]). On 1 October he confirmed the current model as **Gemini 3.8 Flash through GCP**.

**OpenAI is not in the DPA's sub-processor list**, and a sub-processor that appears only during a failover is still a sub-processor. If the chain stands, Schedule 4 needs a third name and an EU-endpoint commitment for it **before** the pack goes to external counsel, because Dorte intends to go once.

Raised at [[open-questions]] #103.

## Rate limiting is resolved

[[open-questions]] #97, opened a week ago, is answered. Michael had been back to DT:

> *"I also caught up with them on the rate limiting. **So very much external. We can do what we need. We can limit you higher. We can take it off. Whatever we need to do, it's by IP and endpoint. So we can control that fully.** They're quite comfortable with that."*

George confirmed the condition: *"that would require a static IP in order for them to be able to whitelist it."* Michael: *"Yeah. Yeah."*

**So the 15-per-second ceiling is not a constraint on the agent**, provided the agent gets a static IP. That removes the threat to the parallelism that delivered the speed gain, and it leaves one piece of work on Novosapien's side rather than a negotiation with DT.

## Hosting is settled

The question [[open-questions]] #69 and #70 have carried since 25 August now has an answer, and it is a good one.

**Where everything sits today**, per Michael: the Console and the APIs live **inside DT's PCI environment**, *"so it is covered to hold that sort of data. Not PCI in plain text, but personal data and stuff like that."*

**Where the AI layer goes:**

> *"In the initial designs there is console, knowledge hub, website. **All we would do is just spin up another node for any central AI layer**, and that's where it would basically live alongside the API in that same sort of **European Azure stack** that we've got going."*

> *"I think that's pretty much finalised now. Still waiting for sort of documentation, but it's built, it's all there, looking at pushing that towards production. So just be with the small tweaks that you may need for us to stand up to deploy that into that environment."*

**So: a dedicated node for the AI layer, in DT's European Azure stack, inside the PCI-covered environment, already built.** That answers the storage question for the agent's own data, and it is the environment Dorte's privacy policies have to describe.

**One thing it does not settle.** George raised the checkpointing store: a package writes conversation history and traces to a database for the agents, and *"where is that data going to be stored? Is it going to be in the current infrastructure you've got? Is there anything else we might need to use? And obviously, if there's anything else we might need to use, then we're going to need to make sure that we strip out anything that could be sensitive data."* Michael is happy to discuss storing it in the same environment. That is the remaining half of #69.

## The dependency list, delivered

George compiled it immediately before the call and will send it on.

**His own review:** *"there's nothing really I can see there that's going to be problematic, but obviously we don't know what criteria DT are going to use specifically."* His test, put memorably: *"nothing from our side which looks like it's some random package that some guy in Russia has made and there's three people using it."*

| Item | Note |
|---|---|
| **One MCP package** | Has a dependency pinned **below** the current version. *"That might potentially be an issue. I'll do some research to see if there's any way we can get around that"* |
| **Supabase authentication** | **Pilot only.** Used for a quick authentication route on the Console replica. Flagged explicitly so DT does not read it as production intent |
| **Checkpointing package** | Writes conversation history and traces to a database. Raises the storage question above |
| **Console replica packages** | **Removed from the list**, since Novosapien is not building the production Console. Only what the agent, inbox and co-pilot need |

**The review order:** George's list goes to Michael and **Stackworkz first**, *"to make sure it all works and doesn't clash with them"*, then to **DT as the host**.

**Michael's warning, and his optimism:** *"there were quite a few in the knowledge hub that they weren't happy with. But **if they've not done AI before on their side, I don't think they're going to have much to say.**"*

## The agent moves from scripted to malleable

George's summary of where it stands:

> *"Current workflows, our opinion, [are] working pretty well. They'll go through step by step. **Failure rate is minimal.** Speed is improved, can still be improved."*

**What changes next**, and it is the real agentic step:

> *"Making it a bit more malleable... you can go in, ask anything. It might construct one or two workflows together. It might find the correct tools at the right time, which is not something we've been focusing on too much, but it's something we're going to be focusing on now. So you get that kind of **full agentic experience where it's able to do anything and everything within the bounds of the access that you have**."*

Alongside it, **permission-based tool calling** in the agent's MCP server, tested against real roles: *"somebody's a program manager, they're going to get this level of access, somebody else is going to be a lower or a higher level. How does that work? How does the agent deal with it?"*

That is [[open-questions]] #73 moving from design into implementation, against the permission documents Michael sent.

### A gap George raised and nobody has designed

> *"One thing I forgot to mention, we'll need to think about **how we're going to summon somebody for an approval**. What does that look like? How are they notified? Is it just in the console?"*

**The approval model is settled, the human summons is not.** [[approval-queue-integration]] records the mechanism agreed on 15 September, each permission carrying an approval flag, requests going to a queue approvable in the Console or on mobile. What nobody has specified is **how the approver learns there is something waiting**, which is the difference between a queue that works and one that fills up. Raised at [[open-questions]] #104.

## Three MCP servers, and why they stay separate

George set out the shape clearly for the first time:

| Server | Purpose |
|---|---|
| **Agent MCP** | For the full agentic experience. **Reused by the Console co-pilot** at the same access level when that gets built |
| **Docs MCP** | For the knowledge hub co-pilot. Mostly the local file representation of the Umbraco content, refreshed on publish webhooks, **plus tools for simulating API requests** |
| *(Third implied)* | George refers to three; only two were described |

**His reasoning for keeping them apart is operational rather than architectural:**

> *"MCP servers are really, really cheap to run. And obviously **we wouldn't want traffic from the docs MCP server causing issues on the agent one.**"*

Plus isolation on access: separating them means *"we're not having to play around too much with extra levels of access."*

## Co-pilot progress, with updates due Thursday

| Feature | State |
|---|---|
| **Page navigation** | Ask about an endpoint or page and the co-pilot takes you there |
| **Chat export** | Markdown, or straight into Claude, ChatGPT or Perplexity. The Marqeta pattern Michael raised on 29 September |
| **Sandbox calls on the user's behalf** | **Next on the list.** The agent runs the test, shows the payload and the request |
| **Copy for Postman** | A quick copy button so a developer can take the payload out and run it themselves |

Michael's response: *"you've covered a lot of that... being able to run stuff and navigate around the pages is great additions as well. That's pretty much covered off what we expected to do."*

**And he set the retention position for the public sandbox:** *"we're looking at keeping the public sandbox for a very short window of time, obviously public data. **So the next level would be having a separate environment, a personal sandbox**, so you can sign up, log in."* That is the per-user sandbox [[open-questions]] #91 identified as the dependency for log-based support, confirmed as a later phase rather than MVP.

## DT built the internal API wrong, and everything downstream is waiting

The most consequential delivery fact on the call.

> Michael: *"The internal API was built quite wrong. **Where storing the data was very wrong.** So they're currently **rebuilding that entirely**. So DT's build, obviously we can't build any further until they've done that."*

**The silver lining:** *"it does mean that hitting the internal API is a little bit easier than it was before. Sort of a generic JWT access rather than scoping per program manager. **So it's really split them properly now.**"*

**The cost:** *"[Stackworkz] are getting a bit stuck now with some of the endpoints... they're really stuck basically for signed-off endpoints."*

### Michael's UAT, at scale

| | |
|---|---|
| **Test cases run** | **About 6,000** so far |
| **Defects** | *"Quite a lot coming out, ranging from little to critical"* |
| **Sign-off** | *"A while before we can get it signed off"* |
| **Method** | Prioritised by launch need rather than by endpoint order |
| **Timeline** | *"Probably looking at a couple of weeks at least for the rest of the testing"* |

He is running it with AI assistance and credits it: *"I blew 33% of my usage yesterday... it's been running for two days basically consistently"*, and *"I wouldn't have found some of the defects I found with it. It's just been really trying to break it."*

**Dorte's observation on the asymmetry is worth keeping:** *"the only challenge Mike has now, he's so productive, the other side can't keep up with it, because he's just putting them in a big black hole."* DT are not using the same tooling, *"they use some things but we don't really can work out what it is and they're not really openly sharing with us."*

### What gates the launch

Explicit, and useful:

> *"We're very much focused now on what can we do to get the website and the knowledge hub live. And for that, obviously we need some endpoints that are at least signed off and documented properly. So we're aiming for the **cardholders, cards, accounts**, those ones to be done, then we can look at launching the website and the marketing exercise, and then very much focusing on the MVP."*

> **"The core five we're not going to launch without them."**

So launch is gated on a named set of endpoints passing Michael's UAT, and that is roughly a fortnight of testing away before sign-off even begins.

## Marqeta now leads with a co-pilot, and Dorte wants ours prioritised

George offered a choice: keep both tracks moving in parallel, or *"ultra prioritise"* the knowledge hub co-pilot so it is ready for launch.

**Dorte's answer is a clear strategic statement:**

> *"When we go to market we need to have **a differentiator to keep the interest**, because the moment you launch something that doesn't look fairly interesting testing, people don't go any further. **So it's the one time we launch, we need to get it right.**"*

**Michael supplied the competitive reason:**

> *"Especially now **Marqeta has redesigned their website to be very much co-pilot up front**. So that's quite a shift from them from how it was before. So I think **at least matching that would be ideal**, either at launch or very close afterwards."*

**And he noted the timing has moved in everyone's favour:** the AI was always expected post-launch, *"it just happens that the timelines have matched up a little bit better than initially planned"*, because DT's delays have pushed launch out while the co-pilot has come forward.

**Dorte deferred the decision to Ian** but her preference is on record. Michael asked for an estimate of when a first deploy or integration could happen so he can fit it into the DT timeline. Note that deployment to production runs through DT, *"so there's a few hoops we need to jump through."*

Raised at [[open-questions]] #105.

## Direct access to Stackworkz, and the DT question

**Michael opened the door:**

> *"The next step is obviously getting you talking to Stackworkz, and then we can have that initial meeting, and then if there is anything you want to discuss between the two of you, I'm happy for you to do [that]. If there [are] any code or integration questions, we can hook you up together and **you can start talking directly as well.** The only thing we ask is where it's feature changes or anything, you come back to us."*

**DT stays out until the API integration stage.** Michael: *"I don't think they'll need to be involved until you get to the API side... DT just need to be involved in terms of 'you will be hosting this, are you happy' type conversations."*

**Two cautions came with it.**

**DT has misinformed Stackworkz before.** Dorte: *"you will be surprised how sneakily they get in, because they think they understand what we want."* Michael clarified it is DT rather than Stackworkz: *"DT explaining it incorrectly... but it's been built wrong, so there's just some misunderstanding there that we have to be cautious that DT don't tell you and Stackworkz something that we haven't signed off and approved."*

**And Michael set the design authority plainly:** *"we've always said that **design comes first**. If you aren't happy with it, we will look at it and discuss a way forward. But **we should be making decisions that improve our design, not take away from it.**"*

## DT still knows nothing about the AI

Dorte raised the timing, and it is a judgement call rather than an oversight:

> *"We haven't given them anything about what we want to do with AI, Mike. I believe apart from some initial [things]. **This will blow their mind and it will send compliance guys into a black hole again.**"*

> *"It's the fine balance, when is the right time to drop it. If we're going with launch, we need to do that drop rather sooner than later."*

**The mechanism she and Michael are building first:** a **launch tracker** of the genuine must-haves for the website and knowledge hub launch, with later phases behind it, *"like we do with you guys."* Once that exists they decide when to bring DT in, because *"they are very slow in responding if we need something from them."*

**Brett's instinct is to minimise the ask:** *"there's a lot that we can do just with the existing APIs. Let's not rattle any changes on DT."*

**For context on who is being managed here:** DT is roughly **60 people** on one floor of a corporate building in Centurion, South Africa.

## Findings and where they landed

### Commercial and legal

| Finding | Destination | Action |
|---|---|---|
| **No signed DPA; MSA not in play; current phase has no appendix** | [[commercial]], [[open-questions]] | New row **#103** |
| **The DPA drafting is substantially complete from July**, rebuilt as a real DPA with Article 28(3) obligations | [[commercial]] | Recorded; the facts Dorte needs largely exist |
| **OpenAI is in the fallback chain and not in the sub-processor list** | [[open-questions]] | Recorded in **#103** |
| Dorte's US-transfer worry maps to the July note on **pinning EU model endpoints** | [[open-questions]] | Recorded in **#103** |
| She wants one trip to external counsel, so the pack must be complete first | [[commercial]] | Recorded |

### Architecture and delivery

| Finding | Destination | Action |
|---|---|---|
| **Rate limiting resolved**: controllable per IP and endpoint, needs a static IP | [[open-questions]] | **#97 answered** |
| **The AI layer gets its own node in DT's European Azure stack**, inside the PCI environment, already built | [[architecture]], [[open-questions]] | **#70 answered**, **#69** advanced |
| Checkpointing store location still undecided | [[open-questions]] | Remaining half of **#69** |
| Dependency list delivered; Supabase auth and checkpointing flagged as pilot-only | [[integrations]] | Recorded |
| **DT built the internal API wrong and is rebuilding it entirely** | [[txn-api-reference]], [[open-questions]] | Added to **#32** |
| **6,000 test cases run**, defects minor to critical, a fortnight more testing | [[open-questions]] | Added to **#32** |
| **Launch gated on cardholders, cards and accounts being signed off** | [[delivery]] | Recorded |
| Public sandbox retention short; per-user sandbox is a later phase | [[open-questions]] | Added to **#91** |

### The build

| Finding | Destination | Action |
|---|---|---|
| Agent moves from scripted workflows to **malleable** ones, with permission-based tool calling | [[agent-orchestration]], [[open-questions]] | **#73** moving to implementation |
| **No mechanism to summon a human for an approval** | [[open-questions]] | New row **#104** |
| **Three MCP servers**, kept apart so docs traffic cannot affect the agent | [[docs-mcp-server]], [[mcp-server]] | Recorded |
| Co-pilot: page navigation, chat export, sandbox calls next | [[portal-co-pilot]] | Recorded, updates due Thursday |
| **Marqeta now leads with a co-pilot**; Dorte wants ours prioritised for launch | [[open-questions]] | New row **#105** |
| Direct Stackworkz access granted; DT held until API integration | [[integrations]] | Recorded |
| **DT still knows nothing about the AI**, and the timing is deliberate | [[open-questions]] | Recorded in **#105** |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Send the dependency and repository list | George | Compiled; goes to Michael and Stackworkz first, then DT |
| Send Dorte the MSA and data framework | Brett | **The vault's July drafting is the better starting point** |
| Book a session with Dorte on the data agreement | Both | She asked for it |
| Add OpenAI to the sub-processor schedule, or drop it from the chain | Novosapien | Before the pack goes to counsel |
| Verify EU model endpoints are actually pinned | Novosapien | The July note's open item, and Dorte's actual worry |
| Give the agent a static IP | Novosapien | The one condition on the rate limit being lifted |
| Decide where the checkpointing data lives | Both | Michael open to the same environment |
| Set up the Stackworkz session | Dorte | Brett asked; she will send dates |
| Estimate when the co-pilot could first deploy | Novosapien | Michael needs it for the DT timeline |
| Decide whether to prioritise the co-pilot for launch | **Ian** | Dorte's preference is yes |
| Send the Marqeta menu user story | Michael | For the portal export features |

---

## Transcript

Oct 6, 2026

## **TXN \- Agentic AI SU \- Transcript**

### **00:00:02**

**George Westbrook:** No sapion. The f\*\*\* is this? Perfect.

**Vineth Siriwardana:** It's great.

**George Westbrook:** Hello.

**Michael Moores:** Are you okay?

**George Westbrook:** All good. How you doing?

**Michael Moores:** Yeah. Well, thank you.

**George Westbrook:** So, we were just testing out the raise your hand feature in uh in Google Meet. I think it was one one day we're in a meeting and somebody's gone like that and we're like, "What?" Then, yeah, we were all children at heart.

**Michael Moores:** Let me just check with I think Ian's traveling at the moment and I'll just check with Twitter.

**George Westbrook:** How was How was your weekend?

**Michael Moores:** Yeah, that's about Thank you.

**George Westbrook:** It It was all right. It was all right. traveling on Sunday. So, back in back in England now, which is a bit different.

**Michael Moores:** Definitely. It's a lot colder now.

**George Westbrook:** Yeah, I think it was when we got off got off the uh the plane and were getting the train at around 6:00 in the No, about 8:00 in the morning and it was just gray outside and we were like, nah,

### **00:03:17**

**Michael Moores:** Yeah. Yeah.

**George Westbrook:** little bit little bit different. The holiday blues

**Michael Moores:** Yeah. Definitely.

**Max Kingaby:** Glad you got holiday blues, George, cuz I actually got work blues because I was working out there.

**George Westbrook:** You know what I mean? When you go to like a holiday country.

**Max Kingaby:** No, cuz I wasn't

**Michael Moores:** Okay, I've not got anything back from me. So, we can start from your side if you want.

**George Westbrook:** All right. Um, yes. I think first thing is the the list of packages. Literally did that before the call. Um, so I'll send that over after. Um, I mean, I'm looking through I'm getting it to do a review. Um, there's nothing from our side which looks like it it it's some random package that some guy in I don't know, Russia has made and there's three people using it. Um, oh, here we go. How we doing,

**Brett StClair:** Hello mate.

**George Westbrook:** Brett?

**Brett StClair:** Hello guys.

**Michael Moores:** So

### **00:04:19**

**Brett StClair:** Sorry I'm running late. Little bit train train issues. I've been training trying to I haven't trained all I just

**Michael Moores:** this

**George Westbrook:** Don't lie.

**Brett StClair:** got on one

**George Westbrook:** Yeah, we were just going through the packages. Um, so yeah, there's nothing really can see there that's going to be that I we could see for being problematic, but obviously we don't know what criteria DT are going to use specifically. Um, I think there's only one one thing which is the MCP package which I put a note in there where there's one of the packages has got a dependency which is a lower version than the updated version. So that might might potentially be an issue. Um, I'll do some research to see if there's any way we can get around that, but it shouldn't shouldn't be too much of an issue. Um, and then yeah, I think I'll get that sent over after. outline some of the repositories as well um that we've currently got. Um and then I think there's and anything that we've used that's just for the pilot only.

### **00:05:26**

**George Westbrook:** So I think one of them is like superbase um authentication which because we just for the console needed a quick way to implement authentication. So that we've just put a note it's what we're using. If they got access to the repo now they're going to see that. Um but that's only for the pilot.

**Michael Moores:** Yeah,

**George Westbrook:** And I think the only other one would be there's a package we use for checkpointing for a lot of the agents. So, it's automatically writing to a database for kind of conversation history and tracing purposes. Um, and I suppose that's one thing we'll need to think about is where is that data going to be stored? Is it going to be in the current infrastructure you've got? Is there anything else we might need to use? And obviously, if there's anything else we might need to use, then we're going to need to make sure that we strip out anything that could be sensitive data. Think about where it's going to be stored and things like that.

### **00:06:23**

**Michael Moores:** Yeah, definitely. I think um yeah, if you send that across, we have a look with DT obviously the where everything sits today sort of console the API is within DT's PCI environment. So, you know, it is covered to hold that sort of data.

**George Westbrook:** Yeah.

**Michael Moores:** Um not not PCI in plain text but personaliz personal data and stuff like that. So we can speak to GC if we want to store it in there as well. I said we haven't got anything specific for the AI. I don't know if you're doing a separate deploy but in the initial designs there is uh console knowledge of website. All we would do is just spin up another node for any central AI layer basically and that's where it would

**George Westbrook:** Okay. Mhm.

**Michael Moores:** basically live alongside the API in that same sort of European Azure stack that that we've got going basically. So I think that's pretty much finalized now. um still waiting for sort of documentation but it's it's built it's all there um looking at pushing that towards production.

### **00:07:20**

**Michael Moores:** So just be with the small tweaks that you may need to you know for us to stand up basically to deploy that into that environment.

**George Westbrook:** Okay, perfect. Um I suppose some of the other things that we've been well not related to that um obviously thanks for sending over those documents still having a look through but what we've seen so it seems to pretty much everything that we want cuz I think that was I think like I mentioned last time it's obviously there's always been that not looming cloud but of permissions different users doing different things being allowed to do different things but obviously it's good to to see what what those things actually are now so I think some of the things we'll be working on um or

**Michael Moores:** Yeah.

**George Westbrook:** the let's call it the the main agent um is trying to get in. So first thing will be at the moment it's very good well in my opinion very good given a workflow

**Michael Moores:** Heat.

**George Westbrook:** it's going to follow that um but when some things are a bit tangential so like it's it might need to on the fly come up with its own workflow um or just do these quicker actions in succession um sometimes it's a bit more limited so I suppose it's making sure that when it's got a workflow that is a set workflow it follows that to the tea um which I think it's doing pretty well at the moment Um but then some of that more those more malleable workflows um I think that's where

### **00:08:38**

**George Westbrook:** we'll be we'll be doing a bit of work alongside the MCP server for the agent um trying to add in some of those permissions so that we can test somebody's a program manager they're going to they're going to get this level of access somebody else is going to be a lower lower level or a higher level. How does that work? how does the agent deal with it? Um, I think that on the the agent side, that's where we'll be focusing on. And I think in terms of the the co-pilot, um, I think by Thursday, we'll have some good updates to show. Um, for example, I think one of the one of the things we've been working on is the like when when you are asking about a certain page, um, it's going to actually navigate to that page so that the user can have a look, click around, do whatever they need to do. um exporting of chats as well just in case you want to take it or get a markdown file, copy it to cla like that Marquetta thing that you mentioned last time with the like copy and then it goes directly to that that URL which I think is a cool feature and I think next on next on the list is allowing the agent to actually make some of the sandbox calls on behalf of the user so that they're not having to go in go into Postman do it.

### **00:09:56**

**George Westbrook:** Obviously, if they want to, I think there's a quick copy paste button that we'll probably add so they can just copy the payload and it's going to be easily able to get into Postman.

**Michael Moores:** Yeah,

**George Westbrook:** And then is there is there anything else that you'd want to see or prioritize when it comes to the the docs co-pilot

**Michael Moores:** I think you've covered a lot of that. Yes, obviously helping them implement the code and direct in the right places. So, have I think number one, you know, be able to run stuff and navigate around the pages is is great additions as well. So I'll have a think but I think that's pretty much covered off what we expected to do. Obviously certainly for the first MVP phase obviously we discussed logging in and you know having some sort of this. So we're looking at the public sandbox now about retention. So we're looking at keeping the public sandbox for a very short window of time. um obviously public data. So the next level that would be having a separate environment for you to you know it's personal sandbox basically so you can log sign up log in and I think that will give us a bit more potentially on the knowledge of that we may want to do but I think certainly for the FP while it's public I think that's exactly what we need

### **00:10:59**

**George Westbrook:** Yeah.

**Michael Moores:** um going forward so that's that's Hey.

**George Westbrook:** And Yeah. And then I suppose the other the other side of that coin is the MCP server. Um so I suppose there's the three MCP servers I think we'll have is obviously one for the one for the agent which is almost certain we haven't started building the co-pilot in the console yet but is going to be the same MCP server like with the same

**Michael Moores:** Yeah.

**George Westbrook:** access level. So that's easily able to be reused. Then there's the the MCP server for the co-pilot in in the knowledge hub which the large majority initially is just going to be probably is it's that kind of local file system search where we build the build the local file representation of the of the things that's in Braco. Um I think like I said last time it's amazing to see that they got the web hooks as well. So rather than us having to be like, "Yeah, once once an hour we refresh or after a certain amount of requests, it's just going to be when it's updated, we update it." But it also allows us to add in MCP tools,

### **00:12:11**

**George Westbrook:** say for simulating API requests or doing other actions um and keeping it a bit more isolated from the the agent one. So we're not having to play around too much with extra extra levels of access because at the end of the day MCP servers are really really cheap to run. Um and obviously we wouldn't want traffic from the docs MCP server causing issues on the on the agent one.

**Michael Moores:** Yeah, that sounds good. Um, yeah, no, that's great. Obviously, um, I've had a look at the with the DT team, so we're sort of progressing there as well. Um, and I'll send you a few emails after. So, we've got some sort of, um, response on the versioning as well for you from the YAML.

**George Westbrook:** Okay.

**Michael Moores:** Um, so that's gone a bit further. So it states specifically what it's for, what the channel is, and where to get that YAML from as well. So a new endpoint that they're going to do. So I'll send you their proposed, again, it's not built yet, but the proposed model response and stuff.

### **00:13:09**

**Michael Moores:** See if you're happy with that. Um, so that's that one there. And I also caught up with them on the rate limiting. So very much external.

**George Westbrook:** Mhm.

**Michael Moores:** We can do what we need. We can limit you higher. We can take it off. Whatever we need to do, it's by IP and endpoint. So we can control that fully um as well. So you shouldn't have any issues there. Um they're quite comfortable with that.

**George Westbrook:** And that would that would require a static IP in order for them to be able to whitelist it to in order to give to give that level of access. That correct?

**Michael Moores:** Yeah. Yeah.

**George Westbrook:** Yeah, all good. Um, think what else is there? There's there's a few things on outbound and well, not not content anymore, but the outbound, which I suppose we can catch up with with Ian on the on the side. Um, I think the other thing is with Stat Works, I think might be good either next week or the week after when they're ready if we could just have a another kind of catch up with them, be able to talk about like when when is good to start having those conversations about integrating into what they've built because I think at the moment we've got we've got our console replica which we're building against which in the packages I've removed all those those ones because yeah like it's it's not really re relevant.

### **00:14:26**

**George Westbrook:** because yeah, we're we're not building that part. So, it's only going to be the things that that that we think we need for the the agent, the agent inbox, stuff like that.

**Michael Moores:** Yeah.

**George Westbrook:** But yeah, I think having a conversation with them just just to see how they want to work and I think catching up with them on their thoughts on the the repo that we shared them as well.

**Michael Moores:** Yeah. Yeah. I think um probably a good time to do that. They they're getting a bit stuck now with some of the end points and stuff. Obviously um we're pushing DT um quite a bit. So the internal API was built quite wrong. Um you know where storing the data was very wrong. Um so they're currently rebuilding that entirely. So DTS sort of build obviously we can't build any further until they've done that.

**George Westbrook:** Yeah.

**Michael Moores:** So it does mean that hitting the internal API is a little bit easier than it was before. Sort of a generic JT access rather than scoping per sort of program manager.

### **00:15:25**

**Michael Moores:** So it's really split them properly now. So we're waiting for that to happen. So I think they're they're really stuck basically for you signed off endpoints. Um you know we're going through the sort of UAT testing now. I've done sort of 6,000 test case so far. Um and just pushing to quite a lot of defects coming out from you know ranging from little to critical. So a while before we can get it signed off but we're working in order of what we see priority for um sort of what we call launch. So we're very much focused now on what can we do to get the website and the knowledge hub live. Um and for that obviously we need some endpoints that are at least signed off and documented properly. So we're aiming sort of for the card holders cards accounts those ones to be done then we can sort of look at launching the website and and the sort of marketing exercise and stuff around that and then very much focusing on the MVP. So DT is still building quite a lot the stuff towards the end, but they should be, you know, finishing that off and and looking at the defects as well.

### **00:16:26**

**Michael Moores:** So um we'll keep keep you updated on that as well. But I think yeah, next week if we set up a call between the three of us, we can talk um and obviously just have a look at those some of those points that I sent across as well and how they want you to do that. I think obviously if you've got that um list I think that the first review is them obviously to make sure it all works and doesn't clash with them and then obviously once we've had a discussion and we're all happy between the three of us we can then you know double check with DT that the one's hosting it basically. So um but you know if there's nothing that's you know obscure there then I don't think there should be too much issues. You can have a look.

**Dorte Dye:** Apologies. Step one moment from my desk and didn't came back for some reason.

**Brett StClair:** I was wondering where you are.

**Dorte Dye:** It's like I saw a message popping up from Mike, but it didn't make sense.

### **00:17:34**

**Dorte Dye:** The one moment that means you were late as well, were you?

**Michael Moores:** I was just finished some testing here.

**Dorte Dye:** Sorry about that.

**George Westbrook:** Yeah, I suppose with testing it's kind of like I've got Oh, wait. Somebody on low mute. Yeah, when it's uh you've got like a few more left, you're like, "No, I'll get I've got to get these last few done.

**Dorte Dye:** It finished.

**George Westbrook:** I've got to get the last few done.

**Michael Moores:** Yeah, I blew 33% of my usage yesterday. So, it might it might not survive the week. We'll see.

**George Westbrook:** But I feel like that's the new like productivity metric now. It's it's like whereas people be like, "Oh yeah, did this many did this many commits or this many lines of code," it's now like I've I've blown

**Dorte Dye:** It's broken.

**George Westbrook:** 40% of my usage this week.

**Dorte Dye:** I'm all

**Michael Moores:** Yeah, it's so much better. I wouldn't have found some of the defects I found with with it. It's just been really trying to break it.

### **00:18:19**

**Michael Moores:** So, it's been running for two days basically consistently just Yeah.

**George Westbrook:** Is it

**Dorte Dye:** I think the only challenge Mike has now, he's so productive, the other side can't keep up with it because he's just putting them in a big black hole.

**George Westbrook:** DT DT not using claw codeex and all that.

**Michael Moores:** I don't think so. No, not last.

**Dorte Dye:** They use some things but we don't really can work out what it is and they're not really opening sharing with us which again it's like different companies different approaches right

**George Westbrook:** Yeah.

**Dorte Dye:** it's just um they asked I would say they ask Mike always for more because

**Brett StClair:** That's

**Dorte Dye:** he's delivering more than 30 You know,

**George Westbrook:** They're like, "Mike, are you by any chance do you have like a team of five

**Dorte Dye:** I just do this. It's like, no.

**Michael Moores:** Yeah, not too bad.

**Dorte Dye:** Okay. What have I missed? Have we done?

**George Westbrook:** to be fair,

**Brett StClair:** it.

**George Westbrook:** we are are closer, I think, just skimming over it quickly.

### **00:19:20**

**George Westbrook:** um agent working on making it more so current workflows our opinion working pretty well. They'll go through step by step. Failure rate is minimal. Um speed is improved will can still be improved but what we're going to be working on now is making it a bit more malleable. What do I mean by that? So like you can go in ask anything. It might construct one or two workflows together. It it might find the correct tools at the right time. um which is not something we've been focusing on too much um but it's something we're going to be focusing on now. So you get that kind of full agentic experience where it's kind of able to do anything and everything within the bounds of the access that you have and then given that we'll be updating the MCP server as well. Um so that is trying to pull in more of the permissionbased tool calling. Um, which one thing I forgot to mention, we'll need to think about how we're going to summon somebody for an approval.

### **00:20:21**

**George Westbrook:** Um, what does that look like? Um, how are they notified? Is it just in the console? Things like that on the

**Dorte Dye:** Where I was just wondering because that's where my brain is going.

**George Westbrook:** Sorry,

**Dorte Dye:** Where where are we with the knowledge hub?

**George Westbrook:** next thing. knowledge hub the so we're working on a few extra features um so one of them will be the page navigation so let's say you ask a question about um a certain endpoint or a certain page um it's going to navigate you to that specific page also B. the Mareta feature that Mike mentioned where you can copy either copy the chat or copy something into an LLM into perplexity chat GV claud all that stuff what were the other ones that I mentioned the actual testing of APIs as well um in the sandbox so the agent can actually do the test um it's going to show the user the payload show the request that it's making um so that if they wanted to copy them out into something like Postman um to test it themselves.

### **00:21:33**

**George Westbrook:** they can um MCP server for the co-pilot the docs co-pilot as well um using the actual data that's in and Braco um is going to be updated the well not the instant but

**Michael Moores:** Okay.

**George Westbrook:** whereas before we were thinking what we might have to do is poll um or set a scheduled job that pulls in the data from Umbraco then recreates the local representation for the agent or the co-pilot, we've got web hook. So the instance something's published, unpublished, we can update it.

**Dorte Dye:** Okay. So, my my head is going DPA again on that one with the privacy policy. So, it's like what what do we want to go live at the launch and what the policies need to have in place?

**Michael Moores:** I guess it depends when when we're actually launching it as well. Obviously, we need to make sure we're happy with how the agents functioning. Obviously, knowledge is done from the stack work sides all ready to go. So, we're just literally the final bits where we're adding let's say the bits from the website or you know whatever you have ready.

### **00:22:43**

**Michael Moores:** So, there's a section we've got is coming soon for you the LLM.ext and AIS and stuff like that. So we can easily turn stuff back on to download or whatever it may be. I think in our call next week that probably should be the first upwind I think just to see when likely you're going to be ready how long that works may need to you know help you work that in basically. Um but I think yeah we need to sort of assess that to where we are and obviously we will feed

**Dorte Dye:** Yeah, I would

**Michael Moores:** in where we are with DT that that's the underlying thing now I think where we're going to be with DT API. Um I say the core five we're not going to launch without them. So it just depends how long it's going to take us to resolve them and sign them off basically. And that's the real um timeline there.

**Dorte Dye:** I was just thinking of when I have to get the policies to external council, I want to have the maximum in there that I don't have to go back.

### **00:23:36**

**Dorte Dye:** So while I might have a slim down version for launch, I want to just go once to that. So we both might need to just work out a timeline.

**Michael Moores:** Yeah, definitely we can work that. Yeah, I think the next step is obviously getting you talking to Stat Works and then we can have that initial meeting and then if there is anything you want to discuss between the two of you, I'm happy for you to do home. And then They're doing that with DT at the moment. So if there any code or integration questions, we can hook you up together and you can start talking directly as well. Um obviously the only thing we ask is where it's feature changes or anything you come back to us um

**George Westbrook:** Yeah. Yeah. Yeah.

**Michael Moores:** stuff. So, but yeah, we can have that meeting and then go from there

**George Westbrook:** Yeah. I suppose. Yeah. Not having a conversation with like we're going to change everything and then go to Mark is like we've changed it all.

### **00:24:25**

**Dorte Dye:** Yeah,

**George Westbrook:** Here you go.

**Dorte Dye:** but you will be surprised how sneakily they get in because they they think they understand what we want. And I was like,

**George Westbrook:** Watch.

**Dorte Dye:** what?

**George Westbrook:** Has that happened already then?

**Michael Moores:** from the DT side. Yeah, not not stat works. Um, but yeah, it's no issues with stats. you saw DT not not really DT explaining it incorrectly which makes sense but it's been built wrong so I think there's just some misunderstanding there that we have to be cautious that DT don't tell you and start work something that we haven't signed off and approved that sort so um but we're we're ironing that out so I don't see an issue with too much now and I say from a DT point of view I don't think they'll need to be involved until you get to the API side the integration stuff like that I think we can talk about the console and that integration with statist directly DT just need to be involved in terms of you will be hosting this are you happy type conversations and obviously when we get to the API integration we get a few more signed off and you want to have a look at that we can then talk with DT about that integration to the API with you specifically

### **00:25:30**

**George Westbrook:** Perfect. Um, and I think I think I think that's everything for today. Um, like I said, we'll we'll be hammering along. I think that was one thing I was thinking is obviously with the knowledge hub being done um one thing we can do is just start ultra prioritize I suppose it's up for debate is ultra prioritizing anything to do with the console so it's a point where we can hand it to stack works and be like this is pretty much done um do you want to start working on this now or we can kind of carry on as we are at the moment which is more obviously both progressing um but more in in parallel rather than just ultra focused.

**Dorte Dye:** Is the the co-pilot done for the knowledge?

**George Westbrook:** No. No. So, so it's both the the co so when we say co-pilot as well, we kind of we we're automatically including the MCP server for the co-pilot for the knowledge hub and then obviously the the agentic experience piece as well. So, at the moment there's progress on both of them.

### **00:26:33**

**George Westbrook:** Um, but we could potentially prioritize more time and resources onto the the co-pilot track, let's say, um, to accelerate that for launch. Um, if if that's something that you think would be more viable.

**Dorte Dye:** I think that would be my preference Mike but I guess it's Ian's I mean the thing is when we go to

**Michael Moores:** Yeah.

**Dorte Dye:** market right we need to have a differentiator to keep the interest because the moment you launch

**Brett StClair:** Yeah.

**Dorte Dye:** something that doesn't look fairly interesting testing people don't go any further. So it's the one time we launch we need to get it right.

**Michael Moores:** Heat.

**Dorte Dye:** Hence why Mike said we need to have these core components ready. Without it it's a complete nogo.

**Michael Moores:** Yeah, I think especially now Marquet has redesigned their website to be very much co-pilot up front. So that's quite quite a shift from them from how it was before. So I think at least matching that would be ideal either at launch or you know very close afterwards. So I say we if you get an idea from that how long you think you'll be into a position where you can do let's say the first deploy or integrate that and then we can work that into our timelines in terms of the DT one.

### **00:27:39**

**Michael Moores:** I'm probably looking at couple of weeks at least I think for the rest of the testing um I'm honest with the defects that coming back and stuff. So, we've got a bit of time there to make sure it's aligned and and ready to go. And then obviously um getting that deployed into production will be through sort of DT. So, there's a few hoops we need to jump through before it can go in with launch, if you will. Um obviously, we always expected it would be sort of post launch anyway. It just happens that you've the timelines have matched up a little bit better than initially planned. So, um yeah, leave it with us. Please have a look at that and see if we can get that for us. If you've got that um data um packages, we can get that over DT. That's going to be the longest bit if anything comes out of it.

**George Westbrook:** Yeah.

**Michael Moores:** Uh there was quite a few in the knowledge hub that they weren't happy with.

### **00:28:27**

**Michael Moores:** But if they've not done AI before on their side, I don't think they're going to have much to say. I'm hoping uh with that. So that'll be great.

**George Westbrook:** Yeah. I think it there might be some things that are added or some things taken away. Um, I don't think it'd be too much. Um, but I thought we'll just get we'll get what we've got at the moment rather than it being something that we're like, "Oh, no. We might add this later." And then still is there's nothing that's been sent over.

**Michael Moores:** Yeah, at least it's a smaller discussion. If you do add something, then we can just say we're adding this in,

**George Westbrook:** Yeah.

**Michael Moores:** you know, have a look basically and go from there. We've always said that, you know, design comes first. So, you know, if if you aren't happy with it, we will look at it and, you know, discuss a way forward. But I think you we should be making decisions that improve our design not you know take away from it basically.

### **00:29:14**

**Michael Moores:** So if there's a live you think absolutely you need to have because it'll provide a worse experience. If not then obviously we will prefer that approach and obviously we will handle it with with DT basically. So yeah just keep that as no and we can go from there. And then what I'll do as well is I'll send you the user story properly for that menu on Marqueta. Just got a few more bits to put into it. Not sure who does what in I went from the Marqueet website. A lot of it is just a link to chat GP and stuff like that.

**George Westbrook:** Yeah.

**Michael Moores:** Something that Statworks can do quite easily themselves. It's more the bottom ones like the installing MCP obviously that we I think we just need the URL for basically from MCP. Um and then we can go from there. So I'll send that out and see what sort of comments you've got from both sides basically as well.

**George Westbrook:** I think I think that's I think that's everything.

### **00:30:02**

**George Westbrook:** I think bang on time as well. If you want to just wait like 40 seconds so we we're not like on time.

**Brett StClair:** Hello. Hello.

**Dorte Dye:** You should have given us a warning that you're back in the UK and the call is in the evening. I was like

**George Westbrook:** Oh, well, I I was confused by that the other day as well.

**Brett StClair:** No.

**George Westbrook:** I was

**Dorte Dye:** because I like I Paul I know you just migrated. I mean I know Brettbecause you hated the heat but and the shirts.

**George Westbrook:** It was It was hilarious seeing Brett sunbathing. It'd be sat there in a shirt with a hat on underneath an umbrella for about two minutes before it was like, "I'm going back in the air conditioned room."

**Brett StClair:** Me and Sunshine,

**Dorte Dye:** This is the problem.

**Brett StClair:** not friends.

**Dorte Dye:** When you're old, George, you can't cope anymore. Either drinking or the sunbathing.

**George Westbrook:** To be fair, Brett's good at drinking. I'll give him that.

**Dorte Dye:** I would never have expected anything less.

### **00:30:58**

**Dorte Dye:** Okay, cool. Lots of moving parts again. Move.

**George Westbrook:** It's all good fun.

**Dorte Dye:** That's what you think. Mike and I are just like spinning ahead. No. Cool. So, we come up with a with a proposal and then I just probably need some input from the LLMs and bloody data storage. Did you Brett, did we sign a a data processing agreement with you guys?

**Brett StClair:** No,

**Dorte Dye:** Did we sign an agreement or did you just had small order forms with Ian

**Brett StClair:** we no in we on the agreement side we put an agreement together. We then did a appendix to the agreement uh for the first two bits of work and then the second work we've just got a proposal but no appendix to that agreement and the agreement still needs to be in play. In that agreement I put a very lightweight data components because I know you were working a whole lot of data compliance components that need to be

**Dorte Dye:** This this is the s\*\*\*

**Brett StClair:** added.

**Dorte Dye:** that really ruins my life.

### **00:32:05**

**Dorte Dye:** Seriously.

**Brett StClair:** So

**Dorte Dye:** And we don't we don't have a specialist in the company. So I need to gather all of the facts and then we go to external council. But for that I really need to have everything watertight that I can explain everything. Um

**Brett StClair:** well shall I send you what I had put together as the baseline proposal and then how we split it out was um appendixes to the propo like a like an MSA sorry baseline MSA and then within that MSA I had a very lightweight data framework which

**Dorte Dye:** Yep.

**Brett StClair:** I kind of kept it that way because I knew you were working on a whole lot of really deep uh kind of components that we can either put in as an appendix or build into the main NSA as

**Dorte Dye:** send me what you have. I need to have a think about it because again at the moment I don't know while you're building this stuff you still would be running it right because all of the LLMs are via your contracts And for as so it's like I think that's where the joy always goes when the LLM sends something to the US

### **00:33:05**

**Brett StClair:** Yeah,

**Dorte Dye:** or

**Brett StClair:** correct. At the moment I'll build. So this is going to be the slight complication. So got two components.

**Dorte Dye:** do not complicate anything on top of my life already please

**Brett StClair:** Tell you what, let's take it offline. We need everyone else.

**Dorte Dye:** a glass of wine at 7 in the morning Mike and I started working at

**George Westbrook:** Yeah.

**Dorte Dye:** 4 and we haven't even been in Bali so it's like our bodys are just completely

**George Westbrook:** Yeah.

**Dorte Dye:** screwed.

**Brett StClair:** Sure. That's okay. I'll send you what I have.

**Dorte Dye:** Yes, please.

**Brett StClair:** And then uh the key thing was

**Dorte Dye:** And then book something in with you to just get my head around that. Um

**Brett StClair:** around that. And then can I book with you some of um stuck work

**Dorte Dye:** me.

**Brett StClair:** time just that seemed to work really well last time.

**Dorte Dye:** Oh yeah.

**Brett StClair:** You coordinated them and kicked their asses to the point we could get a meeting.

### **00:33:58**

**Dorte Dye:** Honestly, they are so responsive. I don't see any problem with them. Um,

**Brett StClair:** Okay.

**Dorte Dye:** did we say we're waiting to introduce DT until we're a bit further down the line? Okay,

**Michael Moores:** Yeah.

**Dorte Dye:** fine. Don't want to wait. The sleeping tigers or what do you say? I don't know. It's like, see, my brain is not working.

**Brett StClair:** That's leaving behalf beast.

**Dorte Dye:** Oh,

**Brett StClair:** Um the way we can also like there's a lot that we can do just with the existing APIs like let's

**Dorte Dye:** okay.

**Brett StClair:** not rattle any changes right.

**Dorte Dye:** No,

**Brett StClair:** on DT.

**Dorte Dye:** but it's the point of this is a massive change for them.

**Brett StClair:** Yeah.

**Dorte Dye:** We haven't given them anything what we want to do with AI, Mike. I believe apart from some initial this will blow their mind and it will send um compliance guys into a black hole again.

**Brett StClair:** I don't know what finance compliance like.

**Dorte Dye:** I I think it's the fine it's it's the fine balance when is the right time to drop it.

### **00:34:54**

**Dorte Dye:** If we and we going with launch we need to do that drop rather sooner than later. So Mike and I are just finalizing a launch tracker for they are the really musthaves for website and knowledge hub launch anything around that and that would feed into that one then as well. So um and then you will have the other phases like we do with you guys right it's like what we're building out for the next customer and all of that stuff. So I think um once we have done that then we should have that discussion when we bring them in because they are very slow in responding if we need something from them.

**Brett StClair:** How big is DT by the way?

**Dorte Dye:** They had a really pretty good big office right like a big corporate building one whole floor

**Michael Moores:** s\*\*\*.

**Dorte Dye:** I would say 60 poua

**Brett StClair:** They they based in Centurion.

**Michael Moores:** Yeah.

**Brett StClair:** Yeah.

**Dorte Dye:** ptoria have

**Brett StClair:** Centur I think I've actually been to their offices before and a a lifetime ago like Absa days Barkley's days.

### **00:35:53**

**Michael Moores:** I think it's one of them. Is it Mercedes office? It used to be. I think there is.

**Dorte Dye:** Yeah.

**Michael Moores:** Um Yeah.

**Brett StClair:** Yeah. I was wondering if it is the same. I was like because I've been I went to visit a whole bunch of houses

**Dorte Dye:** It looked very new. So if you have been an absess times,

**Brett StClair:** and how

**Dorte Dye:** I don't think so. I think that building is not that old old. That was looked like a new development because they have shops there and restaurants nearby as

**Brett StClair:** is it Stephanie

**Dorte Dye:** well.

**Brett StClair:** Centurion? When was my days? 2017 2018 2019

**George Westbrook:** What was that in your 50s?

**Brett StClair:** twat. My daughter's only 21\. She turned 21 today.

**Dorte Dye:** Wow. That's why she's not here.

**Brett StClair:** I said to her, just enjoy the She's got a bunch of friends and everything over at the moment.

**Dorte Dye:** Nice.

**Brett StClair:** It's just like you only turn 21 once and you've had to spend the morning with these people.

### **00:36:47**

**Dorte Dye:** But you always say that you only turned 22, 23\. It's like my daughter turned 16 the other day and it's like for f\*\*\*\*\* sake, it's American marketing s\*\*\*. is like 16 you can't do anything different. You can drink a glass in the pub with a beer.

**Brett StClair:** I I 21\.

**George Westbrook:** You can vote. You can vote.

**Dorte Dye:** Huh?

**George Westbrook:** You can vote, I think, when you're 16\.

**Dorte Dye:** Yeah. But you know when you're 16 that's the least that they think

**Max Kingaby:** Satan. Satan.

**Dorte Dye:** in really I think in Germany they moved it down to 16\.

**Brett StClair:** Well,

**Dorte Dye:** But who

**George Westbrook:** Perfect.

**Brett StClair:** I turned 21 29 times.

**Dorte Dye:** are you at the end of the alphabet right? you start counting again. Okay, on that note, I get you couple of dates from Stack Works.

**Brett StClair:** I'll get you.

**Dorte Dye:** Ping ping me some dates and then I uh ask them and send me the other stuff and then we'll pick up from there when I'm awake.

**Brett StClair:** Perfect.

**Dorte Dye:** Thank you guys.

**Michael Moores:** Cheers.

**George Westbrook:** Thanks very much.

**Michael Moores:** Take care.

**Dorte Dye:** Bye.

**Michael Moores:** You say that way.

### **Transcription ended after 00:37:58**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*