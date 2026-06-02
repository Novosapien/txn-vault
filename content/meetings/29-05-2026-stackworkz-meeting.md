---
date: 2026-05-29
type: general
scope:
  - "[[agent-access-layer]]"
  - "[[full-agentic-experience]]"
  - "[[developer-support]]"
status: extracted
extracted-to:
  - "[[vision]]"
  - "[[components]]"
  - "[[integrations]]"
  - "[[agent-access-layer]]"
  - "[[index]]"
---

# Stackworkz Ways-of-Working Call — 29 May 2026

> **Type:** General (partner integration / ways-of-working)
> **Parties:** Novosapien · **Stackworkz** (Corneil Clasen, Ruan Sunkel, Liza van Eyssen) · **TXN** (Mike Moores — CTO, Dorte Dye — COO)

First working session between Novosapien (AI layer), Stackworkz (Console + Developer Portal build), and TXN. Purpose: integration scoping — who builds what, how the AI layer plugs into Stackworkz's environment, and where the ownership boundaries sit.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| **Partner landscape named** — Stackworkz builds the Console (frontend + back-end-for-frontend) **and** the Developer Portal; Super Ultra is the design team; Direct Transact (DT) builds the Core API / card-system backend + Data Lake | [[vision]] §1 Scope boundary · [[components]] out-of-scope | Updated |
| **Stackworkz stack & infra** — C#/.NET BFF, React + Material UI, Umbraco headless CMS, Azure DevOps, VM-based; DT on Kubernetes; BFF↔Core API is API-only; permissions + user management live in the Stackworkz BFF, not the Core API | [[integrations]] | Note added |
| **MCP-server ownership split** — docs/dev-portal MCP (LLMS.txt) Stackworkz wants to own; card-acquiring-API MCP ownership unresolved (possibly DT); avoid duplicate MCP servers | [[agent-access-layer]] | Open question added |
| **Permission model source** — granular permissions live in Stackworkz's BFF; the agent permission model must mirror it | [[agent-access-layer]] | Dependency updated |
| **AI data-access pattern** — data-lake plug-in vs pull-and-aggregate via Core API; DT open, depends on their timeline | [[integrations]] | Open question noted |
| **Full agentic console experience (AG-UI)** — agent renders the real React/MUI components in a chat surface, persistent; reuse Stackworkz's components; build a POC (fake/MUI library) so stakeholders have something tangible | [[full-agentic-experience]] | Flagged for deep-dive |
| **Portal AI = knowledge-base only for MVP** — doc search, surfacing existing support tickets, co-pilot view; one central knowledge piece serves portal + console; CMS docs exposable via API | [[developer-support]] | Flagged for deep-dive |
| **Dev environment** — build in Stackworkz's existing env vs a TXN-controlled Azure env; cost attribution unresolved; Mike to resolve with Ian | [[integrations]] | Flagged (TXN decision) |
| **Timelines** — Dev Portal + API target **October** (go-to-market first); Console follows, aligned to first-customer onboarding, date not locked; AI may be a fast-follow if it misses MVP dates | [[index]] | Note added |
| **Next steps** — Super Ultra console design session Wed 3 Jun 2026; Stackworkz finalising console scope + cost with Mike/Dorte | [[index]] | Note added |
| Ways of working — Stackworkz flexible/agile, happy to fit into Novosapien's plug-in points; consolidated environment preferred | — | No action (context) |

---

## Transcript

### 00:00:00

   
Michael Moores: Are you okay?  
George Westbrook: How we  
Liza van Eyssen: Well,  
Brett StClair: hey George.  
Liza van Eyssen: thanks.  
George Westbrook: doing?  
Corneil Clasen: Hey.  
Brett StClair: Um,  
Corneil Clasen: Hey everyone.  
Liza van Eyssen: Thanks a lot.  
Brett StClair: um, I just want to make sure everything's recording.  
Liza van Eyssen: Yeah,  
Brett StClair: Yeah. Yeah. Okay. Cool, cool, cool, cool, cool. Um, who else are we waiting for?  
Liza van Eyssen: I see Da did say that she was coming. So, I'm guessing that she'll join. I know that her leave, I think,  
Brett StClair: Okay,  
Liza van Eyssen: ended yesterday, so I think she would be on the call today. Michael,  
Brett StClair: we go.  
Michael Moores: Yes, you chasing  
Liza van Eyssen: cool. So,  
Brett StClair: She's coming  
Liza van Eyssen: she might  
Brett StClair: through.  
Michael Moores: them.  
Brett StClair: Is she coming in? I don't know. Oh,  
George Westbrook: There we  
Brett StClair: there we go.  
George Westbrook: go.  
Dorte Dye: No. Morning.  
Ruan Sunkel: Thanks.  
Brett StClair: Uh, why is it saying deny admit?  
   
 

### 00:02:07

   
Brett StClair: Here we go. There we go. Hello,  
Dorte Dye: I  
Brett StClair: son. Um, I think that's everybody.  
Dorte Dye: need  
Brett StClair: Happy days. Okay, let me kick this off. Um, thank you everybody for joining the call. Um, the safans, are you guys mainly in job or Cape Town by the way? Victoria,  
Corneil Clasen: Victoria best the best best city.  
Dorte Dye: that.  
Brett StClair: all all of you guys.  
Corneil Clasen: Yes. Yeah.  
Brett StClair: So,  
Corneil Clasen: All of us.  
Brett StClair: second best city. Hey  
Corneil Clasen: Definitely the best city. Yeah. Depends. Cape Town I don't think is a city you live in. It's a city you visit.  
Brett StClair: No, no, no, no, no. I was comparing you to Joe  
Corneil Clasen: Um okay.  
Brett StClair: Book.  
Corneil Clasen: It is definitely best by far.  
Brett StClair: I  
Ruan Sunkel: Yep.  
George Westbrook: I think the smiles on everyone's faces said said a lot there.  
Brett StClair: fought  
Liza van Eyssen: Jober is very expensive, very expensive and very unkind.  
   
 

### 00:03:11

   
Brett StClair: and run down.  
Liza van Eyssen: Pritoria is more homey and friendly Africans  
George Westbrook: Okay.  
Brett StClair: Yeah,  
Liza van Eyssen: people.  
Brett StClair: it's lovely there.  
Corneil Clasen: Where are you? Great.  
Brett StClair: I'm based in London. Um, moved out about five years ago.  
Corneil Clasen: Okay. Sorry  
Brett StClair: Sorry,  
Corneil Clasen: about  
Brett StClair: at the moment I feel like I'm in a sweat box. It's so hot here.  
Corneil Clasen: that's why that's why I'm sorry I've heard  
Brett StClair: Uh,  
George Westbrook: We're not built for that sort of weather over here. As soon as it crosses 20°,  
Brett StClair: print.  
George Westbrook: roads start melting. It's just Yeah,  
Corneil Clasen: no we're we're in the middle of winter here FYI and today is 24 degrees  
George Westbrook: it's  
Corneil Clasen: just to put it into perspective.  
George Westbrook: Yeah. Cheers for that.  
Dorte Dye: I want to 20 next week. So it's like whatever you call our  
George Westbrook: Yeah, I I'll be thinking of that comment in uh in December when it's our winter and it's raining outside and it's  
   
 

### 00:03:56

   
Corneil Clasen: Yep.  
Dorte Dye: summer  
George Westbrook: 2° and it's like, "Oh, the the sappers will be 25 degrees  
Liza van Eyssen: But also in your guys' defense,  
Corneil Clasen: Right.  
Liza van Eyssen: because I've heard talk from my husband's colleagues um of 33° in  
George Westbrook: us.  
Liza van Eyssen: London. Um, you guys have very humid weather. So, like 33° in humid temperatures is a very different story to 33° in dry temperatures. Like it's you have to keep like 33 humid is like 40 something  
Brett StClair: Yeah.  
George Westbrook: Oops.  
Liza van Eyssen: actually.  
Brett StClair: And it's it's not your Durban humidity cuz there's wind to cool you down. It's no wind.  
Liza van Eyssen: It's from the ocean.  
Corneil Clasen: when they start urging the elderly to carry water on the tube.  
Brett StClair: and Cornel I  
George Westbrook: Okay.  
Brett StClair: do  
Corneil Clasen: Shame.  
Brett StClair: sorry let's get into this so uh the point of today is uh do some introductions and we want to We want to understand how we need to work together like figure out a ways of work um uh understand we don't you know you guys are going to be guiding on code base and interactions and how you want to govern and control and so we want to understand how you guys are managing that and how we can best fit in to your environments uh without being a  
   
 

### 00:05:26

   
Brett StClair: hindrance with fitting into your deployment mechanism. um and where we touch base because we are going to be touching into your space, right? Um and just decide where, how, how do we execute, how do we set up the permissions, what repositories do we need to get set up. Um and you know, if if we're suggesting stuff that's going too far, please push back. Right? This is trying to find a a space where we can all work together and we don't want to infringe in your space. You're like the you're controlling the uh domain of of code and and and how to deploy it all. And so we'll fit into that. Um and and make sure that we're not breaking anything. Uh we've got the right testing procedures in place to ensure we're not infringing on anything on your space. So I just want to be clear like like that's how we want to approach this. We do not want to be causing a challenge in your space and then take that as a starting space and then figure out how do we integrate and and understand how you guys are building so that we fit into your ways of work essentially.  
   
 

### 00:06:40

   
Brett StClair: Are you guys cool with  
Corneil Clasen: Yeah,  
Brett StClair: that?  
Corneil Clasen: I'm happy to maybe Brett if you if if I can take a few a few minutes just to I think like just from the outset like we're super super kind of open and flexible like we're keen to kind of work with you guys see what we can kind of accomplish together like so if you're kind of looking for a team that's um that's what do you whatever you want to call it kind of ready and kind of in the modern stack etc kind of here with you guys then then it's us I think it is probably just important to to um and Mike um please just interject here if I'm going off the rails but it is probably have you guys had a similar discussion with the the DT team the direct transact team okay do you guys have like an an  
Brett StClair: Watch it.  
Michael Moores: Not  
Corneil Clasen: idea of where kind of where we play versus they play kind of or should I give you an idea or are you happy there?  
   
 

### 00:07:30

   
Brett StClair: Yeah, we're happy there.  
Corneil Clasen: Yeah.  
Brett StClair: Maybe paint out kind of like how you're actually integrating with the DT guys and maybe give us a sense on you microservicing.  
Corneil Clasen: Yep.  
Brett StClair: How would we leverage maybe assets that you guys have for certain circumstances or where we would just integrate directly into DT?  
Corneil Clasen: Yeah.  
Brett StClair: I guess it's figuring those little softer components and we're going through the requirement phase from a an agentic point of view over the next week to really understand. I mean the design teams have done an amazing job really mapping out the journey is fabulous. You guys are going to be executing on all of that. Now we've got to understand what does it look like from that agentic point of view and making sure that we're fitting it in as unobotrusively as possible. I  
Corneil Clasen: Yeah. Okay.  
Brett StClair: guess.  
Corneil Clasen: But I think maybe then like a good a good starting point is just to to explain to you how we see the pieces. Um, and then sorry I just jumped in straight now, but Ron stop me if I'm um if if you disagree,  
   
 

### 00:08:25

   
Brett StClair: Yeah.  
Corneil Clasen: but I think the the the biggest thing like so originally we were contracted, we have a history with with TT um we've done some projects with them in the past. So we originally contracted to kind of for lack of a a simpler term just to build the front end like the so the front end for what they've bought or the front end for the console that then kind of quickly grew into like what I currently see as there's a like a card system back end which is what DT is building then there is like a back end to the front end um which we are taking control over and then there's a front end um we as stack works and that back end to the front end will interact with the the card system back end only via API. So, um like I'll get back to the to the to the actual infrastructure portion um in a moment, but like in terms of um um coupling there, like yeah, we are interacting with that card service with the the API that DT is building and that's it.  
   
 

### 00:09:25

   
Corneil Clasen: And that would be the same API that their clients would use that go that don't go through the console that just use the API to build out their own guard systems. So a big portion of what um what Mike and Dort and them are dealing with with the DT team is to ensure that everything that Super Ultra is designing in the console is possible through the API um because it's ultimately one API and the same one that their clients will interface with. So I think the why but you obviously understand that but why that's important is if there is if there's an AI  
Brett StClair: Thank you.  
Corneil Clasen: component that need that's deeply integrated into the data then we would consume that data through the API but you'll probably have to have a discussion with the DT team to see like they expose all that data into a data lake and you plug into that or like do you also have to pull it through the API and aggregate and whatever that strategy is and I think the we haven't had a lot of discussion DT but I think they are also open to all of that.  
   
 

### 00:10:16

   
Brett StClair: Um,  
Corneil Clasen: It's just kind of where it fits into their timeline and set of priorities I guess. Um so from our perspective the the only pieces that are quite obvious at this stage that we will handle um in the in the in the front end slash the back end to the front end is uh there's a CMS. So there's a content management system that's generating the documentation etc. And why I'm mentioning that is there's obviously some flows and that I've seen from an AI perspective having a kind of a search across the documentation as example. So that will be in our domain. Um so we should like we can possibly kind of expose that whether it's from the CMS or or whatever. And then the the other portion is more on the console side. We've agreed that all the permissions and user management and all of that lives with us. it does not live in the the core um API. Um so those things possibly as well.  
Brett StClair: Yeah.  
Corneil Clasen: But if it comes to things like what suggestions are made for setting up a a card program um we will have that information by means of the API but we won't be the source um the actual source that would be would be DT.  
   
 

### 00:11:28

   
Brett StClair: Done.  
Corneil Clasen: So there like I'm not certain kind of um what the strategy should be there for integration. And then to your last thing and then I'll I'll go quiet. Um just in terms of your questions, Brett. So we're in the .NET ecosystem.  
Dorte Dye: Oops.  
Corneil Clasen: So it will be a um yeah it will be a a C#.NET back end for that front end. It's a React front end. Um and it is we will be using material UI from a component library perspective. Um uh for the front end itself and then there's some custom pieces for like the API but I mean that's not necessarily relevant to you guys. Um, and then we're using Braco for the CMS, but that has a we're using it headless. So, um, it's headless exposing APIs that you guys can probably plug into as well if it get that. We're using those APIs to generate the front end the front end.  
Dorte Dye: It's  
Corneil Clasen: Um, so yeah, that's the stack. We're in DevOps.  
   
 

### 00:12:22

   
Corneil Clasen: So is DT.  
Dorte Dye: good.  
Corneil Clasen: So currently we have a development environment in our um in our infrastructure but soon the discussion will kick off with DT and we'll basically mirror that DevOps repo to their um uh um setup and then they will run it probably they've just mentioned like a QA pre whatever their staging setup is in their infrastructure but to get us going and not um stop kind of from an infra perspective we have an environment on our side in our control um with a repository on our side etc. that sits and lives in DevOps. Yeah.  
Brett StClair: Lovely. Absolutely lovely.  
Corneil Clasen: Thing Ron were you  
Brett StClair: Um  
Ruan Sunkel: uh just just one comment that might help uh just guide the discussion from a technical perspective. Um if you look at the designs the design of the development portal, there's two main ways in which AI is used. Uh the one is in the form of a chatbot on the site that's got access to the um the relevant information and also guide the user on what to click and and in some cases even perform actions.  
   
 

### 00:13:30

   
Ruan Sunkel: And then the other side so that's more of an operational focus. The other side is more of a dev focus where um sorry before I go there so on the  
George Westbrook: Hey,  
Ruan Sunkel: site um the chatbot that will be a sitewide AI so that's probably more where you will integrate so there will be a single LLM somewhere I don't know what your setup looks like the other perspective is from a is the developer focus where I as a developer make use of e either thems are available but I use my own setup my own agent and my own LLM. Um and so part of this discussions I think um you can also weigh in here is is who is responsible for what because we as stack works we we can implement the developer side of it like setting up the MCP servers um constructing the LLMS.txt ext um because we don't have to worry about the LLM component um but the sitewide uh AI that's a different story um where I think Teraflow will mostly be involved  
Corneil Clasen: And I think just to add to that, Ran, Mike, for you and Dorte,  
   
 

### 00:14:34

   
Ruan Sunkel: in  
Corneil Clasen: these are some discussions that we we plan to still have with you, but Ran saying there like, yeah, if the if the MCP server for the docs dev portal side or the ll um m.txt txt sits with us like we're happy for that to sit with us like regardless now of scope like we're happy for that to sit with us because those are things that are more in our control and I think obviously the teraflow team is there because they have experience in in in solving the yeah let's call it the kind of the more intrinsic agentic stuff um  
Ruan Sunkel: Yes. And then there's just a last point.  
Corneil Clasen: yeah  
Ruan Sunkel: There's the um we also distinguish between online and uh sorry just give me a second. Um, oh so um developer focus and part of the operational focus is um actually executing actions on behalf of the user um on the production API. Okay. So there's two different ways uh in which it can be used. So Cornell I'm also I'm not exactly certain who's going to take responsibility for because there's an MCP server and it can do one of two things.  
   
 

### 00:15:40

   
Ruan Sunkel: It can consume docs with a dev process or it can actually consume the production APIs or expose the production APIs for an  
Corneil Clasen: Yes. And that that's also an unknown for us kind of Michael is like we we having an MCP server for the docs like that's fairly straightforward um and makes sense to us. Having an MCP server for the actual card acquiring API is something that we are also happy to take on. But it's but that's definitely needs like a deeper conversation because um maybe that's maybe  
Ruan Sunkel: with D.  
Corneil Clasen: yes exactly that's maybe something DT wants to do. They maybe want to expose. I'm not saying they want but might  
Brett StClair: Yeah,  
Corneil Clasen: be  
Brett StClair: George.  
George Westbrook: So I suppose in terms of building the MCP server for access to be it our agent, external agents, blah blah blah. It's ideally we wouldn't want to be building say three different MCP servers that do do the same thing. So maybe one that's for an external, one for say the internal agent that we're building.  
   
 

### 00:16:42

   
George Westbrook: Ideally want it to be usable everywhere. Like one one of the things we did discuss is this for the console is this completely agentic experience where any action a user wants to do they can do it through this interface like they would with claude it's generating components in real time so like let's say there's an aspect of the console where um they're viewing a specific chart it's going to render that in real time so one of the things I think we were we were thinking is in that in that situation and a completely agentic experience ience would how would you see that working? Would it be we we say here you go this is what we think it looks like here you go would you be able to build this or would you be comfortable with going okay look George okay see these requirements you've got to use these these these components make sure it's like this and we're happy for you to branch off make those changes we push them to you for you to approve um maybe make some changes so out of those two ways of working it just take the completely agentic experience because I don't think that's um necessarily been worked in in the in the current designs.  
   
 

### 00:17:49

   
George Westbrook: How how would you potentially see that working? Like what works best for you guys?  
Ruan Sunkel: Cornel, I don't have an answer to that, George. Honestly, I don't I don't know.  
George Westbrook: Okay.  
Ruan Sunkel: Um,  
George Westbrook: Cuz what  
Ruan Sunkel: you talking about the the the console or the development portal specifically because we haven't really um went through the design or discover design for the console just yet.  
George Westbrook: Mhm.  
Ruan Sunkel: Um,  
George Westbrook: It would be more in initially in the context of the the console. Um and I suppose what yeah initially more in the console and then I think way to think of it conceptually is literally as if it was clawed. Um but TXN's claude um where it is generate like generating those components that you've already you're already going to be building um in the actual application um but within the chat UI because I think when we when we were having a chat I think it was last week or the week before it became clear that one of the things is there's different different types of users first being I am somebody I want to be clicking buttons I need it to feel look act exactly the same and in that situation where what we were thinking in um is just we weave AI into it.  
   
 

### 00:19:11

   
George Westbrook: So maybe there's some AI alerts, um, something a bit more proactive. Um, and then maybe a co-pilot on the side that can take a few actions, but it's not a completely agentic experience. And then say user user two is I don't want to click any buttons. I want to speak to my computer and it does everything for me, which is obviously a very very different experience. um which obviously hasn't been incorporated into the designs,  
Ruan Sunkel: Yes.  
George Westbrook: but everything's reusable. Like let's just say take that analytics chart whatever be the same same component maybe resized a bit and all the agent would be doing is it would query the database in the same way that you would when um when a user clicks onto a certain page. However, what happens is the agent decides it's like okay, I identify the user wants to see analytics. Let me execute the analytics tool given some existing state that we've got from the user like the user ID, the date range that they're looking for. they'll make the API call the same as the front end would and then all that happens is I think what the approach we might take is using a a framework or library called agui um which just kind of standardizes this interaction between an agent and a UI and it's really really good when it comes to generating or rendering these generative UI components but all it is is a tool call that the agent makes with with arguments that gets sent to the front end and it  
   
 

### 00:20:43

   
George Westbrook: renders the component  
Corneil Clasen: But do you see that as like if you take the that user journey you explained there? Now, do you see that as the um like let's say that  
George Westbrook: Yeah.  
Corneil Clasen: TXN claude code whatever has access to some skills and it has access to to maybe the the DT  
George Westbrook: Mhm.  
Corneil Clasen: API maybe our front end um back end for front API like we expose all the  
George Westbrook: Mhm.  
Corneil Clasen: data then in theory like that can actually sit anywhere like we're going to we're going to have let it manifest in the console from a from an from from an entry point perspective  
George Westbrook: Mhm.  
Corneil Clasen: but in theory that can sit anywhere it can be a little outlet on someone's desktop for that matter because it has access to all of the  
George Westbrook: Mhm.  
Corneil Clasen: data. Um in your example there do you see it almost like obviously it will end up being some chat interface whether it's voice or  
George Westbrook: Yeah.  
Corneil Clasen: whatever but some chat interface I say cool compile me a dashboard give some parameters  
   
 

### 00:21:29

   
George Westbrook: Yeah.  
Corneil Clasen: what it goes away and it presents back like it actually renders in the UI or it presents back a PDF or what do you think there  
George Westbrook: renders the actual the actual component. Um, and it it cuz I think for us an ide in an ideal world  
Corneil Clasen: Okay.  
George Westbrook: for that kind of completely agentic experience is we build on the foundation that that you guys are building and that the that Super Ultra built, which is these lovely rendered components. Um and then we kind of for lack of a better term copy and paste them um and then  
Corneil Clasen: Yeah.  
George Westbrook: work with the call it aentic UI um and then we we work together but we we might be writing um the code for that that kind of cornered part the one where  
Corneil Clasen: I think. No,  
George Westbrook: I sorry go on is the one where I think it will have to be more let's  
Corneil Clasen: no, no. I  
George Westbrook: say traditional is where it's in the console um there's an alert coming up blah blah So obviously I appreciate if you're if that's that's where you're living that's your bread and butter.  
   
 

### 00:22:38

   
George Westbrook: You don't want don't necessarily want someone like me or Hassan going in. Um I mean if you do that's great. Um but obviously I appreciate that sometimes is isn't isn't  
Corneil Clasen: I think the in that example you have there,  
George Westbrook: ideal.  
Corneil Clasen: George, like do you because for me it's always about the the like something like Claude code makes sense because you're starting from nothing there and you kind of know where you're going whereas what we're what you're pitching there is like we we're starting with all the data but we don't know where we're going like we don't know what we want to want to present.  
George Westbrook: Yeah.  
Corneil Clasen: So would you like do you see the rendered output there like being stateless or does it persist like can  
George Westbrook: Yeah.  
Corneil Clasen: I go in tomorrow and view my dashboard again? Is it like  
George Westbrook: Yeah. So it it would think like say I will just use claude or chat GPT  
Corneil Clasen: how  
George Westbrook: as example. As soon as you click into that chat it's going to it is going to render exactly what it was before with the components.  
   
 

### 00:23:30

   
George Westbrook: Um, I wish I had the example that I think I showed before exactly there. Um, but I don't, so unfortunately. Um,  
Corneil Clasen: But I think I think I can appreciate your example. Let's take let's take it back it back to a simple example like chatt that we all understand.  
George Westbrook: yeah.  
Corneil Clasen: So I'm in there. I ask chat GPT render me a graph.  
George Westbrook: Yeah.  
Corneil Clasen: It's got access to that skill. It's got access in that instance maybe to like Excel sheet with my data. It renders me the graph as a PNG or whatever in there.  
George Westbrook: Mhm.  
Corneil Clasen: What you're suggesting is that it actually uses the components that we're building in the front end.  
George Westbrook: Yeah.  
Corneil Clasen: you then have access to those components um via the um your kind of let's call it your chat context or chat window or or your your your your agent you then render that  
George Westbrook: Yeah.  
Corneil Clasen: and and but like visually does it like if you go back to that chat tomorrow I see that page  
   
 

### 00:24:17

   
George Westbrook: Yeah.  
Corneil Clasen: in my chat and click on it and it it opens up as an HTML rendered page in a big in a in a exploded  
George Westbrook: it. So it would it it would render it in exactly the same way with the React code that you would have somewhere else cuz what the the payload that the agent would give wouldn't wouldn't necessarily be the  
Corneil Clasen: Okay.  
George Westbrook: code. It just be like the arguments for that specific component.  
Corneil Clasen: Yeah.  
George Westbrook: So it look, feel, act, exact like it's clickable.  
Corneil Clasen: Got it.  
George Westbrook: Um like it it potential.  
Corneil Clasen: Got it.  
George Westbrook: Let's just say it's show me my 10 recent card transactions.  
Corneil Clasen: Yeah.  
George Westbrook: Um and then it render that they could click in and then maybe it takes them to a page in the console um for that. So it  
Corneil Clasen: Yeah, I think the um Ron,  
George Westbrook: Yeah.  
Corneil Clasen: you can validate. I think what you what you're pitching there, George, is definitely technically possible. Um I think we can uh um uh if we have a I mean we have we're going to be building the front end component based like you you'll be able to kind of have access to that.  
   
 

### 00:25:13

   
Corneil Clasen: I think there's a lot of technicalities we need to talk through kind of how but maybe it is as simple as you guys building  
George Westbrook: Yeah. Yeah.  
Corneil Clasen: some some form of a skill that has access to the codebase and it uses that to render the components. Um I think it's definitely technically possible. I'm almost like two things there I would almost suggest to you guys not knowing kind of how your commercial relationship with TXN works but like almost like building a PC for that like like obviously all the components aren't ready yet so you can't really do it so you might have to fake some but like like whatever is ready from from DT's perspective um like having I don't know like giving instead of giving it the skill to our components just give it the material UI library as whatever and then and almost try to so so people have something to hold on to. Um,  
George Westbrook: Let me let me let me have a look.  
Corneil Clasen: as an example,  
George Westbrook: See if I can get  
   
 

### 00:25:59

   
Corneil Clasen: and then my other comment, sorry, was was to you, Mike. I think,  
George Westbrook: the  
Corneil Clasen: yeah, you guys need to make a call here and and push us in a direction. I think we're going to we will be able to ideulate for days, but I think you guys need to need to take the driving seat in the decision.  
Michael Moores: Yeah, I think obviously we we're very keen on exploring all possibilities.  
Dorte Dye: It's  
Michael Moores: So you we discussed it length with George and Brett on this as well. I think that you know while still I think plan for the Breton team to to do the AI pieces that we just need scope specifically the touch points are on you know what interaction point I think we're pretty clear on the where we want the push be pushed in and obviously on conversation with the is ongoing with detail will be a data lake this s of analytics will have to be done obviously that's where the AI will will largely feed into. So I think that's a sort of customer in obviously um yes at some point touch the API so the addance and risk level based on what the actions we want to do.  
   
 

### 00:27:18

   
Michael Moores: We will build that sort of more actions if you will from AI versus non still scoping out the specifications we want to do sort of you know in initial phase. essentially yes there will be agent to it as well the knowledge stock is a big part of that as well so the um the self-improvement documentation all all sort of hinges in aim here and obviously just sort of interface with those  
Corneil Clasen: Okay. Yeah. Um, no, that's cool. I I I think we from our perspective, we'll um we'll Yeah, we we'll we'll obviously play ball. We'll do whatever is needed kind of to facilitate that. I think um we are we are going to kind of be in a position myself and design in the next week or so where we're where we'll finalize our understanding in scope and cost etc specifically for the console um and then I think we'll need your guidance there Mike Dorte just to tell us yeah what is what is in and out and what because I think a lot of this is very might be kind of exploratory or might be kind of conceptual at the moment.  
   
 

### 00:28:37

   
Corneil Clasen: So, we're gonna we're going to stick to kind of what we know and exactly what we what we need to do and then um we'll yeah work with you guys on the unknown  
Michael Moores: I think on the on the design  
Corneil Clasen: pieces.  
George Westbrook: Okay.  
Michael Moores: side we're sort of waiting to find out what obviously the sort of trip party. So the design's weighing on conversation with Brett and team know what we can get in from an AI point of view for MVP. We've locked that down design. we can then give you what you need from one and stuff like that. So we have this conversation and we have another one with super just to sort of final the console clearly. Okay, we're focused on this part of the build um for phase one AI will come obviously depends on when George B can get these things in. Would it line up with the MVP dates and stuff like that? Obviously the date pretty much set you can get some AI pieces that be great. Um but otherwise it be sort of a fast follow and stuff like that.  
   
 

### 00:29:42

   
Michael Moores: So um we'll draw that line with culture and then get back  
Corneil Clasen: What's the All right,  
Brett StClair: Hi.  
Michael Moores: to  
Corneil Clasen: go for it.  
Brett StClair: I'm just curious on um your MVP data. I can't remember if my brain's a bit rusty. What are you targeting? What date?  
Dorte Dye: October.  
Michael Moores: it.  
Brett StClair: October.  
Corneil Clasen: Yeah,  
Brett StClair: Okay.  
Corneil Clasen: but you're targeting October for the for for what you need to go to the market with, which is the API and the dev portal,  
Brett StClair: Yeah.  
Michael Moores: Yeah. Yeah.  
Corneil Clasen: right?  
Ruan Sunkel: Yes,  
Michael Moores: So uh you know  
Ruan Sunkel: sir.  
Michael Moores: we are looking at we go shortly after.  
Brett StClair: I  
Michael Moores: So we will have uh um you know months afterwards we would need some for like the first we're targeting for  
Corneil Clasen: Yeah, sorry Mike.  
Michael Moores: console.  
Corneil Clasen: I think um I just lost the important part. So what data are you um going for for the console?  
Michael Moores: So, we're aligning that with the first customer on boarding and I don't know if we've got that as a provisional one  
   
 

### 00:30:51

   
Dorte Dye: Nope. Nope.  
Brett StClair: Oh my  
Dorte Dye: I mean as close to October as best as possible.  
Corneil Clasen: Okay,  
Michael Moores: yet.  
Brett StClair: god.  
Corneil Clasen: cool. Well, um Okay, but cool. I I think we can we can align with you and Ian and Mike on that separately because that that hasn't been communicated to us.  
Dorte Dye: Con  
Corneil Clasen: Like the dev portal always been clear kind of we understand and you guys have our timelines there, but in the console, we'll just need to yeah align on that. Cool. All good. All good. Um yeah,  
Brett StClair: Yeah.  
Corneil Clasen: but I think we're Brett in terms of ways of working to your question right at the beginning like we're yeah fairly flexible and agile. We um especially with um with this project because our typical project is full full stack. So we're kind of from the ground up um then it's then it looks a little bit different in terms of um how how  
Brett StClair: Ow.  
Corneil Clasen: we write run the projects.  
   
 

### 00:31:43

   
Corneil Clasen: But um yeah, in this instance, like we're happy to um to kind of yeah, work with you guys where we need to.  
Brett StClair: Yes. Yes.  
Corneil Clasen: Yeah.  
Brett StClair: Um just thinking again um idea out there just uh George's son. Um yeah, I guess also Canel, I'm floating it to you. Um is maybe we should be doing the instead of us setting up a separate dev environment. You guys already have a a dev environment. maybe we should be building in your dev environment. So that's all in a consolidated consolidated space. Um and when you guys do the move, we're pretty much timing everything with you guys as well. Um Mike,  
Corneil Clasen: Yeah,  
Brett StClair: I  
Corneil Clasen: I think that's I think that's fine conceptually.  
Brett StClair: guess  
Corneil Clasen: I I'm just worried about that at the moment like we we can control exactly the cost there.  
George Westbrook: Come  
Corneil Clasen: Um and that's not a that's not a line item we pass on to to TXn because that's just like we need the Devon to get going.  
   
 

### 00:32:49

   
Corneil Clasen: So I think but I do agree with your strategy.  
Brett StClair: Uh  
Corneil Clasen: So maybe Mike there's a conversation to spin up a Azure environment in TXN's direct control but I know you guys have one in DT so I'm not you 100% sure what's the best but we can give you access and do that I'm  
Brett StClair: kind of I'm worried that you end up,  
Corneil Clasen: just  
Brett StClair: you know, you've got all these different environments that are coming in and then trying to branch everything up,  
Corneil Clasen: yeah  
George Westbrook: on.  
Brett StClair: merge everything might be a bit more tedious if we kind of work with what you've got and like be flexible there. It's just again it's not infringing,  
Corneil Clasen: I think that's That is a good idea. Maybe Mike, we can then discuss with you and Ian if we can if we can pass that dev cost on to you guys and we make make  
Brett StClair: right?  
Corneil Clasen: our lives easier. Um, but you I think that's your  
Michael Moores: Yeah, I think we'll speak to Ian when he gets back on the structure where obviously we've got the the  
   
 

### 00:33:31

   
Corneil Clasen: call.  
Michael Moores: DT still being as well. So, just sort of trying to iron them out from that side of where this thing will will live ultimately. So, uh, one of the back we'll have a good idea of that and we'll push that conversation on  
Brett StClair: Okay.  
Corneil Clasen: Okay,  
Brett StClair: The infrastructure just purely intra sake um VM  
Michael Moores: with  
Corneil Clasen: cool.  
Brett StClair: based uh Kubernetes uh containerized kind of environment. Uh what does the infrastructure look like?  
Corneil Clasen: It's um it's VM based on our side, but I believe DT is running.  
Brett StClair: Okay.  
Ruan Sunkel: Uh,  
Corneil Clasen: Can you recall?  
Brett StClair: Okay.  
Ruan Sunkel: yes, that's  
Brett StClair: Yeah,  
Ruan Sunkel: correct.  
Brett StClair: I can I can picture that being the right call on their side,  
Corneil Clasen: Yeah.  
Brett StClair: right? Hosted on a Kubernetes stack with all the API calls and Yeah.  
Corneil Clasen: Yeah. But in terms of what we would be hosting or Yeah. It will probably be a simple simpler setup. Yeah. Just um  
   
 

### 00:34:37

   
Brett StClair: Okay, perfect. Um, this is really nice, guys. I feel like this will be I mean, it's going to be fun. I can't see too many complexities. I can't I'm feeling quite comfortable. I don't know how about Do you guys have any questions or concerns on your side?  
Corneil Clasen: Lots of questions, but I guess run now.  
Ruan Sunkel: Yeah, we're talking about AI for the for the console. Um, what about AI for the development portal? Um, which is what we're quite busy developing now. Um, yeah. So conneil I I looked at the latest PC now I think most of the AI functionality has been taken out for MVP but with regards to timelines will that be first or will we switch to the console API secondly because that that's a completely different uh style or way in which it's used there versus the developer console sorry the development portal  
Corneil Clasen: Yeah. Yeah. Yeah. there. I think from a kind of a product side, D and Michael need to tell us um what would come first.  
   
 

### 00:35:46

   
Corneil Clasen: But if I had to read between lines, I think we'll probably finish the dev portal, start with the first section of the console, decide if that includes AI or not, maybe come back to some AI portions of de portal. But that's just my gut  
Ruan Sunkel: because I think um with regards to the implementation the what George described um on the console side with  
Corneil Clasen: feel.  
Ruan Sunkel: AGUI that's definitely the most complicated what it will be. Yeah. So I think yeah just from our side we can also just investigate how how that could work um with how we're setting up the application just  
Michael Moores: Yeah, I think from the the portal side, I think we're very much looking at what we do here for the console. So very much knowledge base only for the portal.  
Ruan Sunkel: Um,  
Michael Moores: So obviously searching for that knowledge helping them understand that um existing tickets from uh support case as well. So having that sort of co- pilot view in the portal is all we've sort of um and obviously that'll be big largely part of the console as well.  
   
 

### 00:36:48

   
Michael Moores: um sort of use that same central piece for both um to get that the board obviously will give based on you being a you know public and uh locked in basically  
Corneil Clasen: Okay. Yeah. Then I think I think we're Brit, I know you set up this call. Did you kind of get out of it what you hoped  
Brett StClair: Yeah, I do. Uh, George or something.  
Corneil Clasen: for?  
George Westbrook: Yeah. Yeah.  
Brett StClair: Any other  
George Westbrook: I suppose it's it I suppose all we've got to do in the first few weeks is if we both set our ideals for how we want to work and just make sure we try and work as close to that. It's probably not going to happen. Um but as long as we're singing off the same him sheet in in some respects. Um but I mean like like you said Brett after speaking today it's one of one of my concerns coming in would have been no you have to do it this way and it has to be passed over in this way and we've got this specific way of doing it.  
   
 

### 00:37:46

   
George Westbrook: So it's quite it's quite refreshing that is yeah you're very open as the same same that we  
Ruan Sunkel: Thanks.  
George Westbrook: are  
Corneil Clasen: Oh,  
Brett StClair: I feel like Yeah.  
Corneil Clasen: I'm going to I'm going to remember that singing from the same him  
Brett StClair: Go cover. Well, I was going to say this feels like corporate word bingo talking to him.  
Corneil Clasen: sheet.  
George Westbrook: It's my It's my favorite favorite corporate saying  
Brett StClair: No,  
George Westbrook: the look on disgust on everyone's faces says another  
Corneil Clasen: I I am It is very  
George Westbrook: thing.  
Brett StClair: it's  
Corneil Clasen: consulting.  
George Westbrook: Yeah,  
Corneil Clasen: Yes. Um Okay.  
George Westbrook: I've just got I've just got my book of words to say on a meeting next to me and I thought I'd throw that one  
Corneil Clasen: Awesome.  
George Westbrook: in.  
Corneil Clasen: No. Well done. So getting points for it.  
Brett StClair: Uh well,  
Corneil Clasen: Cool. Yeah.  
Brett StClair: I think we're happy here.  
Corneil Clasen: Thanks for setting up  
Brett StClair: Yeah. Um uh this is going to automatically send out meeting notes and then what we do with all our meetings is we load it into an agentic vault that then processes it, make sure that anything that's been spoken to, action points and agreements gets put into the knowledge base.  
   
 

### 00:38:53

   
Brett StClair: Um and then um we've published those knowledgebased results both to the agentic stack as well as to uh whoever needs it. I  
Corneil Clasen: We would have expected nothing  
Brett StClair: guess  
Corneil Clasen: less.  
Brett StClair: there's there's another corporate word bingo.  
Corneil Clasen: Yeah. Have a good weekend everyone. Good luck with the with the  
Brett StClair: Funny.  
George Westbrook: Can you Can you see this big bottle of water?  
Corneil Clasen: stroke.  
George Westbrook: This is the I've I've got five of them stacked up.  
Corneil Clasen: Good. Good luck.  
Brett StClair: Brilliant.  
Corneil Clasen: Cool. Cheers  
Brett StClair: Anything from daughter Mike? You happy? Happy.  
Corneil Clasen: everyone.  
George Westbrook: Perfect.  
Brett StClair: You're happy if we're all happy,  
Michael Moores: Yeah.  
Dorte Dye: Yeah,  
Michael Moores: Yeah. Thank  
Brett StClair: right?  
Dorte Dye: we we we just need to work out the dependencies, right, when we're comes in because I think that's the hard part with four different parties.  
Michael Moores: you.  
Dorte Dye: Um, we have a session with Supra Ultra on the console next Wednesday.  
   
 

### 00:39:52

   
Dorte Dye: So I've already invited you to nail down all of the discussion ones and then right when we had our  
Liza van Eyssen: What's the angle?  
Dorte Dye: component workflows through then we go down the items so that we can finalize that for super ultra and then it's literally working it backwards right we know when we want to launch  
Brett StClair: Yes.  
Dorte Dye: when needs each part each part how much time do they need what's the latest date to  
Brett StClair: Plug plug.  
Dorte Dye: fulfill all of that stuff so I think there's quite a few dependencies on DT and we need to see where they are with everything so that we can unblock both parts. So that's the magic work that needs to happen. Then later  
Brett StClair: Magic  
Corneil Clasen: Yeah,  
Brett StClair: indeed.  
Dorte Dye: you have your agent that will find all that will kick our ass the German  
Corneil Clasen: sure.  
Dorte Dye: way.  
Ruan Sunkel: run.  
Brett StClair: Beautiful.  
Dorte Dye: Okie dokie.  
Brett StClair: Very good.  
Dorte Dye: Perfect.  
Brett StClair: Awesome.  
George Westbrook: Perfect.  
Dorte Dye: Thank you so much.  
Corneil Clasen: Go.  
Brett StClair: Thank you everybody.  
George Westbrook: Thank you very much.  
Brett StClair: What I have  
   
 

### Transcription ended after 00:41:14

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

**