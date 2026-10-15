---
date: 2026-10-15
type: standup
description: "Ian's first look: on the right track but too API-heavy, the guides journey is missing, and an internal stakeholder demo becomes the gating milestone"
scope:
  - "[[developer-support]]"
  - "[[commercial]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[portal-co-pilot]]"
  - "[[docs-mcp-server]]"
  - "[[developer-support]]"
  - "[[commercial]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-15)

> **Source:** Gemini transcript, 15 October 2026, 14:31 BST, 51m. **Novosapien:** Brett StClair, George Westbrook, Hasan Ahmed. **TXN:** Ian Johnson, Michael Moores. Ian back from Lisbon and Bulgaria, *"pretty exhausting to be honest."*
>
> **Ian's first sight of the co-pilot.** He has been travelling through every demo since it was built.

## Ian's verdict, stated accurately

**Two things happened, and they should not be collapsed into one.**

**The demo ran badly.** Ian: *"it's been very difficult to follow it because I don't think it's been the sickest demo in the world and I haven't been able to read the text for half of it. Um, which is not obviously not ideal."* The screen was fuzzy, the text unreadable, and the cold start made every answer slow.

**The product is on track.** Ian corrected himself, unprompted: *"by the way, I always dive straight into the challenges rather than the good stuff. **So, it's great. It's on the right track of the things that we were thinking about.**"*

> So the criticism below is about a gap in coverage and journey design, not a judgement that the build is wrong. He also noted that Michael *"has seen much of this already and was pretty impressed"*, and that the cold start is *"not a permanent issue"*.

## The real finding: it answers the API reference and skips the guides

This is the substantive gap, and it goes straight at TXN's core claim.

> *"What we just looked at is **very heavy on the API reference**. But the part for me, Mike, is **people who don't even know how to go about starting**. So we dive straight into how do I issue a card? What's the relationship between an account, a card holder, a card, those type of things... the reality with a card program is you have to have some understanding of what the sequence of things is."*

**Even the demo question assumes the knowledge it should be teaching.** Ian: *"how do I create a card, that question assumes that the person understands that there needs to be an account and a card holder set up before they get to creating a card, which they may not have."*

**Why it matters commercially, in his words:**

> *"It's such a key part of our messaging, as you know, Brett, about **not needing to be a card expert to be able to launch a card program**. So we need to be able to show that that's the case."*

**And his working assumption about the user:** *"most people are lazy and don't want to sit there and read a bunch of docs"*, so the co-pilot has to *"disseminate the key information that's in docs relative to a natural language question"* and get them to a position where they can then use the API reference. New row [[open-questions]] #114.

## Ian names two interaction modes, and one of them is new

**Mode one, the guided walkthrough with confirmation at each step.** This is not in any current specification.

> *"One is explaining step by step and asking them to make a positive approval to move to the next stage. So if it was, for example, first step is create account, and you explain how you create account, and then it says next step create card holder. **Would you like me to explain how to create a card holder?** Yes. And then you get the card holder and then you get to the card piece."*

**The reasoning is about outcome, not interface:** *"the ultimate goal is to make sure they can do it. **Just giving the information and assuming that they've read it and understood it without any kind of feedback doesn't really necessarily work.**"*

**Mode two, the data dump.** *"There might be people who just want the dump of the data because they're just going to go away and stick it in AI and they're going to get that to figure it out for them."*

**Three personas, in his framing:** someone who already runs a card programme and dives into the API reference; someone AI-savvy who takes the MCP server into their own environment; and someone who needs the relationships and the sequence explained first. New row #116.

## An internal stakeholder demo becomes the gating milestone

This is the biggest change of direction on the call, and the reason for it is political rather than technical.

**The chairman is selling something he has never seen.** Ian:

> *"I've spent multiple meetings these last two days with **Steve the chairman** where he's talking about the fact that we've got this amazing platform, and I'm thinking you're going totally on what we've told you, because **you have not seen it**... he absolutely does not know it to be true."*

**And the demo is a lever on Direct Transact.** *"We don't want any blockers with actually getting the stuff set up. So we need to see the thing in action, understand how important it is to our user experience."* His reasoning from experience: *"if they're brought to something completely cold... it's just going to be more challenging. So if you can take people with you and they're like, yeah, this is great, what can we do to get this up and running, then it's going to be a lot easier."*

| Element | Position |
|---|---|
| **Audience** | **Steve**, chairman, who *"won't know one end of an API from the other"*. **Gavin**, CTO at PayCorp. Possibly **Anthony** and others at DT |
| **Scope** | **Knowledge Hub only**, not the Console. Ian: *"that's the first thing that will hit the market"* |
| **Environment** | **Novosapien's own demo environment**, not the real hub |
| **Format** | **Live**, with a recorded walkthrough as backup |
| **Date** | **None set.** Ian deliberately did not press: *"I'm not going to push you guys for an answer right now"* |

**The two objectives he set:** that stakeholders leave understanding *"why we're saying that you don't need to be a card expert to launch a program with us"*, and that the platform will *"meet you wherever you are"*, whether that means reading the hub or taking the content into Claude.

**The tension he named himself:** *"the longer it is to wait to get the demo set up, the further we've pushed before we can actually push on them to get the stuff."* Against that: *"the most important thing is the quality, the speed, and the completeness of the experience that we're showing."* New row #115.

### The demo runs on Novosapien's environment, deliberately

Ian accepted it: *"we're not going to be ready in time to have everything knitted into the actual knowledge hub to do the demo from there."*

George's proposal: keep the demo environment, which *"looks, feels, acts exactly like the real thing"*, make sure *"we've got enough mock data so that it looks and acts like the real thing"*, and build the real integration in parallel. That is the demonstrability requirement at #90 being met by a parallel environment rather than by seeded production data.

### Live, with a recorded backup, and Brett overruled the alternative

Ian suggested a recorded walkthrough: *"working with kids, animals, live demos, all things that you probably shouldn't do."* George asked whether that replaced the live demo. **Brett: *"No, that's a backup. We need to be ultra prepped for a live demo."*** Then: test everything, script it, *"pre-run every single scenario"*, record it, and fall back to the video if the connection fails, *"the connection to South Africa can be temperamental."*

**Ian's standard for readiness is not a clean rehearsal.** *"It doesn't matter if on Monday we did a live demo and everything went swimmingly... It doesn't ring true that when we actually did the one on Friday the same would be true. So I'm not really interested in that bit. It's the functionality and hitting those different personas and a varying level of complexity in query."*

**What he actually wants to survive:** *"somebody says, well, ask it this. That's the thing that I would be doing... you've gone through all of these things and then somebody goes in and asks a question and it just brain farts everywhere. Which is going to happen."* And the reason it frightens him: ***"some people won't necessarily know that what they've just had back isn't accurate."*** That is #89 restated by the person who found it.

## Cold start is the immediate blocker, and the fix already exists

George: *"there'll be some of the same issues we did have before in terms of speed. We just need to apply them to this... **that's a solved issue. You just need to propagate it to this.**"*

Hasan, on demoing: *"we need to turn off the cold starting so then it's a lot quicker."* Ian, bluntly: ***"if the cold start is active, it won't go well."*** George's commitment: *"get those speed issues sorted. We'll set up a small environment that's always on."*

Then the sequence he proposed: everyone plays with it, early issues get caught, and only then *"plan out how we're going to do the demo. We're going to position it at this user, we're going to achieve these three or four outcomes."*

## George proposes an evaluation harness, which is new scope

Ian asked the right question: the demo prompts are easy ones. *"Show me how to create a card is a relatively simple prompt. What about more complex things that might get asked in the knowledge hub that will undoubtedly happen when we hit the real world?"* He wants *"a list of more challenging prompts to see how it behaves with those."*

**George's answer goes considerably further than a list:**

> *"If we could get an example of as many questions as you can think of, then what we can do is say, given that query, **what is the acceptance criteria for that query being done**... let's say you've got 10, 20, however many, **run them all in parallel, churn them through the agent, do a hundred of each**, look at what the output is **not just from one turn but a whole conversation, rank them, score them, categorize them**, take that information, and initially we'll just see where the gaps are."*

**Why, in his words:** *"we all know from testing it's very good to see it with your own eyes, but **it's not very scalable**."*

**He named the failure mode in both directions.** On a simple query the agent *"has gone and done a 500 word message where all it needed to do was go, here, look at this page, here's this snippet, bam, done."* On complex queries the opposite problem.

**Personas become a test variable:** *"create those different personas. Maybe it's just three to start with, the ultra developer type and the opposite end of that spectrum. Add them in as a variable. Test, test, test."*

**And a future idea he flagged as a rabbit hole himself:** analyse the collected conversations, then either tune towards the complexity that actually arrives, or *"put something in place so that after the first two or three turns of the message, we try and identify what style of communication this user has got and dynamically adapt it."*

**Both sides to brainstorm the query set**, and crucially *"what's a good answer and what's a bad answer."* New row #117. This is the first concrete proposal against the benchmark gap at #87.

## The documentation state, and a job nobody has scoped

**Forty guides are published**, at version one. Michael: *"it's 40 in there already, as best as they can be."*

**All of them handwritten, because Umbraco gives him no choice.** *"They're all handwritten because that's what Umbraco requires. So, no AI, unfortunately."* The cost: *"I went through all 40, took about 30 minutes each"*, roughly twenty hours, because *"every title's got to be its own component and every table's got to be. You can't just copy anything in. You've got to create a component for a title, create a table, add every single row and column."* Updating afterwards is easy: *"once it's in, you can just add extra text to the text box. It's a structure more than anything."*

**They deliberately omit payloads**, *"on purpose"*, which is the two-layer design the co-pilot exists to rejoin.

**Ian asked the obvious question: why can't AI do it?** Michael: *"I just need to have a look at the API. I guess there's no direct MCP. So we'd have to build something with Stackworkz or something to integrate that. **It's just not been built yet.**"* Nobody scoped it. New row #118.

**Michael has not tested the co-pilot against the guides** and agreed to: *"I can do that testing specifically on the guides and make sure it's there."* He also described two existing routines worth knowing about: a daily check of the docs against their own vault, *"a personal routine that I've got"*, and a Freshdesk check that incoming questions can be answered by the docs.

**Ian's docs feedback loop, restated.** *"If there's a question that's asked that the docs don't answer, or the docs are ambiguous about, that's the bit that we then need to make sure that we know, so the docs can be updated, so the source is always accurate whether you're looking at the docs or going through the AI."* That is #92, raised again by its author.

## What George added to the demo: the MCP server and the router

George positioned both as ways to bypass the interface entirely.

**The docs MCP server**, taking Umbraco content into the local representation, *"which we can expose to other people so that even if they don't want to use the docs assistant, they can put that MCP server into their own Claude within one or two commands."* On gating, he repeated the position and flagged it as unsettled himself: *"it doesn't need to be authenticated, **what's up for debate**, but doesn't need to be, because all it's doing is accepting the information that's there already."* Still unanswered at #113.

**The llms.txt router, now cleared with Stackworkz.** *"We were speaking to Stackworkz about this yesterday and there wouldn't be an issue."* One router file plus text files on other routes, so *"even if a user hasn't connected the MCP server, they can paste in the handover message and they're going to get the source of truth for that page in a format that's easily digestible for the agent."*

**And a discovery argument for it that had not been made before:** *"if somebody's typing in, hey, I've seen this platform TXN, thinking about it, it's going to be coming up in the search results... So you're capturing people who actively want the MCP, but you're also giving more information to people that might be doing that AI-assisted discovery."* That reframes the router as a marketing surface as well as a developer one, alongside #106.

## Two decisions and one commitment

### Languages: publish in English only, let the AI translate

Prompted by Brett's account of an unplanned Hebrew demo in insurance that worked. Ian:

> *"We're not going to support clients in other languages early. So I don't think there's any point publishing assets, websites, knowledge hubs in a language that you can't support at the end. But with AI, they can take that information that's in English, dump it into Claude, and they can get Claude to do the translation or whatever their desired tool might be. **So it takes a lot of onus off us in having to do all that translation stuff.**"*

### Stackworkz: code access yes, environment not yet

George: *"just a code base for the time being."* A branch has been set up for Novosapien. The preference is to run it in Azure, *"if we could get it into Azure that would be ideal"*, otherwise locally or on Novosapien's own infrastructure. **Brett pushed on it:** *"what are we waiting for on access to the environment... make sure we get it today, tomorrow, ASAP."*

George on yesterday's call: *"they're very happy for us to work on what they've already got... it's unlocked a lot of potential blockers that could have been there."* And honestly on the risk that was avoided: *"it could have gone two ways, where they might have liked a bit more control and said no, we'll write this."* Ian: *"we have selected partners that we believe are collaborative, and Stackworkz have been excellent throughout."*

### Brett owes Ian two documents

- **An updated flight plan**, revised that morning, *"I was just planning some issues in it, ironing that out."*
- **An architecture diagram for the LLMs and data processing**, covering *"how the different models use data, on what licenses, and what all your different options are"*, explicitly *"to help you with your data agreements and regulatory compliance."* Brett admitted the difficulty: *"I started trying to do it and I was struggling."* This is the material behind the sub-processor and model-residency gaps at #80 and #103.

**And a note on the commercial upside.** Ian, lightly but not idly: *"if you do a really good job, it might help me secure more funding to do more AI things."*

## Findings and where they landed

| Finding | Destination | Action |
|---|---|---|
| **Ian: on the right track**, but the demo itself ran badly | [[portal-co-pilot]] | Verdict recorded in full |
| **Too heavy on the API reference, the guides journey is missing** | [[portal-co-pilot]], [[open-questions]] | New row **#114** |
| **Guided walkthrough with step-by-step confirmation**, a new pattern | [[portal-co-pilot]], [[open-questions]] | New row **#116** |
| Three personas: existing programme, AI-savvy, needs the sequence | [[portal-co-pilot]] | Recorded |
| **Internal stakeholder demo becomes the gating milestone**, no date set | [[delivery]], [[commercial]], [[open-questions]] | New row **#115** |
| Audience: Steve the chairman, Gavin at PayCorp, possibly Anthony at DT | [[commercial]] | Recorded |
| **Knowledge Hub only**, not the Console | [[delivery]] | Scope recorded |
| **Demo runs on Novosapien's environment with mock data** | [[portal-co-pilot]], [[open-questions]] | **#90** extended |
| **Live demo, recorded backup**, Brett's call | [[delivery]] | Recorded |
| **Cold start is the blocker and the fix exists but is not applied** | [[portal-co-pilot]] | Recorded, owner Novosapien |
| **Evaluation harness proposed**: acceptance criteria, 100 runs per query, scored | [[open-questions]] | New row **#117**, first answer to #87 |
| **Forty guides published, all handwritten**, 30 minutes each | [[developer-support]] | Recorded |
| **No AI path into Umbraco**, and nobody has scoped one | [[open-questions]] | New row **#118** |
| Michael has not tested the co-pilot against the guides, and will | [[portal-co-pilot]] | Open on Michael |
| **Docs feedback loop restated by Ian** | [[open-questions]] | Recorded at **#92** |
| **Wrong answers nobody can detect**, restated by Ian | [[open-questions]] | Recorded at #89 |
| **The llms.txt router doubles as AI-assisted discovery** | [[docs-mcp-server]] | New argument recorded |
| MCP gating still *"up for debate"* in George's own words | [[open-questions]] | Stands at #113 |
| **English only, let the user's AI translate** | [[commercial]] | Decision recorded |
| **Stackworkz gave code access, not environment access** | [[delivery]] | Recorded, Brett chasing |

### Context, no action

| Finding | Note |
|---|---|
| Ian back from Lisbon and Bulgaria | Four days then two, *"pretty exhausting"* |
| Brett owes an updated flight plan and an LLM licensing diagram | The second feeds Dorte's data agreements |
| Ian hints at more AI funding if the demo lands | *"it might help me secure more funding to do more AI things"* |
| Brett booked a meeting for 12:00 Monday | Diary invitation sent on the call |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Fix the cold start and stand up an always-on environment | Novosapien | Ian: it will not go well otherwise |
| Come back with a demo date | Novosapien | Brett: *"a date that we can be as best prepared for ASAP"* |
| Build the guides journey and the step-by-step walkthrough | Novosapien | The substance of Ian's feedback |
| Draft the challenging prompt list and what a good answer is | Ian and Michael | Novosapien brainstorming in parallel |
| Build the evaluation harness with personas as a variable | Novosapien | George's proposal |
| Test the co-pilot against the 40 published guides | Michael | Agreed on the call |
| Publish the remaining documentation | Michael | *"still a lot to be published"* |
| Chase Stackworkz for environment access, not just code | George, pushed by Brett | *"today, tomorrow, ASAP"* |
| Send Ian the updated flight plan | Brett | Revised that morning |
| Produce the LLM, data and licensing architecture diagram | Brett with George | For Ian's data agreements and compliance |
| Everyone to play with the build and catch early issues | All | Before the demo is planned |

---

## Transcript

Oct 15, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:09**

**Brett StClair:** Hello.

**Ian Johnson:** Hey, how you doing?

**Brett StClair:** Well, in how's your travels been?

**Ian Johnson:** Uh, good. I mean, good meetings and stuff, but it's pretty it's been pretty exhausting to be honest.

**Brett StClair:** Oh, yeah.

**Ian Johnson:** Pretty old.

**Brett StClair:** Whereabouts were whereabouts were you traveling?

**Ian Johnson:** I was in Lisbon last week for four days and then uh Bulgaria on Tuesday and Wednesday. So yeah,

**Brett StClair:** Nice.

**Ian Johnson:** but u pretty productive.

**Brett StClair:** Damn.

**Ian Johnson:** So can't complain. You're all back in the real world now, are you?

**George Westbrook:** Yeah.

**Brett StClair:** No,

**George Westbrook:** All all back in the UK with the uh

**Brett StClair:** just No, no, no. We just changed our backgrounds.

**Ian Johnson:** Yeah. You know nothing.

**George Westbrook:** We decided to stay out there for another 10 months and uh we just created an AI program which simulates the office.

**Ian Johnson:** Thought you had done that by now to be honest.

**Brett StClair:** Yeah, exactly. Um, let um, okay, I think that's everybody. Shall I jump in?

### **00:01:24**

**Ian Johnson:** Thank you.

**Brett StClair:** Um, but I'm going to be sending you just an updated flight plan. I've just updated it this morning and I was just planning some issues in it. Um, ironing that out and I'll get that to you. Um, and I also I need to spend a bit of time with George on that architecture diagram for LLMs and our data processing all work through it and licensing models and get that to package properly. I started trying to do it and I was struggling. Um, so that at least you can clearly see how the different models use data on what licenses and what all your different options are. Um, that should be able to help you with your data agreements and regulatory compliance. Um then and I think maybe we do a walkthrough of what we've built end to end. So the team pushed it through this weekend and have done some further refinements. Um the goal was to get as much as we can done barring getting it deployed onto your environment.

**Ian Johnson:** Yeah.

### **00:02:37**

**Brett StClair:** Um so we'll do that. Mike and a quick update on the stack works guys. Um that went really well. Really pleased with the outcome of that. Um George and team have access to the environment or is it just the code base? George.

**George Westbrook:** uh just a code base for the time being. We'll get we'll get on that after the demo.

**Brett StClair:** Yeah,

**George Westbrook:** Where is this at?

**Brett StClair:** he's behind me.

**George Westbrook:** Are you ready to call?

**Brett StClair:** I'm wondering if Hasanis wearing the wired piece or is he going to risk his demo with wireless?

**Hasan Ahmed:** Um, I think it should be okay. Um,

**George Westbrook:** You're going to smash up your headphones so you can never use them again if it's not.

**Hasan Ahmed:** let me think it should be okay. Hope I'm I'm hoping it's okay. Let me stop demo. Um okay. Um chat

**George Westbrook:** Wait a sec. I think it's bit fuzzy for me. I don't know if it's Yeah.

### **00:03:52**

**Hasan Ahmed:** um zoom in a bit. Yeah. So um um I mean like at the moment I'm a bit unsure how much you've already seen on this. So I'll just start from the um beginning. So I mean essentially it's just a way to explore the the API docs if you want to ask them questions on how to do things, how to integrate, how to then test. Um it's all be pretty much doable. So I'll start off with a question. So how do I issue a card? Um I believe it's on a cold start. So, it might take a second, but

**George Westbrook:** So there'll be on this some of the same issues we did have before in terms of speed. We just need to apply them apply them to this. So, and obviously in terms of there'll be the cold start because obviously you'll notice when it's responding it's taken way too long. Um, but that that's a solved issue. You just need to propagate to this.

**Hasan Ahmed:** Yeah.

### **00:05:22**

**Hasan Ahmed:** And and so like if you ask a question, how do I issue a card? It's going to explain to you the like exacting header um the ID like as in like as in like as in like it will explain each other like individual um like individual fields and how to use it. So you try an example like um can you give me an example payload

**George Westbrook:** Stop.

**Hasan Ahmed:** and so then like it will give you like examples with all of these like individual ual fields are added in. So like if I expand the actual view there are there are two options if you as as in if you want to view as like I think smaller sidebar or if you want the expanded view and

**George Westbrook:** Goodbye.

**Hasan Ahmed:** so I think added in like a few things. So if you want to do like a quick thing copy paste there's like a quick action here and so then I can click copy and then it'll be on my clipboard. So if I paste you see there um and then I threw this if you see like a example payload and you want to try it out in the actual sandbox you can say um can you run a test with this in the

### **00:06:59**

**George Westbrook:** Yeah.

**Hasan Ahmed:** sandbox and then on here like it will think um like it will like add it into like a like a like example the payload and then it will and then it will execute it for you and then it will I mean I believe it will ask you for like approval first like if you want to execute it um yeah and so like it will give you the like example request here in the like output as well. And then like if you want to do it on your like your own like in like the for example like Postman like you you have the exact curl as well. Um and then if you want to approve it. Um yeah. And then after you like approve it, it will give you the actual card details as well. So like I asked the the actual style that um how

**George Westbrook:** All right.

**Hasan Ahmed:** do I actually issue a card and so then it will issue like a card on like an example account and then like I give you the output that as well.

### **00:08:34**

**Hasan Ahmed:** Um let's say for example you are trying to speak to the claude now and you um as in if you want to start speaking to the actual agent and you want to and if you want to take it off here and go into claude or go into the chat GBT we have the option to export it as like a MD file and like I mean like essentially it's more of like a

**George Westbrook:** What is happening?

**Hasan Ahmed:** handover so it will explain into your AI agent, how to use it, how to access everything. So, if I open up the markdown and bring it over um

**George Westbrook:** So, go away.

**Hasan Ahmed:** um drag it over um

**George Westbrook:** Don't miss.

**Hasan Ahmed:** um screen. Yeah. Um if I drag this over here um it will be the um

**George Westbrook:** Yeah.

**Hasan Ahmed:** the oh okay um I think it's a share my window not screen um a second to be Sh screen. Okay. Um, so if I open up this back to

**George Westbrook:** Yeah.

**Hasan Ahmed:** um as in like over here like it would just explain to your like AI agent like everything in the like actual um like in the act the accident chat summary um like as in like it explain that it's a handover and then like it'll give you brief like a sort of like a summary.

### **00:10:39**

**Hasan Ahmed:** And so then it will say like I asked how to issue a card and then I asked to do a like example payload and then it will explain everything that the actual agent like I mean like it um like like it will explain everything that the like agent also like executed as well and then it will give that onto your like claw or like RGBT or the castle like any sort of like AI agent and then it will have the entire transcript as well included. Um we also have I think it's also the chat history as well. Um so as in like it's stored inside the actual the browser cache as in so if you are not think signed in it will be stored in your actual browser um for I think it's up to 30 days and then it will just like clear out and then I think after we have I mean I believe after we have um like authentication sorted out um we are able to to install like actual chats like on like a person's like account for example.

### **00:11:58**

**Hasan Ahmed:** And then if they want to see the entire history or or if they want to go to an old chat Like if I click on this one here for example as in like it would just be like a old chat with the entire transcript. If I I mean like if I just want to export it and also then you use it as like an example for then claude I can just go to here to an old chat export that or I can I can just like also then copy it to my clipboard as well. Should resh it.

**George Westbrook:** That's

**Hasan Ahmed:** Yeah. Uh yeah. I don't know why. Yeah. No, I'm sharing the entire screen right now. Um but yeah. Um, and so yeah, um, if there's any sort of other questions or if you have any sort of issues or anything that's really standing out to you that you want to really ask about, then yeah.

**George Westbrook:** I think I think I think there's two things that would be that would be worth adding to that as well is is is stuff that the agents using behind the scene and in turn what users are going to use as well.

### **00:13:15**

**George Westbrook:** So incorporated into this is the the docs MCP server um which is taking the content that's published on the knowledge hub via Braco. Um, effectively what we're doing is we're pulling all of that in and then putting that into an MC what putting that one for the agent. So there's a a local representation for the agent to use which means it can search so it very easily navigates the pages by blah um but also allows us to build an MCP server which we can expose to other people so that even if they don't want to use the the docs assistant they can put that MCP server into their own claude within one or two commands um because it doesn't need what up for debate but doesn't need to be authentic authenticated um because all it's doing is accepting the information that's there already. Um so if people want to skip this step, they integrate the MCP server, bam, they're done. They're going to get the access to the same information. Um and then on top of that, one of the things that we're most likely going to add to the handover as well is let's say somebody wants to take it off of here onto their own claude.

### **00:14:25**

**George Westbrook:** Um we're going to have the so there's the LLM.txt TXT, which is with a lot of companies, what they'll do is they'll just have one 2,000 5,000 line line file. Um, I think we were speaking to Statworks about this yesterday and that there wouldn't be an issue. Um, is effective will have one LLM.txt which acts as kind of like a router. Um, and then at the end of the other routes for these certain pages, we'll have other text files as well. So even if a user hasn't connected the MCP server, they can paste in the um the handover message um and they're going to get the source of truth for that page in a format that easily digestible for the agent. Um so if somebody's typing in, hey, I've seen this platform uh TXN thinking about it, it's going to be coming up in the search results um or they'll go to the docs page, they'll see the llm.txt TXT and then that's going to expose expose a whole host of other information. So you're capturing people who actively want the MCP, but you're also going to be giving more information to people that might be doing that AI assisted discovery because there's that content available in that easily digestible format for the AI.

### **00:15:44**

**Ian Johnson:** Yeah, I I'll be honest, it's been very difficult to follow it because um I don't think it's been the sickest demo in the world and I haven't been able to read the text for half of it. Um which is not obviously not ideal. I know that Mike I think you've seen much of this already and were pretty impressed. I know there uh you mentioned the cold start and kind of that's not a permanent issue. I I think there's a couple of things from my point of view. So what we just looked at is very heavy on the API reference. Um but the part for me Mike is people who don't even know how to go about starting. So we dive straight into how do I issue a card? Does the relationship what's the relationship between an account card holder a card those type of things which I understand to be contained in the docs which I'm also interested in seeing because we skip right to let's get coding I know that's what you engineers like doing but the reality with a car program is you have to have some understanding of what the sequence of things is.

### **00:16:51**

**Ian Johnson:** So, I'd be super interested in understanding what's on the guides page and available. Um, I think the same principle applied, Mike, that we talked about being able to copy a page and um, have that in a kind of AI friendly format. So, I'd like to see some stuff around there as well to kind of I think there's the context of somebody going in and saying this is what I I need to do and walking them through it step by step because we got to realize some of these people will not have idea where to

**George Westbrook:** What the hell is that?

**Ian Johnson:** start and the working assumption is that they will start because it's they can't be bothered to read the docs. Whereas if we can disseminate the key information that's in docs relative to a natural language question then that will put them in a position where they get the information they need to then get to the API reference. So I think need to think a little bit about the different types of journeys that customers will be will be on.

### **00:17:58**

**Ian Johnson:** I mean my my understanding of this is should pretty straightforward because you're just reading available documentation and answering the question based on what's available. suppose the the point comes Mike is if there's a question that's asked that the docs don't answer or the docs are ambiguous about that's the bit that we then need to make sure that we know that so the docs can be updated um so the source um is both is always accurate whether you go whether you're looking at the docs or whether or not you're going through um through the AI so what where are we with the with the docs versus the guides rather versus the API reference stuff. Have you tested queries on the docs?

**Michael Moores:** Not yet. No, not from my side anyway. Obviously the docs will largely depend on what I publish. So obviously there's still a lot to be published and secured away. So I think that's the the bit on us there. There's a lot of foundation there, but I think you know we need to make sure that all the stuff you've sort of talked about there is covered off and the linkage and stuff.

### **00:19:04**

**Michael Moores:** I think most of it is,

**George Westbrook:** All

**Michael Moores:** but um we will publish that obviously into there. So I think it's on version one at the moment. So it's it's all getting ready for that. So obly I can put more content in there. We can check against some of those docs as well. So I'll do that on my side um and make sure that's there.

**George Westbrook:** right.

**Michael Moores:** But obviously from our side we've got something checking the docs every day as well. So from our vault making sure we've included everything. So that's a personal routine that I've got that will spot that while we're building and then obviously um we've also got a fresh desk check to make sure the questions coming in can be answered by the docs. So we've got enough foundation there to you know so make sure those docs will will compete basically. Um but I can do that testing specifically on the guides um as well and make sure it's there.

**Ian Johnson:** Okay. So, I think where I am with it is we're at a point, Brett, where um by the way, I I I do think it I always dive straight into the challenges rather than the good stuff.

### **00:20:07**

**Ian Johnson:** So, it's great. It's it's on the right track of the things that we were thinking about. What we need to be able to do a team is to be able to start demoing this to some internal people from uh Pay Corp and DT because you know they've heard a lot about it. I mean I've spent multiple meetings this last two days with Steve the chairman where he's talking about the fact that

**George Westbrook:** Let's

**Ian Johnson:** we've got this amazing platform and I'm thinking you're going totally on what we've told you because you have not seen it. Um,

**George Westbrook:** go.

**Ian Johnson:** so he does he absolutely does not know it to be true. Uh, which we need to kind of make sure that he's got a sense of it. And I think also crucially with DT, we don't want any blockers with actually getting the stuff set up. So we need to see the thing in action understand how important it is to our user experience so that when it comes to the point of okay now this needs we need these things to become true so that we can actually put this out in the wild whereas at the moment they've not seen it either.

### **00:21:18**

**Ian Johnson:** So all they've seen the the only thing they saw on AI Mike if correct me if I'm wrong is the super ultra design type stuff which this moved I think most of that was on the like if not all on the console as well. So this has moved somewhat significantly into you know almost being real life and we need to startizing some of that so that we get the things done that we need to get done. Um, so I guess my question is like I hear what you say about the guides and I know that the um I know that we've still got moving parts with uh DT, etc. But I I think we're going to have to have something substantial in there to be able to demo it even even though I know that it will change. Um, and I do think one of the things we need to think about is what are people coming to do? Who are the different types of people and where are they in their journey and what they're trying to do? So, if they already had a card program and they wanted just to dive into it and they understand broadly how card programs work, then great.

### **00:22:31**

**Ian Johnson:** Maybe they dive straight into the API reference, ask some questions. if they're AI savvy, maybe they just download stuff, maybe they use the MCP server from their own own environment, whatever it might be. But there's also other people that will come well who will want to understand, as I said before, the relationships between things. How do I actually go? What's the sequence of how I go about building these things? Um, and again, you can read the docs and it will tell you, but I still work on a basis that most people are lazy and don't want to sit there and read a bunch of docs or they'll want to be able to take that information, dump it in Claude or have Claude read it and then it tell them a summary of what that. So, that's what we're trying to replicate. So, I just think we need to think about first most importantly to make sure it's covered off effectively for when we actually go live. But second, you know, secondary importance is that when we actually demo it to the internal stakeholders that we're cognizant of the fact that some of those people will not be developers and come with a mindset of well hold on a minute, you just dive straight into how do I create a card?

### **00:23:50**

**Ian Johnson:** Um and and then even on the how do I create a card that that question assumes that the person understands that there needs to be an account and a card holder set up uh Mike before they get to creating a card which they may not have.

**Michael Moores:** Yep.

**Ian Johnson:** So there's some work to do just to think about the real life usage of this. But I think I can see that it's not I don't think that's backbreaking or or extensive work to get to that point. I think it's just thinking through uh how different people will use it. And then I really do think we need to think about when it is that we could actually get to demo this thing with absolute confidence that we're not going to be looking at a fuzzy screen or you know we've got a walk through to go through people because 100% don't want to be saying to the likes of Steve and possibly Anthony you know what you know have you got any questions or anything like that. We want to be able to say that we're going to come at this as this type of user and we're going to make the transition through guides into the API reference and give them a sense of what it is.

### **00:25:06**

**Ian Johnson:** It's such a key part of our messaging as you know Brett about not needing to be a card expert to be able to launch a card program. So we need to be able to show that that's the case.

**George Westbrook:** Yeah, one of one of the things I was thinking is it is so the conver the bit the conversation we had with Statworks yesterday was about that that integration piece where we're at the point now with the um with the knowledge hub side of things where it's a lot a lot of it is built and a lot of the changes that we're talking about is rather taking what we've got and optimizing it. Be it changing a prompt, representing the knowledge in a different way. Um, and really good conversation yesterday where folks they're very happy for us to work on what what they've already got. We've got access um got access to their environment um where they store their repos. We're able to claim the repos and get going on that work. Um and I suppose one of the questions is related to that with the demo is we we've got our demo environment at the moment.

### **00:26:12**

**George Westbrook:** Um look feels acts exactly like the real thing. There's going to be some divergences. Um we could keep that for the time being. Keep on working on it and treat that as this is the environment we are going to use when it comes to speaking to those internal stakeholders. Um make sure everything's there. make sure that we've got enough mock data so that it looks act like the real thing. Um, and we can really start to hammer down on that in parallel, making sure that we're getting the real thing ready for launch so that the day that that's that launch happens, um, everything on the knowledge hub side is there and obviously anything that needs to be in the console as well. Um, because I think that was the really good thing about yesterday is that way of working sorted. It really suits us and it really suits really suits them as well. Um and and it could have gone two ways I think where it could have been they might have liked a bit more control and said no we'll write this we we'll do that but for us it's unlocked a lot of potential blockers that could have been there which was which was booing for us.

### **00:27:18**

**Ian Johnson:** Yeah, that like like I say we we have apart from one where we didn't have a lot of choice but we have selected partners that we believe are collaborative and can work together and works have been excellent throughout it. So I'm not surprised that that's their attitude and mentality to it.

**George Westbrook:** Yeah.

**Ian Johnson:** Um, so I I I think the answer is that we're not going to we're not going to be ready in time to have everything knitted into the actual uh knowledge hub to do the demo from from there. Um, and when I I think that's the question I'd have for you guys is how long before you would be convinced that we could absolutely solidly set this demo up. The key thing being the longer it is to wait to get the demo set up, the further we've pushed before we can actually push on them to get the stuff. Now, as I understand it, Mike, we've got the things that we need them to do and we know what they are. Um, I just know DT well enough now from the last however many months that if they if they're bought to something completely cold, not they're not completely cold, they know it's coming, um, then it's just going to be more challenging.

### **00:28:29**

**Ian Johnson:** So, if you can take people with you and they're like, "Yeah, this is great. What can we do to get this up and running?" Then it's going to be a lot easier. I don't want to I want to The most important thing is the quality, the speed, and the completeness of the experience that we're showing. So, w with that in mind, I'm not going to push you guys for an answer right now. I think you obviously need to have some think thought about it. But my one question is have we and I'm sure that everyone whoever did it would use AI to do it. But some of these some of the things we've asked to do are really basic and I expect the I would expect the answers. I'm not saying that doing it is basic, but saying show me how to create a card is a relatively simple prompt.

**George Westbrook:** Yeah.

**Ian Johnson:** What about more complex things that might get asked Mike in the knowledge hub that we will undoubtedly happen when we hit the um hit the real world?

### **00:29:39**

**Ian Johnson:** And I just think it would be worthwhile pulling together a list of more challenging prompts potentially to see how it behaves with those.

**George Westbrook:** I could I think one thing we could do on that um now we've got now we've got a lot of the stuff in place is going to I think remember talking about ages ago go is that that kind of simulation. Um so if we could get an example of as many questions of you as you you can think of um then what we can start to do is say given that query what is the acceptance criteria for that query being done and then what we'll do let's say you've got 10 20 however many run them all in parallel um churn them through the agent do a hundred of each look at what the output is not just from one turn but a whole conversation um rank them score them, categorize them, take that information, and initially maybe we just look, we'll just see where the gaps are. Um, this response, which was a really quick response, the agent's gone and a f\*\*\*\*\*\* ramble and done a 500word message where all it needed to do was go here, look at this page, here's this snippet, bam, done.

### **00:30:48**

**George Westbrook:** Going to the longer, more complex ones is the opposite problem. It could be two. Um, and it like we all know from testing it's it's very good to see it with your own eyes, but it's it's not very scalable. So, I think now we're at that point. It might be it might be good if we have a brainstorm both on our side and your side and what those what those queries look like. Um, and what the expected not the expected output would look like, but what's a good answer and what's a bad answer.

**Ian Johnson:** Yeah, Mike, I don't I know you've got loads on your plate, but I can't imagine that that takes very many minutes for you to do based on you've got all the documents in the vault about how the whole thing works. I don't mean the whole AI piece. The the the one thing I'd ask you to think about is when they are longer more complex queries and bearing in mind it's not they're not quering live data they're coming

**George Westbrook:** Here

### **00:31:43**

**Ian Johnson:** from it from trying to understand how to do something is for example you know if I was to say explain to me what I need to do to be able to issue my first card then that's there's quite a lot of information

**George Westbrook:** we go.

**Ian Johnson:** there Mike in terms of it could be very it could be very high level well you have to create an account actually I don't know if all of this is true but I know I know the account car holder and card is true there might be some stuff above that you could be really thin on what that information is um or you could just bulk it all on one page and make it kind of really difficult for people to scroll down and I think

**George Westbrook:** Let's

**Ian Johnson:** the thing we've got to bear in mind is that we're trying to educate people I think there's two things right.

**George Westbrook:** see.

**Ian Johnson:** So one is explaining step by step and asking them to make a positive approval to move to the next stage. So if it was for example first step is create account and you explain how you create account and then it says next step create card holder.

### **00:32:50**

**Ian Johnson:** Would you like me to explain how to create a card holder? Yes. And then you you go like you get the card holder and then you get to the card piece. So, you're being walked through step by step how to do it. Um, but your the ultimate goal is to make sure they can do it. Just giving the information and assuming that they've read it and understood it without any kind of feedback doesn't really necessarily work. Equally, George, there might be people who just want the dump of the data because they're just going to go away and stick it in AI and they're and they're going to get that to figure it out for them. So you've got these I say come back to different personas using the system but I do think with the with the bigger and I think it's the same my experience at least is with claude that the bigger more complex things that you're asking it to do it will come back and ask you to give you a number of options of what you want to do and then you approve it and then back and it goes okay this one.

### **00:33:49**

**Ian Johnson:** So I think we just need to think about some of that stuff because the the ultimate goal is people are able to launch card programs faster

**George Westbrook:** Yeah,

**Ian Johnson:** in Card Experts

**George Westbrook:** I think and so there's a now and there's a future. So the now what we can do in that simulation is create those different personas. Maybe it's just three to start with. the ultra comp the ultra developer type and the the opposite end of that spectrum. Same thing. Add them in as a variable. Test test test. And the the future part could be when we've got all of those chats, we can analyze those guess whatas they are um and take a view. One view could be right. We see we thought it would be this low complexity one. It turns out a lot of them are high. Okay. let's tune it so it's more focused towards them. Or it could be let's put in something in place so that after the first two or three turns of the message, we try and identify what style of communication this user has got and dynamically adapt it.

### **00:34:54**

**George Westbrook:** Um that's a rabbit hole. It's just an idea I'm throwing out,

**Ian Johnson:** Yeah.

**George Westbrook:** but I thought I thought I've mentioned it because otherwise so we've got our AI notes in there.

**Ian Johnson:** Yeah. Yeah. No, understood. So where in terms of where we are from a demo perspective before the things that I just talked about where where are we as far as you're concerned in terms of being ready to demo this to the kind of stakeholders that I just mentioned

**George Westbrook:** Correct. If I'm wrong, this is this is on the the production environment, isn't it? On the knowledge of of our production envir uh environment.

**Hasan Ahmed:** Um yeah I mean at the moment it's on our think client like facing like environment but I mean like if we um like if we are going to think demo it then we need to turn off like the code starting so then it's a lot quicker to answer you I mean cuz at the moment

**George Westbrook:** Yeah.

**Hasan Ahmed:** cuz like it's only thing here and there we are going to be demoing so like it's just on a cold start just to you know Yeah.

### **00:36:03**

**Hasan Ahmed:** But um I think

**Ian Johnson:** If any if the characters that will be on that call, if the if the cold star is active, it won't go well.

**George Westbrook:** Yeah.

**Hasan Ahmed:** yes.

**George Westbrook:** So, I think yeah, it's it's get those speed issues sorted. We'll get we'll set up a small environment that's always on. I think what would be good is if we all go in, we have a play around with it, catch some of the first issues that we've got up until it's at a point where we're like, no, look, this is this is good. We're happy with this, then plan out the this is how we're going to do the demo. We're going to position at this user. We're going to achieve these three or four outcomes, these three or four flights, so that when it comes to that point, it's it's like you said, it's slick. Nobody's needing to ask a question at the end because they've already been answered in in the de um though yeah I think it's speed issues pretty easy to sort um testing identify some of those issues incorporate those fixes then get that plan of what what we want to do but suppose it'll be a what do we think how it should go and then what you what you you guys think align on that make sure we've got that solid so that

### **00:37:15**

**George Westbrook:** when that demo happens They're like, "f\*\*\*\*\*\* hell. I thought it was good, but I didn't know it was this good.

**Ian Johnson:** That would be the desired outcome. George. Yeah.

**Brett StClair:** Or they just go, "Man,

**George Westbrook:** That's

**Ian Johnson:** No, they probably some of them might not understand it, but we will.

**Brett StClair:** what

**Ian Johnson:** I think the point is got a mixed bit. So, you got Steve you got Steve who ultimately is the chairman. He needs to actually see the thing. Let's be clear about it rather because I think it's important. Um and then I think we'd want um Gavin who's the CTO at Pay Corp. Um and then I'm not quite sure it might be Anthony Mike at um DT. Could be a couple of folks from DT. Um, so it's it's they'll have different levels of understanding. Steve won't know one ass one end of an API to from from the other. Gav Gavin will uh Anthony may do. Um but I think it's really that if we think about if we think about with the end in mind is at the end of that demo do the stakeholders see it and go okay I can understand why we're saying that you don't need to be a card expert to launch a program with

### **00:38:37**

**Ian Johnson:** us and the meet you wherever you are. So if you don't want to go into the knowledge hub and read docs and do all that kind of stuff and you want to just basically take that information and stick it into um into claws whatever then you can do that also. So I think that those are the headline objectives of what we're trying to achieve.

**George Westbrook:** And is this is this just a demo of the the knowledge hub side of things. Nothing.

**Ian Johnson:** It is.

**George Westbrook:** Okay.

**Ian Johnson:** It is. Yeah. That's the thing that we need to that's the first thing that will hit the market when we uh when we finally go to market. Um so that's the that's the thing that we're focused on.

**George Westbrook:** Okay, perfect.

**Brett StClair:** George, what are we waiting for on access to the environment that we can just make sure we get it today, tomorrow, ASAP, and start getting at least in some feedback on us getting it into the Stackworks DT environment.

**George Westbrook:** Uh, so I think we just got to start working on integrating the what we've built into the into Stat Works' version.

### **00:39:43**

**George Westbrook:** Um, so we've got we've we've got our own branch that Vinethkindly set up. Um, so we can start working on that. We can yeah get that spun up either on our local machine. Um, if idea if we could get it into Azure that would be ideal. If we can't in the time that's fine. we can set up a version on our infrastructure um or have it running locally. Um so when it comes to deployment, there's plenty of different options that we that we can use.

**Ian Johnson:** Yeah. C can I can I make a suggestion as well just and take it the right way. I love working with you guys but sometimes the demos don't goly right.

**Brett StClair:** No,

**Ian Johnson:** This one has got to but you can't control everything. working with kids, animals, live demos, all things that you probably shouldn't do. There are many other things you shouldn't do, but I'm not going to say

**Brett StClair:** I've sacrificed all my children. I don't have any more left.

### **00:40:36**

**George Westbrook:** God.

**Ian Johnson:** is settled on a a set of prompts that based on those different persona journeys that we should probably get it done on one of those Loom videos or whatever you said you were going to do.

**George Westbrook:** Huh?

**Ian Johnson:** I I think I'm not suggesting we just sit there and press play on it, but I think it's a super useful asset to have where where it's in a controlled environment, we know it works. We know it's delivered what we want it to deliver. And all of the gremlins that might kick us in the, you know, where with slow broadband speeds or whatever else it might be, that's not going to be the end of the game.

**George Westbrook:** So the demo won't be a live demo. It will be either a loom we send to people or on a call a video we are playing and talking through as it's happening.

**Brett StClair:** No, that's a backup.

**George Westbrook:** Okay.

**Brett StClair:** We need to be ultra prepped for a live demo.

**George Westbrook:** Yeah.

**Brett StClair:** Test absolutely everything. Make sure everything's running as fast as possible.

### **00:41:42**

**Brett StClair:** Scripted as clean as possible. Pre-run every single scenario that we're going to test. Make sure we address the right audience. Record it. have it as a backup. If connectivity bombs or things are falling apart, then we either try whip up the video or we can send the video and walk everyone through as they're watching on their side. Cuz I agree with you, the connection to South Africa can be temperamental.

**George Westbrook:** Oh yeah, I forgot about that.

**Ian Johnson:** Well, and Steve, I don't know where Steve will be, but it's hardly like to be South Africa. He's he's all around the place. But I think the other thing is if everyone's if Mike's got the Loom video, I've got it, you've got it,

**Brett StClair:** Oh yeah.

**Ian Johnson:** D's got it. If all all of us are screwed from an internet perspective, then there's not a lot an awful lot you can do about it. Um, but I think it's just belt and braces to make sure that it goes well.

**George Westbrook:** Okay,

### **00:42:41**

**Ian Johnson:** I mean,

**George Westbrook:** perfect.

**Brett StClair:** So we need to come back to you with a a date that we can be as best prepared for it ASAP.

**Ian Johnson:** yeah. Yeah. ASAP. But the focus is those two outcomes. And if you need longer to make sure that we're confident on those two outcomes, what I'd really like to happen is that somebody, you know, we walk through the demo and then somebody says, "Well, ask it this." That's because that is the thing that I would be doing. In fact, it's the thing that keep doesn't keep me awake at night, but that's the thing. That'll be the first thing you go. You go live, you've gone through all of these things and then somebody goes in and asks a question and it just goes it brain farts everywhere. Um, which is going to happen. The problem with some of this stuff is that some people won't necessarily know that what they've just had back isn't accurate.

**George Westbrook:** Huh?

**Ian Johnson:** So um but yeah if you can have a think about that it it will be it's an important kind of um milestone to get through um and then it will get it will definitely if it goes well well it will go well it will definitely give us the impetus we need to make sure that we don't go through some kind of loop with DT where they're questioning everything like no this is We're delivering

### **00:44:06**

**George Westbrook:** Let

**Ian Johnson:** tools that deliver the vision. We just need you to do this thing quickly and without too much noise. Okay.

**George Westbrook:** Perfect.

**Brett StClair:** Yeah. And one of the best demos we ever had, it was an unplanned in an insurance space. The client went, "Could this do it for me in Hebrew?" and she sent through an email with all the attachments in Hebrew. It pulled it all out. It presented it back in English. She then responded to the agent in Hebrew and then said, "Listen, I want you to talk to me in Hebrew thereafter." And it worked. We had not f\*\*\*\*\*\* planned it. Did not know could do something like that.

**Ian Johnson:** I shouldn't imagine that you had to be honest.

**Brett StClair:** It threw us and it came back and it just worked. Thank God. That was one of the most stressful moments.

**Michael Moores:** This is

**Brett StClair:** So,

**Ian Johnson:** Yeah,

**Brett StClair:** I get where you're coming from.

**Ian Johnson:** I think you could have got away with that one was to go and say, "Well, that's we weren't really expecting that." Probably.

### **00:45:18**

**George Westbrook:** Oh,

**Ian Johnson:** But you never know. You do never know what these people might come up with. Um, it does raise an interesting question on the on the language side of things, but I do think one of the things is that we're I think from a language point that that's super interesting to me is so we're not going to support clients in other languages early. So I don't think there's there's any point publishing assets, etc. websites, knowledge hubs in a language that you can't support at the end. But with AI, they can take that information that's in English, dump it into Claude, and they can get Claude to do the translation or whatever their desired tool might be.

**George Westbrook:** All

**Ian Johnson:** So, it takes a lot of owners off us in having to do all that translation stuff

**George Westbrook:** right.

**Ian Johnson:** quite frankly. But yeah, that doesn't sound I would imagine that was a bit squeaky bum time to be honest. But it worked. You know, more by luck than judgment, but it works.

### **00:46:23**

**Ian Johnson:** Uh so we'll leave that for you to have a think about my I

**Brett StClair:** Well, no.

**Ian Johnson:** guess the question for you is and I suppose working back from when you guys think you can be ready what are the prerequisites that you need to have all the dependencies that you've got of us I I mean specifically might probably the documentation um being available um knowing it's not going to be the end version of it.

**Michael Moores:** Yeah, it's 40 in there already. Um, as best as they can be.

**Ian Johnson:** You make it sound like there were three.

**Michael Moores:** No, I've done the whole 40 40 on I think.

**Ian Johnson:** Anybody else get the impression that there were hardly any docks in there? as I did.

**Michael Moores:** Yeah, they're there.

**George Westbrook:** No

**Michael Moores:** Obviously, they don't mention the payloads and stuff on purpose, but I need to have a look at those questions you sort of stated and make sure they're covered off as well. Um, but yeah, they're all handwritten because that's what Umbrau requires. So, no AI, unfortunately.

### **00:47:26**

**Michael Moores:** But, um,

**George Westbrook:** heat.

**Michael Moores:** yeah, I went through all 40 took about 30 minutes each. So,

**Ian Johnson:** They're all handwritten.

**Michael Moores:** you've got to put like every title's got to be its own component and every table's got to be. So, you have to drag. You can't just copy anything in. You got to create a component for a title. create a table, add every single row and column. It's quite a long process. Um, but yeah,

**Ian Johnson:** Yeah, it sounds painful.

**George Westbrook:** It's 10 times more painful when you know if you just gave it to AI just like do it in a second. Yeah, it's weird going back and doing things the way they always used to be used to have to be done.

**Ian Johnson:** But isn't it so what's stopping them? call it from being able to do.

**Michael Moores:** I don't know. I just need to have a look at the API. I guess there's no direct MTP. So obviously we'd have to build something with Stack Works or something to to integrate that.

### **00:48:17**

**Michael Moores:** It's just not been built yet. So

**Ian Johnson:** No, I think it I mean at the end of the day they don't get changed that often. They're getting changed quite a lot at the moment, but they don't get

**Michael Moores:** once it's in, you can just add extra text to the text box. It's not it's a structure more than anything.

**Ian Johnson:** Yeah.

**Michael Moores:** Um it's pretty easy to update after that. So it's not too much of an issue after.

**Ian Johnson:** All right. So, you guys can leaz with each other to figure out um a timeline and then I'll take responsibility for making sure we get it on. We'll obviously do a pre run through um and obviously you can do that by sending the yeah send send the Loom video in advance. We can do it that way or we'll jump on a call. To be to be perfectly honest, it doesn't matter if we it doesn't matter if let's say on I know these are not time frames, but if on Monday we did a live demo and everything went swimmingly and no internet connection problems or whatever else there might be.

### **00:49:14**

**Ian Johnson:** It doesn't ring true that when we actually did the one on Friday, the same would be true. So I'm not really interested in that bit. It's the functionality and hitting those different personas and a and

**George Westbrook:** H.

**Ian Johnson:** a varying level of complexity in query and seeing how it performs from that point of view. Okay,

**Michael Moores:** Yeah. So, let's

**George Westbrook:** Ly.

**Brett StClair:** Happy days.

**Ian Johnson:** we're getting there.

**Brett StClair:** We're getting there. Um,

**Ian Johnson:** I mean,

**Brett StClair:** I'm popping.

**Ian Johnson:** the other thing the other thing to say, you know, if you do a really good job, it might help me secure more funding to do more AI things.

**Brett StClair:** Come on.

**Ian Johnson:** You know,

**George Westbrook:** Oh,

**Ian Johnson:** George is thinking, I don't want these guys to get any more funding to do things.

**Brett StClair:** What?

**George Westbrook:** Ian, I'm a sad bastard. I love building this stuff. science.

**Ian Johnson:** Give me an insurance company any day. That's what bother when your provider or partner says they'd rather work with an insurance company. Right.

**Brett StClair:** Um,

**Ian Johnson:** Enjoy the rest.

**Brett StClair:** Ian,

**Ian Johnson:** I'll leave it to you. Anything else? Sorry.

**Brett StClair:** I'm just dropping something in diary for 12:00 Monday. Is that okay?

**Ian Johnson:** All good.

**Brett StClair:** Perfect. Thank you.

**Ian Johnson:** Bye folks.

**Brett StClair:** Superb.

**Ian Johnson:** Catch you later.

**Brett StClair:** Thank you.

**Michael Moores:** Cheers. Okay,

**Brett StClair:** Catch you later.

**George Westbrook:** What's

**Michael Moores:** take care.

**Hasan Ahmed:** All right, is

**Brett StClair:** Chow.

### **Transcription ended after 00:51:02**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*