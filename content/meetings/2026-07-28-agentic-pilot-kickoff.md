---
date: 2026-07-28
type: general
scope:
  - "[[agent-access-layer]]"
  - "[[co-pilot]]"
  - "[[architecture]]"
  - "[[txn-api-reference]]"
status: extracted
extracted-to:
  - "[[agent-access-layer]]"
  - "[[mcp-server]]"
  - "[[permission-scoping]]"
  - "[[full-agentic-experience]]"
  - "[[guided-onboarding]]"
  - "[[integrations]]"
  - "[[open-questions]]"
---

# TXN Agentic AI Pilot Kickoff (2026-07-28)

> **Source:** Fathom transcript, synced from the shared folder (`shared/txn/meetings/`). Attendees: Brett StClair, Dorte Dye, George Westbrook, Hasan Ahmed, Max Kingaby, Michael Moores. Duration 00:34:54.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Pilot build order: mock DT API → monolith MCP (all tools, no scoping) → scoping later | [[agent-access-layer]], [[mcp-server]], [[permission-scoping]] | Update banners added; supports register #42, #2 |
| React replica of the Control Center is the pilot build base; chat/agent space is the only review surface; sidebar entry point TBD | [[full-agentic-experience]] | Update banner added |
| First build slice = onboarding (LLM + one workflow, end of week; mock API, URL flip to real later) | [[guided-onboarding]] | Update banner added |
| API status: Friday spec latest; YAML quality (missing limits) is the main issue; possible program manager ID field; UAT access + key offered | [[open-questions]] #32, [[agent-access-layer]] | Register row updated |
| DT architecture discussion down to four points, still the foundation blocker; Novosapien terraforms + deploys once decided | [[open-questions]] #48, #49 | Register rows updated |
| Stackworkz: knowledge hub handed over (DT code review); Console renamed "Control Center"; Super Ultra prototype final; "Sunpox" access blocking sign-in testing | [[integrations]] | Update block added (Sunpox flagged as transcribed) |
| Synthetic-data environment is pilot step one; TXN to review data realism; mock API randomises responses | [[open-questions]] #43 | Register row updated |
| Review mechanics: screenshot-based UI/UX feedback tool + in-chat agent-execution feedback button (voice planned); feedback aggregated with full chat history for bulk changes | — | Context captured in transcript; part of ways of working, no doc change |
| Ways of working: standups roughly every second day, 15-20 min, name TBD ("touchdowns" floated); sign-off phrase TBD; vault-based async reviews, all audited; started a week early, aiming to compress toward 3 weeks; next call Monday 11:00 | — | No action (process/logistics) |
| Content workforce: Brunwin session to be scheduled; LinkedIn groundwork before September; product extensible if gaps found | — | Action item (GTM Workforces scope, separate from this vault) |
| Invoice paid | — | No action |

## **TXN \- Agentic AI pilot Kick off  \- 2026/07/28 13:00 BST – Transcript**

# **Attendees**

Brett StClair, Dorte Dye, Dörte's Fathom Notetaker, George Westbrook, George's Fathom Notetaker, Hasan Ahmed, Max Kingaby, Michael Moores, Michael's Fathom Notetaker

# **Transcript**

Brett StClair: That's why I was pretty in here.

Dorte Dye: Hi guys. my Phantom is in. That's weird.

Brett StClair: We got Mike in here.

Dorte Dye: I No,…

Brett StClair: We can invite George's as well. that meme…

Dorte Dye: I stopped because I thought there is a Mike mentioned that Google allows one. So, I took mine out and mine is in. I don't know what's going on.

George Westbrook: mind if you join in.

George Westbrook: Mine's in now.

Dorte Dye: We all just jump off and let the AI do the meeting.

George Westbrook: There you go.

Brett StClair: where there's more note takers than meeting attendants.

Dorte Dye: And then they're all different anyway.

Dorte Dye: So, it's awful.

Brett StClair: Hello Mike.

Brett StClair: We received payment on the invoice. So, thank you very much for processing that.

Dorte Dye: So, now the pressure is on you.

Brett StClair: Not the weekends are for a weekend is you get a strong And you get a weekend for the rest of your life.

Dorte Dye: That basically means you have to deliver the pilot in four weeks…

Dorte Dye: till the end of the month. Easy. There you go. I think that's…

George Westbrook: What are weekends?

Dorte Dye: what George is for, right?

George Westbrook: What's a weekend I know the office is not as busy…

Dorte Dye: That's the things as a founder George you never heard of and you will never experience…

George Westbrook: which is quite nice.

Dorte Dye: but then on the other hand you got paid which doesn't happen often either right okay thanks for jumping on the call I just wanted to use the opportunity to just align what's happening in the next six week how the cadence will work because Mike is off for a couple of days, Ian is off for a big chunk. I just have couple of days, but how it all will slot together. I've also contacted Brunwin Brett to have a session with you and her to run through the content manager.

Brett StClair: Hat.

Dorte Dye: So then because it's a remate marketing, right?

Dorte Dye: We really like what we have seen but we need just someone behind the scenes maybe to do some things on the end or not if we all do do it…

Dorte Dye: but we just want to make sure that she is in the loop of everything and provide some input as well. So I will come back to you once she has come and proposed some dates because her diary is normally a bit more crazy.

George Westbrook: I think one thing that's worth mentioning with the content workforce as well is if there's certain things you don't like or there's certain gaps, it's not like this is the product,…

George Westbrook: this is what it is. We're not changing anything. Obviously, we build that in the same way that we're going to build all of your stuff. So, if there's anything that you think would be a good addition, it's obviously bit different to what we're building for you where obviously if you say X, we're going to build X. the products there might be a bit more like okay we'll think about this think about that but there's scope to add stuff in…

Dorte Dye: No. And again,…

George Westbrook: if there's gaps. Yeah.

Dorte Dye: that's perfect, But by the sounds of it, we don't really need proper marketing input if that makes sense. It probably between the three of us that we can run it. But on the other hand, we still want someone with that expertise challenge before we take anything over in house and everything. And I think with this one, we need to think about as well how we want to start off if we're launching in September because there might be some ground work to be done on our profiles as well.

Dorte Dye: That would be a nice one to No, not that.

Brett StClair: We'll help you with that.

Brett StClair: We've got a bunch of system prompts that we help all our CEOs with that walk you through, jazz up your LinkedIn, and properly set it up really.

Dorte Dye: That's what is good in the summer, So, we can just do it alongside everything else before it gets really mental and…

George Westbrook: Honest.

Dorte Dye: then September. but I shut up.

Dorte Dye: Let's get to the real work.

Brett StClair: It's also a good point.

Brett StClair: Bronin's never really seen the content workforce either.

Brett StClair: I don't really talk business with Yeah.

Dorte Dye: No, I believe they're all working the old fashioned way in marketing and…

Dorte Dye: everything. So, it would be nice to get the two parts together and also to see how far they have come with the website because now our knowledge hub is up and running and the next part will come shortly after. So, how do we bring all three of them together and then managing it from one angle.

Brett StClair: So, can I walk you guys through ways of working?

Dorte Dye: Yep.

### 00:05:00

Brett StClair: I guess is a good place to start. and how we going to deliver and deploy, how we going to manage the knowledge repository or the bolt? and a starting point. so, let me caveat it. We've actually started a week ago, because we were worried about timelines. So, we've just got kind of the baseline preparation, all that kind of stuff going already. and essentially how we'll work is we'll set up standups and…

Dorte Dye: Mhm. Okay.

Brett StClair: I think we just need to look at diaries and let's not make it every probably every second day based on your who's when And what we do in the standups really is we see how we all have a nice chat, and then we do a quick update on what's been coded, the status How we'll be working is as we do releases, we're going to publish it into the vault. And so this is not about gating things. We want to remove all gates and keep the flow of information feedback and cadence and conversion into code etc. liquid as liquid as possible.

Brett StClair: And so I think it'll work quite well with your holidays because you guys can go on holiday and know that it's still Cheesy analogy, but it doesn't stop because you've gone.

Dorte Dye: Mhm.

Brett StClair: And so the reason why we do it in a vault, you can do the reviews, do your feedback in your own time, wherever you are, whenever you are, however you want to do it. If you want to do a quick 5minute review, you jump in, you do a quick fiveminute review. If you got something to contribute to it and you want to change something, you do it. If not, then that's fine. We're working on the next round of releases. If you come back 3 weeks later and go, I've been using this and I really can't stand how it starts. And all of this code is throwwayable. Even if you were in production, we can throw it away and we get it rebuilt.

Brett StClair: So, I don't want you guys ever stressing about a decision and thinking that everyone has to get a review on it. If you got a great idea, you want to give it a bash and you want to try something different, you pop it into the review, you highlight the area. We're going to be building some really clever automations off the back of it as well. And then the standups really are to kind of just touch base as humans. So, we got face to face. Did you see that? What do you think about this? We've done a new component here. We're trying something different. we're responding differently here, etc. The point of this is a pilot, so We need to create a working environment with synthetic data and we need to make sure that that data is holding together. So, probably step one is getting that environment set up, making sure that the data looks real. So, what we'll be asking of you guys is to just do a quick review. Does it feel like it would be as in live?

Brett StClair: is this data really kind of what it would look like and give us some feedback there. Then the next step is we start the build process. we're going to try to get this done as quickly as possible. If we can get it done in 3 weeks, we get it done in 3 weeks. We know 6 weeks is tight, hence why we've started a week earlier. So we know we're working towards a bit of a deadline. we're working non-stop. So we're still confident we'll be able to hit it. I'll just chew up some weekends and my weekends are spent in a spa and I have this camera in the office that just looks at her son George and…

George Westbrook: That's a rare occasion that we laugh at one of British jokes.

Brett StClair: and Max and I like this is great and I drink champagne and I don't really do No, I'm kidding. it doesn't look like that. Just bad. Just seeing how much Max is listening.

Max Kingaby: No, I was just laughing at your joke,…

Dorte Dye: Thank you.

Max Kingaby: I was waiting for the punchline, but once again, just never came.

Brett StClair: You have to push the laugh button. Come on. This is Damn you guys.

Dorte Dye: Classic dad jokes. He doesn't get any

Brett StClair: You're bloody difficult audience. so that's going to be the approach to everything. the final sign off is a bit like the vault, So, you're going to have everything through the vault. Once you're happy with everything, everything is teed off. In the vault, we track absolutely every single review and change and make sure that it's been processed or if you decide you don't like it, we dismiss it. But everything is audited,…

Michael Moores: Amazing. Thank you.

Dorte Dye: No, sounds good.

Brett StClair: so nothing is lost. Any questions?

Brett StClair: Happy day. So, what I'm going to ask George to do, and I don't know if you're ready, George, or do you want to do this later?

### 00:10:00

George Westbrook: No, that's fine.

George Westbrook: One thing I suppose I'd talk about is the process of reviewing. I know we've talked about it before. but I suppose the two main review surfaces are going to be like UI UX, which is I think we showed it before where there you go in take a screenshot of the page. There'll be a tool that will do this. and then you can just click be like, right, this agent tool call message, I don't like this. It says there's too much information. this needs to be rounded a bit more. So, kind of look and feel stuff. and then the actual kind of the actual agent execution.

George Westbrook: So, what we'll do, let's say you're testing it out, maybe after we've simulated some stuff, let's say the agent, the language is a bit too informal, is there'll be a button, click it, put in your feedback. I think what we'll do is we'll probably add a way to do it via voice as well. then it's going to get the whole chat history. It's going to understand everything and then we'll load it in that way. So we'll see the full chat history, we'll see your feedback, we'll aggregate all of it and then make changes in more of a bulk fashion. so look through, okay, maybe we need to change the prompt, maybe we also need to change the way that the tool calls represented. and then we'll have all of the API calls, all of the results as well. So it was too informal and then we just go in and update the prompt. It's grounded in what actually happened in the chat that you were speak speaking to it with.

George Westbrook: we'll do something similar behind the scenes in a higher scale but obviously users being user feedback we want to hold at the gold standard. So I suppose then that kind of leads into what we've been doing in the last week is so With the pilot, I suppose there were two approaches we could have Just do everything in isolation. We kind of make up the look and feel and get it we think kind of looks nice. Or what we actually did, which we've basically built a version of the console with the prototype.

George Westbrook: So in the stack that you're going to be using in React, there might not be exactly the same as what stack works are doing, but what we wanted is something that feels, acts exactly like what the console is going to be given the prototype that we've got. so that when we're testing alerts, when we're testing the agent, we've got all the styling, we've got all the components. and it understands how the flows are. So that say for example we're building a skill or an SOP which is going to issue cards. It's going to understand how it works in the actual application. So then when it's building the skill it's going to understand a bit better. So I'll just show it now.

George Westbrook: Suppose it's going to look pretty much exactly like the prototype, but we wanted to make it real as possible. so what we'll do after this is we'll deploy it so that you can have a click around if there's any issues. But this is going to be the base that we build off of.

George Westbrook: So is that there we go.

Brett StClair: Can you zoom in just slightly?

Brett StClair: Thank you.

George Westbrook: So what we'll probably do maybe add in an agent here or somewhere where it won't really matter. but I say if you click around it's going to be exactly like the application. obviously some of it's kind of mocked. it's all like the platform health and by the way we thought that we were saying this earlier the designers have done an amazing job on this. It looks really good. what else is there? So it's basically everything that was in the prototype is built in React. It's fully functional obviously all mock data.

George Westbrook: Maybe what we could do when the APIs are available is connect to them. Obviously we won't have maybe the security hardening because obviously this is not something that's going out in the real world. This is just going to be for internal use. there's a documentation as well. there's an agent working on it in the background. So, if something doesn't load, that might be why. There we go.

George Westbrook: Yeah, so the API reference this will be handy for the agent as well. obviously with the YAML and it's going to really help. So it's got the playground things do disappear. so yeah, it's basic everything's there. So like I said, why have we done this? So when we're creating the aentic experience, it's going to use exactly this styling and exactly these components that are within the application. So if we go back to the console, let's say we wanted to show the transactions. What we would do is take this actual component and render it within the chat.

### 00:15:00

George Westbrook: maybe change it slightly. in terms of we're obviously probably going to squash it a bit. but maybe I think we showed on the outbound where there's the canvas on the right hand side. So if it's like I want to review my transactions, it's going to render it on the right hand side. It's going to look like this. The user can speak to it and say, " can we review, let's say there's a tick box here. Can we review this one?" Then it's going to fetch it and it's going to be working alongside the user. but we've got this base now. So it's took a bit of time but we've got the base to push off of. I think one of the things to bear in mind is all the UI stuff is very easy to get to that 80%. you might look at it in a week or two weeks be like it's all done. amazing. It's not.

George Westbrook: It's that last 20% takes so much time. it's all the behind the scenes, all the iterating things like that is where a lot of the time is. Hence why we've got the reviewing process which speeds it up so that not just so we can see it but also the agents can see it as well. Okay. I think yeah that's our console replica. so I suppose we've gone through the standups,…

George Westbrook: gone through the ways we're going to be working. what else do you think

Brett StClair: I think…

Brett StClair: what we need to think about is the start of the journey just from an experience, So, we've got the replica. where's it going to sit on the sidebar? a lot of that kind of UX style thinking about where we're going to put this Aentic AI experience. do we the pilot's going to be there so that's different. on boarding it's going to open up into that shared kind of co-pilot experience.

Brett StClair: So that's different. So, I guess it's just find an area on the sidebar.

Brett StClair: something that makes sense. Give it a name or whatever some iconography we click on it and then it'll open up that kind of claude styled experience. I don't think we need to worry too much more than that. just that if you guys are happy, we have a space in your navigation Drop it in there. You click on it, opens up, and then it's about how we reuse when we do pull up those graphical user interfaces that we actually reusing the same look, feel, and style that you're running at the moment. so if it's a graph or a dashboard or a table, it looks in similar to the tables that you're currently running at the moment, that's going to be a really important trap.

George Westbrook: Yeah. And in…

George Westbrook: because I think one thing that could happen is maybe stack works diverges a bit and maybe this isn't exact. Not too much of an issue. we just kind of either port over or copy what they've got then we can carry on working. Like we said code is relatively cheap now. so a lot of the work will be behind the scenes with the agent. so we want to change the UI in aligned with…

George Westbrook: what Stack Works has. it's not weeks, it's days.

Brett StClair: next steps…

Brett StClair: what we're going to do on our side is we're going to kick off doing the first version and we're going to be layering it. So we'll be going through each of the vaults kind of sections picking out an experience that we want to manage and I guess George will probably start with the onboarding right from that point of view and then layer it up start getting those components right we'll probably need a couple of days I assume two three days to get that first iteration out what are your thoughts

Brett StClair: Go.

George Westbrook: probably by the end of the week.

George Westbrook: Something that gets the look and feel maybe on boarding flow as well, but what it could be is more like we'll get something out by the end of the week. there will be an LLM attached and then maybe one workflow as and I think envelope said on boarding will probably be one of the best to start with. once again it's not going to be obviously connecting to the real APIs. we'll build a mock API. Make sure that it's randomizing the responses as well. So it's not like every single time it's doing exactly the same thing. so from a presentation perspective it's going to appear to be the real thing.

### 00:20:00

George Westbrook: And then obviously once we've got the real APIs, it's going to be a matter of just flipping over the URLs.

Brett StClair: Do you want to be building those stubs based on as latest version of the current API set,…

Brett StClair: George, so that when we do the switch out, it's not too much of a

George Westbrook: Yeah,…

George Westbrook: I mean the latest that we've got as of today today or tomorrow would be ideal. if not it's not too much of an issue like we said we can just rebuild it. I'm assuming it's not going to be completely ripped down and then completely changed. It's going to be a field is slightly different or this payload has got two extra fields and one taken out which isn't too much of an issue.

Michael Moores: Yeah. We've got latest one from Friday which is the biggest issues right now is the YAML quality basically. It's missing the limits and stuff like that.

Dorte Dye: Thank you.

Michael Moores: So, they're doing a lot of work on that.

Michael Moores: The actual payloads themselves aren't changing too much. we're still finding out the architecture which may strip a few extra fields going from that sort of single API instance versus separate that we discussed, we're still out and…

George Westbrook: Yeah. Perfect.

Michael Moores: obviously if we do keep that then there'll be an additional sort of program manager ID field for example just to route certain things.

Michael Moores: But yeah, I can send you one from Friday that we've got there is an API now. So for the ammo as well specifically. So you can pull that as well. I'll make sure I can share my key in UAT. They might benefit you doing it perhaps a stage earlier in the development side.

George Westbrook: Okay,…

Michael Moores: So I'll speak to the team and…

Michael Moores: see what they think. But I have got UAT access and that API at least to start off as well.

George Westbrook: perfect. Yeah.

Brett StClair: George, will we use that link that you've built for the demo?

Brett StClair: We'll publish that to the vault, So guys can click around in the other areas, but that all the other areas are not really that relevant for us. we just needed the components when we're inside the actual chat kind of stream. So that's why that's being built out. so when you do your reviews, don't worry about reviewing the other stuff because those are not the components we're going to be doing. It's going to be focused on the reviews within the chat and agent space that those are going to be built out to you.

Michael Moores: Stop it.

Brett StClair: I don't really want to waste your time or…

Brett StClair: you going, " I don't like that there." Yeah, don't worry about it. Happy.

Dorte Dye: So how does it work?

Dorte Dye: The pilot had three building blocks, didn't it? It had the full agentic experience, the internal ops and then the agentic access layer.

Dorte Dye: So are we tackling then the last one first the internal ops and then you have roughly some ideas when you would start the other ones or all very agile.

George Westbrook: So I think with the first it's kind of two buckets in one with the full agentic and…

George Westbrook: So first level of the access layer is going to be let's just build the mock API.

Dorte Dye: Mhm.

George Westbrook: So it's going to be taking the structure of the API. and then creating the MCP server over the top of or first step is let's replicate the API. then once that's done, let's build the first version of the MCP server over the top of it. So, it's probably not going to have all of the access stuff initially. that's something that we'll add in later. So, I think what we might do to start with is one kind of monolith MCP with all the tools built in.

George Westbrook: Then next step will be the access stuff. So given a user and their access levels on which tools do we turn off? but I think for first let's build the monolith all access to everything. get the full agentic experience the UI sorted the back or the agent. get that working so that there's something to test and then as time goes on we refine that.

Dorte Dye: Okay, sounds good.

Brett StClair: How are things on your guys timelines? Are you guys still on the same cadence as we last spoke? Because it has been a couple of weeks,…

### 00:25:00

Brett StClair: I guess. is anything that we need to be aware of? if you're boarding forward or you happy with where everything's landing if we are pushing for kind of our original timelines anything we need to be aware of I guess just yeah and that's

Dorte Dye: I mean,…

Dorte Dye: we still pushing for the original timelines, but we are still in an architecture discussion with DT. I think we nailed it down to four points at the moment.

Dorte Dye: And the sooner we can put that to rest easy everything else comes right.

Dorte Dye: So Mike has really a hard job to have everything a flawed and all of the different parties without the foundation. That's the challenging part at the moment.

Brett StClair: Yeah, cuz I was thinking about that infra.

Brett StClair: This is the architecture you're talking about. Yeah, I was thinking it was a bit quiet on that from our side. Super easy.

Brett StClair: Once you've decided, we terraform everything and deploy. So where it should be everywhere I hate using that word the salesman approach to delivery.

George Westbrook: Yeah, touch wood.

Dorte Dye: Yeah, that's commercial.

George Westbrook: Mr. Super easy.

Dorte Dye: What do you think, George?

George Westbrook: 

George Westbrook: I'll be all right. Taste the Ted.

Dorte Dye: We don't need legal product compliance.

Dorte Dye: Anyone can do that.

George Westbrook: No. How is Stack Works getting on?

Dorte Dye: Brilliant. No. so they have handed over the knowledge hub.

George Westbrook: Where's their status on things?

Dorte Dye: So DT is doing the code review. There are some outstanding items at the moment. and they're scoping the console and I forgot the name for the console now.

George Westbrook: Control center.

Brett StClair: the console.

Dorte Dye: No, we have renamed the control center.

Brett StClair: 

Brett StClair: Let's see what Yes,…

Dorte Dye: The control center. So, they will start charting on that one as well, but again there certain elements they're waiting for. So, they will do the similar approach to you guys start doing the frame and…

Dorte Dye: everything and then hopefully by the time DT has caught up with the API so that they can actually do the connections. So I'm sure you have seen the latest one.

George Westbrook: Is there an updated prototype from Super Ultra that Stack are working from or…

George Westbrook: is it just the same one that we would have been sent over?

Brett StClair: Okay.

Dorte Dye: So we had done the extension where they worked two more weeks and then they have handed over. I believe you were in that one. So there's nothing else after that that came out.

Dorte Dye: And again to the knowledge h the only outstanding items is the Sunpox access.

Dorte Dye: So we can't really do any proper testing of it yet because the sign is not there. So it's more look and feel at the moment.

George Westbrook: Okay. Mhm.

Dorte Dye: But then hopefully that gets sorted in the next couple of weeks as well so that the knowledge hub is all done for the launch and then at the control center we have a little bit more breathing time. Mike

George Westbrook: because I'd say what might be worth once it'll be sometime this afternoon I'll get that our version of the console deployed it'll be on our infrastructure obviously deploy link sent over if you just have a click around through some of the pages just to make sure that it is that exact version of the prototype if it doesn't matter too much we can do that at a later point where we're taking the new version and we re rebuild

George Westbrook: and then Yeah, but that's not going to stop anything.

Michael Moores: Yeah, I think it's the final version.

Michael Moores: I'll just double check though. But yeah, if you send across, I'll have a look.

Brett StClair: Awesome,…

George Westbrook: Perfect. Yes.

Brett StClair: guys. So, at the end of standups and we've got two choices that we've got to make. What are we going to call these standups? Do you want to call it a standup or do we want to call it a transaction or keep that thing?

Brett StClair: And we only put it out there because we have some customers who call them touchdowns because a NFL trading app so everything is a touchdown. if you want to keep it to a standard, we keep it to a standard. We do have customers who keep it to standups. if you do want to rename it, it can be a little bit fun. Does never take Max's suggestion.

George Westbrook: Touchdowns. Sure.

Brett StClair: You're getting the butter of all my jokes today, Max. and then touch down.

Max Kingaby: When the joke's going to start then, just so I know to ready myself.

Dorte Dye: That's alone.

Brett StClair: Have a think about that. We can decide in the next one and then I'll set up all the timings. No daughter. you and I spend a bit of time just allowing the right kind of times to do that. we try to do them after just because the teams are working till 1 2 in the morning most days.

Brett StClair: 

### 00:30:00

Dorte Dye: We know that torch is not working before 10:00.

George Westbrook: Yeah, I was very happy when this one was 1:00 cuz sometimes the 10:00 or…

George Westbrook: the 9:00 ones it's Good morning everyone.

Dorte Dye: I'd rather you are awake and…

Dorte Dye: we are in the middle of the day than the other way around.

Brett StClair: All right.

Brett StClair: And then at the end of every standup, we say something. And so we just got to decide what it is. I'm going to let Max share with you what one of our customers says.

Brett StClair: I don't know if you want to go with that phrase. So, it's kind of like a get everyone motivated like come on guys,…

George Westbrook: He accidentally left.

Dorte Dye: I think

George Westbrook: The pressure was on.

Brett StClair: let's go kill it or let's go smash it or let's go. These guys go let's f\*\* go. is their big thing and they shout it out and…

Brett StClair: everyone's like yeah, you don't have to do that.

George Westbrook: They're American.

Dorte Dye: But they don't swear. This is what I don't understand. Americans supposedly don't swear.

Brett StClair: I know.

George Westbrook: I think they've spent too much time with us. I think it's worn off.

Dorte Dye: I've not heard you swearing yet. So that's something to keep an attention on.

Brett StClair: Your name's not Claude.

George Westbrook: Yeah, I think yeah,…

George Westbrook: Claude is I'm going to be one of the first to be killed by the AI overlords, I think.

Brett StClair: Have a think about that as and…

Brett StClair: and just a out could be a sign out. Roger that.

George Westbrook: Yeah. Yeah.

Brett StClair: Rog Who's Roger?

Dorte Dye: You're listening to the call.

Max Kingaby: Thank god not another one but it's the dust something like that be quite cool.

George Westbrook: Or we all cheer because Brett's leaving the call.

Max Kingaby: 

Max Kingaby: That was bus.

Dorte Dye: I'm joined.

George Westbrook: Yeah. When he joins,…

Dorte Dye: Cool.

George Westbrook: we go, " yeah.

Brett StClair: When I'll go first every time and…

Brett StClair: then you can all go crazy how do you think about those two things just to make it a little bit more fun…

Dorte Dye: Yep. Just one quick question.

Brett StClair: because we're going to spend a lot of time together. so we do keep it pretty casual though it is professional and formal and make sure good work stand.

Brett StClair: Let's have a bit of fun together.

Dorte Dye: How long are the standups?

Brett StClair: Anything from 15 to 20 minutes.

Dorte Dye: Okay, that's fine. Cool.

Brett StClair: Y we want to straight in I'm getting roasted by you too.

George Westbrook: I thought we were going to do twoour standups.

Dorte Dye: If he wants to put his stats in, then we might need to. But Maybe that's our signing off.

George Westbrook: We'll get a shot caller for Brett as soon as we hear a dad joke start.

Max Kingaby: You have to get some big back, please.

Dorte Dye: No jokes. We survived another meeting without a bad joke.

George Westbrook: We never say it though.

Dorte Dye: We can repay him. So, okay,…

Brett StClair: Yeah, awesome.

Dorte Dye: we checking diaries then later, Brett, that we get everything scheduled.

Dorte Dye: I have holiday calendar already for you. So we plan around it. don't do that. before we jump off when do we want to catch up while we're all on the call this week then?

Brett StClair: Okay, we'll do that.

Brett StClair: So, should we quickly load that in?

Dorte Dye: Fine for me.

Brett StClair: Let me just see how does Thursday 11:00 a.m. sort suit So,…

Dorte Dye: M looks clean as well. you're off the rest of the week.

Michael Moores: I'm off rest of the week.

Michael Moores: I've got tomorrow and I'm off rest of the week.

Dorte Dye: Clearly, I haven't got the holiday calendar proper.

Brett StClair: how about Monday? Because then at least we'll have a bunch of stuff done by Monday.

Michael Moores: That's The carrot.

Dorte Dye: Cool. Yeah,…

Brett StClair: Monday 11:00 a.m.

Dorte Dye: then. Perfect.

Dorte Dye: Speak later.

Brett StClair: I'll get that set up.

Brett StClair: Awesome. Thanks, guys. Let's go.

Dorte Dye: Take care.

Max Kingaby: Thanks everyone.

George Westbrook: Perfect. Thanks very much.

George Westbrook: Speak soon.

Brett StClair: Cha chia.

### Meeting ended after 00:34:54 👋

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*

