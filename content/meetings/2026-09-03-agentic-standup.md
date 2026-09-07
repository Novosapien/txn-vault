---
date: 2026-09-03
type: standup
description: "Ian's first standup back, turned into a live demo: he rejects the show-every-step interaction model and gives the value test that should govern the design"
scope:
  - "[[full-agentic-experience]]"
  - "[[co-pilot]]"
  - "[[agent-inbox-alerts]]"
  - "[[agent-access-layer]]"
status: extracted
extracted-to:
  - "[[process-surfacing]]"
  - "[[agent-orchestration]]"
  - "[[approval-queue-integration]]"
  - "[[agent-inbox-alerts]]"
  - "[[scheduled-reporting]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-09-03)

> **Source:** Gemini transcript, 3 September 2026, 14:30 BST, 40m. Brett StClair, George Westbrook and Max Kingaby with **Ian Johnson** and **Dorte Dye**. **Michael Moores absent**, his leave having started that day.
>
> **Filed 7 September, four days late and out of order.** The 3 September ICP session and the 4 September domains session were both processed ahead of it. That matters here more than usual, because this is the call where **TXN's commercial lead gave the first substantive critique of the agentic experience**, and it sat unread while the pilot's final week ran.
>
> **Shape of the session.** Ian's first standup since returning from holiday. Brett made it a demo rather than a status round: *"Ian hasn't been in a standup since he's been back from holiday. Shall we do a demonstration for you?"* George showed two builds from two work trees, the **agent inbox** (conceptual, mocked) and the **full agentic experience** (deployed). It became a design review.

## The headline: Ian rejects the interaction model

Not the product. He was warm about the product throughout, *"it looks great and I'm super positive about it"*, and *"there's been a tremendous amount of progress."* What he rejected is how it talks to the user.

### What he said

> *"I don't care when Claude tells me what agents it's running or tools it's running. I literally do not care."*

> *"The only interaction should be: I need you to confirm something before I go and do something."*

> *"Showing all the steps, either that you're going to take or you are taking, I think that's probably just a little bit [much]... for the really basic ones. I want you to suspend this card and you need to suspend it straight away."*

And on the chain of approvals, which is the sharpest line in the session:

> **"Nobody will ever use this. They'll do it once, they'll never do it again."**

> *"Seeing through and waiting for each of these steps to go, notwithstanding the speed thing, it's just too much for something that has a low risk."*

### The journey he wants, in his words

Suspend a card, end to end:

1. *"I've put in a simple request that requires me not to come with any information but apart from the person whose name I know: suspend this card."*
2. *"I do need the next thing, the interaction should be: this is the card that I'm going to suspend, please approve. Or, here are a number of cards in James Thornton's name, which one is it you want me to suspend?"*
3. *"From the minute that you click approve, I expect that that's done."*

He conceded the confirmation step willingly, and for a precise reason: the name is not an identifier. *"James Thornton in an API call doesn't mean anything, it won't identify."* So the approval exists to resolve a person to a card, not to gate the action.

George's read-back, accepted: *"it would just be, please suspend this card, quickly get the plan, is this good, yes, do it. And then it's done. Then they can go away and they don't need to worry."*

### The comparison that makes it urgent

> *"By now, in the console, they would have found James Thornton's card and suspended it. Not by now, probably about five minutes ago."*

> *"We're just going to have to make sure that we're super conscious of the fact that these things are supposed to be making things easier and faster."*

George agreed without qualification: *"if it took 20 seconds to get a response back to me, I'd just click in the console and not use it again."*

### Why this is a trust problem, not a speed problem

Ian's argument runs past latency into abandonment:

> *"The minute they start distrusting, either through speed or because something gets lost in the ether and doesn't work... I just worry that people won't go back to actually using [it]."*

He built the failure case out loud. A user can already check the API themselves through the health endpoint, so if the API is up and the card was confirmed and the suspension still fails, *"that's down to the AI, that's the issue. And it would worry me if that was the case."*

George's answer, which is the right one and is not yet built: the agent gets the error and the reason back, and can investigate with its own tools rather than the human having to. *"Rather than a human going, oh wait, this got suspended, oh let me go check health, oh let me speak to John because he knows about this part... the agent's going to do all of that."*

## The value test Ian gave us

The most useful thing in the session, and better than anything currently written in the vault. **Judge every agent action by how the user would do it without the agent.**

| | Low value | High value |
|---|---|---|
| **Example** | Suspend a card | Investigate declines, analyse a programme |
| **Ian** | *"minimal speed or ease value... I didn't have to move, but it wouldn't have been the end of the world if I had to go to the control center"* | *"I probably wouldn't have even done that. I might not have even known that was happening in my card program because I wouldn't have known necessarily where to start"* |
| **The general case** | The user already knows how, and it is two clicks | *"If I had to do that manually, that would be horrific. And that's the point of it"* |

> *"So some of the things will be relatively low value and people will say 'oh well, okay, it's great, I didn't have to move.' And other things will be, well, I probably wouldn't have even done that. So I think you just have to think about it in those terms really."*

**This is a design principle, not feedback on a build.** It says the ceremony a task carries should be proportional to the value the agent adds, and low-value tasks should carry none.

## What it does to a decision the vault has held since June

[[process-surfacing]], the Co-pilot's trust UI, was settled on 9 June with two positions:

- **Surface bucketed categories** of activity rather than raw per-agent detail
- **One universal altitude**, with the per-user "AI slider" (0 to 4) **rejected** as needless complexity

**Ian does not reopen the slider, and it is worth being precise about that.** The slider varied the detail level **per user**. Ian is varying it **per task**: nothing for a card suspension, more for an analytical session. Different axis, so the June rejection stands.

**But "one universal altitude" does not survive.** That position assumed a single level works for everything, and Ian has just said the level that works for declines analysis actively drives users away from card suspension. The dial the June session set is real; what it got wrong is that there is one setting.

## George's resolution: two classes of workflow

Proposed on the call and accepted by Ian. This is the actionable outcome.

| Class | Behaviour | George's framing |
|-------|-----------|------------------|
| **Quick actions** | Confirm the target, then go. No step surfacing, no chain of approvals | *"I've got this, just do it for me, I don't care, just get it done"* |
| **Work with me** | The conversational build-up stays. Plan, discuss, refine, then act | *"let's investigate declines given this, let's analyse, let's create a plan... the sessions where you go and spend about half an hour speaking to it before you make an action"* |

**The work it implies:** *"go through those user journeys, turn them into those skills or SOPs, and then rank them in terms of what ones are these quick actions."*

That is a classification pass over the thirteen journey documents and every SOP already built, and **it has to happen before the SOPs are written against the wrong shape**. Six ranked workflows already exist on `main` from the 26 August slate build, written before this conversation. Raised at [[open-questions]] #83.

George's own assessment of where that leaves the build is fair: *"we've got most of the parts. It's now just assembling them in different ways for different use cases."*

## The gap this opens: input without a chat

If quick actions run silently, the agent still needs a way to come back for a **question** rather than an **approval**, and the answer cannot be "reopen the chat and read everything."

> George: *"the one thing that we haven't got, that we would need, because I think we need to change the UX a bit, is that it's a quick action, go away and do it. I need your input. What's the best way to do that? Is it going back to a chat? Is it a little icon up here which you click on, it opens out a modal in the middle, then you just put in a quick response and it goes away and you're not having to open a chat and read through everything."*

Nobody answered. Raised at [[open-questions]] #84.

George noted the audit position is unaffected either way: *"the good thing for us is, from an auditable perspective, we're going to have everything as if it was a big long chat with every single tool call."* So hiding the process from the user does not cost the record.

**And Dorte set the hard constraint on it before she dropped off:**

> *"Would you see then if it asks for a request? Because that I think is important. I'm happy when the agent needs a request and it takes longer, but I get really impatient if nothing explains why [I'm] waiting."*

**Silence is only acceptable when the agent is working. A wait must always carry its reason.** That is the boundary on Ian's ask, and it comes from the other TXN user.

## The agent inbox, demonstrated

First proper walkthrough of the alert flow, from the conceptual work tree.

**The sequence:** alert arrives → an **agent team** investigates → produces what happened, a graph of why, what it means, and **what has been ruled out** → proposes a plan → human approves → executes and **runs tests**.

The approval is **editable, not binary**. George demonstrated changing a proposed transaction limit from one value to another before approving, and the UI shows the consequence of the change.

**Audit trail on the panel:** alert detected, analysis started, analysis finished, plan proposed. More to come.

### Staleness re-analysis, and the risk George named himself

A plan approved a day after it was proposed gets **re-analysed before execution**, to catch a larger impact or an outdated plan.

He flagged the failure mode without being asked: *"the only issue I can foresee is if they're waiting a day every time, and it keeps on saying 'well I need to change this, I need to change this'... it could get annoying."*

His resolution: **"it's better to be safe and annoying than easy and destructive."**

> Worth holding that against Ian's feedback above, because the two pull in opposite directions and both are right. The reconciliation is the two-class split: a low-risk quick action does not need staleness re-analysis, an alert remediation plan does.

**This week's build:** making it real. Real agents executing real tools against the **mocked API**, so *"from the agent's perspective and our perspective when testing, it's going to look exactly like the real thing, just not touching any real endpoints."*

### Ian's alert question, unanswered

> *"What defines the need for an alert? How are we going to identify that something requires an alert?"*

He set out the two poles himself: it is either *"really resource-heavy"* or *"driven by the agentic"*, and he noted the historical alternative, *"you would configure the alerts on a platform and then they would just run."*

George's answer was partial and honest: it depends on **what Direct Transact expose** (*"we probably have to have a look more at what's being exposed"*), and the creation mechanism would work like the reports, below.

**This is [[open-questions]] #68 arriving from the other direction.** #68 records that DT has no alerting system and Michael wants the AI to be the central one. Ian is now asking what triggers an alert in the first place. Neither is answered, and they are the same question from the two ends: **if nothing on the platform side raises alerts, the detection logic is ours to define as well as to build.**

## Scheduled reporting: speak it into existence

Same interaction pattern for both reports and alerts, and it is the strongest UX idea in the demo.

> *"Rather than it being you click, click around, blah blah blah, you just... put in like a sentence. I want to see a report every two weeks on this, this, this. You just speak it into existence and then the agent's going to understand what you've put in. It's going to turn that unstructured data into structured outputs."*

**The second half is the part not yet built.** The natural-language spec also generates **the prompts or guidance for the agents that will do the analysis**, not just the query parameters:

> *"let's say it gets the decline rates every week for a card program. Then you could maybe put in: analyse these transactions to see what the merchants are and if there's any similarities between XYZ. Which is more like AI-focused rather than just a database query."*

So a scheduled report is two things: a recurring data pull, and a standing analytical instruction. Alerts work the same way, *"alert me when blah blah blah is over a certain amount."*

Manual creation stays available for anyone who prefers to click, and George raised creating them **from inside the agent** as a third route.

## Permission-aware behaviour, demonstrated

The agent attempts an action, the user's access level rejects it, and the agent then tells the user **who to request approval from** and waits.

Visual states: **flashing orange** waiting for approval, **green** clear to proceed.

This is the first time the vault has seen [[permission-scoping]] behaviour running rather than described, and it lands on the pilot's deliberately deferred all-access monolith, so it is a demonstration of the shape rather than of real scoping.

## Smaller build changes

| Change | Detail |
|--------|--------|
| **Tool names replaced with plain language** | Was *"I'm going to execute this tool [name]"*, now *"I'm going to take this action."* Directly in line with Ian's feedback and predates it |
| **Skills auto-load without slash commands** | Slash commands exist as quick actions, but are not required. *"If you go 'please suspend James Thornton's card', it's going to load in the skill anyway"* and follow the process |
| **Checklist in the top left** | Written as the agent works. Two purposes: *"it keeps the agent accountable"* and the user can see *"I'm at stage one and there's three steps left."* Collapsed by default |
| **Canvas rendering** | Components render in the chat and expand to the side panel. Continues the 4 August canvas-primary decision |
| **Voice dictation** | Present in the agent surface |
| **Feedback flag per message** | For testing: flag a specific message rather than writing one long note, *"less chance for confusion."* A production version would sit at the bottom of the surface |

## Two technical findings worth separating out

### The demo was hit by an Anthropic outage, and the conclusion is architectural

The agent stalled live. George diagnosed it mid-call: *"code has a partial outage... I've seen it here on Claude Code actually. This has got to be an Anthropic issue."*

**His conclusion is the finding, not the outage:** *"what we'll need to do there is have the fallbacks with the LLM"*, arranged as a hierarchy.

He also proposed a model change for speed, off Sonnet or Opus onto a faster model, on the reasoning that *"the faster they are, the cheaper they are... but the good thing now is the fast models are still really really good."*

> **Nobody connected this to [[open-questions]] #70**, which asks whether hosting in DT's Azure tenant constrains which models can be used, and where the action on Novosapien is to produce the list of models and frameworks for Michael to put to DT. **A fallback chain across providers makes that list longer and harder**, and if the primary model changes as well, the list changes before it has been sent. Michael is away until 15 September, so the list should be ready when he returns rather than started then.

There is also a **UX bug** George found in the same moment: a pasted message does not render until the model responds. Fix identified, render on send rather than on response.

### Ian and Michael want opposite things, and it was resolved by hiding one

Michael asked for **every tool call visible in the chat**. George: *"one of the things Mike said that would be really handy is seeing, in the chat, every single tool call that happens."*

Ian, immediately: **"Valuable for who? Valuable for who?"**

George's resolution is to keep it, hidden in the top right, *"only going to show up when it's clickable, but no user is ever going to see that."* Brett: *"unless the user's name is Mike."*

**Recorded because it is a genuine disagreement between the two TXN stakeholders who matter**, and it was settled by concealment rather than by a decision. It works, but it means Michael's request has been honoured in a form he has not seen and Ian's objection has been honoured in a form he has not been told about. Worth naming when Michael is back.

## Dorte has still not tested

Said plainly, and the reason is not reluctance:

> *"That's why I haven't done any testing yet whatsoever. I gave it a warning last week. I just really need a day deep dive where I just focus on your stuff and nothing else."*

She is in compliance and regulation work, and named it as what is eating her: *"the topics these days are not fun. I want to do operations. I want to talk to customers, to human beings."*

**She has since booked Monday 7 September for exactly that deep dive**, with written feedback by close of business Wednesday 9 September ([[2026-09-04-domains-and-september-schedule]]). So this resolves the following day, but it means **that as of the 3rd, with the pilot completing on the 7th, no one at TXN had tested it**: Michael left that morning, Ian's testing has been *"limited"* by his own account, and Dorte had done none.

## Findings and where they landed

### The interaction model

| Finding | Destination | Action |
|---------|-------------|--------|
| **Ian rejects step surfacing and stacked approvals for low-risk actions** | [[process-surfacing]], [[agent-orchestration]] | Recorded; the June "one universal altitude" position is superseded |
| The value test: judge every action against how the user would do it without the agent | [[process-surfacing]], [[full-agentic-experience]] | Recorded as a design principle |
| Speed is an abandonment risk, not a performance metric | [[agent-orchestration]] | Recorded |
| The confirmation step survives because a name is not an identifier | [[approval-queue-integration]] | Recorded; it narrows what approvals are for |
| **Two classes of workflow, and every journey needs classifying** | [[open-questions]] | New row **#83** |
| **No way to ask for input without reopening the chat** | [[open-questions]] | New row **#84** |
| **Dorte: a wait must always explain itself** | [[process-surfacing]] | Recorded as the boundary on silent execution |

### The agent inbox and reporting

| Finding | Destination | Action |
|---------|-------------|--------|
| Alert flow demonstrated: investigate, report, rule out, plan, editable approval, execute, test | [[agent-inbox-alerts]], [[plan-and-execute]] | Recorded |
| Staleness re-analysis on delayed approval, and the annoyance risk George named | [[plan-and-execute]] | Recorded, with the two-class reconciliation |
| Real agents against the mocked API, in build this week | [[agent-inbox-alerts]] | Recorded |
| **Ian: what defines the need for an alert?** | [[open-questions]] | Added to **#68**, which it meets from the other end |
| Reports and alerts are both created in natural language, and the spec generates the **analysis instruction** as well as the query | [[scheduled-reporting]], [[alert-detection]] | Recorded |
| Permission-aware rejection and request-approval routing, demonstrated | [[permission-scoping]] | Recorded |

### Technical and delivery

| Finding | Destination | Action |
|---------|-------------|--------|
| **LLM fallback hierarchy needed**, surfaced by a live Anthropic outage; and a model change proposed for speed | [[open-questions]], [[architecture]] | New row **#85**, tied to #70 |
| Michael and Ian disagree on tool-call visibility; resolved by hiding it | [[open-questions]] | Added to **#26** |
| Tool names replaced with plain language; checklist; skills auto-load; canvas; voice; feedback flag | [[agent-orchestration]], [[conversational-interface]] | Recorded |
| **No one at TXN had tested as of 3 September** | [[open-questions]] | Added to **#51** |

### Context, no action

| Finding | Note |
|---------|------|
| Ian on the outbound sessions | *"Outbound workforce, or compliance or regulation, will get me off this call in short order."* Said as a joke, in response to ten two-hour sessions in his diary. The Outbound engagement depends on his time, so it is worth knowing how he experiences it |
| Two work trees, run in parallel | The conceptual inbox and the deployed agent are kept in separate work trees *"so they don't get mixed over"* |
| The knowledge hub is live in staging | Ian: *"the knowledge hub is actually in staging in Azure in Europe and that health point call works."* Novosapien's equivalent is the mock. Relevant to #62, where Dorte named the knowledge hub as the launch blocker |
| George deployed shortly before the call | *"I shouldn't push things to deployment right before a call"* |

## Open actions from the call

| Action | Owner | Note |
|--------|-------|------|
| Classify every user journey as quick action or work-with-me | Novosapien | The pass George proposed. Six SOPs already exist, written before this |
| Decide the input-without-chat mechanism | Novosapien | Icon, modal, or back to chat. Undecided |
| Build the LLM fallback hierarchy | Novosapien | Surfaced by a live outage |
| Decide the model, then update the list for DT | Novosapien | Ties to #70. Michael back 15 September |
| Answer what triggers an alert | Both | Ian asked, nobody answered. Depends partly on what DT expose |
| Dorte's deep-dive testing day | Dorte | Booked for Monday 7 September |

---

## Transcript

Sep 3, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:03**

**Brett StClair:** from that. Oh, yeah. I I was speaking to listening the other night. Oh. Oh, you're probably going to have to demo the card. Ian's in his first meeting for the stand up. So, be ready for a demo. Oh s\*\*\*. Anyway, this girl's not happy. Okay. I'm going to dial in. Okay. But be ready for a a demonstration. Hello everybody.

**George Westbrook:** Hello.

**Ian Johnson:** Hey, how are you doing?

**George Westbrook:** Long time no see.

**Brett StClair:** No, don't

**George Westbrook:** How we

**Ian Johnson:** Yeah,

**George Westbrook:** doing?

**Ian Johnson:** we're doing all right. If D sent me any emails that had any good news on them, I'd be saying fine, but she never does.

**Brett StClair:** D. What I'm going to do is I'm going to send you a good news email that you can forward on to

**George Westbrook:** I'm send you some knowledge. Oh, what is this with the the the 10 other um outbound workforce sessions? The 10 2hour workforce

### **00:01:20**

**Dorte Dye:** It looks like a lifetime,

**George Westbrook:** sessions.

**Dorte Dye:** George. A lifetime.

**Ian Johnson:** You think that's that is not the most painful thing in the day of the life day in the life of tick then let me tell

**Dorte Dye:** I mean,

**Ian Johnson:** you first I wouldn't

**Dorte Dye:** that's the entertaining part, right? Boring,

**Brett StClair:** It's actually It's fun

**Dorte Dye:** but entertaining.

**Ian Johnson:** describe either.

**Brett StClair:** though.

**Ian Johnson:** So that's

**Brett StClair:** Um, while everyone's here,

**Ian Johnson:** not

**Brett StClair:** Ian and I would like to just finish off the first the last part of the outbound. Um, we just need to finish the last ICP. Okay, let's go, Ian.

**Max Kingaby:** This guy's on that sub list that I was just talking to you about,

**Brett StClair:** Stop it.

**Ian Johnson:** there's two things you can say to me.

**Max Kingaby:** bro.

**Ian Johnson:** Outbound workforce or compliance or regulation will get me off this call in short order.

**George Westbrook:** What? You put us in the same bucket as compliance.

**Ian Johnson:** Okay.

**George Westbrook:** Oh my god.

### **00:02:08**

**George Westbrook:** Oh

**Dorte Dye:** You last time you said you love legal,

**Ian Johnson:** Nothing's

**George Westbrook:** no.

**Dorte Dye:** George. Compliance is so close. We love the whole s\*\*\* what they're throwing at us.

**Ian Johnson:** nothing is in the same bucket as

**Dorte Dye:** Seriously, that's why I haven't done any testing yet

**Ian Johnson:** that.

**Dorte Dye:** whatsoever.

**Brett StClair:** Oh,

**Ian Johnson:** Yeah.

**Brett StClair:** now

**Dorte Dye:** I gave it a warning last week. I just really need a day deep dive where I just focus on your stuff and nothing

**Brett StClair:** what? Should we make this a little bit fun?

**Dorte Dye:** else.

**Brett StClair:** Because Ian hasn't been in a standup since he's been back from holiday. Shall we do a demonstration for you, Ian? Would that

**Dorte Dye:** I thought you asking about naming the Asian again because Ian would really love

**Brett StClair:** be

**Dorte Dye:** that.

**Brett StClair:** So,

**Ian Johnson:** No,

**Brett StClair:** did you hear the the idea I had to call you agent?

**Ian Johnson:** no.

**Brett StClair:** So if you guys are a card transaction system then surely it should be Kardashian.

### **00:03:06**

**Ian Johnson:** Oh my god.

**George Westbrook:** Yeah,

**Ian Johnson:** I can actually see I can see Lily visibly dying each time you you crack a dad

**George Westbrook:** I know.

**Dorte Dye:** I mean, can you imagine Lily?

**George Westbrook:** f\*\*\*.

**Ian Johnson:** joke.

**Dorte Dye:** Poor Lily. She has spent now even more time with him.

**George Westbrook:** I'm just worried when Lily gets more comfortable to start making jokes that she's grown up under Brett and that they're gonna we're gonna have two people making Brett jokes.

**Dorte Dye:** I don't think so.

**George Westbrook:** I

**Dorte Dye:** It doesn't work for Dorte and father yet. Give a couple of weeks and he I think Brett will be in hell. I mean that would happen with my daughters.

**George Westbrook:** I think I think as soon as as soon as Lily starts cracking those jokes, we're going to have a a 4day work from home

**Dorte Dye:** Pardon?

**George Westbrook:** policy.

**Ian Johnson:** Five.

**George Westbrook:** Yeah. Yeah. Just just cancel cancel the office.

**Brett StClair:** So,

**George Westbrook:** So

**Brett StClair:** this will be a fun session then and we'll do a demo for you.

### **00:04:03**

**Ian Johnson:** know that would be welcome relief. I would

**George Westbrook:** Let me just get it out. There'll be there's two there's two different things that one of them.

**Ian Johnson:** say

**George Westbrook:** One's more conceptual with which in the background is being work like making it real and the other one is is real like is the agent that full agentic experience that we talked about. Um just loading them both up.

**Brett StClair:** Is it take time because you're firing up the one container that you've got running to host it all?

**George Westbrook:** No,

**Brett StClair:** No.

**George Westbrook:** one's locally with one's one work tree,

**Brett StClair:** Okay.

**George Westbrook:** one's another work tree, so they don't get mixed over. So, if I can start with this one. So, this is the when it loads up. Can everyone everyone see this? Yes. So this this is one of the things that we f\*\*\* sake turned off stop presenting. Still

**Max Kingaby:** George,

**George Westbrook:** can't.

**Max Kingaby:** I can't see it.

**George Westbrook:** There we go.

### **00:05:16**

**Dorte Dye:** Okay.

**George Westbrook:** So this this is one of the things that that we were talking about the the agent inbox. So I think Dorte you saw this saw this I think earlier on in the week. Um and this is where that alert happens. Um, obviously initially it would just maybe be just an alert and then maybe a little bit of AI analysis, but we could go straight to this point if needed where an alert's going to come in. What's going to happen is there's going to be an agent team behind the scenes that that is going to handle um both the investigation of the alerts, the building a kind of mini report um and then a plan of potential action. Um, so let's say this is this is a an alert that has been picked up. So there'll be a team that's going to go out and given this alert is going to investigate for the for the user or for the um program. Um it's going to say what happened, build a graph as to say depending on what the actual alert is um why it happened um what it means and what what things have been ruled out and then it's going to propose a plan.

### **00:06:26**

**George Westbrook:** So this is always that human in the loop. It could be set in certain instances that it just goes away and auto fixes it. But obviously first we'd want to start with the investigation, the plan, and then the approval of that plan. Um so let's say here, restore the max transaction limit to here. Um let's say no, I want to do 300\. So you'll see what would happen if if you change certain things. And then once you click approve, this is all mocked at the moment. So there's not actual agents in the background doing it. Um but what it's going to do, it's going to go away. It's going to create take the necessary action. Um run some tests as well. And I think what would be good after just more validation, more more kind of reporting after. Um so this is different to what we're calling I think we'll call it the main agent at the moment which is more that Claude style question answer things like that. This is that proactive um Brett with the M dashes.

### **00:07:27**

**George Westbrook:** This is AI. That's right. That he's he's got to chime in every time. Um but this is more like the the workforce thinking. Um where it's not just one one agent. It's teams of these specialized AI agents working together, tightly scoped um responsibilities. um they've only got access to certain tools in order to be able to do their job, but when they work together, it's way more powerful than um a single agent that just goes,"Let me do everything." Um so along here you've got the audit trail as well. So when was the alert detected, when did the analysis start, when did it finish, um when was the plan proposed? Um there's a few more things we're going to be adding to the UI. Um but one of the things that that we're going to add is initially it's going to make that plan. Um, but let's say it created the plan a day ago. Um, you click approve. What it's going to do is then re kind of reanalyze it if there's a certain amount of time in between it to see if there's any larger impact or if the plan that it proposed is outdated.

### **00:08:34**

**George Westbrook:** Um, the only issue I can foresee is if it's every they're waiting a day every time in order to do it and it keeps on saying,"Well, I need to change this. I need to change this. I need to change this." It could get annoying. Um, but it's better to be safe and annoying than easy and destructive in my in my opinion. Um, so one one of the things we've been working on this week is making this real so that when you click when you click approve so at the moment you see this will just restore it um when you click approve there's actually going to be real agents executing real tools not on the real API um because we've currently just mocked the whole API um with mock data like like we said we were going to do um but from the agents perspective and our perspective when testing it's going to look for act exactly like the real thing just not touching any real end

**Ian Johnson:** It's great. I suppose I saw Mike had made a sent an email about

### **00:09:28**

**George Westbrook:** points.

**Ian Johnson:** where alerts were going to be managed and how is that whole piece going to be. I guess for me the question is really what defines the need for an alert? How are we going to identify that something is requires an alert?

**George Westbrook:** H

**Ian Johnson:** Um, and that that can be either really resourceheavy or it could be driven by the agentic, I guess, in terms of here's here are the things that we think we should alert you to because the only other way is typically if you if you go back some time, you would config configure the alerts on a platform and then they would just

**George Westbrook:** Yeah.

**Ian Johnson:** run

**George Westbrook:** So I I think with that there might be some new bill need like needed um maybe a depending on what DT are able to do um we probably have to have a look more what what's being exposed um but one in in terms of actually creating the alerts it would be similar to these how we're thinking about creating these reports as well.

### **00:10:54**

**George Westbrook:** So what it would rather than it being you click click around blah blah blah you just go once again this is mocked. So just imagine I'd put in like a sentence. I want to see a report every two weeks on this this this. Um you just speak it into existence and then what the agent's going to do it's going to understand what you've what you've put in. It's going to turn that unstructured data into structured outputs here. And then also um which I don't think added into here is if there's any like AI analysis that is needed um it's going to construct like the prompts or the guidance for the agents which are going to then go out and analyze that data. So let's say it gets the decline rates every week for a card program. Um then you could maybe put in analyze these transactions to see what the merchants are and if there's any similarities between XYZ which could be which is more like AI focused rather than just like a a database query. But in in the same way for alerts.

### **00:12:01**

**Ian Johnson:** Yeah.

**George Westbrook:** So it could be the there's an alerts one here where you create the alerts. We say alert me when blah blah blah is over a certain amount. Um it creates alerts. It can tell and may yeah there's there's a lot we can do there. Whereas I think from a user's perspective they just speak it into existence. Also give them the flexibility that if they do want to click around and do want to manually create it they can. Um and then also potentially creating it actually from within the agent as well. Um which I think if I go to here, this is the better version of the agent. So let's just say so one of the things we've got are these slash commands similar to Claude like kind of quick actions. um with a lot of kind of like the the SOPs that that we spoke about, but you don't need to use them. Um like you can say, right, I want to do the suspend a card one, but if you go please suspend James Thornton's card, it's going to load in it's going to load in the skill anyway.

### **00:13:22**

**George Westbrook:** Um, so as soon as it detects, oh, you're working on you're working on this part. I'm going to load in this skill and then follow this process. Um, I think the only thing so one of the things we were working on which I'm not sure is included in in this version that's deployed is it was a tiny little thing where the agent would say,"Oh, I'm going to execute this tool." And then give the tool name. Um, now it's going to say it in I'm going to take this action. Um, rather than a more like technical focused approach. So, usually with all of these, it's going to say this is my plan. This is what I'm going to do. Do you agree? So, just put in yes. And then what it's going to do in the top left is it's going to start writing. I think it does it for this one is it's going to start writing like a to-do list or a checklist. So, one, it keeps the agent accountable.

### **00:14:15**

**George Westbrook:** So it's always top of mind. Um but also from a user's perspective, they can see like, okay, I'm at I'm at stage one of um of the process and there's there's three steps left. Um and then if they want to see more detail into the tool calls, they can um but the default view is it's all it's all collapsed. um cuz most people just want to know right what what happened um what's been loaded. So I think now it's just speaking to the MCP server

**Ian Johnson:** Yeah, we need to speak a lot faster than this.

**George Westbrook:** is so with with some of the with some of the the tools where it's writing a lot of data into a tool call. Um like say for example one one might pop up in I'll show another one where it creates like a a list of all the transactions. Um it's got to manually write in all of the data that goes into it. Um but this one should be a lot quicker than this. still still working away.

### **00:15:31**

**George Westbrook:** Um, but one of the things we've also got is because we can imagine over time the these might be longer workflows or if there's like approval that's needed from let's say I'm one user, I've only got certain access and it's I'm working through something and I need to take an action that I'm not authorized to do. The agent's going to try to take the action, but given the user's access levels, um it's going to reject it and then tell the agent to go, you need to request approval from XYZ in order to um in order to carry on. And then there's just these like colors down here where it's okay, this one, it's a flashing orange one. It's waiting for approval. This one's green. You can carry on. Um, just so it makes it a bit easier to see

**Dorte Dye:** But would you see then if it asks for a request because that I think it's important.

**George Westbrook:** visually

**Dorte Dye:** I'm happy when the agent needs a request and it takes longer but I get really impatient if nothing explains why waiting.

### **00:16:33**

**George Westbrook:** that yeah, this I I think this is why I don't I shouldn't push things to uh to to deployment um right before a call. Um, code has a partial outage. Oh, does it? Uh, that might be why. Yeah,

**Dorte Dye:** What? You run out of

**George Westbrook:** that's No,

**Dorte Dye:** credits.

**George Westbrook:** it's I I've seen it here on claw code actually. So, what we'll need to do there is have the fallbacks with the LLM. So, if one LLM um if it if it Yeah.

**Dorte Dye:** the exchange to a one.

**George Westbrook:** So then it's every like a hierarchy that like first will be um

**Dorte Dye:** Yep.

**George Westbrook:** let's let's try this again cuz like some of these like tiny UX bugs as well like I've just pasted in that message and it's not popped up yet because the LLM um the LLM hasn't responded yet. So it's like where what we'll need to do is we'll just rather than it we send it and then when we get a response um that's when it's currently rendered we just render it straight away.

### **00:17:44**

**George Westbrook:** Yeah, this has got to be this has got to be an anthropic issue. I'm shoot I was think I was thinking what is going on but the fact that he's not

**Ian Johnson:** But it was slight.

**George Westbrook:** even

**Ian Johnson:** My general feedback when I when I have tested it's been limited is that it has been it has been pretty slow and I think the challenge there is what have we

**Dorte Dye:** Hello.

**Ian Johnson:** improved from a customer experience here versus what they could do in the console by now in the console they would have found James Thornton's card and suspended it not by now probably about five minutes ago so if we're

**George Westbrook:** Yeah. Yeah. Yeah.

**Ian Johnson:** not We're just going to have to make sure that we're super conscious of the fact that these things are we're supposed to be making things easier and faster.

**George Westbrook:** Yeah. Yes. I think maybe what we might need to do is take a a slightly Well, to be fair, there was a new model that came out yesterday that'll be that'll be perfect for this.

### **00:18:52**

**George Westbrook:** Um, it's it's a lot faster because it's always trying to balance the the performance and the speed.

**Dorte Dye:** Oops.

**George Westbrook:** Usually the the the faster they are, the cheaper they are, which is better, but then the more likely they are to like misconstrue something. But the good thing now is the the fast models are still really really good. Um, so it's like I think we maybe switch it from I think we're using Sonnet Sonnet or Opus at the moment. um and Sonet or Opus at the moment and switch it to that um Gemini Flash 3.8 which is meant to be absolutely rapid. Um one of the things we got as well is the the voice dictation as well. So if somebody wants to speak into it, they just click um click and speak into it. This is taking a lot longer than usual as well. Because I think one of the things um we're all speaking about as well is these multiple multiple approvals one after another. Like that's just it could be too safe.

### **00:20:34**

**George Westbrook:** Um but also from a user perspective like for me I just want to click approve once. Um so it's just trying to work out technically what's the best way to do that. Um because initially you if you click approve on everything um then one thing doesn't run correctly um then you have to kind of go back and then redo the approval which I think most of the time it there's not going to be those issues. um where it gets rejected because the agent should have already done the investigation as to see what's going to happen. Um but maybe doing that bulk approval. um slightly less safe um but the experience is going to be way way way

**Ian Johnson:** Yeah.

**George Westbrook:** better

**Ian Johnson:** No, nobody will ever do Nobody will ever use this. They'll do it once they'll never do it again.

**George Westbrook:** just just from in terms of

**Ian Johnson:** It's It's not just speed.

**George Westbrook:** speed.

**Ian Johnson:** It's just you got to consider um what we're really talking about in terms of your first point was so in this scenario whatever his name is James Thornton's got two cards so there is a decision to be made to say it's one of these two cards he's only got one card that's available I still agree with the fact of confir having the approval to say confirm this is the card.

### **00:21:59**

**Ian Johnson:** But then as far as I'm concerned as a user, that's it. Now, if in the background something runs and we we find that

**George Westbrook:** Okay.

**Ian Johnson:** that's been unable to we've been unable to complete the suspension, then there needs to be some way of alerting that. Um, but seeing through and waiting for each of these steps to go, notwithstanding the speed thing, but it's just too much, I think, for something that's has a low risk.

**George Westbrook:** Okay. So, so we what we could do is literally it would just be please suspend this card quickly. Get the plan. Is this good? Yes. Do it. And then it's done. then they can go away and they they don't need to worry.

**Ian Johnson:** Yeah. And of course if it if we can't get it if we fail because if I'm

**George Westbrook:** Okay.

**Ian Johnson:** understanding correctly the bottom line is the the little approval piece you've got because this is always the thing James Thornton doesn't really mean anything in our system.

### **00:23:09**

**Ian Johnson:** James Thornton in an API call James Thornton doesn't mean anything does it won't identify. So, you're identifying the the card number and then you're using the MCP server as I understand it to trigger the API call to suspend the

**George Westbrook:** Yeah.

**Ian Johnson:** card.

**George Westbrook:** So, all of the all of the data fetching and all of the like actions is all all done through the MCP server.

**Ian Johnson:** Okay. So from a from a from a user's perspective, um it would the thing I'm trying to figure out is what go what would go wrong in this scenario. Um, and then also if something does so long. What do we what do we do about it? Because the because the user's already told you suspend this card. The question then is if we're unable to suspend the card and there's no logical reason why that is. So we found the card, we sent the request and then for whatever reason that doesn't complete that then begs the qu that then starts to um dilute the trust that people have got in using the AI.

### **00:24:34**

**Ian Johnson:** So, for example, they could very quickly go to um their own uh health API and test whether or not the API is up. So, I think that's actually in the knowledge hub, right? So, well, it is there's a there's an endpoint check that you can test. So, they they know our APIs up. They know that they've given you approval on the card number that was the right one. And then somewhere in between those two things, we failed to suspend the I don't know if you've got the one that's in um if you go to API reference and health. If you go to health, it's underneath digital digital wallet tokens. Um, should be able to go to playground and then send a test request.

**George Westbrook:** I think I think this is I think this is only the mock this is the mock one that we've this is like the mock version that we built.

**Ian Johnson:** Well, well, the knowledge hub is actually in staging in Azure in Europe and that health point um call works. So, the is if I'm if I'm a user

### **00:25:53**

**George Westbrook:** Okay.

**Ian Johnson:** um the minute they start trusting the distrusting either through speed or because something gets lost in the ether and doesn't work um the whole I just worry that people won't go back to to actually using Okay.

**George Westbrook:** So maybe we need to transition away from thinking about as like a clawed experience where it's it's chat and you work with me to more of a I go in, I tell you what I want and you tell me when it's done. And then rather than it being they coming back to a chat, although the chat could be there, maybe it's something similar to that agent inbox which is on this version. Um not not exactly the same where it's like I give you a task, you go away and do it once I've once I've agreed with the plan. Um you notify me one if something's gone wrong, two if I need your input. Um and three if there's anything that I think you need to know. So I think one of the benefits with the with obviously the agentic approach is let's say it tries to suspend the card um it doesn't work.

### **00:27:04**

**George Westbrook:** It's going to give the error message back and give the reasoning which then allows the agent to use its set of tools in order to investigate that further. So rather than a human going oh s\*\*\* wait this this didn't get this got suspended. Oh let me go check health. Oh let me speak to John because he knows about this part a bit more than me. Um, it would just be the agent's going to do all of that. It's going to know the same, if not better, than a user as to what to do cuz not only is it got access to all of the tools, so it doesn't have to click around, um, it's going to have the whole the whole knowledge base as well.

**Ian Johnson:** Yeah, I I I can see that. I mean, don't get me wrong, I can I think there's been a great a tremendous amount of progress that's been made, but I think there the sledgehammer to crack a nut thing is to me. I've I've put in a simple a request that requires me not to come with any information but apart from the person whose name I know suspend this card.

### **00:28:16**

**Ian Johnson:** I don't need to know what you're going to go away and do. I do need the next thing the interaction should be is this is the card that I'm going to suspend. Please approve or here are a number of cards in James Norton's name. Which one is it you want me to suspend then?

**George Westbrook:** Yeah.

**Ian Johnson:** From the minute that you you click approve, I expect that that's done. In the same way that if I went to the console and said and found the card and then suspended

**George Westbrook:** H.

**Ian Johnson:** it, I I expect that that is done. It works on exactly the same basis that it's um it is the it's calling APIs and I don't know what would happen during the scenario that the console the control center itself was unable to complete the uh API call. I don't know how that would be handled by stack works, but I am just not anticipating that that there should be issues with something as basic as that the API is available because if the API if the first bit's been done, the API is available, then then that's down to the AI that's the that's the issue.

### **00:29:33**

**Ian Johnson:** And it would worry me if that was the case.

**George Westbrook:** I I think it's bit maybe the approach I was take is quite like pessimistic in that there there could be something that goes wrong this needs approval blah blah blah but like you say most of the time it's going to work and most of the time being like 99.9% and I think obviously the benefit with agents are that it can kind of fix its work itself. Um, and with with the fact that it can notify you as well. I think it's just we need to think about what's the best interface and method of of alerting them. Um, because I agree simple actions like suspending a card most of the time that's going to work or pretty much all of the time. Um I think it's just in terms of the um maybe some of the longer workflows um that's where it will there could potentially be like oh this this was maybe done before this but which we can iron out most of it with with testing because I think what one of the things we were trying to achieve with some of these workflows is not this is what we think exactly it should be in terms of all of the approval steps.

### **00:30:46**

**George Westbrook:** It was more like conceptually like this is this is what the this is what this canvas is going to look like. Um where's one? Um yeah, it was it was conceptually testing things with workflows being as real as possible. Um it's just some of the mechanisms like the approval might be a little bit different. So I think the one of the things that we've got here is in similar to Claude is these canvases. So what Claude will create when it executes uh is getting up Sarah's details. Um it's going to pull in and render those components some of them in the chat. So like maybe here this table um obviously that's not really a component but um but also on the side. So, the ability to expand it so you can see what you need within the

**Ian Johnson:** Yeah, it's great. Look, listen,

**George Westbrook:** chat.

**Ian Johnson:** don't don't get me wrong. It looks it looks great and I'm super positive about it. I just want us to make sure that, you know, that claw experience.

### **00:32:03**

**Ian Johnson:** I don't care when Claude tells me what agents it's running or tools it's running or I just don't I literally do not care.

**George Westbrook:** Yeah.

**Ian Johnson:** The only interaction should be I need you to confirm something before I go and do something. So if that is in a more complex task as you suggested George there you find once the agent starts running you find that the agents start running you find there's a rec there's a need for some point of clarification totally fine come back and ask that point of clarification but showing showing all the steps either that you're going to take or you are taking I think that's probably just a little bit

**George Westbrook:** Yeah.

**Ian Johnson:** Um, now maybe with some of the more complex tasks it's somewhat useful, but for the really basic basic ones. I want you to suspend this card and you need to suspend it straight away.

**George Westbrook:** Yeah.

**Ian Johnson:** If somebody's going to suspend somebody's card, they're doing it because they they want them not to be able to transact as soon as quick as soon as possible.

### **00:33:13**

**Ian Johnson:** the bottom

**George Westbrook:** H. So yeah,

**Ian Johnson:** line.

**George Westbrook:** I think what we need to do go through is look through those user journeys, turn them into those what skills or SOPs and then rank them in terms of what ones what ones are these quick actions where it's just go away and do it. Um which ones are yeah, I've got this just do it for me. I don't care. Just get it done. Then there's the kind of work with me ones which could be um let's investigate declines given this. Let's analyze. let's create a plan. Um like those where we all know the the sessions where you go and you spend about half an hour speaking to it before you make an action. Um I think that's where some of this stuff like is going to be more useful. But yeah, when you're trying to suspend a card, I know I agree with you. If it took if it took 20 seconds to get response back to me, I just click in the console and not use it again.

### **00:34:08**

**George Westbrook:** But I think the good we've got the most of the parts are

**Ian Johnson:** Yeah.

**George Westbrook:** there. It's now just assembling them in different ways for different um different use cases. So like obviously we've got that approval. I think the one thing that we haven't got that we would need because I think we need to change the UX a bit is that it's a quick action. Go away and do it. Um I need your approval. Not the approval, sorry. I need your input.

**Ian Johnson:** All

**George Westbrook:** Um, what's the best way to do that?

**Ian Johnson:** right.

**George Westbrook:** Is it going back to a chat? Is it a little icon up here which which you click on, it opens out a like a modal in the middle, then you just put in a quick response and it goes away and you're not having to open a chat and read through everything. Um, but I suppose the good thing for us is from an audit auditable perspective. We're going to have we're going to have it everything as if it was a big long chat with every single tool call.

### **00:35:04**

**George Westbrook:** Um, I don't know if it's in this one that here. So, I think one of the things Mike said that would be really handy is seeing every in the chat every single tool call that happens. Um, so this one, what was this? This was the suspender card. So having the ability to go in look see all of the data that's that's returned but returned from the agent what the were pardon say that

**Ian Johnson:** Valuable for who? Valuable for who?

**George Westbrook:** again Mike yeah this

**Ian Johnson:** Because

**Dorte Dye:** That's

**George Westbrook:** this why I've hidden it in the the top right hand corner which is like it's it's only going to show up when it's clickable but no user is ever ever going to see that.

**Brett StClair:** Unless the user's name is Mike.

**George Westbrook:** Yeah.

**Brett StClair:** In that case, tada.

**George Westbrook:** because there's like a few as well like this flag this flag flag um that's only there for our testing purposes. So like if you just wanted to provide quick feedback in the actual in the actual production version that users will see there'll probably be something here if they wanted to provide a little bit of feedback but it's only going to be at the bottom.

### **00:36:19**

**George Westbrook:** Um, but from our testing perspective, like if you want to if you want to raise something for for here, it's just a lot quicker rather than having to do one big long message and say it's this specific part of this message that I don't like and then then it it's not going to get confused, but there's less chance for confusion with um by doing it this way, we think.

**Ian Johnson:** Yeah, agreed. I I do I do think it's it does it will come down to whether or not doing it through the agent adds any value whatsoever. um which again is for me is about ease and speed in the case of the suspend card piece. Um I'm there anyway that I do I if I'm going to if I'm going to

**George Westbrook:** H.

**Ian Johnson:** interact with TXN I'm in the agent anyway. So that's where I work. So it's logical that I'll say please suspend this card and then coming back and saying okay which one is it approve and it's done. So it's a quick action that compared to doing it in the console there's minimal speed or um ease value but actually I didn't have

### **00:37:35**

**George Westbrook:** Yeah.

**Ian Johnson:** to move just did it from here but then there are other things where I'm asking for more of an analytical type uh engagement with the with the agent where you just got to look at it and go how and we've got to think this as a as a team. How would they go about doing that without the agent? That's the bit where people go, well, that's I think that's everyone's experience with Clawor or any AI at the moment is you look at what you're able to complete and and work you can get through and think, geez, if I had to do that manually, that would be horrific. And that's that that's the point of it. So, um, some of the things will have will be relatively low value and people like,"Oh, well, okay, it's great. I didn't have to move." But, um, it wouldn't have been the end of the world if I had to go to the control center to to do it. And other things will be,

**George Westbrook:** Yeah.

**Ian Johnson:** well, I probably wouldn't have even done that.

### **00:38:41**

**Ian Johnson:** I might not have even known that that was happening in my uh, card program because I wouldn't have known necessarily where to start. So I think you just have to think about it in those terms really.

**Dorte Dye:** I'm really sorry. I need to drop off. I have a school meeting.

**Ian Johnson:** Yeah. So, Jose, I was going to suggest that we cancel the team meeting because you're going to talk to me about compliance and regulation and I can't

**Dorte Dye:** Brilliant. Story of my life.

**Ian Johnson:** tomorrow.

**Dorte Dye:** Yeah,

**Ian Johnson:** Tomorrow I I can do it.

**George Westbrook:** That's

**Ian Johnson:** I can do it.

**George Westbrook:** one.

**Dorte Dye:** you should just get a bottle of beer and then you can do it at any time.

**Ian Johnson:** I have might impose a strict thing of not

**Dorte Dye:** No,

**Ian Johnson:** drinking during the week.

**Dorte Dye:** seriously.

**Ian Johnson:** By the way, the week is Tuesday, Wednesday, and Thursday. I play football on Monday, you have to have a drink after that. Friday, still part of the week.

**Brett StClair:** I don't know in the city

**Dorte Dye:** No, no worries. I really need to jump.

**Brett StClair:** Thursdays.

**Dorte Dye:** I booked something in for us tomorrow. Okay,

**Ian Johnson:** Yeah,

**Dorte Dye:** I'll catch up.

**Ian Johnson:** please.

**Dorte Dye:** Sorry about that.

**Brett StClair:** Awesome.

**Dorte Dye:** Thanks,

**Brett StClair:** Thanks,

**Dorte Dye:** guys.

**George Westbrook:** Tuesday.

**Brett StClair:** guys.

**Dorte Dye:** Fight.

**George Westbrook:** Have a good one.

**Ian Johnson:** Bye.

### **Transcription ended after 00:40:04**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*