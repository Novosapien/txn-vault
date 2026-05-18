---
date: 2026-05-13
type: vision-call
scope:
  - "[[vision]]"
status: extracted
extracted-to:
  - "[[vision]]"
  - "[[components]]"
  - "[[index]]"
participants:
  - Ian Johnson (TXN — CEO)
  - Michael Moores (TXN — CTO)
  - Dorte Dye (TXN — COO)
  - Brett StClair (Novosapien — facilitator)
  - George Westbrook (Novosapien)
  - Max Kingaby (Novosapien)
---

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Full TXN product vision extracted across all 8 sections | [[vision]] | Document populated (Draft) |
| Strategic framing: TXN as the **agentic-native** issuer processor | [[vision#1. What Are You Building?]] | One-liner + detailed narrative |
| **Three trust concepts** (co-pilot → agent-advisor → A2A) as the core organising framework | [[vision#1. What Are You Building?]] | Embedded in narrative paragraph 2 |
| **Scope split** — Novosapien delivers AI layer only; Core API, Console, Portal, Data Lake built by other partners | [[vision#Scope boundary]] | Documented (including "Novosapien's delivery scope" delineation) |
| **B2B audience model** — Card Program Operators, Integrators, Client's Agent, TXN Internal Operator (no demographics, no switching triggers per scoping decision) | [[vision#2. Who Are You Building It For?]] | Audience table + unifying non-expert thesis |
| **Differentiation thesis** — agentic-native vs. retrofitted; positional advantage, not defensible moat | [[vision#4. What Makes This Better Than the Alternatives?]] | Documented; competitor research explicitly out of scope for this vault |
| **Pricing/billing scope** — TXN owns commercial; Novosapien needs tier structure visibility for AI surface area | [[vision#5. How Does It Make Money?]] | Documented |
| **6 Novosapien-scope components identified** from the narrative | [[components]] | Components added with `Collecting` status |
| Multi-vendor delivery structure (TXN dev team, third-party designer, third-party portal team, DT) | [[vision#Dependencies]] | Documented; reference materials catalogued in §7 |
| Pre-launch state — no customers, no transaction data; simulation discussed as the early-data substitute | [[vision#7. What Exists Today?]] | Documented |
| AI-layer risk inventory (prompt injection, permission escalation, hallucination, alert fatigue, etc.) | [[vision#8. Risks]] | Novosapien-added; not raised explicitly in the call |
| Gaps consolidated per section for the next conversation | [[vision]] (inline) | Inline "Gaps to raise next call" subsections in §§3, 4, 5, 6, 7, 8 |
| Action: attend Developer Portal final prototype review on Thursday 19 May 2026 | [[vision#7. What Exists Today?]] | Logged |
| Action: request reference materials (Core API docs, Console design prototype docs, Portal site docs, brand guidelines PowerPoint, Michael's AI user-journey designs) | [[vision#7. What Exists Today?]] | Logged |

---

## Transcript

> **Source:** TXN Discovery Workshop — Google Meet recording, 13 May 2026
> **Duration:** 02:10:18

### 00:00:00

   
George Westbrook: Join Max. Is it on? Uh, no. On Google Meet.  
Brett StClair: Oh, I'm going to hop into Teams as well.  
George Westbrook: Okay.  
Brett StClair: Um,  
George Westbrook: I'll send you that document quickly as  
Brett StClair: in case they  
George Westbrook: well.  
Brett StClair: sweet.  
George Westbrook: What' you say, Max? Send you the link.  
Brett StClair: Thank you.  
George Westbrook: Cheers.  
Max Kingaby: I mean,  
George Westbrook: speaking. What' you say?  
Max Kingaby: would you say you speak?  
George Westbrook: Ready to be speaking.  
Max Kingaby: You can  
George Westbrook: You can hear me.  
Max Kingaby: hear  
George Westbrook: Put your If you can put your blur on as well,  
Max Kingaby: as well.  
George Westbrook: please. There you go.  
Max Kingaby: There you go. Don't Don't I'm I'm muted on purpose.  
Dorte Dye: Hi, George. Are we Are we all in different  
George Westbrook: That's Well, that's what we were thinking. So, we've got we've we've got Brett.  
Dorte Dye: meetings?  
George Westbrook: I think his machine's crashed because he's tried joining Teams. One thing.  
   
 

### 00:03:17

   
George Westbrook: Yeah, it's Don't That's the That's the night the nightmare of having different conferencing providers.  
Dorte Dye: Yeah. But you know what? You're providing software services, right?  
George Westbrook: Yeah.  
Dorte Dye: But the worst thing that's always for us is like I'm not working in technology.  
George Westbrook: Well,  
Dorte Dye: I can't make that s***  
George Westbrook: yeah. Well, the thing is we've been we've been indoctrinated by Brett,  
Dorte Dye: work.  
George Westbrook: Mr. Google. Um, morning, Mike. How we doing?  
Michael Moores: Good thing  
George Westbrook: Good, good, good. Don't we were just talking about the uh the woes of trying to do all these different conferencing providers.  
Michael Moores: yourself.  
George Westbrook: I was saying Brett Brett is Mr. Google. So, it's uh anything other than Google is a a no no. But we've we've got stuff set up in the the back end as well off off Google Meet so that it's especially for sessions like these. Um I think he's going to be I think he's going to be about two or three minutes he's just having to  
   
 

### 00:04:16

   
Dorte Dye: So,  
George Westbrook: reboot his machine.  
Dorte Dye: so while we wait for him, what have you set up in the background and how can we copy that?  
George Westbrook: So one of the it's at the moment it's kind of like a really raw automation um or not automation but so basic what we have is given a meeting um the transcript will be sent to an AI agent or an agent team which is going to look at all of the different meeting types that we've defined look at all of the different potential clients that we've got and existing clients then it's going to analyze the transcripts bucket it into the the types of  
Dorte Dye: Okay.  
George Westbrook: calls as well and then just spit out what what we need. Um, so for more sessions like this, um, there's more of a structured way of extracting stuff, but obviously sometimes it's you're just having a call, a 15-minute call to catch up with somebody and then those ones those ones get ignored.  
Dorte Dye: Yeah. Yeah. Interesting.  
George Westbrook: Um,  
Dorte Dye: So, it's not the note taker as such.  
   
 

### 00:05:13

   
Dorte Dye: It's basically more for what you're taking out of the meetings when you have scoping meetings to follow through.  
George Westbrook: yeah. Yeah.  
Dorte Dye: Okay.  
George Westbrook: because it one of the things we're working especially for like our standups as well um is obviously we've got we've got backlogs in in linear and things like that which need updating. I'd be a liar if I said we're doing this at the moment um but it's in our things to build where it's just automatically updating the statuses. So, if we talk about the the the bezels on the edge of a  
Dorte Dye: Nice.  
George Westbrook: button on one thing we're building, it's going to go in, it's going to find the linear issue, it's going to update it and maybe add some notes as well. Um, because the is the the issue we've got is it's it it's very weird. Everything we do, we have to position it for both humans, but also AI agents. So obviously if we if we have a if we have a call me me Max um Brett and the rest of the team um we can remember it um but obviously an AI agent that might be working on one part of a certain application it's not going to have any any any idea  
   
 

### 00:06:18

   
Dorte Dye: Yep. That's a good picture. Yep.  
George Westbrook: um so it is it is quite funny trying to make technology choices whereas before it's like what is the most user friendly now it's like how easy is it to get it into markdown or HTML so uh so an AIA agent can uh can utilize it.  
Dorte Dye: lots to learn. Mike is quite good with automating all the s*** out of his stuff. It's like it's crazy. It's like he's doing one thing and then he's updating 10,000 documents where it's cross reference and all of that stuff. And it's like, okay, I'm still in the totally early days of adopting. It's like, how do I get better at  
George Westbrook: Well, I I find the biggest bottleneck now is how many how many monitors I can fit on fit on a  
Dorte Dye: that?  
George Westbrook: desk. It's like I don't want to be that guy who's got like four monitors, but I'm I'm sat here with two decent sized ones at the moment and I'm thinking, is this enough?  
   
 

### 00:07:14

   
George Westbrook: I don't know if I've got enough  
Dorte Dye: How's your brain working?  
George Westbrook: space.  
Dorte Dye: It's like you can't look at all of the screens at the same time anyway. So, it's like you can just flick screens  
George Westbrook: I It's maybe a bit of bit bit of ADHD,  
Dorte Dye: 360.  
Brett StClair: It's  
George Westbrook: but that's what I need.  
Brett StClair: great.  
George Westbrook: I need a 360 death so I can just spin around and  
Dorte Dye: Yeah. But then you're like in the cartoons where they're all minions and they don't know what's happening anymore because  
George Westbrook: uh  
Dorte Dye: it's like you're in your artificial world and you fall off the cliff.  
George Westbrook: Yeah, VR headsets. That might be the  
Brett StClair: Sorry I'm late, guys.  
George Westbrook: thing.  
Brett StClair: My machine decided to go goodbye as I dialed in to Teams and it just  
Dorte Dye: I just told George it gives us all the confidence that we have chosen you as a technology  
Brett StClair: went  
Dorte Dye: provider.  
George Westbrook: It's It's hilarious how many times it happens where we're on a call and it always seems to be like the first big important call.  
   
 

### 00:08:10

   
George Westbrook: It's like, "Yeah, sorry. We promise. We promise we do no technology. I know we can't get a meeting thing to work,  
Brett StClair: Have a good  
Dorte Dye: We will knock something off that invoice now.  
Brett StClair: day.  
George Westbrook: but  
Dorte Dye: Um Ian will join a little bit later. He's just over running in another meeting. So I would say let's kickstart this one because I think you have a lot with us um planned. Um yeah.  
Brett StClair: Yeah. So, let me explain to you how we going to make this work. There's some slight differences in how we are going to approach this. Um, so it's a two week period. Um, we essentially use a Gentic AI to help power us to make sure that we map out a knowledge graph so that we're not missing anything. And then we power everything through conversation. And so we're just going to be talking to you and asking you further and further questions. And we break it up into a couple of core kind of hierarchal layers.  
   
 

### 00:09:17

   
Brett StClair: And the point of doing this is it helps our teams understand where the gaps are. It also helps us understand where we have dependencies. Hence the knowledge graph kind of ties everything together. an example how we stitch this together. Um, and thank you for coming over to the Google Teams environment. So, we've just set everything up. So, it goes from this recording. We extract the right kind of data detail. We then run it through our processes. It takes a couple of days and we're doing reviews and we're pulling everything together, but it does the right analysis. Um, and then we start publishing it. And we start publishing it on a on a portal that we're going to give you guys access to. And again, that portal allows you to provide review comments. Have we correctly understood? Are there questions that we still have that we're unsure of? Um, but it literally allows a bit of a review kind of phase and then um, uh, like a decision kind of point.  
   
 

### 00:10:25

   
Brett StClair: So if one person's going to make a final decision, who is that? They can see what's been made and they can give a signal. Then off we go. We start packaging everything out. Um it's pretty eloquent when you get it going. Um so we start off with a bunch of workshops. So we start off with this vision workshop. Um it could be an hour, could be two hours. Um we have one little bit concern. We usually address everything, but the design teams already had done a whole lot. So, we're pulling out the core components um of the design and starting to bring this into this knowledge graph so it can better understand everything. Um so, there's a slight nuance there that we're just going to have to figure out as we talk through it. We've got our guidelines on how we take the conversation. At the end of it, we draw up a vision statement that we should have ready by the end of this week. Um, from there, we look at components.  
   
 

### 00:11:27

   
Brett StClair: Um, each of those, we try to break each kind of function, form, feature into a highlevel set of components. Terrible, terrible kind of analogy because as we go, you'll start to see how the components come together. Um from the components we then go publish those as well. So we'll do component workshops. So we might have three, might have four, we might have five, we might have six. Um they're usually anything from half an hour to an hour. It's very disciplined. We smash through it very quickly. the it's really to try to get all three of your brains plus all the design team discovery work pull it all out um present it back that we've understood it and how AI is going to play a role it comes up with recommendations and then we've got a great base a backlog set of requirements that we can build from as we go through that we look at the architectural requirements the infrastructure that's going to be required all those kind of components and we pull it together and we're able to start figuring out what components need to be built.  
   
 

### 00:12:40

   
Brett StClair: How are we going to build them? How are we going to deploy them? How it fits into your user experience. It's kind of this layered approach. We get to a phase that's called subcomponents where we really look at it and we go okay now we're going to and think of it as like microservices. You kind of got your core feature and the subcomponents. That's really getting into a bit of detail. We'll do that part based on what we've understood from everything and then we present back to you guys that then at the end of the process you'll have an incredibly welldefined approach to how you're going to use generative and agentic AI in your space how we are going to build it how we're going to deploy it how we're going to design it etc any questions  
Michael Moores: I was listening to you.  
Brett StClair: Um, George, sorry, my machine's all crashed, so Obsidian's dead, all that kind of stuff. you want to quickly whip up and just walk through an internal product, not a custom one.  
   
 

### 00:13:47

   
George Westbrook: Mhm.  
Brett StClair: Maybe um uh content workforce just just so you can get a  
George Westbrook: Yeah.  
Brett StClair: sense of what we're going to try aim for. So, um, you're not kind of talking with absolutely zero idea. You can see what we're heading towards. Um, and then we'll publish it. By the way, do you have brand and CI guidelines yet or can we draw that  
George Westbrook: Reloading.  
Brett StClair: from the designs that you've got at the  
Dorte Dye: I have a very slim PowerPoint presentation program guidelines I can share  
Brett StClair: moment?  
Dorte Dye: over  
Brett StClair: Thank you. We'll just build your portal,  
Dorte Dye: here.  
Brett StClair: review portal and kind of console um with your brand guidelines as well. Just feels a little bit more like home. Um and George, let's just quickly walk through kind of what some example components look like, the visions that we try to achieve, and then a quick the knowledge graph looks sexy. It really is for our Gentare and our own purposes to try to figure out dependencies and what's missing.  
   
 

### 00:14:56

   
Brett StClair: And we're building this. This is your long-term knowledge repository. And you know, we're in a world where suddenly knowledge graphs actually quite easy to do in the past. I don't know how many knowledge graphs you've had to try and build. Nightmare. It really is painful to do it manually. But this technology allows you to do it. You might need to zoom in a bit.  
George Westbrook: There we go. Is that all right for everyone?  
Brett StClair: George  
Michael Moores: Have  
George Westbrook: Yeah. So,  
Dorte Dye: Yep.  
George Westbrook: all all it really is is it core is just a a set of markdown files.  
Michael Moores: fun.  
George Westbrook: Um but we've got a very structured process for codifying the vision. It might feel sometimes we're going one step back maybe talking about things that we've already talked about but the main reason for this is just so that we make sure that our our understanding of what what you want and what you actually want is aligned as close as possible.  
   
 

### 00:15:54

   
George Westbrook: Um like we said everything we do is both for us and for the agents. Um because like we said numerous calls we might have had we think we've got an idea in our head but we really need to codify and get that down. Um so like Brett said with the with the components once again that's a bit more bit more high level and then when it gets to the subcomponents that's where we break it down into like data requirements um user journeys the acceptance criteria for for that so that we can build out the testing criteria as well for the agents. Um, so this this is yeah an example. I think Mike you might recognize this is Obsidian. It's just just a way for viewing these notes. Um, so what we really start to do is for each each component, break it down into its subcomponents, get these really really really fleshed out and agreed upon so that we've got that base to push off when we're when we're developing. It's not a static document.  
   
 

### 00:16:50

   
George Westbrook: Um it's it's it's something that's going to be ever evolving. Um it might change a lot for some components or subcomponents. For others it might not change. Um but the idea will be that we can build out this this knowledge graph here which just allows for both us and the agents to really navigate down to it. So we're building up the the context bank for both us and the agents. So whenever there's something that needs to be worked on, um it knows exactly what it's doing and exactly how to do it. Um part of this is for the initial development process, but also the ongoing developing process and also what we like to call like the self self-healing aspect. So say for example in in production um there's there's a bug setup sentry tracking that error then gets sent to a an agent that's running in a virtual machine which will then navigate this navigate this to find out the exact component what should be happening what's the acceptance criteria why is it why is it failing create a PR which we will then review um and then it just allows us to get that velocity But also for during the development process, let's say there's a piece of feedback for um that you guys have got for um one of the journeys that the agent is taking.  
   
 

### 00:18:17

   
George Westbrook: So one of the things we like to do is build in Have I got a good example? Um, so yeah, let's say the agent agents output wasn't exactly what was needed or a tool call was malformed or the popup for a notification um that the AI is done is is not where it is in the development deployment or the the UAT deployment, there'd be maybe a little button in the bottom corner, take a snapshot of the state of the page, the state of the agent, the timestamps, so that when that feedback's submitted, Um, same thing. It's going to go to an agent. An agent's going to investigate. It's going to look at the changes. We'll sit down. We'll debate with the agent. Okay, let's make this change. Blah blah blah. The wording was too formal or it was too informal. Let's look and identify. Once again, look through the knowledge graph, navigate to the right component, the right subcomponent, what should be happening, what shouldn't be happening. Um it just helps us to keep the velocity a lot a lot higher than obviously waterfall which is define all up front um and build to that and even agile like two week two weeks now is quite quite a long time um  
   
 

### 00:19:30

   
Dorte Dye: Sorry, I have to bringing I'll back in a  
George Westbrook: and  
Dorte Dye: second.  
George Westbrook: but but yes so I suppose Brett is there anything else you think worth going in with with this aspect?  
Brett StClair: Um maybe just a quick touch maybe pull up one of the clients uh portals.  
Dorte Dye: to be another  
Brett StClair: Um trying to think who's probably most suitable.  
George Westbrook: Yeah,  
Brett StClair: Probably someone in the US.  
Dorte Dye: one.  
Brett StClair: Um  
George Westbrook: potentially we could bring up the content workforce one.  
Brett StClair: content reforce. Yeah.  
George Westbrook: Let me have a look. You got I think you can hear a bit of the music in the background,  
Brett StClair: Hold on.  
George Westbrook: Brett.  
Brett StClair: Let me see if I can put the filters on.  
Dorte Dye: Sorry.  
George Westbrook: Right.  
Brett StClair: That's probably better. Push and hold.  
George Westbrook: Yeah, that's that's a bit better. Um, so if I share my screen here, so this is this is an internal application. So it's not as not as polished as um some of the other aspects.  
   
 

### 00:21:00

   
George Westbrook: Um but yeah, so as simple as just a button down here, enter in a bit of feedback. Um, the coloring of the cards is not what I would like. And then it's going to submit that there. And then we'll go to this kind of admin panel that we'll build out. Um, so pop into the user feedback. It's going to have a screenshot. It's going to have some aspects of the state of the page as well, which we can then easily get into fix any issues. So, let's say this issue, diagnose it, and then what it's going to do is it's going to send us a message on Slack that is starting to diagnose the issue. Um, and then where is this one? Yeah, it's going to start diagnosing the issue. receive the message, have a communi, have a conversation on Slack. Once we're happy with the diagnosis, then click fix now, it's going to create the PR and pull it in. Um, with UI, more UI focused ones, there will be one of the things we like to do in certain deployments is you click the feedback, take a screenshot, and then you can select the specific components on the page, add feedback to that specific component.  
   
 

### 00:22:33

   
George Westbrook: Let's say it's a a chat bubble or the actual chat, add specific components there, uh specific feedback there, draw around it, add shapes, things like that. It's just we like a like I keep on saying, we want to keep the velocity of the changes up. So, it's not those two week sprint reviews where it's we're having a conversation one day, two weeks later we see the change. It's two weeks is a lot of time. that can be made in in in that amount of time.  
Brett StClair: So you guys are starting a journey with us where this world of authentic AI and Gen  
Dorte Dye: What?  
Brett StClair: AI has changed everything right the ways of work the approach the release cycles the testing the Q&A and so we're starting starting the process with the ability to capture the requirements um I think it's fair to jump into it the first we're going to ask a bunch of questions we're doing this mainly for the purpose of gathering the knowledge base. So you're going to feel we've already told you some of this but we're just going to ask it again so that we can get it into the system.  
   
 

### 00:23:44

   
Brett StClair: Um and then there's going to be a whole lot of stuff that we're going to take you down different routes to get a deeper understanding. Are you all fine with that? Happy days. So very very first question um tell us about the  
Dorte Dye: Yep.  
Brett StClair: entire platform and key pain points that you're looking to solve in the market and why you are going after those pain points and what you're looking to and the solution you're going to provide in the market. and just do an overview of that.  
Michael Moores: Yeah, absolutely. I think it's starting at the individual components and platforms we're offering. So, um obviously Tix will be providing the the core API of an API first offering. So, that's where we'll do sort of all the card issuing and that's the instance we sort of provide to our customers. Um so that's sort of a standard issuer processing sort of API with a small few tweaks in inside that that we sort of manage on the pain points which I'll come to in a minute.  
   
 

### 00:24:53

   
Michael Moores: Um sort of to accompany that we have the what we call in the TXN console. So this is sort of the um admin uh panel if you will where once you're a client with TXN you will have access to the console where you can sort of manage and administer your program. So this will very much connect to the existing APIs that that we we sell and we have the benefit of doing this and why we're sort of providing a console for this was especially in previous companies you'd have to build out to the APIs to do standard simple um you know operating functionality. So whilst we have the APIs for everything we have sort of made the APIs you probably use once a year if you're changing a product or a look of a card. we've pushed that all into the console. So basically that you don't have to build that and spend time building that. Obviously allowing you to get to market quicker. So that's the sort of main focus for the console making sure we wrap up that core um program management side of it.  
   
 

### 00:25:52

   
Michael Moores: Now the console is sort of multi-use. We do have uh whilst we are an issue of processor and not sort of pure core banking we do have like a customer service sense as well. So in there you can look at card holders you can issue new cards that sort of sense as well. very much split views from what an admin would do versus that. Um, so this is all managed by what we're calling sort of granular permissions. So every element on the screen has a permission. So can you suspend a card versus terminate a card? So you can actually build this um permission layer up. So essentially you can have very custom roles. Um, you know, we have sort of different. So for example, TXN will be very fixed. We know what we want inside our company. So we'll be sort of assigned to individual roles. Whereas for our client, we're letting them create those custom roles themselves. So if they do have someone that does a bit of program program admin and also a bit of customer service, they can build those custom roles based on lessons learned that roles aren't always defined the same in different companies.  
   
 

### 00:26:48

   
Michael Moores: So that's where that sort of granular come from. Um and that's all building that up as well. So that's where sort of the AI we want to touch there. So obviously main thing there for that is sort of navigational helping them go through that. So the main aim between the AI and the console is to reduce tickets into what would be my team. So you know with previous companies we had a lot of tickets saying where do I get this how do I do that you know it's either in the documentation or it's there as well. So sort of putting those sort of friction points to help them in to say you know have you looked at this are you sure to really avoid the question. So that's the the biggest pain but it was the unnecessary tickets u we were getting. So obviously that's sort of multi-pronged how we solve that AI the console and good documentation are the three sort of solutions we've come up with to sort of each are individual barriers ideally the documentation would take all of that away but then we also got the console and AI there to support just in case we can answer one of the things we are keen on is again self-learning so making sure the documentation doesn't go out of date um we have every time we deploy the the API we have a YAML file that you know  
   
 

### 00:27:56

   
Michael Moores: gives us the latest API references. Um, and all that is sort of packaged into what we're calling the developer portal. So, we see this a sort of one long journey which I'll come to in a second. The portal is ultimately uh a sales tool as well as an integration tool. So, it's very much open to the public as as current design stands. It'll have our API reference on there. So you can look at every time an API is deployed, you'll have the latest and greatest API specs there all rendered into that sort of in live. Basically, we have a CRM in our developer portal that's going to basically allow us to write custom documentation. So whilst the API reference is there, we may want to write a custom documentation for if you're doing a specific, you know, card like CL or something like that or a specific use case, we may go end to end as well. So allows us to provide a little bit more business type documentation on top rather than just pure code and API as well.  
   
 

### 00:28:54

   
Michael Moores: So they'll be sort of manually at the moment manually written. Our hope there is that with the ticketing system, the documentation and the AI, you can then start continually updating that documentation and you know if it does get through to me and I manage to answer the question, it will learn and then feed that back in and ultimately keep reducing those tickets as well. So that's the the central aim and one thing we're not really focused on too much right now is is a corporate website which is a separate site to our our website essentially the marketing side as well. We will be looking at some sort of AI to help them there but obviously different context based on where you are. So very much the corporate website would be you know are you a good fit for me?  
Dorte Dye: Okay.  
Michael Moores: Can I partner with you? That sort of thing. Whereas the developer port is more you know how do I actually integrate with you? Can I do this in your platform? And obviously when you get right to the TXM console it'll be more okay now go and do these things for me.  
   
 

### 00:29:48

   
Michael Moores: So we have sort of different context based on where you are in your sales journey if you will. Um and obviously we can provide more guidance as well. So for example in the TXN console one of the things we're sort of planning there is um analytics as well. So not only just from your own program but this is what other people tend to do in your same situation. So if you're in the lending space or whatever space we can go you know five of our programs do this. we recommend you doing all this thing as well. Um that's sort of how it evolves over the three sort of platforms if you will. Um and that's the sort of core uh for me the core features we're doing and obviously the main sort of injection point for the AI would be initially helping and navigating as well. Obviously with um payments and AI there's a little bit of a higher risk there. So we obviously I think we discussed in our first meeting about the risk tolerance and stuff like that.  
   
 

### 00:30:43

   
Michael Moores: So we need to understand what our risk tolerances are but I think this is why our API sort of split into something that can affect an entire program versus something that affect one card. So naturally you probably start there okay terminate this card help me find this transaction those sort of things as well and then we can build up to more larger recommendations. So I think one of the big ones on the console is the onboarding flow. And now that's something that would probably take a good couple of weeks with one of us. Whereas ultimately, especially at the previous companies, you're not that special of a company. You're going to do you've already done it before. That's what we tend to see. Everyone thinks they've got a really good idea, but ultimately under the back end, it's the same structure in an issue of processes. So it's one of the maybe four variants we would do. So it's quite easy to get that understanding again as it evolves with AI and people change. what sort of spend controls get applied on uh travel rewards program and say you know this is what most people do for travel you want to apply them so sort of pushing recommendations rather than not enforcing so ultimately we offer a solution that allows them to be compliant but  
   
 

### 00:31:52

   
Michael Moores: we are not responsible for the compliance so if there's something they should do in the UK for example we'll push that much more heavier but ultimately it's up to them to say yes I want this so that's what the sort of on boarding flow will do is sort of push that in you know, we've noticed you're in the UK, you should do this, this, and this. Um, do you want to accept them? It sort of builds that journey up for them. I think you saw some of the screens of the consoles as well, sort of pushing that advice and helping sort of set that up. Now, especially when you come to sort of a card product, there's maybe 50 or 60 properties in that um JSON object. So, it's very detailed, but ultimately, you know, if I want one functionality, there may be sort of six properties to configure that and how it works basically. So sort of distilling that down into I need to turn X and a few sort of really key easy questions to understand and that's the biggest thing from previous places is that yes we have all these properties but unless you know what they mean and understand truly what they do in terms of the business sense people turn them on and off and and they can break things.  
   
 

### 00:32:52

   
Michael Moores: So especially with AI and making banking easier we get more and more people through that just really don't understand banking or transactional stuff. So that's the sort of people we're trying to target there. If you don't have that um expert knowledge, we can help and provide our own guidance to support you through that sort of journey basically. So that's the the very high level overview of where we are and obviously um in addition to this I've got sort of user journey specific user journeys on some of the AI stuff I think we shared earlier that we can resend as well that sort of hopefully build the you know what we've thought about and again we're very open to your ideas and where we can interject that but essentially that's where we are and obviously the more data we get the more powerful it becomes. So obviously we can start doing fraud and anomaly checks and stuff like that. So that's a sort of later on down the line as we build that up, we want to sort of provide that sort of basis to offer those analytics and those fraud and stuff like that.  
   
 

### 00:33:57

   
Brett StClair: So I'm hoping as we also go through this you'll see some of the powers of what the authentic role can do especially around documentation around how to manage support cues more effectively um how to do the analysis how we can support on the co-pilots manage that complexity so it's super simple um so our goal is to kind of Show you while we get to that point what this technology can do as well.  
Dorte Dye: I think what I would be interested in to see it's a it's a scaling process right it's like we need to have the first customers to collect the data how do we can accelerate that process to show more if there's a way around it I think a lot of companies will have probably the same challenge right particular when they're starting of how do we make um the best use of AI and simulating ing things if we can ex uh pull external data or something for the comparison. I don't know it will be just interesting to see your ideas how we can bridge that gap because it will take a while till we get the first few customers and then it's again how reliable it is when we just have two customers to give a comparison.  
   
 

### 00:35:08

   
Dorte Dye: You have one in one sector and one in the other. The goal is very clear what we want to do but for that we need to really have the data.  
George Westbrook: And when you say when you say simulate, could you could you give me more bit more context where around you see like what what would you simulate? How would you want  
Dorte Dye: I'm I'm I'm just wondering Mike if there's some way or form that we can get data from from the card  
George Westbrook: to  
Dorte Dye: schemes or I don't know I'm just playing where where we could acquire data to to get to that level.  
Michael Moores: Yeah, I think transaction dates will be sort of the more difficult one and that's something that will grow in time. I think there's obviously to more to the documentation. I know Ian raised one about can we simulate some sort of test tickets, you know, actually evaluate them. So, okay, ask the question, can I answer this? No. And then sort of that self-learning. without the tickets in that system can we bump through let's say a hundred okay I can't answer that  
   
 

### 00:36:00

   
George Westbrook: No.  
Michael Moores: then list the ones it can't answer so we go okay right I need to back fill this so I think that's one Ian  
George Westbrook: Yeah.  
Michael Moores: had I think yeah with transactional data obviously the the fraud junk data is we have to try and get hold of for you so there's that's something that builds up in time so one is features we are looking at later is you know we don't know it's fraud so we have to be told if it's fraud so that build that that's sort of sort of phase two for  
George Westbrook: Yeah.  
Michael Moores: our API sort of yeah this is fraud but then look at decline rates um how often they get disputed and stuff like that. So you can really build this portfolio about okay this is likely happening. Obviously you've got anomaly detection.  
George Westbrook: Yeah.  
Michael Moores: So the standard rules for if it's a small transaction then a large. There are some sort of key rules we can we can spot. Obviously we're not fraud experts there. Um but I think that's why we rely on the data to tell us the story for now and then what do is sort of we're obviously not going to provide a complete fraud solution but we're going to provide something to say I think this may be fraud or you may need extra care.  
   
 

### 00:37:05

   
Michael Moores: So we pass all that over to our customer because ultimately one of the most important or one of the most core  
George Westbrook: Yeah.  
Michael Moores: flows is that we will and bringing the transaction with Visa. We will give that it to them and say would you like to approve? So the the sort of keys set up we're doing for MVP is that we don't have the balance. So we literally go out to them and say can we approve this on your behalf but in as part of that we'll go okay here's what we thought it's it's been secured by X Y and Zed. Um you know their card is not suspended. um we don't think it's a suspicious merchant. You know, those sort of things we can pass over to them. You know, they can do sort of hard declines. We will offer sort of a a fraud engine that says if it's these conditions, then block. That's a sort of level at the moment we're looking to do is these rules. But from that, we can then with the air go, okay, we've noticed you've got this rule.  
   
 

### 00:37:56

   
Michael Moores: Consider adding this merchant to this rule because of these reasons. And then obviously we can add that support there to to help them on their way. they will have the fraud expo expert. We're just sort of assisting with we've seen this in the data, you may want to consider that's a sort of angle we're coming at to start with and obviously until we get that fraud expert on our side and can actually do that. We will rely on them sort of telling us it's fraud and building our model up from that. Um I think that's the sort of core there and his point is you know where we can get some sort of transactional data to feed it you know x00iles and transactions to start with because I know the models take a while to build up on the transactional data itself. So going to need quite a few transaction but we could look at potentially getting some you know good transaction data possible fraud data from I'm not sure what visa can provide us but we can look at providing that sort of sample set data to at least start the training uh initial training and then from our own data obviously we will that will come as and when we can we can get that through basically Yes.  
   
 

### 00:39:02

   
George Westbrook: I think I I think one it's it's an example of something we build about like the power of simulation. So it's it's it's not a similar issue. Um it's one of the things we're building is kind of like a a saleserson. So something that does phone calls, emails, LinkedIn messages and things like that. So one of one of the challenges we had is obviously testing it. You don't want to test that in the in the real world if it's not polished. So one of the things that we will do is build up say personas of potential leads um and then different user journeys. So let's say we have a hundred personas each with maybe three different user journeys. And then what we do before before we released it is we will run thousands of simulations. So there'll be one agent which is acting as the customer and then the agent team which is acting as the saleserson and then we'll just run all of those tests in parallel. We'll see what should have happened, what actually happened, get the delta, work out where in the system that error occurred um and then use that as the feedback loop.  
   
 

### 00:40:07

   
George Westbrook: So say for support ex for example, we could look at the documentation um and we could build up a hundred different um hundred different support people that are requiring support. Get them to have different user journeys for the things that they're asking. Um some that are going to be there so that we're testing if the information is there. Is it going to answer it correctly? Is it the right tone? Is it saying the correct things? Is it hallucinating? Is it grounded in truth? And then also things that that aren't there. Testing is it making up the answers? Things like that. And then some in between where it knows some things, it doesn't know others. So that really we can like you said simulate all of this before and even work out where the gaps are in the the documentation or support process. So I suppose that's that that's before. Um, I think one of one of the things with situations like this, so with support for example,  
   
 

### 00:41:01

   
Michael Moores: Okay.  
George Westbrook: I think I talked about it uh last time, is obviously the last thing you the ideal world is zero tickets on your desk. In reality, initially that's probably not going to be the case. Um, because like you said, we're not going to have the data set. But as over time, what we can do is start to build out these defense layers. So let's say the agent in the console is not able to um not able to answer it then it gets handed over to h the next the next level of support have another agent team which is maybe pre-analyzing it so that when it does come across your desk it's half solved and the amount of cognitive effort you've got to put in  
Michael Moores: Yeah.  
George Westbrook: is there and then like you said that's now been answered. It then goes to the documentation. Let's let's just say yeah. So it maybe updates the the YAML file or the text on that, creates the PR for you. You just review it, go, "Yep, that is the answer. This is what I've said to the client and it's done." I mean,  
   
 

### 00:42:04

   
George Westbrook: that process could be half an hour, an hour. Um, and then if we add more layers of support into that, um, it's going to be that maybe out of that 100% of the tickets that were coming across your desk in a couple of months time could only be 10%. Um, so I'm trying one of the things I'm trying to think is where where are these buckets or modules um that it could be and I think obviously support support is a big one. That's maybe more of a there's I suppose the front end support the user in the console asking a question they've got an issue how can we solve that effectively then the more kind of backend more um internal ones that like those lines of support um then I suppose there's from what you've said obviously the onboarding one of one of the things we need to work out is what what actions would we want the agent to take and what actions would we not want the agent to take um or the agents to take um and I suppose that's just a trust process over time because in theory it could do the onboarding end to end take all of the actions for the users any sensitive actions make sure that it's got explicit approval from the user and maybe even based on different user access levels they can they can do more with the with the agent Um, yeah.  
   
 

### 00:43:35

   
George Westbrook: So, I suppose what's  
Brett StClair: Can can we spend a bit of time on the developer portals because that'll be your core kind  
George Westbrook: what's  
Brett StClair: of focus. Um what has been built out already? Um how are the developers working with you? Where are some of the pain points that sit around there? Um, and let's go a little bit more detail about how the AI components can support the developers and better. I guess let's thrash that out a little bit more. Is is that okay? You guys fine with that?  
Michael Moores: Yeah.  
Brett StClair: Thank you.  
Michael Moores: So the portal started development this week pretty much. So very early early stages sort of concept building the pipelines and stuff like that. So that's being done with a third party. All the requirements are very clear. We are just sort of finishing off. I think you're invited to a session with the portal d I think as well aren't they? So I think there's a final playback for the portal and basically we're almost in sort of what they call MVP phase.  
   
 

### 00:44:42

   
Michael Moores: So we've got the full prototype now. We'll be narrowing it down to what the MVP will look like. So um we're pretty clear on the design and the developer portal dev team. They're building basically the the background the stuff like that. We just saw the external CMS that we're using. So we're using something called Umbraco uh which we sort of are allow us to sort of put the manual documentation in there as well. So we're sort of pulling the the components together for now. That's sort of the current situation where we are. Yeah, the design and the direction is pretty clear. We have sort of gone with a portal as a one-stop like MVP is the sort of only planned phase for now. It's everything we want. the only consideration will be the AI piece. So that's they may do additional work to allow you to you know plug in the AI basically. So that's the only um the piece we're looking at at the moment that may extend that development a little bit further based on you know the progress of this uh project.  
   
 

### 00:45:47

   
Brett StClair: And thinking around the AI components you're having is around supporting answering question knowledge base kind of access for the developers Right.  
Michael Moores: Yeah. Yeah. So all public. So um the main interaction with the the user would be uh through a sort of chatbot type support thing. Um we have the ability to submit feedback. So if they do spot um a bug or and you know even just a product improvement that's quite a core component because again there's different teams behind it. So we need to be able to split the the sales team from sort of the product enhancement bug team to the actual technical support team. So that's sort of the way we kind of split that up. So we have sort of specific support that we discussed briefly. That will be the same process where it's in the portal or the console that's just going to go through the same AI, the same um discovery layer into ultimately my team if you know we can't support that. And then the bug and sort of product feature enhancements will take sort of context about where you are as well.  
   
 

### 00:46:52

   
Michael Moores: So if you're looking at some documentation that says I don't like this, it'll take all that context of the screen and push that into a separate queue obviously probably split the product enhancements and bugs separately because obviously timelines will be different for each of them. So product enhancements they can raise doesn't mean we're going to do them necessarily. It's something you know we won't do that if just one customer asks but if there's three or four we may go okay this is a feature that we probably should do whereas books is specifically wrong.  
George Westbrook: Uhoh.  
Michael Moores: So they have put tighter timelines and you know we will actually do something about them. It's just about whereas a product enhancement needs a full review and sort of do we actually want to do this as a a product enhancements for the API. Obviously depends on the size of it and stuff like that. Um so that's ultimately guiding them through. So it's very simple um and I say we can we can show you the the prototype but very simple sort of view.  
   
 

### 00:47:47

   
Michael Moores: you've got sort of a little bit of a overlap to marketing. So, it's very much sort of a landing page for targeted at developers, still marketing, still showing what we can do. Um, showing what we offer in terms of integrations. Then, we do have uh guides, uh, API reference and change log. They're the three core sections. um guides and change logs will very much be uh well manual to start with but hopefully AI driven to publish those but obviously guides are the lengthy guys that we want to publish ourselves and change just are um our release is basically what we've changed what's coming naturally we it's some sort of manipulation from developer notes to fully English understanding release notes um so that's something we will do that as a manual step for now is because the release notes we get from be um you know documentation ready so there'll be some sort of process there make sure they go out the thing as well um and obviously the API referencing um automated and ra so they're building the API they're giving it back to want and the portal will manage s multiple versions So there's a period of time where um the new version might not be the production version public sandbox so they can publicly might not have that latest version.  
   
 

### 00:49:21

   
Michael Moores: So there that's all we anticipate showing just those as we roll it out obviously we'll go back just to the sort of one but um sort of sandbox this will be reference comes into it so we actually have like a try out so you know here's the API reference this data comes back that's where the public sandbox comes into play there they get it working without having to sign up that's sort number one and then you have loads of responses and stuff like that in there. So they can actually see how it works. they can download the relevant code they want and just integration and and get those quick tests done. That's a sort of basically the three core of that portal. There's a few other pages more marketing and all but essentially that's the three core components of the portal and then the AI will sit over the information I need and that sort of thing as well. Uh from that point.  
Brett StClair: kind of feel like I want to we should show you a little bit about how we managing the automation of our documentation.  
   
 

### 00:50:38

   
Brett StClair: George is um I mean it's also working out how to kind of bring that together like you're doing releases into your and updating your YAML we should be able to pull all of that just instantly and just generate it roll it out for you. It's it's really fairly simple stuff these days. Um, I don't know. What are your thoughts on  
George Westbrook: It's I there's not really a a way to show it but it's it may be the maybe the approach the approach that that that we take so it's a lot of our obviously anything code related any changes managed by git um the more human facing ones are linear so the way that we will build our change logs is it's okay Mr. agent can you or Mr. or Mrs. agent, can you please generate a change log for the last two weeks? So, it will go away, look through all of the git commits for the last two weeks, all of the linear issues that are corresponding to that. So, each linear issue will have all of the commits associated with it, and then it's going to look through the codebase to make sure it understands the context of those changes.  
   
 

### 00:51:46

   
George Westbrook: Um, and then build out the change log for us. Because exactly like what you said, some of the change logs that people receive are this variable had this and this wrong with it and this exception was not caught. That's not good enough for business focus users. They need to understand okay the higher level details. So there's basically any way that the documentation wants to be presented um we can do it. So for us internally um if we've got new developers being on boarded they want to see the the technical changes this happened that happened that happened but obviously for say something like a content creation platform they just need to know what extra functionality are they getting what issues were they could they have been having that is now fixed. Um so it's very malleable in that sense and it's a five five 10 minute job. We receive the notification it's done and then we we merge it into whatever um place it needs needs to be done. Be it a website, be it the change log within an  
   
 

### 00:52:52

   
Michael Moores: Yeah, I think that's great.  
George Westbrook: application.  
Michael Moores: I think obviously the only considerations would be just how this hand it would be very sort of disjointed different developers for the portals for the  
George Westbrook: Yeah.  
Michael Moores: API eventually you know will handle a lot more of that but I think obviously where sits obviously the PRs and the direct and um for the need to consider that how how we get that in there and stuff like that as Guys,  
George Westbrook: Yeah.  
Michael Moores: look it  
George Westbrook: Yeah. Yeah. I suppose it's a cuz correct me if I'm wrong once once they've done is it going to be  
Michael Moores: up.  
George Westbrook: handed over and it's all going to be within within TXN's organization or is it going forward for at least the next 6 to 12 months it's going to be parts with this this place and parts with that place.  
Michael Moores: Yeah, it'll be a considerable future. Um, at least we can until we build out TX and have our own developers and stuff like that,  
George Westbrook: Okay. Yeah.  
   
 

### 00:53:55

   
Michael Moores: which is sort of a longer term plan,  
George Westbrook: Yeah. Yes. I suppose it's it it it's still it's obviously still possible.  
Michael Moores: but  
George Westbrook: It's just obviously the the complexity um with different environments and I suppose if it's Yeah. Okay. That's yeah that's one avenue. I suppose we we think what going up a level again what are the key challenges a really high level that users are facing that AI is going to be needed to solve. I always like to think of it through the lens of if there was a little human sitting on their shoulder, um what task would it want to be doing? The proactive ones, ones that more co-pilot in the back. Um and just scattering out scattering out some of them would be really helpful.  
Michael Moores: Yeah, I think for the developer portal it's very much um on that one would be sort of clientdriven and so it's very co-pilot type mechanisms. Um obviously with the exception of the the change loads and stuff you mentioned there more development practices I think for the the portal it's very much a co-pilot design that they've done it's very much side panel you ask it questions show me this that's how designed to date when we come to  
   
 

### 00:55:10

   
George Westbrook: Yeah.  
Michael Moores: the console and things like that that's very much um a different story so some of making a change on the console the AI will go this is what the impact's going to be. So prompting you back saying are you to make this change X,000 cards. So we have all that built in the design. This is what you're going to do and those sort of things and recommendation a lot of stuff we have on pages in the console is you know card holder or card level or product level is like here's our recommendations our analysis. So you quickly get the key rather than actually having to you know scroll all the way down as part of design you'll see um sort of and that sort of thing in alerts. So that's where the proactiveness will come in. So we have a whole alerts and not notification back end essenti will allow us to sort obviously the thing with designing needs the works we're we're doing. So what we are looking at with the people that building the console is over building the notifications and alerts just in the console itself to say I can pull in every alert.  
   
 

### 00:56:33

   
Michael Moores: I can pull in for the notifications. So whether we're using or the console or the portal we have one central place that will manage those preferences for the client. So that's one thing we're exploring there. So when we do build this that each of the functionality in the products can use you know that that also that we want to do in terms of alerts is quite wide. I think there's a couple of good ideas we want in terms of high volume you changing this URL um you know some of this stuff can be done by pure data that the AI can read it the data lake and how we can easily roll some of this stuff up for you to say okay we know you've got you left and the AI service and have this to perform you know de as well so we are in all this into single day delay with all that. But obviously from your side, we need to know what information you may need. Make some of the suggestions. Make sure we all that up into why there'll be you know 200,000 transactions with potentially 40 50 fields.  
   
 

### 00:57:45

   
George Westbrook: Yeah.  
Michael Moores: So from our through this understanding how we structure this data um for the data lake. Now just to sort of cure the reporting and the run latest when they an API for the reporting or we it' be good for us to know what sort of key data elements from that model will give you the model and  
Dorte Dye: Cool.  
Michael Moores: model and how do um how do you sort of understand that as  
George Westbrook: Mhm.  
Michael Moores: well um that that's the sort of the recommendation stuff will be recommendations alerts is a sort of key fil. Um but as as AI moves forward they may not use these well. So make making sure we can use some MCP layer or directly from clawterm goal as well. You know whether or not the existing MCP or build is it differently we're open to that but ultimately we want the same behavior where console or us via claw via MCP that they get that same sort of structured behavior for that text. Obviously for some of the and more riskier some sort subscription where we can okay as you access this MCP you're allowed access to X Y and Zed naturally a person on the just go change a program that say who you are in that you can actually pull that person we would once all some manager over the top of any MTP that we could based potentially  
   
 

### 00:59:33

   
Michael Moores: basting access to the console as you know access we could here's the access that this individual user has how does that affect how the MCP works and stuff like that so being able to connect from other agents as well obviously we offer a console but you know they want to build their own console and then pull on or they may have their own AI already in their app that they want to extend say you know in inside their mobile they may want to suspend the chat which obviously they can just find and we can suspend that for them have that AI to AI sort of conversation layer going on as well so that's the sort of how we want it to manifest so  
George Westbrook: Yeah.  
Michael Moores: doesn't matter where you are you t behavior based on the cost and the permissions that you  
George Westbrook: What?  
Brett StClair: Does that happen quite often where the guys build their own interface on top of your API? I mean like replicate your console. to to gr that  
Michael Moores: Yeah. Because we're future banks obviously as we our only initial we only manage card transactional stuff our balance there are accounts there's other stuff in the larger businessing systems.  
   
 

### 01:00:54

   
Michael Moores: So it easy got an existing system or stuff into that but  
George Westbrook: What is it?  
Michael Moores: obviously the is I think I'd probably say 70% of people from my past use the versus 30% building their own but they're more existing longstanding banking that it's easier for them that rather than switching to use us uh as well. So that's the that's why we offer them all as well. So it's what you want to do we offer multiple things with our console you want to build more custom. So the way our portal will be here is all the APIs you have to integrate. So that's obviously ordering a card because you wouldn't do that have some sort of applic you can use if you want them from you but you don't really need them if you don't want flexibility of what they want to do um and obviously run the MC on top core um integration layer if you will and then  
George Westbrook: Just kidding.  
Michael Moores: obviously hooks which are sort of going as well. So we have all that.  
   
 

### 01:02:04

   
Michael Moores: So wherever they are, whatever system they have, they can in you know come into us in one way and we can also send data to them in a specific always have that continuous loop to make sure our system and their system is sort of in sync. So ultimately they are balanced they are managing um you the client and the card holder ultimately their system is basically the system of record for a lot and we're just sort of processing that transaction. So we can branch out or for the day one we'll just be processing managing those in the card layer basically.  
George Westbrook: Yes. So I suppose there's like three areas I'm thinking. There's the there's the console, the AI with the human. So I am doing something I'm clicking around and there's the notification there's the co-pilot and then I suppose the more forward thinking is the complete agent view within the within the application. So your version of Claude within the console that can take the actions and then I think there's a third aspect which I don't think I don't think any of us considered before the call because of the fact that so let's say they wanted they had their own AI within their platform that they've built or they're interacting with it with claude one approach would be like you exactly what you said here's an MCP server blah blah blah but then that might there's certain best practices I suppose  
   
 

### 01:03:34

   
George Westbrook: that that you guys are going to have that are going to be built into say your AI, your support mechanism, things like that. So what what could be good there is you have a rather than claude or their application speaking to an MCP server, it's communicating with a with an agent that does that functionality. So rather than it be here's the MCP server, plug it into Claude. The issue there might be is it's not going to have all of the say the system prompts or the skills or the the the ways of working that you might have defined. So rather it's connecting Claude or their platform to another agent or agent team via say like the A2A protocol. So it's their agent speaks to your agent acts as a digital representation um for TXN. So let's say they're in their platform. I want to I want to issue a card rather than it being look through the tools for um issuing a card. It might get it right, it might not. But then there's going to be variance depending on what their AI is doing.  
   
 

### 01:04:37

   
George Westbrook: So rather it would be their AI agent messages your AI agent with I want to issue a card. It looks through sees the tools that it think might might need to happen. presents that plan back to the back to Claude, back to their agent. It then validates it. Your agent then goes away, does the required searches in in your data lake to see if it's possible, looks through the permissions of the user, executes some of the tools, and then presents it back to the agent. So then you've got the three avenues with Sorry, D, are we going  
Dorte Dye: Just wondering who's then doing the mapping.  
George Westbrook: to  
Dorte Dye: I mean with the MCP server, here's the knowledge. You just extract whatever we need.  
George Westbrook: Yeah.  
Dorte Dye: But what you're proposing, we need to understand how they're set up. They need to understand how we set up to align it. It's the same way in the reality is like I need to find my counterpart in that other company that I get what I need to get the project off the ground.  
   
 

### 01:05:31

   
Dorte Dye: So it's like how do you propose to overcome that  
George Westbrook: So the so the two so two approaches would be here's the here's the MCP service.  
Dorte Dye: then?  
George Westbrook: It's got all of the the tooling linked up with the descriptions, but there's still the the issue that they're they might know they might not know what tools to execute in what order. So effectively be replicating your internal agent on their system.  
Dorte Dye: Okay.  
George Westbrook: Potent potentially that's an approach or another approach is adding an agent on top of the tools. So rather than them interacting directly with the tools is in they're interacting with an agent which has the ability to execute those tools. So kind of like um let's just say some of the internal stuff that that I'm doing like say the the bug fixing the user feedback one approach could be here you go daughter here's the tools please can you use them obviously without much guidance it might be quite intimidating to use them there might be some issues that come up rather the approach that might be best is okay you you want me to do a certain functionality um or a certain and process a certain thing.  
   
 

### 01:06:44

   
George Westbrook: You give me the information of what you want and then I go away and I use the tooling myself with the knowledge I've got in order to be able to execute it. So rather Yeah, it's does that make a bit bit more sense or is that is any any  
Dorte Dye: It makes sense,  
George Westbrook: further?  
Dorte Dye: but it's still quite a confusing level because you need to meet the other side and work out where they're coming from and without overengineering it because we can build the world and if just one customer  
George Westbrook: Yeah.  
Dorte Dye: takes it, it's we have overengineered, right?  
Ian Johnson: don't that's sorry apologies for being late. Um I don't think that's what you're saying is it George?  
George Westbrook: Yeah.  
Ian Johnson: My understanding is what you're saying is that there'll be an agent that essentially interacts with any client user and there and any agent that they use through some some form of standard protocol.  
George Westbrook: Mhm.  
Ian Johnson: you mentioned a way. Um,  
George Westbrook: Mhm.  
Ian Johnson: and then once that is established, then our agent will figure out what it is that their agent is to do  
   
 

### 01:07:53

   
George Westbrook: Yeah.  
Ian Johnson: and go and manage below that.  
Dorte Dye: Okay.  
George Westbrook: Yeah.  
Ian Johnson: Um I think can I just take it can I because one thing I know this is a vision conversation and I've only been on it for a few minutes but I'm conscious of the fact that there's a lot of solutioning and stuff that's being discussed about how will we do these things um and I just want to you know at the very top level we want to automate as much as we possibly can both within our business and for our clients.  
George Westbrook: Beautiful.  
Ian Johnson: So the the part where we're talking about release notes and um those type of things you know automating the the generation of those and ensuring that the developer portal is always up to date because that is the source that whether it's agents or what or whether it's a user interface that is the source that needs to be kept up to date to ensure en sure that what our clients are looking to do is always accurate and it's as easy as possible.  
   
 

### 01:09:07

   
Ian Johnson: So you got two levels of what I would kind of the inputs come from within our business. So what's going on in the in in um in GitHub as you mentioned um what's going on with YAML all of those things the automation of those things to are invisible to the client but they're very visible to us Mike in particular yourself I accept the fact that we have to figure out how we would do those things when things are held elsewhere but it it's it is twofold it's not just from a client perspective It's also organizationally how do we op how do we run our business in the most crucial areas through the use of agents so that we're not the people that are doing it al so so it's 100% something that we're interested in are there some potential blockers and hurdles to get over Mike yes there are things we need to consider but I don't want to lose sight the fact that that's what we want to do it would be absolutely crazy if we dealt with the what I would call the outputs of the client's interacting with and at the top level we're still doing a bunch of stuff manually.  
   
 

### 01:10:19

   
Ian Johnson: Yeah, some at some point those things are you know there's going to be some friction that's caused there. I think from the just on the client interaction stuff for me, you know, one of the things I took away from the conversation, Brett, that we had um last time is and I'll be very open about my interpretation of your guys reaction to the console and the proposed use of AI was like that. and and to a certain degree it's also as to be clear in terms of that console experience as most people would use the SAS console today what we have designed and thought of as guides and prompts and notifications to try to help somebody then do something and take action in my opinion is quite a step forward to what most people are doing Right. But it's a iterative layer over the top of the SAS platform. Okay. It's not rethinking the way that businesses are going to work both as humans and with agents and AI. It's it's not that it this isn't this is a user experience.  
   
 

### 01:11:47

   
Ian Johnson: I I prefer to go and log onto a console and what you guys are doing with is providing me information and prompts and tools that allow me to make to do that a lot quicker. But that is not the fastest way of doing it as we move forward. And we have to cater for those different things in the sense that so do you do you log on to uh does GXM have its own version of claude as you describe it George where all of this stuff here you don't see it? I think you showed us a little bit, you showed something last week that was kind of rendering the UI within the AI itself. Uh, which I think is super powerful. Again, it's a user taking action based on a more on a less rigid approach to to what I'm trying to do. In the same way that we go to Claude and Claude has no idea and doesn't present us with anything until it starts to get some context of what's trying to happen. How that what happened in the background in terms of use of agents and all those kind of things is a separate thing.  
   
 

### 01:12:55

   
Ian Johnson: Um and then the other part is actually there is no human interaction with TXM as we see it. Of course, there is always some human interaction somewhere up the chain, even when it's when we're using agents or when even when the client's using agents. But I don't want us to lose sight of the fact that I still got this this viewpoint of um I don't know there's almost things in my mind and again far from an expert. You guys are experts in this but there are things that happen in the kind of in the card payment space that that kind of triggers an event. Something happens. We think that the client should know about this and that's what we're dealing with in notifications at the moment in the console. That's where it kind of stops. I think there's some use of AI to prompt what action somebody wants to take. So here's a we this event has been triggered. We tell you about this. Here are the here are the things that we would recommend you can do.  
   
 

### 01:14:06

   
Ian Johnson: Do you want to do them? Again, human interaction. But as far as I'm concerned, theoretically, there's no need for a human to intervene in that and a and client's agent could make that decision. Um, you know, we're the source of data. It's again not for us to actually say what a client wants to know and doesn't want to know. not know that old way of trigger it of configuring notifications so that tell me when this happens or what you know these tolerances or those kind of things and exist in a SAS platform if that's what people are used to doing that's fine um but ultimately I I don't know part of this project should be about imagining a different a different way that people are Thank  
George Westbrook: I suppose one one thing I was thinking is protect So if we view a completely agentic world,  
Ian Johnson: you.  
George Westbrook: there's the let me go in, I speak to an agent, normal, blah blah blah. And what you said about the notifications, there's we we could build some sort of kind of agent human inbox.  
   
 

### 01:15:18

   
George Westbrook: So there is an alert. There might be some changes needed. What the agent goes away and does is it investigates this. I think the limit on this should be increased by x amount. It does that pre-investigation. It goes in and says, "Right, what I think we need to do is update this, this, this, this." user goes in, they've got an agent inbox, maybe there's five in there. Click on the first of that. Here is my proposed plan. I've identified that there's these three issues. In order to mitigate these three issues, I think there could be these three actions. Do you approve of this? You just think yes, I approve. It goes away, does that shows the user maybe it's incorrect. Um, then the user can have a conversation about that specific issue on that, call it ticket for a lack of a better term. um and then go no actually I think the limit should be XYZ and then the a has a conversation with the with the the user and the agent have a conversation they debate what needs to be doing they agree on the plan which before a human would have to go in click this click that blah blah blah even if it's got the even if it's got the analysis but like you said we know with AI it can do the analysis  
   
 

### 01:16:27

   
George Westbrook: and it can take the action  
Ian Johnson: Yeah. Complete. And and that's the that's the part that we have to make sure we don't lose sight  
Brett StClair: Can I just  
Ian Johnson: of.  
Brett StClair: I think I just want to layer two concepts together because I think what's coming out of this is really good. So if we take the concept of the three trust principles in agentic AI, you know, phase one, uh the the human initiates, the bot works, the human validates, and that very much aligns to I've got a co-pilot. The human's going, I want to configure. The agent's going actually need to configure it this way. Human goes great. I'm I'm totally on board with you. I will put the configuration in place on your hand. Right? So you kind of we're addressing that first phase of I don't quite trust Agentic AI. I'm not used to it. I'm used to a co-pilot. I'm used to something guiding me. Fine. you kind of then evolve your end user to um the agent initiates, the agent works, the human validates and that's kind of where you're going into this area where it's your own kind of clawed space and you're going I'd like to configure a new card program.  
   
 

### 01:17:45

   
Brett StClair: Walk me through it. And so the agents now initiating the steps and sits on the blower down. It's going great. I'm going to initiate that step. I think you need to do that next. We need to do this. We need to do that. are you happy for me to go and execute on it? And so humans validating on it, right?  
Ian Johnson: Exactly.  
Brett StClair: And I think we've got a slightly more advanced thinking is when we're going to the agents and the the the agents responding to humanbased triggers as well. So, um, like what you were just talking about there, George, kind of fits into the agent initiates, agent does, agent validates, but we actually got a parallel validation with a human. It's going, we've got this, we need to act on that. I'm going to act on it for you. Let's go. We talk about the A to A component. We're getting into that very pure agent initi agent does the work. agent validates.  
   
 

### 01:18:47

   
Brett StClair: But that's so agent agent is is an exploding field of technology at the moment to your point is that there you have exactly it's able to find the exact exact skills that that agent is governed to be able to execute on and it knows to operate in that framework that the other agents willing to execute on. So you've got a lot of governance between those two agents. But I think we're in that very much very mature space and what I'm hearing from you in is let's start with that safety net that early stage trust. Let's create those spaces so that your user feels more comfortable moving into it and then we're using these different mechanisms to drive it. So that's just your your user experience. internally, you can also be driving it quite hectically. And I do like the fact that you guys are open to actually building your business as an agentic business. Um, we'd love to spend a bit of time operationally, internally. So, what do I mean by that? uh every part of our business for if we take uh Nova Sapion we've  
   
 

### 01:19:58

   
George Westbrook: Hey, stop.  
Brett StClair: identified and every time we see that there's a gap we go build more G uh agents to help us scale more do more make better decisions that too is a process in itself being able to understand what are those process and the best way we found to start it is start with your ticketing mechanism that's where errors issues start coming in you've got manage it. You're distributing it to different areas of the business and a lot of that can be automated. You want to still have that pain, that window, that view to be able to see what's happening, get a a feeling, a gut feeling. But a lot of the rooting and whereas you might have you feel you got a complex environment. Actually, it's good for it. You've got multiple vendors doing multiple lines of code. When they submit something, the agent picks it up and goes, "Great, it's been submitted. I'm gonna make notes that this is there and so it takes that complexity of many kind of touch points bringing it back to solve one problem to update that problem and that's why ticketing is quite a quite a central kind of task in driving your Gentic AI and you get to physically see it working really well within your operational side of your business.  
   
 

### 01:21:19

   
Brett StClair: Um how are you guys feeling about that trust factor? I mean is that does it kind of make it clearer to see? It's about authorization. It's about uh doublech checking and it kind of works with your end user. And then you apply the similar kind of trust metric internally. Start with an area. Start with  
Ian Johnson: I think it's a I think so all three of the concepts you you mentioned I completely understand. Um I suppose there's a timeline of things where we we need to we need to go to market with something that offers differentiation against what people are used to working with and that's the first concept that you described. However, that that is either going to be obsolete very quickly um or somebody is just going to come out and do number two at least which is more agentic where um the the rather than say you need to do these things and then you go in and do them yourself, you the AI says these are the things that need to happen.  
   
 

### 01:22:36

   
Ian Johnson: Do you want me to do them? And then it goes away and executes by through the use of a of of agents. I I don't I think those the first two are near-term requirements and realities because truth of the matter is I I don't think in in the world that we're in today, I don't think it'd be very long by the time we launched the concept one on the console and dev portal might before concept two was starting to be rolled out a more on a on a more broad basis. Not just necessarily in our industry, but it became something that more of our users were generally used to seeing in the other applications that they use and the other interactions they have to the point where we've all been there where you go, yeah, I want to why why can't you do it? Why to do it? you've identified this and I know that technology exists that I can tell you just to do it and then I don't do these key strokes or click any stuff and yes okay the way that you do it's intuitive and it's nice and it's pretty but you still made me do it so at some point the fact that we make people do it will mean that we in their mind we suck and it all depends on how far they are on the adoption of AI curve so I don't know but for me Mike and Da  
   
 

### 01:23:58

   
Ian Johnson: I just think those two things are really close in the sense  
Dorte Dye: Oops.  
Ian Johnson: that something's been identified or you either we've triggered something that's alerted you to something that then needs to happen and then we tell you what it is you need to do or we've alerted you to something. Um and then uh we've made the we've made recommendations and the an agent can then or agents can then in the background go and do it and all you have to do is say yes do that and that's it. That's the only thing I did was that human confirmation everything else happened in terms of the kind of timeline of things. Actually for me personally the third one is the more trust that you build in particularly the second well the first and the second but particularly the second one because the first one is do I trust this information that you're telling me I have to act on and the more time you spend it and the more you see that it's accurate it's it's real and because Mike the stuff that you've designed in the sense of um the impact piece explaining what the impact will be if you make that change is a little bit of building trust with people and then when you enter you move from one concept as more people see concept one and concept two in action as in they said yes do these things for me collectively people who are not used to that hold their breath wondering  
   
 

### 01:25:33

   
Ian Johnson: if the thing's actually going to get done and they need confirmation that this happened and confirmation of the impact the more people move to the fact that okay so you always get it right the alerts and notifications are always really um the right things that I need you know me you know the things I need to know about you can do those things and proven that you can execute them rather than me do them now stop asking me so if I think about the whole thing ultimately that human that makes the decision to say yeah I'm okay with doing that ultimately is the thing that needs to become obsolete based on I don't know let's let's say risk and compliance data the human taking into account a number of different factors to determine what action to taken based on input as a risk and compliance officer or whatever it might be that that job ultimately shouldn't freaking exist the very short term if you ask me because there's nothing that is not known that that AI can't read that can't create a better understanding and just do it.  
   
 

### 01:26:49

   
Ian Johnson: The reality is how many of us are are going to be comfortable anytime soon in that total hands-off approach without having actually seen the thing in operation. And that's why I think it's just a timeline of adoption. But we shouldn't lose sight of the fact that there will come a point when people are like, why am I even involved in this? the thing about it as a just as an employee or a leader, you know, one of candidly, you know, Mike and Da don't do this, but I've had plenty of people that that I've worked with in the past where everything they do, they always want approval that that's the right thing to do.  
George Westbrook: Yeah.  
Ian Johnson: Even when every single time they bring it to you, you go, you don't need to ask me about this anymore. this is fine and it's within your re you know this is in your control but they still keep coming back because it's habit forming um and some people will always want to be the people who check and say it's okay other people will be the thing of hold on a minute I did the work here up front to lay the context of who I am what the role is all the things that matter all the input sources why are you why are you asking me because ultimately the recommendation you come back with I'm going to assume is the right  
   
 

### 01:28:15

   
Ian Johnson: recommendation and if I've then got to read through your recommendation and say yes I'm happy for you to execute on what you've recommended doing it's not really going the  
Dorte Dye: Let's  
Ian Johnson: full way is it still but I do think concept one and concept two for the to the TXN folks I don't think we can do concept one and  
Dorte Dye: go.  
Ian Johnson: then at some point in the future do concept two because I think somebody will beat us to  
George Westbrook: H.  
Brett StClair: I think another way you need to look at this is in the same way I don't know how much  
George Westbrook: Okay.  
Brett StClair: you you guys use co-work and cl code and automate and identify your own business. So we use we use a lot of tools and we build a lot of tools to automate everything. You guys are one of those tools for your customers. You used to be a tool that configured but you're now the agentic tool that does all this work for them. They don't necessarily know that they need an agenda,  
   
 

### 01:29:14

   
George Westbrook: It's going  
Brett StClair: but you're essentially another way to think of it.  
George Westbrook: to  
Brett StClair: You're the claw cowork for your industry. You're going to come in and you're going to automate and speed up, take their load off and make more effective and squeeze more margin out, manage their customers better. You are the core code of your industry. that kind of starts resonating in your thinking and your product development, you know, then it starts making sense exactly what you're saying here because then you're thinking about how you going to mature that end user into this world where that's what that that's your role and if you look at the market the the software as a service industry is getting hammered by this right because resources around engineering are no longer you precious, you know, it's far more accessible. Um, and the same thing in operational side of things, it's just getting easier and better and faster. And so, actually, you want to be playing that logic to scale and organate faster than any other platform by making use of these tools.  
   
 

### 01:30:25

   
Dorte Dye: Just  
Brett StClair: And these tools are exactly like cloud, right? When everyone built SAS, we all built on cloud. No one was like, you didn't go in and say, I've built it on my AWS infrastructure. You just rolled out your cloud platform, but everyone was using AW. Everyone was using Google. Everyone was using all these managed service environments. And when you dig into it, you're like, oh jeez, everyone's using the same tech underneath. It's just it's just an interface. And this is what's happening with this agentic world of automation is everyone's going to be using the same set of models. You're going to be training them in your own way. Your IP sits in the ability to execute and make those decisions and advance your end user to a way more automated space i.e. freeing them up to make higher level decisions. Freeing them up to be able to manage other areas of their business. and they should be coming to you. We've got like three or four people managing our carton forms at the moment.  
   
 

### 01:31:31

   
Brett StClair: But when we plugged you guys in, we literally just watch some dashboards and we watch we watch the money. We finetune our P&L. That's power. And I think you literally,  
Ian Johnson: Yeah.  
Brett StClair: by the way, this this is only really possible in the last three, four months to be thinking like this.  
Ian Johnson: Yeah. So um that that the only reason I interjected is really to make sure that we I think the the way Brett the way you outline the concepts and what you were talking about George is um really powerful. I just don't want to come out of this and kind of, you know, go, "Oh, yeah, okay, that's all right. I was a bit better." But in fact, you know, everything that we read and and ultimately the way that Mike and Da more so than I am starting to get there, but are working with tools like Claude increasingly trying to seek ways of not having to do this stuff themselves. Um, and now, you know, there are specialized agents, skills, whatever they they they are called that allow you to do things that ultimately, you know, we're not talking about researching to find out how to do something anymore and then going off and doing it and using AI to do the research.  
   
 

### 01:33:01

   
Ian Johnson: We're talking about a specific skill that will just go and do that thing for you.  
Dorte Dye: Oops.  
Ian Johnson: Is that all interconnected in our in our end to end business operation? No, not yet. Ultimately, is that the aim? Yes, it is. The primary aim though is on the client side. So, in terms of prioritization, it's about creating differentiation and that differentiation is really about that experience. So, not just a better experience on concept one, but on concept two. I think concept one and concept two are very closely aligned. Same thing happening in the first step. Here's something you need to be aware of.  
George Westbrook: Okay.  
Ian Johnson: and these are the things I think you should do. The second step varies because it's not a recommendation of we recommend you do these things and this is the impact if you do them. It's this is the same thing that's triggered this notification. These are the things that need to happen. Do you want me to do it?  
   
 

### 01:34:04

   
Ian Johnson: Those two things from a client perspective are incredibly closely connected. And when it comes to organizationally, which is the bit that was being talked about, Mike, when talking about GitHub and stuff, what has to be in place in this first deployment of AI as we think about it to make sure that the business itself is not a throttle to the experience we give to our clients. So making sure the developer So if if we don't automate the developer notes the sorry the the release notes Mike and and you're the person that's doing them then you're the throttle to it and despite you know despite the the throughput and the amount of sheer amount of work that you do and how quickly you do it you are the single point of failure. So, you're the risk to not getting the release notes out on time and then being completely accurate to to what's actually happened. You're the risk because there's a human element to it. So if something here in the in the experience we're trying to deliver to the end customer is relying on something organizationally being up toate accurate you know instantaneous or whatever then we have to address that bit as well otherwise the experience is just not going to be the right one.  
   
 

### 01:35:26

   
Michael Moores: I think on there as  
Ian Johnson: this the very last. Sorry, Mike.  
Michael Moores: well I just before I just want  
Ian Johnson: Go ahead.  
Michael Moores: to you know in the console right now we do have a you know someone else must approve your change. So that's the sort of current state we're in. There are some things that don't things that need another person's approval. So as we think about this make sure that we include that goes well with your sort of trust element is okay we'll go into the same approval queue it needs and then we can then start to give more access and we'll give more flexibility to our client how much approval versus not does actually that's what we've built in the console for now approve your own changes we just need to consider that as we're looking at this bas  
Ian Johnson: Yeah, but I I think the thing for me though,  
Michael Moores: Yes.  
Ian Johnson: Mike, is that is always going to exist in an organization, but the point is in my mind that's an agent doing that work still you you're you're not allowed to make these ch.  
   
 

### 01:36:32

   
Ian Johnson: So I can make these recommended changes and rather than saying do you want me to action them it would be do you want me to send this for approval in a different world I would see that that another agent handling the receipt of that approval request or whoever the approver is the the approver is an agent and going yes approved and then thing just getting it done. So even the part of you can't do this. Okay.  
Michael Moores: Yeah.  
Ian Johnson: So we know you can't do it. We know who can. So if I'm the user and let's say that I want to be the laziest person in the world. What? Okay, great. Go and get approval and and do it. You know, I don't care what happens. So D asked me for something.  
Michael Moores: Yeah.  
Ian Johnson: I have to ask Mike if it's okay to do it. So D can't do it until Mike's approve. If I'm the agent, D can't do it till Mike approves it.  
   
 

### 01:37:31

   
Ian Johnson: She doesn't want to do anything beyond just it being done. And Mike really you don't either. Is this approval request? It's just an authorized, you know, is the date based on the data that's received and the thing I'm being asked to approve. Is that okay to approve? No. human interaction that you make that decision like some an agent makes that decision and just says done and then the whole thing is completed is the the thing that I see in my mind. So I completely agree with you by the way the approval levels and the security and all the things associated with a car program. We cannot underestimate making sure those things are done right. But I just think the whole the point that the reason I started this huge long monologue which I apologize for is I really think we need to go to this on the basis of giving giving people as little as possible to do in order to deliver the outcomes they're looking to get the business outcomes they're looking to get.  
   
 

### 01:38:36

   
Ian Johnson: I want to I want to make money from a card program. Um and I want to do as little as possible to manage it. Fine. That's what our aim and goal is. Um, and I I want to know as little as possible about the lo the details about card programs and all those things because I'm not a card expert. I don't want to employ a card expert. I want you to be my card expert. And that's got to be the starting point is how do we allow customers to do the least amount of work to deliver the most the best possible outcomes because that's where we'll win. Like I say, the concept one, concept two is an improvement on people's ex experience of a of a SAS console today and we'll move the needle along, but it's not it's not the end game when you stretch imagination.  
Michael Moores: Yeah, I think what  
Brett StClair: I actually can't believe I'm going to do this.  
Michael Moores: might  
Brett StClair: Sorry.  
Michael Moores: uh No,  
Brett StClair: German.  
   
 

### 01:39:46

   
Michael Moores: what I was going to say is basically We've got the bits that you may be touching in the console, the requirements and stuff for that. So, we haven't sent them to the team yet for the requirements. So, it's very worthless showing you what we're doing for the approval queue and the console. Those sort of bits that you'll potentially interject with an agent. Then, if there are any changes that you think we need to make to facilitate that for both sides, then we can do that as well. So, we haven't sent them across yet, but we can send them to you as well, get your initial views on them, and then if we do need to tweak the API or how the console's handling that to support agents and that sort of thing, then obviously we can do that as well. So, I'll send those across to you so you've got them as well.  
Brett StClair: Um so what we're also trying to get to in this process is highlight some core modules and um it's tough getting them correctly kind of aligned.  
   
 

### 01:40:39

   
Brett StClair: We we were going to make an attempt now. But before we do that, I was thinking about your card platform and what you should call your um agent. And I think you should call it card dashing.  
George Westbrook: How do you know how to boot somebody from a call on Google  
Ian Johnson: f***. I don't know. Please tell me please tell me this session is free.  
George Westbrook: Meet?  
Dorte Dye: This is so bad.  
Ian Johnson: Jesus  
Dorte Dye: Your team's work,  
Ian Johnson: Christ.  
Dorte Dye: right? It's like you just made the whole appointment for free with that  
George Westbrook: is honest think you only you only have to deal with it for two hours on a Wednesday.  
Dorte Dye: joke.  
George Westbrook: Brett Brett sits there. Wonder why I always wear headphones. Don't  
Ian Johnson: It sounds  
Brett StClair: It's terrible when I laugh so hard at my own  
Ian Johnson: painful.  
Brett StClair: jokes.  
Dorte Dye: Very  
Brett StClair: Okay, let's get back to it. So,  
Dorte Dye: nuts.  
Brett StClair: I was going to make an attempt to round up the modules, but I'd rather just dump it on George's shoulders, put him on the spot.  
   
 

### 01:41:51

   
Brett StClair: Um, and then I'm going to add to you, George. Do you want to give it a bash or do you want me to start?  
George Westbrook: Yes. So I suppose it's we probably kind of all need to direct. So what what first of all what are we trying to achieve with the the modules is kind of just putting them into buckets of areas of work. And I think the phases that you mentioned Ian might be might be a good place to start. So there's the phase one which is just the the augmenting what 99% of people are going to do where it's the SAS platform is the the main part and then they're using AI to augment it. And like you said there's going to be certain users that they're not going to want to use the AI um like the full call it full agentic experience. Um, and like I said, we're going to have to cater for them. So maybe that's module one, the meeting the user where they are in the console. And then I suppose the other one of the other buckets is that completely identified experience.  
   
 

### 01:42:49

   
George Westbrook: Um, which can potentially be broken into two further. So the the user initiated action. I go in, I want to achieve something, the agent helps me to understand the steps that go into it and then actually does the steps. And then maybe the third one is the the proactive. There is this notification. This is what I think needs to happen. Do you agree this needs to happen? Yes. And then it goes away and does it which in time can transition to it's just doing those changes. Maybe the user sets some guidelines. It goes in and sets a um what what they are optimizing for. So I am optimizing for this metric. So whenever the agent gets a request that comes in, it's going to make sure the actions that it's t it takes is optimizing for that. Maybe also identifying the user thinks it needs to optimize for XY Z given the information I'm seeing. You also need to optimize for ABC or change your thought process on that.  
   
 

### 01:43:52

   
George Westbrook: So I suppose how do we what do we call those buckets? Let's say more more traditional augmentation the user initiated agent agent view and then the kind of agent initiated user validate and in time agent just does  
Brett StClair: agent advisor or something is essentially being playing like an  
George Westbrook: everything.  
Brett StClair: advisory role. I think there's also two more components. Do you want me to fire away?  
George Westbrook: Yeah. Yeah.  
Brett StClair: I think there's also on the um support side  
George Westbrook: Go.  
Brett StClair: um helping manage and add value and augment and try solve the support requests like we were talking about earlier. And then I think there's around the documentation. So pulling out the necessary changes in the documentation with available portals to kind of accelerate and maintain all the different changes and push requests and stuff like That  
George Westbrook: May maybe we keep it higher level than that where it's it's just the all of the other ones are more client  
Ian Johnson: Good.  
George Westbrook: facing. So the support blah blah blah all of that phase one phase two the agent stuff that's all client facing and maybe there's a fifth a fifth bucket which maybe is not a priority now but is over time is the internal operations.  
   
 

### 01:45:16

   
George Westbrook: So fix bu fix fixing the business all of the human the human errors where the bottlenecks are um that that could be another module as well.  
Ian Johnson: Yeah, I mean, you know, my intention is to from a go to market point of view, we're going to and I think from a number of different things, dirt, we're going to build a bunch of stuff in claw to try to minimize the amount of effort and increase the amount of productiv productivity we've got. So I'm less concerned about some of those things. I think the one thing I would say is anything associated to the product and platform Mike and the support of clients that that's the bit that really um I think is the most important thing when we think about organizational um automation because those are the things that ultimately have a very direct impact um on both um the experience well the experience for the client and for our own people and also quite frankly from the the the financials of the business. Um we don't want to we don't want to employ more and more people to do something we know we could we could do um with agents etc. I got I've got a question for you and this is basically my just a lack of understanding from my perspective.  
   
 

### 01:46:39

   
Ian Johnson: We obviously we showed you the console and we showed you the areas where we could see um AI adding some value in a co-work type um experience really what how how do we get the insights you know from an AI perspective what what tooling will you use to get those insights to bring them back and serve them up to say okay these are the things that you need that we think you need to be aware of ei degradation in authorization response times Mike or whatever it might be how are we getting that data from I mean I don't even know where it will sit like but but wherever it sits how we get that data into concept one and into the console to serve it up to a client  
George Westbrook: I suppose I think from some so I think two the two aspects are where the user is in the application and whatever so basically where they are what's the state of what they are what buttons what buttons there what components what's the current state of what they're doing um and then that can inform form what data also needs to be collected for the agent along with maybe questions that are asking.  
   
 

### 01:48:00

   
George Westbrook: So it would be right, they click copilot, it pops up, it sees the state of the application, it sees that they're on the uh on a certain page. Given that they're on a certain page, it's going to pre-pull some of the data in into the state of the of the agent. Given the question that it's asking as well, maybe it pulls more information, maybe it loads in some more things. Um cuz one of the things we it'd be important to make some it'd be it'd be important to make some assumptions um about what they want to do given the page that they're on, but also give it the flexibility that um we're not being like, "Right, you're on this page. The only things that you can do are these five things." Because sometimes users might be on the configuration page and they want to ask about something completely  
Ian Johnson: Yeah, I think there's two things there, isn't it? There's the what I would consider to be the userdriven event where I  
George Westbrook: different.  
Ian Johnson: ask whatever I ask the AI something and it, you know, theoretically it doesn't matter where I ask it.  
   
 

### 01:49:09

   
Ian Johnson: Um obviously there has to be some limitations on this is not this is not clauded or chat GPS this is only related to to this stuff and then  
George Westbrook: Yeah.  
Ian Johnson: there's how we are alerting somebody based on where they are to some things that they should be aware of. So some important information that then they can take action on if we've got recommendations or whatever it might be. I always think um not everything some some information is just information but I always find that to be I don't know things like revenue um almost any  
George Westbrook: Hello.  
Ian Johnson: any information that you provide without a recommendation or an impact or what you're actually telling me about something is just pointless in a business context. text. It's like it's almost that so what thing. So you're almost heading towards a so if we're going to if what we display with this AI should be something that has got an action that could be taken from it. Something that we believe could improve their their business or it's decreasing risk, increasing opportunity, whatever it might be.  
   
 

### 01:50:32

   
Ian Johnson: Otherwise, what's the point? Because if you just want something on a dashboard that tells you how many transactions you processed yesterday and exit and all that kind of stuff, right? That's what people go to dashboard for. When you're in this operational tool, you expect the information that gets relayed to you to be something that you should probably take action against. Otherwise, why are you telling me about it? I didn't know. I didn't need to know that. So, who cares? Um and that's the kind of way of thinking about it. So will it so will you build will you basically deploy agents to get the data that you need to get to serve up this  
George Westbrook: Yeah. Yeah.  
Ian Johnson: information  
George Westbrook: So I think it Yeah. So let's say what could be the things that could trigger it to get some information. A user question, an alert. One potential thing is every single time a user goes onto certain pages, maybe it pre pre-colcts some information, does a bit of analysis, or maybe it's on certain schedules.  
   
 

### 01:51:43

   
George Westbrook: So say maybe once a week it checks the health of a certain aspect. Um and then maybe there's certain things that a user might want to yeah they can set the schedule for what they want the agents to do like say if they had a human it's like check the health of the of this specific program um do it on every day do it once a week things like that. So yeah, I suppose that's one thing we didn't think of. Maybe userdefined scheduled actions or scheduled analysis for things that the users actually want to  
Michael Moores: So I think from there as well just to sort of bring the soul in is obviously to  
Ian Johnson: Yeah,  
George Westbrook: know.  
Ian Johnson: I mean  
Michael Moores: your point yes we've got I think the difference is real time versus both sourcing real time we're going to pull that data down I think with the alerts we've got that proactive make. So it's got that ability to pull the data in and make all we need to do in the console that alert. So I think you know the console design does have in there.  
   
 

### 01:52:47

   
Michael Moores: It does have alert me when type conditions merchant decline rate is above X. They're the sort of things that the conso's order and obviously you've got our own anomaly and detection like that. I think that sounds to me like it sits well together from an an AI point of view. Look at this. put alerts down for D alerts endp point down for DT in phase one but it see I think more align the AI piece than D at this point I think where we are so as long as some other systems as well AI generating if we've got infrastructure or like that I think AI is primary driver of this now it makes sense for all of this stuff to sit with elves as long as we can feed specific alerts as well. because you know we have these all these separate environments we do alerts to sit that can be sort of interrogated as well I guess you know what we can do but the simplest and API calls if it's more basic but you know ultimately other systems can speak to the agent and that's yourself as well where together and simple for back end process that uh speed dependent the real time one is more speed dependent where we're probably going to make sure is there quickly to or whatever so I think I'm not too concerned about that sort it's more the analytical real time that we need to make sure we pro provide you with a basis that ask basically obviously we don't want to wait you know 10  
   
 

### 01:54:32

   
Michael Moores: seconds for it to pull that analytics if you what you said is an alert. We can store that on our AI side and the console just pulls that down from that all alerts for this user. We've to get that alert and we've already got the action should be quite quick where you consider the real time aspect that and there is well if a huge amount of data that the AA may have to sit we are planning on putting the data lake centrally one so you can do that cross program you can also but those table potentially can get quite big so I think we just need to what it is and the key data elements we can roll up in depth to that matter that we can get that to you quickly from an AI agent of  
Ian Johnson: I think I think the thing for me, Mike, I agree with all of that.  
Michael Moores: view.  
Ian Johnson: I think that I think you have to work back start almost with the end in mind, which is what are the things that a client really needs to know about that has got a subsequent action associated to it.  
   
 

### 01:55:50

   
Ian Johnson: because those are the things that you need to be getting in real time. So you know if I think about real time processing Mike  
Michael Moores: Yeah.  
Ian Johnson: if if we don't if we only if we only need to pull back you know once a day as an example what the authorization success rate was then we would not be alerting a client to the fact their authorization success rate was below a threshold that probably needs some kind of action or they're you know API responses whatever it might be and there's an a and there's an action that needs to be taken and obviously following the flow we talked about and an action we can recommend and they can ask us to undertake um so I think when we talk about there's notifications and alerts and I think we just need to think about what those things are you can send me a notification that perhaps I don't want I don't need to do anything about why you send me a notification to tell me that, you know, there's a thousandth card that's been issued today.  
   
 

### 01:57:02

   
Ian Johnson: Great. That was interesting. Thanks very much. Versus an alert that tells me I've only got a thousand card numbers available on the bin that I've currently got. And here's the things you can do about it. What do you want to do? I think it's just that. And Mike, you may have all of this covered and thought about, but I think we just got to think about AI really being, you know, AI being used to pull back information. Great. The most benefit is in my opinion is AI pulling back information that needs to be actioned on or could be actioned on whether it needs to be because there's a risk or could be because there's an opportunity um either way.  
Michael Moores: Yeah, I think it's um time to raise this like you say it's think we're talking to DT about the data lake  
Ian Johnson: So  
Michael Moores: and anything they do it is slow harded type table how how do you understand how you work obviously potentially you could get the A roll up So to your point here is how do you manage a decline rate if  
   
 

### 01:58:12

   
George Westbrook: That's  
Michael Moores: you bucket it daily minutes or hourly that's obviously something we  
George Westbrook: beautiful.  
Michael Moores: need to either feed into BT and say that's that's what they need to build or we need to sort of potentially have the data lake benefits of doing that I know it's more complex but benefits of agent would be we can pivot we can do new tables we can do new is anything we rely on DT to do an API and scheduled reports and I think stuff we want hardcoded there is a visa report that is always like this that's the sort of stuff it's the same stuff you know give transactions give me this these are sort of static reports we class as there I think it's going to be a subsection especially with the custom reporting that we want to offer in the console and these analysis of potentially And obviously it'll be good to get your inputs on the date as we put these requirements forward. We still have requirements to direct transact as it stands. So it'll be good to get your input from that as how whether you you can interact with uh spin up tables and bucket that data as well.  
   
 

### 01:59:31

   
George Westbrook: Yeah, because I suppose one one approach there is of the potentially having like a say like a reddish memory store that on a schedule um the agent is querying and filling the memory store so that when a user asks a question go straight to there and within couple hundred milliseconds it's got the results back because it's already been premputed which I suppose is more of maybe more of a traditional technology approach um but I suppose it's it rather than it querying 200,000 rows at the time that the the user wants it and it has to wait 5 seconds. Obviously, that's not a good user experience, but we're going to know there's certain things the user is going to want to access, we can have it there. We can have it ready. Um, and then the agents can just go bam, done. It's in there. The data is there. Within 5 seconds, they've got a response. Um rather than waiting five seconds to query the  
Ian Johnson: Well, I I think for for me that almost splits into two different  
   
 

### 02:00:27

   
Michael Moores: Yep.  
George Westbrook: database.  
Ian Johnson: things. If there's something that you need to render immediately on a console, I would consider that to be something that um is not userdriven and the experience would be that if I go to my console and I go to the a certain page, I wouldn't expect to see AI working in the background to pull information back. So if it was taking five seconds for information to render and I know that I know what should be there because it was there that would be odd and that wouldn't be great user experience. If I ask it for something we're all used to Claude or DBT telling us it's working on it. That's a completely different thing. And I think the bit we've got to just think about when we think about the experience is nothing. You know if you ask a question to cla it doesn't come back in milliseconds well anything you ask it of remote interest it can't it won't come back in milliseconds so I just think we need to think about um the different data that were coming back sorry I need to jump I need to jump off I think that the point for  
   
 

### 02:01:35

   
George Westbrook: Yeah.  
Ian Johnson: me is  
Brett StClair: I think we we pretty much got everything we need, right?  
Ian Johnson: yeah I hope so I I suppose um my my  
George Westbrook: Okay.  
Ian Johnson: takeaway input to you guys is obviously we've I you know I think we've always been  
Dorte Dye: Thank Okay.  
Ian Johnson: aligned in terms of where we're trying to head. You guys have helped us stretch that ambition a little bit more with the kind of the thoughts about agent to agent. We've been thinking about MCP etc. But we have still got to deliver this. All right. number one priority is concept one closely with  
George Westbrook: Okay.  
Ian Johnson: concept two behind them and whatever the back whatever the infrastructure and the and the tooling that needs to be in place to drive those things that then allow us to to take the next step towards concept three but we need a I think Mike is fair to say we need a we need a road map to understand how we get from where we are now where we need to be we've shown some we've shown you the console design and what we thought um about things etc. So to one degree you can say well how do we make that a reality?  
   
 

### 02:02:59

   
Ian Johnson: What how do we use AI to make that a reality? Of course even within concept one if there's things that we've seen and you see and you think well actually we could probably make that better or actually delivering concept two is not that far away from concept one. Once you the first bit then actually the the second part is not that complicated. We need a road map that's going to take us on that journey to how we get there and what we need to have in place to make it happen.  
George Westbrook: You're on mute, bro.  
Brett StClair: Yeah, I know. I agree with you. It needs to be mapped out. Need to pick what's going to land, what's going to hit your MVP. A lot of stuff was spoken about that really cool, but what's actually doable? We'll lay that out for you guys as well. All  
Dorte Dye: So we got from super ultra the feature list as well. How do we want to approach that? I think we can't select the MVP features as standalone that needs to come with the piece.  
   
 

### 02:03:58

   
Brett StClair: right.  
Ian Johnson: We've got this conversation already. I am going to work on the fact that the AR was there anything that you saw when we did the console demo that you thought I don't know how we deliver that with AI? No.  
Dorte Dye: No,  
Ian Johnson: Well, I was actually asking the Teraflow guys because they've got to do it to be honest. But if you can do it, why are we talking to these guys?  
Dorte Dye: I'm using claw then I break everything.  
Ian Johnson: So I think I think the I think the point is I don't think we need to restrict anything in the design that we then think well actually what happens if we say yes, it's in and then we and then Brett or George or Matt's come back and go, I don't know what you've said yes to that for because we you can't do it with AI. There's nothing that we've done that we can't. I would suggest that I think the point for me is more once that the the AI piece is not in their wheelhouse.  
   
 

### 02:05:01

   
Ian Johnson: We've got some ideas of the different user stories, Mike, that we've thought about for the use of AI. But in terms of the AI experience, they're not building that experience. You guys have got to build that experience. as I understand it or at least the input into the design. So within that remit if there are things that come out that are closer to con you  
Michael Moores: Yeah.  
Ian Johnson: know whether in concept one or closer to concept two that's fine. What we've done is broadly set set out something I think ded that is along the  
Michael Moores: Heat.  
Ian Johnson: the right lines for what you'd expect to see from a co-work sorry a co-pilot type  
Dorte Dye: What  
Ian Johnson: solution. Um,  
Dorte Dye: was  
Ian Johnson: of course we can keep you guys informed about that, but I'm I'm just not sure that that dependency is quite as great as we think it is because we we've got to start building the console.  
Dorte Dye: incredible?  
Ian Johnson: I mean, in an ideal world, you know, we'd be in a different place, but we're not.  
   
 

### 02:06:01

   
Ian Johnson: We're trying to run multiple different streams concurrently or overlapping so we can move this thing forward.  
Brett StClair: We do need to talk to the guys about the console build and how we  
Dorte Dye: So,  
Brett StClair: integrating the back end of the API and the chat interface. Just make sure that we're feeding in the right way that they are designing their kind of interface architecture.  
Dorte Dye: I have invited you to the uh final prototype review for the developer portal that you can see that as well on Thursday.  
Ian Johnson: Okay. So,  
Dorte Dye: Brad  
Ian Johnson: would you replay not back everything we've said obviously, but but just replay your kind of summary from this? I mean, I'm I'm surprised that you haven't already done it with all the agents you've got working, but I'm sure it'll happen very quickly. Um, but it would just be good so that we can start to ground some  
Brett StClair: We're going to essentially build out a portal.  
Ian Johnson: things.  
Brett StClair: We've got portal that builds all this out, takes all our conversations. And so today we we're trying to get to the point where we get a very clear each list what's doable, what's not doable, categorize into modules, categorize into vision.  
   
 

### 02:07:18

   
Brett StClair: And so we start with the vision today and sorry that's why we use Google Meets. It's all integrated into this agentic AI stack. So it takes about four or five hours before we get the transcripts and everything that we need in the right format and then we start the process tomorrow essentially different agents cutting everything down building out all kind of portal environments and by the end of the week we have the first hit of it and in there it's got all these review mechanisms it builds out this knowledge base we build out the knowledge graph um and everything becomes automated and so any discussion,  
Dorte Dye: Oops.  
Brett StClair: any any chat, we don't want to get it mustn't get lost in a conversation, mustn't get lost on a piece of paper. We look  
Ian Johnson: I hope all this is true, Brett, honestly, because if not,  
Brett StClair: forward  
Ian Johnson: you're the best snake skin snake oil salesman on the planet. So, I I fully believe you do all this. There's not 500 Indians find you, is there?  
   
 

### 02:08:18

   
Brett StClair: in your if you checked your doorbar Amazon arrived, there's there's a bottle of snake oil for you. Can't believe you didn't go get it.  
George Westbrook: Oh s***, the 10 of them are coming in now. No. Get out. Get out. Get out.  
Brett StClair: Sorry.  
George Westbrook: Still on the  
Ian Johnson: Hopefully I'll use the connect connectivity with Brunwin.  
George Westbrook: call.  
Ian Johnson: So if you shaft shaft us then I'll just get Bronwin on to you.  
Brett StClair: God. Well, then she can punish the crap out of  
Ian Johnson: Yeah.  
Brett StClair: Ben.  
Ian Johnson: All right. That sounds good. mic or  
Dorte Dye: Nope. What's the next step? That's the only question.  
Michael Moores: Nobody.  
Dorte Dye: So,  
Ian Johnson: anything.  
Brett StClair: So we'll send you a calendar some options to pick. Uh it's based they'll be about hourong sessions to flesh out the real detail in each  
Dorte Dye: yep.  
Brett StClair: of the modules. Um might feel like we thrashed out a bit of detail today.  
   
 

### 02:09:10

   
Brett StClair: We haven't. We we we're going to get into it. Um, and then off the back of that, we'll draw up the sub modules and we'll have your entire backlog plan, flight plans, the works ready for the back of that. Ian, by the way,  
Dorte Dye: Cool.  
Brett StClair: it's it's impressive. Like, every time we do this,  
Ian Johnson: sounds impressive.  
Brett StClair: it's it's it's a  
Ian Johnson: I'm looking forward to seeing in action. It's not that I distrust you,  
Brett StClair: good  
Ian Johnson: Brett, by any such imagination or or George for that matter or Max. You know, it's just you do hear horror stories, don't you, that these AI built companies have just got like kind of bunch of 13year-old kids tapping away on keyboards. I'm sure that's not the case.  
Max Kingaby: You You don't want to know what age they found me at,  
Brett StClair: No, it is  
Max Kingaby: Ian.  
Ian Johnson: I say you do George and Max do look like they could be there.  
Brett StClair: right.  
Ian Johnson: All right, I'm going leave you to it  
Brett StClair: Awesome guys.  
Ian Johnson: then.  
Brett StClair: Thank you very much for your time today.  
George Westbrook: speak to you soon. Thank you very much.  
Ian Johnson: rest.  
Brett StClair: It's trouble.  
Ian Johnson: Thanks, F.  
   
 

### Transcription ended after 02:10:18

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.