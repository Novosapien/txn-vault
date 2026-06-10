**

Jun 10, 2026

## Component 6 - developer-support - Transcript

### 00:01:08

  

Brett StClair: Oh,

Ian Johnson: Hello. How you doing?

Brett StClair: very well. And you caught between

Ian Johnson: Not bad. Braving the outdoors.

Brett StClair: him.

Ian Johnson: Braving the

Brett StClair: I uh I'm undercover.

Ian Johnson: outdoors.

Brett StClair: I got caught between the offices and a and a client meeting. I'm not going to make it. coffee

Ian Johnson: No problem.

Brett StClair: shop.

Ian Johnson: No problem. How you doing,

Michael Moores: Yeah,

Ian Johnson: Mike?

Michael Moores: yourselves. It's a busy morning this morning, so apologies for being a bit late.

Ian Johnson: They're all busy, aren't they?

Michael Moores: back toback calls in 7:30 this morning.

Ian Johnson: since

Michael Moores: So that's been fun.

Brett StClair: Oh my goodness.

Michael Moores: Yeah,

Ian Johnson: 7:30

Michael Moores: DT dropped one in their daily meeting this morning. So now it was good though. Data lake hour and a half call. So they've come a full presentation of how to do it.

Ian Johnson: and

Michael Moores: So yeah,

Ian Johnson: happy.

Michael Moores: I've got a few things I want to send to Brett and the team just to make sure the AI bits align.

  
  

### 00:02:10

  

Michael Moores: So I'll send that after this meeting. But yeah, it's good so far.

Ian Johnson: Wow. That's not very often that that's a summary of a meeting that you have like

Michael Moores: No, no, it's good. There's obviously very early thinking making sure we cover everybody needs and stuff like that. So, um, just make sure all line, but I was relatively happy.

Ian Johnson: Cool.

Michael Moores: There's some stuff I just need to make sure vectors and all sorts to be AI based and make sure we have enough context in that side as well to do what you need to do. So, I'll send some summaries across after.

Ian Johnson: Good stuff. Hey J,

Dorte Dye: Hi.

Ian Johnson: how are you?

Dorte Dye: All

Ian Johnson: Morning,

Dorte Dye: right.

Ian Johnson: son.

Hasan Mohammed Ahmed: Hello. Good morning. How are you doing?

Ian Johnson: All right. Thank

Dorte Dye: What's happened to George? Is he stuck in a lift

Ian Johnson: you.

Brett StClair: I saw a message and saying, "Please,

  
  

### 00:03:04

  

Dorte Dye: again?

Brett StClair: will someone have a a flat white with an extra shot of coffee on my desk before I get there.

Ian Johnson: Okay. Excellent.

Brett StClair: Like, okay. And no one's in the office, George. So, I have a feeling he's trying to squeeze a quick dose of caffeine on

Dorte Dye: priorities.

Brett StClair: while running to the office. Um, and because I don't think Max is in. I'm not in here at home. Okay. So, let me just pull up where we are. So, I'm feeling that the developer support landed pretty well. By the way, it's feeling quite good. Um, how are you guys feeling about it? I kind of ran out of time and didn't quite get to a conclusion, but I felt right.

Michael Moores: Yeah, the front.

Ian Johnson: There was just there was just a couple of things that I thought of after um I agree I think it was a good session but they're just questions for me really. So the the documentation where will the documentation be hosted that the AI will interrogate to answer any questions?

  
  

### 00:04:50

  

Ian Johnson: So I mean I know we haven't got the the kind of architecture everything sorted out yet but you know my assumption is that it's hosted in an AI friendly way somewhere rather than the documents as they stand Mike in terms of what would be published on uh in the um knowledge hub. So there's that I was trying to understand that and then the other thing that we talked about um was the

Brett StClair: Yes.

Ian Johnson: whole MCP server whether local or hosted and we all agreed hosted um but from memory super ultra design Mike they were designing I can't remember the terminology they used um for the file that basically somebody could just go and download um and then just to can you know use that for their own AI. So I just wanted to make sure that you know firstly just from my understanding where will this where will the document documentation be hosted and secondly are we still pursuing that route of having a kind of AI ready uh document set somebody can just go in and say you know download or or whatever that they're

  
  

### 00:06:10

  

Michael Moores: Yeah, I think so documentation obly will be stored in two places.

Ian Johnson: Okay.

Michael Moores: Um, DT YAML being the the source of the code. So that'll be the one there. So that's available to the AI, same API that anyone would use on the portal. The rest of the documentation, the guides and stuff and the change log will be hosted in Umbrau which obviously has an API to get access to that as well. So we'll probably need to discuss it the how you want to get hold of that assume the AI will obviously learn from that as well. So you know there'll be some sort of reading of that whether it scrapes or actually reads the API. um I need to see the structure of that API to understand exactly how it will pull the documents into the AI but essentially it'll have access to that on broker's side the pulling same way that the document or the dev portal sort of renders it basically so all that information is API ready that the AI can pull in uh which hopefully should be a read nice read format for them um but yeah the the super ultra did design like an LLM slash sort of a knowledge document for the agent it's not gone any further than the design that they suggested.

  
  

### 00:07:16

  

Michael Moores: So I think that's something we we do need to discuss. I think their design was a little less than an MCP. So we're more this is what you're doing. This isn't everything you need to understand. So maybe it's a good, you know, halfway point that we can have some sort of readymade documentation that that we can have. But I think for the MCP do this, do that type behavior. I think the hosted seems better for that. Um obviously we're more in control but there may be a solution whereby we can just have this is TXN this is the endpoints that you have you know generic documentation help that they may want to pull in on a you know release live release basis. So that's the sort of file I think super ultra designed for us. We just need to talk about in theory how that will work. I don't think we've picked that up at the moment and again who who's going to do that. So is it um AI or you know stat works did say something they could build from a basic understanding sort of point because they obviously have the data of the the portal and all that they can actually pull that together or if we think it's better for AI to generate that so that base layer file

  
  

### 00:08:21

  

Michael Moores: basically so that's something that's good point we haven't covered that so

George Westbrook: How how static is the documentation going to be? Like what how many how many changes is it? Is it going to be weekly, monthly, or every like three months, do you reckon?

Michael Moores: Um so the YAML itself will obviously be every release which I vis every month would be that sort of change there. So the portal will pull that from there. The guides and stuff you know we we don't want to put anything that's going to go stale in there from our side. So all the reference to the code will be a link to the API reference basically.

George Westbrook: Yeah.

Michael Moores: So it's only going to be sort of business and procedural and general guidance. So I don't foresee us changing that a lot. Obviously if we add new functionality that we want to do a good overview then we may do a new page of that.

George Westbrook: Huh?

Michael Moores: But yeah it's going to be as and when we develop functionality it's not something we're going to keep sort of iterating on.

  
  

### 00:09:15

  

Michael Moores: Obviously the only caveat to that will be the AI side. Obviously, we we do want to pick up questions that aren't being answered that we could potentially put into the documentation. So, I guess it depends on the frequency of that as when it spots, you know, things that could happen. So basically this whole sort of learning approach whereby the first line of defense should be the documentation and then the AI and then obviously myself but then that whole sort of loop if the AI can't answer something you know my support answers go back into the AI and similarly it goes back into the documentation. So we have that full loop because one of the the worst things that I saw is obviously you're answering questions but you might do the same question the

George Westbrook: H.

Michael Moores: next day. There's obviously a gap in the documentation and it'd be good to sort of spot those from, you know, that side of it as well. Um, yeah, there's not sort of regular changes we would do. I think we need to sort of map out the documentation specifically.

  
  

### 00:10:08

  

Michael Moores: It's all under our control from the Umbrau editor. We're going to have those base ones. This is what a card is. This is what a card holder is. You know, they're fundamentally not going to change. It's the only if you add some species on European or anything, you know, the really detailed stuff we may decide to add in there. the rest will leave for the code in the API reference to the specific this field that field. We don't want any of that in the guys. It's more what TXM does. This is how you're probably going to build your program. Some stuff that sort of stays true, if you will, regardless of the code um as

George Westbrook: Yeah,

Ian Johnson: Yeah,

George Westbrook: cuz I should try going

Michael Moores: well.

Ian Johnson: go on. No, no. I was just going to say because in my mind with it, Mike, was this thing of um as you say about the AI, you know, when when we get queries that are raised and it's about specific areas of the documentation, um you know, in my mind that was okay.

  
  

### 00:11:07

  

Ian Johnson: So if something gets raised then typically what what happens is somebody like yourself Mike or a content writer basically changes the the guide um let's just stick to the guides rather than the the text stuff but in reality wouldn't we want the AI to propose to somebody to approve some change to the documentation that I I think we'd have to have an approval cycle otherwise it's just putting whatever it feels like up there. We know that that's risky. But again, I'm just trying to think how we stop stop you having to do any of that work or some a human having to do that work because ultimately if it's the same thing over and over again um then that it's an opportunity to propose those changes and then I suppose and I'm just thinking about the very basic stuff that I've set up on the go to market um stuff in Claude where you know it can basically edit the document and I mean I haven't given it um anything outside of read access so it say it it basically gives it to me for me to then upload into the relevant file and replace the old one but I'm assuming that it could just read right directly to the to the document I'm just I just want us not to miss those little things that might not seem like very big things but it's just It could take some work off your plate

  
  

### 00:12:41

  

Michael Moores: Yeah, I think that's why we we put these requirements in the Umbraco or the content management system

Ian Johnson: really.

Michael Moores: requirements to have that ability to edit update via API. So we do have that ability that it's not just the editor, we can have the AI push stuff into the API in draft mode, you know, where someone can approve that as well. So you based on the requirements we asked for obviously Umbra looks to meet that bill but you know with the API we should be able to sort of manipulate that data as well wherever we're from where we do it from the console the API what you know whatever um so that should be there for us to do that and then yes to your point we probably want to go in there and prove before it goes live but at least we can have a load of draft versions on that basically to say this is what we're looking at and obviously as you've seen in the sort of testing the Umbra has an editor as well so we go and actually see how it looks before pushing that out as well.

  
  

### 00:13:32

  

Michael Moores: So the umbra side for AI team they have sort of components in there not just text it's bit more like design things as well. So that's a sort of bit more than just a a basic text basically but we have design specific components that we want on our documentation from tables to you know card type things as well. So, um, that all renders inside the Umbrau portal and obviously we then publish that out to the the death portal site basically.

George Westbrook: One one thing I was thinking in terms of that those updates say with the with the chat feature on the developer portal is analyzing each chat. So I go in, I'm a developer, I ask a question. Um I have a conversation, maybe we uncover something that's clear. Two options could be the first one being a bit more let's say traditional. Um but is after every chat or where it concludes having a how did you rank this out of 1 to 10. I don't think that's the best option, but but it is an option. Um the second being every time there's a session that ends the AI analyzes that performance um tries to analyze the user sentiment of the questions um and then also assesses how well it actually answered that then tries to work out is it a if it couldn't answer it correctly um was it user question wasn't um wasn't good enough um or wasn't detailed enough or was it the actual information behind it wasn't good enough.

  
  

### 00:15:10

  

George Westbrook: Um, and in in that situation, it's either going to be, let's say it was the user question wasn't good enough. Um, that's an agent issue. So, the agent then needs to have its prompt optimized so that if there is an unclear question, it asks the user more details in order to get it. But obviously more important for this conversation is if it was a documentation issue and the agent didn't actually have the answer, maybe it needs to be right need to improve the the agent knowledge base because there could be a situation where maybe we have this might not sound the best idea but it might make sense like divergent copies of the documentation. So an agent version and then a user a userfacing version. So obviously the userfacing version needs to be tight, concise, to the point with enough detail for them to be able to understand it but not being overwhelming. Whereas obviously with an agent it might need a bit more fleshing out. Um we might find that they can it can be exactly the same.

  
  

### 00:16:11

  

George Westbrook: Um and and that's fine. Um but with it with it understanding where was that issue maybe then we can go okay well we need to provide more information around this or this section in the documentation isn't too clear. So maybe we need to improve this part and rather than it being an automatic update, maybe there's a time in the future where we we trust it enough and it's I suppose the trust principles that that we always talk about and but obviously initi initially it is that validation step. So maybe for every single chat we're analyzing it. We're saying right there's a gap here, there's a gap there. We need to update the prompt. We need to update the documentation here for the user version. We need to update the agent version here. Um, and then it goes into kind of like a um, what I'd probably suggest is maybe it's every every day or every week. There's a cron job for lack of a better term. Um, that's collecting all of the support queries, analyzing all of them.

  
  

### 00:17:10

  

George Westbrook: So, you're not having to go through every single chat and look at the feedback for that. the AI is going to analyze all of them and then present you like a consolidated report with maybe suggestions and snippets for what to actually add in. Um, and then it's first step might be you go in and you make those updates or like we've been saying with I think like the alerts you the agent actually goes in and updates it because obviously I'd be very surprised if the agent wouldn't wouldn't be able to access in Braco. Um, I haven't I haven't looked into it, but I'd assume there's going to be some sort of API it's going to be able to access. Um, and then yeah, that approval step and the levels. So, first, here you go. Here's what you need to update. Second, um, here's what I think we should update. Do you want me to do it? And third, which might be a bit off, is it just is continually updating.

Ian Johnson: Yeah, there's a there's a I think all of that makes sense.

  
  

### 00:18:08

  

Ian Johnson: The one thing I was just going going to say is um if I think about day zero where nobody has used the knowledge hub. So the you you're the first person on you ask the first question. Um for me, yes, all this learning and based on real life experience is exactly what we should be doing, but I also think that we need to consider the agent teaching itself ahead of launch as we asked the agent based on the documentation to create a raft of potential questions that would come um and then to answer those questions so that we get into this loop and and we do two things. We do one where the the question is exactly as the agent would like it to be. So it's got the full context that we need because then once that's done I think you can then you one of the steps you talked about George is the agent being able to understand the nature of the query and ask for the information that's needed to make sure it can be accurate. The other thing that I was thinking we could do might we talked about this ages ago is have some quite ambiguous almost test questions.

  
  

### 00:19:36

  

Ian Johnson: So you ask the agent to to basically write questions that doesn't contain all of the

George Westbrook: Yeah.

Ian Johnson: context. I don't know if it can do it. I'm assuming it can. And then you and then you run the thing.

George Westbrook: Yeah.

Ian Johnson: So it's learning. We're learning before the thing goes live.

George Westbrook: Yeah.

Ian Johnson: So it sense of what might land so that when they do land, we're not at day zero

George Westbrook: Yeah. So I think yeah what we could do there is we could create diff 20 different

Ian Johnson: effectively.

George Westbrook: personas or let's let's say developer personas um with varying degrees of um proficiency and different backgrounds and then what we do with all like multi-phase workflow all in the background. They'll be like, "Right, you are a junior developer for a mid-level bank. Um, and this this is like your personality or whatsoever." Your first task is to go and look through the documentation. This is what you're trying to build. This is what you're trying to implement.

  
  

### 00:20:36

  

George Westbrook: Um, see if you can answer all the questions that you need from looking at the documentation. Um, so then that's the kind of first step. Is the documentation provided enough? If it's not then it will speak to its next job will be let me speak to the support agent and have a conversation um like a normal user would um and then do that roll out where it's like hey Mr. agent um how do you do XYZ? Um then it will go through that chat and then we'll do that hundreds if not thousands of times and then collect that like sample data set which we can use initially run that maybe every day for a couple of weeks and it's going to dramatically dramatically improve it. Um and then also have that in we can have that going periodically live as well. So we've got the like simulated um simulated testing the real usage and then using both of them to inform what the update should be. Obviously as time goes on and users pick up maybe the simulations become less relevant but then actually know I'd argue all that that would do with the real data is give us the ability to improve the actual um personas that we have.

  
  

### 00:21:55

  

Ian Johnson: Yeah, I I think I think it's something we should definitely think about how we implement because otherwise the whole thing can fall flat on it. I mean it's two things we need. We need customers and we need users but we need and users generally speaking for the health of the business. Um but we also need to hit the ground running with a with a good experience. And I mean I I can't remember the last time I looked at the Marquetta one, but I asked the Marquetta one something. I wasn't trying to catch it out like a pretty basic question and it was it was crap uh to put no and that and from the minute I I read it just turns you off the whole thing. There's no reason with the technology that we can't to your point be miles ahead of the curve when it comes to it. Doesn't mean that we'll that we'll have we'll pick everything. we'll have done everything before we hit the kind of hit the market, but at least we'll be in a much better position and it'll be a better experience.

  
  

### 00:22:56

  

Ian Johnson: Um I think I think one I think I asked the Marqueta thing and it says I'm sorry I can't help you read read the documentation. I was like brilliant. Um we obviously I know we won't do that but we but anything we can do in advance to really think about and then to your point keeping that going as just a recurring thing that we do just so that we're already always trying to make it as intelligent as possible. what you know one of one of the and I don't know if it lands but the whole one of the kind of website strap lines that's being considered is intelligence built in complexity taken out the overall TX and experience so it better be intelligent and it better complexity otherwise uh will have fallen foul at the first hurdle and it has to do that from day

George Westbrook: Hey.

Ian Johnson: one so

George Westbrook: Yeah. Yeah.

Michael Moores: Yeah, I think from from that as well,

George Westbrook: Yeah.

Michael Moores: I think we just need to be cautious about the way our clients sort of work.

  
  

### 00:24:02

  

Michael Moores: They can be sort of not contradicting per se, but almost quite different in how they build to our API. So what might be true for one might not be true the other. So we do need to look at sort of trends and themes rather than just otherwise we're editing the documentation to be right for that one client. So you know the core is obviously pretty straightforward. The car does this but there may be different reason you use a spend control versus something else and you know debit credit travel whatever you're doing. There's a lot of different variants inside here. Um, so we just need to make sure that it is like a actual trend before we raise it rather than a one-off thing as well. So I think that's important to add in. And I think we just need to think about how we say potentially surface these to us. There's a lot of talk now that we've had about the agent, you know, alerting us about stuff. You know, where where is that going to be stored for us to action as well?

  
  

### 00:24:54

  

Michael Moores: So obviously Umbra is one. I know we've discussed about alerting and stuff like that. I think obviously from a a TXN side, we use the console a lot. So we just need to have a think about where potentially some of these things can be you know raised to us to thenction then you know whether we put it all in the console and say okay documentation yes I'm happy with that version then it updates from brocker and someone goes in there to publish or we just need to think about that I think from the txn side as well where we want it I think the console feels the right place for for most of it especially for the alerts and stuff like that but we haven't really scrubbed the full like admin piece for the console so we just take that into consideration that you maybe that we have a separate AI interface that we we do this or I don't know what the best approach is but I just don't want to over complicate the console obviously that will have some stuff in there in terms of you know the client alerts and stuff we discussed anyway you know what if we sort of completely separate that and have an AI interface where we can manage that or do we want to incorporate that into the console and stuff like that it's just considerations we need to think about because obviously that will alter the design

  
  

### 00:25:59

  

Michael Moores: of potentially the console if we do leave in there

Ian Johnson: I I think I've been thinking about this as well, Mike, because and I think we just got to think about how we will work

Michael Moores: basically.

Ian Johnson: to your point. How will we work? And like all the stuff that I've read is my my view on it was our customers are going to access whatever the claude like experience is. Um, and it would seem logical that that's where we accessed as users to get that type of information because then you can build whatever you like, Mike, as far as I can tell. I mean, you could build within your own claude instance to receive that information from our agent and build your own dashboard that's that's just refreshes consistently. I mean, that's the difference, isn't it? I would caution against building any more software into something like the console to manage things that are coming that are AI driven because it just seems to be it doesn't seem to be the most efficient way of going about doing stuff in my opinion.

  
  

### 00:27:11

  

Michael Moores: Yeah, I think as well the way we work is obviously with Claude being the center I think you know we're going to have the obviously AI yourselves build the the ticket system hopefully and start building that sort of corpus up in inside CL as well. I think it makes sense for something like that to be in there and just need to think about how we service that in a in a guarded way as well potentially

Ian Johnson: and and in teams as well. I mean, that's the other thing.

Michael Moores: from

Ian Johnson: Not not I'm a massive fan of Teams, but that's what our channel is. Um, so I'd expect alerts and things to go directly into into there. Um,

Michael Moores: Yeah.

Ian Johnson: but again, we're going all over the place. Can't remember because it it did say developer experience for this one, but I think we did that yesterday,

Brett StClair: did yesterday and I think we're on track and I was just processing the available support last

Ian Johnson: right?

George Westbrook: Yes.

Brett StClair: night and its next suggestion is that we do the internal ops and it feels like we're actually leaning

  
  

### 00:28:08

  

George Westbrook: Yeah.

Brett StClair: into the internal ops ticketing system. Let's talk about that.

Ian Johnson: There you

Brett StClair: Feel come.

George Westbrook: that that's that's what I was thinking because obviously apologies once again few a few minutes late and then uh I was

Ian Johnson: go.

George Westbrook: like oh we must be doing internal ops um and

Ian Johnson: Been a few minutes late, George. But it should be for a better reason than the fact you haven't got coffee because your boss,

George Westbrook: uh

Ian Johnson: by the way, completely sold you out. He didn't We didn't even have to shine a light in his eyes. He just gave you away straight away.

George Westbrook: the funny thing I didn't I didn't even get one this That's what I was thinking. I was think I need my brain to be on. I need my brain to be on. But it's It seems like it's working. It seems like it's all right.

Dorte Dye: That's the one thing I can't help you with.

George Westbrook: No, I know.

  
  

### 00:28:49

  

Dorte Dye: Getting your

George Westbrook: That's why robotics. Need a need a robot a ping as I'm coming in. Please, can you get me a flat white with an extra shot of espresso, please?

Brett StClair: That That's why I use that coffee shop underneath the building there. Whatever it's called, Black Sheep Coffee. You literally order it on your phone and I'm like literally walking and I'm five minutes away.

George Westbrook: Okay.

Brett StClair: Order. And I'm I time it perfectly and they go Brett as I'm

Ian Johnson: slightly slightly worrying the the AI project lead that we're working with hasn't figured out that

George Westbrook: Yeah.

Ian Johnson: you can

Brett StClair: boss.

Ian Johnson: order

George Westbrook: Do you know that is I'm too tight. The coffee up here is free.

Ian Johnson: like be like that you need to be tight as well not just forward thinking but you need to be tight on um okay we

George Westbrook: Yeah.

Brett StClair: So yeah.

Ian Johnson: So let's carry on on the internal support and operating thing

Brett StClair: It's

George Westbrook: Yes.

  
  

### 00:29:49

  

George Westbrook: I suppose this is this is where it's the art of the

Ian Johnson: then

George Westbrook: possible is like completely wide open cuz this is really what do you guys want and need. Um and this is probably not one where we're going to solve it in an hour session, a couple of hour session. This is probably going to be one where it's we're doing we're doing some work. You've noticed that there there's this repeated task that you're doing, right? we need an we need an AI workforce for this or we need an agent here. Um, but I suppose it's obviously starting out which which things are going to be the the key pains to to start. And obviously I think we'd all agree support is is definitely going to be um well hopefully it's not one of them. Um but I think obviously it's the real world and with the nature of software there's going to be support

Ian Johnson: Let's let's let's start at the um let's start at the beginning or almost the beginning.

George Westbrook: support.

  
  

### 00:30:45

  

Ian Johnson: So let let's just park what I call as the go to market piece. start at the point where we've got a commitment from a client and whether that commitment is they've signed a contract or whatever the trigger is there to for us to say okay well we're happy for this to become a project wherever they are in that um in that kind of um process and then let's think about the human effort involved from that point forward So for me the next part is really um there's two types of onboarding. There's technical on boarding which we've been talking about in in the support and then there's the kind of project on boarding. So typical project stuff. Do we understand the scope of the project? Has it been documented? Has it been approved and signed off by the client? So everyone's agreed. How do we manage changes? All of those things. If we start right at that very beginning point with the with the very candid aim of trying to limit the number of resources that we have to hire to manage the two processes.

  
  

### 00:32:02

  

Ian Johnson: the technical on boarding piece we've we've been talking about and obviously that need that's going to need more work. Um and we've got Mike who's responsible for product and tech. You've got dirt responsible for operations and that includes the customer operations from an onboarding point of view. And then in our financial plan, we've got this thing of hiring customer success managers who will both manage the project on boarding um and then ultimately manage the relationship and service with the customer. Now, typically typically a CSM uh trajectory of hires is directly linked to how many how many clients have you got? Okay, we're going to need another person. We've got 10 more clients. We need another person, etc., etc. But in my mind, much of the stuff that they do can I think with is a target for from from an AI perspective. So just as the most basic example, um people they typically have project kickoff calls which Mike hates by the way and would like to just for the record. Um and those project kickoff calls, you know, ultimately typically would have been somebody taking a load of notes, basically going back in re replaying all of those notes.

  
  

### 00:33:34

  

Ian Johnson: Exactly. We've already we've already got that and I think it's building a what's the what's the process we're going to go through and how do we build to a point of okay here here's the statement of work or whatever we call that with the client that that is automatically emailed to the client for their approval. Um and that once it's approved the data from that's captured there is stored somewhere wherever it needs to be aggre put into so that ultimately the next stage of the process has got the information it it needs. I know Mike and Dur have been doing a a bunch of stuff on that with non-c customer related. So before this process or or not really so so product management Mike as an example dirty you for example on the legal stuff and you know other bits and pieces but again we got to come come to it from a mindset of understanding what the typical process

Dorte Dye: Yeah,

Ian Johnson: is and then how do we eradicate the need for human intervention in that

Dorte Dye: I would even start a little bit earlier with the due diligence what we need to do on the customers.

  
  

### 00:34:54

  

Dorte Dye: I know we still defining what the due diligence is,

Ian Johnson: That

Dorte Dye: but going out to do the certain checks on customers before we even start with the statement of work. So there's there's a lot of things there at the moment very manually and labor intense. We just really need to this are the requirements. How do we build the AI agents to fire that off and then suggest the next steps like the gatekeepers for the next phase? So I don't know what the best approach is to just map high level out what the gates are and then think about where can we accelerate with AI and then prioritize it that way.

Brett StClair: I think it's also thinking about where you're going to store that CRM

Dorte Dye: Yep.

Brett StClair: styled and what tool because you don't want to reinvent that,

Dorte Dye: Yep.

Brett StClair: right? You want to use something with an FCP server.

Dorte Dye: No 100%. Mhm.

Brett StClair: We kind of walk through and then map that through and you got your kind of source of truth that you just bring into your core platform too, right George?

  
  

### 00:35:55

  

Brett StClair: Or am I just going a bit too far?

George Westbrook: No. So maybe start with so process is new potential customer due diligence um due due diligence. I'm assuming that's just researching um a bit bit of conversation information collection back and forth with them as well.

Dorte Dye: Please say I

George Westbrook: Okay. Um and then after after that's all done

Ian Johnson: Yeah.

George Westbrook: then so due diligence after they've said, "Yeah, let's go." Or is this before they say, "Let's go."

Dorte Dye: from the moment they do the application form in. So application form we do the diligence and then the contract is

George Westbrook: Okay.

Dorte Dye: alongside that's what we're trying to define

Ian Johnson: What an application form is

Dorte Dye: what we need to do and that comes back to are there specific requirements from a dora perspective we need to show what we have done or not um in gen general it's ownership 25% um if there are any um red flags negative press or anything and then what was the other it can be very light but it can be very detailed as well.

  
  

### 00:37:21

  

Dorte Dye: So we trying to find the the must have and then what tools can we use to do these checks because you can do some things via company's house or some other ones you need to plug in for the due diligence stuff and everything.

George Westbrook: Yeah, because I think that that due diligence I that process um there may be some data sources that we might not be able to access, but I can imagine a lot of them we would be able to. Um, so will that be application form?

Dorte Dye: Yep.

George Westbrook: Bam, bam, bam, loads of research. Here's the due diligence report because I'm I'm thinking what for more maybe the internal op stuff. Um, I there's going to have to be some sort of agent or business operating system interface. Um,

Dorte Dye: I didn't

George Westbrook: which covers all of this. So all of these all of these agents maybe dashboards as well situated in in there could could be in the console as well. Um, but I think obviously to your point Ian, if we're adding complexity in there, is that a good thing?

  
  

### 00:38:23

  

George Westbrook: Is it a bad thing? Um, so we just there's this interface. So maybe there's um, yeah, it goes in, the agent does the research, it's going to present to you the research with all the sources so that you can validate. Um,

Dorte Dye: Yep.

George Westbrook: but all of the work's pre-done. Um, that's that's definitely definitely something very doable.

Dorte Dye: Yep.

George Westbrook: So after due due diligence that's you you're happy with that. What's what would you say would be the next step in the process?

Dorte Dye: That will be the statement of work and the contract negotiation.

George Westbrook: And I'm assuming in order to do that there'd be a meeting or multiple multiple meetings to

Dorte Dye: So that's an interesting one because the platform is very flexible. So they can build everything themselves. However, we need certain level of information to do the scheme project on the back end and that's the question if we can pull it out of the the console as a report what they have set up. But there probably is a transition phase where we need both until we have really ironed out this is what the customer is doing.

  
  

### 00:39:28

  

Dorte Dye: This is the date and then we just do the snapshot of what they want to build to keep them more accountable because that's always customer wants more but don't deliver. It's like how do you keep the project on track kind of thing.

George Westbrook: And and because I'm trying to what what would be the the method of communication between you and the client? Would it be purely email? Would it be a mix of email and like a a team's

Dorte Dye: I think email for the track record and having everything in writing.

George Westbrook: call?

Dorte Dye: Um but meetings is the most productive one I find.

George Westbrook: Yeah.

Dorte Dye: But bearing in mind if I need Mike then I want to limit that kind of input for him that he has to join customer calls.

George Westbrook: I suppose the the emailing one once again that's a I'm assuming it's given the due diligence questions the the questioning from in the email is pretty standardized

Dorte Dye: It will be but yeah that will be an extra form rather than an email because they need to sign that

  
  

### 00:40:26

  

George Westbrook: yeah and then okay

Dorte Dye: we can do the searches on them as well.

George Westbrook: yeah um because it's that email then let's say form submitted research done the the information request sent out to them via email with an email that's drafted by the agent or if it's standardized AI is probably not needed. It's just a standard email sent out.

Dorte Dye: Mhm.

George Westbrook: Um but obviously if there is some changes needed then obviously we put AI in there then there's the approval process.

Dorte Dye: Yeah.

George Westbrook: Um and for the things like meetings as well um similar similar to to what what we're doing where it's there is a notetaker um we might find the need that we need to build a custom note taker um that sounds way more intimidating than it is. I know there's there is a specific API which does this and it's very easily but then it gets the meeting it's going to see the see the attendees. Um, I'm assuming do you have a CRM as well?

Dorte Dye: Yeah.

George Westbrook: What's the What's the CRM?

  
  

### 00:41:33

  

Dorte Dye: Fresh

George Westbrook: Fresh sales. Okay. I'm assuming that's got an API as well.

Dorte Dye: sales.

George Westbrook: Um, then what we can do, we can look at the the emails of the people in the in the meeting, see where they are in the pipeline, which will then inform what type of meeting it is, or maybe in the meeting header, it's got the name.

Dorte Dye: Yep.

George Westbrook: Then the agent will go look through let's say a bank of meeting analyses agent teams um and it will work out okay this was a a a call for the step after the due diligence um think of the name um and then it's going to analyze it in that specific context give you the report and just take any actions and we can keep on like looping that um and what do I mean by looping that so that let's say there's three meetings um first meeting information collected. Maybe there's a plan for the next one. Maybe it expands on that plan, presents it to you. So you've got those meeting notes before and then when there's a second meeting, same thing.

  
  

### 00:42:34

  

George Westbrook: Analyze it and then keep on going through that until it's done. Um and then let's say it's at that point where all of those meetings, all of that information collection is done. What what would be what would be the next step after that?

Dorte Dye: So that will be raising the scheme project to do the implementation with the card

George Westbrook: Okay.

Dorte Dye: scheme.

George Westbrook: What? What goes into

Dorte Dye: So depending of the customer type,

George Westbrook: that?

Dorte Dye: it might be a triparty call. So if the customer is regulated themselves, they're a scheme member that can initiate the project themselves. If not, they need the third party to do that and then it's discussing the scope with the schemes, what the project scope is. And then it's a form filling requirement and um then the bird

Ian Johnson: that that's there's a couple of points I just want I want to make here.

Dorte Dye: phase.

Ian Johnson: What one of them is to pick up on the comment you made about saving Mike's time and given the fact that I know how much he hates client on boarding calls.

  
  

### 00:43:34

  

Ian Johnson: The other part to this to bear in mind is whoever goes on that call there is no reason why they can't answer any question almost any question the client asks without having to be having to have it in their head and that's the thing we need to think about. So what's that experience that client asks a question that you know we don't know the human on the end of the call doesn't know the answer to they should readily be able to get that answer that isn't eradicating this whole thing of I don't know the answer to that I'll come back to you because what you going to do if you're going to go to Mike and ask him the answer to that question I know for certain Mike is going to say he won't say anymore because we're in an AR world but he would what he would have said was read the f****** document mentation, which is what he secretly wanted to say to clients on these on boarding calls. And it's totally understandable, right?

George Westbrook: which is the right answer.

  
  

### 00:44:34

  

George Westbrook: Yeah.

Dorte Dye: We literally just have an AI mic who is answering all of that,

Ian Johnson: It is well

Dorte Dye: not just joking.

George Westbrook: Hey,

Ian Johnson: to be perfectly well, yeah, we've got better uses for mind than answering dumb questions. It's not the question dumb. It's just that the it's there that you know the thing is if if the AI can't answer the question,

George Westbrook: no.

Ian Johnson: if we can't access answer that question that is that we are a user of the the fact that the documentation needs to be updated uh to basically work for more users. Right? So that's the first thing I'd say to answer your point about limiting calls because of Mike's need for availability. We should start with a point of assume that Mike is not required for that call. All right. Now there may be things that come up but if those things come up they will have been captured in the notetaker and then we figure out how they get how they automatically get into Mike for Mike to be able to respond to them.

  
  

### 00:45:35

  

Ian Johnson: Right? So that we need to think about that that first and foremost. I think the second part is if we think about think about start with the end in mind. If I've from memory Mike at Marqueta because one of the things that really annoyed me is somehow we ended up taking responsibility for completing the client CIQ with visa because the CIQ is the document as I understand it is the document that you basically when when D talked about the form this is the thing that the visa need to be able to go away and configure their systems to meet the client's requirements. Right. So that's where the thing ends up and again in my opinion what we need to be aiming for and this is both a positive for for three positive one for us one for the client and one for the bin sponsor is that we that we understand what needs to go into CIQ and we are basically ticking off whether or not that information has been captured in these calls or whatever it is that's still missing.

  
  

### 00:46:45

  

Ian Johnson: in working to a point where I'm not saying we complete the CIQ document DA but we should surely be able to provide all of the all of the data that needs to go into

Dorte Dye: So there there are certain elements we have to complete as the processor side of things and that's

Ian Johnson: it.

Dorte Dye: what I'm trying to work out with the DD team. What is our template and what are the parameters we would change or can change? What information we need from the customer? And then there information which is purely down to the sponsor and to the program manager where we wouldn't get involved.

Ian Johnson: Let me just let me just make sure I understand that there's data that we have to give. We don't we're not responsible for completing anything in the CIQ

Dorte Dye: Mhm.

Ian Johnson: form.

Dorte Dye: As the process will have to

Ian Johnson: No, they will have to give whoever it is that's submitting the CIQ form the information to go into it.

Dorte Dye: Okay. Terminology.

Ian Johnson: But it's important in the process thing because there isn't going to be a process where

  
  

### 00:47:45

  

Dorte Dye: Yeah.

Ian Johnson: we have to access the CIQ document and put things in that because that's something we don't control that document. That's the challenge. I mean it could be to the end to the end degree that we that based on the conversations George if if the CIQ was a shared document that every multiple people have access to not via email but it's stored we could automatically update the data items in that CIQ form but I think that's a step too far and I think the point is helping build from those conversations what we believe needs to go into the CIQ. Both the things that we have we are on the hook for but also the other things that Marqueta we ended up figuring out with the client because they had no idea how to complete a CIQ for

Dorte Dye: So that's really interesting because With all of the processes previously I've worked with, the processes always completed the relevant apps on that form directly because it was so much to give that information to the customer or the sponsor that would have made more damage to it than um than good.

  
  

### 00:49:12

  

Ian Johnson: E either way, I'm a little bit skeptical about that whole notion of because what happens, they send a blank CRQ document, we update our things, we save a new version, then we send it to them because it's not it's not a shared source document, is it? It's a it's a it's it's a flat copy document. It's here it is. Fill it in.

Dorte Dye: It is but what what I was envisaging that we have a template for us for our settings. This is always the information that they're add in that will be not changed. Only these few things can be changed and then work out what's the reason behind this is for the change. So that it's very easy to duplicate all of that

Ian Johnson: Yeah, I I agree.

Dorte Dye: stuff.

Ian Johnson: So, we're completely aligned. There's two things here. What are we solely responsible for?

Dorte Dye: Mhm.

Ian Johnson: and how do we get that data and how do we use AI to capture what's been said in chats etc so that it's populated um what else in CIQ form are we not responsible for but we can help the client through the conversations capture what they're actually going to put into that document and then to your point that's then the part where we can have a template completely agree can be a complete copy of the CIQ that is a stored document and that we update the various data

  
  

### 00:50:38

  

Ian Johnson: items from and that we're building it we're building essentially a CIQ form I mean we could have the conversation with well we can have conversation with Michael can

Dorte Dye: laughing.

Ian Johnson: have conversation with visa I don't know if other people basically always stick to the the I mean the the point is it avoiding in a situation where something we're capturing all this information and then somebody is receiving a CIQ document from a client and they go can you just populate your information in this CIQ document? Well, no. We can give you what needs to go in the CIQ document. That last part of it we we need to figure out. But to to your point, George, that's the end, right? in terms of there's two things. What do what do we need from our to set up this project customer etc. To D's point um they can go off and and build anything they want to build and we'll have we'll know what they've built but we won't have the context of what they were trying to build.

  
  

### 00:51:59

  

Ian Johnson: So we won't be able to guide them. Now, if they'd asked the AI, if they'd gone in and used AI and said, "I'm building an expense management program for targeting small businesses in France, we' have there's some context there we could capture and we could put into the CRM system. But if they don't and they just go and build there's the starting point then if something wasn't working or they weren't getting the outcomes they were expecting is we'd have to understand, well, what was it you were trying to do? That's the reason statement of work in the first place.

George Westbrook: Yeah.

Ian Johnson: I mean, we're doing the same thing here, right? You guys could go off and build anything you like and give it to us and then we go, "What the f*** is that? That's not what we were thinking." That's the whole purpose of doing this thing. Statement of work is the thing that really helps us understand what they're trying to do. So, we're grounded in it. it really and and some things that we need to do in the background to enable that to happen.

  
  

### 00:53:01

  

Ian Johnson: And then the CIQ is the thing that ultimately they need to submit to Visa to get the thing to work. Either them directly or their issuer partner need to submit. So those are the two main things. And then the you know the other part to it is a project plan. So these things are typically littered with unre unrealistic dates. Okay. When do you want to go live? Tomorrow. Yeah. But the lead the lead time with visa is 12 weeks. When do you want to go live? Tomorrow. So it's that's the whole thing that I think and this is totally in your wheelhouse da but thinking about what it is that you want to achieve. My only guidance on it is try to avoid a human having to be in there to do anything other than to approve and to be on the calls. And whoever that person is, if Mike's off doing whatever he does in his spare time, racing cars or whatever else, and he's not available, we can't be in a position where a we've got to have another mic.

  
  

### 00:54:14

  

Ian Johnson: Well, there isn't mic. So, a we have to have another mic or somebody else or B we say we can't have a meeting with them for a week or two weeks because we don't have the technical expertise. That that cannot happen.

Dorte Dye: Okay.

Ian Johnson: So, I think that's just what we need to think about. We need to break this thing into bite-sized chunks. As much as the the experience on the with the technology is vitally

Dorte Dye: Yep.

Ian Johnson: important, so is the experience when they do interact with our people. And I'll be honest with you, you well, you you you know this because I do it all the time. I'm happy to talk until the cows come home. What I don't really like doing is writing documentation. So, somebody then says, "Can you just put all that in a document and confirm it for me?" I'll be like,

George Westbrook: H.

Ian Johnson: "No, I've just we've just done it all." So, when we have those client conversations, they need to be guided.

  
  

### 00:55:16

  

Ian Johnson: We need to be we need to know what we're trying to get from them. We need to capture it all. Um and then it needs to be um the single source of truth. And the thing I wanted to ask you, Mike, was because I know this happened at Marqueta. I know it's a frustration, but you've got a statement of work and then there's a conversation that goes on or a client has changed their mind and we're not aware of it and whatever else it will be and then ultimately it comes out that something's not in sync. And in the worst case scenario, we might have done something we had to do with the setup that we then find actually that's not what they're wanting to do anymore. So that's the other thing that we need to figure out how we always avoid that. So if there is a conversation you're not part of Mike that does result in a change to a statement of work that is required for us to be able to deliver the service that that statement of work change is automatically identified and flagged.

  
  

### 00:56:22

  

Ian Johnson: Um, so that we're always we always know what we're supposed to be doing. I mean, none of this is rock science,

Brett StClair: I mean George I'm just going to that interview process that we do

Ian Johnson: right?

Brett StClair: for the content workforce in the similar way we're doing an onboarding agent that instead of a straight form you might have form on boarding agents kind of built into that and right up front you're dealing with all those kind of high level timings be aware visa takes 12 weeks be aware and you kind of those real pain points on f***** sakes how many times do I have to tell you you're just driving that point home as quick reminders but so we we have something called a content workforce and when we take businesses through it we sit with the business and it's That's two-day interview process and it understands their content manifesto and and content pillars and their and we spend time oneonone but the talking us through the agents understanding saying when we do it

George Westbrook: Oh, I think you might bre

  
  

### 00:57:43

  

Brett StClair: Oh.

George Westbrook: connection.

Ian Johnson: All

Brett StClair: Oh.

George Westbrook: Got a lovely still image of you there.

Dorte Dye: Okay.

Ian Johnson: right. You don't that coffee shop you're in at the moment, Brett. Although I can understand why it takes two days.

Brett StClair: I'm back. Hey, can you guys hear me?

George Westbrook: Yeah, that's

Brett StClair: Um,

George Westbrook: better.

Brett StClair: so we also do one for personal and that's all like an agent that talks through and says this is what I've understood. I need the following information from you. This is what I've understood. You need to know this, you need to know that. And you can guide that conversation. Get a whole lot of output that you require, that visa requires. Then you can also highlight when there's changes. You can go, well,

George Westbrook: Were

Brett StClair: the agents picked up that they're wanting this change to your standard kind of terms. Flag it, send it to Mike. That's kind of what I'm thinking.

  
  

### 00:58:44

  

Brett StClair: Where is your head space there, George? And that kind of flow of a on boarding agent,

George Westbrook: you were you thinking when you say content workforce agent,

Michael Moores: Awesome.

George Westbrook: do you mean the agent user Or you were you were

Brett StClair: the brand entity. Yeah.

George Westbrook: you thinking the agent speaking to the user or the user and the the human speaking to each other which is recorded by the agent which then provides suggestions? Which one?

Brett StClair: the personal brand

George Westbrook: No,

Brett StClair: one.

George Westbrook: but they're they're the same one. I'm saying is it the one where you speak to an agent like Yeah.

Brett StClair: Yeah.

George Westbrook: Okay. Yeah. Yeah. No, that I think Yes, but I think it's depend like I I don't know what goes into a CIQ form. It could be 10 fields or it could be a thousand. It's a thousand then obviously that's quite a lot of information and then you've obviously got the risk of a user dropping off um if they're having to well they're probably not going to drop off if they're at that stage.

  
  

### 00:59:53

  

George Westbrook: Um, but it's I suppose it's it's it's weighing up. Is it something that they're going to go through from start to finish? But then there's also the the possibility that then they don't have to do it all in one go. They can go they can start they can be presented the information they need. They can be told where to find it or how to get it.

Dorte Dye: It's never that straightforward.

George Westbrook: Um.

Dorte Dye: Normally the schemes give you three weeks to complete the document because it's so complex.

George Westbrook: Ah.

Ian Johnson: Yeah, I think and we should definitely think with that lens of do we need humans to be involved in it at all? But there's a balance to be struck in terms of we want to use tech as much as possible to allow clients to self-s serve and to support them and internally but we also you know we want to establish relationships with clients. What we don't want to do is the the the preceding administration work and the administration work afterwards to actually capture what is that conversation.

  
  

### 01:01:01

  

Ian Johnson: Now it can you know so there's always going to be an initial project kickoff discussion that needs to take place you know my experience with those things is as it any meeting tell people what it is you're going to talk about and what you know what information they need to be aware of in advance. Share that information with them. Have the meeting. Try to tick off as many boxes as you can during that conversation. replay it back to them and replay back what the gaps are. Now, the determination of what we do after that, George, as to what the gaps are as to whether or not it requires another conversation because of context and making the client feel as though they're being supported or whether it is something that can just be completed through using an agent. Um, I don't know. But um we we need to just think about which areas of the process we'd be happy to be fully automated. Ones are probably a bit too daunting for a be left

  
  

### 01:02:10

  

Dorte Dye: Mhm.

Ian Johnson: with even with

George Westbrook: So,

Dorte Dye: Yep.

Ian Johnson: guys

George Westbrook: my next suggestion of an AI avatar to actually run the meeting, I I don't think that would be a good one.

Ian Johnson: possibly. I don't this the thing is I don't want to say no to anything but I I do think there are certain areas that the industry just would not be ready for at this stage.

George Westbrook: Yeah.

Ian Johnson: Um so we just need to be somewhat cognizant about that. But I do think it comes back to starting with the end in mind. What is it that we are that we have to achieve from this part

George Westbrook: Sorry.

Ian Johnson: of the customer life cycle and then figuring out how best to get to the point where we achieve that both internally to limit resource usage and then from a client perspective to strike that balance of having meetings, feeling supported but also, you You know, you can you can just go off and and do this yourself and it will be

George Westbrook: Yeah.

  
  

### 01:03:26

  

George Westbrook: Maybe there's with that with that form there's having like

Ian Johnson: updated.

George Westbrook: a I was going to say part of the console um where it's got that where it's got that that form on there which both they can write to you can write to and also the agent can write to with different like say maybe for say if the agent's working away it captures um 10 10 fields. It goes in, it writes it to that shared form view um with the little status which is under review or needs to be reviewed. Um so it's going to fill out everything. You can see when it's an AI that's put it in, when it's the client that's put it in, when it's maybe you guys that have put in, and then different like say if the client's put it in, maybe we'd always assume that it's approved. So we don't need to change that. That's like locked down. Um but say if it's uh an agent input field um meeting one it puts in x equals y but in the next meeting um it might uncover that x x doesn't equal y equals z.

  
  

### 01:04:35

  

George Westbrook: Um but because it knows it was an agent written field that there could be it can build up the picture from both those both those meetings. But then also there's the flexibility you can go in you can add stuff in. there's flexibility that you can just say to them, please can you just fill this in? Because I suppose for different clients, maybe different ticket sizes, you maybe the bigger ones, you might want to be like, no, f*** it. We're going to we're going to fill in everything for you. Please just please just give us

Ian Johnson: Well, so conscious of the fact that we've I think we've run over,

George Westbrook: money.

Ian Johnson: so we need to wrap up. But one thing I think one thing to think about is what what is the target system for holding that information, right? So yes, we actually need some of that information, Mike, to be able to set up the client and therefore some of some of it would logically could be in the console. But in my mind the central source of everything associate to do with a client should be the CRM.

  
  

### 01:05:42

  

Ian Johnson: What comes from the CRM into what the console needs or another internal system needs should be something where you just send that data out. But if you are writing directly to the console then you've split over two systems to understand the context and the data items. it's in the CRM which you which again I don't know you could write to directly I don't know the its capability that's a different thing but I think from memory Mike we had everything in this Salesforce and then what came after that and I think that's the right way to go because otherwise who goes to interrogate that to get the full picture.

Dorte Dye: or would you have bin splits in the in the CM system?

Ian Johnson: Why

Dorte Dye: Isn't Isn't it more like you have the statement of work in there and then you have everything in there rather than having all of the fields in

Ian Johnson: not?

Dorte Dye: there from the

Ian Johnson: Well, whatever we decide to do and not to do,

Dorte Dye: form.

Ian Johnson: the whole point is if it's in a flat document, then it kind of limits the use of those data items.

  
  

### 01:06:54

  

Dorte Dye: No. Yeah.

Ian Johnson: If they're in the CRM, then there's a lot more that you can do in my opinion from that point. But again, I say we've run over to the point that you said earlier about how this internal operations thing can be huge. There is no point us trying to boil the ocean on our end to end internal operations. We just need to pick something that's going to happen first.

Dorte Dye: One,

Ian Johnson: Okay.

Dorte Dye: two,

Ian Johnson: And the first thing that's going to happen is that customer on boarding stuff. The go to market stuff we can park and keep separately. Um but that's the first thing that's going to happen. So I think we just need to think about the scope of what we're trying to do as being that there because really from that moment onwards there's general management stuff but we've already started talking about support and what support would look like. So how do you get a client to be a client and and on boarded and then how do you support those clients through that cycle?

  
  

### 01:08:05

  

Ian Johnson: So we just need to keep the scope of this relatively thin. Um and and I think we need to we need to start thinking about what what our vision is for this particular area. Um and again it's all it's all completely I'm totally open to it. I just don't like the idea of if it's logic if it this logically needs to be in the console mic already then fine but does that mean that that's the place that we write to or is it so it's just it needs that information at a certain point in the process and it gets it from somewhere else that is actually the best place to store that information so that whether it's an AI agent that's supporting the client or It's our individual people. They go somewhere and they can see all the information they need to about a client that that experience.

Dorte Dye: What?

Ian Johnson: Let's say there is a call required and you have to flick between two systems to answer the question. So you've got a CRM that tells you who the client is, who the contact is, got all of the notes, all of that stuff. And then you get into a conversation about some specifics around the setup and you can't see that unless you open a flat document or you go and have a look at them in the console. That's that's s***. Frankly, that just can't happen. All right.

Dorte Dye: So we

George Westbrook: Perfect. Right.

Dorte Dye: look

Ian Johnson: Good.

George Westbrook: Have a good day.

Ian Johnson: Yeah, you too.

George Westbrook: Speak to you. Speak to you tomorrow.

Ian Johnson: Hi.

George Westbrook: I think it Yeah, we got the next one tomorrow, haven't we?

Dorte Dye: Yep.

Ian Johnson: Yeah.

George Westbrook: Love it.

Ian Johnson: All good.

George Westbrook: Right.

Ian Johnson: Catch you later.

George Westbrook: Me. Have a good one.

Brett StClair: Guys, catch

  
  

### Transcription ended after 01:10:24

  

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

**