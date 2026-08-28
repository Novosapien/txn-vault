---
date: 2026-08-26
type: general
description: "Transcript and analysis of the 2026-08-26 Stackworkz session: the permission framework, the approval-routing fork, deployment into DT, and the code-sharing options"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-access-layer]]"
  - "[[architecture]]"
  - "[[integrations]]"
status: extracted
extracted-to:
  - "[[agent-access-layer]]"
  - "[[mcp-server]]"
  - "[[architecture]]"
  - "[[integrations]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Stackworkz agent interface demonstration (2026-08-26)

> **Source:** Gemini transcript, arrived 28 August. Attendees: Brett StClair, George Westbrook, Max Kingaby (Novosapien); Michael Moores, Dorte Dye (TXN); **Armand Pretorius** and **Ruan Sunkel** (Stackworkz). Duration 00:47:19.
> **Parties:** Novosapien, TXN and **Stackworkz**. Prior ways-of-working session: [[29-05-2026-stackworkz-meeting]].
> **Delivery:** [[delivery]]

> [!note] Upgraded 28-08 from a second-hand note to a full extraction
> This record was first written on 27 August from Brett's account, and said plainly that **no transcript was captured**, so the detail was deliberately thin and four things were listed as undecided. The transcript has since arrived and is attached below. Three of those four are now answered, and the session turns out to carry the sharpest architectural finding of the week. The original note's judgement was right: it mattered more than it looked.

## Why this session mattered

The pilot has always run on Novosapien's own surface. `txn-console-react` is a full React build of the Control Center that Novosapien produced so the agentic experiment had something real to drive. **Stackworkz builds the production Console and the Developer Portal**, so at some point the agentic experience has to live inside their build rather than ours.

Every previous plan treated the wire-in as a **Direct Transact problem**. This session establishes that it is also a **Stackworkz problem**, and gives it a mechanism for the first time.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| **The permission model belongs to Stackworkz, and this closes [[open-questions]] #71.** Michael: *"One thing Stackworkz are building for us is the user and permission framework. So what the user sees in the UI and what they can do... They will be governing the user access. So this is what the agent will be looking at and what you'll be sort of integrating with."* The register raised #71 on 25-08 because Michael described standing up the permission model as his action while Pilot Order deliverable 2 names it as Novosapien's. **They are two different things, as suspected**: Stackworkz builds the Console permission framework, and the agent scopes itself against it | [[open-questions]] #71, [[agent-access-layer]] | **Register row answered** |
| **The permission framework in detail**, so the agent can be designed against it. A backend API with roles and complex permissions. **Four role templates**: TXN, bin sponsor, client self-issuing, and client with a programme manager. **TXN governs the ceiling**, the absolute maximum any role can do, with no customisation for TXN or bin sponsor roles. **Clients build their own roles** beneath that ceiling, with standard ones provided for smaller clients who want defaults and full construction for enterprise clients. **User overrides** sit on top, so a sales lead can hold one permission more than their team. Michael is sending Brett the framework document | [[agent-access-layer]], [[permission-scoping]] | Update banner. Design input for the deferred permission work |
| **The MCP server may need its own permission model, separate from the Console's.** Michael: *"I know we're talking about for now the agent in the console, but obviously we discussed MCP and stuff like that. I think we maybe a separate model more aligned to maybe the API sort of systems we discussed, and obviously this will cover off the user permissions basically"* | [[mcp-server]], [[open-questions]] #73 | **New register row** |
| **The approval-routing fork, and it is the most consequential finding of the week.** Ruan Sunkel (Stackworkz) asked where the MCP server sits and what it talks to. His point: the Control Center *"is effectively just a proxy to the server. So we add authorization, extra user authorization which can include agent authorization as well."* Therefore *"if the MCP server talks directly to DT, then yeah, good luck with the approvals. I don't know that that's going to work."* **Michael confirmed the constraint: *"this approval part is console specific. DT aren't building any approval layer or anything like that."*** The emerging shape is a split between **system-to-system** traffic, agent to agent, which can hit DT endpoints directly, and **user-to-system** traffic, which must route through the Console so approvals are enforced | [[agent-access-layer]], [[mcp-server]], [[a2a-endpoint]], [[open-questions]] #74 | **New register row.** Not previously in the vault in any form |
| **Two MCP servers confirmed as the shape.** One the agent uses from inside the app, holding the user's tokens; one that developers and clients connect to directly, for example from their own Claude. Same access controls intended, different authentication, OAuth or an API key, *"whatever's best and works with DT as well"* | [[mcp-server]], [[a2a-endpoint]] | Update banner. Corroborates the A2A split |
| **The agent may be allowed to do things a user cannot.** Michael, on how the agent meets Stackworkz's approval queue: *"we may extend that to say a user can't do this without approval but an agent can."* Also open: whether an agent's own approvals go into that same queue for a human, or bypass it. George's variant: a user approves an action, and a second tier routes an approval into someone else's inbox, with the chat resuming statefully once granted | [[approval-queue-integration]], [[open-questions]] #74 | Folded into the new row |
| **Deployment goes into Direct Transact's environment, not Stackworkz's.** Brett asked whether Novosapien would deploy into Stackworkz's Azure; Michael: *"will deploy into DT's. So yes, it's all the same."* The shape: **APIs are instance-per-client**, while **knowledge hub, console and AI sit as one central scalable layer**, and *"the client won't get their own layer."* Michael sending the latest confirmed architecture | [[architecture]], [[open-questions]] #48, #70 | **Architecture decision recorded.** Partially answers the multi-tenancy question |
| **Code sharing: two options on the table, and the codebase is being handed over now.** George offered either Novosapien working inside Stackworkz's repository on isolated branches with Stackworkz reviewing the pull requests, or handing the codebase over entirely for Stackworkz to absorb. Ruan could not answer without seeing the generated components and knowing where the MCP server lives, so **a smaller technical session was agreed, ad hoc rather than diarised**. George is sending the codebase immediately; Michael approved: *"I'm very happy between yourselves... I don't think I need to be involved in that per se"* | [[integrations]], [[delivery]] | Update block. Closes three of the four unknowns in the original note |
| **Stackworkz's release path, which the two cadences have to reconcile with.** Own repository, own dev environment, link sent to Michael to check, then pushed to DT for staging and production. Novosapien deploys on push to `main`. Ruan: *"on our side we're 100% flexible"* | [[integrations]] | Update block |
| **How generative UI actually renders, explained to the partner.** The agent does not generate component code, which George named as *"a potential security nightmare"*. It calls a tool, builds the payload, and passes the **component name plus its data**, so the Console imports its own pre-built component. This means **the agent can use exactly the same components as the Console**, with small changes for dynamism | [[generative-ui-rendering]], [[open-questions]] #35 | Update banner. Concrete answer to the component-library handle |
| **The Novosapien stack was disclosed to Stackworkz, with an offer to rebuild it.** AG-UI from CopilotKit, headless, manages the agent-to-UI connection; **LangChain deep agents** run the agent itself, fully isolated; deployed on **Cloud Run in a single Docker container**. George: *"just point us in the right direction and we can rebuild it all. It's fine, it's not an issue"* | [[architecture]], [[integrations]] | Note added |
| **The Super Ultra prototype we hold is the final one.** Michael confirmed no further work is being done on it. The only possible discrepancy is Figma mock-ups that came after, which he will send | [[open-questions]] #35, [[delivery]] | Register row updated |
| **The data lake structure went to DT on 25 August**, with AI access explicitly considered. A European regional data lake with rollup tables the console pulls from as-is, plus a layer for AI access. Michael is pushing DT for a presentation to both Novosapien and Stackworkz, and is still waiting on DT's finalised architecture. Open considerations he named: hot versus cold data, and *"a lot of data floating around from AI agents, your system, what you're storing, DT's pure code sitting separate to TXN's code, and also what TXN is storing"* | [[architecture]], [[open-questions]] #69 | Register row updated |
| **Stackworkz are being given access to TXN's vault.** Michael: *"we're happy for them to have access to that as well, so you can see how we're building the AI"* | [[internal-ops-agents]] | Note added |
| **Michael will clear everything he owes before he goes.** *"I'm here till Wednesday, so I can coordinate anything else between the two of you and I'll get all of the stuff that I owe everybody before I go on Wednesday."* Away 3 September, back the 15th, and contactable while away: *"if there's anything you need while I'm away, fire it across"* | [[delivery]], [[open-questions]] #50 | Corroborates the dates |
| Stackworkz's stated posture for the session, from Ruan: *"this process now is not to make decisions, just to understand what it looks like so we can help with decisions later"* | n/a | Context, sets expectations for the follow-up |
| Michael's crossover list: he will identify the interjection points between the two builds and circulate them, naming reporting and the agent inbox as specific pages that have to merge cleanly | [[integrations]] | Note added |

---

## Transcript

Aug 26, 2026

## **Stackworx \- Novosapien update \- Transcript**

### **00:00:03**

**Max Kingaby:** Nice.

**Armand Pretorius:** How are you?

**Max Kingaby:** Good. How are you

**Armand Pretorius:** Good,

**Brett StClair:** Hello everyone.

**Max Kingaby:** both?

**Armand Pretorius:** thanks.

**Ruan Sunkel:** How's it?

**Brett StClair:** How you guys?

**Ruan Sunkel:** Good. How are

**Brett StClair:** Good man. I'm the only South African this side.

**Ruan Sunkel:** you?

**Brett StClair:** So the rest of the problems I'm sorry about that.

**Max Kingaby:** You can't call yourself a suffer, you half English boy.

**Brett StClair:** Just my English has got my accent's gotten a bit softer. I will talk more South African. Oh, four guests waiting. I bet all four guests are It is. Let's see if we can have more of There we go.

**Max Kingaby:** Yeah,

**Brett StClair:** Did you let everyone or did you kill it, Max?

**Dorte Dye:** You did it again, Brett.

**Brett StClair:** I promise you it wasn't me.

**Dorte Dye:** She hates my Fathom. Yes,

**Brett StClair:** That was Max this time.

**Dorte Dye:** Max. You're not passing probation at that rate.

**Brett StClair:** Resubmit.

**Max Kingaby:** All right.

### **00:01:15**

**Dorte Dye:** Let me try again.

**Max Kingaby:** I'm so used to kicking George. It's just natural habit now.

**Brett StClair:** Um, and it is transcribing. So,

**Ruan Sunkel:** Thanks.

**Brett StClair:** you should get a copy of it if if if you don't want to resubmit, but you're also welcome to resubmit. Um, we waiting for George.

**Armand Pretorius:** Good

**Brett StClair:** He he promises me he's one minute away.

**Armand Pretorius:** job.

**Brett StClair:** I assume he's coming up the lifts. Um, is he there yet? No,

**Max Kingaby:** Yeah,

**Brett StClair:** he's probably coming up.

**Max Kingaby:** being said

**Brett StClair:** Um,

**Max Kingaby:** that

**Brett StClair:** now don't touch it, Max. I'm going to admit entry data. Yours has decided no, it's not going to join. So,

**Dorte Dye:** It's

**Brett StClair:** question Armand Ruan,

**Dorte Dye:** night.

**Brett StClair:** how do you enjoy merged audio? Isn't that just the crappst invention in the world?

**Armand Pretorius:** It is

**Brett StClair:** Oh, do you does it work for you

**Ruan Sunkel:** It works perfectly.

**Brett StClair:** guys?

**Ruan Sunkel:** It's amazing.

### **00:02:16**

**Ruan Sunkel:** Yeah, it it works perfect when we're in the

**Armand Pretorius:** the same room. We we have had challenges where we're all in the office joining the same meeting but no one can hear each other. Then no one can hear each other. That's happened.

**Brett StClair:** Yes.

**Armand Pretorius:** Yeah, that has definitely happened. But what about this?

**Ruan Sunkel:** Yeah.

**Armand Pretorius:** Yeah.

**Ruan Sunkel:** I usually just

**Armand Pretorius:** Put my earphones in and and like Yeah.

**Ruan Sunkel:** immediately

**Armand Pretorius:** Unmerge.

**Brett StClair:** I walk out.

**Armand Pretorius:** Yes.

**Ruan Sunkel:** Amazing. If it doesn't work, it's horrible. Yes. Yeah. Yeah. Exactly. That's Yeah. Exactly.

**Brett StClair:** I see it works well, right? When you got so both your computers are on and it's picking up and you don't have your headsets. Okay, so that's what it's designed for.

**Armand Pretorius:** Yeah.

**Brett StClair:** So when when there's all the headsets and it just goes

**Armand Pretorius:** So,

**Ruan Sunkel:** Yeah, But

**Armand Pretorius:** I had to like the the our speakers are just like slightly out of sync.

### **00:03:01**

**Brett StClair:** ballistic.

**Armand Pretorius:** So, we're like so I had to like turn my volume off now. Um, which that's so you

**Ruan Sunkel:** Let's see.

**Armand Pretorius:** can

**Ruan Sunkel:** It's probably There we

**Brett StClair:** Do you reckon it's going to work? I find it fascinating to Is it working?

**Ruan Sunkel:** go.

**Brett StClair:** Okay.

**Armand Pretorius:** Yeah.

**Ruan Sunkel:** Perfect.

**Brett StClair:** Wait, wait. Is it Is it working?

**Armand Pretorius:** Yeah.

**Ruan Sunkel:** Yes. Yes.

**Brett StClair:** working.

**Ruan Sunkel:** There we go.

**Max Kingaby:** Maybe we got the cheap plan,

**Brett StClair:** Yeah, we're on the Google startup

**Max Kingaby:** bro.

**Brett StClair:** license. Um, okay, we might as well get cracking. Uh, George literally should be here in the next couple of minutes. I can just picture him running. He's on his line bike, I think. Uh, hight tailing it. the most of the team on the engineering side only gets in at 11:00 cuz they're all grafting till 1 2 in the morning. Um so apologies for that. So um Mike, do you want to run this and how we should orchestrate and get to know each other and is that the better way to do it?

### **00:04:24**

**Max Kingaby:** It's

**Brett StClair:** It's your guys audio

**Max Kingaby:** me.

**Michael Moores:** Sorry, I keep muting myself. Yeah,

**Brett StClair:** version.

**Michael Moores:** I think if I if I go through the background obviously and then probably if you can show what you guys have done from the AI side. Um then Ruan maybe some updates on on your console work and and the backgrounds there in terms of the technologies used. The aim of today obviously is just to show you what we've been working on with um Brett and the team. They've taken the existing uh prototype from um Super Ultra using that as a just a quick reference for now. So we can actually build those screens. Obviously there's going to be some sort of realignment as you build the screens. We'll make sure the components built over here will also look the same as well and then look at how we integrate that with yourselves obviously. So very early on at the moment focusing purely on right now the agent chat bots. That's the main bit.

### **00:05:17**

**Michael Moores:** But um it's yes working quite nicely. A lot of um stuff going through already. You'll see a lot of similarities to the prototype already. And then obviously the aim of this is to make sure we're not sort of stepping on any toes. Everything that you're building will work together as well. So I think that from my side that's where we can start. Um and I don't know if Brett would it be George demoing from your

**Brett StClair:** Yeah. So,

**Michael Moores:** side?

**Brett StClair:** George will do the demo.

**Max Kingaby:** I was just literally just got here.

**Brett StClair:** Um, he'll do the demo. And I'm just thinking about um, we're not we're not going to be plugging into any APIs from your guys site, right? Are we? we just consume DT at the moment.

**Michael Moores:** Is that good?

**Brett StClair:** So, I'm just thinking of like just it's probably a good point just to chat about timings and make sure that we're lined up that we're not overshooting. You guys not overshooting.

### **00:06:07**

**Brett StClair:** We try sync as best as

**Michael Moores:** Yeah. Yeah. So, it's probably worth sort of digging into that. So,

**Brett StClair:** possible.

**Michael Moores:** obviously DT APIs exist and you're both sort of building into them. One thing um Startworks are building for us is the user and permission framework. So, what the user sees in the UI and what they can do. So I think obviously we've been discussing Brett about access to the the MCP the agents and stuff like that.

**Brett StClair:** Yeah.

**Michael Moores:** They will be governing the user access. So this is what the agent will be looking at and what you'll be sort of integrating with. So got a pretty good idea with them.

**George Westbrook:** Morning

**Michael Moores:** We're just going through the permissions for the initial build and stuff like that. But it's a very sort of complex permission model that every function we release basically will will be there.

**George Westbrook:** everyone. Sorry. Sorry for being late.

**Armand Pretorius:** memories.

**Michael Moores:** There

**George Westbrook:** Sorry.

### **00:06:56**

**Armand Pretorius:** All

**Michael Moores:** is.

**Brett StClair:** I guess that's the only place I can also think of where we are going to integrate there and that'll work really nicely.

**Armand Pretorius:** right.

**Brett StClair:** So, if we cover that off as well today, that would be

**Michael Moores:** Yeah. And obviously there's, you know, DT is progressing. Um, our hope is that when you get there,

**Brett StClair:** awesome.

**Michael Moores:** obviously I know Brett, you're working with the current version of the APIs right now. I can adapt quite quickly. the console side, we've per purposely pushed that back a bit so we get more confirmation and more confirmed structure of those APIs before we start integrating the console into it. So obviously Ran and team have built the knowledge hub. So they're familiar with the style. We're just trying to finalize that specifically with the UAT testing trying to get a few signed off before we start building those screens. So what the Starworks team are doing right now is the core application the screens that you see the user permission model and getting that framework sort of built so that when we do have a bit more confirmed from DT we can go ahead and start building that.

### **00:07:50**

**Michael Moores:** So that's a sort of split right now. Obviously we're focused on the user permissions right now. We've got a good idea from TXN obviously Ruan and Armand are going through the that now and you a few responses on that anyway and then we're sort of building that framework out. The idea of the framework is that it's a backend API. It has very complex sort of permissions, roles. The problem we've got with the console and and the agent probably is that we have many user types working in the same space. So TXN which we want very governed. So production support can only do what they can do and that's something that we're going to govern. Obviously we don't want sort of customization or flexibility in that. very similar to bin sponsors that they are external but we are deciding from TXN what they will have access to there's no customization you know we're going to set up very specific roles and they will get given a role for that so that's a sort of govern side obviously we support clients as well with very different business strategies so what we have done is this sense of a role template so each of those I've just mentioned TXM bin sponsor and and client there's two version the client sort of if they're selfissuing which means they're basically the bin sponsor themselves or if they're a program manager which means they do have also a

### **00:09:04**

**Michael Moores:** bin sponsor. So the sort of accesses and what you'll do will change based on that sort of model. So essentially we have four what we call ro templates where TXM will govern the absolute maximum you can do um basically so that's the sort of the ceiling. Then for our clients we have the ability to create their own roles basically. So we will set a few standard ones. You customers, customer customer support, operations, those sort of things that we will help them. The reason we do that is obviously some smaller clients who just want what do you normally give out? Obviously that covers that where some of the more enterprise customers will have I have a very specific need and I would like to build a roles myself. So that covers both of those size off as well. So they can build up ROS and obviously having a RO means you don't have to make a hundred user changes. So you can just make one RO change and that'll be easy as well. And we also do have a final part which like user overrides.

### **00:09:57**

**Michael Moores:** So let's say you have a sales team that does you know X things but you want your sales team just have one more permission basically. So that's sort of covering that off where a sales team lead could actually have a little bit more access um than it team basically. So that's a sort of broad thing. I will send you Brett the framework document that we've sent to Statworks for this so you get a good idea of what we're building. Obviously, it's not confirmed yet until we work through that with Stack Works, but you'll give you an idea of where we're coming from in everything we're trying to support from that. And obviously, I know we're talking about for now the agent in the console, but obviously we discussed MCP and stuff like that. I think we maybe a separate model more aligned to maybe um you know the API sort of systems we discussed and obviously this will cover off the user permissions basically. So, I'll send that all across to you. That's where we are at very high level.

### **00:10:52**

**Michael Moores:** Uh now I don't know George if you want to put potentially share with Starworks what you've been building and just a short short demo so you can see that answers all other

**Brett StClair:** Yeah,

**George Westbrook:** Let me

**Brett StClair:** one very quick just um infrastructure.

**Michael Moores:** questions

**George Westbrook:** in.

**Brett StClair:** Um so at the moment we deploying into our own environments. We're going to want to deploy into Stackworx um as your environment, right?

**Michael Moores:** will deploy into DTS. So yes,

**Brett StClair:** going to go to

**Michael Moores:** it's all the same. Yeah. So I will dig out the again it's still moving but the the most the latest confirm

**Brett StClair:** det.

**Michael Moores:** architecture which has the APIs sitting in one one environment and then separate services we've got AI um you know knowledge hub console all that sort of set separately sat. So of the APIs will be sort of instance per client whereas these three we're talking about knowledge hub console and the AI stuff will be sort of one central layer. So the client won't get their own layer for example.

### **00:11:49**

**Michael Moores:** This will be sort of scalable central layers which DT have already sort of sectioned off at a very high level where that would sit in the ecosystem. So you will be in the same environment. ironment has you know everything you need to connect to basically is the right now. Um so let me send that across to you as well. So you've got that current thinking. I don't think it's going to change much but just iron out more of the API side. Obviously what's under all we've done is sort of the ecosystem where this sits we haven't dug down into in the individual architecture for each of those components yet and that's something we can get on to yourselves and as we build the console out. Um but that's a sort of the hierarchy that we have right now. I'll send them both over to you after this call.

**Brett StClair:** Brilliant.

**Michael Moores:** You've got that as

**Brett StClair:** Thank you, George.

**George Westbrook:** Right. Let me share my

**Michael Moores:** well.

**George Westbrook:** screen.

### **00:12:43**

**George Westbrook:** Can everyone see this? There we go.

**Ruan Sunkel:** This

**George Westbrook:** So this this is kind of a a replica of of the console at the moment. I I'm not sure if this is the most upto-ate prototype. So there might be a few things that are different. I think it might be worth us at some point pulling up the prototype that you guys are working from just to make sure it's the same as ours. Um but this is what we're calling like the the full agentic experience. So kind of that claude like experience where users can take most of the actions that they would want to do in the console um but in a chat interface. So very free um I think first one let's say the suspender card. So please can you sus you go I can't remember his sent. So, what we what we have behind the scenes is just a singular singular agent for the time being. Um, let me make sure this is all running. No, it's not.

### **00:14:01**

**Brett StClair:** Looks like Hitznut Germany is down again.

**Armand Pretorius:** We hope there's

**Ruan Sunkel:** Yeah.

**Armand Pretorius:** Yeah,

**Ruan Sunkel:** Thank you.

**George Westbrook:** Cloud agents are telling me it's running now. So,

**Armand Pretorius:** quickly.

**George Westbrook:** right. So I think with the any of these components the way that it looks all up for debate and obviously we take your guys guidance on that. Um,

**Michael Moores:** Oh jeez.

**George Westbrook:** so I think one of the things we might need to work out is do do we do we build it, give it to you, or do we describe what it is we want? pass over maybe a mock and then you guys do the integration. I think that's up for debate. It's what whatever works for you guys and obviously we'll need to manage access in in that case.

**Michael Moores:** Listen.

**George Westbrook:** But let's see. Please can you suspend Diego

**Armand Pretorius:** Okay.

**Ruan Sunkel:** Go

**George Westbrook:** behind the scene we've got all the the skills associated with all of the standard operating procedures.

**Ruan Sunkel:** ahead.

### **00:15:28**

**George Westbrook:** So out of them you can go and do like a a quick action here. Click in and it's going to do them or you can speak to the agent and it's going to work out what you need to do. Pull in the relevant skill at the point in which it's needed. It's not static in that it's like you use one skill and you use it one skill in that chat. Um it's very flexible. Um, and most of the time it's going to state a plan, ask the user, do you agree with this? Do you want me to execute against it? So, this one is going to be for suspending a card. So this is this is what we call like the the generative UI component. So what what's going to happen is the point at which a certain piece of data is going to be needed or certain components the agent's going to execute a tool um which is going to affect fetch some data and render a component within within the actual page.

### **00:16:36**

**George Westbrook:** So you can close expand them the different canvases. So it looks, feels, acts like the console but rendered within the chat. Currently this is all using mock data. Um so it's not calling any of any of the APIs, not even the the mock APIs. The tools are um so the process that we've gone through to kind of get around the hurdle of the the the APIs not not being there is effectively we've built a full replica of it, same endpoints, same structure and we're just mocking the data that's coming back and randomizing it. And then over the top of that, we've got the MCP server for the for this specific agent. So I think what what's really going to happen is there's going to be maybe two different types of MCP servers. The one maybe that the agent uses and one that the the users might use if they want to directly connect to the MCP server. Um, there might be a way that we can reuse both, but I think with an MCP service, it's just a layer that sits on top that's consuming the actual API.

### **00:17:44**

**Ruan Sunkel:** George,

**George Westbrook:** So,

**Ruan Sunkel:** when you say the two MCPS, the second one you said when a user wants to connect you, are you talking about a developer that's integrating?

**George Westbrook:** yeah. Yeah.

**Ruan Sunkel:** Okay.

**George Westbrook:** Yeah. So the one where maybe they went to they went to the knowledge hub and they're like I want to connect connect this to my claude. Um cuz I think with with this agent obviously it it sits within the app. Um we're going to be having all of the tokens for authenticating the user, things like that. And for the one where the user connects directly to it, obviously we're going to have the same we want to have exactly the same access controls, but I think the way of filtering that out might might have to be slightly slightly different. um given if it's clawed connecting to it, it might have to be a worth or an API key. It's whatever whatever's best and works with DT as well. Um so yeah, it's going to ren render the components.

### **00:18:41**

**George Westbrook:** These not loads of thought has gone into what's being shown here. I think one of the things that we might like to achieve with this is you can obviously there's this tab navigation at the top. maybe navigating a bit more down it or think clicking on some of these things and it's taking it you to pages actually within the console and then could think about maybe when they click on it it goes to another page it turns into co-pilot mode where it's just on the side but I think we've got a few design decisions there I think obviously with transactions and anything to do with cards approval is really key um we don't want these agents going I've just suspended your whole team's cards and um I've raised the limit to the other ones to a billion pounds. Um that could be a bit problematic. So this approval mechanism is going to be key. Um but you'll see from this one we need to work out when there's loads of sequential approvals. Do we want to be keep on showing them um popping up and the users going this is really annoying.

### **00:19:46**

**George Westbrook:** Obviously we can probably manage that with different success layers. So, if somebody's top top tier, maybe we're only approving super super super sensitive ones like simulating a transaction for example. Maybe that's that doesn't need approval for certain for certain people, but for others it does. Um, but I suppose it's going to be all the same approval layer and user access layer that's used throughout the console just so that it's mimicking um what's actually happening.

**Michael Moores:** It's probably worth mentioning while you're going through that.

**George Westbrook:** Hey,

**Michael Moores:** Obviously the approvals here obviously ran the team the approval you're doing the approval queue we're going to have to look at how that sort of syncs obviously some of these actions such as approving the tool use and stuff like that we still need to gloss over about how can the agent bypass that approval queue do we still want that to go in the approval queue for someone else so that's something that we're reviewing as a a TXN layer as well but um obviously

**George Westbrook:** hey,

**Michael Moores:** the plan is that some things will go into there obviously as an agent doing the task we may decide to open that up or as part of the the agent permissions, we may extend that to say a user can't do this but a you know without approval but an agent can.

### **00:21:02**

**Michael Moores:** So as we develop this later it may go for that. So that's sort of decisions from our side we're still looking at and and making

**Armand Pretorius:** I

**George Westbrook:** Well, I think we mentioned potentially like if there's there's they may be I'm a user,

**Michael Moores:** basically

**Armand Pretorius:** know.

**George Westbrook:** I need to approve an action and after I approve the action, it's taken and then the second level of approval might be I want to take an action as a user but I'm not allowed to do So I send the approval to an inbox for maybe Mike who's got higher higher access. He he clicks approve. Then the chat carries on. So it's it it's stateful and you'll see all of these all of these little flashing icons here. So green is basically I'm done but you haven't read me. Orange is there's an pardon me there's an outstanding approval. um look at me and approve it. Um so we just need to work when we've got like the the other people approving what we're going to do it what we're going to do in that scenario.

### **00:22:04**

**George Westbrook:** Um I think one one thing that might be worth going through and I suppose it depends how how

**Armand Pretorius:** Hey.

**George Westbrook:** we we want to work together is what we've got here is our our feedback mechanism. So both for UI feedback and also for conversation based feedback. So for UI UI based feedback, this one's not rendered correctly, but going to take a screenshot of the page. Um, then it just allows you to select select the different components. So let's say one that's meant to be there. Um, let's just say this card is too big. or you can draw draw around it or draw shapes, put pins in it. Um, and for us it just it helps us to iterate a bit faster. So the process will go through there'll be the screenshots, there'll be the pins in there, we'll have a look through the feedback, we'll pull it into our agents which will then look through it, we'll have a conversation, debate and and try and what not try, we will we will fix and update it.

### **00:23:15**

**George Westbrook:** Um the second of which is the conversation based feedback. So for every message you can just select there's the wrong answer blah blah blah blah blah select multiple messages. Um and I think it's just for us it's helpful um to obviously get that cadence right for iterating.

**Armand Pretorius:** What?

**George Westbrook:** I think potentially obviously the the more agentbased conversation feedback um might not be as relevant for for you guys at Stack Works, but maybe the the the UI stuff could be could be something. So when we're we're diverging maybe at the moment um where we've got our workstream, you've got your workstream just to make sure we're aligned. Um, it could be useful If if you guys look periodically through um test it, make sure okay, this component's good. We've changed this color, we've made this design decision, are you able to update this?

**Armand Pretorius:** Are they sleeping?

**George Westbrook:** Um I think I can show you every single workflow we've got,

**Michael Moores:** Yeah.

**George Westbrook:** but I think I think you get the the the gist gist from from this one.

### **00:24:19**

**George Westbrook:** Um, I think some of the some of the things that we're going to be working on over the next week or

**Michael Moores:** Heat.

**George Westbrook:** two is a kind of different way of interacting with the kind of AI workforce that sits behind the scenes. So, so one of them is going to be we're calling it like an agent inbox. So, one example would be an alert happens a user's had 10 declined transactions in a day for example. um then that's going to send an alert to the agent which is going to investigate and then propo going to propose a pan to fix it. So it's going to be a different interface to this because it's not for me as a user I wouldn't want to be what alerts have I got Mr. agent and then it goes away and searches it. You want to you want to know something flashing in the in the top of the corner or a specific section where you can look through all of your alerts quickly look through the plans um and then quickly take action.

### **00:25:14**

**George Westbrook:** Um, and I think the last one would be kind of a scheduled reporting. So maybe once a week you want to have a a nice graph of um how many declined transactions there have been and what are there any merchants that stick out as constantly being declined but it's all on a schedule. So we've got the kind of user initiated the and the user initiated and kind of ad hoc user initiated and scheduled and the kind of agent initiated human validated

**Michael Moores:** Yeah, I think all that's sort of in the prototype that you're seeing obviously various places in the console.

**George Westbrook:** one.

**Ruan Sunkel:** Thanks.

**Michael Moores:** So, it's probably just worth for you Ruan and team just discussing where you can get information from. Obviously, we've got some standard reports that DT are going to build, you know, out the box, their stuff we need for the core, and then we want to enhance that on top with AI stuff and look at reducing the cost by making sure we can rerun those

**Armand Pretorius:** Yeah.

**Michael Moores:** reports without going through the LLM again, stuff like that.

### **00:26:15**

**Michael Moores:** So, when we get to that point, it's probably worth crossing over and discussing. Um, so I I'll get a list together where I think there are crossover points and then when either party gets to that, it's probably just worth catching up again just to make sure we're not missing anything and everyone's got all the the clear uh frameworks and stuff, but there's frameworks for everything from a a UI console side. Anyway, obviously Breton team, we have that vault there where you can see the decisions we've gone through and stuff like that. So from our side, we're happy for them to have access to that as well. So you can see the how we're building the AI and stuff like that. So that's all the the framework type stuff we've given to you but in a in a vault. So, I think yeah, we'll we'll document that and just make sure we're aligned on Those those touch points basically where they interject.

**George Westbrook:** I think one of the things that we probably need to cover and maybe you covered at the start of the call so apologies if I'm going over old ground.

### **00:27:11**

**George Westbrook:** um is at the point in which we we need to integrate what for you

**Ruan Sunkel:** Yeah.

**George Westbrook:** is the ideal situation is it because I suppose the two the two that we kind of see is maybe we we have access to the code base we can make changes um obviously not anything to do with the the console or parts of the console that aren't involving AI but the areas in which we're we're focusing on um keep it isolated on certain branches. Make you make sure you're reviewing the PRs so that you we're not doing anything. You're like,"What the f\*\*\* are these guys doing?" Um, just so we keep that safety. Or the other option is we kind of keep this as a um as a replica, give you guys the code base, and you can do what you see fit with it. Obviously, I I know if I was if I were you guys, I'd probably prefer that you guys do it and we'll we'll review. Um because obviously it takes a bit of that work off your hands, but obviously I understand that that might not be

### **00:28:16**

**Armand Pretorius:** Um, Don't.

**George Westbrook:** ideal.

**Ruan Sunkel:** Yeah. So, I can't give you an exact answer. I have two questions that might help me answer uh your question. Uh the first question was um the components that you that the AI generates um I would like to see what that looks like. number one that would help me to also answer is it better for you to work on our side or us to work on your side.

**George Westbrook:** Yeah.

**Ruan Sunkel:** The second question is the MCP server. So not the one that the developer will use the first MCP server that you basically demonstrated.

**George Westbrook:** And then

**Ruan Sunkel:** Um and Mike maybe this yeah it's more an architectural question is where does that live and what is it talking to? Is it talking directly to DT or is it talking to the control center? Uh now the reason I'm asking is if we want to make use of the approval logic or workflow it has to go through the control center which is effectively just a proxy to the server.

### **00:29:07**

**Ruan Sunkel:** So we add authorization extra user authorization which can include agent authorization as well. Um yeah, so Mike, I don't know what the answer is. Just uh maybe just something to think about. Um because if it if the MCP7 talks directly to DT and then yeah, good luck with the approvals. I don't know that that's going to work. Um, so I I suspect that it in the end the that MCP server, the ones you demonstrated, is going to talk it's going to go through the control center, which means we can intercept and do approvals and um, but you you're calling the same

**Michael Moores:** Yeah. Yeah. So,

**Ruan Sunkel:** APIs.

**George Westbrook:** Yeah.

**Michael Moores:** I think there's a decision obviously we the MCP said we'll be looking at sort of agent to agent conversations for our clients as well when we get on to that later obviously, but we're also looking at the the chatbot here. So, I hope there's some decisions to make in that regard. cards and ultimately yes it's all hitting the same DT endpoints eventually you make a good point though this approval part is you know console specific DT aren't building any approval layer or anything like that so we do need to be conscious that if it requires approvals it does go through there obviously if we are separating it I think George we spoke about this if the MCP is completely separate from the console that would be sort of DTAPI system level so you know an agent to an agent that that covers that quite easily and quite nicely is as that but then we do have to consider that side where we are

### **00:30:33**

**Michael Moores:** working inside um the console and we may have a user base I guess that's that decision between system to system and user to to system basically so I think we need to work through that and just

**George Westbrook:** Yes.

**Michael Moores:** see from your side how best to split that up so we can achieve both things um as well and obviously into the there's a whole API in approval Q4 the console as well that obviously we can hook into and and build into

**George Westbrook:** Yeah, I think in terms of your first question around so the way in which it renders some of these components is what it will do the agent will maybe have a list of a list of tools or a list of components that it's aware of. So rather than it generating the code and then the code is kind of sent to the console and rendered obviously that could be a the potential security nightmare. I mean usually it's not going to do anything like that but there's always that risk. Rather what it does is it builds the payload um for that specific component in the same way that it'd be calling an API or when you render the component it's it's pulling in the data from the API.

### **00:31:39**

**George Westbrook:** So it's effectively built calling a tool building the payload sending the data for data in the payload for that component and also the the component's name. So let's say it's um render transactions. It will it will pass component name render transactions. Um then the payload for that and then when it reaches reaches this it's just going to import that into the into the chat. So it's it's it can use exactly the same components as in the console if needed. I think realistic there'd probably need to be some some tiny changes so that maybe it's a bit more bit more dynamic but it's it it's not as if it's writing the code and every other chat is going to be looking different. Um that port it doesn't work is a nightmare.

**Armand Pretorius:** No. Can

**Ruan Sunkel:** Can you show me an example any like just of what you what you have now? Um because I think it's something that we um uh uh have to take into account now and it's it's we're still early days so we can actually cater for it from the start.

### **00:32:46**

**Michael Moores:** f\*\*\*.

**George Westbrook:** Yeah.

**Ruan Sunkel:** Um,

**George Westbrook:** So do you mean like one of these. So what this obviously this would be oh at

**Ruan Sunkel:** Yeah. Give me an example of what it looks like at the back.

**George Westbrook:** the back

**Ruan Sunkel:** Yeah. If you like like code wise anything like how how's that component defined at the

**George Westbrook:** um

**Ruan Sunkel:** moment?

**George Westbrook:** um I'd need to look through I'd probably I'd probably need to send that to you after rather than me look looking through every uh every single thing.

**Armand Pretorius:** Yeah. Fine.

**Ruan Sunkel:** Okay.

**George Westbrook:** So

**Ruan Sunkel:** And just thinking now um at the moment our workflow is we've got our own repo and we have our own dev environment that we deploy to and test and we send the link to Mike and them just to check if everything's fine.

**George Westbrook:** yeah.

**Ruan Sunkel:** When when we're happy with everything and all the tests succeed only then do we push the code to DT and then it goes into the actual staging environments and eventually the production environments.

### **00:33:45**

**Ruan Sunkel:** So, but on our side, we're 100% flexible um with um so but I

**George Westbrook:** Okay.

**Ruan Sunkel:** think maybe uh maybe we can have another session maybe with a smaller audience and we just see actually what the project looks like, what you have and then we can decide is it better, what's better. Um do you mean like

**Armand Pretorius:** uh get getting into our environment first then into DT. This what discussion would

**Ruan Sunkel:** need to get it running on our side? On our side. Okay. and and also whether where the project will live. Do we do you give us a copy of the code or do you actually create branches on our repo and we deploy it to our dev environment and test it and uh yeah I think that maybe that um a separate session or just a a deep deeper dive into that. Yeah,

**Michael Moores:** Yeah.

**Ruan Sunkel:** I'm happy to do

**George Westbrook:** Yeah.

**Michael Moores:** Yeah.

**Ruan Sunkel:** that.

**Michael Moores:** I think there's probably obviously two two sort of models of discussion here.

### **00:34:36**

**Michael Moores:** Obviously, how do we want to work now as we're building this thing out? Obviously, you're in similar sort of stages. Obviously, at the right time, we'll pull in DT. Obviously, we can build this thing completely separate of DT.

**Ruan Sunkel:** Yeah.

**Michael Moores:** DT is going to run and and essentially own the code that side as well. So there will need to be a separate conversation about how we interject how we push it in. Obviously as George mentioned to you everyone already knows that DT are very specific requirements for code that obviously we need to again pass to them make sure this is all the parties you know libraries we're using are you happy then I know we brought up yesterday about the the models as well. If we just go with the design as we said document that this is the plan we're going with. So as soon as we can get to that point where this is a plan, we can service that with DT. I think there was quite a few rounds last time around wasn't there back and two with DT on what we want to use

### **00:35:25**

**Armand Pretorius:** What?

**Michael Moores:** is acceptable and stuff like that. So the early we can get that in front of DT we can sort of stop that the pass basically and say this is what we're going to use this is the approved libraries and then the way we've got it with DT is anything we add in X we'll just run it by them you know as and when then as long as we can get that that core this is the technologies we're using this is how the code is going to roughly run um are you happy to that it's just from a running point of view from them that you they've got to run and support this application essentially um from that side as well

**George Westbrook:** which I think is it. So I suppose next steps are we'll set up that new session um to go through all of that. Um,

**Ruan Sunkel:** Yep.

**George Westbrook:** obviously we're gonna we're going to keep keep on working away. Um, and I mean is is it worth us just sending you the code base now?

### **00:36:20**

**George Westbrook:** Like it's not not an issue if you're comfortable with that, Mike. It's it's fine with us.

**Michael Moores:** Yeah. Yeah. That's fine. Obviously,

**Armand Pretorius:** Yeah.

**Michael Moores:** I'm I'm very happy between yourselves.

**George Westbrook:** Um,

**Michael Moores:** I say I'm away on the 3rd of September. So, you know, if the sessions before then happy to have a conversation, but I'm also happy for you to have that separately from a repo code level. I don't think I need to be involved in that per se. But obviously, if I'm round, feel free to invite me. Um, yeah, that would be that' be great.

**George Westbrook:** Okay. So, yeah, we'll we'll get we'll get that sorted after the call so you can have a you can have a click around. Um, and then we I mean we can probably also send access to the the current prototype well current replica. Um it I think in terms of the that's what I wanted to ask the the prototype we got from Super Ultra. Um I don't know if that's the most upto-date one.

### **00:37:13**

**George Westbrook:** Is there is there a newer one? I mean we need to see the date in which we got that actually. Let me have a

**Michael Moores:** So that that's the that's the latest prototype.

**George Westbrook:** look.

**Michael Moores:** I know Ryan,

**Ruan Sunkel:** Well,

**Michael Moores:** you've got some UI mockups and components that are Figma based. So that's the will be the only potential discrepancy between that's the prototype end.

**George Westbrook:** Okay.

**Michael Moores:** Then it went into Figma to be those mock-ups as well.

**Ruan Sunkel:** heat

**Michael Moores:** So we can give you them as well. Um, but yeah, that's the last working code prototype basically. I think there are some small UI changes in there, but from a prototype point of view, that's the the latest and the final. There's no more being done on

**George Westbrook:** That's perfect then. Yeah,

**Michael Moores:** that.

**George Westbrook:** because I didn't I was just wondering if we're going off like this direction and all the colors have changed and everything, but I think they didn't need to change, so that's good.

### **00:38:00**

**Michael Moores:** Yeah. No, I I'll double check the figment. I can send that across to you. There may be some small changes in there, but ultimately that was this is what it's going to look like. Then the UI obviously team built the the frameworks and stuff like that front end. So that's what Ryan and team have been building for the knowledge hub and seems to quite well.

**George Westbrook:** Yeah.

**Michael Moores:** So we can make sure you've got that as well. Um just so you can sort of check that as well.

**George Westbrook:** Thank

**Armand Pretorius:** Sorry. Uh no. Uh I'm I maybe just uh just to understand like uh uh the path forward um in terms of timeline when uh like Mike maybe in terms of like for the control center when all of these different because obviously we're working on a for for a specific deadline for the functionality and then I'm I'm sure the the AI team is doing the same like what does the timeline between the two kind of portions of the eight.

### **00:38:59**

**Armand Pretorius:** look

**Michael Moores:** Uh don't don't you've got those dates to hand.

**Armand Pretorius:** like.

**Michael Moores:** I can't remember them top of my head. But basically obviously I think Brett and team the pilot's going to probably concede earlier than sort of establishing it ready in terms of the the whole thing. That's obviously I think we need to discuss when we pull certain functionality across and you know if we do get into stadium or production like that how we cut that across but I think a lot of this AI chatbot will be done in in the coming couple of weeks I know we're doing a lot of testing now obviously we're looking at the AI inbox and stuff like that so potentially if we bucket that into those specific components that we're working on we can then look at dates when we can sort of move that across and say that's out of development if you say and then into more of your proper life cycle and stuff like that. So, um, but yeah, we we can get back to you on on that as well and the workflows we're working through and stuff like that.

### **00:39:52**

**Michael Moores:** But the pilot is due I don't know what the date is,

**Armand Pretorius:** They're

**Michael Moores:** George. You remember the pilot end date off the top of your

**George Westbrook:** Can't remember the end date,

**Michael Moores:** head?

**George Westbrook:** but I think with 7th of September.

**Brett StClair:** 7th of

**George Westbrook:** Yeah,

**Brett StClair:** September.

**Armand Pretorius:** ground.

**Michael Moores:** Yeah.

**George Westbrook:** I think I think it's in terms of the pilot, I think it's pretty much there. It's just a bit bit of testing. Um, but we're not we're not bottle bottlenecked by by anything.

**Ruan Sunkel:** All

**George Westbrook:** we can. We've got the agent inbox, the scheduled reports, um, and a whole host of other stuff. So, it's it's Yeah, we'll be we'll be firing away. Um, I'll be shouting at my computer.

**Ruan Sunkel:** right.

**Armand Pretorius:** Okay,

**Michael Moores:** Yeah, that perfect.

**George Westbrook:** Um,

**Michael Moores:** I say I'll get that um interjection point so we know obly we need the screen before the

**Armand Pretorius:** cool.

**Michael Moores:** the inbox. We need the screen from your side as well.

### **00:40:40**

**Michael Moores:** So there's going to be certain things we need to make sure you have aligned before we pull it all together. So there's a couple on the top of my head that I'll I'll pull back. obviously reporting agent inbox again specific pages specific sections in the console. So they're going to have to interject properly and and merge up that nicely as well. Um and then obviously the report the reporting side also loops in DT as well. So that literally went across to them yesterday in terms of the data lake structure the API that sits in front of that data lake with considerations for the AI accessing that as well and all that stuff prepared. So I'm pushing for a presentation for um both of you really about how we access that data and obviously there's consideration in terms of where does the long and long and short-term data sit the hot and cold data there's a lot of data floating around from obviously AI agents your system what you're storing there's DT's pure code that's sitting separate to TXN's code and also what TXN is storing so there's a lot of stuff we need to basically boil up into a a proper regional data lakeink in the right place.

### **00:41:44**

**Michael Moores:** So um obviously for this phase of a European data lake we're looking at the structure they're then building the rollup tables which is the basically the thing that the console just pulled down as is from that API and obviously we can layer on top your access, make sure it's all vector in and things like that and is in a proper format. I know I sent you a couple of presentation screenshots from DT originally. We're still waiting for that finalized architecture if you will from them to say this is what they're planning to implement and again we'll we'll provide that to both of you to just double check it all works for your side as well uh from that point.

**Brett StClair:** Happy days.

**Michael Moores:** Yeah.

**Brett StClair:** This is the moment where we take time

**George Westbrook:** Wonderful.

**Armand Pretorius:** Sorry.

**Brett StClair:** back.

**Armand Pretorius:** Sorry. Sorry. I go.

**Ruan Sunkel:** demo that you showed us. What agent runtime are you guys using? What does the setup look like?

**George Westbrook:** So for like the managing the interaction between the agent and the UI, it's agui.

### **00:42:47**

**George Westbrook:** Um I think it's by a company called C-Pilot kit. Um and then on the actual agent we're using lang chain deep agents but that's completely isolated. So the only thing managing the connection between the front end and the UI is that agui which is a AI they love to use the standardized protocols but there's about 10 different standardized protocols so it's not really f\*\*\*\*\*\* standardized. Um,

**Ruan Sunkel:** Okay.

**George Westbrook:** the only one that's actually survived is MCP. Um, which is which is pretty good.

**Ruan Sunkel:** Yeah.

**George Westbrook:** Um, but yeah, co-pilot kit AG AGUI. It's the headless version as well.

**Ruan Sunkel:** Okay.

**George Westbrook:** So that because the non- headless one obviously your lot things are dictated to you. So we we can send over a list of everything everything that we're using. We tried to

**Ruan Sunkel:** Yeah. And is it um is it hosted in the in the cloud? Can we replicate the the environment or easily replicate it if we need

**George Westbrook:** Yeah. Yeah.

### **00:43:45**

**Ruan Sunkel:** to?

**George Westbrook:** It to be all we've got is just deployed on Cloud Run in a in in single Docker container. So it's like that's that's why when when I click on it and it takes a while to load,

**Ruan Sunkel:** Okay.

**George Westbrook:** it's because it's scaled down. So it's like no, it's not that it's slow. It's not that it's slow. It's just scaling up. Don't worry. Don't worry.

**Armand Pretorius:** You're completed.

**Ruan Sunkel:** Okay.

**George Westbrook:** But yeah, we can we can send all that over. Um, obviously um in terms of like front end frameworks and things like that,

**Michael Moores:** What?

**George Westbrook:** we've made like a like a lot of inferences. So if we've gone, oh, we're using Nex.js, we're not, but just imagine that we did. Um, then just point us in the right direction and we can rebuild it all. It's fine. It's not not an issue. Um, just so that we're not Yeah.

**Michael Moores:** Sounds good.

**Armand Pretorius:** Thank you.

**Michael Moores:** Awesome.

### **00:44:38**

**Michael Moores:** Yeah, that's it for me. I'll send you Brett and team the documentation for you and team are working on you've got that and then that's a base at least we can go off and then yeah,

**Ruan Sunkel:** I keep going.

**Michael Moores:** I'll get that other document over to both of you about how we interject and deal with that and go from there. Awesome.

**George Westbrook:** Excellent.

**Michael Moores:** Thank

**George Westbrook:** Lovely to speak to you guys.

**Brett StClair:** Happy days.

**Armand Pretorius:** Brilliant.

**George Westbrook:** Thank

**Ruan Sunkel:** Brilliant.

**Dorte Dye:** Can I just ask who's setting up the follow-up meeting?

**Armand Pretorius:** Yeah.

**Michael Moores:** you.

**George Westbrook:** you.

**Dorte Dye:** Do we want to do that while everyone is on the call because it took a while to get that one in the diary?

**Brett StClair:** Good.

**Dorte Dye:** Sorry. Always the one for the organization

**Brett StClair:** Good.

**Dorte Dye:** stuff.

**Ruan Sunkel:** If um if George is going to send us the code, we don't necessarily have to set up a a meeting. We can we can do it ad hoc if if necessary.

### **00:45:25**

**Dorte Dye:** Okay.

**Ruan Sunkel:** Um

**Dorte Dye:** Okay. Sounds good.

**George Westbrook:** Do you guys use Slack at all?

**Ruan Sunkel:** so

**George Westbrook:** Cuz that

**Armand Pretorius:** We're dead, but we're not anymore.

**George Westbrook:** Oh,

**Ruan Sunkel:** unfortunately the email or

**George Westbrook:** you've not gone to Teams, have you? You've not gone to teams,

**Ruan Sunkel:** excuse me not not Stackworx but

**George Westbrook:** have

**Dorte Dye:** No,

**George Westbrook:** you?

**Ruan Sunkel:** I am on teams you can't reach me there will just jump on a

**George Westbrook:** Don't.

**Dorte Dye:** just like you, George.

**Armand Pretorius:** Otherwise,

**Ruan Sunkel:** mute

**George Westbrook:** Yeah. Yeah. Yeah. Okay.

**Michael Moores:** Yeah, if anything else, like I'm here till Wednesday,

**George Westbrook:** Perfect.

**Michael Moores:** so I can coordinate else between the two of you and I'll get all of the stuff that

**Ruan Sunkel:** Okay,

**Michael Moores:** I owe everybody uh before I go uh on Wednesday.

**Dorte Dye:** Awesome.

**Ruan Sunkel:** I think Mike and just this process now is not to or at least from Stackworx side not to make decisions just to understand what it look like so we can help with decisions later. Okay.

**Michael Moores:** I said I'm back on the 15th though.

**George Westbrook:** Yeah.

**Michael Moores:** If there's anything you need while I'm away, fire it across. I will do my best and get everything back to you. There is a lot of actions at the moment, but uh I'll make sure it's done.

**George Westbrook:** Heat.

**Michael Moores:** Um and then we can reconvene on the

**Armand Pretorius:** Oh yeah,

**Michael Moores:** 15th.

**Armand Pretorius:** hopefully hopefully we don't have to bother you at all. Um, yeah.

**Michael Moores:** No worries at all.

**Dorte Dye:** Okay,

**Michael Moores:** Cheers.

**Dorte Dye:** speaking.

**Michael Moores:** Take care.

**George Westbrook:** Love it.

**Dorte Dye:** Bye.

**Michael Moores:** Bye.

**George Westbrook:** Thank you so much.

**Ruan Sunkel:** Five. Six. Six. didn't uh

### **Transcription ended after 00:47:19**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*