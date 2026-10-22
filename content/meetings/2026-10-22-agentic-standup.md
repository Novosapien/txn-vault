---
date: 2026-10-22
type: standup
description: "The co-pilot goes live on the production demo, the agent loses the power to change permissions, and chat retention drops from 30 days to 72 hours"
scope:
  - "[[developer-support]]"
  - "[[agent-access-layer]]"
  - "[[architecture]]"
  - "[[delivery]]"
status: extracted
extracted-to:
  - "[[portal-co-pilot]]"
  - "[[permission-scoping]]"
  - "[[architecture]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-22)

> **Source:** Gemini transcript, 22 October 2026, 27m 30s. **Novosapien:** Brett StClair, George Westbrook, Max Kingaby, Lily StClair. **TXN:** Michael Moores, Dörte Dye, Ian Johnson. Ian joined a few minutes late. Hasan was addressed on the call but does not speak in the transcript.
>
> **A note on sources.** A Fathom transcript of this call also exists and merges every speaker into one voice. The labelled Gemini transcript below is the record, and it corrects the Fathom version in two places that matter: **"DT" was rendered as "Dörte"** in the Azure discussion, so the party to be asked about hosting is **Direct Transact, not Dörte**; and the per-tenant storage question was rendered as *"may be perfect"* rather than *"per tenant"*.

## The co-pilot is live on the production demo

**Knowledge Hub, explicitly not the Console.** Ian asked for the clarification: *"just on the co-pilot, you said it's ready to test. Is that the, we talking about knowledge [hub] or we talking about control center?"* George: **Knowledge Hub.**

- It sits on *"the production demo version at the moment"*, and TXN can try it whenever: *"whenever you got any spare time, feel free to test."*
- **The evaluation harness from #117 is running.** George: *"obviously got the automated test set up loaded in the personas. So we're just running that, iterating on that."* Michael's personas and questions drive the background cases.
- Novosapien are watching for UI and speed problems: *"if there's anything any of you find, just drop us a message. We'll get on to it like right away."*

### The test ask is deliberately narrow: three flows

George scoped TXN's own testing down rather than up:

> *"The main thing would be those flows that you mentioned, Mike. Just making sure for next week that they are **exactly how you want them to be**, both in terms of the responses and the way that the UI is functioning, so that we absolutely nail them."*

**And he said why.** *"Obviously appreciate you guys don't want to be going in and going through 40, 50 different questioning styles and testing each one multiple times. It's not feasible. So by doing those three, that would really really help."* Changes to those three carry over to the other workflows. Michael: *"yeah, sounds good."*

**This is the right shape against #115**, where the demo window is 28 to 30 October. The three flows are what will be shown.

## Ian asked for assurance the agent cannot go rogue, and got a protocol rather than a guarantee

**The ask, and it is the governance moment of the call:**

> **Ian:** *"George, just on this one thing, I think we just need you guys to give us some assurance that it's been properly tested, that **this thing can't go rogue and do anything it's not meant to**. We talked about it yesterday. I'm far from an expert. Mike's giving you one of the output things that we think is the protection, but I don't know, anything you guys can do just to make sure that we're not in a position where **something goes and starts running havoc**, then that would be great."*

**George's answer had two parts.** First the code: *"make sure the code in terms of permissions, they can't do that."* Second, and this is new scope:

> *"Also maybe things they do have access to, similar process to what we're doing with the co-pilot at the moment. **We'll create the testing harness. We will [run on] mock data as well. We will create the most malicious personas that could ever be**, they're trying to do this and do that."*

**Then the caveat, which he volunteered unprompted:**

> ***"So I mean there's bound to be one out of a thousand where it is able to do something. But we'll stop that with this testing protocol."***

**Why volume rather than inspection:** *"as we all know, going through one person, one chat, doing that is not high enough volume. Hence why we'd like to do the **agent speaking to agents**."*

**So the assurance Ian asked for has not been given.** What exists is a method that would find most of it, an acknowledgement that some would get through, and no agreed threshold for what counts as passing. New row [[open-questions]] #123.

## Two permission decisions, both changing what was recorded on 20 October

### The agent cannot add users or roles, and TXN is forcing it

**Michael announced it**, as the one change to come out of the Stackworkz call:

> *"The one thing we did agree with them afterwards was that **we'll be revoking the ability to update a user to the agent credential**. So just to avoid that ability where you give yourself more permission. So that's a change they're doing. So you can have access to everything the user does **bar any user or role addition**. We're going to **force that through the console** for that user, just so we avoid that. You know what you hear about them going in and managing to change the permission to do something. So we're actually enforcing on that side."*

That is a privilege-escalation guard: the agent inherits the operator's rights and can never widen them, its own included. **Stackworkz are making the change, TXN are mandating it.**

**Alongside it, two layers of validation**, which George described: *"we'll have the first layer of validation on the MCP server, the second layer in the control center. So we're catching any potential errors, no matter how small they would be, at two points."*

### Permissions arrive as a full list, not as one of four buckets

**George reasoned this out on the call, and it supersedes the 20 October position.**

> *"There could be, let's say, four buckets. A user fits into one bucket, **but they might have some custom permissions associated with that**, and that would obviously be overlaid onto the Control Center as well. So, thinking about it, whereas before I thought maybe we get a variable which comes back to say they're in bucket one, **what might be better is we get back their full permissions list, and then given that we turn them off. So it mimics the console or Control Center exactly**, rather than being like, no, we can only do it for these four buckets."*

Michael agreed twice: *"yes."*

**Why it matters:** a per-profile skill set cannot express a per-user override, so the bucket model would have diverged from the Console the moment anyone was given a custom permission. See [[permission-scoping]] and #107.

**On the Stackworkz relationship**, George had been worried about the load he was creating: *"I was just conscious, didn't want to give, because of us, give them loads of extra work, but it seemed like that was something they weren't bothered [by] at all."* Michael confirmed the follow-up: *"a call with them afterwards as well, so they're pretty happy with that. So they're just going to work through a couple of ideas, and obviously we spoke to them with **Ian as well as Dörte**. So all aligned and moving forward."*

## Where the agent's data lives, and the PCI boundary

**George raised it and separated the two surfaces.**

**The Knowledge Hub is not the problem.** *"It's not sensitive data. The questions, well, it's not as sensitive data. They're asking questions, the tool results, the tool call results. It's information that's in the Knowledge Hub."*

**The Console is.** His questions were precise, and they follow from something Michael had said earlier about **per-tenant** storage:

> *"You mentioned previously the approach of storing data maybe **per tenant**. So we might need to get more of an understanding about how that data is stored. **Are we going to have to put the traces for the agent within certain locations depending on where the tenant is? So does that mean we need access to update the schema of certain databases that exist, or do we isolate them**, so it's just an AI database, so that it's not touching any of their current data, because in the Control Center there could be sensitive data."*

And the forcing function: *"in order to manage the chat history we're going to have to store that data. So it's just a matter of where your preference would be, be it an isolated database or the one that you're currently using."*

**Michael's answer is an architectural decision, and it keeps the AI outside PCI.**

> *"We've got **a database per program manager or TXN client**. I think that is governed under **DT's PCI environment**, so be careful there about where we put that in. So I think **there'll be pushback from DT** on putting that in there. So potentially having **a database on that node for the AI specifically** might be the best way to go. We will also have **a data lake** where all of this will eventually feed back in. So I think that's where the data will connect back together... but I think it'll probably be an **AI-specific database away from the PCI stuff**."*

So: the agent's own store sits on the AI node, outside DT's PCI environment, with the data lake as the eventual join point. **It depends on a node nobody has yet asked DT to build** (#119).

## Retention: Ian asked, and 30 days became 72 hours

**Ian asked the question:** *"How long are we planning on retaining data that's in the chat?"*

**George put it back to TXN**, while making the case for keeping it: *"it could be a day, it could be 30 days. So that decision kind of sits with you guys. Do you want it stored forever? Because with storing it for a longer time there's extra functionality we could add in, searching through previous [chats], drawing maybe user preferences or certain actions that are taken a lot."* His own starting position was *"something like the knowledge hub, I think 30 days is a good target."*

**He also noted where it actually sits**, checking with Hasan: most of it is in the browser, because Knowledge Hub chats are short. *"Whereas the agent in the console, although it appears it's doing one tool call, behind the scene it might be 10 or 20."*

**Michael set the number, and the driver is the public sandbox, not the chat.**

> *"I do know that we, from a public sandbox point of view, will be **dropping the data in there every 72 hours**. So just in case there is personal data in there... whilst it's a public sandbox, and we discussed doing an isolated one later behind login, whilst it's fully public, whilst we tell people not to put real data in there, [they] could do, and we don't want to store that. So **we've come with 72 hours**, meaning you can go away, come back the next day and still test and check that, but it's not so long-term storage."*

**So the chat aligns to the sandbox.** George: *"at the moment we've got it 30 days for the knowledge hub. Drop that to 72 for anything that's being stored."* Michael's reasoning for aligning them: *"if that chat ends, the data is also gone."* He added there is *"no issue with having a chat that's longer than the data that exists."*

**Ian's defence of 72 hours is a statement about what the co-pilot is for**, and it is worth keeping:

> *"Theoretically there's nothing stopping somebody from copying and pasting the response that's in a chat into whatever they want to paste it into... I'm trying to think of the scenario where I'd want to come back 48 hours later to find something that I've just asked a question about on the knowledge hub, because really the idea was **to enable them to do the thing that they're looking to do rather than build up their knowledge of card programs**. If they want to build up their knowledge of card programs, then that's a case of, well, you can copy what the response is, put it somewhere that you can keep it, because **it's only meant to be effectively a shortcut to reading all the docs and deciphering it yourself**. So nothing's being removed from them, the source material is still there."*

And on the balance: *"bear in mind we've gone from a position where most people don't have anything, or if they do it's not very good, to, okay, we've got something we think is really good, and it'll still be there 72 hours later. Seems more than fair to me."*

> **Worth holding next to #114.** On 15 October Ian wanted a step-by-step walkthrough because *"they don't know what they don't know"*. Here he says the co-pilot is not for building knowledge of card programs. The two reconcile as teaching the task in front of the user rather than the domain, but it is a line to keep in view when the guides journey is designed.

**The MCP server raises nothing.** George: the data is *"only really going to be information about the docs"*. Michael: *"for MVP, obviously we keep it the same."*

### The second tier, which is how #92 finally gets a mechanism

**George proposed it straight off the back of the retention cut**, because the value of the chats is not only to the user:

> *"Let's say you've got loads of users asking loads of questions. Obviously it's providing value for them, they're learning, they're understanding, but also **it's very very valuable for you guys in that every once in a while, looking at the chats, being like, what questions are people asking? There's this one question everybody asks about two or three turns into a chat. Everybody's asking [it]. Maybe we need to update the docs.**"*

**His middle ground:** *"is there a kind of middle ground wherein, when it's being stored long term, **we strip out any tool calls that are going to hold anything potentially sensitive**, but retaining the data that's valuable for all of us in terms of improving, be it the docs, the experience, or any aspect of TXN?"*

**Michael accepted it:** *"that works for me. The sensitive data is a key there. So removing that means **we can store as long as we need**."*

**So retention is now two-tier:** the full chat for 72 hours, and a sanitised store with tool calls stripped, kept as long as needed, for improving the documentation.

**And Michael is already running the loop by hand.** *"We're doing the same from a ticket side as well. We want to collect that all together, so we can have a look at who's asking the questions on the knowledge hub. From a production point of view we'll also be looking at what tickets we get in there. How can we add that back in? And ultimately, **I've built it out right now, but [I] have like a doc improvement thing to say, we've seen these questions highlighted.** That's something we can go with yourselves to say, extend this to say this is what we think, and actually raise that, and ultimately you could do it as a draft as well. So right now obviously [I'm] doing [it] on **my own Claude**, but I think that's somewhere we could go from a full suite perspective, to actually build it to the bot itself and **self-improvement**."*

**Ian's endorsement names exactly why the harness is not enough on its own:**

> *"You beat me to it, George. That was the thing that just crossed my mind: **if we only got [72] hours, how do we make sure that we're getting better with time?** We've given a set of sample questions, but **I can guarantee the chances are the first one probably is not on that list.**"*

That is the strongest argument yet for the live loop at #92 running alongside the test harness at #117, rather than behind it.

## Infrastructure: containers are portable, Azure Front Door is the unknown

**Nothing is in Azure yet.** Ian asked directly: *"Have you got it stood up in Azure? Are you going to stand up in Azure? I'm just thinking about moving forward. How are you going to make sure that this thing works in the infrastructure that you're planning for us to ask **DT** to put in place?"*

**George's answer is that the question largely does not arise.** *"At the moment we've got it all in GCP, but it's all containerised. So we're using Docker containers, and with that it's kind of plug and play. **A Docker container is a Docker container.** We could put it on AWS, GCP, Azure, and it's going to look, feel, act exactly the same."*

| Difference he named | Effect |
|---|---|
| Request timeout | GCP 300 seconds, Azure 240. *"We're never really going to have that issue"* |
| CPU and RAM allocation | *"Maybe it's in increments of one and a half instead of one"* |
| **Fallback if Azure Container Apps is unavailable** | *"Something that's a bit more VM based, same thing. Get into the VM, make sure Docker's installed, load in the image"* |

**He asked for Azure Container Apps** as the equivalent of Cloud Run: *"it's similar to Google Cloud Run[ning], that it's got that scaling up, scaling down. Or is there any kind of step choices and limitations that might be there that we should be aware of?"* Michael: *"not that we're aware of."*

**The one real technical unknown is Azure Front Door.** George: *"with the agents, they **send server-side events, which sometimes Azure Front Door doesn't like**, but we found a, it's not a workaround, it's a solution, because obviously we don't want to be finding workarounds when it comes to infrastructure. We want to make sure that we're doing it the proper way, but we know what we'd need to do in that instance."*

Michael confirmed it is in use: *"definitely. The front door's across the front of the API already, so **the nodes sort of sit to the side, but they are governed by the same thing**, assuming they're putting them where the rest of the stuff sits."* He will raise it immediately: *"I'll send that question now, and then if there are any questions we can get that in front of them early, early doors, and then at least we have a clear direction to give them when we're ready."* New row #124.

**George asked for fallbacks before the request goes in, not after:** *"making sure that if that's not the case, that we've got a fallback, so that if they say no, we're not sat there thinking, what are we going to do."*

**Michael owes George two things:** the list of what TXN is already being charged for, which Ian sent him, *"so you can see what we're already using as well... see if that aligns"*, and the ecosystem diagram. Anything beyond that goes to DT directly.

**And the request to DT is being held deliberately.** George: *"taking what you said the other day, we don't want to rush it. We want to make sure it's well thought [through], hence why we haven't sent something over already."* Against #119, where the hosting requirements were due to DT on 21 or 22 October, that is a choice to trade a day or two of lead time for a better-specified ask.

## Cost control: acknowledged, deferred, not built

**Ian raised it**, returning to an earlier conversation: *"we did talk about, particularly on the knowledge [hub], and it's relevant to the control center, making sure that we had something that managed the workload, to make sure that we weren't getting into a situation where **this thing was exploding from a cost perspective**."*

**George's answer is that it is tractable and not yet done:** *"our priorities at the moment have been, right, let's get the look, the feel, how it's speaking sorted, because that stuff in terms of, say, rate limiting, we can deal with, because there's going to be a way we can identify a user, and given that user, what are they doing? Are they sending a thousand requests per second? Well, no, they're not going to be able to. The max is going to be, maybe two, three, five."*

Recorded against #97, which is marked answered on DT's own rate limits. **The co-pilot's own per-user limit is a different thing and does not exist yet.**

## Dörte's idea: publish the odd questions

Off the back of George joking that someone will ask the co-pilot how to make spaghetti bolognese, **Dörte proposed turning it into content**:

> *"I think we should put that in, one day a week our co-pilot does something funky. So like **Monzo has a LinkedIn account** with these, from fancy tech, where everyone is talking about [it]."*

Ian extended it: *"or the questions they got asked."*

**It was not taken as a decision**, but it is the third instance in a month of TXN wanting the AI made visible as marketing, alongside the published skills list at #106 and the co-pilot as a launch differentiator at #105. Worth remembering when the launch content is chosen.

> Ian also named the real version of the risk underneath the joke: *"we will check to see if anybody asks how do you make spaghetti bolognese on the first day we go live... but it won't take very long to track down the perpetrator."*

## Findings and where they landed

| Finding | Destination | Action |
|---|---|---|
| **Co-pilot live on the production demo**, Knowledge Hub only | [[portal-co-pilot]] | Recorded |
| **The evaluation harness is running** with Michael's personas | [[portal-co-pilot]] | Recorded at **#117** |
| **TXN's testing narrowed to three flows** before the demo | [[portal-co-pilot]], [[delivery]] | Recorded at **#115** |
| **Ian asked for assurance the agent cannot go rogue** | [[open-questions]] | New row **#123** |
| **George's answer: malicious personas on mock data**, plus *"one out of a thousand"* | [[open-questions]] | Recorded at **#123** |
| **The agent cannot add users or roles.** Stackworkz building it, TXN forcing it | [[permission-scoping]], [[open-questions]] | **#107** updated |
| **Two layers of validation**, MCP server then Control Center | [[permission-scoping]] | Recorded |
| **Permissions pass as a full list, not four buckets** | [[permission-scoping]], [[open-questions]] | **#107** corrected from 20-10 |
| **An AI-specific database on the AI node, outside DT's PCI environment** | [[architecture]], [[open-questions]] | Recorded at **#119** |
| A data lake as the eventual join point | [[architecture]] | Recorded |
| **Chat retention drops from 30 days to 72 hours**, aligned to the sandbox drop | [[portal-co-pilot]] | Decision recorded |
| **A second, sanitised long-term store with tool calls stripped** | [[portal-co-pilot]], [[open-questions]] | **#92** gets a mechanism |
| **Michael already runs the docs-improvement loop on his own Claude** | [[open-questions]] | Recorded at **#92** |
| **Ian: the first real question will not be in the test set** | [[open-questions]] | Recorded at **#92** and #117 |
| **Ian: the co-pilot is a shortcut to the docs, not a teaching tool** | [[portal-co-pilot]] | Recorded; read against #114 |
| **Containers make the cloud choice mostly moot**, VM fallback if needed | [[architecture]] | Recorded |
| **Azure Front Door may not accept server-sent events** | [[open-questions]] | New row **#124** |
| Michael owes the cost list and the ecosystem diagram | [[delivery]] | Open on Michael |
| **The DT hosting request is being held deliberately**, to specify it properly | [[delivery]] | Recorded at **#119** |
| **No per-user rate limit on the co-pilot yet** | [[open-questions]] | Recorded at **#97** |
| **Dörte: publish the odd questions as content**, as Monzo does | [[commercial]] | Idea recorded, no decision |

### Context, no action

| Finding | Note |
|---|---|
| **Novosapien's own note taker used for the first time** | Lily's work, and Dörte spotted it: *"I can tell Lily has taken over."* Brett: *"it goes into an area into your vault. Actions are pulled out, decisions are made"* |
| **Dörte wants to talk to Lily about it** | *"Lily, we need to catch up. Seriously."* She asked whether it is a company setup rather than *"the free cheap option as we do"* |
| Dörte distrusts Fathom's notes | *"I read the meeting notes from Fathom, I was like, blimey, have I been in a different meeting? I don't recall half of that stuff."* She rewrites them through Claude to her own style |
| The Novosapien bot left the meeting partway | George had declined Dörte's Fathom bot days earlier. *"It's got offended. It's like, don't talk about me"* |
| Ian joined a few minutes late | The call had just started |
| Brett was in the Cotswolds | A mystery tour with family, his mother visiting from South Africa for a month. Dörte's daughter has just arrived in South Africa |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Test the three agreed flows on the co-pilot | Michael | Responses and UI, before the demo |
| Report any UI or speed problems | TXN | *"Drop us a message. We'll get on to it like right away"* |
| Send the cost and usage list, and the ecosystem diagram | Michael | Ian already sent him the cost list |
| Ask DT about Azure Front Door and server-sent events | Michael | *"I'll send that question now"* |
| Prepare fallbacks before the Azure request goes to DT | George | So a no does not stall the work |
| Drop Knowledge Hub chat retention to 72 hours | Novosapien | From 30 days |
| Build the sanitised long-term store, tool calls stripped | Novosapien | The #92 mechanism |
| Build the malicious-persona harness for the Console agent | Novosapien | Ian's assurance request |
| Revoke the agent's ability to add users or roles | Stackworkz | Forced through the console by TXN |
| Send the last batch of targeting questions | George | Shorter than the call set |
| **Answer them by voice note**, WhatsApp or otherwise | Ian | *"We'll get that transcribed, updated, send you over the final versions"* |
| Prepare the demo | Novosapien | Window is 28 to 30 October |
| Catch up with Dörte about the note taker | Lily | She asked twice |

---

## Transcript

Oct 22, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:00**

**Max Kingaby:** Guests waking fab. No doctor's in.

**Dorte Dye:** Excuse me.

**Max Kingaby:** Hello.

**Dorte Dye:** Hello.

**Max Kingaby:** Oh yeah,

**Dorte Dye:** I'm all right.

**Brett StClair:** Oh, Novosapiennote taker.

**Dorte Dye:** My Fathomis still in a waiting room waiting.

**Brett StClair:** He's in the waiting room.

**George Westbrook:** What?

**Dorte Dye:** George declined me the other day. My Fathomnoteaker.

**Brett StClair:** Note, we've got a new thing. Novosapiennote take.

**Dorte Dye:** I can tell Lily has taken over.

**Brett StClair:** This is Yeah. H nice. It's the first time I've seen it in Hey,

**George Westbrook:** Hey, George.

**Brett StClair:** George's Fathom Noteaker. Deny

**George Westbrook:** Don't know it.

**Dorte Dye:** So, do you have it set up as a company one then? So, you're not going for the free cheap option as we do.

**George Westbrook:** custom

**Brett StClair:** custom.

**Dorte Dye:** Lily, we need to catch up.

**Brett StClair:** Custom.

**Dorte Dye:** Seriously.

**George Westbrook:** goes into an area into your hole.

**Brett StClair:** It goes into an area into your vault. Actions are pulled out.

### **00:01:12**

**George Westbrook:** This is so bad.

**Brett StClair:** Decisions are made.

**Dorte Dye:** Yeah,

**Brett StClair:** Very slick.

**Dorte Dye:** but I don't like the transcript that much. I was like, I'm always using it via claw to tailor it to the style I have. That that's the problem what I have because I read the meeting notes from Fathom.

**George Westbrook:** Yeah,

**Brett StClair:** Yep.

**Dorte Dye:** I was like, blime me, have I been in a different meeting? I don't recall half of that stuff.

**Brett StClair:** Custom notes. Our style, not Fathom style.

**Dorte Dye:** That's why I said Lily, we will catch up.

**Brett StClair:** Yes.

**George Westbrook:** it has been removed from the meeting though. Or is it hiding?

**Brett StClair:** What? Where is it?

**George Westbrook:** Yeah, it's amaz just got

**Dorte Dye:** I think you just wanted to decline me and then you take that out, right?

**George Westbrook:** offended.

**Brett StClair:** It's got It's got offended.

**George Westbrook:** It's like don't talk about me.

**Brett StClair:** How do we reinvite it? I think we're recording.

**Max Kingaby:** We're recording anyway.

### **00:02:04**

**Brett StClair:** We're recording anyway. Yeah. So, um, hello everybody. Cotswwells was lovely.

**Dorte Dye:** What? Why have you been in a cut?

**Brett StClair:** I did something called a mystery tour. And, uh, everyone has to answer questions to figure out where we're going throughout the weeks before. And then as we're leaving, everyone gets clues as to where we're going. And I do these stops on the way.

**Dorte Dye:** But it wasn't with the team,

**Brett StClair:** And then yes and that

**Dorte Dye:** it was with your family this time.

**Brett StClair:** one.

**George Westbrook:** We didn't get the invite.

**Dorte Dye:** I want to say you have such a social life at work and at home. It's like

**Brett StClair:** That's cuz my mom's art. So she's out from South Africa for a month. So got to give her some family love.

**Dorte Dye:** Sounds amazing. My daughter is in South Africa now.

**Brett StClair:** Oh yeah. Is she having fun?

**Dorte Dye:** She arrived yesterday. It was s\*\*\*\*\*\*\* down like hell.

### **00:03:05**

**Dorte Dye:** They wanted to go to the table mountain and went shopping and

**Brett StClair:** I was about to say the weather should be better now. Hey, it should be good.

**Dorte Dye:** yeah, they have a whole day of f\*\*\*\*\*\* today. But I shut up now. Let's work.

**Brett StClair:** Walk to I love talking.

**Max Kingaby:** I love talking for work as well.

**George Westbrook:** I wish you didn't.

**Dorte Dye:** You mean Max, not me, right?

**George Westbrook:** Uh, yeah, Max, give it give it a few more months, daughter. May May maybe so

**Dorte Dye:** Oh dear.

**Brett StClair:** Okay,

**George Westbrook:** updates. So on the testing of the agent um that should be on so the the what's it called? The co-pilot um should be on production now ready to let in it. Oh hello Good,

**Ian Johnson:** Hey, Sean. How you doing?

**George Westbrook:** good, good. Don't we,

**Brett StClair:** Okay.

**George Westbrook:** we we just started. So, um just saying the so the co-pilot that's that's on the the production um demo version at the moment.

### **00:04:18**

**George Westbrook:** So, whenever you got any spare time, feel free to test. Obviously, we're going to be testing a lot our end. Um got obviously got the automated test set up loaded in the personas. So, we're just running that, iterating on that, not not too much similar to the process mentioned on Tuesday. any UI issues that we see, any speed issues, be picking up on them. Um, if there's anything any of you find, just drop us a message. We'll get on to it like right away. Um, and then I suppose the that call yesterday we we had Mike with with Statworks, that was Yeah, that that was really good. I suppose all happy with the with the outcome.

**Michael Moores:** Yeah, a call with them afterwards as well. So they're they're pretty happy with that. So they're just going to work through a couple of ideas and stuff and obviously we spoke to them with Ian as well as Dorte.So all aligned and moving forward. So that's good.

**George Westbrook:** I think yeah because I was just conscious didn't really didn't want to give basically give because of us give them loads of extra work but it seemed like that was that they they weren't bothered at all and I think yeah that's going to it's going to work really well like we said we'll have the the first layer of validation on

### **00:05:26**

**George Westbrook:** the MCP server the second layer in the control center. So, we're catching any potential errors, no matter how small they would be, at at two points. I mean, it won't get through anyway. So, um it's perfect. Um so, I think yeah, there's

**Michael Moores:** The one thing we did um agree with them afterwards was that we'll be re revoking the ability to update a user to the agent credential.

**Dorte Dye:** Yep.

**Michael Moores:** So just to avoid that ability where you give yourself more permission and that that sort of stuff. So that's a change they're doing. So you can have access to everything the user does bar any user or role addition. We're going to force that through the console for that user just so we avoid that.

**George Westbrook:** Okay.

**Michael Moores:** You know what you hear about them going in and managing to change the permission to do something. Um so we actually enforcing on that side. So that's the only difference from from our conversation since

**George Westbrook:** Okay. So, there could be, let's say there's four buckets.

### **00:06:16**

**George Westbrook:** A user fits into one bucket, but they might have some custom permissions associated with that. And that would be that would be obviously overlaid onto the control center as well. So I think actually thinking about whereas before I thought maybe we get a variable which comes back to say they're in bucket one. What might be better is we get back their full permissions list and then given that um we turn things turn turn them off. So it mimics the console um or control center exactly rather than being like no we can only do it for these four buckets but that that should be fine.

**Michael Moores:** Yes.

**George Westbrook:** Um,

**Michael Moores:** Yes.

**Ian Johnson:** I think I was just going to say,

**George Westbrook:** okay.

**Ian Johnson:** George, just on this one thing, I think we just need you guys to give us some assurance that it's been properly tested, that this thing can't go rogue and do anything it's not meant to. We talked about it yesterday. I'm far from an expert. Mike's giving you one of the output things that we think is the protection, but I don't know, anything you guys can do just to make sure that we're not in a position where something goes and starts running havoc, then that would be great.

### **00:07:24**

**George Westbrook:** Yeah. Yeah. So, one of the approaches obviously make sure the code in terms of permissions they can't do that. Um, but also maybe things they do have access to similar process what we're doing with the co-pilot at the moment. We'll create the testing harness. We will unlock mock data as well. Um, we will create the most malicious personas that could ever be. they're trying to do this and do that. Um, so I mean there's bound to be one out of a thousand um where it is able to do something. Um, but we'll we'll stop that with that with this testing protocol. Um, because as we all know going through one person, one chat doing that is if it's is not high enough volume. Hence why we like to do the the uh yeah the a the agent speaking to agents.

**Ian Johnson:** Ju just just on the the co-pilot you said it's ready to test. Is that the we talking about knowledge or we talking about control center?

**Dorte Dye:** Love it.

### **00:08:20**

**George Westbrook:** uh knowledge hub.

**Ian Johnson:** Okay, cool.

**George Westbrook:** Yeah, because I think it's the I think the main three things would be well the main thing would be those those um flows that you mentioned, Mike. Um just making sure for for next week that they are exactly how you want them to be. Um both in terms of the responses and the way that the UI is functioning um so that we absolutely nail them. Obviously the changes we make to them going to carry over to the other workflows. Um but well the other test cases in in the background will be doing it with those personas that you sent over Mike with the with the different questions. Um but I think as a as a focus for for next week we make sure that the um those three because obviously appreciate you guys don't want to be going in and going through 40 50 different questioning styles and testing each one multiple times. it's like it's it's not feasible. Um so I think but by doing those three that would that would really really help.

### **00:09:20**

**Michael Moores:** Yeah, sounds good. Perfect.

**George Westbrook:** Um and I think the last thing is the or one of the last things is the the architecture the infrastructure stuff. Um so I've been looking into it. We've got a Yeah, I I suppose only one question would be is would do you know if we'd be able to use the Azure container container apps um because it's similar similar to Google Cloud running that it's got that scaling up scaling down or is there any kind of step choices and limitations that that that might be there that we that we should be aware of?

**Michael Moores:** Yeah, not that we're aware of. I still need to send you a list of Ian sent me a list of stuff we were getting sort of charged for so you can see what we're

**George Westbrook:** Yeah.

**Michael Moores:** already using as well.

**George Westbrook:** Okay.

**Michael Moores:** uh it doesn't mean too much to me or us, but I think at least you can see what we're already using,

**Ian Johnson:** Yeah.

**Michael Moores:** see if that aligns,

**George Westbrook:** Yeah.

### **00:10:10**

**Michael Moores:** and then if there's anything else we can ask DT specifically if we can use that, anything like that. So, I'll send that across to you and I've got the ecosystem diagram as well,

**George Westbrook:** Oh,

**Michael Moores:** send across.

**George Westbrook:** perfect.

**Michael Moores:** That's as much as we've got so far, but if there's anything specific,

**George Westbrook:** Okay.

**Michael Moores:** we can ask DT you directly as well.

**George Westbrook:** Yeah. Do do you know if you're using as your front front door as well at the moment?

**Ian Johnson:** Yeah.

**Michael Moores:** Uh definitely.

**Ian Johnson:** Wait.

**George Westbrook:** Okay.

**Michael Moores:** Yeah.

**George Westbrook:** Yeah. Okay. Yeah. Because I think there was there initially when we were looking we thought there might be there might be not an issue with using that but with the with the agents they they send server side events which sometimes as your front door doesn't like but we found a it's not a workaround it's a it's a a solution because obviously we don't want to be finding workarounds when it comes to infrastructure.

### **00:10:55**

**George Westbrook:** um we want to make sure that we're doing it the proper way. Um but we know we know what we'd need to do in that in that instance and maybe it's just getting once we send it over to DT there might be a few questions for them in terms of are you able to do this? Are you able to do that? Blah blah blah. Um and making sure that if that's not the case that we've we've got a fall back so that if they say no, we're not sat there thinking uh what we going to do.

**Michael Moores:** Yeah. Yeah. I know definitely the front doors across the front of the API already. So the nodes sort of sit to the side, but they are sort of governed by the same uh the same thing assuming they're putting them where the rest of the stuff sits basically. So yeah, I'll send that question now and then um if there any questions we can get that in front of them early early doors and then at least we have a clear direction to give them when we're ready.

### **00:11:42**

**George Westbrook:** Okay,

**Michael Moores:** Jesus.

**George Westbrook:** perfect.

**Ian Johnson:** Have you got it stood up in Azure? Are you going to stand up in Azure? I'm just thinking about moving forward. How are you going to make sure that this thing works in the infrastructure that you're planning for us to ask DT to put in place?

**George Westbrook:** So, at the moment, we've got it all in in GCP, but it's all all containerized. So, we're using Docker containers. Um, and with with that, it's kind of plugandplay. It's a Docker container is a Docker container. Um we could put it on AWS, GCP, Azure and it's going to look feel act exactly the same. Um there's different there's different configuration settings like say for example I think uh GCP the m um request time can be 300 seconds and on Azure it's 240\. We're never really going to have that issue. Um or the way that it breaks up the CPU or the RAM is maybe it's in increments of one and a half instead of one. Um, so with with container apps, it's Docker container.

### **00:12:46**

**George Westbrook:** Um, put that in, scales up, scales down. Um, if we're not able to use um, container apps and it has to be something that's a bit more VM based, same thing. Get into the VM. Um, make sure Docker's installed. Um, load in the image and it's going to be so it doesn't matter if we're testing our machine on GCP or on Azure. Um, it's going to it's going to work the same.

**Ian Johnson:** Okay, one last point for me. And I can't remember where what the outcome of it was, but we did talk about particularly on the knowledge of it's relevant to the control center making sure that we had something that managed um the workload to make sure that we weren't getting it getting into a situation where this thing was exploding from a cost perspective.

**George Westbrook:** Yeah. Yeah. So, I think there there obviously things we we we've thought about. Um our priorities at the moment have been right, let's get the the look, the feel, how it's speaking sorted.

### **00:13:46**

**George Westbrook:** Um because that stuff in terms of say rate limiting um we we can deal with because there's going to be a a way we can identify a user and given given that user what are they what are they doing? Um are they sending a thousand requests per second? Well no they're not going to be able to the max is going to be whatever maybe two three five. Um so there's ways in which we can limit that. Um I think the yeah the only thing I think might in terms of the the architecture while I while I remember is the so it's not so relevant for the for the knowledge hub I couldn't foresee it being a problem is in terms of storing the data around the agent um so for the knowledge hub obviously it's not it's not sensitive data um the questions well it's not as sensitive data they're asking questions the tool results um the tool call results um it's it's information that's in in the knowledge hub. The only one would be with the with the control center.

### **00:14:46**

**George Westbrook:** Um obviously you mentioned previously that you the approach of storing data maybe per tenant stuff like that. So we might need to think about um or get more of an understanding about how that data is stored. Are we able to um put the traces? Are we going to have to put the traces for the agent within certain locations um depending on where where the where the tenant is? So does that mean we need access to update the schema of certain databases that exist or do we isolate them um so it's just an AI database so that it's not touching any of their current data because in in the control center there could be sensitive data and we make a talk call we get back the result um and in order to manage the chat history we're going to have to we're going to have to store that store that data um so it's just a matter of where your pre preference would be um as to where we store that be it isolated an isolated database or the one that you're currently using.

### **00:15:47**

**Michael Moores:** Yeah, I think obviously we've got a database per uh program manager or TXN client basically. I think that is governed under DT's PCI environment. So, be careful there about where we put that in. So I think there'll be push back from DT on putting that in there. So potentially, you know, having a database on that node for the AI specifically might be the best way to go obviously. Um we will also have a data lake as well where all of this will eventually feed back in as well. So I think that's where the data will connect back together. So I think we just need to take a think about that and have a look. But I think it'll probably be AI specific database away from the PCI

**George Westbrook:** Yeah.

**Michael Moores:** stuff. Um, basically

**Ian Johnson:** How how long how long are we planning it?

**George Westbrook:** Yeah.

**Ian Johnson:** So I think like that's right anyway. Just um but how long are we planning on retaining data that's in the chat?

**George Westbrook:** So for the for the knowledge hub it well for all of them it could be whenever

### **00:16:44**

**Ian Johnson:** Yeah.

**George Westbrook:** it could be a day it could be 30 days. Um so I suppose that decision kind of kind of sits with you guys um in terms of how long do you want it stored? Do you want it stored forever? Um because there's with storing it for a longer time, there's extra functionality um that that we could add in um in that searching through previous tracks, drawing maybe user preferences or certain actions that are taken a lot. Um be it I don't know, maybe there's things you can do with if you store the data forever. Um but obviously appreciate that there's some instances where you you don't want to be storing it forever. Maybe it's 30 days. So something like the knowledge hub, I think 30 days is a good good good target. Um most of it's going to be stored, correct if I'm wrong, Hassan. Um in in the browser um because they're not long that I can't foresee them being chats which consume a lot of a lot of memory with 50 to 100 calls whereas the agent um in the console um although it appears it's doing one to talk call behind the scene it might be 10 or 20\. Um I think they were those speed speed bumps that we've got like say say for example investigating a decline previously why it was taking so long was if there was 50 declines it would call one after another

### **00:18:05**

**George Westbrook:** after another now all in parallel so it's it's it's a lot quicker um that was a bit of a ramble appreciate um but yeah knowledge hub we don't even have to store them um but it might be a good idea to store them um the the agent. I think that's that's up to you guys. I think if it's flexible

**Michael Moores:** Yeah, I think we need to have a thing in on the the data retention side. I do know that we from a public sandbox point of view will be dropping the data in there every 72 hours. So just in case there is personal data in there. So we just need to be cautious that if we reuse a chat for a command that there anymore. So that's the the one thing we have decided on there just because whilst it's a public sandbox al we discussed about doing a isolated one later behind login wh it's fully public whilst we tell people not to put you know real data in there could do and we don't want to store that so we've come with 72 hours meaning you can go

### **00:19:02**

**George Westbrook:** here.

**Michael Moores:** away come back the next day and still test and check check that but it's not so longterm storage so that's why we land on the 72 hours there I think we just need to consider Huh?

**Ian Johnson:** I think I think that's perfectly fine.

**George Westbrook:** It's

**Ian Johnson:** I think um because correct me if I'm mistaken, but theoretically there's nothing stopping somebody from from copying and pasting the response that's in a chat into whatever they want to paste it into.

**Michael Moores:** Yeah.

**George Westbrook:** Yeah.

**Ian Johnson:** So, if it's not, if it's not, it's f it's fine. What I'm thinking about is I'm trying to think of the scenario where I'd want to come back like 70 I don't know 48 hours later to find something that I've just asked the question about on the knowledge hub because it's really the idea was there was to it's to enable them to do the thing that they're looking to do rather than build up their knowledge of card programs. if they want to build up their knowledge of car programs, then to me that's a case of well, if you can copy what the response is, um, put it somewhere that you can keep it because it's only meant to be effectively a shortcut to reading all the docs and deciphering it yourself.

### **00:20:27**

**Michael Moores:** Watch

**Ian Johnson:** So, nothing's being moved from them. the source material is still there in terms of how we answered their uh query. So I think we just need to think I mean I think 72 hours is more than feasible. Bear in mind we've gone from a position where most people don't have anything or if they do it's not very

**George Westbrook:** Yeah.

**Ian Johnson:** good to okay we've got something we think is really good and it'll still be there 72 hours later seems more than fair to me.

**Michael Moores:** Yes.

**George Westbrook:** Yeah. Yeah. Cuz I think at the moment we got it 30 days for the knowledge hub. drop that to drop that to 72 um for anything that's being stored. Um and I suppose so I can't imagine there'd be any issues if let's say they're using the the knowledge hub MCP um that data is going to be what it's only really going to be um information about the docs I suppose that's stored. So that's not that's not too much of an issue, is it?

### **00:21:28**

**Michael Moores:** Yeah, I think for for certain for MVP obviously we keep it the same. There's no issue with having a chat that's longer than the data that exists as well. Obviously we can look at that if we want to, but I think aligning that means that you know if that chat ends the data is also gone. So I think that's that's fine from my side as well.

**George Westbrook:** One actually one one thing I'm thinking of is in terms of so let's say you've got loads of users asking loads of questions how do I do this how do I do that in the in the knowledge hub um obviously it's providing value for them they're learning they're understanding but also it's very very valuable for you guys in that every once in a while looking at the chats being like okay what What questions are people asking? There's this one question everybody asks about two or three turns into a chat. Everybody's asking maybe we need to update the docs. So is there a kind of middle ground wherein when we it's being stored longterm we strip out any tool calls that are going to hold anything um that so potentially sensitive data um but retaining the data that that's valuable for all of us in terms of improving be it the docs the experience or any aspect of TXN

### **00:22:41**

**Michael Moores:** Yeah, I think that that works for me. Obviously, I think yeah, the the sensitive data is the is a key there. So, I think removing that means we can store as long as we need. I think you got good point there in terms of learning. Obviously, we're doing the same from a a ticket side as well. So, you know, we want to sort of collect that all together. So, we can have a look at who's asking the questions on the knowledge hub. You know, from a a production point of view, we'll be also looking at what tickets we get in there as well. How can we add that back in?

**George Westbrook:** H.

**Michael Moores:** And ultimately, you know, I've built it out right now, but have like a doc improvement thing to say, you know, we've seen these questions highlighted.

**George Westbrook:** Yeah.

**Michael Moores:** That's something we can go with yourselves obviously to say, you know, extend this to say this is what we think and actually raise that and ultimately you could do it as a draft as well.

### **00:23:22**

**Michael Moores:** So I think what right now obviously doing on my my own claw but I think that's somewhere we could go from a a full suite perspective to actually build it to the the bot itself and self-improvement as well. So I think that's makes sense to me.

**Ian Johnson:** You beat me to it, George. That was the thing that just crossed my mind is if we only got two hours, how do we make sure that we're getting better with time? But we we we've given a set of sample questions, but I can guarantee the chances are the first one probably is not on that list.

**George Westbrook:** Yeah, somebody asking about how do I make spaghetti bolognese for dinner? Something like that. I I always do find that fun going on to a support or co-pilot or something like that and asking it random random questions to see what it does.

**Ian Johnson:** You single George

**George Westbrook:** Am I allowed to swear on this meter?

**Ian Johnson:** far away. What do you do for fun?

**George Westbrook:** Yeah. Yeah.

### **00:24:25**

**George Westbrook:** AI stuff. Unfortunately, as a as a sad bastards,

**Ian Johnson:** Lily, don't stand for that. I got I don't know or Lily well enough, but I can say the three of you are.

**George Westbrook:** I'm taking that as a compliment.

**Ian Johnson:** Yeah, you go for it, mate.

**George Westbrook:** Yeah.

**Ian Johnson:** We're glad we're glad that you are.

**George Westbrook:** Positive mental thinking. Yeah.

**Ian Johnson:** We're glad that you're although we will check to see if

**George Westbrook:** Yeah. Um,

**Ian Johnson:** anybody asks how do you make spaghetti bolognese on the first day we go live the sure but it won't take very long to track down the perpetrator to be honest

**George Westbrook:** yeah. Musical George Westbrook is asking how to make Italian cuisine.

**Dorte Dye:** I think we should put that in one day a week our co-pilot does something funky.

**George Westbrook:** Yeah. Yeah.

**Dorte Dye:** So like Monzo has a LinkedIn account with these from fancy tech where everyone is talking about.

**Ian Johnson:** or the questions they got asked.

**George Westbrook:** Yeah.

**Dorte Dye:** No to find someone for George.

### **00:25:30**

**Ian Johnson:** I think I think Georgeis more than capable. We just needs to step away from his computer.

**George Westbrook:** No,

**Ian Johnson:** One more.

**George Westbrook:** that's the only relationship I need.

**Michael Moores:** What the f\*\*\*?

**George Westbrook:** Nonsexual, obviously.

**Ian Johnson:** Okay. Have we got any more orders of business before this thing goes completely off the rails?

**George Westbrook:** Yeah. Um, so I think it's we'll keep on looking into the uh the infrastructure stuff. Um, might when when you can send over that info you talked about that be that' be amazing. Um, obviously taking what you said the other day and that we don't want to rush it. We want to make sure it's well through who hence why we haven't sent something over um already. Um, testing on the knowledge hub co-pilot. just those three questions, any any feedback you have. Obviously, we'll carry on our testing. Um, ICPS by personas, all that stuff. There's going to I think we mentioned yesterday, there might be one more email with some quicker questions. Um, I think the easiest way just if you just want to send us a voice note, um, be it on WhatsApp or whatever. Um, we'll get that trans transcribed, updated, send you over the final versions. um examples of um messaging um that we'll need to tweak, refine, things like that. Um obviously in boxes warming going ahead um and yeah and preparing for that demo next week.

**Ian Johnson:** All good.

**Michael Moores:** Sounds good.

**George Westbrook:** Perfect.

**Ian Johnson:** Cool. Have a good evening when you get to it, folks.

**Michael Moores:** Cheers.

**Dorte Dye:** Thank you.

**Michael Moores:** Take care.

**Ian Johnson:** Cheers.

**George Westbrook:** Have a good one.

**Michael Moores:** Bye.

**Ian Johnson:** Catch you later. All right. Bye.

### **Transcription ended after 00:27:30**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*