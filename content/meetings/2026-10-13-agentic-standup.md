---
date: 2026-10-13
type: standup
description: "First release of the co-pilot executing live API calls with an approval step, a dedicated UAT at last, and the knowledge hub launch date going open-ended"
scope:
  - "[[developer-support]]"
  - "[[agent-access-layer]]"
  - "[[architecture]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[portal-co-pilot]]"
  - "[[docs-mcp-server]]"
  - "[[approval-queue-integration]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-13)

> **Source:** Gemini transcript, 13 October 2026, 15:29 BST, 23m. **Hasan Ahmed** and **Brett StClair** with **Michael Moores**. **George absent**, on a train. **Ian travelling** this week.
>
> Brett and Hasan presented from a coffee shop. The office had been evacuated for a real fire and, on Hasan's account, there is *"literally nothing left"*. The demo ran over a phone hotspot, which slowed several steps.

## The co-pilot ships its first release, and it executes

Everything promised on 6 October and still pending on 8 October is now built. Brett: the team *"pushed through this weekend"*, and it is **in production phase but sitting in UAT**, tested, with the API integration and the deployment into the Stackworkz console the only pieces outstanding.

Brett set expectations honestly: *"it is the first release of it. So, I'm sure we're going to find problems with it and we'll continue to iterate it."* Hasan named his own open bugs twice during the demo.

### What Hasan demonstrated

| Step | Behaviour |
|---|---|
| **Ask a question** | *"How do I issue a card"*, and the agent walks the process |
| **Version awareness** | It states that the API has been updated and what changed in the payload, **and tells a developer on an older version that a newer one exists** |
| **Example payload** | Produced on request, with the request body shown |
| **Execute against the sandbox** | The agent runs the call itself, returning **the input, the output and how long it took** |
| **Take it elsewhere** | Code is offered for copy and paste, so a developer can run the same call in Postman |
| **Follow-on tests** | It then offers further options, for example a virtual card, fetching that payload and testing it too |
| **Approval before execution** | The account ID and card type are shown for review: *"if you think it's good, you can approve it"*, then it executes |

Michael's verdict: ***"No, I think it was great."*** And at the close, ***"I think it looks great. Thank you."***

Two small items Hasan raised against himself: the page does not always open cleanly before a test runs, and the execution status renders too small and too far from the buttons.

## A dedicated UAT environment, which is the fix #93 was asking for

Michael named the cause of the moving-build problem plainly. The API has been running in **one environment shared by development, QA and what was being called UAT**, so it changed *"sort of every day."*

> *"We are building a dedicated UAT now which means that we can give you a more stable version that has been through QA rather than changing sort of every day."*

Due **14 October**. Two further changes come with it:

- **Dedicated API credentials for Novosapien**, split from the console, so keys can be rotated without affecting anyone else.
- **Sign-off of endpoints as they pass**, so Novosapien can confirm its calls land correctly against something fixed.

This is the structural answer Dorte asked for on 17 September and nobody had offered. See [[open-questions]] #93.

**The cost of not having had it:** *"we've had about two weeks block so far on UAT testing with these issues we've had."* The overlap was wasteful in a specific way, Michael raising defects DT had already fixed, so TXN stopped testing rather than keep duplicating.

## The launch date has gone open-ended

Brett asked directly whether the launch date still held for the developer portal. Michael: ***"I'd say no at this rate."***

The position, in his words:

- **Launch and go-live are separate dates.** It does not need to be perfect until the full go-live.
- The gate is **the first five endpoints**, *"which are like what I consider core to transact"*. When those are done, the knowledge hub launches.
- **Nothing is signed off yet** and there are *"quite a few defects on each"*. DT was due back with timelines that day.
- The knowledge hub itself is **finished and in production**, *"all deployed and done from a code side of it"*. What is missing is the back-end sync working against the YAML DT produces.
- Marketing is ready and waiting: Michael has **about 50 pieces already written**, to be chosen once the launch scope is known.

Ian's standing position, as Michael relayed it: *"we can go live today if we really wanted to, but we have to have some differentiation and something to sell."*

## The AI layer has overtaken Direct Transact

The consequence matters more than the delay. Michael: ***"it does look like we are ahead of sort of DT at this point."*** And therefore:

> *"We did plan this knowledge hub as like a later phase but by the looks of it it's probably going to be much closer to launch having the AI functionality in then than it was before."*

So the co-pilot moving into the launch is now the likely outcome, arrived at because DT slipped rather than because anyone chose it. That is the question at #105, which was waiting on Ian, being settled by circumstance. New row **#109** records the difference, because a decision taken by default is not the same as a decision, and the commitments that follow are real either way.

## Novosapien takes the llm.txt, and Stackworkz populates it

Answering Michael's email, Brett confirmed it will be **easier for Novosapien to control the llm.txt from a consumption point of view**, with **Stackworkz populating it** and **DT doing the API versioning**.

Hasan gave the reason, which is about update latency rather than ownership:

> *"If we are going to integrate all of the MD files it'll be a lot easier on our side, because then if there's any updates then we are to update the MCP server and our agents as well. Instead of, if there's an update, we need to speak to the Stackworkz and then it's a lot of back and forth."*

Michael agreed and put it on the 14 October agenda with Stackworkz. This confirms the local filesystem representation of the docs recorded at [[docs-mcp-server]], and makes the refresh path an internal one.

## Stackworkz built the permissions layer, and want the agent to route through it

Michael reported that **user permissions are built and demoed**, not just specified in the documents he sent earlier.

The part that affects the agent architecture:

> *"They have basically a layer over the API that has the access as well. So it has approval queue everything built in. So their sort of suggestion was coming through that back end and routting that accordingly basically."*

Michael has asked Stackworkz to explain it to Novosapien directly. **The open piece is authentication:** *"the main one for us is how how to authenticate through that."* New row **#107**.

This is consistent with the 15 September position that approvals follow the Console permission model, and it makes [[approval-queue-integration]] a question of integrating against a built surface rather than agreeing a model.

Also noted: DT being stuck has slowed Stackworkz, who cannot sign off pages until the endpoints behind them work, so they have **paused page work and concentrated on the core and the permissions**.

## The review audience widens, as it did for the knowledge hub

Michael wants to repeat what worked. The knowledge hub ran **two rounds of structured testing** and the feedback was *"really valuable"*.

- **Testers from both DT and PayCorp**, a deliberate spread *"from technical background to to not so technical"*.
- **Dorte picks the pool**, Michael writes the test cases.
- First, Michael and Dorte review it themselves. Ian is travelling this week.
- Hasan offered access through the admin panel in the meantime.

Worth noting against #93: this round can now be ring-fenced in a way the last one could not.

## Findings and where they landed

| Finding | Destination | Action |
|---|---|---|
| **First release executes API calls against the sandbox**, returning input, output and timing | [[portal-co-pilot]] | Recorded as delivered |
| **An approval step before execution**, showing account ID and card type | [[portal-co-pilot]], [[approval-queue-integration]] | Recorded |
| **Version awareness is built**, warning a developer on an older version | [[portal-co-pilot]], [[open-questions]] | **#101** moves to partly built |
| Copy and paste code for Postman, and follow-on test suggestions | [[portal-co-pilot]] | Recorded |
| **Dedicated UAT environment due 14 October**, plus split credentials for Novosapien | [[open-questions]] | **#93** narrowed, cause and fix both named |
| **Two weeks of UAT lost** to QA and UAT running over each other | [[open-questions]] | Recorded at #93 |
| **Launch date open-ended**, gated on five core endpoints with nothing signed off | [[open-questions]], [[delivery]] | New row **#108** |
| **Novosapien is ahead of DT**, so the co-pilot likely lands at launch | [[open-questions]] | New row **#109**, touches #105 |
| **Novosapien controls the llm.txt, Stackworkz populates it**, DT versions the API | [[docs-mcp-server]], [[architecture]] | Decision recorded |
| **Stackworkz permissions layer built**, with the approval queue in it, proposed as the agent's route | [[approval-queue-integration]] | Recorded |
| **How the agent authenticates through that layer is unresolved** | [[open-questions]] | New row **#107** |
| Review widens to DT and PayCorp testers, Dorte picking the pool | [[open-questions]] | Recorded at #93 |

### Context, no action

| Finding | Note |
|---|---|
| The office was destroyed by fire | Brett and Hasan presented from a coffee shop. The demo ran on a hotspot |
| George absent, on a train | Second standup running without him |
| Ian travelling this week | Michael and Dorte review in his place |
| Knowledge hub code is finished and in production | Only the back-end YAML sync is outstanding |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Stand up the dedicated UAT environment | Michael / DT | Due 14 October |
| Issue Novosapien dedicated UAT API credentials | Michael | Split from the console, rotatable |
| Explain the permissions layer and its authentication to Novosapien | Stackworkz | Michael has asked them |
| Agree who populates the llm.txt, and how | All three | On the 14 October agenda |
| Pick the UAT tester pool and write the test cases | Dorte and Michael | Spread of technical and non-technical |
| Confirm the five core endpoint timelines | DT | Was due back 13 October |
| Iron out the page-open bug and the status placement | Hasan | Raised against himself |

---

## Transcript

Oct 13, 2026

## **TXN \- Agentic AI SU \- Transcript**

### **00:00:11**

**Brett StClair:** are they? For f\*\*\*\*\* sakes. What? Uh, yeah. You know what I say about common sense? Yeah. It's not that common. Hello there.

**Lily StClair:** Hello.

**Brett StClair:** That would go. Can you hear in the background?

**Lily StClair:** No.

**Brett StClair:** Good. You let that night take us in. Okay. I let Mike's not take it in because he likes to go his own.

**Lily StClair:** Wait, what happened? What happened at the office

**Brett StClair:** Fire like full on fire. They kicked everyone out and we can't get back in.

**Hasan Ahmed:** whole thing but

**Lily StClair:** for the rest of the day?

**Brett StClair:** And it was the son who started it, but he won't admit it. We're not complaining now.

**Hasan Ahmed:** yeah I think stepped away for like an hour I came back everyone's outside the

**Brett StClair:** He was having a poo and he was playing with his lighter and tissue paper and it all went out of

**Hasan Ahmed:** Yeah.

**Brett StClair:** hand.

**Hasan Ahmed:** As in like everything's burned down.

### **00:01:25**

**Hasan Ahmed:** So like if like if you come to the office there's literally nothing left.

**Brett StClair:** We're not complaining though. We're working in this lovely coffee shop. It's really nice.

**Hasan Ahmed:** Yeah.

**Brett StClair:** Is this kind of coffee shop?

**Hasan Ahmed:** A lot of coffee being drank right now.

**Brett StClair:** Hello. And after this we've got um a very important meeting called I forgot what it was called. Business exit exceptional run.

**Lily StClair:** Except

**Brett StClair:** Figure that out.

**Lily StClair:** the night pending.

**Brett StClair:** No, it's mommy's birthday.

**Lily StClair:** Yeah, true.

**Brett StClair:** Hello, Mike.

**Michael Moores:** Are you okay?

**Brett StClair:** Good. We're presenting to you outside our offices because we have a fire alarm. And turns out it's a real fire alarm and we think it's George.

**Michael Moores:** Oh, wow.

**Brett StClair:** We think he started it.

**Michael Moores:** Wow.

**Brett StClair:** and it went on and on and we wait try to wait it out but it turns out not a wise idea. So apologies we are outside the building. We managed to find a quiet little spot.

### **00:02:42**

**Michael Moores:** There it is.

**Brett StClair:** Uh trying to improvise here. And luckily as I was leaving, my son was out for lunch.

**Michael Moores:** Very

**Brett StClair:** So I saw his laptop and I thought, "Oh, not letting this thing be thrown down." and took his laptop too.

**Michael Moores:** good.

**Brett StClair:** Do you know what is amazing though? We're sat near a train station and there is actually people leaving to go home from work at half three. It's amazing. Do you think it's cuz they've just gone building shut down? We're out. They just walk. I just think they're lazy.

**Michael Moores:** Excuse me.

**Brett StClair:** Half is impressive to be on a train high. Um so very quickly Mike um just a quick response to your email. My son will send you a full-on email but um yes is the answer and most likely it'll probably be easier for us to control the llm.txt as in from a consumption point of view. Um, Hassan will detail out kind of what we think is the best way, but I think it's a really good point to talk about tomorrow with the um, stack works guys on them kind of populating it.

### **00:03:56**

**Brett StClair:** We're consuming it. DT is doing the API kind of versioning and all that kind of stuff. We're already pulling and looking at how we manage all the versioning as well. I think that'll work quite nicely. HasanI summarize the son gave me the technical version. And I went, "Yes, I think I get it.

**Michael Moores:** No,

**Hasan Ahmed:** Yeah,

**Michael Moores:** this is not

**Hasan Ahmed:** I mean to be fair I mean yeah that's just uh like he like all it's just um if we are going to integrate like um like all of the like MD files it'll be like a lot easier on our side because then if there's any updates then we are to update the MCP server and our agents as well all as in like as in like it's just easier like instead of if there's an update we need to speak to the stack works and then it's a lot of back and forth.

**Michael Moores:** Yeah,

**Hasan Ahmed:** Yeah.

**Michael Moores:** sounds good.

**Hasan Ahmed:** Okay.

**Michael Moores:** Yeah, yeah, we can talk about it tomorrow as well.

### **00:04:53**

**Michael Moores:** Um, but sounds good for me.

**Hasan Ahmed:** Yep.

**Brett StClair:** Um, so the team basically pushed through this weekend for you. We've tried to tick off and complete as much as we possibly can barring the actual API integration and getting it deployed into the stack workspace.

**Michael Moores:** All

**Brett StClair:** Um, so I think we've done pretty much everything. So, we want to demonstrate it all to you. Um,

**Michael Moores:** right.

**Brett StClair:** it's all kind of in production phase, but sitting in UAT. It's all kind of ready to go. We've run a bunch of tests. It's feeling good. Um, it is the first release of it. So, I'm sure we're going to find problems with it and we'll continue to iterate it. Um,

**Michael Moores:** Yeah.

**Brett StClair:** but shall we jump in and do you want to share your screen and let's go through the work that you guys punch through? George isn't able to join us.

**Hasan Ahmed:** Okay,

**Brett StClair:** He's on a train at the moment. He might jump in. Um, but again, it's just been we figured you've got a deadline probably looming up this week.

### **00:05:56**

**Hasan Ahmed:** let's make sure up as much as

**Brett StClair:** So we've done as much as we can on our side and all that it requires is some kind of integration and then talking with stack works our best to get that integrated along with your ideas but actually get

**Hasan Ahmed:** I did that.

**Brett StClair:** the code in.

**Michael Moores:** Yeah.

**Brett StClair:** Um and I'm sure there'll be a bunch of debates on how best to do it. Um kind of feeling part of me is feeling let us act with the code and let us do some quick changes might be the quickest way because we'll do it all at gentrified. Um,

**Michael Moores:** Hey.

**Brett StClair:** but again it it depends on kind of where you guys and them land with it, I guess. But I think it's looking very good at the moment.

**Michael Moores:** Yeah.

**Brett StClair:** We've had a quick go through yesterday and it was looking fabulous. And I know the changes you tidied up today look amazing. It's over to you.

**Hasan Ahmed:** Yeah. So in terms of updates um so like all it

### **00:06:47**

**Michael Moores:** Heat.

**Hasan Ahmed:** is is um if you were to speak to the actual agent like it would be be able to execute like API calls as well. So if I just start with an example like how do I issue a cards um and there's a few updates in here as well. um be just like a process. Um I think it's on God right now, so it might take a few seconds, but um I mean I tried to add in the like example of if there's update to the API like it will tell you that then there's update onto the actual API spec and so then it will as like it will kind of let you know in like advance.

**Michael Moores:** Yeah.

**Hasan Ahmed:** Um let me just let this load. Um as in so over here like it would just kind of give you like a bit of overview like there's an update to the API. Um it's updating the the actual payload for example. Um as in over here just to kind of thing let you know that even if you're on like an older version that there is a updated version which you are able to use as well.

### **00:08:06**

**Michael Moores:** Yep.

**Hasan Ahmed:** And then for this new part, it was um can I let's see can I test payloads? Um if you give it a second, it will ask you to go through the the the actual try

**Michael Moores:** Good.

**Hasan Ahmed:** section or if you ask the actual agent to execute the entire thing for you, it can do that as well. So just give me a second. Open the page first. Um I mean it is open. I mean like I need to find out that's like a a small bug. But if I say can you test I mean like it will give you the like example payload. It will give you like the the entire execution and then the actual output as well. So give it a second.

**Brett StClair:** I think it's our Wi-Fi connection.

**Hasan Ahmed:** Is it? Oh yeah. Yeah. So I mean I'm on my hotspot but out here is it's a bit slow but as in um over here it will execute like a payload.

### **00:09:36**

**Hasan Ahmed:** It will give you the output and how long like it actually took as well. Um I think it executed too. I mean there are small like as in a smallish I mean actual the bugs which I need to iron out but like it should be pretty simple but it will give you the actual input and then the output of like um as in after executing it. So like here's the entire output and then like here's all of the input information and then it'll give you like a code as well. So if you want to test it as well but on your own like a post line or something it will also be here if you want to copy paste it in. Um so let's say if and then after this it will give you a few more options if you want to do like I'm doing more testing. So if you want to do like a virtual card as well it will get that payload for you and then also test it on the actual sandbox. Uh yeah, there's there's a few things I need to add still, but then like it'll give you the input for that here.

### **00:10:57**

**Hasan Ahmed:** And then if you want to approve it, so if you go through it, you want to see the account ID, the actual type. If you think it's good, you can approve it. And then like it would do like a bit of thinking and then it should execute for you. And then it will and then it will execute for you. It will say like 2011\. I mean up here like it's a bit small. I mean if you want to make it a bit more prominent like be to have it like down here um like a bit closer to the buttons itself. And then here will give you the example the request the output as well. Yeah. Um I think in terms of like API testing, um I mean I mean I guess we need to integrate like a bit more into the stack works and so that we like are able to do actual testing on the actual sandbox Hands. umbrella as well. But other than that, if you have any questions on how it looks, how it feels, if you want anything change from it, but yeah.

### **00:12:07**

**Michael Moores:** No, I think it was great. Obviously, yeah, I think the next steps would be for us us three internally to to go through that ourselves and just have a look.

**Hasan Ahmed:** Yeah.

**Michael Moores:** And I think we're kind of keen to widen that up a bit like we did for our knowledge hub. So, we've got some sort of testers in both DT and uh Pay Corp that could probably test as well. So to sort of widen that audience to get a proper sort of review process going.

**Hasan Ahmed:** Yeah.

**Michael Moores:** So when you're happy and if you if you're happy for that u we can schedule that and see I'll get data to um look at the pool of people you want to do and come up with some

**Hasan Ahmed:** Yeah.

**Michael Moores:** specific test cases for them to do that and we got quite good feedback last time on the knowledge hub. So I think that would be good place to go through.

**Hasan Ahmed:** Okay. Yeah.

**Michael Moores:** Um but I think yeah the next sort of steps for me obviously we are had a bit of an issue with the API because this the same environment that's they're developing and QA in and what was kind of UAT so we are building a dedicated UAT now which means that we can give you a more stable version that has been through QA rather than changing sort of every day which is what it has been doing.

### **00:13:15**

**Hasan Ahmed:** Yeah.

**Michael Moores:** that should be built by tomorrow.

**Hasan Ahmed:** Okay.

**Michael Moores:** And then what I'm pretty keen on doing is giving you obviously to split you up from the the console and the dollar. So get you dedicated access to the API for your own JT um access. Obviously if we do need to swap or rotate any keys, it's easy to you sort of split them stuff up as well. So um we can give those credentials out into the UAT environment

**Hasan Ahmed:** Oops.

**Michael Moores:** and then get you sort of map into the the API. exactly and see how it performs. Obviously, we still got quite a bit to go with the API itself. Um, we having quite a few issues with the stability. I think mainly because they're still QAing and and making changes. So, I'm hoping tomorrow the UAT is a bit more stable. Actually, works will be step one. And then we do still need to go through the UAT testing. So,

**Hasan Ahmed:** Okay.

**Michael Moores:** we've had about two weeks block so far on UAT testing with these issues we've had.

### **00:14:11**

**Michael Moores:** So, I'm hoping to start as of tomorrow and then try and get some stuff signed off for you so at least you can start confirming those sort of stuff work and and hitting properly basically.

**Hasan Ahmed:** Yeah. Yeah.

**Michael Moores:** Um, so yeah, I think that's the next step from us and obviously I'll speak to DA on potentially getting someone or a group of people to do the UAT kind of testing. Um, I think it was good to do. We did two round of knowledge of last time and it was really valuable to to get that feedback and stuff. So, um I'll see who she wants to give out to and we can go from there and that would be the best way of getting feedback I think to start with. Um we pick a variant of different people of different skills and stuff. So, I think it results quite nicely from technical background to to not so technical. So yeah, I'll speak to her and we'll try and get that arranged and um you know once you're ready just let us know where it's going to be deployed or where the best place to test it is and stuff like that from a UAT standpoint and then we can go and speak to whoever's testing that.

### **00:15:10**

**Michael Moores:** I'll make the uh make the test cases

**Hasan Ahmed:** Yeah. Um I mean as I say if um if I mean I think if you want to access it it's on the admin panel. Um I I think recently check to tx um um I mean if you want to play around I mean just on your own or if you want to ask you can jump in to the paddling pum wants to add on. It should have give me a second. Yeah. So if you can click on her on the spot, I mean it should open up digital page and then if this whole time just have like play around just I mean it's going to have like a like a feel for it just to do some API testing and see if it goes to the page and everything.

**Michael Moores:** Yeah.

**Hasan Ahmed:** Yep.

**Michael Moores:** Yeah. Perfect. I'll take a look myself and get I think Ian's traveling this week, but me and D can certainly have a look and then once we've done that sort of prey testing and stuff um we'll make sure we've got a select group of users we can sort of get to do it as well.

### **00:16:56**

**Michael Moores:** Um and then we can come back.

**Hasan Ahmed:** Yeah.

**Michael Moores:** So I think it looks great. Thank you.

**Brett StClair:** So yeah, I guess ne um the next kind of steps is spend a bit of time with stack works. The pin for us is trying to understand and start stitching stitching up the console side of things.

**Michael Moores:** Yep.

**Brett StClair:** This will keep ticking and bits will come in and we'll iterate it. But now our focus is let's get this into the actual console. How's your where's your head space on that timing wise and um API wise?

**Michael Moores:** Yeah. So um I think from the console side um you know statworks are doing as much as they can from a from their side. So you know user permissions will probably be the next one that's good for you. Obviously they are finishing that build and that's under their control. So I think that's the major part for us in the first bit. So obviously we need to discuss with them on is it tomorrow?

### **00:17:55**

**Michael Moores:** I think it is. Um how we actually stitch that in. But then yeah user permissions they came back to me demoed it working. So probably good for you to see what they've done as well. Um, obviously I sent you those documents, but they've actually built it now. So, we can see how that works. I think the main one for us is how how to authenticate through that. So, I spoke to them the other week. They were quite keen. They have basically a layer over the API that has the access as well. So, it has approval queue everything built in. So, their sort of suggestion was coming through that back end and routting that accordingly basically. So they can I'm going to I've asked them to explain that to you how that works and we just sort of see how you know everything works from that side and then I think obviously from a DT point of view starts are a little bit stuck now with finalizing the stuff off. So the development for that is slowed down quite a lot.

### **00:18:46**

**Michael Moores:** So obviously before we can sign off every page we need to make sure it's actually working and you know stuff are coming back. So they have paused on a lot of that stuff and focused on the the core and the permissions that they can do. Um, so I think we'll have that conversation. Um, so both sides can get a bit bit of background and then obviously I've listed a few things from in my email, but I'm sure there's going to be more from each side as you explain your architecture and stuff like that and then we can go from there I think and probably have quite a few sessions but some more detailed um on each topic that comes up I think.

**Brett StClair:** Perfect. Happy.

**Michael Moores:** Awesome.

**Brett StClair:** And um your launch date, is that still looking good for the clical portal?

**Michael Moores:** Um I'd say no at this rate. Um we had a conversation with them yesterday. Obviously without this being signed off, we're not happy to sort of go ahead. So obviously the the launch is one thing and the go live is sort of kind of separate dates.

### **00:19:46**

**Michael Moores:** Um obviously we don't need it sort of working perfectly until the go live fully. there's still some sort of YAML issues that you know don't look great client facing. So it's very much we've targeted the five the first five endpoints which are like what I consider core to transact that's going to be our cus off point when they're done we'll be launching the the knowledge hub basically so it's a bit of an open-ended date right now um as of now there's nothing signed off quite a few defects on each so DTR coming back to today on timelines because they still doing QA testing themselves on those endpoints as well so obviously we're not going to do any more testing until we've got assigned our QA and we can proceed. So there's a lot of overlapping with the QA and UAT testing when we were doing it. So that's why we sort of took that break and step back um because you know we're we're sort of raising stuff they've already fixed. So it's kind of a waste of our time to to keep doing that.

### **00:20:44**

**Michael Moores:** Um so yeah, I'll know this week the dates that they plan to meet those those core as well. Um but it does look like we are ahead of sort of DT at this point. So from a connection to stat works obviously we did plan this knowledge hub as like a later phase but by the looks of it it's probably going to be much closer to launch having the AI functionality in then than it was before. So I just need to get those dates off them and then we can have a a speak about when we want to put it in and get that first sort of live version out. Obviously knowledge hubs all deployed and and done from a code side of it. It's got production. It's all ready to go. Uh, and it's been tested. It's just the back end syncing and making sure that works properly with the the YAML that DT produced. basically.

**Brett StClair:** Okay, good. That's good. The nice thing is you don't have like this set in stone have to.

### **00:21:40**

**Brett StClair:** You can play with it, which is good.

**Michael Moores:** Yeah, because Ian's always came out, you know, we can go live today if we really wanted to, but we have to have some differentiation and something to to sell.

**Brett StClair:** Yeah.

**Michael Moores:** So, you know, I've got about 50 odd guys that I've written already that just depends on what we're going live with, I'll sort of put up at the time. So, you know, we've got all the content there to to do a marketing launch, stuff like that. It's just whenever the API is in a, you know, when we consider stable state, we will then, you know, pivot pretty quickly and and get it going.

**Brett StClair:** Cool. Awesome. Mike, thank you.

**Michael Moores:** Awesome. Thank you. And I'll speak to you tomorrow.

**Brett StClair:** We'll see you tomorrow. Yeah.

**Michael Moores:** Cheers. Take care.

**Brett StClair:** Keep up.

**Michael Moores:** Have a good one. See you later.

**Brett StClair:** You too.

**Michael Moores:** Bye.

**Brett StClair:** Bye.

**Hasan Ahmed:** Cha.

**Brett StClair:** Cheers, Mike.

### **Transcription ended after 00:22:50**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*