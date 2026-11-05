---
date: 2026-11-03
type: general
description: "Knowledge Hub demo to TXN's chairman and DT, then the first hosting talk: no deal-breaker, but no design or cost until Willie Olivier's questions are answered"
scope:
  - "[[portal-co-pilot]]"
  - "[[architecture]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[portal-co-pilot]]"
  - "[[architecture]]"
  - "[[permission-scoping]]"
  - "[[agent-access-layer]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Knowledge Hub Demo and AI Infrastructure, with DT (2026-11-03)

> **Source:** transcript from a new notetaker, titled "Fw: AI Infrastructure Context", 3 November 2026, 14:00, about 53 minutes. **Novosapien:** George Westbrook, Brett StClair, Hasan Ahmed (camera off, does not speak). **TXN:** Ian Johnson, Steve (group chairman). **Direct Transact and others:** Anthony, Willie Olivier, Marco, Zane, Jacques, Pete, Shaul, named in passing. Michael was expected and is not heard. This is the demo #115 has tracked since 15 October, held a day later than the earliest date given on 27 October.
>
> **The speaker labels are unreliable, so this page attributes by content.** The transcript has three named voices for at least six people:
>
> - **The demo prompts** George typed are labelled *Anthony De Gray Birch*.
> - **The technical questions in the second half**, labelled *Anthony*, are **Willie's**: Brett answers *"Right questions, Willie"*, the speaker asks *"do you use OK, if"*, the Open Knowledge Format George looked up afterwards ([[2026-11-03-agentic-standup]]), and Michael says Willie works on the data lake. The audit and federated access questions earlier, also labelled *Anthony*, are a DT voice who says *"I'm not a technical person"*, most likely Anthony himself.
> - **"Steven Kark"** is Steve the chairman (*"it's all Greek to me"*, addressed as Steve by Ian), and also a DT lead who promises a design and a cost model, and someone asking about Gemini, possibly Marco.

## The demo landed with the audience it was for

**Ian framed it as two parts**: the Knowledge Hub demo, because *"many people haven't actually seen what we've been building"*, then hosting. *"The Knowledge Hub... is the first asset of what's being built that has to go live, ready for go-to-market."*

**George ran the agreed script** from 27 October ([[2026-10-27-agentic-standup]]): what TXN does, *"I want to give my customers a card but I've never done this"*, the sandbox walkthrough, the lost card with Apple Pay, node code, and the export to Claude and Perplexity. Points he made along the way:

- **Answers adapt to the asker.** A developer gets payloads; a head of operations gets the process, with detail on request.
- **The agent shows what it is doing**, because *"you could be sat there waiting for 20 seconds and nothing's popping up"*.
- **Workflows run from SOPs in its memory** so everyone gets the same experience, and it asks when the request is ambiguous, such as the card type.
- **The one-approval flow is built.** *"Rather than having an approval for every step it's going to say these are going to be the three operations that I'm going to do in this sequence."* That was a plan on 27 October.
- **The docs MCP server** for Claude or ChatGPT: *"exactly the same guides that the Docs assistant has, obviously just limited by the functionality that's within their assistant of choice."*

**Brett's line**, for the record, since it sits alongside George's SOPs: *"the user journeys are not pre-designed or pre-programmed. This is agentic AI... we have guardrails but we don't do what your traditional agent from three, four years ago was about, shaping user journeys."*

**Steve's verdict:** *"It's all Greek to me, but looks quite good."* And as he left: *"It looks great."* Ian, afterwards: *"Pretty standard response from Steve after 30 seconds."* **The fallback videos were not needed.** George: *"had the three different videos as well lined up, but fortunately we didn't need them."*

**Ian's positioning, which is the clearest statement yet of what the Knowledge Hub is for:**

> *"The way that it's been designed is to adhere to the kind of meeting people where they are... Some people actually that we interviewed during the process said I'll just start coding and then if I have a problem I'll look at the docs. Some people will value the copilot... Others will do what George showed towards the end, which is I'm just going to copy these pages and put them into my AI coding thing. **What we've designed is to make sure that it doesn't matter how you want to work.**"*

### Adding APIs costs nothing, and the Console is a different experience

**Steve asked how hard it is to add APIs** *"without heavy lifting and heavy cost"*. Ian, translating George: guides come from Umbraco on publish, the API reference from the YAML, *"so there is no rework for the Novo guys to do to add more feature functionality. It's just reading from other sources."*

**A DT voice asked whether the Console reuses the Knowledge Hub work.** Ian: the Control Center *"is less about reading documentation... and more about taking actual kind of action"*, with impact guidance on parameter changes and natural-language product set-up for approval. George described the two Console experiences, the co-pilot beside the page and the full agentic experience in one chat pane, and claimed nobody else offers both. Ian: *"We haven't seen it."*

**A Control Center demo for DT** is promised *"in the next few weeks"*.

## Permissions and audit, as DT heard them

**The question**, from the non-technical DT voice: if the agent can block card 1234 for me, does it understand the access control the program owner federates?

**George's answer is the two-layer model** recorded on 22 October ([[permission-scoping]]): the agent never sees a tool the user lacks, and if it somehow had one, the Control Center back end blocks the request. **New detail: the block becomes a route, not a dead end.** The error tells the agent the action was unauthorised, so *"it would then go to an alternative route. Might be you need to speak to Sally for approval. I'm going to create an approval request which is going to go to Sally."*

**Ian added the human-approval case**: a support team suspending or reissuing cards *"you might want those to be approved every time"*. George added that some actions always need the user's explicit click when an agent does them, deleting a card for example. Typed approval is possible too, but the button is preferred for sensitive actions.

**Then the audit question.** *"We have audit trail on every click you do. If it's an AI instruction and the action is taken, how do you retain audit trail?"* George: **the tool-call traces**, *"obviously redacting some of the sensitive data in the tracing... for an audit perspective, you understand everything that the agent said and everything that is done."* He also framed the traces as training data for making workflows faster.

**What was not asked.** Whether redacted traces satisfy TXN's audit obligations as a card program, how long they are kept against the 72-hour retention, and whether they join the Console's own click trail. New [[open-questions]] #128.

## Marketing the AI without giving it away

Steve: how do we explain it on the website *"without showing everything? Because I suppose that would be a competitive issue."* **Ian: *"I think the answer is not to tell people, but to show them."*** Short video snippets, already under discussion with Bronwyn and Nicola, *"without fully opening the kimono"*, and especially for the Control Center, *"where you only get to experience that once you're a client."* On the Knowledge Hub people can try it themselves. That is the same direction as the Loom discussion on 27 October. See [[commercial]].

## Who supports the AI code: Novosapien, until TXN takes it over

**Ian, to DT, before the hosting conversation:**

> *"When we talk about the AI code, that AI code is going to be **supported by Novo until such time that TXN decides to take it over**. Which would mean us employing our own AI engineers and also having a period of handover between Novo and those guys so we could take ownership of it. **What this conversation is not about is putting code into DT and asking you guys to support it.** This is literally about the infrastructure and the hosting."*

That settles the support line DT were told on 20 October, and it names the end state: TXN's own AI engineers after a handover. It also answers part of #126: when the agent fails in production, the people to alert are Novosapien. No support terms, hours or handover plan were discussed. See [[commercial]].

## Hosting: no deal-breaker, no design, no cost, and no deployment time

**The documents reached DT, via Jack.** Two of them: one lists libraries, one lists the Azure services Novosapien think they could use. Several people were unsure they had been sent at all, and the DT lead said *"I may not have been part of the distribution list."*

**DT were not ready to decide.** *"I don't think it was expected to give an update or a view in the session... the team is aware, they did look at the documents and do have feedback on a high level."* Then the line that matters:

> *"I just quickly scanned the documents. I mean, **there's nothing that's really a deal-breaker in it.** So I think we need to just put it into our design and send you a bit of a design in terms of what we can do. I think the only thing is that we just have to **optimize the cost slightly**. But I'll put it also in... an **infrastructure cost model** for you, Ian."*

### The LLM section got discussed with DT anyway

On 27 October the LLM section was held back from DT for an internal call between Dörte, Ian and Novosapien. That call did not happen ([[2026-11-03-agentic-standup]]), and DT asked directly: *"behind the scenes, it's going to run some sort of Gemini consumption as well, is that correct?"*

**George's answer corrects what the vault recorded on 27 October.** Testing uses Gemini **directly from the Gemini API**, not through Azure. The Azure options are Gemini through **Azure Databricks**, *"which to me sounds ridiculous"*, priced per token rather than deployed, and OpenAI or Anthropic models through **Azure AI Foundry**. **Fallback is built in**: if a region or provider is down, *"it's going to fall back to different models."*

**LLM costs go into DT's infrastructure cost.** DT asked whether that should be included. Brett: *"Yes"*, and Novosapien have sent estimates across a couple of providers, because TXN should *"really want it in your ecosystem and lock it down."* See [[architecture]] and #70.

### Willie's questions gate the design and the cost

**Willie asked the sharpest questions of the call.** Is Foundry used for indexing the documentation, or are pipelines feeding the context window? *"And how do you limit the data that's actually passing into the large language models? How do you separate that? How do you split that out? **Do you use something that masks it** beforehand, afterward, or within the pipeline?"*

**George answered the first half.** No indexing and no vector database. At start-up the agent reads Umbraco into an in-memory copy and searches it with read, glob and grep, *"the tools that they've been trained on"*, isolated so it can only touch those files and never run anything destructive. **The masking question was not answered.**

**Willie pushed on cost:** *"we all understand that it takes everything out of the context. We know it takes a hell of a lot of tokens."* No vector database means no double storage, *"which in the first case saves some money"*, but there are transfer, token and conversion costs, and he asked whether OKF structures the files. George: *"No, I don't think so"*, to check with Hasan. (After the call George found that OKF is effectively what Novosapien built.)

**He will email about five questions.** Ian confirmed the order: the answers come first, then DT's design and costing. Willie on the cost model: Azure charges for indexing per region, token usage, storage and Foundry, and failover regions add cost. New [[open-questions]] #127.

### Two weeks to launch, and no deployment time

Ian asked for *"a sense of the actual deployment of the capability once we're settled on a design and the associated costing... how long it would actually take to deploy"*, against go-to-market *"currently planned to be the 17th of November, which is two weeks away."* Then: ***"Deafening silence. Understandably, this is what this is, this is the challenge."*** Deployment time was deferred to a separate conversation. Willie: *"most of us have rolled out in Azure before. It's not going to be the complication."*

> [!warning] Ian said 17 November.
> Every other record, including the standup an hour later, says **16 November**. The vault keeps the 16th until the date is confirmed.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Demo held, landed with Steve; fallback videos not needed | [[delivery]], [[open-questions]] #115 | Callout added; row **answered** |
| One-approval sandbox flow shown live; MCP server shown | [[portal-co-pilot]] | Callout added |
| Adding APIs needs no rework (Umbraco webhook, YAML) | [[portal-co-pilot]] | In callout |
| Ian's "meet people where they are" positioning | [[portal-co-pilot]] | In callout |
| Control Center demo to DT in the next few weeks | [[delivery]] | In callout |
| Blocked action routes to an approval request; sensitive actions need a click | [[permission-scoping]] | Callout added |
| AI audit trail is redacted tool-call traces; fitness and retention unasked | [[agent-access-layer]], [[open-questions]] #128 | Callout added; **new row** |
| Show, don't tell: short videos, with Bronwyn and Nicola | [[commercial]] | Callout added |
| Novosapien support the AI code until TXN hires and takes over | [[commercial]], [[delivery]], [[open-questions]] #126 | Callouts added; row updated |
| DT: no deal-breaker; design and cost model to follow; cost to optimise | [[delivery]], [[open-questions]] #119 | Callout added; row updated |
| LLM discussed with DT despite the hold; Gemini API direct in testing; Databricks or Foundry on Azure; fallback built; LLM cost in DT's cost | [[architecture]], [[open-questions]] #70 | Callout added, corrects 27 October; row updated |
| Willie's questions, masking unanswered, gate design and costing | [[architecture]], [[open-questions]] #127 | Callout added; **new row** |
| No deployment time, two weeks to launch | [[delivery]], [[open-questions]] #119, #125 | In callout; rows updated |
| Ian said 17 November | [[delivery]] | Flagged, not changed |
| Brett: journeys are not pre-designed | n/a | Context, recorded on this page |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Email his questions (about five) | Willie | Not dated |
| Answer Willie's questions, including data masking | Novosapien | As soon as they arrive |
| Check with Hasan whether OKF is used | George | Done after the call: effectively yes |
| Send a design and an infrastructure cost model | DT | After Willie's answers |
| Say how long deployment takes | DT and Novosapien | Separate conversation, not booked |
| Show DT the Control Center | Ian, Novosapien | In the next few weeks |

## Transcript

# Fw: AI Infrastructure Context

Tue 3 Nov, 14:00  
Client: TXN

**Brett StClair** (0:00): Thing and essentially will be a replica of George's fantastic acting that he'll be doing in this next demo.

**George** (0:09): To see exactly.

**Steven Kark** (0:10): It needs a voiceover to see exactly what that thing does, because without the sound, it's too tough, you know?

**George** (0:15): Yeah, exactly.

**Brett StClair** (0:16): Exactly.

**George** (0:18): You got me today for the voiceover.

**Steven Kark** (0:19): Unfortunately, you're in the other one as well, George. Yeah, I mean, can't you have a. Can't you just use like an AI voice so you actually need someone to talk?

**Brett StClair** (0:31): George is the AI avatar.

**Anthony De Gray Birch** (0:34): Okay.

**Steven Kark** (0:35): He's not. It's not a real person. All right, excellent.

**Ian Johnson** (0:40): I'm good. Sorry.

**Steven Kark** (0:42): We've got camera. Camera shy Marco and camera shy Zane and camera shy Hasan. All right, very good.

**George** (0:55): Yeah, Hasan. Hasan meant to be turned on. He's not. Yeah, he's not an angel that's in heaven with a white screen. That's Brett today.

**Ian Johnson** (1:04): They're just. A few people are just wrapping up this session that we've had with the DT teams that I'll be joining shortly. Here we go.

**Steven Kark** (1:13): Good.

**Ian Johnson** (1:20): I thought the voiceover was good, by the way. George just listened to it this morning.

**George** (1:24): Yeah, I thought. I thought I'd take out some of my. My Jacques usually put in. Brett tells me they're not very funny, but they come from Brett.

**Steven Kark** (1:32): So

**Ian Johnson** (1:34): I've gotta be honest, you guys are awesome at what you do, but the AI geekness is off the charts when it comes to comedy.

**George** (1:44): I have to speak to my Claude, who tells me the jokes when we're on the call. So Ian said they need to be funnier.

**Ian Johnson** (1:51): Try.

**Steven Kark** (1:53): Is everyone on? No, Mike is missing. Is he. Many people.

**Ian Johnson** (2:03): Good. So just. Just to frame this. So what we. There's two parts of the meeting. The first part is the bit that we really wanted. Any. Hello. Any, by the way, Anthony. And to join. Just to see. Obviously we've been talking about the AI and how we're intending to use it as TXM with it being a foundational pillar of what we're trying to do. But we're at a point now where the second part of the meeting. We need to talk about actually getting this thing into production so that we can start to offer it for go-to-market date. But conscious of that many people haven't actually seen what we've been building. So today's demo is focused on just the Knowledge Hub. So the Knowledge Hub, or otherwise people might call it kind of developer portal, is the first asset of what's being built that has to go live, ready for go-to-market. So we thought we would ask the Novo guys to give you a demo of what we've built, what they built. So George, over to you, over to me.

**George** (3:11): Right, let me get this screen shared. Can everybody see my screen?

**Anthony De Gray Birch** (3:21): Yeah, all good. Perfect.

**George** (3:24): Anybody need me to zoom in, zoom out? I'm going to be there. You don't count.

**Steven Kark** (3:33): You have seen it.

**George** (3:37): So I suppose, yeah, this is, this is the Knowledge Hub. Obviously people might be familiar seeing this, but obviously we're in a world now where a lot of people are expecting these AI features and functionality to assist them, be it with understanding or actually when it comes to be it writing code or integrating into systems. So we'll go through some of the features that, that we've got in here today. And I think the best place to start is the copilot. So it's really a digital assistant to allow users to explore the documentation, understand how things work, test in the sandbox and provide a lot of value when it comes to navigating around the system. So I think first question, let's just go, what does TXM do and how

**Anthony De Gray Birch** (4:23): does it all fit together?

**George** (4:29): So one of the things behind the scenes we have is an MCP server which, without going into too much detail, effectively, I'll expand this quickly. So if anybody wants to read it, it's just a way for the agent to have all of the context behind answering the questions. So one of the tools that we have gives the agent the ability to search through the guides, search through the API references, to understand some of the workflow that people are going to be going through. So it's grounded in the truth that is the TXM platform. And there we go, you can see, see the response there. Some of the nice features and functionality we've added in with the team is it's going to navigate to the page that's most relevant to the question that the user said. It's not to say it's always going to go to a page, but if the agent thinks, okay, this user is asking about how TXM works, well, it makes sense as long as, as well as giving my answer, I'm going to also take them to the relevant page so you can expand along, ask more questions if needed, navigate to other pages. And yeah, I think the, the next part that we good to show is a pick a real workflow. Let's go.

**Anthony De Gray Birch** (5:48): I want to give my customers a card, but I've never done this. Where do I start?

**George** (6:04): So one of the things the agent's going to do when it's speaking to the user, given the nature of the questions that they're asking, is going to cater it to, let's say it could be a developer who might be asking a more technical question. So it's going to adapt its responses to fit with the user that's asking the question. If somebody's just coming and asking, how does it work? It's more of a business-focused person. Maybe it's a head of operations, for example. Obviously there might be some technical detail that's needed there, but it's maybe not going to be going into this is this payload? This is that payload. If the user requests it, it's going to give them that detail, but it's going to cater the responses based on the user. So let's go.

**Anthony De Gray Birch** (6:43): Yes, let's look into those three things, please.

**George** (6:51): So on top of that, you might have seen flashing up there. When the response is done, it's going to suggest questions to the user to allow them to go in a bit deeper. Because I think maybe, maybe this might just be a me thing. But sometimes as a developer you can be a little bit lazy. You might ask your question, you might not go into the detail. So by prompting the user, do you want to ask this? Do you want to ask that? It's going to help them really to get into the weeds of all of the different parts of TXM. So let's go.

**Anthony De Gray Birch** (7:22): Yes, let's look at the card.

**George** (7:38): So one of the things is going to be showing the user what's going on behind the scenes. Because I think what a lot of some providers get wrong is you send a, you send a response and you could be sat there waiting for 20 seconds and nothing's popping up. But by understanding what the agent's doing, it helps to make it a bit more interactive. So here it's saying, would you like to issue it on the sandbox? So you can see. So that hints to one of the features that are added in there, is that the agent will work with the user to execute requests in the actual sandbox. And I think we'll go to another question for that one. So let's say a user wants to go through issuing their first card. Let's go.

**Anthony De Gray Birch** (8:20): Walk me through issuing my first card in the sandbox, please.

**Brett StClair** (8:30): Your typing is very much an indication of how little you type and how much you just talk to your machine now.

**George** (8:38): Ignore the spelling mistakes.

**Ian Johnson** (8:41): We were your boss, wasn't.

**George** (8:43): Yeah, no. So, yeah, what the agent's going to do now is it's going to work. Okay. This is a specific workflow and there's a specific way this needs to be done. So it's going to search for, kind of call them SOPs in its memory to make sure that it's consistent and repeatable so that anyone who speaks to the agent, they're going to get that, get that same experience. There might be some times with these workflows where there might be some ambiguity in the user's request. So say, for example, for this example could be a virtual card type, card type. And it's going to ask those questions to the user to make sure that it's not taking a stab in the dark and missing the mark. So what it's going to do now is it's going to be obviously searching through the documentation, it's going to be checking the health of some of the endpoints as well to make sure that it's not sending a request in the dark and getting an unknown error. Like I said, it's going to be looking up all of the specific endpoints, working out some mock requests that can be sent to the sandbox, but it's going to show the URLs that are going to be hit, it's going to show the payloads, it's going to show the responses. So as a developer, you can really start to get a hang of, to get a hang of what it's like to work. But with some of the TXM APIs, it's also going to ask for approval for certain actions. So say, for example, when hitting a sandbox, when the request comes up, it's going to say, would you like to approve this action? Would you not like to approve it? Like we said, you can see the request there. Appreciate that one went off the screen a bit quickly. But once the request has been sent through to the sandbox, you'll be able to see the response.

**Anthony De Gray Birch** (10:30): So if I click here, see the

**George** (10:33): request if you want to copy and paste it. If somebody's working with Postman, see the curl as well, just to allow for them to get full visibility. I think the next thing that would be good to say is the customer

**Anthony De Gray Birch** (10:52): has lost that card.

**George** (10:57): What do I do?

**Anthony De Gray Birch** (11:00): Including their Apple Pay.

**George** (11:08): Wait, was that every single word spelled correctly? I think there was only one or two backspaces as well. So for some of these requests, it might be chaining two or three together. So rather than doing do you want to approve this? Do you want to approve that? It's going to help the developer to understand, okay, this is, this is the typical sequence of actions. So maybe imagine on one endpoint within their software, they might need to chain two or three of these requests together. So what it's going to do now is it's going to say what you need to do and then after that what we'll do is we'll run that in the sandbox to see what that might look like. And like we said before, the pages are going to be up there. So while, while they've got the, some of the detail on the right hand side, they're able to scroll down here, see what's here, maybe click around. I want to explore this endpoint, this endpoint. So they've always got that truly digital assistant that's there side by side working with them. So navigating to the right page as well. Is there any, anything I've shown that I've gone a bit too quickly over or anything where people are like what does that mean? What does this mean? Are we all happy so far,

**Ian Johnson** (12:40): all good for me, George. I have seen you already.

**George** (12:45): Just waiting for it to send it

**Anthony De Gray Birch** (12:48): to the Sound. Important to add that

**Brett StClair** (12:50): the user journeys are not pre-designed or pre-programmed. This is agentic AI. It is understanding and best trying to apply based on what knowledge is sitting there and shape it based on who's actually enacting what are the process, what's being taken. So we have guardrails but we don't do what your traditional agent say from three, four years ago was about shaping user journeys. This is being built and driven by teams of agents in the background that are working out what the best experience should be.

**George** (13:29): So I think now let's ask it,

**Anthony De Gray Birch** (13:31): please can we do this in the sandbox.

**George** (13:38): So then now this is where it's going to look through the, the SOP for, for this specific workflow in the sandbox. Like I said before, going to be checking the, the health of the endpoints and this is the one where it's going to be multiple request chains together. So rather than having an approval for every step it's going to say these are, these are going to be the three operations that I'm going to do in this sequence. Would you like to have a look at all of the, all of the detail that goes into that do that bulk approval, then behind the scenes it's going to execute them in the sandbox. I think one thing that might be worth talking about as well is a lot of people are going to obviously be using the docs assistant but sometimes they might want to take it off into their own, into their own agent. Be it Claude, be it ChatGPT. So it's allowing them a safe, secure way in order to access, access this information, but making sure that it's getting a similar way that it would be into the Docs Assistant. So would be exposing an MCP server for agents like Claude or Chat GPT so that they can really deeply understand what TXN is about. So it's not going to maybe one web page which might or might not be about it. It's going to have exactly the same guides that the, that the Docs assistant has obviously just limited by the functionality that's within their assistant of choice. So same as before, be able to click in, See the, see all of the detail. And I think the, so say for example, some of the ways that I might be working is I might be having this conversation with the assistant. I might want some help when it comes to writing some of the code. Obviously not writing the whole code base for me, but little snippets that might be, might be useful in, in integrating with txn.

**Anthony De Gray Birch** (15:40): So let's say using this writes me some node code to run the lost card flow against the TXN API.

**George** (15:57): So it's going to write some of the code out obviously with the full context of, of the conversation so that it's not just writing a few snippets. And at this point, if it was my, me myself, what I might want to do is export this chat or export the code into my coding assistant of choice. So once the answer has come back, there's the option to either copy the whole response to the clipboard or download it as a markdown file or export to Claude as well. So download the file, put that, give that file to the coding agent and it's going to have not just everything that's in the chat, but also links to relevant pages as well. So if that coding agent or if that user wants to navigate to that specific web page, they can also we have on this page the option to open it in a specific LLM provider, LLM Providers agent. So say for example, with perplexity they click in here, it's going to paste in a message into the browser so that they can carry on the conversation if needed. Yeah, so at the moment that's the AI functionality that's in, in the Knowledge Hub. Is there any questions? Anything people would, would like to test out, anything that you're unsure of?

**Steven Kark** (17:28): This is the thing that, this is the thing that spoke focused specifically to the developers on the technical side and the, the kind of the control panel which is for users of the Systems people that are configuring a program or support agents or etc. This is not that. This is basically for people to talk to the API docs in an efficient way. Right. This is not the other one.

**Ian Johnson** (17:50): This is the first.

**George** (17:51): Yeah, correct.

**Ian Johnson** (17:52): This is the first thing that will go live, Steve. The control center will come after because you can't use that.

**Steven Kark** (17:59): So this, this console is effectively as we know this is. There's the business piece which as we sell and then there's the technical side. If someone's comfortable to work with us, they then unleash their technical people on the API API docs. This is a much more efficient way AI centric mechanism by which developers or technical people can interact with API docs in a seamless way. Right. This is not the, this is not the, the control panel or the. Whatever it is that we.

**Ian Johnson** (18:31): The next part that's coming later. I think one thing to point out is the way that it's been designed is to adhere to the kind of meeting people where they are. So some people might not, might want to read the documentation, Steve. Some people actually that we interviewed during the process said I'll just start coding and then if I have a problem I'll look at the docs. Some people will value the copilot so if they're unsure about something they'll ask the question. Others will do what George showed at the. Towards the end, which is I'm just going to copy these pages and put them into my AI coding thing and it's going to do it for me. What we've designed is to make sure that it doesn't matter how you want to work. You can work in the most efficient way with txn and we're not gone fully to the. Just the AI developers. We've been an understanding that people are working at different paces when it comes to AI and the whole thing is however you want to work. We're the right solution for you to do that. And this is the first thing that we will go live with when we go to market. Yeah.

**Steven Kark** (19:36): And how difficult will it be? So there's the APIs that we currently have now. I'm sure as the system evolves and more clients come on board and additional functionality which comes into. Into play. Is it a. How easy is it to add additional APIs into this thing without heavy lifting and heavy cost?

**George** (19:58): So, so in, in terms of how we've built the, let's call it the, the knowledge base and its understanding is it's not a statics thing. So say for example, with the guides and the documentation, we're pulling it directly from Umbraco, which is obviously the CMS. So we'll have a webhook set up so that when anything's published, anything, just.

**Ian Johnson** (20:22): Let me just explain that to the group because obviously you're talking about things that we know intimately. So Umbraco is the content management system that Mike puts all of the documentation on. So each time you release a new document, the AI tool has access to that new document. The same with the API references themselves. Each time something called the YAML is updated, that's what is being pulled down into the Knowledge Hub. So it's always up to date. So there is no rework for the Novo guys to do to add more feature functionality. It's just reading from other sources.

**Steven Kark** (21:00): Okay, so it's not too heavy lifting every time we publish a new API?

**Ian Johnson** (21:05): No, as far as I'm concerned, George. Right.

**Anthony De Gray Birch** (21:09): Just a quick question from my side. I mean, from an API perspective, there's quite a overlap between the Knowledge Hub, I'm assuming, and the console, you know, in the same API being used for both. From the AI perspective, will they be. Would there be a lot of rework or will a lot of the work already done from the Knowledge Hub just be used within the console as well? When it comes to.

**Ian Johnson** (21:33): So the Control center is somewhat different in the sense that it's less about reading documentation to come back with responses and to help guide people, and more about taking actual kind of action. There is guidance, George, within the Control center. And one of the. One of the key things is giving people guidance when they're about to change a parameter so that we can tell them what the impact of changing that parameter will be. If they ask in natural language, I want to create an expense management program, then it will basically populate a product already for them and ask them to go through and approve it. So it's a different experience, but it's the same.

**Anthony De Gray Birch** (22:22): Is most of that in the documentation behind the AI and not in necessary the AI tool, or is it actually within the setup? Meaning it's a different experience, it's different questions, it's different responses, but I'm assuming it's coming. The responses are coming more from the back end and from the documentation around it.

**George** (22:43): Yes. So it depends. So for the sake of the Knowledge Hub, one that's going to be grounded in everything, like the guides, the documentation, so that if a user asks a question, they get an answer, it's going to be very, very. It's not going to be exact, as in word for word. But it's, it's all going to be singing from the same hymn sheet and like we said, it's going to be dynamically updated so that if, if as soon as something is published or unpublished, it's not as if the agent's going to be for the next hour responding differently to what's said in the guides, it's always going to be up to date, it's always going to be consistent.

**Anthony De Gray Birch** (23:22): Yeah. So if the question is how do I stop a card or how do I block a card, or how do I reissue a new card on the Knowledge Hub, that's quite a technical question from an API perspective. From a console, it's actually a user perspective, how do I, on the console stop it? So it's the same question from an AI perspective, but it's actually how you retrieve the data to respond back to the question that differs.

**George** (23:46): Okay, so is it worth me quickly mentioning about how the, how it might work in the console?

**Anthony De Gray Birch** (23:54): Ian?

**Brett StClair** (23:55): Yeah.

**George** (23:57): So with the, with the console, what we effectively kind of create is a. So one of the key things in the console is permissions. So what users can do certain actions. So basically every single user obviously has their permission set set against them. So some might be able to issue new cards, some might not be able to. The agent's going to replicate that exactly. So if I, for example, have got all access and Brett got slightly more limited access, it's not as if because I'm speaking to the agent or Brett speaking to the agent, he's now suddenly able to do more things. So first of all, we're limiting the functionality. Also, the agent's aware of the current structure of the console as well. So there'd be two different experiences. The full agentic experience, which is the aim is anything a user could possibly want to do, they would be able to do through the agent, which we appreciate for a lot of people it's quite intimidating. I mean, myself, we've been in AI a decent amount of time. Going into a completely AI first environment is a bit difficult. So there's the co-pilot that sits along with that, which will navigate the user to different pages, will tell them what to do, but will also be able to take those actions for them. So certain things, like updating one tiny thing for a cardholder, there's times and places where it's going to guide the user to the page in the console and help them to make the action, it can also take the action for itself, but longer workflows which for human might take them half an hour, an hour with these long chain multi-step workflows where they're navigating across 10 or 20 different pages with a full agency experience, they're in one place, they go directly from thought to action with the agent. The components are rendered within the actual chat so they're not having to go to different pages. So they're getting a unique experience which I feel like a lot of consumers are kind of expecting now like when we've been speaking to people, that whole Claude experience of I've just got one chat pane, everything I want to see, everything I want, want to be able to do, I can do in this one interface. But the benefit is with the TXM platform that's being built is they've got every way of doing it the traditional way, the co-pilot way, but also the full agentic experience which I mean I don't think, correct me if I'm wrong and there's not anyone else in the market that currently offers that.

**Ian Johnson** (26:32): We haven't seen it.

**Anthony De Gray Birch** (26:34): George, just last question. I'm not a technical person, so please excuse if I'm missing it completely, but if the AI agent can actually act on behalf of the user, please block card 1, 2, 3, 4 and it can actually go and do that for me, does it? I mean obviously from the card program owners, do they federate access control or access to you and you. The AI actually understands the federated access to what is allowed and not allowed.

**George** (27:05): Yeah, so we, rather than. So as I said, all of the permissions are going to be replicated and the way in which the AI is going to access the API is through the control center back end which has obviously the, the limitations on okay, this user is id 04267 or what's. Whatever. It's not as if it's going to bypass that. We'll have two layers of protection. So first on the, let's call it the agent side will have some of those, those permissions built in so that the agent's not even going to be able to see the tool that might be able to block a card if the you. If the user's not got access. This won't happen. But let's imagine a world where it for some reason did have access to that tool. That request is then, then going to be passed to the control center back end which is going to completely block the request. What it's then going to do to the agent is give a piece of what in the error message is going to feed back the fact that this was an action that they weren't authorized to do. So it would then go to an alternative route. Might be you need to speak to Sally for approval. I'm going to create an approval request which is going to go, go to Sally so that she can approve this action in the same day in the same way that it would be if they weren't. If they weren't using any of the AI functionality at all.

**Ian Johnson** (28:30): So you said that in the control center on the, on the user roles and permissions that George might have a user role and set of permissions that says he never needs to ask anybody for permission to do something. He doesn't have to ask for approval. But others particularly thinking about a customer support team, Anthony where people are managing people's cars, putting them on, suspending them, asking for new cars. You might want those to be approved every time. Just to make sure that from a human perspective nobody's doing anything that they shouldn't be doing without somebody else giving it the okay.

**Anthony De Gray Birch** (29:07): Now I just wanted if the agent also, you know, read the federated access so that it knows what you can or can't do. Obviously it has to go through that layer.

**George** (29:19): Okay, yeah. Yes. And I think one, one thing to mention as well is there's. There's certain actions that when it's in the context of an agent executing them, you're always going to want to ask the user for approval. Be it so not requesting approval from Sally. Let's say it's deleting a card for that you might. The agent. We don't want it to be able to just take that action. We'd be. It will take that action, but only once the user's clicked a button to say I approve that you to delete this card.

**Anthony De Gray Birch** (29:53): Will it always be an approval button or could it be an instruction through AI?

**George** (29:58): Yeah, it could be both. It's just with, with certain like really sensitive actions by having that explicit clicking of a button one in for a user's perspective like I'm. I can be quite lazy sometimes. I don't want to type it out. I want to click a button and click approval.

**Anthony De Gray Birch** (30:17): Okay. And then the audit trail on the button I get. Because we, we have auto trail on every click you do. If it's an AI instruction and the action is taken, how do you retain audit trail?

**George** (30:28): So what, what what the agent when it takes and takes an action we'll call it. It's called a tool call. So what we will have is we'll have a trace of all of the tool calls that have been, have been executed, obviously redacting some of the sensitive data in the tracing. But we'll understand what actions have been taken, what came before, what came after, and for tx. And it acts as kind of like a training data set so that it's constantly being improved. So let's say we've noticed that one workflow is taking one minute when we really think that that's too long, too long of a period of time. And maybe it's. There's three or four redundant tool calls that it's making. So we've got the audit trail. We can maybe rework some of the tools so that it's not a static thing in that like these tools and these tools, they're never going to change. There's things that we can do to bucket certain tool calls together, make them execute in parallel so that that experience both behind the scenes and for the user on the screen is always constantly improving. And obviously in terms of an. For audit perspective, you, you understand everything that the agent said and everything that is done.

**Anthony De Gray Birch** (31:45): Okay, cool.

**Ian Johnson** (31:48): So we will set up some time to show you guys the control center before, before we need to put that live, I think George, I think we've got a pretty solid working version already or being focused on closing down the, not closing out the knowledge of. I think in the next few weeks we could show you guys the control center as well so you can experience what George is talking about. Again, it comes from the, from the general principle of meeting people how they want to work. If you just want to type something natural language with a, with an instruction, then you can do that. If you prefer to click around pages and find, you know, and use search buttons, that's entirely up to you. And if you want somebody to help you when you're doing any of it, then that's available at the side of the page for you constantly. So that's the general principle.

**Steven Kark** (32:42): Yeah. How do we, how do we explain this without getting it, you know, down and Dörte on the website, as far as some of the AI functionality is concerned with that A. Without showing everything? Because I suppose that would be a competitive issue. And at the same time giving Brett strokes as to what the AI overland functionality as that looks for the control panel, for the sandbox, for Knowledge hub and all of that stuff. So without giving enough detail to get users enthusiastic, but not so much as we give too much away up front.

**Ian Johnson** (33:21): I think the answer is not to tell people, but to show them. So I think little snippets of video content on the website. It's already something we've been talking to Bronwyth and Nicola about, so that you kind of take to your point, Steven Without fully opening the kimono, taking snippets of things that you think will give people a flavor of it, and then just having them posted as kind of little videos that they can watch and see what it would actually be like, particularly on the control center. On the Knowledge Hub, they will be able to do it themselves. On the Knowledge Hub. That's not to say that you shouldn't. Shouldn't still show people, but on the control center, where you only get to experience that once you're a client.

**Steven Kark** (34:04): Yeah.

**Ian Johnson** (34:05): Yeah, we definitely need the video content for that stuff, but that's the plan.

**Steven Kark** (34:10): I mean, it's all Greek to me, but looks quite good. You think we can sell anything?

**Ian Johnson** (34:14): I think.

**Anthony De Gray Birch** (34:15): I think we'll understand the console better than the Knowledge.

**Steven Kark** (34:22): Top card, I kind of understand. Or like a print card. This one is just. I saw more than three lines on the page and my head started spinning, so.

**Ian Johnson** (34:33): Well, I think maybe Village.

**Brett StClair** (34:35): Zane.

**Ian Johnson** (34:36): Marco.

**Steven Kark** (34:36): Yeah, I mean, exactly. All the propeller hits on the call. They kind of got it just because this went straight over my head.

**Ian Johnson** (34:43): Okay.

**Steven Kark** (34:45): Not you, Peter. You're not a propeller head. Only the rest of them. I'm sorry for. All right, cheers, everyone. Thank you. It looks great.

**Ian Johnson** (34:54): Okay, thank you.

**Steven Kark** (34:57): Thank you.

**Ian Johnson** (35:03): Is everybody left forgetting we've got an infrastructure conversation to do?

**Steven Kark** (35:08): It looks like a lot of people

**Brett StClair** (35:10): have said,

**Ian Johnson** (35:15): I saw a couple of people disappear. And I thought, yeah, that's okay. And then I was like, no, no, you should definitely not be legging it.

**Steven Kark** (35:23): Must I quickly get Shell back into the conversation?

**Ian Johnson** (35:27): I think that would be a good idea.

**Steven Kark** (35:29): Let me just go and ask him to quickly join again. Just give me a second.

**Ian Johnson** (35:39): Cheers, guys. Appreciate it.

**George** (35:43): No worries.

**Ian Johnson** (35:44): Pretty standard response from Steve after 30 seconds, it's like, okay, yeah, this looks. This looks good. I don't understand any of it.

**George** (35:59): Don't know how to. Had all the. The three different videos as well lined up, but fortunately we didn't need them.

**Steven Kark** (36:12): You better prepare than the other versions where nothing worked.

**Brett StClair** (36:19): All I heard was, Hasan, you rubbish.

**Steven Kark** (36:24): Okay. I gave Hasan our honest feedback already. I said, you need to grow some balls and you need to learn it.

**George** (36:32): Yeah, yeah.

**Steven Kark** (36:34): I mean, it was quite, like, improvised, so that's why I didn't really, you

**Ian Johnson** (36:40): know, you had no prep.

**Steven Kark** (36:43): Yeah, it's like. I mean, because it's like there's like an entire script now, like, do this, then do that and do this. You know, a lot more organized for this one.

**Brett StClair** (36:54): But what no one saw was all the heavy lift you did for George to get that ready.

**Steven Kark** (37:00): But it's always like that, right? The person who's in front, who shines, not the workers at the back.

**George** (37:09): Oh, funny.

**Ian Johnson** (37:18): Don't be shitting me, right? I'm doing a webinar with PwC and Super Ultra. I think you might have met Super Ultra. They were the design guys.

**Brett StClair** (37:27): Yeah, they were really good.

**Ian Johnson** (37:29): Listen, this is. This is the most tightly controlled webinar in the history of the world, including. I just got an email for them with the explanation of what business casual is from a dress code perspective. I'm like, you've got. Listen, now that you sent me that, I'm going to turn up in a T-shirt. Seriously, I'm like, T-shirt time. The best thing is. The best thing is it's a. It's a thing about using AI for product design. And it's like what you're worried about is that we all turn up looking like we never seen AI before in our entire lives. So awesome. I think of something suitably annoying to wear because they can't do anything about it. It'd be too late. I might put the business casual on for the, for the, the prep session from 8 till 9 and then quickly whip it off.

**Steven Kark** (38:26): Yeah, just.

**George** (38:27): Just have like the, the, the trousers and the top that you could just pull off and then. And then underneath is the, the thing that Brett wears and just walk out on stage.

**Steven Kark** (38:37): Sorry, guys. Charles, we just quickly went for a. For a little walk, but he's, he will be joining us just now.

**Brett StClair** (38:52): So I'm just thinking. I've once gone to the meeting where I actually thought I'd dress up. I put on a shirt and a jacket and then I was critiqued that I'm meant to be the digital guy. What on earth am I coming in with a jacket and not a T-shirt? And that was confusing.

**Ian Johnson** (39:10): We used to have a lot of fun when we were at Marketer in particular when people used supplies used to turn up or invested. All kind of suited and booted and it was just good. What, what have you come out like? Literally, people just shorts, flip flops, whatever. Yeah, those were the days. Those are the days. Okay, who is. Who's leading this one, by the way? Everybody looks around. Have we submitted the infrastructure requirements document to dt? Yeah, checking.

**George** (39:50): Not sure. I think so.

**Steven Kark** (39:53): Yeah. I saw a male a while ago. I'm not sure it was a document.

**Ian Johnson** (40:01): If it was a mat, was it a mail mic or a docket?

**Anthony De Gray Birch** (40:03): I'm not sure it's mail with two documents on. I believe it was sent to Jack.

**Steven Kark** (40:11): No, it's been shit, Mike.

**Ian Johnson** (40:14): Okay, so what one's listed libraries and

**George** (40:16): stuff and one's list of services in

**Brett StClair** (40:19): Azure that we think we could use.

**Ian Johnson** (40:22): Okay, so the objective of the meeting, we won't obviously resolve everything in 20 minutes, but we want the knowledge hub AI capability to be part of the go-to-market launch. It's such a key part of our messaging, etc. And what we're trying to achieve from a functionality perspective. Correct me if I'm wrong, guys, but from a Novo point of view, everything is built. Obviously, we know that there are more API endpoints for YAML being updated, etc. Not sure, Mike, if there's more to be done on guides or that's just an evolution. But ultimately, from a functionality perspective, we are good to go. But obviously, we need a place to host this capability. Hence, I'm sending across what the Novo guys think would be needed in an Azure environment and then setting up this call so we can start to look at making it a reality. Now, I should be clear that when we talk about the AI code, that AI code is going to be supported by Novo until such time that TXN decides to take it over. Which would mean us employing our own AI engineers and also having a period of handover between Novo and those guys so we could take ownership of it. What would, what this conversation is not about is putting code into DT and asking you guys to support it. This is literally about the infrastructure and the hosting.

**Steven Kark** (42:26): Okay, yeah, so I'm just trying to, I know there was mail sent, but I'm not sure. I may not have been part of the distribution list. Maybe I'm getting so many mails, so I don't know if these details that obviously we just need to run through it. What does it mean from a hosting perspective, then? But if that's outlined in the document, I don't know. Jacques, if you share. Yes. So the team started looking at that. Okay, cool. Yeah, they've started analyzing and reviewing and putting the ideas together. So I don't think it was expected to give an update or a view in the session. Apologies if that was misread, but the team is aware, they did look at the documents and do have feedback on a high level, but I don't think it's ready for this decision specifically. You know, maybe from my side, I think what we can do is because I just quickly scanned the documents. I mean, there's nothing that there's really a deal-breaker in it. So I think we need to just put it into our design and send you a bit of a design in terms of what we can do. I, I think the only thing is that we just have to optimize the cost slightly. But, but I'll put it also in the cost, just an infrastructure cost model for you, Ian, that we can just show what, what it's going to be. Additional cost going to be perfect.

**Ian Johnson** (44:13): Marco.

**Steven Kark** (44:16): So I've started looking at the proposal as well as the AI tech stack. I do have a question though. If I understand it correctly, behind the scenes, it's going to run some sort of Gemini consumption as well, is that correct?

**George** (44:32): Yeah. So in terms of the LLM of choice, there's a lot of flexibility at the moment. When we've been testing, we have been using Gemini. It's been directly from the Gemini API. So Google has two different versions, Vertex AI and then the Gemini API. But there's also the ability to, within the Azure stack, which to me sounds ridiculous, but you can actually consume a Gemini model via Azure using Azure Databricks. If that's an issue, then so a note on the Azure Databricks, it's not deploying something, it's a per-token model. But also there's obviously the AI Foundry within Azure. So if we needed to switch over to OpenAI models, that's not too much of an issue, or Anthropic models as well. One of the things we've built in there as well is the fallback capability. So let's say there's a region that's down or one of the providers is down and let's say OpenAI models are currently not being served. It's going to fall back to different models as well to make sure that there's, there's, there's always the AI functionality available. Okay, 100%.

**Steven Kark** (45:53): The reason I'm asking is I'm trying to figure out if that should become part of the infrastructure costs. So it's a definite yes, then?

**Brett StClair** (46:03): Yes.

**Steven Kark** (46:04): Okay, cool, thanks.

**Brett StClair** (46:06): Yeah, I think we've sent in just some estimates and pricing, so factor that in across a couple of model providers and you really want it in your ecosystem and lock it down. So it's important to, to kind of consider those options and get it through the API stack and make sure we've got full control of it.

**Anthony De Gray Birch** (46:35): Yes.

**Ian Johnson** (46:35): Hi.

**Anthony De Gray Birch** (46:36): Hi everybody. Just a couple of technical questions. You, I understand that you're going to use Foundry, which is great. Question on my side is, are you only using the indexing portion from the Azure perspective, using the, for the documentation or using pipelines and feeding that straight into the context window? And how do you limit the data that's actually passing into the large language models? How do you separate that? How do you split that out? Do you use something that masks it beforehand, afterward, or within the pipeline? Just two or three questions.

**Ian Johnson** (47:12): Sorry, man.

**George** (47:14): So in terms of the, the how the agent gets its, gets its context, we're not, we're not indexing anything, we're not using a vector database. What we do is when the, when, when the agent starts up, what it's going to do is speak to Umbraco and build a, I say local, it's not local, but a local representation for the agent to be able to execute certain commands to search through the documentation. Because we found in our testing, the best method of search for let's call it medium, small to medium sized data sets that are unstructured is usually the tools that they've been trained on, which are say, read, glob, and grep. Obviously, exposing some of those tools can be potentially dangerous, but we find fine-tuned it so that we make sure that it's never going to run anything destructive. It's completely, completely isolated and has only got access to, to those files. And in terms of.

**Anthony De Gray Birch** (48:18): Sorry, no, no, it's perfectly fine. I'd like to have a chat with you about GREP, because we all understand that it takes everything out of the context. We know it takes a hell of a lot of tokens, but that's not the discussion today. So I think that gives me clarity. Do you use OK, if for that to structure that locally?

**George** (48:38): No, I don't think so.

**Anthony De Gray Birch** (48:39): Okay.

**George** (48:39): I think I might, I might have to, might have to speak to Hasan on that one just to double-check, but what we can do is, yeah, we can have a look and if there's, if there's any questions that we've not might not been able to, to answer on this call, feel free to send them over and then, then we'll get back to you on them.

**Anthony De Gray Birch** (48:55): Ah, perfect. I've just got it. I've got a small list because I need to understand the dimensions that you're using as well. You're not using vector databases, which is great. So you don't have that overhead. So we're not double-storing, which in the first case saves some money. There's still transfer costs, there's token costs, there's conversion costs, and I need to understand that a bit better because indexing could be out of sync. If you're using grep, you're going to use a lot of tokens. So I've got a couple of questions, but it's either day, so it

**George** (49:22): depends on what you use.

**Brett StClair** (49:23): Yeah, we also, we continuously testing like where's that pricing landing versus an architecture that does so. Right questions, Willie. Right questions.

**Anthony De Gray Birch** (49:33): Good job. So I'll get back to you guys. I'll just put it in an email. It's going to be five bullet points. I think it would answer my questions.

**George** (49:40): Perfect.

**Ian Johnson** (49:41): Awesome. Any more? Okay, so we need to answer your questions really as a precursor to really being able to look at the design and the, and the costing. Is that right?

**Anthony De Gray Birch** (50:01): Yeah. So that would kind of dictate to me. Exactly. I mean, I had a brief look at the expected expenses and that would give me an indication of where that expense actually lies. Because if you spin up in different regions, near failover, there's a cost involved from an Azure perspective. But they charge on multiple levels, so they could charge. I mean, we've eliminated embedding and storage, but they charge on indexing in different regions, they charge on token usage, in usage, they charge on storage. And we are storing something, we are using Foundry, so there's a light and costing board for Foundry. So and if I put all of that together, that would answer the question. I can get back to the team and make my recommendations.

**Ian Johnson** (50:47): Cool. So if you can send those across that would be as soon as possible. But he will get them answered quickly as Olivier. And then I guess we just need to, it would be good to get a sense of the actual deployment of the capability once we're settled on a design and the associated costing. Is how long it would actually take to deploy? I think it's, that's a separate conversation as to how that happens and the timing. But obviously Pete, what we're trying to get to, as I say, is this AI being available for the knowledge hub when we go to market on what's currently planned to be the 17th of November, which is two weeks away. Deafening silence. Understandably, this is what this is, this is the challenge. So if you get the questions over, we'll get them answered quickly, and then if we, I'm sure we will need follow-up calls. Probably not for myself and maybe Pete, I'm not sure the value that we can necessarily add to the conversation when it comes to technical stuff. But you know, definitely Mike, the Novo guys, Vinny Shaw to just figure this thing out.

**Anthony De Gray Birch** (52:12): Yeah, it's fun. I think I think most of us have rolled out in Azure before. It's not going to be the complication. So I'm not going to speak on the rest of the team's behalf. So I'm just going to stick to the AI portion.

**Ian Johnson** (52:25): Okay.

**Anthony De Gray Birch** (52:25): That's all I wanted to say.

**Ian Johnson** (52:28): Cool. Well, in that case, I will let Jacques, Pete, and Shawl finish the however many hours of marathon conversations I've had with TXN today. I know some of you have only been on single calls, but these guys have done three or four hours so far. You can now go and get yourself a nice glass of South African red wine or whatever it is you think to get over the TXN days. But we'll get back to you with the answers. As soon as you get the questions, we'll get them back to you very quickly. Okay, cool, cool.

**Steven Kark** (53:02): Thank you. Thank you. Thanks.

**Ian Johnson** (53:05): Thanks a lot.

**George** (53:06): Lovely to meet you.

**Steven Kark** (53:07): All right. Same, right?
