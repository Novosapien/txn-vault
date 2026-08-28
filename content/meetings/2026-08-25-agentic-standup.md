---
date: 2026-08-25
type: standup
description: "Transcript and analysis of the 2026-08-25 TXN standup: Michael away 3 to 15 September, DT has no alerting system, and nine of thirteen workflows tested"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-inbox-alerts]]"
  - "[[architecture]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[agent-inbox-alerts]]"
  - "[[alert-detection]]"
  - "[[architecture]]"
  - "[[integrations]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-08-25)

> **Source:** Gemini transcript, synced from the shared folder. Attendees: Brett StClair, George Westbrook, Max Kingaby, Dorte Dye, Michael Moores. Duration 00:30:43.
>
> **Filed 28 August, three days late.** This standup sat in the inbox while the 26 and 27 August sessions were processed ahead of it, so the vault carried a gap between the 21st and the 26th. That matters here more than usual: the acceptance-window answer the register has been chasing since 13 August was given on this call, and the spec-URL fault recorded as a 27 August finding actually surfaced on this one.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| **Michael is away 3 to 15 September, and the acceptance window as planned does not work.** Dorte opened with it, having checked the flight plan with Ian and Michael: *"your window to sign off to UAT actually doesn't work for us because Mike is off on holidays from the 3rd already and he's coming back on the 15th."* She proposed sign-off after his return with buffer afterwards. Brett offered to run it earlier; Dorte: *"I don't think Mike will be ready."* **Michael settled it himself**: he is in *"full UAT for knowledge hub and the API right now... that has to be done before I go unfortunately."* So he cannot take the pilot UAT before he leaves, and when he returns the Novosapien team is in Bali. **The pilot completes 7 September and acceptance cannot sit between the 7th and the 10th** | [[delivery]], [[open-questions]] #50, #54 | **Register rows rewritten.** #50 given exact dates and Michael's own answer; #54 reframed from a three-day squeeze to a collision |
| **Direct Transact has no alerting system, and Michael wants the AI to be the central one.** In full: *"DT don't have an alerting system per se... the endpoint we had DT was sort of just a post get type situation. There was no clever technology behind it. It was just a system would push that up and they were basically the system of record. So they weren't going to build anything very good basically."* His direction: *"the one thing we do want is sort of central place for alerts... whether we build the AI first and then tack on other things afterwards then obviously that's the source"*, with any blocking system feeding in so an operator gets *"here's the errors, here's the actual thing going on"* | [[agent-inbox-alerts]], [[alert-detection]], [[open-questions]] #68 | **Update banners + new register row.** Materially changes the component's dependency assumptions |
| **Nine of thirteen workflows are built and tested; four are held back deliberately.** George: *"all of the workflows apart from the ones that were kind of net new are all done. Still testing them. Tested most of them at least once or twice."* The four outstanding are **guided product launch, scheduled performance report with drivers, alert to investigation to proposed plan, and create a monitoring alert by conversation**. Three are held because they need a **different interface** rather than the shared conversational one; guided product launch is the exception and *"can be done... either today or tomorrow"* | [[delivery]], [[full-agentic-experience]] | Note added. Maps exactly onto ranks 7 to 10 of [[2026-08-25-workflow-slate-decision]] |
| **Approval stacking resolved, and the 20 August proposal was tried and rejected on evidence.** The agreed approach on 20 August was to render every approval up front in one go. George tested it and found it wrong: the agent *"has to first map out all the tools it's going to use and sometimes there's a bit of a decision tree and then it's going to make a mistake. Then it's going to have to go back"*, which reads as confusing. **The shipped behaviour instead collapses each card once approved** before rendering the next, so history stays visible without consuming the screen | [[approval-queue-integration]], [[generative-ui-rendering]] | Update banner. Records the rejected approach and why |
| **Tool names are leaking to users.** The interface shows raw snake-case tool names and announces the tool it will call: *"I am going to execute the check card tool"* rather than *"I am going to check a card"*. George has it fixed on a parallel worktree. Settles the long-open tool-call visibility question in practice: the answer is plain language for users | [[generative-ui-rendering]], [[open-questions]] #37 | Register row updated |
| **A dev mode is being added.** Michael asked to see the tools being called; George's answer is a **dev mode exposing every tool call**, off in the user version. Michael's preference is to review endpoints in-cell as he tests rather than from a separate document. The testing flag currently visible in the build is dev-only and will not ship | [[generative-ui-rendering]] | Update banner |
| **Michael tests with Playwright, wired to TXN's own vault.** He connects it to the back-end vault to check work against what was discussed, with *"loads of PCI, GDPR, all that stuff, extra sort of rules in there."* His method is manual tool-call verification first, *"make sure the tools that I see are what I expect"*, then Playwright to find paths that call the wrong thing. George offered test hooks so Playwright can target elements directly | [[delivery]] | Note added. The reviewer engagement risk is materially better than the register records |
| **Storage is an open architecture question, newly raised.** George: where do the chats and the alerts get stored, *"is it interacting with the database you've already got or having a specific smaller one just for the chats?"* Michael tied it to the data lake work happening now: pooling client data centrally *"brings in GDPR regulations"*, and if Novosapien stores client data in responses it lands on the same side as client data. **Novosapien will not get production database access**; Michael is writing the deployment document to DT now and will add it as an open question to them | [[architecture]], [[open-questions]] #69 | **New register row** |
| **Hosting confirmed: a TXN subscription inside DT's Azure tenant.** Michael: *"we have confirmed that we will at least for now be going in the DT tenant as one of our own subscriptions."* George asked the consequential question: does Azure hosting force Azure-provided models? Michael has not resolved it, and flagged precedent: DT rejected several third-party frameworks for the console before agreement was reached. His position is **design first**, list what we want and he will take it to DT, *"we don't want to sacrifice the design and the performance and functionality"*, and there are other options if DT will not accept | [[architecture]], [[integrations]], [[open-questions]] #70 | **New register row** |
| **Michael owns standing up the permission model.** *"It's quite a lot of actions on me to get the permission model stood up, which I think that'll be an important crossover point for you and them."* The vault carries the permission model as a Novosapien deliverable in Pilot Order deliverable 2, deferred by decision. **Two sides may be holding different pictures of who owns it** | [[agent-access-layer]], [[open-questions]] #71 | **New register row** |
| **The spec-URL 404 surfaced here, two days before it was recorded.** George hit a 404 pulling the updated YAML on this call. Michael diagnosed it live: credentials had been rotated, then the URL itself had changed, differing by one letter of case in `api`. He was sent it by a project manager rather than the developers and undertook to check what changed. Register #67 dates the discovery to 27 August | [[open-questions]] #67, [[txn-api-reference]] | Register row corrected to 25-08 origin |
| **Decline reasons will exist.** George asked whether the missing decline reason would be added or whether transactions simply carry none. Michael: *"that should be yes"*, with response decline reasons, statuses and layered error payloads. **Gated on ISO-level certification**, so *"a little bit way down the line"*. The original YAML had no statuses at all and that is being pushed through now. This closes the gap behind `investigate-declines`, which deliberately stops short of a cause because no decline reason reaches the agent | [[open-questions]] #72, [[full-agentic-experience]] | **New register row.** Also unblocks slate rank 1 in its full form |
| **TXN-side status: 83 bug fixes awaited, and the knowledge hub goes live first.** Michael is waiting on 83 fixes, with YAML quality the critical one: *"if the YAML's not good, we can't go live with knowledge hub. So knowledge hub is going live first."* Functional issues otherwise minor. External API testing follows | [[delivery]], [[integrations]] | Note added |
| **Deployment to both testing and production.** George deploying the current build to both environments *"so it doesn't matter which one you use"*, then testing. New work promised by Thursday | [[delivery]] | Note added |
| **The next phase is being scoped now.** George intends to start on the agent inbox and the alert surfaces, mocking what DT cannot yet provide: *"if some of the stuff's not ready we'll just mock it... it's going to be a payload. So if it changes, that's fine."* Approach is UI-first clickable prototypes to establish the flow, then wire the AI in | [[agent-inbox-alerts]], [[delivery]] | Note added |
| Stackworkz call confirmed for 26 August to realign and plan the merge of the two builds | [[integrations]] | Context. Covered by [[2026-08-26-stackworkz-agent-demo]] |
| Dorte on her own UAT automation: it failed and she had to redo parts manually, *"it's amazing what you find out when you just check because you can't trust everything"* | n/a | Context, no action |

---

## Transcript

Aug 25, 2026

## **TXN \- Agentic AI SU \- Transcript**

### **00:00:10**

**Dorte Dye:** you again.

**Max Kingaby:** Oh, no time.

**Dorte Dye:** Tell me about it. My brain is still toast.

**Brett StClair:** My brain is toasted because it started with 15 minutes going f\*\*\*.

**Dorte Dye:** George, that was a classic example where AI is going wrong and it went

**Max Kingaby:** No,

**Dorte Dye:** wrong.

**Max Kingaby:** daughter. It was a classic example of not being prepared of the meeting ahead.

**Dorte Dye:** Ooh, isn't that your meeting, not Brett? Is he not just jumping

**Brett StClair:** That's a good point.

**Max Kingaby:** need that

**Brett StClair:** Who's the specialist on work forces,

**George Westbrook:** Hi.

**Dorte Dye:** in?

**Max Kingaby:** one.

**Brett StClair:** Max? Who's not the new specialist on work on outbound

**Max Kingaby:** I got I got two days of stick.

**Brett StClair:** workforces?

**Max Kingaby:** You can have half an hour.

**George Westbrook:** Um,

**Dorte Dye:** Mike's laptop just crashed. So will be a while.

**Brett StClair:** I get where he's coming from.

**Dorte Dye:** Yeah. But for use user error. He's just treating his machine that it's collapsing.

**George Westbrook:** instant

### **00:01:16**

**Dorte Dye:** He has too many jobs running.

**Brett StClair:** My news era was the cloud provider going down in that particular region where I was hosted and then um you don't want

**Dorte Dye:** Which was that Tim booku?

**Brett StClair:** to know it was HNA in Germany.

**Dorte Dye:** Really? I'm pretty sure that's another Russian

**Brett StClair:** I know that's why I was like,

**Dorte Dye:** attack.

**Brett StClair:** "No, that can't be right. What the f\*\*\*\*\* going on here?" I quickly hop on. IP address is not available. I'm like,"Oh s\*\*\*, it is." So,

**Dorte Dye:** Really interesting. Okay.

**Brett StClair:** I was panicking. I was having to pull everything onto my local machine.

**Dorte Dye:** Weird.

**Brett StClair:** So, who waiting for? Like George, did you just let your fathom in there so that you can keep Dörte's fathom

**Dorte Dye:** Yeah.

**George Westbrook:** No, someone someone let it in or it let itself in. It's going

**Brett StClair:** company?

**George Westbrook:** rogue.

**Dorte Dye:** Okay. I think Brett is just so cautious that he doesn't kick me out like he did last time.

### **00:02:24**

**Dorte Dye:** He's just admitting everyone now.

**George Westbrook:** They kick kicked you

**Dorte Dye:** He see Fathom and he thinks it's me.

**Brett StClair:** No.

**George Westbrook:** out.

**Brett StClair:** Fathom. That's where I kicked

**Dorte Dye:** Um the one thing I've um flecked with Ian and Mike from your flight plan,

**Brett StClair:** up.

**Dorte Dye:** your window to sign off to UAT actually doesn't works for us because Mike is off on holidays from the 3rd already and he's coming back on the 15th.

**Brett StClair:** Okay,

**Dorte Dye:** So when when when Mike is on the call.

**Brett StClair:** that's probably legacy 8\.

**Dorte Dye:** We just need to make sure he's comfortable because he's one man and he's just managing everything on DT side.

**Brett StClair:** So, did you say did you say Mike signing off right now on UAT?

**Dorte Dye:** Hello.

**Brett StClair:** That's what I heard.

**Dorte Dye:** Mike is doing

**Brett StClair:** No, no,

**Dorte Dye:** everything.

**Brett StClair:** no. Signing right now.

**Dorte Dye:** Just look at the recording. I said not such thing.

**Brett StClair:** Hello, Mike. Do you have a

### **00:03:24**

**Dorte Dye:** I was just saying Mike that um we need to talk about uh the proposed UT sign off for the pilot because that falls in your holiday. So whatever you're comfortable with if we do that when you're back and then give you some buffer time after because the guys can work in where are you going the Bahamas again? I forgot somewhere where I'm jealous.

**Brett StClair:** close.

**Dorte Dye:** I just said that like that you're probably traveling on two days or something. So that would take a break anyway. And then Mike is back on the 15th.

**Brett StClair:** I mean we can do it before because we are

**Dorte Dye:** No, I don't think Mike will be ready. But Mike, that that's your

**Brett StClair:** Oh yeah,

**Dorte Dye:** call.

**Brett StClair:** you're on mute as

**Dorte Dye:** But we all heard he was shaking his head. There's no charm.

**Michael Moores:** uh no in full UAT for knowledge hub and the API right now. So that's uh has to be done before I go unfortunately.

**Dorte Dye:** skip.

**Brett StClair:** Not a problem.

### **00:04:26**

**Brett StClair:** Not a problem. Um, how's that going, by the

**Michael Moores:** a lot. Uh yeah,

**Brett StClair:** way?

**Michael Moores:** waiting for the 83 bug fixes today. Uh should tie up the YAML and stuff like that. That's the major one because obviously that hinders on the go live for knowledge hub. So if it's not YAML's not good, we can't go live with knowledge hub. So knowledge hub is going live first. So we're sort of prioritizing those YAML fixes now. And then obviously functionally um not too bad little you know small here and there issues and then um once I've got through that obviously the testing of the rest of the external

**Brett StClair:** Perfect. Well done.

**Michael Moores:** API

**Brett StClair:** Sure. That's a lot to be managing. Sure.

**Dorte Dye:** Mhm.

**Brett StClair:** Um I don't envy you going through all that detail either. That's just not good for me. I'm bad

**George Westbrook:** Oh, no. That sounds It sounds really really fun.

**Dorte Dye:** That's the two geeks talking again,

### **00:05:20**

**Brett StClair:** at

**Dorte Dye:** right? I mean, Mike has automated so much. This is like probably how you work as well, Brett. It's like not Brett, George. Brett is doing everything manually with the pen and the paper,

**George Westbrook:** Brett writes his pro prompts on a piece of paper, takes a picture of it, then gets it to write write it out,

**Dorte Dye:** uploaded it.

**George Westbrook:** then copy and pastes it.

**Dorte Dye:** Oh, hilarious.

**Brett StClair:** Both of you.

**Michael Moores:** Oops.

**Brett StClair:** One each.

**George Westbrook:** We're we we put a job posting

**Dorte Dye:** I honestly I'm just laughing because I'm trying to automate, but it's like Mike is light years ahead of me. It's like I did some UAT test and automated and then it failed and I had to do some manually.

**Brett StClair:** Restoring.

**Dorte Dye:** But it's amazing what you find out and when you just check because you can't trust everything. You just need to be really mindful of that. Okay, let's get quickly started on the project. What do you have for us?

### **00:06:15**

**George Westbrook:** So the so basically all of the workflows apart from I think there was it was the ones that were kind of net new things um are all done. Still testing them. Tested most of them at least once or twice.

**Dorte Dye:** Wow.

**George Westbrook:** Um but they're all flowing. It's flowing nicer. I think a lot of your changes, Mike, have have been been integrated. Um the one thing that we're still kind of it's not working on is we've is the approval of the approval cards. Um, I'll show all of this now, but I think the work the workflows it is the um, so I suppose it's easy to say the ones that that haven't been done. Um it is the the guided product launch um scheduled performance report with drivers alert investigate proposed plan and the create a monitoring alert by conversation because the the create a so why some of those haven't haven't been done yet is because they'll require like something something else like say for example the alert investigation proposed plan um that's going to probably be a separate interface where you see the alerts um then you click investigate or it pre-investigates then it's a proposed pan um so I thought let's get all the ones that are same interface same process just different workflows let's get all of them completed um similar one with the scheduled performance reports it's probably better to have a different interface for

### **00:07:53**

**George Westbrook:** that and the guided product launch I to be fair that's that one can be done so we can I think we'll get that one added in either today or tomorrow. Um, but apart from that, all of those on the workflow list are done, tested. Um, a lot of those bug fixes are are gone where there might be an empty card that's rendered. Um, and if there is a card that's empty or loading in, it's going to show that it's loading in rather than before it was just either crashing or showing an empty box and I'm looking at it like, what what is this? Why is it showing that? So I suppose if I share is it this one?

**Brett StClair:** You can

**George Westbrook:** Oh god zoomed in the wrong thing. Can you unsuspend it please? So this one will be about the approvals.

**Brett StClair:** engagement.

**George Westbrook:** So I think before what we had is those like if there was sequential approvals the four say it was four in a row and they would just take up loads of space and my opinion it looks absolutely awful.

### **00:09:09**

**George Westbrook:** Um now it's still going to render it. I'll zoom this in a bit for you Brett.

**Brett StClair:** I said you zooming in the mouse for me as well.

**George Westbrook:** No, I think it automatically does that. Oh, has it restarted it locally? This why you don't make changes just before a call.

**Brett StClair:** You should be better prepared for this.

**Dorte Dye:** I you beat me to it. It's like I had my microphone on me. Brett was really terrible prepared on our meeting with Ian.

**George Westbrook:** remove.

**Dorte Dye:** Ian wasn't happy. Mike and then he was blaming Amazon Germany for not being able to pull his cloud session.

**George Westbrook:** It's those Germans.

**Dorte Dye:** group.

**George Westbrook:** They're not very good at engineering, are

**Dorte Dye:** No,

**George Westbrook:** they?

**Dorte Dye:** not at all. Look at all the British people.

**George Westbrook:** So,

**Brett StClair:** Jes I asked you to zoom it in because

**George Westbrook:** oh, just changed the buttons around on my m mouse, so it's accidentally pasting things when I'm used to my old way of working.

### **00:10:33**

**George Westbrook:** Um, so yeah, same thing. Going to put the task list up here. I think one thing we need to change is instead of it being like snake case where it's like it's just not good for a user. Um, on top of that, some of the other things that we're going to need to change is it's telling you what tool call it's going to execute with the actual tool name. Um, this is the there's two versions going in parallel on different work trees. So, that that is fixed on the other one, this part here. Um, but so what it's going to do now once it's approved, it should collapse it down um before rendering the next one. So it's not taking up loads of the screen. I know before what we did say was ideally it's all rendered in one go. Um the issue with that is is it's try testing it. You have to do a lot of like it what's the word? It's just not the proper way to do it because let's say it executes one tool.

### **00:11:32**

**George Westbrook:** It's got to first map out all the tools it's going to use and sometimes there's a bit of a decision tree and then it's going to make a mistake. Then it's going to have to go back. then it's going to change and from the users's perspective I can imagine it'll be a bit confusing. So at least now it's you're going to see the approval, you can see the full detail, but once you click approve it's going to go down back down nicely. So you can still see what's happened. Um. You can have a look to see what's we can add. We can add more detail or less detail there if needed. Um, but I think it's just overall a much better user experience. Um, in terms of the Oh, let's just get this one through to the end. This flag here, this is this that's not going to be there in the users version. Um, this is just for us for testing. So, cuz it's annoying that it's got everything there, but I think from our perspective, we want to if you want to flag a message, it's just a lot quicker and easier.

### **00:12:30**

**George Westbrook:** Um, and close that down as well. Um, so I think yeah, some of the things we need to change are tool calls, not actually saying the tool name, um, what's on there on the server, just saying what it's going to do. I am going to check a card rather than I'm going to execute the check card tool. So, they're tiny changes. it's not too much of an issue. Um, and then with the we've got this like slash commands slash commands kind of quick actions. Um,

**Dorte Dye:** Cool.

**George Westbrook:** if a user wants to go in and select one um also if they just want to say just want to speak to their machine and say I want to suspend a card, it's going to pick that up as well. um if they would say I want to suspend a card and then review alerts, it's going to understand that and it's going to do it one after another. So it's not as if you've got to explicitly select it. It's very very malleable. Some people like some people like this, other people don't.

### **00:13:32**

**George Westbrook:** So just having that flexibility there I think's think helpful. So I think in terms of the workflows um have a look again into the guided product launch but I think for what we've got at the moment I think it's ready to ready to test um and I think what we can I think so there'll be tiny iterations that we'll pick up get it from the feedback panel iterate iterate iterate um but I think now it's at the point where we can start going and looking at some of these some of these other ones which are not in the pilot but if we're at the point where we need to we need to start working on them, we we might as well. Um, and just building out maybe some new pages for the alerts, mocking it as best as we can. Um, that's one thing I've remembered. Actually, I I I think, you know, you sent me that thing, Mike, with the um in order to get the updated YAML. Um, I think it's return of 404 at the moment.

### **00:14:32**

**Michael Moores:** Let me double check.

**George Westbrook:** I'm not sure.

**Michael Moores:** I know changes the other day. So, was it working

**George Westbrook:** Yeah, I think f first time used it,

**Michael Moores:** before?

**George Westbrook:** it was working. Um,

**Michael Moores:** the last time they had to rotate the credentials. So, let me just double check.

**Brett StClair:** Hey,

**George Westbrook:** yeah, cuz I thought I thought that might be what it was, but I thought what would that be before before Number

**Brett StClair:** water.

**Michael Moores:** Yeah, I I know it's not responding how it should at the moment. So,

**George Westbrook:** three.

**Michael Moores:** let me just double check. Okay, that one works.

**Brett StClair:** Are they are they happy to help you?

**Michael Moores:** Yeah, I've got some qu seem to be working. So, let me just send it across again.

**George Westbrook:** I think we have a

**Michael Moores:** See if there's anything else in

**George Westbrook:** look.

**Michael Moores:** there. It's a structure. Just a second. So you can see if it's changed what everything else subscription key should end F37 if that's the same one still

### **00:16:13**

**George Westbrook:** F37.

**Michael Moores:** Brett This

**George Westbrook:** There we go.

**Michael Moores:** should

**George Westbrook:** Let's have a look.

**Michael Moores:** actually move that now outside of the subscription key. Anyway, I don't think it needs authentication. Now, that one I just sent

**George Westbrook:** I think it that might be a different URL to the one we had.

**Michael Moores:** you

**George Westbrook:** I'm just checking to see if what the URL is.

**Michael Moores:** last sent this morning. Let me see what's in here.

**George Westbrook:** Yeah. So, it says the new URL works fine with or without the

**Michael Moores:** Let me pick it up with them now.

**George Westbrook:** key.

**Michael Moores:** Looks like it has changed. Let me just That one works. Now, let me just speak to them and see what the changes were. Um, obviously that's not going to be the URL we use for real when we get the URLs anyway, but um I'll see why that's changed. It does look different. Uh, I'll get back to

**George Westbrook:** It I'm looking at it.

### **00:17:42**

**Michael Moores:** you.

**George Westbrook:** It looks exactly the same as the It looks exactly the same. Oh, no. There's There's like a tiny uh I think it was API. So there one letter where API in the old one was lowerase and the new one is

**Michael Moores:** Yeah. Well, yeah, this is a project guy that sent me this.

**George Westbrook:** capital.

**Michael Moores:** So, I'll double check with actual devs and see what's going on there because it's it does look different. So, uh but I know they have been making massive changes there and how we deploy and push push out specifically. So, um let me just double check with them and get back to you.

**George Westbrook:** Perfect. Yeah. So, we'll pull what we'll do. will pull the latest version of that, check to see if there's any changes or changes, what changes there are, update any tools that need to be updated. Um, I think in in the version that we had, I think there was one one endpoint that was to do with declines and the no decline reason.

### **00:18:46**

**George Westbrook:** Is that is that something that's going to be going to be added in or is there just not going to be a decline reason for a transaction?

**Michael Moores:** That should be yes.

**George Westbrook:** Okay.

**Michael Moores:** So transactions are ones they we yet to test and sort of obly go through certification from the ISO level. So they're sort of a little bit way down the the line there ones.

**George Westbrook:** Yeah.

**Michael Moores:** So there's a lot of sort of errors, decline reasons and all that.

**George Westbrook:** Yeah. Perfect.

**Michael Moores:** So especially you the original version didn't have any statuses in or anything like that in the YAML. So we're just trying to push that through and and get that document ready as well.

**George Westbrook:** Okay.

**Michael Moores:** But yeah, everything should have a reason for what's you know what's going on. So obviously decline or a transition you'll have API errors which obviously will come back in the payload you've seen. So result payload and errors payload. But then if it's actual like a you know transaction isn't really an API failure but that trans

### **00:19:36**

**George Westbrook:** Yeah.

**Michael Moores:** transaction object will be a response decline reasons you know status there's quite a lot of different layers in the transaction so um what I do is to have a look at it see what you think there's any questions let me know because

**George Westbrook:** H.

**Michael Moores:** it's different like what we sent back to the network what we actually did what the client responded with so if we need around

**George Westbrook:** Yeah.

**Michael Moores:** that there's a little bit more to it than just a this is a response sorry explain

**George Westbrook:** Yeah. Yeah.

**Michael Moores:** through that for you as Well,

**George Westbrook:** Okay. Perfect. Um, so yeah, I think from now is I'll get this get this deployed.

**Michael Moores:** um

**George Westbrook:** Um I'll put it to testing and production as well. So it doesn't matter which one which one you use. Um and then it's then I suppose it's testing um just testing testing testing. What we'll do is we'll start thinking and looking at these these other ones which are like outside. So the kind of when we talked about like the agent inbox.

### **00:20:32**

**George Westbrook:** So what we might do there I'll look through the I think we mentioned about the alerts. So with with the alerts if there if some of the stuff's not ready we'll just mock it. Um, but is all it's going to be is a payload. So, if it if it changes, that's fine. Um, a way that we can store the alerts, we'll set up like some sort of simulated thing where we can run run it. It's going to simulate it and Then yeah, then that and then we'll need to think of a different interface for that. Rather than me going down a rabbit hole, we'll start working on the other

**Michael Moores:** Yeah, I think alerts especially from a you'll see it in the the YAML obviously that's not sort of committed to from

**George Westbrook:** ones.

**Michael Moores:** T from DT right now.

**Dorte Dye:** Stupid.

**Michael Moores:** So it's very much a later phase. They've not even suspect that. So you know the one thing we do want is sort of central place for alerts wherever that sits you know whether we build the

### **00:21:21**

**George Westbrook:** Yeah.

**Michael Moores:** AI first and then tack on other things afterwards then obviously that's the source so DT don't have an alerting system per se um so just keep that in mind when you're sort of specking that and if we can AI one the sort of central place that you know everything else could feed into then

**George Westbrook:** Yeah.

**Michael Moores:** that's a better process to go because obviously DT the endpoint we had DT was sort of just

**George Westbrook:** H.

**Michael Moores:** a post get type situation. There was no you know clever technology behind it. It was just a system would push that up and they were basically the system of record. So they weren't going to build anything you know very good basically. Um whereas this is obviously a more advanced now where we can actually push that in.

**George Westbrook:** Yeah.

**Michael Moores:** You know any blocking system we get as well we could pour those sort of in as well. So you get that full here's the errors, here's the actual thing going on. So try and boil that uh central

### **00:22:14**

**George Westbrook:** Okay. Yeah, that sounds good. Yeah, we'll do thinking around that. I think one thing we might need to think as well is what what we might need to do in terms of databases for

**Michael Moores:** is

**George Westbrook:** obviously storing the chats maybe storing storing the alerts and then if there's extra fields that we we might need to add um I think definitely for the for the even for the the um collagentic experience obviously we're going to have to store that somewhere. So is it interacting with the database you've already got or having a specific smaller one just for the chats? Um, I think maybe if seed that thought and then when we get to that in the next few weeks, um, that might be helpful to talk about in a bit more

**Michael Moores:** Yeah, it's a timely one actually. We're going through that now with the data lake.

**George Westbrook:** detail.

**Michael Moores:** Obviously, um we have keeping clients data together for the ease of obviously migrating or or keeping that data. So that's one consideration. Obviously the data lake we're pulling everyone into one central place that then brings in GDPR regulations and stuff like that.

### **00:23:14**

**Michael Moores:** So going through that now um obviously this we need to see what you're going to store as well if you're storing client data as part of the responses that obviously then

**George Westbrook:** Yeah.

**Michael Moores:** becomes more over to the side with the client data as well and and the same place I think which obviously you need some sort of mechanism to push that into or or to connect directly. So we need to DT on that one. But yeah, we're literally just doing a document now to DT to finalize that deployment of where our access will be. Obviously,

**George Westbrook:** Yeah.

**Michael Moores:** we don't want production access to the database ourselves. So we're just over layering. So, we're just building out your side as well in terms of the data lake access and obviously any production access as as well. So, I'll add that in there as an open question to them and see where we can fit that in because obviously they're they're managing the sort of PCI and the regulatory sort of stuff on that side as well.

### **00:24:07**

**Michael Moores:** So, we need to make sure we keep it all in one place. So, it might just be that we have to open connection to you and obviously I'll put that down to DT to consider in their build plan basically.

**George Westbrook:** To be fair, one thing we could on the AI server. No, actually, I was having a conversation in my head. Don't ignore ignore what I was saying.

**Michael Moores:** Yeah, I think it's probably an important thing to maybe speak to directly to DT about U. So, let me position this document as it is,

**George Westbrook:** Yeah.

**Michael Moores:** give them some time to read it and then we can speak to them. So, I assume you're okay now in development for now.

**George Westbrook:** Yeah. Yeah. Yeah. That's fine.

**Michael Moores:** Um but yeah, we'll get that conversation underway and then when we get towards deploying this into some form of you know fully UAT or fully production on our hosting environment then obviously we can go from

**George Westbrook:** Okay, perfect. Um, and then I suppose we've got the stack works call tomorrow,

### **00:24:55**

**Michael Moores:** there.

**George Westbrook:** haven't we? I suppose that's just realigning, understanding where they're at.

**Dorte Dye:** Yes.

**George Westbrook:** We talk a bit about where we're at and how we're going to merge it together.

**Michael Moores:** Yeah. Yeah, definitely. So I think they're they're very good.

**George Westbrook:** That's it.

**Michael Moores:** So they're underway with the the core. So it's quite a lot of actions on me to get the permission model stood up which obviously I think that'll be an important

**Dorte Dye:** Okay.

**George Westbrook:** Mhm.

**Michael Moores:** crossover point for you and and them and obviously the where it's going to land in the interface which I think what

**George Westbrook:** Yeah.

**Michael Moores:** I've seen is not the most complicated point. I just think how it gets deployed as well. So obviously from a DT will be hosting this.

**George Westbrook:** Yeah.

**Michael Moores:** So we have confirmed that we will at least for now be going in the DT tenant as one of our own subscriptions. So we will have some sort of access to to make sure you get your pipelines and stuff in there as well.

### **00:25:49**

**Michael Moores:** So that's another conversation we'll need with DT as well and see what's part of yours goes in with stat works and that DT pipelines already sort of engaged and working for the UI side and what you for the sort of the agent side as well you know hosting

**George Westbrook:** Yeah, I think that's I suppose that's you mentioned Azure Azure that it's going to be deployed on.

**Michael Moores:** that

**George Westbrook:** Would that mean that there's a requirement to use models that are through Azure?

**Michael Moores:** Um yeah, we'll have to speak to DT about we had a lot of issues with the console about them accepting it. So we'll have to make a plan what we want to what you want to use. So it always design first and functionality. So if you list me what you want to use, we'll pass that to DT and they'll say I'm not quite happy with this or that.

**George Westbrook:** Yeah.

**Michael Moores:** Then we can sort end if that's okay. But we would prefer to go with what we want and the best sol and

### **00:26:44**

**George Westbrook:** Yeah.

**Michael Moores:** then work on DT about accepting that or you know making sure they're happy with that sort of thing in there as well. So there's quite a few sort of third party frameworks that DT weren't happy with for the console that we work through managed to get that but obviously we don't want to sacrifice the design and the the performance and functionality meet what their needs are.

**George Westbrook:** Yeah.

**Michael Moores:** We do have other options if it doesn't suit with DT. So um you know potentially with

**George Westbrook:** Okay, perfect. That sounds good.

**Michael Moores:** that

**George Westbrook:** Um, I think I think that's everything. So I suppose it's yeah testing testing testing. We're going to have a think run through some ideas for the for the other parts. Um it'll probably be more UI focused initially and like clicky demos just so that the flow we're understanding the flow what it's going to look like and then integrating the the AI into it and getting it more like a live a live version rather than a a clickable prototype.

### **00:27:43**

**Michael Moores:** Yeah, sounds good. In terms of the the tooling, you said you're adding that into the demo. So, I can see what tool it's calling now.

**George Westbrook:** Um,

**Michael Moores:** Don't

**George Westbrook:** no. I know. I know what we need to do. What I might add is a dev mode. So, in the dev mode, you can see every single tool that's called that. That'll be good. Yeah. I did Did we mention that last time? I can't remember. Um,

**Michael Moores:** just go on your document and sort of mention what the likely end points were on that.

**George Westbrook:** yeah.

**Michael Moores:** might be better for me just to test and go no or yes on there maybe um in the cell as I'm testing might be more beneficial to it that

**George Westbrook:** Yeah.

**Michael Moores:** way I have done yeah

**George Westbrook:** Okay. And are you using playright to test it?

**Michael Moores:** but

**George Westbrook:** Okay. what I could I might have a think about how there's maybe think I don't know but if there's certain things that

### **00:28:28**

**Michael Moores:** yeah

**George Westbrook:** I can expose or guidelines that I could hand over so that when it's using playright it's like let's just say for example it's a button click rather than it looking opening having a look we can give it the actual um just just make it a bit more a bit easier

**Michael Moores:** Yeah. Yeah. We obviously go through it manually and the sort of workflows you sent are really good to to walk through that and then I just connect sort of play right to our back end vault to see what we've discussed and like that. Make sure it's aligned stuff.

**George Westbrook:** Yeah.

**Michael Moores:** So there's loads of PCI, GBR, all that stuff, extra sort of rules in there that I'm just going to do once over to make sure there's nothing I've

**George Westbrook:** Yeah.

**Michael Moores:** missed basically. But most the tool calls mostly I'll do myself and make sure it's called right

**George Westbrook:** Yeah. Yeah.

**Michael Moores:** thing as a a principle and obviously use sort of play right to say is there any other avenue that doesn't call that properly and stuff like that. So I think I'll run through it first and just make sure the tools that I see are what I expect and that you've got the sort of right endpoints and then at least we have as a basis to say yes that's calling the right tools and then obviously been tested there to make sure it's consistently calling the right things in the right order

**George Westbrook:** Yeah. Okay. Yeah,

**Michael Moores:** basically.

**George Westbrook:** that makes sense. So, dev mode, new, and then the new stuff. Dev mode, new stuff. Okay,

**Michael Moores:** Perfect.

**George Westbrook:** perfect. Right.

**Michael Moores:** Sounds great.

**Dorte Dye:** smashing

**George Westbrook:** Have have a good one.

**Michael Moores:** Perfect.

**George Westbrook:** Have a good one everyone.

**Dorte Dye:** it.

**George Westbrook:** And uh yeah, we'll have some have some new stuff by Thursday.

**Michael Moores:** Sounds good.

**Dorte Dye:** Sounds good.

**Michael Moores:** Thank you.

**Dorte Dye:** Thank you. Bye.

**George Westbrook:** Perfect. Speak to you in a bit. Have to get buns.

### **Transcription ended after 00:30:43**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*