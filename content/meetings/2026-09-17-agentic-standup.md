---
date: 2026-09-17
type: standup
description: "Short status standup: speed fixes land in two to three days, the MCP server starts, and Dorte asks how to ring-fence a build that keeps changing"
scope:
  - "[[full-agentic-experience]]"
  - "[[developer-support]]"
  - "[[delivery]]"
  - "[[content-workforce]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[docs-mcp-server]]"
  - "[[content-workforce]]"
  - "[[delivery-schedule]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-09-17)

> **Source:** Gemini transcript, 17 September 2026, 10:00 CEST, 13m. **George Westbrook** and **Max Kingaby** from Bali, with **Dorte Dye** and **Michael Moores**; Hasan Ahmed joined late, Tyler Thompson sitting alongside Max. Lily St. Clair in the office.
>
> **A short status call**, the day after the phase two discussion. George's own verdict: *"I think it's quite a short one today."* Michael contributed nothing beyond *"not for me."*
>
> **Read it alongside [[2026-09-17-dorte-feedback-review]]**, written the same day, which analyses all 41 of Dorte's written feedback records. This call is where she raised what that review's data quietly demonstrates.

## Two streams, running in parallel

Confirmed from the 16 September decisions ([[2026-09-16-next-phase-discussion]]):

| Stream | State |
|---|---|
| **Improve the agent** | Active. Speed and efficiency work |
| **Knowledge hub** | Starting. **MCP server first** |

George on the split: *"the two main things that we're going to be working on in parallel now are the stuff to do with the knowledge hub and obviously improving the agent."*

### The agent work, and a date

Three things in flight:

- **Frontloaded questions.** *"At the moment, say you want to suspend a card, it's going to ask you questions after it's executed like 20 tool calls. Just making sure it's getting that information up front."*
- **The SOPs, rewritten again.** *"I'd rewrote the SOPs from what they were originally, but there were still some things that weren't quite right. So it's just going through that process again."* That is the **third** pass: the original set, the 8 September rewrite, and now this one.
- **Specialised tools**, the composite tools agreed on 16 September.
- **Dorte's feedback** is being worked through alongside.

> **"Hopefully in the next two to three days a lot of those changes should be implemented and ready to test."**

That puts a testable build around **20 September**. It is the first date attached to the speed work.

**The agent inbox** *"should be working"*, but George wants attention on the agent itself for now rather than splitting the stream further.

### The knowledge hub work

**MCP server first**, and the first step is to use it themselves: *"working out how we're going to do that and get something built and tested on that front so we can all play around with our own Claude agents, and then that will bleed quite nicely into the co-pilot."*

**And an access request for TXN.** George: *"we're going to investigate Umbraco and we might need some sort of access there, so that we can have a look, so that we're not getting stale information and that it's constantly being updated."*

That is the hygiene requirement from 16 September becoming a concrete ask. It is on Michael, and he was on the call and did not respond to it.

## The finding: Dorte tested a build that kept moving

The most useful thing in the session, and it is a process problem rather than a product one.

> *"For me it's with the testing, because there were so many moving parts working in the background. **I didn't have one state of the build where I was testing against it, because things were changing.** So as I did [it] over a couple of days, things have changed again."*

> **"If we do another round of testing, how do we want to ring-fence it, that we have a true outcome?"**

### Why this matters more than it sounds

**It describes the conditions under which every piece of UAT feedback so far was produced.** [[2026-09-17-dorte-feedback-review]] analyses 41 records that Dorte filed on **21 August, 8 September, 11 September and 14 September**. That span covers the 8 September decision to strip out approvals, the model switch, and two SOP rewrites.

**And it shows up directly in that review's headline finding.** The review reports that between 8 and 14 September the agent made 68 writes and rendered zero approval cards, with the agent telling Dorte in plain words: *"approvals are disabled in this deployment."* **That is the deliberate strip-out from 8 September**, where George said *"we've turned off a lot of the approvals"* and would reinstate them by sensitivity and permission ([[2026-09-08-agentic-standup]]).

So the safety behaviour Dorte's headline feedback is about was **intentionally absent** during her testing window, and is being restored through the permission model agreed on 15 September. The defect is real and the fix is already specified; what the review cannot do is tell which of her 41 records describe the build as it will be, and which describe a build mid-surgery.

**That is the cost of no ring-fence**, and it lands on two things the vault already carries:

- **[[open-questions]] #51**, where Ian's and Dorte's verdicts are the evidence of record
- **[[open-questions]] #54**, where **acceptance now triggers on TXN finishing UAT**. If UAT has no fixed build, the trigger has no fixed meaning

Raised at [[open-questions]] #93.

### George's answer, which is half of one

Two commitments:

**1. Always test the production URL.** *"I know it seems a bit weird that we're calling it production, but the most up to date and the most durable and the best one to test is always going to be the production agent, and then testing will be for our testing."* He acknowledged the oddity twice: *"doing testing on production just seems weird, but that's how we're going to do it for the time being."*

This repeats the correction from 8 September, when Dorte had been testing in UAT.

**2. Tell TXN when a change is pushed.** *"It would be a lot easier if, when we're pushing up changes, we let you know, rather than you come in and suddenly [find] now it's doing this new weird behaviour."*

Dorte accepted and checked it with Michael, who agreed.

**What it does not give her** is what she asked for: a **known state** to test against. Push notifications tell her the ground moved; they do not hold it still. A tagged build, a short freeze during a test window, or a version stamp visible in the interface would. Nobody proposed one.

## The domains are unblocked

Dorte reported the sign-off she was chasing on 16 September:

> *"I just got a written sign-off from Pay Corp CTO that he's fine with what we agreed yesterday. So I'm just sending it back to Ian, and I will ask him for the naming convention as well."*

**So the approval Dorte corrected George about on 16 September has now genuinely arrived**, in writing, from Pay Corp's CTO. The remaining gap is the one she flagged: **Ian has not yet given the naming convention**, and domains were already purchased without it.

**Next step:** George will speak to **Alex** about getting the domains onto **Cloudflare**, *"what the typical process for him would ideally look like."* Then set up, warm, and start sending.

## Content Workforce

The session booked for later that day had a full agenda. Max: *"me and Tyler have sat there for some good time today. We've got a list of everything we want to go through on the call"*, with **five or six items** beyond LinkedIn, headed by **prioritising and aligning the entities**, which is Ian's blocker from 16 September.

### LinkedIn: nobody knows who owns it

Max asked to get the TXN business page set up that day. Dorte pushed back, and the exchange exposes a genuine gap:

> *"There was the miscommunication [about] who was doing it, you or Bronwyn. You didn't seem to recall, as we asked the question before. So I have it still as open."*

> *"Brett couldn't really remember, he said it's not a problem, you guys can do it. So let's bring that to Ian. What is his last take on it? Because for all I know, maybe Bronwyn has it already, because I made her admin and she's doing that in the background."*

**Max separated the two things usefully:** setting up a profile, *"a banner, a small bio"*, does not need the tone of voice. So the branding work is not blocked by the messaging alignment, only by knowing who is doing it.

**Dorte's constraint is the one to respect, and it is a platform fact:**

> *"It's all about timing. We don't want to put something on there if you're not ready to launch. **You don't have the not-publish option at LinkedIn.** So when you do a change, it is only visible."*

**LinkedIn has no draft state.** Anything published to the page is live immediately, to whoever is already following, which makes the page's first appearance a launch decision rather than a preparation task. Left to Ian on the content call.

This sits alongside [[open-questions]] #63, where Bronwyn's action to brand the page was recorded on 16 September with no completion date.

### A small friction worth fixing

Dorte has to verify her Google account every time she opens a document Tyler shares:

> *"When I want to open the link Tyler has sent, it always asks me to verify first. And this morning I just wanted to get everything open and I was like, oh, I can't be asked any more."*

**Two fixes offered:** George, share as *anyone with link*; Dorte, *"just send us a Word document or PDF, because I think that's what Ian prefers when he's reading this stuff, rather than he has to go into other applications."* Tyler agreed to send PDFs.

**This is the same preference Ian stated on 16 September**, when he asked for the messaging output as a PDF rather than branded HTML: *"I know you're working in an AI world, but I need this in a human world that can be shared."* Two people, two days, the same request. It is worth treating as the default for anything TXN has to read or forward rather than something asked for each time.

## Findings and where they landed

| Finding | Destination | Action |
|---|---|---|
| **Dorte has no fixed build to test against, and asked how to ring-fence it** | [[open-questions]] | New row **#93**, tied to #51 and #54 |
| George's answer: always test production, and announce every push | [[delivery]] | Recorded as a commitment, and as a partial answer |
| The approvals gap in Dorte's feedback is the **deliberate 8 September strip-out** | [[2026-09-17-dorte-feedback-review]], [[open-questions]] | Recorded in **#93** as the clearest instance |
| **Speed fixes testable in two to three days**, around 20 September | [[delivery]], [[open-questions]] | First date on the speed work. Added to **#87** |
| Third SOP rewrite in progress, plus composite tools and Dorte's feedback | [[agent-orchestration]] | Recorded |
| Agent inbox working; attention deliberately kept on the agent | [[agent-inbox-alerts]] | Recorded |
| **MCP server started, dogfooded internally first** | [[docs-mcp-server]] | Recorded |
| **Umbraco access requested from TXN**, to avoid stale docs | [[docs-mcp-server]], [[open-questions]] | Added to **#92**. Michael did not respond |
| **Domain sign-off received in writing from Pay Corp's CTO** | [[delivery-schedule]] | Recorded; the 16-09 correction now resolved |
| Ian still owes the naming convention; Cloudflare via Alex next | [[delivery-schedule]] | Recorded |
| **LinkedIn ownership unresolved**: Max's team or Bronwyn | [[content-workforce]], [[open-questions]] | Added to **#63** |
| **LinkedIn has no draft state**, so publishing is a launch decision | [[content-workforce]] | Recorded as a constraint |
| PDFs preferred over Google Docs links, by both Dorte and Ian | [[content-workforce]] | Recorded as a default |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Land the speed changes and make them testable | Novosapien | **Two to three days**, around 20 September |
| Announce every push to TXN before they test | Novosapien | Agreed on the call |
| Decide how to ring-fence the next test round | Both | Dorte asked; not answered |
| Grant Umbraco access | Michael | Asked on the call, no response |
| Send the naming convention for the domains | Ian | Dorte chasing that morning |
| Get the domains onto Cloudflare | George with Alex | After the naming convention |
| Confirm who brands the LinkedIn page | Ian | Max's team or Bronwyn |
| Send documents as PDFs rather than Google Docs links | Tyler | Agreed on the call |

---

## Transcript

Sep 17, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:20**

**George Westbrook:** That's me.

**Dorte Dye:** Morning.

**Max Kingaby:** Hello.

**George Westbrook:** And how are we doing?

**Dorte Dye:** All right. Lily is in the office. Nice.

**George Westbrook:** Yeah.

**Dorte Dye:** At least one one person is working and not holiday.

**George Westbrook:** Must excuse me. I will take I will take a picture of my setup to show you.

**Dorte Dye:** How many screens do you have? Did you have to bring them all?

**George Westbrook:** No, no, no. So we we found a place that where you can rent monitors. So you can rent them by the week.

**Dorte Dye:** Oh,

**George Westbrook:** So we've got if you see if you see our table, it looks pretty similar to our office where we've got like loads and loads of monitors set up. So

**Dorte Dye:** okay. That makes sense because that's what I don't like when you're away and you just have a portable one and just I can't work. I'm just spoiled. Hi. Hi, Mike.

**George Westbrook:** morning. How we doing?

**Max Kingaby:** I'm like,

### **00:01:37**

**Michael Moores:** That's

**George Westbrook:** Good. Good. Good. So, it's already 4:00 here. So,

**Max Kingaby:** Gosh,

**Dorte Dye:** That's when you normally start working.

**Max Kingaby:** this

**Dorte Dye:** So,

**George Westbrook:** it's I don't Well,

**Dorte Dye:** what are you complaining about?

**George Westbrook:** I'm having to get up a bit earlier. Not today, actually. I think I think my body's fighting to get me back into my old um old habits.

**Dorte Dye:** I mean, you getting up at 7:30 yesterday was already a new

**George Westbrook:** Yeah, I know.

**Dorte Dye:** high.

**George Westbrook:** That was that was that was that was weird for me as well, I think. And then it was the I think it was on Monday. I actually got up at like 5:00 or woke up at

**Dorte Dye:** Welcome to my holy club.

**George Westbrook:** 5:00. I was like,"This is this is just not right. This is just should not be happening to me."

**Max Kingaby:** It was nice though cuz we both went swimming in the pool and stuff and it's quite a nice morning.

### **00:02:29**

**George Westbrook:** Yeah.

**Dorte Dye:** Yeah. Rub it in. Rub it in. Okay.

**George Westbrook:** Yeah.

**Dorte Dye:** Are we waiting for anyone else?

**George Westbrook:** I think I think Hassan's just joining. I can see him sat over there. He had to run run back and get his AirPods, I think. One second. just shouted,"Did he join in?" And then literally the instant he said that he started. So yeah, I suppose obviously kind of following on from the the call we had we had yesterday. Um so I suppose the two main things that we're going to be working on in parallel now are the the stuff to do with the knowledge hub and obviously improving improving the agent. Um so in terms of the agent um like we mentioned yesterday and on the standard it's just making it a bit more efficient and in being more efficient it should speed it up. Um so whereas obviously at the moment it's like say you want to suspend a card it's like it's going to ask you questions after it's executed like 20 to calls just making sure it's getting that information up front.

### **00:03:48**

**George Westbrook:** to it. Bam, bam, bam, done. And then re whereas I'd rewrote the SOPs from what they were originally, but there was still there were still some things that weren't quite right. So, it's just going through that that process again. Um, and then creating the those specialized tools that we worked about. Um, also look through some of the feedback that you've provided, Dorte, and we're we're working on them as well. Um so hopefully in the next two to three days a lot of those changes should be should be implemented and ready ready to test. Um, I think in terms of the agent inbox, um, that's that should be working. But I think what what would be ideal is if we focus on the the agent, um, for the time being on that kind of stream of work. Um, and then what we're going to do going on to the knowledge hub is start thinking about I think first I think we're all in agreeance the MCP server. um and working out how we're how we're going to do that and get get something built and tested on that front so we can all play around with our own with our own clawed agents and then that will bleed quite nicely into the co-pilot any anything I said there which is making making you seem like what what is he talking about why are we doing this why are we doing

### **00:05:16**

**Michael Moores:** Not good for me. Thank you.

**Dorte Dye:** I think for me it's with the testing because there were so many moving parts working in the background. I didn't had one state of the bid where was testing against it because things were changing. So as I did over a couple of days things have changed again.

**George Westbrook:** Yeah.

**Dorte Dye:** So I think that will be just my question. If we do another round of testing, how do we want to ring fence it that we have a true

**George Westbrook:** Think I think what be Yeah.

**Dorte Dye:** outcome?

**George Westbrook:** I think I think always with testing if you go on to the production URL um because I know I know it seems a bit weird that we're calling it production but I think the most up to date um or the one that is going to be the most durable and The the best one to test is always going to be the the production agent and then testing will be kind of for for our testing. Um,

**Dorte Dye:** Okay.

### **00:06:08**

**George Westbrook:** so let's say we push a change.

**Dorte Dye:** Okay.

**George Westbrook:** Um, which I know doing testing on production just seems weird, but that's that's how that's how we're going to do it for the for the time being. Um, and I think what would it be a lot easier if when we're pushing up changes that we let you know um, rather than you you come in and suddenly like, okay, now it's doing this new weird behavior or this thing's rendering.

**Dorte Dye:** I guess makes sense, right, Mike? Or do you see that already with your connections?

**Michael Moores:** Yeah, that makes sense.

**George Westbrook:** Okay. Um, so yeah, we'll get the get the stuff of the agent done. We'll start thinking on the MCP server. I think what we might need to do um is we're going to investigate say in Braco and we might need might need some sort of access there so that we can have a look so that it's we're not getting like dale information um and that it's constantly being updated. I think obviously we spoke about a lot of that stuff yesterday.

### **00:07:15**

**George Westbrook:** Um, correct me if I'm wrong. There's a call you you guys have got a call for the content workforce later. I don't know if there's anything Max you want to you want to talk about on that front.

**Dorte Dye:** Yeah.

**Max Kingaby:** Um, no, we've got me and Tyler have sat there for some good time today. Um, we've got a list of everything we want to go through on the call. Um, ideally would be great if we could get your LinkedIn going today. Tyler is sat next to me, so that's that's fine.

**Dorte Dye:** if you're saying you're linked in going

**Max Kingaby:** Uh, your your profile set up, your TX your TXM business one.

**Dorte Dye:** because that's what we just yesterday discussed is like we need to agree on the tone of voice and everything and I think there was the miscommunication who was doing it you or Bronin you didn't seem to recall as we asked the question before. So I have it still as open. Um let's pick it up with Ian on the call.

### **00:08:10**

**Max Kingaby:** Yeah, I we by set up the profile. You don't need your tone of voice. I'm just talking I I just assumed the come, you know, get a banner, you know, get a a small bio and

**Dorte Dye:** I no I completely agree but uh I was from the last we spoke I was under an impression that Brumin is doing

**Max Kingaby:** Yeah.

**George Westbrook:** there.

**Dorte Dye:** that now because it was like oh you both are sure Brett couldn't really remember he said it's not a problem you guys can do it so let's bring that to Ian what what is his last take on it because for all I know

**Max Kingaby:** Mhm.

**Dorte Dye:** maybe Brman has it already because she I made her admin and that she's doing that in in the background.

**Max Kingaby:** Hello.

**George Westbrook:** Anything

**Dorte Dye:** It's it's a again all about timing, right? We don't want to put something on there if you're not ready to launch. So, it's like maybe getting it ready, but you don't have the not publish option at LinkedIn, I think. So when you do a change it is only visible.

### **00:08:59**

**Dorte Dye:** So

**George Westbrook:** Yeah.

**Max Kingaby:** Yeah. Okay. Well, if we don't have to set up your LinkedIn profile, that's great because we've got about five or six other things which we also want to talk about on the call. Um, prioritizing aligning your entities, which was something Ian brought up yesterday.

**Dorte Dye:** yep.

**Max Kingaby:** So,

**Dorte Dye:** Yep.

**Max Kingaby:** we'll crack on with that.

**Dorte Dye:** Uh, one question I just had, as you send all of that stuff across, I always have to put in a verification code, which gets over time pretty much annoying with the Google documents.

**George Westbrook:** a verification code.

**Dorte Dye:** Yeah, I always have to verify myself on the Google account.

**George Westbrook:** Is that a Google is that a is that a Google sending you an authentication code or is it something on our side?

**Dorte Dye:** It's from Google. Basically, when I want to open the link um Tyler has sent, then it always asked me to verify first. And I was this morning, I just wanted to get everything open and I was like,"Oh, I can't be asked anymore." Now,

### **00:10:02**

**Max Kingaby:** Maybe just copy and paste it onto

**George Westbrook:** No, I think Max,

**Dorte Dye:** I'm

**George Westbrook:** if you if you if you change it to when you share it, it's anyone with link rather.

**Max Kingaby:** what document is

**Dorte Dye:** And the other option is you just send as a word document or PDF because again I think that's what

**Max Kingaby:** saying is

**George Westbrook:** Yeah.

**Dorte Dye:** Ian prefers when he's reading this stuff Robert and he has to go into other applications or you just send us a PDF

**Max Kingaby:** Sorry. Sorry. I missed that Dorte. What? What did you say?

**Dorte Dye:** of the documents and then we can review and can feedback. Amazing.

**Max Kingaby:** Tyler said he will do that in a minute for you guys.

**Dorte Dye:** Perfect.

**Max Kingaby:** Cheers.

**George Westbrook:** And I think the last things on the the outbound stuff obviously in terms of the domains has Ian provided any feedback?

**Dorte Dye:** So,

**George Westbrook:** back on what what he would be looking for.

**Dorte Dye:** I just got a I got a a written uh sign up from Pacop CTO that he's fine with what we agreed yesterday.

### **00:11:01**

**Dorte Dye:** So,

**George Westbrook:** Yep.

**Dorte Dye:** I'm just sending it back to Ian and I will ask him for for the naming convention as well.

**George Westbrook:** Okay.

**Dorte Dye:** And so that's on my to-do list for this morning to get that sorted out.

**George Westbrook:** And then yeah, once you've got that, then we'll then we'll I'll speak to what's his name, Alex, about getting it on Cloudflare as well.

**Dorte Dye:** Yeah. Yep.

**George Westbrook:** um what that typical process for him with what ideally looked like. Then once we got that then we can get all the sets up going, get the domains formed um and then get some stuff hiring out.

**Dorte Dye:** Yep. That's the bomb. Cool.

**George Westbrook:** I think I I don't I think it's quite a short one today. Um is any anything else from from your side that you wanted to talk about or ask?

**Michael Moores:** Not for me. Okay.

**Dorte Dye:** No,

**George Westbrook:** Amazing. Let's Let's get building. Maybe Maybe that's our Maybe that's our um the thing we say at the end of every stand up.

### **00:11:56**

**George Westbrook:** Let's get building.

**Dorte Dye:** you should do I already. Don't you have the agents doing that while you do the talking?

**George Westbrook:** Yeah, but we've got to have we we've got have something we say at the end.

**Dorte Dye:** I don't know. It's like I can tell it's party time for you. We just started the day and there's a head of a day ahead of us. Send us a cock day.

**George Westbrook:** We we we'll test out different things and see which ones stick. I'm guessing from everyone's faces, let's get building was not the one.

**Dorte Dye:** Nope. Nope. Keep trying. Yeah,

**George Westbrook:** All right.

**Dorte Dye:** it feels a little bit like you're replacing Brett. So, I think that's not a goal you should aim for.

**George Westbrook:** Oh god. Right. I need to reconsider a lot of things now.

**Dorte Dye:** Okie dokie. Speak later, guys.

**George Westbrook:** Right.

**Michael Moores:** Yes,

**George Westbrook:** Have a lovely day.

**Michael Moores:** take care.

**George Westbrook:** Speak to you later.

**Michael Moores:** and said goodbye.

### **Transcription ended after 00:12:53**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*