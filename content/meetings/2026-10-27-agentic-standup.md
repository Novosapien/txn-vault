---
date: 2026-10-27
type: standup
description: "The DT demo slips to 2 November and becomes a courtesy, the LLM section is held back for a Thursday call, and the co-pilot test scores climb"
scope:
  - "[[developer-support]]"
  - "[[architecture]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[portal-co-pilot]]"
  - "[[architecture]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-27)

> **Source:** Gemini transcript, 27 October 2026 (a Tuesday), recording ends at 49m 09s. **Novosapien:** George Westbrook, Brett StClair, Hasan Ahmed, Max Kingaby. **TXN:** Dörte Dye, Michael Moores. **Ian was not on the call**, and several items are explicitly held for him. Max speaks once, in passing. The second half of the call is George walking the demo script live, with Michael and Dörte commenting.

## The DT demo slips to Monday at the earliest, and stops being a pitch

**The date.** Dörte: *"it's Tuesday, end of business. No one is there from South African side. They're heavy on working on another release... realistically **the first possible date will be probably Monday**."* That is 2 November, outside the 28 to 30 October window at [[open-questions]] #115.

**The purpose changed, and George named it.** Novosapien had prepared *"the full sales pitch of why this is this and this is that"*. Dörte reframed it as a courtesy: DT *"need to know what they're hosting and what the TXN platform is about"*, but must not get an opening on behaviour:

> *"We don't want them to give any input on how it's behaving because this is set by us. We don't want to muddle the waters and DT is saying, 'Oh, have you thought about this and you should do this.' **It's too late.** And B, I think we just need to protect what we having... we just need to start delivering this stuff."*

Michael agreed: *"they have a habit of saying things and trying to change things."* So the demo shows what is landing, then moves to the real agenda, the architecture. George: *"if anything, it takes a bit of pressure off."*

**The one thing that must not happen:** *"Don't f\*\*\* it up by connection issues and cold start."* Dörte expects the security and liability questions to come from the hosting side: *"where is that all sitting, are you liable because you're hosting"*. She and Ian will tighten the roles and responsibilities in the agreement. See [[commercial]].

## A two-week delay Dörte already expects

Dörte, unprompted, at the top of the call:

> *"Stackworks I was already expecting a **two week delay** because DT has certain code standards they want to have and play, and I already challenged them on that one. **You're just hosting AI. You're not owning the code as such.**"*

And on the date: *"at the moment we're **very tight already till the 16th**."* Her concern is that DT *"have not seen a thing yet"* and *"it will rattle some cages"*, so the earlier they see it the better. **This is new.** It is a delay on the Stackworkz side driven by DT standards, with no detail on which standards, whether they reach Novosapien's code, or whether the two weeks is inside or outside the 16 November plan. New [[open-questions]] #125.

## The hosting documents go to DT this week, without the LLM section

**Michael has both infrastructure documents from George** and sends them to DT this week: *"we've got that infrastructure level at least."* That moves #119, where the request was held on 22 October.

**One part was cut on purpose.** George: the way *"we're dealing with the LLMs in terms of fallback... are we limited to Azure?"* was *"purposely left out"*. Brett gave the reason: *"we were going to add it to this and then we went, actually, just before we sent it, no, don't. **That could just light a fire in your data space.**"*

**Dörte agreed and moved it up a level.** Michael is too busy with UAT, the data discussion *"just completely blown out of proportion"*, so she wants it settled first between her, Ian and Novosapien, scoped to the Knowledge Hub only, before anything goes to DT. Brett sends the LLM document after the call, and the meeting is **Thursday 29 October, 3 to 4pm**, with Michael optional.

## The harness: from extremely low to high, in four days

**Hasan showed the results.** The harness loads Michael's question pack, iterates, and flags failures for a human to check, since some flags are only wording differences: *"it will give you all of the key information except it's not going to be the exact output."*

- **Runs started on 23 October**, *"extremely low"* at first. A partner asking how to issue a card would get *"random facts"*.
- **The fix was guardrails** that keep the agent to the key facts, plus changes to how it lays out the answer, to keep it *"clear and understandable"*.
- **Results are split by persona** (a partner, a prospect and others in Michael's pack) and *"a lot of them are doing extremely well"*.
- **The grey "held" rows** are questions the docs cannot answer yet. Michael: *"stuff we've still not got in the documentation... where I wasn't sure from DT on the accurate values."* They are excluded from the score.

**George's point is that it is reusable.** *"We can add more personas, we can add more test cases... and also have something similar for the console as well. So **long gone are the days of going through a chat one by one, looking at the answer, putting it in a Word document**."* That is the machinery #117 asked for, now with results. What is still missing is a pass mark.

## The demo script, walked live

George ran the three flows and asked what to add or cut. **Michael: *"That's covered off most for me."*** The order:

1. *"What does TXN do and how does it all fit together?"* Typed live in the demo, *"so they don't think we're cheating"*. Show the expanded panel, the tool actions at the top, the sources, the link to the most relevant page, the quick downloads.
2. *"I want to give my customer a card but I've never done this. Where do I start?"* Answers in steps, opens each page, then runs it in the sandbox.
3. *"Walk me through issuing my first card in the sandbox"*, then the lost card flow including Apple Pay, then *"write me some node code to run the lost card flow against the TXN API"*, then **download the markdown and paste it into Claude**.

**Architecture goes at the end**, George's call: opening on *"this is deployed here and we're thinking about doing this"* loses people.

**Two additions, both agreed by Michael.** Show **copy to Claude or Perplexity**: *"yeah, I think it's great to see."* And mention **the docs MCP server and the LLMs.txt**: *"Yeah."* George will look for visuals for it. **Michael's priority:** *"just showing the ease of developing into, I think, is a big one. So obviously taking this elsewhere."*

**George will export the chats** and send them over, so TXN can read the answers without replaying them.

### The approval clicks go, and a plan up front replaces them

George named the weak point himself as it happened on screen: in the sandbox flow the user clicks approve, then approve, then approve.

> *"Whereas we're going to sort that out so that it's: here's what I'm going to do. Do you approve it? Still going to show the payloads, give them the detail that they need, but kind of that **progressive disclosure** where it's going to show the higher level part, and then if the user wants more detail they can get it."*

One approval for a stated plan, with requests and curl still one click away. See [[portal-co-pilot]] and #116.

### Some of the wait is the API, not the model

*"This is where some of the almost unavoidable speed things are... **it's not the model being slow, it's just sending the requests**."* The mitigation is text before the call, *"so that the user's got something to do while they're waiting."*

## Loom videos: a fallback, a leave-behind, and a sales tool

The fallback recordings for the demo are done. George asked whether to send a prepared Loom after the call. Michael: useful *"just in case someone can't make it"*, and Ian wanted it shared with Steve. Dörte: *"we also could use it as a **sales tool** going forward."* George took it further: videos on the website for what will not be there on 16 November, such as the agent inbox, because *"a lot of people find it hard to conceptualise"* an agent until they see one.

## After it is deployed: the model, the data, and nobody watching

**Dörte asked the operational question.** Once the test results are good, *"is there any case where that could change once we have deployed it?"* George: not really, unless the model changes. **The model is named on the record for the first time:** a Gemini Flash model, *"available for you through Azure"* (the transcript renders the version as "3.8 8 flash"). If DT insist on another model, the test cases are run again and fixed. See [[architecture]] and #70.

**There is no continual learning.** George: the data is stored and reviewed by hand, *"a semi-manual process"*, looking for the most common follow-up questions as a sign that the docs or the agent need changing.

> [!warning] George said 48 hours. On 22 October the number set was 72.
> *"Storing the data for what was it **48 hours** with any personal information and then after that strip the personal information out."* On 22 October Michael set **72 hours**, aligned to the sandbox data drop, and George agreed to drop from 30 days to 72 ([[2026-10-22-agentic-standup]]). Nobody corrected it on this call. The vault keeps 72 hours until someone confirms otherwise.

Dörte: *"didn't we say we tell everyone not to use personal data in the first place?"*

**Monitoring is not agreed.** Dörte: *"we want to know before a customer tells us something is not working."* George: Sentry is Novosapien's usual tool. Michael: DT and Stackworkz have *"only what's built in Azure. They've got nothing else."* George will check the architecture document. Dörte: *"anything you can put in just makes me feel a bit more safe than relying on what we're expecting from DT."* New [[open-questions]] #126.

## Smaller items

- **How DT see the build.** Dörte's email asked about giving DT access and changing the authentication. George: without the link to the admin vault *"there's no way that they'll even be able to find it"*, or Novosapien can *"spin up a new environment where there's only one sort of authentication"*. TXN's choice, not made.
- **The Console co-pilot.** Work has started, but *"majority of resources and thinking"* go to the 16 November launch.
- **The ICPs.** No more questions are needed from Ian.
- **TXN's own testing.** Optional. *"If there's any time... just run through the questions. But if not, we'll be testing it regardless."*

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| DT demo no earlier than Monday 2 November; reframed as a courtesy showing of what DT will host, no input on behaviour | [[delivery]], [[open-questions]] #115 | Callout added; row updated |
| Dörte expects a two-week Stackworkz delay from DT code standards; 16 November "very tight" | [[delivery]], [[open-questions]] #125 | Callout added; **new row** |
| Infrastructure documents with Michael, to DT this week; LLM section held back | [[delivery]], [[architecture]], [[open-questions]] #119 | Callouts added; row updated |
| Internal LLM call, Thursday 29 October 3 to 4pm, Dörte, Ian, Novosapien | [[delivery]], [[open-questions]] #70 | Recorded as an open action; row updated |
| Harness results by persona, guardrails added, "held" cases excluded, reusable for the Console | [[portal-co-pilot]], [[open-questions]] #117 | Callout added; row updated |
| Approval per step replaced by one plan-up-front approval with progressive disclosure | [[portal-co-pilot]], [[open-questions]] #116 | Callout added; row updated |
| Demo script agreed; copy to Claude/Perplexity and MCP server plus LLMs.txt added | [[portal-co-pilot]], [[open-questions]] #110 | Callout added; row updated |
| Sandbox latency is the API calls; holding text planned | [[portal-co-pilot]] | In callout |
| Model named: Gemini Flash via Azure; retest if DT mandate another | [[architecture]], [[open-questions]] #70 | Callout added; row updated |
| Retention stated as 48 hours against the 72 agreed on 22 October | [[portal-co-pilot]] | Flagged, not overwritten |
| No monitoring agreed; Sentry versus Azure built-in only | [[architecture]], [[open-questions]] #126 | Callout added; **new row** |
| Hosting liability; Dörte and Ian to tighten roles and responsibilities | [[commercial]], [[open-questions]] #103 | Callout added; row updated |
| Loom: fallback done, leave-behind after the demo, sales tool, website videos | [[delivery]], [[commercial]] | In callouts |
| How DT access the build: unlinked, or a single-auth environment | [[portal-co-pilot]] | In callout |
| Console co-pilot started, launch takes priority | n/a | Context, no action |
| Ian needs no more ICP questions | n/a | Context, no action |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Send the LLM document to Dörte and Ian, and book the call | Brett | After the call |
| Internal call on LLMs, fallback and data, Knowledge Hub scope | Dörte, Ian, Novosapien (Michael optional) | Thursday 29 October, 3 to 4pm |
| Send the infrastructure documents to DT and propose a demo date | Michael | This week |
| Export the demo chats and send them over | George | After the call |
| Add copy to Claude/Perplexity and the MCP server/LLMs.txt to the demo | George | Before the demo |
| Replace per-step approvals with one plan-up-front approval | Novosapien | Not dated |
| Check monitoring in the architecture document | George | Not dated |
| Tighten hosting roles and responsibilities in the agreement | Dörte, Ian | Not dated |
| Decide how DT get access to the build | TXN | Not dated |

## Transcript

Oct 27, 2026

## **TXN \- Agentic AI SU \- Transcript**

### **00:00:00**

**George Westbrook:** The Sapian notetaker.

**Brett StClair:** This is just Hello there.

**George Westbrook:** Hello. Oh, good, good, good. How you doing?

**Dorte Dye:** Don't ask.

**George Westbrook:** Uh, cold. I can see see you with your jumper. Your nice fluffy jumper.

**Dorte Dye:** Actually, it's nice and warm. I just like that jumper so much. It's that time of the year.

**George Westbrook:** Yeah. Don't. It's Yeah. When I'm when I'm leaving leaving the house in the morning, I'm like, I can't just wear a little jile and a jumper anymore.

**Dorte Dye:** I went out with my winter jacket during the day and I was like, "Oh yeah, this is too hot." And I was like, I arrived here sweating and then in the morning I go out in shorts and no this is not right. So like

**George Westbrook:** Oh,

**Brett StClair:** It's a Funny temperature right now, right? Either too hot, too cold. You are too cold.

**Dorte Dye:** you can't make it right for me anyway. So it is what it is.

### **00:01:05**

**Dorte Dye:** So I guess we have quite a few things talking through and one of the things and apologies Mike for jumping in. We had a conversation with the stuck works team.

**Brett StClair:** Welcome to

**Dorte Dye:** Um so testing everything is okay and honestly Mike if you're okay with that

**George Westbrook:** okay.

**Dorte Dye:** because it's all friendly testers don't bother about testing. We just tell them exactly just go to the knowledge hub ignore everything left right center to keep it simple.

**Brett StClair:** Maggie.

**Dorte Dye:** Um the challenge what we have at the moment is um with moving you over to DT into production. So we need to have that call with them rather sooner than later. Um Stackworks I was already expecting a two week delay

**Brett StClair:** Hold

**Dorte Dye:** because DT has certain code standards they want to um have and play and I already challenged them on that one. You're just hosting AI.

**Brett StClair:** on.

**Dorte Dye:** You're not owning the court as such. But that might be just one additional conversation we need to have them when we run them through the demo where there might be some push back.

### **00:02:10**

**Dorte Dye:** So at the moment we're very tight already till the 16th.

**Brett StClair:** Pink.

**Dorte Dye:** If we can get that out rather sooner than later then let the bomb explode on the other end. But I think that my concern is at the moment they have not seen a thing yet and everything even though they talk a lot about AI it will rattle some cages. So I think the earlier we can do it and the better prepared we are

**Brett StClair:** He's

**Dorte Dye:** it gives me a little bit more comfort if that makes sense. And then we can push anything down the line there after

**George Westbrook:** It's it's so so is that is that in the context of giving them access to the UAT environment or the or the demo? or both.

**Brett StClair:** happy.

**Dorte Dye:** I don't know what you see. I would not give them access to the to the UAT because it's just side

**George Westbrook:** Okay.

**Dorte Dye:** noise for them at the moment. They need to fix the background. Why what they need to get their head around is this is what is lending on your desk.

### **00:03:08**

**Dorte Dye:** This is what we're proposing with the hosting. Get everything ready for the hosting because what we're trying to avoid is they're coming in and they will have a say and they want to know it's nothing to do with you guys. It's hosting. Simple. It is. But I might just over oversimplify that because I'm not a techie. So I shut up. I'll let Mike do the talking now.

**Michael Moores:** Yeah, I think that's fine. I think that's a good uh approach. Obviously, we've got both the documents now from you, George. So, thank you. I'll send that to DT this week. So, we've got that infrastructure level at least. U we start on that. So, I'll send that to

**George Westbrook:** I think there was one one thing we purposely left out of there at the moment is the the way that we're dealing with the with the LLMs um in terms of fallback. Where are we going to do? Are we going to do is is it are we limited to Azure?

### **00:04:02**

**George Westbrook:** are we going to do this? Are we going to do that? Um, so that's been purposely left out. Um, can quickly add that back in and we'll be do a bit of turbo thinking if needed, but I thought it was it was something that we were

**Brett StClair:** So it's around your kind of guidance like what's happening with LLMs, where does the data go, how to fail over, how to set up and I was we were just carving that out for you and we thought maybe we don't want to blur things up being in that architectural diagram.

**Dorte Dye:** So I think what we should do have a conversation when you have that stuff. Um Mike is incredible busy at the moment with the UAT that maybe between you and Ian and I we have that discussion on the first level because what happened at the moment with all of the data stuff it just completely blown out proportion. So let's we're just looking at the knowledge hub for now. What can we do? Where does it sits?

### **00:04:54**

**Michael Moores:** Do this.

**Dorte Dye:** Make a quick agreement on that one before we then present it.

**Brett StClair:** Thank You get two eyes.

**Dorte Dye:** And then again we do the stuff at the knowledge hub.

**George Westbrook:** Yeah.

**Dorte Dye:** Let's do that. Let's focus on the roll out first, the launch. Then everyone is comfortable. We have a baby step at the knowledge hub. So let's look at the console because the console has a little bit more substance, right?

**George Westbrook:** Yeah.

**Dorte Dye:** Because it has the real data even though let's bridge

**Brett StClair:** Okay guys,

**Dorte Dye:** that.

**Brett StClair:** thank you again for

**Dorte Dye:** Let's get that bridge. Whatever.

**George Westbrook:** Yeah. Yeah. Yeah. That that that makes a lot of sense. Yeah.

**Dorte Dye:** So,

**George Westbrook:** They're similar to what we were thinking as well.

**Dorte Dye:** do you have already something ready you can share with Ian and me? I mean, by all means, share it with Mike as well, but then um quickly book something in for for us to have that conversation with you guys.

### **00:05:43**

**George Westbrook:** Yeah. Is that is that that's doc that document you prepared,

**Brett StClair:** the LLM.

**George Westbrook:** wasn't it, Brett?

**Brett StClair:** Yeah. Yeah.

**George Westbrook:** Yeah.

**Brett StClair:** Yeah.

**George Westbrook:** Yeah.

**Dorte Dye:** When When did you send it?

**Brett StClair:** We haven't sent it. We were going to add it to this and then we went actually just before we sent it. No, don't. That could be that could just light a fire in your data space.

**George Westbrook:** Yeah.

**Dorte Dye:** Honestly,

**Brett StClair:** We pulled it out.

**Dorte Dye:** everything is set fire to whatever I'm doing at the moment as like I'm too lowle down. So that's why I really need Ian to lift it up a level. This is what we're comfortable with it. And again, it's a very limited scope for for the knowledge base, right? But then when we know what the the whole remmit is, then we just take it the next level.

**George Westbrook:** Yeah.

**Brett StClair:** Perfect.

**Dorte Dye:** Yeah.

**Brett StClair:** We'll get that to you after this.

### **00:06:27**

**Dorte Dye:** So if if you if you send that across, um Ian is out tomorrow afternoon. Um maybe we book something in for Thursday.

**Brett StClair:** Happy.

**George Westbrook:** Hey,

**Dorte Dye:** We we used to have a slot from 3 to 4 which is I'm pretty sure it's still available if you want to book that in when you when you send the email out as discussed or we

**Brett StClair:** Okay. Okay.

**George Westbrook:** heat.

**Dorte Dye:** book that slot and then you you can put Mike in an optional so if Mike is is free

**Brett StClair:** And then book that

**Dorte Dye:** or blocked from testing then he's more than welcome to join.

**Brett StClair:** Perfect.

**George Westbrook:** By the by the sounds of it,

**Dorte Dye:** I think Mike we need to send you I think we need to send him a survival packet.

**George Westbrook:** that's not going to be the case.

**Dorte Dye:** I was like, I would just eat s\*\*\* at the moment non-stop or drink

**Michael Moores:** It's very busy at the moment.

**George Westbrook:** Need some coffee, some nicotine, and some sweets. That's a That's a That's a care package.

### **00:07:20**

**Michael Moores:** Yeah.

**Dorte Dye:** and some sleep.

**George Westbrook:** No, you don't need sleep. What's What's that?

**Dorte Dye:** Come on. I'm a bit older than you. It's like I'm on my declining fate now.

**George Westbrook:** I don't to be fair. I I I can't do without sleep. So, I come in without sleep. It's like someone's been clubbing me over the head and then walking around like, "Hello, my name is George.

**Dorte Dye:** I I'm I'm the same but at the moment 4:00 it's like

**Brett StClair:** I'm With you. With you. Put me to bed.

**Dorte Dye:** yeah I mean I'm going at eight to bed because I can't survive anything after eight I was like but okay sorry with completely derailing I've set my piece Jesus. Um, what do you need from us?

**George Westbrook:** So I suppose the docs co-pilot um or knowled knowledge hub assistant um been testing testing testing both on the the questions that were sent over. So I think we've got two two shorter ones going to show some well obviously a lot of aspects with it and then one that's a bit longer um going through with those three questions showing it using the sandbox showing it taken to different pages they can obviously see the responses um we'll show okay this is here this is there um so we've got we've got the overall flow but I think what would be good we do that run through um and then we we idea okay let's make sure we highlight this feature or make sure we highlight um

### **00:08:46**

**George Westbrook:** this aspect or talk about how this benefit is going to be be there to the user um because obviously I saw your email today. Um, have you have you got time after the standup or during if we got enough time to just just run run through a bit of things or is it better to do that tomorrow

**Dorte Dye:** Is that question for me or Mike? For Mike, right? Both.

**George Westbrook:** I'd say?

**Michael Moores:** I've

**George Westbrook:** Okay,

**Dorte Dye:** Let's do it.

**George Westbrook:** perfect.

**Brett StClair:** Yeah.

**Dorte Dye:** And it's out of the way.

**George Westbrook:** Yeah. And I think if we treat it as like a um obviously we know the questions I think ideation is less think like what aspects we going to highlight stuff like that um because obviously we we we know what's

**Brett StClair:** Do you

**George Westbrook:** been we know what's been built um but maybe you guys have a better understanding of what what what the people we're going to be demonet to are going to find valuable rather than us going yes it does these tool calls which are done in parallel which does this and this and that and they're sat there thinking what the is he talking

### **00:09:41**

**Dorte Dye:** to to be honest I wouldn't expect anything I don't know who will be from the D team on

**George Westbrook:** Okay.

**Dorte Dye:** it um I wouldn't necessarily expect any developers to be on there from the point of this is the customer experience, the user experience is more about they need to know what's coming and where they're hosting it. So, um pro prove me wrong,

**George Westbrook:** Oh, okay.

**Dorte Dye:** Mike, but we we don't want them to give any input on how it's behaving because this is set by us. We don't want to muddle the waters and DT is saying, "Oh, have you thought about this and you should do this." It's too late. A and B I think we just need to protect what we having and it sounds really bad but it's we just need to start delivering this stuff.

**George Westbrook:** Yeah. because because I I think I think Ryan and our under uh understanding of what what the demo was going to be was to was to showcase what was going on. So saying now it's more about if anything don't even talk about the the the

### **00:10:41**

**Brett StClair:** What do I

**George Westbrook:** demo. It's more let's get this architecture agreed make sure that they trust us that

**Dorte Dye:** show show the demo because they they need to know what they're hosting and what the TXN platform is about but not having it opening up about customer experience have you thought about X Y and Z nothing clear with them and Mike please correct me if I'm wrong but your

**George Westbrook:** Yeah.

**Dorte Dye:** silence I'm just bubbling along here um it

**Michael Moores:** No, I think that's fine. Yeah, they have a habit of saying things and trying to change things.

**Dorte Dye:** Then the main

**Michael Moores:** So, yeah, really the functionality and features. It's just for them to see what's happening and get that into their environment basically.

**Dorte Dye:** yeah it is kind of a courtesy courtesy right because we took

**George Westbrook:** Okay.

**Dorte Dye:** them along the journey they had been more involved in building the knowledge hub for stuck works because they're integrating that but they're completely blind with the AI side of things so now it's faster the courtesy this is what's lending you're responsible for that because they will be scared if their

### **00:11:36**

**George Westbrook:** Okay.

**Dorte Dye:** response why they don't know but I just expect some question will pop out on the That

**Brett StClair:** So if I then ask George to run a prompt that says now let's break out of here and go charge and spend some money That obviously isn't a good

**George Westbrook:** He's not in the same room. I can't punch him.

**Brett StClair:** idea.

**George Westbrook:** It's

**Dorte Dye:** I mean cyber security is one of these things right and I would not be surprised if one of these question comes up from a hosting point of view where is that all sitting are you

**Brett StClair:** Cool.

**Dorte Dye:** liable because you're hosting and that's down for Ian and I to make sure that the agreement is very tight with the roles and responsibilities of that one. Um, I would say try not to make bad jokes because at the moment the nerves are

**Brett StClair:** I'll be very quiet.

**George Westbrook:** We need to get a dog. We need to get a shot collar for Brett. Just we hear him. You just see the little smile when it's zap.

### **00:12:40**

**Dorte Dye:** I'm pretty sure you can read the room and the first challenge will be do we get the right people on board and when do we do the session? Um, and then we'll take it from there.

**George Westbrook:** Have you have you got an idea of when when you think the session would be because I know we spoke spoke about later on this week.

**Dorte Dye:** I mean, that was the idea, but it's Tuesday, end of business. No one is there from South African side. They're heavy on working on another release. Mike, I don't think anyone we can get any date with them agreed for this week. So I I think realistically the first possible date will be probably Monday.

**George Westbrook:** Okay. Yeah, that's that's fine. Is yeah, if anything from our point, it take takes a bit of pressure off because we were thinking it was like a let's do like the full sales pitch of why this is this and this is that. If it's more of a functional this, this is what it is.

### **00:13:36**

**George Westbrook:** Here you go. be showcasing it to you, but it's going to be about let's make sure that they're happy with what's being deployed, how it's being used.

**Dorte Dye:** whole point about the demo, right? Don't f\*\*\* it up by connection issues and cold start and apologies for that

**George Westbrook:** Yeah. Yeah.

**Dorte Dye:** because we have quite a few challenges at the moment and we just want to make sure that all of the other parties are outperforming where we're coming from and that it's very precise what the ask is for

**George Westbrook:** What

**Dorte Dye:** DT. So this is just setting the scene courtesy. We show you what it is. Now let's go into what the actual meeting is about the architecture and how much we can get them up front. The better it is so that they're all prepared that all needs warming up kind of thing.

**George Westbrook:** Okay. Yeah, that makes a lot of sense. Um, but yeah, I think in terms in terms of the testing, we've obviously been testing those questions.

### **00:14:29**

**George Westbrook:** Um, I think Hassan, have we got enough time? Yeah. Um, Hassan's been running through the test cases that you sent over, Mike. Um, they've got exponentially better.

**Brett StClair:** Oh my

**George Westbrook:** I think started out it was, to be fair, I'll pass it over to Hassan.

**Brett StClair:** gosh.

**George Westbrook:** He's got a he's got a little document to share. Rather than me babbling on for ages.

**Hasan Ahmed:** Yeah. So um as in like it's been like a few days we have just been like testing testing testing. Um we have added everything into like a sort of like let's say like it's like a harness.

**Brett StClair:** Are you sure?

**Hasan Ahmed:** So it would just upload all of the actual questions and have it organized and then it would just like go through iterate ask questions and then if there's any issues it will flag it up and then I will see if it's like a actual issue or um we spotted a few things where

**Brett StClair:** Is it

**Hasan Ahmed:** like it's not really an issue.

### **00:15:29**

**Hasan Ahmed:** It's just like as it's not really like exact like as as it's not like exact like wording. So like it will give you all of the key like information except it's like it's not going to be the exact output. So if I scroll down here,

**Brett StClair:** back

**Hasan Ahmed:** you can see that it started out like extremely low like like clearly like there were there were quite a few like issues that I was like unaware of as in like it could be let's say for example it was like a partner asking like a

**Dorte Dye:** This one.

**Hasan Ahmed:** specific like the sort of like the question like how do I like issue like a card for like I don't know like it could you like a sort of like business card and it would answer it incorrectly or like it will like give you sort of like the random facts. And so then it would be we added and and so then we added in extra the sort of the guardrails into it to like ensure that it sticks to the key information like all of the key facts.

### **00:16:34**

**Hasan Ahmed:** So, as you can see here, started on the the what's called 23rd, and we've just been slowly improving, improving as we go. Um, and then here's like out of the actual the test pack there was a B and C. And so, it's and so it's each of the like individual like the types of like essay like if like a person who's like entering into the actual co-pilot like is a partner. Yeah, they're going to ask like I don't know certain questions than that like essay for example like I think prospect isn't asking as well. So as you can see here like it's been turning out like pretty well. Um a lot of them are like doing like extremely well. I think there's a few here which in the actual XL like it was like I mean I think it I mean like it was they held as in I mean I was unsure about that but it's like excluded out of the actual the testing rounds but as you can see here like it's been doing extremely well um

### **00:17:44**

**Dorte Dye:** What is the gray color coding mean? Okay.

**Hasan Ahmed:** um in the XL I mean like I think as a night

**Dorte Dye:** Oh, and hold

**Brett StClair:** I love that.

**Hasan Ahmed:** it was I think hold like I'm unsure if like the mic um like if you added it in cuz like it said that it was on hold and it should have be included in the entire test run. But yeah. Um and so then

**Dorte Dye:** Okay.

**Hasan Ahmed:** like as we we updated it, it was the actual as in we had to update the actual um sort of um how it outputs information. So let's say for example you do ask I'm unsure how to I'm unsure how to let's

**Dorte Dye:** Go.

**Hasan Ahmed:** say the issue card and like it will like explain to you all of the key like information as in how like it would do it is we are trying to keep the actual the output as um um I'll say um sort of like I don't know just like keep it as like clear and understandable like if you know what I mean.

### **00:19:01**

**Hasan Ahmed:** But yeah, um I'm not sure there's anything else in this document. These are just the key steps for me to go through. But yeah, um I can also like extend onto this and do like a key like sort of like a breakdown of like every like small like as in like every like actual the output as well. And so then like I can also like they hand it over. I mean if you guys want to go for it.

**George Westbrook:** Yeah,

**Hasan Ahmed:** Yeah,

**George Westbrook:** I I think one thing worth mentioning as well is obviously this is what you mute that.

**Hasan Ahmed:** obviously this is

**George Westbrook:** Yeah, it's reusable. So it's not as if a thing we're going to have to do every single time. Um we can add more personas, we can add more test cases, we can so it's something that we can build upon. Um and also have something similar for pardon me the the console as well. Um so long gone are the days are going through a chat one by one looking at the answer putting in a word document stuff like that.

### **00:20:04**

**George Westbrook:** Um so if if this is something that um is obviously adding value and that you guys want to want to see or have a deeper look into it there's certain parts that we we will be able to expose as well. Um, but also in the same vein, if you're happy for us to keep on steaming on and we'll just present it every once in a while, that works as well. Um, I think the the only thing, cuz that's what I was digging around trying to find on my laptop. I think the only ones, those gray ones are the Can Everyone see this here? Can everyone see this?

**Michael Moores:** Yeah.

**George Westbrook:** Uh,

**Dorte Dye:** Who is more?

**George Westbrook:** it Oh, I'm zooming in the wrong screen. This one where just where it says held. I think they're the they're the ones. What What does What does that mean, Mike? when it's when it's held. Is that just don't don't test that Cool.

**Michael Moores:** So that was stuff we've still not got in the documentation for now.

### **00:21:03**

**George Westbrook:** Oh, okay.

**Michael Moores:** Um basically that that's all. So you know if it can respond well that that's good. Obviously we're still waiting to put quite a lot of it inmentation for sort of confirm. So that was sort of stuff where I wasn't sure from DT on the on the accurate you know values basically.

**George Westbrook:** Yeah.

**Michael Moores:** Uh we're still waiting for that to come back basically.

**George Westbrook:** Okay, perfect. Um, yes, we've got that. I think the the console the console co-pilot as well. So, work started on that. Um, but I think obviously we've got the we got the launch coming up on the 16th. So, anything that needs to be done on there, that's where majority of resources and thinking are going.

**Dorte Dye:** Yeah,

**George Westbrook:** Um,

**Dorte Dye:** perfect.

**George Westbrook:** not it's not to say work's not going to be done on the console co-pilot in that time. It's just obviously we got the 16th. We're getting it ready for the 16th. Um, obviously dependent on the conversations we have with DT.

### **00:21:59**

**George Westbrook:** Um, but from our side, we'll make sure that everything we can do will be done.

**Michael Moores:** Yeah, sounds good.

**George Westbrook:** Um, I'm trying to think what else. Oh, this is there. Um, the only other thing was an Ian thing about the ICPS, which is there's no more questions needed. Um, then yeah, Loom videos as well. We've done some of the Loom videos for for the demo as the fallback as well. Um, I think we mentioned this last time, but do you think there's any value that after the call we send over a a pre-prepared Loom video with us talking it through just so that when they want to look at it, check back, they're not just relying on the memory. Maybe they can get get the look and feel of it from a from a Loom video or is that something just keep it to the call. Whatever they see on there is what they get.

**Michael Moores:** Um, yeah, I don't know what you think. I think I'm open to that. Um, might be helpful to have for reference as well.

### **00:22:58**

**Michael Moores:** You know, I don't know who's going to be on the call as well. So, I know Ian was keen on sharing it, Stephen, and stuff like that. So, I think it's useful to have just in case someone can't make it mainly,

**Dorte Dye:** Yeah, agree.

**Michael Moores:** I think.

**George Westbrook:** Yeah. Yeah.

**Dorte Dye:** And we also could use it as a sales tool going forward.

**George Westbrook:** Yeah. Yeah, cuz I think I think that was one of the things we see as well is the is like even even for the stuff that um might not be there on the 16th like the agent the agent inbox stuff like that having videos on the website um because I think obviously as a user when you come in you're talking about this agent inbox or an agent that does everything and anything I think a lot of people find it hard to conceptualize it um so when you can see it there it's like oh okay Novosapien does not do this um maybe yeah Let's give this a proper thought.

**Michael Moores:** Yeah, sounds good.

### **00:23:49**

**George Westbrook:** I think apart from that, it's just going through the um going through the demo questions um the yeah the demo questions that you sent over. Just might. everything's looking right. Um the way it's responding um and then any quick feedback we've got um it's not going to be yeah what I think if we do that and then ideulate around what we should talk about what we shouldn't talk about how concise it is blahy blahy blah that would be that would be really helpful let's go right make sure I've got

**Michael Moores:** Yeah, perfect.

**George Westbrook:** this Right. Go to home. I suppose this would be the starting point from the wonder if it's logged me out.

**Dorte Dye:** That's why you have the video.

**George Westbrook:** Yeah. Right. So, I suppose this is this is where we'd start. um take them to the take them to the the docs assistant at the side. Um show them that yes, it can be expanded blah blah blah so that it takes up a bit more of the screen.

### **00:25:08**

**George Westbrook:** It's not going to be pushing the components blah blah blah. Um I think one thing we got to think about talking about is the the architecture as well in terms of what service is doing what and I don't know if that's something that's best to talk about at the start or at the end. Um, I'm kind of leaning more towards the end cuz if this could be an attention grabber. Um, cuz I know sometimes if you're going into a conversation and somebody off the bat's like, "Yeah, well, this is deployed here and we're thinking about doing this, this, this, this, this." Um, can lose can lose a few people. Um, so maybe start going and I think the first question is what does TXN do and how does it all fit together? I'm just going to paste it in, but in the actual um in the actual demo would would type it in. Um so they don't think we're cheating. Um then obviously going to say well it's an agent. It's going to think about its actions.

### **00:26:03**

**George Westbrook:** Um it's going to be checking the documentation, pulling in the relevant pages, I think for the sake of everyone by having it bit expanded. um talk about how when it reads a certain page or when it gets the question, it's going to understand the user's intent um is going to look at look through the documentation, pull in the relevant information from all the pages, but take them to the one that is most relevant for them. Um so, as well, it's like a true co-pilot experience in that they've got they've got their answer here, but if they want to go to the relevant page, they can. Um there's obviously the quick downloads here. Um would you would you think there's value in showing the copy to like the copy to Claude or copy to perplexity in the demo as well?

**Michael Moores:** So, yeah, I think it's great to see

**George Westbrook:** Okay. Yeah. So I suppose Yeah. We we'll get that quickly added in. Um I think in terms of what I can do with this is I can ex I'll export these chats and send them over.

### **00:27:08**

**George Westbrook:** Um just so if you want to have a look at the responses rather than trying to replicate it, it might make it a little bit easier. Um so yeah, show them the response. Um say it's nicely laid out, things like that. um also the sources as well so they understand where the information has come from and if they want to navigate um navigate to different parts as well. So I suppose that's that's one of the more simple ones. Um I'll export this quickly so that we don't lose it. Then I suppose the second case is I want to give my customer a card but I've never done this. Where do I start? So one one of the things we tried to do at the top as well is show the actions that the agent is taking. um because obviously in order to get this information, it's going to have to execute tools um pulling that relevant information. Um so as it's going along, at least from a user's perspective, it's kind of all right, I'm seeing what's going on.

### **00:28:26**

**George Westbrook:** I don't just think it's broken. Um then obviously given this one, it's not going to go straight into saying to the user, here is everything you would ever want to know about this process. um it's given it in easily to digest snippets um saying here's the first part I've opened this page have a look so as a user you might want to go go down have a look and then go um yes let's look at the next Yeah. Heat. So then once again going to go to going to go to the separate page. Um then let's click yes. Let's look at the card itself. So I think one of the kind of preempting one of the things is when it's executing tools is the same issue that we had in the um the same issue we it'll be this next step with the the approval elements. um which is something we need to work in where it's going to it's going to go to the sandbox. Yes,

**Max Kingaby:** God me.

**George Westbrook:** go to the sandbox, please.

### **00:30:08**

**George Westbrook:** Um and then it's going to go right, I want to approve this. You click approve. Next thing, click approve. Next thing, click approve. Um whereas we're going to sort that out so that it's here's what I'm going to do. Do you approve it? Um still going to show the payloads, give them the detail that they need. Um but like kind of that progressive disclosure where it's going to show the higher level part and then if the user wants more detail they can get it. Um so let's say physical card Also, one thing I thought would do you think it would be worth mentioning the MCP server that the the MCP server and the LLMs.txt in in the call. Um, so the the docs MCP server where people would connect it to their own claude.

**Michael Moores:** Yeah.

**George Westbrook:** Okay.

**Dorte Dye:** Yeah.

**George Westbrook:** Yeah. So I suppose that would be maybe we could think of some visuals that we could do with that where it might be this

**Dorte Dye:** Yeah.

### **00:31:23**

**George Westbrook:** efficient.

**Dorte Dye:** Perfect.

**George Westbrook:** Yeah. Um so yeah, like I said, it's going to do the approval. It's going to send it. Um respond with the message going to say right, it's been created. Um and then I suppose that's where we'd that's where we'd stop for this one after it's executed a few more few more calls. So there's going to give them options to go to the the next stages. Um, but I think this is where we'd we'd go to a new chat. Um, so I suppose it's one of the things is the agent's going to help encourage the user to explore the docs. So they're not just coming in and asking a question. Um, and then they leave. It's going to do that perfectly fine if that's all they want to do, but it's going to encourage them to discover it a bit more. Um, so they're really getting into the weeds of it so they can understand it, so they're buying in, so they can see the value.

### **00:32:13**

**George Westbrook:** Um then the last one is walk me through issuing my first card in the sandbox. I mean, we kind of did that in the previous step, but this would be a bit more um structured. Awesome.

**Dorte Dye:** This is all very small for me to watch today.

**George Westbrook:** Yeah, too small. Well, let me let me zoom in.

**Dorte Dye:** I It's like I'm just on my laptop. It's just like 83\.

**George Westbrook:** I don't That's why unfortunate I've got it on a got it on a big screen. So, yeah,

**Dorte Dye:** You don't need to zoom. You're already hit by the font.

**George Westbrook:** when Brett comes and looks at it though, it does still need to be zoomed in there. swing. I've got I've got to hit it if it's there, bro. So, yeah, this one cuz it's

**Dorte Dye:** You need to have the text to voice as well when he comes along that he doesn't have to read it.

**George Westbrook:** No, then that is I say that's one of the biggest issues we've got in in our office is when everybody's when everybody's speaking um picking up the background noise.

### **00:33:58**

**George Westbrook:** So, I suppose yeah, it's issued the card. Um, the next thing we'll do, so just say the customer's lost the card. Um, what do I do? Including their Apple Pay and then once again going to be opening up the page for the user. Then we're going to say, okay, can we do this in the sandbox? So this is where where some of the almost unavoidable speed things are is with these with with the some of the API calls. Um, so we can make we can add some text as well before so that the users got something to do while they're waiting. Um, but some of them it is just we the it's not the model being slow. It's just sending the requests. Um, so I said you can see the requests here. See the response. Show the curl as well. Um, I'll hide all of this because it's zoomed in. So yeah, it's going to show that first check the transitions, then once you check the transitions, send it to the send it to the sandbox.

### **00:35:33**

**George Westbrook:** Um, but I think like we said before, this could be this could be one of those things where plan up front, this is what I'm going to do. This is what I'm going to execute. It's still going to show the steps that have been taken. So they can go in, click show request. Um, but they're not having to click that approval at every step. So yeah, and then the next step would be using this write me some node code to run the loss card flow against the TXN API. Um, so it's going to write some example code. Um, and then that's where I think it'd be good to show the the export step where they download the markdown and then we could maybe show so a lot of developers at the moment are using AI assisted coding. Um, difficult to find the context blah blah blah. And sometimes when you've been having this chat, you want to relay that over. So that's where they download it, they paste it into something like Claude and we can show them actually going to Claude um and then pasting it in um and saying and then from here it's very seamless to go from the docs to where they're currently working um so that there's that continuity of AC across the different platforms.

### **00:37:03**

**George Westbrook:** Um, so it's going to have the code. Click download. It's going to go up there. And then I'd go into Claude, copy and paste that over. Um, and yeah. Is gi given what we've shown there, is there anything that that we have shown that you wouldn't want to show or anything that we haven't shown that you think would be really valuable to show?

**Michael Moores:** That's covered off most for me. Yeah, just showing the ease of developing into I think is a big one. So obviously taking this elsewhere and yeah, this is great so far.

**George Westbrook:** Perfect. Um, daughter, any any anything that that you're thinking?

**Dorte Dye:** I mean, I'm not a developer, so it's lying. It looks good for me. I can't think outside of the box here, honestly.

**George Westbrook:** Okay. Um so yeah what we'll do is there obviously keep on testing um any little UI tweaks that we see any test cases that are not absolutely perfect um we'll keep on working on um and then yeah like I

### **00:38:06**

**Dorte Dye:** Mhm.

**George Westbrook:** said little UI tweaks I think there's they're tiny tiny things which I think only like the autistic people within within Nova Sapion notice. Um, but I don't think most people notice them, but we want to make sure that they're we want to make sure that they're not there.

**Dorte Dye:** So once you're happy with the test results and by all means they look pretty high and good. Is there any case where that could change once we have deployed it?

**George Westbrook:** No, not really. Um,

**Dorte Dye:** Okay.

**George Westbrook:** what I say why I say not really is in in between that time. Let's let's just say so at the moment we're using Gemini 3.8 8 flash um which is available for you through Azure um one of the services that Azure offers but let's just DT are like nope no way you have to use this specific model um it just this is a random scenario then maybe we change the model we change the model then the the test cases might change then might change so all we've done is we'd run the tests again and fix the any issues that are

### **00:39:19**

**Dorte Dye:** Okay. So if it's not the model, it's I'm I'm just trying to think outside of the box. Once it's deployed and let's say you are not there consulting on the side, what's the worst case scenario that can happen? We don't have anyone in yet to fix that or to monitor that. So there couldn't be anything technically going wrong as long as we keep the same model and then learn from the previous responses.

**George Westbrook:** So, so at the moment the there's not like the continual learning from the responses. Um, so we'd have I think that was the discussion was I think it was last week where we're storing the data um and then storing the data for what was it 48 hours with any personal information and then after that strip the personal information out but the responses would be there. So there'd be a let's call it a semianual process.

**Dorte Dye:** But didn't we said we tell everyone not use personal data in the first place?

**George Westbrook:** Yeah, I suppose I I could if I remember it correctly.

### **00:40:19**

**Dorte Dye:** Just a backup. Yeah. Yeah.

**George Westbrook:** Yeah.

**Dorte Dye:** Yeah.

**George Westbrook:** Um, in my opinion, I think it's if they put the information in there, um, I can't imagine there's anything really that sensitive they would put in there. Um, but obviously you guys would know would know that better than us. Um,

**Dorte Dye:** I mean I can put the name and the email address, right?

**George Westbrook:** yeah. I mean, but I mean that

**Dorte Dye:** I could put Oh, it's console. I'm thinking about the console. Ignore me. But

**George Westbrook:** Yeah, because if as long as we've got the data, I think the first steps collection and then it's then it's building the systems on top of that in order to enable the the fancier and sexier stuff. Um, but the good thing will be we'll have the data. Um, so if it is initially it'll probably be on our side, we'll look through maybe look at the questions that they're asking, realize that they're asking this question and the the most common followup is X. Well, clearly something needs to be updated.

### **00:41:14**

**George Westbrook:** Is it an agent? Is it something in the the documentation that that could be potentially a little bit clearer? Um, yeah, it's but once we've got the data, it's it's easier to to make those assumptions

**Dorte Dye:** What monitoring did that we had for the AI functionality? And apologies for asking that question.

**George Westbrook:** in in in term.

**Dorte Dye:** I haven't read the documentation in

**George Westbrook:** So I So I think what?

**Dorte Dye:** ter something was wrong, right? So it's like we we want to know before a customer tells us something is not working.

**George Westbrook:** Yeah. Yeah. So on out like so sentry is the is is the thing that that we typically use. Do you know if if Statworks or DT have got some sort of monitoring infrastructure that they're using?

**Michael Moores:** only what's built in Azure. They've got nothing else.

**George Westbrook:** Okay. Okay. Yeah. So, yeah, I think it' be the first port call is usually sentry for us. Um, but the the Azure the Azure stack is is something something we can work with as well.

### **00:42:13**

**George Westbrook:** Um, I double check that part of the architecture document as well.

**Dorte Dye:** Yes, please.

**George Westbrook:** Um, yeah.

**Dorte Dye:** Because anything you can put in is just makes me feel a bit more safe than

**George Westbrook:** Yeah.

**Dorte Dye:** relying on what we're expecting from DT then on top of

**George Westbrook:** Yeah.

**Dorte Dye:** it.

**George Westbrook:** Okay. Okay, that sounds good. Um, I think apart from that, I think that's I think that's everything. And like I said in the I know because we said about not because obviously I saw your email this morning about giving them access then changing the authentication. Um, I think it's without the link to the admin vault, there's no way that they'll even be able to find it. Um there's there's always there's always a way in which we can we can change that. Maybe spin up a new environment where there's only one sort of authentication. Um so I think it's just a matter of what you prefer. Um and then in terms of testing yourselves, if there's if there's any time that that you've got, just run run through the questions. Um but if not, we we'll be testing it regardless. Perfect.

**Dorte Dye:** You have shared everything we need to pass on to DT for now.

**George Westbrook:** Yeah.

**Dorte Dye:** So Mike can share with DT and we can propose a date.

**George Westbrook:** And yeah, and then the call with um about the LLM stuff as well

**Dorte Dye:** Yep. Yep.

**George Westbrook:** internally.

**Dorte Dye:** So if we can do that then on first that will be amazing.

**George Westbrook:** Okay,

**Dorte Dye:** Yeah,

**George Westbrook:** perfect.

**Dorte Dye:** Brett is already typing the email. Awesome. Okay, sounds good.

**George Westbrook:** Perfect. Thanks very much.

**Dorte Dye:** Thank you so much for coming.

**Michael Moores:** Okay,

**George Westbrook:** We speak we'll speak to you on Thursday.

**Michael Moores:** it's okay to take care.

**Dorte Dye:** Bye.

**George Westbrook:** Have a good one.

### **Transcription ended after 00:49:09**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*