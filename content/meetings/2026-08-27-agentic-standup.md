---
date: 2026-08-27
type: standup
description: "Transcript and analysis of the 2026-08-27 TXN standup: the pilot is functionally done, the agent inbox and scheduled reporting demonstrated, UAT split agreed"
scope:
  - "[[agent-inbox-alerts]]"
  - "[[full-agentic-experience]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[agent-inbox-alerts]]"
  - "[[scheduled-reporting]]"
  - "[[generative-ui-rendering]]"
  - "[[delivery]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-08-27)

> **Source:** Gemini transcript. Attendees: Brett StClair, George Westbrook, Hasan Ahmed, Vineth Siriwardana (Novosapien); Michael Moores, Dorte Dye (TXN). Duration 00:23:39.
>
> Runs the same day as [[2026-08-27-outbound-workforce-offer-session-2]], which is a separate engagement. This one is the build standup, and it is the last with Michael before he goes away on 3 September.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| **The pilot is functionally complete.** George: *"on the pilot front it's more just minor changes, but from our point of view it's done in terms of a pilot. It's just progressing it to that next stage where it's as close to production ready as we can get it."* What remains is **prompt wording**, so the agent says *"I am going to check a card"* rather than naming the tool, and **dev mode**. Michael raised nothing he wanted changed: *"from the look and feel of it, absolutely perfect. I don't think there's anything I saw that was a change"* | [[delivery]], [[full-agentic-experience]] | **Delivery status changed.** The remaining risk is calendar, not build |
| **The agent inbox was demonstrated and endorsed.** Michael: *"it looks great. I think exactly what we had in mind."* The flow: an alert arrives, the agent investigates, builds a short report, and **proposes a plan** the operator approves, edits or declines. The agent shows its work as it executes and writes to an audit trail throughout. Entirely mocked, no real data or execution yet | [[agent-inbox-alerts]], [[plan-and-execute]] | **Update banners.** First built expression of the C2 lane |
| **Declines become training data, and the learning loop is deliberately manual first.** Declining a proposed plan requires a reason. Those reasons aggregate: *"50 out of a hundred were declined because it needs a wider review, so what we need to do is go in, tell the agents, update the prompts."* George was explicit that this is **not autonomous learning yet** and that it should transition only once it is working with humans in the loop: *"it's gradually taking humans out of certain parts of it, but initially we're going to need them in"* | [[ai-analysis-impact]], [[plan-and-execute]] | Update banner. A design decision worth preserving |
| **Scheduled reporting was demonstrated, created conversationally.** The operator describes the report in natural language and the agent turns unstructured description into structured definition, then renders an example to correct before setting a cadence. Delivery is to the inbox for now, with email notification linking back to it as a later addition. **Rate limiting was raised unprompted**, so no client runs twenty reports hourly | [[scheduled-reporting]] | Update banner |
| **The three interaction modes are now named, and they are being built in isolation on purpose.** George's framing: **user-initiated ad hoc** (the conversational agent), **scheduled** (reporting), and **agent-initiated, human-validated** (the inbox). The distinction he drew: *"is it working with you or is it working for you?"* The plan is to build the three separately and then work out how they mix | [[full-agentic-experience]], [[agent-inbox-alerts]], [[co-pilot]] | Note added. Useful architecture of the whole client-facing surface |
| **The co-pilot is the acknowledged gap, and has a shape.** Michael: *"that's the only bit that's missing... if I'm on a page asking about a particular transaction."* George's answer: a co-pilot button that looks like a co-pilot but runs **the same agent behind the scenes**, scoped to the page, pulling in app state rather than rendering into the chat | [[co-pilot]], [[process-surfacing]] | Update banner |
| **Michael prefers the inbox in the left sidebar over the original prototype's co-pilot placement.** His reasoning is about the relationship rather than layout: *"originally the prototype was sort of very much co-pilot side... it naturally fits better in this left hand menu because you're more involved with it now rather than just ask it a question and go away"* | [[generative-ui-rendering]] | Note added |
| **The UAT split during Michael's absence is settled.** **Dorte and Ian do the user-side testing** as the closest users to the product: *"you can do a lot of the testing directly and it's not really developer wise. Obviously we need to cover off that customer support type role as well."* **Michael does the technical and tool-call testing before he goes**, and will *"send my UI agent at it as well"*. Dorte committed to *"put some proper time for testing"* | [[delivery]], [[open-questions]] #51 | **Register row updated.** The reviewer-coverage risk is materially reduced |
| **Ian still has not logged in.** Michael has sent him instructions again: *"I've just sent Ian some instructions as well. I don't think he's logged in yet."* First flagged on 20 August, and it is now eleven days later with the pilot functionally complete and Ian named as one of the two user-side testers | [[open-questions]] #51 | Register row updated. Persistent |
| **Direct Transact decommissioned the old spec URLs without telling anyone.** Michael: *"they decommission the old ones before telling us basically."* This is the actual cause of the 404 George hit on 25 August, rather than the credential rotation first suspected. **82 defects fixed** in the new release, most of them YAML: *"we should be getting closer to the actual source of truth now"* | [[open-questions]] #32, #67, [[txn-api-reference]] | Register rows updated |
| **Michael's Content Workforce session moves to after his return**, two one-hour slots, angled at the technical side of TXN. His own read on voice: he has plenty of documents but *"I don't really post on LinkedIn. It's all Marqeta gave me to post, so that's not really my voice"*, and the documentation is much closer to how he writes. He has samples to send. **Dorte and Ian go first as the test cases** | [[commercial]], [[content-workforce]] | Note added. A fourth content session moves past 15 September |
| Michael was running roughly twelve agents concurrently and crashing his laptop, which interrupted the call twice | n/a | Context, no action |

---

## Transcript

Aug 27, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:00**

**George Westbrook:** Sweet. They're not there yet. That's good. I need a haircut. I'm going to get my hair really short. Yeah. No, just shave my head. I'm not shaving my head. I've done it. I've done it once before. f\*\*\*\*\*\* awful. Uh you guys are no it's fine. Yeah. Wait. Hello there. s\*\*\*. I know. Wait.

**Brett StClair:** Ding through one of us

**Vineth Siriwardana:** You guys are in a good mood today.

**George Westbrook:** Uh as to what we're not usually How dare you f\*\*\*\*\*\*

**Brett StClair:** as to what we're not

**George Westbrook:** say that.

**Vineth Siriwardana:** All right, I'm I'm going to leave.

**George Westbrook:** Lazy bastard as well.

**Vineth Siriwardana:** I'm just going to leave.

**Brett StClair:** bastard as well as coming to the office today.

**George Westbrook:** Couldn't be asked to come into the office today.

**Vineth Siriwardana:** I have no way of coming. I would fly if I could,

**George Westbrook:** Nah,

**Vineth Siriwardana:** you know.

**George Westbrook:** you could have got a

### **00:01:06**

**Hasan Ahmed:** Bless the top.

**George Westbrook:** bike.

**Vineth Siriwardana:** Oh yeah, my bad. I I'll just walk it next time.

**George Westbrook:** Yeah. How we doing, Mike?

**Michael Moores:** Are you

**George Westbrook:** Good. Good.

**Michael Moores:** okay?

**George Westbrook:** Good.

**Brett StClair:** Good. Have you just had a haircut recently? I'm sure you have. You look quite smart and tidy there, Mike. compared to say

**Michael Moores:** Yeah. a couple of days ago. Uh, always before my holiday I,

**Brett StClair:** George.

**Michael Moores:** uh, I get it cut. So,

**George Westbrook:** Where you off to?

**Michael Moores:** Tan, well, this weekend we're going to Cardiff temporarily and then next week we're in Tanzania till the

**Brett StClair:** Yeah.

**George Westbrook:** Yeah.

**Michael Moores:** 15th.

**George Westbrook:** Bit different uh locations.

**Michael Moores:** Yeah, definitely. Um, yeah. So, not not too bad. So, you probably don't want to be going away this weekend. We've had a like a experience day that keeps moving for like this cocktail making, gin, rum making class, but the only weekend they can do for months is this one that just drops like three days before we go.

### **00:02:08**

**Michael Moores:** So,

**George Westbrook:** Yeah.

**Michael Moores:** just trying to slot it in basically.

**George Westbrook:** What? Double double holiday. Not too bad.

**Michael Moores:** Yeah, can't complain. Just see

**Brett StClair:** Only time I go to Cardiff is when there's a rugby game on. That experience with all those pubs and everything is the maddest experience.

**Michael Moores:** Yeah,

**Brett StClair:** Yeah.

**Michael Moores:** definitely. Not heard from the team if they're joining. One second.

**Brett StClair:** I've got a million WhatsApp from Da.

**George Westbrook:** I don't

**Brett StClair:** Let me just quickly have a look and see what she says. Trying to plan the rest of the sessions end.

**George Westbrook:** know.

**Michael Moores:** I've got another at the moment.

**Brett StClair:** Sorry, I added Lily to the stand up and I see it's just sent off a billion invites.

**George Westbrook:** Sorry.

**Brett StClair:** So, I do

**Michael Moores:** No

**Brett StClair:** apologize.

**George Westbrook:** Updated. Updated.

**Michael Moores:** worries.

**George Westbrook:** Updated.

**Michael Moores:** Yeah, no sign of a joint. So, I'm happy to start you

### **00:04:17**

**Brett StClair:** Yeah,

**Michael Moores:** guys.

**Brett StClair:** let's get cracking.

**George Westbrook:** Perfect. So, what are we what are we doing? What have we got to show? I think one of one of the main things we've been working on and thinking through is like conceptually that agent inbox and the reporting. So, it's all mock at the moment. Um there's there's nothing real happening, but I suppose it's just trying to think through what's a good user experience going to be, how do we want it to look like? Um, so it's it's quite natural for them. Um, one of the things we started as well is the that kind of dev mode as well. So it's going to include a lot more detail for you, Mike, so you can see the tools. That's not it's not done yet. Um, but we're we're working on that. So this is the kind of agent inbox thing for the for the alerts. So the idea will be what will happen? Alert happens. agent looks into it, investigates, builds a kind of mini report um as to what's happened.

### **00:05:14**

**George Westbrook:** Um there we go. There's the just joining. Hello.

**Dorte Dye:** Sorry, completely missing the plot. Yeah, I thought we were on the other meeting which we canled.

**Brett StClair:** And I sent through a million accidentally.

**Dorte Dye:** I know. It's like never give Brett the power. He's destroying your

**George Westbrook:** Yeah, you've got you've got to use the excuse you were getting a coffee.

**Dorte Dye:** outlook.

**George Westbrook:** That's my favorite one.

**Michael Moores:** It's

**Dorte Dye:** I just block him. How easy is that? What have I

**George Westbrook:** Uh it's really annoying.

**Dorte Dye:** missed?

**George Westbrook:** I can't I can't block Brett. He always finds a way to unblock me.

**Michael Moores:** okay.

**Dorte Dye:** Does he has finally some technical skills you didn't know about?

**George Westbrook:** I know. surprises is anything anything to do with Google. He's a whiz, so his emails always seem to find a way through.

**Dorte Dye:** I'm pretty sure Lily is behind

**George Westbrook:** Better not be. Lily sits next to me,

### **00:06:07**

**Dorte Dye:** it.

**George Westbrook:** so I need to I need to get like a cattle prod when she next does it. Go. Um yeah,

**Michael Moores:** Oops.

**George Westbrook:** I just just saying so one of the things we've been working on is the the concepts behind thinking around like the agent inbox and the reporting um that dev mode which I think's going to be relevant to see the see the tool calls when you're going along with the chat. Obviously something a user is never going to see but I think for us obviously it's good to to validate that. Um this is the like kind of first version of what we think the agent inbox will look like. So the idea will be an alert happens um gets sent to gets sent to us or we whatever we receive an alert the agent's going to then investigate is then going to build out this kind of mini mini report some might be longer some might be shorter and then what it's going to do given this let me refresh because I was testing this just before is it's going to propose a plan so given what it's found in this alert um it's going to say this is what I think needs to happen.

### **00:07:18**

**George Westbrook:** Um there's going to be an audit trail of what what's happening, what the agents done, what it's received. um can put more shout out bro that it's AI you trying to drum out m dashes from them is yeah to

**Dorte Dye:** Have you seen the other stuff what he did with his claw with his banking responses?

**George Westbrook:** be

**Dorte Dye:** Gosh, was he proud. Nina when it's spinking it always says something really funny like testing or bullying and I was

**George Westbrook:** oh Yeah,

**Dorte Dye:** like I've asked the finance team they said no not approved and all kind of s\*\*\* comes out of

**George Westbrook:** the where where Brett started changing them was that was quite funny.

**Dorte Dye:** us

**George Westbrook:** So one one day Brett left his computer on and um I was like I know what I can do here. So I changed all of them to just be taking the pit out of Brett and

**Dorte Dye:** he said and Max

**George Westbrook:** Yeah.

**Dorte Dye:** Right.

**George Westbrook:** Yeah. They It was an

**Dorte Dye:** That's that that's the new thing when you don't lock your PC, you know?

### **00:08:20**

**Dorte Dye:** It's like in the old corporate world, you were always punished.

**George Westbrook:** Yeah.

**Dorte Dye:** Someone sent the screen upside down or said something stupid.

**George Westbrook:** Yeah. Change the background

**Dorte Dye:** I'm so glad we're working remote.

**George Westbrook:** image.

**Dorte Dye:** I'm safe. Sorry, I shut up. Let's go to work.

**George Westbrook:** But yeah, so it's going to propose the propose a plan. I think there's still there's there's going to be more than more than this in the plan. Um, this is kind of it pre-analysis. Um, so obviously there's just approve. You click approve. It's going to show its work as it's doing it and then give you back the result. going to be updating the audit trailers. as well. Um I think what would be nice as well maybe um an impact an impact statement after um or the ability to run the impact before you actually even click approve. Um like I said, none of this is real. It's all just it's all just mopped.

### **00:09:14**

**George Westbrook:** So I can refresh it. If there's edits that you want to make, I'm thinking we add in like a a free text as well where maybe it's thinking the transaction limit is the thing that needs to be changed. It might not be. Speak to the agent, have a conversation. um and then change it or the quick actions. Let's put it at 350 300 and you can see what's what's going to happen. Um or just decline it and then choose the reason. Um which is going to act as kind of like training data as well. Um so that let's say it's needs a wider review. we can aggregate that use that in um updates so that we can go right let's look through all of the stuff that's happened in the agent inbox part and 50 out of a hundred that were declined because it needs a wider review. what we need to do is we need to go in, we need to tell the agents, update the prompts so that they're doing this wider review.

### **00:10:10**

**George Westbrook:** Um, so that over time it's albeit it's not kind of autonomous learning at the moment, it's more get the data, sit down, analyze, and update it.

**Dorte Dye:** Thank you.

**George Westbrook:** But over time, that can transition into that automatic learning where maybe we're running a a job once a week which is looking at all these reasons and automatically updating it. But obviously first it's we've got to make sure that it's it's working with us in the loop. Um the thing the same with anything with AI, it's gradually taking humans out of certain parts of it, but initially we're going to need them in. Um so in terms of like the UI, it's going to be this kind of this. So these are all the the ones that haven't been read. Um you can see all of them, look back in time, look at the audit trails, things like that. Um, raise a test alert. This is just for us internally testing to see what happens. Um, the next thing are the reports. So, this is where it's kind of those scheduled reports where each week you might want certain things that you want to that you want put in your inbox.

### **00:11:20**

**George Westbrook:** So, the way that we're thinking about creating the reports is you go in, you just speak to it and describe the report. So please build me a report that does XYZ and puts it in this format. Then like I said, it's all mocking it. So what the agent's going to do is take that unstructured information that you've given it, turn it into structured data so that it's going to build out this report. So if you want to go in, let's say it's it's messed it up. No, I want it to be consumer program and I want it to be for the previous month. You can still click around. Um, it's going to give you an example. You can set the set the cadence. Um, obviously there'll be more detail here so that maybe maybe if you want it every hour, we can have it every hour. Um, we can also probably maybe put limitations in. So there's not you or there's not companies or users who are having 20 reports that are running every single hour.

### **00:12:16**

**George Westbrook:** Um, put certain limitations on there. Um, and then obviously delivery at the moment it's always going to be inbox. But then we can add things like email notifications when the report is done which links to the actual inbox. Um I think with the inbox as well, we're probably going to want to have maybe it's segmented a bit so it's not all just alerts and reports. Um maybe think about that. It could be we show everything and then if they want to filter down or we could just have a separate report section um which is just just for those reports. Um, but I think yeah, apart from that, that's that's what we've been thinking. Like I said, this is all all mocked. We're going to we're going to the next layer or I think first it's iterate on the UI, make sure we're happy with that with the flows, how things are looking, then start adding in some real real AI, doing stuff, executing tools. Um, but I think yeah, cuz the the pilots's at a a good point.

### **00:13:19**

**George Westbrook:** I think there's still some of those changes with the the prompts where it's not saying I'm going to execute the update um update card holder tool in the in what the tool is actually called. Put it in actual human language so that they can understand. Um, but apart from that, it's just tiny tiny iterations. Um, and I think it's a good point where we can start powering ahead with with this stuff. Um, and making progress on all on all fronts so that we've got lots of avenues to make progress. So if some things bottleneck, we can still carry

**Michael Moores:** Yeah, it looks great. I think exactly what we had in mind.

**George Westbrook:** on.

**Michael Moores:** Um, yeah, still got the agent sort of style and the the uh the discussion topic there. So, I think that's great as well. Um, yeah. No, I think that's great. Obviously, we go and test it ourselves as well. Um, yeah, I think the order the sidebar looks good. Obviously, in the original sort of prototype, we had it all over the place versus I think originally the prototype was sort of very much co-pilot sort of side.

### **00:14:23**

**Michael Moores:** So, it was up up near the alerts where you just press the sort of like dark mode, but I think naturally it sort of fits better in this left hand menu because obviously you're more involved with it now rather than just ask it a question and go away type thing. So, I do like the way you've positioned it as well. Um, goes really nicely with that as well. So, yeah,

**George Westbrook:** cuz I think I think it's it's the different modes for an agent.

**Michael Moores:** great.

**George Westbrook:** Is it is it working with you or is it working for you? So, a lot of the stuff in here is it's going to be working working for you where you don't really need that chat. It's a bit of like this I want this change. Do it. There are maybe going to be situations here where a co-pilot or co-pilot feeling thing might be good where and this is where I think we need to we need to think is I think we build these three things in isolation and then work out how we can mix them in between so let's say there's something on here that you want to you do want to discuss with an agent then there is the co-pilot button in the corner which is going to look like a co-pilot but it's going to be exactly the same as this agent behind the scene um wherein it's it's got all the same smarts.

### **00:15:26**

**Michael Moores:** Yeah.

**George Westbrook:** It's just a bit more scoped to this specific page where like we said, it's going to be pulling in the the app data, understanding what's on the page, um rather than rendering rendering it in the actual

**Michael Moores:** Yeah. Yeah. I think that's the only bit that's missing sort of the services is obviously if I'm on a page asking about a particular

**George Westbrook:** chat.

**Michael Moores:** transaction for example I think that's the other avenue which is is really good and obviously that agent bought you know will be a large proportion of that anyway it's just obviously what it can get access to so obviously on our conversation from statworks the day just looking at the interjection points there so we'll get that document over to you soon just finishing that off but no I think this is a great great direction thank

**George Westbrook:** Perfect. Yeah. So, I think from from today on what we're going to be focusing is obviously refining this a bit. most of it is probably going to be UI and then try to get some actual like some stuff actually happening rather than just a a prototype.

### **00:16:28**

**George Westbrook:** um on top of the the dev mode um and changing those changing some of the prompts to make it seem more natural for a human to to look at rather than say us stop where we we see a tall call name and we're like that's fine like yeah I get that obviously users it's going to be bit different so I think yeah on the on the pilot front it's more just minor changes um but from our point of view it's it's it's done in terms of a pilot It's just progressing it to that next stage where it's as close to production ready as we can get

**Michael Moores:** Yeah, that's perfect.

**George Westbrook:** it.

**Michael Moores:** And obviously I have got a confirmation just before of the URLs have changed for the YAML. So, I'll get that back over to you properly. They decommission the old ones before telling us basically.

**George Westbrook:** Perfect.

**Michael Moores:** So, uh I'm just waiting for that.

**George Westbrook:** Yeah.

**Michael Moores:** It's just a small change to the endpoint. Um so, I'm waiting to find out why,

**George Westbrook:** Okay.

### **00:17:21**

**Michael Moores:** but I've got the new reals for you anyway. So,

**George Westbrook:** Perfect.

**Michael Moores:** I'll send that across as well. And that's um yeah, 82 defects of the YAML should have been solved in that new release as well. So, we should be getting closer to the uh the actual sort of source of truth now and stuff like that. So,

**George Westbrook:** Perfect. Well done. I think I think from our side that's that's everything. Is there is there anything say we've shown today or any other things that that you guys might want to bring up?

**Michael Moores:** No, I think yeah, from the look and feel of it, absolutely perfect. I don't think there's anything I saw that was a change. Obviously testing it, seeing how it feels is is the next But yeah,

**George Westbrook:** Yeah,

**Michael Moores:** I think the direction looks good and where you've positioned stuff works well. Um, it says that's great for me. Thank

**Dorte Dye:** Mike,

**George Westbrook:** perfect

**Dorte Dye:** how do we want to do it when on holidays.

### **00:18:07**

**Michael Moores:** you.

**Dorte Dye:** I mean,

**George Westbrook:** setups.

**Dorte Dye:** I'm mentioned it to Brad already. I'm I'm happy to join the course, but there is probably just very limited input I can give in a period your way to the team direction

**Michael Moores:** Yeah,

**Brett StClair:** actually.

**Michael Moores:** speak speaking to Ian on this one.

**Dorte Dye:** wise.

**Michael Moores:** Obviously yourself and Ian are the closest users to this is direct to that. So obviously you can do a lot of the testing directly and it's not really developers wise.

**Dorte Dye:** Hey

**Michael Moores:** Obviously we need to cover off that customer customer support type role as well. So,

**Dorte Dye:** Yeah.

**Michael Moores:** I think what you two can do is I can make sure

**Dorte Dye:** No.

**Michael Moores:** it's working okay and stuff like that. But, um,

**Dorte Dye:** Okay.

**Michael Moores:** yeah, I think that that's fine for my side. You want to continue with that and sort of feed that back in. I've just sent Ian some instructions as well on I don't think he's logged in yet.

### **00:18:59**

**Michael Moores:** So, he's going to start doing that and start having a look at from his point of view in his past as well.

**Dorte Dye:** Okay.

**George Westbrook:** Okay.

**Michael Moores:** Obviously, I'll do my testing and more specifically on the the tool calls and sort of more technical side I'm going to focus on.

**George Westbrook:** H.

**Michael Moores:** Um hoping to have a little run through it before I go from that specific side and obviously look at this new stuff as well uh and get back to you basically. But I'll also send my UI agent at it as well just so we can have a look

**George Westbrook:** Cool.

**Michael Moores:** and

**Dorte Dye:** Okay, I'll put some proper time for testing and then

**Brett StClair:** George,

**George Westbrook:** Which one?

**Brett StClair:** do you want to make sure that Ian's got

**Michael Moores:** try different variations from from our side of

**Brett StClair:** access?

**Dorte Dye:** is it Mike's internet? I thought I had a dodgy one living in the middle of

**Michael Moores:** the

**Brett StClair:** No. No. It's Mike's internet.

**Dorte Dye:** nowhere.

**Brett StClair:** Where does he live?

### **00:19:51**

**Dorte Dye:** But uh up north somewhere the mecca field. But at least he doesn't look as silly as I'm when I'm

**Brett StClair:** Okay,

**Dorte Dye:** afraid.

**Brett StClair:** there's feedback there. Um, so when you say up north is north beyond Chang uh King's

**Dorte Dye:** Yeah.

**Brett StClair:** Cross.

**Dorte Dye:** Why? No, he lives near Manchester Meccasville. Mike,

**Brett StClair:** That's that's not that that's not north.

**Dorte Dye:** sorry we lost you. Is west

**Brett StClair:** That's um north that that's north pole for

**Dorte Dye:** east.

**Brett StClair:** me.

**Michael Moores:** Sorry, I've got far too many agents

**Brett StClair:** You're back.

**Dorte Dye:** No,

**Michael Moores:** from

**Dorte Dye:** I told you he has he's having an army and is killing his laptop.

**Brett StClair:** We We know that feeling when your

**Dorte Dye:** Yeah, but I'm sure George is a very powerful machine,

**Brett StClair:** machine it is a

**Dorte Dye:** right?

**Brett StClair:** Mac kitted out to the max.

**Michael Moores:** that my laptop laptop can't support so keeps crushing.

**Brett StClair:** Well, you've just made us proud, Mike. You've made us proud.

### **00:21:00**

**Michael Moores:** I try I try and make sure they finish, but there's there's about 12 running at the moment. So, uh, it's shutting things down to try and give itself some

**Dorte Dye:** Brett, what while you and Mike are on the same call right now,

**Michael Moores:** room.

**Dorte Dye:** should we quickly just touch base on what is from Mike required for the content workforce and how long it will

**Brett StClair:** Yeah. So, I think Mike,

**Dorte Dye:** Okay.

**Brett StClair:** we do your content workforce when you're back. And um on that side, we we we should be pretty tight by then. We'll do two 1-hour slots. Um and really your approach is going to be from TXN's kind of point of view but more technical whether it's technical around um how you build or technical how you uh deploy card services and stuff. So we'll work on your content manifesto. It really is we're trying to map you and then we work out content pillars from that and then we map a brand identity and it's kind of how you like to speak all that kind of stuff.

### **00:22:05**

**Brett StClair:** Um so we'll do it when you're back when your mind's feeling fresh and it's stuff that you never really think of so it is quite intense. Um what's wrong?

**Dorte Dye:** I'm sure Mike has documents already. I mean, his tone of voice for all of the documents is already nailed down.

**Brett StClair:** Oh really?

**Dorte Dye:** It's literally just me being all over the place.

**Michael Moores:** Yeah, obviously I've got loads of documents. I don't really post on LinkedIn or anything like that. It's all Marqueta gave me to post. So that's not really I'd say my voice. So yeah,

**Brett StClair:** Yeah.

**Michael Moores:** the documentation is much closer to how I write and stuff like that. So um I've got a couple of samples I sent can send across.

**Brett StClair:** Okay. We'll we'll schedule some time when you're back. Uh but our test dummies will be Dorte and uh Ian.

**Dorte Dye:** Looking forward to it.

**Michael Moores:** Yeah,

**Brett StClair:** Awesome.

**Michael Moores:** perfect.

**Brett StClair:** Anything else? Okay.

**Dorte Dye:** Nope. Cool.

**Brett StClair:** Happy days.

**Dorte Dye:** Thanks, guys.

**Brett StClair:** Thanks, guys. We're gonna let Mike's agents do some

**Dorte Dye:** Take care.

**Michael Moores:** Yeah.

**Brett StClair:** work.

**George Westbrook:** Speak to you soon. Have a good one.

**Brett StClair:** Cha cha.

**Michael Moores:** This bite.

### **Transcription ended after 00:23:39**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*