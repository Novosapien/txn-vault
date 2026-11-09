---
date: 2026-11-06
type: general
description: "Hosting sync: the AI already runs in Novosapien's Azure for launch, DT come off future development, and Ian forecasts 18 months of support"
scope:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[commercial]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# Novosapien <> TXN: AI Hosting Sync (2026-11-06)

> **Source:** transcript from Lily's app, Friday 6 November 2026, 15:30, about 34 minutes. **Novosapien:** George Westbrook, Brett StClair, with Hasan Ahmed messaging George during the call. **TXN:** Ian Johnson, Michael Moores. Ian called it to agree the hosting in principle, which George had already said yes to.

## The AI is already running in Novosapien's Azure

**George, cutting it short:** *"We've already deployed it. It's already running in Azure. What we've done is we've taken the code that Stack Works have for the Knowledge Hub, put that in Azure, in our Azure just so that we can test it."* Most of the security is done; a few Azure Front Door items were left, and Hasan messaged during the call that *"all those issues I mentioned should be all sorted now."* What remains is connecting to Stackworkz's deployed version. That finishes the 5 November action ahead of its Tuesday 10 November date.

**The shape for launch, in Ian's words:** *"The Knowledge Hub will be in the DT environment. The AI service... will be in Azure environment hosted by you guys temporarily but essentially the way that they work won't be any different once we move the AI service into the DT environment."* The Knowledge Hub calls the agent service as an API. George expects only small changes when it moves, where DT have things locked down.

**Monday is now a connection call.** The Stackworkz, Novosapien and TXN alignment call on Monday 9 November, agenda from Dörte, becomes *"this is what we've got... how are you going to connect?"* George: *"by the end of the week it should, should all be done, tested and ready. For the 16th."*

### Technical points

- **SSE became WebSockets.** Azure ruled out one way of streaming the agent's messages to the front end, so it now uses WebSockets, in the code and in the Azure deployment. The front end connects through the **AG-UI** package, with a matching piece on the back end.
- **Region: North Europe**, which is Ireland. There was some confusion with West Europe, the Netherlands, which DT use for other services. George: *"if it needs to be another one we can switch it."*
- **Latency is not a Knowledge Hub concern.** Michael's worry is the Console in the long term. George: an LLM reply takes two or three seconds anyway, so an extra 100 milliseconds hardly matters.
- **Resilience.** Container Apps is managed and restarts itself. Brett will set up **a copy of the data every 15 minutes**, content only. Michael: *"especially where we are in the Knowledge Hub. I think that's fine."* The Console needs proper thought later.

## What DT must allow

George's one caution: *"is it going to be allowed to communicate with our service which is external?"* **Ian is confident**, because the Knowledge Hub already calls an external service, the Umbraco content system, and DT *"were not remotely uncomfortable"* about this on their call earlier that day. Charles, DT's CTO, sees no issue.

**What is not written down is exactly what DT must do.** Ian: *"we need to just be explicit about exactly what it is we need them to do or to enable us to do."* George: either DT do it themselves or Novosapien get a service account, and both are fine, though access would be quicker. Michael is to set up a call with DT and Charles. See #129.

**Ian on priority:** *"we are going to go on the 17th"*, and the API defects left are small enough that hosting is *"the primary thing we need to get closed down."*

## Monday's Knowledge Hub release

Michael listed two changes coming on Monday 9 November:

- **A version API**, showing the current version and the next one. Stackworkz must also deploy versioning in the Knowledge Hub. This touches #101.
- **The public sandbox** gets its own subscription key, authentication by **card program ID**, hard-coded for the sandbox, and **pre-loaded data**, so *"every single request will always work regardless of the retention period."* See #31.

Michael sends the release notes on Monday.

**Coding standards:** the Sonar check needs over 80 percent, and the branch scored 82. George: *"let's get it up a bit more than 82. Don't want to be passing by 2%."* An email goes to Roanne at Stackworkz, who reviews next week. Michael: Stackworkz run their own checks for DT as well. #125.

## DT come off future development

**Ian will tell DT, within a couple of days, that they will not take on future development of the Knowledge Hub and the Control Center**: *"I've had enough of an experience with them on things they're supposed to know what to do, so they can forget that."* **Stackworkz keep supporting and maintaining both**, and any front-end change that needs AI work goes **directly to Stackworkz**. DT stand down the people they had planned for it.

**On DT:** six engineers and 11 people in total on TXN's project. Ian praises **Billy** as the person who makes it work: *"when he's involved in the conversations... everything is solution based."* The trouble starts when others step in between.

## Support: an 18-month forecast and a new model

**Ian has forecast Novosapien's support from January 2027 to June 2028**, 18 months. TXN will bring in its own AI engineering team at some point, three months before a handover. He does not want new people in the early years: *"I just can't be asked with adding the risk."* Novosapien can say no or pick a length.

**The current proposal is loose on dates.** Ian: *"I'm not sure the proposal for support fee actually closed down when it started and when it ended."* He cited the **£4,250 a month** fee. He had pictured a pause in build work, then about four more months of build from **August 2027**, but is open to *"another way of doing it that kind of flattens that out, increases the monthly rate, but provides the whole lot."* Brett: a different rate on different deliverables for a longer term.

> [!warning] Support start: January, or 16 December?
> Ian's forecast starts in **January 2027**. The SLA, rebased on 7 October, starts support on **16 December 2026**, the day after Phase 2. See [[commercial]] and #130.

**Hosting is paid for.** Ian: *"I'm not expecting not to pay for what you're standing up"*, with no end date other than not long term. Brett: *"we'll just pass through the transaction cost on the invoice."* Brett mentioned Mazars as another client asking Novosapien to host. No terms are written for this.

## 24 November in London

Ian, Michael and Novosapien meet at **Novosapien's London office on 24 November**, a session and then dinner. On the agenda: what is left of the planned scope, how to get it done, support and maintenance, and possibly a new commercial structure. **Brett wants to show Project Genesis**, Novosapien's agent workforce platform, of which Outbound is one part. Ian: TXN's focus for now is the platform and its clients, but *"I'm open-minded to all of it."* **Brett organises it.**

Ian's plan: the Monday call, finish for go-to-market, the week after for the launch, then London.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| AI already deployed in Novosapien's Azure; Novosapien host for launch; Monday becomes a connection call | [[delivery]], [[open-questions]] #119, #49 | Callout added; rows updated |
| SSE to WebSockets, AG-UI, North Europe, latency, Container Apps restarts, 15-minute data copies | [[architecture]] | Callout added |
| What DT must enable for the outbound call is not written down; call with DT and Charles | [[delivery]], [[open-questions]] #129 | In callout; row added |
| Version API and public sandbox changes on 9 November | [[open-questions]] #101, #31 | Rows updated |
| Sonar at 82 percent, to be raised; Roanne reviews next week | [[open-questions]] #125 | Row updated |
| Launch: George says the 16th, Ian the 17th | [[delivery]] | In callout, still flagged |
| DT come off future development; Stackworkz keep Knowledge Hub and Control Center | [[commercial]] | Callout added |
| 18-month support forecast, new model, support start conflicts with the SLA, hosting cost passed through | [[commercial]], [[open-questions]] #130 | Callout added; row added |
| London session and dinner, 24 November | [[commercial]] | In callout; open action |
| Billy praised; DT headcount; Mazars | n/a | Context, no action |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Stackworkz, Novosapien and TXN alignment call: how Stackworkz connect to the AI service | George, with Stackworkz and TXN | Monday 9 November |
| Send the Knowledge Hub release notes (version API, public sandbox) | Michael | Monday 9 November |
| Set up a call with DT and Charles on exactly what DT must enable | Michael | After the Monday call |
| Raise the Sonar score above 82 percent and email Roanne | George | Before Stackworkz review next week |
| Set up 15-minute data copies for the Azure environment | Brett | Before launch |
| Tell DT they will not take on future development | Ian | Within a couple of days |
| Organise the London session and dinner | Brett | 24 November |

## Transcript

# Novosapien <> TXN - AI Hosting Sync

Fri 6 Nov, 15:30  
Client: TXN

**Ian Johnson** (0:00): Right. I'm glad it's Friday.

**George** (0:06): I was gonna say. What. What is the difference? It's just more people out on a Saturday and Sunday in London. All I notice, Fridays are absolutely dead.

**Ian Johnson** (0:18): Yeah. Whereabouts in London do you live? So I

**George** (0:21): live right near Tower Bridge. So it's. So it's relatively central, which for me I'm a lazy bastard. So when I decided on new places to. To live, I was like, I do not want it to be more than like five, ten minutes from the office. And where's the office? It's. It's. So it's near, near Fenchurch Street. It's right near all gay station. So it's, it's, it's easy to get to. And fortunately it's not too far in Whitechapel, which is not

**Ian Johnson** (0:52): there. Not. Yeah, no, no, I know, mate, I get. You don't have to

**George** (0:56): say anything else. Yeah, well, let me. I just gotta send. Yeah, Sam's gonna

**Ian Johnson** (1:02): join as well. Hey, Brett, how you doing? I'm all right. I was like

**Brett StClair** (1:08): missed your email by a while and didn't see all the other.

**Ian Johnson** (1:14): There we go, Mike. Oh, it's there. All right, mate?

**Michael Moores** (1:21): Yeah,

**Brett StClair** (1:23): good.

**George** (1:25): You've got your home set up. Brett, he's. I know. Yeah.

**Ian Johnson** (1:30): Somebody give values fame too much. That's what the only people have that kind

**George** (1:34): of setup. He's gonna turn the lights on, look.

**Brett StClair** (1:48): What? Why is my lighting

**Ian Johnson** (1:49): not going on? You failed at the first hurdle, mate.

**Brett StClair** (1:59): There we go.

**George** (2:05): My

**Michael Moores** (2:06): partner's got sick of the lights not turning on when there's no Internet. So we have to keep some normal bulbs. She told me undo half of them, They don't go off till 10. But when the Internet's off, you have to wait until it's 10 o'. Clock. So if you try and go bed any earlier, it's just like. Nope. Staying on the bedroom,

**George** (2:26): just getting a T shirt. Wrapping it around. Around your head so

**Ian Johnson** (2:29): you can get to sleep. What's a good old fashioned light bulb? That's what I want to know. Yeah. If you

**Brett StClair** (2:36): see what I've got in front of me, it puts George to shame. The amount of kid that just stands in front of me pretending to look cool.

**George** (2:44): No.

**Ian Johnson** (2:47): Right. Thanks for jumping on. I don't think. I don't think it should take long because I think there's. George has already kind of said yes in principle. Before we dig into it, I just want to check because Dirt has shared an agenda for a meeting on Monday, which is Stack Works, Novo and TXN alignment. I think how to Integrate stackworks and Novo Sapien as your environments share the architecture. We're deploying at Novo Greece. Security requirements, integration points, blah, blah. Is that kind of specific to the Control center more than anything else? No.

**George** (3:30): So I'll kind of cut a long story short. We've already deployed it. It's already running in Azure. What we've done is we've taken the code that Stack Works have for the Knowledge Hub, put that in Azure, in our Azure just so that we can test it. But correct me if I'm wrong, Hasan everything's up, everything's running. Most of the security stuff is done. There's still, I think, a few bits with Azure front door which we'll need to play around with, but then there's nothing where we've gone. Oh God, what are we going to do? So by the call on Monday with Stat Works, it will be more of a. This is what we've got. How, how are we going to. How are we going to connect or how are you going to connect? So we'll have the whole week to make sure that it's. Yeah, like ready. This is

**Ian Johnson** (4:22): in the principle that you will host the AI service in Azure because what we were actually talking about is again, you guys will know better, but as far as we understood it, the Control center calls. Control center, the Knowledge Hub calls an API to access the AI

**George** (4:51): service. Correct? Yeah. So in the front end code we'll have the standardized way of connecting it, which the AGUI package, which will have a corresponding thing on the back end so that when they're communicating, it's standardized but separate services communicating to the. The Agent service, which effectively is an API. So all it will be is an API call. The. Wait, I have one thing, Hasan The. Is it using WebSockets? There was one slight change that we had to make based on Azure which was we couldn't use one method of basically the agent sending the messages to the front end, so we're using another method. So instead of SSE, it's WebSockets, which we updated in the code and in the version that we've deployed in Azure it's using that as well. So I think like we said, there's maybe one or two small issues that, that we've got left to sort out, which will be done by the end of the day so that by, by Monday Stack Works should have everything that they need in order to connect and it will just be hopefully that call and then by the end of the week it should, should all be done, tested and ready. For the 16th well should it will be okay

**Ian Johnson** (6:17): and that's Stackworks will be placing that call from DT's environment by the way DT has said they couldn't see a problem with it on the call earlier Mike, they've got more There'll be many more questions about the whole control centerpiece and the AI but we understand that so this effectively will be the stack. The Knowledge Hub will be in the DT environment. The AI service I know I'm simplifying it will be in Azure environment hosted by you guys temporarily but essentially the way that they work won't be any different once we move the AI service into the DT environment. Theoretically it could still work that way. Yes

**George** (7:10): I think the only in the DT environment there might need to be some like slight changes in terms of obviously they might have some part locked down which we would then need to get into change a few things but it's. It's all that's all fine the only thing would be could be one cause for cons well not concern I don't like using that word is given what's been deployed on the DT side is it going to be allowed to communicate with our service which is external? I think there's always if there's a will

**Ian Johnson** (7:45): there's a way. No so would it be able to. We're already using. We're already connecting to an external service because of the Umbraco content management system which is the general principle that we talked to them about today. I think they were not remotely uncomfortable about what we were talking about doing for the Knowledge Hub because they don't see it as a risk. So I'm comfortable and confident around that piece. I think was it you Mike that raised the latency question

**Michael Moores** (8:29): obviously with it being Azure and the same thing. I think that's especially the knowledge it was more control center that I was concerned about with knowledge Hub wise it's already communicating to Umbra and stuff anyway so the latency shouldn't be a thing there in terms of a long delay it's more the control centerpiece I was concerned about long term which

**Ian Johnson** (8:50): Azure region is the instance that you stood up. EU north Perfect. I think that's one of our advice that Amsterdam.

**George** (9:13): I literally had the bloody diagram up.

**Ian Johnson** (9:16): I think it's Amsterdam.

**George** (9:21): If, if, if, if it needs to be another one we can switch it. Yeah, I think

**Michael Moores** (9:26): it's out. We're in Ireland, in the Netherlands, I think so. I think it's your north was Ireland and then Brett region, Euro West was Netherlands, I think. We're in for the other stuff as per dirt. Okay. Yeah. North Europe. Let's

**Ian Johnson** (9:44): have a look. North Europe is island actually. Yeah,

**Michael Moores** (9:50): that was, that was based on an active, active conversation with DT dirt. We got that from. So I

**Ian Johnson** (9:54): think that's pretty accurate. But the, it says the Brett region is Western Europe. Yeah. Which that's on a page called as your speed apparently, whatever that is, is your latency test. Anyway, it's a, it's a. Not. I don't, I don't think it's an issue. And we were just thinking about what are the ways that we can minimize any risk of

**George** (10:24): latency. Yeah. I think if one, one benefit with latency and LLMs is obviously with database stuff. You want it to be as quick as possible. User clicks a page, you want it as quick as possible. With LLMs it's going to be at least 2 or 3 seconds. So an extra 100 milliseconds is from my experience. Maybe I'm just used to it. It is not too much of an issue. But obviously you want to get as quick as possible anyway. Yeah.

**Ian Johnson** (10:56): But it's not the, it's not the most important factor in the speed. Okay. So. But by the way, Brett, I'm not. Because I'm not expecting not to pay for what you're standing up and I can't tell you how long it will be for other than there is no intention that it's a long term thing. We know what your business is. We just need to give DT some space because despite the fact that they said to us this is no problem and no risk, there's still no commitment to say, oh, don't ask them to do it, we'll spin it up ourselves nice and quickly. So we, we've got Mazars,

**Brett StClair** (11:36): I don't know if you know Mazars, the tax consulting conglomerate who we're building agentic AI, firing up workflows to build LLM environments across all the different types of LLMs in the cloud based in Europe in a controlled environment that we're hosting and then playing on. So we're finding ourselves in this weird space where guys are actually coming to us going, please help us just with all this hosting and getting all the data and compliance and everything right. So it's quite interesting you guys have come sit up like, oh, no worry, we'll just forward it to you. By the way, we'll just pass through the transaction cost on the invoice. Yeah. So it's not a

**Ian Johnson** (12:20): problem at all. Perfect. So the only other question is, even though we think it's temporary, it's super important. So what's, what is the position from a resilience perspective

**George** (12:34): in it? What do you mean in terms of like fallback stuff like that? Yeah, so we'll make. Because, because it's container apps, it's usually if, if something goes down, it comes back up straight away. So it's a, it's more of a managed service from, from Azure.

**Brett StClair** (12:51): Okay. And it will just do snaps on the data environments. So it will be not a crazy full backup, docker kind of environment. It's content only, your processing and everything will have the resiliency, and then the data will just. We'll set up regular snaps. Mike. Unless you want more. But I mean, like I don't think you need more on, on a fully production environment like on the console. Like you've got to think about what kind of resiliency you want. But on this, I think if you've got it every 15 minutes doing a snap, being able to back out and do a recovery should be fine. Yeah, I

**Michael Moores** (13:30): think that's especially where we are in the Knowledge Hub. I think that's fine. And then we can review that when we get to the control center and the DT and stuff. So I think

**Brett StClair** (13:39): that makes sense. Okay. Yeah, control center and everything. You need, you need to

**Ian Johnson** (13:44): think about it properly. So you align with Stack Works on Monday and then coming out of that will. Will there be something explicit that we can ask DT that they need to do to allow that call get made in terms

**George** (14:04): of the getting it from us to them? Yeah, I suppose it's. Yeah, I suppose it's not too, it's not too dissimilar to the document that we've already sent over. I suppose it's maybe just a more. What sort of access are they going to give us? Are they going to do it all, or are we going to get a service account which has got the ability to. To update it? I suppose both are, both are fine situations. Obviously, if we got the access. Maybe, maybe this is an incorrect statement, but I feel like we'd be able to do it a bit quicker. But obviously appreciate that statement. Yeah.

**Ian Johnson** (14:44): I don't understand this world. I mean, to be clear, I'm aware of the fact that servers aren't actually in the clouds, right? What? Wait, now I'm confused. I'm blowing your mind now. Don't put that on LinkedIn though, that you've only just found that out. And don't say that it's me that told you, whatever you do. So, so Mike, I think you just need to, and I know it's not your area of expertise either, but I think we just need to make sure that we, we have, we are going to go on the 17th. The bottom line is, I think my view is that given the nature of the defects that remain outstanding on the API, barring them any more of them up whilst trying to fix one thing and breaking another, we've got sufficient time to get that done and therefore this is the primary thing we need to get closed down. So I think having a call with DT would be super helpful, probably definitely with Charlotte at least. But he Charles the CTO and from his perspective, he's like, yes, he doesn't see any issues with it, but I think we need to just be explicit about exactly what it is we need them to do or to enable us to do to allow this to happen and then we can go from there.

**Michael Moores** (16:16): Yeah, perfect. It's probably worth mentioning on the couple of things outstanding as well. So on Monday we will have two changes very specific to the Knowledge Hub. So the first one shouldn't impact you too much, I don't think so. It's a version inside, so depends what we're doing on there. Obviously it's going to be one version for now. Essentially the version API is coming so you can see what is the current version, what is the future version that's coming in. The second thing is that connecting you up to the public sandbox. DT are going to set you your own subscription key up, just so we know the difference between the two. I've asked for a document on how to put this back in and the biggest one is we're going to a card program ID for authentication level. So obviously for the public sandbox, again, doesn't impact too much. You'll be given the card program to send up every time. So it's going to be a hard coded, but they're going to pre-seed all the data as well. So literally you can just click go and it will run and there's an account that's going to be pulled back as well. So they're doing all that pre-seed data. So if you did just want to click around, then it'll pull back. Every single request will always work regardless of the retention period and stuff like that. So there's a couple of bits that need to connect up. Obviously Stack Works needs to do the versioning in the Knowledge Hub as well and deploy that. So there's a couple of things that need to align there. But as soon as I get the release notes on Monday, I'll let you know what that is. Just so we can make sure it's connecting to the right bit. Obviously, public sandbox is there and ready. We can start, you know, getting that ready to connect to it,

**Ian Johnson** (17:50): basically. Okay, perfect.

**George** (17:56): Yeah, yeah, yeah, all good. So up and running. I think Hasan messaged me during the call saying that is all, all those issues I mentioned should be all sorted now. It's just that that process of connecting to the deployed Stack Works version, which I say can't imagine would be too much of an issue. Yeah, I think they

**Michael Moores** (18:18): mentioned today that they've got their own. Is it sonic checks that they're doing the DT? So when they push that in with you, they'll be running that anyway. So that's the only thing that might not align to DT standards. But they said they'll check that and stuff. I think your own UAT and your own branch, I think at the moment. Was that correct? And then. Yeah, merge it in and I think they've got a few changes to do as well, last I spoke to them. Did we

**Brett StClair** (18:46): apply DT's coding standards in full? Yeah,

**George** (18:50): in the end. Yeah. So, and I think it's correct if I'm wrong, it's 80, but for the solar thing it's got to be over 80. I think we tested a couple of days ago and it was 82, so obviously we passed. But let's get it up a bit more than 82. Don't want to be passing by 2% and yeah, but obviously almost that's all good. That's on our. That's on our branch. I think we've got an email to send over to Roanne about well, that's been done, blah, blah, blah. So then next week they can have a look. Obviously, the tests will already be there, so there's not anything that they will have to do that we. We should be surprised by. So yeah, yeah,

**Michael Moores** (19:37): I think we've got the. Not the production URL, but we've got a vision to get into production, if I remember rightly. Obviously once that's done, we can get in and test, and then it'll just be a matter of fact of making that live URL available. Basically. Yeah,

**Ian Johnson** (19:55): as easy as that. So one other thing that I wanted to. Or two things. One of. One of which it won't impact you right now, but at some point it will. So at the moment, DT think that they are going to be supporting and taking on future development of the Knowledge Hub and the control center. In the next couple of days, I'm going to tell them no, they're not, because I've had enough of an experience with them on things they're supposed to know what to do, so they can forget that. So as and when we evolve the front end, if there's stuff that requires any change in from an AI point of view, that will. That will be done directly with Stack Works, because they're going to continue to support and maintain it, and we're going to stand down the DT people that they planned to do it. Similarly and more importantly to you I've extended forecast of how of this support that we're going to ask you guys to do from more basically, I think it's start in Jan next year and running all the way through to June 28th, so 18 months. Of course, you could say no, we don't want to do that and that's fine. But I because the deal at some point we want to bring in our own AI engineering team into it. Do a proper handover. Yeah. And we will bring them on three months before we do the handover. But if I'm really honest I just can't be asked with adding the risk into this thing in the same way that we're asking staffworks to continue to support the Control Center Knowledge Hub because they built it and in these early years it's just a risk that I don't really think we need to take by. By bring introducing new people into it. That said you guys decide whether you how long you want to continue to support it or if you don't want to support it. But I've

**Brett StClair** (22:09): basically. And we love working with you

**Ian Johnson** (22:11): guys around for the next. We love working with you and Snap Works and super ultra.

**Brett StClair** (22:19): Good bunch. Thank you. What about D2? It's like a great

**Ian Johnson** (22:23): bunch. I will tell you this about dt. I'll tell you this about dt. There is one guy in particular, I'm sure there are many more who is brilliant and when he's involved in the conversations Billy, everything is solution based and let's find a way of working. It's when other people insert themselves between him and us that it all starts going Tits up frankly. How many engineers. Sorry,

**Brett StClair** (22:54): how many engineers do they have? There's

**Ian Johnson** (22:58): six that are on our project but the six engineers and 11 resources. So this is the bit that pisses me off when I look at it and go what the hell, you know, manager we've got for paying for a product for people who wrote user stories that a three year old could have wrote. I'm paying for QA that do QA testing that finds nowhere near as many things as Mike's testing finds. So it's just, I mean it's, it's all right. But the relationship we've got with you guys where we're actually talking to people who are doing the work, it's just the better way of doing it. So we have actually got some really good partners in this. And I just think from my point of view we just want to continue that. Until such time that we're confident that we can take it on ourselves basically. No, we'd love to.

**Brett StClair** (24:00): I must admit that like

**Ian Johnson** (24:04): we work

**Brett StClair** (24:05): with so many different types of customers and 90% of them are DT styled and, and to work with you guys is so refreshing. You're properly agentic, you think out the box. It's just. Oh, it's like one of the. We, we look forward to stand ups with you guys, we other consumers. It's like the stand up with eight project managers and scrum masters and I'm like where the hell are the engineers in this that

**Ian Johnson** (24:34): we're working with? What's going on? I hear you on that for definite. Okay. I don't think we, perhaps we could pick it up after next week, Brett, just to see if there's anything, any documentation we need to put in place to that effects. I know that we, we had the proposal. I'm not sure we. I'm not sure the proposal for support fee actually closed down when it started and when it ended anyway. To be perfectly honest. It was just. This is how much it is.

**Brett StClair** (25:06): So what kind of support are you thinking of? Do you want like the kind of support we're helping on build or do you want the support mechanism where we're just supporting you? You want to call. How are you seeing that? So there's,

**Ian Johnson** (25:17): there's two things, right? So one is the one you quoted us £4,250 a month which I assume is general kind of support and maintenance stuff

**Brett StClair** (25:37): because we can come in at a different rate on a different set of deliverables that make more sense on a longer term. Right. Because at the moment project based stuff you probably want to be something a bit more optimum but where you've got this constant build capability. I'm just. Hold on

**Ian Johnson** (25:57): a minute. I'm just looking at. Yeah. And then we'd kind of envisaged and I am open to a different model but we'd kind of then envisaged that we take a break on the project type stuff and then pick that Back up around kind of August time next year. And then we got another kind of four months worth of build stuff. Now if there's another way of doing it that kind of flattens that out, increases the monthly rate, but provides the whole lot. Yeah. Knowing that I don't. There are things that were in the phase. I lost track of phases. They kept changing. Phase three. Yeah, we were

**Brett StClair** (26:45): in phase zero and then phase zero,

**Ian Johnson** (26:47): whatever that phase is. There's a bunch of, of stuff that some of which I think has been done, some stuff got dragged forward. So it put not, not before, not next week because it's. We should focus on what needs to get done. But it's probably worthwhile just coming back to the table, Mike, and just saying, okay, this is what we thought. What, what do we think is the best way of working together going forward so that we can keep iterating on what we're doing, which we're going to need to do. So love to

**Brett StClair** (27:19): do something like that. I think we can do something interesting. We've been going to market quite a bit across the hospitality space, across recruitment, in a space where I think you guys might be interested and I'd like to take you guys through it. But it's more an agent workforce space. We call it our Project Genesis. And it is like a full agent management platform that runs various components of the business. So you're going to get a taster on Outbound, that's one of a handful in revenue. And then we're building out. As each of the various industries grow, the whole thinking is you have your vault, but we've actually evolved it into a brain and it allows a team to kind of scale where they are without adding additional resources across various different platforms. And I just don't know if you want to have a chat. Look at that. It might be something as you starting to accelerate, but only when you starting to accelerate, like you don't want to be putting that kind of stuff down on the ground until you know you're getting your customers and you're under pressure and you need to move stuff along. And I know Mike, you're building your headspaces there, but this is all pre packaged agents all lined up. We instruct them. We've got the full management capability, all the brain capability, all the integration points, like some of the solutions we're doing for the Ivy group, you know like Ivy and sexy fish and Caprice and all that kind of stuff. So we're doing the whole group there is. It's, it's remarkable.

**Ian Johnson** (29:02): It's not that restaurant.

**Brett StClair** (29:05): Yeah, it's kind of restaurant that George, Max, Lily go to. We don't go at

**Ian Johnson** (29:14): certain times of the evening. Yeah, I'm sure, I'm sure there's one in Manchester that I. Yeah, that's right, there's one in Manchester. Thank you. It's even for

**George** (29:24): me I think stuff that's a bit too much where you're trying to eat your food and somebody's dancing on a bloody table next year and you're like

**Ian Johnson** (29:29): yeah, yeah, it's right in the corner of. What's the name? What's the. You know what I'm talk. Spinning Fields, Mike. Where our office used to be. Right as you enter Spinning Field, it's right on there. I'm like who goes to these places? I don't, I don't really. That's not me, that's for sure. I. I would say this Manchester's got some of the best kept old-fashioned pubs that you will find. I mean, not full of old crusties but brilliantly maintained, and they might. And absolutely fantastic. That's more my cup of tea. That's my

**Brett StClair** (30:02): cup of tea as well. Right.

**Ian Johnson** (30:05): What, what. Let me suggest something. I think, I think at the moment, our focus is on that. I think might be the platform and the solutions we're delivering to our clients. But I'm open-minded to all of it. Maybe because we still haven't done this face to face.

**Brett StClair** (30:27): Why did I start doing that? I. I don't know why I did it. I didn't

**Ian Johnson** (30:30): see. I was looking at my. I was looking at my calendar. So you're all right. Decision if you're around on the 24th of November, we in London, we could meet and talk about what. I'm assuming, yeah, we're free. Bike is. Yeah, yeah. I was meant

**Michael Moores** (30:52): to be racing, but obviously I'm not

**Ian Johnson** (30:53): now, so. No, no, no, don't be stupid, mate. I just picked. I just picked my car for other reasons. Broken.

**Michael Moores** (31:02): So I'll take that off my calendar.

**Ian Johnson** (31:05): I'm so sorry, Mike. Yeah, no, that

**George** (31:07): SC me. Yeah, you get lime bikes, Mike, and race around London.

**Michael Moores** (31:14): Yeah, no

**Ian Johnson** (31:15): free on there. Absolutely. So I, I think that would be a good time to explore what's left to do of the things that we'd envisaged already, and then we can talk about how we get those done and get the support maintenance thing and maybe the. It looks like a different commercial structure than the one that we'd envisaged for it. I'm totally open-minded to that. I know we know that this is not. This isn't going to end at some point. It needs to never end, but be continued by our own people. But it's. I don't think, Mike, you're in any rush to start hiring AI engineers right now. No, definitely not. No. There you go, then. All right, I'll. Brilliant. So, thank you. Can you just say, can I leave you to organize it? Because obviously you would need to host. Would

**Brett StClair** (32:13): you like to come to offices? We would do a little session and go out for some dinner after that. It's

**Ian Johnson** (32:19): fine by me, mate. Yeah, perfect. I'll

**Brett StClair** (32:22): get the logistics all set up and

**Ian Johnson** (32:23): I'll.

**Brett StClair** (32:32): tell you. I went this morning that I've never been to. I felt really posh. Insurance customers took me to the Ned. I was dressed like this. You must imagine they're like, sir, are you a member? Are you a guest? Get the out.

**Ian Johnson** (32:56): Surprises me that that still exists today. That's the thing that just. You don't get in California, all that is like mad, right? Nobody cares. But apparently here they do. I remember it wasn't that long ago, people still expected to work. Well, trousers and shoes and a white and a shirt to go into a nightclub. Be like, what the hell are you doing? He's like, literally, look at everybody. Nobody's gonna do that. Stuff is off. I used to

**Michael Moores** (33:23): wear trousers and a. All inclusive in Tenerife. I wasn't allowed in my shorts. It was. It's four weeks in their winter months. You have to wear trousers. It's like 29 degrees.

**Ian Johnson** (33:36): Kidding me.

**Michael Moores** (33:37): Obviously, I didn't bring anything with me, so I'm like, I don't really want to eat here then. It's only the buffet. It wasn't my. You know what I mean? It's the standard food as

**Ian Johnson** (33:46): well. Right. We appreciate it. So we'll have the call on Monday. Let's focus on getting this thing finished, ready for go-to-market launch, and then leave the week after for the launch and stuff that goes with it. Hopefully, no fallout, but who knows? And then the week after, we'll come down and see you guys and look at what comes

**Brett StClair** (34:15): next. Guys, I've just seen the time. I've got another call, so I'll chat

**Ian Johnson** (34:19): to you all later. Yeah, thanks, guys.

**George** (34:22): All right, have a good one.
