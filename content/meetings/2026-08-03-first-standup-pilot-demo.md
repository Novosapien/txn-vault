---
date: 2026-08-03
type: standup
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-access-layer]]"
status: extracted
extracted-to:
  - "[[conversational-interface]]"
  - "[[generative-ui-rendering]]"
  - "[[mcp-server]]"
  - "[[permission-scoping]]"
  - "[[approval-queue-integration]]"
  - "[[integrations]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN — First Standup / Pilot Demo (2026-08-03)

> **Source:** Gemini transcript, synced from the shared folder (`shared/clients/txn/meetings/`). Attendees: Brett StClair, George Westbrook, Max Kingaby, Michael Moores, Dorte Dye. Duration 00:27:38.
>
> An earlier slot the same day (11:00 BST) was **rescheduled before it started** — Michael was away from his desk, so the standup moved to 15:00. That call carried no product content and is deliberately not filed.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Conversations list with status colours — green = finished/unread, orange flashing = paused for approval; work runs in the background and resumes on click | [[conversational-interface]] | Update banner added |
| Agent build state: skills, slash commands, streamed tool calls, plan-then-confirm, task list, message queue/stop, voice input; sub-agents not yet wired; panel placement still movable | [[conversational-interface]] | Update banner added |
| Rendering splits inline (small results) vs right-hand **canvas** (lists); canvas expands full screen, filters client-side; deep-links designed, not wired | [[generative-ui-rendering]] | Update banner added |
| **Component gallery** built as the review harness for every agent-renderable component | [[generative-ui-rendering]] | Update banner added |
| Component detail baselined on the **customer-service persona**; technical fields (network reference ID) demoted to caption level | [[generative-ui-rendering]] | Update banner added |
| Canvas/chat **flip** planned — canvas primary, chat alongside walking the user through it (stated 04-08) | [[generative-ui-rendering]] | Update banner added |
| MCP v1 runs as a **separate service on top of the API**, not embedded, because DT owns the Core API | [[mcp-server]], [[open-questions]] #42 | Update banner + register row |
| Approval thresholds **vary by user role** — super-admin acts, junior sends for approval, degrees in between | [[permission-scoping]] | Update banner added |
| Console has **no field-level permissions** today — page-level only, "given everyone everything so far"; Michael to review fields + confirm UI controls | [[permission-scoping]] | Update banner added |
| Michael's guard-rail steer: **start tight, loosen later**; **irreversible/terminal actions** are the priority (suspend recoverable, terminate not) | [[approval-queue-integration]], [[open-questions]] #26 | Update banner + register row |
| Blast radius through volume — the agent "could be doing 100, 200 at once"; lifecycle transitions are the bulk of the conditional logic | [[approval-queue-integration]], [[open-questions]] #26 | Update banner + register row |
| Mock DT API still built on the **old May YAML**; port to the July external/internal split still to do | [[integrations]], [[open-questions]] #32 | Update block + register row |
| Tool-call visibility undecided — show every call, make them expandable, or show only "I'm working" | [[open-questions]] #37 | Register row updated |
| Testing largely run by an **AI workforce**, not just George and Hasan by hand | [[open-questions]] #43 | Register row updated |
| Timeline: end-August bedded down, **final two weeks formal UAT** + environments/CI-CD; three weeks left; review turnaround is the constraint | [[index]] | Activity row added |
| Deploy behind basic auth with the screenshot feedback tool so TXN can play and break it (1–2 days); next demo Wed 5 Aug 15:00 | — | No action (ways of working) |

---

## Transcript

Aug 3, 2026

## **First standup \- TXN/Novo \- Transcript**

### **00:00:06**

**Brett StClair:** Hello.

**Max Kingaby:** Howdy.

**Brett StClair:** Hello.

**Max Kingaby:** Howdy.

**Dorte Dye:** You okay? Howdy. Howdy. Sounds like he had not enough coffee.

**Max Kingaby:** I I could definitely do with one. Definitely

**Dorte Dye:** Say too much red wool.

**Max Kingaby:** could

**Brett StClair:** Uh, we've just finished a meeting now and George is just nipping off for a uh

**Max Kingaby:** to go to the toilet.

**Brett StClair:** privacy

**Max Kingaby:** Yeah.

**Brett StClair:** toilet.

**Max Kingaby:** Where where where are you again, Brett?

**Brett StClair:** Hey,

**Max Kingaby:** Where are you

**Brett StClair:** um,

**Max Kingaby:** again?

**Brett StClair:** Iceland

**Max Kingaby:** Was it

**Dorte Dye:** I think he didn't made it out of his

**Max Kingaby:** nice?

**Dorte Dye:** bed.

**Brett StClair:** Forgot I had this on.

**Dorte Dye:** My dad is pretty crap. Let me just switch it off. Look like I'm sitting in a

**Brett StClair:** What do you mean turn mine off?

**Dorte Dye:** sauna.

**Brett StClair:** What am I doing? We spent the day this which is really terrible.

**Max Kingaby:** I quite like yours. I quite like yours.

### **00:01:13**

**Brett StClair:** Hey.

**Max Kingaby:** Oh, not that

**Brett StClair:** Yeah, I know.

**Max Kingaby:** one.

**Brett StClair:** I don't know why we do this sort of stuff. Uh, where's the background? Take it off.

**Michael Moores:** Please.

**Brett StClair:** There we go. Um, George is coming now. Um, the meeting that was meant to end half an hour ago ended at exactly half it went on. Um, we're having, it's weird on Mondays we try and keep relatively free, but jeez stacks up quickly.

**Max Kingaby:** It's cuz we have all our standups on Mondays, don't we?

**Dorte Dye:** But listen,

**Brett StClair:** Let's fit them all in.

**Dorte Dye:** I'd never have a Monday with you on Monday, though.

**Brett StClair:** I just try not to Mondays. Free it up. The other days are relatively free. Um,

**Max Kingaby:** Tuesday is always quite

**Brett StClair:** yeah. Tuesdays clear.

**Max Kingaby:** good.

**Brett StClair:** Thursdays are clear. Hello, George.

**Max Kingaby:** Hello. Sorry about that.

**Brett StClair:** It's weird. It's not quite picking up. I think Max's mic is picking you up.

### **00:02:25**

**George Westbrook:** Oh, testing.

**Brett StClair:** There we go.

**George Westbrook:** Testing.

**Brett StClair:** You're being picked up now.

**George Westbrook:** Sorry about that. That was me. I was I was on time for the call before that we that we had this morning.

**Dorte Dye:** That's true.

**Brett StClair:** I was explaining it went over.

**Dorte Dye:** I was

**Brett StClair:** It went over

**Dorte Dye:** late.

**George Westbrook:** And it we we had a few calls after each other and it was like the I needed to go to

**Brett StClair:** massive.

**George Westbrook:** the toilet. Put it that way. I was going to wee myself.

**Dorte Dye:** Okay, then show us what you have Another

**Brett StClair:** Okay.

**George Westbrook:** Right.

**Dorte Dye:** weekend.

**Brett StClair:** Um,

**George Westbrook:** Excuse

**Brett StClair:** so let's see what George and her son have basically been pumping out.

**George Westbrook:** me.

**Brett StClair:** It's going to be interesting for me, too.

**Dorte Dye:** Ah, so Hassan had to work on the weekend, too. You taking the time off and you make your team

**Brett StClair:** No,

**Dorte Dye:** work.

**Brett StClair:** I wasn't.

### **00:03:18**

**George Westbrook:** Yeah.

**Brett StClair:** I'm just sporting a hangover this morning.

**George Westbrook:** So, we have the the location for this little agent. We can move it wherever. We can have it as a tab here. We can have it up there. We can have it up here. Um, just put it here for like ease of use. Um, but this is a first hit on the agent. Can everyone see that?

**Michael Moores:** Yeah.

**George Westbrook:** Um,

**Dorte Dye:** Yeah.

**George Westbrook:** so we've got the conversations tab here. here. So you can see all of the previous conversations. Um, and these little colors here. So what do these mean? Green is I'm done. You haven't looked at me yet. So let's say you went away and said, could you go and research XYZ for me in the background? It's going to go away. It's going to do the research. You can go away, go onto a new tab, and it's just an easy way to know um, I'm done.

### **00:04:16**

**George Westbrook:** You click on it, it's going to come back. It's going to finish off where it's left off. Um the orange flashing one, that's when it needs approval. Um so let's say you asked it to suspend a card, for example. You don't want it to just go away and suspend the card. Um it's going to go away, do what it needs to do, and we will define the guard rails like right at this point, you stop and you ask the user, and you do not do not go on, you do not do any more than that. Um, and I suppose let's see, let's have a little play with it. So, at the moment, this is very extremely democratized. So, the workflows or the skills are not going to be ultra refined. Um, I mean, it looks good because a lot it looks like loads have been done, but there still loads more to do because this is all very for not for Gazi like it's going to be speaking to the agent. is going to be speaking to the services that we've built.

### **00:05:14**

**George Westbrook:** Um, but you might notice on some of these it might not follow the exact process that you'd want. So I suppose what is what has been built so far. So obviously we've got this the console which given the prototype look feels acts is pretty much the real thing just not connected obviously to live APIs. So it's it's mock data that's kind of hardcoded in. Um, but like I said last week, why do we want to build that? So that when we're doing the stuff with the agent, it's not in some isolated thing that doesn't really have much of a resemblance to what the console is actually going to look like. Um, so let's call it console replica. That's the first thing. Then what we did is we built the mock version of the API. It's currently on the old YAML file, but very easy to port it over. So, we built a specific service just for that so that it's going to be like what it's going to be when we're interacting with the API.

### **00:06:13**

**George Westbrook:** Um, randomizing the payloads, things like that. But, we've got kind of a a data store behind the scenes. So, it's going to be um Oh, a bit of audio feedback. Um yeah, so it's it's going to make sense the data. Um but it's all all mock data. Um and then the MCP server. So V1 of the MCP server kind of like a monolith where it's just sitting it's a separate service which is going to connect to the API um so that it's going to be mirroring what the actual real API would be like but is not integrated into the actual API. So sometimes when we'd be building um call it an MCP server, we'd have the deployed API and the MCP server would be sat inside that effectively which is obviously we're not going to be able to do that with DT. So it's going to be something that sits the top of it. Um then also built the the agent. So it's going to give you that clawed feel. Um we haven't got the sub agents and stuff like that working, but it's obviously going to execute tools.

### **00:07:20**

**George Westbrook:** Um, it's got skills baked in, things like that. Slash commands. Um, so it should be looking and feeling quite good. So I suppose if we go, let's go suspend a card for example. So it's going to load the skill in with these things like tool calls. We can show we can work out um or debate which ones do we want to show. Do we want to show them like that? Show every single tool call. Do we want users to be able to click in and see it or do we want it to kind of be like I'm working. I've been doing this in the background. Um then there's obviously the granularity like this. We don't really I don't really think this is relevant to show a user. Um but we we've got it here at the moment. Um, so yeah, let's go. Yep. So, usually with these, it's going to show the plan first. This is what I'm going to do.

### **00:08:22**

**George Westbrook:** Um, are you happy with that, Mr. or Mrs. user? You go. Yes. Um, and it's going to follow the plan. It should create a task list as well. Um, I'm not sure if this is going to work, but we've got the little voice icon here as well. So, let's just test this on my phone. Yes, that looks all good. Please, can we add that in or please can we just do this? There we go. It's that voice in UT's working now. It's going to be speaking to the MCP server. So, it's going to be querying, finding all the card holders. Let's go first one, please. So, this is the kind of what we call like the gener generative UI component. So these are aspects from the actual this is zoomed in quite a lot. So aspects from the actual application in the console that are going to be rendered within the actual chat window. So you could go that open the canvas and click through look at James Thornton see some of the details look through some of the controls that he's got any transactions.

### **00:09:52**

**George Westbrook:** um it's not wired up yet, but like say for example, if you clicked on this, it's going to take you to the actual relevant page for that specific component. Um you can expand it out as well, so it's going to appear full screen like the actual application. Um these aren't wired up yet, but if you just wanted to take those actions yourself, um it's going to let you do that. But we'll do the agent version. Um, so like I said, it said, "Right, let's cancel the cards for James Thornton." It's not just going to pick a random one. It's going to give the user, "Okay, well, I've noticed there's actually two cards. So, which one do you want?" Um,

**Brett StClair:** George, can I just let James know his part's about to be cancelled quickly before you do

**George Westbrook:** let's go.

**Brett StClair:** that?

**George Westbrook:** Yeah. Drop him a message, bro. And it's it's similar to Claude in the way that if you wanted to cue a message, you can type it in, it's going to cue.

### **00:10:51**

**George Westbrook:** If you want to stop it, it's going to stop. Um, this one I forgot to cancel before. Um, so here's the the approval step. So any of these sensitive actions, obviously, we might want to change the way this looks. It's going to stop, go to the user, are you sure you want to do this? Um, we can play with the user access as well. So, let's say if there's somebody who's got like super admin, certain things they don't have to ask for approval, but let's say you've got more junior team members. Um, maybe a lot of things you want to put for approval. Um, and then varying degrees up and down based on who the user actually is. So click. Oh, think that just broke. Love that on the demos. Um, there we go. I think that's bugging out. But what it's going to do is it's going to um Where are some of the old ones? Yeah. So, one what it's going to do, it's then going to run the test authorization to make sure that it's actually been suspended.

### **00:12:34**

**George Westbrook:** Um then after it's going to update the update the canvas to show that it's to show that it's been suspended. Um so why did we why do we do it? Just so that we can test the flows make sure the agents simple things like when you send it a message is it going to respond? Um when it executes tools is it doing that in a durable way? Um so although this might appear like oh sweet there's here's the agent there's still loads more to do. Like I said, when I just tried to do that suspension there, um, it didn't go through. So, just making sure that we're hardening it so that it's not nothing's going out there that's got these little errors in there. So, I suppose thoughts, any any questions, any concerns, anything that you're like, "What the f\*\*\* are you doing, George? Why are you doing that?

**Michael Moores:** No, I think it's good for me. Great, great direction. I say yeah, I think we need to have a think about those controls.

### **00:13:31**

**Michael Moores:** I think we discussed broader that we'll probably start pretty tight and see what we can loosen. And I think top of my head obviously as you've done suspension is probably right. Obviously in the API or console we're a bit more lapsed on that because obviously it could be undone. So with the AI you could be doing 100 200 at once. So you don't want around and go oh I've suspended loads of stuff and the most important one is the final actions terminates

**George Westbrook:** M.

**Michael Moores:** that can't be undone is the real to target.

**George Westbrook:** Yeah.

**Michael Moores:** And obviously you'll see in the YAML pretty much everything has a termination state or a a transition endpoint basically. So that for me would be the the one to be cautious because that's changing functionality. Um so I think they're definitely the way where we should focus on putting that sort of additional uh governance around. But yeah, I think it looks looks

**George Westbrook:** Perfect. Yeah,

**Michael Moores:** great.

**George Westbrook:** because I think what where we we'd be thinking what what's going to happen next is fix some of the bugs, keep on testing, keep on testing.

### **00:14:28**

**George Westbrook:** Like you can see here, it's don't get me wrong, me and Hassan have been testing it a lot. Um, but a lot of these are AI testing itself. Um, having a workforce that's going through testing, making sure everything's as as needed. Um, so testing what we got at the moment and then starting to think about like some of these components. So, for example, is this too much? Like if a user is just wanting to suspend a card, do they need to be able to see everything? Um and it's is the look feel. Okay. So, I think I can't remember if I had it. Uh, you agent here. So, what one of the things we've been building is kind of like a gallery for the components that the agent is going to that's the agent's going to render. Um, but this is where we can have a play around to like if it's rendering a transaction detail. Is that enough? Is it too much? Does it look good?

### **00:15:28**

**George Westbrook:** Does it look bad? Um, because over time, what we're going to be building is like a uh a collection of all these different components that the agents um that the agent's going to show. And I suppose it's when is it showing it, how's it going to show it? Um, and then obviously going back to all the access stuff as well, like if the user is the lowest tier of user, is there certain information that we might want to hide? Um and that yeah that wouldn't be so much deliver the agent more like the actual front end kind of client client facing filtering. Um or the to-do list as well. Yeah,

**Michael Moores:** Okay.

**George Westbrook:** that's what the to-do list will look like when it's when it's there. Um but I think as well as that is it's just working out what workflows are there that we want to start with. Um mapping them out start to finish. Um what API calls need to be made. Um, and what should the overall process be

### **00:16:26**

**Michael Moores:** Yeah, that looks great. I think yeah, I think we should think on our side.

**George Westbrook:** like?

**Michael Moores:** I say you don't want to show too much of the the detail. I think here also I think we need to consider what type of user. So that transaction one for example is good detail. Again, I need to think about all the fields we have. But one thing that swings to mind maybe the the like network reference ID. So you need that to speak to Visa and Mastercard. So that's something that's a little bit more technical. Again, it depends if you're a customer service agent versus a technical agent. So I think I just need to have a think about what do we want to show to everyone to your point and what else do we want to have in there to say this is some more of the detail stuff and obviously how does that align to what we show in the UI as well. Um there's not too much at the moment in terms of you can see this field but not that field in the UI.

### **00:17:14**

**Michael Moores:** It's more you can see this entire page or you can't. Um we sort of just given everyone everything so far. So I think from showing the information we just need again to look at what's suitable for everyone for now

**George Westbrook:** Yeah.

**Michael Moores:** and then we can go into that you know specifics if we want to. I think certainly for the start it would be yes you have access to products or you have access to this page and not the other. So I think that's where we probably first and then um yeah obviously have a look at

**George Westbrook:** Huh?

**Michael Moores:** what we've actually got in there. Um obviously any controls that we do put in the UI we'll also let you know as there still some sort of ongoing

**George Westbrook:** Yeah.

**Michael Moores:** discussion that we've got a broad idea obviously you know in terms of the UI the basic one would be if it's already suspended you can't suspend again that that's the the basics putting in. So, it's all about learning those life cycles. I think they're all pretty much the same.

### **00:18:04**

**Michael Moores:** You know, active to suspend, suspend to active or terminate. But if it is suspension, obviously you go suspension to terminate or suspend to active is terminated, then there is nothing you can do. So, it's those sort of life cycle events that are going to be most of the conditional stuff in there. Um, so yeah, we'll have a think on those components you've done and then just try and pull out some of the key details. I think what you've got there is a good start. I was just trying to think if there's anything extra you want to put in there. Maybe, you know, smaller text, more caption type rather than in the I think would be, you know, the network reference, for example, would be one that if you're looking for it,

**George Westbrook:** Yeah.

**Michael Moores:** you'll know it's there. If you don't really care about it, having it in the bottom in the sort of caption may be the better way gloss over it. So, I think we just need to sort of see how obvious going to make that data.

### **00:18:52**

**Michael Moores:** Basically, we know it looks looks great.

**George Westbrook:** Yeah, because because I think like so one of the things you've got is to call it the inline ones and then the like so we'll call this part on the right hand side the canvas um is like things like transactions like this is for me I don't want to be seeing transactions in a massive list here like it it interrupts the flow of the chat um but then you so what say for example we could have here is like a a canvas card summarizing how many transactions and then when they click open canvas that's where it's going to show here. So we could have so all of those things that that you mentioned before like I want to see this field, I don't want to see this field. Some of it is maybe needs to be enforced on our side in that you even though you might want to see this buddy, you cannot you're not allowed to. But then also for like user preferences like let's say they they don't want to see the um the date.

### **00:19:43**

**George Westbrook:** I mean most of the time they are. We could have filters up here that in the actual canvas they can click and it's going to filter it because the data is already in the front end. So we can manipulate it in the same way that we would do with a wi with a normal

**Michael Moores:** Yeah. Yeah. Sounds good. I think I say I think happy with that.

**George Westbrook:** table.

**Michael Moores:** Obviously, I think we just need to think later on about how we, you know, open canvas. You know, we probably sort customer service view transaction. It's more descriptive on there.

**George Westbrook:** Yeah.

**Michael Moores:** These are things that we can do later but it's more just driving them through that thing if we are showing a summary. I think we have to target this at the the lowest user which is the customer service then add those beneficial stuff on you know for the technical stuff but I think for now yeah aim it at the customer service and

**George Westbrook:** Yeah.

**Michael Moores:** then we can see once we've done that we can see is there anything else we can do specifically for you know a certain type of user I think but yeah for what we've got here and the type of queries and questions you've already done I think these fit really well with customer service obviously when we start talking configurational

### **00:20:37**

**George Westbrook:** Mhm.

**Michael Moores:** and stuff we can then look at perhaps that's terms of that sort of flow and then naturally you can't configure products. Therefore, you know, when you're in products and you're in spend controls, that that terminology, that that context becomes more technical whereas if you're just creating generic transactions card holders then we can have sort of you know different sort of flow there basically but no great for start thank

**George Westbrook:** What what we can do is we can get this get this deployed.

**Michael Moores:** you

**George Westbrook:** Um I might add I might we might add some like basic authentication so that you can play around have your own chats things like that. Um, obviously it's not going to be battle hard and it's just for internal internal use, but we'll get deployed authenticated. So, you can go around play with the play with this, play with the slash commands. Um, and then it makes it feel like less of a less of a demo and something that, like I said, you can play around with and break. That's the most important thing.

### **00:21:45**

**George Westbrook:** Just try and break it. Um,

**Dorte Dye:** I'm good at

**George Westbrook:** so I'm good at doing it,

**Dorte Dye:** that.

**George Westbrook:** but in the situation where you don't want to don't want it to break. I when you're showing something to somebody and you're like, "Well, this this worked. This worked when I tested it 10 minutes before."

**Dorte Dye:** So if y'all

**Michael Moores:** No. Yeah, that's great idea. Um, I say I'll do a bit more thinking on our side and get sort of concrete ideas of how how these flows

**George Westbrook:** Um

**Michael Moores:** looking. But I think I don't see that's, you know, wrong. It may just be adding some additional stuff in to benefit that user trying to think about what they're doing at that time. Uh,

**George Westbrook:** yeah.

**Michael Moores:** I think that will come anyway as we get into the workflows as you say. So think on that as well.

**George Westbrook:** Yeah. Because I think where feedback would be best spent is in terms of like UI um maybe how components are looking, how they're rendering, things like that.

### **00:22:43**

**George Westbrook:** In terms of processes like oh it asked me um the plan it gave wasn't actually what's going to happen. It's it's it' be really good to know. Um just note that we haven't really put much thought into this needs to happen at this step. Um, but that's not to say don't give us that feedback because I say we'd rather we'd rather know.

**Michael Moores:** Yeah, that was

**George Westbrook:** Um, yeah, I think I suppose what we'll do,

**Michael Moores:** perfect.

**George Westbrook:** we'll add in the the feedback screenshot thing. Um, so then it's just going, it will do the screenshot, add in the comments, things like that. So, we might need might need a couple of days to get that integrated um, and then obviously get it deployed as well. So yeah, what's it in Monday? Yeah. So yeah, deployed um running live authentication um feedback and then what we've got is a really nice foundation to push off of. We've got an agent that you can speak to. We know it can render components.

### **00:23:45**

**George Westbrook:** Everything else is very raw and ready, but at least now we can get into the cadence of right here's some here's some feedback. Let's get it in. Let's go. Let's get it run through. Um and yeah and then go for there and feel free to click around here as well. All these other ones.

**Michael Moores:** Yeah, that's perfect. Looks great.

**George Westbrook:** Um I think yeah I think in terms of demoing I think that's yeah that's that's everything in terms of the agent side. Um,

**Dorte Dye:** Okay.

**Brett StClair:** I think goal is to after by the end of this month that we've got pretty much

**George Westbrook:** yeah.

**Brett StClair:** everything bedded down and then you're essentially doing formal UAT um for the final two weeks and making sure all the right environments are stitched up, all the deployments properly stitched up, the CI/CD, all that kind of stuff. So when you look at it from a month point of view, the turnaround time on reviews is important. Um, and so George putting in the review functionality, um, it just takes us a bit of time to get it stitched in. Um, I think becomes really important because by the end of this week, we're down to three weeks and the hard part is this, you know, constant because we're you're going to keep every time you use you're going to pick up things

### **00:25:07**

**Dorte Dye:** Yep.

**Brett StClair:** that bother you or once you've gotten used to the experience, you'll want it better. And so that's the point of it, right? You know, code is throwwayable. So you want something flowing better or better look and feel, just tell us and and we get it there. But it's now this backwards and forwards, backwards and forwards, backwards and forwards, backwards and forwards. That's that's the real hard part.

**Michael Moores:** That sounds

**Brett StClair:** Anything else?

**Michael Moores:** good.

**Brett StClair:** I think that's it.

**Dorte Dye:** So, when do you want to do the next demo? On Thursday.

**George Westbrook:** Um,

**Dorte Dye:** What's feasible?

**Brett StClair:** We can also demonstrate the review stuff.

**Dorte Dye:** Perfect.

**Brett StClair:** Um, let's look at diaries.

**George Westbrook:** Thursday.

**Dorte Dye:** 11 o'clock is very fast.

**Brett StClair:** Everyone fine with 11:00?

**Dorte Dye:** Uh I'm off on

**George Westbrook:** Um.

**Dorte Dye:** Thursday.

**Brett StClair:** Are you off on Friday as well?

**Dorte Dye:** Yes,

**George Westbrook:** Oh.

**Dorte Dye:** just this week.

**Brett StClair:** Well, let's let uh Wednesday. Are you off?

### **00:26:21**

**Dorte Dye:** No, Wednesday. I'm available.

**Brett StClair:** So, maybe we do an afternoon one on Wednesday.

**Dorte Dye:** Yeah.

**Brett StClair:** Give us a bit of

**Dorte Dye:** Mike, your afternoon looks completely free.

**Brett StClair:** time.

**Dorte Dye:** I just have one meeting at 2:30 at 2:30 to 3\. So, we could do it after that meeting at three

**George Westbrook:** Yeah.

**Brett StClair:** Um 3:00.

**Michael Moores:** Yep.

**Dorte Dye:** again.

**Brett StClair:** Does that suit you?

**George Westbrook:** Yeah.

**Brett StClair:** Does that give you Okay,

**George Westbrook:** Yeah, that's all

**Dorte Dye:** Perfect.

**Brett StClair:** cool.

**George Westbrook:** good.

**Brett StClair:** I'll send out the meeting

**Dorte Dye:** Awesome.

**Brett StClair:** invite.

**Dorte Dye:** Cool. And we have a play around then.

**George Westbrook:** Perfect.

**Brett StClair:** Should cover us.

**George Westbrook:** Yeah, it I maybe need a bit of time to get it deployed, maybe a day, maybe two. Um, and then that will hopefully have all the feedback stuff in there as

**Dorte Dye:** Okay.

**George Westbrook:** well.

**Dorte Dye:** So then just ping us when it's deployed. Then we go in.

**Brett StClair:** Yeah,

**Dorte Dye:** Yeah. Awesome.

**George Westbrook:** Okay,

**Dorte Dye:** Perfect. Thank you guys.

**Brett StClair:** perfect.

**Dorte Dye:** See you later.

**Michael Moores:** Take care.

**Dorte Dye:** Bye.

**George Westbrook:** perfect. Speak to you soon. Bye-bye.

### **Transcription ended after 00:27:38**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*