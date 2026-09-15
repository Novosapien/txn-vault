---
date: 2026-09-15
type: standup
description: "Michael back and Ian's first hands-on test: too slow to use, a false spend-control answer from a stale spec, and approvals tied to console permissions"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-access-layer]]"
  - "[[txn-api-reference]]"
  - "[[commercial]]"
status: extracted
extracted-to:
  - "[[agent-orchestration]]"
  - "[[approval-queue-integration]]"
  - "[[process-surfacing]]"
  - "[[txn-api-reference]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-09-15)

> **Source:** Gemini transcript, 15 September 2026, 09:00 BST, 37m. **George Westbrook** and **Max Kingaby** from Bali, **Brett StClair** from a UK train, with **Ian Johnson**, **Dorte Dye** and **Michael Moores**, back from leave the previous morning. Lily St. Clair present.
>
> **The first standup after UAT.** Dorte and Ian had both tested the build during Michael's absence, and the first thing George asked for was their feedback. Ian opened with *"I'm going to give some brutally honest feedback."* Brett's reply set the tone for the rest: *"prefer the brutal, right?"*
>
> **Read it alongside two earlier sessions.** On 3 September Ian rejected the interaction model after watching a demo ([[2026-09-03-agentic-standup]]). On 10 September he tied the next phase of Novosapien spend to whether the work *"moves the needle"* ([[2026-09-10-content-workforce-company-closed]]). This is the first time he has used it himself.

## Ian's verdict, after using it

### What he said

> *"It is so slow, and it's not remotely intuitive."*

> *"I could have done almost everything that I did faster just on the control center."*

> **"My overriding concern is I just don't think people would use it.** I genuinely just look at it and think there's too much. You wait too long, and then when you do get stuff back..."*

George asked the question Novosapien most needed answered: had there been **bugs**, messages failing, tool calls erroring? Ian's reply is the most important sentence in the session:

> **"I can't remember getting any errors particularly, but to me, it taking so long, it might as well be the same thing."**

**So the build works and the client experiences it as broken.** Novosapien's internal bar has been correctness; TXN's bar is speed, and on TXN's bar a slow correct answer is a failure.

### This is an escalation, not a repeat

| Date | Basis | Ian's position |
|------|-------|----------------|
| 3 Sep | Watched a demo | Rejects step narration and stacked approvals. Praises the product: *"super positive about it"* |
| 10 Sep | Positioning discussion | Ties next-phase spend to whether it *"moves the needle"* |
| **15 Sep** | **Used it himself** | **Doubts adoption: *"I just don't think people would use it"*** |

**And it came after the fixes.** On 8 September the model was switched for speed and most approvals were turned off ([[2026-09-08-agentic-standup]]); George confirmed today that *"most of the approvals are turned off."* The SOP rewrite that frontloads questions is still in progress. So either the tested build predates the rewrite or the model change was not enough, and **nothing currently measures which** ([[open-questions]] #87).

### His three worked examples

**1. Suspend a card.** From Michael's test script, suspend James Thornton's card. The agent went away, fetched *"all the assets associated with James Thornton, so cards, accounts, all that kind of stuff"*, then came back with a list. Ian's fix is to **ask first**:

> *"If intuitively in a UI somebody says 'I want to put this card on hold', and then you ask them 'what is the last four digits of the card?'... that just trims that next bit down significantly. It happens in Claude all the time, that it asks for a recommendation before it goes off and does something."*

He also questioned whether the no-information case should be catered for at all: *"where somebody would come to suspend a card without knowing anything more than the guy's name, it just seems unlikely, and also seems like something that we probably don't need to cater for."*

**2. Onboard a cardholder on the consumer program.** The agent returned **every program**, including corporate platinum, travel expense and corporate purchasing. *"Clearly the first bit, the consumer bit, has served no purpose."* It then asked for the cardholder details as **a numbered list of eight fields in the chat**, *"rather than it coming in the UI that basically looks like a little form for you to complete."*

**3. Apply a monthly limit to every card on the consumer program.** A false answer, covered in its own section below.

## Ian does not want quick actions pushed out, and that refines #83

George's instinct was to concede the simple actions to the console:

> *"Those quick actions, it is just going to be simpler in the console. So I think where we are going to need to think is, where is the actual value going to be: those longer horizon tasks... like five or six different pages."*

He added the case where a quick action does earn its place: **bulk**. *"Where it's useful to have that in the agent is if that is one of maybe a ten path process... let's say they want to update ten cards and then given that they want to do some investigation after."*

**Ian disagreed, on the engagement's own principle:**

> *"If we follow that meeting clients where they are kind of philosophy, if you're pushing somebody out because we don't allow them to do something like put a card on hold or suspend a card, because of how long it takes, that could become somewhat frustrating, because you're then into that 'well, why have I got to leave where I am to go and do that? That should be straightforward.'"*

And he set the order of operations:

> **"Before making those decisions, we need to find a way of optimizing the speed of these things, so that we can then take a judgment and say 'actually, now that it goes that quickly, let's leave that in, because there's probably value.'"**

**This changes [[open-questions]] #83.** That row, opened after 3 September, frames the work as classifying journeys into quick actions and work-with-me sessions. Ian is now saying **speed first, classification second**: you cannot judge what belongs in the agent until you know how fast it can be. It also means classification should not be read as licence to remove simple actions.

### The split-screen idea, and why it was dropped

George proposed multiple chat panes, borrowed from how the team runs Claude Code, so a user can start a second task while the first runs. Ian: *"I'm not sure about the need for split screens. I generally think the thing that we've got to look at is how do we speed this now."*

George conceded it on the spot, and his phrase is the right verdict: **"It's like putting a plaster on the problem rather than actually fixing the issue at hand."**

## How Novosapien proposes to make it faster

| Fix | Detail |
|-----|--------|
| **Bundle tool calls into specialist tools** | Where a workflow runs call, result, call, result, the agent investigates up front, writes all the arguments, and makes **one** tool call. *"Rather than having like five or six turns"* |
| **Frontload the questions** | *"A few questions up front, get all of the information, here is my plan, and then it just executes, rather than that back and forth behaviour"* |
| **Send and forget** | Execution without further interaction, with completion reported through the inbox ([[notification-routing]]) |
| **Approvals already cut** | Most turned off, so *"we now know that the approvals work when they need to"* |

The bundling is new and it is the most concrete of these, because it attacks the cause George identified on 8 September: latency comes from the model reasoning between each tool call.

## Michael's proposal: a hybrid of chat and click

The most useful design idea in the session, and it came from TXN.

> *"If we know the scope is card and the action suspend, we could have a simplified UI that says 'here's the cardholder you're talking about', rather than asking those multiple questions. Like a landing page for the cardholder, and actually have those quick actions on the UI. So you can just go down and say 'oh, there's five cards here, you asked to suspend', and there's a simple suspend button."*

> *"A mix of agent versus click."*

**It answers Ian's form complaint and his speed complaint at once**, and it uses what already exists: the agent renders Console components in the chat ([[generative-ui-rendering]]), and Michael noted *"we load that screen and it does look quite good."*

He framed the design problem around **who is asking**:

- **A technical user** gives everything, card number and last four, *"that's the ideal outcome... it'll be a simple 'are you sure', carry on"*
- **A customer service user** usually gives less, *"so that can get quite lengthy"*

And he added a constraint nobody else raised: **LLM cost** belongs in the decision about where simple tasks break off from the agent.

### The agent-to-agent caveat

Michael was careful that a Console shortcut cannot replace the agent's understanding:

> *"When we come to that agent to agent discussion that we had, the agent still needs to know about these actions, to do [them] when we haven't got a UI in place... the environment is a little bit different when you're in the console versus when you're doing agent to agent."*

George's bulk example applies directly: *"if we're suspending 100 cards we need that module to go through that suspension and that understanding."* So the hybrid is a **Console presentation** choice, and the underlying capability has to survive for [[a2a-endpoint]].

## The agent explained something false, and explained it well

The part of the session that concerned Ian most, in his word *"deeply."*

### What happened

Ian asked it to apply a monthly limit to every card on the consumer program. It replied that **spend controls carry no program-level filter** and **are configured at the BIN sponsor level**, so the rule could not be isolated to one program.

> Ian: *"Spend controls are not applied at bin sponsor level at all in the TXN architecture... So firstly, number one, I don't think they are."*

**And the explanation was persuasive.** Ian, later: *"the response that actually came back following that is pretty good in terms of explaining. I mean, it's wrong. It's wrong in the sense that it shouldn't be that way, but you've explained why that might be."*

### Why it happened: two causes, both known

**One. The agent is running on an out-of-date API.** George: *"we still need to update to the latest version... last week we had a look and there was an issue with the URL. So the current version of the API that it's using is out of date."*

**That is [[open-questions]] #67, which has now bitten in front of the client.** #67 recorded on 27 August that DT moved the spec URLs and that Novosapien's fetch script cannot pull the internal spec from the new shape. It was marked *"not currently biting."* It is biting.

**Two. The endpoints do not exist yet.** Michael: *"DT's API is pretty broke right now for that"*, and *"we haven't approved the user stories of spend controls yet. That's what they've automatically built."* The real design has spend controls **per hierarchy level, on separate URLs** to make ownership clear, *"they just haven't built them yet basically."*

### Why this is worse than a slow answer

A slow answer costs time; **a fluent wrong answer costs trust**, and it teaches the user something false about their own platform. Ian's 3 September warning was exactly this: *"the minute they start distrusting... people won't go back."* The agent did not say it was unsure, did not say the endpoint was incomplete, and produced a plausible architectural reason for a constraint that does not exist.

**Nothing in the current build distinguishes "the API does not support this" from "the API I was given is incomplete or stale."** Raised at [[open-questions]] #89.

## The spend control hierarchy, as Michael described it

Recorded in full because it is the domain the agent got wrong, and Michael expects it to be **"one of the most used"** areas.

| Rule | Detail |
|------|--------|
| **Depth** | A **nine-level hierarchy**, from BIN sponsor (strictly, BIN range) down to card |
| **Ownership by URL** | Separate endpoints per level, same request schema. *"Bin sponsor spend controls, program manager spend controls. We've separated them out on separate URLs to make that ownership clear"* |
| **Access** | A program manager cannot act at BIN sponsor level. The agent should offer only the levels the user can reach: *"this is the hierarchy you can apply to"* |
| **No raising a parent's ceiling** | *"You couldn't go and say put £1,000 on this card if the program was set to 500. So there's no way you can override a higher limit"* |
| **Guide before the API refuses** | *"Naturally the API will just tell you to go away anyway, but if we can frontload that ahead, so we're guiding them properly into what they can and cannot do"* |
| **Merchant controls** | Same hierarchy, but **yes or no** rather than an amount, *"so it's a little bit easier"* |

**The analytical case Michael expects**, and it is a strong work-with-me example: *"if I did a transaction of £500 at this merchant, would it go through? The AI would need to go away and make sure that the controls are in place"* across every level. His analogy for the model is ringing your own bank before a large payment.

**Incoming:** Michael has **around twenty DT specification documents** on the hierarchy and will send them once he has finished answering DT's questions: *"it gives you a good background about the hierarchy, how that works."*

**On BIN sponsors that are not BIN sponsors.** Dorte asked how this reads to a client that issues in its own right. Ian: *"technically there's always a bin sponsor, even though they're not really a bin sponsor... there always has to be a bin sponsor, whether that's the client themselves or [someone else]."* He parked the naming question as bigger than this conversation.

## Approvals follow the Console's permission model

**The decision the approval work has been waiting for**, and it resolves the open half of [[open-questions]] #83.

Michael:

> *"For now, I think if we stick with the user permissions: **each permission has an approval field on it or not.** And then what we need to do is say 'okay, this action attributes to this permission, and that permission needs approval'."*

> *"We had a discussion before I went away: probably to start, we'll align that with the console. So you push that as well, and then I guess the agent will be more confirmation. 'Are you sure you want to do this?' Yes. Then it'll be 'okay, I need approval for this, I've submitted it to the approval queue, wait for someone to do that'."*

**So Novosapien does not decide which actions are sensitive.** The Stackworkz permission framework does ([[open-questions]] #71), and each permission carries its own approval flag. The agent's job is to map each tool to a permission and honour the flag. Michael said the detail is largely in the Console backend API document he has already sent.

### Two kinds of approval, which George separated cleanly

| Kind | Trigger | Mechanism |
|------|---------|-----------|
| **Permission approval** | *"I am a user, I've not got enough access. Even if I was doing it in the console, I need approval"* | Submitted to the **approval queue**, approved in the Console or on **mobile**, on the go |
| **Agent confirmation** | *"I as a user have access... but an agent taking action on behalf of me might want to just double check: are you sure you want to delete a card?"* | A confirmation in the conversation |

**And the future direction Michael flagged**, deliberately deferred: *"down the line, the agent, when this user uses that agent, they have higher privileges... this user's unskilled, let's say, but with the agent they can do higher skilled things with guard rails."* That is the same idea he raised on 26 August at [[open-questions]] #74, and it stays later.

## Verbosity should depend on where the user is

Ian's second complaint after speed:

> *"It talks in a very much AI way, that I'm going to give you all of this detail and context that I've got. I'm going to share it with you."*

His examples: unrequested references to *"contracts and storage"*, the entity *"accessed and managed under"* a named endpoint, *"and then it continues to quote other API references that are just kind of unnecessary... I don't care where it is."*

George agreed, recalled the earlier *"I'm going to execute the update_cardholder tool"* problem, and floated **user-defined verbosity settings**, since Hasan prefers full explanations. His default: *"as a default, it should just tell me what I need."*

**Michael supplied the better answer: it depends on intent and surface, not on the person.**

> *"If you're saying 'how do I do this in terms of the API', then I'd expect that detail, rather than saying 'I want to do this' and getting the whole workings and background behind it... If it's on the knowledge hub, that would have been a great answer, versus 'I'm trying to do this quickly'."*

**That is the same axis Ian set for step narration on 3 September**: detail varies by task, not by user. Recorded against [[process-surfacing]], where it extends the two-class ruling to language as well as progress.

## Dorte's feedback: helpful when lost, slow when not

She tested **randomly** rather than by Michael's role split, and hit one flow that failed in UAT but worked in production, so her results are partial. What she found:

**Good.** *"I really liked when it explains something, when you sometimes don't know where you are and you just zoom out and ask for certain things."* And the visuals: changing a spend limit showed the effect on the transaction limit, *"the description and how it looked, it was really great."*

**Not good.** *"It took ages for some of them... for the onboarding, it's fine, because it's a massive job. But when you have the smaller ones, where you just want to change a limit or something, then it's much easier to do it yourself when you know how to do it."*

**Her request:** orientation first, detail on demand. *"My brain always goes, I need to go up, where do I sit, where I am in the flow... rather than having it really wordy, and you always can click or ask for more clarification."*

**Both testers reached the same verdict from different starting points**: onboarding justifies the agent, small changes do not, at current speed.

## What is next

**Phase two call tomorrow, 16 September.** George: *"we'll talk about some of the phase two stuff, prioritisation"*, plus Content and Outbound updates. He noted that phase two has in a sense already started, since the **agent inbox is now working in production** for Dorte.

**Michael has not reviewed the build yet.** *"From my side I need to have a look at what you've done properly."*

**Outbound:** the sending domains *"should be done very shortly"*, then lead lists get built and sent over for review.

**Content Workforce:** Dorte and Ian want to hold Tyler's kick-off until after the session with Brett on AI positioning ([[open-questions]] #88). Dorte: *"I want to just see where we are, what is missing, and then we regroup."* Ian agreed.

## Findings and where they landed

### The verdict

| Finding | Destination | Action |
|---------|-------------|--------|
| **Ian, after testing: "so slow", "not remotely intuitive", "I just don't think people would use it"** | [[commercial]], [[open-questions]] | Added to **#88**, and to **#51** as the testing outcome |
| **No bugs, but "it taking so long, it might as well be the same thing"** | [[agent-orchestration]] | Recorded: the client's bar is speed, not correctness |
| The verdict followed the 8 September fixes, and nothing measures their effect | [[open-questions]] | Added to **#87** |
| **Ian: fix speed first, then decide what stays in the agent; don't push simple actions out** | [[agent-orchestration]], [[open-questions]] | **#83** reframed |
| Split-screen chat panes proposed and dropped as *"a plaster on the problem"* | [[agent-orchestration]] | Recorded |

### The design

| Finding | Destination | Action |
|---------|-------------|--------|
| Ask for the identifier first, as Claude does, rather than fetching everything | [[agent-orchestration]] | Recorded |
| Program filters ignored; eight required fields listed in chat instead of a form | [[agent-orchestration]], [[generative-ui-rendering]] | Recorded |
| **Bundle multi-call workflows into specialist tools** | [[agent-orchestration]], [[tool-catalogue]] | Recorded as the concrete speed fix |
| **Michael's hybrid: a simplified cardholder view with action buttons, in the chat** | [[generative-ui-rendering]], [[agent-orchestration]] | Recorded; LLM cost added as a factor |
| The agent must still understand the action for agent-to-agent use | [[a2a-endpoint]] | Recorded |
| **Verbosity depends on intent and surface, not on the user** | [[process-surfacing]] | Recorded, extending the two-class ruling to language |

### Approvals and the platform

| Finding | Destination | Action |
|---------|-------------|--------|
| **Approvals follow each Console permission's approval field** | [[approval-queue-integration]], [[open-questions]] | **#83** and **#26** updated |
| Two kinds: permission approval via the queue, agent confirmation in conversation | [[approval-queue-integration]] | Recorded |
| **The agent gave a fluent, false answer on spend controls** | [[open-questions]] | New row **#89** |
| **Cause one: the agent runs on an out-of-date API** | [[txn-api-reference]], [[open-questions]] | **#67** now biting |
| Cause two: spend control endpoints unbuilt and user stories unapproved | [[txn-api-reference]], [[open-questions]] | Added to **#32** |
| **Nine-level spend control hierarchy, ownership by URL, no raising a parent's limit** | [[txn-api-reference]] | Recorded |
| Michael sending around twenty DT specification documents on the hierarchy | [[txn-api-reference]] | Recorded as incoming |

### Delivery

| Finding | Destination | Action |
|---------|-------------|--------|
| Phase two prioritisation call on 16 September | [[delivery]] | Recorded |
| Agent inbox working in production | [[agent-inbox-alerts]] | Recorded |
| Michael has not yet reviewed the build | [[open-questions]] | Added to **#51** |
| Tyler's kick-off held until after the AI positioning session with Brett | [[content-workforce]] | Recorded |

### Context, no action

| Finding | Note |
|---------|------|
| Michael's return took 21 hours via Addis Ababa, back 09:00 on 14 September | He described himself as *"very, very tired"* |
| Brett joined from a train; the team is in Bali except Brett and Lily, both going next week | |

## Open actions from the call

| Action | Owner | Note |
|--------|-------|------|
| Update the agent to the current API version | Novosapien | Fixes the cause of the false answer. #67 |
| Bundle multi-step workflows into specialist tools | Novosapien | The concrete speed fix |
| Frontload questions in the SOPs, asking for the identifier first | Novosapien | Continues the 8 September rewrite |
| Explore a hybrid cardholder view with action buttons in the chat | Novosapien with Michael | Michael's proposal |
| Map each tool to a Console permission and honour its approval flag | Novosapien | Detail in the Console backend API document |
| Cut API and architecture detail from action responses | Novosapien | Keep it for knowledge hub questions |
| Send the DT specification documents on the spend control hierarchy | Michael | Around twenty, once his DT questions are answered |
| Review the build properly | Michael | He has not yet |
| Phase two prioritisation | Both | 16 September |

---

## Transcript

Sep 15, 2026

## **TXN \- Agentic AI SU \- Transcript**

### **00:00:19**

**Ian Johnson:** Morning.

**George Westbrook:** Hello.

**Ian Johnson:** How are we doing?

**George Westbrook:** Good, good, good. How you doing?

**Ian Johnson:** All right. Thank you, mate.

**Max Kingaby:** Such a way of words. Good, good, good.

**George Westbrook:** Yeah, just this just just the standard way. No matter how you feel, you always go. How you doing? Good. Yep. Good. I don't know if that's it's not just a British thing, I suppose. How we doing,

**Ian Johnson:** Here it is.

**George Westbrook:** Mike?

**Michael Moores:** Are you okay?

**George Westbrook:** All good. All good.

**Ian Johnson:** How's your holiday

**George Westbrook:** You feeling refreshed after your holiday.

**Michael Moores:** Yeah. Very, very tired, but uh I'm back.

**Ian Johnson:** get back?

**Michael Moores:** Um took us 21 hours and I got back about 9:00 a.m. yesterday. So,

**Ian Johnson:** Holy s\*\*\*.

**George Westbrook:** Oh god,

**Ian Johnson:** 21 hours.

**Michael Moores:** yeah,

**George Westbrook:** that is

**Michael Moores:** quite big layover and stuff, but getting back from London at rush hour was lovely.

### **00:01:10**

**Ian Johnson:** Okay.

**George Westbrook:** Yeah. Where where was your layover?

**Max Kingaby:** I just got back.

**Michael Moores:** um Ethiopia for four four five hours there which is fun but

**George Westbrook:** Bloody hell. Yeah.

**Michael Moores:** yes we left half left halfway on the 13th uh from our hotel and obviously got back like you know almost 24 hours afterwards

**George Westbrook:** Oh no, I can imagine. Was it that Ad is it Adis Aba the airport the main airport there? I can imagine that's not the nicest airport to have a four or five hour layover either.

**Michael Moores:** No, definitely not not at like midnight or wherever it was we were flying at. So,

**Ian Johnson:** He's

**George Westbrook:** Yeah. I think we we were fortunate on our layover it was in Hong Hong Kong airport.

**Brett StClair:** Hello everybody.

**George Westbrook:** So

**Michael Moores:** yeah, definitely that's much better.

**Ian Johnson:** doing the job.

**Brett StClair:** Good morning. How's everybody doing?

**Ian Johnson:** Hi. How are you?

**Brett StClair:** Good. Good. I'm just on a train, so I might have a bit of a spotty connection, but the train's still at the moment.

### **00:02:18**

**Brett StClair:** Mike, you have a good break.

**Michael Moores:** Yeah, very good. Thank you. Very, very good.

**Brett StClair:** Looking very relaxed.

**Michael Moores:** Tired more than anything. It was a lot. 12 hours driving a day. It was quite a lot.

**Ian Johnson:** So, who's actually in Bali at the minute then?

**Brett StClair:** Everyone except for Lily and I.

**Ian Johnson:** Oh, that makes

**Brett StClair:** I'm on a holiday.

**George Westbrook:** got the just the the monitor setups there quite Yeah, I was expecting them when they delivered the monitors to be like carrying them on their shoulders on the bikes, but they fortunately turned up in a van.

**Max Kingaby:** That's awfully culturally aware of you, isn't it, George?

**George Westbrook:** What did you have you the amount of stuff they carry? I think I saw a guy with about a thousand eggs on a bike the other day. I was like, how is he I can barely get eggs home from the supermarket without breaking them in in a car, let alone on a motorbike.

**Michael Moores:** Yeah.

**Ian Johnson:** Okay.

### **00:03:16**

**Ian Johnson:** Should we get started?

**Brett StClair:** Yeah, let's get into it.

**George Westbrook:** Let's go. So, I suppose UA UAT testing on the agent seen seen your feedback, D. Thank you. Thank you very much for for that.

**Michael Moores:** Heat.

**George Westbrook:** Um, is there any concerns that are top of mind when testing it that that you want to want to start with or should we just go through go through some of the the feedback that you've heard?

**Dorte Dye:** I think the the main thing was for me I did run random testing because I hadn't didn't had the different setups what Mike said Ian was meant to be the administrator and I was just restricted access there

**George Westbrook:** Oh,

**Dorte Dye:** was one one that didn't work in UAT but it worked in production so I did some of them in UAT and tried to do them in production. I probably haven't finished because I made the comments on it. I couldn't really see where I was and I attended them differently. So, I think just let's go through and then I can do more testing after.

### **00:04:16**

**George Westbrook:** okay.

**Dorte Dye:** So there were some really good things and I really liked um when it explains something when you

**George Westbrook:** It's Oops.

**Dorte Dye:** sometimes not know where you are and you just zoom out and ask for certain things but some of them were not as intuitive and the the main concern I had I got quite annoyed because it took ages for some of them particularly when you when you started things and we touched base on

**George Westbrook:** Yeah.

**Dorte Dye:** the last two weeks right um it just for smaller things for the onboarding it. It's fine because it's a massive job. But when you have the smaller ones where you just want to change a limit or something,

**George Westbrook:** Yeah.

**Dorte Dye:** then it's much easier to do it yourself when you know how to do it.

**Ian Johnson:** I I'm in a slightly different place. I'm going to give some brutally honest feedback, but it it is it's so slow and it's

**Michael Moores:** I'm sorry.

**Ian Johnson:** not it's not remotely intuitive. So, I did do some testing.

**George Westbrook:** Hey.

### **00:05:12**

**Ian Johnson:** So, so the the the speed thing is I could have done almost everything that I did faster just on on the control center. Um,

**George Westbrook:** Yeah.

**Ian Johnson:** and one of the things that that I think became clear to me is we're not thinking enough about the steps that will speed the thing up. So, for example, Mike gave a script and one of them was put on put a card on hold for whoever it I can't remember whoever it was or suspend a car for somebody and then you wait for absolutely ages for it then to come back and say here are the cards forever. You know whi which one is it? And to me, you just got to think, we got to think a bit smarter there because I I can go to a control center and search for that person's card faster. Um, and there's not enough information that's being asked at the point of the of the um of the of the kind of prompt being raised to to cut that down.

**George Westbrook:** Yeah.

**Ian Johnson:** So,

### **00:06:30**

**George Westbrook:** Yeah.

**Ian Johnson:** for example, if intuitively in a in a UI, somebody says, I want to put this card on hold, and then you ask them,"What is the last four digits of the card, Mike?" Or,"What is the something else that just trims that next bit down significantly?" Um, which is not unreasonable. um you know it happens in Claude all the time that it asks for a recommendation before it goes off and and does something. So, I think we just need to think about that generally because my overriding concern is I just don't think people would use it. I genuinely just look at it and think that there's too there's too much um you wait too long and then when you do get stuff back um for example, it'll ask you to provide something and it just says,"Oh, here we go. Where is it? I think I asked to create a card for somebody card order on boarding and first card like you said set up a new card holder on the consumer program and issue their first card.

### **00:07:47**

**Ian Johnson:** So you do that and you get a list of multiple programs. One of which is a corporate platinum program. The other is a travel expense card, a corporate purchasing card. So clearly the first bit, the consumer bit s has served no purpose because we haven't filled the list of what it is. Um and then it says to proceed please provide the card holder details and just lists one through to eight of the things that are required but it's just in a normal chat prompt then so what am I doing number one name number two whatever it is rather than it coming in the UI that that basically looks like a little form for you to complete

**George Westbrook:** Yeah.

**Ian Johnson:** to um so again I realize it's it's quite brutal feedback but I'm I'm I'm somewhat concerned that not going to this is Welcome.

**Brett StClair:** prefer the brutal, right?

**George Westbrook:** Yeah, is I I think in terms of speed, there's definitely certain things we can do to speed it up and I agree with you in certain aspects. It's like those quick actions it is it is just going to be simpler in the console.

### **00:09:07**

**George Westbrook:** Um so I think where we we are going to need to think is where is the actual value going to be those longer horizon tasks which are we need to investigate. We need to analyze like this is something that a human if they were doing it they'd be going to like five or six different pages. They might have to do stuff outside of the platform. And I think like I agree with you, it's updating maybe the status of a card. It's two or three clicks. And where it's useful to have that in the agent is if that is one of say maybe a 10 path process that somebody's going through. Let's say maybe they want to update 10 10 cards and then given that they want to do some investigation after. Um that's where I think those so-called quick actions can be done a lot well a lot quicker than if it was in the console. If it's just one one to one, I think I don't think there's much we we can do there. But I think from our perspective where we're where we're happy is it seems like the feed the feedback that you guys are giving is this workflow is doing things in the wrong order or this this is too slow blah blah blah.

### **00:10:14**

**George Westbrook:** Um but the agent is is working. I think correct me if I'm wrong. Has there been any like bugs or um like where you've sent a message if not gone through or the tool calls failed or things like that? because that's I think for us initially that's where we'd be most concerned because when it comes to like the SOPs that's I'd say more optimization in terms of like the actual workflows

**Ian Johnson:** I didn't I can't remember getting any errors particularly, but to me it taking so long, it might as well be the same thing.

**George Westbrook:** yeah I think what we can what we can probably start to do

**Ian Johnson:** That's the point.

**George Westbrook:** is where it's so with certain workflows where it's doing tool call get result tool call get result tool call get result we'll just we'll create kind of like specialist tools so whereas at the moment it might be one API call in one tool and if it needed to make three or four calls that's going to three or four um tool calls that be three or four API calls what we can do most what we can do is bundle it.

### **00:11:27**

**George Westbrook:** So, let's say up front the agent does a little bit of investigation um writes all of the arguments and bundles it into one tool call rather than having like five or six turns. Um, also, so one of the things that we've been working on the last week and thinking quite hard about is so obviously first of all taking away um some of the approvals um to to hopefully speed it up, but also completely rewriting all of the all of the all of the workflows or SOPs. So whereas before it was kind of this is what this is what I'm going to do um Mr. User of an agent. Do you do you accept this? You click yes. Then it does a bit of investigation. Then it does this. Then it asks you some more questions and then it goes into that approval mess. Um trying to frontload it. So few questions up front. Um get all of the information. Here is my plan and then it just execute rather than that back and forth behavior that it's got at the moment.

### **00:12:24**

**George Westbrook:** Um so it is kind of that send and forget. Um it's just a mechanism of how do we how do we alert the user when it's done and if there is extra information needed how do we do that in a more seamless way. Um one one thing I did think we did think we could potentially do is have the ability to have maybe multiple chat windows within the actual screen. So just taking from the way that say me and some of the team work when it comes to claw code is that exact issue you you get it to go away and do some work and you're waiting two or three minutes before it comes back. So then we'll have like maybe three three panes up. Um so when one's working we can start going back to the other one and going back to the other one. So maybe there's a way that we can have like a split screen view. So if a user wanted to have maybe two things working at the same time, they could.

### **00:13:22**

**George Westbrook:** I don't I don't know if that's something that you you guys think could be valuable.

**Ian Johnson:** I think I think what's needed is some real careful consideration about what the what we want to what we think is valuable to come from the agent versus what we kind of probably don't think is. I think it's there's a little bit of a challenge there because if somebody if we follow that meeting clients where they are kind of philosophy if you're pushing somebody out because they we don't allow them to do something like you know put a card on hold or suspend

**George Westbrook:** Okay.

**Ian Johnson:** a car because of how long it takes that could become somewhat frustrating because you then into that well why have I got to leave where I am to go and do that that should be straightforward. So I think it comes down to before making those decisions Mike at least for me we need to find a way of optimizing the speed of these things so that we can then take a judgment and say actually now that it goes that quickly.

### **00:14:35**

**Ian Johnson:** Let's leave that in because there's probably value. You know if somebody doesn't want to use the agent to do a certain thing and they decide it was faster to go and do something somewhere else then fine they can do that. If somebody has one thing to do and they just don't want to go into the control center and they want to put a card on a suspender card and go into control center but go through the normal way of finding um a card then they you know they can do that but it's some of those things just come to they let me give an example this thing about putting I don't know Mike I put I said something like put James Thornton's or suspend James Thornton's card or whatever it was um and then he goes off and comes back and says here are all the assets associated with James Thornton so cards accounts all that kind of stuff. Well, I've asked to suspend a card or whatever it was. The first thing immediately and it really quickly should be asking for some more information or would you like me to pull back, you know, do do you know which specifically which which card it is or would you like me to pull back the a list of cards under James Thornton's name, whatever it might be.

### **00:15:59**

**Ian Johnson:** because that way if I've come to the query mic with no information um then I I I could accept the fact and I have to wait a little bit longer

**George Westbrook:** Yes.

**Ian Johnson:** because I can find what are then once I found them I can pick the one that it is and make sure I've selected the right one. Um whereas I'm just trying to think of that scenario, Mike, where because where somebody would come to suspend a card without knowing anything more than the guy's name. It just seems unlikely and also seems like something that we probably don't need to cater for. As in the suspend action is something that can't be done until you tell us what it is that we're suspending with a associated reference. If you then want to do a first call, which is pull back those cards, that's kind I'm just trying to think how you would actually work. So, let's say some you you've had a call with somebody and they've asked you to suspend a card or whatever it might be and then you haven't taken the I don't know you've made a note of something but you you you just want to double check to make sure you're absolutely clear which one it is you suspended.

### **00:17:27**

**Ian Johnson:** Then logically you would want to see what list of cards we're talking about and then you make a choice. Okay, I'm gonna suspend. This is the card that I want to suspend. I just feel that like because it's not broken up, you just sit there waiting for a very long time to get to something that really

**George Westbrook:** Yeah.

**Ian Johnson:** should be quick. I'm not sure about the need for split screens and and things like that. I think I generally think the thing that we've got to look at is how do we speed this now

**George Westbrook:** Yeah. Access by It's like it's like putting a plaster on the problem rather than actually fixing fixing the issue at hand. Yeah.

**Ian Johnson:** Yeah.

**George Westbrook:** Okay.

**Michael Moores:** I think as well obly from from my side I need to have a look at what you've done properly but I think obviously we look at the the agent to agent side and you know in the console there's two big differences there obviously the we have the UI we have the console so you know stuff like this is going to be needed for that agent to agent to your point George like if we're suspending 100 cards we need that module need to go through that suspension and that understanding.

### **00:18:34**

**Michael Moores:** I guess with a console, we could have some sort of either redirection or you know a simple action. So we if we know the scope is card and the action suspend, we could have like a simplified UI that says here's a here's the card holder you're talking about rather than

**George Westbrook:** Come on.

**Michael Moores:** asking those multiple questions say here's like a landing page for the card holder and actually have you know those quick actions on the UI. So you can just go down and say,"Oh, there's five cars here. You asked to suspend and there's a simple, you know, suspend button." So I think we just need to balance obviously looking at the cost of the LM as well. Where do we break up those what we call simple tasks and I guess from the user point of view, it's you've got perhaps a technical user will give you all the information. That's the that's the ideal outcome whereby we have the card number, you know, the last four, we have everything we need. In that situation it'll be a simple are you sure carry on whereas the majority I think of people might just be very sure and answer you look at the customer service might say I want to submit a card here's additional details so that can get quite lengthy so I think we need to try and bridge the gap in terms

### **00:19:39**

**Michael Moores:** of who will use this for speed and give the full context whereas where can we identify those quick actions or the the simple actions should we say that we just sort of ether redirect them or you know show them a simplified UI component that we already have in that chat window to sort of use a mix of agent versus click and obviously what before is is quite seamless between the two obviously we load

**George Westbrook:** Yes.

**Michael Moores:** that screen and it does look quite good. So perhaps we we can look at some sort of option there where we know okay this is a single card single action is it just easy for them to show the screen this they press approve or yes I want to suspend this card something like that and obviously that's on me to have a look at the the tool call still as well and see where we can do those approvals we could look at something like that perhaps as well you know we have that benefit that UI but I do think you know when we come to that agent to agent discussion that we had the agent still needs to know about these actions to do when we haven't got sort of a UI in place you specifically at the console u because I think the environment is a little bit different when you're in the console versus when you're doing sort of agent to agent you know discussions

### **00:20:48**

**Ian Johnson:** There there's one there's there is one I mean aside from the the the general theme I've spoken about there there is one thing Mike that concerned me deeply which was I I did the one Where? you say apply a monthly limit to every card on the consumer program. So just just generally as I was saying I think the fir the first thing there is here are here here are a list of the programs which one are we talking about okay just from a usability point of view the bigger concern is what came back is because spend controls carry no problem level filter a rule cannot be isolated to cars on the consumer program alone so It's basically saying that spend controls are configured at bin sponsor level. All right, here we go. Spend control not applied at bin sponsor level at all in the TXN architecture. Spend again just spend controls are not applied at bin sponsor level at all in the TXN architecture. Spend controls are configured at the bin sponsor level. So I firstly number one I don't think they are like

### **00:22:07**

**Michael Moores:** That may be that may be DT's API is pretty broke right now for that.

**George Westbrook:** So,

**Ian Johnson:** Thank you.

**George Westbrook:** one caveat as well is we still need to update to the latest version of the I think last week we had a look and there was an issue with the URL. Um, so the current version of the API that it's using is out of date. So there's going to be instances like that in its current format where it's going to be slightly different. So that that might that might be the reason

**Michael Moores:** Yeah. Yeah. Yeah, I think for SP we haven't approved the user stories of spend controls yet. They that's what they've automatically built. So from a from a technical point of spend controls will be per endpoint basically. So sort of association model bin sponsors spend controls you know program manager/spend controls. We've separated them out on separate URLs to make that ownership clear. So obviously all those endpoints will be coming. They just haven't built them yet basically.

### **00:23:02**

**Michael Moores:** It's all the same request schema just s different urls to show we're talking about this program manager the espend control so it will be there at the different hierarchies bin sponsor has a bit of a different so it's not sort of bin sponsor level it's more bin bin range there is a hierarchy there but um you know we do have that hierarchy that can go down as low as possible so we just need to make sure when we do that one we get the right level naturally if you're a program manager not a bin sponsor and you know bin sponsor is not even a thing. So there's levels of access and control here that you know a person wouldn't get access to. So in that situation we would sort of say right this is the hierarchy you can apply to and obviously that's what the context come from rather than this is what we have available. So I think that one's very specifically um an access thing as well. So we'll okay you can only do program manager product and this basically um obviously there's also overrides as well.

### **00:24:01**

**Michael Moores:** within this hierarchy. you couldn't go and say put £1,000 on this card if the program was set to 500\. So there's no way you can override a higher limit as well. So stuff like that, we're going to have to need to build in naturally the API will just tell you to go away anyway. But if we can, you know, frontload that ahead so we're sort of guiding them properly into what they can and cannot do. Um, as well basically

**Dorte Dye:** How do we deal with it when there is no sponsor? When they're an issue in their own right, will that not be confusing for them as well when we're referring to a sponsor?

**Ian Johnson:** Well, there technically there's always a bin sponsor even though they're not really a bin sponsor. You know, they are in terms of the role within our system. there always has to be a bin sponsor like right it doesn't matter who that is whether that's the client

**Michael Moores:** Yeah.

**Ian Johnson:** themselves or it's Agentic I understand I understand where you're coming from in terms of

### **00:24:58**

**Dorte Dye:** Okay.

**Ian Johnson:** the confusion but that's that's not nothing to do with this conversation that's a bigger what do we call a bin sponsor if you want to change it the response that came that actually came back following that is pretty good in terms of explaining I mean it's wrong. It's wrong in the sense that it shouldn't be that way, but you've explained why that might be. Um, the the only thing is that it kind of it comes back and and talks in a in a I know it's AI, but it talks in a very much AI way that I'm going to give you all of this detail and context that I've got. I'm going to share it with you.

**George Westbrook:** Yeah.

**Ian Johnson:** For example, contracts and storage. I no nothing's been mentioned about contract and storage that so that's a very AI terminology the spend control entity is accessed and managed under and then it gives me um bin sponsors spend controls like I I don't I don't care I don't care where it is and then it continues to quote other API references that are just kind of unnecessary to to the thing that

### **00:26:16**

**George Westbrook:** Yeah,

**Ian Johnson:** It's like sharing information.

**George Westbrook:** suppose that's the Yeah,

**Ian Johnson:** No point.

**George Westbrook:** I suppose for for something that's in the not in the console the the knowledge hub that's information like that I suppose for Google but not for like you're in the console you don't want to know what API endpoints is being used it's just this is I think that's definitely another thing we need to improve is some of the language I think before we had the issue where it was going I'm going to execute the update\_c card holder tool. Um which is kind of like I like for me for me in my head when I was testing initially I was like okay that's fine but then think about from a user like f\*\*\*

**Ian Johnson:** Yeah.

**George Westbrook:** it update unto a car holder. So I think it's yeah cutting back on some of that overexlaining. um 100%. Um making it not as verbose um or maybe I think we spoke about this is like the maybe some user defined settings. Um so like I think I'm with you Ian.

### **00:27:15**

**George Westbrook:** Um I don't want to know all this other random s\*\*\*. I just want what what is it? Just tell it to be as short and concise as possible. Um but I think Hassan's the opposite. He loves he loves the full explanation. He's a bit of a speed reader. So, I think once once we've nailed like the core, maybe adding a bit of that flexibility in for the user as well um could be good. But I think as a default just should tell me what I need.

**Michael Moores:** I think as well it's probably the context obviously as you say that if you're saying how do I do this in terms of the API then I'd expect that detail rather than saying I want to do this and getting the whole workings and background behind it because I think there are that's a good answer if I said how does the

**George Westbrook:** Yeah.

**Michael Moores:** API work That's a really good answer.

**Ian Johnson:** Yeah. Yeah.

**Michael Moores:** You just need to decide what context it's coming from as well.

### **00:28:05**

**Michael Moores:** You know to your if it's on the knowledge of that would have been a great answer versus I'm trying to do this quickly. I may have misunderstood slightly should be a redirection to you can apply being sponsored level because

**George Westbrook:** Yeah.

**Michael Moores:** you access or this is a level you can provide. Where would you like to to set that basically? Um, and this is the probably the most complicated setup in the system as well because obviously we have that nine level hierarchy from bin sponsor all the way down to card. And then you have sort of certain things can be overridden and certain things can't. So obviously you're recognizing your own bank like if I want to buy a house, I've got to ring my bank up. I want to make a big payment today. That's sort of model that we're we're trying to create there. So it is very complicated. That's something we're working with DT. So you know we will put so much in the API to protect that naturally but I think if a um the agent have a really good understanding of that hierarchy how naturally obviously when you get the end points it'll be better we have the full I've got like 20 documents for for DT on the specifications as well I'll give you once I've finished with them answering a lot more questions about what you can and what you can't do naturally that's all going to be in the the YAML anyway but it gives you a good background

### **00:29:15**

**Michael Moores:** about the hierarchy how that works as well. So, I'll send that across once I've got that. Naturally, we still need to build that, but that's the sort of idea behind it. And this is probably one of the most I say complicated hierarchy in the system, allowing multiple people who own different bits to set the the risk basically the spend risk. Um, and I think that is it's probably going to be one of the most used I say as well in this situation

**George Westbrook:** Okay.

**Michael Moores:** because they, you know, they might want to manage five products or 10 products and they want to make sure it aligns or they want to make sure which one differs. You know, if I say if I did a transaction of £500 at this merchant, would it go through? Obviously, the AI would need to go away and make sure that the controls are in place. Israeli and we have merchant controls too which is same hierarchy but it's yes or no rather than a spend type association so it's a little bit easier but it'll have to go away and make sure that that transaction could take place on that card so that's why sort of more difficult in nature and I think we just need to think about that order how's best to position that with a a user that might not understand fully the the inner workings of the hierarchy

### **00:30:26**

**Dorte Dye:** What I thought was really helpful when you have the visuals in there, when you had to change the spend limit, it didn't give me the impact on the transaction limit before it did it and it didn't ask me could approve it, but the description and how it looked, it was really great. So I think my brain always goes I need to go up where do I sit what where I am in in the floor and that might be helpful as well rather than having it really wordy and you always can click or ask for more

**George Westbrook:** Yeah. Okay.

**Dorte Dye:** clarification or go more detailed.

**George Westbrook:** Okay. Yeah. Cuz I think at the moment moment most of the approvals are like turned off. So then it's just working out. I think whereas before obviously it was kind of like every little action you wanted to do was needed to be approved. Um now it's gone the opposite way but in doing it that way we now know that the approvals work when they need to.

### **00:31:18**

**George Westbrook:** So it's just I think when it when it comes to say certain workloads what needs to be approved and what doesn't need to be approved which I suppose we might we might need a bit bit of your help on on understanding that. So I think if there's we've got the the old kind of workflow PDF but I suppose it's bucket in what's sensitive and needs approval and what what doesn't.

**Michael Moores:** Yeah. Yeah. I think that largely will be in that document I sent you about the you know the the backend API for the console.

**George Westbrook:** Yeah.

**Michael Moores:** So we've pushed a lot of that but I think we had a discussion with him before I went away is probably to start we'll align that with the console.

**George Westbrook:** Yeah.

**Michael Moores:** So you push that as well and then I guess the agent will be more confirmation. Are you sure you want to do this? Yes. Then it'll be okay I need approval for this. I've submitted it to the approval queue. Wait for someone to do that.

### **00:32:08**

**Michael Moores:** I think that's the the sort of way it all work now and then we may look in the future though say

**George Westbrook:** Yeah.

**Michael Moores:** okay user can do this but the agent could do more. So you push more of those actions out. So it's more of a you know this user's unskilled let's say but with the agent they can do you know higher

**George Westbrook:** Amazing.

**Michael Moores:** skilled things with guard rails basically. So you know down the line make okay the agent when this user uses that agent they have higher privileges. So that's something we come about later.

**George Westbrook:** Yeah.

**Michael Moores:** But for now, I think if we stick with the user permissions, I think each permission has approval field on it or not. And then obviously we what we need to do is then say, okay, this action attributes to this permission. And obviously that permission needs approval.

**George Westbrook:** Heat.

**Michael Moores:** And then we fold that in whether or not we have something in the agent says, okay, you've got one pending approval.

### **00:32:56**

**Michael Moores:** You make that agent easier for to approve and and discuss that approval.

**George Westbrook:** Thanks.

**Michael Moores:** Obviously we also have the approval queue pages. as well for them to go on and either do it in the console or their mobile to quickly approve things on you on the go. Basically,

**George Westbrook:** Yeah. Yeah. Because I suppose the the two approvals are I am a user. I've not got enough access. Even if I was doing it in the console, I need approval. And then I suppose there's the approval of I as a user have access if I wanted to do it in the console but an agent taking action on behalf of me um maybe might want to just double check that are you sure that you want to do this like are you sure you want to delete a card?

**Michael Moores:** Yeah.

**George Westbrook:** Okay. Um okay that feedback really really helpful. Um, never worrying about too brutal feedback. It's it's it's it's quite what it's good getting that sort of feedback.

### **00:33:56**

**George Westbrook:** Um, I think we we've got a call tomorrow, haven't we? I think where we're going to go through some of the the phase phase two stuff. Um, I mean, we kind of started on some of the phase two with that agent inbox. Um, which Dörte should be working working in production now. Um so I suppose it's so tomorrow we'll talk about some of the phase two stuff prioritization um and then obviously content workforce and outbound um quick updates on that. So I think Tyler will probably be reaching out um having conversations with you guys and then outbound through the process of what getting the getting all the domain sources. So that should be done very shortly and then getting the lead lists built as well. So send sending them over just so you can have a look as well.

**Max Kingaby:** Just just to um that I have messaged Dörte had been your response. So would you like to wait then until we've done that session with Brett before we kick off from Tyler or we like to

### **00:34:59**

**Dorte Dye:** Yeah,

**Max Kingaby:** experiment

**Dorte Dye:** I mean Ian, that's what I said this morning to Max that I want to just see where we are, what is missing, and then we regroup and book a follow-up session with Tyler and Max to push on with the content works.

**Ian Johnson:** Yeah, makes sense.

**Max Kingaby:** just yeah uh we'll do that call and then we'll book I'm a thought of Jesus.

**Ian Johnson:** Sounds good. I enjoy barley. Lily, I don't know how you managed to like kind of not get an invite or what's going on there was

**Lily StClair:** I'm going next week.

**Ian Johnson:** going.

**Lily StClair:** I just have a lot of hockey to do.

**Ian Johnson:** Okay, got it. All right. Okay, cool.

**George Westbrook:** Unfortunately, Bre's coming next week as well.

**Ian Johnson:** Yeah. Well, get you funny while you can.

**George Westbrook:** Yeah,

**Ian Johnson:** Dad jokes are bound shortly. So, you just you got

**Max Kingaby:** Oh god,

**George Westbrook:** that that Yeah,

**Max Kingaby:** I might get the next fight home now.

**George Westbrook:** that's that's the good thing about having calls with Brett when he's in the tunnel is you usually can't hear him because he's not connecting. size was

**Ian Johnson:** I I'll leave you to your internal disputes.

**George Westbrook:** Right.

**Max Kingaby:** guys.

**Ian Johnson:** Dear folks,

**George Westbrook:** Perfect.

**Dorte Dye:** Okay,

**Michael Moores:** Okay,

**Dorte Dye:** take care.

**George Westbrook:** Speak to you soon.

**Michael Moores:** take care.

**Max Kingaby:** Bye.

**George Westbrook:** Have a good one.

**Michael Moores:** Bye.

**Max Kingaby:** Bye.

**Lily StClair:** Bye-bye.

**Max Kingaby:** Night.

### **Transcription ended after 00:37:32**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*