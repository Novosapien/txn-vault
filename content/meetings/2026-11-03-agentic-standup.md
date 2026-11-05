---
date: 2026-11-03
type: standup
description: "After the DT call: UAT complete at 58 percent passing, coding standards still owed, the JWT scope moves to card program, and Console data flows to map"
scope:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[agent-access-layer]]"
status: extracted
extracted-to:
  - "[[delivery]]"
  - "[[architecture]]"
  - "[[permission-scoping]]"
  - "[[portal-co-pilot]]"
  - "[[co-pilot]]"
  - "[[full-agentic-experience]]"
  - "[[delivery-schedule]]"
  - "[[commercial]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-11-03)

> **Source:** transcript from a new notetaker, 3 November 2026, 15:30, about 16 minutes, an hour after the DT call ([[2026-11-03-dt-demo-and-infrastructure]]). **Novosapien:** George Westbrook, Brett StClair (driving, and mostly inaudible: *"I spent 15 minutes talking"*). **TXN:** Dörte Dye, Michael Moores. **Ian was not on the call.**

## The DT call, looked back on

**The demo worked and the meeting did not.** Dörte:

> *"I think the demo was great. What was not so great that **no one had a plan, that this one was a two-stage call. They hadn't read the documentation.**... I think it's because Jack sent the invite and he completely lost the purpose of the meeting."*

Michael: *"No, I think it was so good."* Both recordings, with and without voiceover, are with TXN, and George offered shorter cuts for circulation.

**Willie Olivier is an ally.** Michael: *"one of the good ones... he's very open to this stuff"*, pushing DT *"to do things differently than they have done in the past"*, and the person doing the data lake. Dörte's read was less generous: *"he wanted to learn more for himself than for our project."* George looked him up: head of research at a long-context AI company.

**The OKF question, answered after the call.** Willie asked whether Novosapien use OKF, and George said on the call he did not think so. Afterwards he and Hasan found it is the **Open Knowledge Format**, markdown files carrying the metadata an agent needs to traverse them, and *"pretty much what we've done... we just didn't know the name."* See [[architecture]].

**The infrastructure documents.** George: *"I can't remember who said it, but they were like they've not seen anything that's like a deal-breaker."* He allowed for the other reading: *"at least maybe none of them actually read any page of it."*

## UAT is complete, at 58 percent passing, and that is better than it sounds

Michael:

> *"We have completed UAT on our side. Not signed off, but we at least know everything... There's no material huge payload changes. Now it's more backend logic and validation... **It's 58% passing.** But... that one defect will clearly wipe out 30% of the test cases. So **we're not as far away as I thought originally.**"*

- **All 82 endpoints for 16 November are tested.** About 40 more come after launch.
- **Most of the 42 percent failing is one back-end validation defect.**
- **DT now order defects by visibility at launch.** The Knowledge Hub only needs what the YAML has right, so back-end validation can follow after launch: *"very much focus on launch."*
- Michael: *"Still a lot to do, but yeah, we're working towards that date."*

That is the first measured state of the gate at #108. See [[delivery]].

## The code has moved once, and the coding standards are still owed

**The first migration into the Stackworkz environment is done.** George asked Michael for the coding standards, so the code can be fixed before it reaches DT rather than after: otherwise *"we update the code, it goes to DT, they say it's not in the coding standards and then there's a day or two."* That is the mechanism behind the two-week delay Dörte expected on 27 October (#125), and it is still the same gap as #111: no standards named.

**The Knowledge Hub build is finished.** *"In terms of the build, when it comes to the Knowledge Hub, we're all there. It's just that migration and deployment part."* Hasan's local testing, against Novosapien's deployed services, is *"all seeming good"*. Security work will be mostly through Azure. See [[portal-co-pilot]].

## Agent authentication waits on Stackworkz, and the JWT scope changes

**Stackworkz have not come back** on agent authentication since the last call, when they were *"happy with the approach"* and wanted to do more thinking. Michael: they sent *"a couple of questions"* and are busy elsewhere.

**New: the JWT scope moves down a level.** Michael:

> *"In the middle of discussing a large-ish **JWT change to how it's scoped from program manager level to card program**, which is just to make sure there's no rework on their side as well... It's just not scoped to the right level at the moment."*

He will send it to Novosapien too. George: not a blocker, because the process from permissions to exposed tools and skills is in place, *"it was X, now it's Y, let's update it."* See [[permission-scoping]] and #107.

## Console data and the LLMs: map the flows now

**Dörte raised it**, thinking about the Console rather than the Knowledge Hub: *"we have card data there, we have cardholder data... all of the LLMs are all over the place... quite often they process them outside of Europe and then when you have GDPR data, what is being sent up the chain."* She has not read the infrastructure document, and it covers the Knowledge Hub only.

**George: there is flexibility.** Azure services can be pinned to regions. Anthropic and OpenAI models can be reached through Azure in specific regions, UK included, which he double-checked. Gemini through Azure Databricks needs more detail.

**Dörte wants the map before the decision:**

> *"I think what we should start doing is **mapping that stuff out**. I mean, don't forget **the data sits in South Africa as well** and processes through South Africa. But if we can minimize whatever goes out of Europe, the easier it is for all of the documentation, the **DPA** stuff... then we can plug and play with the different modules."*

**The internal LLM call did not happen.** It was set for 29 October between Dörte, Ian and Novosapien. Dörte held it while Ian and Michael deal with DT, and will *"start some prep work"*. Meanwhile the LLM question was put to DT directly on the DT call. See [[architecture]], #70 and #103.

## The other workstreams

- **Console co-pilot.** Good progress. George wants feedback on **Thursday 5 November**, then a deploy to the test environments. See [[co-pilot]].
- **Full Agentic Experience.** Back in work, in tandem with both co-pilots. See [[full-agentic-experience]].
- **Outbound.** *"There's still some warm-up to do for the inboxes"*, and messaging needs aligning with Ian before anything sends. The schedule had warming starting 16 September and finishing around 29 September, so this is a slip or a restart, cause not recorded. See [[delivery-schedule]].
- **Scribe.** George proposed a conversation in the next week or two, after Dörte's talk with Vanessa and Lily, on *"what could be valuable, what might not be valuable."* Dörte: *"Are you trying to upsell now?... No, absolutely. I mean it's brilliant."* She catches up with Brett on Thursday. See [[commercial]].
- **The customer meeting** has moved to next week. Context, no action.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| Demo great, meeting unplanned; DT had not read the documents | [[delivery]] | In the 3 November callout |
| Willie an ally; OKF is what Novosapien built | [[architecture]] | In callout |
| UAT complete, 82 endpoints, 58 percent passing, one defect most of the failures, defects ordered by launch visibility | [[delivery]], [[open-questions]] #108, #32 | Callout added; rows updated |
| First migration done; coding standards still owed | [[delivery]], [[open-questions]] #125, #111 | In callout; rows updated |
| Knowledge Hub build finished; migration and deploy left | [[portal-co-pilot]] | In callout |
| Agent authentication waiting on Stackworkz; JWT scope to card program | [[permission-scoping]], [[open-questions]] #107 | Callout added; row updated |
| Console data and the LLMs: regions, map the flows incl. South Africa, for the DPA | [[architecture]], [[open-questions]] #70, #103 | Callout added; rows updated |
| Internal LLM call of 29 October did not happen | [[delivery]], [[open-questions]] #70 | In callout; row updated |
| Console co-pilot feedback on Thursday 5 November | [[co-pilot]] | Note added |
| Full Agentic Experience back in work | [[full-agentic-experience]] | Note added |
| Outbound inboxes still warming | [[delivery-schedule]] | Flagged as a slip, cause not recorded |
| Scribe conversation proposed | [[commercial]] | In callout |
| Customer meeting moved | n/a | Context, no action |

## Open actions from the call

| Action | Owner | When |
|---|---|---|
| Send the coding standards | Michael | When he can |
| Send the JWT scope change | Michael | When settled with DT |
| Come back on agent authentication | Stackworkz | Not dated |
| Map the data flows for the LLMs, South Africa included | Novosapien, with Dörte | Not dated |
| Prep for the internal LLM call | Dörte | Not dated |
| Show the Console co-pilot for feedback | George | Thursday 5 November |
| Align outbound messaging | Ian, Novosapien | Before sending |
| Book a Scribe conversation | George, Dörte | Next week or two |

## Transcript

# TXN - Agentic AI SU

Tue 3 Nov, 15:30  
Client: TXN

**Michael Moores** (0:00): Yeah, I've got the ATIO things joined

**George Westbrook** (0:05): that one, the new note taker. We're testing for something else, so apologies for that. Yeah, I suppose. Thoughts on. Thoughts on that call. You think it went well? Think it went badly?

**Dorte Dye** (0:17): You were terrible.

**Michael Moores** (0:20): Oh, that's it. Love it. No, I think it was so good.

**Dorte Dye** (0:24): I think the demo was great. What was not so great that no one had a plan, that this one was a two-stage call. They hadn't read the documentation, but it's as much as you can do. I mean it's like Mike shouted a week ago. I think it's because Jack sent the invite and he completely lost the purpose of the meeting. But I didn't want it to argue, hence why it's like, yeah, whatever you want to do.

**Michael Moores** (0:53): I think Willie was. This is one of the good ones. So I think having AI focus as well from the. The DT side. So I think he's, he's very good. Actively pushing DT to do. Do things differently than they have done in the past. So he's very open to, to this stuff as well. So it's, it's good to have him on there.

**Dorte Dye** (1:13): I had a feeling that he wanted to learn more for himself than for our project. It seems like, okay.

**George Westbrook** (1:20): Because there was, there was one thing he said. He was like, are you using. I didn't know if I was hearing it correctly because of his accent. It sounded like, okay, if I was like, what, what does he mean? And then me and Hasan asked the calls like, was it this? And we found what it was, is, oh, it's called OKF, which is like Open Knowledge Format, which is pretty much what we've done. Which is when you've got markdown files, blah, blah. It's not just a file, it's got metadata to allow it to traverse. Because after we were like, is this something we should know? Is this something we should have done? We're like, oh, we've already done it. We just, we just didn't know the name of what it was. Yeah. Which was. Yeah, was reassuring. But yeah, we looked at his LinkedIn profile after and he's like, like head of research at this research company for long context AI stuff. And I was like, oh, bloody hell. Yeah, he's a, he knows what he's talking about.

**Michael Moores** (2:13): It's been, he's one doing the data lake as well. So it's been pretty helpful with that.

**Dorte Dye** (2:17): So,

**George Westbrook** (2:19): yeah, I suppose it's. Yeah. Demo seemed like they were all happy with it. Obviously we've got the, the non-voiceover version and the voiceover version as well. If there's any issues with that, let us know and we'll be happy to. We're happy to do another one. There's other ones that you want maybe a bit.

**Brett StClair** (2:39): A bit.

**George Westbrook** (2:40): Bit shorter to circulate the same as always. Just, just let us know and we'll get them, get them sorted. But I suppose it's yeah the next things to the infrastructure. So it's. Yeah, once, once we hear back from them with the questions, we'll get on to them straight away and get the answers over yeah infrastructure. Then the migration of the code as well onto the. Onto the Statworks, let's call it a Statworks environment. So we've done. Done the first migration but I think with the, with the coding standards, if you'd be able to send them over Mike when you get a chance. And then we might have to update certain things just so that it's not. We. We update the code, it goes to DT, they say it's not in the coding standards and then. Then there's a day or two if we, we could just sort that out before. But we've been correct if I'm wrong on any of this. Hasan Testing. Testing it locally, all seeming good. Obviously connected to our deployed versions of the services. But it's going to be the same if it's in Azure, if it's in GCP, just with obviously some of the security aspects that we'll need to bottom but that'll be mainly through Azure anyway. But yeah, I think obviously in terms of the build, when it comes to the Knowledge Hub, we're all there. It's just that migration and deployment part. So I think the next. Yeah, the next thing which I think would probably be best if we go through parts of it on Thursday is the console Copilot. So been working on that, making good progress on that and I think, I think it'd be good to get some feedback on Thursday, show that around and then we'll get it deployed to the tested environments as well so that we can, we can start making progress on that, I think. What else is there? Oh, with.

**Dorte Dye** (4:43): Sorry DT, I'm just thinking about the console, about the data stuff and everything where that is flying because we have card data there, we have cardholder data. What have you done there? And I must admit I still haven't read the document you've shared.

**George Westbrook** (5:01): Is that is. So is that the, the. The document on the infrastructure for the Knowledge Hub?

**Dorte Dye** (5:07): Yeah, so that hasn't really probably covered it. I'm more thinking about the data on the control center when we're using AI and when it goes to the different LLMs, because all of the LLMs are all over the place.

**George Westbrook** (5:19): Right.

**Dorte Dye** (5:19): And quite often they process them outside of Europe and then when you have GDPR data, what is being sent up the chain.

**George Westbrook** (5:29): So with that there's a bit of, there's like flexibility. So with the, with some of the deployed services in Azure you can set it to certain regions. So say if it's. I think with Azure Databricks we need to dive into a bit more detail. But Azure Databricks would only be for using Gemini models. With any Anthropic model or OpenAI model, there's multiple ways we can access them through Azure in specific regions as well. So if it needs to be UK, I double-checked. If it needs to be South Africa, I'm assuming it's all going to be UK.

**Dorte Dye** (6:11): But yeah, I think what we should start doing is mapping that stuff out. I mean, don't forget the data sits in South Africa as well and processes through South Africa. But if we can minimize whatever goes out of Europe, the easier it is for all of the documentation, the DPA stuff, it will be just good to get ahead of it to have a proper flow there. And then we can plug and play with the different modules, right. LLMs what you want to use and then if the team makes a decision we can say, well, we will prefer this route because of X, Y and Z. So just that we are a step ahead of that, if that makes sense.

**George Westbrook** (6:47): Yeah, yeah, I think obviously we did. We didn't go into loads of detail on the infrastructure stuff on that call, but I think obviously a few of them have had a brief look through and I mean even if it's the first two pages, it's talking about a lot of the services anyway. And I can't remember who said it, but they were like they've not seen anything that's like a deal-breaker. Which is, which is good because I assume obviously everything's in. Well, not. I assume everything's in Azure. So it's just a service that they need to need to expose for us. Which, I mean it's good because that was one of the things like, no, it has to be done this way, this, this, this, this, this, this, this. But at least maybe none of them actually read any page of it and they were just pulling it out of where the sun doesn't shine to just contribute. But.

**Dorte Dye** (7:40): We give them the benefit of the doubt.

**George Westbrook** (7:42): Yeah, but Yes, I think we got so migration deployment, console Copilot focusing back on the full agentic experience as well. So that we've got in tandem the Copilot, the console Copilot and the full agentic experience being worked on. I think one thing that we, I think we're waiting on from Statworks is the agent authentication stuff which obviously like how it was left from the last call was happy with the approach. Let us do a bit more. This is them saying let's do a bit more thinking and then they'll get back to us. So I'm not sure if there's anything that they shared with shared with you guys updating on that or if. If they're. If they're still having a think a

**Michael Moores** (8:31): couple of questions from them to help them format what they want to do, but other than that, no, not nothing yet. Okay. They've been quite busy with the other side of the certain stuff we're trying to do as well. So yeah, still waiting to hear back from them. So we'll let you know when we do and we can discuss it with you. So yeah, perfectly in the middle of discussing quite a. Well, a large-ish JWT change to how it's scoped from program manager level to CAR program, which is just to make sure there's no rework on their side as well. So we'll send you the same thing as well. So you can see. Perfect. It's just not scoped to the right level at the moment. So adding that CAR program level in as well at the. I think at the scope JWT scope we're just sort of hashing out now with DT to get the final bits over the line with that authentication basically.

**George Westbrook** (9:24): Yeah, because I think what we, what we can. So what are those things on the. Both the full agent experience and the console Copilot is obviously first there's the authentication element which it's not a blocker but I suppose it's looking at the permissions and the process around, okay, this user's got this permission, which tools do we expose, which skills do we expose and as long as we've got the process in place, if there's slight changes, it's not an issue like with anything. It's just a matter of okay, it was X, now it's Y, let's update it. And then I suppose any UI or UX issues that anyone sees will obviously be working and fixing them as well and building new features and functionality in.

**Michael Moores** (10:16): I think apart from that

**George Westbrook** (10:19): the, the other thing is the. With which I think I suppose is more for. More for Ian is the. The outbound workforce need to just get some messaging, messaging sorted and aligned because the warm-ups is there's still some warm-up to do for the inboxes. It's just letting that finish, making sure that the deliverability is there and then, then we can get firing those messages out as well.

**Dorte Dye** (10:43): Okay. Or when Kejopism or not,

**George Westbrook** (10:47): I can't remember. Did, did you daughter of Ian and Brett have the chance to have that conversation about the LLMs last week or is that, is that.

**Dorte Dye** (10:55): No, no, no, that's what I meant. I haven't really everything that happened at the moment with DT. I wanted Ian to focus with Mike on that and then once that's settled then we can look at that. I will start some prep work for that actually.

**George Westbrook** (11:10): Okay, perfect. Yeah. If there's anything that doesn't make sense in there, just let us know and we'll get it updated. But yeah, like I said with the LLMs, there's lots of flexibility and then all we'll do, we'll update the model, do the testing, make sure it's all there, make sure it's hitting the same criteria. So no real blockers on that. I think, I think apart from that, unless anybody else has got anything. I think that's, I think that's everything. 15 minutes back. I love it when you're in the car driving.

**Dorte Dye** (11:47): He doesn't want to talk, right? Concentrating on the street, talking the whole time.

**Brett StClair** (11:51): Didn't you guys hear me?

**Michael Moores** (11:53): No.

**George Westbrook** (11:55): You don't need to repeat what you were saying either.

**Brett StClair** (11:58): I spent 15 minutes talking. I'm going to repeat everything.

**Dorte Dye** (12:02): What's good enough.

**George Westbrook** (12:08): But yeah, I think that's, I think that's everything. Yeah, good call with DT. Have to have the next one. But yeah. Didn't seem from our spot, it didn't seem as if there was anything they said where we were like, oh yeah,

**Michael Moores** (12:22): I think from our side as well. We have completed UAT on our side. Not. Not signed off but we at least know everything that he's doing. So there's no material huge payload changes. Now it's more backend logic and validation. That's the problem. It's 58% passing. But you know the stuff I just mentioned is about 42% of it failure. So that one defect will clearly wipe out 30% of the test cases. So we're not as far away as I thought originally. So we managed to get through all that of the 82 endpoints we're going to. So the 16th of November has 82 endpoints. We've tested all those. There are another 40 odd that are coming later. But we have run through the testing completely there. But obviously now try and sign them off. So at least you get that as well. And Statworks as well. Perfect.

**George Westbrook** (13:18): Let's roll on the 16th.

**Michael Moores** (13:22): Still a lot to do, but yeah, we're working towards that date. So we had a good call with DT today on the defects and stuff like that. So prioritizing. Well, you're prioritizing the defects based on how visible they are for the launch. So you know, only going to be used from the Knowledge Hub for now obviously. AI anything that the YAML's got correct, we're good. So backend validation, we can probably leave it a bit later. So that's just what we're discussing with DT on the the order right now. So trying to reduce that down as little as possible to as little as possible and then we can fix them in the backend as we've gone launch. So very much focus on launch.

**George Westbrook** (14:00): One thing I suppose that popped into mine is obviously I think Dorte, also you had a conversation with Vanessa and Lily about what we're calling Scribe at the moment. So I suppose it might be worth in the next week or two set up a conversation around that have have a talk about what could be valuable, what not what might not be valuable and get into a bit deeper, deeper on that.

**Dorte Dye** (14:23): Are you trying to upsell now? The one time Brad is silent, George is doing the sales bridge.

**George Westbrook** (14:32): All right, I'll do this. I'll be. Brett,

**Dorte Dye** (14:37): I know you put yourself on mute and keep talking. No, absolutely. I mean it's brilliant. And Brett and I are catching up on Thursday so maybe we already have a step on that one as well. There's a lot to catch up at the moment.

**Brett StClair** (14:50): I'll move it out.

**Dorte Dye** (14:51): This should be all in the right

**Brett StClair** (14:52): orders to move out till 3 o'.

**Dorte Dye** (14:55): Clock. Actually, we don't have to because the customer meeting is now pushed to next week. But we might need. Sorry, have a message about that one. So we can stick as usual times for first year, then we might need to adjust next week, but I will let you know. Describing again.

**George Westbrook** (15:17): Yeah, I think that's it. Yes. Okay, perfect.

**Dorte Dye** (15:21): Both thumbs up. Oh, dangerous.

**George Westbrook** (15:23): Yeah.

**Dorte Dye** (15:24): Okay, cool.

**George Westbrook** (15:26): Perfect. He's putting his thumbs up now in the chat.

**Dorte Dye** (15:32): I don't know how you do that when you drive. Brad, that's a serious security issue.

**George Westbrook** (15:38): Yeah, he's just. He's on his third car this month. Right, perfect. Well, speak you all on Thursday.

**Dorte Dye** (15:51): Oh, yeah.

**George Westbrook** (15:52): Take care. Have a good.
