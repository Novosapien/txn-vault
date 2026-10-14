---
date: 2026-10-14
type: general
description: "Three-way alignment: Novosapien builds inside Stackworkz's codebase, the llms.txt becomes a router, and Stackworkz want the agent in Control Center"
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
  - "[[architecture]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Alignment Call, TXN with Stackworkz and Novosapien (2026-10-14)

> **Source:** transcript, 14 October 2026. **Novosapien:** Brett StClair, George Westbrook, Hasan Ahmed, Lily StClair. **TXN:** Michael Moores, Dörte Dye. **Stackworkz:** Ruan Sunkel, Armand Pretorius. **Ian Johnson absent**, travelling.
>
> **A note on attribution.** This transcript is diarised as "Me" and "Them". **"Me" is Brett**, so his lines are certain. Everyone else is merged into a single speaker, so the names against the other quotes below are read from context, and the technical explanations are attributed to George and Hasan, and the Stackworkz positions to Ruan, on that basis rather than from the transcript itself. A few short lines are too garbled to use and have been left out. Some names are mangled in the source, including a Stackworkz participant rendered variously as Cornel, Cornelia and Kuneel, so no quote is attributed to them.

**Why the call happened.** Brett: *"get the 2 teams to sync over the dev portal. How do we get the Copilot linked up to you guys... figure out ways of working, your coding standards, how do we work together to get it all done."*

## The main outcome: Novosapien works inside Stackworkz's codebase

This is the first time the two build teams have agreed a working method, and it was settled quickly.

**Stackworkz proposed it.** Ruan: *"I think it would be best if we give you access to the codebase and you make your changes."* Then: *"We can even show you how to run it locally."*

**George accepted and set the terms himself:**

> *"We get access, we'll obviously test it locally, push it to whatever branches that you need for it to be deployed onto the testing environments, and then go from there to get it into production... You guys review it, make sure that we're not stepping on your toes. If there's any coding standards that you want us to abide by, let us know, and then we'll make sure that we fit into the way that you guys have done stuff."*

| Element | Agreed position |
|---|---|
| **Codebase** | Novosapien gets access to the Knowledge Hub codebase |
| **Who writes the code** | Novosapien implements the co-pilot in it |
| **Who reviews** | Stackworkz, with standing permission to object early |
| **Standards** | Stackworkz name them, Novosapien follows them |
| **Branches** | Whatever Stackworkz need for their test environments |
| **Access** | George sends the usernames after the call |
| **The Console later** | Same method, *"not just yet, but hopefully rather than later"* |

**The reason both sides wanted it.** George: *"you guys have got like loads on your plate, so the last thing you need is getting access to a random codebase which is kind of similar."* Michael, on the replica Novosapien has been building against: it was *"a kind of quickish thing that we were using to kind of get going, get ahead. So it's not perfect; it's just a base."* The aim now is *"to get it into where it's actually going to be used, obviously not just chuck it over the fence."*

**The Knowledge Hub is further along than the Console.** It is not launched, but *"it's got a production site that's already up"*, and Stackworkz have their own test environment. Authentication there is simpler because it works against the sandbox.

## Stackworkz reviewed Novosapien's code, and it passed

Michael had sent Novosapien's libraries over that morning. George asked directly whether anything had alarmed them.

Ruan: ***"It's actually very cool.*** So we actually, we got it running with a local model. I actually got running on my machine with a local model that I downloaded from Ollama... and I got the thing working. So it's pretty cool. So I don't foresee any problems there."

- **No issues with the AGUI front-end code**, the part that will live in the Console.
- **One reservation**, named up front: *"maybe one or two concerns about how authentication authorization will work, especially for the agent."* That became the second half of the call.
- They had **not seen the Knowledge Hub plan**, which is why Hasan demonstrated.

> The local model Ruan named is transcribed as *"Quin 3.8"*, most likely Qwen 3 8B. Worth confirming rather than recording as fact.

## #110 is answered: the llms.txt is a router, not a monolith

The contradiction logged yesterday turns out to be a misunderstanding of which artefact was meant, and George resolved it unprompted while answering Michael's email.

**What was dropped in September** was the monolith. **What is being built** is an entry point:

> *"One approach a lot of people take is just one massive file. It could be some are a couple of thousand lines, others 10,000 lines. So we were thinking maybe taking a slightly different approach where there'll be an llms.txt, which will be that entry point, which acts as kind of like a router. So the user will go in, they'll download that. Their agent will read it. It will have some high-level information about everything, all of the different pages, but more importantly, it would contain links to other pages for it to consume."*

So the agent reads the router, then fetches only the pages it needs on their own routes. **The September objection does not apply**, because the context never holds the whole corpus.

**What Stackworkz have to build is small.** George: *"all it would be is the ability to serve those pages. It's just literally normal text files, does not need to be rendered in any nice way. That's just the standard approach doing it because users are never reading it, it's always their agents."*

## The docs MCP server needs no authentication, and can be built independently

**Ruan's observation, which cuts Stackworkz out of the dependency:** if the endpoint schema comes from DT, then *"the MCP server for the Knowledge Hub can also be implemented independently of us because the upstream information sources is public anyway."*

**George's position on gating it:** no authentication, *"unless, Mike, you say there needs to be, because they're not accessing private data. It's data that they can access if they read the Knowledge Hub themselves."* **Michael did not answer on the call.** New row [[open-questions]] #113.

**The whole deliverable is one page.** George: a guide on connecting *"if you're connecting via cURL, Claude Code, Codex, how you do that, and then it's just a URL... I think it's one extra page that needs to be served."*

**And the copy-to-AI buttons are nearly free.** The feature Michael wanted after seeing them elsewhere: *"all it would be is we just add an extra query into the string, which points to the page that's got that content."*

## #107 gets a real proposal: route the agent through Control Center

Both sides described the same intent and disagreed about the plumbing.

**George's design, as built.** Whatever access the user has is passed down to the agent, so *"the agent is only ever going to see tools that allow actions that the user would have been able to take in the console."* His worked example:

| Case | Behaviour |
|---|---|
| User can suspend a card | Agent **asks that user for approval** on sensitive actions, then executes |
| User cannot suspend a card | Agent **sends a request to a user who can**: *"this user is wanting to do this, do you authorize this action?"* It does not take the action |
| Action needs a second approver anyway | *"the agent's going to handle that as well"* |

His principle: *"it's not as if users are going to be getting a different experience in the AI or full agentic experience in comparison to the console."*

**Ruan's counter, which is an architecture argument rather than an objection.**

> *"Most of that workflow and the approval workflow we're already building in the console. So a possible solution is for the agent not to call the TXN API directly, but go through the control center, which means what you'll get out of the box is all the approvals already and permissions and everything, because that's not simple. It's not trivial for the agent to know which user it is, what permissions they have. That's not just available. That lives in the control center. So if the agent lives separately to that, doesn't have access to all that, doesn't have that context. So that's a problem. But it's not a problem we can't solve."*

**And the cost of not doing it:** *"if we don't address that, you're going to duplicate a lot of the logic that we already built within the control center."*

**Where it landed.** George accepted the logic without conceding the mechanism: *"maybe we might not be consuming the same services, but we'll be consuming the same logic. Maybe we're replicating it on our side, but as long as the logic's the same, perfect."* A **breakout session** was agreed, realistically **early next week**, with Stackworkz sharing what they have built first.

**Michael's priority, stated plainly:** *"the main one being obviously the approval queue. I think Knowledge Hub is quite straightforward... the bigger one is going to be the authentication, the permissions... That's the main point for me that we just need to dig into."* Stackworkz then scope the work.

**A useful verdict on the architecture document** Michael had sent them: Ruan, having gone through it that day, *"I think it's like 80% fine. Maybe with a small tweak here and there, it will work fine."*

## The content pipeline, confirmed and one thread left open

George confirmed the design already recorded on 1 October, and added that both parties draw on the same source.

> *"Rather than it querying an API every single time it wants a piece of information, we will build a local file system representation for the agent based on the content, so that we can get links between the different pages so that the agent can easily traverse and use the tools that they've been trained to use really, really well. And then we'll have a webhook set up. So when a piece of content's been published or unpublished, it's going to refetch it, rebuild it, serve that to the agent."*

- **Source is Umbraco**, and *"we'll be consuming it from the same source as you guys."*
- **Local is cloud-hosted**, *"I say local in quotations because it's going to be in the cloud."*
- The agent greps it and runs **a tightly restricted command set**, *"not any bash commands, very, very limited."*
- **Freshness is event-driven**, not scheduled: *"it's not as if we're doing a cron job once a day or once a week."*

**The open thread.** Ruan asked whether Novosapien use **the delivery API Stackworkz provided**, serving the same content the Knowledge Hub renders. Hasan: at the moment it is all in a sandbox and *"it's not implementing any of that yet."* Nobody decided whether it should. New row [[open-questions]] #112.

## The demo, including a failure that was useful

Hasan showed the build from the day before, against Novosapien's own sandbox.

- Navigation, example payloads with headers, copy and paste, and the Try It panel driving the execution.
- **The approval step**, with the request shown before it is sent.
- **A test that failed**, and explained itself: the cardholder ID was still a placeholder. Hasan: *"it'll be really handy if you want to do any sort of like debugging as well."* **A failure path that teaches is worth more here than a clean demo**, given Ian's standing requirement that sandbox error diagnosis should not need a human.
- **Chat export as a handover document** for another AI, carrying the summary, the sources and the transcript, including the failed test so work can continue elsewhere.
- **Cold start latency** was visible, and someone noted *"we need to turn the thinking level down on this."*

**Chat history, with the reasoning given for the first time.** Unsigned-in history sits in the browser cache and clears at 30 days, as recorded on 8 October. The new part is why: adding an authentication layer *"on top of what's already there for people who are not paying customers at the moment is obviously a big piece of work"*, so it stays out to keep complexity down, *"because obviously at the moment, we just need to move fast."* Storing history properly arrives with sign-in, *"it's up to each of the users."*

**One risk Novosapien raised against itself:** the co-pilot in the sidebar *"might mess with some of the components that are already on there"*, though the expectation is that it will not be serious.

## Findings and where they landed

| Finding | Destination | Action |
|---|---|---|
| **Novosapien implements in Stackworkz's codebase, Stackworkz review** | [[portal-co-pilot]], [[delivery]] | Ways of working recorded |
| Stackworkz to name coding standards, Novosapien to follow | [[delivery]] | Recorded |
| **Stackworkz ran Novosapien's code locally and found no issues** | [[portal-co-pilot]] | Recorded |
| **The llms.txt is a router with links, not a 10,000 line file** | [[docs-mcp-server]], [[open-questions]] | **#110 answered** |
| **Docs MCP server needs no authentication**, Michael has not confirmed | [[docs-mcp-server]], [[open-questions]] | New row **#113** |
| **Docs MCP server can be built independently of Stackworkz** | [[docs-mcp-server]] | Recorded |
| **Stackworkz propose the agent routes through Control Center** rather than the Core API | [[approval-queue-integration]], [[architecture]], [[open-questions]] | **#107 extended**, breakout booked |
| The duplication argument: otherwise Novosapien rebuilds Console logic | [[approval-queue-integration]] | Recorded |
| **George's permission pass-down design**, with the suspend-card cases | [[approval-queue-integration]] | Recorded |
| **Architecture document judged about 80% fine** by Stackworkz | [[architecture]] | Recorded |
| **Umbraco is the shared source**, webhook-driven, cloud-hosted representation | [[docs-mcp-server]] | Confirms 01-10 |
| **The Stackworkz delivery API is not being used**, and nobody decided whether to | [[open-questions]] | New row **#112** |
| Copy-to-AI buttons are a query string change | [[portal-co-pilot]] | Recorded |
| **A failed test explained itself**, useful for debugging | [[portal-co-pilot]] | Recorded |
| Browser-cache history is a complexity decision, not a privacy one | [[portal-co-pilot]] | Reasoning recorded |
| Co-pilot sidebar may clash with existing Knowledge Hub components | [[portal-co-pilot]] | Risk noted |

### Context, no action

| Finding | Note |
|---|---|
| Ian absent, travelling | Second TXN meeting running without him this week |
| The replica was always a stopgap | Michael: *"it's not perfect; it's just a base"* |
| Knowledge Hub has a live production site | Not launched, but deployed |
| Cold start latency on the demo | Plus a note to turn the thinking level down |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Send Novosapien usernames for codebase access | George | Promised straight after the call |
| Grant access to the Knowledge Hub codebase | Stackworkz | Then show Novosapien how to run it locally |
| Name any coding standards to follow | Stackworkz | George asked for them explicitly |
| Share Control Center information, codebases and documentation | Michael and Stackworkz | Ahead of the breakout |
| Share what Stackworkz have built for permissions and approvals | Ruan | So Novosapien arrive informed |
| Book the breakout on authentication and approvals | All three | Realistically early next week |
| Decide whether the docs MCP server needs authentication | Michael | George's position is that it does not |
| Decide whether to consume the Stackworkz delivery API | Novosapien and Stackworkz | Raised by Ruan, not resolved |

---

## Transcript

Meeting Title: Alignment call: TX <> SW <>Novosapien
Date: Oct 14
Meeting participants: Brett StClair, Hasan Ahmed, George Westbrook, Ruan Sunkel, Michael Moores, Armand Pretorius, Lily StClair, Dörte Dye, Ian Johnson

Transcript:
Me: Big orange sausage. You love a bit of orange sausage, don't you, Missa? I can't find your name. Can I just pick any of these? For now.
Them: Oh, my camera is working again. How nice.
Me: Yeah. I mean, it's hard work for me.
Them: Oh my goodness. Hello.
Me: Hello guys.
Them: Hello. Hello, hello.
Me: Hello, hello. How's everybody going?
Them: Good.
Me: I see the weather in South Africa is phenomenal, or By the looks of it, Cornel, is that— yeah, yeah.
Them: Always. Always is. Yeah. It's a little bit too hot.
Me: Are we there? Our weather is perfect. It's a nice cool 17 degrees. Oh yeah. Summer still. Who are we waiting for? George, why is he not in? I saw him wander off to his little room.
Them: He's joined, just joined.
Me: Where we like to, where we like to keep George locked away in a little compartment.
Them: Hello. Can you all hear me?
Me: We can hear you. We can't— I can't see you. This is just me.
Them: I can see him. Yes. Oh no, it's typical. Every time I've got a meeting, everybody else has got one. So I've been walking around trying to find a meeting room. It's like, nope, that one's taken, taken, taken, taken.
Me: Ah, there you are. Dörte, you sound like you don't believe George, or you look.
Them: I mean, I don't believe you, but that's another story, right? I'm looking why my Quantum is not in it. Like, oh, I don't care, just something doesn't work today on my PC. It's just small things.
Me: Yeah. Can we record this meeting? Is that possible? Who's the meeting owner on this?
Them: That's me.
Me: Is it you? Can we record this meeting, Dörte?
Them: I think. You can try, or do you want me to press the button?
Me: Mine, mine says you've got no access to any of that stuff.
Them: See, how cool is that?
Me: That says stay away, Brett.
Them: Okay.
Me: Cool. Oh, oh, has it started recording? Oh, okay, nice.
Them: There you go. Stop recording. Start recording.
Me: There we go, look at that.
Them: There we go.
Me: Awesome. So, um, Shall I start? Is everyone here? Shall we kick off?
Them: Yes, I think Ian will not be able to make it. He's traveling.
Me: Yeah, yeah. So I guess the purpose of this call, uh, get the 2 teams to sync over the dev portal. How do we get the Copilot linked up to you guys, right? Mike, I don't know if you're trying to speak, but you don't seem to be coming through. Your thing's flashing. I don't know if you're trying to. Oh no, mute.
Them: So it's working now. Sorry.
Me: Oh, okay, now it's working. Yeah, yeah, yeah, we got you.
Them: Can you hear me okay?
Me: And so it's just to figure out how we're going to work together. Um, I think you guys have, uh, the code that we've been working on, on the Agentic AI layer. Um, so you can kind of see how we operate and work. And today it's really to kind of go through what we've built, how do we get it into the dev— is it called the dev portal now, hey? Or have I got the word wrong?
Them: Not a chop.
Me: Sorry?
Them: Knowledge Hub.
Me: Knowledge Hub. Sorry, my apologies. Get the Copilot working on the Knowledge Hub, figure out ways of working, your coding standards, how do we work together to get it all done. Agree on a way forward and then go from there. Mike, are you happy with that?
Them: Yeah, sounds good. I think obviously we've sent across your sort of libraries and stuff to StatWorks today, so they've worked on that as well, so we can dig into that. But I think, yeah, that'd be great from StatWorks' side and just show what you've been doing as well from this authentication user side. Just align on that, and then if we need any follow-up sessions on those specific topics. To align, I'll do, Cornelia, I saw your email before, we'll discuss that as well. But I think just aligning, obviously, because it will need to connect into this, the AI piece into the console at some point. So just align on that before we go ahead, basically. The thing is worth saying, like with the, with call it that replica we built, it was a Kind of quickish thing that we we were using to kind of get going, get ahead. So it's not it's not perfect; it's just a base that we've been we've been using. But I think for us now it's getting to the point where. We want to get it into where it's actually going to be used, obviously not just chuck it over the fence. And I suppose it's just working out from your guys' perspective what looks ideal from our guys' perspective, how we'd like to work, because we appreciate you guys. You've— we're focusing on the AI side and you've got so many other stuff to be focusing on. So what is, what is that best route forward so we're not stepping on your toes and vice versa?
Me: Good point.
Them: I think
Me: One of the things
Them: One of the things for us is the first port of call would be that Docs Copilot or the— I'm not sure if you guys have seen it, but it's basically just allowing a user Ask questions similar to that Marketo one that you mentioned, Mike, where it's going to guide people through the docs, they can ask questions, they can test API calls, they can navigate to different pages. So I think that'd be the thing for us that we'd be really, really keen on getting into that live environment as quick as possible obviously first getting it into the codebase, I think first of all it'd be we kind of paint our ideal picture. And see if that's something that you guys would be able to fit into, if that works for you. So obviously you guys have got the codebase that you're working on. Was there any quick question as well from that codebase that we sent over to you? Was there anything where you were going, What the fuck are these guys doing? Are they absolutely mental? Was there anything there that kind of worried you? George, no, it was, it's actually very cool. So we actually, we got it running with a local model. I actually got running on my machine with a local Model that I downloaded from Ollama. I think it was Quin 3.8 and I got the thing working. So it's pretty cool. So I don't foresee any problems there. With regards to the bigger architecture, maybe one or two concerns about how authentication authorization will work, especially for the agent when, but that Mike, I think we'll get to at some point. But other than that, From a control center perspective, At least from the, let's say, the AGUI side. So the code that will live in the front and no issues from it. Yeah. It looks good so far. We haven't seen what's planned for the Knowledge Hub yet. Yep. Because I think so with the knowledge hubs on.
Me: That's what I can do.
Them: Hasan, is it worth you just pull it up? Rather than trying to explain it, I think it'd just be easier.
Me: Do a quick demo.
Them: It's going, it's going to do this, it's going to do that, and then you just see it. I know that's bringing it on you at the last second. So 2 minutes of small talk. How's the weather over there, guys? Is it amazing? Oh, it's shit here in the UK. Okay. That's too hot for my liking. Okay. I should be sharing. So yeah. Can everyone see my screen?
Me: Yep.
Them: Yes. Okay. So, um, Here is our like a sort of like agentic experience we've like added into the Um, actually, like, As I enter here, basically, I mean, it's just going to be like a sort of, I mean, at the moment it's just sort of like a basic implementation. Here, if you're not asking any sort of other questions or if you want to do any sort of like API testing, like let's say for example, how do I issue a card?
Me: Any questions?
Them: As in, like, it wouldn't go through the entire docs. It wouldn't get the individual resources. If we give it a second. I think one thing that's important to say is where it's getting this knowledge from is from Umbraco. So effectively all it's doing is It's going to speaking to Embraco, it's building a, let's call it local representation. I say local in quotations because it's going to be in the cloud. But from the agent's perspective, it can grep through it, it can execute bash commands to do that. Not any bash commands, very, very limited. That sits on our backend any content that's served on the console is going to be the content that the agent has access to. It's not as if we're doing a cron job once a day or once a week to update the content. As soon as that content is updated, it's updated for the agent. Are you making use of the delivery API that we provided in the same, basically the same content that's rendered in the knowledge hub? I mean, at the moment, this is all in like a sort of Latin sandbox. And so it's not implementing any of that yet. And so then here, like, it just has the headers and then like the exact payload. You can ask it a question like, can you show me an example payload?
Me: Other headers? Yeah, and then I'm letting you ask him.
Them: Yeah. And then, um, like if you ask like any sort of question, it will also take you to that page as well. And so then if you want to read through it on your own, so you want to see like each of the individual fields, you want to see the headers. It's all here as well if you want to, I mean, if you want to read it or if you want to speak to the agent and then if you want to get like an example, like for the individual payload, you can just do a quick copy paste.
Me: I'll pull it in. Let me just do a quick test. And then add it into your
Them: And then add it into your And include, for example, into your own Nothing Sort session. There's also, if you want to try it, so we can say, can you run a test payload? In the sandbox. Yeah. Yeah. And then it will draft like a sort of, like example, the payload, it will give you the input, the that output as well.
Me: The output as well.
Them: Um,
Me: And then I always have everything here.
Them: And then like how it's also doing it is through the actual Try It panel. And so like it's just going to pull in all of that information. It will think it's— I'll show you exactly things. Oh, what, like it's going to send as well? And so that if you want to skim through it, see if it all looks good, if you want to approve it, or if you want to say no, you aren't really happy with it, but I'm just going to approve it here.
Me: Of what, like? What's the difference? In our preview.
Them: And then it will do the entire test for you and then it will give you the exact output as well. And so then if you want to just see and
Me: Try us visit.
Them: To try out specific things. I think we need to turn the thinking level down on this. Yeah, I mean, I think it's starting from like a cold start. So yeah, no, because at the moment it's on a cold start, so it needs to load up. But I mean, here's an example. Basically, it will show you the Request and then the actual output as well.
Me: Request.
Them: And then because here like it failed and then, and then if like it does fail, you like obviously see why it says, oh, like it has not the cardholder ID with this placeholder. And so then it'll be really handy if you want to do any sort of like debugging as well. So if you want to try out specific IDs and just as in, let's see if it works, have a play around.
Me: So try it.
Them: We also have the actual option if you want to export the entire chat as well. I believe we spoke about integrating with Claude and any sort of LLMs. Having GPT or At the cursor, we just added in like a way if you want to then download the entire chat as well.
Me: I also have Casa. I'm able to
Them: And then if we give it a second, I Open that up. So as in, like, it will just give you an example. Of like the like entire chat history and then it will give you like a sort of guide for like anything LLM who is also going to be reading this. And so then it's going to say as a handover, like it said, the conversation with the like AI assistant. And so then like it would do like a brief sort of summary, like, I mean, everything like established here. And so then like it says here that we did an API test, it also failed. So then if you want to then continue on, do like Any sort of like further testing?
Me: AI like assistant.
Them: And then it will have the entire thing transcript as well here. Um, And so yeah, um, So I think also as well, there's the chat history as well. Isn't there, Sam? But that's like, I think it might be worth explaining like how that chat history is stored. Obviously there's no authentication on there at the moment, so.
Me: Yeah.
Them: Yeah, and so if you aren't actually signed in, it's just going to store it in like the actual browser cache.
Me: Yeah. Then I'll play a song later.
Them: And then after like a certain amount of time, so here it's for like about like 30 days, it'll just be stored in like your actual cache and then it'll clear as soon as your actual cache is also cleared that's stored anywhere at the moment.
Me: Oh, like it's not anywhere at the moment.
Them: As in, it's not stored. Like I'll say, as in, it's not really stored anywhere long-term.
Me: Like, I'll say, like, it's not cool. So if you watch it inside, like that, I mean, I think you would.
Them: And so then if you write in a sign-in and then as soon as we have that authentication in place, like there, I mean, ideally if we can add an option where you can store the entire chat history, it's up to each of the actual thing users as well. At the moment, it's just stored in the actual browser cache.
Me: I hope to do that. Like as well.
Them: I think part of the reason for doing that is to obviously allow Go there, come back, and not completely forget everything. But also, we know adding a new authentication layer on top of What's already there for people who are not paying customers at the moment is obviously a big piece of work. So there's some sort there at the moment, so it's keeping the complexity down, but obviously there's scope to improve. But also, we know adding a new authentication layer on top of what's already there for people who are not paying customers at the moment is obviously a big piece of work. So there's some sort there at the moment, so it's keeping the complexity down, but obviously there's scope to improve that in the future. Because obviously at the moment, we just need to move fast, we need to get it built, we need to get it implemented. So by going, can we add authentication onto this new part for like a completely different way of doing it, might be a little bit of an overstep. I think it's, I suppose, I think it was just important to show like this is what we're thinking. I feel like one of the only maybe minor issues is obviously now there's a Copilot on the sidebar, so It might mess with some of the components that are already on there, but I'll say I'm assuming that might not be as big of an issue as I initially might have thought. I think now we've— well, first of all, is there any questions on anything that you've seen, anything that's worrying or anything where you need a bit more clarity on? Well, I think from our side it looks amazing. I'm like trying to think 2 steps ahead. So I think the knowledge I have at this point is already It's not launched officially, but it's already, it's got a production site that's already up. We have our own environment that we do tests on. So I was thinking, I think it would be best If we give you access to the codebase and you make your changes. The actual system as it is deployed. And then we can see, okay, what are the real problems if they are? With the Knowledge Hub, I don't see any issues because authentication to the DXN API is simpler because we're working with the sandbox. So that's not an issue. And then, yeah, if you have the codebase, we'll be able to see if The, the Copilot will be an issue. I don't think it will be. I think it will be fine. But yeah, what does that sound like if you get access to our codebase?
Me: Yeah. Yeah.
Them: Perfect. We can even show you how to run it locally. Yeah, yeah, I think For us, that's the ideal situation as well. Like I said, you guys have got like loads on your plate, so the last thing you need is getting access to a random codebase which is kind of similar, then you're spending time trying to get— it's difficult enough. So I think I can imagine for both us and you guys, if we can get that access, we can make the changes. You guys review it, make sure that we're not stepping on your toes. If there's any coding standards that you want us to abide by. Let us know, and then we'll make sure that we fit into the way that you guys, you guys have done stuff. So yeah, I think, like I said, we get access, we'll obviously test it locally, push it to whatever branches that you need for it to be deployed onto the testing environments, and then go from there to get it into production. Other test environments as quick as possible. Okay, and then I've got 2 questions. Does it make use of the same agent backend that the control center will use? Was it a different one? Okay. Yeah. So it would all be that AGUI. Okay, and the information that it has access to with regards to guide content and the API reference, where at the moment, where, how did you, how do you get the information? Well, how does the agent get that information?
Correct me if I'm wrong on any of this, Hissam, but this might kindly send access to Umbraco. So effectively what we do, we found with agents, rather than it querying an API every single time it wants a piece of information, effectively what we do is we will build a local file system, local file system. representation for the agent based on the content so that we can kind of get like links between the different pages so that the agent can easily traverse and use the tools that they've been trained to use really, really well. And then every time there's— so we'll have a webhook set up. So when it's pub— a piece of content's been published or unpublished, it's going to refetch it, rebuild it, serve that to the agent. So the content's always staying fresh. Anything that's published gets added in, anything that's unpublished gets taken out. So we'll be consuming it from the same source as you guys. Okay, I think once— That's perfect. One thing that I've I think it was in your email yesterday, Mike, before, like, while it's top of mind, is the kind of llms.txt. So I think what one approach a lot of people take is just one massive file. It could be some are a couple of thousand lines, others 10,000 lines. So we were thinking maybe taking a slightly different approach where there'll be an llms.txt, which will be that entry point, which acts as kind of like a router. So the user will go in, they'll download that. Their agent will read it. It will have some high-level information about everything, all of the different pages, but more importantly, it would contain links to other pages for it to consume. So let's say there's one specific endpoint or group of endpoints that they're focusing on. They'll go into the llms.txt, the agent will read that, it'll be the links to the other pages which will be served on Dodo. On other routes, then it will just do another query to get that page, another query. So I think it's just, all it would be is the ability to serve those pages. It's just literally normal text files, does not need to be rendered in any nice way. That's just the standard approach doing it because users are never reading it, it's always their agents. And I think the only other one would be the MCP server. So I mean, there's a few different MCP servers in the architecture, but I think the main one will be the kind of docs MCP server, which will be similar to how we do it with the agent, where it's building that local representation for them, but effectively all we do is we mimic bash calls or a command line, severely limited, so all the agent can do is write commands that we say it can. Then it's going to execute it, serve the content back, but there doesn't need to be any sort of authentication for that unless, Mike, you say there needs to be because they're not accessing private data. It's data that they can access if they read the Knowledge Hub themselves. It's data they can access if they look at the llms.txt. It's just served on the MCP server. So all that would really be needed is just kind of A guide on how to implement it. So I think a lot of, a lot of places I do, if you're connecting via cURL, Claude Code, Codex, how you do that, and then it's just a URL. So it's not, I think it's one extra page that needs to be served. So that should be relatively simple. The last thing would be that And you, the thing that you said, Mike, that copy, that copy thing that they have on the top of the pages where it's like copy to Perplexity, copy to ChatGPT. Once again, that's relatively simple. I think all it would be is we just add an extra query into the string, which points to the page that's got that content. And yeah, then they should be good to go. Yeah, sounds good to me. Thank you. I feel like that's everything for the Knowledge Hub. Which I think if you're happy, we're happy with the route going forward. We'll get the access, we'll add the code in, you guys review, we go through that process with the console with a similar approach. work for you guys as well? Obviously, I appreciate the console's not at the same point which the Knowledge Hub is, but is that same ways of working good with you guys as well? Yes, I think that's what we'll do. Not, not just yet, but hopefully rather than later. Yeah, this is something, yeah, this, There's a possible authentication issue that, yeah, like we're trying to work through. But yeah, in the end it will work the same. Yeah, we'll give you access to the code and you can implement. What you need to implement. Sorry, just a quick question on the Knowledge Hub. Just the last question, the information regarding the API and the endpoints that are available, where do you get that? Do you call the DT endpoint to get the schema or? Yeah. I just saw your head bobbing, Hasan, so. Yeah, I think there was one. I'm off thinking what it was. Yeah, the reason I'm asking is if that's the case, then the MCP server for the Knowledge Hub can also be implemented independently of us because the information sources, the upstream information sources is public anyway. So Control Center works differently. That's what I was saying. In terms of authentication as well, all we're going to do is— what we'll be doing is passing down whatever credentials the user has to the agent. So with the MCP server, this is, this is for the console. So the MCP server for that, in theory, can do everything and anything. But obviously we know we don't want to— we don't want a user who's got a certain access level to be able to take actions with an agent that they wouldn't necessarily be able to make if they were in the console. So all we're going to be doing is whatever access that user's got is going to be passed down to the agent. Really straight direct to the MCP server. The agent is only ever going to see tools that allow actions that the user would have been able to take in the console. So say, for example, Suspend a card. Random example, user 1 can't suspend a card. User 2 can suspend a card. User 2 is going to always ask for approval from the user for sensitive actions. So ask for approval, then the agent will execute. For user 1, what it will do is it will take a different approach where it would send a request to user 2. And say, this user is wanting to do this, do you authorize this action? Or there's going to be some approval layer. So it's not going to actually take the action, it's going to request it from somebody else. And obviously in situations where Even if the user's got the access level and there needs to be a second one as well, the agent's going to handle that as well. So it's not as if we're going to be passing anything and users are going to be getting a different experience in the AI or full agentic experience in comparison to the console. Okay. Yeah, yeah, there I think we need to just talk about that workflow because most of that workflow and the approval workflow we're already building in the console. So one possible Way to get around the issues that I'm trying to surface is the A possible solution is for the agent not to call the TXN API directly, but go through the control center, which means what you'll get out of the box is all the approvals already and permissions and everything, because that's not simple. It's not trivial. For the agent to know based on, to know which user it is, what permissions they have. Yeah, that's not just available. That lives in the control center. So if the agent Lives separately to that, doesn't have access to all that, doesn't have that context. So that's a problem. But it's not a problem we can't solve. Yeah, so the Yeah, we were thinking of having some breakout session that we can go deeper into that. But yeah, we saw, we saw the architecture document that Mike sent us and, and I think it's like 80%. Fine. Maybe with a small tweak here and there, it will, it will work fine. Yeah. And if we, if we don't address that, you're going to duplicate a lot of the logic that we already built. Within the control center. Yeah, so that's good. So it's a, yeah, we all went through it. We went through it today, so it's all fresh. Okay. Yeah, it's up for discussion. Yeah. I think it's one of, if you, if, if, if you're happy to share what you've got. at the moment when it comes to that, then we can, we can have a look. Then when it comes to that discussion, we'll be, we'll be way more informed because like you said, if maybe we might not be consuming the same services. But we'll be consuming the same logic. Maybe we're replicating it on our side, but as long as the logic's the same, perfect. Okay. Is there, is there anything else, Mike, that you've got top of mind that you want to talk about? No, I don't think so. Yeah, the main one being obviously the approval queue. I think Knowledge Hub is quite straightforward, but it seems, and then I think the bigger one is going to be the authentication, the permissions, obviously the stuff that's that we're building specifically on top of the TXN API. That's the main point for me that we just need to dig into and see what the solutions are for that. And obviously Stackworks team can then scope the work for the stuff to implement that as well. So that'll be great. Perfect. So I suppose Next steps, if you'd be able to give us. Access to what you think we need, we'll get busy working away. And like any issues with anything we've done, let us know straight away because then the quicker we know, quicker we can fix it. Any standards you want us to abide by, Let us know and we're happy to do that. And then I suppose it's setting up a— sending over the information about the control center, any code bases you think we might need to access, any documentation, and then let's get that, then let's get that That's booked in so we can have that discussion either— realistically, it's probably going to be early next week. And then, yeah, anything else I forgot? That's it from my side. Thank you. Yeah, I think that's everyone. But yeah, I think, yeah, we'll share all that information and then obviously set up another call to go on the specific topics. If, Ruan, you can have a look at, you know, the stuff from your side, just show what you've got. I think that's the bit that we've been missing up to now. We just see how we— how it looks like we can integrate to the console. And obviously, Kuneel will discuss further. On next steps from your side as well. Yeah, all good. Thanks, Mike. Thanks, George, Hasan. Thank you. Sorry, George, with regards to access to the codebase, who do we give access to? I'll send you after this call the usernames. Okay, cool. Thanks very much, everyone. Cheers.
Me: Perfect. Thank you, everybody. Cheers.
