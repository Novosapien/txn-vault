---
date: 2026-11-10
type: standup
description: "A week from launch: Novosapien's side finishes on 11 November, the browser calls the AI directly, Dörte tells the lawyer 24 hours, and the Console date slips"
scope:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[portal-co-pilot]]"
  - "[[co-pilot]]"
  - "[[commercial]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[portal-co-pilot]]"
  - "[[co-pilot]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-11-10)

> **Source:** transcript from Lily's app, Tuesday 10 November 2026, 15:30, about 22 minutes. **Novosapien:** George Westbrook, Brett StClair, with Hasan Ahmed answering George off mic. **TXN:** Michael Moores, Dörte Dye. Ian was not on the call.

## Launch: Novosapien's side done by Wednesday

**George now says the 17th himself:** *"getting ready for the 17th"*, and later *"17th is looking all good."* With Ian using the 17th since 3 November, both sides are on it, but nobody has said the 16th is withdrawn. The vault keeps the flag until George confirms.

**Where it stands:**

- **DT's key has arrived** and is being added. **Stackworkz have the token**; Ruan has it working locally. A PR from Stackworkz's .NET back end was rejected, so they are changing one or two things.
- **What is left to migrate** is the AI Resources page: the MCP server URL, `llms.txt`, and "copy page to AI". George: *"not big changes... the big one was the agent because everything else is relatively static."*
- **Everything on Novosapien's side, including Michael's updates, done by the end of Wednesday 11 November.** The rest hinges on Stackworkz getting their release out.
- **Michael:** Stackworkz's and Novosapien's PRs are going up to DT, and Stackworkz expect to clear DT's comments today.
- **George joins the DT and Stackworkz standup on Thursday 12 November.** Michael will move it from 8am to the afternoon, for a sync before the weekend.

George: *"maybe whereas a few weeks ago... some people were like well 17th or. I think it's looking looking in good shape."*

## The AI has been reading staging, not production

George thought the AI used production Umbraco. Michael: **production has three or four test documents and staging about 40**, so it must be staging. Michael is validating the documents and moving them to production this week, and will check the URL Novosapien hold.

**No webhook is set up for Novosapien.** Michael added a document and *"the AI didn't pick up my new document."* Stackworkz already have webhooks; Michael can set one up for Novosapien once given an endpoint. See [[portal-co-pilot]].

## The browser calls the AI directly, with no proxy

Novosapien and Stackworkz spoke on 9 November about how the Knowledge Hub calls the agent: **from the browser, or through Stackworkz's .NET back end as a proxy.** Stackworkz prefer direct: *"it's public anyway, anybody can use it. The rate limits are going to be there... It's not as if it's a shortcut."* George added that the agent talks to the front end over a WebSocket, so a proxy would need **two WebSocket connections** or a way to route through. **Michael: "Yeah, that's fine with me."**

So the public, ungated endpoint (#91) is now guarded only by rate limits, and no limit has been written down.

## Models, the lawyer, and retention

**Dörte asked to confirm the models:** **Gemini, with Claude as the backup, and OpenAI not switched on**, because *"OpenAI would be possibly going outside of Europe."* George: direct from OpenAI, yes, but he is *"like 95 sure"* the Azure deployments of OpenAI have UK and EU regions.

**TXN's lawyer wants low-level detail**, and Dörte will *"only give her what is true."* Then: **"we can confirm it's 24 hours hold."** Nobody corrected it.

> [!warning] Retention: 24 hours, 48, or 72?
> On 22 October chat retention was set at **72 hours**, matched to the sandbox data drop. George said **48 hours** on 27 October. Dörte will now tell TXN's lawyer **24 hours**. This is going into a legal draft. See #131.

**Data processing:** Dörte asked whether the agreement Brett signed with Ian covers data processing. Brett: **it is in the agreement, but it is not signed yet.** Dörte will flag it. The lawyer asked only about the LLMs, and the MCP server holds no personal data. The Console *"is a whole new beast"*, to be done from the beginning. #103.

## One-click examples, and the public sandbox

**Ian reported the one-click flow was not working.** Michael: the AI is using **poor examples from DT's YAML**, and one failure was a **duplicate ID**, a DT fix. DT redeploy today to fix the last YAML problems so a user can click straight through. **DT are pre-loading the public sandbox**, leaving out internal items such as real BINs, so the default works first time. The Knowledge Hub and the AI behave the same, which Michael called good.

**Michael has his own production access**, restricted to his IP address, to run validation checks as things deploy. The final checks on the new public sandbox, the same API in a separate environment, come after production.

## The Console date will slip

**After the 17th the priority is the Console:** permissions, skills by access level, testing, then UI and UX tweaks. George: *"it's not a quick task."*

**Michael:** the Console was planned for **later in November**, but *"we are probably going to push that one out."* Stackworkz were blocked on DT's APIs and are behind, and **the first client is also delayed**. Ian will set a proper target date once launch is out and the APIs are signed off. DT keep changing the APIs, so Stackworkz paused to avoid wasted work. The API UAT is **about 82 percent passing**, with a few validation and back-end behaviours left. See [[co-pilot]].

## London, 24 November

**A late lunch instead of dinner**, so everyone gets home at a decent time. Dörte arrives at King's Cross, Ian at Euston. **The plan:** a meeting at Novosapien's **Aldgate East office from about 10am**, a late lunch around **2pm near St Pancras** (Dörte knows a steak place), then a pint, and home by eight or nine.

**Brett writes the agenda:** ways of working, products to pitch, lessons learned, and **slides on a different commercial model**, which Ian asked for. Dörte: *"you know what that means... cheaper"*, since the shareholders are South African. Brett: *"I convert everything to Rands."* **Breakout groups:** Michael with George and the engineers; Ian, Dörte, Brett and Lily on the commercial side. See [[commercial]] and #130.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| George now says the 17th; Novosapien's side done 11 November; AI Resources page left; PRs with DT; George joins Thursday's DT standup | [[delivery]] | Callout added; launch still flagged |
| AI was reading staging Umbraco; no webhook for Novosapien | [[portal-co-pilot]], [[delivery]] | Callout added; open action |
| Browser calls the AI directly, no .NET proxy; rate limits are the only guard | [[architecture]], [[open-questions]] #91 | Callout added; row updated |
| Gemini main, Claude backup, OpenAI off for data residency | [[architecture]] | In callout |
| Dörte tells the lawyer 24 hours; vault says 72 | [[open-questions]] #131 | Row added |
| Data processing in the agreement, not signed | [[open-questions]] #103 | Row updated |
| `llms.txt` ships on the AI Resources page | [[open-questions]] #110 | Row updated |
| One-click failures from DT's YAML and a duplicate ID; sandbox pre-loaded | [[delivery]] | In callout |
| Console date to slip; first client delayed; UAT about 82 percent | [[co-pilot]], [[delivery]] | Note added; in callout |
| London: 10am meeting, late lunch, commercial model slides, breakouts | [[commercial]], [[open-questions]] #130 | Callout added; row updated |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Finish the AI Resources page (MCP URL, `llms.txt`, copy page to AI) and Michael's updates | Novosapien | End of Wednesday 11 November |
| Give Michael a webhook endpoint for Umbraco | Novosapien | Before launch |
| Move the validated documents to production Umbraco, and check Novosapien's URL | Michael | This week |
| Move the DT and Stackworkz standup to the afternoon; George joins | Michael, George | Thursday 12 November |
| Redeploy to fix the YAML examples and the duplicate ID; pre-load the public sandbox | DT | 10 November |
| Confirm which retention figure goes to the lawyer | George, Dörte | Before the draft is finalised |
| Write the 24 November agenda and the commercial model slides; book the lunch | Brett | Before 24 November |
| Confirm the launch date, 16 or 17 November | George | Before launch |

## Transcript

# TXN - Agentic AI SU

Tue 10 Nov, 15:30  
Client: TXN

**Brett StClair** (0:12): Are you okay? Hello? Mike. Hey, how are you doing? Why can I not hear anybody? It's just me. You just.

**George Westbrook** (0:34): You beat me to it, daughter. Damn

**Michael Moores** (0:37): it, you beat me to it.

**Brett StClair** (0:43): Oh boy, oh boy, oh boy. You know what that was, Mike? Until it was the volume on my machine. Oh my

**George Westbrook** (1:00): God.

**Brett StClair** (1:02): Oh. Can't get it to go through my AirPod.

**George Westbrook** (1:10): I feel like what we should start doing is set the calls at two minutes to when we actually want to do it and just invite Brett to the first. For the

**Brett StClair** (1:19): first Brett so pleased. I can't see George on my screen for some

**Dorte Dye** (1:27): reason. He said to find you. Right.

**Brett StClair** (1:35): Okay. Shall we jump into this? I believe the Net wants to do a demo for you. So he's going to take control and do the demo, I think. I'm just kidding. That was funny.

**George Westbrook** (1:54): Just throwing them in the deep end. Yeah. So I suppose obviously top of mind the getting. Getting ready for the. For the 17th. Obviously. Saw your email this morning. Might. I thought we just wait till this call to talk about it because I think the obviously got the key over from dt, so thanks very much for that. Get that. Get that updated. Get that added in. Correct me if I'm wrong, Hasan We're already using the production Umbraco, aren't we? Yeah, yeah. So we've got that set up that all working. What we needed to do has been handed over to stackworks as well. So they've got the token. I think they tested most of it their side. I think there was a PR that went in that got rejected, but that was from their dot net backend. So I think maybe there's one or two things they're changing on their end. But Ruan said he got it all working locally. I think it's just the process of getting it into that specific environment and I think the. In terms of our migration, I think the only part is that AI Resources page, which. Or AI integration page, which is just the MCP server and like the LLMs TXT stuff that we mentioned. But apart from that I say. Oh no, that was one thing. Obviously we spoke about the method of all of calling the. Calling the agent and between having it in either in the browser or in the. Or using the back end as a proxy. I think that we. We had a quick call with stackworks I think yesterday and they seemed pretty keen on doing it the. The first way. So not using the proxy because they were saying it's public, it's public anyway, anybody can use it. The rate limits are. The rate limits are going to be there. It's not, it's. It's not a risk. It's not as if it's a shortcut to get something out the door. So that, that would probably be their, their preferred way of doing it. And then after we realized that. So the way in which the agent communicates with the front end is via a websocket. So if we were to use the back end as a proxy, we'd have to have the front end having a websocket connection to the net back end and then another websocket connection or finding a way to route the request through and then have the connection from the front end directly to the AI service. But obviously doing it in the way that we. What the stat works are doing now, it's just direct connection, so it avoids any of those complications for stuff they might have to do. So as long as you guys

**Michael Moores** (5:02): are happy with that. Yeah, that's fine with me. Yeah, I think that makes sense. Obviously. The only thing for me is I'll double check the URL you've got. So I think the production one is empty at the moment. So I don't know if you've got how much documentation you've got right now. So I'll double check the URL for all brocker just to make sure. Yeah. You mentioned a webhook as well. I don't think we've set it up. Set that up for you yet. Because I was testing and obviously the AI didn't pick up my new document. So I think you mentioned a web hook side. I don't

**George Westbrook** (5:32): know if we said yeah. Or we

**Michael Moores** (5:33): need to.

**George Westbrook** (5:36): Is that on the. So it must, it must be using the testing then. Because if you say if that's right, that there's no documents on the production. It's got, it's got to be. Got to be the testing. There's.

**Michael Moores** (5:46): There's like three or four if that just a test. There's like 40 odd on the staging. So I think. Yeah, it may be just in the staging at the moment. Obviously we're going to start moving them across this week. So just validating them. Moving them across to. Yeah. The production. So I just wanted to make sure you had the web hooks on. Whatever you need to. Yeah, make sure you've got that. Obviously we've set up some for stack works as well. We can set them up for you if you've got that webhook endpoint. I can find the page to show you the details that would be there. I think that's it from a. Integration into sort of umbra point of view

**George Westbrook** (6:22): as it stands. Okay, perfect. Yeah. Sorry about. I thought. I thought it was the production one. So. Yeah. Staging. Get that sorted on production, the LLMs TXT stuff, the MCP URL and the, the copy page to AI stuff. We did we integrate that as well? Okay, yes. I think it's the. That's like. I think they're like two, two or three of the last things we need to migrate over which are not. They're not big changes. So we'll get. We'll get them sorted asap. Because obviously the big one was the agent because everything else is relatively static. So it's. Yeah. Just a matter of serving different pages which, which is all good. So 17th is looking. Looking all good. Can I just

**Dorte Dye** (7:24): ask one quick question with the model. So we have Gemini and Claude as a backup, but we're not switching on OpenAI. Right. We can do. Because OpenAI would be possibly going outside of Europe. So I think for the short term

**George Westbrook** (7:41): with. So with directly via OpenAI. Yes, but with the Azure deployments of OpenAI, I'm like 95 sure that they've got like I could, I could go 100, but I'm like 95 sure that they, they've got. Okay. Like UK and EU deployments. Our lawyer asked

**Dorte Dye** (8:07): now for very low level details. So I just want to only give her what is true. So yeah, I do these two and then there's a backup option if she asks and I give her the details and we can confirm it's 24 hours hold. And Brett, the agreement you have signed with Ian had the data processing in there. Right? Amazing. So then I just refer back to him.

**Brett StClair** (8:31): Not signed yet. Okay. So yes, it's in that agreement, but not

**Dorte Dye** (8:39): signed yet. Yeah. Okay, I will flag everything. Fine. Cool. And there was nothing else about the MCP server. Because the lawyer just asked about the LLM morsel. I'm just wondering from a data point

**Brett StClair** (8:58): I'll have to check. It was quite a big document and it was a while back. What would, what would the

**George Westbrook** (9:04): MCP stuff in that document be relating to? Because it's, it's. It's just. It's just kind of data in there. No,

**Dorte Dye** (9:13): there's no personal data. She just wanted to have the LLMs or just give her everything she needs that she is comfortable because she has to finalize the drafts and then we take it from there. And then the concept is a whole new beast. Where we start. Yeah, from. From the beginning. Yeah. Okay. No, that's Cool. Perfect on that one. Okay.

**George Westbrook** (9:36): Yes I think all of the stuff related to the 17th I think. I think we pretty much come just looking through your email again Mike. I suppose production deployment the. Well we've effectively got our. Our production deployment done obviously but it's obviously hinging a lot on on Stack Works getting getting their stuff out so I say that's the. Yeah and say we had that quick call with Ran and AR yesterday so just said to them as well anything in the meantime just give us a ping obviously we'll let you know what's going on as well to make sure make sure that it's sorted I mean obviously. Why? Well I think every. Everything on our side will be even those updates you mentioned done by end of tomorrow so 17th yeah it's. Yeah maybe whereas a few weeks ago we. Well I'm always quietly arrogant but maybe some people were like well 17th or. I think it's looking looking in good shape. Yeah yeah

**Michael Moores** (10:39): I think you're around mentioned today that I think theirs and your PRs were going up to DT. I think they had a couple of comments that stat works think they can get through today So I think that's going well with the DT side obviously we have joint calls with them and DT every day so what I might do is see we have a stand up on Thursday so it may be worth you joining that. Yeah I'll get them to move it because it's stupidly early because they're all in South Africa like 10 in the morning 8am

**Dorte Dye** (11:10): you can start

**Michael Moores** (11:11): George. That's fine. So it might be worth just moving that to the afternoon so we can have a sort of sync before the weekend if you will See where we're up to and go on there. We've sort of been doing some testing in the. The staging of just the. Obviously the idea of the. The knowledge was sort of one click. Ian fed back some feedback today it wasn't working and I think that's just because the AI is using poor examples from the YAML. Okay. Basically so.

**George Westbrook** (11:47): Your

**Michael Moores** (11:47): connection went there. Mike, my laptop is dying,

**Dorte Dye** (11:53): killing everything. Right. Have you updated it yet? Can you see us by

**Michael Moores** (11:56): the way? I can see you just about yeah. I lost my camera and

**Dorte Dye** (12:00): everything this before two days because he didn't want it to shut down the

**Michael Moores** (12:04): laptop. I've run out of memory. Not good. It's just pause clawed because it's crashed. Yeah Basically the knowledge hub and AI is behaving the same so that's good from that point of view DT are Going through and making sure the examples are one click. So the one issue Ian was having was a duplicate basically. So the same ID was being sent, which obviously is a DT fix. So they're doing another deployment today to fix the final YAML things to make sure we can just click all the way through. They're preceding the public sandbox, obviously there's some internal bits we're just not going to have. So real bins, for example, so preceding that environment with stuff. So if someone comes in they can just click it once and it will work. Having to change everything just to make it work. So the default will work and then we'll just obviously test that and make sure everything we need is working on a sort of core point of view. And then there's a final couple of validation checks in production, obviously with the new public sandbox, which is the same API but separate environment. So that'll be sort of post production. So I do have access to production just for myself, IP sort of blocked. So we can do those sort of validation checks as we deploy and get them in as well. So that's,

**George Westbrook** (13:23): that's good. Perfect. Yeah. And I suppose the, the next part we will be working on, but obviously will be a bigger priority after the 17th is the. Obviously the console stuff. So it's similar to what we mentioned before around, because it's not a quick task. Is that the permissions or all that stuff and then the different skills based on that and then running the testing, making sure that it's there and then it's. Then it's UI tweaks, UX tweaks as well. Which. Yeah, we'll, we'll. We'll be testing and running to make sure that, make sure that it's there. What's, what's the date again that you're, that you're planning for the console?

**Michael Moores** (14:06): It was later in November I believe from memory. But I think there's a lot still to do. So I think we're talking with Stat Works on that. Obviously they've been largely blocked on a lot of these APIs, so that they're behind almost, if you will. So we are probably going to push that one out. And you basically did the need is sort of the first client. So with this delayed and obviously the first client is also delayed. So yeah, we're just working for Ian to get the, the proper target date for that. So yeah, once this is out and we have a better sort of sign off of the APIs and stuff like that. So, you know, Stat Works are doing a Lot of changes after change with dt, changing stuff. So we sort of paused it a lot because it's just sort of wasted work. So yeah, we've got the, the core working and like say it's. I think it's 82 pass at the moment, so it's getting there. So I think we're mostly there a couple of small validation and back end behaviors that don't affect the request and the response, basically. So we're just working through them now and they can sort of start that ahead. So they've done all the stuff for their core and the user information, stuff like that. Just waiting on the last of the APIs for DT. Okay,

**George Westbrook** (15:25): perfect. I think I'm trying to think what else there is apart from let's get going and oh, Brett got his hand up.

**Brett StClair** (15:36): The most important thing that we got to get right

**Dorte Dye** (15:42): is it, oh, gosh, I spent too much time with you. I'm on your length of

**Brett StClair** (15:49): thinking. It's awful. Oh, no. The question, shall we do a late lunch or should we do a dinner? And so the thinking around the late lunch is we can probably get together, do a bit of a meet, go into a late lunch and then finish off at a pub somewhere.

**Dorte Dye** (16:11): I think it will be my preferred option because we all have to go home. Right, Mike, you have two hours from London as well.

**Brett StClair** (16:17): So instead of any risk of dinner and then it's rushing to get those trains at the end and everyone's a bit buggered and everyone's getting home really late, we do rather a later lunch, can go for a pint or two and then head and then at least everyone's home at a decent time. Makes

**Dorte Dye** (16:36): sense, but it all depends on how next week goes. Right.

**Brett StClair** (16:45): Then it's book hotels because we're getting wankered. Is that

**Dorte Dye** (16:48): what you mean? No, maybe we both crash. Right, Mike? I mean Mike for

**Brett StClair** (16:53): me, but yeah, probably. So the next question is where. What station do you guys leave from? And I'll make sure that we book something, you know, not miles away from there. I know a

**Dorte Dye** (17:10): good place. So I think Ian comes in at Houston. Yeah, I come in at King's Cross and make you Kings Cross as well, or Pencrest. Houston. Houston

**Brett StClair** (17:19): is why. So we're all around the

**Dorte Dye** (17:21): similar area. There's a very good steak

**Brett StClair** (17:24): place. Are you. Which steak place is

**Dorte Dye** (17:28): it? I forgot the name where we went last year. It's literally just at

**Brett StClair** (17:33): San Pancras. Okay, I'll have a look at that. Let's. I'll see if I Can book it. I'll send it to you, see what I can find.

**Dorte Dye** (17:41): By all means. I'm open to anything else

**George Westbrook** (17:43): steak related. Yeah if we don't go there that'd be a huge mistake.

**Dorte Dye** (17:50): No, I'm easy as like as long as Mike and Ian are happy I'm fine. I probably can't eat and drink that

**Brett StClair** (17:56): much anyway. Okay, perfect. I'll do some shopping around what time? What time are you getting into London? Just so I don't do any mistiming there definitely for

**Dorte Dye** (18:07): nine. So that's too early for George.

**Brett StClair** (18:11): So if I plan something lunchtime. 3ish. Get there chilled, do like that. Kind of late. We wanted to do

**Dorte Dye** (18:19): a meeting beforehand. Yeah, that's what I

**Brett StClair** (18:21): was thinking. A meeting beforehand. Okay. And

**Dorte Dye** (18:24): that's in your office and we can

**Brett StClair** (18:25): do it in our office then we wonder our office in Aldgate East. But it's like a 15, 20 minute tube ride to Houston. Some pancreas around there. It's quite easy. So we can. I

**Dorte Dye** (18:40): guess it would make sense to end the meeting at 10. Right. So that.

**Brett StClair** (18:44): Yeah. Chilled. Wander up. I'll book something maybe 2ish. 2ish. I guess that's fine. Finish up 5 a pint. 6 and then you know you're not going home crazy late. Eight o' clock, nine o' clock you're home. Okay. And

**Dorte Dye** (19:06): do we have an agenda for the meeting? Do you need anything from us?

**Brett StClair** (19:11): We will put together something. I think we'll take the opportunity to maybe showcase some ways of working. Pitch more product, share some knowledge around new products that you can buy from us. Now I've got you locked in a room. You thought sales Brett was bad remotely.

**Dorte Dye** (19:33): I mean it is at least not you alone again. There's a balance with everyone else. Right? Yeah. They probably can't send you much longer than 30 minutes anywhere

**Brett StClair** (19:46): anyone's left anyway, the room's just empty. I'll put together a bit of a structure. I think it'll be good to revise it'll look through it. Ian's also asked us to look at maybe a different type of commercial model going forward. So I'll put together some slides around that and we can walk. But you

**Dorte Dye** (20:07): know what that means. No commercial model.

**Brett StClair** (20:09): Yeah, cheaper.

**Dorte Dye** (20:13): I mean after all the shareholders are South African. You know where

**Brett StClair** (20:16): they're coming from. Right. I 100% get where they're coming from. Right. So completely going to be building it in with that kind of thinking. It's kind of when we do the sums I convert everything to Rands. And go. Okay. Is this a doable thing for the shareholders you're going to. I mean, as

**Dorte Dye** (20:38): long as everything is under 10,000

**Brett StClair** (20:42): Zimbabwean rands. I mean, Zimbabwean dollars. Okay, all

**Dorte Dye** (20:46): good. You sent an invite then, for the 24th, right? Yeah. I'll send

**Brett StClair** (20:50): the structure together and. And then let's also take some. I think also just sharing some knowledge might be a good thing as well. Just some of the lessons we've learned. Mike. I think that that could be a fun thing. But

**Dorte Dye** (21:06): then it means we need breakout sessions. Because then Mike and George go together.

**Brett StClair** (21:10): That's what I think. George go. Whatever. They're talking again. So maybe it's Mike and the engineers and then yourself, Ian, myself, Lily. You can be our engineer. That helps us do the more commercial Ford deploy stuff. You're just going to

**George Westbrook** (21:28): be drinking. Okay. At least in the evenings we get to go home and

**Dorte Dye** (21:39): not see Brett. I think Lily will move out very soon. I mean, she didn't sign up for working with him.

**Brett StClair** (21:47): She keeps talking to me about moving to London. Data is moving closer and closer

**Dorte Dye** (21:55): just to work from home and not from the office. Okay. I think we have everything, right, Mike? Yeah, perfect. Amazing. I'll check if I find the name of the place and I'll ping

**Brett StClair** (22:06): that to you. Cool. You? Perfect. Awesome.

**Dorte Dye** (22:10): Sounds like we have

**Brett StClair** (22:13): a good one. Just.
