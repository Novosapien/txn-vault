**

Jun 11, 2026

## Component 2 (Notifications/Information Layer) Part 2/2 - Hold - Transcript

### 00:00:13

  

Brett StClair: recognize I was sitting in another hangout going, "Where is everybody? What's going on here?" It's

Dorte Dye: It's always

Brett StClair: always something.

Dorte Dye: something.

Brett StClair: Hey, I'm just glad it wasn't George this time. I'm I'm really pleased he was on

Dorte Dye: I mean,

Brett StClair: time.

Dorte Dye: he is not on the screen yet, so for all we know, he might be still stuck at a coffee machine.

Brett StClair: This is George's note taker.

Dorte Dye: There you go.

Brett StClair: Oh, I see George hasn't done his

Dorte Dye: It's it's a better time for you 10 o'clock, right?

Brett StClair: hair.

Dorte Dye: So, you're already three coffees

George Westbrook: I have my coffee to the to the to the side of me

Dorte Dye: in

George Westbrook: pre-prepared, I think.

Brett StClair: So, um George, just double checking. I'm merging your open questions with um my gap analysis and then I'm going to regenerate the gap analysis with your open questions and my gap analysis. Is that okay? If not, too late. I've started the process.

Dorte Dye: Ian sends his apologies.

  
  

### 00:01:20

  

Dorte Dye: He's tied up. So if there's anything we need him on, then we just park it to the end and then he we can back in.

Brett StClair: No worries. No worries.

Dorte Dye: It's one of these days back to back

Brett StClair: That's so bad. Right. I hate it when I look at my diary and it's just meeting meeting meeting.

Dorte Dye: when you don't get anything out of them, right? Because you don't have the time to process

Brett StClair: Right. That's the thing.

Dorte Dye: it.

Brett StClair: Um, so, okay. So, today, um, it's labeled. It's actually a hold. It's an extra session for us to go through anything that we're missing.

Dorte Dye: Yeah.

Brett StClair: That's why I'm just quickly rejigging. Um, I didn't realize Georgia also had a bunch of open questions. There we go. There's my I am going to share this. me get it on to the right machine quickly. Um, just going to pop this on here quickly.

  
  

### 00:02:23

  

George Westbrook: There we go.

Brett StClair: Put it on to tick in upload reasons. There we go. I've just shared it on the Slack group, guys. And we can just want to be able to pull it down here. And then I'm going to share my screen.

George Westbrook: I I didn't quite hear what you were saying saying there Brett because mying audio was going in and out.

Brett StClair: No, it's okay. I've taken your I see you had a bunch of open questions on your side.

George Westbrook: Um,

Brett StClair: So what I did is I took the gap analysis I did merged it just made sure that there was nothing overlapping on your with your open questions popped it into there then I pulled that information and recreated the gap analysis and I figured it just be good to

George Westbrook: okay.

Brett StClair: have um that here. Right.

George Westbrook: H

Brett StClair: Um now I've just got to figure out how to download this thing.

George Westbrook: Click click on the snippet. Click on the cloud and then click open file.

  
  

### 00:03:42

  

George Westbrook: Proper boomer behavior. Brett, how do I how do I open

Brett StClair: What is going on here? I feel like a proper boomer going on here.

George Westbrook: this?

Brett StClair: Hold on. Click on the snip. Oh, there. That one. There we go. I was clicking on the wrong snippet. Okay. And then let's I'm just going to put this here. I'm going to share my screen with everybody. Um okay. So two things I'd like us to cover today is let's just felt like we didn't really touch on the internal support tickets. self-healing, that kind of stuff at all. Is there any reason, George, why we might have held back or we just didn't get to that from an internal ops point of

George Westbrook: I think we kind of we kind of touched on the support,

Brett StClair: view?

George Westbrook: but I agree we didn't we didn't go we didn't go as deep as maybe we could have. Um, this self-healing, I think the only time we mentioned something about that was, and this was ages ago, was like the the self-healing of the the document.

  
  

### 00:04:58

  

George Westbrook: Oh, no, we mentioned that yesterday. the self-healing of the documentation. Um there's there's the possibility about the the self-healing code itself. Um but I think that could potentially be rather than actually Oh, he's dropped off. Um yeah, it's basically because I think we showed we showed it to you a while back was how we deal with errors where obviously we got everything tracked. An error happens, Sentry picks it up, it then goes investigates blah blah blah which is obviously something that we we can do with um with you guys as well. It's obviously just dependent is that is that just the just the AI piece? Is it potentially stuff that stack works doing as well? Obviously, I can imagine from what you guys have said that DT wouldn't want to touch that with a barge pole. Um, but if it's there, it's it's there. Um, and effectively all that is Mike is and daughters is just claw code in a VM that's going to go investigate on a specific part of your code base, say what the error could be, submit, and then go all the way up to submitting a PR as well.

  
  

### 00:06:14

  

George Westbrook: Oh, I think you're on

Michael Moores: Sorry, keep ming. Um, yeah,

George Westbrook: mute.

Michael Moores: so you have to consider obviously so DT is going to be basically owning all of this stuff sort of post, you know, stat works going to build it and then hand it over. So you have very very strict policies that we've, you know, even down to the framework and the libraries were allowed to use and stuff like that. So if they're managing it, it is very difficult to add certain stuff in. So I think with that they would be it's very hard against something like that.

George Westbrook: Yeah.

Michael Moores: Um so yeah I think that that's the difficulty we have. Obviously in terms of self-healing we were sort of referring to I guess the more knowledge type things you

George Westbrook: Huh?

Michael Moores: know self-healing documentation more from an operational standpoint I guess obviously just making sure any learnings that we do have aren't sort of lost in in the pipeline basically you know from the the knowledge um the AI and the the tickets basically that's sort of it's

  
  

### 00:07:08

  

George Westbrook: Yes.

Michael Moores: certainly for us a first aim um I say we can speak to detail about the the self-healing code potentially um But we're still sort of iring out the architecture, let alone the as well.

George Westbrook: Nothing.

Michael Moores: So, it's difficult for us to sort of say where we're going to be on that. We don't even know how we're going access to the data or the logs ourselves yet. And it's quite a sticking point with them at the moment to to try and get in there because I think a lot of it sort of DT environment which we're coming across a lot of blockers with because obviously TX should be owning the system, but we're going through sort of DT firewalls at the moment and we're having to sort of try and unstrip this stuff. So it's very difficult for us to get any traction on on that side

George Westbrook: Yeah, that's yeah, that's fair enough.

Michael Moores: basically.

George Westbrook: Um, I like because I think like we mentioned yesterday with the with the internal agents piece, it's one that can that can balloon.

  
  

### 00:08:05

  

George Westbrook: Um, and it's it's one of those things that as we're going along, we'll probably be all right, got this issue, right, let's let's build let's implement this in whereas obviously the other stuff being more user facing, we've we've obviously got to get to that get to that now.

Michael Moores: Yes.

George Westbrook: And I mean there's still massive there's still massive components. Um, so there's yeah, there's going to be a lot a lot done regardless.

Michael Moores: Excellent.

George Westbrook: Mr. Gap analysis, you want to You're mute, Brett.

Brett StClair: Should we do a quick flick through here? Um, and see if there's anything that's really tried to figure out its own kind of build blocking outstanding decisions where it is. And, you know, we just need to make sure either it's missed it or we've missed it or if it's vital or crucial. um whether we just take it off the list or we do keep it on this kind of register. And so the thinking here is always to keep the register so we know any decisions, anything that might be pending something or other, we've just got a note of it.

  
  

### 00:09:20

  

Brett StClair: And so the first hit on this is not going to be that accurate. Um, but it's quite nice to kind of keep track of this, especially at the stage we're at at the moment. Um, does anyone mind if I just quickly whip through this with everybody? And then we just do a quick Yeah. Yeah. Yeah. That's still a block. Um, so it links everything back to various numbers. It kind of uh it's tracking a whole lot of stuff. So when we comment on it, we just got to call out the number, comment it, and then it should go and resolve that analysis or add a decision or make a change point to it. Um, ordered immutability, append only and retention. The assumption is immutable retent retention window and storage location is undecided. Um, this is around the access layer. I think we just briefly touched on it. That's why it's kind of highlighted as a kind of blocking. I would say that's true, right?

  
  

### 00:10:23

  

Brett StClair: We It needs to be immutable. But I guess the question is where the storage location that it's trying to pull out. That's yet to be decided, right,

Michael Moores: Yeah,

Brett StClair: Mike?

Michael Moores: we've had a conversation with obviously I sent you some questions this morning, but we had some conversation with DT yesterday on the data lake

Brett StClair: Thank you. We saw that.

Michael Moores: to interrogate the data lake as in push stuff in from a a client point of view as well. So we do have that ability to push from the AI side into our data lakeink as well which is one of the important things. So we already have quite a intensive audit log history there anyway from a a DT and a sort of core point of view. So I think it would make sense from there. We just need sort of flesh out the some of the stuff in terms of availability what the the hot data is and stuff like that. So I think as we go forward we just need to see what is the data we need regularly versus what we could put on sort of cold storage as well.

  
  

### 00:11:20

  

Michael Moores: So I think it currently makes sense to go there. We just need to go a little bit further with DT in terms of the actual data architecture and stuff like that before we can absolutely confirm that's where it'll go. But um yeah, definitely need that um at some

Brett StClair: Okay.

Michael Moores: point.

Brett StClair: 0.9 AI permissions config building or user permission mirror for non-console access no API today when and owned by whom gates all agent execution outside of the console. Um, so this is people coming back in and how to manage the permissions. Again, I think we just touched on it. This is we kind of parked this a bit for the AI to AI if I remember correctly,

George Westbrook: No,

Brett StClair: George.

George Westbrook: it was so an organization will have a set of permissions which we I think we settled on assuming the organization is going to pretty much have access to everything and then obviously different users within within the organization are going to have different permissions within the scope of what the organization has and then how are we going to do that with the with the agent because the no I think you were kind of right actually about the A2A um kind it is and it isn't so it's so I think Mike you said that there's going to be one API key for the organization correct me if I'm wrong and then we might need to have different API keys for

  
  

### 00:12:52

  

Michael Moores: Yes.

George Westbrook: each user um to when we send it to the send it to the MCP server it turns on or turns off certain tools. Um part of me think does it need to be an API key? All we need to do is just have the user ID and then given the user ID we can query their permissions and then it does it that way. Um, to be fair, I think that's that that's something that's it's it's not a massive thing. It's just we know we need that with a specific user, they're going to have certain going to have certain permissions and they're not going to have others that the organization might. So, we need a mechanism in order to turn off certain tools and turn on other ones.

Michael Moores: Yeah, I think from our side as well, it's just the sort of two use cases. Obviously, what about if they connect their app into our AI? So AI to AI that is more of a system to system very much like a system to API. So that's that's we've got I think the AI sits across both those.

  
  

### 00:14:03

  

George Westbrook: Yeah.

Michael Moores: So console and the API are very much separate. I think the AI bridges that gap between system to system and users system basically. So we just need to make sure that if someone's trying to build something into our AI to improve their banking application or whatever then we can do that a system level. But also if someone's just using cloud for example then they're they're not sort of bypassing their permissions that they would get on the console by going this route

George Westbrook: Yeah. Okay. Yeah. So,

Michael Moores: basically.

George Westbrook: yeah. If we take the if it's their system, so if it's their version, let's say they've got an agent in their application, um it's possible, but would be obviously more difficult because there isn't a login to TXN, so we wouldn't really know what the permissions are and then they'd have to replicate the permissions on their side, which need to kind of perfectly align up. Um, so that possible but more difficult the let's say the claude experience then we'd have to have like some sort of oorthth for the MCP server um which would link them as a user not as an organization and then we could get the permissions that way.

  
  

### 00:15:24

  

George Westbrook: Yeah. Okay. Yeah. Um the

Michael Moores: system where you know if we need to generate another key I think just having to think of the permissions that we want from the AI they may be more granular than the API again so it may be that we just have to have that here's your AI system system key for example and then we go off so very much happy to do that obviously we'd have to service that in the console But we have sections for that in the console ready for API keys AI and stuff MCP. So it's something we can do just need to think about how we generate those keys. I think for the API there's this ongoing discussion about moving to JWT tokens. We're just looking at the possibility of that.

George Westbrook: H.

Michael Moores: So obviously whatever method we use will probably align it standard.

George Westbrook: Yeah.

Michael Moores: So I'll confirm on what that's doing. I'm just making sure that basically the API key shouldn't expire ever. similar to it should be long-term standing key.

  
  

### 00:16:18

  

George Westbrook: Yeah.

Michael Moores: So if they can support that with JT or their version of JT tokens then we'll go for that. Um obviously suspending rotating any action that the client wants to do to refresh that key should be possible. Uh or that access you know whatever we decide on that access should be refreshed if they ever leaked the authentication fl basically.

George Westbrook: Yeah, because I know that there's a few I think it's notion when we used to use notion quite a lot. Every time I'd log in, I'd have to reauthenticate and I want I just that was genuinely part of the reason we stopped using notion because every time you want to use it, you got to relog in. And I was like, right, just we're getting it local and we'll just use git to manage it, which could argue is a bit bit worse, but it had so many more benefits.

Michael Moores: Yeah,

George Westbrook: Um, sign up login

Michael Moores: definitely.

George Westbrook: design.

Brett StClair: So I think this is around the developer portal and talking about our sandbox and it's just

  
  

### 00:17:15

  

George Westbrook: Yeah.

Brett StClair: saying great the sandbox is there and everything. Have we thought about a sign up carrying through because it's a public portal right? Then how would we manage or and I guess it's more for you Mike just on the design side somewhere you need to be able to say login boom and then they've got access to those kind of sandbox kind of environments I think that's what it's trying to call

Michael Moores: Yeah, I think this one is still we haven't scoped it in the design for a login or sign up right now, but there are several things that may change that behavior in terms of if DT need a key per person, for example, and it's not fully open. That may change our mind. Um, in terms of Ian's AI cost and that sort of stuff, we may decide to restrict some behind that. So,

George Westbrook: Amen.

Michael Moores: that's still being scoped in terms of exactly what we're going to hide behind it. I think for this, you know, let's say we don't have a true login identity.

  
  

### 00:18:11

  

Michael Moores: I think we should, like you said before, still capture that email to get access to the AI. So, we're still tracking that session and that sort of stuff like that as well. Um, so we'll we'll speak to Ian and the DT team to see how that's going to happen. Um, but I guess we will still need some some sort of

George Westbrook: I just thought something that could be quite good and could so this is yeah this is for developer support and it

Michael Moores: email.

George Westbrook: could be people who haven't already signed up. So one potential benefit of getting them to log in is obviously one you get the lead. So I think the point worth noting as well is this this would in my opinion be a completely different MCP server from the actual inuse in use uh in use um like the co the logged in the paid for user um it'd be a slightly different one. So what yeah this is kind of a light version more heavy on documentation and testing the

Michael Moores: Yeah.

  
  

### 00:19:08

  

George Westbrook: sandbox. So the user signs up you've got their email you might know their company or whatever. Um but then what we can do is track every single request um that

Michael Moores: Heat.

George Westbrook: they've that they've done what endpoints they've hit what documentation pieces of documentation that they've got. So if they ever become a client or ever book a call to start the sales process, you've got all of that information. So maybe there's a centralized database. You got Joe Blogs at ABC Bank. Um he's requested a meeting. You can go and look at through all of his MCP usage. Um and see that he's very he's asking a lot of questions about this specific page. So then as soon as you get on the call, it's almost like you've read his mind and you can answer those answer those questions before they even come up from him. It's I suppose it's just it's just building I suppose in helping in the sales process just collecting as much information as possible so that you know they've tested the API you know they've hit these end points you know these are the questions that they're asking you know and then you can start to understand what what is it about the the API or the platform that it is they value and then suppose makes the sales process a bit easier.

  
  

### 00:20:23

  

Michael Moores: Yeah, definitely. I think we looked at this a while ago obviously sort of future for before AI was even there but developer to console is a is a journey. The only thing we need to consider obviously people use Gmails and then use company. So we haven't start scoped it but some sort of migration to a actual account going from a Gmail to a work

George Westbrook: H.

Michael Moores: one. So again that's something we could build in the console and if we do log in so we have a back end for the console which is just sort of the user permissions like I said we could expand that to you know if we did log in a developer portal role you then have that user account in there it manages all the authentication and then you can then migrate that user easily into a boarded customer and obviously that will go nicely with the the AI tool as well.

George Westbrook: Um,

Michael Moores: That's some the sort of future state we were looking at. Um we just need to decide obviously it definitely will be phase two in terms of develop portal now because it's going to be ready by end of July.

  
  

### 00:21:18

  

Michael Moores: So we have got a phase next phase in with the portal. So it may line up nicely with this that we're actually looking at doing that as well anyway. It just needs to be sort of rescoped with stat works basically. Uh but yeah ultimately I think it's good to have. We just need to see aim, you know, what do we want to give them? And then that most important one is capturing that data and it's not lost if we do actually end up getting another client as

George Westbrook: Yeah, because I suppose the I suppose to avoid that email email problem of them putting in a

Michael Moores: well.

George Westbrook: Gmail, I suppose You just put company as a mandatory field as well. It just email email company. Um then I think the drop off if you put company might be like 1% 1 2%. You maybe people put fake companies but then at least I think it's going back to the sales process right you know their you know their um the request the question they're asking.

  
  

### 00:22:13

  

George Westbrook: You know the company you probably know the person as well from their email. Get some agents that go out research the individual. research the company, create kind of like a a pre-sales or a sales pack with what they've been asking, every single thing about the company and the individual. Um, and then it's yeah, sit down and a lot more a lot more

Michael Moores: Yeah, I think yeah, I didn't think about company,

George Westbrook: informed.

Michael Moores: but you see that quite a lot, don't you? When you log into things, even with your Gmail. So, I don't I don't think that would put people off. I think obviously people are they use Gmail, they're very early on, so they might not even have a company name. So, we just need to have a think about that. So you know very early on we have a lot of people just sort of triing um you know from Marqueta we had a lot of like students trying it out as well. Not that we target them, but just they're the sort of type of people that were using that as well.

  
  

### 00:23:00

  

George Westbrook: Okay.

Michael Moores: So, I think we should consider that and make sure we're not turning away too many people. Okay, we never tried a Marqueta. It was sort of they were very different. Here's your portal. You create a brand new account. That created a problem that if you did sign up with your company email, you couldn't use that email in the console. That reverse problem. So, we're just making sure that we don't want that problem. And also, obviously, if they do use a personal, we can pull them in. I say I think the is potentially a good way to go for

George Westbrook: Yeah. Yeah. Okay.

Michael Moores: now.

George Westbrook: Yeah, that makes a lot of sense. Um the persistence store where save render views recurring task definitions live state model for RS. Brett I know I know you built built this one with number 22. Oh, I I think I know what

Brett StClair: This is this is um uh having a state right when we are

  
  

### 00:24:06

  

George Westbrook: this

Brett StClair: in the co-pilot section and where are how we going to store that state like in a persistence kind of store kind of environment. Um I think it's just picking out that we're talking a lot about statefulness in the co-pilot and it's highlighting nothing's been spoken about with regards to the actual

George Westbrook: Yeah,

Brett StClair: store.

George Westbrook: I That's a the the only one which probably require a bit more thought is the recurring task. But I mean that's just a like a what a job. Um but like the save save

Brett StClair: We we we're we going to store to um Stack Works's database,

George Westbrook: save

Brett StClair: right? Everything that we're working. So whatever kind of calls, they're going to be that source of truth. We're not carrying a necessarily a separate database, are we?

George Westbrook: I suppose that's that's a decision in itself we can do we can do either um I suppose it's just it for is it better to isolate or be be in the same but then I suppose No, I think the same would be better if we're rendering in the console as well rather than having to connect two different database.

  
  

### 00:25:24

  

George Westbrook: Yeah, that makes sense.

Brett StClair: And we're also calling the APIs, right? So rather do a single clean IO.

George Westbrook: Yeah,

Brett StClair: Um

George Westbrook: but it's going to be two queries anyway, so it doesn't matter if it's to different places because it's

Brett StClair: the only thing I worry about is I think about the like our usual caching kind of store environment tracking everything from an order point of view. all the uh agentic behavior. Um maybe that'll just overload their their and dirty their data environment. Right. And I guess I'm also going to use this point. Mike, if you could talk us through the two slides as well after this point because I was just having a look through it and it's probably worthwhile you talking us through it so we don't make any assumptions on those two slides. I was having a look at it

Michael Moores: Yeah,

Brett StClair: now.

Michael Moores: I think in terms of the the database side again we're sort of still working with DT on the architecture will be obviously the DT side then basically I built sort of one architecture diagram.

  
  

### 00:26:37

  

Michael Moores: So on the left hand side is sort of the DT owned core and then there's instances for the portal and the uh console sort of separately. So there is the ability for them to share the dashboard. There also the ability to have, you know, separate ones as well. So we're just sort of working through how that works from that. So again, I'll send you the I can send you the draft architecture diagram that they're proposing. We still sent a lot of questions back and concerns on on that, but it's probably worth you seeing how to structure that as well. Um, and then you get a bit more idea where everything going to sit together basically. And then we can see where the AI bit can plug in essentially as well. Yeah, I can walk through those slides.

Brett StClair: This just quickly

Michael Moores: Not

Brett StClair: Okay.

Dorte Dye: I just have a question. Mike, did you actually send an email at that time in a day or was it your agent?

Brett StClair: What time is

  
  

### 00:27:32

  

Dorte Dye: Crazy. Absolutely crazy. 10 to 5.

Michael Moores: sleep.

Dorte Dye: The new Ian, you know,

Brett StClair: that?

Dorte Dye: it's like Ian at least is scheduling his emails now. Ian doesn't have

Michael Moores: I couldn't sleep.

Dorte Dye: mind.

Michael Moores: I've got a intercostal tear between my rib. Uh so I was in a lot of pain.

George Westbrook: Oh,

Michael Moores: So I got up a sports massage.

Dorte Dye: Oh s***.

George Westbrook: how did how did that happen?

Michael Moores: She nick my rib. So can't breathe.

Brett StClair: No.

George Westbrook: Oh,

Dorte Dye: Wow.

Michael Moores: Stand up. It's it's fun.

Dorte Dye: I think you should never go to that woman again

Michael Moores: Yeah. It's very sore. So yeah,

Dorte Dye: then.

George Westbrook: what did you what did you say to her before?

Michael Moores: I just Yeah,

George Westbrook: You must have said something and then she's just

Michael Moores: must must have done. So, I don't know.

George Westbrook: gone.

Michael Moores: But yeah, that's why I was up

  
  

### 00:28:13

  

Dorte Dye: Oh.

Brett StClair: So just for the agents point of view um we're just going to talk about the

Michael Moores: anyway.

Brett StClair: um big data um setup and configuration and the impact on AI. I and we've got two slides which I'll upload separately into the vault. Sorry, just want to make sure

Michael Moores: There's a whole um whole deck. I just want to get these two specifically, but we'll make sure you the whole end to end.

Brett StClair: it's

Michael Moores: So, I'll step back a second and touch on the the flow of the data lake. So, we have this you'll see curated on this slide, but we've got raw, curated, and consumption layer, which again raw is basically we have lots of different places where this sim's running. We have to contain all this data in one place. So, this is sort of a for me to query live support. You need to come in here very quickly. It's raw. but it's untouched. It just stays there. So that's the first thing that they're building for us.

  
  

### 00:29:10

  

Michael Moores: Then the next level we have is sort of curated. So this is sort of cleaned um eventually potentially AI improved as well. So this is where we actually start making use of our data um and sort of cleaning it and making sure it's it's good to go. Then we have our consumption layer which we have sort of roll up tables I think we briefly discussed. So if you're pulling down a daily dashboard, you don't want to be querying every transaction. we're going to have some sort of jobs in the background to roll that data up to a you know maybe a per program per day something that's easy for those reports to pull down. So that's the sort of three stages that I had in mind. Now um what this is looking at is on top of that how do we store the data from an AI point of view. So obviously AI uh we've got the tabsql which is good for searching and in the big queries but there's also sort of um JSON basically. So DT's recommendation here is both because obviously J um AI they're assuming imp uh prefers the JSON prefers those vectors as well so we can actually pull that down quicker.

  
  

### 00:30:14

  

Michael Moores: So that's sort of what they're suggesting here is that we we do both of those. Obviously, we need the tabular anyway because that's something we're doing, but providing these vectors and obviously the slide goes into the depth those vectors, but essentially providing those JSON layer those vectors to you can pull that down instead of those typed tabular sort of queries as well. So, that's a sort of current approach. Obviously, they're doing their own AI investigation. This is um this is a solution they've built for them based on the TXM requirements. So they're trying to make sure it fits everybody and their own AI objectives. So this is why you see sort of these decisions they've made, but they have taken in every TXM requirement into that. Um and so basically it form it'll be a raw dump of the entire core um issuing stack. We'll have sort of supplementary data like settlement clearing data that we'll be pulling in as well. We're not using that right now, but we want to store that for potentially doing settlement or reconciliation with the AI or the console later.

  
  

### 00:31:18

  

Michael Moores: So, we're going to store all that extra data that we could then later on use. And then obviously, like I said, the rollup tables and then, you know, a bit down the line when we get into sort of machine learning or stuff like the fraud monitoring, the enhancement of that data for AI, there's so much more we can do with the data that basically these card don't send very nice data. Um and a lot of these companies you know offer data enhancement for visa master that's something we could do on this as well with AI. So you know some of the companies charge a huge fortune for just adding a location for example on a mer they give you a name and that's it pretty much but you you don't get the geol location or anything like that. So obviously it takes a while to build that data up but those sort of things you could build and that's why we have this curated layer is like a step in the middle just to make sure that it's side you know potentially we need to scope it but we might drop some fields that just aren't relevant for you know curating the data in there we basically this is our reporting data on what we want to report on.

  
  

### 00:32:17

  

Michael Moores: So um obviously all of our programs will feed into one place. So there is slight differences of the raw data. So we each client will have its own tables and its own raw data. We'll then port that excuse me port that into the data lake with the addition of one field which is the program identifier. So we know exactly where that data's come from and the transactional data we have basically a uh I say I'll send you the the deck as well. It goes into the the rowle security and stuff like that to make sure only people are accessing the data. So inside the database there is this rowle security that makes sure client A can't get to client B and also bin sponsor which is another user. So bin sponsor might work with client A and B. So they should have access to client A and B's data specifically. So we're all building that into this as well. U but ultimately for us right now um we'll be going through the console and the AI to pull that data as it stands and obviously we'll end up building a API in front of it.

  
  

### 00:33:19

  

Michael Moores: So pull the relevant reports down and stuff like that. So this is something we just scope on there. But yeah, that's the sort of background. Like I said, I'll send you a full deck. I just wanted to get these two questions up

George Westbrook: Perfect.

Brett StClair: I just double check something here.

Michael Moores: front.

Dorte Dye: Mike, how far is DT doing with testing everything or is

Brett StClair: Okay. Yeah.

Dorte Dye: that they're planning and our requirements are in there and still working everything? So, it's it's early on. So, there might be still things that can change. So, it's not okay. I just want to make sure because it looks good,

Michael Moores: Yeah.

Dorte Dye: but if it's still early days, then there might be some bumps along the

Michael Moores: Yeah. So, you'll see on here that this, you know, number eight,

Dorte Dye: way.

Michael Moores: there's three options. Their recommendation is you'll be 1536. So, um, yeah, very much to change. They hadn't even considered the European side of it at all.

  
  

### 00:34:11

  

Michael Moores: There's many open questions,

Dorte Dye: Mhm.

Michael Moores: but this is to get us thinking about how we want it to be structured and then obviously I'm going to feed the questions back to them. Um, speaking to Ian this morning, there's already some push back on um the seven-year PCI that we have to keep. Where's that going to live? There's there's a lot more stuff in there and obviously the costing as well. So that we're sort of just working both sides out, the technical and the costing ultimately this is the the vector um depth basically. So they've done some research into the open AI standard and they recommend uh 1536 depth for that um just to balance sort of the recall and the cost basically. So um that's sort of think at the moment and I don't have any sort of push backs per se unless you've got any you know specific knowledge on AI side. I think that obviously that gives us enough context for my opinion on the sort of level of queries we're looking at doing.

  
  

### 00:35:05

  

Michael Moores: So I didn't have sort of any issues there but obviously you know you've got a good idea what the sort of size we're going to be doing of these things and I know we can sort of manage most of its skills and very structured approach as well which should also sort of reduce that down but yeah that's a sort of current thinking they've done um with a native vector in SQL server

George Westbrook: Yeah, because I think it's this what we've got to think with the AI sections is what what type of search do you want to do? So there's I mean the the most performative one is this new method called RLMs, recursive language models. It's effectively just agentic search, but you just keep on looping it and looping it and looping different smaller language models in order to find it. And I think it's like on like hundreds of millions of tokens um worth of worth of context. That's supposedly the best the best way at the moment to um to do the search. Then there's just more um aentic search which is just effectively an agent writing code to execute bash tool uh bash commands which will like gp the local.

  
  

### 00:36:13

  

George Westbrook: So I think say for things like documentation for the agent um I think the best approach in my opinion would be at runtime we load in the latest version of the documentation locally to the agent which it searches itself. But there's going to be times where we might want to use semantic search um or for ultra long context maybe um recursive language models um but then also there's like for fetching data as well the agent's just going to write the write the SQL query um and then going to pull back that data as well. Um but there's always a there's always a time and a place for vector search as well.

Michael Moores: Yeah. Yeah. So that's a sort of current thinking obviously and I did tell them that this will largely depend on the conversation with yourselves and that sort of thing. So you know very early on but we've pushed for this plan to sort of get an idea. So it's not being built immediately. Like I said what I'll do is I'll send you the full deck as well.

  
  

### 00:37:13

  

Michael Moores: see if you've got any other concerns there. It's sort of just generic data storage and showing how DT feeds in basically um obly the raw we need that very quickly and then the curated sort of

George Westbrook: Hey.

Michael Moores: a little bit later you know 15 minutes or so we can have a short refresh. I know in one of the super designs we discussed about real time sort of transactional monitoring as well they brought up. So I don't think that's feasible or we did think we probably go for a web hook method there or something like rather than database queries because you know the hot storage is is is very expensive. So I think there decision made there sort of go towards a colder storage then archive some of the stuff off. So obviously a lot of the stuff we'll do is re you know current if you're looking for a transaction you're probably looking at 30 to 60 days from a card holder or you know client

George Westbrook: H.

Michael Moores: perspective. Um so obviously we need to understand when do we put that into archive coal storage and then I said to him this morning it also depends on the type of information.

  
  

### 00:38:14

  

Michael Moores: So transaction you'll probably use more often but reference data that doesn't get updated might be queried you know once a month whatever. So I think it will change based on that type of data as well. So we're still working out the the levels but basically that's where we are so far.

Brett StClair: What do they expect from a transaction point of view per month to be stored in this database? Like it's large,

Michael Moores: Uh yeah.

Brett StClair: right? I mean, it's ridiculously large.

Michael Moores: So I've not seen how they're they're building it specifically, but from Marqueta,

George Westbrook: Cool.

Michael Moores: we had one table. We had that translog that was one entry per transaction. Some of our customers doing a million plus a month easily.

Brett StClair: Thank

Michael Moores: Uh yeah, that hammered.

Brett StClair: you.

Michael Moores: Obviously, we've got our production database that it'll go to first and then we'll have a stream going there. But yeah, so essentially we had a trans log entry which is the basic information then this is probably not the best way of doing it.

  
  

### 00:39:10

  

Michael Moores: But they had a TR cache which they just dumped the JSON for the rest of it which made quering very very difficult. So we obviously want to optimize that as much as possible but yeah basically these were sort of 30 columns 40 columns wide tables with you know millions and millions of rows in it. Um so obviously we well we couldn't even query the production database due to the size of them. So we all did all of our stuff in the database.

Brett StClair: Yeah. And the card transaction record is a fairly standard record.

Michael Moores: No.

Brett StClair: I'm assuming like internationally it's like a call data record in mobile

Michael Moores: Uh yeah.

Brett StClair: terms.

Michael Moores: So the way it comes in it does obviously visual master send it in ISO format which is like field one is this which no one likes to read.

Brett StClair: Yeah.

Michael Moores: So what we did at mark and what we're doing here is we'll we'll transport that into in a JSON payload. So structure JSON payload. So you know that field one is is X and it's always that.

  
  

### 00:40:04

  

Michael Moores: So that will always be like structure payload that's you know a decent sort of 40 plus sort of fields in there that that can grow based on you know what we need to give them. So we obviously need to pass a lot of data on to them to make a decision. So everything that comes into us is sort of numerical. So a card input method is 01 that might mean

Brett StClair: Okay, got it

Michael Moores: transport everything into basic English language.

Brett StClair: now.

Michael Moores: So even if you don't have that ISO understanding, we have that layer to flip that into JSON. And obviously we built those JSON models as well um to support that

Brett StClair: Okay. Interesting. I just found it really interesting.

Michael Moores: basically.

Brett StClair: My background is telco and then my banking background is at sea level. So I didn't really get my hands dirty.

Michael Moores: Yeah, it's very I know are different as well, which is even better. So some fields are there, some fields aren't.

Brett StClair: Oh.

  
  

### 00:40:59

  

Michael Moores: because there's no there's no standardization really standardizes the format but the inputs and the values they put in there are just all different so um you know we when I was at Marqueta we had someone very amazed at Mastercard that we could match

Brett StClair: Oh.

Michael Moores: 98% plus they expected between authorization and clearing they expect about 60%. Um, so even they don't believe they can match it together. Uh, just because merchants do basically whatever they want to do and they just throw random rubbish at

Brett StClair: Yeah.

Michael Moores: you and they don't stop it and we we have to do all the cleaning and the and the

George Westbrook: Very

Brett StClair: I mean,

Michael Moores: stuff.

Brett StClair: if they just get it right, right right from source, right? Imagine how awesome the world would be.

George Westbrook: nice.

Michael Moores: Yeah.

Brett StClair: All the cool things you could do.

Michael Moores: But then those companies like I think it's stone stone drop they

Brett StClair: No.

Michael Moores: literally make their money on just enhancing the poor visa data and that's all they do they

  
  

### 00:41:52

  

Brett StClair: Huh?

Michael Moores: just yeah it's m it is really beneficial obviously we're hoping with this we can improve it somewhat because I said they just do that and you know we looked originally at marketplace actually connected these tools but it' be much better if you had the central core that could improve that data over time obviously with AI and stuff like that. So I think that's much later but that's a sort of idea of where we obviously the

Brett StClair: Very

Michael Moores: matching then we had very strict matching at Marqueta which is pretty good.

Brett StClair: cool.

Michael Moores: Uh we found a nice combination over you know many many years doing that with AI you could just swap that tomorrow so it's I think that's the benefit so they have those strict rules have those core rules if it fails find any matching data and then and iterate basically. So I think that's some exciting things we can do in the in the future as

Brett StClair: Very nice. Thank you for that.

Michael Moores: well.

Brett StClair: Um, I'm going to whip through these.

  
  

### 00:42:56

  

Brett StClair: Some are not making sense to me. product config size, 200 fields, 50 to 60 properties, two figures from two calls. What the f*** is it talking about? Don't

George Westbrook: I think when we were I can't remember the context of what it was

Brett StClair: know.

George Westbrook: but maybe it was a transaction.

Michael Moores: I think for the or I can answer this anywhere the product come with size. So I think we don't we don't know the true size with right now we're looking at that we've proposed some stuff but essentially it's big um complex configuration is is the point and it's going to grow. So when we're configuring this, we need to make it simpler. Obviously, I think I mentioned that yes, it might have X properties, but let's say address verification has seven. You don't need to fill those seven in unless you turn that on. So I think that's the point discussed that when we build the AI,

Brett StClair: Yes, I remember.

Michael Moores: we just need to make sure like okay, you've turned on address verification, what do you want?

  
  

### 00:43:56

  

Michael Moores: So talk about the functionality and the feature rather than individual properties. I think that's the thing because I will know the properties but unless you read the documentation in depth and and study that you're not going to know. So I think that's the concern there is that the product size can can be large.

Brett StClair: Happy coffee.

Michael Moores: We need a very clear and the thing in there as well nothing is mandatory per se like you can turn anything you want on in our platform whenever it might be wrong for you because you're doing the wrong type of program. Our our platform is purposely flexible. you can do whatever you want, but that does unfortunately mean some clients can turn stuff on they don't understand and and and ultimately break stuff or they don't turn stuff on that there's a compliance and a reason for in Europe or whatever. So, we have to because the API is so flexible, we have to push that guidance into the AI into the console to say, you know, you're in the United Kingdom, you're going to need these four things.

  
  

### 00:44:52

  

Michael Moores: Uh we recommend this strongly that sort of push the recommendations. So ultimately we we are the knowledge, we are the experts, but ultimately it's their um regulation, their compliance, they're liable. So we can only really say you probably should do this. It's ultimately up to them what they do. There's sort of dis dispensations and exceptions for all sorts of stuff. So we don't want to get into doing that. We just say, you know, if you turn this on, you need to do these things typically and then just sort of provide that guidance on the product basically rather than having a very very strict you must do this because with us being a global platform like say address verification that's mandatory in the UK. It's not really anywhere else. So you can't really build a system that makes it mandatory versus not. This is why we have that product basically so you can configure it and stuff like that.

Brett StClair: Yeah.

Michael Moores: Our hope is that over the course of as we grow the AI will understand okay these type of people do this configuration and start bucketing those people because realistically think I mentioned that all the apps are basically the same in the back end whatever mobile banking app you have they're all pretty much doing the same thing in in the back end at txn so with a a few small configuration tweaks basically to make that sort of experience unique for them so we can look at those sort of verticals and say okay you are in buy now I'll pay later you are in credit debit and

  
  

### 00:46:17

  

Michael Moores: go okay then the AI goes right typically people in your situation normally do

Brett StClair: What?

Michael Moores: this and we have an actual rather than just our knowledge that may shift over time with the industry it's actually evolving knowledge based on who we have and what they have configured because that changes daily as well so building that sort of corpus up and the knowledge to say this is what you probably will most likely end up doing because 95% of you, your type of people do

Brett StClair: Nice. I'm glad it's picked up that um we've rebranded from Teraflow to LLM to Nova Sapion. What that's saying? Thank you. Thank you AI for picking that up.

Dorte Dye: We still call you Teraflow though. I don't know. It's still in my head and I can't spell your name

Brett StClair: I know I catch myself doing it.

Dorte Dye: but

Brett StClair: Um, okay. Point four system defi defined alert corpus. Uh, which alerts TXN is obliged to raise catalog undefined. I think it's still undefined, right?

  
  

### 00:47:22

  

Brett StClair: We we're going to leave that one open because there's a lot there,

Michael Moores: Yeah.

Brett StClair: right?

Michael Moores: Yeah. I think it's very we're trying to push on this a lot. We don't know the login. We don't I'm still trying to get in to see the data that's being logged in the back end. So of our UAT I'm looking at logs the data stored make sure firstly I can support it but secondly looking at what we can actually system define it obviously the we know the core transaction declines being the big one like that's really important if it goes up um obviously infrastructure level stuff which I think we will as we discussed we'll have sort of normal sort of logging based on that as well to say this threshold was hit um with the issues we have on access with DT stuff we're looking like a central logging you know data do type thing now um as well as the data link we'll have those two things so scoping that out is where that will be and then we we'll know a bit more what that can do uh basically so that's still

  
  

### 00:48:21

  

Brett StClair: It's made an assumption here and it does this occasionally.

Michael Moores: underway

Brett StClair: We try to catch them, but I think it slipped through. AI layer P2 residency redaction may card holder P2 appear in chat logs.

George Westbrook: PI personal

Brett StClair: Oh, is it PII? f****** hell.

George Westbrook: identifier.

Brett StClair: Um, do we want them appearing in chat logs? I think that's fine,

Michael Moores: Yeah.

Brett StClair: right? Because it's all locked down and internal. Be secure. I don't see why. I think they're just calling it

George Westbrook: I I think it's it's more for the obviously at

Brett StClair: out.

George Westbrook: every turn we are sending that to the LLM provider. However, we're going to be using either let's say Gemini through Vert.ex X AI or the the Gemini API um which it's it's safe there or if we go open AI using either directly the Open AI um API or the Azure serving of it um or if it's clawed maybe AWS or um Gemini again is I suppose it's just dependent on what what provider we use but I mean 80 yeah it's the the these

  
  

### 00:49:39

  

Brett StClair: All of it's secure at least. Yeah.

George Westbrook: were issues that were had like in first year of um in the first year of all these providers really switching on their APIs. So it's it's pretty good now. Um but it's a decision may maybe because obviously it's a financial product um we might need we might need to look at that and see what see what the standards are, see what the risks are. Um

Michael Moores: Yeah, I think from obviously our side they well firstly we always try to limit PII where possible.

George Westbrook: Yeah.

Michael Moores: So if you don't need to send it we try and not do that. Um secondly we like logs like audit logs we probably would redact that from. So any logging that is just in clear text or whatever, it's just easier to to keep your logging and your stuff sort of clear and keep that in data. Obviously the in the European Union in the Europe, we have to basically ensure that data stays in Europe.

Brett StClair: What's

Michael Moores: So we just need to be conscious of where that data is going,

  
  

### 00:50:38

  

Brett StClair: that?

Michael Moores: where it's being stored in transit, it's absolutely fine. It's the being stored at rest is the concern and stuff like that. So, whoever we use, you just need to make sure we have that uh you know, if it's a third party, just make sure we we have that acknowledgement. We understand where it's being stored as well. So, it's defensible if we do that. But I think yeah, it's a good uh call out.

Brett StClair: Perfect. User defined optimization metric. Should the user set an objective the agent optimizes towards and suggests more?

George Westbrook: I don't really think that's too relevant because the user question is the objective like what whatever they're trying to achieve is I think is maybe I think for maybe longer longer horizon tasks is where the agent just creates a checklist or a task list which which I think we're going to do we're going to do anyway. Um it's yeah I suppose it's just when the when the agent receives a request or goes into a kind of more discovery what do you want to do Mr. user or Mrs. user um assessing the complexity of that so that it's not the objective is set in message one and by message 20 it's losing it.

  
  

### 00:52:07

  

George Westbrook: But by by now it's it's pretty good even that if it was in message one it's still going to remember it. Um.

Brett StClair: CRM are we comfortable with that?

George Westbrook: Um.

Brett StClair: Right. I agree with you. It's defined based on what the interaction is and it's what the goal of the end user is. You know, let's set it there. Um CRM versus console data split. which client data lives in the CRM versus needed in the console and how much

George Westbrook: I mean,

Brett StClair: they

George Westbrook: I suppose for everything that's in the console that's going to

Brett StClair: sync.

George Westbrook: be stored in the pardon me, the it's going to be stored in normal database. And I think it was only really when we were talking about the customer on boarding and pre-sales that there would be that data that lives in the in the

Michael Moores: Yeah, I think we well stopped as we got to this point yesterday.

George Westbrook: CRM.

Michael Moores: So obviously as we move the statement of work and they actually sign the contract um I'll talk about MVP.

  
  

### 00:53:14

  

Michael Moores: So basically that's the handoff point. So future state CRM triggers a client build in the console. I don't have to do anything. So it's a it's a good split between CRM ends technical build starts because it's quite a nice thing. So the technical build does capture the client information but only name email addresses. That that's the sort of limitation it does. It's not doing a full sort of sync or anything like that. It's just for the purpose of grouping and permissions later on. So I will go in I'll create the client and I'll create the program underneath it. I say ideally all that information will come straight from the CRM in the future and the bill just get will just get done and we'll come back there's many many manual steps for now but yeah it's very much split quite nicely that CRM will do all the the salesy businesses stuff um capture that information you know the projections that they're going to hit all that sort of stuff for the sales team and then at the point the contract signed or whatever trigger we go for triggering the UAT UAT and the production environment the system will just hopefully automatically build that um or at least trigger for now trigger to me to say build that and confirm to the client.

  
  

### 00:54:21

  

Michael Moores: Yeah.

Brett StClair: Then what I'm about to say will probably ruin our lives forever, but the co-pilot will now be called Dot.

Dorte Dye: It's fine. No one can pronounce your pronounce my name anyway.

George Westbrook: It's

Brett StClair: Anyway,

Dorte Dye: Like get nothing done.

George Westbrook: okay.

Brett StClair: what AI does is it goes really okay.

Dorte Dye: Can I know? Can you imagine? It's like you ask me it's like and you can't pronounce my name and it doesn't do anything because this is when I'm talking in the car in German because Google doesn't while it does it in

Brett StClair: Yeah, Ruby.

Dorte Dye: Germany it I don't know what I still haven't figured it out two languages the pronunciation is just like whatever let's try that one that would be hilarious

Brett StClair: So,

Dorte Dye: is

Brett StClair: we call our agent Jarvis and Nova. Actually, no, we've shifted it to Nova. Sorry, that's right. We've got Nova.

George Westbrook: Yeah.

Brett StClair: Nova.

Dorte Dye: our uh Google thingy is called Javas as well.

Brett StClair: Nova.

  
  

### 00:55:24

  

Dorte Dye: We have all fancy names. It's like we have Etka the Hoover, we have Larry the Malone.

Brett StClair: I love Larry Little.

Dorte Dye: Yeah, we couldn't come up with something more funny. Don't know. I like

Brett StClair: What? So you guys have a think about a name.

Dorte Dye: that.

Brett StClair: It's the fun part of this I guess. So AI, we're just kidding about name. It has yet to be decided.

George Westbrook: Terry the TXN assistant or

Dorte Dye: You know,

Brett StClair: Only the TF

George Westbrook: Tony.

Dorte Dye: this is the part when you really want to piss Ian off. Can we ask him on the call is that he doesn't give three cents for their

George Westbrook: Maybe maybe what we do for the next call we put it in we do a twohour twohour slot and just call it

Michael Moores: What?

Dorte Dye: work.

George Westbrook: agent naming call.

Dorte Dye: I think you can brew your coffee on your own now.

Brett StClair: Um, okay. It's 11 o'clock. What I'm going to suggest is I'm going to send you guys this.

  
  

### 00:56:26

  

Brett StClair: If you just want to send us a voice note and we'll ingest the voice notes. Um, we'll make a first hit. So, George and I will quickly walk through and see if there's anything we can answer very quickly. Um, and then we'll just republish it with all the work that we've just done now and then we'll send it to you guys. If you can give it a quick once over, even though like literally a voice note on a WhatsApp would be perfect. We'll ingest that and then load it in. Um, we're about halfway through there. Now there's a fair amount of this stuff but I think this is more taking note of design things where we say ah this is probably a design consideration. Um I think we've got one more. Hey we

Dorte Dye: Uh, no, we just have to review the playback tomorrow.

Brett StClair: done.

Dorte Dye: Um,

Brett StClair: Yes.

Dorte Dye: next week. So, you wanted to pull everything together, but I'm just conscious. I haven't logged into the portal anymore or commented on anything.

  
  

### 00:57:24

  

Brett StClair: Yes.

Dorte Dye: I'm not sure how Mike is getting on. I think that's the most important part, right? That we just double check everything what's in there that we're happy with it before you crunch and come back with. Um this is what we hear, this is what we see, this is what we propose and then let's strip out for the different phases.

Brett StClair: Okay.

Dorte Dye: Mike, do you think you you have some benders to comment on it this week or should we push this a bit out or that means I have to

Michael Moores: Yeah, I can find some time. Yeah.

Dorte Dye: work on my day off?

Michael Moores: Uh yeah,

Dorte Dye: I was counting on

Michael Moores: I'll take a look today.

Dorte Dye: you.

Michael Moores: I'm just doing the testing at the moment. So, um that's killing me at the moment, but yeah,

Brett StClair: I mean,

Michael Moores: not too bad.

George Westbrook: That's my favorite

Brett StClair: if you need to push out a couple of days, it's not a problem,

George Westbrook: part.

  
  

### 00:58:16

  

Brett StClair: right? It's it's there's a fair amount.

Dorte Dye: It really depends how long you need. Last time you said you needed less than a day to put all of that stuff together.

Brett StClair: Yeah.

Dorte Dye: So if we have the meeting actually next Wednesday, I believe if we have commented by Monday, you should be in a good position. Mr.

Brett StClair: Yeah. Yeah.

Dorte Dye: D.

Brett StClair: will

Dorte Dye: Okay,

Brett StClair: be

Dorte Dye: then. Yeah, I I will um make some time to to look at it as well. I mean, there was probably not as much comments for me than for Mike, but it's crazy what it has all pulled together, how automated it is. It's like you both you and Mike are on the same level with getting really the geeky stuff out here, how it all built together.

Brett StClair: Yeah. Thursday morning. By the way, we we're doing the

Dorte Dye: Okay. So, fine. If we have something over to you by Tuesday at the latest,

Brett StClair: Yeah.

Dorte Dye: then you have a good day to pull the rest out.

Michael Moores: Awesome.

Dorte Dye: Sounds good.

George Westbrook: Perfect.

Brett StClair: Perfect.

Dorte Dye: Okie do.

Brett StClair: Awesome guys.

Dorte Dye: Speak to you shortly then.

Brett StClair: Thank you for your

George Westbrook: Sweet.

Brett StClair: time.

Dorte Dye: Okay.

George Westbrook: Have a good rest of your week.

Michael Moores: Sh.

Dorte Dye: In the rain. Bye.

George Westbrook: We're in England.

Dorte Dye: English summer, right? Con.

George Westbrook: Yeah.

Dorte Dye: I'm already depressed. I don't for that. Okay.

Brett StClair: What the hell?

Dorte Dye: Speak soon. Bye.

George Westbrook: Make him drive.

Brett StClair: Bye.

  
  

### Transcription ended after 01:01:07

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

**