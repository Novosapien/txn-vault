---
date: 2026-09-22
type: standup
description: "Standup: the API spec drops to 46 operations with no design spec behind it, the speed build ships, and Michael answers the Umbraco key request"
scope:
  - "[[txn-api-reference]]"
  - "[[agent-orchestration]]"
  - "[[docs-mcp-server]]"
  - "[[portal-co-pilot]]"
  - "[[delivery]]"
  - "[[content-workforce]]"
  - "[[delivery-schedule]]"
status: extracted
extracted-to:
  - "[[txn-api-reference]]"
  - "[[agent-orchestration]]"
  - "[[delivery]]"
  - "[[docs-mcp-server]]"
  - "[[portal-co-pilot]]"
  - "[[content-workforce]]"
  - "[[delivery-schedule]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-09-22)

> **Source:** Gemini transcript, 22 September 2026, 09:00 BST, 24 minutes. The Fathom recap gives 26 minutes.
>
> **Speakers:** George Westbrook (from a cafe), Max Kingaby and Hasan Ahmed for Novosapien. Dorte Dye, Ian Johnson and Michael Moores for TXN.
>
> **Invited, not heard:** Brett StClair (on a flight), Lily StClair (on the way with Brett) and Vineth Siriwardana.
>
> **A naming note:** Gemini writes **"Stat Works"** throughout. It is **Stackworkz**, who build the Console and the Developer Portal.

## The API surface shrank, and there is nothing fixed to build against

George opened the API item with a count. About **96 operations** on the 10 August spec, *"40 48 or 46"* on the latest. The areas he named as gone: transactions, spend control creates and updates, spend overrides, alerts, PIN, 3DS and digital wallets.

The measured figures from the delta he ran the same morning:

| Spec | Paths | Operations | Schemas |
|---|---|---|---|
| Build pin, 10 Aug | 67 | 98 | 327 |
| 25 Aug | 22 | 35 | 177 |
| 21 Sep | 30 | 46 | 223 |

**Michael's explanation is that the spec got honest, not smaller.** DT moved to a new OpenAPI service: *"before they've just uploaded everything, so you had everything that wasn't even built. Now... you're actually seeing the true live reflected."* The missing areas *"will be coming in in one way shape or the other"*, and the remaining build, FDS, transactions and spend controls, is *"around"* October, because TXN needs it to go live.

### The finding under the finding

George asked for the full spec DT builds to, so Novosapien can build ahead of the live surface. **There is no such artifact.**

> *"There isn't one sort of one defined spec that keeps rotating. Basically we just have these small user stories unfortunately that that they're sort of building from... So we have sort of documentation for it but not specifically you know a design YAML if you will."*

Two consequences, both stated on the call. **Nothing is signed off:** *"we haven't actually signed off any of the endpoints yet."* And **TXN carries the same risk as Novosapien**, because its test suite follows the same YAML, which is why Michael will ask DT what changed and why.

He named the two changes he knows: the **spend control identifier moves out of the URL and into the body**, and the rest are mostly extra fields that come from the Visa mandates.

### The rule that keeps the build moving

George proposed it and Michael accepted, *"Yeah. Yeah, definitely. I appreciate that."*

| Case | What the mock API does |
|---|---|
| The endpoint survives with field changes | Update it to the new shape |
| The endpoint is absent from the 21 September spec | Keep the 10 August version until DT confirms the drop |

**Why it matters:** the live API misses at least one tool call in **8 of 13 agent workflows**. Building against the live surface alone would stall most of the slate. Recorded in [[txn-api-reference]].

### Ian asked what the churn costs, and the answer on the call was lower than the analysis

> *"We could be wasting a bunch of time and money because things are not settled... how far away are we from getting all of the APIs done and settled that's in MVP?"*

Michael has no date and will ask DT on the 10:00 project call. George's answer was that the cost is low: *"most of it's going to be slight iterations or updates or an extra field"*, with real rework only where operations disappear and the SOPs that consume them must be rethought.

**The impact analysis run that morning returns the verdict STOP.** It found nested spend-control fields, two new enums that reject values the SOPs send, no masked card number for last-four targeting, and 20 of 43 MCP tools absent from the spec. Both statements are on record; the gap between them is tracked at [[open-questions]] #94.

## The key is rejected, and the gateway moved again

George raised the subscription key as *"not urgent"*: *"it's always returning 401, 403."* Probing confirms it. DT moved the prefix from `/api/stg/` to `/api/staging/`, every old route returns 404, and the key is refused on every route that checks one.

Michael: DT rebuilt the environment in **Azure API Management**, he has a new key from that morning, and he will send it once tested. Later there will be a dedicated key per application, production separated, and the authentication method itself will change. New row at [[open-questions]] #95.

**A side effect worth having:** the two specs now differ by base path under the same filename again, which is the shape `fetch_spec.py` expects, so [[open-questions]] #67 may no longer need its fix.

## The speed build went to production

George pushed it straight after the call. It is the build promised *"in the next two to three days"* on 17 September, so **two days late**.

- **Bucketed tool calls:** *"it's not going one, two, three, four, all the way up to 11."*
- **One approval, up front:** approve the plan, then *"it's going to do everything it asked for."*
- **Card selection** in the chat, and **inline forms** on four or five workflows.

**Two of Ian's three rules from 15 September are answered by this build:** ask for the identifier first, and collect structured input in a form rather than a numbered chat list.

**George named the defect before TXN found it.** A required field cannot be deferred to the agent: *"I kind of just wanted to put I don't know this, just look look it up for me. But it was saying no, this is a required field."* He asked the group to *"rip it to shreds."*

**And the speed claim is by feel again**, *"a lot more noticeable"*, with no figures, on the first day a before-and-after comparison was possible ([[open-questions]] #87). TXN still has no ring-fenced build, and George told them more changes are coming ([[open-questions]] #93).

## The knowledge hub work has its key request answered

Michael responded to the Umbraco ask he had let pass on 17 September: *"it's just a API key as far as I'm aware."* He will ask Stackworkz for a **separate key** for Novosapien. The UAT hub already holds *"about 30 odd documents"*, with a production hub alongside.

George stated the mechanism: hold a copy of the Umbraco content on the **MCP server** and refresh it *"be it on a timer or more webhook based."* He also has a **basic UI prototype of the co-pilot** for look and feel, with something to show the week of 29 September, and wants the entry point moved from two clicks to an always-visible panel.

## GTM

**Content.** Only the personal pillars and a review of Tyler's drafts remain. George set the expectation that the work is iterative.

**LinkedIn has an owner at last.** Ian: *"Bronwyn's going to set up the company LinkedIn profile page"*, and he will tell Max when it is done ([[open-questions]] #63).

**Domains have not moved.** Dorte has emailed Ian a summary and will settle the rest offline. George: *"until we've got the domains, hands are tied."*

## Post-Call Analysis

| Finding | Destination | Action |
|---|---|---|
| **The external spec is 46 operations against 98** on the 10 August pin; DT's new service renders only built endpoints | [[txn-api-reference]], [[open-questions]] | Section added; **#32** updated |
| **No design spec exists**; DT builds from approved user stories, and no endpoint is signed off | [[txn-api-reference]], [[open-questions]] | Recorded; **#32** updated |
| **Mock API rule agreed:** follow field changes, keep absent endpoints until DT confirms the drop | [[txn-api-reference]] | Recorded as a decision |
| **8 of 13 workflows** miss at least one tool call on the live API | [[txn-api-reference]], [[delivery]] | Recorded |
| **Ian asked how far away a settled MVP API is**; no date, October for the remaining build | [[open-questions]], [[delivery]] | New row **#94** |
| The rework estimate given on the call is lower than the same-day impact analysis (verdict STOP) | [[open-questions]], [[delivery]] | Recorded in **#94**, both statements kept |
| **The subscription key is rejected**; the gateway prefix moved to `/api/staging/` | [[txn-api-reference]], [[open-questions]] | Section added; new row **#95** |
| The new URL shape matches what `fetch_spec.py` expects | [[open-questions]] | **#67** marked likely moot |
| **Routing changes from program manager ID to card program ID** | [[txn-api-reference]] | Recorded |
| **Stackworkz blocked on schemas**; "search all cards" is not a public API call | [[txn-api-reference]] | Recorded |
| **The speed build is in production**: bucketed calls, one up-front approval, card selection, inline forms | [[agent-orchestration]], [[delivery]] | Recorded; two of Ian's three rules answered |
| Required form fields cannot be deferred to the agent | [[agent-orchestration]] | Recorded as the known defect for this test round |
| No `cardNumberMasked` in the new spec, and the forms ask for the last four digits | [[agent-orchestration]] | Recorded as a dependency |
| Speed still judged by feel, on the first day a comparison was possible | [[open-questions]] | **#87** updated |
| The build was handed over with no ring-fence, and more changes are coming | [[open-questions]] | **#93** updated |
| **Umbraco needs only an API key**; Michael will ask Stackworkz for a separate one; ~30 docs loaded | [[docs-mcp-server]], [[open-questions]] | Recorded; **#92** updated |
| MCP server holds a copy of the content, refreshed by timer or webhook | [[docs-mcp-server]] | Recorded |
| **Co-pilot UI prototype exists**; the panel becomes always-visible | [[portal-co-pilot]] | Recorded |
| Content: personal pillars and a review of Tyler's drafts remain | [[content-workforce]] | Recorded |
| **Bronwyn owns the LinkedIn page setup** | [[content-workforce]], [[open-questions]] | **#63** updated |
| Domains unchanged; Dorte to settle with Ian | [[delivery-schedule]] | Recorded |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Ask DT what changed in the spec and why | Michael | TXN's own test suite follows the same YAML |
| Get a date from DT for the remaining endpoints | Michael | Asked at the 10:00 project call the same day |
| Test the new key and send it | Michael | Received that morning, untested |
| Ask Stackworkz for a separate Umbraco API key | Michael | For the MCP server and the co-pilot |
| Test four or five workflows on the new production build | TXN | Expect an over-strict required field |
| Update the mock API to the 21 September spec | Novosapien | Under the rule agreed on the call |
| Settle the domains with Ian | Dorte | Naming convention still outstanding |
| Complete the personal pillars, review Tyler's drafts | Max, TXN | Last content items |
| Set up the company LinkedIn page | Bronwyn | Ian will confirm when it is done |

---

## Transcript

Sep 22, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:31**

**Hasan Ahmed:** What up?

**Dorte Dye:** Morning guys.

**Max Kingaby:** Hello.

**Ian Johnson:** Morning.

**Dorte Dye:** Was really bad feedback. Hi.

**Max Kingaby:** How are you both?

**Dorte Dye:** All right.

**Max Kingaby:** Good. Um, we should be getting joined by George. I believe he's just setting up his laptop. He's he'd like to come to a cafe to to jump on our calls. He should be handy. There we go. Like that.

**George Westbrook:** No. Can anyone hear me?

**Max Kingaby:** I go down a BrettLet's

**George Westbrook:** Oh, okay. So, there's me. There's there's me rushing to try and fix it.

**Max Kingaby:** go.

**George Westbrook:** So, how how are you all doing?

**Ian Johnson:** Good.

**George Westbrook:** Good.

**Ian Johnson:** You

**George Westbrook:** Good. good don't been uh busy working away today. Um I think we've got got some good updates as well obviously after the call that that you guys had yesterday with the the content workforce as well. So

**Ian Johnson:** I'm waiting for Brettor not.

**George Westbrook:** no Brett Brett's just on a just on a flight at the moment.

### **00:02:11**

**George Westbrook:** Um I think he's he's landing in landing in about an hour. So then he's then he's uh then he's joining in our setup that we got here. So yeah,

**Ian Johnson:** Thank you.

**George Westbrook:** Lily Lily and uh Lily and Brett just on their way.

**Ian Johnson:** Okay.

**George Westbrook:** Perfect. So I suppose maybe do a quick roundup of the that content call that you had yesterday. So I suppose every everything's everything's all sorted after that. Correct me if I'm wrong. The only only thing that needs to be done is maybe the the personal pillars. Max, is that is that right?

**Max Kingaby:** Yeah, the personal pillars. Um, and then a review on the content that Tyler has already made up.

**George Westbrook:** Okay, perfect. Yeah. And I suppose it obviously went through how like what Tyler's role is, how you can how you can use him, how he's going to how he's going to be helping you along that as well. Um, I think one thing to stress as well is is initially it's an iterative process with the like with some of the the context documents and the and the content.

### **00:03:19**

**George Westbrook:** So, there might be some things that are going to be you like some people go into it thinking it's going to be perfect first time. Sometimes it is. Um, but obviously sometimes it's difficult to know exactly what you want first time as well. Um, so it's making sure that both everyone and the AIS are all aligned. Um, and it just gets better and better over time.

**Ian Johnson:** Okay, we're good.

**George Westbrook:** Um, I think another another thing is on the outbound is there has there been any updates regarding the any decisions around the the domains for the outbound yet?

**Dorte Dye:** I've sent you the email yesterday, didn't I? Yeah.

**Ian Johnson:** Me

**Dorte Dye:** But do you Let me check.

**Michael Moores:** Jesus.

**Dorte Dye:** I've I've summarized everything what we agreed. So, no, George, leave it with me. I'll pick that up with Ian afterwards.

**George Westbrook:** Okay. Okay. Yeah, cuz once we've got that, get it all set up, get it warmed, and then then get it then get it firing.

### **00:04:20**

**George Westbrook:** Um but yeah, it's just until until we've got the the the domains, there's like kind of hands are tied. Um but we've got obviously plenty of other stuff that we can we can be getting on with. Um so I think apart from that on the outbound there's there's not not too much more. Um thanks for sending over the API stuff, Mike. Um there's few questions got on that because I think the the original one we we got which I think was when we when we queried it I think it was around the 10th of August um there was around I think 96 operations um I think on the latest one for the external API I think it's coming in at around 40 48 or 46 um and I think it was mainly let me just double check because I've got it noted down somewhere Um, some of the mission areas were in transactions, spend control, creating and updating, spend overrides, alerts, but I think I can understand alerts were something that you mentioned would be would not be in there. Um, PIN, 3DS, and digital wallets, and I remember you saying something about 3DS as well.

### **00:05:35**

**George Westbrook:** Um, is that is that something that's going to be added in or is it for initially that's going to be left out?

**Michael Moores:** Yeah. So I think what they've done is um they've moved now to a new um open API spec service they've built. So before they've just uploaded everything. So you had everything that wasn't even built. Now what they've done they've moved to this service so it's actually rendering properly. So you're seeing what's been built, a to date,

**George Westbrook:** Okay.

**Michael Moores:** So they will be there. It's just the progression that we have so far basically. So you know everything you had before will be coming in in one way shape or the other but it's just I think they've moved to a service now. So you're actually seeing the true live um reflected basically not so before they had like an XML type approach and now they've built a full service to get the you know the full deep descriptions and and everything we needed in there as well. So that's the sort of reason for the switch.

### **00:06:32**

**Michael Moores:** Um, and yeah, that's about right to where we are at the moment in terms of what they're building.

**George Westbrook:** Okay. Okay. is so in terms of timings for when when the stuff that hasn't been built is going to be built, do you say is would you say that's like start start middle end of October or is is is the time horizon for that a bit longer?

**Michael Moores:** Yeah, that should be around there. Yes. So obviously we need all that for going live as well.

**George Westbrook:** Okay.

**Michael Moores:** So they should be sort of imminent pretty much. Um I know they're building the SP controls now sources is literally the last couple of things they're building. So yeah, they should be out as soon as they are. So that's the staging/ internal UAT. So as soon as we get them, you'll get them as well. So it'll be sort of going through at the same time that we're you're actually testing them as well.

**George Westbrook:** Okay. Is there obviously I appreciate you said when as soon as you get them we'll get them.

### **00:07:25**

**George Westbrook:** Is has the spec for those changed at all? cuz what what I'm thinking is rather than us waiting until um cuz I'm assuming obviously they're building they've got a spec that they're building to um which is I'd assume relatively static at the moment um after after some of the testing um if we'd be able to have access to the latest version of the the full spec then when we're building some of the agentic stuff we we build against that rather than the the current live version because I think in the in some of the workflows for the agents. I think it's eight out of eight out of 13 at least one of the tool calls um that it needs in order to complete that workflow won't be there with the current version of the live API. Um so all we're doing is we're building the obviously the the mock API against the spec. But after noticing that drop, we've we've left some of those tools that are not what some of those endpoints that aren't currently in there in there for the workflows.

### **00:08:27**

**Michael Moores:** Yes. So what I'll do is I'll ask them what's changed and why. Obviously the original was the design. So what's happen at the moment we're going through the user stories and approving them. So it is possible that the design we pass in isn't a design that comes back. there's not sort of a real full spec if you will. So I know for example spend controls there was quite a lot of suggestions and changes in in that one from what I asked for all to keep it consistent aligned and obviously better but it is possible that they're they're

**George Westbrook:** Yeah. Yeah.

**Michael Moores:** changing. So for example the spend control one we've dropped the identifier from the URL and put it into the body. So that's that's what two of the largest changes we've done whereas the rest of them will just be sort of

**George Westbrook:** Okay.

**Michael Moores:** additional fields. So obviously what's happening is we're going through the visa mandates obviously we then identify additional fields that we need. So a lot of it will just be sort of more fields that we have to have in there rather than a full you know change of the the object basically.

### **00:09:22**

**George Westbrook:** Yeah.

**Michael Moores:** So I think the the the version you had was probably the closest that we have so far.

**George Westbrook:** Okay.

**Michael Moores:** Um but there isn't one sort of one defined spec that keeps rotating. Basically we just have these small user stories unfortunately that that they're sort of building from. Um obviously they then comment and change based on their suggestions and obviously we approve them. So I've tried to put a pull everything together where I can. So we have sort of documentation for it but not specifically you know a design YAML if you will. Um but I will just double check with them as why it's changed because I said we were we are also following the same um YAML as you.

**George Westbrook:** Yeah.

**Michael Moores:** So that would also impact our uh testing suite as well. So I will double check why if it's been purposely dropped and when those will be sort of reshamed basically.

**George Westbrook:** Okay. So I think I think what might be best best then is when there's a a like for like let's say this endpoint in the old version there it exists on the new version but there's some field changes we'll update our mock API so that it aligns with that but anything that's kind of appears to be dropped or not built yet we'll keep as long as it was in the first the first version and then when we've got an update we either update or if it's gone we'll get rid of it.

### **00:10:43**

**George Westbrook:** Does that sound like a approach you're happy with?

**Michael Moores:** Yeah. Yeah, definitely. I appreciate that.

**George Westbrook:** Perfect. Okay.

**Ian Johnson:** So,

**George Westbrook:** And I suppose Sorry.

**Ian Johnson:** can I just check, Mike, when we're expecting them to complete? I mean, we can ask them on the project call at 10:00, but the thing to me seems to be that we could be wasting a bunch of time and money because things are not settled at the moment and therefore, you know, it's okay that you guys are doing work and you're able to kind of mock up APIs, etc., but at some point there's rework to do to actually work to the correct APIs. And I just I think part of the question is just how how far away are we from getting all of the APIs done and settled that's in MVP so that you guys could be starting from what is the final set that we're ready to go to Okay.

**Michael Moores:** Yeah. Yeah. I don't know the date right now. I think we'll need to ask them, but there's quite a considerable amount of, you know, FDS transactions, spend control, probably the three biggest things that we have left.

### **00:11:56**

**Michael Moores:** So, you know, I think they will be longer than the others. Um, again, obviously, we got to test them as well before we know. So, a lot of the UA at testing is going back with changes as well. So I think we can just ask them when at least it'll be built and obviously we still need to go through a UAT test everything pretty much. So um you we haven't actually signed off any of the endpoints yet. So that's when I completely comfortable but I think if we get at least a date from them when it's been built at least we can have a you know first version rather than just a you know potential draft at least.

**George Westbrook:** I think I think for us in terms of the the uplift when there's changes is don't it's not a five minute and it's done but it's not it's not days of work I think it's if if a lot of things are changing in terms of like these endpoints are now never they're not here they're gone this operation is not going to happen that's where there's a bit more reworks we need to rethink about some of the SOPs and workflows that are consuming that um but I think in terms of that cost benefit it's we can steam ahead.

### **00:13:04**

**George Westbrook:** Most of it's going to be slight iterations or updates or an extra an extra field. Um, which is which is not too much of an issue. Um, so from from from our point of view, it's it's not not as concerning as obviously maybe previously in a software project where it's like, yeah, well, there's one API and a lot of things might change and you're like thinking, oh my f\*\*\*\*\*\* god, like what's what's what's going on? Obviously, we all bang on about AI, but it's it has got its benefits with with things like this.

**Ian Johnson:** Okay.

**George Westbrook:** Um, I think the next thing is the the agent. Um, so going to be pushing some changes to production literally after this call. Um, that should hopefully you should see an increase in speed. Still not obviously where we well not obviously, but there's still some things I think we need need to change. Um, but from my perspective, it's a lot more noticeable. the the changes in speed. Um, optimize a decent amount of the tool call.

### **00:14:02**

**George Westbrook:** So, it's not going one, two, three, four, all the way up to 11. Um, it's bucketing them, bucketing them in a bit more, so it's a bit more efficient. Um, and in terms of like quicker operations, it's a lot quicker. There's still that approval step. Um, and it's obviously I think we mentioned before how whereas before it would be here's this plan I'm proposing. I accept the I accept the plan. Then there's like four approval steps after, now it is let's push everything up front. I'll ask you what you need. Um, here's my plan. Once you've clicked approve on the plan, it's going to do everything it asked for. Um, also on some of the so I think say for example if you went I want to suspend James Thornton's card um and there's two cards there just the ability you can click click the card kick through and then it's going to then it's going to go um and also if I can't remember an exact example, but it's it's going to show some of those UI elements like a form to fill something in. Um, I'm not happy with where it's currently at because it's a bit too restrictive.

### **00:15:14**

**George Westbrook:** Like I found there was one form I didn't know one aspect. Let's say it was the last four digits and I kind of just wanted to put I don't know this, just look look it up for me. But it was saying no, this is a required field. So you might notice some of them. Um, and I think it's on like four or five workflows. So, it' be good if you could have a play around once again, rip it, rip it to shreds. Um, and then we'll we'll keep on iterating and iterating on that.

**Michael Moores:** Yes,

**Ian Johnson:** Okay.

**Michael Moores:** sounds good.

**George Westbrook:** Um, and then I suppose new pieces of work that we we started is obviously what we spoke about last week with the with the knowledge. So I've been work busy working away getting like a UI version of in the in the knowledge hub of the co-pilot um just so that you can get a look and feel. Um obviously very basic at the moment. Um main focus will be uh look and feel.

### **00:16:10**

**George Westbrook:** Um and then I think one of the things we wanted to talk about was getting access to the content via um because we're just trying to think it's difficult for us to think without knowing how how we'd necessarily access it. Um, so if we if if possible, mate, if we could get access to to Umbraco, how we can query it via an API because what what we're what we're going to be doing is given the content that's in there, we'll build a representation on the MCP server for the agent. Think about refresh cycles be it on a on a timer or more web hook based where it's like content changed update so that next time that the MCP tool is queried it's going to make sure that it's always fresh content.

**Michael Moores:** Yeah, it's just a API key as far as I'm aware. So,

**George Westbrook:** Perfect.

**Michael Moores:** I'll speak to Stat Works. They've been managing this so far. I'm just getting them to show me how to set them up. Obviously, we're reading it from the knowledge hub already.

### **00:17:12**

**Michael Moores:** Um,

**George Westbrook:** Yeah.

**Michael Moores:** so it just be an API into that as well. So this week I've been putting up some documentation in there as well. So about 30 odd documents in there already. So at least is going to have some text for it to read as well uh when you're in there.

**George Westbrook:** Okay.

**Michael Moores:** So um that's the UAT and obviously we've got the production as well um that we're working on. So yeah, I'll speak to them today and see if I can get you the a separate key um from the knowledge and then we can make sure they're separate and then give access to that as well.

**George Westbrook:** I think also with the with this isn't this isn't urgent at all is with the with the API I don't think our subscription key is working. It's always returning I think 40 401 I think 403. Um, yeah, I think I suppose for us as long as we know for the time being the what the what the schema is, what the payloads are going to be, that's fine.

### **00:18:11**

**George Westbrook:** So that's that's not too early. But obviously when we get to testing on live APIs, I think that' be something we might need to get sorted.

**Michael Moores:** Yeah, I think with uh obviously at the moment you've got a shared one as well. I think as you said they rebuilt the environment and did a lot of stuff in the API um management in Azure. I have got a new key this morning. I've not tested it yet. So, as soon as I test that, I can send that across to you.

**George Westbrook:** I want to

**Michael Moores:** Uh, make sure you have that. But, yeah, when we, you know, get into the proper sort of stages, I think we'll get a dedicated key for for everybody. Obviously, especially production as well. So, when we get closer, I'll make sure we separate that and it's going to be consistent. Obviously, there's still legitimate to look at and and implement as well. So, there's still work authentication piece.

**George Westbrook:** PM

**Michael Moores:** So I do think that piece is going to change at some point as well.

### **00:19:01**

**Michael Moores:** So when we get to that point, I'll let you know what it is and make sure we have dedicated callings for each of the applications and then obviously we can make sure they're sort of long-term uh credentials basically.

**George Westbrook:** Okay, perfect. Um, and how's Stat Works getting on with with the with with their side of the bill?

**Michael Moores:** Yeah. So they show us quite a lot of stuff. Obviously they're they get obviously blocked much more than you do. So we have now hit a point where they need to know the APIs, they need to know the schemas etc. So it has slowed a little bit but they have done the you know the core the bits that they they can do such a permissions stuff like that.

**George Westbrook:** Yeah.

**Michael Moores:** So it's a good working copy but yeah there's some that need um multiple API calls. There's a couple of things that we need to pull down like um all cards for example from the the drop down. So we're speaking with DG how to do that.

### **00:19:55**

**Michael Moores:** it's not sort of built for, you know, public API because obviously you don't normally search all cards. So, a couple things like that we just need to align with DTON and make sure but they're yeah they're pretty good building the pages out. It's just a connection to those APIs that you know we have to hold a little bit on because you know things have changed from the design where we didn't even have the YAML at all. So there's quite a big change from their point of view in terms of um the fields that are shown and the validation and stuff. So, it's a bit more hardcoded than than automated,

**George Westbrook:** Yeah.

**Michael Moores:** but um yeah, it looks good. Um and I think yeah, as and when we go through the UAT and similar to you really as and when we get them, we'll let you know then at least we can align and obviously as soon as we sign stuff off that isn't going to change, we can tell you specifically. Uh but a lot of the focus at the moment from their side is the internal side.

### **00:20:45**

**Michael Moores:** Basically, how do we create a program? How do we get them set up? So, a little bit before the APIs that you're looking at. Uh, and then I've moving on to the external now, which we're going to start doing the UAT testing on as soon as we get the final piece, which is um the header. Um, so the moment The program manager ID is what we pass in. We've switched that to car program ID just so you don't have to give both IDs basically.

**George Westbrook:** Okay.

**Michael Moores:** So there's a little bit of stuff there um as and when you're calling basically. So that may change based on you know what we're doing. Obly internal API does have the full list of car programs as well. So you connect to that as an internal source. You get the car program that they're talking about. Naturally a user is assigned to a car program that sort of gives you that the ID. So it's just going to be sort of a um a body in a body input there just to sort of split that and that allows the routing on DT side to the proper infrastructure or wherever that's sat basically.

### **00:21:42**

**Michael Moores:** So it's still quite a large piece to iron out but I think they've just come back saying they're happy with the approach and just getting the time and obviously implementing that and applying that basically.

**George Westbrook:** Okay, perfect. Um, yeah. So, I think that's everything from from our side. Is there anything else any of you want to talk about?

**Michael Moores:** Not for me. Thank you.

**George Westbrook:** Okay, perfect. So I suppose got the stuff with the content side which I suppose Max and Max and Tyler you got you got hold of. Um obviously know know what we need to do with the with the outbound. Um get I'll get those changes pushed to the what the production version for testing for the agent. Um so be interested to hear your thoughts on that. Like I said still still more work to do still things that are going to be changing. Um, and then hopefully by the by next week there'll be something to show on the the co-pilot as well. Um, can't promise the the MCP is going to all be sorted by then, but at least they'll be able to get a look and feel for what the the co-pilot might be.

### **00:22:52**

**George Westbrook:** Um, I think what So, go on, Max.

**Max Kingaby:** I was just going to say um if I'm correct in saying we're waiting for something from Vonwin before we can proceed with the LinkedIn profile set up. Am I correct in saying that?

**Ian Johnson:** Yeah, Brmond's going to set up the company LinkedIn profile page.

**Max Kingaby:** Fantastic.

**Ian Johnson:** So, will let you know

**George Westbrook:** Um I think I think yeah I think that one of the things with the co-pilot that we were thinking is changing the position because I think at the moment it was click one thing and then you click ask AI and then it pops up. So, we might play around with the like position and location to be more like a like a typical co-pilot where it's kind of always there. Click it, pops up straight away. Um, just play around with a few ideas so that it's not not intrusive, but it's easy easy for a user to get to.

**Michael Moores:** Yeah, for me.

**Ian Johnson:** Yeah, sounds good.

**George Westbrook:** Perfect. Right.

**Ian Johnson:** All right. Cheers, folks.

**Michael Moores:** Cheers.

**George Westbrook:** Speak to you all soon.

**Michael Moores:** Thank you.

**George Westbrook:** You never get Press your feature on Thursday.

**Michael Moores:** Good afternoon. See you. Take care.

**Max Kingaby:** Yes, guys. My

### **Transcription ended after 00:24:13**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*
