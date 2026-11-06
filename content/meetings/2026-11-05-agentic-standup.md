---
date: 2026-11-05
type: standup
description: "DT say the AI hosting cannot be ready for launch, so Novosapien stand it up in Azure by 10 November to time it; the Console co-pilot is demoed"
scope:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[co-pilot]]"
  - "[[permission-scoping]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[co-pilot]]"
  - "[[permission-scoping]]"
  - "[[open-questions]]"
  - "[[index]]"
  - "[[2026-11-03-dt-demo-and-infrastructure]]"
  - "[[2026-11-03-agentic-standup]]"
---

# TXN: Agentic AI Standup (2026-11-05)

> **Source:** Gemini transcript, 5 November 2026 (a Thursday), recording ends at 35m 30s. **Novosapien:** George Westbrook, Brett StClair, Hasan Ahmed. **TXN:** Ian Johnson, Dörte Dye, Michael Moores. Michael joined a few minutes in, from a call with DT; Ian joined around the ninth minute.

## DT say the hosting cannot be ready for launch

**Ian reported where DT are, two days after the demo:**

> *"We passed them the document that you gave to us... 27th October, and **they haven't done anything with it** would be the first thing to say, and Pete's opening gambit was **we don't think there's any way we can get that stood up to support a go-to-market launch on the 17th**."*

**And DT say they did not know.** Ian: *"somehow DT have missed the fact that the AI is a crucial part of going to market with the knowledge hub... They also made reference to the fact they didn't know that AI needed to be part of the go to market launch, which I don't think it's true either."* Dörte: *"It's not true."* Ian: *"unless it's tattooed on your forehead... they kind of don't get it."* DT are now working out how long it would take them.

**Ian's position:** *"the task in hand is that we need to make sure we can get the AI deployed, tested as part of the knowledge hub launch. Otherwise, we can't really do it given the fact that it's a key part of our messaging. So **not a lot of choice really**."*

**Dörte's read on why DT are slow to see it:** the Knowledge Hub is new to them, because *"all the APIs are consumed by one customer. They're not visible."* The Console is the operational side DT know, and that is where they lit up on 3 November.

> [!warning] Launch date: Ian says the 17th, the vault says the 16th.
> Ian said **17 November** on 3 November and again here, quoting Pete. Every earlier record says **16 November**. The vault keeps the 16th until it is confirmed, and the question is with George.

## Novosapien will stand it up in Azure by Tuesday, and time it

**Ian asked the question that matters:** *"You guys have not spun this up in Azure, right? You've just told us what you think it needs to be in... So you don't actually know if it will work in Azure the way that you've designed it."* George: *"It will."* Then the offer: **"We could have a version running in Azure to fill you with confidence"**, by Monday or Tuesday.

**What Ian actually wanted was the timing, not the proof:**

> *"If you take away the actual doing of it then what you're left with is just process, so there's less of an argument... **if we can actually say, well, we've stood it up with Novo in exactly the way we're asking you to stand it up**, then it will just help if the conversation gets tricky. Well, not, it will get tricky."*

**The plan:** start tomorrow, block out time to do nothing else, and report how long it took. Brett guessed seven hours. **George's caveat:** it is not a like-for-like test, since DT have locked-down existing deployments, and ingress and egress to their services; Novosapien could mock some of that. Ian: *"Don't go too far with it... it's just the challenge that we can raise them."*

### Container Apps against DT's Kubernetes

The deployment plan is **Azure Container Apps**, the Cloud Run equivalent. **DT run everything else on AKS.** George had expected Container Apps to be the sticking point, and DT called nothing a blocker on 3 November, *"I don't know if they were just plucking out of their ass, pretend that they'd read it."* The remaining blocker for the Knowledge Hub is **a DT-approved environment, including the data and the database**. See [[architecture]] and #49.

## The code passes Stackworkz's standards check

The first migration into Stackworkz's branch ran without the standards. **Novosapien are now aligning the code to them**, so the standards have arrived. The check passes at 80 percent and **the code scores 82 percent**: *"if we did nothing else, it's going to be passing."* It then goes into Stackworkz's build pipeline, with the AI services connecting to it.

George's read on DT's approval: DT will probably treat it as Stackworkz code, so *"as long as it passes the coding standards and coding guides then it should be all good."* That is a guess, and it is the thing #125 was about.

**Agent authentication does not block the Knowledge Hub**, because the Hub has no permissions to manage.

## Permissions: built now, from Michael's document, with a harness

**Stackworkz have not come back on agent authentication.** Michael will chase them tomorrow.

**Novosapien will not wait.** George: the agent access layer sits underneath, with the Console co-pilot and the Full Agentic Experience on top. Work starts now from Michael's permission layout document, *"subject to change a little bit, which is completely fine"*: turning tools on and off, and changing skills by access level.

**And a permission test harness**, the same idea as the Knowledge Hub's with more detail:

> *"There'd be the user with their permissions with the workflow from the human's perspective. Then **the tools that we would expect to see** during that workflow and **the tools that we would definitely not expect to see**. The not expecting to see is one where **even if it thinks about calling it there's an issue**, because it shouldn't even really know of its existence."*

So the test is stricter than refusing a forbidden call: a forbidden tool must not appear in the agent's reasoning at all. George's reason: it replaces a UAT process of *"picking a workflow, picking a user access level, thinking about how it should work."* Michael: *"That sounds great."* **This is the first concrete method behind Ian's request** that the agent cannot go rogue (#123), and it still has no pass mark. See [[permission-scoping]].

## The Console co-pilot, first working version

**Hasan demoed it**, without rehearsal: *"this might not be as smooth a demo because we haven't been practicing for hours like we did for the other one."*

- **Navigation:** *"take me to the transactions"*, and it goes there.
- **Page awareness:** it sees what is on screen, so *"tell me about this page"* gets an explanation. **One attempt failed** live, on the cards page.
- **Records:** *"take me to"* a named cardholder, through a tool call.
- **Mostly question and answer for now.** Actions with an approval card, such as cancelling a card, are not added yet.

**George on how it differs from the Full Agentic Experience:** a similar look and feel, but **no generative UI**: rather than rendering components in the chat, *"it's going to take you to that screen"* and act there. **What comes next is memory across the session**: where the user has been and what they did, so that if someone *"three steps ago... took this action on Priya, now they're trying to cancel a card, but she's on the dashboard"*, it can take her to the right page. *"That true co-pilot that's kind of looking over your shoulder."* Michael: *"Yes, that was great."* See [[co-pilot]].

## Corrections to 3 November

- **His name is Billy, not Villi.** Ian: *"It's not Willy, it's Billy."* Ian met Billy and Peter (Pete) in South Africa. The 3 November pages, [[architecture]], [[delivery]] and #127 are corrected; the transcripts are left as they are.
- **Ian does not think Billy's questions gate anything.** *"What that was was just an AI pissing contest... It had nothing to do with what the task in hand is... I'm not sure any questions are coming from him that actually are anything to do with DT."* No questions have arrived. #127 recorded those questions as gating DT's design; it is revised to say that what gates the hosting is DT not having started, and the masking question is kept for the Console.
- **OKF, more precisely.** George: *"we're not using the exact format, we're using a different permutation of it."*

## Context, no action

- **Michael ran out of Claude usage** on Tuesday night. TXN's skills and knowledge sit on his account, and the PayCorp SSO stops them using a service account without switching SSO off and on. TXN's own tooling, not Novosapien's.
- **Brett sent Dörte a guide** on folder structure for her SharePoint set-up, with instructions to follow.
- **Brett is sorting the flight plan.**

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| DT: no way to stand it up for launch; had done nothing with the documents; say they did not know AI was in launch | [[delivery]], [[open-questions]] #119 | Callout added; row updated |
| Novosapien stand it up in Azure by Tuesday 10 November and time it | [[delivery]], [[architecture]] | Callouts added; open action |
| Container Apps against DT's AKS; DT-approved environment with data and database is the blocker | [[architecture]], [[open-questions]] #49 | Callout added; row updated |
| Code at 82 percent against an 80 percent standards check | [[delivery]], [[open-questions]] #125, #111 | In callout; rows updated |
| Agent authentication does not block the Knowledge Hub | [[delivery]] | In callout |
| Permissions built now from Michael's document; harness with expected and never-expected tools | [[permission-scoping]], [[open-questions]] #107, #123 | Callout added; rows updated |
| Console co-pilot first version: navigation, page awareness, Q&A; no actions yet; no generative UI; session memory next | [[co-pilot]] | Note added |
| Billy, not Villi | 3 November pages, [[architecture]], [[delivery]], [[index]], [[open-questions]] | Corrected |
| Ian: Billy's questions do not gate anything | [[open-questions]] #127 | Row revised |
| Launch 16th or 17th | [[delivery]] | Flagged again, sent to George |
| Claude usage, SSO, SharePoint guide, flight plan | n/a | Context, no action |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Stand the Knowledge Hub AI up in Azure and record how long it took | Novosapien | Start 6 November, done by Tuesday 10 November |
| Chase Stackworkz on agent authentication | Michael | 6 November |
| Build tool and skill gating from Michael's permission document, with the permission harness | Novosapien | Not dated |
| Add actions with approval, and session memory, to the Console co-pilot | Novosapien | Not dated |
| Confirm the launch date, 16 or 17 November | George, with TXN | Before launch |

## Transcript

Nov 5, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:16**

**Brett StClair:** And if you ready to demo

**George Westbrook:** iPod as well.

**Brett StClair:** Fancy seeing you again. Has anyone else got internet problems?

**Dorte Dye:** I did.

**Brett StClair:** I do. Ah, there we go. Hello.

**Dorte Dye:** But I guess because you had internet property,

**Brett StClair:** That's But I guess

**Dorte Dye:** you could have let me in.

**Brett StClair:** that's really weird how it Oh, wait. My thing is doing the craziest things at the moment. Hold on. There we go. Now I can hear you. Did the guide help, by the way?

**Dorte Dye:** I was just looking at it. Fancy you and your html.

**Brett StClair:** I tried.

**Dorte Dye:** It's interesting because folder structure I I've done something similar of how I set up SharePoint and then I was like not sure if it's working and I tried to find different models. It's like whatever. I think the main thing for me is I'm going too much into the low-level detail and that just complicates stuff. Just keep it all in one and that's it.

### **00:01:41**

**Brett StClair:** I forgot to add one thing was for your um I remember what it's called now. Um let me see if I've got it here. I'll send it in a separate folder. Um oh let me pull it up. can't remember what it's called. Brain dead. Uh instructions to help you with that.

**Dorte Dye:** Okay,

**Brett StClair:** I'll send you through just how to get that done properly. Um and I think that should work.

**Dorte Dye:** amazing. Just checking what's with Mike.

**Brett StClair:** Um I'll tell you what

**Dorte Dye:** He seems busy.

**Brett StClair:** Mike's doing.

**George Westbrook:** What's this?

**Brett StClair:** He's busy creating more skills.

**Dorte Dye:** No, he's very busy with um the UAT stuff.

**Brett StClair:** Ah, yes.

**Dorte Dye:** He's just texting. Oh no, it's a lot. Um he blown his whole credits yesterday and he has done

**George Westbrook:** That's it.

**Dorte Dye:** everything about automation. This is the upper thing, right? He's using the different models for the different tasks and he has built so many workforce sub many agents.

### **00:02:54**

**Dorte Dye:** It's not like me. I mean it's like it's amazing. Yeah. He's he's on um on a call with us DT at the moment.

**Brett StClair:** Um, we can always push it out a bit when he's free. I don't think we have anything that we can't push back a little bit after this. Um,

**Dorte Dye:** That's fine.

**Brett StClair:** I guess the key things was really just to kind of walk through a little bit where we are with the co-pilot on the console and then just talk about getting some facetime with the uh, stack works guys around authentication and DT around infrastructure. Hey guys.

**George Westbrook:** Yeah. Yeah. I think it was so in terms of the co-pilot um got like a first visual visual version um which obviously we'll be we'll continue to be working co-pilot for the console as well.

**Dorte Dye:** Thank you. That was my head like what?

**George Westbrook:** Um yeah I I saw your face and that was uh wait we're still working on the the knowledge hub one.

### **00:04:04**

**Dorte Dye:** No, we changing the knowledge hub.

**George Westbrook:** Yeah.

**Dorte Dye:** No, I was just thinking um DT is onlying you some questions for the infrastructure. So we what would be really helpful and they're really slow with that kind of stuff that they collect their thoughts, send a question over and then there's a follow-up meeting rather than follow-up meeting and then they're not prepared again.

**George Westbrook:** Yeah.

**Dorte Dye:** At least it gives them some time. Hi Mike, you're mute.

**Michael Moores:** Are you okay?

**George Westbrook:** heard you hit the dreaded point in the week where you run out of uh claw usage.

**Michael Moores:** That was Tuesday night. Yeah.

**George Westbrook:** Cheers. I keep happening to me as well. You're like, you see that 80% has been already been used this week. You're like, s\*\*\*, it's on it's a Monday or a Tuesday and I have to wait until Friday to reset.

**Dorte Dye:** So what are you doing then actually George if that happens to you you're getting on this

**George Westbrook:** use another account that is

**Dorte Dye:** nerve I mean Mike and I discussed it but because he has built everything on his account because we have

### **00:05:07**

**George Westbrook:** yeah

**Dorte Dye:** two extra licenses but we can't use because all the knowledge is attached to his pound as I

**George Westbrook:** god. Yeah, that's yeah that's that's where that's where it is a that's where it is an issue. Um I think cuz in terms of how we navigate say obviously in skills it's in a marketplace so it's everyone can use it but when it's like say anything scheduled tied to your clawed account with all your all your connectors and it's trying to move them across is yeah I can imagine that is a nightmare

**Dorte Dye:** can do a marketplace with code.

**Michael Moores:** Yeah, we've got one already.

**George Westbrook:** with

**Dorte Dye:** Oh, we got one already. And that wouldn't work if you have the marketplace. You just use another license and use the same.

**Michael Moores:** Yeah. So, got log out my desktop. There's a problem in all my open chats.

**Dorte Dye:** Okay,

**Michael Moores:** Um, and plus we can't use SSO on our other account. So,

**Dorte Dye:** that is true.

**George Westbrook:** Uh

### **00:06:00**

**Michael Moores:** Yeah, we've got a service account that we can't get in because the SSO from PayPal. They won't let us log in with that service account obviously. Um, so that's running a lot of our stuff, but I have to turn off SSO, jump on, change stuff, and then turn it back off, which is not ideal.

**George Westbrook:** oh god. God.

**Michael Moores:** Uh, so it's definitely not feasible to keep using and swapping.

**George Westbrook:** Yeah, it's I think there's I I think I've seen somebody on um on Twitter where they built something where you can have like two or three accounts and as soon as the usage is going low, be at the 5h hour limit, which isn't there anymore, it will switch accounts automatically. But obviously that's not incorporating things like SSO into it. It's just for people using the um the normal accounts.

**Michael Moores:** Yeah, I've got the uh separate profile on my laptop, but it's a you'll see. So, I've got my Chrome logged into my own account. Having to do incognito to try and log in is just a night.

### **00:06:56**

**George Westbrook:** Don't um but yeah, we were what was it we were just saying? So the the co-pilot, Mike, we've got the co-pilot in the console. Got a first working version of that which we'll be we'll be iterating on. Um, and I'm assuming we'll have time today. We can we we can just go through that quickly. Um, the has there been any updates from Statworks on the agent agent authentication kind of idea that they were they they were were working on?

**Michael Moores:** Not yet. No. Um, I can chase them again. We'll do to speak to them tomorrow.

**George Westbrook:** Okay.

**Michael Moores:** Ask them.

**George Westbrook:** Yeah. Because I think because in terms of the so obvious the agent access layer that's obviously the agent access layer on let's call it along the bottom and then the the console co-pilot and the um the full aentic experience obviously sit on top of that. um it's not a block of the agent um authentication because obviously we've got our unauthenticated version unauthenticated because obviously it's on our um what's it demo version um but when it come what we'll be working on well from now or building on top of is all of that permissions stuff.

### **00:08:14**

**George Westbrook:** So even though there's not going to be the the call it the stack work side of things which is going to be passing the permissions through um we've got we've got that document that you sent I think it was a few weeks ago regarding the permission layouts and things like that which I appreciate might be subject to change a little bit um which is completely fine but we'll be just be working on the mechanisms of turning the tools on turning them off um how the different skills are going to change based on the different user access levels Um and then building the building the testing harness for it as well.

**Michael Moores:** Yeah.

**George Westbrook:** So similar process that we went through with the knowledge hub just with a bit more bit more detail. So where the there' be the user with their permissions with the workflow from the call it the humans perspective. Um then the tools that we would expect to see during that workflow and the tools that we would definitely not expect to see um the not expecting to see is is one where even if it thinks about calling it there's an issue um because it shouldn't even really know of its existence.

### **00:09:20**

**George Westbrook:** So it'll be a good way for us to to make sure that it doesn't even understand that it could call this tool um even if it's not meant to. Um so work on that so that like we said before there's not this UAT process which we're all having to go through of picking a workflow, picking a user access level, thinking about how it should work. Um it will bootstrap it a lot.

**Michael Moores:** That sounds good. Um, yeah, that sounds great. Thank you.

**George Westbrook:** Perfect. Then the Yeah. So then we mentioned the the infrastructure the infrastructure with with DT where we'll need to get get those questions. Obviously we'll get back to get back to what was his name? Was it Willie? The the guy who said he would send through the send through the questions. Brett's trying not to make a joke there. I can tell.

**Brett StClair:** Billy,

**Ian Johnson:** It's not Willy, it's Billy.

**George Westbrook:** Oh, Billy.

**Ian Johnson:** Billy. I bet should know given he's the he's South African,

### **00:10:17**

**Brett StClair:** don't call him Willie.

**Ian Johnson:** but it's Billy. I mean, honestly, you wouldn't call him that if you saw him because the bloke is freaking massive. So, there's two people. There's Billy and Peter who I met in South Africa and I went like that when they walked into the room. They are gigantic. Peter's an ex like kind of proper professional rugby player, dude. He's m he's huge. He's like a building.

**Brett StClair:** Is that pizza bur?

**Ian Johnson:** Yeah, he's Yeah.

**Brett StClair:** And his name is Bur. I mean that's brilliant.

**Ian Johnson:** Say no more. They He played on He played on a provincial team that beat the Lions. That's all I'll say. So there you go.

**George Westbrook:** Okay, Oh,

**Ian Johnson:** Yeah,

**George Westbrook:** right.

**Ian Johnson:** exactly.

**George Westbrook:** Make sure make sure to be extra nice next time we speak to them.

**Ian Johnson:** Exactly. And he's one of the nicest people you could ever meet because we've given him plenty of calls to be able to get slightly annoyed at us, but he never does.

### **00:11:07**

**Ian Johnson:** Um, so we haven't had the questions from Billy yet.

**George Westbrook:** Okay. Yeah,

**Michael Moores:** Yeah,

**Ian Johnson:** We all Okay.

**George Westbrook:** that's

**Michael Moores:** if I see them

**Dorte Dye:** easier.

**Ian Johnson:** Well, we Okay. So I don't know how but some somehow and I don't know what your view is but somehow DT have missed the fact that the AI is a crucial part of going to market with the knowledge hub um which it is. So uh they are now off to scurry around to find out how long it will take them to stand up the uh environment that's required. I think the questions that Vinnie was asking, um, they were they really about the infrastructure or

**George Westbrook:** No, there was there was it it seemed like he was more interested on the process of because there were some of the questions he were ask he was asking I was like well I wasn't wasn't expecting those sorts of questions um but then we were looking at him after he's like the head of research at some AI AI thing um and but the questions you asked him were really really good um I think one of the ones which initially we were unsure of was for the knowledge base so we're using OKF format open knowledge format um which we we're not using the exact format we're using like a different permutation of it.

### **00:12:31**

**George Westbrook:** Effectively all it is is just you have a file with metadata so that the agents can search it properly. Um and I think cuz he was he was interested in are we using a vector database what like for the vectors what dimension we using which we're not.

**Ian Johnson:** Co cover your ears,

**George Westbrook:** So

**Ian Johnson:** Lily. What that was was just an AI pissing contest. That's all it was. It had nothing to do with what the task in hand is. Nothing at all. So, you know, just let that stuff write. I'm not sure any questions are coming from him that actually are anything to do with DT it where we are is we passed them the document that you gave to us I don't know couple of weeks ago Mike 27th

**Michael Moores:** the 27th October.

**Ian Johnson:** so yeah whatever um and they haven't done anything with it would be the first thing to say and that Pete's opening gambit uh was we don't think that we can there's way any way we can get that stood up um in to support a go to market launch on the 17th.

### **00:13:41**

**Ian Johnson:** Now I am not as you have already gathered I am not a technologist by any stretch of imagination but I thought spinning stuff up in the cloud in Azure and Google and freaking Amazon was supposed to be easy and

**Dorte Dye:** seems done.

**George Westbrook:** That would be our impression as well.

**Brett StClair:** Oh, though I do have a story in Absa and Barclays Africa where they had got it down to a point where to spin up stuff in Amazon took six months.

**Ian Johnson:** Yeah. Now I can imagine that there's some DT is like kind of I can imagine there's some process stuff that is part of the issue. So he's talking about getting through in for ops etc. I have a question for you. You guys have not spun this up in Azure, right? You've just told us what you think it needs to be in.

**George Westbrook:** Yeah.

**Ian Johnson:** Okay. So you don't actually know if it will work in Azure the way that you've designed it.

**Brett StClair:** Oh boy.

**George Westbrook:** Um, it it it will I tell you I tell you what I tell you what we can

### **00:14:49**

**Ian Johnson:** Okay.

**George Westbrook:** do by Monday or Tuesday.

**Brett StClair:** By Monday, we could have

**George Westbrook:** We could have a version running in Azure to fill you with confidence.

**Ian Johnson:** That's what I was about to ask you.

**Brett StClair:** Yeah.

**George Westbrook:** Yeah.

**Ian Johnson:** What you've got to realize is the bit about the fact you haven't tested it was not really the bit I was driving at. What I was asking you in a roundabout kind of way was would you mind spinning up an as your environment and sticking in there to make sure it works.

**Brett StClair:** Yes.

**George Westbrook:** Yeah.

**Brett StClair:** We're good.

**George Westbrook:** All good.

**Ian Johnson:** Um it's not a can just help me understand something Mike or whoever this integration with the stack stack works code that is there. So is that altered the knowledge hub code base?

**George Westbrook:** Yes.

**Ian Johnson:** Yes.

**George Westbrook:** So what we because I think we had the call with stat work probably two or three weeks ago. Um basically to establish what what is the process going to be like and it could have gone two ways which were the first way which was here's what we've built could we give you a guide on how to implement it or you look at our code base and implement it in the way that you want.

### **00:16:03**

**George Westbrook:** The second one which is the one we are doing is that works very kindly said look here you go here's access here's a branch to work on could you please put the code that you think you need in there we'll check it and then we'll integrate it so I can imagine from DT's perspective there's no or I don't want to say there's going to be no approval necessary obviously I can't pretend I know everything about how DT works but it's probably they're going to probably view it from this is stack works code so as long as it passed is the the coding standards and coding guides then it should be should be all good. um which so we did the initial migration without the standards got it running locally now we've done the I think we've done on in the process of doing but the

**Dorte Dye:** Perfect.

**George Westbrook:** later end of the process aligning it to the the coding standards um which I think from memory it was there was some kind of check with the structure as long as it passes 80% um then that's all good to go and it's going to pass their CI um I think at the moment we've got it is 82%.

### **00:17:09**

**George Westbrook:** So if we did nothing else, it's it's going to be going to be passing. Um so that's all good. And that will go into call it the build pipeline for stack works. Um it will all it will be is the um what's it called? The AI services which will connect to that. Um so I'd say the because there's obviously the conversation with stat works about the agent authentication. What's that going to hold? That's not a blocker on the knowledge hub. um because the there's no permissions to manage. Um the only blocker on that in terms of infrastructure would be obviously getting it in a DT approved um infrastructure environment um including the data and the database as well. Um and then apart from that it's like the only part where there might not need to be some work is probably around the the the data side. Um because the way that we're going to be hopefully deploying it using container what's it uh Azure container apps which is like the the cloud run equivalent um is when when we were on the call I mean I don't know if they were I think I said this on Tuesday I don't know if they were just plucking out of their ass pretend that they'd read it but they said there wasn't anything in there that they saw that that would be a blocker um which initially we thought container apps could potentially be one um because everything else is running on uh AKS um or Kubernetes which

### **00:18:39**

**George Westbrook:** container apps is it's just a managed service um so that's that's why we're we're say ultra if ultra confident in terms of the that it's going to work um but like we said by Tuesday we'll we'll make sure that not that we're ultra ultra confident that we know

**Ian Johnson:** Yeah, if you don't mind. I think one of the things it allows but just ask answer me a question. So, doing it by Tuesday, when will you actually start doing it? And I'll explain why I'm asking the question.

**George Westbrook:** Probably tomorrow. I say pro.

**Ian Johnson:** Okay.

**George Westbrook:** Yeah. Is is Yeah. Is pro probably tomorrow. What is it? Are you I'm trying to read your mind here and I'm thinking you're trying to

**Ian Johnson:** I just want to know how long it actually takes.

**George Westbrook:** Yeah.

**Ian Johnson:** So,

**Brett StClair:** Yeah.

**George Westbrook:** Yeah.

**Ian Johnson:** if you sat down and did nothing else but just do this,

**Brett StClair:** Seven hours.

**George Westbrook:** Okay. Okay.

**Ian Johnson:** how long does it take?

### **00:19:41**

**George Westbrook:** So, okay, what yeah, what we might do is find a find a time where we've got the this is all we're doing and just try and get it done as quickly as possible.

**Ian Johnson:** Sunday mornings are good,

**George Westbrook:** Um they are

**Ian Johnson:** George.

**George Westbrook:** Yeah.

**Ian Johnson:** I would not I would not advocate for that at all. Not at this stage anyway. But um yeah, I just what I just want to do is I if it it's not about how long it takes to get it done. I'm sure there there will be things that DT come with and say well it has to go through this XY Z all those kind of things that's fine but if you take away the actual doing of it then what you're left with is just process so you know there's a less of an argument

**George Westbrook:** Yeah.

**Ian Johnson:** to drive through that process than there might be if if they say well actually this thing takes a week to stand up which I think we all know it doesn't but if we can actually say well we've stood it up uh with with Novo in exactly the same in exactly the way we're asking you to stand it up then it will just help if if the conversation gets tricky.

### **00:20:45**

**Ian Johnson:** Well, not it will get tricky.

**George Westbrook:** I I think where I think where it wouldn't be necessarily a fair test comparing what we do to they do is in terms of they've obviously got all the existing thing. Uh um existing deployments um which will be which will be locked down which obviously we we will do in that environment as well. But certain things like ingress and egress to ports that or to services that um that they've already got um we could pro we could see if we could mock that. It's just we'll have a think

**Ian Johnson:** Don't don't don't don't go too far with it. At the end of the day, um we'd have done it. We'll know anyway is a separate exercise. We'll have know how long it took without the other things that DT need to consider. Um and it's just the challenge that we can raise them to say, well, hold on a minute guys, we've done it and it took this long. So, what's the other stuff that you need to to do around it?

### **00:21:43**

**Ian Johnson:** I just actually don't think they've looked at it, Mike. They also da made reference to the fact they didn't know that AI needed to be part of the go to market launch, which I mean I don't I don't think it's true either,

**Dorte Dye:** It's not true.

**Ian Johnson:** but I think sometimes with these guys, unless it's tattooed on your forehead, so they're looking at it all the time, they they kind of don't get it. So that's besides the point.

**George Westbrook:** Yeah, because I think it it was they obviously when we were talking about it it seemed like what's his name? Steven I can't remember the other guy. Longish hair with glasses.

**Dorte Dye:** Anthony.

**Ian Johnson:** Anthony.

**George Westbrook:** Yeah. When we were talking about the the console one that seemed like it seemed like they got a bit of a a fire in their eyes when we were talking talking about that.

**Ian Johnson:** Yeah.

**George Westbrook:** Open fire.

**Ian Johnson:** I Yeah.

**Dorte Dye:** He's used to that side of things, right? It's the operation side.

**Ian Johnson:** the more operational side of things.

### **00:22:39**

**Dorte Dye:** Knowledge hub. They don't have anything similar for their customers because it's all the APIs are consumed by one customer. They're not visible. So, this is all completely new for them.

**Ian Johnson:** Yeah. Anyway, the the task in hand is that we need to make sure we can get the AI uh in deployed, tested as part of the knowledge hub launch. Otherwise, we can't really do it given the fact that it's a key part of our messaging. Um, so not a lot of choice really. Um, right. If you don't mind doing that, get that stood up and just tell us how long it how she took that be useful.

**George Westbrook:** Okay. Um, yeah, cuz I suppose if if anything as well, it's Yeah, this will be a rabbit hole. Yeah, we'll do that.

**Ian Johnson:** Okay, cool.

**George Westbrook:** Um, and then so we just think the I suppose have we got are you able to pull up the we've got like a demo version of the the console co-pilot as well. Um, which which we're actively working on.

### **00:23:44**

**George Westbrook:** Um, so obviously like the branches of branches of working agent access layer which is obviously going to carry over to the cons full agentic experience and the console co-pilot um with all the permissions and stuff like that. I think Hassan's just bringing his screen up now. And this might not be as smooth a demo because we haven't been practicing for hours like we did for the other one.

**Hasan Ahmed:** Yeah. So, um, so I get started. So, on the like actual the console, there's a option to have like I actually the co-pilot as well. So the here is to more um I'll say as in like if you want to explore or if you want to get to like a certain page if you want to see the specifics like it will help you then get to that page. So, let's say instead of having to click around, head to like a certain page and be like, "Oh, like I can't find this." You can just ask um take me to the transactions and as you can see like it wouldn't take you there as it will also like allow you to sort of like explore have a look.

### **00:25:12**

**Hasan Ahmed:** Um it will also be be able to see like everything on your actual screen. So you can say tell me about this page and as you can see here like it will give you like a brief like explanation. um we can actually go like a bit more like into like a specific um card holder. So if I get the example of um I think the name was take me to Ka Sharma. I think this was the example I was using earlier. But it would do like a tool call like it will take you there. So and then if you want to explore have a look and see like a specific information. Um it's also something handy as well. So if like instead of so let's say for example you're on the actual overview page um you want to go to let's say uh service uh let's say cards and you can say uh tell me about the page I'm on and then see Uh, oh, it doesn't seem to Okay. Well, um, like I need to do like a bit more like actually cleaning up, but like at the moment it's um quite um as in like it's more of like a Q\&A thing.

### **00:26:59**

**Hasan Ahmed:** So if you ask it like specific sort of like questions it will as as it will answer it. It will also like take you on to the actual page to expand onto it. It will also be able to do the actions. Um at the moment I haven't added it in yet but it will be able to say um if I want to cancel the cards it will ask you like if you want to do it ask for like a like approval card for example. Um but yeah. Um

**George Westbrook:** I I suppose it's well obviously like we've mentioned before you mute your There we go. Um yeah, so it's it's it's going to be similar to the look and feel of the the the full Agentic experience with obviously some some stuff added and maybe some stuff taken out as well. So the things that might be taken out are the things like the generative UI components where it's bringing up the components in the screen rather with the co-pilot. It's going to take you to that screen.

### **00:28:06**

**George Westbrook:** It's going to take certain actions on that screen as well. Obviously the main things that we showed you at the moment is it's more in terms of UI in terms of here you go. This is how it's going to look at the side. Here's some functionality. Um so now we've got that that base in terms of UI and call it the the base agent. That's where we'll start to be layering on that extra functionality. So rather than it being a a Q\&A, um it's just taking you to a page. It'll be taking actions. It'll be suggesting if you're stuck on a page, what it's going to have is the let's say you open a chat, you navigate to one page, then to another page, and then another page, and then back to another page. It's going to understand where where you are and where you have been before, the certain actions that you've taken as well. So, if you're stuck on a certain step, um it's going to be like, okay, well, the user three steps ago tried to or took this action on Priya, um now they're trying to cancel a card, but she's on the dashboard.

### **00:29:03**

**George Westbrook:** Um let's navigate to the right page, dive into a bit deeper as to what it is she actually wants to do. Um though, it's it is that that true co-pilot that's kind of looking over your shoulder to make sure make sure that you're doing the right things, but also take the action for you.

**Michael Moores:** Yes, that was great. Okay.

**George Westbrook:** Um but yeah, I think apart from that, we've got yeah, the yeah, we'll wait for the the infrastructure stuff. Um we'll get that thing in Azure by by Tuesday. Make sure we know how long it is. Um and yeah, I think that's I think that's everything.

**Michael Moores:** Yes, me.

**George Westbrook:** Perfect. Right. Speak to you. I'll speak to you on Tuesday. For some reason, I thought uh a Tuesday today.

**Michael Moores:** Perfect. Nice. Thank you.

**George Westbrook:** Lovely. Cheers. Have a good one.

**Brett StClair:** Okay,

**Michael Moores:** Take care.

**Brett StClair:** I I'll sort out the the fly plan for you.

**Dorte Dye:** Take amazing

**Brett StClair:** Yeah, I just thought I'd get you unfiltered version.

**Dorte Dye:** never rush anything if it should.

**George Westbrook:** Didn't that was a hint, Brett?

**Dorte Dye:** Oh, he knows already. We were texting. It's like can't be sh at the end.

**George Westbrook:** Perfect.

**Brett StClair:** That's pretty

**Dorte Dye:** You didn't make your homework. No. Okay.

**Brett StClair:** cool.

**Dorte Dye:** Speak you later.

**Brett StClair:** Good job.

**Michael Moores:** Jessica.

**George Westbrook:** Speak to you soon.

### **Transcription ended after 00:35:30**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*