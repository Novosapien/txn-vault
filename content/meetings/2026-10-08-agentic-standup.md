---
date: 2026-10-08
type: standup
description: "Hasan demos the co-pilot alone: it navigates the docs itself, history lives in the browser and clears at 30 days, and the skills list becomes a shop window"
scope:
  - "[[developer-support]]"
  - "[[commercial]]"
  - "[[txn-api-reference]]"
status: extracted
extracted-to:
  - "[[portal-co-pilot]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-08)

> **Source:** Gemini transcript, 8 October 2026, 15:28 BST, 32m. **Hasan Ahmed** and **Brett StClair** with **Michael Moores** and **Dorte Dye**. **George absent**, unwell since returning from Bali. Brett joined late.
>
> **A light call**, and a demo rather than a status round. Half of it is banter. The substance is a co-pilot walkthrough, two decisions and one design choice that helps TXN's legal work.
>
> **Hasan ran it on his own**, pushed into it by Dorte when Brett had not arrived: *"grow some balls. If it goes [wrong], you learn. Seriously, you don't need Brett and George. You learn more when you do it on your own."* He had been hesitant, *"I was assuming that there were also going to be other questions which I'm not sure I can answer."* It went well.

## The co-pilot, as demonstrated

Everything promised on 6 October is now working, plus more.

### It navigates the documentation itself

Asked *"how do I issue a card"*, the co-pilot answered and **opened the relevant API page**. Dorte checked whether that was Hasan or the software:

> **Dorte:** *"Did you open the create a card page, or did the AI do it?"*
> **Hasan:** *"It was the AI that did it."*

Same again for *"how do I list cardholders"*: it navigates, then explains what is on the page. This is the page-navigation feature George described two days earlier, delivered.

### The rest of the surface

| Feature | State |
|---|---|
| **Example payloads** | On request, with a **copy button on each example** |
| **Chat history** | Behind a clock icon, with previous conversations browsable |
| **Export** | To clipboard or download, as a **handover document for another AI**: an explanation of how to use it, a summary, **all the sources**, and the full transcript |
| **Animation** | Brett: *"I do like the animation"* |
| **Execute API calls** | **Next.** The agent runs the call and shows the payload and the output |
| **MCP server** | **Still being built**, to be integrated into the co-pilot after |

**The export format is the part worth noticing.** It is not a chat dump. It is built to be pasted into Claude, Gemini or ChatGPT and be useful there, carrying the sources and a usage note alongside the transcript. That is the same instinct as the portal export features Michael specified on 29 September, applied to the conversation rather than the page.

**Reception:** Dorte, *"I just want to play with it."* Michael, *"I think it's great."* Hasan offered a testing link.

## Chat history lives in the browser, and it solves something for Dorte

The most useful thing in the call, and it was almost incidental.

> Hasan: *"It's not really stored in a database. It's **stored inside the browser cache**. And so then **after 30 days it will just automatically clear itself out**. And then if you were to sign in, if you want to store them indefinitely, it can be an option as well."*

**Dorte's reaction:**

> *"It's brilliant, because this goes to my bloody privacy policies in terms of views and all of that malarkey."*

**Why that matters beyond the compliment.** [[open-questions]] #103 records that Dorte has to assemble the data facts herself before going to external counsel, once. An unauthenticated co-pilot that keeps nothing server-side and expires at 30 days is **far less to declare**: no new data store, no retention schedule to negotiate, no subject-access route to design for anonymous visitors. The build choice has reduced her legal surface rather than added to it.

**It also aligns with Michael's position from 6 October** that the public sandbox is kept *"for a very short window of time"* and the per-user store arrives with sign-up as a later phase. Both halves now say the same thing: nothing persists until someone signs in.

**She has more to come:** *"I have a big list of questions."*

## Two decisions

### The assistant does not get a name

> Dorte: *"I was just thinking about naming it. **I don't think we need to name the assistant at all**, because everyone calls it [something] anyway. This does the trick."*

Small, and worth recording because it closes a question that tends to resurface. No branded persona on the TXN side, in contrast to Novosapien's own **Nova** in the Content Workforce.

### API versioning is accepted

Brett, answering Michael's outstanding question: *"on your API versioning question, I think that's all fine. Happy."*

Michael: *"That's great, I'll go back and tell them. They say they're still working on that... Stackworkz are happy. So long as you're happy as well. **I think it gives everything we need from a this is the latest versus whatever version.** So I will let you know when that's actually out and we can start testing that."*

**So DT's proposed versioning model is now accepted by all three parties**: TXN, Stackworkz and Novosapien. It is **not built yet**, and testing waits on DT shipping the endpoints. That advances [[open-questions]] #101 from unsolved to agreed-and-pending.

## The skills list becomes a shop window

A short exchange with a larger implication. George had sent Michael a breakdown and clustering of the agent's skills. Michael needs Ian on it first:

> *"He was the one that spotted it on Perplexity's site. They've done an integration with MX, and **he doesn't want to download them at the start, but he wants to show what type of skills we have in place, to sort of show them off as well.** And [create] that from the start. We'll have a look at what we can do to show them off, or group them into business logic."*

**So the skills catalogue stops being internal plumbing and becomes a marketing surface.** Ian's reference point is Perplexity's MX integration, where the available capabilities are published as a visible list rather than discovered by use.

**Two consequences.**

**It needs grouping by business logic, not by tool.** A list organised around API endpoints is an engineering artefact; a list organised around what an operator can get done is a selling document. That is the same translation [[tool-catalogue]] already does in one direction, business-language wrappers over endpoints, now needed one level up.

**And it is the third thing pointing the same way.** [[open-questions]] #90 says every feature needs to be demonstrable; #105 says the co-pilot should ship at launch because Marqeta leads with one; and this says the capability list itself is sales collateral. **The demonstrability requirement is becoming the dominant constraint on how this work is packaged**, not just on whether it works.

Raised at [[open-questions]] #106.

## A clarification worth keeping

Dorte was confused by a login screen: *"So logging into the... I thought there's no login in the knowledge hub."*

**Resolution:** this is **Novosapien's own replica**, in staging, so it has a login. Brett: *"This isn't your knowledge hub though, right? This is the knowledge hub we built out."* Dorte: *"I just got confused why we would log in in a knowledge hub... in the future it's publicly available, so it's not like the console where they need to have registration."*

**The real one stays public and unauthenticated at MVP**, as recorded at #91. The replica is the same relationship as `txn-console-react` is to the production Console: a surface Novosapien controls so the experiment has somewhere to run.

**Open on Hasan:** the co-pilot is not yet linked from the admin portal, reachable only by appending `/docs`. Brett asked for it, *"so everyone can go into the admin and access it from there."*

## Dorte names her own role in reviews

Said as a confession, and it is useful information rather than self-deprecation:

> *"Can I make a confession? The last time you demoed, I said to Mike afterwards, I'm glad you liked it, because **I could not follow**. But Mike needs to like it, right? **If Mike understands it, he's a happy customer.** And I just don't speak tech."*

**So the technical judgement on this engagement is Michael's, and Dorte's is a judgement about Michael.** That is worth holding when deciding how to pitch a demo: a session that satisfies Michael satisfies both, and a session pitched at Dorte's level satisfies neither, because she is not trying to evaluate the build.

It also explains the pattern in the record. Her strongest contributions have been about **consequences** rather than mechanics: the ring-fencing problem on 17 September, the demand for figures rather than feel on 8 September, the launch differentiator argument on 6 October, and the privacy observation above. None of those required following the technology.

## Findings and where they landed

| Finding | Destination | Action |
|---|---|---|
| **Co-pilot navigates to the documentation page itself**, verified by Dorte | [[portal-co-pilot]] | Recorded as delivered |
| Payload copy buttons, chat history, and **export as a handover document** for another AI | [[portal-co-pilot]] | Recorded |
| **Chat history in the browser cache, clearing at 30 days**, nothing server-side until sign-in | [[portal-co-pilot]], [[open-questions]] | Recorded; **reduces the scope of #103** |
| Executing API calls is next; **the MCP server is still being built** | [[portal-co-pilot]], [[docs-mcp-server]] | Recorded |
| **The assistant gets no name** | [[portal-co-pilot]] | Decision recorded |
| **API versioning model accepted by all three parties**, not yet built | [[open-questions]] | **#101** moves to agreed, pending DT |
| **The skills list becomes a marketing surface**, on Ian's prompting from Perplexity's MX integration | [[open-questions]] | New row **#106** |
| The login was on Novosapien's replica, not the real hub | [[portal-co-pilot]] | Clarified |
| Co-pilot not yet linked from the admin portal | [[portal-co-pilot]] | Open on Hasan |
| **Michael is the technical judge; Dorte judges by whether Michael is satisfied** | [[portal-co-pilot]] | Recorded as review context |

### Context, no action

| Finding | Note |
|---|---|
| Last month's invoice is paid | Brett asked Dorte to thank Ian |
| Hasan ran the demo alone for the first time, at Dorte's insistence | George unwell, Brett late. It went well |
| Dorte on DT's pace | Asked when the go-live dinner could be booked: *"at the current speed for DT, 2013"* |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Link the co-pilot from the admin portal | Hasan | Currently only reachable at `/docs` |
| Send Dorte and Michael the testing link | Hasan | Offered on the call |
| Discuss the skills breakdown with Ian | Michael | Ian wants them shown off, grouped by business logic |
| Tell DT the versioning model is accepted | Michael | Then testing waits on DT building it |
| Build the MCP server and integrate it into the co-pilot | Novosapien | In progress |

---

## Transcript

Oct 8, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:11:35**

**Dorte Dye:** Oh, one person more. No, not one person more. Same family just exchanged.

**Brett StClair:** My name's Lily.

**Dorte Dye:** Poor. Poor her. She called you and he ignored her.

**Brett StClair:** No, no coverage. I promise. And then when we walked out of in that whole area, we walked out of the thing and I'm like, "Ah, dude. Can't get hold of anyone. No coverage.

**Dorte Dye:** Whatever. Whatever.

**Brett StClair:** Purple

**Dorte Dye:** 1 hour.

**Brett StClair:** because you guys want to come with us, too." You want to

**Dorte Dye:** What?

**Brett StClair:** Let's go drink it. Set up a dinner or a lunch.

**Dorte Dye:** Your connection sounds really weird. It sounds like you're in a fish tongue.

**Brett StClair:** Ready? Oh, that's why. Yeah, my mic's Is that better?

**Dorte Dye:** your your mic is in the fish tank in your

**Brett StClair:** It's literally on my hip in my

**Dorte Dye:** coffee.

**Brett StClair:** coffee. Hello, Mike.

**Dorte Dye:** Okay, you're mute.

**Michael Moores:** Are you okay?

### **00:12:59**

**Brett StClair:** Good. My apologies for earlier today. It was completely unplanned and we thought we had plenty of time to do this and it turns out we didn't. And since then Dörtehas been taking the piss out of me.

**Dorte Dye:** What do you expect? I mean, it's like this month's invoice will be not paid.

**Brett StClair:** Exactly. On that note, please let Ian know thank you. The invoice was paid for last month that came in yesterday.

**Dorte Dye:** Oh. Oh. What he Oh, what he texted him was like, "We need a new supplier.

**Brett StClair:** That's it. Chances are done. Okay. So, let's get into it. I think key thing is we want to demonstrate where we are uh what's being built and go through what we are planning to do next. Is everyone okay with that?

**Michael Moores:** Yeah.

**Dorte Dye:** Who? Who's demonstrating? Hassan have you have to do it now. It's clear.

**Hasan Ahmed:** Yeah. No,

**Dorte Dye:** It's not bright.

### **00:14:05**

**Hasan Ahmed:** it's my turn.

**Dorte Dye:** And Georgeknock knock knock knock knock knock knock knock knock knock knock knock knock knock knock knock knock knock knock knock knock knocked out after the boozy lunch

**Brett StClair:** So po Paul po Paul George has been suffering from barley belly since he's been back.

**Dorte Dye:** barley belly sounds like pork belly

**Brett StClair:** I know he's not been a good way. He's like had this delayed Bali belly thing and we we saw him yesterday. He did come to the lunch thing and he was it's gray. It's like gray.

**Dorte Dye:** he really good on Tuesday and then

**Brett StClair:** He looked brilliant. literally went and went to the facilities,

**Dorte Dye:** after that. Are you sure that he just didn't had a cape up around the corner?

**Brett StClair:** came out sweating.

**Dorte Dye:** I don't think that has anything to do with Bali. Seriously.

**Brett StClair:** I don't know. He's blaming it on Bali. So, he bought our our medical pack. So, we took this medical pack. So I'm used to traveling with teams all over the craziest worlds and I bring in medical packs with everything and I think half the team were laughing at the fact until everyone got sick in some way or form and was heavily reliant on the ingredients of that medi

### **00:15:13**

**Brett StClair:** pack.

**Dorte Dye:** So what is in a medieval?

**Brett StClair:** So how's how cool is this? I use claude. I said we're visiting this kind of space. I've done this many times before. I usually kit up with the following um kind of medical kind of stuff. I'm not sure what Bali will allow me to enter and what Bali will not have.

**Dorte Dye:** Okay,

**Brett StClair:** These are the diseases and illnesses that I want to make sure we cater for. Um please can we stock it? It went away, stocked it, loaded into my trolley on Amazon um business and all I did was hit buy and in over a week we just had hundreds of medication arriving. We loaded up the pack and took it to Bali. And then everyone's like having a good laugh until everyone needed

**Dorte Dye:** needed it.

**Brett StClair:** the right

**Dorte Dye:** So maybe that's a really good business idea. Create a website. We make a new travel kit versus my my daughter goes um on

### **00:16:13**

**Brett StClair:** travel good.

**Dorte Dye:** a trip to South Africa in 10 days. Maybe I should make a one for

**Brett StClair:** She needs liver pills.

**Dorte Dye:** malaria.

**Brett StClair:** No, for drinking.

**Dorte Dye:** She is 13\. You m for drink.

**Brett StClair:** Okay. Can Can I introduce you to Lily, who at age 13, her and her mates were literally robbing my bar at age

**Dorte Dye:** Yeah, but that's different.

**Brett StClair:** 13\.

**Dorte Dye:** That is absolutely different. I mean, I must say they're going on a sports trip. So, they're playing net ball and um cricket and they're going on a bloody fly

**Brett StClair:** Oh, wow.

**Dorte Dye:** zip which is like 200 m off the ground. It's like a why do they going on a fivestar holiday with the school and why they're doing I'm not letting them jump. Oh, I can't see.

**Brett StClair:** Where they going?

**Dorte Dye:** I'm emotional. I can't even say the zipline.

**Brett StClair:** Where they going? No. No. Uh, what schools are they playing?

**Dorte Dye:** So they're flying into South Africa to Cape Town.

### **00:17:16**

**Brett StClair:** Yeah. Okay.

**Dorte Dye:** Uh then they are in Stellenbush for some time and then they're going on a really posh

**Brett StClair:** Nice.

**Dorte Dye:** game reserve for two days as well.

**Brett StClair:** Oh, nice. And so it's h netball and cricket.

**Dorte Dye:** Five star. No, these two. No, no, just hockey and net.

**Brett StClair:** Hockey, net. Okay. Awesome. There's some really, really, really good hockey and net schools in in Cape Town. So, she'll have fun. It's amazing there. What a tour, man.

**Dorte Dye:** I know. I'm jealous.

**Brett StClair:** What a tour.

**Dorte Dye:** I I volunteered, but the teacher said I don't need anyone.

**Brett StClair:** See what my wife used to do. That's so Lily went on a also 13 she and on a tour to

**Dorte Dye:** Sorry, Hasan.Six. Sh and I take that offline.

**Brett StClair:** Holland. I think we should. So Martha went with Lily, but Lily got concussed and then started two weeks, three weeks after the concussion had fits and she was playing for the first team and was one of the youngest ever to play.

### **00:18:15**

**Brett StClair:** And so the first team were like, "No, we want to bring her." And we were worried. So Martha was like, "Screw your policies. I'm coming with you." So she went on a tour around Holland for two weeks. Literally the day before Lily went, I had her go plan all of the stuff in South African rans. Where you guys going? Can you not stay in a hostel, Martha? Anyway, Hasan,over to you. Otherwise, we can carry on going all day.

**Dorte Dye:** You could have said that Hasan.We could have had the call without Brettif you in charge.

**Hasan Ahmed:** Yeah.

**Brett StClair:** When I did arrive,

**Dorte Dye:** I'm really sorry about

**Hasan Ahmed:** I mean,

**Brett StClair:** when I did arrive, I was like, "f\*\*\* sakes, Hasan.Just do the bloody demo.

**Hasan Ahmed:** just do a lovely demo. Yeah. I mean, like I was like also planning on doing it, but but then I thought that there were I mean, I was assuming that that there were also going to be other questions which I'm not sure I can answer, but yeah.

### **00:19:12**

**Dorte Dye:** grow some balls. If it if it go s\*\*\*, you learn. Seriously, you don't you don't need Brettand George. You learn more when you do it on your own.

**Hasan Ahmed:** Yeah.

**Dorte Dye:** And we don't bite. I mean not right but

**Hasan Ahmed:** Yeah. I mean like I did like I mean I did actually learn like ages ago like after I did like the demo. I mean like the Brettknows that demo was quite shocking.

**Dorte Dye:** again that's how you learn.

**Hasan Ahmed:** Yeah. But Yeah.

**Dorte Dye:** Can I can I make a confession?

**Hasan Ahmed:** Yeah.

**Dorte Dye:** The last time as you demoed I said to Mike afterwards I'm glad you liked it because I could not follow. But Mike needs to like it, right?

**Hasan Ahmed:** Yeah.

**Dorte Dye:** If Mike understands it, he's a happy customer. And I just don't speak tech.

**Hasan Ahmed:** Yeah.

**Dorte Dye:** That's all it is.

**Hasan Ahmed:** Okay. Let me start this demonstration then. Um, okay. Okay.

### **00:20:10**

**Hasan Ahmed:** So, it's like a few like extra like smaller features we've added onto this actual co-pilot.

**Dorte Dye:** Is it just my picture?

**Hasan Ahmed:** Um is

**Dorte Dye:** Okay, now it's clearer. It It looked really fuzzy. It was like like I had something to drink.

**Hasan Ahmed:** so if we just start from let's say for example we ask this um let's say how do I issue a card and so if you ask about the actual and and I mean if you ask about the actual API spec. It will then take you onto that actual like API that page now. So it will then go through the entire guide. We can try to find what are the actual as an all of the actual API sources. And so then if we can give it a second. Yeah. And so then here like it'll be the actual thing. And so this is going to be the actual API page. And so this is how you can issue a card. Um it will have all the information that you need and then it it will also like explain to you like all of the key information in there as well.

### **00:21:22**

**Dorte Dye:** Did you open the uh create a car picture or did it the AI did it? AI.

**Hasan Ahmed:** Um like Yeah,

**Dorte Dye:** Okay. Yes,

**Hasan Ahmed:** it was the AI that did it. Yeah.

**Dorte Dye:** cool.

**Hasan Ahmed:** And so let's say um how do I list card

**Dorte Dye:** Cool.

**Hasan Ahmed:** holders? It would just automatically just I mean it should automatically take you. So if you just give it a second. Yeah. Here's the API automation and then it will explain to you again everything on the the actual page as well. Um and then we've added in so let's say you want an example payload. So, um, can you give me an example of a payload? Uh, give it a second. Um, I mean, I think it's on COD star right now, so it's going to take a bit longer to get through it, but um, see, there you go.

**Brett StClair:** I do like the animation by the way.

**Hasan Ahmed:** Take the elevation by the flashes and then stretches

### **00:22:38**

**Dorte Dye:** Um,

**Hasan Ahmed:** out.

**Dorte Dye:** I quite like that, I must say. And I was just thinking about naming it. It's like I don't think we need to name the assistant at all because everyone calls it B or whatever.

**Hasan Ahmed:** Yeah.

**Dorte Dye:** It's like this does the trick.

**Hasan Ahmed:** Yeah. And so yeah. Um, if I expand this out and then let's say for example on the this like example and payload if you want to copy it there's like a quick like a copy button like at the at the top of each like

**Dorte Dye:** Cool.

**Hasan Ahmed:** example option here. So here if you want to copy this one or if you want to copy this one I just click paste here it will have the entire payload just copied in. Um, then we also added in if you want to get the actual the chat history as well. So, if you click on this like the clock icon, it'll just have all of your s like pre previous of the chats and then it's stored in the actual as it's stored in the the actual um what's called as in as it's not really stored on like in a database.

### **00:23:58**

**Hasan Ahmed:** is stored inside the extra like browser cache. And so then after that 30 days, it will just automatically clear itself out. And then if you were to sign in and then I mean it is more more of like a future feature, but if you were to sign in, if you want to store them like indefinitely or store them somewhere like it can be an option as well. Let's look.

**Dorte Dye:** It's brilliant because this goes to my bloody privacy policies in terms of views and all of that malarkey.

**Hasan Ahmed:** Yeah.

**Dorte Dye:** I have a big list of questions. Okay. Like it.

**Hasan Ahmed:** And so yeah, if you were to go to an old chat here, you can just go through scroll through it. Or let's say for this one here, it just has all of the like actual the details. And then if you want to ex and then if you want to export as well onto either your like act of the clipboard or if you want to download it and then if you want to hand it onto like cloud or something um so after it exports I'll quickly show you the export itself and so like it's more of like a handover I think as in it's more like a handover as in like it's like a hand over like a certain

### **00:25:07**

**Hasan Ahmed:** document. So if I I don't know if I can zoom this in but like it'll just explain onto like any of your like AI like assistants or it can be clawed like it can be the Gemini the chat GBT it will just give like a explanation on like how exactly to actually to use it then it will have a summary and then it will have all of the sources as well and then the entire transcript of the actual chat itself. I mean, yeah. I mean, yeah. I mean, I think in terms of everything we've like added in there so far, like this is it like at the moment. Um, we are planning on adding in a like extra options. So I mean if you want to actually execute like um like any sort of as in like any sort of like the API calls as well like the actual agent can do it for you and it can give you the example like the payload and the like actual the output of it as well and then there's also the actual MCP server which we are still in the the process of actually getting it built out and then after we do that we are going to integrate that into this like entire the co-pilot as well.

### **00:26:41**

**Hasan Ahmed:** answer. Yeah. Um any questions or

**Dorte Dye:** I just want to play with it.

**Michael Moores:** Yeah, I think it's great.

**Hasan Ahmed:** um Yeah.

**Michael Moores:** Okay.

**Hasan Ahmed:** Yeah. If you want to have like a play around, I can give you the the testing link as well. And so then if he hitting sign in, in with the TXN I mean I think it's the like I if you want to access the actual um I mean I forgot the like exact the details it's like as if you were to access the actual the console like it's the exact same nothing like if you want to have a sign in it's like the exact same so difference Yeah.

**Michael Moores:** Yeah, perfect.

**Hasan Ahmed:** Is this on?

**Dorte Dye:** So locking into the I thought there's no lock in in the knowledge hub.

**Hasan Ahmed:** Um,

**Dorte Dye:** I'm now

**Hasan Ahmed:** so if I let's say if I just do this, it's I think this will go to the actual like entire console here. So if this loads

**Brett StClair:** Hasanis this on the admin portal as well.

### **00:27:55**

**Hasan Ahmed:** portal as well.

**Brett StClair:** So everyone can go into the admin and access it from there.

**Hasan Ahmed:** So go to the admin and access. Um I still need to add I mean I think I still need to add it onto there. I mean because all it is is if you are on this standard at the s page if you just add in I think it's the SL docs it will go to the the docs page and then on here it will have the agent.

**Dorte Dye:** Okay. So we we are on a knowledge hub and that's what I thought.

**Hasan Ahmed:** Yeah.

**Dorte Dye:** I just got confused why we would lock in in a knowledge hub.

**Hasan Ahmed:** Yeah.

**Brett StClair:** This isn't your knowledge hub though, right? This is the knowledge hub we built out.

**Hasan Ahmed:** We built out.

**Dorte Dye:** Yeah. Yeah. Yeah.

**Brett StClair:** No.

**Hasan Ahmed:** Yeah.

**Dorte Dye:** But I I meant in the in the future so it's publicly available. So we don't need it's not like the console where they need to have to have registration and everything.

### **00:28:49**

**Dorte Dye:** That's why it's because it's in staging,

**Hasan Ahmed:** Yeah.

**Dorte Dye:** right? So that's why you would give us a login on that one. Yeah. Yeah. Got you. Okie do.

**Brett StClair:** Then just a quick answer for you Mike

**Dorte Dye:** Looks good.

**Hasan Ahmed:** because

**Brett StClair:** on your API versioning question. I think that's all fine. Happy Abby.

**Michael Moores:** That's great. Yeah, I'll go back and tell them. They say they're still working on that. Um, but I think it's, you know, console team are happy. Sorry, knowledge hub team, stat works are happy. So long as you're happy as well. I think it gives everything we need from a this is the latest versus whatever version. So I will let you know when that's actually out and we can start testing that.

**Brett StClair:** Perfect. Perfect. Um, and then are you happy with the skills and the breakdown and clustering and everything that George sent you?

**Michael Moores:** Yeah, just need to chat over it with Ian.

### **00:29:45**

**Michael Moores:** He was the one that spotted it on Perplexity site. So, they've done an integration with MX and I think he he doesn't want to download them at the start, but I think he wants to sort of show what you know type of skills we have in place to sort of show them off as well. And that's creates from the start and we'll have a look at what we can do to sort of show them off or group them into sort of

**Dorte Dye:** Amazing.

**Michael Moores:** business logic and stuff like that. So, I'll go through that and have a look. Thank you.

**Brett StClair:** Perfect, perfect, perfect. Happy days.

**Dorte Dye:** Good

**Brett StClair:** Thank you everybody. And um I'm going to do another nudge. When you are officially live, can we plan a dinner or something after that?

**Dorte Dye:** at the current speed for DT 2013\.

**Brett StClair:** You unformed today.

**Dorte Dye:** That's just for people that missed the first meeting. No, we will we will get it done. Don't you worry.

### **00:30:45**

**Dorte Dye:** We will be in London. It's more my needs to come down to London. Ian and I are more often in in London actually.

**Brett StClair:** Okay, we're going to keep hustling until we get you guys down and then best get a place to stay, Mike, cuz we're going to drink you into the ground.

**Dorte Dye:** Oh, honestly, I won't really see who is more drink stable.

**Brett StClair:** Really?

**Dorte Dye:** I don't know how you say that because Ian is very petite, right? But he can drink. It's like that's Mike.

**Brett StClair:** Really?

**Dorte Dye:** I wouldn't expect anything less because Michael is like you. But it was hard.

**Brett StClair:** do how how's I was about to say how's your your

**Dorte Dye:** Last year was really hard to keep up with this too

**Brett StClair:** drinking capabilities?

**Dorte Dye:** at the moment. Zero.

**Brett StClair:** Zero really.

**Dorte Dye:** I was on drugs and I don't want to have the extra who

**Brett StClair:** Of course you were. You had a preferred alternative.

**Dorte Dye:** and I can't do anything. No, I mean like normally when I'm training I'm not drinking much but I can drink. Don't you worry.

**Brett StClair:** Yeah,

**Dorte Dye:** Sure.

**Brett StClair:** I had a feeling and the right steak.

**Dorte Dye:** It just needs to be the right drink and the right steak.

**Brett StClair:** Okay,

**Dorte Dye:** Then the right.

**Brett StClair:** so mental note, it's a Hawksmith or Hawks Mall or something like that.

**Dorte Dye:** Isn't that where we went last time, Mike?

**Michael Moores:** Yeah.

**Dorte Dye:** Literally next to the train station and everyone could buy. We just made it to the train.

**Brett StClair:** Oh, that's beautiful.

**Dorte Dye:** Yeah, it's forward thinking. Needs to planned.

**Brett StClair:** thinking.

**Dorte Dye:** Okie do.

**Brett StClair:** Okay guys,

**Dorte Dye:** Thank you so much.

**Brett StClair:** thank you very much.

**Michael Moores:** Thank you. You say to take care.

**Brett StClair:** Ta.

### **Transcription ended after 00:32:22**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*