---
date: 2026-11-12
type: standup
description: "Launch settled: Knowledge Hub live Monday 16 November, press release on the 17th; the DPA is due 13 November and retention is 72 hours"
scope:
  - "[[delivery]]"
  - "[[commercial]]"
  - "[[portal-co-pilot]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[commercial]]"
  - "[[portal-co-pilot]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-11-12)

> **Source:** transcript from Lily's app, Thursday 12 November 2026, 14:30, about 22 minutes. **Novosapien:** George Westbrook, Brett StClair, with Hasan Ahmed in the room. **TXN:** Ian Johnson, Michael Moores, Dörte Dye. The recording starts mid-sentence, with Michael on prioritising the JWT work so Novosapien's credentials are right.

## Launch: live on Monday 16 November, press release on the 17th

**Both dates were right.** Michael, having spoken to Ian that morning: *"Monday morning we'll be putting the Knowledge Hub live with the website as well, obviously, then press release the day after."* So **go-live is Monday 16 November** and **the press release is Tuesday 17 November**. Little traffic is expected on the Monday.

**Order on the day:** the Knowledge Hub goes **an hour before the marketing website**, because the Microsoft side takes about 20 minutes to deploy and half an hour to refresh. Ian has Visa and then a board meeting on the Tuesday.

## The data processing agreement, due Friday

**Brett is drafting it** and will have it to Ian on **Friday 13 November**. Ian: *"we do have to have that in place before we launch and **somebody from our board is going to need to sign it**."* Brett is building it from standard clauses and George's analysis, which links each point to its GDPR source. He is aiming for seven or eight pages. Ian: *"Well, it won't get read."*

**What it has to cover, in Ian's words:** *"how the security measures are in place for the host, the temporary hosting of the AI service and obviously the handling of the IP address and random ID and the chat stuff."* And *"what is classed as personal data for that period."*

**DT's 17 pages are not needed for launch.** Brett was reviewing a 17-page DT document with 33 questions. Ian spoke to **Charles** the day before: *"nothing is needed for the 17th... they're all systems go."* Ian dismissed most of the document as one DT person showing off: *"that's not the immediate ask. So don't worry about having to address all of that in this agreement."*

## Retention is 72 hours

**Ian set out the basis for the agreement:**

> *"There's a random ID that basically can be linked to an IP address, and there's an ID for the chat. Those things are **retained for 72 hours** within the session and then they are dropped. But the chat stuff, borrowing without any personal identifier can be moved into your long-term storage... **that's the basis of what we should be writing the DPA around.**"*

He added that the length makes no difference to whether GDPR applies: *"The fact that it's retained for 72 hours means it's fully in GDPR anyway."* This settles the figure for the agreement against the 24 hours Dörte was going to give the lawyer on 10 November. See #131.

## No cookies

**George answered Dörte's email**, which came from a question by **Lara**, TXN's lawyer. Nothing in the browser is a cookie:

| Item | Where | What it is |
|---|---|---|
| Docs session | Session storage | The random ID |
| Docs thread | Session storage | The chat's ID, not linked to the user |
| Co-pilot layout | Local storage | Docked, floating or expanded. Can be removed |

Keeping the ID for a long period in local storage was where the concerns were, so it moves to session storage, and the random ID is cleared from the browser and from the database link to the chat.

**Ian's line for the privacy policy:** don't mention cookies. *"We store a random ID for the session, an ID for the chat, and the IP address. They're dropped after 72 hours and that we've got the back-to-back agreement with Novo to manage that."* A separate letter already agreed with DT covers IP addresses and the public sandbox logs; Brett's draft will be checked against it. Ian: *"too many cooks... people are not involved in the operational reality conversations."*

## What is left before Monday

George's list:

- **`llms.txt`**: downloadable now, being changed to serve at its own address, done within two or three hours. It is **dynamic**, built from the published guides like the Docs MCP server.
- **Production Umbraco credentials**: not received yet. Switching from staging is the same process.
- **DT's production sandbox credentials**: awaited.
- So *"really all it is is just switching out some credentials on those two points."*

**The click-and-go failure is one endpoint.** Michael checked them all: only **creating a card product** requires a unique name. The Knowledge Hub fix adds a timestamp to the name. Michael: *"something we have to consider as we add more unique validations later."* Novosapien had not hit it in testing, possibly because staging and testing behave differently.

**The public sandbox is locked to IP addresses** until go-live. Novosapien must send **the IP addresses that will call it**, so it can be checked first. The lock comes off on Monday. Michael has access from his IP and can add George's.

**Umbraco webhook:** Michael sends the details needed and sets one up.

**Stackworkz flagged one URL** that Novosapien had not allowed, so a test failed. It is now allowed, and George took it as a good sign that the limits work.

## DT release one endpoint at a time

Michael: DT are *"pretty much done"*. They release endpoints to production one at a time rather than as one release. **Authentication goes first**, because it blocks George, and is done by the end of the week. Then each tested endpoint follows. Stackworkz are testing the complete setup in Dev. Ian confirmed this is everything needed for the Knowledge Hub in DT's environment to call the AI hosted by Novosapien. See #129.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Go-live Monday 16 November with the website; press release 17 November; Knowledge Hub an hour first | [[delivery]], [[index]] | Callout added; launch flag closed |
| DPA due 13 November, needed before launch, board signs; scope is temporary hosting and personal data | [[commercial]], [[open-questions]] #103 | Callout added; row updated |
| DT's 17 pages not needed for launch; Charles says all systems go | [[commercial]], [[open-questions]] #129 | In callout; row updated |
| Retention 72 hours, then sanitised chat to long-term storage | [[open-questions]] #131, [[portal-co-pilot]] | Row updated; callout added |
| No cookies: session storage for IDs, layout in local storage; privacy policy wording | [[portal-co-pilot]] | In callout |
| `llms.txt` dynamic; prod Umbraco and sandbox credentials awaited; IP allow list; webhook | [[delivery]] | In callout |
| Click-and-go: only the card product endpoint needs a unique name | [[delivery]] | In callout |
| DT release authentication first, then endpoint by endpoint | [[delivery]] | In callout |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Send the DPA to Ian | Brett | Friday 13 November |
| Sign the DPA | A TXN board member | Before go-live |
| Serve `llms.txt` at its own address | Novosapien | 12 November |
| Send production Umbraco credentials | TXN | Before go-live |
| Send production sandbox credentials | DT, through Michael | Before go-live |
| Send the IP addresses that call the public sandbox | Novosapien | Before go-live |
| Send the Umbraco webhook details | Michael | Before go-live |
| Release authentication to production, then each endpoint | DT | End of the week |
| Remove the co-pilot layout preference from local storage, if needed | Novosapien | Not dated |
| Knowledge Hub live, an hour before the website | Michael, with Novosapien | Monday 16 November |

## Transcript

# TXN - Agentic AI SU

Thu 12 Nov, 14:30  
Client: TXN

**Michael Moores** (0:00): While. So they've proven it. Just not done it for a while. So yeah, prioritizing the JWT stuff so you can get your credentials perfect and then obviously

**George Westbrook** (0:10): we'll pull everything else over. Yeah, it's a good one. Yeah. Don't say was it? Yeah. Today, tomorrow and Monday. And I suppose this, the website's going up on Monday as well, isn't it? So

**Dorte Dye** (0:22): it's Brett joining or. Can you give me good news how. There he is.

**George Westbrook** (0:28): He's there.

**Dorte Dye** (0:33): He looks a bit lost.

**George Westbrook** (0:35): He's. He's. I think they've just come up with a. They've just done a joke brainstorming session. So yeah, they thought preparing all the, the jokes that he's

**Dorte Dye** (0:45): going to come up with. Are they basically scripted? I thought he was an original.

**George Westbrook** (0:50): No, I think, to be fair, I think only Brett could come up with

**Michael Moores** (0:52): those.

**George Westbrook** (0:57): How are we doing, Ian?

**Ian Johnson** (1:00): You know.

**Dorte Dye** (1:01): Oh, okay. That's problem one.

**Michael Moores** (1:06): That's the

**George Westbrook** (1:06): most beautiful, beautiful camera angle I've ever seen of you.

**Ian Johnson** (1:11): Who are we talking

**Dorte Dye** (1:12): about? Brett. Oh my goodness, look at all of the screens, George.

**George Westbrook** (1:20): Yeah, it's still connected to his phone. When we, when we do our stand ups, there's one guy who joins remotely. So we put the, we'll put the phone up in like the corner up high so he can see everyone. But then every once in a while it's still connected to Brett's phone.

**Ian Johnson** (1:39): All good.

**Brett StClair** (1:42): Ian, I saw your note about the contracts. I'm working on them at the moment. I'll just do the DPA section of it and I'm currently reviewing the 17 pages from. From DT. So.

**Ian Johnson** (2:01): Sorry, the DT 17 pages. I spoke to Charles yesterday and what he said to me is nothing is needed for the 17th that they're all systems go. I'm not. I think the DPA basically needs to deal with how the security measures are in place for the host, the temporary hosting of the AI service and obviously the handling of the IP address and random ID and the chat stuff. Stuff that's the primary thing there. But all of the detail there. The document was very misleading, I've got to be honest because when I got it and saw 33 questions I was like, what the fuck? This is easy. But it is a bit of. Close your ears, Lynnie. It's a bit of a dick swinging from Vinny, I think just being puked up all over a page. Willy swinging

**Dorte Dye** (3:06): his willy.

**Ian Johnson** (3:12): But that's not the immediate ask. So don't worry about having to address all of that in this agreement. What we really need to deal with is this short term hosting solution and how we're managing that. What is classed as personal data for that period. Okay,

**Brett StClair** (3:33): I'm gonna have something for you tomorrow. I think I'm just going through. We've got a bunch of standard clauses. George has sent me through his analysis on everything and now it's just pulling it all together and get the word right. This is a lot of, you know, you change, you make changes. You've got to read through everything and make changes. Read through it. So it's just a

**Michael Moores** (3:50): bit of. It's a bit laborious. It's

**George Westbrook** (3:53): got the sources to the GDPR policies as well. So it's not like it's. Yeah, it's like, okay, this part is from this part. Here's the link actually to it. Not some random AI going, yes, you can store as much information about you want from the user. I found this page which doesn't actually exist.

**Ian Johnson** (4:12): Yeah, no, I appreciate that. If I hear those four letters again after next week, I'm gonna blow my brains out. Yeah,

**George Westbrook** (4:22): That's. That's the fun part. Not building stuff. It's the GDPR stuff. I

**Dorte Dye** (4:27): think we have other four letters and the next door comes when the customers on board.

**Ian Johnson** (4:35): I don't know. Anyway, it is what it is. But if you can get that to me tomorrow, because we do have to have that in place before we launch and somebody from our board is going to need to sign it apparently. So, yeah, just yet more bureaucracy, but there you go. It is what it is. Let's talk about the fun stuff. Oh, I've got, I've.

**George Westbrook** (5:01): I've got. Got maybe one part which isn't. Isn't as fun. It's. But it's a good answer. But it's not fun thing to talk about is the cookies and the email you sent, Dorte. So there's. There's not any cookies, but there's three things that are in the browser. They're not cookies. They're not cookies. One is the docs session, which is that random ID, but it's in the session storage, not on local storage. Then there's the docs thread, which basically the ID for the session, which is not inherently linked to the user that's in session storage, and the only thing that's in local storage is something that we can remove. It's not really going to have an effect, but it's basically just the layout of the copilot. So if, if they like it docked or floating or expanded, that's the only thing that's stored. Can get rid of that if needed, but it shouldn't. It's. Yeah, I don't

**Ian Johnson** (6:01): think anybody cares what people's preferred choices of layout when it comes to personal data or I don't, anyway. And then the other two are going to be covered off by, by this DPA anyway, aren't they? What were we getting into

**George Westbrook** (6:18): cookies for? So they're saying they're not, they're. They're not technically classed as cookies then. They're not in local storage, they're in session storage, which when we were looking at it yesterday, it's when it's in local storage and when we're keeping the ID for a long period of time, that's where. What long? Not too long. That's where there were the issues. But we'll move it to session storage, which alleviates any of those concerns around and, and then the clearing of that session, that, that random ID from both the user's browser and from the chat in the database linking that chat to

**Ian Johnson** (6:57): them. Look, you can see on Brett, by Brett's face that he's been working on contracts and GDPR today. Look at it. This is not what you signed up for, is it, Brett?

**Brett StClair** (7:10): I was saying to George this, when I relate it in my desires, I relate it back to my days of rugby and the one thing I could never do was kick a place kick because I was a lock and an eighth man and you can imagine I kicked like that. And sometimes I feel like they're doing content.

**Ian Johnson** (7:35): I think it's much worse than that. You're just talking about something you're not very good at and nobody would ask you to do anyway. This, you've got no choice but to do. You've got no choice. Right, let me just put this in practical terms because I don't know where the cookies bit's come from. Dorte, aside, I don't know. That's

**Dorte Dye** (7:50): from Lara's last email where she wanted to have some extra qualification clarification. If they're technically not cookies, then honestly, it

**Ian Johnson** (8:01): doesn't. It literally doesn't matter. But let's just break this down. At the end of the day, this is going to have to be covered under DPA with Novo Sapien. Anyway, if we're talking about the privacy policy, then ultimately how we. I mean, a cookie basically is only a. Data is data that you're using for storing and using. And we're not. We're still storing and using the random ID and the chat ID that I just want to make sure, completely clear that's what it's talking about. By the way, how long it's retained for makes not an iota of difference. The fact that it's retained for 72 hours means it's fully in GDPR anyway, so it doesn't really matter. But as I understand it from what we talked about yesterday. There's a random ID that basically can be linked to an IP address, and there's an ID for the chat. Okay. Those things are retained for 72 hours within the session and then they are dropped. But the chat stuff, borrowing without any personal identifier can be moved into your long-term storage to be used for tracking, well, for improving model performance or whatever else. Yeah, yeah, that's, that's the basis of what we should be writing the GPA around for this, for this particular point. It's just there's too many, there's, there's too many cooks involved in this whole thing and too many things coming back where people are not involved in the operational reality conversations. So if we, whatever we need to call out in a privacy policy for the website, Dörte's, if that's where she was looking at it, we can just not mention cookies and just talk about the fact that we store a random ID for the session, an ID for the chat, and the IP address. They're dropped after 72 hours and that we've got the back-to-back agreement with Novo to manage that. And then from your perspective, it's anything to do with GDPR and how you are adhering to them, and then the kind of security provisions that are in place in terms of how you actually handle the data itself. There's a letter that we agreed, we've got agreed with DT, which is, which is different. It's really about then the IP addressing the logs from the public sandbox. But whatever you put together, we'll just check it against that. It doesn't have to be the most complex thing in the world.

**Brett StClair** (11:06): I was going for about 7, 8

**Ian Johnson** (11:07): pages. Well, it won't get read. I

**Brett StClair** (11:13): want to keep it as tight as

**Ian Johnson** (11:14): possible. Okie doke. So where are we in terms of actually being able to put this thing live? So the LLMs

**George Westbrook** (11:27): txt. Mike, so there is the LLMs Txt, which is available to download on the current version, but it needs to be changed so that it's just there. Be done two or three hours time with all of the routing, all that necessary stuff. Then there's the, the prodom Braco, which yeah, that was the confusion between me and Hassan where it was, I think we've got the URL, I think. I think have we got the credentials now? No. So I'm not. I don't think we got the, the credentials for the prod, for the prod version, but obviously it's same, same process regardless if you're on stage and testing or prod. It's just a matter of switching them over. And then the, I think the only thing we're waiting on from DT is the, the prod sandbox things, which obviously you mentioned was like was going to be coming over soon. So really, really all it is is just switching out some credentials on, on those two points. And then the only call it net new thing is the LLMs txt, which is so very, very, very simple, and it's. Yeah, it's just a matter of serving some, serving some text, which will be the exact same text that's in the guides. So similar process with the LLMs txt as it is for the guides, and it is for the Docs MCP server in which it's only going to show what's on the guides if it's published. When it changes, it changes as well. So it's not a static bit of text that's behind some URL, it's dynamic like everything else. And I think the only other thing which you mentioned was that the click and go ID thing, which we've, we've not encountered an issue in testing and we're doing some more tests today and we haven't encountered it, but that might be because we're, we're on the staging and testing environments. So when it gets, when it gets to production, once we've got, once we've got that access, it will, we'll be able to see. But I mean, in my head, if it works on staging, it works on testing. I don't like to use the word should because it's very like, oh, it should do. But obviously once we've got the credentials, we can, we can have a look, we can see, and then we've got Thursday, Friday, Saturday, Sunday if there's any issues. Yeah, that's perfect. We

**Michael Moores** (14:13): went through them all and it's only ideal endpoint and the only one that doesn't do a specific check. Switch products. So the name of the product needs to be unique. Yeah, we're doing in the knowledge, or we're just putting the current time basically in the, in there. So it creates the same car product with specific timestamps so as it keeps going, it'll always create a brand new one. So that's The. Yeah. Fix that they've found in the Knowledge Hub anyway. Oh, perfect. The rest of the endpoints are just ID to the moment. So it was something we have to consider as we add more unique validations later. But that's all it is for now, which is lucky. So yeah, we'll get that tested on our side and obviously run through that and let you know then. I think the public sandbox is locked down at the moment before we go live. So if we want to validate it before they've asked if you've got your IP addresses of what's calling the public sandbox from your side, just so you pre-validate that before we remove the blockers on. Yeah, so need

**George Westbrook** (15:23): the. Need the IP addresses of the thing that's going to be calling the public sandbox and you need us. Okay,

**Michael Moores** (15:29): yeah, we'll get there just to test that. So obviously for today, tomorrow should be in ready. Small fixes might be going on top from DT, but it should be in production from our side. Ready from Knowledge Hub and public sandbox. And then I think we said speak to Ian this morning. So Monday morning we'll be putting the Knowledge Hub live with the website as well, obviously, then press release the day after. So we shouldn't get that much traffic on the Monday. We've not, but just making sure that's aware and that obviously lift that blocker on the Monday as well so we can undo that validation. So I've got access to it now with my IP, and obviously if you want access to it yourself as well, let me know your IP as well and I'll just get that opened up for you so you can actually see it as well and do some testing as that

**George Westbrook** (16:19): goes in. Perfect. Yeah, I think I'll say fingers crossed, it's all looking. All looking very good. Do you need a

**Michael Moores** (16:30): Umbraco webhook set up in the end?

**George Westbrook** (16:34): Yeah, yeah, I think, yeah, we will do. Yeah. And then just let us know what. What we need to give you, what we need to give you for that, and then. Yeah, we'll get that sorted asap. Yeah, I can grow.

**Michael Moores** (16:47): Set one up for us. It's quite easy. So I will send you the details it needs. It's pretty basic, and then we'll get that question. Perfect. Yeah,

**George Westbrook** (16:57): because I think there was only. There was only one thing that stack works flagged, which if anything was, what is a good thing was something to do with one URL and we hadn't allowed. We hadn't allowed it so they couldn't test one certain part. Obviously, the way we, let's say, fix it is allow, allow something. But the good part out of that is they were trying to access it and they couldn't because there's obviously those limitations in place. So I think. I think we've sent that over already and. Yeah, so all good. All good on that front. Perfect. Yeah. I

**Michael Moores** (17:32): say there's quite a bit on. Well, there will be some stuff on production as well for us to test, but as we go through this week, there'll be even more as I start pushing the guys this week as well. Yeah.

**Ian Johnson** (17:43): What about the DT side?

**Michael Moores** (17:47): Yeah, DT are pretty much done. So. But by the end of today, they should have obviously goes in the stages so they can release endpoints to production rather than a whole release. So the first one he's doing is the authentication, which is the blocking point for George and the team. And then they'll be releasing each endpoint that we've tested basically and making sure that works. But the priority is the authentication right now just to get that new connectivity and they'll have that done by the end of this week so we can actually start validating that

**Ian Johnson** (18:20): and testing it. Okay, so that will be everything that needs to be in place for the Knowledge Hub to call out to the AI service within DT's hosted environment. Yeah. And obviously the AI service being hosted at Novo. Yeah, I

**Michael Moores** (18:39): know they're testing it in the completed setup in Dev now. I think George messaged you about some issues they were seeing. So just sort of do that validation, checking in Dev to make sure everything's working there and then they'll obviously push all that code and everything to production and confirm it's working.

**George Westbrook** (18:58): Perfect. Do

**Dorte Dye** (19:00): we have a time when we want to set everything live? Do we agree on when we want to do that on Monday?

**Michael Moores** (19:07): No, we just. Knowledge just needs to go an hour before the marketing website. Yeah, it takes about an hour to. Well, 20 minutes to do, half an hour to refresh sort of thing on the Microsoft side. Perfect. And

**Dorte Dye** (19:20): I will have Bron on. No, she.

**Ian Johnson** (19:22): No, don't. Oh, she does. Okay. Don't worry about Bromin. That's all in hand.

**George Westbrook** (19:32): Have you got your bottles of champagne ready for when it's switched on? I

**Ian Johnson** (19:36): can never even thought about it, to be honest, mate, but drink a bottle of whiskey. I think I'm at Visa on Tuesday and a board meeting on Tuesday afternoon. So maybe a bottle of

**George Westbrook** (19:49): that. You know that like Apple one that looks like champagne. I remember I used to get it as a kid.

**Dorte Dye** (19:54): So you mean appetizer. No, I know.

**George Westbrook** (19:58): I always used to get it when I was in. When I was in France. It would be like everybody else would be having, like, sparkling wine, and me and my sister would be having, like, something that looks like champagne, but it's just fizzy apple juice. I don't

**Ian Johnson** (20:10): see the point of that. What's that? Cider, isn't it?

**George Westbrook** (20:15): Yeah, anything for, like, 4%. Still an alcoholic, really, isn't

**Ian Johnson** (20:18): it? Yeah, I agree. It's not.40 and single malt scotch, and I don't count it. Right. Are we good? I

**George Westbrook** (20:26): think we're good. If, like I said, if there's anything tomorrow, Saturday, Sunday, just let us know. And then, yeah,

**Ian Johnson** (20:38): I'll be sending Brett notes about where's my contract and GPA on a regular basis. It would be a terrible thing if we weren't able to set it live because Brett didn't complete his end of the bargain. You know, at least he's laughing. He's not even laughing fully. You can see it's through a pained expression.

**Brett StClair** (20:57): It is pain going through these things.

**Ian Johnson** (21:01): You only do it once. Yeah, I

**Brett StClair** (21:05): know. I have to admit, I. I do kind of also get where Dörte's been over the last three months, falling through those kind of. I think if

**Ian Johnson** (21:14): we had enough money, we should just buy everybody that we need. Well, almost everybody that we need for the setup, make them all part of our organization and all sat in Europe, and the whole thing would be a whole lot

**Brett StClair** (21:25): easier. Oh, gee. It is what it

**Ian Johnson** (21:29): is. Anyway, Brett, I will let you get on because I don't want to delay you from doing your fun exercise to get this contract done. George is really enjoying this. Occasionally to herself as well. So. Although all those years have been a Brett of a father, and Lily's enjoying watching you go through his pain now, and you get to sit

**George Westbrook** (21:51): right next to him as well. Oh,

**Ian Johnson** (21:53): dear me. All right, folks, we'll leave you to it. Thank you. Have a

**Michael Moores** (21:57): good one. Take care.
