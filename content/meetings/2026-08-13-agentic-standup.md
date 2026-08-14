---
date: 2026-08-13
type: standup
description: "Transcript and analysis of the 2026-08-13 TXN agentic standup: three workflows running end to end, approval grouping direction, per-run tool audit, Stackworkz sync"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-access-layer]]"
status: extracted
extracted-to:
  - "[[conversational-interface]]"
  - "[[generative-ui-rendering]]"
  - "[[agent-orchestration]]"
  - "[[approval-queue-integration]]"
  - "[[audit-attribution]]"
  - "[[mcp-server]]"
  - "[[internal-ops-agents]]"
  - "[[architecture]]"
  - "[[integrations]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN — Agentic AI Standup (2026-08-13)

> **Source:** Gemini transcript, synced from the shared folder (`shared/clients/txn/meetings/`). Attendees: Brett StClair, George Westbrook, Hasan Ahmed, Max Kingaby, Dorte Dye, Michael Moores. Duration 00:24:46.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| **Three workflows run end to end.** Remaining defects are front-end: components render then jump position, and a one-to-two second render delay reads as "where has my message gone" | [[generative-ui-rendering]] | Update banner added |
| **Task list moved to a persistent panel** in the top-left corner, replacing the inline treatment | [[conversational-interface]] | Update banner added |
| **Approval cards to become collapsible**: a smaller card carrying approve and reject, expandable for detail. George's open question is whether users need the full detail to validate | [[approval-queue-integration]] | Update banner added |
| **Approval granularity is the live design question.** "It just seems like approval after approval." Options: one approval covering a bundle of tool calls, or one per call. **Michael's direction: group by common action** (cardholder plus card as a single approval since creating a card is routine; PIN separate because it is set separately; sensitive payment actions separate). Michael is documenting the grouping and will come back | [[approval-queue-integration]], [[open-questions]] #26 | Update banner + register row |
| **New ask: a per-run audit of the tools called and the API endpoints hit**, raised by George and aimed at Michael's review needs | [[audit-attribution]] | Update banner added |
| **Input validation is working**: George demonstrated invalid data being rejected rather than accepted into the flow | [[mcp-server]] | Update banner added |
| **Workflows are malleable after the structured start.** Once the scripted path completes, the agent knows what else it can do and proactively suggests next steps (simulation, funding the account, setting limits). Open design question: curate the suggestions or leave them to the agent | [[agent-orchestration]] | Update banner added |
| **Strategic choice put to TXN**: perfect and extend the existing workflows, or move to the proactive agent-inbox concept where the agent comes to you. Michael to review the candidate slate against TXN's own vault and identify gaps. Slate to be sent as a PDF | [[components]], [[open-questions]] #4 | Register row updated |
| **The vault MCP is in active use.** Michael on the connector: "It's been used several times. So it's good with the contest as well. So yeah, it's been perfect." | [[internal-ops-agents]] | Update banner added |
| **TXN runs its own vault**: nightly sync from SharePoint, meetings, decisions, and Michael's full release testing and UAT logs. He describes the two as working hand in hand, with Novosapien's holding the architectural and foundational material, and finding contradictions and gaps in TXN's own documentation | [[architecture]] | Decision note added |
| **Sentry error tracking to be added**, with errors linked to the feedback records so UI drawing, agent feedback and stack errors give one holistic view | [[integrations]] | Update block added |
| **Final wireframes exist** (not the prototype). Michael to share. Design alignment needed on agent location, the AI button in the header, and how it translates to the knowledge hub. A UI rebuild against final designs is "a run over two or three days" | [[integrations]], [[open-questions]] #35 | Update block + register row |
| **Stackworkz sync call targeted for next Friday.** Dorte arranging; their weekly TXN call is Wednesdays; they have a new project manager (predecessor on maternity leave). Stackworkz to get access to the console build to click through the agent and check design alignment such as fonts and payload rendering | [[integrations]] | Update block added |
| Dorte asked how far down the six-week line the pilot is and what remains; Brett to run the product-owner tooling over the backlog | [[delivery]] | Answered by the flight plan |
| Both George and Michael hit Claude usage limits | — | No action |

---

## Transcript

Aug 13, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:04**

**Brett StClair:** No one guessing. We got loads of guests. We've got bunch

**Hasan Ahmed:** They just join.

**Brett StClair:** of

**Dorte Dye:** Hi

**George Westbrook:** Good

**Max Kingaby:** They don't.

**Brett StClair:** Hello.

**Max Kingaby:** How

**Dorte Dye:** guys.

**George Westbrook:** afternoon.

**Brett StClair:** Howdy dudy.

**Max Kingaby:** they

**Brett StClair:** Hello Mike Fathom notetaker. How are you

**Dorte Dye:** I was saying where's Mike?

**Brett StClair:** doing?

**Dorte Dye:** There are more note takers from TXN than actually employees, right?

**Brett StClair:** Holy efficiency.

**Dorte Dye:** That's called efficiency.

**Brett StClair:** Oh, I think Mike's in.

**George Westbrook:** It's

**Brett StClair:** Hello, Mike.

**Michael Moores:** Are you

**Brett StClair:** Good, good, good, good. Um,

**Michael Moores:** okay?

**Brett StClair:** oh, how's everyone doing?

**Dorte Dye:** Yeah.

**Brett StClair:** Shall I do this? Hold on. Wait.

**Dorte Dye:** Is there a joke coming? George Co

**George Westbrook:** Please. No. Let's all

**Dorte Dye:** is

**Brett StClair:** No, I've just let in torches. No

**George Westbrook:** leave.

**Brett StClair:** taker.

**Dorte Dye:** I thought you record any anyway while Google.

**Brett StClair:** I know.

### **00:01:11**

**Brett StClair:** It's

**Dorte Dye:** I I I felt a bit funny that I sent you meeting notes from the earlier meeting,

**George Westbrook:** We

**Brett StClair:** like

**Dorte Dye:** but I felt like no, I need to be on top of Brett if he just waits till he gets his stuff.

**George Westbrook:** don't we I always like to have the Fathom one as a as a backup because there has been I think there was one meeting we did once which we really needed notes and uh it wasn't there.

**Dorte Dye:** Oh, yeah. You said

**George Westbrook:** So now it's just just in case we forget to click the button.

**Dorte Dye:** I think I think it's a problem. It's you're paying less attention making mental notes, isn't it? Because you're in the meeting and then you think it's like what did we say? It's like not

**George Westbrook:** Yeah.

**Brett StClair:** Um,

**Dorte Dye:** good.

**Brett StClair:** I could do with one when I'm doing uh drinks. with clients cuz after two beers I forget everything.

**Dorte Dye:** I think we should go very soon and then you forget all the statement of work.

### **00:02:05**

**George Westbrook:** Yeah.

**Brett StClair:** Just

**Dorte Dye:** Job done.

**George Westbrook:** Yeah, we'll do we'll do everything and we'll do it in two weeks.

**Brett StClair:** watch

**Dorte Dye:** I mean,

**George Westbrook:** That's what you

**Dorte Dye:** that's what you promised me before. To be fair, it was actually Max.

**George Westbrook:** say.

**Dorte Dye:** He's too close

**Brett StClair:** right. Max literally went I can do it way faster than two weeks.

**Dorte Dye:** to

**Brett StClair:** I was like,

**Max Kingaby:** I you're talking about the content workforce.

**Dorte Dye:** Mhm.

**Max Kingaby:** I've I've already uh made a nice a nice head start on it actually.

**Brett StClair:** "Yes."

**Max Kingaby:** So,

**Dorte Dye:** I mean the pressure will be on Max. I keep you to it.

**Max Kingaby:** a lot of pressure.

**Dorte Dye:** Okay.

**George Westbrook:** Pressure makes diamonds.

**Dorte Dye:** or breaks them.

**George Westbrook:** Yeah.

**Brett StClair:** He's dirty. You feeling full today? You're having a good holiday.

**George Westbrook:** What?

**Dorte Dye:** I mean like I'm so on form because I was too early up and it's like if I start working at 6 or before 6, it's like my brain is toasted at that time.

### **00:03:06**

**Dorte Dye:** So you don't want to talk to me after that time at

**George Westbrook:** Yeah.

**Dorte Dye:** all.

**George Westbrook:** Wait. After 6\. That's like That's That's like lunchtime, isn't it?

**Dorte Dye:** No,

**George Westbrook:** After 6:00 p.m.

**Dorte Dye:** in the morning this is when you actually go to bed.

**George Westbrook:** Oh, 6 6 in the morning.

**Dorte Dye:** I start working.

**George Westbrook:** I don't. Yeah, it's at 6 being up at 6:00 in the morning. I'd be like a vegetable.

**Dorte Dye:** But the thing is I have an hour extra anyway. So which is extra early.

**George Westbrook:** Oh,

**Dorte Dye:** So we're getting there.

**George Westbrook:** yeah.

**Dorte Dye:** Okay, back to you

**Brett StClair:** Yeah,

**George Westbrook:** Hey, let's go.

**Brett StClair:** we do a quick update um on where we

**Dorte Dye:** guys.

**George Westbrook:** So, let me So,

**Brett StClair:** landed.

**George Westbrook:** still testing out those three workflows um because it's they're working end to end. It's just some of the some of it doesn't look good. Sometimes there's like a few little bugs wherein it would render something then move the position.

### **00:04:04**

**George Westbrook:** It's so from a backend perspective is fine. Um it's just the way in which we're rendering it on the front end. um where there's a few where there's a few issues. So tiny little things um that that we've added like the the what's it called? The task list persistent in the the top left corner um rather than it

**Brett StClair:** progress.

**George Westbrook:** being inline. Um, and then the approval cards have changed a bit, but it's one of those I don't think we need all of this detail, but maybe we do because I'm assuming the users if they're going to want to validate and approve something, they're going to want to see it. So, I'm thinking maybe we just have it as collapsible where it's a smaller card where they can approve or reject um reject it. So, we'll get some of those changes in. But I show you where the one of the first ones is at. Um, see like even here the rendering that takes a second or two to render in whereas it should just be instant.

### **00:05:08**

**George Westbrook:** Um, just a better user experience because otherwise they're like wait where's my message gone? That like slight panic for a second. Um, so like with some of these workflows um should be in the right order. um should be getting the right data, but it's all at the moment a should be. Um so I think that's where it' be good with with your guys feedback in that okay is it is the I've just thought of something that we probably want to include as well. Um is it asking the right questions? Is it collecting the right information? Which leads me on to what I think I need to add is maybe for each run probably more for you Mike is an audit of the tools that were called and in turn the API endpoints that were called in order to take those actions. So I suppose I'll just go through this now. Um, oh no. First name is Hasan. Um, last name is McFarland. Date of birth, 4th of November, 1989\. Email address is first name, last name, um, at Gmail.

### **00:06:18**

**George Westbrook:** Address is the shard EC2Q 4BD. Currency is pounds. card type is physical. The PIN is one, two, three, and it needs to be corporate platinum. So, one thing which I'm I'm annoyed that I added it in um is if you go I'll just make it up for me. Um I was doing that as testing. It's going to reject that. So, it's not going to let you just put in random things. Um that So, see that tiny bit of rerendering? It's just I don't really don't like that. Um, so the approval as well, sometimes this will jump around. Um, and then what we what we need to do is work through all of these approvals. Is are all of these approvals needed? Is it too much? Is it too little? Um,

**Brett StClair:** Good.

**George Westbrook:** there we go.

**Brett StClair:** Good.

**George Westbrook:** It just seems like approval after approval. So I think potentially one good thing could be this is what I'm going to do.

### **00:07:30**

**George Westbrook:** I'm going to call these four tools. Do you approve it? Or we could have an approval per per tool call.

**Michael Moores:** You know, that's good. I think we usually have a think about like say we bundled up and you know certain stuff we probably could um you know card and card you probably bundled into one you know where pin you may leave out because you do set the pin separately. So you could have a card or one card that's one approval uh because that's like quite a common action whereas stuff like more sensitive payment and stuff like that. So I'll have a think and see where you want to group those or get those approvals and let you know but yeah I'll document that as we go through anyway.

**George Westbrook:** perfect. Um and then yeah so then it's going to suggest potential next step. So yes let's do the next step please. So not rendering it again but you can cue messages and after can we do the full card. Yes.

### **00:09:19**

**George Westbrook:** So, I think one thing that's important to know is even though this is a structured workflow to start with, afterwards it's very malleable. you can do loads of different things after the agent's going to be aware of what what things um what things it can do. So it might proactively suggest things. So like that simulation like checking different things or like funding the account um or

**Max Kingaby:** I think I

**George Westbrook:** setting limits.

**Max Kingaby:** suppose this maybe

**George Westbrook:** So I suppose it's maybe we want to Max can you mute your mic please? Um, so maybe we want to think, are there certain things that we specifically want to suggest or do we leave it up to up to the agent or up to the user um to decide what what happens next? I suppose that's just kind of a agent design decision in terms of how we want it to behave. Um, so I think we've got the three main three main workflows that we've been building and testing. the card hold uh where is it?

### **00:10:18**

**George Westbrook:** The these are the new ones. Um so there's yeah three main workflows that we that we have been testing and I suppose today it might be worth going through some of the proposed ones that we might work on next. Um so I think we've got the offboarding if needed. So in this we'll just obviously say what what it is but I sure you you guys will know that better than us. And then also the likely end points that we're we're most likely going to call. Um and I think the the ordering as well. Um so we've got the offboarding, any card service actions, um decline investigation, spend exception, then merchant control change. I think it might be better if we we send send this over after. But one other thing we can decide as well if we want to start working on maybe if we want to rather than going let's do more workflows is conceptually let's work on something different where the agents coming to you. So where you can it will look at look at an alert um and then or you can schedule things maybe we can have a look at some things like that.

### **00:11:34**

**George Westbrook:** So I suppose that's the decision we've got now. Do we take some of the workflows that we've got, perfect them, add some new ones in, or do we move on to something a bit more different where it's it's more more proactive where with that kind of agent inbox style thing?

**Michael Moores:** Yeah. Yeah. I think what I'll do is I'll take a look at these and then use all of them. Obviously, I think top you've most of them at least on sort of the core operational ones. So it's worth me just taking a pass there to see if there's any that have been missed that are obvious that I think but then yeah if it's all good there we can then move on to some more specific things.

**George Westbrook:** Yeah,

**Michael Moores:** So yeah, if you send that across to me, I'll have a quick look. Um, and just I'll run that against our vault as well,

**George Westbrook:** perfect.

**Michael Moores:** just to see if it's could find anything. Um, it's missing and

**George Westbrook:** that please could you put in a PDF and downloads?

### **00:12:31**

**George Westbrook:** Um, okay. Yeah. So, we'll send this over, have a look, get decisions on what we want to do next. And I think one of the biggest things is we just all need to have a a play around, get some get some feedback in there. Um, and then we can start churning out um some fixes to what we've currently got as well as working on pushing what we have got forward as well. Um,

**Michael Moores:** Yeah.

**George Westbrook:** so yeah, this that How's the How's the MTP server

**Michael Moores:** Yeah.

**George Westbrook:** going?

**Michael Moores:** It's been used several times. So, it's good with the contest as well. So, yeah, it's been perfect. Thank you.

**George Westbrook:** What What would you say is the difference between the vault that you've got and the vault that we've got? Is it is yours is there some overlap or is there

**Michael Moores:** Um obviously our vault's got everything in it. So um it does a nightly sync from our SharePoint. So any human human will drive a document change or take a sync into our vault just so it's got it.

### **00:13:30**

**Michael Moores:** It's got meetings uh decisions sort of thing as well. Also got my full release test in here. So UAT logs. So yeah,

**George Westbrook:** Yeah.

**Michael Moores:** pretty much the same as what you do in the core, but obviously a bit more specifics on top for testing and stuff like that.

**George Westbrook:** Yeah.

**Michael Moores:** So it's very much aligned. It is very much our knowledge store. So

**George Westbrook:** Is is there any issue having two separate ones or is is that just working

**Michael Moores:** um

**George Westbrook:** fine?

**Michael Moores:** yes. Yeah. So I've got it hooked up now. So if you can't find it, I'll flip over to to yours. Obviously we've got some more of the architectural the foundational things that we're working with detail the vision and stuff like that. So I think it works quite nicely hand in hand with that.

**George Westbrook:** Yeah.

**Michael Moores:** So it it does pour a lot more of the the technical stuff and obviously um it also finds any contradictions or gaps in our own documentation that that your sort of fills in as well.

### **00:14:22**

**Michael Moores:** So things working quite well um so

**George Westbrook:** Okay, perfect. Because like I said with with anything it's I suppose if we go to the uh there dreaded dreaded cold starts. This is where you jump in with one of your s\*\*\* jokes. All right.

**Brett StClair:** There's a whole lot of containers trying to be lifted and they're struggling and they're lifting and they're pulling. Now they're ready to go. Was that a joke or was that just a statement or was that reality?

**George Westbrook:** I think I think that was a statement. I really hope it wasn't an attempt at a joke. Um, yeah, I suppose if you if you look through obviously this vault and if there's anything that you feel might be either valuable to for us to know or anything that that you want to add in here yourselves, let us know. um and we can get it added added in the right place, change the structure a bit. Um and yeah, that could be that could be quite helpful.

### **00:15:31**

**George Westbrook:** But I suppose it's like we said the feedback um have a play around, break it, just break it as much as possible. Um I think one thing that we'll probably set up on our side is sentry tracking. Um so that when it does break, we're not just it's it's not just going to be done via feedback. is going to be right. Let's see what actually happened. Then let's see if we can find a way actually to link it to the actual feedback record as well, which we should be able to do. Um, so then we're getting like a holistic overview of not just the feedback, be it drawing on the UI, the agent, but also any any errors as well. I think that might be worth us adding in here as well as an error error tracking. Um, error tracking. Um, and then yeah, the workflows, just going through having a look, um, seeing which ones you think would be good to work on cuz like I said, the the bottom ones are the kind of the top ones are more let's add on more what to what we've already got and the new these ones down the bottom are more let's add net new functionality um maybe new new UI elements as well.

### **00:16:45**

**George Westbrook:** Um, because I think it' be good to good to have a play around with that at some point as well. So it's it's not just like a normal claw. It's like an actual digital worker or AI

**Michael Moores:** Yeah, that's great.

**George Westbrook:** employee.

**Michael Moores:** Yeah, I've got that down for tomorrow anyway. So, I've run out of usage on call now. So, I'll do actual not

**George Westbrook:** That what that's what that's what scared me is that apparently they've increased for the last what

**Dorte Dye:** Yeah.

**Michael Moores:** working

**George Westbrook:** May till August it was 50% extra usage and I've ran out ran out on usage. Yesterday I was like ah that's not good. gonna need to buy another account.

**Michael Moores:** Yeah, I've got till Sunday to wait.

**George Westbrook:** Oh,

**Michael Moores:** I my own person,

**George Westbrook:** that's not that's not fun.

**Michael Moores:** but I don't use that for TX. So,

**George Westbrook:** Yeah,

**Michael Moores:** I got a home.

**George Westbrook:** don't Yeah,

**Michael Moores:** So,

**George Westbrook:** it's always horrible when you've got you you run out of the session limit and you're like, hm, what am I going to do for the next 40

### **00:17:39**

**Michael Moores:** yeah.

**George Westbrook:** minutes?

**Michael Moores:** No. See, it works quite well. I've got a lot of testing yourselves and knowledge of it anyway. So, I think tomorrow you're working on that as well.

**George Westbrook:** Yeah.

**Michael Moores:** Um, so yeah, I'll use that today, tomorrow.

**George Westbrook:** Okay, perfect. I think I think that's everything from our side. Is there any any questions or any any concerns you've got on your side that we we can help

**Michael Moores:** I'm very very happy. Obviously, we'll test it,

**George Westbrook:** with.

**Michael Moores:** but it looks great. Um, yeah, also we'll just make sure you keep align with the the stuff like the design and stuff. So, we're getting more of the final designs.

**George Westbrook:** Yeah.

**Michael Moores:** I think I've got the final wire frames. It's not the prototype, but the proper wireframes. So, you can start making it look and feel similar as we get there.

**George Westbrook:** Yeah.

**Michael Moores:** Obviously terms about the where you locate the agent as well. Obly we just need to make sure we keep a stand over knowledge hub and stuff like that.

### **00:18:30**

**Michael Moores:** So part of what I was going to do is just sort of pick the pieces out because again AI is not part of any of them yet.

**George Westbrook:** Yeah.

**Michael Moores:** But there are some designs in there where we did a lot of stuff for the AI button in the head and stuff like that. So we just need to think about what we do in knowledge hub make sure it translate nicely across as well. So I'll I'll bundle that up in the feedback anyway.

**George Westbrook:** because I think yeah with the with any any finalized or any even changing prototypes um

**Michael Moores:** Um,

**George Westbrook:** just yeah once we've got them we can rebuild it all um like a lot of the a lot of the issues that we have with the agent are it's not so much look and feel it's kind of just a functionality in the front end behind the agent.

**Michael Moores:** heat.

**George Westbrook:** Um, which is very very very portable. It's like, okay, this needs to look slightly different. Fine. All the functionality behind it is the same.

### **00:19:19**

**George Westbrook:** Um, so what we'll do is we'll do a run over two or three days to rebuild it. Um, and then it just makes sure that we're we're not getting too far out of sync with designs. Um I think one thing I I think like we said last time is either some point next week or the week after when um Stack Works feel it's it's necessary is if we have a a sync pardon me a sync call with them maybe just show them some of the stuff we've been doing if it's aligned to what what what they're doing um and start thinking about okay when it gets to that point where we're needing to hand stuff over to them or collect stuff from them. um just nailing down that process, making sure that we're not we're not stepping on their toes and vice

**Michael Moores:** Yeah, that's probably the right time to take that.

**George Westbrook:** versa.

**Michael Moores:** They've got the project plan, high level stuff from them. So I think they've got a pretty good idea of where this is going to go.

### **00:20:10**

**Michael Moores:** So it's probably a good time to at least get an intro call. Not good idea. They've done several sessions with DT on how it needs to be structured.

**George Westbrook:** Yeah.

**Michael Moores:** So they've got the code framework there as well. So they'll know that as well. So that's probably good time to do it next week.

**George Westbrook:** Would would there be any value at some point in adding some of

**Michael Moores:** Um,

**George Westbrook:** the stack works team to maybe not not necessarily the full admin panel but maybe the console version that we've got um so that they can provide once we've got that kind of call it synced design um so that they can have a click around mainly the agent stuff um and then just provide feedback I suppose and not obviously probably not so much on the AI functionality but in terms terms of the fonts. Maybe if there's a stupid little things like if there's a a payload and we use a different font and we're rendering it in there, is that aligned to to what what they've

### **00:21:12**

**Michael Moores:** Yeah, I think yeah, we can align them with that and sort of tell them what we want to test and look at.

**George Westbrook:** got?

**Michael Moores:** So, I think that'll be beneficial. So, yeah, I think if we meet with them and then give them access to this, we can promp them on that call and then I think they'll be quite busy with the the engineer and the foundations, but I think it will line nicely when they start doing the screens and stuff and start sort of flipping back into to

**George Westbrook:** Yeah.

**Michael Moores:** make sure You know, we are in a lot of

**George Westbrook:** Yeah. Okay. Perfect. I think I I don't think there's anything else from our side.

**Michael Moores:** Michigan.

**George Westbrook:** Um I think we got was it next call? Next call on Tuesday. We've got the we got the set times now.

**Dorte Dye:** Yeah.

**George Westbrook:** Perfect. I think anything

**Dorte Dye:** So, how far we down the line when we said the pilot is 6 weeks? I mean, you have delivered lots,

### **00:21:56**

**George Westbrook:** else.

**Dorte Dye:** but I'm not quite sure what is still left in that six weeks time

**Brett StClair:** tell you what I'll do is uh we have a really sexy product owner skill

**Dorte Dye:** frame.

**Brett StClair:** set that sits on top of the uh backlog. So, let me give that a run on a curation and I don't think it'll look as good as your project plan, but I'll try and make it look

**Dorte Dye:** That was a classic sales

**Brett StClair:** nice.

**Dorte Dye:** move.

**George Westbrook:** You got a bit you you you got something on your nose,

**Brett StClair:** Sure, you're on today on all of my stuff.

**George Westbrook:** Brett. Brett, you need a tissue. I think you got something on your nose. What would you tell your

**Max Kingaby:** What would what would you have done when you were ex Google country manager, bro?

**George Westbrook:** ex

**Dorte Dye:** Nice. I've told him off earlier because he's mentioned on every single call we're on. I was at Google.

**Brett StClair:** Hey,

**Dorte Dye:** We

**Brett StClair:** Mike.

### **00:22:52**

**Dorte Dye:** did.

**Brett StClair:** Did you know

**George Westbrook:** Max told me after the court was like hilarious walking around with

**Dorte Dye:** No, that would be but that would be really helpful Brett if you could uh ping that across and then we can

**George Westbrook:** his

**Dorte Dye:** see what what's what's missing and I will um so we have our weekly call with stack works on Wednesday. Um we have a new project manager because our old one is going on maternity leave so he's just in the swing of things. So if we trying to aim something for next Friday like a quick intro call um and I and I have already someone in mind to who we can set up on that one to to um have a look around and then we just link you guys up for Friday.

**Brett StClair:** Happy

**Dorte Dye:** So Brett if you want to give me some times as well when the team is free then I can arrange that in the

**Brett StClair:** day.

**George Westbrook:** Perfect.

**Dorte Dye:** background.

**Brett StClair:** Perfect. Preferably sometime at about 8 8:00 in the morning.

**Dorte Dye:** Cool.

**Brett StClair:** Suits everyone perfectly.

**Max Kingaby:** Thank you.

**George Westbrook:** I think it will only be George's Fathom Notetaker joining that from my side.

**Dorte Dye:** You should have asked which time zones, George. It's flying.

**George Westbrook:** Yeah.

**Brett StClair:** Cool

**George Westbrook:** US Times.

**Dorte Dye:** California for that.

**George Westbrook:** Yeah,

**Dorte Dye:** I'm off.

**Brett StClair:** guys.

**Dorte Dye:** Okie do.

**Brett StClair:** Thank you.

**Dorte Dye:** Thank you.

**George Westbrook:** perfect.

**Dorte Dye:** See you next week.

**George Westbrook:** Thanks very much.

**Michael Moores:** Okay.

**George Westbrook:** Have a good one.

### **Transcription ended after 00:24:46**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*