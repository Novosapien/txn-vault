---
type: general
subtype: gap-analysis / dependency-review
date: 2026-06-18
title: "AI Scope and Dependency Review"
participants:
  - Brett StClair (Novosapien)
  - George Westbrook (Novosapien)
  - Max Kingaby (Novosapien)
  - Michael Moores (TXN)
  - Dorte Dye (TXN)
status: digested
digested: 2026-06-18
description: "Digest and transcript of the 2026-06-18 TXN gap-analysis call — gap register walked: MCP ownership, reconciliation, A2A resolved; DT multi-tenancy opened"
---

# AI Scope and Dependency Review (18 Jun 2026)

> **Post-call digest.** General gap-analysis / dependency-review call. Brett walked the [[open-questions]] gap register item by item; this digest records what resolved and where it landed. The full transcript follows below.

## Resolved this call (gap register → Answered)

- **#8 MCP ownership** — docs / dev-portal MCP = **Stackworkz**; card-acquiring-API MCP = **DT**; DT owns all post-handover.
- **#25 Reconciliation** — becomes its **own component**, dual-use (Novosapien internal + client-facing); needs a short capture session; DT data format still unknown. Flagged in [[components]] / [[internal-ops-agents]]; new **Reconciliation** component, capture session pending.
- **#28 In-product pricing** — **not** surfaced to the AI or website (bespoke per client); pricing questions route to the account manager / CS via the CRM. See [[co-pilot]].
- **#36 A2A enablement** — MCP-as-message **passthrough** confirmed (thin MCP over the main MCP) until direct provider A2A. See [[a2a-endpoint]].

## Working updates (still Open / Parked)

- **Partner / DT:** #10 webhooks (late, post-Visa-cert), #12 data-lake deck (owed; Dorte chasing; joint session proposed), #13 alerting (observability trigger → central store; ownership TBC), #31 sandbox key (escalated; JWT vs long-lived keys under review), #32 endpoint QA (YAML in, **0% passed**, Postman+Claude testing), #34 Umbraco (API live, UAT up, moving to paid cloud), #35 component library (Figma handover pack is the handle; console pack 9-Jul).
- **Client / design:** #24 cost model (calc exists, ~$1.15/user blended; add price-rise scenario; per-level gates still need Ian), #26 risk boundaries (API layer covers most; bulk-change confirmation; define per use case), #27 benchmarking (summary-only, no PII/client-name; field-map from spec), #29 email gating (personal email OK; account-transition is the priority; not urgent), #30 voice (Parked; triggers = demand/volume; layered support), #33 console instrumentation (Stackworkz to expose app state + caching; post 9-Jul), #47 self-healing (code off-table for DT; Novosapien-side in scope; future crossover).

## New open questions

- **#48 DT multi-tenancy** — one central system (DT) vs per-client (TXN); single containerised API gateway + per-client DBs; commercial driver (clients expect separation); TXN leaning per-client. See [[integrations]].
- **#49 TXN ↔ DT infrastructure separation** — DT build currently inside the DT domain (emails/VPNs) + 3+ shared core services; end goal TXN fully separate on **TXN-controlled Azure (Europe)**. See [[workstream-1-2-architecture]].

## Decisions & context

- **Infra:** TXN-controlled Azure (Europe) reconfirmed; Novosapien is containerised, so it can build/test on any cloud until production.
- **Dates:** dev portal **end-July**; console (config portion) **October**; **market launch early October**; Super Ultra console handover **9 July**; DT delivery is certification-first (Visa).
- **Build method:** synthetic-first — build whole components against mock APIs / simulated front-ends in parallel, drop demo-data flags as real data/APIs are stitched in (reinforces #43).
- **Closed action:** Mike's API spec + architecture are now in the vault ([[txn-api-reference]], [[workstream-1-2-architecture]]).
- **Next:** vault polish → regenerate proposals; client review week of 24 Jun (Wed 24th 10:00).

---

**

Jun 18, 2026

## AI Scope and Dependency Review - Transcript

### 00:00:00

  

Brett StClair: honestly follow up with her. Like I'm having a Oh.

Max Kingaby: Ah,

Brett StClair: Hello.

Max Kingaby: can't even hear Brett. No way.

Brett StClair: Can you hear me?

Max Kingaby: You

Brett StClair: f****** hell.

Max Kingaby: Oh, it's cuz my headphones aren't connected.

Brett StClair: Hello Good morning,

Max Kingaby: England.

Brett StClair: England. What again? What again?

Max Kingaby: Never seen

George Westbrook: That was You look like you got hay

Max Kingaby: it.

George Westbrook: fever, bro.

Brett StClair: My whole face is puffed up. Hey, weird. What the f***?

George Westbrook: Morning.

Brett StClair: I'm like, what the f***** going on here? I've taken an anti- what's it tabs, but I'm everywhere now. Sent a message to the doctor going, "You c***."

Max Kingaby: Nice.

Brett StClair: Hello, Mike. How you doing?

Michael Moores: Okay.

Brett StClair: Um, just make sure I've got all the stuff. Where is it?

Max Kingaby: How was your celebratory Chinese All right.

Brett StClair: Um yeah, it was good. Um um my um daughter got a distinction in her disc like for uh analyzing uh how you can use neuroscience

  
  

### 00:03:11

  

George Westbrook: Morning.

Brett StClair: to gauge and develop empathy within LLMs.

Michael Moores: I

Brett StClair: So she got back yesterday. So we went out to London to the Chinese,

Michael Moores: Looks

Brett StClair: our celebratory Chinese in Chinatown.

Dorte Dye: Morning guys.

Brett StClair: How are you?

Dorte Dye: All right,

George Westbrook: Okay.

Brett StClair: Good. That's what I'm trying to do.

Michael Moores: heat.

Dorte Dye: Mike. Did you mention already dead and senses

Brett StClair: No worries. No worries.

Dorte Dye: apologies?

Brett StClair: So then let's I'm just going to I have many screens today, so I can move stuff around,

George Westbrook: Okay.

Brett StClair: so you'll see my head moving around a lot. Um, let me make use of

Dorte Dye: And Brett, apologies for not replying to your email.

Brett StClair: it.

Dorte Dye: We had and again I don't know if Mike has mentioned already, we had um some interesting couple of days with the DT

Brett StClair: Oh,

Dorte Dye: team um which um put all our focus in.

Brett StClair: really?

Dorte Dye: So

Brett StClair: I'm assuming those interesting couple of days came as a result of Mike's testing of an API or set of

  
  

### 00:04:25

  

Dorte Dye: yeah,

Brett StClair: APIs.

Michael Moores: Yeah, it's just fundamentally a little bit different than we're expecting. So, we're we're pretty blocked on the first one at the moment. So, just ironing that out uh with them. It's just the way they sort of structured it. Theirs may be better,

Dorte Dye: please

Michael Moores: ours, maybe. We just need to make sure that the requirements are met basically. So, go through that. Make sure everything's okay.

Dorte Dye: I like to a little

George Westbrook: That sounded like a very diplomatic answer. Theirs might be better. Ours might be

Dorte Dye: bit.

Michael Moores: No, I think yeah,

George Westbrook: better.

Michael Moores: tech technically I think the difference is they've done like one central system for every client where we had it as per there's pros and cons of both really. Uh just need to make sure that you know there's risks in there that of you know resource capacity impacting other clients. We just need to make sure that's um ironed out and make sure you know risk is minimized.

  
  

### 00:05:29

  

Michael Moores: Otherwise, we'll switch to a uh per client. The architecture works for either way you do it. You just need to make sure you replicate that. So, it's not huge, but it's important we get that sort of discussed and uh ironed out basically.

Brett StClair: Are they using an API gateway?

Michael Moores: Yeah,

Brett StClair: Are they containerizing that gateway?

Michael Moores: they are. Yeah.

Brett StClair: So, some good things. I've seen way too many that aren't even near that stage and then you're just going,

Dorte Dye: That's

Brett StClair: "Oh my goodness, you have a world of pain." And I agree with you. If you're not um if you're not able to scale those API endpoints, that's your bottleneck every time. That's what breaks every time.

Michael Moores: Yeah, I think obviously we have to the commercial side as well is we need to dig into obviously clients expect their stuff to be completely separate. Now the API gateway is one instance but there are per client databases. So it's a bit of a gray area whether they want it completely separate or I think most of them will want the data separate basically.

  
  

### 00:06:34

  

Michael Moores: So we just need to make sure that if we do go that way we can defend that position and make sure they are separate and this is why. So just making sure we don't affect oursel commercially by putting this in. Technically they both work very well. It's just the commercial aspect and what clients will likely want basically.

Brett StClair: Nice. Nice. Yeah, that's difficult. Yeah, I get why they would have gone with how they've gone, but I also get why you guys are going with how you've gone. But like I kind of I think you guys are taking the right approach because if they've set the infrastructure the way they've set it up, it's actually a doable solution. Um if they'd gone on these heavyweight VMs and essentially run a messaging bus styled API, you would have been properly screwed. But with that architecture, you should be able to manage that fairly

Michael Moores: Yeah. Yeah.

Brett StClair: seamlessly.

Michael Moores: Obviously when we tested it was a quite a big difference. So I think that's the first we heard of it.

  
  

### 00:07:36

  

Michael Moores: So obviously needing extra parameters internal APIs living next to external APIs you just sort those stuff we need to iron out that you know I'm testing from the YAML directly which is what our client will do. So, just adding those first couple out. Make sure they're they're right.

Dorte Dye: But it makes gap analyzes really hard for us,

Brett StClair: Yeah.

Dorte Dye: right? Because we're so much dependent on DT and we can't push because we need to get the foundation right.

Michael Moores: Basically,

Dorte Dye: Once the foundation is right, then we can put the timings on it. But it's how do we manage that? Because we want to start with you as soon as possible. But what actually can we start

Brett StClair: Yeah,

George Westbrook: Eat it.

Brett StClair: that's core to this conversation.

Dorte Dye: on?

Brett StClair: Um, so a couple of things I wanted to talk through with you guys is just kind of where are you landing with it? Um what I've started putting together is the proposal. I've based it on the same pricing by the way.

  
  

### 00:08:30

  

Brett StClair: So I've taken the same pricing said okay what can we do with that pricing? Um how do we do it in the timelines that you require? Um strip out the sprint zero. I mean I've still got to invoice and get all that set up. But we've also got some entity challenges outside. Our accountants are going let's not merge the businesses. Let's set up it as separate entities and then do all this. And I'm like whoa hold on. I've set up these entities like this and it's like, oh s***. So, we got to back everything out.

Dorte Dye: It's okay. You don't have to invoice that at all if that's

Brett StClair: Yeah. Figured it's what a great way to start a relationship.

Dorte Dye: easier.

Brett StClair: Don't worry about it.

George Westbrook: Yeah.

Brett StClair: Just do the work. But yeah, like we are quite chilled, right, around those kind of things. So, and like we really want to work with you. Like we love working with you.

  
  

### 00:09:19

  

Brett StClair: I tell you what, such a pleasure to work with people who know what they're doing. And I don't say that flippantly.

George Westbrook: Yeah.

Brett StClair: Like 90% of our customers don't know what they're doing. Like I'm amazed they're in f****** business.

Dorte Dye: But

George Westbrook: Can you just can you just build my startup for me?

Brett StClair: Um,

George Westbrook: What is it you do?

Dorte Dye: that's

George Westbrook: Uh like this. Uh can you help

Brett StClair: oh, we're struggling with sales. Please can you build a sales engine for us?

George Westbrook: us?

Dorte Dye: one.

Brett StClair: What?

Dorte Dye: So, you're making really lots of money. That's

Brett StClair: Well, especially our US customers,

Dorte Dye: okay.

Brett StClair: they just keep throwing cash our way. It's insane. We like, you know, if we were dodgy m************

Dorte Dye: We need to repivot.

Brett StClair: could clean as Yeah. But I'm, you know, I've got my moral compass going, they need help, you know, like they've got to get this right.

Dorte Dye: Republic.

  
  

### 00:10:11

  

Brett StClair: George and I look at each other and we're like, let's build this as best as we can. Give them a worldass solution. But they don't appreciate it, right? They have no idea. guys in the US. So, we actually really really appreciate working with you guys. You know your s***. You've got to bloody hell. You know your market. You understand stuff. Technically, it's joy. Anyway, that's enough um

George Westbrook: You got a bit Yeah, you got bit you got you got a bit of poo on your nose there,

Brett StClair: assing.

George Westbrook: Brat. You might want to wipe it off.

Brett StClair: Sorry. Gone. Um, so what? So let's do this today. Can we make a quick hit to finish off the gap analysis? Run that through because there are some gaps. Um, the goal is what we want to do is you've got your logged in admin portal that becomes the backlog. That's the that's what the agents are going to build the agents with.

  
  

### 00:11:12

  

Brett StClair: Um, that's what we're going to use to orchestrate everything. Um and so going forward when we get into the build cycle um however frequent we do standups and so we found that we started doing standups about 6 months ago every day. Um but actually because we are taking decisions in the standard and pulling them straight into the build and the requirements and adjusting the standups don't actually need to happen daily. They can happen every second day for instance. um which is quite nice, right? Because sometimes you find yourself staring at each other in a standup um talking through some arbitrary task lists, but the standups are there as a ritual to ensure that the teams have picked out their six hours pieces of work and have committed if they're done or not. In this world, um they're done. So, it's not a debate about whether it's not done or is done or the complexity. It's more about uh we finding it becomes a discussion on decision points. Um it becomes a demonstration, a period of demonstration.

  
  

### 00:12:21

  

Brett StClair: And so during all of those things, as you period of demonstration, you're taking in feedback and then you're loading it back into this engine. So getting this vault right, that's the key to success of this requirement session. And so a good indicator is we've got a bunch of what we call deal labs. Um they run the back off the back of this vault and then the team and I we go through it and we check it against previous commercials and it pulls and assembles everything. So usually it would take us two weeks to do a proposal. It takes like a day because it's mainly reviewing and stuff. But we know when a backlog or a vault's in good shape, when the proposals, for instance, come out very clean and it makes sense and there's no gaps. At the moment, I'd say we're about 90% done. We're still getting uncertainty in certain areas. So I think if we cover off the gaps today um a clear a clear red flag that's bringing up at the moment is is dates dates and timing um which we all know right is is an issue.

  
  

### 00:13:32

  

Brett StClair: So I want to just kind of talk you through what I'm estimating doesn't have to be kind of secure because I know you guys are going to hit these things. And then what we've tried to build in the plan is the ability to do a pilot um like a a PC. So you can see this working on syn on a synthetic environment or simulated environment and if APIs are ready then we'll stitch those APIs so that we can actually get some real data and how we generally run those environments is we flag it whether or not the data is demo

George Westbrook: It's

Brett StClair: data or the result is a demo result. Um you'll have to see how we do it in this example but as we get real data so we drop that flag. This is real data. Um, so it's a nice way to kind of see the evolution. How builds work here is very different. So how a build would work traditionally is you lay down your infrastructure database ways of work CI/CD code environments start coding the baseline kind of core application stacks start building out your your kind of graphical user interfaces and then it's kind of back and forwards linking things up this world is build the entire lot here for this component entire lot here entire lot there entire lot there stitch So it is slightly different when you're working with us.

  
  

### 00:15:04

  

Brett StClair: It feels a little bit like wow magic cuz things are working and it's only working because a lot of the times you're just running synthetic data and the stitch is linking up the real data sets. And the reason why I'm explaining this to you, I think it works to your benefit where you're having an unstable timeline on delivery points. You can still move ahead with a lot of the builds across each of the components as long as we're very clear where those data points are synthetic or not. And then it's plugging into the front ends. That's actually even easier because we'll generate a simulated front end and all we do is we drop that simulated front end and plug into the actual front end when they're ready. So the point is we need to get the intelligence working right. That's what we need to get right. That's the hard part about this. Everything else in this world is very easy. And so as and when your APIs are ready, we can cater for it. as and when your front ends are exposed and we can plug into their coding environments.

  
  

### 00:16:15

  

Brett StClair: Perfect. The only kind of traditional kind of fixed dependency we're going to have is making sure that we're setting up on stack works. I'm assuming they're going to build your uh infrastructure. We want to build on the same infrastructure as where all your code is. And so whoever's managing and building that out will give you the specs or give us access so that our agents can fire up the Terraform scripts that we have they have. Um, is there anything else I'm missing? Just giving a description before we start getting into the final steps of this. George

George Westbrook: I think one thing was like in the the way let's imagine there's six components. I think it just really like Brett was saying helps to manage those dependencies. So it's we can sprint maybe forward with three of them but get to a point and there's dependencies but then we can make progress on the other the other components in in parallel. So really the this this those sticking points are removed a lot rather than obviously something like waterfall it's like right we're going to do this to start with oh wait there's a dependency here right we got to wait till that's done um we can work on a lot of things in parallel um like even the front end for example

  
  

### 00:17:26

  

Brett StClair: What?

George Westbrook: um I'm assuming that that um the thing that super ultra showed it was on lovable so I'm assuming that's either in like HTML um with a bit of JavaScript linked in one

Brett StClair: What?

George Westbrook: of the things we can do. Let's just say the console there's there's nothing ready until August. All we can do is pull that in, rebuild it. Um or be it all be it a more primitive version, but just so that we can start say say for the alerts, we've just got a base that we can test on. Um, like we said with the APIs, build build mock APIs that show mock data that replicate the structure of the endpoints. Um, or what we think the structure is going to be. Um, so that we can start to test everything that is testable. If the APIs change, feed it into the agents, rewrite these APIs, look everywhere else where there's a dependency on that in in our code, and just rebuild it. Um, but it's cuz obviously I think initially we we were all thinking, okay, if the if the console's not ready till this date, what can we do?

  
  

### 00:18:34

  

George Westbrook: But it's after we've been looking through it, there's a I think there's a lot of progress we can make quite quickly with without anything. Um, the only one would be the API is just a rough a rough structure.

Michael Moores: Yes. Yeah. I think I say I've got um so I was sort of talking to the the super team about the prototype. So I've already got the developer portal one from them the code and I stood that up on our side as well.

George Westbrook: Perfect.

Michael Moores: So you can have that for the portal side. Similar will be coming for the console. They're just finalizing a few tweaks as that piece off but I've already asked for that code as well. So we'll have both of those as a history on our side as well which we can give you um and go from there basically that's a a good start. Obviously the APIs whilst we have some pretty large issues with the architecture and the YML's not too horrendous. Obviously the structure of the API the fields may change certain things like that but the actual sort of accounts cards card they will change basically.

  
  

### 00:19:33

  

Michael Moores: So um the structure is pretty good.

George Westbrook: Yeah.

Michael Moores: It's just the sort of minimal field changes name changes that you might change basically. So, um, what I sent across is pretty much, um, all of it. There's a few more bits there, but obviously it's a lot closer than I originally thought it would be. It's just obviously we're still ironing out the there's some the subtle changes they've done on terms of I think do is align to their platform.

George Westbrook: Yeah.

Michael Moores: Uh, the one thing we will have an issue with and it comes down to the architect is is the infrastructure. Uh obviously DT will be well it will be in the DT host next to the API basically but we recently found out that um what they've built so far sits inside the DT domain which obviously needs their email addresses their VPNs which isn't going to work for

George Westbrook: H.

Michael Moores: us and it's very much they can give access to us not the other way around. So that's a large sticking point for us that we're sort of pushing back on heavily.

  
  

### 00:20:29

  

George Westbrook: H

Michael Moores: So that would be the only sort of restriction from our side at the moment. We need probably need to get that stood up first for you before we know and can obviously grant access to that. Basically, we are pushing pretty heavily on on getting a solution together. Obviously, what we've been working on this week is the the main topic points. Um, and then we're pushing that as well. Obviously, the console, the development portal, all is supposed to sit next to all of this stuff.

George Westbrook: Yeah.

Michael Moores: Um so there's a pretty large open question on the infrastructure that we're trying to work through pretty quickly with them and get sort of confirmed your infrastructure and then secondly actually standing something up in a TXN domain in Europe uh as well is the next thing it's all in South Africa all very very much UAT you know local testing type thing um so we're sort of pushing on that quite heavily that we can give you some sort of you know working UAT environment that's close to compliance what we don't want to do instead set it up now and realize it's it doesn't work when we move it or whatever happens.

  
  

### 00:21:33

  

George Westbrook: at the uh

Michael Moores: So try and get very much um close to how it will be and then start giving that out as well. So obviously not not only yourselves is it a importance for developer portal should be done end of July as well. So they're already pushing for finalized things and finalized YAML.

George Westbrook: H.

Michael Moores: So you know we are working on that as well and we'll keep you updated on how we get on with the infrastructure basically.

George Westbrook: I I think in terms of infrastructure for I mean everything we will do will be containerized so we can be testing on whatever cloud platform we want. It doesn't need to be next to DT to start with and then at the point at which we need to move it over. I mean it's a container so we can just move it over. Um so it's obviously at the point where it needs to be in production obviously that is a key dependency but

Michael Moores: Perfect.

George Westbrook: for building testing that that should be that should be

  
  

### 00:22:28

  

Michael Moores: Yeah, that's great. Uh, yeah, we we'll send across the diagrams as well.

George Westbrook: fine.

Michael Moores: Make sure it all fits what you're doing. It's just I say we push back quite heavily on the first one. Um, waiting for sort of the an actual document to say you this is why we've done it and this is how it works. Um there's quite a few dependencies on DT outside the API. So they've got some sort of core services as well which again wasn't what we expected. So you know it was is very much like we should have a TX environment. there's three at least three services that they have that sh are shared with DD clients which obviously we need to res well so we can't have anything that basically uses their services uh whether that's something we do now or there's a plan to you know remediate going forward but essentially the end goal is that TXN is entirely separate from DT and obviously we just plug in their API yourselves developer port and console into the relevant uh places basically

  
  

### 00:23:30

  

Brett StClair: Um, when you talk about the infrastructure in Europe, you mean on Azure, right?

Michael Moores: Yeah.

Brett StClair: Cool. I know. I know it's a basic question, but I just suddenly thought,

Michael Moores: Yeah.

Brett StClair: wait, DT, I'm pretty sure they're going to be running on-site infrastructure and I

Michael Moores: Yeah. So is is definite.

Brett StClair: just

Michael Moores: So uh obviously we've got some access to pacilian switches and internal stuff but yeah all of our stuff will be on Azure just moving it basically from South Africa to to Europe basically. So we've got a lot to do internally but essentially Azour will be the the place in Europe we will

Brett StClair: Okay,

Michael Moores: uh host

Brett StClair: brilliant. Brilliant. Um, okay. Happy days. Um, so end of July for the dev portal APIs you're trying to get as soon as possible as you fight through this. Um, okay, cool. Um, then what was October? That was getting the dev portal live and into the market,

Dorte Dye: That

  
  

### 00:24:35

  

Brett StClair: right?

Michael Moores: So is as soon as possible obviously that's a good signals icon.

Dorte Dye: was

Michael Moores: Um the console is the October date but the portion of the console we want in October.

Brett StClair: No

Michael Moores: Um some of the stuff will come later before our first client.

Brett StClair: thanks.

Michael Moores: So the the configuration bit is the most important that we're aiming for sort of October for. Then there's stuff I think you saw like customer service and that sort of things that we'll add on as we go. Yeah, the core needs to be ready October. Um, and we're just sort of going through the pricing with that now and the looking at kicking that off. Essentially the same team. So it'll be after July that they start on that. So we're definitely doing the portal then moving on to the console um post July just waiting for a start date.

Dorte Dye: October was also our expected launch what we were aiming for to go to the

Brett StClair: Brilliant. Brilliant.

Dorte Dye: market.

  
  

### 00:25:30

  

Brett StClair: Perfect. Okay, I think I've got all those dates mapped out correctly. I think I was targeting beginning of October as a launch date. Um. Um. Okay. Let's That's great. Well done. Um, sure. It's a lot of moving parts you guys are dealing with. Um, let me share my screen. Crack out these gaps.

Dorte Dye: Mhm.

Brett StClair: Once we got the gaps done, I can then just run it through the vault. Then the vault will be done. I'll send it to you guys for a bit of weekend reading or whenever you love to do this fun, stimulating, exciting read. Um, I just want to make sure you guys have got access to the vault. So, I resend the vault link and everything if that'll be helpful.

Michael Moores: I've got it. I can get it.

Brett StClair: Okay, cool. Cool. Um, and so that'll then tidy up the final stage of the vault.

Michael Moores: Yeah.

Brett StClair: Bear in mind vult the way we try architecture it is it's human readable and it's definitely agent readable.

  
  

### 00:26:36

  

Brett StClair: Um so when you read through some things you're like why am I going to one folder and then to another folder. We're optimizing it for an agent read for instance. Um because the agents are expecting everything to be in subfolders even though there isn't a subfolder or subcomponent in that particular case. So you'll just see some strange like slight quirks. Those quirks are really where we're designing for the agent to be as optimal as possible. Okay. Now, out of the million tabs that I have open, I need to go find where did I put this? Okay, there it is. Let's slide it out to here.

George Westbrook: Is it the one the 15th of June one? Right.

Brett StClair: Yes. Um, so what I did with the 15th of June one is I took our last

George Westbrook: pockets.

Brett StClair: discussion about the gap analysis and ran it through the vault. And this is it answered a bunch of stuff. It kept a bunch of stuff open where we said we need to keep it open.

  
  

### 00:27:55

  

Brett StClair: And um then it cleared off a bunch of client decisions. Um so where it says answered, we can see that we're clearing it off where we've left it open. And what I'm going to do is I'm going to go to Yeah, we got to here. Um, that's right. I remember us having another laugh about the co-pilot name. Um,

Dorte Dye: What do you came up this time with? Do we want to

Brett StClair: I'm still still a big fan of his dirt.

Dorte Dye: know

Brett StClair: See how it's gone. Oh, no. You called it. I thought it called your name as the co-pilot. That would be too funny. or Mike. It's like a big Dave.

George Westbrook: We

Dorte Dye: I I came up with some things but it it's not really high priority at the moment.

Brett StClair: Mike,

Dorte Dye: So it's like the naming thing we can put in

George Westbrook: just

Dorte Dye: whatever.

Brett StClair: fire out an example.

Dorte Dye: What did I add?

  
  

### 00:29:04

  

Dorte Dye: I had access. I'm trying to play around with the TXN one.

Brett StClair: Oh,

Dorte Dye: Access Nexa and then I had another one.

Brett StClair: that's nice. Quite like that. Quite like Nexa. Hey, Nexa.

Dorte Dye: Me too. It's my favorite. Even though axis is more the central point which was probably stronger but next is for me. Yeah. But again it's not really

Brett StClair: Yeah, it is important.

George Westbrook: I like Tony.

Dorte Dye: important.

George Westbrook: Tony. Tony the TXN assistant.

Brett StClair: Okay.

Dorte Dye: That's my old boss code.

George Westbrook: Got an issue? Speak to Big Tone.

Dorte Dye: That was his nickname. Big T.

Brett StClair: I used to have a mate called Tony the Tiger. Portuguese guy. Okay. So, yes, that's what we got to. We'll park that. So, number 23, let's park um per level cost token model cost per thousand calls uh set to developer support. I can't remember what this was about.

  
  

### 00:30:10

  

George Westbrook: Good night.

Brett StClair: I did send Ian a token costing uh culk that allowed him to select whatever models that he wanted to run. Um and then it was it then looked at every single component, looked at how a user could possibly use it, started working out the number of tokens and the size of the tokens or calls and gave them a bit of an estimate based on the scale and also looked at a period of time with an estimate of 30% reduction in LLM costs per year um if we kept to those ex existing models. mod because we don't know what future models costs were. So I just kind of took what the trend was and if we hold those models our systems are designed as the latest model comes out you can plug in or change out a model. Um but you needed to get some kind of costing on it. Um if I remember the figure correctly let me see if I got it here. I think I've actually got it to hand. Just pull it up.

  
  

### 00:31:20

  

Brett StClair: Um Yes, I do have a tab, but not on that tab. On the bloody tab. There it is. Um, probably looking at a cost per user of $1.15. 15ish on your LLM fees.

Dorte Dye: And that's internal and external,

Brett StClair: Uh it is

Dorte Dye: right?

Brett StClair: across every single possible use case I could find internal and

Dorte Dye: Okay,

Brett StClair: external.

Dorte Dye: because the internal we can scale the external we just have to do assumption because we do not

Brett StClair: Correct. You can probably separate it out.

Dorte Dye: know

Brett StClair: I didn't separate the two. I just took absolutely everything. Um, interesting. I thought it would be the other way when you swap around models, take the Claude's latest models. Um, and you see we try to balance, you know, simple lookups using a lower model, etc. All that kind of stuff to try optimize the cost as best as possible. But it's almost double the cost. Interesting.

George Westbrook: No, that that

Dorte Dye: And that's and that's just the beginning,

  
  

### 00:32:55

  

Brett StClair: Yeah.

Dorte Dye: isn't it? I mean,

George Westbrook: checks.

Dorte Dye: we talked about that the pricing will go up. I mean, everyone gets hooked and then they put up the prices and then where do we sit in the dependency and where

Brett StClair: Yeah.

Dorte Dye: does it leave us? So has that be factored in in the proposal as

Brett StClair: Um, what I did is because I don't know I don't want to make an estimate on what the price going up would be,

Dorte Dye: well?

Brett StClair: I essentially took what the baseline costs and it made the assumption that the model stays the same. So if you stay on 3.1 and we know it's working well on 3.1 then you know you're only going to upgrade to the bigger models if you are not getting the output that you want or you want to improve the

Dorte Dye: It's this time we don't get them from the US anyway.

Brett StClair: output. Yeah. Yeah. Or we switch to Chinese

Dorte Dye: really interesting. I discussed it with my husband because he's a developer.

  
  

### 00:33:41

  

George Westbrook: Yeah.

Brett StClair: models.

Dorte Dye: He said like it always has been like that. It's like we never got the latest encryption models because the US always had the finger on it. It just now because it's so public, everyone is just suddenly talking about it, right?

Brett StClair: Yeah. What's

Dorte Dye: Um I'm not sure about the pricing increase.

Brett StClair: it?

Dorte Dye: I haven't mentioned it to Ian, so it's maybe just worth um that in there as well.

Brett StClair: We can build that in. Yep.

Dorte Dye: Yeah.

Brett StClair: So everything. So I've got a pricing LLM decrease assumed every year. I put in cost multipliers, exchange rates, contingency overheads, all that kind of stuff. So you can play with it like I mean if he wants to

Dorte Dye: You need filter. You know that you need a trump filter now because whenever does something the market goes

Brett StClair: Hey.

Dorte Dye: completely I mean it's like I was looking at the charts yesterday and it was like it was speaking and it was like this again.

  
  

### 00:34:26

  

Brett StClair: Yeah.

Dorte Dye: You can't you can't factor at the moment anything.

Brett StClair: So the scenario I just put in different range of scenarios to make it easy to calculate. So if I've blown the numbers like here um again I tried to break it down per what they're going to use and how they're going to use it and what the token kind of amounts would be and all that kind of stuff. But then I figured actually it's easier for you guys to go let's look at a high level scenario. What would that cost versus a expected scenario? So he's got all of that.

Dorte Dye: Yep.

Brett StClair: I'll send this to you guys as well to have a play with it. And the way it works is you just download the HTML just written

Dorte Dye: And then you just fill in the figures.

Brett StClair: in.

Dorte Dye: I like that.

Brett StClair: There's no fancy storing in a

Dorte Dye: I know. I did that on the weekend as well.

Brett StClair: database.

Dorte Dye: I built a tracker exactly the same for for a different model.

  
  

### 00:35:19

  

Dorte Dye: It's so easy.

Brett StClair: So easy, right? Oh,

Dorte Dye: I'm right on the weekend.

Brett StClair: just makes that's because you have a new superhuman

Dorte Dye: Okay.

Brett StClair: string, right?

Dorte Dye: Pony.

Brett StClair: Um,

Dorte Dye: Okay.

Brett StClair: okay. So, we've got some pricing. We've I think what we're talking about here is putting some kind of controls in on public availability. So, that they can't query anything. So, necessary guard rails to stop them querying anything outside of the TXN environments. and also put some caps in on spend that they've blown their spend for the day it will reset in. So those kind of things and then I think we had a bunch of questions around what pricing could look like and I made a a guesstimate and my guestimate wasn't far off from what those calculations were when it came to a per user cost. Um then reconciliation's home um its own payment ops component or does it stay internal ops? That's just trying to figure out whether reconciliation deserves its own component.

  
  

### 00:36:31

  

Brett StClair: I can't remember what we decided. I think it's an internal ops thing,

Michael Moores: So I think as dual use this obviously we will use it internally to make sure everything's working but ultimately our

Brett StClair: right?

Michael Moores: client will also use this heavily as well. So it's not just sort of our own internal ops it's definitely a bigger thing. Uh and obviously reconciliation is a very big part. So it's something we are looking at wanting to do. Um so yeah definitely I think it might be beneficial of his own component

Brett StClair: Um,

Michael Moores: potentially.

Brett StClair: okay. So, we'll put it into both. Um, what we'll need to do is set up a small session, but we can always do a pre-ro um, and we'll highlight it that it hasn't been done. So, we separate set up a reconciliation component. do like a half an hour session in the actual project and quickly capture that. Um the internal ops one how I'm managing it is that's an ongoing as you start you'll be like ah I've got a bit more ideas what I want to put into internal ops and so as that'll pick it up out of the standups and any other meetings that we have and it'll pull and slowly but surely populate out the internal ops components.

  
  

### 00:37:50

  

Brett StClair: Um, and I think that's a nice eloquent way to handle the internal ops cuz you're going to keep on seeing changes, wanting things done, and we just need to be able to put into the system, point the Aentic AI at it, and start building out those

Michael Moores: Yeah, I think that makes sense.

Brett StClair: components.

Michael Moores: Especially for reconciliation. We're still unclear on how that will be, what data we're getting yet. So, everything else we're pretty clear on. Reconciliation is still something we definitely want to do. It's just we haven't got much information from DT on how that will work, what you know, format they have yet. So, we're still waiting for that heavily on them.

Brett StClair: Okay, perfect. Uh, AI risk tolerance boundaries. Um, what's never allowed even with approval? What blast radius forces a human override? Beautiful. It's a bit what we were talking about further up and defining those and it feels like those again we define as we kind of hit the use case and trying to define those in detail without being deep in the use case could be an overkill thoughts.

  
  

### 00:39:02

  

Michael Moores: as well.

George Westbrook: Yes.

Michael Moores: We've got we've got a lot of um gates already in the API and stuff like that. Obviously, you know, there's no deletes on cars or card holders because, you know, we don't want that data to deleting and stuff like that. So, you know, there's still some stuff they can do that's quite bad. You know, if they change the whole, you know, a thousand products, it's pretty bad. But I think this is the use of the AI making those large scale changes. So I wouldn't want to stop them doing that. But I think we have covered off most of them with the API uh layer. Obviously the internal stuff we wouldn't allow in here anyway.

Brett StClair: Okay.

Michael Moores: So it's not like they could completely deactivate an entire program or the entire TXM. We'd always back that off. You know whether we have our own internal stuff for that or not is another story. But yeah, it'll only be sort of publicly facing APIs that they have access to anyway.

  
  

### 00:39:53

  

Michael Moores: So, you know, they're only doing actions that they could do with their own AI or with a script from the API. So, I don't see that as too much of a concern at this stage in terms of that. I think we just need to add extra caution. If someone is going to do a 100 products, for example, then we're like, you know, are you sure you're going to change all this? I think we discussed this anyway. Um, you're going to make this whole scale change. the impact. I think we've covered that there as

Brett StClair: You know what? I've just realized I haven't uploaded the uh your

Michael Moores: well.

Brett StClair: API documentation like into the vault. Um George, just a question for you. How should I go about that? Do I create another section like I did with um the UX environments and then run the product manager across it?

George Westbrook: to to create what? Sorry.

Brett StClair: So Mike sent through the API specifications and architecture.

  
  

### 00:40:51

  

Brett StClair: Um I've downloaded in my thing and I just realized I didn't run it through.

George Westbrook: The

Brett StClair: I was meant to run it through but I think I stopped because I suddenly realized it's not a meeting. It's not a UX. Um, I'm just wondering if we need to build out a new subskll for that.

George Westbrook: It it's it probably going to sit in the architecture and then in part of

Brett StClair: So, if I drop it into the architecture,

George Westbrook: the

Brett StClair: will it manage it? Okay, perfect.

George Westbrook: Yeah.

Brett StClair: I'll give it a run after this and get your feedback on it. So, Mike, there might be a bunch of stuff that is sitting in there that we'll be able to extract out. What I'll do is um I'll pull out just a quick report of what's additional and just send that to you and see if you pick up anything that it it shouldn't be pulling in or that we might have spoken about before I actually committed to the branch.

Michael Moores: That's perfect.

  
  

### 00:41:44

  

Michael Moores: That's good.

Brett StClair: Um uh postprogram benchmarking consent anonymize can still identify with a few clients. Consent and thresholds are going to be monitored later. This is in the agent inbox alerts. Anyone remember or understand what that is?

George Westbrook: So it's where we would be. So let's say program A, program A wants some advice on what settings or what configuration um could allow them to perform better. And I think we talked about how using the data from other card programs that are slightly similar um and seeing the results that they've got to give them advice. But it's one way that we can a test that we could do in order to make sure that it is anonymized is have an agent that speaks to the agent that tries to interrogate it to work out what client is. there's maybe some stuff we can do there. Um but then also I think it is just a pen and paper exercise where it's just okay this needs to be gone. This needs to be gone. We will probably know by looking at the data.

  
  

### 00:43:04

  

George Westbrook: All right, this is quite obvious that it is this client. Um I suppose it's just how do what do we gate and how do we gate it and what do we just remove?

Michael Moores: Yeah, I think largely for that I think we're looking at sort of summary data. You're looking at you know in my industry who has this setting on essentially. So I think already the use cases are quite targeted obviously um bin and bin ranges that's not sort of specific to a client but you still get an idea of who's that who's issuing that card basically. obviously card holder account names, addresses, stuff like that. We'd never have sort of back in there as well. So, and you know, and also never the client name. So, I think they're the sort of core. Obviously, we can map out everything explicitly when we get the API spec to say, you know, you cannot give out this field, that field. There only a few of them obviously PAN, CVV, there's stuff in there that, you know, ultimately you may never have access to that.

  
  

### 00:44:01

  

Michael Moores: we need to decide is what API endpoints that you have access to versus not. So for the SEC secure card stuff, we've purposely got on a separate API. So you'll never be given that information unless you specifically ask for it. So we have our cards endpoint, we have a a show pan endpoint that will basically go here's that extra detail. So we've already purposely moved any PCI information out of those payloads unless you explicitly ask for them and you have the right role that we give you as well. So it's that's governed then obviously PII the the personalized information that will be in everything you pull back in terms of cards and stuff like that automatically. We don't sort of pull that out or mask that. So we just need to make sure we don't send any of that sort of back.

George Westbrook: Yeah.

Brett StClair: Perfect. So, impro improduct pricing transparency pricing in the console so the carpilot can reference it or held externally. I can't remember. I know what it's talking about.

  
  

### 00:45:04

  

Brett StClair: Can't remember what we're talking about whether it's internal or external. Anyone remember that?

Michael Moores: No, I think I mean generically on the pricing I don't think we're advertising our pricing at all

George Westbrook: Yeah.

Michael Moores: anyway. So it'll be very bespoke to that client.

Dorte Dye: No.

Michael Moores: So it's not something we would expose on our website and obviously not need to expose any AI. So I think um yeah from that point we won't be exposing the pricing. I think the only thing that may come in in the future will be obviously billing you know what is actually being used what is actually being bu about that but there will be some pass on costs from you know providers sort of certain things that we can say you know this is your bill for this month or whatever it may be and maybe we can tie it to invoicing. Yeah we will actively sort of display specific pricing or cost per use or anything like that. It'll be what we discuss with them. This is your access fee for the platform.

  
  

### 00:46:00

  

Michael Moores: And then we'll try and stick to that as much as possible. And if there's any sort of sort of future products for example that we want to charge extra for then we may add on for that individual product. But right now it's just be a core this is how much we're charging you for access to the entire platform. What they use is up to them. Basically that includes both the console and API.

Brett StClair: Would you wanted to if it did start asking about specific pricing maybe refer to account manager or hand out account manager details that kind of thinking as

Michael Moores: Yeah,

Brett StClair: well.

Michael Moores: I didn't discuss what we're going to call them, but I think account manager, CS, whatever we call them, they I think obviously we'll discuss,

Dorte Dye: Yeah.

Michael Moores: but you'll probably have that account will be assigned to somebody. So we'll probably have that information in the CRM like that that we can pull and get that information. But yeah, ultimately if there's anything that needs to go specifically to and obviously we can map this out as well,

  
  

### 00:46:53

  

Dorte Dye: So,

Michael Moores: but we can also direct them if there's something that AI or personally we don't want the AI to answer, we can then add those routes to direct them to either technical support or account management depend on what they're asking.

Brett StClair: Perfect. Uh, corporate email gating policy avoid junk uh signups without blocking genuine startups. That was on the dev portal.

Michael Moores: I think that one's still largely openly dependent on the cost as well. I think we need to have a look at what we want to give out publicly versus um you know corporate as well. So I think we're still looking at the the login the sign up. Obviously for the July date there won't be any login or sign up for the developer portal as it stands. So this one's not an immediate issue but I think as we work through these use cases we may decide this portion of the AI is available if you sign up and then obviously we have that issue then where you say the corporate email.

  
  

### 00:48:02

  

Michael Moores: I think having a um junk sign up or a personal email is fine. And I think it's just making sure we can transition that account into uh a proper client if we need to. I think that's the most important. So nothing's lost between the two because a lot of them will just sign up with their personal accounts, especially if they're early fintex that may not even have a name for their company yet. Um so as long as we can transition them, I think that's that's not as important. Um so we never lose that context. Obviously will be more important as we build the AI AI out and have that context. But yeah, the most important thing there is transitioning that from dev dev portal into the console into the actual TXN system

Brett StClair: Perfect.

Michael Moores: basically.

Brett StClair: Voice support tier 2 voice agent. Um on the dev support. Yeah. Did we say

George Westbrook: I think we said text first at launch and then

Brett StClair: first?

George Westbrook: potentially either adding it in later or adding it in as an extra paid for feature.

  
  

### 00:49:09

  

George Westbrook: Um, I mean, I suppose one of the things, it depends if it's the developer support. It could be like one of the last lines of defenses before it's human escalated as

Michael Moores: Yeah, I think this one I say text for to launch.

George Westbrook: well.

Michael Moores: I think we need to see what the ask for is um how well obviously the textbased system is doing it, understanding that problem before sending to me. So I think that's the two triggers. Either it's being asked for um and we can charge for something like that or we're having a lot of tickets. I think would be the trigger point where I look at probably introducing something like this. But I think for now uh text base as they'll be familiar with and then we can look at that sort of voice support do the research and see if we want to as well.

Dorte Dye: I mean that was the differentiator right Brett that's why you recommended that because no one really has it at the moment but then it's the cost factor as well so I guess We will monitor the market what what's coming out if people

  
  

### 00:50:03

  

Michael Moores: Yeah.

Dorte Dye: are start using it and know we just really need to do the commercial

George Westbrook: I think that there's I suppose there two different approaches as well.

Dorte Dye: modeling.

George Westbrook: It's like there's imagine like a a layered level of support where first it's go to the docs, second it's speak to the text agent and then third could be the voice agent and then finally would be the internal support team. One way could be that when it reaches a certain point um let's say it's text and then they're like I want to speak to somebody um say the person who is covering support can look at the request and say to an agent right can you go out and collect this information from them. So rather than sending an email um it's kind of like you've got an agent workbench which you send out to whoever you want to collect whatever information. So you're not having to do the, "Oh, let me call them now or let me send them an email now." And then they don't respond and then you've got to wait to remember to follow

  
  

### 00:51:02

  

George Westbrook: up and things like

Dorte Dye: Sure.

Michael Moores: Yeah, that sounds

George Westbrook: that.

Brett StClair: Okay,

Michael Moores: good.

Brett StClair: let's work through some partner dependencies. Just open questions. Need quick sign offs. Um first one MCP ownership splits uh dev portal docs to MCP to stack works card acquiring API MCP to DT. Is that

Dorte Dye: Thank

Brett StClair: correct?

Michael Moores: I think that would be the split.

Dorte Dye: you.

Michael Moores: Obviously, they'll ultimately end up with DT owning and manage it as it stands.

Dorte Dye: What's

Michael Moores: Ultimately,

Brett StClair: Yeah.

Michael Moores: post this, DT will manage all of it.

Dorte Dye: this?

Michael Moores: Um, but for now, yeah, essentially they're the two splits that we have for the current um development that's ongoing.

Brett StClair: Um because we're going to be calling those MCP servers, right, George?

George Westbrook: the what the agents will be.

Brett StClair: The agents, I mean. Yeah. Yeah. Yeah. Yeah. So,

George Westbrook: Yeah.

Brett StClair: what will we be calling the MCP?

  
  

### 00:52:02

  

Brett StClair: back. Hey, you

George Westbrook: Huh?

Dorte Dye: He's making his inside jokes. Only he

Brett StClair: was a terrible joke.

Dorte Dye: understands.

Brett StClair: It was a terrible joke where my brain went

George Westbrook: This just I think we've

Max Kingaby: that

Brett StClair: down.

Max Kingaby: one.

George Westbrook: I think we've just got to ban Brett from making jokes.

Brett StClair: Sure. Awful.

Dorte Dye: You should get a t-shirt like daddy jokes, you know,

Max Kingaby: No.

Dorte Dye: because that really what what it comes down to.

Brett StClair: Bad daddy. Um, product web hooks. Will GT add it? Uh, on what timeline? Underpins change impact alerts D.

George Westbrook: I think that's just a alerting system, isn't

Brett StClair: That's the alerting system right

Michael Moores: Yeah. So,

George Westbrook: it?

Michael Moores: web hooks, well, we we've added requirements for specific web hooks and then as specific statements as anything else that's

Brett StClair: here.

Michael Moores: necessary. Now, they haven't got to web hooks yet. Web hooks is one of the very last things.

  
  

### 00:53:06

  

Michael Moores: Um, obviously we got the visa certification, so it'll be quite late in the in the flow that that would come in.

Dorte Dye: No.

Michael Moores: we can speak to them about what they're planning, how they're planning it, and just make sure this is on their radar. I say we've not explicitly asked for it. We've called out several web books that we absolutely need. And then, you know, we've also sent any other web book that we may need as well because we knew this was happening and these engagements were

Dorte Dye: Oops.

Michael Moores: happening. So, we can draft up an email to them and say, you know, this is or document and say, this is what we need. Whether they push for a change request or not is on well is they may they may do but they haven't even started scoping. We haven't done the user stories for it yet. So I think we're at quite a good position where we can adopt this basically but yeah I don't know what the time will be yet. I can get you the I think we need to get you the the timeline on the delivery anyway from DT.

  
  

### 00:53:58

  

Michael Moores: Um so I think D you've got the latest one of them have you? Yeah. So we'll send that to you anyway.

Dorte Dye: Yeah.

Michael Moores: is roughly the order it's going in. Obviously the dates may slip or change based on actuals but um that was a targeted uh when we want it basically and the reason for that is obviously certification we need to pass for visa whereas web hooks and spend controls and stuff like that is not really needed for the certification so they come so later on. So that's why the we sort of pushed everything up that we absolutely need to get a certification done

Brett StClair: Perfect. Perfect.

Michael Moores: basically.

Brett StClair: um core API stability and versioning when stable app okay we've had a chat about that um already data lake schema when does DT share it I see we've got a little bit of an update actively building it

Michael Moores: Yeah. So, I owe you the I don't know if we've got it off DT yet, but we owe you the presentation from

  
  

### 00:55:03

  

Brett StClair: oh

Dorte Dye: No,

Michael Moores: DT.

Dorte Dye: I will chase them again.

Michael Moores: Yes,

Dorte Dye: Nice.

Michael Moores: obviously what I sent you the two slides, but there's a whole extra thing. So, we we're open to and would like your feedback on that. Um, obviously the DT stuff we have is very static. It's mainly for our own central API. You're the ones that are going to be actively using it in in an aggressive manner in terms of the console. Console just be obviously doing roll up reports and stuff like that. I think this is a lot more granular. So if we do need to, you know, change anything, I think that'll be good for you to review.

Brett StClair: Perfect.

Michael Moores: So I think we'll chase them and get that back to you first. It's still very much an open decision. We probably we've got lots of questions on the back of it to them. I mean they have their own internal questions as well that needs to be answered.

  
  

### 00:55:51

  

Michael Moores: Um and then yeah if we can get your feedback we can pass that into them as well. Um and potentially I think it might be worth having a session with them with yourselves as well just so they can understand how you'll be using it. Um again we still don't know how the data is structured yet. I'm still trying to get access to the the database itself that sits behind the APIs to know what the data structure is. But ultimately with those vectors, it should make it a lot easier for the AI as well. Um, so you know, we'll look at the design and then I think make sure you're uh in sync with us to looking at everything that comes out of that. Basically, the proper plan and stuff like

Brett StClair: Perfect.

Michael Moores: that.

Brett StClair: Uh alerting system build ownership dtar to contact context list post alert API nobody scope to build detection. I remember speaking quite a bit about this. I can't remember where it finally landed.

Michael Moores: I think that was your suggestion to have a standard observability

  
  

### 00:56:55

  

Brett StClair: Is that

Michael Moores: platform trigger the trigger the alert and then you do something with it.

Brett StClair: right?

Michael Moores: That again subsequently has gone into our logging and alerting and monitoring discussion with DT sits very much around the architecture and stuff like that that we need to scope out first. Um let's say there is a phase two like post an alert more a functional thing that we had scope with DT knowing we wanted to build the alerts but with the discussion we need to understand where that inbox is going to sit where who's going to own all of them essentially what we want is a central place for every application to to set those alerts so the console will pull the alerts basically and say here's all of them and whether it's DT that pushes it in or yourselves somewhere that can hold those alerts centrally and then we can just surface them to a user on you know for a particular program.

Brett StClair: now like an alert center and it's been kind of graded and and

Michael Moores: Basically

Brett StClair: flagged correctly so you don't yeah get absolutely drowned and all that stuff.

  
  

### 00:57:58

  

Brett StClair: Okay. Um AI ready downloadable doc file. This was for the developer support. So I think this was the NCP server,

George Westbrook: that that no one of the things people started doing is

Brett StClair: wasn't it?

George Westbrook: they literally just have in their docs folder uh in their docs website is just a text file for LLMs. Um,

Brett StClair: Oh, I see.

George Westbrook: I mean it there's many different approaches we could take. There's like some people just do like a massive just a massive long file. What we could do is just have one file which has all of the endpoints and when you might want to use them and then you link to another link or another text file so that you're not say consuming let's say it's 20,000 tokens for the full for the for all of the docs. But then if you shorten that down and just have the more condensed version, it could be 2K and maybe they need three endpoints each at 1K. Then it's five 5K consumed instead of

  
  

### 00:59:04

  

Michael Moores: Yeah. Yeah. Yeah, I think for this one I think we're happy.

George Westbrook: 20.

Michael Moores: You know, I know it says text there, but we're happy whatever it is from a stat works point of view. They just need to know where they're pulling it from to download it. I think it does make sense to be in the AI side essentially obviously with it being changing a

George Westbrook: Yes.

Michael Moores: lot and obviously aligning to that. So I think with that we can also put some sort of additional improvements on top of the documentation as well that we learned. So that makes sense. But yeah, they're they're pretty happy stat works are. They just need to know where who's hosting it, where is it, where is it hosted, and how do they pull it down. Basically, that's the final thing that they will need.

George Westbrook: Okay.

Michael Moores: Obviously, we sent the DT stuff, but this will be something they need to know. Obviously, we can choose whether or not to put that in the initial version of the developer portal or not.

  
  

### 00:59:52

  

Michael Moores: Um, depends on our timelines. Obviously, I finished in July. we may need to sort of hide that for now and come back in a phase two with a portal and them basically. But yeah, ultimately we just need to make sure we have that file um or or if we can generate a static one for for launch or

George Westbrook: Yes.

Michael Moores: something like that that have rather than a hosted one.

George Westbrook: Yes.

Michael Moores: But ultimately if we can get the design in and and keep it as is, it's a lot easier for Statway then to swap that out essentially as well. So um yeah, great.

Brett StClair: public sandbox AP. API key model. Does the sandbox need a per user key? Change whether when sign up 21 is required. What's 21? Okay, we've passed

Michael Moores: um yes that's not the only question.

Brett StClair: it.

Michael Moores: So works also absolutely need this for the developer portal. Um we have raised an escalation yesterday on the the top priority things.

  
  

### 01:00:48

  

Michael Moores: So these are the two or three things that statworks need to finish is the AI LLM, the public sandbox API key and there are some stuff in the YAML that isn't there yet. So there's three core things that we absolutely probably want to know. Obviously public sandbox isn't built yet, but I think we can get a good idea of what the public key model is. I think I referred to so essentially they're still looking at authentication as well. So originally we had long-standing API keys. I got sent a document yesterday suggesting JWT tokens. So they're looking at moving to that and obviously we have some concerns because that is you know functional shift for the client. Instead of hitting one endpoint there's a refresh and and all that stuff. So you if there's benefits there we will look at switching but we just need to understand it properly um to know for sure that that's the the method we want to go down basically. you know, logically makes sense for security, but obviously we need to make sure that these clients are they they own this themselves basically and it's easy enough for them to build.

  
  

### 01:01:52

  

Michael Moores: So, you know, for processes, it's very, you know, it's normal to have long-standing API keys. Obviously, that's not great for security. Um, and that's why we sort of rotate them every sort of six months. So, this may allow you to get over that hurdle. So obviously we've allowed them to rotate it themselves in the console but also this may just give them that extra confidence as well. We just need to sort of test that against the market that they'll be happy with that. So I think we just need to make sure everything's fine there. So that's once that's decided obviously we we'll know the public sandbox stuff as well. So it's a very important topic for us.

Brett StClair: Perfect. Uh, endpoint QA test status 80% endpoints 80 to 90% untested affects mock API fidelity for every build on direct transact.

Michael Moores: Um, yeah, I think that's still the same point. So, we've sent the EAML. I still need to functionally test it. As it stands, it's 0% passed so far.

  
  

### 01:02:55

  

Michael Moores: Um, I was unable to test um originally.

Brett StClair: Okay.

Michael Moores: Um, some of the end points aren't working that I need. So, um, I will continue to do that. Obviously, we'll let you know which ones are passing UAT and stuff like that as we get them. But ultimately, we're looking at, uh, from a client or developer portal view right now because that's the first thing we're publishing. So, the ammo that they give me, it's going to Postman. If it doesn't work in Postman, we're essentially failing it because it has to work for a client's. So, we're being very strict there. If it's not working properly, we're pushing it back because it might be something very small that the field name is wrong or whatever or the examples aren't good enough. But as the portals go out in July, you know, ready from July, we need those good quality descriptions and stuff like that. So that's how we're testing and I've got sort of Postman doing and Claude doing some sort of automatic testing as well.

  
  

### 01:03:45

  

Michael Moores: So it should speed this up once we get through the initial barriers. Um, even though the architecture is open, I'm still going to proceed with the functional testing because it'll change it slightly the the endpoint mockup and makeup of those, but the functional side behind it won't change. So, I can still progress a little bit in terms of um actually making sure accounts work with cards and things like that that don't rely on that uh underlying architecture as well.

Brett StClair: Perfect. console implementation depth page states component ids action handlers micro flag the plugin some plug-in work knows what that is

George Westbrook: may need extra work to expose the page the component identifiers

Michael Moores: Okay.

Brett StClair: hey

George Westbrook: and action. I've got an expanded version that I'm referring to.

Brett StClair: oh good because This needs expanding that.

George Westbrook: Um

Brett StClair: It's gone too summarized,

George Westbrook: um yeah, I think it was around that obviously one of the things that we would be pulling into the

Brett StClair: right?

George Westbrook: agent would be the call it the application state.

  
  

### 01:05:04

  

George Westbrook: Um, so I suppose it's just working out one, how are we going to get that? Are stack works going to be able to what what do we need to do in order to get stack works to to expose that? Um, and then are we going to need like a a caching mechanism um in order in order to maintain that? Because I think it was one thing I think it was Ian's example of his mom using her phone where she starts on one page goes to another blah blah blah and I think quite a nice feature would be for the specifically the co-pilot is it understands given a used session where they started where they went from and then also what they say they're trying to do so that we can kind of replay and said oh you went here then you went here then you went here what you actually need to do is go back to this page then click this and then click

Michael Moores: Yeah. Yeah. I think what we can do there is obviously Statworks haven't even began.

  
  

### 01:06:01

  

Michael Moores: They're just doing the costing. So I think this will probably align quite nicely this project. So Statworks are very good at working with other vendors if you're if you're open with it. So, we're very happy for them to talk to you and and vice versa. Um, I think what would be good though is if we wait till we get the hand over pack from the design, that will be the finalized screens and stuff like that. Statworks will know a bit more about what's going on from the design point of view. I think that will be a good point to touch base then you'll know a bit more about what you want to build and how you want to build it. I think that'll be a good discussion point about how they can make sure that's baked in as well. um because I not put any specific requirements into caching anything or anything like that for them but obviously they know the AI is coming and it's going to be part of it so it'll be good point then to discuss with them I think and see if we can get some sort of action plan with them if you're open to

  
  

### 01:06:53

  

George Westbrook: Perfect.

Brett StClair: uh umbrellas doc APIs and vector index docs by API for AI search draft API for the knowledge engine. This is the your

George Westbrook: this I think this I think this was one of the parts of this was about when we were talking about the

Brett StClair: CMS.

George Westbrook: AI optimized docs um which I think we kind of we kind of pushed pushed a bit down the road didn't we um because that would be more of like an internal internal ops thing but I suppose it really it's just I'm assuming and Barco's got an API which

Michael Moores: Yeah.

George Westbrook: which we can access um in order to update stuff. So cuz I think to be honest re realistically that LLM's txt is going to be in embraco as

Michael Moores: Yeah, I think um obvious we've seen it.

George Westbrook: well.

Michael Moores: It's pretty much functioning correctly. Um, so they've done all the work. They've done a load of component mockups as well in in Umbraaku. Um, so when we render the documentation, they can see you very well.

  
  

### 01:07:58

  

Michael Moores: We've got a UAT environment. We can show you how it looks like as well. Um but ultimately the requirement was that there was an API for you know AI purposes anyway. So that should be there. We are working on getting the paid account set up for Umbrau. So that will be happening soon. They will have a full non-trial version. Then that will be in the cloud. So we're not hosting that but that's going to go in the cloud with Umbrau. U just better support from you know where we hosting as well. So yeah, we can give you all that information. You can start looking at how that will be. But yeah, I didn't think about what LM would make sense in the Umbra. That would be limited um stuff for Statworks to do. I think obviously host that as well. Um you know, we can even put a static file there for launch. Um I think is a good is a good start.

  
  

### 01:08:50

  

Michael Moores: So I'll confirm that with them. I think that's a good idea that we'll have Umbrau do that. Obviously they can link that up from LM's point of view. That will then allow them to put like a a document in place already so that it's working. We can see it. And then what we can do is before we actually put this live is potentially um collect a static version we yourselves based on our documentation um and put that in for now and then as we get the autogenerated at least it's there in the backgrounds there. Yeah, let me confirm that to them and make sure they get the placeholder for that as

George Westbrook: Yeah.

Dorte Dye: Mike,

Michael Moores: well.

Dorte Dye: should we share the link to the UAT that the team can look at? And I just posted in the

Michael Moores: Yeah, yeah, it's it's I'm pretty happy with it actually.

Dorte Dye: chat.

Michael Moores: So, obviously the formatting is not there yet. They're looking at very much functionality, but it's come a long way.

  
  

### 01:09:41

  

Michael Moores: It's got the you got a good look and feel of it. So, um yeah, we're pretty happy with it so far. So it's obviously the only blockers now are the ones I mentioned before from DT basically. So I think this should be open.

Dorte Dye: Yep.

Michael Moores: This is on Azure as well. So it's similar speeds that we're sort of getting from there. So um you can sort of see the stuff. So it's coming on

George Westbrook: Oh, nothing.

Dorte Dye: Sorry, I didn't want it to side rail. Oh, it was really nice that we had a meeting yesterday and they showed it to us like wow. And um just to uh clarify uh the handover from the console from uh super order will be on the 9th of July. So two weeks out then we should have everything there as

George Westbrook: Okay.

Dorte Dye: well.

George Westbrook: And because I think what what thinking about the process what we might do is just once we've once we've got that then we'll just try and replicate it so that when we want to test things like I said like the agent alerts or co-pilot it's I mean it's it's until stack works are done there might be there might be a little bit of delta but I mean it's going to look feel act exactly the same um we'll just get something spun up so that we can we can fire away and as soon as we know the differences

  
  

### 01:10:55

  

George Westbrook: Then off we go.

Dorte Dye: by the way.

George Westbrook: That looks cool.

Dorte Dye: The black the dark version looks much better.

Michael Moores: Yeah, it's our

Dorte Dye: The the the light really irritated me as he started.

George Westbrook: That I I I

Michael Moores: version.

Dorte Dye: I looked really bad.

George Westbrook: always look at things in dark mode. The issue is is say for example a website. If we're building a website for us, I will only look at it in dark mode and then someone else will look at it and be like, "George, this looks absolutely atrocious in light mode." I'm like, "Oh s***. Yeah, I need to remember to look at

Dorte Dye: Does it not work? You just try to uh change the mode because I have it on dark.

George Westbrook: it.

Brett StClair: Yeah,

Dorte Dye: I haven't even changed it to light yet.

Michael Moores: Yeah, I don't see button works, right? I said there's still stuff there,

Dorte Dye: Okay.

Michael Moores: but yeah,

Brett StClair: it's looking good.

Michael Moores: it's Yeah, dark mode is a lot better.

  
  

### 01:11:46

  

Michael Moores: Uh, but yeah, essentially, obviously, it's still very early days. It's just a dev. Yeah, it's a it's a dev, not even a UAT. So, it's it's literally just so we can feel how the development's going. Um, so this will change more than the UAT one would. At least you can see the sort of how far it is and stuff is working. So, uh, we're relatively happy with that so far.

George Westbrook: Yes.

Brett StClair: Peace.

Michael Moores: Yeah, we haven't even tested it yet. They've not in a position to do so. You know, on API reference, you can see there some of the issues we're having. So, some of the text is massive. Uh, you know, especially the side menu there. If you look at anything in the side menu basically um if you click on bin range or anything like that. So um some of this stuff they're fine but some of these are too long. So we're looking at making use of like summary and description.

  
  

### 01:12:31

  

Michael Moores: There's some fields that sort of detail missing basically that Starworks have fed back to improve this. Um but ultimately this is this is actually working from DT's API as well. This is full end to end uh to their dev.

Brett StClair: Nice.

Michael Moores: So it's pulling the API YAML is looking at it and and passing that as well.

Brett StClair: Yes.

Michael Moores: Uh obviously send request. We're still waiting on the public sandbox to your point as well. So it's connecting up quite nicely so far. But yeah, we'll uh that that URL we're using.

George Westbrook: Right,

Michael Moores: So I'll let you keep that and uh we'll go from there.

George Westbrook: I'm going to put this in our Slack because I know for a fact we will we

Brett StClair: Oh yeah, it's

George Westbrook: will There we

Brett StClair: getting

George Westbrook: go.

Dorte Dye: Is your AI agent not automatically picking it up when it makes the meeting notes and then puts the link into the documentation?

George Westbrook: I don't we don't I I don't

Dorte Dye: Don't tell me you I found a flaw here.

  
  

### 01:13:26

  

George Westbrook: know because I think it's just recording the speaking.

Brett StClair: speaking. I do know and it's just doing the speaking.

Dorte Dye: Woohoo.

Brett StClair: It's a fail. You know what?

George Westbrook: You failed. Yeah.

Brett StClair: I knew flipping Jan is

Dorte Dye: Put

George Westbrook: Yeah.

Brett StClair: rubbish.

George Westbrook: It's a fad. It's a fad.

Dorte Dye: on.

Brett StClair: Um, okay. Where we console component library handle address react mi mui components for the agent to render generative UI. that was in the full Gentech stuff. Um, George, I'm wondering if uh you share your screen if you've got an expanded view. It might be easier because it's somehow degrading the description as we go

George Westbrook: Um,

Brett StClair: along.

George Westbrook: mine doesn't look as user friendly as that unfortunately, but I will pull it up. Wait, let me put it on this Um. Oh, zooming in the wrong thing. What number was that?

Brett StClair: uh 35

Dorte Dye: Okay, I can't read a bloody thing

  
  

### 01:14:50

  

Brett StClair: enough.

Dorte Dye: now.

Brett StClair: I'm finished.

George Westbrook: 35 that did that. I need to compare it to this.

Brett StClair: It was the console component library handle.

George Westbrook: There we go.

Brett StClair: There we

George Westbrook: Yeah. Yeah. Yeah. So,

Brett StClair: go.

George Westbrook: it's b it's just the I don't think that' be too much of an issue because the it's basically just going to be there is going to be components that we will copy. We might change slightly. Um, so let's say it's a let's say it's like a graph for example and on on the page it might be from one end to the other and obviously in a chat window we might want it only in the in limited in size. So there might be things that we might need to change. So there's probably going to be some shared some unique components and then all that happens is is when what the what the agent does rather than it say writing the code for the component which you can do but obviously there's a lot of variability in that it just it it basically just creates the arguments for the component and then when the message come back comes back it's like right fetch me this component and then put in these arguments and it's fully interactive as well.

  
  

### 01:16:18

  

George Westbrook: So if it's if it's say a um show me my card programs, it renders a component with five card programs. Then you can click into the card program and pop up a modal which shows some information and things like that. So that's where there might be it might be a bit more unique. Other times it's going to be right we have a button for approving a request. We just use the same buttons that you already use.

Brett StClair: So this is then the partner reliance. Is there something that we require from the partners either stack works or super ultra on that a design component or

Michael Moores: Yeah, I think so. Obviously, Super Ultra I I can send you the developer portal one so you can see if it's enough for you. Essentially they provide a handover pack which is like UI components in Figma. Stack works say it makes it very easy for them to develop against. So should be very similar. So we can give you that portal one so you can see it.

  
  

### 01:17:15

  

George Westbrook: Hm. it

Michael Moores: The console one is coming at some point but essentially yesworks have been able to render what you see there very quickly off the design. Um, so I'm hoping that will give you enough that you but I'll send the portal over make sure it's you're happy with it uh and the structure of it and then if we need anything slightly different for the console we can then discuss with super ultra all works then. So, let me send that across to you and uh see

George Westbrook: it so in in the Figma is that going to be slightly different or slightly more high fidelity than

Michael Moores: that.

George Westbrook: what was in the lovable example that they showed or is it one and the

Michael Moores: No.

George Westbrook: same.

Michael Moores: So, the lovable is purely the prototype. From there,

George Westbrook: Okay.

Michael Moores: they then make those models and they're more frameworks rather than every single page. They're framework page, frameworks of a button,

George Westbrook: Yeah.

Michael Moores: that sort of thing. So, yeah, it should be um exactly what you need.

  
  

### 01:18:05

  

Michael Moores: The statworks have even said that you know if we want to change something they don't need to go back to super ultra. So they have that model and superl and statworks work together all the time. So they good working relationship but ultimately yeah if they want to do a new page they can do with existing

George Westbrook: Yeah.

Michael Moores: frameworks. Um it's only if there's any large redesign that they need to go back.

George Westbrook: Okay.

Michael Moores: So it should give us need to to your point make different components that look essentially the

George Westbrook: Yeah.

Michael Moores: same.

George Westbrook: Because what what could be quite handy is having having both. I don't know if um if that lovable version that they've done they want to want to give away. Um but for for us what we do is just let's just assume that the the structure was the same like so this page would have XYZ on it. This page would have XYZ on it. this corresponds to these Figma um Fig components and then just basically build it in

  
  

### 01:18:58

  

Dorte Dye: I'm sure we can give you access to the the lovable accounts.

George Westbrook: parallel.

Michael Moores: Yeah,

Dorte Dye: I mean, I can ask for that.

Michael Moores: I said I've already got the code for the portal.

George Westbrook: Oh,

Michael Moores: So they So they as soon as this finishes I'm I take everything off them.

George Westbrook: perfect.

Dorte Dye: Okay.

Michael Moores: So I've got the portal.

George Westbrook: Okay.

Michael Moores: Um I've convert I'll send you the raw. I've just converted into something I can deploy. But they've got the raw code and we've got the the handover pack. I'll send you out for the portal. I've asked for exactly the same thing for the console as well. So just you know in case we want to do any sort of future prototyping, we can mock it up and stuff like that. Um because it's all hosted by them. So I've asked them already for that. So they'll be we'll be providing that for the console. But let me send it to you so you can see what you could be getting, see if it works for you um and go from there.

  
  

### 01:19:45

  

George Westbrook: like perfect. Um next

Brett StClair: 36 A2A provider enablement direct ATA connections

George Westbrook: this is

Brett StClair: from providers MCP as a message fall back in the meanwhile anthropic providers is

George Westbrook: so what what that is is so 80a is something some people use not many but how do you provide that or agentto agent experience in the absence of A2A and then I think it's just using an MCP server as that fallback. So let's just say it's so what would A2A be? You'd have like a there's some aspects where it's about if you imagine you've got like thousands of agents and then there's some discovery aspects blah blah blah. Um but then also there's like the communication protocol. I mean, all we could do is it'd be like an MC this getting like matrix stuff. Um, an MCP server on top of our MCP server where there'd be like maybe one or two tools exposed. Um, and then all we do is pass through the message. So it just be rather than let's say query um query this endpoint, it would just send the LLM would send a text message um via MCP to our agent which would then use our main MCP server to do the work and then feed it back into into Claude or chat GPT.

  
  

### 01:21:19

  

Michael Moores: Yeah, that sounds

George Westbrook: Um, self-healing code ownership.

Michael Moores: good.

George Westbrook: Where is that one? Just jumbled it up.

Brett StClair: code is suffering is off the table now.

George Westbrook: Um,

Brett StClair: DT owns the code base and over Sapion lacks log data to access. Focus is for self-healing docks and

George Westbrook: I think we can have the self-healing aspect on our side.

Brett StClair: knowledge.

George Westbrook: um that would just be let's just say um API changes, we've got an MCP server um that's querying that endpoint. We get a 422 error. Um the agent sees that, flags it to us in Slack. We could diagnose it. Goes looks in the vault or wherever the YAML is, looks at the change of fields and then fixes it in a 5 10 minute process. It's I just I love it when I get those notifications when I'm just about to go to sleep and I'm like,

Michael Moores: Yeah.

George Westbrook: "Oh s***." Right. Click diagnose in in Slack and then fix. But it's quite nice that it's not all panic stations.

  
  

### 01:22:33

  

Michael Moores: Yeah. Yeah. I think obviously from a TXM, you know, if we do take over the development, we're we're very interested in this. So I think as we just sort of think about this, how can we make sure we can potentially use it later? I guess is it works in your side but you know if we can expand it to different piece pieces of the code as

George Westbrook: Yeah.

Michael Moores: well and stuff like that just so we can have that whole self heaving we just add sort of DT console

George Westbrook: Yes.

Michael Moores: whatever it may be because ultimately you know when if we do take this over it'll be sort of in a small capacity to start with but on our side and at least we can you know at worst we can say okay just raise these issues um obviously we need to discuss with DT about the codebase access

George Westbrook: Yeah.

Michael Moores: and stuff like that But we can say, you know, we we found these issues. Can you fix them? I think that's a good sort of maybe crossover point.

  
  

### 01:23:22

  

Michael Moores: And then obviously we can go into the full thing basically. So yeah, sounds

George Westbrook: Um then I think that's everything on the partner dependencies and then I think the only things that

Michael Moores: good.

Brett StClair: Yeah.

George Westbrook: really left it's kind of for us to us to decide is the I pull this version up. It's just kind of like open open design decisions. um which realistically I think is is something that we'll cross off as as we go along. Um like it's the say permission model for MCP. Um that's I think going to be an open discussion that's going to going to change with testing and simulating it as well to see what once we've got like the high priority so high um high risk actions what does the agent do? should be allowed. Some users do it, some users not. Um, which I think is only really going to come out in in testing and a bit bit further in uh yeah, down down the line, I think. Um, right.

  
  

### 01:24:27

  

Michael Moores: Perfect.

George Westbrook: Yeah. So, I think that's I think that's all of the open questions done.

Brett StClair: Uh yeah, there's yeah, a whole lot of those design questions,

George Westbrook: Yeah,

Brett StClair: George.

George Westbrook: I I was just I was just saying that the they're they're they're probably imple they're they're more for us when we're when we're in the weeds.

Brett StClair: Yeah. Yeah. out you're right just having a look at them these easy.

George Westbrook: Um

Brett StClair: Okay. So what we'll do is we will ingest this uh meeting update the gap register and then polish off the vault and then from there I'll regenerate the proposals. Um I'll send you a message once the vault is ready for a review. Um, if you can take the next week or so, go through it. If there's anything that's glaring, um, highlight as you highlight it, it'll pop into a review mode and you can leave a review if there's something that you're not sure on or don't like or want to leave out or hasn't been added.

  
  

### 01:25:43

  

Brett StClair: Um, then we'll do one last kind of wraparound on the vault and then the vault will be ready to go. Um, and then what I'll do is I will package up for tomorrow um, uh, a bit of a proposal and get that sent to you and then let's lock and load a date next week and we can review the vault and go through the proposal as well.

Dorte Dye: Sounds good. Did we had a session for next week already booked in? I can't really recall if we

Brett StClair: I think hey,

Dorte Dye: stop.

Brett StClair: let's just let me just pull up my diary quickly.

George Westbrook: I can't see it.

Brett StClair: What's my computer doing? It's just clicks bombing out this

Dorte Dye: I think we stopped this week with the gap. I can't see anything.

Brett StClair: week. Um, okay. Let's pop something in then. Um, uh, Wednesday or Thursday?

Dorte Dye: Um, let me just look at the diaries because Oh, we have foxes. So, next Wednesday 10:00 looks free 24th.

  
  

### 01:26:51

  

Brett StClair: Perfect. Does it suit everyone?

Dorte Dye: I mean from our end yes because I have Ian and Mike's

Brett StClair: Perfect. Um,

Dorte Dye: calendar.

Brett StClair: so it is a final bolt review with proposal review.

Dorte Dye: I just got feedback from DT on the presentation. They're working on it. They're not comfortable with sharing it. So, I don't know.

Brett StClair: That's

Dorte Dye: You didn't you didn't took enough screenshots,

Brett StClair: okay.

Dorte Dye: Mike, did

Michael Moores: No, I mean I did say that I was going to raise it with Brett and the team.

Dorte Dye: you?

Michael Moores: So I think we can push back again is that if they want the comments they need we're not not saying it's sort of a finalized one. We need the feedback from them I think.

Dorte Dye: Okay.

Michael Moores: So I think we want to raise we if we can sort of force the hand to send that I think

Brett StClair: I'll also upload all the stuff you sent me last week,

Michael Moores: so.

Brett StClair: Mike. And we should have everything there then. Um, and then everything's pretty much captured. I'll ping you once it's done. It'll probably be tomorrow afternoon sometime.

Dorte Dye: Sounds good.

Michael Moores: Yeah. Great.

Dorte Dye: Okay,

Michael Moores: Thank you.

George Westbrook: Perfect.

Brett StClair: Super.

Dorte Dye: thank you so much.

Brett StClair: Thank you everybody.

Michael Moores: Yeah. Take care.

Brett StClair: Chat.

Michael Moores: Bye.

Dorte Dye: See you next week. Bye.

George Westbrook: Thank you very much.

Brett StClair: Thank you.

George Westbrook: Have a good one.

  
  

### Transcription ended after 01:28:38

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

**