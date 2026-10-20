---
date: 2026-10-20
type: standup
description: "Launch set for 16 November, DT never asked to host the AI, hosting split from the demo, a 28–30 October demo window, and the test harness built"
scope:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[developer-support]]"
  - "[[agent-access-layer]]"
status: extracted
extracted-to:
  - "[[open-questions]]"
  - "[[architecture]]"
  - "[[delivery]]"
  - "[[portal-co-pilot]]"
  - "[[permission-scoping]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-20)

> **Source:** Gemini transcript, 20 October 2026, 29m. **Novosapien:** George Westbrook, Vineth Siriwardana, Max Kingaby. **TXN:** Ian Johnson, Dorte Dye, Michael Moores. Brett was not on the call.
>
> **The call that found the hosting gap.** Since 6 October the vault recorded the AI node in DT's European Azure stack as built. On this call it turned out that nobody has asked DT for anything about the AI. Ian then made the main decision of the call: DT gets the hosting requirements now, with no wait for the demo.

## DT was never asked to host the AI

Ian thought an email showed that DT *"had already set up the AI... node in Azure"*. Dorte corrected him: *"No, that was Brett's point that we need to do that."* Ian then read the plan aloud: *"Brett has asked for it on the 16th of October and the flight plan says AI node in DT European is built and only access remains."* And: ***"So has anybody actually asked DT to do anything yet?"***

Dorte: *"No, because of everything we have hold of speaking with them about AI."*

Michael now describes the node in the future tense: *"I think it's just a node they'll spin up inside... it should just be a brand new node that they do spin up alongside everything else."*

**So the 6 October record is wrong on one point.** The shape holds: a dedicated node in DT's European Azure stack. The build status does not. Two vault documents carried the error, register row #70 and the hosting callout in [[architecture]], and this digest corrects both. Two more carry it and are Brett's to correct: the 16 October flight plan, which says that the node *"is already built. What remains is access"*, and the MSA reviewer brief in `content/legal/`.

## The launch is 16 November, and hosting no longer waits for the demo

Dorte showed the go-to-market plan: *"we planning to launch on the 16th of November. So we just need to play backward from that."* Her gates after the demo are UAT, DT acceptance of the hosting, and endpoints from DT and Stackworkz that fully work. Ian: *"our number one priority is to get to market on the 16th of November."* [[open-questions]] #108.

**Two work streams, one gate.** Ian: *"you've got two distinct work streams"*. One is the functionality, which moves into the Stackworkz code. The other is the hosting. Both start after the sign-off of the Knowledge Hub AI, and that sign-off is Michael's alone: *"The only people who need to say that they are happy with the demo ultimately is Mike."*

**Ian's ruling: the hosting does not wait for the demo.** *"I still want to do the demo, but I think we need to break the link between assuming a demo is needed in order for us to get this set up. I think we work the other way around which we tell them what we need."* George committed to send the requirements by the end of 21 or 22 October.

**Accuracy before speed.** Ian: *"DT think everything's a change request basically... the speed is not the most important thing. It's being completely accurate giving them as much information as possible."* [[open-questions]] #119.

**One version, not two.** George offered to move the build into the Stackworkz codebase while the demo build continues, and to sync the two. Ian declined: *"I think it's much cleaner to just do as much work as we possibly can to make sure that when we're ready to deploy it is the single version of what we want to put out in the wild on the 16th of November."*

## The timeline back from launch

| Step | Owner | Date |
|---|---|---|
| Hosting requirements and package list to DT | Novosapien, sent through Michael | End of 21 or 22 October |
| Build fully tested (*"battle tested"*) | Novosapien | End of the week, 23 October |
| Demo dry runs | Novosapien | 26 and 27 October |
| Demo to DT and PayCorp | Novosapien | 28 to 30 October |
| DT provision the AI node | DT | Weeks of 26 October and 2 November, *"at the outside"* |
| Checks in the hosted environment | Michael, with Novosapien | At least one week before launch |
| Launch | TXN | 16 November |

Dorte on the demo date: *"if we can run it via DT by the end of next week, that will be brilliant because it's a week earlier than the current plan."* Michael agreed. [[open-questions]] #115.

**The DT lead time is the risk.** Dorte's plan gives DT one week, and she said that week already is a buffer: *"they're very slow in responding."* Ian: *"I would not count my chickens with respect to that being the lead time frankly."* George allows one week from a codebase that is tested locally to a deployed one, for access issues: *"if you say a week, a week to be safe."* Ian: *"if they take two weeks, you still got a week."*

## The hosting shape for the Knowledge Hub

There are two deployables. George: *"there will be the actual agent and the MCP server. So the MCP server's quite lightweight."* For the agent: *"Ideally, what we'd want to use is an autoscaled service similar to Cloud Run that will scale up, scale down based on the demand for it"*, with some instances always on to stop cold starts. Nobody has yet researched which Azure service fits, and George called it *"not a long task"*. Novosapien deployed agents on Azure for another client, *"a slightly different style of agent"*. [[open-questions]] #49.

**Dependencies.** The only DT dependency for the Knowledge Hub APIs is the sandbox. The docs MCP server reads the CMS, Umbraco, which is live. The other blockers are access to the infrastructure and the move into the Stackworkz codebase.

**What helps.** Michael: Stackworkz accepted the package list, and it goes to DT *"in one go"* with the hosting requirements. DT only host this time: *"they were sort of only asking them to host only this time whereas the others are host and support type things. So it should be an easier run through."* Michael knows of no hard no from DT on Azure.

## The test harness is built, and TXN has not used the build

George: *"we've finished the testing harness today."* Michael sent the personas and the questions, which [[open-questions]] #117 recorded as the blocking input. Next, Novosapien loads them, and the three personas must be *"absolutely nailed"*. UI and speed changes are already in.

**Nobody at TXN has used the build.** George asked if anyone had tried the dev console. Ian: *"No."* The latest co-pilot goes to the test and production versions of Novosapien's admin console. George asked everyone to run a few questions and check the output against *"the eyeball test"*, for wrong answers, UI bugs and improvements. He also said that this is *"maybe not as urgent in the next day or two because there might be some new changes going in."* See [[portal-co-pilot]].

## Control Center authentication, before the 21 October call

The Stackworkz call is on 21 October, and it covers how the agent authenticates in the Control Center. George's position: the agent needs *"a token as well, so that it can be validated on behalf of the user"*. The first request to the Control Center returns *"a permissions payload"*, and the payload decides which MCP tools the user sees.

**A new design choice: one skill set for each permission profile.** The alternative is one skill with permission branches. George's reason: with branches, the agent sometimes tries a tool it cannot use, *"one in a thousand times"*, and then it *"might spin a bit and say to the user, oh sorry, this tool isn't available."* With separate skill sets, *"it's not aware of it. It's not in any of its skill files."* [[permission-scoping]], [[open-questions]] #107.

The call does not block the Knowledge Hub, because the Knowledge Hub has no signed-in user.

## Stackworkz: the ways of working are set

George: *"We've got access. The ways of working are sorted."* Novosapien works on its own branch and tests locally, and Stackworkz approve merge requests before they reach the main branches. Review turnaround, deploy ownership and a definition of done are still not agreed. [[open-questions]] #111.

## Findings and where they landed

| Finding | Destination | Action |
|---|---|---|
| **DT was never asked to host the AI; the node is not built** | [[open-questions]], [[architecture]], [[delivery]] | **#70** corrected; architecture callout corrected |
| **DT's lead time now sets the launch** | [[open-questions]], [[delivery]] | New row **#119** |
| **Launch on 16 November** | [[open-questions]], [[delivery]] | **#108** updated |
| **Hosting does not wait for the demo**, Ian's ruling | [[delivery]], [[open-questions]] | Recorded at #115 and #119 |
| Hosting requirements to DT by 21 or 22 October; accuracy before speed | [[delivery]], [[open-questions]] | Recorded at #119 |
| DT timeline: weeks of 26 October and 2 November, then a week of checks | [[delivery]] | Timeline table |
| **One version, not a demo build and a production build** | [[delivery]], [[portal-co-pilot]] | Recorded |
| Michael is the one sign-off before the Stackworkz migration | [[delivery]], [[open-questions]] | Recorded at #115 |
| **Demo window 28 to 30 October**, dry runs 26 and 27 October | [[delivery]], [[open-questions]] | **#115** updated |
| Hosting shape: agent plus docs MCP server, autoscaled, minimum instances | [[portal-co-pilot]], [[open-questions]] | **#49** updated |
| Stackworkz accepted the package list; DT host only | [[open-questions]] | Recorded at #119 |
| **Evaluation harness built**; personas and questions received | [[portal-co-pilot]], [[open-questions]] | **#117** updated |
| Nobody at TXN has used the build | [[portal-co-pilot]] | Recorded; action on TXN |
| **One skill set for each permission profile** | [[permission-scoping]], [[open-questions]] | **#107** updated |
| Stackworkz review gate in place | [[open-questions]] | **#111** updated |
| The flight plan and the MSA reviewer brief say that the node is built | Brett | Flagged; this digest does not edit them |

### Context, no action

| Finding | Note |
|---|---|
| Brett was not on the call | He sent a message during it |
| Ian's "fire drill" last week | It set the must-complete list, and the AI piece is on it |
| Novosapien's Azure precedent | Agents deployed on Azure for another client, a different style of agent |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Write the hosting requirements, with a backup for each service | Novosapien (George) | End of 21 or 22 October |
| Review the requirements and flag anything DT will refuse | Michael | Then send them to DT with the package list in one batch |
| Deploy the latest co-pilot to the test and production admin console | Novosapien | 20 October, afternoon |
| Run a few questions and report answer and UI issues | Ian, Dorte, Michael | Not urgent for a day or two |
| Load Michael's personas and questions into the harness | Novosapien | Three personas must be *"absolutely nailed"* |
| Test the build fully, then run the demo dry runs | Novosapien | By 23 October; dry runs 26 and 27 October |
| Control Center authentication call with Stackworkz | George, Michael | 21 October |
| Correct "already built" in the 16 October flight plan and the MSA reviewer brief | Brett | See #70 |

---

## Transcript

Oct 20, 2026

## TXN - Agentic AI SU - Transcript

### 00:00:07

  

George Westbrook: Give me a second. I just got on my f****** headphones. Literally was just cleaning them. Let's see. Hello. Can you hear me? Hello. Can you hear me? Come on.

Vineth Siriwardana: That was nice. Oh, yes. I was nodding. Yeah.

Dorte Dye: Hello.

Max Kingaby: Guys, how are you up?

Dorte Dye: All right.

Ian Johnson: living the dream. It's just not mine.

Max Kingaby: Stared so enthusiastically.

Ian Johnson: Yeah, it's not it's I've always I've had this saying for quite some time. I'm living the dream. It's just not mine. It's somebody else's.

Dorte Dye: Just wanted to say you just came off a meeting for me.

Ian Johnson: Somebody needs to Let's go have a meeting with you

Dorte Dye: So that's why

Ian Johnson: about legal.

George Westbrook: They're they're the most fun meetings, aren't they?

Ian Johnson: Nope.

George Westbrook: That's what I wake up in the morning if I see anything about legal. I'm like, "Oh, yes. My day is going to be absolutely amazing.

  
  

### 00:02:16

  

George Westbrook: Yeah. Don't It's uh Not everyone shares my passion. I would not want to be a lawyer. Put it that way.

Max Kingaby: Lawyers don't want to be lawyers cuz their jobs aren't existing.

George Westbrook: I don't know. I'm sure there'll be a way that they'll find find a way to justify the hundreds of pounds an hour that they apparently charge.

Dorte Dye: You could argue your job doesn't exist soon either, Max.

Max Kingaby: I am nature.

George Westbrook: All of us. We're all gone.

Dorte Dye: We retire.

Ian Johnson: Bring it on.

George Westbrook: Yeah.

Ian Johnson: Bring it on.

George Westbrook: Thanks. I think I think that's everyone that's everyone from our side. Um, so I suppose one one thing I think that's top of mind for me at the moment is the that call with um, Stack Works, Mike, that we're that we're going to do tomorrow. Um, because obviously there was a bit of bit of back and forth with them because from our side it was we were just a bit unsure as to what what it was they were they were talking about and didn't really want to go into the conversation a bit blind.

  
  

### 00:03:18

  

George Westbrook: Um, it was all all to do with obviously the authentication, how the agent's going to be authenticated. Um, but given what they sent over, we got a bit bit better of an idea. Um, I think they'll still today I'll be doing a bit more thinking on that. But I think all it is is the only thing I can see is we'll need to find a way to give the agent a token as well. Um, so that it it it can it can be validated on behalf of behalf of the user. um and maybe finding a way in which when it when it requests information from the control center initially, it passes back that let's call it like a permissions payload so we can reconfigure things so that we've got the certain MCP tools are exposed to certain users and not others. Um and I think one deci one like kind of design decision with is in terms of skills as well. So think the skill obviously you know what skills are there just a text file with effectively steps in there a lot more goes into it but so one of the things we're thinking is the two options are when let's say we got one user with permission A another user with permission B um is they will have two separate versions of the skills rather than having in the actual this user is got has got this permission then execute this tool.

  
  

### 00:04:44

  

George Westbrook: Um if they've got that permission then execute another tool rather just have two completely different sets of the skills. Um so given a user they're always going to get that it just reduces the amount of error because sometimes an agent um let's say one in a thousand times might go I'm going to try execute um the create card holder tool um even though it's not going to have access to it. it might spin a bit and say to the user, "Oh, sorry. This tool isn't available." Rather, if we isolate it, um it's not it's not aware of it.

Michael Moores: Nice.

George Westbrook: It's not in any of its um skill files. So, it should well, it will make sure that it's a bit more bit more durable. Um so, yeah, authenticate, talk about that, talk about that tomorrow. Um and I think obviously the next big one is the the dev console or knowledge hub. Um, so thanks very much for, pardon me, for sending over those personas and the the guy the questions. So we've finished the testing harness today.

  
  

### 00:05:51

  

George Westbrook: Um, so what we're going to start doing is loading in um the personas and the questions so that we're testing everything but obviously making sure that those three that that we've outlined are going to be absolutely nailed. So we've already done some changes in terms of UI some speed some speed as well. Um so in parallel to that it'll be focusing on what is it actually saying how is it responding to certain users. Um so I think in parallel with the um the testing harness as call it the the autonomous testing what would be really helpful is if if we all just go in go through a few questions just see if the the output meets the eyeball test um doesn't need to be super super extensive um but so we're catching anything um on the like what it's saying but also any UI bugs that we see or any improvements Has

Michael Moores: Yeah, that sounds brilliant. Thank you.

George Westbrook: anyone ever had a chance to have a little play around with the with the dev console?

Dorte Dye: Hello.

Ian Johnson: No.

  
  

### 00:06:57

  

George Westbrook: Okay. Um, yeah. So, we'll we'll we'll make sure that all of that is pushed by this afternoon. Um, and then we'll let you know we'll let you know when it's there. Then have a play around. Like I said in in terms of timelines as well. Um obviously you mentioned Mike that ideally the the back end of next week is is is when you want to do it. Um we can oh I think Bre just sent a message. Um that's that's fine. Um like from our side we think by by the end of this week it should be should be battle tested. Um then idea could be maybe Monday, Tuesday, um we sit down, maybe do a right dry run of the demo. Um just so the way that we're speaking is is right, the way it's flowing. Um maybe a few more dry runs so that we've got Wednesday, Thursday, and Friday completely free um to do the demo. Is is that quick enough or do do you need it do you need it quicker than that?

  
  

### 00:07:59

  

Michael Moores: I think that's okay from my stylist. Any else got any other concerns?

Dorte Dye: No, I think if we can run it via DT by the end of next week, that will be brilliant because it's a week earlier than the current plan.

George Westbrook: Okay. Yeah, cuz I suppose it's balancing getting it done as quick as possible and then making sure it's like abs absolutely nailed.

Ian Johnson: the the the latter,

George Westbrook: Um, yeah.

Ian Johnson: I think that um we positioned I know we didn't really touch on detail in the AI, but if I if I've understood correctly, D, what you're saying is that there's an acknowledgement from DT that they in fact I read an email today that suggests that DT had already set up the AI my node in Azure.

Dorte Dye: No,

Ian Johnson: Yep.

Dorte Dye: Stephan Pete from

Ian Johnson: Nope. From here, I'm pretty sure of it.

Dorte Dye: me.

Ian Johnson: Yep.

Dorte Dye: No, that was Brett's point that we need to do that.

Ian Johnson: Uh Oh, I've got it. So Brett has asked for it on the 16th of October and the flight plan says AI node in DT European is built and only access remains.

  
  

### 00:09:20

  

Ian Johnson: So has anybody actually asked DT to do anything yet?

Dorte Dye: No, because of everything we have hold of speaking with them about AI.

Ian Johnson: Okay. So let's just let's just walk this through then. We've got a go to market actually does. Why don't you pull up your screen?

Dorte Dye: Yep. Can you see?

George Westbrook: Yeah. One try.

Dorte Dye: So we planning to launch on the 16th of November. So we just need to play backward from that. Initially you said you would have the scripts ready by the end of next week which mean the earliest we could demo it will be the week after. So if that moves the week forward then I would just leave us with the UIT testing and then DT to be happy with the hosting and obviously they need to have the endpoints you both rely stack works and you guys to be fully working. So that's the biggest challenge at the moment. The moment they release Mike is full on with the testing.

  
  

### 00:10:59

  

Dorte Dye: So the the endpoint testing and then the knowledge hub testing with the AI in the environment from stackbox as a first phase and then there's a second phase once it's in the hosting production environment with DT.

George Westbrook: I I think in terms of in terms of APIs for the knowledge hub, the only one where we'd be dependent on DT would be for the sandbox because

Dorte Dye: Yeah.

George Westbrook: the like the MCP server for the for the knowledge that's going to be all through um not Marqueta um the CMS um and I can't believe that name slipped out my mind. So it's all dependent on that which is which is which is up and running. Um obviously there might be some more pages added or some pages taken out but that's that's relatively quick work. Um in terms of the the only blockers would be us getting access to the the infrastructure and setting that setting that all up. um the migration onto uh the codebase that stack works have provided us for the for the knowledge hub um which I think we've held off on that to make sure that the demo is apps are absolutely nailed um because obviously there's going to be some be some changes over maybe the next week um so that by next week we're at a point where okay this is good to go um let's get that migrated over to the codebase any deploy deployables that we need to deploy on the infrastructure,

  
  

### 00:12:30

  

George Westbrook: we'll already start research, make sure that we know right, this is ideally how we want to deploy it. Um, if this is not the case, this is a backup, this is a backup, this is a backup. Um, so a lot of the work and thinking would have already be done. It would just be managing managing access.

Ian Johnson: How how much hosting are we actually talking about for the AI component?

George Westbrook: So for the for the knowledge hub there will be the actual agent and the MCP server. So the MCP servers quite quite lightweight and then the agent um depending on if there's any limitations on the sort of services that we can use from Azure. Ideally, what we'd want to use is an autoscaled um service similar to Cloud Run um that will scale up, scale down based on the demand for it with with obviously a few set up to minimize cold starts as well because that's why in some of our demos specifically on like the testing where we're like there's a cold start it's slow is slow.

  
  

### 00:13:32

  

George Westbrook: Um but obviously in production that's not going to be the case.

Ian Johnson: But you you know what it is that's needed.

George Westbrook: Yeah. Or we Yeah. We we know the style of the stuff we need to do. We just need to research which which services on Azure are going to be the best fit which is it's not a not a long task.

Ian Johnson: Is this that's because you haven't deployed in Azure before?

George Westbrook: Uh no, we've well the the stuff that we've deployed on Azure um might be slightly different to this um like one of the one of the other clients we were working with their their agents deployed on Azure but it's just it's slightly different style of agent um but it's yeah it's

Ian Johnson: So I I think I think for me um there's if I'm understood correctly, what you're saying is you want to make sure the demo is 100% spot on before you do the work on the stack works code. Is that right?

George Westbrook: Um that was one of the approach. It doesn't have to be the approach.

  
  

### 00:14:38

  

Ian Johnson: I I I'm okay with it. But I think the point there is that's not the demo. That demo doesn't need to be to the wider audience. The only people who need to say that they are happy with the demo ultimately is Mike,

George Westbrook: Yeah.

Ian Johnson: but it's within TXM the and that is the bit that says, okay, right, this is what we're going to do. Um, and we're happy with it. which allows you to then do the stack works work. Um, I don't know how many alignment sessions we're having in staff works because it sounds like there's one tomorrow.

George Westbrook: Yeah. Yeah. So, tomorrow the one is mainly around how the agent's going to authenticate in in the control center. So, it's it's not it's not going to block anything uh for for the knowledge hub integration. Um because at the moment it's just there's there's no authenticated user. So, it's mainly around when um the agent in the the console or control center is is taking actions on behalf of the user, how do we mimic the controls that they've they've got so that they're not doing things that they wouldn't be able to do in the console?

  
  

### 00:15:45

  

George Westbrook: Um,

Ian Johnson: So if we if we turned around and said tomorrow and said everything you've built is fine from a knowledge hub perspective you are ready to go and do the work needs to be done on the staff works code for knowledge hub.

George Westbrook: Yeah, because the reason why we were holding off a bit was because see that given the testing there might be some changes um in the front end code for

Ian Johnson: It's currently fine.

George Westbrook: the Yeah.

Ian Johnson: I I'm just trying to get a clear picture of where we are with this stuff because ultimately the control the work on the control center I understand is to make sure that it's not a blocker but our number one priority is to get to market on the 16th of November.

Michael Moores: Oops.

George Westbrook: Yeah.

Ian Johnson: the so getting Mike to a point where you you we sign off the the knowledge of AI capability to to then say okay go and put it in the stack works code I I don't know how long that takes how long that will take you to do it then we've got the demo that we want to do to DT and payor which is solely for the purp well the primary purpose is to get make sure that there's no hold up in getting the DT hosting set up the AI components.

  
  

### 00:17:05

  

Ian Johnson: So to me, you've got two distinct work streams function the functionality piece including into staff works code and then you've got the hosting piece. Um we can't start any of that until we've signed off on the AI on the knowledge of AI piece which completely agree. think it's it's definitely the right approach to do it. I get that. But I think we need to work back to a point where the only thing that's outstanding with a reasonable amount of debt because I I look at that and say DT hosting for AI components one week. I wouldn't I would not count my chickens with respect to that being the lead time frankly.

George Westbrook: Is is that is that in terms of them them giving access?

Dorte Dye: I just put in buffer because they're very slow in responding. So,

George Westbrook: Okay.

Dorte Dye: I didn't wanted to say they just switch it on and off you go.

Ian Johnson: But I I would I would have said that you need to be working back from there.

George Westbrook: So do we in order to aid that conversation by let's say end of tomorrow or Thursday do you need the kind of exact requirements as to what we need to deploy

  
  

### 00:18:21

  

Ian Johnson: I I think that based on today's conversation, Mike, and the fact that it was already, you know, Pete did, as I requested, put it on the agenda. Okay, we didn't get to it, but they know it needs to be addressed. I still want to do the demo, but I think we need to break the link between assuming a demo is needed in order for us to get this set up. I think we work the other way around which we tell them what we need and then if somebody comes along and says well hold on a minute we already know what this thing does then we can say you make sure that you understand and

George Westbrook: Yeah.

Ian Johnson: uh the details of how you can provision these the um what we need from the from the Azure infrastructure um so that we're not doing we're not kind of having two dependencies but I think the sooner they get the information of what's required at least from my

George Westbrook: Yeah.

Ian Johnson: perspective like the better.

Michael Moores: Yes.

George Westbrook: Okay. We'll we'll fast track that and make sure that by like I said, end of tomorrow or Thursday, there's there's something there with almost exact exactly what what we think we need.

  
  

### 00:19:25

  

George Westbrook: Um so that if there's any feedback from them, we can quickly quickly change it, make sure it's aligned. Um and then yeah I suppose the demo we'll keep on working on that and then cuz one one thing we one thing we could do um in terms of that wait for the demo then migrate we could do both in parallel and then all we could do is we'll have a process of let's say the let's say this side is the the migration and this side is the demo at at one point they'll both be at the same level. Let's say the the demo version for the demo we've noticed a few issues that creeps up to here. We can just bring that back up. Um both as viable. Um maybe you could argue there's risks on both sides like there could be bit of divergence in terms of what the demo is and what the um what the let's the production version is going to be. Um but they're both they're both doable. It's just a matter of where do we where do we want to power ahead with

  
  

### 00:20:29

  

Ian Johnson: No, I I I I don't I don't think there's any need for that.

George Westbrook: Okay.

Ian Johnson: I think it's much cleaner to just do as much work as we possibly can to make sure that when we're ready to deploy it is the single version of what we want to put out in the wild on the 16th of November.

George Westbrook: Yeah.

Ian Johnson: point is that we the sooner we can tell DT what's going to be required things

George Westbrook: Mhm.

Ian Johnson: have shifted a little bit over the course of last week because we kind of uh we set a little bit of a a fire drill to say look this is people this is just going on and on and on and we need to get around got the absolute things that need to be completed as a priority the AI piece is in there So I I think that realistically

George Westbrook: Mhm.

Ian Johnson: speaking, we need to get that information to them by if we do it by the end of this week, even if there's a week of, you know, I think we then got to say how how long a period do you want to be able to effectively deploy and make sure that everything's working the way it's meant to be working.

  
  

### 00:21:47

  

George Westbrook: I think for a Yeah,

Ian Johnson: You want to weak.

George Westbrook: I think that's probably overestimating it. Um but I think ju just on the rather than saying yeah it's going to be two or three days um if you say a week a week to be safe um from a point where we've got a code base that is ready tested locally um to being deployed um because there might there might be certain access issues or there might might be other issues.

Ian Johnson: I I I agree.

George Westbrook: So I think a weeks Mhm.

Ian Johnson: I completely agree. So I think the point is you we have in this when we're going to tell DT what the hosting requirements are this week and then that effectively would leave us we commencing 26 and week commencing the sec the second at the outside for them to actually put it in place and at least a further week to make sure Mike that everything is working as it's meant to be working then for the 16th of November. I don't know how long it'll take to spin up this is your stuff.

  
  

### 00:22:56

  

Ian Johnson: They're just not very fast at anything they do. That's concerns me. Um, and then we still need to prep for the demo, but to a certain degree, you know, the de the demo is a subset of all the things that Mike sent across to you to say these are all the things that we've kind of thought about as the test questions. It's that and then it's those three personas from memory. But I'm I think there's enough momentum now that that we won't get back from them going, "Hold on a minute. We've done anything about this, we're not even going to look at it. Um, but the sooner we get the information to them, well research and you're comfortable and confident that's right,

George Westbrook: Mhm.

Ian Johnson: the better." And then the clock can start ticking and then that's working in parallel to us

George Westbrook: Yeah.

Ian Johnson: actually doing the um continuing on the kind of functionality and making sure that's right.

George Westbrook: Yeah. Yeah. Okay. Yeah. Yeah, cuz I think as as soon as we get to the point where we've not got the the demo and the let's call it our our version of the console and the actual version of the console where they are one and the same, those changes are there's there's not going to be that potential issue.

  
  

### 00:24:14

  

George Westbrook: Um so yeah, no, I think that yeah, that sounds good. So we'll we'll after this call um we'll have a sit down, we'll have a think um we'll get something over to you as quick as possible. Um, and then yeah, Mike, if you could have a look, any feedback, like if if there's something that's in there that you know that's not going to get approved, let us know and we'll we'll quickly iterate it until until we've got something that we're all happy with and then pray DT take uh less than a week to to sort it out.

Michael Moores: Yep.

Ian Johnson: Well, if they take two weeks, you still got a week.

George Westbrook: Yeah.

Ian Johnson: I I think I I would just say take the time to make sure that you're absolutely confident on what you're asking for. That would be the biggest risk to it is because DT think everything's a change request basically. I think when it I think when it moves from night to day they flag it as a change request. So you just need to be super the speed is not the most important thing.

  
  

### 00:25:20

  

George Westbrook: Okay.

Ian Johnson: It's being completely accurate giving them as much information as possible. Um and then we've got we've got sufficient time but because literally you have to

George Westbrook: Yeah.

Ian Johnson: spell out everything which we are learning or Mike in particular is learning to his great enjoyment.

George Westbrook: You love getting those feedback emails, Mike, where where they're like, "This this there was a space in this paragraph that shouldn't have been there. We cannot accept this.

Michael Moores: Yeah.

Ian Johnson: It's more a case of you didn't tell us exactly how to develop everything and what code standards are. So now we going to blame you because it wasn't in a user story anyway.

George Westbrook: I don't it's Yeah.

Ian Johnson: It matters. It matters little.

George Westbrook: Yeah.

Ian Johnson: So are we so there's no there's no issues with stack works on

Michael Moores: Thank you.

Ian Johnson: the knowledge of that. That's all aligned.

George Westbrook: Yeah. We we've we've got access. The ways of working are sorted, which I mentioned is really good for us.

  
  

### 00:26:20

  

George Westbrook: It's kind of here you go. Do whatever you feel you need to do. But there's also their approval layer in there. So, we're not just going straight into the into the main branch and changing everything. We've got our own branch, make changes, make sure we can test it locally, and I'm assuming they're going to test it locally before they merge any um requests into the the more main branches. Um and then yeah, the discussion tomorrow is maybe a bit more of a forward thinking one in terms of the the control center authentication. Um but it's not not not going to limit the um the progress on the other stuff.

Ian Johnson: Okay. Okay.

George Westbrook: I think I think that's everything. Um oh Mike, I think there's yeah two things I was thinking. So first one was was there any feedback on the list of packages that we sent over from DT or is have we not heard anything back yet?

Michael Moores: That's these go to them. So Statworks are happy with that from from their side.

  
  

### 00:27:19

  

George Westbrook: Okay.

Michael Moores: So yeah, we just got to send that across to them about you know with everything you've got. So it' be sort of packages what we need to be built that'll go across to them in one go and then yeah as part of that bill we can we can go from there. But I don't see any issues from from that side.

George Westbrook: Okay. And then in terms of anything Azure related, are there any things that will be a hard no from them or anything that that we should know before we we we nail down the solution to it?

Michael Moores: Not that I'm aware of.

Dorte Dye: It's

Michael Moores: No, like I said,

George Westbrook: Okay.

Michael Moores: it's a bit of a new one. They were sort of only asking them to host only this time whereas the others are host and support type things. So,

George Westbrook: Yeah.

Michael Moores: um it should be an easier run through because it's only sort of hosting only. Um yeah,

George Westbrook: Okay.

Michael Moores: not that I'm aware of anyway.

  
  

### 00:28:03

  

Michael Moores: So if you just sort of document what you're thinking and we can get that across with along with the libraries and then

George Westbrook: Yeah.

Michael Moores: put it in front of them and see how that fits into our uh ecosystem. Obviously like I said last time I think it's just a node they'll spin up inside.

George Westbrook: Yeah.

Michael Moores: So it shouldn't be like it causing any issues or anything like that but it should just be a brand new node that they they do spin up um alongside everything else.

George Westbrook: Okay.

Michael Moores: So that's my expectation anyway.

George Westbrook: Okay. Perfect. Sounds good. Um yeah, I think that's everything unless anything else anybody's got anything else.

Dorte Dye: No, sounds good.

George Westbrook: Perfect. Right, we'll we'll get that sent over once once we're sure. And um like I said, we'll get the we'll get the latest version of the co-pilot for the knowledge hub deployed to both the testing and the production versions in the the admin console we've got. So whenever you've got spare time to play around, um maybe not as urgent in the next day or two because there might be some new changes going in. Um, but yeah, apart from that,

Ian Johnson: Sounds

George Westbrook: let's uh let's go.

Michael Moores: Yeah, sounds great.

Dorte Dye: Oh, thanks.

George Westbrook: Perfect.

Ian Johnson: good.

Dorte Dye: Bye.

George Westbrook: Speak to you soon. Have a good one.

Ian Johnson: All right.

Michael Moores: Just take care about

Ian Johnson: Bye.

  
  

### Transcription ended after 00:29:18

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.
