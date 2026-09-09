---
date: 2026-09-08
type: standup
description: "Ian's feedback acted on in five days: faster model, approvals stripped back, SOPs being rewritten, plus the true agent inbox and Dorte's ask for benchmarks"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-inbox-alerts]]"
  - "[[content-workforce]]"
  - "[[architecture]]"
status: extracted
extracted-to:
  - "[[agent-orchestration]]"
  - "[[agent-inbox-alerts]]"
  - "[[notification-routing]]"
  - "[[content-workforce]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-09-08)

> **Source:** Gemini transcript, 8 September 2026, 15:30 BST, 21m. **George Westbrook** and **Max Kingaby** with **Dorte Dye**. **Hasan Ahmed** present, his first appearance in a standup on this record. **Brett absent. Ian away. Michael away** until 15 September.
>
> **The last call before the retreat.** The Novosapien team flies on 10 September. Dorte confirmed no session this week and that standups resume **Tuesday 15 September**, moved to a morning slot for TXN because of the time difference.
>
> **What makes this one worth reading** is that it is the answer to the 3 September session. Ian's critique landed on 3 September and was written up on 7 September; by 8 September three of its consequences were already in the build.

## Ian's feedback, acted on in five days

George opened the substantive part by attributing the changes directly: *"the other things that we've changed based on the conversation we had with you and Ian last week."*

| Change | Detail |
|--------|--------|
| **Model switched** | Off the previous model onto **another Gemini model** purely for latency. *"The one we were using was good. It just wasn't quick."* |
| **Approvals stripped out** | *"We've turned off a lot of the approvals."* Deliberately over-corrected, then added back |
| **SOPs being rewritten** | So investigation is frontloaded and the approval sits at the end, once |
| **New signalling states** | Working, needs help, error, distinguished by colour in the sidebar rather than by an approval card |

### The rewrite, and why it is cheaper than it sounds

George was careful to say the change is structural rather than large:

> *"What we're going to need to do is kind of rewrite all of the SOPs... it sounds like a way bigger job than it is. Whereas before it might do 'right, here's my plan', and in the plan there's going to be some investigation work, and then after the investigation work then you approve what I need to do. Ideally what we want is everything's frontloaded. So the investigation, blah blah blah, and then anything that requires an approval, that's when you click yes, or not even click, just say to the agent yes, and it goes away and does the work."*

**Note the second half of that sentence.** *"Not even click, just say to the agent yes"* moves approval from a UI control to a conversational turn, which is a smaller and more natural interaction than the approval card. It has not been recorded as a decision anywhere else.

### Strip everything, then add back deliberately

The method matters more than the change, because it inverts the default:

> *"For the time being, if we strip most of them out and then work backwards so that we go 'right, this is a sensitive action where we're going to need the approval'. And then based on different user access roles as well."*

> *"The good thing is, it's already built. It's just a matter of going 'right, this tool for this user, this needs to be used'. So it's like we always said, we've got it there. It's just a matter of turning it on and turning it off for different aspects."*

**This is [[open-questions]] #83 already in motion.** That row asked for a classification pass over every user journey to sort quick actions from work-with-me sessions. The pass is happening as part of the SOP rewrite, with a stated method: default to no approval, then reinstate on sensitivity and on user role.

**What is not yet decided is the list itself.** Nobody has said which actions count as sensitive, and Michael's 13 August direction on approval grouping (cardholder plus card together, PIN separate, sensitive payments separate) is the nearest thing to a ruling. It predates this inversion and should be checked against it.

### This week's commitment

> *"For us until we [speak] next week, it's going to be: let's get those SOPs rewritten. Let's make sure that this agent inbox is wired up properly with the real agents on the production deployment, because it's all good me showing you and saying 'oh, it works on my machine'. But obviously you guys need to be able to test."*

Two named deliverables across the retreat travel week, and the second is explicitly about making it testable by TXN rather than demonstrable by Novosapien.

## The true agent inbox

The shape that answers [[open-questions]] #84, proposed by George and improved by Dorte in the same exchange.

### George's proposal

> *"One of the things we might need to think of is those things that Ian was saying about 'I just want to fire it away and forget about it, and it just does it'. How do we notify the user that that's been done?"*

His answer is to split the inbox in two:

| Surface | Purpose |
|---------|---------|
| **Alerts inbox** | What exists today: an alert arrives, agents investigate, a plan is proposed |
| **True agent inbox** | Work the user asked for. *"I've done this piece of work for you, this is what I've done"*, or *"I need this help here"* |

The framing is the useful part, and it is a positioning statement as much as a design one:

> *"Rather than everything being like what everyone else is doing, where it's 'here's this chat interface and this is the only way you can interface with the agents', is having that kind of **true digital worker experience** where it's 'I've done this work for you, I need this help here'. So it's just a bit easier to see rather than having to click into a chat and read it."*

That is the direct answer to Ian's objection: the alternative to narrating every step is not silence, it is **reporting on completion**.

### Dorte's addition, and her guard on it

> *"Would it make sense to have kind of a popup if I'm in the console already, and then it just flashes saying like 'I'm done, I need help' kind of thing? And then there's a link and it directs me to the more detailed information."*

George extended it to **system notifications and agent notifications as separate streams**, with an unread count on the inbox.

**Then Dorte immediately constrained her own idea**, which is the part worth keeping:

> *"The only thing we just need to be mindful of is that we're not over complicating it, because it might be a number of different things coming in. It's like you lose the plot where you actually are. What is really important?"*

**So the requirement is not "notify me", it is "tell me what matters."** Two notification streams plus unread counts plus popups is exactly the over-complication she is warning against, and she raised the warning against a design she had just proposed.

Read alongside her 3 September rule, *"I get really impatient if nothing explains why I'm waiting"*, her position is consistent: **explain a block, report a completion, and do not narrate anything else.**

### The engineering position

George's assessment of cost, which sets the sequencing:

> *"We focus on the inbox, we'll get the backends all really good and solidified there. The front end stuff is a bit easier. All it needs to do is emit a message when it's done. It's just a matter of where we're going to put it. If it's in the chat, it's just sending the chat message back. In the agent inbox, same thing as putting it back to the inbox. So if we needed to mould some of them together, it's very doable."*

**The emit is one event; the routing is a placement decision.** That means #84 does not need resolving before the backend work proceeds, which is a genuine de-risking of that row.

## Dorte asked for benchmarks, and she is right to

The strongest thing she said, and it should be treated as a deliverable rather than a nicety.

> *"When you rewrite it, what would be interesting to see is how much you can cut it short. You said you changed the model: what difference from the speed does it already make with that? And then the next step, when you take some approvals out of the flow, what speed increase is that? That we can see that actually **in figures rather than manually trying to test it and then say 'oh it feels now right' but it has no figure attached to it**."*

George agreed and proposed the method: *"let's run the same workflow 100 times, see what the timing is for one model compared to another model."*

**Why this matters beyond the number.** Ian's rejection on 3 September was a judgement about feel, and the fix is being measured by feel too. Two changes have landed, the model and the approvals, and without separating them nobody will know which one mattered. Dorte is asking for exactly that separation. Raised at [[open-questions]] #87.

## Reasoning depth as a dial, and Dorte's challenge to it

The one genuine engineering idea in the session.

George explained where the latency actually goes:

> *"With the models, they will reason, where effectively they just print out some text before they actually start doing what they're going to do, and that's usually where a lot of the time [is] spent. So imagine if you needed to execute three tools: it would reason, execute the tool, get the response, reason, execute the tool."*

**Dorte's pushback was immediate and correct:** *"But if you cut down the reasoning, will it lose some of the quality? Because that's the challenge again, to get that balance right."*

**George's answer is the design**, and it is better than a flat setting:

> *"At the start, when it's doing that investigative work or setting out the plan, maybe it's got higher levels of reasoning so that the agent's thinking a bit more, really nailing down what it needs to do. And then as soon as it's got the plan, we just change [it] on the back... From the user's perspective they're not going to notice any of this. But when it comes to the actual execution, it's just 'right, go', and it's a lot quicker."*

So: **think hard while planning, run fast while executing**, switched on a flag once the plan exists. It also gives a per-workflow tuning lever, since testing can show which workflows degrade at which reasoning level.

**This is a second model change on top of the Gemini switch**, and it compounds the problem in [[open-questions]] #85 and #70: the list of models and settings Novosapien owes Direct Transact keeps growing before it has been sent.

## Testing: late, and both sides know it

Dorte opened the call with it and did not soften it.

> *"I tried to do some UAT testing. I just keep running out of time."*

> *"I'm conscious we are both a bit late on that one already."*

> *"It's Mike, he's coming back. I'm scared."*

George's reply is generous and also lets the slip stand: *"we're firing and stuff anyway, so it's not too much of an issue."*

### The URL confusion cost her time

She had been testing in the wrong environment:

> *"Did you send different URLs? Because I was reading through Mike's test script that I'm a client agent with restricted access, but it doesn't seem to be right where I am."*

George's correction: **the production console is the one to use**, not the testing console, because testing is where Novosapien pushes work in progress. He acknowledged the inversion himself: *"I know it seems a bit backwards, but obviously at the moment it's just for our internal use."*

She had done her earlier work in UAT as a result. She also hit a second small confusion, expecting the console to open in a new tab when it opens inline.

**Two small things cost a client several days of testing on a build whose acceptance is contested** ([[open-questions]] #54). Neither is a defect; both are onboarding gaps.

### How Michael split the testing

> *"The way he has split it is giving me a task of workflows to do, and Ian [another], so that we both come from a different angle. And I actually need to catch up when Ian is back to see how far he got."*

So Michael wrote a **test script with workflows divided between Dorte and Ian by angle**, before he left. That is more structure than the vault has recorded, and it means the UAT split agreed on 27 August has an artefact behind it.

Dorte's feedback so far is **unstructured**: *"I already put some feedback on there, but they were more random ones as I was clicking around rather than following the workflows through."*

## The content workforce interview went off script

The most important finding outside the agentic build, because five more of these sessions are planned.

> *"It felt for me like I'm doing the TXN manifesto again. The wording was wrong. So I was always referring back to my and Ian['s] and I was like 'hold a minute, this is about me, it's nothing to do with the company'."*

> *"Somewhere it went off script without knowing why it went off script. So it wasn't really down to me as the person, the role I'm having in the organization and what we actually want to cover."*

She tried to diagnose it herself and could not: *"I always run it back against what we had said before because I wanted to make sure I'm in line with what we said, but I couldn't work it out."*

George's hypothesis: *"maybe there might have been some cross context pollution or something."* Novosapien will investigate.

**Two further data points from the same session**, and they are consistent with drift rather than with a slow interview:

- **It took four times as long as she expected.** *"I didn't know where I was and how long it would take, because I thought I'm in half an hour, but it took me two hours then in total."*
- **She could not tell how far through she was**, which is the same complaint she has made about the agent waiting without explanation.

**This is [[open-questions]] #82 with a second, harder failure mode.** #82 says the elicitation may be mood-dependent. This says the elicitation may not stay on its subject. The first is a stability problem, the second is a correctness one, and only the second would make an entity write in the wrong voice entirely. Raised at [[open-questions]] #86.

**She has also asked for status and break reminders in the interview**, which Max has and which George has scheduled for next week.

## Dorte gets her own content pillar, and the reason is a finding

Max is building an **additional pillar for Dorte as an individual** rather than as a TXN employee.

Her reason:

> *"My posts, I'm posting as a person rather than as an employee, get far more feedback and engagement than when they're company posts."*

**That is a client observation about LinkedIn distribution, not a preference**, and it points the same way as the 3 September ruling that the team's own networks are the most likely source of the first client ([[outbound]]). It is worth carrying into [[content-pillars]] as a general principle rather than as an exception for Dorte.

Max will teach **Tyler** to do the pillar work: *"it will be Tyler, but Tyler doesn't know how to do it yet. So it'll be me teaching Tyler."*

## The agent database question returns, and is deferred again

George raised it unprompted:

> *"The agents are going to need a database that they can [use], that all of their stuff's going to go into. So it's just a matter of, I suppose, speaking to Mike to work out: are we going to have a separate one just for the agents, or is it linked into there?"*

**Neither party could remember the hosting decision.** Dorte: *"with the databases that we decided where they would be sitting, who's hosting them?"* George: *"off the top of my head I can't remember."* Dorte: *"me neither."*

She will take it to Michael next week, and flagged it may need to go to Direct Transact.

**This is [[open-questions]] #69, unchanged since 25 August and now deferred past the retreat.** That row records George raising the same question on 25 August, Michael tying it to the data lake and GDPR, and Michael undertaking to add it to the deployment document for DT. **Nobody has the answer and nobody remembers what was decided**, which is a sign the 25 August discussion did not produce a decision at all. It is not blocking today; it bites at production hosting.

## The live demo did not work

George demonstrated the agent inbox with real agents against the mocked API, and it hung on both machines.

> George: *"this has taken a while. I think it's just not set up properly."*
> Dorte: *"mine is still loading."*
> George: *"mine's still going as well. I don't know why that is."*

**Recorded without alarm**, because it is a local wiring problem on an in-progress build rather than a regression, and it is exactly why the production wire-up is this week's second deliverable. But it is the second consecutive standup where a live demonstration failed in front of the client, after the Anthropic outage on 3 September.

George also confirmed the tool-call trace is now correctly positioned: *"this is something that usually a user is never really going to see, unless an alert occurs and they click onto it."*

## Findings and where they landed

### The agentic build

| Finding | Destination | Action |
|---------|-------------|--------|
| **Model switched to a faster Gemini model** for latency | [[agent-orchestration]], [[open-questions]] | Recorded; added to **#85** |
| **Approvals stripped out wholesale**, to be reinstated on sensitivity and user role | [[agent-orchestration]], [[approval-queue-integration]] | Recorded; **#83** moves to in progress |
| **SOPs being rewritten** so investigation is frontloaded and approval sits once at the end | [[agent-orchestration]] | Recorded as this week's commitment |
| Approval may become a **conversational turn** rather than a card: *"not even click, just say to the agent yes"* | [[approval-queue-integration]] | Recorded, not previously stated |
| **Reasoning depth switches mid-task**: high while planning, low while executing | [[agent-orchestration]], [[architecture]] | Recorded; second model change, added to **#85** |
| **The true agent inbox**: alerts and completed work as separate surfaces | [[agent-inbox-alerts]], [[notification-routing]] | **#84** answered in shape |
| Dorte's popup, plus her own warning against over-complicating it | [[notification-routing]] | Recorded as the constraint on the design |
| Emit once, route later: the notification is one event, its placement a separate decision | [[notification-routing]] | Recorded; de-risks **#84** |
| **Benchmarks asked for, in figures not feel** | [[open-questions]] | New row **#87** |
| Live demo hung on both machines; production wire-up is this week's second deliverable | [[agent-inbox-alerts]] | Recorded |

### Testing and delivery

| Finding | Destination | Action |
|---------|-------------|--------|
| Dorte testing in the wrong environment; **production console is correct**, not testing | [[delivery]], [[open-questions]] | Added to **#51** |
| **Michael left a test script splitting workflows between Dorte and Ian by angle** | [[delivery]] | Recorded; more structure than the vault held |
| Both TXN testers are behind, and know it | [[open-questions]] | Added to **#51** |
| **Agent database still undecided, and nobody remembers the earlier discussion** | [[open-questions]] | **#69** updated, deferred past the retreat |
| No standup this week; resumes **Tuesday 15 September**, morning slot for TXN | [[delivery]] | Recorded |

### Content Workforce

| Finding | Destination | Action |
|---------|-------------|--------|
| **Dorte's personal interview drifted onto company material** | [[content-workforce]], [[open-questions]] | New row **#86** |
| It took **two hours against an expected thirty minutes**, with no sense of progress | [[content-workforce]] | Recorded; status and break reminders scheduled |
| **Dorte gets a personal pillar**, because personal posts outperform company posts | [[content-pillars]], [[content-workforce]] | Recorded as a distribution finding, not a preference |
| Max is teaching Tyler the pillar work | [[content-workforce]] | Recorded |

### Context, no action

| Finding | Note |
|---------|------|
| **Hasan Ahmed** attended, first appearance in a standup on this record | No contribution to the substantive discussion |
| Dorte on why she is behind | *"He's working 24/7 to get all of the stuff done. And it's not that we are not working 24/7, it's just we have all the other stuff and it just forces me in the cracks"* |

## Open actions from the call

| Action | Owner | Note |
|--------|-------|------|
| Rewrite the SOPs with approvals frontloaded | Novosapien | This week, during travel |
| Wire the agent inbox to real agents on the **production** deployment | Novosapien | So TXN can test it rather than watch it |
| Benchmark the workflows, per model and per approval change | Novosapien | Dorte's ask. 100 runs per configuration |
| Decide which actions are sensitive enough to keep an approval | Both | Check Michael's 13 August grouping against the new inversion |
| Investigate why the personal interview drifted onto company material | Novosapien | Five more sessions depend on it |
| Add status and break reminders to the interview | Novosapien | Scheduled for next week |
| Settle the agent database with Michael, and possibly DT | Dorte | Next week, on his return |
| Catch up with Ian on his testing progress | Dorte | On his return |

---

## Transcript

Sep 8, 2026

## **TXN \- Agentic AI SU \- Transcript**

### **00:00:01**

**Hasan Ahmed:** So, yeah,

**George Westbrook:** and oh

**Hasan Ahmed:** I'll probably give me a sec. I don't have my connected storage

**George Westbrook:** right

**Hasan Ahmed:** like that much.

**George Westbrook:** at

**Dorte Dye:** Someone got a haircut.

**George Westbrook:** I did quite quite quite a dramatic one. I think the whole the whole of yesterday I think all the calls that we had um half of the

**Dorte Dye:** Everyone commented on it.

**George Westbrook:** time half of the time was spent taking the piss out of me and my hand

**Dorte Dye:** Why taking the face? They're just jealous.

**Max Kingaby:** I'm going to take the pistol

**Dorte Dye:** You have to cut.

**George Westbrook:** jeel jealousy. I think it is it was mainly coming from Max strangely enough. But now looking at the video, I can kind of see why

**Dorte Dye:** I think he's fearing competition.

**George Westbrook:** I Yeah,

**Dorte Dye:** And Hassan is really quiet.

**George Westbrook:** I don't

**Dorte Dye:** He's not cutting his hair.

**Max Kingaby:** I'm I'm just I'm just worried because now there's a threat for barley.

### **00:01:13**

**Max Kingaby:** George's trim is so fresh.

**Hasan Ahmed:** Yeah, that's what happened.

**Dorte Dye:** I mean holiday. What do you expect?

**George Westbrook:** It's cuz it's going to be hotter, so it needs to be more more streamlined.

**Dorte Dye:** You could go to Siberia. Don't have to go to Bali.

**George Westbrook:** We could change it. We could change it. I did, to be fair, I did actually get worried at the weekend because it I think like Cracker Tower, the the mountain in um Indonesia, they were like,"Oh, it's it's starting to erupt." And I was like,"I swear there was quite a bad eruption there like hundred years ago." Um but fortunately for us fortunately for us the group that we're going on we'll we'll be fine. Touch wood.

**Dorte Dye:** Yes. When we go in before we start, quick question. I tried to do I tried to do some UAT testing. I just I keep running out of time.

**George Westbrook:** Yeah this

**Dorte Dye:** Did you send diff different URLs? Because I was reading through Mike's test script that I'm a client agent with restricted access, but it doesn't seems to be right where I am on.

### **00:02:21**

**Dorte Dye:** I'll show you.

**George Westbrook:** I I don't think you should have any restricted access to be honest. I think it's for for me the best best way to access it is if you go to the admin panel and then in the admin panel there is a like open console button then it will open it

**Dorte Dye:** I don't just

**George Westbrook:** in line. If you just go to if you just open it in a new tab it should take you to it. I think literally No,

**Dorte Dye:** the the the testing console because that's the only one that works anyway.

**George Westbrook:** no, no. The I think the the main production one is is probably the best at the moment. Um because what we might do periodically is push things to testing. We I know it seems a seems a bit backwards, but obviously because at the moment it's just for for our internal use.

**Dorte Dye:** No, no, it's it's it's all good. I just want to make sure I'm using the right one. So, I'm in on the dashboard and then I have testing console and console.

### **00:03:11**

**Dorte Dye:** And if I Oh, no. It works. Must have been me. I tried the console and it didn't work.

**George Westbrook:** Oh,

**Dorte Dye:** So,

**George Westbrook:** okay.

**Dorte Dye:** that's why I did everything in UAT. So, I'm doing the production one rather than the UAT one.

**George Westbrook:** Yeah. Yeah.

**Dorte Dye:** Okay. So,

**George Westbrook:** Um yeah,

**Dorte Dye:** it's checking my access. Okay, now I'm back in.

**George Westbrook:** that takes perfect.

**Dorte Dye:** That's fine. Okay, so then I just need to work through what Mike has given me the instruction fiddling around there.

**George Westbrook:** Yeah.

**Dorte Dye:** Okay, fine.

**George Westbrook:** And any issues with that, just just let us know and we'll we'll get on to it straight away.

**Dorte Dye:** That's fine.

**George Westbrook:** Um

**Dorte Dye:** I mean, I already put some feedbacks on there, but there were more random ones as I was clicking around rather than following the workflows through.

**George Westbrook:** yeah.

**Dorte Dye:** I think the way how he has split it is giving me a task of workflows to do and Ian so that we both come from a different angle and I actually need to catch up when Ian is back to see how far he

### **00:04:00**

**George Westbrook:** Yeah.

**Dorte Dye:** got because I'm conscious we are both a bit late on that one already. Okay,

**George Westbrook:** It's it's like we're we're firing and stuff anyway,

**Dorte Dye:** I'll see you.

**George Westbrook:** so it's it's not too much of an issue.

**Dorte Dye:** But it's Mike. He's coming back. I'm scared.

**George Westbrook:** Oh, well, you're gonna get you're gonna get Mike go. Dorte, have you not done this?

**Dorte Dye:** Yeah,

**George Westbrook:** Have you not done that?

**Dorte Dye:** he he's he's working 24/7, right, to get all of the s\*\*\* done. And it's not that we are not working 24/7, it's just we have all the other stuff and it just like force me in the cracks. But that's fine.

**George Westbrook:** Yeah,

**Dorte Dye:** I'm getting on to it.

**George Westbrook:** perfect.

**Dorte Dye:** Okay.

**George Westbrook:** So, I suppose what what has been done since since last last time we spoke? So main things was getting the actual I think it was in progress last time is the actual agent inbox running with live agent.

### **00:04:49**

**George Westbrook:** Um there are live agents. So it's all it's all of testing.

**Dorte Dye:** Okay,

**George Westbrook:** Let me pull up my screen. Um if

**Dorte Dye:** I just email that office and clean it. So, by the way, when I go onto the console, it just opens in the same window with within the dashboard. It doesn't gives me a new tab. Is that meant to be?

**George Westbrook:** If if you click on so open console and then in the top right hand

**Dorte Dye:** But can you see the shower situation?

**George Westbrook:** corner if you click open

**Dorte Dye:** I don't know what you mean.

**George Westbrook:** let me have a look that's uh yeah yeah yeah if that's all Okay.

**Dorte Dye:** So let me just Nope. Nope. Okay.

**George Westbrook:** Um,

**Dorte Dye:** Or access to uh Yeah.

**George Westbrook:** if you click open the console and in the top right hand corner

**Dorte Dye:** So not here.

**George Westbrook:** Huh?

**Dorte Dye:** Ah,

**George Westbrook:** Yeah, it's been

**Dorte Dye:** I'm pretty sure I did had to do that the last time as I went into UAT.

### **00:06:06**

**Dorte Dye:** I thought it open directly. Okay, that's cool.

**George Westbrook:** perfect. Wait. And then if I share this. So, this is on the way. I'll share this um as well. feels act exactly the exact the same now it's

**Dorte Dye:** I'm just very

**George Westbrook:** got agents underneath it. So this one is actually investigating. So the way to test it, we might need we in the production one um

**Dorte Dye:** catch up on

**George Westbrook:** is just go here, click raise test alert and then it is oh doing

**Dorte Dye:** the mind.

**George Westbrook:** that one.

**Dorte Dye:** How do I open the inbox for my settings?

**George Westbrook:** Um on the left hand side down here it it should say

**Dorte Dye:** Yeah.

**George Westbrook:** inbox.

**Dorte Dye:** Oh gosh, I can't read. Yeah, right on agents. Yeah, sorry about that. Okay.

**George Westbrook:** and then click raise test alert and then it's going to raise this test alert. Then what's going to what it's going to show is the the agent starting to investigate um behind the scenes blah blah blah do that.

### **00:07:26**

**George Westbrook:** This might I can't remember if this is

**Dorte Dye:** Yeah,

**George Westbrook:** I

**Dorte Dye:** mine look this. It looks the same. It keeps running. I can't do anything yet.

**George Westbrook:** so it's Oh, there we go. It's updating. Um, so this is just the agents behind the scene calling the tools inating. Um, this is something that usually a user is never really going to see. Um, unless at which an alert occurs, they click onto it. But what what the process will be in in the real world is as soon as that alert then the agent just going to start investigating.

**Dorte Dye:** How are you?

**George Westbrook:** Once that once that plan is there, it's then up to the user to go right hit approve and it's going to go away and make that.

**Dorte Dye:** more days. You think you need to pay You're

**George Westbrook:** Wait, I'm just going to mute you for a second, Dorte, because there there's a fair bit of background noise. Apologies. Um, so yeah, this has taken this has taken a while.

### **00:08:42**

**George Westbrook:** I think it's just not set up properly. Um, the ne and then so the other things that we've changed based on the conversation we had with you and Ian last week was the speed. So we're looking in evaluating a few different models. Um, the one we were using was was good. It just wasn't quick. Um so it's we've switched the model now to um another Gemini model which is which is a lot quicker. Um so should see some speed improvements on that. Um but the thing we we've also been working on is getting rid of a lot of those approvals. Um so I think at the moment what we've done is turned off a lot of the approvals. Um, but what we're going to need to do is kind of rewrite all of the SOPs because what what it was doing before is it's not it sounds like a way bigger job than than it is. Um, but whereas before it might do right here's my plan and in the plan there's going to be some investigation work and then after the investigation work then you approve what I need to do.

### **00:09:47**

**George Westbrook:** Ideally what we want is everything's frontloaded. So the investigation blah blah blah and then anything that requires an approval that's when you click yes or not even click just say to the agent yes and it goes away and does the work. So there might be a few new mechanisms that we need to add in so that if it needs help um maybe it's just a different color in this sidebar here where it's like say um working there's a like a spinning icon. If it needs help, it's going to be yellow. If there's an error, it's going to be red. So, things like that. And it should just make it a lot easier. Um, but cutting down the approvals for things that that are not really going to be needing to be approved. But I think for the time being, if we we strip most of them out and then work backwards so that we go right, this is a sensitive action where we're going to need the approval. Um, and then based on different user access roles as well.

### **00:10:45**

**George Westbrook:** But the good thing is is it's already built. It's just a matter of going right this tool for this user. This needs to be this needs to be used. So it's like we always said, we've we've got it there. It's just a matter of turning it on and turning it off for for for different aspects. Um so I think for for us for the next well until we next week, it's going to be let's get those SOPs rewritten. Let's make sure that this agent inbox um this agent inbox is wired up properly with the real agents on the production deployment because it's all good me showing you and saying,"Oh, it works on my machine." Um but obviously you guys need to be able to test.

**Dorte Dye:** Mine is still loading.

**George Westbrook:** Yeah, mine's mine's still going as well. I don't know why that is. Um,

**Dorte Dye:** I think when you rewrite it, what would be interesting to see how much you can cut it short? You know, you said you changed the model.

### **00:11:39**

**Dorte Dye:** what what difference from the speed it already makes with that. And then the next step when you take the some approval approvals out of the flow again what speed increase is that that we can see that actually in figures rather than manually trying to test

**George Westbrook:** yeah.

**Dorte Dye:** it and then say oh it feels now right but it has no figure attached to

**George Westbrook:** Yeah. Yeah. So, I think what we can do that on our side as well is just let's run the same workflow 100 times, see what the see what the timing is for one model compared to another model. Um, one thing that we can play with as well is the the reasoning. So with the with the models, they will reason where effectively they just print out some text before they actually start doing what they're going to do. Um, and that's usually where a lot of the time spent. Um like so imagine if you needed to execute three tools it would reason execute the tool get the response reason execute the tool.

### **00:12:36**

**George Westbrook:** So it's just so if we cut down the reasoning um that should that should help it a fair bit. Um

**Dorte Dye:** But if you cut down the reasoning, will it lose some of the quality? Because that's the challenge again to get that balance right.

**George Westbrook:** yeah, so it's it it there's different there's different things we can do. Usually the models are once they've got a plan they're they're they're kind of good to go. But we could do in testing we can see okay this workflow it's it's failing a little bit more and when the reasoning is set to this this level um what we can probably do is set a flag for the agent. Um so that after it's done the plan or the investigation we flip it to a model with a different setting. So at the start when it's doing that investigative work or setting out the plan maybe it's got higher higher levels of reasoning so that the agent's thinking a bit more really nailing down what it needs to do and then as soon as it's got the plan we just change on the back.

### **00:13:35**

**George Westbrook:** So from the users perspective they're not going to notice any of this. Um but when it comes to the actual execution it's just right go and it's a lot quicker. Um, but I think one of the things we might need to think of is those things that Ian was saying about like I just want to fire it away and forget about it. Um, and it just does it is how do we notify the user that that's been done? So maybe this agent inbox um

**Dorte Dye:** Let's change your army. So the

**George Westbrook:** it's another agent inbox but I think having maybe an alerts part which is what this current agent inbox is but then also a call it a true agent inbox where it's like I've done this piece of work for you um this is what I've done or if it needs approval rather than everything being like a what everyone else is doing where it's here's this chat interface and this is the only way you can interface with the agents is having that kind of true digital worker experience where it's kind of like I've done this work for you.

### **00:14:38**

**George Westbrook:** Um, I need this help here, blah blah blah. So, it's just a bit easier to see rather than having to click into a chat and read it.

**Dorte Dye:** Oh, would it make sense to have kind of a popup if I'm in the console already and then it just flashes saying like I'm done. I need help kind of thing.

**George Westbrook:** Yeah.

**Dorte Dye:** And then there's a link and it directs me to the more detailed information.

**George Westbrook:** Yeah, we could we could have something like literally like what's here is maybe uh these could be like system

**Dorte Dye:** It's excellent.

**George Westbrook:** notifications and then maybe here we could have like agent notifications as well as maybe this inbox having like numbers for the amount of outstanding messages.

**Dorte Dye:** I think the only thing we just need to be mindful of that we're not over complicating it because it might be now

**George Westbrook:** Yeah.

**Dorte Dye:** a number of different things they're coming in. It's like you lose the plot where you actually are. What is really important?

**George Westbrook:** Yeah. Yeah.

### **00:15:29**

**George Westbrook:** I I I think what we what we can do is we focus on like the we'll keep the agent, keep the inbox, we'll get that we'll get the backends all like really good and solidified there. Um and the front the front end stuff is a is a bit easier. Um it's all it needs to do is emit a message emit a message when it's done. It's just a matter of where we're going to put it. If it's in the chat, it's just sending the chat message back in the agent inbox. Same thing as putting it back to the inbox. So, if we needed to kind of mold some of them together, um it's very very doable.

**Dorte Dye:** Okay, sounds

**George Westbrook:** Um so, I think in terms of the agent, the agent stuff still ticking away on on that. One I think one thing that needs to I think probably Mike when he gets back is in terms of databases is what we I think we mentioned it before is obviously the agents are going to need a database that they can that all of their all of their stuff's going to go into.

### **00:16:32**

**George Westbrook:** So, it's just a matter of I suppose speaking to Mike to work out are we going to have a separate one um a separate one just for the agents or because obviously it's per stuff or is it linked into there?

**Dorte Dye:** with the databases that we decided where they would be sitting, who's hosting them?

**George Westbrook:** Um, off the top of my head I can't remember.

**Dorte Dye:** No,

**George Westbrook:** Um

**Dorte Dye:** me neither. It's just a question if if we need to discuss it as DT or something. It's fine. I will pick it up as Mike next week. We are not having another meeting this week because you're flying,

**George Westbrook:** yeah.

**Dorte Dye:** but then we are back on Tuesday in the morning sessions, right? We moved it to Yeah.

**George Westbrook:** Yeah.

**Dorte Dye:** Okay.

**George Westbrook:** Yeah. I think it Yeah. Well, it be I think for us it will be similarish time. Um, but obviously for for you guys it's going to be going to be in the morning because of the time difference which I think we were going to be a bit jetlagged over the weekend I can imagine.

### **00:17:31**

**Dorte Dye:** I'm sure Brett makes you work anyway. Work and party.

**George Westbrook:** Um,

**Dorte Dye:** Okay.

**George Westbrook:** yeah. So I suppose that's everything on this. I think on the the content workforce and the outbound side um that's as far as I know is all all going according to plan. And I think Max mentioned you had some feedback on the the content workforce

**Dorte Dye:** Mhm.

**George Westbrook:** um like that status status update and the um like the break reminders. Um so I think we'll that there that's stuff that we'll probably get on to next next week realistically.

**Dorte Dye:** Mhm.

**George Westbrook:** Um but yeah, any other issues on that just just let us know.

**Dorte Dye:** I think there were the main things because I didn't know where I was and how long it would take because I thought I'm in half an hour but it took me two hours then in total but then I did everything.

**George Westbrook:** Yeah. Yeah.

**Dorte Dye:** So the other thing that was a bit confusing and I mentioned it to Max already.

### **00:18:28**

**Dorte Dye:** It felt for me like I'm doing the TXN manifesto again the wording was wrong. So I was always referring back to my and Ian and I was like hold a minute this is about me. It's nothing to do with the company.

**George Westbrook:** Yeah.

**Dorte Dye:** So somewhere the sh went off script without knowing why it went off script. So it wasn't really down to me as the person, the role I'm having in the organization and what we actually want to cover.

**George Westbrook:** Okay. Yeah, we have we'll have to have a look into that to see see why that happened. Um, but that's No, that's really that's really good to know. Maybe maybe there might have been some cross context um pollution or something, but

**Dorte Dye:** It it's just really interesting because I always run it back against what we had said before because I wanted to make sure I'm in line with what we said, but I couldn't work it out.

**George Westbrook:** yeah.

**Dorte Dye:** And and the other thing Max and I discussed this morning is about the the pillars.

### **00:19:23**

**Dorte Dye:** So Max is creating an extra pillar for me as a individual rather than as a TXM employee because I think

**George Westbrook:** Yeah.

**Dorte Dye:** that's really important for the contact force as well because my post I'm posting as a person rather than as an employee get far more feedback and engagement than when they're company post.

**George Westbrook:** Yeah. Yeah.

**Max Kingaby:** I've come I've come back to you um on the email you send or just when

**Dorte Dye:** Okay.

**Max Kingaby:** whatever time works for you today can do bl today tomorrow or yeah we can sort

**Dorte Dye:** off. Is it with you or you or Tyler

**Max Kingaby:** that um it it will be Tyler but Tyler doesn't know how to do it yet. So, it'll be me teaching Tyler for T for Tyler to the

**Dorte Dye:** combined? That's fine.

**Max Kingaby:** future.

**Dorte Dye:** And just let's let's keep this slot in what we had initially planned for tomorrow to just tidy up one up. Yep.

**Max Kingaby:** Awesome.

**Dorte Dye:** Cool. Sounds great.

**George Westbrook:** Okay, perfect. I think I think that's I think that's everything. Um, yeah. So, I suppose next next time we speak, we'll all be in uh in sunny Barley.

**Dorte Dye:** swimsuit.

**George Westbrook:** Yeah,

**Dorte Dye:** Brilliant. Okay, then safe flights and then speak to you next week.

**George Westbrook:** perfect. Have a have a good rest.

**Dorte Dye:** Take care.

**George Westbrook:** Speak to you next week.

**Max Kingaby:** Wait, wait.

**Dorte Dye:** Bye.

**Max Kingaby:** I've just looked. We don't We don't have a time tomorrow.

**George Westbrook:** Wait, wait, wait. Then we stop taking nipes.

### **Transcription ended after 00:20:50**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*