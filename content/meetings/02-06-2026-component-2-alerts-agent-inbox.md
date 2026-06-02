---
date: 2026-06-02
type: component-session
scope:
  - "[[agent-inbox-alerts]]"
status: extracted
extracted-to:
  - "[[agent-inbox-alerts]]"
---

# Component 2 — Alerts & Agent Inbox (deep-dive)

> **Type:** Component session
> **Parties:** Novosapien (Brett, George, Max) · **TXN** (Ian Johnson — CEO, Mike Moores — CTO, Dorte Dye — COO)

Deep-dive on the proactive lane: the three alert mechanisms, the central notification hub, the cost/token framework, and the alerting-vs-reporting distinction.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Three alert mechanisms — change-impact, event/threshold, scheduled anomaly/reporting | [[agent-inbox-alerts]] | §2 functional requirements |
| Alert (C1, present info) vs Agent Inbox (C2, analysis + plan + execute on approval) | [[agent-inbox-alerts]] | §1 |
| Central notification hub — any source (AI/DT/Stackworkz) → user's preferred channel; Stackworkz owns delivery | [[agent-inbox-alerts]] | §1 / §4 |
| Cost/token framework — cheap detection (observability / middleware), AI only on trip; bounded queries | [[agent-inbox-alerts]] | §4 |
| Alerting vs reporting — point-in-time vs reflective scheduled summaries (the AI-first differentiator) | [[agent-inbox-alerts]] | §1 / §2 |
| Cross-program benchmarking is data-gated (de-anonymisation, contractual consent) — later | [[agent-inbox-alerts]] | §10 risk |
| Fraud flags may surface here but are serviced on a dedicated fraud page | [[fraud-risk-assist]] | Cross-ref noted |

---

## Transcript

### 00:00:00

   
George Westbrook: Morning.  
Max Kingaby: Morning. Our session slightly overran by half hour.  
George Westbrook: That's all  
Max Kingaby: He's still in  
George Westbrook: right.  
Max Kingaby: a  
George Westbrook: That in.  
Michael Moores: Morning.  
George Westbrook: How we doing?  
Michael Moores: Morning. Okay.  
George Westbrook: Oh, don't I'm not very happy that the weather has changed.  
Michael Moores: Paul back on the furniture yesterday.  
George Westbrook: I don't had to cycle in this morning.  
Michael Moores: So, it started raining.  
George Westbrook: I mean, it was only a five minute cycle, but I was absolutely drenched.  
Michael Moores: It's not good, is it?  
George Westbrook: Well, it'll be mostly audio. Right.  
Brett StClair: Oh, yeah. Um, I sent you an email. I was I'm sure you sent me through API documentation, but I can't find it. And I don't know if I've confused it for the user journeys. Um, if you do have API documentation, that would be great if you could resend it to me. I don't know if you saw my  
Michael Moores: Yeah, I think we've got you've got user stories that are sent.  
   
 

### 00:01:16

   
Michael Moores: We've got I mean depends how much you want.  
Brett StClair: email.  
Michael Moores: We've got about 210 documents. Um we've got uh we've got both markdown and uh word doc as well. So I don't know what's better for you.  
George Westbrook: Mark down  
Michael Moores: Uh,  
Brett StClair: So, I'm loading it all into vault at the moment.  
George Westbrook: please.  
Michael Moores: I'll  
Brett StClair: I just want to make sure we if we didn't cover anything in the conversation that we're picking up everything else.  
Michael Moores: Yeah. Yeah. We've got loads on the console,  
Brett StClair: Um  
Michael Moores: the API, basically everything we've sent to them. So, I can pull that out and see what what's available. Uh, send that across.  
Brett StClair: I think the key thing right now is going to be around the API. Um  
George Westbrook: helpful as well. Um because it's just yeah, the more the more information the better. Um like we'll probably do few scans through, pull out stuff, get it all linked up. Um, and then it just like like know it's just going to add that contextual founding to what we're doing a bit better.  
   
 

### 00:02:18

   
George Westbrook: Um, and yeah, then when we yeah when we come to building some of the docs out,  
Michael Moores: Yes.  
George Westbrook: it will well docs not as in docs but in documents. Um, it just it just makes it a lot a lot a lot easier.  
Michael Moores: Yeah. So, yeah, I'll I'll try and pull out  
Brett StClair: Just quickly my merged audio. Is it working? Okay.  
George Westbrook: the call,  
Brett StClair: Yeah.  
George Westbrook: but I can hear you on. Yeah, just my ears let the pass  
Brett StClair: Right. George and I are sitting next to each other but quite far away from each other but we can still hear each other.  
George Westbrook: through.  
Brett StClair: Not far away enough from each other.  
George Westbrook: Morning  
Dorte Dye: Sorry,  
Brett StClair: See the no worries. Every time I see Fathom,  
Dorte Dye: I'm  
Brett StClair: I keep thinking it's your spare noteaker, George. George also when we're not in the Google environment uses Fathom on his note takingaking side of things.  
Michael Moores: That's good.  
   
 

### 00:03:39

   
Michael Moores: Very good.  
Brett StClair: Good. Are you guys at least getting the recordings as well, right? From that should be sent  
Michael Moores: Yeah.  
Dorte Dye: Do you? Oh, from the noteaker.  
Brett StClair: to It's  
Dorte Dye: I thought from the portal. I'm still waiting.  
Brett StClair: coming. It's coming. It takes us a while to get all the agents firing and consolidating everything and and then it takes  
Dorte Dye: I'm so excited.  
Brett StClair: about 24 hours.  
Dorte Dye: We will have then so much to read through it.  
Brett StClair: Yeah. Don't be that excited. It's not that much fun going through because it's a  
Dorte Dye: something I missed,  
Brett StClair: lot. It's a lot. Yeah. I think those those Aaron  
Dorte Dye: right?  
George Westbrook: where you're getting into the weeds that I mean you got to take two mindsets obviously before it's either right let's take some notes or let's get absorbed in the conversation obviously the absorbed in the conversation after you're like s*** what do we talk about the first 15 minutes blah blah blah and that's the issue is when you haven't got a note taker and then you've got to go into another meeting and uh you can't cannot remember a single thing because the noteaker It just hasn't worked.  
   
 

### 00:04:53

   
George Westbrook: Should we get  
Brett StClair: It's uh Ian  
George Westbrook: cracking?  
Brett StClair: coming.  
Dorte Dye: Uh, you will be probably a bit late. Yes, another meeting.  
Brett StClair: Okay,  
Dorte Dye: So, let's get  
Brett StClair: that's cool.  
George Westbrook: Which  
Dorte Dye: started.  
Brett StClair: Bring up the vault. And I think what we want to do is just go through the components and pick out what you guys are keen on chatting next. Going to have to zoom in. Yeah, I'm going to have to See,  
George Westbrook: Hey, is it going  
Brett StClair: do you see how small it is though on on Oh, yeah. You do see how small it is. Yeah.  
George Westbrook: and then that might help?  
Brett StClair: There we go. Um chips the one  
George Westbrook: The one we did yesterday was that agent access layer. Um, this it kind of ignore this one. This is up for debate because I know I know when we spoke before it was kind of the the fraud the fraud and risk assessment is is something that would be valuable, but how how viable is it obviously initially?  
   
 

### 00:06:00

   
George Westbrook: So, I think that might be one we tap on at the end um and just just flesh that out, see if see if there's anything that we can get out of there. Um obviously we got the co-pilot um which that'll be a session in itself. Um the agent inbox and alerts and the way we'll probably do that in my opinion I think that might be a good place to start today. Um is the alerts are the more we call C1 or version one which is just the more simplified AI application where it's just alerting the user. Um, and then the agent inbox is there. Here's the alert. Here's the analysis. Here's the plan. Do you want me to act? It acts. It executes. Um, the full Aentic experience is that clawed interface where it's rendering the components, things like that. Um, developer support kind of bucketed everything for the developer um, portal into that. Um so just be exploring just be exploring what's what's in there and the internal WOPS ones they might sit across multiple um it's more what can we give you internally or what can we build internally that's going to help you with the task that you need to do.  
   
 

### 00:07:13

   
George Westbrook: So obviously we mentioned about the the documentation things like that or the kind of internal support triaging. So it's it's doing that pre-analysis before. Um, so is there any of them where you're like, "No, I we need to do that one today. That's a burning desire." Or is it is it okay if we start with the the agent inbox and alerts one?  
Michael Moores: for me. Thank  
George Westbrook: Perfect. Right.  
Michael Moores: you.  
George Westbrook: Stop sharing this.  
Ian Johnson: on it. So I am  
George Westbrook: um and the agent inbox. So I think if we think of it in terms of alerts is kind of like what we were saying yesterday. It's just that let's present that information to the user. Um and then the agent inbox is that like I mentioned the here's the information. It's kind of like a a graduation of the the alerts. Here's the information. here's what I think should happen. Um, do you want me to do it? Um, so I think if we start with the alerts and try and think what sort of things do we want to alert the user of and to the two that kind of spring to my mind is one you have just changed this setting.  
   
 

### 00:08:33

   
George Westbrook: Um, this is the implication and then the other one would be here's some behavior I've noticed in your transactions. Um, let me let me surface some information. Um, is apart from those two, is there anything else that you think you'd be wanting a like AI alerts for?  
Michael Moores: I think we had um sort of a a flow in the console sort of centralized obviously alerting so ultimately flexibility to monitor and alert anything the user would like.  
George Westbrook: Mhm.  
Michael Moores: So you know alert me if um transaction decline goes above 20% for example allowing them to obviously take everything in our payload and monitor on that that's something feedback  
George Westbrook: What's  
Michael Moores: into sort of very custom user base obviously we'll have our very our core things our CPU  
George Westbrook: this?  
Michael Moores: infrastructure that sort of stuff we'll build out the box we'll also probably build a a decline as well but you know as an example anything they want let's say they want to look at specific merchant that they are trying to promote or you know push more transactions through they can actually look at that and obviously monitor when that gets to a certain threshold or whatever it may be.  
   
 

### 00:09:42

   
Michael Moores: So that really flexible um alerting sort of monitoring basically  
George Westbrook: No.  
Michael Moores: there one thing we're sort of looking at is where that lives you know we do have we have noted it down in a later phase for DT for an alerting endpoint but we do feel that potentially AI is the sort of center of  
George Westbrook: Mhm.  
Michael Moores: this and it makes it better there obviously we would like sort of a central place that not only does the AI trigger but anything outside of it can also trigger so DT could trigger you know stack works in the console could also trigger those having this centralized sort of inbox alerting that we can actually surface for you know all of TXM basically is the aim here u from our  
George Westbrook: So when obviously but in my lens I'm just thinking like  
Michael Moores: side  
George Westbrook: alerting a user a or a client did correct I'm wrong are you talking about internal alerting for you guys as Oh,  
Michael Moores: no this is for specific to customers so If as we build this out, there may be things that we build in DT that we want to trigger and you know the user um  
   
 

### 00:10:40

   
George Westbrook: okay.  
Michael Moores: don't like I say don't off the top of my head but we have certain things in there that and certain services we may use but yeah anything we want to service to the user will have alerting internal you know we can use what's built but there's no sort of requirements specifically for our our needs in AI right now we've got what we want from our you know what sort of data lake type platforms login platforms anyway so this is very much so userf facing. There may be the other two parties wanting to fire in you know specific things as we build this out. So we're very keen on having two things we're having central is obviously the alerting and the the notifications as well. So you know if you notify someone on their own channel they're currently sat notifications are coming out with stat works to build I say we want a very central place that no matter who triggers it whether it's AI or DT we can send it to their preferred channel obviously have that centralized so that's a very key part that we have whatever we build here can be used centrally obviously AIdriven largely but if we do have some sort of those connections from DT and stack works that we can actually bridge them in as well um and have that sort central place to surface these informations or send it by SL or email wherever it may  
   
 

### 00:12:01

   
George Westbrook: So there's two things my head one is so it seems like there's userdefined  
Michael Moores: be.  
George Westbrook: alerting and then I'm assuming there's going to be just kind of systemdefined alert um or can is it every single type of alerting is completely down to the user or the business to decide I want this I don't want that or are there certain things it's like no we have to make you aware if this if this happens  
Michael Moores: Yeah, I don't think we have to. I think we we would want to. Um, you know, if you suddenly get 90% declines, then we're going to want to. So, there sort of a bit of a learning session there. But essentially, yeah, anything that's anomaly, we would probably want to sort of flag up there. say we've noticed this, you know, all of a sudden from 12:00 every transaction for this merchants failed. Those sort of things that we sort of highlight the big things that could be affecting our program. We would want to provide that sort of status.  
   
 

### 00:12:56

   
Michael Moores: Um and we probably aim for sort of only critical or you know heavy impact in in terms of decline failed to create cars you know whatever it may be those critical paths and then I think we would leave the the very finite granular stuff to the user but we would provide that sort of initial corpus obviously again hopefully it will learn over time so rather than fixed rules it'll be okay these are the sort of things we want to flag as we get more data we understand what the industry is like what the anomalies actually are and we can start triggering based on what we see and that's I think that's to your point in terms of you've made this configuration change is now offset you against the other people in your industry you know are you aware are you happy with that and sort of baseline that as well so you know the data we're going to collect across other programs I don't think has ever I've seen been used before so I think it's really powerful this is how you're comp not comparing directly but this is how you are against this industry this is what's different this is what's an issue this is where you get those recommendations as well.  
   
 

### 00:13:55

   
Michael Moores: So sort of bringing that all in. But yeah, there will be certain certain cause obviously the transaction decline being the the major one from a trans processing now obviously we feed in that what I know you the fraud and the fraud and monitoring I think that could feed in but that's almost you service that separately so that's like this looks fraud versus I think for this we look at a whole program and obviously have the alerts in there you know potentially you might flag a fraud alert in here at some point but ultimately we would service that from a dedicated fraud page because there'll be certain actions you want to do, you know, whether it's a chargeback dispute, whatever it may be. Um, we would service those sort of fraud alerts in a separate uh page in the console. Um, but there's nothing stopping, you know, being flagged in this inbox to start with and then, you know, moving down that action. But yeah, fraud is very specific. You go, you know, your fraud um analysis, you're going in there, you're actually looking at specific stuff and how you compare as well.  
   
 

### 00:14:51

   
Michael Moores: And obviously that's that data we're not going to have. A, we don't know it's fraud because we need to be told it's by our client. So, it's going to take a while for that to build up, but I think that's why that piece is sort of separately, but I think it feeds nicely in later into this whole alerting and and inbox methodology.  
George Westbrook: Oh, I think you're muting.  
Ian Johnson: Sorry, there's a few things for me. Some some of it's to do with phasing. So, let let me deal with the phasing thing. So, so firstly, um consider the two ways you describe it George of like kind of almost I would say behavioral and and changes. So, impact of changes. We discussed heavily yesterday about,  
George Westbrook: H.  
Ian Johnson: you know, advising people about the impact of what they were about to change before they did it as opposed to you just changed this. Did you realize that this that that means that this has happened? So, I'll park that. And if I stick to the change thing, the thing that's Mike's talking about is being being able to look at multiple programs, understand what type of program you are and whether or not the change that you are about to make or have made means that you're adopting a less than industry standard  
   
 

### 00:16:14

   
Ian Johnson: approach. That is some way off, right? we we have to have multiple clients in each of the use cases before that becomes usable or any value. And the reason I say this is that even before the days of AI being there when we explored this as Marqueta with anonymized data, the problem is people know who you who your clients are because you advertise who your clients are. only got two clients in expense management, then it's not anonymized because you're one, they're the other. Okay?  
George Westbrook: Yeah.  
Ian Johnson: If you've got five clients but it's known that one is the standout client in in terms of volume and how that that thing is going again it becomes difficult because it's like well you know let's say it was a volume based thresh you know how am I performing against you know with my volume of transactions of this merchant you've got to really consider how you can put that information back so it's powerful but it has to be very carefully approached even with anonymized data Otherwise, people would just refuse to allow it to be used and we would I think dirty you raised the point already there would have to be a contractual agreement that the client allows us to use their data for certain purposes.  
   
 

### 00:17:42

   
Ian Johnson: So I think we just need to think about that's going to be some time in the future. Um whereas the some of the impact of changes Mike we we can do. So for example, if you just look at a client's data and they reduce the the as I said yesterday the maximum trans transaction limit from €200 to hundred euros you can see how many of their previous transactions were above €100 and you can say well all of these are going to be declined. So you can do something that's this is what the impact is going to be. The behavioral one as in you know show me alert me when I'm I've got you know 20% less transactions at this merchant or whatever it might be and creating those alerts. I just want to understand how you go about doing that and balancing a usability, b accuracy, and crucially token usage. If somebody's just going to can just type natural language anything they want. I I have this thing where there's where the AI there's not enough structure to really pull back meaningful data or accurate data and then you get stuck in a conversation of we couldn't find we couldn't find this merchant or there have been that and then you just start burning through tokens in a conversation that's going back and forth.  
   
 

### 00:19:23

   
Ian Johnson: Whereas if you put some kind of framework in place about what types of behavior and that you talking George about the that kind of surfacing the UI within the AI itself is you know you've seen that thing of okay is is I don't know let's is it all merchants one merchant countries whatever it might be so that you're building it's still within the AI tool essentially the equivalent of a set of filters before you go away and do the search because I think it's important that these queries are built for success rather than just throw anything in there because I can just see people be going back  
George Westbrook: H.B.  
Ian Johnson: and forth. No, I didn't mean that. I meant this and then back and forth. I meant this and it just or now show me just Italy or now show me just France and and it's just all of that and I think that this is a big philosophical thing for me. How much do we surface that we manage within our AI and our AI cost space versus how much is really should be uh for the client because we've given them a bunch of data already.  
   
 

### 00:20:48

   
Ian Johnson: So bear in mind that they get a web hook with all of the transactional data, Mike, anyway. And I've always had the belief that a bunch of I don't I don't know what percentage, but a large bunch of clients will will not never want to use our AI tooling. They'll just use their own.  
George Westbrook: All  
Ian Johnson: Got all of this data, so we just do it ourselves.  
George Westbrook: right.  
Ian Johnson: And that's great for me. I don't care. We gave you the we gave you the data. You're using your AI at your cost to interrogate the data that we've given to you and therefore it's not hitting us. There will be some people who don't want to do that and who will find the AI within our own platform to be useful. But how far do we go before we end up just being this open thing that's going to kill the business very quickly? So I think there's some framework considerations that need to be put in place otherwise I can just see us very quickly causing ourselves a problem from a cost perspective and a usability perspective  
   
 

### 00:21:59

   
George Westbrook: So in terms of say how many ballpark for how many users in like a a year's time and then how many times a day obviously it's impossible to say because it's not there yet but just like ballparks of right let's say there's going to be this many businesses with this many users in total and we envisage they're going to log into the platform this many this many times a day. Um because I I think it would be you you might be surprised that the the the cost is not going to be as as large as as you would you might think. Unless you tell me it's going to be 5 million users and they're going to be on there eight hours a day.  
Ian Johnson: No.  
George Westbrook: Okay,  
Ian Johnson: No. Well, actually, I think Brett provided some indication that I then took to do some  
George Westbrook: then.  
Ian Johnson: modeling on and I'm happy to share that modeling. I I did take Brett's estimate and I can't remember double it or certainly increased it and but it was exactly that principle number of clients number of users per client for both the developer portal and for the console and um number of hours that they would be using the platform on average per day and then that's how I built it.  
   
 

### 00:23:15

   
Ian Johnson: So I'll share it with you to see if it's something that's reasonable. If the if if the cost thing is not the primary concern, okay, I mean, it's going to be I'm always going to be concerned about it because of the horror stories that are out there. Brett gave me a little bit a little bit of comfort around that in those numbers that you  
Brett StClair: protections.  
Ian Johnson: provided. But even then from a usability point of view, and this is where I guess we're looking for your expertise, how would you go about it? So e even if the cost let's say the cost was zero this thing doesn't cost anything.  
George Westbrook: Uh,  
Ian Johnson: So you can type whatever you like and we'll respond the be as best as we can. No framework no things we might need to know. No prompting of you know just put whatever you want in. It seems to me that that's not really the approach that the really good tools like claw. I mean I I I'm we use Claude me not as much as Mike and Da but and some of the things I've done in Claude within that AR within the the UI you get prompted okay before I do this do you want me to do that and next thing is so you get to you have to make some choices before it goes away and then does and in my mind that's what we've got to  
   
 

### 00:24:41

   
Brett StClair: Yeah. So I think  
George Westbrook: Yeah, in terms of like some of these more structured workflows is there'd be like slash commands.  
Ian Johnson: There.  
George Westbrook: Um, so a user goes in, they go forward slash or maybe it's buttons, whatever UX we think might be best. They just go in, there's certain predefined workflows that they might want to do. They're not completely linear like this, this this this, but let's just say it's analytics. I want to analyze my um transactions for the last 30 days above $200. Um so there's there's some structure and then when it it's obviously they can go in, they can ask I want to do XYZ um without doing the slash command. Um and it's going to realize okay, this user is asking about analytics. Let me load in this specific skill. Okay, for this specific skill I need to use these these these tools. I need to make sure from the user state I have I in all of the tool calls I have this argument this argument this argument.  
   
 

### 00:25:38

   
George Westbrook: So even though it's got the appearance of um it's completely free and anything can happen. It's kind of how I like to think about is it's like there's loads of little fishing nets. Um, and the agent's going to kind of if it thinks it needs to put it in this little fishing net, it's going to catch it and then it's going to do this set of structured things. Not structured meaning a b. It's just this is the sort of things that are that are going to happen. Um, so it's semi semistructured. Um, did that did that did that make did that make any sense  
Ian Johnson: Yeah.  
George Westbrook: or I  
Ian Johnson: No, it did. It did. But definitely.  
George Westbrook: think the short answer  
Brett StClair: that we can control those experiences and end the  
Ian Johnson: So  
Brett StClair: experiences when they get to its conclusion.  
George Westbrook: is  
Brett StClair: Right? Because we don't want it to be an open platform and we put in these guard rails that are managed through like a I can probably be blind here.  
   
 

### 00:26:41

   
Brett StClair: kind of deal with a mixture of all of technically not exactly but it's of  
George Westbrook: there's a prompt. pipelines deterministic. This is a general kind of orchestrator um which then has more deterministic workflows underneath but it's free at any time to use any of those workflows.  
Ian Johnson: Yeah, understood.  
George Westbrook: Um but I think if we go if we go back to the to the alerts and  
Ian Johnson: Okay.  
George Westbrook: agent inbox um because this And I'm feel free to disagree with me here. I don't see that living directly with the user would be able to access it in the call it the full aentic experience but the alert um kind of like a a separate part. So the normal alerting maybe there's an a kind of notification center where they can click in maybe a modal pops up and then they're like this is the analysis of this of this alert for the agent inbox there we've got kind of maybe a few design decisions. So where the agent inbox would differ is it does exactly what the alert does.  
   
 

### 00:27:54

   
George Westbrook: Um but if it thinks a change needs to be made, it would proactively say I think so let's say you're you've put your limit to 200 down from a th00and this means this these transactions are now going to get blocked. This makes up 20% of it. I think what you should do is go up and change this setting and this setting. So then what the user would to be I'll show you I'll  
Brett StClair: Thank you.  
George Westbrook: show  
Ian Johnson: So I are use your if somebody wanted to use the AI interface to create an alert, they they can do that,  
George Westbrook: it.  
Ian Johnson: but the alert wouldn't sit in  
George Westbrook: No. So, I think there's two I think there'd be two ways they could create the alert.  
Ian Johnson: Yeah.  
George Westbrook: Um, one of which is the UI. Um, let me uh yeah, let me click a few buttons. This will create that alert. Um, then there is the full agentic experience where it could be I want to create this alert, this alert, this alert.  
   
 

### 00:29:11

   
George Westbrook: And it'd be exactly like they were clicking the buttons. And then what we would have there is it would be this this other example up here. So maybe there's just a forward slashalert skill. Um then it would take them through the workflow in order to create an alert and that would have a specific skill making sure that it captures enough information um in order to be able to fill the tool calls up. And if let's just say it wasn't exactly correct, we're going to have that server side validation on the MCP server which would bounce back. would have a descriptive error message for the agent which would then surface it to the user or autofix it itself  
Ian Johnson: So what what system or part of the overall system is going to be monitoring to see if the alert is triggered?  
George Westbrook: I'd assume and Mike feel free to jump in here is the alert would be once the alert alert is created. Um, we'd get notified via a web hook that there is this alert like let's say 20% of transaction over this amount um is hit this threshold.  
   
 

### 00:30:28

   
George Westbrook: We now need to be alerted. We alert the AI system. Um, this that was the thing I was going to say actually that was what I was going to say. So I think the three types of alert mechanisms, one is user is about to change a setting or user has changed a setting. We receive a request, we do the analysis, um present it back to the user. The second would be the user has set an alert in in the console or they've set it via the agent. When that alert uh event is surfaced, we get notified. we do the analysis. And then the third one which is where we would need to put a lot of thought in is the kind of the scheduled analytics maybe. So there's maybe five things that is analyzing for um looking through the data that might not get surfaced by an event but we can get the AI to look for an anomalies. So, let's just say um twice a day um maybe at 12:00 a.m. and 12:00 p.m.  
   
 

### 00:31:31

   
George Westbrook: the AI will do a scan of certain aspects of their data and look for an anomalies um and if there is any um then it could surface surface that to the user  
Ian Johnson: Okay. Needs some careful thought, Mike, doesn't it? the whole thing because the desire for a central alerting system. um that we then push well to the console to any could be to a user interface it could be to slack teams whatever is the general principle about meeting people where they are so I I totally get that but when you're creating them in AI it's How do what does that actually mean to the central system? What does the central system do to to check if that alert has been triggered? I get the fact that alerting you to the fact that the tri that the um alert has been triggered via a web hook. Understand that as a principle. But what is what is basically running and monitoring everything that we've got alert and alert against and identifying if that alert has been triggered.  
   
 

### 00:33:03

   
Ian Johnson: Is that currently designed or to be built by anybody? Mike, let's just say for the console. Is it designed and to be built by anybody? I think you said stuff, but I  
Michael Moores: Statworks are doing the notification preferences.  
Ian Johnson: don't.  
Michael Moores: So they'll be looking at sending the actual data out. In terms of housing that alert, they're not on the hook for that. No, we have um originally had DT down for it in a later phase, but obviously this was before the AI discussion started. So, you know, if if DT do that, it'll be much later. Um, and it doesn't really fit with them anymore in terms of where the alert is going to sit and how much of this is going to be um in the console and the AI. So, I don't think there's much coming from their side. So, they'll be sort of just building the API for the ability to post an alert essentially uh with no real context or link to their system as it stands.  
George Westbrook: Okay.  
   
 

### 00:34:02

   
George Westbrook: Because I say the init the the the actual alerting would probably be more like traditional software engineering and then at the point at which that alert is surfaced um and sent to the AI obviously that's when it's more AI. So were you imagining that the actual discovery of that alert would be more AI  
Michael Moores: Yeah, usually. Yeah. So, sort of I think it's sort of linked into the the user find one and obviously that anomaly side,  
George Westbrook: based  
Michael Moores: you know, if we need to break it up, we can do what sort of it started with the anomaly detection first, which obviously lives in the AI to to trigger those. Then we sort of built built around that essentially. So if it needs to sit separately in terms of more traditional you know alerting versus that we can look at that but I think yeah we haven't got a dedicated person building that alerting system right now. Um obviously it's in the design as part of the uh super design and something we can speak with stack works to do but it's not specifically uh scoped at the moment.  
   
 

### 00:35:06

   
George Westbrook: because I I think it just if it was AI, it'd really be every single transaction would need to be analyzed which that's where the cost would explode. Obviously, how many transactions you going to get? It's going to be going to be quite a lot. So, obviously, if it's more traditional software engineer, it's just it's kind of just an if if statement or a bit of middleware that sits sits around the transaction request. um anomaly detection. That's where it be probably  
Brett StClair: That's where AI comes.  
George Westbrook: applied um in a in a more suitable way. But then the issue would be it wouldn't be catching the anomaly at the point at which the anomaly occurred. It most likely be at a later point at like so let's say like what I was saying where twice a day it does the an anomaly check or it could be once every hour or it could be four times a day. That's where I think the anomaly detection for AI because otherwise it's we I suppose it's more like support triage.  
   
 

### 00:36:11

   
George Westbrook: So there'd be the the alerts which could if it is a certain alert trigger an anomaly detection analysis but then also the more scheduled one as well. Um cuz I I mean although it's possible to do the alerting the more the userdefined alerts by AI, I think that's where the cost would would explode. Um, and like I said, probably might be better to take more of a traditional um, software engineering approach. And in my opinion, it probably would be best to sit with the API um, rather than having an external service that either interrupts in between the request or sits after the request is completed. Um, yeah, it that wouldn't make too much sense to me. Um, but feel free to  
Michael Moores: Yeah, I think that's it. We really scoped it with DT anyway in in phase one.  
George Westbrook: disagree.  
Michael Moores: So that was our initial plan. Obviously, we're just making sure we have that centralized place. So if the AI can feed into that, you again that fine.  
George Westbrook: Yeah.  
Michael Moores: So I think it's initially scoped for them anyway.  
   
 

### 00:37:21

   
Michael Moores: Uh just sort of a later phase. So we just need to make sure that they all work sort of cohesively together.  
George Westbrook: Yeah. Yeah.  
Michael Moores: Basically the um the console's very much at the  
George Westbrook: Okay. Okay. Perfect.  
Michael Moores: moment except the authentication of the users and stuff like that. The console is very much it gets everything and pushes everything to the API. So it's very much just pull pushing from the API with the exception of the notification preferences and the the other add-ons we've done on the console. So I think that model fits uh fits  
George Westbrook: Perfect.  
Ian Johnson: Can I It  
George Westbrook: Um  
Michael Moores: well.  
Ian Johnson: seems very strange, George. Not a criticism, but I've just heard people were working with around AI says that sounds more like a traditional software development piece. something I don't think anyone in your industry is ever supposed to say, but I I don't let I think sometimes helps me because I'm complete idiot when it comes to this stuff.  
   
 

### 00:38:19

   
Ian Johnson: I don't that that comment about have to analyze every transaction. Well, first of all, the first filter on what you analyze is you're only looking at it for one client. You know who the client is. So, you're not looking at all of our transactional information. Okay. So let let's let's do a part where alert me if my um transactions with Amazon are down 20% you know over the the previous 7-day period and that's the alert. Well f so first of all you know who the client is. Second of all you know the period you're looking for. The next thing is you're doing a calculation of whether what the percentage changes as to whether or not the alert happens. The the question about when does that how do you run that in in terms of surely that is prime AI space and shouldn't be using tokens forever in a day otherwise I don't know maybe I don't understand it but it seems to be we can all rest easy no one's job's going to get taken because if you're actually telling me to do that kind of think you need to build software in the old way of doing it.  
   
 

### 00:39:41

   
Ian Johnson: That seems somewhat scary to  
George Westbrook: Well,  
Ian Johnson: me.  
George Westbrook: so it's how would the So what if it was pure AI based? So let's say it's checking for when it it reaches 20%.  
Ian Johnson: Yeah.  
George Westbrook: the if it was pure AI based and there's no way that the AI gets alerted that this is close to 20%. It would have to analyze every single transaction in that program. It'd say right new transaction let me execute some tools let me query the database let me do some calculations to work out is this above the 20% is it no okay well still consuming those tokens in order to do it it's possible it's AI can do it but what would be best is if it was more traditional software engineering so it's kind of um transaction comes in let me look at this sort of transaction right let me work out the um let me work out the percentage. That's a really really cheap operation in like normal software engineer. It's just a query to the database bit of a calculation to work out if this is above or below 20%.  
   
 

### 00:40:52

   
George Westbrook: If above 20% let me send this to the AI, let me send this event and this payload to the AI to do the analysis only when it's needed. because otherwise let's just say one it's one in a thousand um that these alerts it means 9 99 999 are just wasted tokens. You could say they're not wasted because there could have been an error. Um but I suppose there there's there's times when it is good to just use normal code and times where it's good to use an LLM. And I think the times where it's good to use an LLM is where there is that issue and then you send the webbook request to the to the a call it agent API and then the agent API does that further investigation because it's like I'll show I'll show you this example um here. So, what what we've got this set up. I think I think think shown this before is this is for one of one of the other things we've been working on. Um, and all it does is picks up when there is an error when we need to be alerted.  
   
 

### 00:42:01

   
George Westbrook: Um, and when there is, it analyzes analyzes the impact. So, we click diagnose, it will go away and diagnose it. If we didn't have normal traditional software engineering that would pick up this error, every single request that we had within our system, we'd have to analyze with with AI. And this is not a big product, but it' probably be 10,000 requests a day. Um, I mean, there was, I think, three or four yesterday. Um, so the amount of tokens we've used for only three of those three of those requests. Um and then going back towards like the the agent inbox. So I can imagine this would be like a section on section on the console where it would it would surface these alerts would do a bit of the pre-analysis then the user can trigger that right diagnose it or create a plan and then would surface the plan and then they click implement and it would go in and actually update the settings which is like I said the the later stage more complete agentic experience.  
   
 

### 00:43:07

   
Ian Johnson: Okay. So, let let me follow this thread then. Let's say I set something up on Claude. It's a task a schedule task that every week I want you to analyze these industry websites. look for these competitor names and surface up any news on product releases, new clients, blah blah blah, whatever else it is. All agreed that that's pretty standard Claude FOD and that I've said when I want it to happen, how often and when, and essentially go and do this.  
George Westbrook: Mhm.  
Ian Johnson: So the point then seemed to be that the challenge was figuring out when the 20% thing got reached. Okay,  
George Westbrook: Mhm.  
Ian Johnson: because that would be constantly evaluating every transaction to see if it took it over 20%. to totally get that.  
George Westbrook: Yeah.  
Ian Johnson: But if it's do this once a day and let me know if it's over 20%. That shouldn't be okay.  
George Westbrook: That's That's fine. That's that's absolutely  
Ian Johnson: So I think this is the this comes back to the original point that I made around the framework around this stuff.  
   
 

### 00:44:26

   
George Westbrook: fine.  
Ian Johnson: not necessarily that it has to then be very rigid or it has to sit in DT have to build it which I'm not a massive fan of or it's it's in AI and it's too open and it therefore means it's going to cost us the earth. I think it just needs some really careful thought about what we allow people to do and what we will support and what we won't support. So I completely understand if you said just constantly check every single transaction and as soon as I get over 20% alert me because I can see that that would burn through endless stuff and I can see the alternative for that.  
George Westbrook: What the f***?  
Ian Johnson: Well, if you want to do that, just build it as a query in normal software. I can see that as well. But I think there's something in between the two which actually for a client is the more important thing.  
George Westbrook: Yeah.  
Ian Johnson: It needs some consideration as to how you create a framework of what people are allowed to do when they're in alert.  
   
 

### 00:45:34

   
Ian Johnson: So they can create the alert and ask it to and basically ask to be  
George Westbrook: Heat.  
Ian Johnson: alerted when this happens. But then we can only we could only run it once a day and then essentially if on any day you go over 20% that an alert will happen.  
George Westbrook: If if it's if that's cuz because where I was thinking is alert is crucial at the point at which it happens the user needs to know. But if you're saying it's fine happening at a scheduled cadence of once or twice a day, AI is good at will be good at  
Ian Johnson: I think I think there is some Mike and ultimately Mike's going to be the ultimate decision maker here.  
George Westbrook: that.  
Ian Johnson: I think there are some where it's exactly that Mike. It's as soon as something happens, somebody needs to be alerted. That to me is a different thing to almost an interest thing that the  
Michael Moores: Yep.  
Ian Johnson: client raises. I I want to monitor my program and these are the things that I I'm interested in. So I want you to alert me when this happens or that happens.  
   
 

### 00:46:43

   
Ian Johnson: Um it's as because I can see the dividing line there, Mike, where those things are instantaneous which could be considered the more critical things. you might want to build in DT. Um because ultimately I think more typically in those scenarios might I feel as though we would feel that we are obliged to tell the client of that or alert the client to that. For example, you know, all of your there's been no authorization response from your host for the last 10 minutes or whatever it might be because that's something that needs critical action versus a client initiated. I'd be interested to know when these things happen on my program or if these things happen on my program. I think that that's for me is the difference. It's it's not I'm only here as giving input. I'm al not the ultimate decision maker on it. But the it just feels almost it would feel crazy to me if we built so much alerting capability into into DT that I just I  
George Westbrook: Yeah.  
Ian Johnson: just can't even imagine how we do it.  
   
 

### 00:48:07

   
George Westbrook: Something I personally probably  
Brett StClair: look at building the alerting uh rather use some kind of observability tool. There are lots of these tools that you just plug into your stack and you can configure and then you're not necessarily building the alerting. Can you can you can you  
George Westbrook: set the rule sets for that because these are obviously okay because I was going to say these are obviously TXN defined rules they they're not going to be an error as such um like there's not going to be an exception that's thrown it's so is And observability might be even too  
Brett StClair: Oh, right. Observability is getting right into a real time stream. Maybe that's the case. But like I do get worried. I I agree with you. like building out alerting and all that kind of stuff yourselves is this has been a thousand done a thousand times over right that they're great tools that can then be installed configure and then you float the API up and takes a couple of days to get it in place and then you continuously adding um rules and alerting that you require down from the user because it's all API driven.  
   
 

### 00:49:34

   
Brett StClair: Um, you can feed it back up to the AI and then you kind of avoid building that alerting stack yourself. Like I I agree like I kind of like that these kind of standard platforms. Yes, they might be a little bit different, but there lots of them, right? Um, and it I probably advise looking there first, seeing if it answers your questions around getting the alerting right, expose an API, and then pull it into the notification kind of center. I mean, how does everyone feel about that?  
Michael Moores: No, I think it makes sense. I think yeah, like a lot to build, isn't there with DT? So, we can look at those tools.  
Ian Johnson: Yeah, I  
George Westbrook: I I think even without that the second one you were mentioning Ian with the like once a  
Ian Johnson: I  
George Westbrook: day do this analysis it all it's doing is it's querying querying the data it's building up a picture it's checking it's validating um that wouldn't require the observability it's just the the AI analysis at the point at which that event happens.  
   
 

### 00:50:53

   
George Westbrook: That's where the observability would would would be  
Ian Johnson: Yeah,  
George Westbrook: needed.  
Ian Johnson: I think I think I think we just need to give it some thought, Mike, in terms of you've had a very clear vision for the type of alerts and I don't want to come away from the the design and the principles because I understand that they make complete sense. I know what the drivers are of of using the alerts. Um it's it's how best to deliver them. Um and whether or not in doing that we might have to tweak some or take a slightly different view on how we would do those things. Um so that we we're not creating a behemoth of a an alerting and rule system that exists within uh within DT that ultimately um would just feel a little bit old-fashioned to me. And again, I think it I think the the point with an alert to me is it's just what if you've got a dashboard of all of the most important KPIs or metrics that a client wants to see in their program.  
   
 

### 00:52:18

   
Ian Johnson: The alert thing is typic well the way I think about alerts is yeah but if I'm not looking at that and I miss something I want I want to know that this has this has happened. Um it to to me it's not that every day within the dashboard you can have a KPI or a metric that says your you know decline rate was 5% 5% 5% and then on a day it show shoots up to 20%. The thing is if I didn't look at my dashboard I wouldn't have known that it jumped up to 20%. So we want to tell you Mr. Bryant that this has happened. Now the question is how do we do that in the most efficient way possible? How do we avoid building a huge behemoth of an alerting and rules engine for something that ultimately is shouldn't be so  
George Westbrook: That's the  
Ian Johnson: complicated.  
Brett StClair: Watch out.  
George Westbrook: threshold.  
Ian Johnson: But we need to we need to give it some consideration. Mike, I think it's just one of those when when are we planning this whole piece?  
   
 

### 00:53:45

   
Ian Johnson: Because again, I think some of it is about the timing of it. Bearing in mind, let's say it's CL, let's say client one, Mike, they don't have a huge volume of transactional information. And I'm just going to deal with the alert stuff. So what are the alerts that for a for the first client or any client actually but with a limited number of understanding there's a limited number of transactions what are the types of alerts that we'd want to raise them to that they're almost all entirely associated with critical degradation of something and as I think you mentioned earlier Mike it was the kind of decline thing being First and first first and foremost the fact that your transaction volume is  
Michael Moores: Yeah.  
Ian Johnson: down 20% versus a previous day. I think we just have to understand if that if there's not a way of easily and cost effectively allowing a client to do that um with with AI and not having to build a ton of stuff. Then is it really our place to do it? And are we are we really delivering material value on having that alert available?  
   
 

### 00:55:13

   
Ian Johnson: if we're providing dashboard and we're giving the clients all of the data that they they've all they've got the data anyway. So I think the thing for me is we've got to really understand where can we add material value over and above what they can already do themselves without my critically avoiding the Marqueta approach to things which is well you can just build that yourself has been a fundamental design philosophy of of mics that we don't want to go down that route because clients don't like that either and I suppose the thing was that the AI was the idea with AI was it was almost a bridge to you don't have to build it yourself. There's stuff that you can do in the console if you don't if you want to go down that route. Um if you've full API your data and you're going to build the whole thing yourself you can do that. And if you want somewhere in between, which is you don't really want to go in and and use the console in a more traditional way, but you do want some kind of interface provided by TXM to do some of these things, then how does AI work to allow that to happen?  
   
 

### 00:56:33

   
Ian Johnson: But again, it's it's it still again doesn't need to be total free form of you can do anything and everything because that's not what we're attempting to be. Um, and I suppose that's where it comes to. It's like the AI isn't so it's API and your own data. You can do whatever you like and it's all at your console will provide. You still have to pay for it, but there's a limited number of things that you're able to do within the console, just more than competition. AI wasn't designed to be, oh, and the AI thing is do whatever you like. Fire away, ask us anything, we'll pay for it, and it'll only cost you this fixed amount per month. That is not what it is. And I think that's the bit that we need to be somewhat mindful of.  
George Westbrook: edge  
Brett StClair: It's just how you release and expose what those mechanisms  
George Westbrook: control.  
Brett StClair: are.  
George Westbrook: And so that's the discussion.  
Brett StClair: What do you want to enable them to do through those components?  
   
 

### 00:57:38

   
Ian Johnson: Yeah.  
Brett StClair: And it gives them quite a bit of depth on what they can do, but you're also capping it. And I think some real thought needs to go into it. Now what we're also fans of is you don't need to think of everything up front because a lot of the times in these cases the user is going to drive things and so we can start to monitor the kind of queries that they're asking where we're stopping it or where there isn't a net for us to catch it in. And then we go great guys we've got this. Do we want to quickly build it out? Do we want to enable this feature? So that's also another way to think of this AI world. You know, traditionally in normal digital interfaces, you're trying to picture what the whole world looks like, but you've got this fairly open net. And if you try to think of everything you can or can't offer, my worry is you end up building too much that isn't used.  
Ian Johnson: I think the challenge we've got there, Mike, is is how we knitting it in with the console in particular.  
   
 

### 00:58:53

   
Ian Johnson: um what are we expecting AI to deliver as part of the console experience that at the moment is the priority purely on the basis that it's going to hold things up as I understand it if we don't start and work our way through making those decisions and quickly because people are are wanting to understand that Um because the rest of it, Brett, I I don't disagree with you. Um we don't know yet how people will want to use it, but we do know that we've got more more important things and this  
Brett StClair: Yeah, it's clear.  
Ian Johnson: and we have to be considered about how far we want to go. Okay. What we're saying is you can do any of the you can do anything you like with your data because we will give you the data do what you like right and that's our our role in that is giving you the data in a timely real time manner which we're going to do through web books and reporting or whatever else it is and it's and it's your data do what you like so with TXN if that's what the way you're minded you can do that I think what we serve up as an AI Id driven experience can't it can't be that it can't be we've got all your data come to us we'll do you can do anything you want with us as I said before and you know it's going to cost us all the money to do it it's just not that and I think just listening to it and trying  
   
 

### 01:00:36

   
Ian Johnson: to think it through it's the it's the alert thing that seems to be the biggest issue. And I can see one thing that I said George about just do this once this thing runs once a day and if it's above this percentage you know what I can see that that's somehow a way of managing it. Now the only difference on that one is if you scheduled a task to run every day and then pull back the results. If I didn't look at the for for whatever reason, I didn't look at the results, then I might not know it was over 20%. But to to even simplify it even more, Mike, I'm I'm taking it outside of the console. I run it every day. It gives me the results back. It delivers the results to Slack or wherever or Teams and there you go. So, we ran it and we put it where you wanted it to be. It's your job to determine whether or not the percentage or whatever the metric was something that you should take action on within an experience where you've asked us to just give you information on this particular piece.  
   
 

### 01:01:54

   
Ian Johnson: I think that's the we're trying to get this balance of delivering something that's a differentiated and valuable experience to clients without creating something that is ultimately um you know une  
Brett StClair: I  
Ian Johnson: uneconomical and the other thing is that actually people that were really interested in that stuff probably wouldn't use us for  
Brett StClair: Oh,  
Ian Johnson: it anyway. They're probably the type of people who want to deeply analyze their data and set up a bunch of alerts and all of those kind of things. Are they really the type of people that are going to do it with us rather than just, you know, interrogate their own data with their own AI  
Brett StClair: It's like the lower end user,  
Ian Johnson: tools?  
Brett StClair: the user that's not interested in that, that knows very little about cards. They might benefit from a more smart notification system. That is helpful. That is saying, you know what, you know, you're probably not aware of this, but you've been running at 20% for the last two, three days. We've sent you the report, but that's okay, but we are highlighting it to you.  
   
 

### 01:03:04

   
Brett StClair: It's a bit like if you look at the high-scale digital providers uh on email, right? They have smart email and that smart email is trying to float the most important email to you in a central box and you know I can see that thinking going actually more to the less experienced user. The more experienced use I agree I think get them the information if they want to use it or not. Cool. they the expert that are there to use all of it and will they go there or they just go into your console those experienced users and consume the dashboard and drill into it and surely they'll be monitoring it every day. Maybe it's just like just seeing where that fits in your type of user and you bring different smarts thinking to those two users. It's a terrible term by the way.  
Ian Johnson: I so obviously not going to fix it now and conscious the fact that we've we've  
Michael Moores: Oops.  
Ian Johnson: gone over but I think the thing to think about really is are we trying to deliver what is a pretty typical approach to supporting clients but just trying to do it using AI versus are we trying to deliver an AI first experience to clients to allow them to manage a card program.  
   
 

### 01:04:37

   
Ian Johnson: So we we talked about we got this mindset of alerts and let people know when this happens all those kind of things. Those are the traditional things that you would do. The mechanism, we talked about two mechanisms. Traditional software are doing it via AI, but we're still doing the old thing with AI and maybe better, right? Because we've I know it's a more extensive thing that you're thinking about. Um, I just don't know that it's the thing that moves the  
George Westbrook: It's a nice guiding  
Ian Johnson: needle.  
George Westbrook: principle.  
Brett StClair: Are you an AI first product or are you wanting to leverage AI where it counts? And there's nothing wrong with either. I think it can be both.  
George Westbrook: like because you're just trying to make things complicated again. No,  
Ian Johnson: I  
George Westbrook: I because there's because it's because I think there's the the  
Ian Johnson: don't  
George Westbrook: traditional approach is what the traditional AI approach is let's bolt AI onto something that you already had. So say most program most things they've got some way of surfacing alert.  
   
 

### 01:05:56

   
George Westbrook: Um so the kind of bolting on approach is there is this alert we get AI to analyze it and we give you like an impact statement or some analysis which still does provide value. Um but what like what do you want out of that alert in an AI first experience is here's the analysis here's what I think we need to do. Um do you want me to do it? Yes I want you to do it and then it's done. Um because I suppose what when people get alerted to things that let's say it's an alert where it needs a change, they're going to go have to do that change themselves, but then they're going to have to think, okay, what do I need to do? What page do I need to go to? What button do I need to click? In an AI first experience, they don't need to do any of that. They just need to read it, say, yes, this is what I want to do, and it goes away and does it.  
   
 

### 01:06:38

   
George Westbrook: Um, and I think we can achieve both of those. Um but but I think they're both they both need some maybe traditional software engineering to surface that alert. Um if it needs to be captured at the point at which that issue has happened or there's the let's do it on the the timebased cadence of twice a day that that doesn't need the traditional software engineering because it's just done on a schedule.  
Ian Johnson: I I I I think you're on to something there, George. I I do think it comes down to what are the critical alerts that the time based and when do we need to make them? And to to be perfectly honest, I think those things are are more geared towards the traditional software thing that we will alert you when these things happen. Okay? These are things that we think are important and let's be clear about it. They're important because we feel obliged to tell you because we really think you should know this. And quite honestly, in a lot of instances is if we don't tell them, it's going to cause issues to us in two ways.  
   
 

### 01:07:48

   
Ian Johnson: Number one, their program stats are going to go down and that cost us real money. Or number two, they're not going to know. They're not going to do anything about it. And then there's going to be a s*** storm when they realize and it's going to on our door to fix it. And there be something like, well, why didn't you, you know, we didn't know this had happened. If I just to I know it's more nuanced than that might be but just part those ones there as the things we really feel that you should know. The the other part is actually all of this breaking things down into alerts is not a real world AI experience because for me if I'm the program owner of the cloud program I don't want you to tell me a little bit about my program that's 20% increase I want you to create every day to create me a summary of program performance versus the yes the previous whatever because if I was preparing for a if I was that pro car program owner using AI let's say that even just just Claude has got basically I every day I pump all of my program stats into into Claude and then I just say okay I have a exec team meeting I need the analysis of the of the car program this week, this date versus previous week.  
   
 

### 01:09:21

   
Ian Johnson: Here are all the key things that you need to be aware of. That's actually what I mean by not thinking about the old world of doing something. Whereas there's an alert and then me goes and looks at the data and finds out okay what do what do I need to tell people? what do people need to be aware of and how do I provide that in a in a way that kind of gets whatever it is what the next step is from that particular thing done. So I think we we just need to take a a bit of a step back to determine what is it that we're trying to achieve because they're different things. One of the thing is we want you to know on this point thing that this has happened. The other thing is when do you want to when do you want our analysis of what's happening with your program and the things that we think you should be really be aware of and that's scheduled that's set up as a scheduled task to run whenever you ask us to might be that you've got your executive meeting every Wednesday.  
   
 

### 01:10:27

   
Ian Johnson: So every Tuesday you want this thing to run and you want a perfectly you know written summary of exactly what's going on with what's and and within that what are the drivers behind the fact that your transaction rate has gone down by 20%. Now the drivers are that your your decline rate increased by 20%. And that was because you changed um the maximum transaction limit from two from 400 to 200 on this date. That's that's the real s*** for one of a better  
Brett StClair: Yeah.  
Ian Johnson: expression.  
George Westbrook: that that I could just think there it'd be we just have loads of so main orchestrator agent and then loads of different agents or agent teams which specialize in certain in certain things which the agent would speak to give the research plans it go away it do the analysis it's kind of siloed bring it back up aggregate the report present it to the user I mean that's it you can go a step further right volatility That's  
Brett StClair: when you hit those thresholds even on the dashboard should be floating through the AI recommendation on a little dot on that dashboard.  
   
 

### 01:11:45

   
Brett StClair: So they can look at it and it actually says the reason why this is spiked is because of this action or the reason why this is dropped. Surely we can do something like that, right? But then the AI would need to  
George Westbrook: alerted that that has happened in order to do the analysis.  
Brett StClair: be  
George Westbrook: Yeah, the alert has to come through to the I think keep thinking this is like a it's more like an information  
Brett StClair: presentation layer. It's bringing through information at different points of real time granularity and what we're trying to deliver to the end user is insight packaged at the right time. And so is it always an alert? Maybe not. Is it always a notification? Maybe not. Is it further information being embedded into a dashboard? Possibly. And it's just understanding what those mechanisms are and then using AI in the right way. I suppose you're spitting it into her left  
George Westbrook: reporting really I suppose alerting in my head is this has just happened let me tell you reporting is more I suppose I've done this I've uncovered this you need to be aware of this you might want to do that I mean there's still going to be alerts in there but it's not at the point at which it happens I  
   
 

### 01:12:53

   
Ian Johnson: Yeah.  
George Westbrook: mean  
Ian Johnson: And taking that final part, George, the bit where you said, "You might want to do this. Do you want me to do it?" Okay. That that is the that's the the thing.  
George Westbrook: Yeah.  
Ian Johnson: And I think we just need to think more along those lines. Mike Mike's always quiet in meeting so it makes me very disconcerted because he's probably thinking what the is he talking about? That is not what I'm thinking. But I I just think we need to take a we just need to think about this because ultimately I fear we could end up not really moving the needle very much. I don't that principle Mike of alerting somebody to something that's happened making a recommended action and then allowing them to take that action remains in place with the agentic AI it's really getting to a point where the at the end of it and we'll do it for you.  
George Westbrook: But but that's both in the reporting and the alerts like that take the action do it  
Ian Johnson: Yeah.  
   
 

### 01:14:04

   
George Westbrook: can sit in in both of them. I suggest this  
Ian Johnson: Yeah.  
George Westbrook: be  
Brett StClair: not to this to this at the end of the session uh of the components and we talk through some of the scenarios just to give you guys some time about scenarios that you have in mind.  
Ian Johnson: Yeah. Works for me. Are the other ones going to be easier than this one?  
Michael Moores: Yep.  
Brett StClair: Okay, this is the point of these conversations,  
George Westbrook: Get  
Brett StClair: right? try to do it as conversations cuz we need to get into the crux of it and then we get into further detail when we do the subm modules but we're going to be relying on II tools to help us with that and then once that's all done then the whole point of this is to be able to get you essentially a backlog and this backlog then becomes a Gentai bill friendly as well as human friendly  
Ian Johnson: Okay, let let's not lose sight of the thing that's on the critical path, which is the console. Um, and some, you know, I can see that some of this bridges into how we deliver some of the things that we've imagined in the console. So we need to think about that without losing sight of the of a broader vision of stuff. But yeah, let's follow let's follow  
Michael Moores: The one thing we need to do is um we still need to finalize the consult MVP.  
George Westbrook: Yeah.  
Ian Johnson: up.  
Michael Moores: So I think that will drive this as well. There's a few outstanding items.  
Brett StClair: Yep.  
Michael Moores: So I think we'll we'll push on that and get that finalized. We can at least tell you the priority order on these things as well.  
Ian Johnson: Is that the session tomorrow? like okay.  
Michael Moores: Uh yes, I think  
Ian Johnson: All right,  
Michael Moores: so.  
Ian Johnson: sounds good.  
George Westbrook: Perfect. Thank you very much.  
Ian Johnson: We go lie down in a dark room now. Catch you later. Cheers.  
Brett StClair: You like that?  
   
 

### Transcription ended after 01:16:24

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

**