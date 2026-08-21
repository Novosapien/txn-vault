---
date: 2026-08-20
type: standup
description: "Transcript and analysis of the 2026-08-20 TXN standup: Michael reviewed the workflow slate, six or seven targeted for the pilot, DT architecture moves to an IP question"
scope:
  - "[[full-agentic-experience]]"
  - "[[agent-access-layer]]"
  - "[[architecture]]"
status: extracted
extracted-to:
  - "[[approval-queue-integration]]"
  - "[[generative-ui-rendering]]"
  - "[[mcp-server]]"
  - "[[integrations]]"
  - "[[architecture]]"
  - "[[delivery]]"
  - "[[open-questions]]"
  - "[[index]]"
---

# TXN — Agentic AI Standup (2026-08-20)

> **Source:** Gemini transcript, synced from the shared folder (`shared/clients/txn/meetings/`). Attendees: Brett StClair, George Westbrook, Max Kingaby, Michael Moores. Ian Johnson declined. Duration 00:22:44.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| **The workflow slate has been reviewed and TXN is aligned.** Michael: *"I went through it last week. I'm fairly happy with what you've sent across... they're very much aligned to what we want to do."* He meets Ian straight after this call to agree **the priority order** and will send the list back. **The blocker recorded on 19 August is resolving** | [[open-questions]] #55, [[delivery]] | Register row updated |
| **Target set: six or seven workflows for the pilot.** Brett: *"we're kind of looking for about six or so to get through to completion for the pilot."* George's floor is a minimum of three, with three more if TXN wants them, and the additions do not have to come from the slate: any TXN user journey can be substituted | [[full-agentic-experience]], [[delivery]] | Update banner + register row |
| **The three net-new candidates are confirmed outside the pilot**, independently of Novosapien's parking decision. George: *"there's three at the bottom which are kind of net new, so that's technically not in the pilot"* | [[delivery]] | Supports the 19 Aug parking |
| **Michael will add approval expectations to each workflow**: where an approval is expected and where it is not, plus validation of the likely endpoints against what TXN actually expects. This is the grouping input owed since 13 August | [[approval-queue-integration]], [[open-questions]] #26 | Register row updated |
| **Approval stacking has a proposed solution.** The agent writes all the tool calls up front, renders them together and caches them, rather than serving one card at a time. If a single item is rejected it goes back and reworks. More finicky to build, better experience | [[approval-queue-integration]] | Update banner added |
| **Candidate 2, card service actions, has a platform change underneath it.** PINs previously had a **separate authentication endpoint**; under JWT that layer has been scrapped and it is now central JWT. The workflow shape is unaffected but the authenticate step disappears. Michael wants it fleshed out before it is built | [[open-questions]] #9, #31 | Register rows updated |
| **The TXN API is roughly 60% signed off.** Michael: *"pretty much I think we've 60% signed off of everything... it's more the transactional stuff from the latest stuff we haven't done yet."* Cardholder and card areas are solid | [[open-questions]] #32 | Register row updated |
| **The DT architecture question is no longer about cost.** It has moved to **IP and data access, at board level**: DT wants to retain its IP and its access, and TXN needs them to have none, because under GDPR *"we can't have people in South Africa looking at our data"*. Applies whether the platform runs on DT's tenant or TXN's | [[architecture]], [[integrations]], [[open-questions]] #48, #49 | Register rows updated |
| **Michael has paused UAT testing** to get ahead on user stories, which are being reworked while the build is already underway. His words: *"not what you want to be doing at this point"*, and it has caused some rework | [[delivery]], [[open-questions]] #51 | Register row updated |
| **Ian cannot access the build.** He is getting a **404 on the login page** and has never logged in. George picked it up on the call to fix immediately. Michael wants Ian and Dorte doing the **non-technical UAT**, look and feel, while he covers the technical side | [[open-questions]] #51 | Register row updated |
| **Stackworkz have the console foundation**: login, menus, screens and access. Michael's read is that this is a good moment for the two teams to talk, and that pulling it in should not be difficult | [[integrations]] | Update block added |
| **New deployment is out.** Approval cards look slightly different; transaction lists now render as a summary card that opens into the canvas rather than dumping rows into the chat | [[generative-ui-rendering]] | Update banner added |
| **Security position explained.** Nothing security-focused yet, deliberately. Sub-agents come later and will be hardened then. George's structural point: **the MCP tools sit outside the agent**, so the worst case is code that calls an MCP tool, which already carries its own limits | [[mcp-server]], [[open-questions]] #53 | Register row updated |
| **New term: AAT, agent acceptance testing**, run before user acceptance testing | [[delivery]] | Noted |
| **Decision point set for Tuesday 25 August**: continue adding workflows, or accept the pilot as it stands and start on the agent inbox and scheduled reporting | [[delivery]] | Noted |
| Content Workforce: interview 2 is tomorrow. Ian is complimentary about the process | [[content-workforce]] | Noted |

---

## Transcript

Aug 20, 2026

##  **TXN \- Agentic AI SU \- Transcript**

### **00:00:04**

**Brett StClair:** Yeah. Yo yo yo.

**Max Kingaby:** Yo.

**Brett StClair:** Sorry we've ignored you. Oh, you got him first time without being let in.

**Max Kingaby:** Huh?

**Brett StClair:** How did that happen? We try to keep Mike out. Hey, Mike.

**Michael Moores:** You

**Brett StClair:** Yeah. Not bad. Not bad.

**Michael Moores:** okay?

**Brett StClair:** He's got the

**Max Kingaby:** Mike's got the hacks.

**Brett StClair:** what?

**Max Kingaby:** The axe captain tell George is out

**Brett StClair:** Uh, see now George's on the pool.

**Max Kingaby:** tonight

**Brett StClair:** I'm just glad me and Brett have got the same shirt with the one that he's wearing.

**George Westbrook:** I'm just glad like me and Brett got the same shirt with the one that he's wearing. I've just got a different color. And the embarrassment I had on my face when I came in wearing that shirt and was like,"Oh my god, I've got the same f\*\*\*\*\*\* shirt as Brett."

**Brett StClair:** Does that make me cool?

**George Westbrook:** No, it makes me need need to completely just just burn the shirt.

### **00:01:09**

**Michael Moores:** What

**Brett StClair:** Well,

**Michael Moores:** the

**Brett StClair:** you can always go with horizontal stripes because as a fat man, I've watched too many f\*\*\*\*\*\* fashion movies that my wife puts in front of me that says,"Do not wear f\*\*\*\*\*\* horizontal stripes as a fat man." And yet my wife still buys me horizontal stripes, is a b\*\*\*\*.

**George Westbrook:** Maybe maybe she's just trying to ward off other other women from Brett,

**Brett StClair:** Maybe

**George Westbrook:** obviously.

**Brett StClair:** I can be the only reason why.

**Max Kingaby:** Like that lady that lady at the football that really fancied

**Brett StClair:** It's a problem I have.

**Max Kingaby:** you.

**Brett StClair:** She didn't fancy me. She was all over me because you f\*\*\*\*\*\* ignored her.

**George Westbrook:** to be fair. I think if your if if your wife wanted to keep people away from you, just let you speak.

**Brett StClair:** So glad I'm having to be polite because Mike's in front of me. Otherwise, I would take the closest thing that's heavy enough to cause some form of

**George Westbrook:** Very

**Brett StClair:** damage and throw it your way.

### **00:02:15**

**George Westbrook:** nice.

**Brett StClair:** Mike, has your week been as intense as ours? I'm assuming yours must be getting getting quite hectic at the

**Michael Moores:** Yeah, it's getting there. So yeah,

**Brett StClair:** moment.

**Michael Moores:** a lot of testing and uh still working for the user stories as well, which is obviously not what you want to be doing at this point, but um yeah.

**Brett StClair:** Or or it is

**Michael Moores:** Yeah, not when we're they're already building them is not a good idea. Um so yeah,

**Brett StClair:** Awesome.

**Michael Moores:** a little bit of rework there. So we have pause u testing just while we get ahead a little bit. So um you know, we're still trying to sign off that architecture. It's more costing about our tenant versus theirs. and it's not really a technical thing anymore. Um, but yeah,

**Brett StClair:** Yeah,

**Michael Moores:** it's not too bad. So, you're getting

**Brett StClair:** I mean they they surely don't have much um cloud architecture

**Michael Moores:** there.

**Brett StClair:** to worry about the cost of tenanting it and all that kind of stuff.

### **00:03:13**

**Michael Moores:** No, it's IP discussion at the moment and obviously we're reusing some of them and

**Brett StClair:** Uh

**Michael Moores:** access obviously GDPR. We can't have people in South Africa looking at our data. So they want to retain their IP and access while we need them not to have any access. It's just a bit of a discussion at the board level on what that entails. So all work itself out. But um yeah, basically they they want full control of it whether we're on their tenant or our own basically. So that's that's not really a cost conversation anymore.

**Brett StClair:** Okay, that makes sense.

**Michael Moores:** It's moved more to a IP sort of conversation. So yeah,

**Brett StClair:** That makes

**Michael Moores:** it's going well. Um finally working through some of the stuff and testing so it looks good.

**Brett StClair:** sense.

**Michael Moores:** Um obviously the source stat works last week uh this week sorry and they've got the foundation for the console. So basically what you've got login menu screens access so I think it'll be a nice time to chat to them when we do.

### **00:04:13**

**Michael Moores:** Um and obviously we can then look at how we can get that in. I think that shouldn't be too much difficult but um yeah it's going well.

**Brett StClair:** superb. That's great news. Um,

**Michael Moores:** and will be here shortly. I

**Brett StClair:** yeah, I just had a look.

**Michael Moores:** said

**Brett StClair:** I see his he's got a decline, but I do remember him saying he's keen to jump in and have a look a look

**Michael Moores:** I spoke to Ian this morning. He can't actually get in, so I think he might need a password reset.

**Brett StClair:** see.

**Michael Moores:** Um I don't think he's actually been in uh recently. So obviously I've looked from a technical point of view. Um, it' be good for Ian to pick up some of the the non-technical user type testing as well, look and feel and stuff I may have overlooked being a a technical user. So, um, he's just done that for the knowledge hub and obviously we want him to do it for this as well. So, yeah, he's he said he's getting a 404 when trying to hit the login page.

### **00:05:11**

**Michael Moores:** Um,

**Brett StClair:** Okay,

**George Westbrook:** Okay,

**Michael Moores:** yeah.

**George Westbrook:** that I'll I'll lally have a look at this like now so we get it get it sorted.

**Brett StClair:** that

**Michael Moores:** Yeah,

**George Westbrook:** And

**Michael Moores:** he said he's not he doesn't recall logging in at all yet. So, I don't know if it's on your side or whatever,

**George Westbrook:** hey,

**Michael Moores:** but my working fine as you said

**Brett StClair:** um so like we sent through a list of

**Michael Moores:** that

**George Westbrook:** quick.

**Brett StClair:** workflows for you guys to decide what you wanted to get done in the pilot.

**George Westbrook:** Is that

**Brett StClair:** I mean, at the moment, we're just crunching through them, but there's a fair amount. I don't know if you've had a chance to or you remember getting the the list just to kind of check through which ones we should be focusing on. And so, we've just been starting at the top, eh, George, and working our way down it.

**George Westbrook:** Can't wait.

**Brett StClair:** Yes.

**George Westbrook:** Yes. So, they're kind of like proposed ones that that we're Wait, do you want to mute yourself, Brett?

### **00:06:04**

**George Westbrook:** Um, yeah, they're just kind of proposed ones that we're thinking, oh, potentially we could do that. I think there's there's three at the bottom, which it's I suppose it's in terms of priorities, they're kind of net new. So that's it's technically not in the pilot, but it's one of those if we're happy with how it's functioning now. Um adding new workflows is is not as much of a lift as working on say agent inbox and stuff like that cuz for us it's tiny. It's it's it's like tiny changes in the way that components are rendered, the ordering. It's the real s\*\*\* finicky stuff. Um but we need to get right. But it's one of those once we get it right for for one, it's it's fixed for all of them. So the lift of adding new workflows is not as much. Um that's where with the new workflows, it's more using it, is it saying the right things, even calling the right tools, we can validate that. Um as long as we've got agreement on what tools should be executed when, um then it's just a matter of feeding that to the agents.

### **00:07:06**

**George Westbrook:** it test. Then we go in and do the the human UAT. Um yeah, there's the I coined the term AAT, agent acceptance testing and then the user acceptance testing. Um, I think it's that's where we kind of make the decision is do we do we create more workflows or do we start on net new features which are not in the pilot but I mean if we if we're there already there's no point us going oh no let's wait until the the two weeks is up to start working on XYZ.

**Michael Moores:** Yeah, I think I went through it uh last week. I'm fairly happy what you've sent across.

**George Westbrook:** Yeah.

**Michael Moores:** There's some good detail there. So, we have a meeting with Ian later after this. Then, run it through with them.

**George Westbrook:** Mhm.

**Michael Moores:** Um just just on the ordering more than anything then the most of them make sense. Um lots of good detail there.

**George Westbrook:** Yeah.

**Michael Moores:** So, I think they're very much aligned to what we want to do.

### **00:07:59**

**Michael Moores:** Um, so I just run it by ear and dirt and then we can go from there and say, you know, this is your order basically. Um, but yeah, got and put them into our vault and

**George Westbrook:** Just just trying to get the document up as now.

**Michael Moores:** stuff.

**George Westbrook:** It's a bloody artifact. Uh go I know it's a PDF. Um but yeah because obviously thanks very much for doing that feedback. That was that was really really helpful. Um I think most of most of that feedback should be should be sorted now. I think there was one around security. Um, I think in terms of exposing certain tools, blah blah blah, we we've not focused on anything security related yet. And there's some stuff that's kind of left over because we're going to be adding in sub agents in the future. So, when we get to that, we'll make sure that it's it's hardened. It's not I think it's at the moment it's it's all I think it's the the tools in order to one read skills.

### **00:08:59**

**George Westbrook:** um and get sub agents to start working. Sometimes it appears like certain things are exposed when they're not. Most of it's read only. Um the writing stuff will be writing either with sub aents you can execute them as tools or you can write code which executes the sub aents in parallel. Um, so it's rather than say you want 10 sub agents rather than to 10 sequential tool calls, you write the code to execute them all at once and then it brings the findings back. But we'll make sure that it's not going to be writing arbitrary code. It's not going to be because because the MCP tools are not within the actual agent, anything that's touching a service is outside. So, at worst, maybe somebody could write some code that's going to call an MCP tool um which is going to have the like the limitations on there anyway.

**Michael Moores:** Yeah, that's perfect. That sounds

**George Westbrook:** Um but yeah, the new new version should be deployed.

**Michael Moores:** good.

**George Westbrook:** It's not going to look any different um in terms of but there'll be may I think like maybe approval cards will look slightly different.

### **00:10:13**

**George Westbrook:** um some of the components like I think I was saying to a daughter the other day like there was one it was showing like transactions that when you're doing like um it was something to do with transactions and it was rendering like f\*\*\*\*\*\* 50 transactions in the chat which is horrible. Um so now it's going to be um it's going to render a card which is going to give a summary and then you can click into the canvas to look through the transactions click into them um so that the details there but it's not in the chat. Um, I think the only one where we've got to do a bit of thinking is around the I think it's

**Michael Moores:** Yeah.

**George Westbrook:** when suspending a card where you've got like five approvals one after another and it's five separate cards is just working out how can we obviously make that user experience a bit better. But then what we'd probably have to do is get the agent to write all the tool calls up front, go it to render it on the front end, and then kind of cache it.

### **00:11:11**

**George Westbrook:** But when if let's just say one was rejected. Um, yeah, one if one was rejected, then it needs to go back and do it. So this is a bit more finicky than just agent calls blah blah blah, but it's a better user experience. So we'll we'll work out a way to do it.

**Michael Moores:** That sound great. Yeah, perfect. Yeah, I think I'll have a look at them as well and see if we can add some stuff to you for the approval well and look at those. One thing I want to do with the the workflow is I have a look as well, see if we can expand on them, you know, where we expect approvals,

**George Westbrook:** Yeah.

**Michael Moores:** where we wouldn't. Um, so we'll take that and sort of add to that for you and say these are some considerations that we would want to make sure in there and start doing it that way basically.

**George Westbrook:** Yeah.

**Michael Moores:** So I'll do the same ones for the ones I've tested as well just so we're all aligned as well.

### **00:11:55**

**George Westbrook:** Okay.

**Michael Moores:** But um, it it looks good so

**George Westbrook:** and all the feedback that was that like the the actual way of doing it that was all good.

**Michael Moores:** far.

**George Westbrook:** Was there anything you're like why has he done this? Why why have this team created this way to do feedback in this way? Um it stuff like that can change as well. So if there's something that would make your life easier in doing the feedback just let us

**Michael Moores:** No,

**George Westbrook:** know.

**Michael Moores:** it's great. Yeah, there's no issues there. So, it worked really well. Thank

**George Westbrook:** Um yes,

**Michael Moores:** you.

**George Westbrook:** I think from I think from our answer it'll be those tiny iterations. Um once we're happy with them suppose we'll we'll decide either we'll we'll probably start working on some workflows in the meantime. Um and then maybe Tuesday we'll we'll make a decision. Do we carry on with the workflows or do we accept the pilot's good where it's at? Um obviously we we'll be working on it anyway.

### **00:12:50**

**George Westbrook:** Um, and do we start looking at some of the other other stuff like the agent inbox or the scheduled um scheduled reporting

**Michael Moores:** Yeah, that's perfect. Yeah,

**George Westbrook:** stuff?

**Michael Moores:** I'll raise and then we'll go from there. Obviously said to Ian and D that while I'm doing some of this user stories and UAT testing for they'll have to do sort of like the heavy lifting here.

**George Westbrook:** Yeah.

**Michael Moores:** Obviously, it's quite a simple non-technical thing to do. So, I'll I'll take Ian through it once he's got in and then hopefully some all three of us doing that

**George Westbrook:** Yeah.

**Michael Moores:** um and go from there basically. But um yeah, we'll start testing it out and then get back to those workflows as well um with some more detail.

**George Westbrook:** I think I think I think that's everything unless the content work for stuff. Brett, you said that went that went really well.

**Brett StClair:** Yeah, it Yeah.

**Max Kingaby:** So yeah, so we we've done it slightly differently where we've got so much information on TXN.

### **00:13:52**

**Max Kingaby:** They've already done some work on their own um entity northstar etc. We've kind of compiled all of that, started building out each of the manifesto entity and pillar documents, and then instead of more or less doing the interview from scratch, we're doing more of a refinement session with them. Um, and it's been working really well so far, I think. So, we've done interview one, and then interview two is tomorrow.

**George Westbrook:** And then we got the the outbound stuff as well.

**Michael Moores:** Great.

**George Westbrook:** I suppose that's more more relevant to to Ian, but I suppose that's going to that's going to save a lot of time as

**Michael Moores:** Yeah, I spoke to him before.

**George Westbrook:** well,

**Michael Moores:** He's very complimentary of that as well. So, it's going well. So, it all happened from our side.

**George Westbrook:** completely identify everything. Like we said, the next few years it would just be all of us sat back,

**Michael Moores:** Yeah,

**George Westbrook:** cocktails in hand, just like,"Yes, agent, do that. Yes, please, just do

### **00:14:48**

**Michael Moores:** well it works for

**George Westbrook:** that."

**Michael Moores:** us.

**Brett StClair:** So, George, I thought that's what you do already.

**George Westbrook:** If if I had a heavy object, that I had close to me. I would

**Max Kingaby:** Is there a joke there?

**Brett StClair:** I'm going to put Max down for What does Max get for that? Being funny. No, that's that's your only board that I can say publicly.

**Max Kingaby:** It's very important to say

**George Westbrook:** We got Mike's note taker on the call.

**Max Kingaby:** publicly.

**George Westbrook:** We got to be

**Brett StClair:** Be careful. Uh, what has George got that we can say publicly?

**George Westbrook:** careful.

**Brett StClair:** George's rabbit holes. Um, so do we want to quickly just shall we quickly whip through the workflows, George? Will that help? Uh, yeah.

**George Westbrook:** Yeah.

**Brett StClair:** Narrow things down. Did do you have that to hand?

**George Westbrook:** Yes, here's something I prepared

**Brett StClair:** Yes.

**George Westbrook:** earlier. Can't remember that this is the most up to date one.

### **00:15:54**

**George Westbrook:** Um, there might be ones that we've already done. So, there's the card holder offboarding. You You say zoom in. Ridiculous. You have you got your glasses? No, that wasn't a joke. Um yeah, card holder off boarding service actions. I think these are maybe some of the the lighter ones. Obviously not offboarding. That's not not one. Um decline investigation. VIP spend

**Michael Moores:** Yeah, I think some of them obviously we're trying to sort of prioritize these based on what we've got.

**George Westbrook:** exception.

**Michael Moores:** Obly you look at the is it number two there? So like you know the pin pin for example that's not really so there's quite a lot of changing certain things. So you know we're happy to proceed on the basis that we won't know those tool calls do I mean at the moment so there's quite a large change with pins before we had a separateation endpoint with JT we've

**George Westbrook:** Yes.

**Michael Moores:** we've scrapped the whole layer off and it's it's all central J so there's quite a large change there um let's say it's just a tool call I think the workflow is pretty solid it's just the fact that you won't have to authenticate before that in one so it's not massive in terms of the workflow but

### **00:17:14**

**George Westbrook:** Yeah.

**Michael Moores:** um you know we just want to make sure that one's fleshed out before we go and ahead and build that on this.

**George Westbrook:** Yeah.

**Michael Moores:** So certainly we should prioritize the ones that are solid, you know, everything up sort of card and stuff like that. Card holder, they're pretty solid now with my changes. Um, you know, pretty much I think we've 60% signed off of everything. So there's a lot there already. It's more the transactional stuff from the latest stuff we haven't done yet. So um, but yeah, I think this is great. And obviously I'm just sort of verifying those tool calls as well with the the likely endpoints that you've pulled. So I'll validate them and confirm that's exactly what we expect as well.

**George Westbrook:** Yeah.

**Michael Moores:** Um, and I can also feed feedback onto that for you as well with the so um yeah

**George Westbrook:** Yeah.

**Michael Moores:** I'll pick that I've got a rough idea of my suggestion to Ian I'll just run it through him first and then um I'll confirm the priority to you first and then get on with the confirmations of the end points and stuff as well as and when the priority at least um and then

### **00:18:17**

**George Westbrook:** Yeah.

**Brett StClair:** Yeah,

**Michael Moores:** I'll just go through and make sure we've got the approvals the end points and all that stuff in there and considered basically

**Brett StClair:** we're kind of looking for about six or so. Is that right? To get through to completion for the pilot.

**Michael Moores:** Hey,

**Brett StClair:** That should be able to So, if you can go like,

**George Westbrook:** Yeah.

**Brett StClair:** "f\*\*\* it. This is definitely not going to be ready cuz the way we're building the pilot is the only thing pilot about it is the stub. Everything else is pretty much real.

**Michael Moores:** there.

**George Westbrook:** Anything else?

**Brett StClair:** And so I I do think if you know it's 60% done, let's take the six or seven that we know we can bed down. Then it's all about just switching the API, removing the stub and linking it up.

**Michael Moores:** Yeah, sounds great. Yeah. Yeah, I think obviously we premier, you know, we'll get you to speak to stat works as well. I think be worth having a chat maybe with DT about authentication specifically.

### **00:19:12**

**Michael Moores:** Obviously, we'll have this conversation with the console as well is how do you get access to all those different endpoints? How are you going to find out which one you need to hit and stuff like that? Obviously, a lot of that stuff will come from the console anyway. So I think meeting with Star Wars first will help to identify how you pull that information down and obviously we've got a lot of information in the console already. You'll know sort of what program that that user has access to and stuff like that as well. Um so I think for the console side it's a lot easier to get that permissions and the stuff like that. Obviously for the uh we can build that in as well. So we'll just double check with DT they have a pretty solid GT process now that they're doing the SDK is confirmed they're going to build that. So we'll have all that in place so you can actually authenticate um those requests basically as well. So, um, it' be good to speak stat works on this one and just make sure align

### **00:20:03**

**George Westbrook:** it's yeah because I think the the two I think the the two ones at the end which are kind of net new

**Michael Moores:** basically

**George Westbrook:** is that alert investigate propose a plan which is more not quite agent inbox but no it is it is um so obviously we'd have to mock the alerts um and then We can test that there. Test are we going to represent it to the user. I don't think going into an agent and then asking for alerts. That's really not the point of an alert. Um building an interface for that. I suppose kind of going back to what Brett was saying about the the pilot is most things aren't about the pilot, but obviously in terms of u UI and APIs. So UI obviously stack work might want to change things. Well, I suppose it's pilot and obviously the API is kind of in that it's it's not actually calling them but given the the YAML it's exactly the same structure.

**Michael Moores:** Yeah. Yeah, that was

**George Westbrook:** Um and then yeah the scheduled the scheduled performance reports which I think will probably

### **00:21:02**

**Michael Moores:** perfect.

**George Westbrook:** be another interface as well because same thing you don't want to be going into an agent and asking for something like

**Michael Moores:** Yeah. No, definitely. Yeah, let me speak to Ian in a bit and then I'll we'll get back to the the top six or whatever we want to go ahead with. Is that six extra from the three you sent me before? Is it or three

**George Westbrook:** Um, if to be fair, I think we say a minimum of minimum of three.

**Michael Moores:** more

**George Westbrook:** Um, if there's an extra three that that you feel would be good to add, let us know. It doesn't have to be ones that are on on here as well. If there's certain user journeys that that you've been you've been working on that you'd want to prioritize, let us know. We'll get it planned out. We'll get it scoped and then we'll get it get it

**Michael Moores:** Perfect. Yeah, I will raise that with him.

**George Westbrook:** built.

**Michael Moores:** Make sure he's got a pretty good idea of what he wants to support. So, um, yeah, let me speak to him and we'll get that list back to you.

**George Westbrook:** I think that's I think that's everything. Eight eight minutes back for

**Michael Moores:** Perfect. No, that's great.

**George Westbrook:** everyone.

**Michael Moores:** Uh yeah, we'll get on with some testing as well and get some more feedback to you and uh catch you

**George Westbrook:** Lovely. Thank you very much.

**Michael Moores:** again.

**George Westbrook:** Have a have a good weekend and speak to you next. Well, yeah. speaks to speak to you when he speaks to you.

**Michael Moores:** Cheers. Take care.

**George Westbrook:** Have a good one. Bye-bye.

**Max Kingaby:** That's

**Brett StClair:** Chance.

### **Transcription ended after 00:22:44**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*