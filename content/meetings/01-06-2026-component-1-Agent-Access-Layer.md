---
date: 2026-06-01
type: component-session
scope:
  - "[[agent-access-layer]]"
status: extracted
extracted-to:
  - "[[agent-access-layer]]"
  - "[[co-pilot]]"
  - "[[a2a-endpoint]]"
---

# Component 1 — Agent Access Layer (deep-dive)

> **Type:** Component session
> **Parties:** Novosapien (Brett, George, Hasan, Max) · **TXN** (Ian Johnson — CEO, Mike Moores — CTO, Dorte Dye — COO)

Deep-dive on the foundational tool/permission layer: DT's Core API shape, the permission architecture, validation, the approval queue, audit, and the product webhook.

## Post-Call Analysis

| Finding | Destination | Action |
|---------|-------------|--------|
| DT Core API endpoints (card holder, groups, account, card, product ~200 fields, reporting); platform-mgmt vs day-to-day split | [[agent-access-layer]] | Decisions section added |
| Permission architecture — DT API keys (program level) + Stackworkz user permissions + new AI permission config; client = super-user | [[agent-access-layer]] | Decisions section added |
| Three-layer validation — agent → MCP server-side gating → Core API authoritative rejection | [[agent-access-layer]] | Decisions section added |
| Approval-as-permission, two-person rule, product/multi-card needs approval; agent routes to named approver | [[agent-access-layer]] | Decisions section added |
| Combined console + API + chat audit; "prompted trust" must be provable; retention TBD | [[agent-access-layer]] | Decisions section added |
| Product webhook (DT to add) so any change emits an event | [[agent-access-layer]], [[agent-inbox-alerts]] | Open question + dependency |
| Co-pilot scope debate — scoped to everything (guides user), page-state gates tools | [[co-pilot]] | Captured in §1/§2 |
| Prompted-trust confirmation applies even to full-agentic / agent-to-agent | [[a2a-endpoint]], [[full-agentic-experience]] | Captured |

---

## Transcript

	### 00:00:00

   
Dorte Dye: Good morning.  
Brett StClair: Hello.  
Dorte Dye: How are  
Brett StClair: And you?  
Dorte Dye: you?  
Brett StClair: Max. Hello, son. You both. Is it white t-shirt day today?  
Dorte Dye: Didn't you got the memo?  
Brett StClair: Did they even hear us as we take the piss out of them?  
Dorte Dye: Nothing has ended.  
Hasan Mohammed Ahmed: the I can hear you guys now.  
Max Kingaby: I'm on it.  
Brett StClair: We we were we were having a laugh at your white t-shirt day.  
Hasan Mohammed Ahmed: Yeah. I mean,  
Brett StClair: Thanks for the memo.  
Hasan Mohammed Ahmed: oh yeah, we all teachers I think actually except for Georgia.  
George Westbrook: Hey.  
Dorte Dye: Hi,  
George Westbrook: Oh, merge  
Brett StClair: Hello.  
Dorte Dye: George.  
George Westbrook: audio.  
Hasan Mohammed Ahmed: Over.  
Brett StClair: How's everybody? How's every weekend?  
Dorte Dye: Glorious.  
Brett StClair: Glorious. What we like to hear, right?  
Dorte Dye: That's a British summer as far as it gets.  
Hasan Mohammed Ahmed: Byebye.  
Dorte Dye: Did you manage to sort the access out for us to the platform?  
Brett StClair: Um,  
   
 

### 00:01:30

   
Dorte Dye: Right.  
Brett StClair: I'm going  
George Westbrook: We'll after after this call because we once we've done this we'll load in the the  
Brett StClair: to  
George Westbrook: component documents and then there'll be because at the moment it' just be one one document in there. So,  
Dorte Dye: Oh,  
George Westbrook: we thought we'll wait till after this call and then um upload this and then then we'll get  
Dorte Dye: okay. Perfect.  
George Westbrook: going.  
Dorte Dye: Did you not use uh Friday's meeting to add to the platform as  
George Westbrook: Yeah,  
Dorte Dye: well?  
George Westbrook: but it's still it just be adding to the adding to the vision document and then once  
Brett StClair: Yeah.  
Dorte Dye: Okay.  
George Westbrook: we got the vision document then we'll have all the little component documents sorted as well. Um, we've done some rejigging of the components as well. Um,  
Brett StClair: He  
George Westbrook: which which we can just go through at the start of this where we're where we're kind of seeing it seeing it land as well. Um, because I think the one that we think would be good to start with today is what the agent access layer for lack of a better term.  
   
 

### 00:02:33

   
George Westbrook: is just understanding the the APIs in which are crucial to the the platform that DT DT are building. Um and then we can start to wrap them into MCP servers. So then we can say right which ones are the co-pilots going to use on what page blah blah start right from the bottom and then and then work our way up if that works for everyone else. Um,  
Dorte Dye: Yep.  
George Westbrook: right this up my other monitor.  
Ian Johnson: Mhm.  
George Westbrook: Have we we definitely got this recording as well? That'd be we touch wood. We have every every one of these we've done has been recorded. But I'm living for the day when we do one and we're all sat there hyperfocused on this and then after just going s*** s*** because you can't really redo one of these  
Dorte Dye: It's okay.  
Brett StClair: It has happened has  
Dorte Dye: That's why you have a  
George Westbrook: sessions.  
Dorte Dye: backup.  
Brett StClair: happened and then we kind of repeat the meeting a bit just to make sure we capture everything.  
   
 

### 00:03:42

   
Brett StClair: Um okay so um how do we want to go about this? Shall we do it from the API calls?  
George Westbrook: Yeah.  
Dorte Dye: Click.  
George Westbrook: So I think if we think about what is DT exposing to us um what are the services that they're they're exposing what are the functions of those services so then we can start bucketing them into MCP servers. It's not to say that what we will do is well I think after today we'll realize are we going to have one big MCP server that's just going to sit across um everything or are we going to have them kind of like semantically bucket like this is for on boarding and it might touch these three different services or are we just going to do one service by service to make it easier. Um that that would be the aim of of what we get out of this tool and why obviously why why are we starting here? um we understand the data, we understand the functionality, then it's going to paint a better picture when it comes to say the full agentic experience or the co-pilot or the alerts and things like that.  
   
 

### 00:04:52

   
Ian Johnson: Okay.  
George Westbrook: So yeah, I think think to start with if we if we could go go through exactly that the what services are DT exposing. Um I think obviously said before it's going to be Kubernetes stack. Um so I'm assuming there's their microservices.  
Ian Johnson: Oh, hey  
George Westbrook: I think you might be on mute.  
Brett StClair: I've got the API documents.  
Ian Johnson: monkey.  
Michael Moores: So  
Brett StClair: ments also ready to go. We can pop up and we can go into a bit of detail on that. By the  
Michael Moores: um yes, we don't know sort of the services and stuff like that at the moment. We're just sort of working through that, but we can certainly go into the the end points that we've designed.  
Brett StClair: way,  
Michael Moores: Um there's still some of the sort of reporting ones that we we don't know the full extent of them yet, but there are the core um sort of platform ones that I'll I'll go through briefly. So the largest split really is um between sort of platform management and um sort of day-to-day.  
   
 

### 00:05:50

   
Michael Moores: So you have um let's start at the beginning. So you have a card holder endpoint. So all of these have sort of put post get you know delete where where applicable essentially card holders. So that's the the individual is going to uh hold an account or a card basically. So that'll have stuff like the name address on there. This is all sort of optional data that we capture based on the the services they're going to use. So very sort of free flowing um sort of card holder endpoint that's sort of that individual as a person. Um we have then uh a card holder groups endpoint. Um so basically this is a multi-use uh endpoint to allow us to group a you know bunch of card holders together. So either that's because they're part of a business or that's part of um you know like maybe a tier system or a  
George Westbrook: You're welcome.  
Michael Moores: reward system something where we want to group the card also together to do some sort of logical um you know suspension or change or something like that.  
   
 

### 00:06:45

   
Michael Moores: So that's sort of the driver behind those two and the sort of thing is there we'll obly link them together from a card holder to that card holder group ID. That's sort of the functional sort of stuff you'd do. So if a bank was on boarding a new card holder, that's the first thing they would do. And then the next sort of things are required. So an account would be the next one. Obviously is linked to a card holder. That is basically just sort of your standard sort of bank accounts. That's where the money will sit. Um whether that's on our system or not. There's some two different sort of setups of that which we'll come to shortly. But essentially this is a balance. This account has this much money in it. And it sort of drives the factor. Can you actually approve or decline that transaction? Basically um now a card holder owns or has access to an account but fundamentally the how the money is actually drawn out is based on the card level.  
   
 

### 00:07:37

   
Michael Moores: So card holder will own that account but the card is ultimately the one linked to an account. The reason for this is obviously you can then change the account if you want to. You know these sort of UK bank like Chase you can change that account on the fly. So kind one card six accounts. So it makes everything a lot easier in my in my wallet. Um so the sort of card endpoint is sort of quite a beef free thing. So when you create a card, it will create to a card holder, a card holder group and account essentially. So you've got those sort of mappings and that brings all those four endpoints together. Um so the card has a lot of detail on it. So you know it'll generate the the PAN number, the card number on the the card. All the security details for that card as well will be sort of generated in that flow. There's a variant of overrides that you can do. So if you don't want sort of contactless, if you want sort of online payments off, you can do all these changes on the car level.  
   
 

### 00:08:33

   
Michael Moores: However, they all pull from basically a core template. So which we're calling product. So essentially the card will also be linked to a product. You know, in simplest form, you could have sort of a personal, a business, a corporate card. Each with their own product, each would have a different look and feel. But there's a lot more in those products. to sort of 200 fields in there that control stuff from what it looks like when it expires all the way through to um can you transact on this, can you do that as well. So that's basically the core configuration point. It's probably worth noting at this point that sort of the ones I explained first are something you'd hit your mobile app with. So your banking app would be connecting to them. Your product is something you probably do once per country, once per year maybe. It's very in infrequent. That's why we're building the console. The AI around this piece is, you know, historically people have to integrate into that API.  
   
 

### 00:09:24

   
Michael Moores: Yes, it's there if you want to build something custom, but essentially we have a console. we're going to help push stuff into this. So, there's a lot of configuration there. How can we say, you know, this is what 90% of people do. You're probably going to want to follow this. And that's where I think a lot of the benefits can come because they don't understand what the configuration items are essentially. Um, so that's a sort of getting them onto the system. I don't know if there's any questions to start with there while I pause.  
George Westbrook: There was what what you were saying about the 90% of people do this. Could you just explain explain that one a bit more like in terms of like an an import? So, how would how would that be surfaced to a user or via via the via the API? cuz I'm thinking, okay, if that's uh a user set up a certain configuration, um let's say they've got a ridiculous limit, for example, for this certain type, I'm assuming then there'd be a way that we'd have a web hook set up somewhere which would get notified about that and then that's how we'd need to surf surface it to the user.  
   
 

### 00:10:33

   
George Westbrook: Um so how yeah, how are you tracking that?  
Michael Moores: Yeah. So I think um first of all we bucket the the clients. So you know we have a client at TXN they'll be sort of bucketed in some sort of central uh system. So they're sort of a little bit higher than this. So we have all of our clients, all of our uh bins and bin sponsors that are basically you know provide these services. So we have that in our central database. We will tag that client with a specific category is it you know lending, rewards, travel. Then from there what we can do obviously then compare every other client as well. So with this configuration we know have a data lake that has this information in. So we can actually see okay this this client A and client B have done these things the same done these separately. So obly you sort of building that pattern to say right this is what the the travel industry does. Um so that's at a product level.  
   
 

### 00:11:24

   
Michael Moores: There are some things I'll come on to later like spending controls. You know you block this merchant you allow this sort of spend. There's much more things you can build to get a painted picture of this story. But ultimately we will understand what they want to build as a business. You know all the mobile banking apps may change in the front end but ultimately from an issue of processing point of view you all do the same sort of thing with slight configuration or tweaks. So it's not like a whole shift of what you're doing differently. It's more you just you pull these individual levers to make a slightly different experience for your card holders. So what where we come from here is we'll take all that data and as part part of the onboarding of that client so we have onboarding in the consults and the first point here would be the product essentially. So you said you are travel um you know this is what we know about our people in the travel industry. would you like to apply these recommendations or do you have some sort of specific thing you would like to apply basically so sort of lessons learned if you will um so all that product stuff will sit in a data lake so um all the version in the history will sit in that in that data lake essentially um other things like card creation that sort of thing they will have web hooks for but the configurational pieces don't we just store the sort of version and stuff  
   
 

### 00:12:36

   
Michael Moores: like that reason for that is obviously web hooks are very important for keeping our client system updated of ours. Whereas a like a product thing is something they tend to just leave on ours. They don't have like a you know a store on their side. So whereas a holder may move on to something else into their system as well. So they'll keep all the record of card holder cards accounts and stuff like that whereas the configuration side will live in in TXN and obviously we will maintain those versions as well. A full data link for essentially the AI to access obviously there's an API as well per um client essentially. So they'll have their own instance of the TXN API. So you we would call the relevant ones on there. Obviously naturally the console will also load from those APIs as well. So if we talk about sort of screen presence and stuff like that then there'll be a lot of information on the screen at certain points that they sort of pull from there as well.  
   
 

### 00:13:29

   
Michael Moores: So I think that's where sort of co-pilot comes into it. rather than the having to pull from the API specifically, I think the larger portion would be sort of analytical data from the the larger set rather than pulling individual data because especially from the console side, a lot of that data will already be on the screen. So I think that's a of a mental shift say but console will be very much what's on the screen now how can we help from the  
George Westbrook: All  
Michael Moores: the co-pilot point and then to your point when we get the full agentic it'll be sort of pushing these changes  
George Westbrook: right.  
Michael Moores: in and saying you know as well. That's the sort of the overarching bit so  
George Westbrook: Yeah, because I suppose I suppose maybe what it's worth going into how how we're potentially seeing the the other components as  
Michael Moores: far.  
George Westbrook: well is so obviously we talked about I think Ian you mentioned like the different the different phases for lack of a better term um where there's one end is the full agentic experience which is you do everything for me I tell you and you do it and then say maybe like the the co-pilot at the other end and then the the kind of alerting alerting system in the middle and even the alerts I think there's two two approaches where one fits into more the agentic experience one fits into more the co-pilot so I suppose there's the  
   
 

### 00:14:43

   
George Westbrook: what I'm thinking is let's just say in the less agentic version the user changes a setting that setting obviously then gets updated Maybe there is a request to an AI agent that sits in the background which just kind of analyzes that maybe goes to the data lake queries for other travel companies and goes I know to you notice you've changed this setting to XYZ um when users have changed this setting this is what's happened all it is is just informationbased um and then for the say maybe a Gentic experience it is I've noticed this you're doing this wrong. Do you want me to change it back? Or I've noticed this when you update this setting. Other users have also updated this and seen these results. Do you actually want me to do it? So, I suppose it's just the the next evolution onto that. And I'm just thinking is in the APIs at the moment, we we might need to add in other functionality so that let's say that exact thing setting changed. when that setting changes sends a request to to maybe the AP an API that we might build um which then pulls in the users details pulls in similar users or similar companies and then does that analysis and then presents it to them as that kind let's call it the standard alert um but it's going to be the same mechanism for the agentic alert  
   
 

### 00:16:16

   
Ian Johnson: Mike, let let me ask you a question. Can can the client pull back via API what their product  
George Westbrook: Um,  
Ian Johnson: configuration settings are?  
Michael Moores: Yeah.  
Ian Johnson: They can. So ultimately it it's not it  
Michael Moores: Yeah.  
Ian Johnson: doesn't appear to be a new API setting. If I was if I was to talk about this in terms of if I was to go to the um to an AI agent or to my AI tool and ask the question of you know what's my configuration setting with TXN for I don't know transaction limits per day for and it have to be on a product wouldn't it make it then then the  
Michael Moores: Yep.  
Ian Johnson: API an API exists to pull back that information. Okay.  
Michael Moores: Yep.  
George Westbrook: Okay.  
Ian Johnson: So I'm I'm not  
George Westbrook: Hey  
Ian Johnson: sure in what you're talking about George given the fact that if somebody's changed something on the console so something has changed on the console then they the idea is that as I understand it Mike at least that within the console we will already through the co-pilot give them the information about what that change setting likely means.  
   
 

### 00:17:55

   
Ian Johnson: Um,  
Michael Moores: Yep.  
George Westbrook: But with that I with the co-pilot. I suppose that's it's you still user initiated. So like the user would the user would have to correct me if I'm wrong on any of this. The user would go in and have to start the conversation with the co-pilot and then they'd be having a chat to maybe achieve something that they want on the screen. But if they were just using like a normal SAS platform and they went click click change this, the co-pilot isn't automatically going to well a typical co-pilot isn't maybe going to pop up and say this is what's this is what's and blah blah blah. So then it would need to be some sort of kind of alerting system which maybe users can turn on, turn off certain  
Ian Johnson: So, so let let's follow that logically then. So,  
George Westbrook: things.  
Ian Johnson: let's say because the console is optional, right, Mike? I mean, they don't have to use it. There are certain things that um there are certain functions that somebody can't do if they were to build their own wraparound support configuration and support layer as a client which some people have.  
   
 

### 00:19:04

   
Ian Johnson: I mean that's what they were largely forced to do at Marqueta because the console wasn't very good. um then yes they wouldn't they if they make a change  
George Westbrook: Let's  
Ian Johnson: in their own user interface that calls the API and we make the change at the moment the co-pilot is redundant  
George Westbrook: see. Let's see.  
Ian Johnson: which I think is your point.  
George Westbrook: But  
Ian Johnson: So we're not going to say anything about what that change means.  
George Westbrook: yeah,  
Ian Johnson: we're just going to make the change because that's what was asked by the API. If what you're talking about is then doing the same thing that we would do in the co-pilot of I of explaining what the impact of that change is um then I understand that part more but surely that's the same information source as to what the change impact is we're just talking about delivering it to the client in a different  
George Westbrook: just when we when we say co-pilot I think maybe what we need to align on is  
Ian Johnson: way.  
George Westbrook: what what we what we all mean cuz I don't I'm not sure if when I say co-pilot I mean the same thing as you because I co-pilot for me I'm just thinking down that right hand side of the screen the user has to go in they have to ask um  
   
 

### 00:20:36

   
George Westbrook: you could say that the those kind of alerts things are kind of co-piloty but I think if we bucket that out into something else where it's like user takes action not with AI gets alerted um with some sort of AI analysis. I've put that into a a diff a different kind of um component. Um cuz I think obviously I remember when we were going through the um the designs that Super Ultra did, they did have those those popup alerts.  
Ian Johnson: They do. My my my point is that the AI that is that is driving  
George Westbrook: Um  
Ian Johnson: the content of those alerts,  
George Westbrook: Mhm.  
Ian Johnson: the change that's made, however that change is made, whether it's done on a c on a client's own platform calling the API or it's the console calling the API, the fact is the information about what that means is the same. It's not going to change. It's just the source of how they made that change. and we don't have the opportunity in the client system to show the co-pilot in the same way we do in the console.  
   
 

### 00:21:41

   
Ian Johnson: And I think if I'm trying to understand what you're trying to say is how do how do we surface that information if somebody is doing something in their own client tool? So not in the client tool but in through through some AI capability outside of the console.  
George Westbrook: But no, I I did mean in the console because that's why obviously if it's if it's their own if it's their own wrapper around it obviously we we we might not I suppose there is the potential that we could surface this information to them but then it's kind of re exactly re rebuilding this console. kind of meant in in the TXN console the the showing of those alerts. It was only scoped to the the TXN  
Ian Johnson: Okay.  
George Westbrook: console.  
Ian Johnson: My understanding that of that Mike is that it's analyzing information in the data in the data lake through the AI capability in the console. O through the co-pilot to to surface that information of what we think the impact of that changes or what whatever other information we envisage sharing depending on the part console they're on.  
   
 

### 00:22:53

   
Michael Moores: Yes, that was  
Ian Johnson: So I I don't know I don't know if I understand what the question is because you we  
Michael Moores: it.  
Ian Johnson: start this conversation about APIs. There isn't API that's going to surface that  
George Westbrook: Yeah,  
Ian Johnson: information  
George Westbrook: it we'd need to be able to when the user changes that we'd need a way that when that API request happens in order to update the configuration we'd need to be able to ping a request to let's say our agent API. Um so I'm just yeah it's just trying to work out what what sort of mechanisms we'd need for certain things. I suppose the the alerts one it might be adding in an extra request within that request. So they they ping the update card endpoint um update configuration endpoint and then within that we might need a little ping to our web hook at the end which would be user has updated um this card go do the go do the analysis  
Ian Johnson: Excuse  
George Westbrook: and then we can then surface that in the I suppose we need to think about the mechanism for doing that within  
   
 

### 00:23:53

   
Brett StClair: Oh,  
George Westbrook: the within the console as well.  
Ian Johnson: me.  
George Westbrook: Um so I suppose yeah it's request happens ping to us we do the analysis and then we send it back to we send it back to the console and surface that to the user and it'd be the same mechanism if it was the the full agentic let me take this action blah blah blah um as it would be in just let's call the the standard alert um okay so yeah that's that's making a bit more sense then so the the end points that you mentioned. So there's the there's the account, the cards, the the card holder grouping. Um, which I suppose is all all part of the on boarding. Um, and you said that that you haven't decided if they're going to be all in the same service or if they're going to be in different services. It's just in terms of functionality, you kind of know the end points, not just necessarily what service they're going to they're going to live in.  
Michael Moores: Yeah. So ultimately I think there's a few decisions on DT about what they're doing.  
   
 

### 00:25:09

   
Michael Moores: The only difference we've designed so far in terms of segregating it is permission wise. So obviously cards card holder they're sort of I want one card I want to terminate one card. Whereas products and some of the stuff we'll talk about later is more you're affecting the whole program or a big portion of  
George Westbrook: Yep.  
Michael Moores: products. So we we have a permission schedule that says you can access all this configuration or you can't. So at minimum we would need that but obviously if your thing is sort of we'll bundle you know maybe spending limits together versus cards and stuff like that then I think we can get granular more granular I think we  
George Westbrook: Mhm.  
Michael Moores: at least need to split out from the sort of the operational day-to-day create a card that's mobile banking app may use or you know an AI to do that versus I'm configuring this country or these individual you know specific cards as  
George Westbrook: So I'm thinking potentially it instead of having I say anyone Brett has weigh in on this. I'm just thinking instead of having individual cuz I I can imagine the the different permutations of the configurations could could be quite quite vast.  
   
 

### 00:26:19

   
George Westbrook: So by having them like semantically grouped into different MCP servers can be a nightmare because it might be on let's just sake of argument four MCP servers um given a certain configuration it might need a bit of one a bit of two a bit of three a bit of four. we just have one big monolith API server uh MCP server um and then we have a state file for each user based on the information we know at that point in time. So let's say this user they can only issue cards in this certain area blah blah blah. So every turn we kind of set the tools that are accessible to that user at that point in time based on both their the things that aren't going to change. So maybe they can only issue cards in three these three countries but then also given the stage they're through or the page that they are on. So what do I mean by that? If it's on boarding you can't do step six before you've done step one. So there might be tools associated with step six that can only be used at step six and if all the things before have been done.  
   
 

### 00:27:30

   
George Westbrook: So what we can do is every every request turn we update the kind of the on boarding and then we only expose those certain tools and I think that would be best just having that in one big monolith and in in the same way in the co-pilot um if a user is on a certain page they can only access the tools for that page and then let's call them the holistic tools Um  
Brett StClair: But will the page just call that particular set of features?  
George Westbrook: because  
Brett StClair: So the page gives us the state that they're in in this case.  
George Westbrook: Yeah. Yeah.  
Brett StClair: So we don't have to do the same kind of like this is where we think we are memory store styled.  
George Westbrook: Sorry.  
Brett StClair: Actually in the co-pilot we know all these different things. It's far more static. So it's that smaller call rather than a broader reach and trying to manage  
George Westbrook: But I suppose then there's I suppose we've got a kind of like a design decision for the experience which is with  
   
 

### 00:28:26

   
Brett StClair: that  
George Westbrook: the the co-pilot. Do we want the user to only be able to do things that are on that page or ask questions about things on that page or we or do we want them to have access to everything? In my head, I'm thinking it's a bit in between. Maybe it's like general information they might be able to access, but if they wanted to get certain information, it can only be about that page. Or we can just do on any page you can do, you can ask about whatever you want with the co-pilot.  
Michael Moores: Yeah, I think on the the copilot we sort of scoped to everything. Obviously, you don't need to be on the individual page. So, try and help a a direct them. You know, they don't need to know where to click to get to that information.  
George Westbrook: Okay.  
Michael Moores: So you they could be on products but ask the question about cards and stuff like that and obviously have that experience guide them to the right place show them the right information that so I think the only consideration there would be probably worth touching on our permission model when we come to outside the console so the we have the  
   
 

### 00:29:31

   
George Westbrook: Yeah. All  
Michael Moores: API uh permissions so that's API keys that is a system to system API key that they get access to if they hit the MCP or AI outside of the console we would need to mimic that structure. So they can only get access to APIs that they h they would do already.  
George Westbrook: right.  
Michael Moores: So in that one we have sort of read write as I mentioned program manager which is sort of your products and all your configuration endpoints and then you have the standard ones. So that's the sort of split that we have. Obviously in the console we have that whole thing goes down a whole another level. So not only can you access the card endpoint you can either suspend terminate all of these actions are triggered behind very specific permissions. So that user will have okay that user can suspend but I need a team lead to terminate for example. So we've done that based on who they are what they're trying to do and is it temporary or a permanent so terminating a card is absolutely a permanent solution.  
   
 

### 00:30:26

   
George Westbrook: Yeah.  
Michael Moores: So we've tried to make this permission schedule as flexible as possible and I've got documents on it as well that we've put forward for design but essentially every permutation of a client and their access. How can we do that? So not only getting into the page but what they can do on that page and obviously the console will hide the buttons and stuff like that but we need to make sure the the co-pilot or the the agent jo whatever it may be respects these permissions that an individual user has or that whole client has as well. So we just need to be sure that we have that both APIs are available to access as well. So I see  
George Westbrook: I suppose in a in a situation the agent makes an action that the user  
Michael Moores: you.  
George Westbrook: is not permitted to do. I'm assuming the API, the DT API is just going to reject it. It's not going to go through and make the action. Um like so is it because I'm trying to think is are we going to have to have that validation baked into the tools or cuz so let me so the agent might make the action.  
   
 

### 00:31:33

   
George Westbrook: Um, it might, let's just say it's the context isn't good enough and it takes that action, executes it. The user shouldn't have made that action, but it passes it through to the API. Is the API going to reject it? Pass back the error  
Michael Moores: Um yes that will depend on how we structure it.  
George Westbrook: message.  
Michael Moores: So right now the console for example will get an API key that has access to everything. So the console will manage the permission of the user. Now if we that's fine in the console but you know if we look at outside not using the console you know you may you know if we go with a standard design we'll give you an API key that accesses all clients and everything. So sense no but you know could we say I guess it depends how we set this um MCP or  
George Westbrook: Yeah.  
Michael Moores: agent trading or it could be that they request a specific AI key that you then use for  
George Westbrook: Yeah.  
Michael Moores: program in that case then yeah we just don't know a how you want to do it how you feel better the endpoint for keys is there we can support multiple keys so we can provide that sort of level  
   
 

### 00:32:31

   
George Westbrook: Yeah.  
Michael Moores: of thing at a client level so we've built all you know already and that's something  
Brett StClair: Okay.  
Michael Moores: that our clients don't have access to but we could make sure AI did for example  
George Westbrook: Yeah. Yeah. Yeah, cuz I think in an ideal world it would be say ser server validated rather than client client validated because like let's just say the 99.99% of the time it's going to get it right. But it's that one that obviously we've we've got to be careful with. Um and if it's server validated, let's just say that one in a th00and passes through, hits the server, bounces back, we get the error message. That error message is then surfaced to the agent which can then be like, "Oh, okay. I forgot about the three countries that this um this account can access. Let me make sure that I add this into the payload and let me retry." The only time where it could be a bit difficult is if we're relying purely on um agent context and no server validation.  
   
 

### 00:33:38

   
George Westbrook: But I suppose one thing we one thing we could do if it's client validated is every single user or account has their own API key which has those permissions pre-baked in. So at runtime maybe what we'd need is the API key and then a the users configuration passed in at runtime which changes the how the MCP servers execute the tools and then we can surface the error back to the agent. So yeah so maybe three layers. So there's the agent the agent the MCP server the server ideal world server does the validation um and then we can just have the any API key um worst case it can be the client has the the user or the account has the API key which has a certain set of configuration that goes along with it that's passed along hits our MCP server we do that server side validation um if it's an error, we bounce it back. Agent retries again. If it's correct, then it gets passed through to the server.  
Ian Johnson: Hold on, hold on, hold on. I must I might miss misund lack of technical knowledge,  
   
 

### 00:34:51

   
George Westbrook: Um  
Ian Johnson: but all of these permissions are held somewhere, Mike. Right. So, can they be can you call an API to understand the permissions of a  
Brett StClair: Awesome.  
Ian Johnson: user? Yeah. So, I don't understand why the first thing that an agent does isn't call the API to check the permissions of that  
Michael Moores: Yes.  
George Westbrook: It's it it's because if we take the the one in a thousand one in a  
Ian Johnson: user.  
George Westbrook: thousand calls it might make a mistake. Um we want to make sure that that even in that one in a thousand that action does not happen. Um, and if the server validates the request and checks the permissions, which I it let's let's just say it does. Let's just say it passes the three levels of validation and then gets to the server, that request is going to fail. It's not going to execute and then it's going to pass back up the layers to the agent. the agent's going to see the error and can autocorrect and be like, "Okay, this I didn't put this argument in or I put this was this was the wrong thing. This user hasn't got this permission." And then it fixes the fixes the tool core makes makes the correct one.  
   
 

### 00:36:14

   
Michael Moores: Yeah,  
George Westbrook: Um,  
Michael Moores: I think the only for me the consideration would be the au like you all errors formatted that's all handled absolutely fully by the API. So you just wrong it's not going to let it happen.  
George Westbrook: Perfect.  
Michael Moores: The only concern the authentication side we need to think about. So you know how do you want to scope this AI?  
George Westbrook: Yeah.  
Michael Moores: I I think it's going to be individual user level at that point. There is no sort of API essentially the so user permissions is built by the console. So that's granular one.  
George Westbrook: Yes.  
Michael Moores: So all they do is say okay with these permissions they are built like you say building the client side validation basically. So we have a back API for that permission level and they're then going to transpose that into API calls they're allowed to do. So they're doing that work already. There is nothing on that side that will sort of say you can or cannot do that at that point.  
   
 

### 00:37:06

   
Michael Moores: They obviously will have full access to the API. They're sort of managing that layer basically. Um so that's difficult there because I think we're going to want it granular on an individual user.  
George Westbrook: Yeah.  
Michael Moores: So you think about using your own sort of claw code or indivi you know individual person I think it's going to be that rather than the program level we just need to think about how we make sure that individual the same permissions as they would on the console essentially  
George Westbrook: Yeah.  
Michael Moores: Okay.  
George Westbrook: So I suppose it it all it would really need to be is just a thing a singular API key which is universal and then we pass in the user ID and then in the payload to the agent it's going to contain the permissions and then we rather than it being agent based the agent decides if a user can do this it's just we'll call it functional based for lack of a better term is we rejig the MCP server so that a user can do this and can do that but it can't okay yeah I think that I think that might be might be best  
   
 

### 00:38:02

   
Michael Moores: do is um I'll send you the document of what we've done right now. We haven't actually sent to Statworks team.  
George Westbrook: Um,  
Michael Moores: This is they've not seen it yet. So there is time to change certain things if we need to. But basically it's a very specific roles user base type thing with very flexible permissions. So when we release a new feature, we go this feature has this permission. Then you assign the permission to a user. So we do need something to say validate or whatever it may be. It may be that you go okay, I want to do this action and it goes yes or no, whatever it may be from that side. But essentially I'll send the document across afterwards so you can actually see what we're proposing from a API standpoint and why we've got these sort of different levels because you know for for a client that we're talking about now, it's very flexible. They can have whatever role they want. whatever permission they want for TXN bin sponsors we're having it you have this role this is all you're getting  
   
 

### 00:38:54

   
George Westbrook: Yeah.  
Michael Moores: so that's the sort of we have a very governance side for TXM whereas when it's our client they can set their own governance basically own roles like that so I'll send that across but I think yeah that's the only thing we need to consider the API for formatting and countries and all that is all fully configured you're not allowed to do anything that would break the system so that should be fully covered by the API um you'll get fully formatted errors back. Um, at least you can do something with or you know  
George Westbrook: Yeah. M yeah. So I suppose there's there's there's two and correct me if I'm wrong here.  
Michael Moores: prompt.  
George Westbrook: There's two levels of permissions. I suppose there's the the business level permissions or does every business have the same permissions or because I suppose business and user user  
Michael Moores: Uh, yeah.  
George Westbrook: permissions.  
Michael Moores: So essentially the only way we would sort of separate I say read write program manager is essentially the three we've got. So read we will always give out read and write.  
   
 

### 00:39:52

   
Michael Moores: Now if a client wants to separate read and write that's that's up to them. We can do that essentially they'll always get read and write as a core position. Um there are some sort of contractual things where we wouldn't give out configuration that will be owned by someone else. So that's the only one we would either or either not give out based on um the discussion.  
George Westbrook: Did you say did you say contractual permissions? So I don't know if I heard that.  
Michael Moores: Yeah, essentially based on the the mockup. So it depends who if it's a whole governance sort of client that can do everything, we'll give it all out. There are some where one party takes the day-to-day operations, the other one takes aation and more program management. We would then split that up into two different parties essentially based on the mockup of that client.  
George Westbrook: Okay. Yeah, that makes sense. So yeah there's definitely so as the as there's the first turn to the agent we got to pass in right this business they've got these permissions and then another level down this is the so it's this is the business this is the user given that there's different permissions that both of them can have and then we need to rejig the MCP server so we turn some off turn some off then there's the more thinking about in terms of like an on boarding perspective.  
   
 

### 00:41:07

   
George Westbrook: Then there's the the current how far they are through a process. Um  
Michael Moores: Yeah, that's a good  
George Westbrook: yeah.  
Ian Johnson: Why do we care about the business though?  
Michael Moores: point.  
Ian Johnson: Why do we care about the business? What the business can do? Surely the what the music can do is a sub a sub can't get the word out, but you know what I mean. It's a um it's part of the overall business um permissions. So why would you check the business? Why you not just check the user able to do  
George Westbrook: So making the assumption if you there's certain things business A and business B can do and they might not be the same. Is that is that correct? Yeah. And then obviously within business business A um the users might be able to  
Michael Moores: Yeah.  
George Westbrook: do certain things as well. And I suppose yeah, you're kind of kind of right. It's going to be implicit there from what the user can do.  
   
 

### 00:42:14

   
Ian Johnson: Yeah, it just sounds like a step that's not necessary because the that trickle down of what their permissions are, Mike, they can't have more than the business has got. Um, and we don't really care what the business has got because we're we're dealing on with individual users, right?  
Michael Moores: Yeah.  
George Westbrook: No, because alerts so with let's just take alerts for example the alerts I suppose are going to be business level. Um, no. I think I'm I'm 7030 uh 8020. Sorry.  
Ian Johnson: We don't we don't need to make a there's no decision needed to be made. I think for me um the important  
George Westbrook: Yeah.  
Ian Johnson: part is if you if you're if you don't have permission to do something that you've asked AI to do the sooner that we advise that they don't have the permission to do that the better and and ultimately the wherever the permissions are held Mike and they and they don't need to be as granular for the  
Brett StClair: Correct.  
George Westbrook: Yes.  
Ian Johnson: AI as to do as the console because as you say the console is about you know what's being displayed and all those kind of different things but if there's a you know every single user has got a set of permissions doesn't matter how they arrived at it because this business is this and then they at the end of the day every single user has got them um I suppose the only thing the only question and I'm not necessarily clear about  
   
 

### 00:43:56

   
Ian Johnson: this Mike is if a client just considers themselves to be a single user and they're using AI to to basically call and and ask for things to happen doesn't necessarily mean that there's a user any more than a single user in our permissions database, you might just not have anything if they if they don't use the console as an example. Um, then that's the one thing that we'd need to consider that goes against the business and user  
Michael Moores: Yep.  
Ian Johnson: thing, which is if a client goes, well, I'm not going to use the console or any of that stuff, I'm going to build it all on my side and as far as I'm concerned, if I ask you to do something, then you should honor it because I'm going to allow I'm going to use AI to basically make all of the changes or pull all the information I want and there's just there isn't in that context there's not more than one user because there's no human users necessarily involved there's humans involved somewhere to some degree but not between them using their own AI and saying for example change the transaction limit um on my on card product whatever to this there's no  
   
 

### 00:45:28

   
George Westbrook: So I suppose it's it it's just uh It's just a a user for lack of a better term with the full permissions of the business.  
Ian Johnson: Yeah, the bit I don't know like is how that's actually and it comes back to whether it's business or  
George Westbrook: Yeah.  
Ian Johnson: user. I don't know how that exists in our platform because from a permissions perspective, it's really been designed around the console primarily, right?  
Michael Moores: Yeah, I think if you look at it like I think AI the same split. So maybe the answer isn't one or the other. So obviously API is system to system and then the user is a console. So I think the the three things we need to consider is if a user is using co-pilot they can't bypass their console permissions is is the main one. The second one is to your point I is like what about if I want my whole business to work with your agent agent to agent and I guess the third one would be potentially me as an individual user using claude a client may want to restrict to a user level.  
   
 

### 00:46:28

   
Michael Moores: I think that's the one we haven't really discussed in to date that gives a more granularity. I think you could probably get away with the the system like API does, but you know what about if there's three people using it from a company each one to do different things? That's that's consideration I take from my  
George Westbrook: Is  
Ian Johnson: But surely that's not for us to manage it at that at that point unless we're talking about  
Michael Moores: side.  
George Westbrook: it  
Ian Johnson: create a user and set these permissions being something that someone was able to do via AI, which I don't know that that's necessarily what we're talking about, but if they've got three users in their business, business. It's surely if they got three reasons in the business, they would for us to be involved, they would have had to set some user permissions on our platform. Um, and then at that point,  
Michael Moores: There.  
Ian Johnson: it doesn't really matter. It's a user ID that does it. The point coming back the point I'm trying to make George and again just in in layman's terms for me was the whole conversation about business and user.  
   
 

### 00:47:41

   
Ian Johnson: So if there are users then that it makes logical sense but  
George Westbrook: Mhm.  
Ian Johnson: if client doesn't want to set anybody up as individual users is that or is that client treated as a user? So the client the client always as an entity is always considered a user and then they can have other users that have got different permissions but the client user is always always has to be a client user and that client user is everything that people can do.  
George Westbrook: Mhm.  
Ian Johnson: It's not separate. You don't set up as a business. It has the same effect I think George from what you were driving at. Um but then from our point of view, Mike, we need to make sure that that was something that we can actually manage. Um because it's like a super it's like a super user,  
George Westbrook: I suppose.  
Ian Johnson: right? It's a super user has you can do everything and if you don't want anybody underneath sub  
George Westbrook: Yeah.  
Ian Johnson: users that have got different permissions, that's what you get.  
   
 

### 00:48:44

   
Ian Johnson: So we will do absolutely we'll do whatever you ask us to do within the permissions that are set as you as a super userclient. But then it's we're only ever looking at a user ID. That user ID could relate to a company. Um or it can relate to to still relate to an individual. The fact that the individual is using that user ID in an agent doesn't matter either, does it? Because the permissions are all the things driving that  
George Westbrook: Because how I'm thinking about is if I'm and I'm I'm assuming there's obviously a let's say an organization table and and then a users table which is linked to that organization. So in the payload that's passed to the MCP server there'd be the user ID and the organization ID. So all we would do is be like if um user ID and organization ID query the permissions from the user ID and then that will give us the permissions and then it'll be if only the organization one um then we query the business ones. So it's the same process where it's like each one will have like a call it MCP settings configuration.  
   
 

### 00:49:54

   
George Westbrook: Um if there's both we do it by the user. If there's just the organization then we set the permissions from the organization. Um, and  
Ian Johnson: There's Just so Mike does the ability to pull back permissions at an organizational level exist level  
George Westbrook: then  
Michael Moores: No, that's something we build specifically for the AI.  
Ian Johnson: exist  
Michael Moores: So, it's not we don't need for the API, but you would have to have some sort of permissions for the AI at an organizational level.  
Ian Johnson: which is which is the point I was driving at from our perspective that introduces something new that doesn't exist today yet. My point is that what's the difference? So you have an organization ID. So what these are all the permissions you can have. Okay. The first user that that gets set up has all of those permissions because ultimately as far as we're concerned that is the business. It's then for the business to decide I want another 10 users and they get a different um set of those permissions that are available to them and then in that way all we're interested in is the user ID.  
   
 

### 00:51:10

   
George Westbrook: See who?  
Ian Johnson: So almost to the point where Mike the first user I suppose we'd have to set in that respect every client would have a user set up that had every permission available that we're happy to make available to them. Um that would be the first user and if it stopped at that was what you would check. So it wouldn't be an organization idea or  
George Westbrook: But I thought, and correct me if I'm wrong here, that you could have two different organizations and those organizations could have  
Ian Johnson: anything.  
George Westbrook: different access levels or is it every single business that that joins the platform um has access to all of the permissions of TXN and it's only on a user is a level that it's fine grained  
Ian Johnson: But we we'll have already set the the user permissions at for that  
George Westbrook: or  
Ian Johnson: client. So let's say that the say say the first user is the client. Those permissions, Mike, as I understand it, are set during the on boarding  
George Westbrook: Mhm.  
Michael Moores: Yeah, they they're not sat in the same place.  
   
 

### 00:52:17

   
Michael Moores: So,  
Ian Johnson: process.  
Michael Moores: it's probably worth protection on the architecture. So, you've got all the way under the DT side, you've got API keys that all that does is controls the access to the API for this individual program that we spin up. So, we have a client, they can have multiple programs. So the API keys at the program level. So you have access to the API for this program, this URL. We have a central system that DT is going to build. That's where clients live. That's where programs live essentially. So that's just a store of what they are. There's no permissions there at all. Then you come all the way over to what Statworks is building is the console and the console back end. That's where the user permissions sit. So it's not like one big system. They're referencing the central system DT build for organizational levels. There's no sort of organizational settings outside of the the API keys, if you will. So, it's going to be something.  
   
 

### 00:53:06

   
George Westbrook: Okay.  
Michael Moores: It's going to be a third configuration for us to say this is your AI configuration if you want to do the organizational level essentially to say this is what it is. Um, I think Super did design a screen for it. We haven't dug into it too much, but essentially how do we access the how does the AI access these systems basically  
George Westbrook: Okay.  
Ian Johnson: what are you an agent to do?  
George Westbrook: So it's so there's there's there's client program and users and do you set the permissions for a user at a  
Ian Johnson: Essentially,  
George Westbrook: program level? So be like in this program this user can do XYZ or is it this user within this client across all programs can do these  
Michael Moores: Um, yes. So, permissions are separated.  
George Westbrook: actions.  
Michael Moores: So, a user has a permission set. They can do that. They're then assigned to specific programs. So if I assign to four programs, you'll get the same access across those four programs. It's more a role based this is what this person can do rather than we decided not to go individual  
   
 

### 00:54:02

   
George Westbrook: Okay.  
Michael Moores: program permissions at this time. But that user has access to four programs with these set permissions basically. So that's how that hangs together basically.  
George Westbrook: Okay. So then, yeah. So then we've got the the user and then there's probably going to be some program level ones as well which we might need to factor in. So like given a program Well, I suppose that's not really it's not permissions. It's just kind of that's just the state of this program. Um,  
Michael Moores: Yeah. Yeah. I think from right now we're not using any permissions at the program level internally outside of the the  
George Westbrook: okay.  
Michael Moores: API and that looking at it from an AI lens we're going to have to. So either we need to tweak the internal DT structure for to add those permissions on or some sort of settings or we have AI specific settings which are obviously on your side and say okay you can configure this we set up a access to the MCP via the console for example we tick a few options that's the permission that has it stands there's no place for individual permissions to go outside the user and the the API keys if you will sort of permissions on the access method rather than the the program client  
   
 

### 00:55:24

   
George Westbrook: Okay. And then I with the with the console I think that's very easily  
Michael Moores: hierarchy.  
George Westbrook: controllable. Um it's just the like if we take the the clawed like they're linking the MCP server to their to their clawed account. That's where we need to think how we how we do that  
Ian Johnson: But there's two there's two different things there.  
George Westbrook: and  
Ian Johnson: There's the permissions to do something and there's whether or not it's relevant to do that thing on that program. Let me give you an example, Mike, if I understand it. you have permission to I don't know configure a configure a product or make product changes whatever I'm talking very high level and you might have two programs one of them which a consumer debit program one that's an expense management program I as a user can do these things on either to have the permission to add a card holder remove the card holder, put the program on, suspend the program, change whatever it might be. So ultimately, it's still a user ID set of permissions against what somebody's able to do.  
   
 

### 00:56:40

   
Ian Johnson: The assumption is that you know are we really talking about dividing that into well this user can do this for this program and this user can only do these things for that program because to me I'm not sure that's really our business's work at that granular a level. I mean, we could I'm not I'm not throwing it out and saying it's not something that we need to consider, but if I if I've got the permission to configure a product or whatever whatever it might be, um if I try to change an  
George Westbrook: That's good.  
Ian Johnson: MCC category, add an MCC category onto a expense management product on a well, I don't know, if I went to change something on an MCC category that's effectively not relevant to that program at all, then the fact I've got some permission to do it still means it's not going to happen because it's not relevant at a program level. It's okay, you can do it, but you but we're not going to do it because you can't do it. You can't do it at a program level because I think I'm just thinking from a human perspective.  
   
 

### 00:58:02

   
Ian Johnson: I know I know that's not how we want to design this. But if I've got multiple programs, there are things that are set that you just don't do with a consumer debit program that you might do an expense management program. They're just irrelevant.  
George Westbrook: When when you say you don't do is is it a you shouldn't or it's like you physically cannot if it is this type of  
Ian Johnson: Well, I think there's very few users, Mike,  
George Westbrook: program.  
Ian Johnson: as I'd understand it, that for example, if somebody decided they wanted to add some um MCC category blocking below or below a consumer debit program beyond the ones that are already set by a by the person who set up the product. you wouldn't we wouldn't allow any just any user to do that versus so from  
Michael Moores: No.  
Ian Johnson: a permission point of view um but if you had permission to do it and then you ask to do it. It might be a completely stupid thing to do, but you have permission to do it. So, we'll we'll we'll let you do it.  
   
 

### 00:59:19

   
Ian Johnson: You as a user can do this. I mean, it's not  
George Westbrook: And then I suppose that's where the alerts could kick in because we'll see right this actions happened right it goes through the triage this use we've updated card configuration sends the web hook card configuration updated AI analyzes you're on this program you've made this change. Why have you done this? Alert the user. Here you go, user. You've just changed this. You're currently on this program. You shouldn't do that. That's maybe level level one. And then for the full A gen tickets, you've just updated this. Are you sure you wanted to do it? If I were you, I'd do XYZ. Click a button and I'll go fix it for you.  
Ian Johnson: Yeah, I mean that that's the that in terms of an experience I would envisaged the better solution being you there's a request the request is analyzed however that happens technically I don't really care and before that request we go back with any information to make the make a decision gets you know is made.  
   
 

### 01:00:27

   
Ian Johnson: So even if it's the full agentic flow you there are still thing unless we just say well if it's agent to agent we don't care we'll do whatever's asked which I don't think we we really want to do because otherwise you know everything we've done in the console is tried to help people who don't who are not card experts understand the impact and try to guide them to making the right decisions and making sure that they have the full information. If we were to not have that on the uh pure agentics, my concern is that people think, "Yeah, I don't know. I've just done it and off I go and and everything's fine." And and if you if they make the change and then an alert comes back and says, "Why have you done that?" That to me would be, "Why didn't you tell me not to do it before I did?" So, it's a request. Does that A, can you do that thing? B, does that thing make sense? C, here's the impact and things for you to consider.  
   
 

### 01:01:43

   
Ian Johnson: Confirm you want to make that change. It's no different to essentially what we're doing from a console point of view, which is prompting people just to say, are you sure this is the impact of the change you're going to make? We'll still make it for you because you've got the permission to make that change. It's not for us to say how you manage your program. is for us to help you understand what the impact of what you're doing is or to give you some contextual information based on data that we know because we're consider you know we're we hope we are card experts. So I think it's just that way of thinking about it for  
George Westbrook: Yeah.  
Ian Johnson: me.  
George Westbrook: Yeah. And it how is it in terms of like layers in terms of if we get that request like let's just say example the user they're like agent go away I don't want to listen to you just do this for me just do it and then it reaches that endpoint that request is made is is then let's say it's happened and then we still still surface the alert and say that I suppose that's another design decision if a user has said to do something.  
   
 

### 01:02:56

   
George Westbrook: Do we respect that that is right and that that should happen and we don't alert them? Because then we've got the other flip side is every time a user makes a decision um they're getting alert they're getting alerted. I mean that's I would say that's not a good user experience. I suppose it's we might need to like code a no. So what we'd have is yeah then it would be the more functional layer where it would be right every every decision made we compare it against what is optimal if it's not optimal then we alert  
Ian Johnson: the here's the here's the thing for me with it. So because I always think that there's a way of there's a simple way in you make that request and before the request gets made without pulling any information back you can ask the question you would you like any information or recommendations about the change you suggested. No. Okay. And away you go and you do it. The the point for me is we've we could take a viewpoint of you asked us to do it, we did it.  
   
 

### 01:04:09

   
Ian Johnson: We don't care. The crucial part to it, Mike, is is there an audit trail of everything that happens so if somebody turns around and  
George Westbrook: Yeah.  
Ian Johnson: goes, "Hold on a minute. My transactions are down." Let's give an example. My transactions are down by 50% over the course of the last week. And it looks as though it's because you increased well reduced the maximum transaction limit which is part of the thing as I remember an example in the console where somebody says reduce transaction limit and we go the impact we're looking at data and say the impact is likely to be this in terms of actual spend through the program. Um and then we just didn't prompt them. We didn't tell them anything. We just let them get on and do it. the the downward flow of that George guaranteed is somebody arriving at Mike in whatever way format they do it of contacting Mike or Mike's team to go why I didn't realize that that was going to happen when I did that why you know why didn't you tell me or can't we need to change it back and then that's delivering a really s***** experience to people the thing is there are some things they could change Mike like it's  
   
 

### 01:05:19

   
George Westbrook: Yeah.  
Ian Johnson: not going to really make a blind bit of difference to anybody, but there are other things that they can change in the car program that can have a material impact. It's that balance of it's always the balance of um usability and managing risk. So if you think about 3G secure when that came in and well two factor authentication came in and those type of things there was a bunch of people up in arms about oh this is terrible and he's adding an extra step in and you know gradually where the card industry bid went was to try to make it easier and easier and now it's all second nature but fact simple fact of the matter is fraud went down dramatically as well because of this being created it all got pushed somewhere else and I I don't know my daughter, but to me, if we're not going to play a role in helping clients make the right decision and accept that might be a trade-off where there might be people who are card experts who go, I know what I'm doing.  
   
 

### 01:06:28

   
Ian Johnson: Just I've already analyzed this. I already know what I'm doing. Just get on and do it. then I I do think there's a risk of unintended consequences that people do something and then bizarrely they consider it to be our fault that we let them do it and we just need to find that balance um because of the nature of what we're doing. Um, and in some respects, from what I've seen with some providers so far, they've just massively limited the amount of things you can do through FTP servers so that you can only do the things that come with no risk initially.  
George Westbrook: Yeah. Yeah. Yeah.  
Ian Johnson: Great.  
George Westbrook: I can I can see the information. I can see on a dashboard.  
Ian Johnson: Yeah.  
George Westbrook: Brilliant.  
Brett StClair: Um but I mean surely this is where the trust principles kick in. No matter what your level of expertise you initiate it goes away. It does the necessary work but we always have a validation step before I start.  
   
 

### 01:07:33

   
Brett StClair: This is the change that I'm going to make. Are you happy? And then if they see any problems with it, they get to change it because they're the expert or not the expert. Either way, um, at least they can go ahead. It keeps those steps really short but covers the whole experience by saying we have checked with you. You did confirm it was fine. Um, you know, and in that point if we need to do recommendations, we could always do the recommendations there. We can say this is what we're going to do. You said this and this, but we recommend that and that. Do you want me to go ahead? And I think that solves the  
Ian Johnson: Yeah. Many times there won't necessarily need need to be a second step to it.  
Brett StClair: problem.  
Ian Johnson: you know, it's if what they're asking to do it, you know, there's no real re impact information to pass back. It's like just okay, but but you would still be confirming, okay, this is what you've asked me to do just to confirm.  
   
 

### 01:08:39

   
Ian Johnson: I'll go away and do it. No additional context to what what you're about to do. I think it's always given a personal information. But I did I do think and I've thought it for a long time about this whole piece and generally AI in financial services stuff. This is the nub of the whole thing in terms of the risk of people coming back and  
George Westbrook: Yeah.  
Ian Johnson: going why this has happened to my business why has that happened and yeah we can track back and say okay there was a an API called initiate is through our MCP server requesting us to do  
Brett StClair: Yeah.  
Ian Johnson: this but I don't understand the audit trails of what we  
Brett StClair: Yeah.  
Ian Johnson: will have available to say and we prompted and you confirmed. So prompted this trust thing that Brett talks about. Prompted trust. Obviously not all of the detail of everything that got said, but we prompted you confirmed. Away we go. Then you can imagine the argument gets into well that might be the case but you didn't tell me that this was going to be the impact.  
   
 

### 01:09:53

   
Ian Johnson: So I didn't feel like and this  
Brett StClair: and we could we we could guesstimate the impact right that's that recommendation  
Ian Johnson: Yeah. But the point is if something if we do something  
Brett StClair: thresholds you will see a reduction in spend by X are you aware of  
Ian Johnson: Yeah. But then we do it and then later on there's an impact on the business and let's say that the person who did that thing it comes to light in some financials that something's  
Brett StClair: Yeah.  
Ian Johnson: happened something's down or or there's more chargebacks like I don't know I can imagine these different scenarios and then they're under the under the heat to go  
Brett StClair: Are you  
Ian Johnson: well what what happened I made the I made the change I used Claude requested change got made ten made the change for me here we are um now you can imagine that some businesses that would be the end of the conversation it's like well you asked for it to happen they did it if we're selling on the basis that we're using delivering an intelligent experience that helps customers that don't have to be card experts we're selling that and there's an expectation created that you're going to help me make the right decisions and not allow me to do anything stupid.  
   
 

### 01:11:11

   
Ian Johnson: When the s*** hits the fan, how do we prove that we did give advice? How do we prove that we gave advice? You asked us to do something. We  
Brett StClair: It's called a I told you so  
Ian Johnson: confirmed  
Brett StClair: dashboard.  
George Westbrook: Well, no, because I suppose it's it I suppose this kind of links into like let's call it like the internal ops agents is let's just say we've we've done everything and then it's we've got the support request through um we obviously got all of the more like transaction data but then I suppose there's the agent data as well. So, I suppose that could be a let's call it like a a support investigations agent where it's got access to all of the all of the chats that the user or that organization has had. Um, and then this agent can go query their data, can understand it, analyze it, can also look at the chats and be like, you executed this tool. Um, which in this chat it said it gave you the impact in message three and on message four you click this button or said to the user confirm I want to make this  
   
 

### 01:12:23

   
Ian Johnson: Yeah. So that that's my point and again I don't understand technically what that means not from functionally being able to do it but what it means  
George Westbrook: action.  
Ian Johnson: from storage and size of databases how long we keep that information for all of that off. Um needs to be  
George Westbrook: So I suppose we could Sorry,  
Ian Johnson: considered.  
Brett StClair: And I'm just thinking about our audit databases where we track absolutely everything.  
George Westbrook: bro.  
Brett StClair: Should we not be putting everything into your data warehouse, right? instead of cuz we usually build everything with its own kind of knowledge graph all that kind of stuff that sorry just uh thinking out aloud  
Ian Johnson: It's it it makes total sense to me that that the approach  
Brett StClair: here  
Ian Johnson: of request you know if there's an impact to pull back an impact to pull back contextual information confirmation to go ahead confirmation that the change has been made. Okay. And then if somebody comes back later when the s*** hits the proverbial uh well actually I've got that the wrong way around.  
   
 

### 01:13:34

   
Ian Johnson: It doesn't matter. I've already said s***. But anyway, once the s*** hits the fan and starts going, "What? How on earth has this happened?" We have got an audit trail in the same way that we would have from an API call, Mike. Received an API call from you asking us to do this. We did that. And at that point there's an end of the argument because nobody else is involved.  
Michael Moores: Yep.  
Ian Johnson: I think the AI thing becomes a it's a different world in the sense that identifying that we can identify that the API request triggered from uh what user the user that triggered the request the part for me is and we execute that request. So, normally in normal circumstances, that's that's game over. As long as you've got your permissions right, so this user did something they're able to do, we made the change. And if you just had that as a that's basically the service you're providing, we wouldn't care and be scree because we can prove that through audit.  
   
 

### 01:14:38

   
Ian Johnson: The fact that we're trying to provide more contextual information to get confirmation of somebody doing something and that's a selling point for us. if we do it and then there's confirmation but then somebody in the business says to well they they told you what the impact was and you still went ahead and did it and I know they didn't tell me there was no contextual information provided that's the bit and I don't think it happened that often Mike to be honest but that's the bit where we'd need to be able to get back and go this is what  
George Westbrook: Yeah. Yeah.  
Ian Johnson: was that's bit  
George Westbrook: At 4 4:32 p.m. on Friday the 13th of November, you Yeah. And I think  
Ian Johnson: because you're dealing with because you're dealing with money. That's the challenge. Now, I don't know, Mike, if it's we need to think about things only changes affect multiple card holders because if somebody makes a change on an individual card holder, the impact is going to be limited. And in fairness, Mike, I think the contextual information that we're intending to pass back would be incredibly limited.  
   
 

### 01:15:49

   
Ian Johnson: I just don't see that there's there's not a lot of impact information you could give that is material enough that would make any change. If you reduce this card holders transaction limit to 100 pounds per day, the impact is they're only they're going to make three less transactions a month. So what  
Michael Moores: There's a there's a couple of things in there that's probably worth phrasing now. It's obviously um to your point of the impact is is very important for the transactional one. I think both have some merit. So obviously impact first you you're changing this it's going to reduce your authorizations by you know 20%. If that turns out to be you know 50 60% that's where you sort of alerting comes in I think so obviously intending change versus something's gone wrong. So I think we know the bad things that can happen you obviously reduced authorizations declines and stuff like that. So I think that's that as well. Obviously the API um we have a section for web hooks that any other necessary web hooks with DT.  
   
 

### 01:16:47

   
Michael Moores: So we haven't specifically planned a product web hook but we could do essentially the benefit of that is no matter how you make that change AI console or API a web hook will be produced. So you pull all that data back into the same place. So if I do go in the API the AI agent will know about every change that happens. That's the benefit of those web hooks. So I think that is good for we should get DT to do that. I think the other piece is the approval queue that we have in the console. So you know we have this backend API and these permissions and we do specify which permission needs approval. So some of the high ones we do require a person to have approval in the console. So we could look at using that existing system in there as well to make sure we do that um as  
Dorte Dye: Okay.  
Michael Moores: well. And obviously in terms of the audit as well, we are still working on it, but essentially having a combined audit between the uh console, so you click this, you did this, you navigated here and read this data versus the API which says you've done this.  
   
 

### 01:17:49

   
Michael Moores: Now, even if we we should log the chats anyway, but let's say the AI decides to make a change or card transition, the API will log that that this happened at this time and we'll make sure that the AI has its own use and say it was this person. So we've already got the stuff in there for say the console has done it the you know all these things we will add that in as well but I think to point we need that chat to say you actually said yes.  
George Westbrook: Yeah.  
Michael Moores: So I think all that will provide a really strong audit position. Obviously the API will all be all recording every API call who executed was it console? Was it the admin? We do have some sort of system changes as well. If a car expires will automatically hit the API to do that. So we have this ability in in the transitions. Transitions are a very big thing that I've not touched on yet. But every entity I explained today has its own transition.  
   
 

### 01:18:39

   
Michael Moores: So you can transition a card, an account or a card holder to different states. So that has a timebound thing from this state to that state. So all of those get logged. All the life cycle components are really bolted in that audit. Obviously we can add to that with the the AI charts as  
Ian Johnson: I think you make a really good point though,  
Michael Moores: well.  
Ian Johnson: Mike, and I've forgotten that thing of certain actions and the actions that are that can have the most impact of this approval cue that you described. To me, George, that that's the agent managing that, knowing that. So you say that you want to make this change. We theoretically can give some contextual information or we at that point can just say this this change requires approval from this person. Presumably the agent can you know somehow contact that person whether it's through a I don't know Slack channel or whatever channel it might be to alert them to the fact there's an approval thing. I think you know if you think about how the console's done it but ultimately I think I've forgotten that that bit is typically reserved for the higher risk changes that somebody could make.  
   
 

### 01:19:54

   
Michael Moores: Yeah.  
Ian Johnson: So  
George Westbrook: When when you say notify a use,  
Ian Johnson: Yeah.  
George Westbrook: you mean I'm assuming you mean in a in a client, let's say there's three users, one with super access, two with not. the one of the with not super access request to make a change that gets then put in the triage. Okay. Yeah. And then in the console I suppose that's Yeah. And then it's just having that kind of inbox of approval actions  
Ian Johnson: Yeah. Now on on their side, they might have built in claude or whatever tool,  
George Westbrook: where  
Ian Johnson: a flow, a workflow that basically picks that up and then manages it automatically directly out with wherever it needs to go to. I don't know. But from our perspective, we've advised that there needs to be an approval, I suppose the point there, Mike, is um at that point that the trigger for us actually taking action is no longer from the user that we told them they need approval for because of the approval workflow.  
   
 

### 01:21:07

   
Dorte Dye: Oops.  
Ian Johnson: It's being pat it's being delegated to somebody else to to effectively be the initiator of that action. It's not that they can go away in outside of us understanding it and come back and go approval granted. That has to be they can do whatever they want. But ultimately from our perspective, if I've understood correctly, Mike, it it delegates to another user for them to actually confirm that action to be  
Michael Moores: Yeah, the way we've done it is a approval is actually a permission.  
Ian Johnson: taken.  
Michael Moores: So you'll give out that approval permission to somebody. So if you don't have it, obviously we decide the actions that need approval. Um we've cut it at the moment. Basically anything product and above. So anything affecting multiple cards. If you terminate a card, yes, that's an important action, but that's going to get very annoying. So that's the risk is low because it's one card that you terminate. So that's sort of a privilege action, but doesn't require approval. Whereas if you go and change something on a product level or a spend control, they need approval because they they can affect mult.  
   
 

### 01:22:22

   
Michael Moores: So that's how we sort of split it. We've got privilege actions to govern the terminate in those sort of states as well. Then we have this approval mechanism for anything that affects sort of multiple cards that will go into an approval queue and then yes someone else has to approve that even if you are an approver yourself someone else goes and approves that change for you. So it's always that twoperson rule to make  
George Westbrook: Uh,  
Michael Moores: change.  
George Westbrook: okay.  
Brett StClair: So, actually the agent can't do too much damage anyway with the approval.  
Michael Moores: That's how it works on the console. Obviously we need to discuss how we want agents to work and adding that you know that bypass potentially I think in the future your risk level but I think aimed to do a user level that's what the user  
Brett StClair: Whoa.  
Michael Moores: can do put it into approval then I think you know as gradually you can say okay I actually want to give more access to that AI because I'm doing a workflow or whatever it may be I think that's something we can expect in the future but yeah essentially the the approval queue will govern a lot of the stuff um as  
   
 

### 01:23:29

   
Ian Johnson: But I think I think isn't the po isn't the point really from our perspective to consider what role we can play on managing that situation in an agentic world. So a request gets made It's clear that it needs to be approved elsewhere by another user that we will theoretic the agent would theoretically know who that user is and then it's a case of what role do we play in sending  
Dorte Dye: Mhm.  
Ian Johnson: that approval request to that other user and that approval request then being the thing that the agent says okay confirmed.  
Dorte Dye: I think the question here would be would when the um agent sends the approver request over would they give also the notes about that AI agent made that recommendation because otherwise the audit trail might be not fully consistent.  
Ian Johnson: only to the person that has because this is where I was going with it. Only to the person who's approve that can approve  
George Westbrook: But wouldn't you So let's say I'm I'm in the console.  
Dorte Dye: Yeah.  
George Westbrook: I've got approval to send for an approval.  
   
 

### 01:24:47

   
George Westbrook: Um I get presented the analysis and then it goes are you sure you want to do this? Yes. Then it sends to the other person for I think this is what you would talk about daughter is it gets sent to the other  
Dorte Dye: Mhm.  
George Westbrook: person and then the other person sees um Joe Blogs wants to make this change. This is what we think the act the impact is.  
Dorte Dye: Mhm. Yeah.  
George Westbrook: Are you sure you want to approve it?  
Ian Johnson: Yeah, that's that's right.  
Dorte Dye: Correct.  
Ian Johnson: I was wrong. You're right. That's the better way of doing  
George Westbrook: Yeah.  
Ian Johnson: it.  
Dorte Dye: I take that. I'm just conscious of time. We have another call in five minutes  
Ian Johnson: Need to jump off pretty  
Dorte Dye: and  
Brett StClair: So we've got all the API documentation.  
Ian Johnson: much.  
Brett StClair: So that's fine. We've understood all the I think we got a clear enough view on all the access how we want to approach it, where we want to approach it across the three different say user journeys.  
   
 

### 01:25:39

   
Brett StClair: Uh for a  
George Westbrook: Yeah. So,  
Brett StClair: gentle  
George Westbrook: I think I mean this is possibly one of the least sexy sessions because it's all about permissions and stuff like that, but it's really important because then it it helps paint the pictures for the other things and it's we'll probably in all of the other component sessions touch on aspects of this again um to really to really nail it down. Um, and I suppose the the other ones that we're think obviously there's the the co-pilot. Um, obviously we touched a fair fair bit on that, but that's going to be more like what do we want it to do? Blah blah. Do we want it to take actions? Things like that. The like we said there in a bit more detail on the the agent inbox and alerts, the full agentic experience, the kind of developer support. So both what in in the console, what do we what do we want that to look like?  
Dorte Dye: Do you think do you think you have everything for that  
   
 

### 01:26:31

   
George Westbrook: Um and then the for for the  
Dorte Dye: component?  
George Westbrook: access layer, sorry.  
Dorte Dye: Yeah.  
George Westbrook: Um I I think yeah,  
Dorte Dye: For sessions.  
George Westbrook: I think I think we've got 80%.  
Dorte Dye: Okay.  
George Westbrook: Um and that other 20% is going to come when we dive into a bit more detail on the on the individual components where we're like right in the alerts, what APIs are we going to need to do, blah blah blah. Um but I think conceptually understanding that okay there's certain permissions here there's certain permissions there these are going to be available in the console this is not so in the MCP server if we're exposing it to other people be it through their platform or through claude we need to make sure that this guardrails there and this guardrails here um and I suppose the further we further we get into it the the clearer  
Dorte Dye: And  
George Westbrook: it's going to become  
Ian Johnson: Yeah, listen. I I need to jump. I say we got this other call. What I suggest that there's a there's a lot been talked about.  
Dorte Dye: thanks.  
Ian Johnson: No need to try to make any immediate decisions. It's all been recorded, I think. Do what you guys normally do. Um because some topics have come up today that we haven't necessarily given full consideration to either.  
Dorte Dye: Yep.  
Ian Johnson: So we just need to take a we need to digest and reflect and then kind of get back together and figure it out because this  
George Westbrook: Yeah.  
Ian Johnson: is a very important part.  
Dorte Dye: Great.  
Ian Johnson: All right  
George Westbrook: Yeah. And it's not it's not an issue if we need to do another one another one on this.  
Ian Johnson: folks.  
George Westbrook: I say this is very important and like you said we need to nail  
Ian Johnson: Yeah,  
George Westbrook: it.  
Ian Johnson: agreed. Cheers everyone.  
Dorte Dye: Okay,  
Ian Johnson: Catch you later.  
George Westbrook: Perfect.  
Michael Moores: All right.  
George Westbrook: Thank you very much.  
Brett StClair: Byebye guys. Thank you.  
Dorte Dye: jump off. They will fight the mouse.  
   
 

### Transcription ended after 01:28:38

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

**