---
date: 2026-08-18
type: standup
description: "Transcript and analysis of the 2026-08-18 TXN agentic standup: rendering cleaned up, ready to call real APIs, DT confirmed as the constraint, interview schedule set"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-access-layer]]"
  - "[[commercial]]"
status: extracted
extracted-to:
  - "[[generative-ui-rendering]]"
  - "[[approval-queue-integration]]"
  - "[[mcp-server]]"
  - "[[integrations]]"
  - "[[commercial]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN — Agentic AI Standup (2026-08-18)

> **Source:** Gemini transcript, synced from the shared folder (`shared/clients/txn/meetings/`). Attendees: Brett StClair, George Westbrook, Max Kingaby, Hasan Ahmed, Vineth Siriwardana, Dorte Dye. Ian Johnson declined; Dorte to summarise for him. Duration 00:36:12.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| **The rendering defects from 13 August are fixed.** Components no longer jump position, there are fewer errors, and the build is "a lot cleaner". Last week's version was never deployed; **a deployment goes out this evening** and will reach TXN's environment | [[generative-ui-rendering]] | Update banner added |
| **Canvas now carries long lists.** Suspending a card was rendering 50 transaction rows inline, described as "a horrible user experience"; it now returns a canvas the operator opens and clicks into | [[generative-ui-rendering]] | Update banner added |
| **Approval stacking is still unresolved.** George: *"we're still working out a way to make sure that it's not click approve then click approve again then click approve again."* The approach being explored is having the agent **queue** the approvals, with the open question being how to render the queue | [[approval-queue-integration]], [[open-questions]] #26 | Update banner + register row |
| **Michael delivered written feedback on Friday 14 August** and most of it is already implemented. Dorte has not yet been into the build and will look next week after tonight's deployment; she was explicit that **Michael is the reviewer who matters**: "his word as gospel" | [[open-questions]] #51 | Register row updated |
| **Security is deliberately deprioritised for the pilot.** Features first, on the reasoning that no real APIs are touched. One or two of Michael's items were security-related. User access and hardening come after the workflows | [[open-questions]] #53 | **New register row** |
| **George's read: the build is ready to start calling real APIs**, though it will not yet. *"The core infrastructure is there... it's just a matter of refining some of the components."* Next in order: fix bugs and UI, add more workflows, harden the MCP server, then user access and security | [[mcp-server]], [[delivery]] | Update banner added |
| **Finishing the pilot early would not help TXN.** Brett offered to finish a couple of weeks early. Dorte: it would help "tremendously", **but Direct Transact has to finish their build first**, and "everyone else is finishing before they finish". DT is the binding constraint on the wider timeline, not Novosapien | [[delivery]], [[open-questions]] #48 | Register row updated |
| **Dorte reprioritised: the console matters less than lead generation.** *"The console is not as important as such because we need to have first customers to use the console... the better we get the content workforce and the lead generation running, then we will see if we get a customer through the door sooner."* Pre-launch in September, full launch October or November | [[commercial]], [[delivery]] | Note added |
| **Stackworkz have no deployment scheduled**; Dorte hopes for one in the next couple of weeks. Items still outstanding from DT. The **Friday call with Stackworkz is confirmed**, with their new project manager in place | [[integrations]] | Update block added |
| **George's proposal to avoid being blocked:** push ahead on the replica and start on the **agent inbox and mocked alerts**, so no external dependency gates the work. His view is that the earlier fear of being blocked on the agent inbox is unfounded, because the backend is plug-and-play and the front end can be exchanged with Stackworkz either way | [[agent-inbox-alerts]] | Update banner added |
| **Flight plan cadence agreed: end of week**, not every couple of days. Dorte asked for it weekly since little changes across two days. Novosapien continues to run it daily internally | [[delivery]] | Note added |
| **Content Workforce interview schedule locked**: Wed 19 Aug 10:30 content manifesto and pillars; Thu 20 Aug 11:00 brand entity; Mon 24 Aug outbound interview one, the offer (George attending); Tue 25 Aug 14:00 ICPs; Thu 27 Aug 10:30 personas. Individual interviews follow, led by Tyler | [[commercial]] | Note added |
| **Novosapien team is in Bali from 10 September for three weeks.** Flying the evening of 10 September, travelling the 11th, working from the 14th. Standups move to 09:00 UK time; the 10 September 14:30 call is cancelled | [[delivery]], [[open-questions]] #54 | **New register row** |
| Tyler officially joins on the day the team flies, and is already picking up customers. Max has drafted the interview templates from the vault and is reviewing them with Tyler | [[commercial]] | Note added |
| Ian's main interest is the Content Workforce; Dorte is briefing him separately | — | No action |

---

## Transcript

Aug 18, 2026

## **TXN \- Agentic AI SU \- Transcript**

### **00:00:06**

**George Westbrook:** Hello.

**Max Kingaby:** Yo,

**George Westbrook:** I can't I can't see what you did, but I'm assuming you put your middle finger up.

**Max Kingaby:** no. I was just testing my camera to make sure it worked.

**George Westbrook:** Oh, okay.

**Vineth Siriwardana:** Yeah,

**George Westbrook:** Yeah,

**Vineth Siriwardana:** it's got it's got like

**George Westbrook:** it's got it's got like a bad hair filter

**Max Kingaby:** Yeah.

**Vineth Siriwardana:** bad.

**George Westbrook:** on.

**Vineth Siriwardana:** How are we doing, Max?

**Max Kingaby:** I am good. Mr. with an F.

**Vineth Siriwardana:** How the sound of that?

**Max Kingaby:** So,

**George Westbrook:** Sounded a bit gay there.

**Vineth Siriwardana:** A bit gay there.

**Hasan Ahmed:** Got you there.

**Vineth Siriwardana:** Oh,

**George Westbrook:** Not you.

**Vineth Siriwardana:** you found that one.

**George Westbrook:** Don't worry.

**Max Kingaby:** of course, you joined

**Vineth Siriwardana:** I appreciate my colleague, you know.

**Max Kingaby:** the

**George Westbrook:** Wait.

**Vineth Siriwardana:** Okay.

**George Westbrook:** Good afternoon.

**Dorte Dye:** Hello.

**Max Kingaby:** If I

**George Westbrook:** How are we

**Dorte Dye:** I'm all right.

**George Westbrook:** doing?

**Dorte Dye:** And see, I'm outnumbered again. What's going

**Max Kingaby:** don't

### **00:01:05**

**Dorte Dye:** on?

**George Westbrook:** I don't I've I've heard you're a Claude pro now. A Claude code

**Dorte Dye:** I think you know,

**George Westbrook:** pro.

**Dorte Dye:** we tried to do too many things at the same time and then we got stuck and then Brett had to come to your meeting.

**George Westbrook:** Oh god.

**Dorte Dye:** So, it was full success.

**George Westbrook:** I I think that's the issue. There is there is so much and like especially trying to do it in an hour or a couple of hours,

**Dorte Dye:** To be honest,

**George Westbrook:** it's like it's just

**Dorte Dye:** the setup is always the hard bit. The using is not.

**George Westbrook:** overload.

**Dorte Dye:** But having all of the different applications and I'm making them work when plus I'm using a normal laptop, not a Mac like you guys.

**George Westbrook:** Yeah.

**Dorte Dye:** So then things didn't look like the same way and it's like gosh Max,

**George Westbrook:** Yeah.

**Dorte Dye:** where are you? You're actually away, aren't you?

**George Westbrook:** He is.

**Dorte Dye:** on holidays. Not a fake

### **00:01:52**

**George Westbrook:** He's He's He's in sunny Spain.

**Dorte Dye:** background.

**George Westbrook:** I don't know if he can hear us cuz his face looks just like

**Dorte Dye:** I think he doesn't care anymore.

**George Westbrook:** Max.

**Max Kingaby:** Nice.

**Dorte Dye:** You really can't ask, can he?

**George Westbrook:** God knows what he's doing.

**Dorte Dye:** There's no reaction. Maybe you should say something

**George Westbrook:** Max, you got a s\*\*\*

**Dorte Dye:** nice.

**George Westbrook:** haircut. He had that You're not

**Dorte Dye:** Okay, I said something nice like um George,

**George Westbrook:** You're You're not You're not meant to laugh at that either.

**Dorte Dye:** do you mind to let my fun in because I want to record your

**George Westbrook:** Oh, yeah. Yeah.

**Max Kingaby:** D my my my response every time Brett

**George Westbrook:** Yeah.

**Dorte Dye:** mic?

**Max Kingaby:** um George says my haircut is s\*\*\* is that at least my next barber appointment won't have to be in Turkey.

**George Westbrook:** Just got tired. Shots fired. Yeah, don't just I'm just really offended by that, Max. So,

**Max Kingaby:** Good luck.

### **00:02:53**

**Dorte Dye:** Let me just I just want to Back.

**George Westbrook:** is is is Ian coming along to this one as well?

**Dorte Dye:** check. He might have just crashed out. He has terrible check. Like he started working from two almost like you.

**George Westbrook:** Uh

**Dorte Dye:** As I've heard, you guys were really up like crazy last

**George Westbrook:** yeah, then it was uh yeah,

**Dorte Dye:** week.

**George Westbrook:** thank God for caffeine and nicotine. I think without without that we'd be uh well, we wouldn't been able to stay up as

**Max Kingaby:** Yes.

**George Westbrook:** long.

**Dorte Dye:** Oh, honestly,

**Max Kingaby:** Okay.

**Dorte Dye:** these days are over for me.

**George Westbrook:** Yeah. Don't. But we're lucky we've got quite a decent coffee machine in our office. So, it's just go there, get another coffee, another coffee. Another coffee.

**Dorte Dye:** Can't be healthy.

**George Westbrook:** Oh, no, it's not. But we'll pay for it in a few years time. So, at least you'll be fine now.

**Dorte Dye:** Then you look like we do.

### **00:03:43**

**Dorte Dye:** Ear, no hair.

**George Westbrook:** I mean, Brett says he's in his 30s.

**Dorte Dye:** And I got all of the

**George Westbrook:** He

**Max Kingaby:** could be worse.

**Dorte Dye:** wrinkles.

**George Westbrook:** just

**Max Kingaby:** You could just look like George in the first place, I suppose.

**George Westbrook:** I just wait. How do you how do you remove somebody from a

**Dorte Dye:** So I I think the next appraisal process max will knock away for

**George Westbrook:** call?

**Dorte Dye:** you. Um nothing from Ian yet.

**George Westbrook:** Yeah.

**Dorte Dye:** So I would just say let's just jump in and then keep it

**George Westbrook:** Okay. Yes.

**Dorte Dye:** short

**George Westbrook:** I suppose I suppose this week it just it's these tiny iterations. Um Oh, here we go. Have we got Brett? You on mute,

**Dorte Dye:** and still on mute.

**George Westbrook:** Brett? Mr. Mr.

**Max Kingaby:** go.

**Dorte Dye:** This is a classic entry for that man.

**George Westbrook:** Google when he can't can't work out how to turn it off mute.

**Dorte Dye:** And now he's telling us

### **00:04:29**

**George Westbrook:** Oh,

**Dorte Dye:** jokes.

**Max Kingaby:** I probably bestie does stay on mute

**George Westbrook:** no.

**Brett StClair:** Thought I'd give you guys a bit of a bit of This is my office.

**Max Kingaby:** then.

**Dorte Dye:** You're still in the same box. Don't you have a bigger office?

**Brett StClair:** What are you talking about?

**George Westbrook:** Wait.

**Brett StClair:** Did you not see George?

**Dorte Dye:** This This is your office. It's under the stairs, isn't it?

**Brett StClair:** George sitting next to me.

**Dorte Dye:** Like Harry Potter.

**Brett StClair:** He's sitting next to

**Max Kingaby:** This is an up attempt at a joke.

**George Westbrook:** We have to we He has three strikes and then he's kicked

**Brett StClair:** master.

**Dorte Dye:** I can't blame

**George Westbrook:** out.

**Dorte Dye:** you.

**Brett StClair:** It's like everyone's against me today. Who's Whose Fathom is recording? Did you take note of that Fathom?

**Dorte Dye:** Okay. Ian said for some reason the meeting is not in his diary but he is busy at the moment. So we need to check that he has

### **00:05:23**

**George Westbrook:** Okay.

**Brett StClair:** because he canceled it.

**Dorte Dye:** to

**Brett StClair:** He He rejected it. time is what I what I'll

**Dorte Dye:** that's okay.

**George Westbrook:** Oh,

**Dorte Dye:** I'll give him a summary after.

**George Westbrook:** yeah.

**Dorte Dye:** I mean there's a lot to catch up for him at the moment anyway and he's not not yet in the nitty-gritty.

**Brett StClair:** do.

**Dorte Dye:** So what he is really interested is in the content work force. Brett stay on 10 minutes longer to just book all of the next steps in and then he will be happy because he will then be on your back on on Brad's back by the way.

**Brett StClair:** I know why he's so happy.

**Dorte Dye:** Oh no,

**Brett StClair:** He knows.

**Dorte Dye:** Max, I'm sorry. On yours, too.

**Brett StClair:** most heavy lift. of doing all of

**Max Kingaby:** Hi.

**Brett StClair:** this.

**George Westbrook:** And then I can't wait. I can't wait for the call. So Brett's like, "George, can you join? Can you join this call?

**Brett StClair:** What the hell am I

### **00:06:10**

**Dorte Dye:** I mean if Brett teaches me how to do that s\*\*\*

**Brett StClair:** doing?

**Dorte Dye:** then I will be really bad just as Brett can imagine too from us of

**Max Kingaby:** Lucky you guys will have a

**Dorte Dye:** work

**Max Kingaby:** Tyler.

**George Westbrook:** Yeah.

**Dorte Dye:** good you were rescued.

**Brett StClair:** We're pairing you with a Tyler. Tyler's the best.

**Dorte Dye:** today.

**Brett StClair:** He He officially joins on the day that we fly to Bali, but he started picking up with our customers. So,

**Dorte Dye:** Why are you flying to Bali?

**Brett StClair:** we've got a new because Hold on.

**Dorte Dye:** What's not

**Brett StClair:** The person who's most excited about this should talk about

**Dorte Dye:** allowed?

**Brett StClair:** it.

**George Westbrook:** Well,

**Max Kingaby:** Is that

**George Westbrook:** I don't know if that's me or Max.

**Max Kingaby:** Yeah.

**George Westbrook:** I think it's equal.

**Dorte Dye:** So, you excited that he can go to Bali or you all going to Bali?

**Brett StClair:** Max break down what we're doing in

**Max Kingaby:** We're going to Bali as a team. We're renting a villa for 3 weeks and working at

### **00:06:58**

**Brett StClair:** Bali.

**Dorte Dye:** So that's why you gave us the presentation with the picture how it looks like to hire and go with you on a

**Max Kingaby:** Harley.

**Dorte Dye:** retreat. Maybe I should float that to Ian because our shareholders are South African and they are Scottish moneywise.

**Max Kingaby:** Yeah.

**Dorte Dye:** So I'm surprised that Brett is up for that. George, that must be you. to balance it

**George Westbrook:** Hey.

**Dorte Dye:** out.

**Brett StClair:** remember like I'm going to be the 51y old uh trying to keep up clubbing and at 9:30 going it's bedtime for me

**Dorte Dye:** I mean you will look like the dad of all of them.

**Brett StClair:** everybody

**Dorte Dye:** I mean you want to be very clear right at the end of each night they will come to you and ask

**Brett StClair:** I'm back

**Dorte Dye:** for the bill to

**Brett StClair:** on

**Dorte Dye:** pay.

**Max Kingaby:** Um, we've also got someone who needs to care for her son because he has two beers. And so,

**Dorte Dye:** You know, you can survive without alcohol as well.

### **00:07:59**

**Dorte Dye:** That's totally fine.

**Brett StClair:** her son.

**Dorte Dye:** But it's not fun. I know. Okay.

**George Westbrook:** Um,

**Brett StClair:** her son's code for he's getting absolutely hammered tonight. He goes, "Brett, should we just have two beers?" And then you know you're in trouble because then her son

**Dorte Dye:** So, it's I call her free,

**Brett StClair:** is more like 23

**Dorte Dye:** right? Two of them.

**Brett StClair:** beers.

**Dorte Dye:** Sorry. Okay, come on. Let's focus.

**Brett StClair:** Let's focus,

**Dorte Dye:** Unless you want to take me to Bali,

**Brett StClair:** George.

**Dorte Dye:** too.

**Brett StClair:** Here we go. Let's go. Let's go. Let's go party it up in Bali.

**Dorte Dye:** So

**George Westbrook:** So I think in terms in terms of changes it's going to seem so tiny but it's such a ball because it's the way things render um making sure that it's all clean because I think when Mike was putting in the feedback there was so there was a version that we had last week I think we showed we hadn't deployed that yet because there was a few tiny changes that we needed to make working on it over since then.

### **00:09:02**

**George Westbrook:** Um but it's come out it's a lot cleaner now. So the I think obviously one of the the things that was that were causing an issues with the approval cards. Um we're still working out a way to make sure that it's not click approve then click approve again then click approve again and then click approve again. But one of the issues is the agent it we need to find a way that it's going to go right I'm going to cue all of these and that how what's the best way to render it. Um but in its current format it's just a lot cleaner. Things aren't jumping around. Um there's there's less errors. Um and the three workflows are working really well. Um Mike's Mike's handed over some feedback as well which is really helpful on Friday. Um I think most of that most of that's been done. I think there was one or two things around security um which because this is like the pilot we thought right let's get features features first because we're not touching any real APIs um we'll obviously keep the security stuff in mind um but obviously that's not it's not been a priority at the moment because we're not touching

### **00:09:56**

**Dorte Dye:** No.

**George Westbrook:** any real APIs um so I think yeah the three workloads that we got at the moment we'll add in we'll add in some more as well um and just make sure that's as as bulletproof as as as what

**Dorte Dye:** Amazing.

**George Westbrook:** as we Um but yeah it's I think we'll do a do a deployment this evening um which should be update which should update on your end as well. Well it shouldn't it will um and then you should notice that the agents a bit more the the way in which it's rendering stuff is a bit nicer like I think one it was showing like transactions for example on um suspending a card and it would render like 50 50 rows in the chat which is a horrible user experience. Um, so it would show a canvas which what it would give you the option to open the canvas where you can look in click into them. Um, but I think it's getting to the point now where it's it's it's ready to start calling real APIs. I don't think we do that yet, but it's we're in a good place where it's we can start expanding out into more workflows because the core infrastructure is there.

### **00:11:09**

**George Westbrook:** um it's working very well and it's just a matter of refining some of the components and then moving on to then then moving on to the other stuff as well.

**Dorte Dye:** Mhm.

**George Westbrook:** So like when we've got exposure to the actual console linking it to real pages as well. Um but I say really really happy with the progress on our end but obviously the opinion that matters is is your guys

**Dorte Dye:** I I I looked in it but I hadn't comment on anything. So I will hold off till the new one is deployed and then I will have a look next week. But um far out there where Mike is with his comments. So it's like this word as a gospel.

**George Westbrook:** Yeah.

**Dorte Dye:** If there's maybe a couple from my side that's fine but don't wait on them because he's really the main corner and driver on that. Um from a content point of view,

**George Westbrook:** Yeah.

**Dorte Dye:** we haven't got any deployment scheduled yet from um the stack works guys.

**George Westbrook:** Mhm.

**Dorte Dye:** I hope we will get it in the next couple of weeks so then we can align better what you can do and what you can't do.

### **00:12:04**

**Dorte Dye:** Um there's still a few things out selling from DT as always.

**George Westbrook:** Yeah.

**Dorte Dye:** Um but again you can crash on with everything else and then we just leave the items

**George Westbrook:** Yeah.

**Dorte Dye:** that really needs DTS stack works to do the last bits.

**George Westbrook:** Yeah. Because I think it's I think what what would be what would be good to know as well when we speak to Stack Works is if the prototype that we we got is the prototype that they've been working off if there's any difference same like we always say we rebuild um rebuild it so there's that close

**Dorte Dye:** Yep. Yep.

**George Westbrook:** alignment um and then like we said even if Stack Works has not got things ready when

**Dorte Dye:** Mhm.

**George Westbrook:** it comes to stuff like the agent inbox for example or the alerting um at least we've got a base which is as close to what they're going to have as we can get without actually having it.

**Dorte Dye:** Yep.

**George Westbrook:** Um, so that means I think maybe even before we started this, we thought there could be some blockers around say maybe like the agent inbox and stuff like that because we wouldn't have the platform.

### **00:13:04**

**George Westbrook:** I don't think I don't think they're going to be there because we can all of the backend stuff is going to be plugandplay and even some of the front end stuff might be a process of either stack works gives us access or we give stack work access and they just move over what's what's needed um which should be touchwood um a lot more seamless than than maybe what we thought initially.

**Dorte Dye:** Yep. Yep. Now,

**George Westbrook:** Okay.

**Dorte Dye:** Friday is a good opportunity to run through all of that stuff. And the new project manager has taken over, so you have the right people in the call.

**George Westbrook:** Yeah. So, I think I think what we I suppose focusing on is nail down this pick up any bugs um in terms of UI the a way the the way the agent speaking get some more workflows in there as well. Um, and then I think then I think we should be there and then we can start looking at start looking at

**Dorte Dye:** Yep.

**George Westbrook:** say making the MCP server a bit more bulletproof.

### **00:13:59**

**George Westbrook:** Moving on to the the not so sexy stuff which is like user access things like that security

**Dorte Dye:** I don't know.

**George Westbrook:** but is obviously absolutely crucial. Um, so it's I think that would be next steps and then I I think what be I think we sent over the document last week. So if if you're happy, we'll pick some more workflows or given that document if if there's some that you think, right, we definitely definitely want those ones, let us know and we'll we'll start working on them. Um and I think I suppose in terms of the the content workforce and the outbound workforce. So I suppose like I said,

**Brett StClair:** Before you go,

**George Westbrook:** get those

**Brett StClair:** just before you go,

**George Westbrook:** Oh.

**Brett StClair:** I just want to check um if we're able to finish a couple of weeks early, would that help you on your timeline? Sta

**Dorte Dye:** It would always tremendously help us, but for that to happen is it needs to finish their build first. So I think everyone else is finishing before they finish.

### **00:14:58**

**Dorte Dye:** It's make sense.

**Brett StClair:** Bloody hell. Okay.

**Dorte Dye:** I I don't want to put necessarily more pressure on you guys.

**Brett StClair:** Yeah.

**Dorte Dye:** I think what what is really important is to get the other work stream started then we have

**Brett StClair:** Yeah.

**Dorte Dye:** like you said last week Brett if we can have that on a weekly basis that's where we are because as closer we get in September we wanted to do the pre-launch so that we saying we are ready for the market and certain elements need to be ready for that kind of exercise with the full launch happening in October November um that will be really helpful so that we can really much more closely and the console is not as important as

**George Westbrook:** I suppose if

**Dorte Dye:** such because we need to have first customers to use the console.

**George Westbrook:** I'm

**Dorte Dye:** Yes, we will use the console for us but if Mike and I doing something manually, it it's not the biggie.

**George Westbrook:** Yeah.

**Dorte Dye:** It's the customer the customer experience, right? So the better we get the content workforce and the lead generation running, then we will see if we get a customer through the door sooner than later.

### **00:16:03**

**George Westbrook:** Yeah, that yeah, that makes a lot of sense.

**Brett StClair:** Yeah.

**George Westbrook:** I suppose it's what what we could do is say use this replica

**Dorte Dye:** Mhm.

**George Westbrook:** push push farhead that we've got with this um and then potentially add in things like start working on the agent inbox maybe mocking up the alerts things like that so that like we said we're not bottlenecked by anyone else. Um like we always say code is cheap so maybe we make some assumptions that aren't true. Um we re rebuild it. But I suppose it's just I think for us like we we know that within the next week or what let's say two weeks. Um the pilot's going to be a good point. Um and we might as well start working on um other stuff.

**Dorte Dye:** finish.

**George Westbrook:** Um obviously we've got the the content workforce and the outbound as well. Um which will which will take obviously a bit of time.

**Dorte Dye:** Yeah.

**George Westbrook:** Um but a lot of that's a lot of that's config. Um, so I think like obviously I'm assuming Bre Brett and Max have obviously explained the process of the content workforce and the the outbound um, which will be kind of not discovery sessions but just kind of mapping it out and then I suppose it's speaking to Tyler getting getting that going.

### **00:17:14**

**Dorte Dye:** Yep.

**George Westbrook:** Um,

**Dorte Dye:** Yeah.

**George Westbrook:** get get the engine get the engine turning.

**Dorte Dye:** That's that that's the main goal of and and if you guys have different roles and responsibilities as well. If the content workers is more Max, Tyler and Brett, then you can keep focusing on that side, George. And then there should there shouldn't be much overlap as such.

**George Westbrook:** I think what I think with the with with the content workforce and the outbound as well is is obviously we build them in the same way that we we're we're building your agents and stuff like that.

**Dorte Dye:** Yes.

**George Westbrook:** So that it it's not as obviously malleable and let's destroy this blah

**Dorte Dye:** Yep.

**George Westbrook:** blah blah in comparison to say maybe the the full agentic experience that we're building. But there is always scope to change things. So,

**Dorte Dye:** And again that will come right. So it's like the good thing is he in his early days on that one.

**George Westbrook:** Yes.

**Dorte Dye:** So anything we do will help him tremendously.

### **00:18:07**

**Dorte Dye:** And then when he gets in the swing of things then that when then value for you comes in to say actually have you thought about X Y and Z. Um,

**George Westbrook:** Yeah.

**Dorte Dye:** and then you can fine-tune it for the things you might haven't even thought about with your other customers or anything. So,

**George Westbrook:** Yeah.

**Dorte Dye:** at the moment it just let's get the engine running and be ready before the launch. Um, and I assume we have I mean we have to do the the interviews which takes a lot of proportion and I know Max has already run it against our profile but we haven't really shared much

**George Westbrook:** Yes.

**Dorte Dye:** marketing material because I haven't seen anything from Brunin but we'll pick up with Ian

**George Westbrook:** And

**Dorte Dye:** um that we get all of that stuff fed in before we start doing the first interviews because then we just Nope.

**Brett StClair:** No, no,

**Dorte Dye:** Yes.

**Brett StClair:** no. It's perfect. I just suddenly had a brain wave. If if Bronin's struggling with the marketing material, I mean, it's quite a complex uh B2B kind of messaging stack.

### **00:19:04**

**Brett StClair:** Um maybe there's a way we can help her a bit, get the positioning right once

**Dorte Dye:** I don't know if she's struggling. So, this is this is purely a work stream Ian is um covering. So, I'm not really involved in it. Every so often he asked me and Ian and Mike for feedback, but we're not on the meetings or anything. So I haven't seen the website since I had seen the presentation she has given us I think it feels like months ago now. So it's more about what is there when do you start delivering because the same with for my side it's like I've built all of the CM flows I just need to connect the two. So it's like where are we with that kind of stuff just linking the pieces together now and if there are gaps Brett then yeah maybe then we can look at how we align on that side of things. I think

**Brett StClair:** we we deal with the content, then we deal with the ICPS and offering and and if we building that from scratch and she hasn't got to

### **00:19:51**

**Dorte Dye:** the

**Brett StClair:** that point, a lot of that can go to her and can really help her. Um, it could be really useful for them.

**Dorte Dye:** Okay.

**Brett StClair:** Um, and then it's just the kind of the imagery, right? The corporate identity elements that you can then pin down.

**Dorte Dye:** Yeah.

**Brett StClair:** But a lot of time the marketing's got to speak to the direct outreach, the contact, the content that's going out there, the, you know, it needs to be this kind of rounded approach. That's

**Dorte Dye:** And I think this is this is where I really need Ian on that one again because we

**Brett StClair:** what

**Dorte Dye:** leveraging her expertise but we don't want POP and Roman to drive everything if that makes sense because it's our brand and this we just need to align a little bit better where because I mean she's quite senior as Well, so I'm not expecting her to do all of the work, but if she's running around chasing the people doing the work, there might be an easier way.

**Brett StClair:** Cool.

**Dorte Dye:** But for that, we just need to know where she is and if there are any gaps.

### **00:20:58**

**Dorte Dye:** and then if you can help to fill in the gaps. So what's the next steps on the on these two work streams

**Brett StClair:** Uh

**Dorte Dye:** then?

**Brett StClair:** so next steps let's uh just after this I will send you just an updated flight plan on where we are with the it um

**Dorte Dye:** Got a pilot. Yeah. Okay.

**Brett StClair:** I'm just running it at the moment.

**Dorte Dye:** Does it does it make sense you send it that often or would it make more sense to send me the updated flight plan at the end of the week

**Brett StClair:** Uh

**Dorte Dye:** after two sprints because I assume there's not much

**Brett StClair:** um

**George Westbrook:** probably

**Dorte Dye:** changing between one or two

**Brett StClair:** um I don't know.

**Dorte Dye:** days.

**George Westbrook:** you

**Brett StClair:** It's really quick and easy. Like I mean the only thing is just I just need to make sure George anything that you've committed is committed and I can pull it down and then just I'll just send it to you just I run it every day

### **00:21:53**

**Dorte Dye:** Okay.

**Brett StClair:** by the way for all our clients. Keep an eye on it and see where it's ticking over.

**Dorte Dye:** Okay.

**Brett StClair:** I might just forward it to. And what I'm always looking for is the percentage completion versus duration and then just checking what line items

**Dorte Dye:** Yeah.

**Brett StClair:** might be stuck. Um but it's quite simple. It would you had the look of f\*\*\*

**Dorte Dye:** Yep.

**Brett StClair:** bread. Buy me some more time there.

**George Westbrook:** No,

**Brett StClair:** Did I?

**George Westbrook:** no,

**Brett StClair:** Okay. Okay.

**George Westbrook:** no.

**Brett StClair:** Um what else? Okay. So, let's talk um max. So, we need let's start with brand TXN. We're going to need I know you reckon you can do it in an hour. What happens if we plan two hours, Max?

**Max Kingaby:** Yeah. Yeah. Yeah. Um I've just got some of the stuff I've drafted with Tyler right now. So once um Tyler kind of looks over it, says he's happy, then we'll kick that session off.

### **00:22:57**

**Max Kingaby:** Um basically I just fed the vault into into a load of bits and drafted out some template ideas for that we can feed into the interview. Um shall we just schedule it in tomorrow irrelevant as to what Tyler's response is and then if any changes that Tyler does add between now and then

**Dorte Dye:** Hello.

**Max Kingaby:** we can

**Brett StClair:** So, we have a relatively free day tomorrow from 10:00 a.m.

**Max Kingaby:** implement

**Brett StClair:** to 2:00 a.m. with a half an hour slot at about 11:30 that's taken that usually is actually happens at 12\. Any of those times suit you

**Dorte Dye:** I mean, we need Ian for that one.

**Brett StClair:** and

**Dorte Dye:** We can put in maybe 10:30 for now, for an hour because he's really blocked out then from 12:00. And I know jet lag is really hitting him at the moment. So I don't want to necessarily put much in in the end of the Okay, I will confirm if that's okay with him. Um, so that will be Mike is free on that P as well. That will be the first interview and it will be for the corporate

### **00:24:13**

**Brett StClair:** Yeah.

**Dorte Dye:** identity.

**Brett StClair:** So that's mainly uh it'll be um it'll be the content manifesto manifesto and pillars

**Dorte Dye:** Yeah.

**Brett StClair:** for now. We might be able to get them all done, but if not, then we'll push the entity and everything else uh to later. I'm just banging it in diaries right now. Um Max and Ta. I think that's all. Yeah, that's it. Uh let me set it to record.

**Dorte Dye:** What did we say? How do we call it content?

**Brett StClair:** So, I've called it TXN content workforce interview one um content manifesto and pillars and it's in your diary now. B let's lock and load another meeting

**Max Kingaby:** Bosch.

**Brett StClair:** um as the uh brand entity and then at least we've got the other other hour slotted in. Is there any time on Thursday in this

**Dorte Dye:** Yes. Let me have a look.

**Brett StClair:** diary? And then we can plan each individual's um interviews the following week.

**Dorte Dye:** Yeah, Ian is okay with that one.

### **00:25:45**

**Dorte Dye:** Tomorrow we could do Thursday

**Brett StClair:** Thursday 11:00.

**Dorte Dye:** 11:00.

**Brett StClair:** Perfect.

**Dorte Dye:** So that's only for the content creation. What about the outbound one? Or are we starting to focus on the content creation and then moving into the outbound thereof?

**Brett StClair:** I would get this one nailed because we also lean on a bunch of content here because we got to get the tone right.

**Dorte Dye:** It's that's absolutely fine but just from my head. So it's like we start focusing on that once the base is there then we can start picking up

**Brett StClair:** I can we look at Monday morning or Tuesday morning?

**Dorte Dye:** it.

**Brett StClair:** No. Uh let's do it middayish. Anytime. Middayish. Monday or Tuesday next week.

**Dorte Dye:** Yep. Just give me a

**Brett StClair:** We can kick off the outbound

**Dorte Dye:** second.

**Brett StClair:** offer.

**Dorte Dye:** Just keeping informed that he knows what's going on, all the details, all of the inwards. So, Monday 24th, um, And yeah,

**Brett StClair:** I'm going three 10:30 perfect

### **00:26:59**

**Dorte Dye:** 11:00 or 10:30.

**Brett StClair:** Monday. Okay. And that will be

**Dorte Dye:** Superb.

**Brett StClair:** TXN outbound interview one and that is going to be the offer.

**Dorte Dye:** So, when are you guys going on your retreat? Are you planning to work from the retreat or are you planning to be okay jet like hours

**Brett StClair:** Yeah. Yeah.

**Dorte Dye:** then

**Brett StClair:** No, no,

**Max Kingaby:** Yeah.

**Brett StClair:** no, no, no. We we we um it's a fully working retreat.

**Dorte Dye:** okay?

**Brett StClair:** The only difference is timing. So, we just got to figure out who's going to be up later versus who's going to be up earlier to manage.

**Dorte Dye:** What is the time difference?

**Max Kingaby:** Eight now.

**George Westbrook:** 7 hours.

**Max Kingaby:** Seven.

**Dorte Dye:** So it will be the afternoons then for you anyway. Okay.

**George Westbrook:** Yes.

**Dorte Dye:** But that's fine. That's not a problem.

**Max Kingaby:** Wait

**Dorte Dye:** And do we need to move any of our meetings already over? When are you going away

### **00:28:06**

**Brett StClair:** Um,

**Max Kingaby:** for a

**Brett StClair:** it's it's going to be about the 10th of September.

**Max Kingaby:** second.

**Dorte Dye:** of September?

**Brett StClair:** So,

**Dorte Dye:** Okay.

**Brett StClair:** time we've got time.

**Dorte Dye:** So, we have plenty of time then.

**Brett StClair:** Just a quick one.

**Dorte Dye:** Okay.

**Brett StClair:** George, do you want to be part of the offer or do you want us to finish the offer? the ICP and the personas and then you step in and help or do a review on it.

**George Westbrook:** I think for the offer I think that that that that' be worth

**Brett StClair:** Yeah, cuz I think the offer is the foundational one,

**George Westbrook:** it.

**Brett StClair:** right? Okay. So, I'll bring you into the offer and then the rest we'll do. So, then we need two other slots.

**Dorte Dye:** Is that for the individual interviews or is that for

**Brett StClair:** This is for the TXN outbound. So it'll be three.

**Dorte Dye:** Okay.

**Brett StClair:** Um, one will be the offer, one will be the ICPS, and then the other one, depending on how well we get the ICPS now, will be the personas.

### **00:29:05**

**Dorte Dye:** Okay, first Wednesday actually looks bad for Ian.

**Max Kingaby:** Wow.

**Dorte Dye:** We could do 2:00 on

**Brett StClair:** 2:00 on Tuesday.

**Dorte Dye:** Tuesday

**Brett StClair:** That's fine.

**Dorte Dye:** and then let's do Thursday 10:30

**Brett StClair:** Okay. So,

**Dorte Dye:** again

**Brett StClair:** offer ICPS. Um, and then sorry, what time on Thursday?

**Dorte Dye:** ready.

**Brett StClair:** 10:30. That's no problem.

**Dorte Dye:** Mhm.

**Brett StClair:** And that will be And that will be the um um persona. Perfect.

**Max Kingaby:** Shall

**Dorte Dye:** And do we want to do the individual interviews then in September or when you want to do

**Brett StClair:** We can do them uh because it'll be mainly uh with Tyler,

**Max Kingaby:** we?

**Dorte Dye:** them?

**Brett StClair:** we can overlap him from next week onwards.

**Dorte Dye:** When you started.

**Brett StClair:** But let's get through the TXM one so you guys can see the process and see how much we probably need

**Dorte Dye:** Yep.

**Brett StClair:** to commit to it. Um

**Max Kingaby:** Shall Shall we start getting a time in for the Barbie standups?

### **00:30:32**

**Brett StClair:** um I'm easy with that.

**Dorte Dye:** We can do it now as well. That's

**Brett StClair:** Do you want to have a look at times,

**Dorte Dye:** fine.

**Brett StClair:** Max?

**Max Kingaby:** Yeah.

**Brett StClair:** So doing the at the

**Max Kingaby:** So, plus seven, George. Yeah,

**Brett StClair:** moment.

**George Westbrook:** What' you say?

**Max Kingaby:** we're we're plus seven in

**George Westbrook:** Plus 7\. I thought you said 7 in the morning.

**Max Kingaby:** Barley.

**George Westbrook:** I was like,

**Brett StClair:** Yeah.

**George Westbrook:** uh, yeah.

**Max Kingaby:** I was calling you out there. Um, so plus 7\. So 3:00 our afternoon time,

**Dorte Dye:** which is what time you

**Max Kingaby:** 8:00 in the morning UK time.

**Dorte Dye:** time.

**Max Kingaby:** Should we do 4? 9:00 in the morning UK time.

**Dorte Dye:** Yes, please. Because Mike and I don't mind, but Ian is not keen on that.

**Max Kingaby:** So 4 400 p p.m. Barley time, 900 a.m. UK

**Brett StClair:** want to do 5:00. We can do 5:00 by time.

**Max Kingaby:** time.

**Dorte Dye:** But let me have a look if the diary.

### **00:31:40**

**Dorte Dye:** So it's from the 10th you said

**Brett StClair:** So, uh,

**Dorte Dye:** right.

**Brett StClair:** we 10th we're flying in the evening. 11th we'll be traveling. So it'll be week the 14th and

**Dorte Dye:** So the the 10th we need to cancel in the meeting when you're

**Brett StClair:** then is there a

**Dorte Dye:** flying bas on yeah at

**Brett StClair:** meeting on the 10th?

**Max Kingaby:** All

**Brett StClair:** Yes.

**Dorte Dye:** 2:30.

**Brett StClair:** Um let me just check flight times. I think we're flying in the

**Dorte Dye:** Yeah,

**Brett StClair:** evening.

**Dorte Dye:** but you know you need to be at the airport at it. I know you're all cool and you're probably just going last minute.

**George Westbrook:** Get get there an hour

**Dorte Dye:** The plane is still there for you,

**Brett StClair:** Yeah.

**Dorte Dye:** but

**Brett StClair:** I I Well,

**George Westbrook:** before

**Brett StClair:** the the Leia jet flies when we want it to fly.

**Dorte Dye:** of course it's your private

**Max Kingaby:** right.

**Dorte Dye:** jet.

**Brett StClair:** So, we'll just call the pilot. Take your time, man.

### **00:32:28**

**Brett StClair:** We're doing a hangout now.

**Dorte Dye:** So it's basically from the week after then from the 15th

**Brett StClair:** Yeah,

**Dorte Dye:** We can do 9:00 you Caitlyn. That's fine if you want to move that.

**Brett StClair:** perfect. I will get that cracking. So

**Dorte Dye:** And for the first day it should work as well. So if we just move them to 9:00s when you're away for

**Brett StClair:** TX

**Dorte Dye:** the whatever time you are there a

**George Westbrook:** Stop.

**Brett StClair:** three

**George Westbrook:** We might never come

**Brett StClair:** weeks.

**Dorte Dye:** And who needs to,

**George Westbrook:** back.

**Dorte Dye:** right? I mean, it's like you just have to move the company then to make it tax

**Brett StClair:** That's next thing.

**Dorte Dye:** efficient.

**Brett StClair:** I need to get that one right. Yeah, good call, Max. I'm getting this sorted now. Actually, it's working out really well.

**Max Kingaby:** and there were also 13 hours ahead of the states. So that's confusing me too much to figure it out.

**Dorte Dye:** I can't even deal with one hour between Germany and UK.

### **00:33:32**

**Dorte Dye:** So,

**Max Kingaby:** But

**Dorte Dye:** good luck with that one.

**Brett StClair:** Um, okay. So, that's the the week. Then we're flying back and we'll be in time for the sixth. No problem. Those all fine. And those all fine. That's all fine. Okay.

**Dorte Dye:** So you move

**Brett StClair:** D locked and loaded.

**Dorte Dye:** amazing.

**Brett StClair:** Well done everybody.

**Max Kingaby:** Oh

**Brett StClair:** Do we need to hop?

**Dorte Dye:** So bra one one more thing.

**Max Kingaby:** s\*\*\*.

**Brett StClair:** Can we have another?

**Dorte Dye:** So you created a nice HTML um for the content workforce.

**Brett StClair:** No.

**Dorte Dye:** If you do the similar thing for the outbound, you can put them on the same tab. I don't mind just with the next steps and then I'm boiling off on the back of that. I mean, or I don't need to just summarize what needs doing.

**Brett StClair:** Perfect. I'll I'll bang

**Dorte Dye:** Do we do we need Brumin for any of these meetings as

**Brett StClair:** that

### **00:34:34**

**Dorte Dye:** an FYI or nothing? Fine. Okay,

**George Westbrook:** This

**Dorte Dye:** then we just click on

**Max Kingaby:** She's more than welcome.

**George Westbrook:** is

**Brett StClair:** really really really intense low-level stuff, right? like I think she'll be like um whereas like you need to think about your proposition how you going to talk to the sales people and all that kind of stuff. It's It's really hard. This is not an

**Dorte Dye:** I I honestly I don't think it can be any harder to us than DT is we're

**Brett StClair:** easy.

**Dorte Dye:** already thinking outside of the box.

**Brett StClair:** I You know what? You teing it up so well. I actually want to sit in one of those standups

**Dorte Dye:** It's two worlds collide. I mean, what they're doing is great.

**Brett StClair:** just

**Dorte Dye:** It just a different environment and I just I don't know challenging.

**Brett StClair:** Oh my goodness, we are very late. I forgot it's even getting chased to go on the call.

**Dorte Dye:** You better go.

**Brett StClair:** Did chat to you later very much.

**Max Kingaby:** Oh crap.

**Dorte Dye:** Thank you so much. Speak.

**George Westbrook:** Reach you

**Dorte Dye:** Taking suspension.

**Brett StClair:** Bye.

**Max Kingaby:** She still a bite.

**George Westbrook:** soon.

### **Transcription ended after 00:36:12**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*