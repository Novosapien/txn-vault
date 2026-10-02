---
date: 2026-10-01
type: standup
description: "Content Workforce paused to January, the shrinking spec explained, API versioning unsolved, and PII rather than PCI identified as the real exposure"
scope:
  - "[[content-workforce]]"
  - "[[developer-support]]"
  - "[[txn-api-reference]]"
  - "[[agent-access-layer]]"
status: extracted
extracted-to:
  - "[[content-workforce]]"
  - "[[commercial]]"
  - "[[docs-mcp-server]]"
  - "[[txn-api-reference]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN: Agentic AI Standup (2026-10-01)

> **Source:** Gemini transcript, 1 October 2026, 15:58 WITA, 43m. **Brett StClair**, **George Westbrook** and **Hasan Ahmed** from Bali with **Ian Johnson**, **Dorte Dye** and **Michael Moores**.
>
> **Ian led most of it**, and said so himself: *"conscious of the fact that I've taken up most of the time of this call."* It was largely his questions, and they were good ones.
>
> **The headline is a decision taken by email before the call**, which Brett opened by accepting: the Content Workforce pauses until January.

## The Content Workforce pauses until January

Brett, first item: *"Happy days with everything on that email... Thank you for the processing and no problem on delaying on the content stuff. That's not a problem at all."*

### Ian's reasons

**Too much running at once, and launch comes first:**

> *"We just want to make sure that we're not, we've not got too many overlapping things going on, and given that the launch and the post-launch activity is the primary thing, we're just going to hand that over to the marketing team and the external PR agency to manage that piece, and then **we'll pick back up with you in January**."*

**And the drafts were pitched at the wrong company:**

> *"Some of the themes from Tyler's document were a bit more appropriate to a company that had been in the market a little bit longer. Whereas we just need a plan of what it is we're trying to achieve over the course of the first kind of three to six months in terms of the content that we're putting out there."*

**It is a pause, and he was explicit about that:** *"you guys are very much part [of the] plans. It's just a case of just pausing while we get this first part done."* The marketing team and PR agency will produce a plan for the beginning of 2027, and that will come back before January.

Brett accepted it without pushing, and left the samples available: *"if you do like it, welcome to still post it and use it, on your personal profiles."*

### What it means

**Commercially.** [[commercial]] records the Content Workforce as verbally agreed on 4 August at roughly £1,750 a month plus a £3,000 setup, with papering still outstanding. A three-month pause with no papered agreement is worth checking rather than assuming: what was invoiced, what the pause does to the run fee, and whether the January restart re-opens the terms.

**For the knowledge graph.** Five months of configuration work is now parked: the manifesto, the pillars, the entity work, Dorte's and Ian's personal workforces, and the register rows that chase them. [[open-questions]] #86, the interview that drifted onto company material, and #82, the mood-dependent elicitation, both become January problems rather than this month's. **Michael's personal onboarding, the only one outstanding, does not now happen before launch.**

**And the messaging now sits with the group that took the 23 September position.** Ian has handed content to the marketing team and the external PR agency, which is Bronwyn and Nicola, the two people who agreed to *"be quite bullish about the full proposition"* and to *"get Ian on board with that"* in a room he was not in ([[open-questions]] #96). He is handing them the work without having seen that conversation. That is not a reason to keep the content with us; it is a reason to make sure he sees #96 before January.

Raised at [[open-questions]] #100.

## Outbound continues, and the pause creates a knot

**Ian separated the two engagements cleanly, and the outbound fee stands:**

> *"That's not a timing thing in the same sense of what we talked about with the content workforce. That's a very clear, we're not going to start this till January. **This is just, okay, we'll pay you the outbound fee. I have no issue with that.** You're doing work on the outbound fee to generate [the] list, and there's going to be more work to refine that. It's just when is the right time to start that, and who do we start it off with."*

**Status:** George confirmed the lead list lands **by the end of this week**, and the domains are being sorted.

**Ian wants a session on the list itself:** *"we can have a separate session on the list and how the list has been curated, and then we start to maybe tweak some of that."* That is the session [[open-questions]] on the register has wanted since he judged the earlier artefact too small, and it is also where the unvalidated cohort file from 23 September should be set against a real register.

### The knot

**Ian's own sequencing rule for outbound:**

> *"In go to market there's always been this thing about at least creating a bit of brand awareness and content out there before you start doing it. Otherwise there's nothing. If they search, they find nothing. If they go on LinkedIn, they find nothing."*

**So outbound should not send until there is content, and content has just been paused until January.** The resolution is not Novosapien's to make, because TXN's own marketing team and PR agency are now producing that content and they are working to a launch in the next few weeks. But it does mean **the outbound send date is now dependent on a plan Novosapien has no visibility of**, while the outbound fee runs. Worth naming at the list session rather than discovering in December.

## The shrinking spec is explained, and it is good news

This answers [[open-questions]] #94 directly. Hasan asked whether the OpenAPI spec had changed. Michael had DT's reply from the previous day:

> *"The reason things have disappeared is there are sort of aligning to what's been built, specifically what's been deployed. So very much aligning with what we're going live with. **As they build and deploy these APIs, that's when they'll show up in the YAML.** Hence why the spend controls has disappeared. That's because the initial [one] was basically really quickly generated. Now it's actually built off the code, and as and when they build."*

> *"**In a way it's much better, much more accurate**, but obviously it does mean you've lost some of that future stuff that you did have before."*

**So the 98 to 46 operation drop was not scope being cut.** The original spec was a hand-written forecast of what DT intended to build; the current one is generated from the code that exists. The operations did not disappear, they were never built in the first place.

**That reframes #94's question.** It asked how much rework the moving spec costs and when it stops. The answer is that the spec is now tracking reality rather than intention, so it stops moving when DT stops building, and the movement from here is additive.

### And DT says the build finishes this sprint

| Item | Michael |
|---|---|
| **Development** | *"I've been told that development is meant to finish by this sprint on everything from them anyway"* |
| **JWT endpoints** | Going into the YAML *"today or tomorrow"* |
| **Completeness** | *"From a spec point of view it should be pretty much complete at that point"*, minus the cards endpoint |
| **Caveat** | Michael still has to verify it: *"I've just got to go through that and make sure everything's working properly"*, and *"there may be a few minor changes to the fields if we're missing anything"* |
| **Access** | The YAML can be pulled from the new URLs without a full JWT key |

## How the knowledge hub reads the documentation

Ian checked an assumption and got a useful answer. His question: Umbraco is for pulling documentation periodically, *"but that's not how the co-pilot is going to go and read the documents, right?"*

**George's design, confirmed:**

> *"We're going to build a **local representation, or local file system version, of the documentation within the MCP server**. So when the agent is querying it, it acts exactly like a local file system, which these agents are really, really good at understanding and searching, rather than putting them in a vector database."*

**And the webhooks solve the freshness problem that was still open on 16 September:**

> *"One of the things we were thinking was, how is it going to be updated? Are we going to do a periodic check?... But it's good to know that there's webhooks in there. So when content published or unpublished or whatever event happens, we're going to update the representation for the agent, so that **every single time it's responding, it's directly aligned with what's published**. There's not going to be a case where it's answering from a piece of documentation that's two, three days, or even weeks old."*

**For the API specification**, which has no webhooks, periodic polling is the fallback and George is relaxed about it: *"it's quite a cheap operation. Here's the old one, check to see the new one, is there a change, update."*

## API versioning: the hardest thread on the call, and it is unsolved

Ian pressed this for roughly fifteen minutes and was right to.

### What TXN intends

| Element | Position |
|---|---|
| **Versions kept** | **Two**: current plus upcoming, or current plus previous, *"depends where you are on the release life cycle"* |
| **Lifecycle** | Internal staging, then **public sandbox**, then **client UAT**, then production |
| **Client choice** | **None.** *"When we release, the clients will just get given that release regardless of what they're on. They don't get a choice to pick"* |
| **Release content** | Monthly, **additive and non-breaking**. *"The client should build the system in a way where it can accept new fields without breaking"* |
| **Test window** | *"Two weeks here's a new version for everybody in client UAT, go and test it."* Marqeta precedent |
| **Major changes** | A separate concept, a true API version bump, *"if we do a whole new cardholder, completely different, we would then per se move over"* |
| **Design goal** | *"The whole design of it is that **you don't need to know the version number**"*, using current and latest endpoints rather than numbers |

**Why the past version exists at all**, which Ian asked: it is a by-product of keeping two. *"Once we've deployed and rolled out to production, it's there for... if anything's changed, if we want to look back at what it was before."*

### The problem Ian would not let go

> *"Somebody develops to version one, and then version two is put into client UAT and they just basically ignore it... **How will we know which API reference they're querying?** Because we wouldn't know if they're querying it because they're querying about production, or they're querying something based on the upcoming version that's effectively in UAT."*

**Michael's answer is honest about where it stands:**

> *"That's something we'll have to build into the agent... I say DT should be able to tell us explicitly which those two are, which will allow us to build that specific response in."*

> **"As of now it's all manual versioning. There's no, nothing in place at the moment."**

**It is blocked on DT**, and Michael has pushed it: *"I've not even seen the two endpoints for the different versions. That's something they've worked on with Stackworkz directly."* He sent DT a separate email the previous day listing what is needed to go live on the knowledge hub, and this is on it. Stackworkz has the same problem for the hub itself, *"when did we call it current versus previous."*

### Ian's proposed resolution, and it is the right shape

> *"Isn't the question right at the outset that there is an intuitive ask of which, whether they're asking from a UAT point of view or production, and we look at whichever one the relevant YAML is? **So you don't have to do the version number, but you're just checking what are they at**, because we don't know what they're doing. We don't know if they're querying it because they're looking to build the new stuff, or because there's something they're looking at from a production perspective."*

**That is the same pattern as the suspend-card fix from 29 September:** ask the one disambiguating question up front rather than guessing. Michael agreed it has to be built.

George added the useful extension: with both versions available, a user can ask what changed, and the agent can explain the difference and its implications.

### Use the change log, not a diff

**Ian's caution is the most important design point in this section:**

> *"I don't disagree with that, but I think that's more prone to potential errors... if we're already going to be issuing some form of documentation that accompanies the release... that's just another asset for you to basically go and grab, so that you've actually got the release note information. It just seems to me that that would take away any risk. And let's be clear about it, **however good the models are, they still come up with some stuff that's just not accurate.** And it's important that it is."*

**Michael confirmed change logs go into Umbraco**, possibly on a separate endpoint or folder so they can be filtered separately from the documentation, and published alongside deployment to the public sandbox, with the dates for staging and production in them.

**George's conclusion is the simplest statement of the design:** *"all we need is the current version of the YAML and the change log, without doing any fancy stuff. And then it's going to be able to look back in time and see, this was changed at this point."*

**So the agent should read an authored change log rather than compute a diff.** A diff is derived and can be wrong; a change log is a stated fact. Raised at [[open-questions]] #101.

### Release notes need sanitising before they are public

Ian caught this immediately:

> *"I'd just give a note of caution around publicly displaying the release notes, because I don't think it's for everybody to know... **we don't want our release notes falling into the hands of competitors.** There are things that they just don't need to know... we wouldn't want to say this has changed because we identified a problem with blah blah blah."*

**Michael confirmed the Marqeta precedent and the split:** public release notes existed, but *"internally they were very different. You know, we've done this because this was breaking and this was the impact. [Public] will be, we've changed this field."* Public notes stay at *"this is new functionality, this is a new field"*, with no reasons. More detailed notes go to clients directly.

**This matters for the co-pilot specifically**, because the knowledge hub is unauthenticated at MVP ([[open-questions]] #91). An agent grounded on a change log will repeat whatever is in it to anyone who asks, so the sanitising has to happen in Umbraco rather than in the agent's judgement.

## PII, not PCI, is the real exposure

Ian's last substantive question, and it produced the clearest statement of the data position yet.

### His worry, and George's correction

Ian asked what happens to card data once the agent pulls it back, and specifically: *"when we go to somebody just using Claude to do it, pulling that information back is one thing, that continuing to exist within Claude is not acceptable."* Then the sharper version: *"if you're using an LLM in the agentic experience to handle the queries and pulling back the data, **that data exists within that LLM**."*

**George corrected it, and the distinction is worth holding onto:**

> *"No, it doesn't exist within the LLM. With the Claude app, 100%, it's going to exist there. You can turn it off, but it's still stored on their servers in the chat. **We're accessing it via the API.** So whether we're using a Gemini model or an OpenAI model, they've got specific controls so that they're not going to store your data... these are enterprise APIs with those security measures in place."*

He also named the current model: **Gemini 3.8 Flash through GCP**.

Ian accepted it: *"Okay. All right. Understood."* And then made the right ask anyway:

> *"I think it's just worth getting out in front of this with your assistance, guys, because these are, if they're on my mind, they're most definitely going to be on people at DT's mind, and we should get out in front of that sooner rather than later."*

### The two tiers Michael set out

| Tier | Position |
|---|---|
| **PCI** | **Off the table.** *"I don't think we've scoped PCI at all. So that's just off the table for the agent, and returning the PAN."* Same as the Console, *"we've shielded that up from the API."* And deliberately: *"we can gate the agent to make sure it can never get PCI details. That's something we probably should do, right, you're not having PCI access at all, so the API wouldn't even return that level of detail"* |
| **PII** | **The real exposure.** *"The next one down is obviously PII data, cardholder names, addresses. **I think that's our largest pool that we need to consider that is being lifted and taken out of our system**, and there could be a copy of that as well. So that is one thing we need to consider and probably make clients aware of in some sort of documentation, that if they are taking it then they need to treat it appropriately"* |

**Michael's action:** document which APIs are high sensitivity, *"then we can discuss what we want to do about them, whether we put additional approvals or just don't allow them at all."*

**And he split the MCP server's purpose, which sharpens the problem:**

> *"The MCP for me has two functions. A, can you help me code to this? That's the big one... That's pretty simple, that's everything the knowledge hub does. **It's just the other side we need to have a look and lock down**"*, meaning the operational side, *"can they actually do some of this stuff."*

### Access depends on what is asking, not only who

George's framing, and it is new:

> *"It's not just who's accessing it, but **what's accessing it**. Is it the agent in the co-pilot? Is it the agent in the knowledge hub? Is it the agent in the full agentic experience, or is it their Claude? If it's their Claude, change the access levels. Anything that's ultra sensitive is not going to be returned and all those tools are off."*

**Ian's objection is a good one and it is unresolved:**

> *"It's not the same thing though, is it?... that doesn't really fit the 'we'll meet you wherever you are' scenario, does it? It's like, well, we kind of will, unless you want to do this, in which case you've got to go and log on to the control center to be able to do what you're asking to do. **So it needs some thought.**"*

So the client's own Claude gets a reduced surface, and the engagement's own promise says it should not. Ian accepted it is not the first thing to solve, but wanted it thought through.

Raised at [[open-questions]] #102. It advances **#69** on storage and the GDPR line, and **#73** on whether the MCP server needs its own permission model, by giving both a concrete shape: PCI gated at the API, PII documented and client-warned, and the surface varying by calling context.

### And the hosting question is the trigger for all of it

> Ian: *"We're getting to the point now where I think there's an open question to you guys about **what does the hosting environment need to look like?** With a view of taking that to DT and saying, this is what we're going to need to have in place. That is logically the point when a bunch of questions are going to start flowing through, for sure. So if we don't want a huge delay, we should get out in front of it sooner rather than later."*

That is the same list [[open-questions]] #70 and #85 have been circling since 3 September, now with a reason to finish it: it is the document that opens the DT conversation.

## Smaller items

### Michael's permission documents landed

George is working through them: *"it looks like there's a lot of the details there when it comes to how we're going to restrict the MCP server that the agent is going to use on behalf of the user, because that was always top of mind."* His read: *"it seems like these documents are going to be a thing that solves that, which is really handy."*

Michael's caveat: *"they are the design and requirement documents. The final sort of proof back from Stackworkz hasn't come back yet, but that's what we're working towards anyway."*

### A Stackworkz and DT session, requested

Brett asked for working sessions on **code integration and infrastructure access**, rather than exchanging lists of modules and third-party components: *"let's do a sit down with them, run through how we're going to get that moving."*

**Michael's sequencing, and the warning in it:** *"Stackworkz is the easy one. We still need to go through DT. **They're the ones that pushed back quite hard on some of the stuff last time.**"* Once the plan is settled with Stackworkz, the same run-through happens with DT, because *"if it is going in their infrastructure, they don't want to support libraries that aren't popular, aren't properly maintained."*

So the dependency list is not only models, it is every third-party library, and DT has a record of refusing them.

## Findings and where they landed

### Commercial and engagement

| Finding | Destination | Action |
|---|---|---|
| **Content Workforce paused until January**, handed to TXN's marketing team and PR agency | [[content-workforce]], [[commercial]], [[open-questions]] | New row **#100** |
| Reason: too much running at once, launch first, and the drafts suited an established company | [[content-workforce]] | Recorded |
| **Outbound continues and the fee stands.** List by end of week, domains in progress | [[delivery-schedule]], [[outbound]] | Recorded |
| **The pause creates a sequencing knot**: Ian wants content live before outbound sends | [[open-questions]] | Recorded in **#100** |
| Session wanted on how the lead list was curated | [[outbound]] | Recorded |

### The spec and the knowledge hub

| Finding | Destination | Action |
|---|---|---|
| **The spec shrank because it is now generated from built code**, not forecast | [[txn-api-reference]], [[open-questions]] | **#94 answered** |
| DT development finishes this sprint; JWT endpoints imminent | [[txn-api-reference]], [[open-questions]] | Added to **#32** |
| **MCP holds a local file system copy of the docs**, refreshed on publish webhooks | [[docs-mcp-server]] | Recorded; closes the freshness gap |
| Periodic polling for the YAML, which has no webhooks | [[docs-mcp-server]] | Recorded |
| **No version-awareness mechanism exists**, and it is blocked on DT | [[open-questions]] | New row **#101** |
| Ask the user which stage they are on, rather than infer the version | [[portal-co-pilot]] | Recorded in **#101** |
| **Read the authored change log, do not compute a diff** | [[docs-mcp-server]], [[open-questions]] | Recorded in **#101** |
| **Release notes must be sanitised before publication** | [[open-questions]] | Recorded in **#101** |

### Data and access

| Finding | Destination | Action |
|---|---|---|
| **Enterprise API usage does not retain data**, unlike the consumer apps. Currently Gemini 3.8 Flash on GCP | [[architecture]], [[open-questions]] | Recorded in **#102** |
| **PCI off the table**; the agent should be gated so the API never returns it | [[open-questions]] | New row **#102** |
| **PII is the largest exposure**, and clients need telling how to handle it | [[open-questions]] | Recorded in **#102** |
| Michael to document which APIs are high sensitivity | [[open-questions]] | Action recorded |
| **Access varies by what is calling**, and that breaks "meet you where you are" | [[open-questions]] | Recorded in **#102**, advances **#73** |
| The hosting environment document is the trigger for DT's questions | [[open-questions]] | Ties to **#70** and **#85** |
| **DT has refused third-party libraries before** | [[integrations]] | Recorded |

## Open actions from the call

| Action | Owner | Note |
|---|---|---|
| Produce the lead list | Novosapien | **End of this week** |
| Book a session on how the list was curated | Both | Ian asked for it |
| Define what the hosting environment needs to look like | Novosapien | Ian: the trigger for DT's questions, do it early |
| Document which APIs are high sensitivity | Michael | Then decide: extra approvals, or disallow |
| Gate the agent so PCI is never returned | Both | Michael: *"something we probably should do"* |
| Get DT's version-identification endpoints | Michael | Emailed; needed to go live on the hub |
| Set up the Stackworkz integration session | Michael | Then the same with DT, who pushed back last time |
| Pick the content plan back up | TXN marketing and PR | Plan for early 2027, before January |

---

## Transcript

Oct 1, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:01:06**

**Dorte Dye:** morning.

**Brett StClair:** How are you?

**Dorte Dye:** You have the right outfit now for Bali.

**Brett StClair:** Yeah, I know. I'm running low on clothes now.

**Dorte Dye:** As if they wouldn't have any laundry shops there.

**Brett StClair:** I know I'm lazy like that.

**Dorte Dye:** I honestly I fear for Lily because she's probably the one who has to No, I'm not saying that. I'm just I'm literally just reflecting.

**Brett StClair:** She She'll She'll never do that.

**Dorte Dye:** She would not.

**Brett StClair:** He's like not a job.

**Dorte Dye:** It's a completely different generation, isn't it?

**Brett StClair:** Yeah, exactly. I literally came back from Umbrea. I had a day at home and loaded the washing machine, packed everything up, got the drying, managed to drive. Next morning, everything was dry enough and just repack my bag with the same stuff.

**Dorte Dye:** You need laundry service. You morning

**Brett StClair:** Morning The weather looks great in the

**Ian Johnson:** Morning.

**Brett StClair:** UK. Hey,

**Ian Johnson:** Yeah, it's sunny today. It was hammering down here last night, but yeah, it's sunny now.

### **00:02:25**

**Brett StClair:** I'm I'm hoping to arrive at a cool, slightly overclouded weather and try cool off.

**Ian Johnson:** Uh,

**George Westbrook:** No.

**Ian Johnson:** I just don't just don't ride back in that shirt, Brett. Whatever you do.

**George Westbrook:** No.

**Brett StClair:** So that's you have commented on my stunning shirt.

**George Westbrook:** Take the hint.

**Brett StClair:** Um, cool. So we're all in. Ian, should we just quickly cover up? Happy days with everything on that email on uh kicking off all that kind of stuff.

**Ian Johnson:** Okay.

**Brett StClair:** Thank you for the processing and no problem on delaying uh on the content stuff. That's not a problem at all.

**Ian Johnson:** Okay, cool. Thank you.

**Brett StClair:** So

**Ian Johnson:** I appreciate it. Just we we just want to make sure that we're not we've not got too many overlapping things going on and um

**Brett StClair:** yeah.

**Ian Johnson:** given that the launch and the post-launch activity is the primary thing, uh we're just going to hand that over to the marketing team and the external PR agency to manage that piece and then we'll pick back up with you in uh January.

### **00:03:33**

**Ian Johnson:** But there's well before January because they're going to put a plan together of what they think um the beginning of 2027 should look like. So

**Brett StClair:** And if you I know uh Tyler has generated a bit of kind of sample pieces of posts and stuff. So if you do like it, welcome to still post it and use it and all that kind of stuff. So that's no problem as well on your personal profiles.

**Ian Johnson:** yeah, I think that's partly the other thing. It's also about the the timing of and the themes that we want to go without the doors. So some of the some of the themes from Tyler's document were were a bit more appropriate to a company that had been in the market a little bit longer.

**Brett StClair:** Okay.

**Ian Johnson:** Uh whereas we just kind of need to be um we just need a plan of what it is we're trying to achieve over the course of the first kind of three to six months really in terms of the content that we're putting out there. So, um, we can pick back up on on that, um, whole piece, but you guys are very much part plans.

### **00:04:35**

**Ian Johnson:** It's just a case of just pausing while we get this first part done.

**Brett StClair:** I completely understand.

**Ian Johnson:** Okay.

**Brett StClair:** Um, cool. So, uh, Mike, thank you very much for all your emails on all the detail. Um, got a very happy engineering team who are borrowing away and doing lots of reading. Um, and have some questions. Is it okay if we fire away some questions? I guess do you want to jump in with the broco stuff and then George? How you do you have back?

**George Westbrook:** still still digesting the the stuff with the authentication and and but I mean just a quick one on that. I mean it it looks like there's a lot of the details there when it comes to like how we're going to restrict the the MCP what the MCP server that the agent is going to use on behalf of the user because that was always top of mind is like okay we're talking about restricting the agent actions given the users access levels are we how are we going to work that out but it seems just I can't say everything's in um because I don't know yet.

### **00:05:48**

**George Westbrook:** Um but from looking through it, it seems like these documents are going to be a thing that solves that which is really really handy.

**Michael Moores:** Yeah, like say they are the sort of design and requirement documents. I say the final sort of proof back from Stat Works hasn't come back yet, but that's the what we're working towards anyway. So, should give you some background.

**George Westbrook:** Yes, I fit on the Han on the bra coaster.

**Hasan Ahmed:** Um, so like I did have like a skim through I mean like it was kind of like a brief like overview. I mean I queried all of the like endpoints in the actual the sandbox and everything seems to be in order. Um, I mean like I was going to ask about the actual open like API spec if there's like update like onto that or if there's be any changes as in cuz like I think notice is like only the um actual sandbox and like like everything's there just want to be clear that the open API spec like hasn't also been like updated as well.

### **00:06:55**

**George Westbrook:** Don't know if it's just me, but your mic sounds awful as just put the input as

**Ian Johnson:** It does.

**Hasan Ahmed:** Guess it was a problem.

**George Westbrook:** your your laptop because I feel like I want to have myself in the head when I'm listening to you

**Hasan Ahmed:** Hello.

**George Westbrook:** speak.

**Hasan Ahmed:** Um, is it

**Ian Johnson:** Keep going.

**Hasan Ahmed:** Yeah. So, like I was asking like about the like open API spec if if there has been any updates onto it or if it's the same like as it was.

**Michael Moores:** um yeah so the way we got a response back from DT yesterday so the reason things have disappeared is there are sort of aligning to what's been built specifically what's been deployed so very much aligning with um you know what we're going live with so as they build and deploy these APIs that's when they'll show up in the YAML um hence why the top spend controls has disappeared. That's because um the initial cup was basically really quickly generated. Now it's actually you know built off the code and as and when they build.

### **00:08:01**

**Michael Moores:** So in a way it's much better much more accurate but obviously it does mean you've lost some of that future stuff that you did have before. So um I've been told that development is meant to finish by this sprint on everything from them anyway. So from a build point of view, obviously I still need to go through and check everything. It should be there and done. Um JWT is another one they're putting in the YAML. So you'll have also those endpoints as well that I've sent on the email in that YAML as well. That should be from an endpoint of view minus the the cars endpoint I've put on that email. Um should be complete from an endpoint of view. Obviously, I've just got to go through that and make sure everything's working properly and stuff like that. So, there may be a few minor changes to the fields if we're missing anything or whatever that may be. But, um, yeah, from a spec point of view, it should be pretty much complete at that point.

### **00:08:53**

**Michael Moores:** Obviously JT you don't need the full JT key to get the YAML and stuff like that. So, you should be able to pull down from those new URLs I gave you quite easily. Um,

**Hasan Ahmed:** Yeah.

**Michael Moores:** and that does reference the the most recent one. I think it's today or tomorrow we should be getting the JWT stuff in there as well. Um, so that should change, but there shouldn't be too much in there that changes now.

**Ian Johnson:** Can I can I just check something? I'm pretty sure I know the answer, but I'm getting old, so my memory goes. So, you're just mentioning Umbraco and connecting into Umbraco. That That's just so you can get hold of the documentation on a periodic basis, but that that's not how you're going to that's not how the co-pilot is going to go and read the documents, right?

**George Westbrook:** No. So, so what what we're going to do with the so the MCP server for the well both co-pilots actually um but mainly in the context of the knowledge hub MCP server and knowledge hub co-pilot.

### **00:09:54**

**George Westbrook:** What what we're going to do is build a a local representation or local file system version of the documentation um within the MCP server. So that when the agent is querying it, it acts look fields acts exactly like a local file system which these agents are really really good at understanding um and searching and things like that rather than say putting them in a vector database um and stuff like that um and the way that it's going to because one of the things

**Ian Johnson:** Yeah.

**George Westbrook:** we were thinking was well how is it going to be updated? Are we going to do a periodic check? Are we going to do this? Are we going to do that? But it's good to know that there's web books in there. So when content published or unpublished or whatever event happens and how we decide to deal with it, we're going to update the update the representation for the agent so that every single time it's responding, it's directly aligned with what's published or unpublished. So there's not going to be a case where or I can't foresee a case where it's going to be answering from a piece of documentation that's 2 3 days or even weeks old.

### **00:11:07**

**Ian Johnson:** And does that and then from a YAML perspective so the actual API reference how are you managing Yeah.

**George Westbrook:** Same process. We can just that one might unless we if we we've not got web hooks we just be doing periodic checks. So it could be I mean because it's quite a cheap operation just here's the old one check to see the new one is there a change update um and then that yeah that should that would be the approach or one potential approach Yeah.

**Ian Johnson:** Okay. And then is there any just on the on the two versions that we're going to have available, Mike? Um, so current and if I've understood it understood it current and future, is that right?

**Michael Moores:** Well, it's always me two. So, sort of two uses, current and future, and then current and past. So sheepended. depends where you are on the release life cycle. So it might be this is one we're on now, this is one that's coming and then when we deploy and we're doing nothing in terms of deployment of the month, it'll be this is what you're on now and this was the previous release.

### **00:12:11**

**Michael Moores:** So we'll always keep those two releases uh continuously basically.

**Ian Johnson:** So how how h how how will the MCP server know and I'm talking about in the context of the knowledge hub. So somebody wants to ask the question about the API reference document. How the MCP server know which version of the document to look at?

**Michael Moores:** We're still waiting on that from DT. Same for the console. Uh the the knowledge itself. So did you haven't done any versioning or

**Ian Johnson:** Yeah,

**Michael Moores:** so.

**Ian Johnson:** I don't I mean more in the sense that if I'm a user and I say, you know, please explain, you know, what what field value should go in wherever. I don't know. I'm not a developer as you can probably see by the way that I'm talking about it. But nonetheless, that per we wouldn't know which version of the spec they're looking at, would we?

**Michael Moores:** um DT is is supposed to be providing a solution for knowing what the current versus what the the previous or the upcoming is.

### **00:13:16**

**Michael Moores:** So that's the bit I've not seen yet. But there is supposed to be a solution with their talks with stat work saying we can pull down the the current which is deployed now and also that supplement one whether it's a previous or the other future states. So there should be something in that API call that we know is the current latest one if that makes sense.

**Ian Johnson:** Okay. But I'm thinking more from a user's perspective, right? So they have so they don't necessarily know that there are two versions available and let's say that they're on the old one and there's a current one because they haven't made whatever changes. So they're out there, they make a query. How do we know which a which version of the file the MCP server is supposed to be responding or the co-pilot supposed to be responding to?

**Michael Moores:** Stop saying sorry.

**George Westbrook:** So would we sorry so would I'm assuming usually a user would know if they're working with it what version number they they currently have or is that something that they're not always going to be aware of?

### **00:14:20**

**Michael Moores:** Um so it just be one central version for everybody. So it'll be more life cycle in stages where we are.

**George Westbrook:** Okay.

**Michael Moores:** So we have obviously internal staging that we do. We have um public sandbox which is obviously when we produce it to the world. We would put that on to say this is this is coming up and then after that point we go into client UAT which is obviously where they can test and then we roll it to production. So rather than a knowing what version they're on it's for this is what's coming. So it's knowing what version in each environment obviously that's not something we've given to DT about making sure we know what stage we're in when we produce these APIs. So obviously I think the MCP can look Okay, we've got this new one in public sandbox. So that's where you're going to be connected to um from a knowledge point of view. So I'll know at the point that's a new release and then there's need to be some mechanism to say right we've deployed now in production.

### **00:15:12**

**Michael Moores:** Um so that's a mechanism we're still waiting for DT to confirm and that's the sort of stage that would know okay it's been released to you in production or you go this is something we have built it is coming um you know waiting for the release notes for deployment into production or something like that. So that's a sort of mechanism obviously we can speak to DT on how that works specifically but as as of now it's all manual versioning there's no u nothing in place at the moment so that's something we're working on with stat works with them for the knowledge hub specifically because they have the same issue as Ian's just highlight when did we call it current versus uh you know previous and stuff like that so it's still waiting to be ironed out that but the expectation is DT will present that information to you to make that decision rather than having to try and figure that out yourself basically.

**George Westbrook:** and then we can just given given that just query the the YAML version and then that's the YAML version that the agent agent uses and I suppose if a user is like oh I thought I was on this

### **00:16:09**

**Michael Moores:** Yeah.

**George Westbrook:** version what's the difference the agent can pull in the other version it'll be labeled as past and then current and then the way we represent it is that it's shown as this is past this is the current and then it can look through the difference and I suppose help users that might be wondering what the changes are and what implication that has on

**Michael Moores:** Yeah, definitely. I think obviously um the whole design of it is that you don't need to know the version number. So, it's going to use current, latest, I can't remember the terminology, but using those sort of endpoints to say give me this one, give me that one. It could be whatever version underneath, but you just know the stage it's in and that's the one to present basically. So I've pushed that on a separate email went to DTS yesterday as well with those things to get us live in the knowledge hub. That's one of them in there. So that will be pushed from our side to get a conclusion on basically

### **00:17:03**

**Ian Johnson:** But okay, it might might be my ignorance, but I can still I still foresee some problems here. So, so let's say that even in the flow you just described, Mike, somebody develops to version one and then version two is put into client UAT and they just basically ignore it. They do nothing with it. So they are effectively they've still coded to version one at at some point presumably version two becomes our production API and therefore if I'm if I'm on the person on version one I'm not querying version two necessarily I might be querying version one and it might not be I don't want us to think well again it's been my misunderstanding but what happens if in their they're working in the sandbox using the knowledge hub. they've already built a bunch of API calls and then they've gone live or maybe not even gone live and now they want to add some other things. Okay, so at that point they whatever they've built was built in version one. They're still on version one. Logically, I don't know, wouldn't they still be thinking that they're querying against version one irrespective of the stage?

### **00:18:25**

**Michael Moores:** So there's two different versions here. The one you're talking about is when we make major changes. U now when we release the clients will just get given that release regardless of what they're on. They don't get a choice to pick.

**Ian Johnson:** Okay.

**Michael Moores:** So with our monthly release, we'll just obviously the whole point of it is don't introduce breaking changes. So we introduce it, we warn them it's coming.

**Ian Johnson:** Yeah.

**Michael Moores:** That's that's how Marqueta sorted it. The second one that you're sort of referring to is the API version. So let's say if we do new a whole new card holder completely different we would then persever move over. So that's more for them huge large scale changes. This monthly thing would be sort of the small incremental changes we add new functionality not taking things away not breaking anything. So the client should build the system in a way where it can accept new fields without breaking. So all these changes we do should be additive um and we can roll them out to everybody in one go.

### **00:19:19**

**Michael Moores:** So the reason for the phasing obviously we give them chance to have a look at it. Basically it's a public sandbox first come and play with it. They get a period of time in the client UAT where we go okay have two weeks here's a new version for everybody in client UAT go and test it um and then if there's any issues we obviously alert us before then then in a period of time afterwards we then deploy the production. So for that phase roll out of that version um making sure we give enough time to our clients um you know I think Mark did two weeks for um UAT to test that before they pushed into production. Um so it's more about the notification that's happening and then from our change uh change logs we can say this is the release has been deployed please go and test it for a period of know x weeks and have that in our release plan to say we're going to deploy on this date and that's s sort of communication we would give up to our clients to say that this new release is coming and what and what's in that obviously

### **00:20:19**

**Ian Johnson:** Yeah, I must be being stupid then. So, okay, let me give another scenario. You did what happens is happening as you just described it that there's a new release coming and they've been told that it's in the UAT and they've got a period of two weeks. They've also got an operational system already. How will we know which API reference they're querying? Because we wouldn't know if they're querying it because they're querying it about production or they're quering something based on the the upcoming version that's effectively in UAT.

**Michael Moores:** That's something we'll have to build into the the agent to sort of This cipher um obviously in the knowledge hub is a quick toggle so they can look at what's coming what's not so they can see that quite clearly on the page I think with the agent is going to have to be based on their question and whether we we do compare the differences in the amble to see if there's any you know new changes we'll also have the the change log on the knowledge will just explicitly show what the changes are so I think the agent's going to have to have some sort of connection and context between those to make sure it say you know I found this field but it is in the upcoming release um and that sort of thing.

### **00:21:32**

**Michael Moores:** So, it is something we'll have to build for. Um but I say DDT should be able to tell us explicitly which those two are which will allow us to build um that specific response in basically.

**Ian Johnson:** Okay. So, the aim is that they don't need to know the version number.

**Michael Moores:** Yeah.

**Ian Johnson:** Um, they'd have been alerted if there's a new version in the in UAT. Um so therefore it isn't the question right at the outset that there is an intuitive ask of which whether they're in UAT they're asking from UAT point of view or production and we look at whichever one the actual YAML is the the relevant YAML seems to be the way to do it. So you don't still don't have to do the version number but you're just checking what are they at because we don't know what they're doing. We don't know if they're quering it because they're looking to build the new stuff or they're quering it because there's something they're looking at from a production perspective.

**Michael Moores:** Yeah.

**Ian Johnson:** So, I think that might be the the neatest way to go with it.

### **00:22:35**

**Ian Johnson:** I've got one question. Given everything that you said, why is there a why is there ever a past version? Because

**Michael Moores:** So, well, that's just the the sort of two versions obviously. So the knowledge hub keeps hold of the two versions. So regardless of when it is, it's like okay the past version is this is what was in production. That's the only thing it's there for. So once we deployed and rolled out to production, it's there for sort of see if it anything's changed if we want to look back at what it was before.

**Ian Johnson:** Okay.

**Michael Moores:** Um so it's more just a a fallout of having two versions basically. So we have two versions of knowledge hub. So the idea for that was to show the upcoming one, but it also shows the the historic one by default as well. So that's the only but obviously it's there in case someone wants to go back and have a look what it was, you know, a week ago for example. If we

### **00:23:33**

**Ian Johnson:** And within the co-pilot, would I be able to ask what's changed?

**George Westbrook:** Yeah,

**Michael Moores:** Yeah.

**George Westbrook:** we've if as like I think we've got access to those two versions, we can a user can ask on this version, what's the difference between this and the past the current and the the past or the current and the future? Pardon me. Um yeah, if if if we can access it, we can give it to the agent and the agent can answer from it. We just we just maybe have to work out how do we represent it to the agent cuz we could just say pull down two YAML and then present it like that or we could pull down two YAML do a function see what's the same see what's different so that we're not overloading the context and effectively document

**Ian Johnson:** Well, I I don't disagree with that, but I think that's more prone to potential errors. Um whereas if we're already going to be issuing some form of documentation might that accompanies the release I don't know where that would be whether it would be an umbraco like that's just another asset for you to basically go and grab so that

### **00:24:40**

**Michael Moores:** Turn yourself.

**Ian Johnson:** you've actually got the release note information and that's what you somebody asked that question. It just seems to me that that would take away any risk. And let's be clear about it, you know, however good the models are, they still come up with some stuff that's just not accurate. Um, and it's important that it is. So,

**Michael Moores:** Yeah, and obviously from Umbraco side, the change log stuff is going in there as well. So you'll get all them as well. I think from when I was looking at it, I think you can point it at a folder. So you can have two different endpoints if you wanted to. I will double check. So you can have a change log to one endpoint and you know actual documentation publishing to another. Um I think we can split that out by doing sort of filters as well for you. So all the documentation will come out with content published. So as we publish it, you'll see a new change log in Umbrau.

### **00:25:34**

**Michael Moores:** Um and then obviously you'll get that information as well. Uh from there

**George Westbrook:** I suppose when when there's a future a future one released, there's going to be on the change log. This is what's coming in the future, I'd assume. Okay, perfect. Yeah. Yeah. So, I suppose all all we need is the current version of the of the YAML and the change log without doing any any fancy stuff. Just those two those two documents. And then it it's going to be able to look back in time and see, oh, this was changed at this point, that was changed at that point.

**Michael Moores:** Yeah, I think the the flow I say need to go through it, but the the flow we've done is obviously internal UAT where we we sign it all off. We put it in the public sandbox. The reason for that obviously it's your first initial does it work your sort of pilot if you will. some people start using it but at that point it also updates the website as well.

### **00:26:25**

**Michael Moores:** So that's at the point where you know automatically you'll see there's a change. So I think what we should probably be doing is publishing the release note alongside that deployment to public sandbox. Then you've got this is what's change changing and this is in the public sandbox. Then there's a period of whatever time we decide with with DT of going through client stage client staging and production. So, at that point, we publish the release note, if you will, to say it's coming. Um, it'll have the dates in there when we're progressing as well and when we plan to push that to production and staging. But then also you've got the YAML to go alongside that as well. So when you get that notification, you can you can look at the public sandbox, you get that latest YAML and then you know that that's for the the latest release, if you will.

**Ian Johnson:** So, I'm I'm all right with that. I'd just give a note of caution around if I've understood what you were saying, Mike, about publicly displaying the release notes because I don't think it's for everybody to know.

### **00:27:27**

**Ian Johnson:** Um, so the only people that should really see those that release note information in my opinion are really clients proactively. So we would, as you've already described, we would have to let clients know that this is being deployed into public sandbox and it's going into UAT to follow the process you described. But if if I was just going on and I could be anybody in the knowledge hub, um I think we've got to just guard against the fact that we don't want our release notes falling into the hands of competitors as far as I'm concerned. There's like things that they just don't need to know. It might be standard practice that release notes are published and we're okay with it. Um but again we I think we just need to think about what in that case what's the content of the release note as in we wouldn't want to say this has changed because we identified a problem with blah blah blah. We wouldn't want to do any of that stuff.

**Michael Moores:** Yeah. Yeah. It's definitely so definitely lying to Marqueta.

### **00:28:32**

**Michael Moores:** So I would say it's a full release note, but Marqueta do publish public release notes. Obviously internally they were very different. You know, we've done this because this was breaking and this was the impact. It'll be we've changed this field.

**Ian Johnson:** Yeah.

**Michael Moores:** So there's some sort of manipulation to do there to just pull some stuff out. They definitely didn't say everything in them.

**Ian Johnson:** Yeah.

**Michael Moores:** Um so there were more detailed release notes going to clients but I think for a more this is a new release that's coming obviously that's the point people can look at easily without us giving them obviously we can build off sort of automation off those websites and feeds as well so they can get alerted inside so we'll have to publish you know something just say this is coming then it's up to us how much detail we want to put in there specifically about what's changed um but it's usually just a high level this is new functionality this is a new field. Those sort of things that are not not breaking but different to the payloads.

### **00:29:27**

**Michael Moores:** We wouldn't add any detail about why we've done such things.

**Ian Johnson:** Okay.

**Michael Moores:** Uh we sort of hide that for our internal client basically.

**Ian Johnson:** Okay. Sounds good.

**Michael Moores:** Yeah, like I said, I'm just waiting for DT on the how we get that information. Um I've not even seen the two endpoints for the different versions. So that's something they've worked on with Stat Works directly. So, I'm just waiting to see that and how we can pull that and I'll let you know.

**Ian Johnson:** Okay.

**Brett StClair:** Then can we set up some time with stack works guys to talk about getting the code integrated um and the access to the infrastructure. So, I'm just thinking there's going to be a fair amount to do there. And I think instead of going backwards and forwards and kind of these are the modules and these are the different components, third party components we're going to be using, let's do a sit down with them, run through how we going to go about and get it get get that moving.

### **00:30:28**

**Brett StClair:** I don't know what your thoughts, Mike.

**Michael Moores:** Yeah, I think obviously Statworks is the is the easy one. Um, you know, we still need to go through DT. So, they're the ones that sort of push back quite hard on some of the stuff last time. So, I think certainly for now to get an idea of how we want to integrate, we can speak to Stat Works. Once we sort of finalize the plan with stack works, we probably need to do the same run through with DT just to make sure you know if it is going in their infrastructure um you know they don't want to support libraries that you know aren't popular aren't you know properly maintained for example um so we just need to double check with them that if it is being hosted over there then this is the things that we have in and they're happy with that basically. So yeah, we can certainly get that up.

**Ian Johnson:** So,

**Brett StClair:** Okay.

**Ian Johnson:** so conscious of the fact that I've taken up most of the time of this call, I've got one other point that's bugging me a little bit, which is um in the agent, if I query, I don't know, if I ask the question to bring back cards that are I don't know, issue that have got um a MCC spend control restriction on whatever MCC code or whether it's whatever it might be that will pull back a list of cards presumably.

### **00:31:49**

**Ian Johnson:** Yeah. With whatever information that's available on that. What happens to that once that has been pulled back?

**George Westbrook:** What do you mean in terms of like where is it stored? How is it stored?

**Ian Johnson:** Yeah, that so I'm just I'm I'm pretty sure the answer to it is it's within our environment, whatever that environment is. Uh which is totally fine. Um I'm thinking more about when we go to the somebody just using Claude to do it, pulling that information back is one thing that continuing to exist within Claude is not acceptable. So, it's got to kind I know that I I can't remember who it was. There's a function that you can tell it not to keep the the query,

**George Westbrook:** Yes.

**Ian Johnson:** but I just think we need and the reason I raise it at this point, I'd already written it down, right? The reason reason I raise it on the back of your DT thing is I expect there'll be a bunch of questions that come from DT along those lines which we should have as well but we just need to think the stuff that's within our envir within our environment all of it's stored within our environment as I understand it but still you're still using claude or chat gdt or whatever to do

### **00:33:06**

**Michael Moores:** Yeah.

**Ian Johnson:** the LLM part right

**Michael Moores:** Yeah. I I guess yeah, I think you know DT are going to ask them bits but you know there's nothing stopping you using claw to hit the API as well. So there are mechanisms for claw to keep that in either scenario. Obviously we I don't think we've not scoped PCI at all. So I think that's just off the table for the agent and return the PAN from at least the external point of view. Um same as the console is so so yeah we just have a look at what we store and what we return and make sure it's very clear to DT. I think there's no difference between you going through the console or Claude or if you just gave your API credentials to Claude and and let it go away. So it's going to have the same level access and the ability to pull data that you could get you know elsewhere basically. So I think we just need to align that internally and then speak to make sure it's clear to DT on what's going to be returned and specifically um I say PCI is not so that's a very clear uh one or we can we can gate the agent to make sure it can never get PCI details.

### **00:34:15**

**Michael Moores:** So that's something we probably should do right you're not having PCI access at all. So the API wouldn't even return that level of detail. The next one down is obviously PII data you know card holder names addresses and stuff like that. I think that's our largest pool that we need to consider that is being lifted and taken out of our system and there could be a copy and something of that as well. So that is one thing we need to consider and probably make you know clients aware of as well in some sort of documentation that you know if they are taking it then they need to treat it appropriately.

**George Westbrook:** I suppose in terms of access as well with the MCP service, it's not just suppose who's accessing it, but what's accessing it. Is it is it the agent in the co-pilot? Is it the agent in the knowledge hub? Is it the agent in the full agent experience or is it their claude? If it's their claude, change the access levels. anything that's ultra sensitive is not going to be returned and all those tools are off.

### **00:35:14**

**George Westbrook:** Um, and we'll just maybe make users aware that there's certain limited functionality when it comes to anything that's being used by a third party source. Um whereas obviously I suppose things that are like the full agent entering experience or the co-pilot within the console all gated information is going to be there but in the same way that I think you were saying Mike is you can click a few buttons you're going to see it in the console anyway. Um so it's still same infrastructure same access as if they were in the console.

**Ian Johnson:** It's not the same thing though, is it? So unless I'm misunderstanding, which a very strong chance I am, George, but if you're using an LLM in the agentic experience to handle the the queries and pulling back the data, That data exists within that LLM.

**George Westbrook:** No, it it doesn't exist within the LLM. Um, so say like with with Claude um like the Claude app 100% um it's going to exist there. can turn you can turn it off but it's still stored on their on their servers in the chat.

### **00:36:23**

**George Westbrook:** Um we're accessing it via the API. Um so be it if we're using a Gemini model and OpenAI model um they've got specific controls so that they're not going to store your data because there's say for example I think at the moment we're using Gemini 3.8 Flash um through

**Michael Moores:** Okay.

**George Westbrook:** GCP. I mean, they've got massive, massive, massive enterprise clients who obviously similar to yourself really hot on the fact that I do not want this sensitive data being stored somewhere that I've not got control of um because it's if it was if it was the clawed app or chat GPT app 100% but I think these these are enterprise APIs um with with those security measures put in put in place.

**Ian Johnson:** Okay. All right. Understood. I think it's just worth Mike. I think it's just worth getting out in front of this with your assistance, guys, because these are so if they're on my mind, they're most definitely going to be on people at DT's mind, and we should get out in front of that sooner rather than later.

### **00:37:30**

**Ian Johnson:** We've then got this debate about the whole Claude piece that we need to think about in terms of what we're actually offering there. Um because to a certain degree uh George I agree with you the fact that you could just restrict what you can do but that doesn't

**George Westbrook:** Yeah.

**Ian Johnson:** really fit the we'll meet you wherever you are scenario does it? It's like well we kind of will unless you want to do this in which case you've got to go and log on to the control center to be able to do what you're asking to do. So it needs some thought. I know it's not the first thing that we're doing, but if it's we we need to think it through,

**George Westbrook:** Yeah.

**Ian Johnson:** but the the most important thing is to get out in front of the what the agentic experience really means. How does it work and the things that you've kind of just described in summary? We'll just need to put some more detail around so that we can we can head off the questions before they come.

### **00:38:32**

**George Westbrook:** Hey.

**Ian Johnson:** We're getting to the point now where I think there's an open question to you guys about what does the hosting environment need to look like? Um, and that with a view of taking that to DT and saying, "Hey, look, this is this is what we're going to need to have in place." That is logically the point when a bunch of questions are going to start flowing through for sure.

**Michael Moores:** No.

**Ian Johnson:** So if we don't want a huge delay, we should get out in front of it sooner rather than later.

**George Westbrook:** Yeah.

**Michael Moores:** Yeah, what I'll do as well, I'll put some sort of functional stuff to together. Obviously, pins, pans, we're not going to return, I don't think, in the the agent solution. We aren't doing that in the console either. So, you know, that's we've shield that up from the API. So, I think there's some stuff in there we can look at maybe not allowing and we can discuss which ones are the high sensitivity, stuff like that. So I'll start just I'll document that down so you can see what APIs are the high sensitivity.

### **00:39:28**

**Michael Moores:** Then we can discuss what we want to do about them whether we put additional approvals or just don't allow them at all and then we can see from there. Obviously the MCP for me has two sort of functions obviously a is can you help me code to this? So that's the the big one. So helping them look at the YAML and the endpoints and obviously secondly it's the more operational side like can they actually do some of this stuff as well. Um, so I think we're quite easy on the the developer side.

**Ian Johnson:** All

**Michael Moores:** That's, you know, everything the knowledge hub does. That's pretty simple. It's just the other side we need to to have a look and lock down basically. So I'll put some notes together on that as well.

**Ian Johnson:** right, sounds good.

**George Westbrook:** Okay, I think the last thing is on the outbound stuff like I said there'll be a list by the end of the week domains are being sorted. So I thought just chuck that in at the end rather than just leaving it leaving it to be forgotten about.

### **00:40:21**

**Ian Johnson:** Yeah, we can have a separate session on the list and how the list has been curated and then we start to maybe tweak some of

**George Westbrook:** Yeah. Eight.

**Ian Johnson:** that. But but yeah, that's that's the one that we we do want that to start. clearly question mark of when that starts down to there's in my view in go to market there's always been this thing about at least creating a bit of brand awareness and content out there before you start doing it otherwise there's nothing if they search they find nothing if they go on LinkedIn

**Brett StClair:** Is this Yeah.

**Ian Johnson:** they find nothing um so there's a timing thing there but that's not a

**George Westbrook:** Yes.

**Ian Johnson:** timing thing in the same sense of what we talked about with the um content workforce that's a very clear. We're not going to start this till January. This is just a okay, we'll pay you the outbound fee. I have no issue with that. You're doing work on the outbound fee to generate list and there's going to be more work to refine that. It's just when is the right time to start that and who do we start it off with that type of stuff. So once the list together, we can grab a session and have a look at it.

**Brett StClair:** Perfect.

**George Westbrook:** Right.

**Brett StClair:** Thank you.

**Ian Johnson:** Cheers folks. Have a good day.

**Michael Moores:** Cheers.

**George Westbrook:** Lovely.

**Michael Moores:** Thank you.

**George Westbrook:** Thanks very much. Have a good one.

**Michael Moores:** Take care.

**Brett StClair:** Thank you.

**Michael Moores:** Bye.

### **Transcription ended after 00:42:53**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*