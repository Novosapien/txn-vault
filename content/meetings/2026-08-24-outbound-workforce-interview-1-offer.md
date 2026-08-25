---
date: 2026-08-24
type: general
description: "Transcript and analysis of the 2026-08-24 Outbound Workforce interview one (the offer): TXN tagline, value proposition, pricing, balance-holding contradiction"
scope:
  - "[[commercial]]"
  - "[[vision]]"
status: raw
---

# TXN: Outbound Workforce, Interview 1, The Offer (2026-08-24)

> **Source:** Full Gemini transcript, synced from the shared folder. Attendees: Brett StClair, Max Kingaby, Lily StClair (Novosapien); Ian Johnson, Dorte Dye (TXN). George Westbrook referenced but not on the call. Duration 01:06:58.
>
> The first of the Outbound Workforce interview sets scheduled in [[2026-08-18-agentic-standup]]. Brett was explicit at the top that **this is not a Content Workforce session** and runs in parallel to it: *"I'm not going to use this as the content workforce session. I think we can do this in parallel."* Two further Content Workforce sessions are still to be booked.
>
> Filed here because the second half is the single clearest statement of TXN's own positioning, pricing model and go-to-market sequence on record, and because it surfaces a **direct contradiction with a load-bearing assumption in [[vision]]** (see the flagged finding below).

> [!warning] Digest deferred by decision
> **Status is `raw` on purpose.** The findings below are identified and mapped, but no destination document has been updated. The interview series runs to at least Thu 27 Aug (ICPs Tue 25 Aug, personas Thu 27 Aug), and the positioning material is better written into [[vision]] and [[commercial]] once the full picture is settled rather than in fragments. Revisit when the series closes.
>
> **One item should not wait for that.** The balance-holding contradiction is a factual correction to [[vision]], not positioning material, and it shapes how [[fraud-risk-assist]] is scoped. Raise it with Ian for confirmation ahead of the digest.

## Findings, pending digest

### Flagged for early attention

| Finding | Proposed destination | Proposed action |
|---------|---------------------|-----------------|
| **TXN does hold balances, at least sometimes. This contradicts the vault.** The onboarding skill caught the discrepancy live and put it to Ian: the vault records that in MVP TXN does not hold funds and every authorisation is a pass-through. Ian's answer: *"there are occasions where we can authorize a transaction based on a balance that we hold on behalf of the client... increasingly in this market it typically is that the authorization gets rooted to the customer for them to make a decision... But it's an either or. Sorry, it's it's both, not an either or."* [[vision]] currently states the pass-through model as fact in five places (lines 39, 43, 45, 122, 355), and it is the stated reason [[fraud-risk-assist]] is scoped as *advise, don't decide* | [[vision]], [[fraud-risk-assist]], [[open-questions]] | **Flagged.** Confirm the position with Ian, then correct [[vision]]. Candidate new register row (next number #55) |
| **Multi-tenancy: one client can still affect the others, and TXN knows it.** Ian, in full: the original plan B was each client in their own environment; DT came back with a centralised resource managing everyone into one central place with APIs hitting segregated databases. Clients can still stand up a completely separate environment if it matters to them, but the standard shape is shared components with segregated data. Asked whether one client flooding the system with bad API calls could impact others: *"Yes, we believe there still is a risk that it could impact other clients."* Described as an ongoing conversation between Ian and DT about the proposed architecture | [[architecture]], [[open-questions]] | **Flagged.** Candidate new register row |
| **Mastercard is not in MVP.** Ian: certification is *"the number one"* priority as soon as MVP launch finishes. Dorte: *"we're launching this Visa. The Mastercard comes later."* Ian is comfortable naming both schemes in outbound because the sequencing can be handled in conversation | [[vision]], [[delivery]] | Deferred, pending series |

### Positioning and offer

| Finding | Proposed destination | Proposed action |
|---------|---------------------|-----------------|
| **Tagline agreed: "TXN is the platform for any company launching and operating a card program."** The group rejected two full rounds of AI-generated options as too wordy and too fancy. Ian's reasoning is the substance: the load-bearing word is **"any"**, because the buyer *"doesn't have to be a bank... you can be a trade platform, you can be a marketplace, you can be whatever."* They deliberately dropped "card issuing platform" from the line, because *"you're making more of a bold statement that we are the platform"*. Dorte: *"If you change the four to any then it's powerful."* Ian also drew a distinction worth preserving: a tagline and a plain description of what the company does are two different sentences with two different jobs | [[vision]], [[commercial]] | Deferred, pending series |
| **TXN's value proposition, in Ian's own words.** A card issuing processing platform sitting between a client who wants to issue cards to its customers, consumer or corporate, and the card schemes. **Two sides.** One: letting a client manage cardholder accounts so they can request cards, physical or digital, including Apple Pay and Google Pay. Two: pure processing, handling the messages from Visa and Mastercard whenever a card is presented at any merchant worldwide. On authorisation TXN either checks the balance and any card-level restrictions set by the client, **or** routes the decision to the client. On clearing, TXN receives scheme confirmations, aggregates the day's authorised and cleared transactions, and tells the client what is owed to Visa and Mastercard | [[vision]] | Deferred, pending series |
| **Positioning guardrails, both defensive.** One: do not look like a wraparound on a legacy platform. Ian's worry is that naming DT's 25 years of processing heritage invites *"So your platform's 25 years old?"* The framing must be that TXN uses the know-how, heritage and money of the two parents while the technology is TXN's own. Two: do not AI-wash. Ian named a competitor, **Thread** (as transcribed), who *"suddenly announced themselves as the AI issuer. No, no, they're not. It's absolute nonsense."* His position: TXN has thought about AI from day one, but framed as *"not about how do we use AI but how can AI help us deliver this vision of giving the best possible customer experience"* | [[vision]] | Deferred, pending series |
| **Where TXN chooses to compete: experience, not price.** Ian: *"they can compete on price but we're not going to do that, no one's interested in doing that."* The competitive ground is how easy it is for clients to do what they want to do, specifically not needing deep card expertise and not needing to employ large teams to manage programs | [[vision]] | Deferred, pending series |
| **Two distinct buyer types for a card program**, carried over from the content work. Type one: the card program is **core**, part of the product, they have no choice, and they know the domain well. Type two: they do not know much about running card programs but see an opportunity to create value for their business and their clients. Language must stay simple enough for type two, since the line is used across both | [[vision]], ICP and persona sessions | Deferred. Feeds the 25 and 27 Aug sessions |
| **The joint venture is not the lead message.** Ian: *"I don't see why anybody in Europe would really have any knowledge of a South African payment business."* His analogy: if OpenAI and Anthropic launched a business together the parents would be the headline, but Pay Corp and Direct Transact are not those names. Sequence: the market announcement leads on the launch of TXN and the fact of the JV, then in targeted outbound the JV becomes *"a reason to believe, but it's not the lead message."* Ian was speaking to Bronwyn on Wednesday and Pay Corp the following day about that press release | [[commercial]], [[vision]] | Deferred, pending series |

### Commercial

| Finding | Proposed destination | Proposed action |
|---------|---------------------|-----------------|
| **TXN's pricing model, in detail.** Two core principles. A **fixed monthly licence fee per client** to access the platform, covering the Control Center, the Knowledge Hub and unlimited API calls. Plus **volume-tiered variable fees**: one fee per settled transaction and one fee per 3D Secure authentication, with the unit fee falling as volume rises. Ian noted issues with how the pricing language is currently written | [[commercial]] | Deferred, pending series |
| **The AI layer is currently bundled into the licence fee.** Ian: *"initially the plan is that will also include the the AI elements."* Commercially material to Novosapien, since it sets how TXN expects to recover the cost of the agentic layer from its own clients | [[commercial]] | **Flagged.** Worth a direct conversation |
| **No pricing numbers in outbound.** Asked whether to disclose prices, Ian: *"no."* Brett confirmed: *"For balances and disclosure, definitely no. Do not name numbers."* | [[commercial]] | Deferred, pending series |
| **The Knowledge Hub is the first externally-facing material TXN will have.** Mike has produced draft Knowledge Hub content and sent it to Ian and Dorte. It is where prospective clients will go to understand TXN, and covers TXN's role and the end-to-end card lifecycle. Ian offered to send it to Novosapien for ingestion once approved, which he expects to be quick. His important caveat: **every TXN document shared so far is internally focused**, so this would be the first material written in the register TXN actually uses with the market | [[commercial]], [[developer-support]] | **Flagged.** Chase once approved. Materially improves the vault |

### Outbound Workforce mechanics

| Finding | Proposed destination | Proposed action |
|---------|---------------------|-----------------|
| **Emails send from named individuals on a secondary domain.** Ian rejected a generic TXN address as *"too impersonal"* and because it does not mirror the sales structure TXN is building. Initially all sends come from Ian; as salespeople join, sends move to whoever owns the territory. Brett's constraint: the sending domain must not be TXN's primary domain, to keep it off spam and red lists. The domain extension is transcribed as "axm.global", almost certainly txn.global | [[commercial]] | Deferred, pending series |
| **Domain warming protocol.** New domains stood up, then tested. Brett described colour-gradient deliverability checks that reveal whether a domain has already been used for bulk sending. Warming runs one to two weeks using generic addresses and content unrelated to the business, until every metric is green, then is monitored continuously to keep it green | [[commercial]] | Deferred, pending series |
| **LinkedIn capped at 200 outreaches per week** to stay inside platform constraints and protect profile standing. Sales Navigator required, and profiles need bringing up to standard first | [[commercial]] | Deferred, pending series |
| **No AI outbound voice, and no AI inbound voice either.** Brett clarified Novosapien does not do outbound voice at all, on regulatory grounds, but does do **inbound** voice: a lead arrives, the agent picks it up, responds by WhatsApp and calls back. Ian accepted immediate response to an inbound lead but drew a firm line: *"that inbound lead needs to be picked up by a human at TXN rather than any kind of voice call from AI"* | [[commercial]] | **Flagged.** Narrows Outbound Workforce scope |
| **Market is deliberately small.** Ian: *"We're not talking about 20 or 30,000 target accounts here. This is not going to be a mass thing."* This is a niche, focused market, not a volume play, which changes the shape of the outbound programme | [[commercial]] | Deferred, pending series |
| **The 126-account list.** Ian has a list of about 126 accounts across Europe that Claude assembled during a go-to-market planning exercise, built without paid subscriptions. He is *"still somewhat unconvinced that that's really a high enough number"* and unclear how it was derived. He will send it across | [[commercial]] | Deferred, pending series |
| **Lead qualification is a human-in-the-loop exercise.** AI shapes and identifies candidate company sets; Max then sits with TXN and works through the list by hand, roughly three to four hundred before fatigue sets in, teaching the agents what a good profile looks like. Ian's clarifying question was precisely this: what role does Novosapien play in identifying targets | [[commercial]] | Deferred, pending series |
| **Conversion expectations set low and early.** Brett: response rates of 0.01% to 0.02%, and *"you'll be lucky if you get a response."* Follow-up sequences differentiate by audience, for example CEO versus salesperson. The agent's stated goal is securing a meeting. Email converts less well than LinkedIn. Once a lead is exhausted it is qualified out rather than chased | [[commercial]] | Deferred, pending series |
| **Outbound must be sequenced behind the launch.** Ian: outbound campaigns need to align with the content piece and the launch overall, to *"warm the market"* through existing connections and the Pay Corp and Direct Transact LinkedIn networks first. Brett confirmed the outbound skill has already ingested the current state of the content workforce and will keep re-reading it as that work progresses | [[commercial]], [[delivery]] | Deferred, pending series |
| **Go-to-market launch sequence, as Ian described it.** DT and Pay Corp announce first through their own channels, LinkedIn, industry bulletins and blogs. Then the personal networks of Ian, Mike and Dorte extend the reach. Only then does TXN begin publishing its own content, followed by individual content. Ian: *"TXN can't announce itself and expect anybody to be remotely interested"* | [[commercial]], [[delivery]] | Deferred, pending series |
| **Contradiction to resolve.** [[commercial]] currently records, from [[2026-08-13-content-workforce-initiate]], that the *"Outbound Workforce is deferred to a later phase; the Content Workforce runs first."* This call is outbound work actively starting: domains and email configuration are being scoped for George, and 126 accounts are in play. That note is now stale | [[commercial]] | **Flagged.** Correct when the digest runs |

### Context, no action

| Finding | Note |
|---------|------|
| Ian challenged whether the architecture and authorisation questions belonged in outbound material at all: *"I would challenge why we're getting into that level of detail in outbound emails or LinkedIn anyway"*, and questioned why they were treated as blocking. Brett's answer was that the session is building a knowledge base, not just email copy | Useful signal on how the onboarding skill is perceived by a client |
| Novosapien is running TXN as its own test case. Max: *"You're the guinea pigs."* Brett's read on Bronwyn: *"I think she wants to keep an eye, see how you guys go"* | Consistent with Bronwyn's stated position on 04-08 |
| Ian confirmed Bronwyn has had a general Content Workforce walkthrough, not only in a TXN context, and was interested in it for the Pay Corp group ("payrop" as transcribed) | Corroborates [[2026-08-04-content-workforce-demo-paycorp]] |
| Max's manifesto document not yet read. Ian planned to review it that day and come back to Max, but felt *"comfortable that we're on the right track"* | Action item only |
| Ian's closing position: *"I genuinely am happy with where we're going."* His one ask is clarity on how the Novosapien work fits the overall go-to-market approach | Positive signal |

## Open actions from the call

| Owner | Action |
|-------|--------|
| Ian Johnson | Send the 126-account European target list to Novosapien |
| Ian Johnson | Send the draft Knowledge Hub content once approved, for ingestion |
| Ian Johnson | Review Max's manifesto document and come back to him |
| Ian Johnson | Speak to Bronwyn (Wednesday) and Pay Corp about the launch press release |
| Max Kingaby, Ian Johnson | Work through the target list together to validate accounts |
| Brett StClair | Generate an HTML status printout of the session and circulate for review |
| Brett StClair | Define the technical specification for email configuration and domains, for George |
| Brett StClair, Dorte Dye | Book two further Content Workforce sessions |
| Brett StClair | Arrange a 30-minute session with Mike, George and Jacob, who runs TXN's domains, to hand over setup requirements |
| George Westbrook | Run email configuration and domain warming once the specification lands |
| TXN | Set up the outbound sending domains on their side |

---

## Transcript

Aug 24, 2026

## **TXN Outbound Workforce \- Interview 1 (Offer) \- Transcript**

### **00:00:00**

**Dorte Dye:** Morning.

**Max Kingaby:** Morning.

**Brett StClair:** How are

**Dorte Dye:** You back in the office.

**Max Kingaby:** Morning.

**Dorte Dye:** Is that

**Brett StClair:** you?

**Dorte Dye:** live?

**Brett StClair:** Poor old

**Max Kingaby:** I completely missed what was said there,

**Brett StClair:** Max.

**Max Kingaby:** but I heard Brett laughing, so it can't have been that funny.

**Dorte Dye:** I just said that you're back in the office, but I guess the good thing is that the sister's not around,

**Max Kingaby:** Oh,

**Dorte Dye:** so you can't unsold her now.

**Max Kingaby:** insult her. God, she she didn't get enough of an insult. She singing. She was knocking on the door and talk and was swearing at me to come and open the door and I was like, I'm in the middle of a call.

**Dorte Dye:** That's the joy of working from home. I have the whole family here doing that.

**Max Kingaby:** She got off very lightly. We We run a strict shop around here and uh

**Brett StClair:** Hold on. I'm just doing one quick thing.

**Max Kingaby:** Yeah.

**Dorte Dye:** Hello.

### **00:01:28**

**Max Kingaby:** This is Brett

**Brett StClair:** Meet Brett

**Max Kingaby:** Jr.

**Dorte Dye:** So now Max, we can see what taste of humor runs in the family.

**Brett StClair:** Jr.

**Dorte Dye:** Sorry, you will get lots of beating for your dad, but that's the joy of working with your dad.

**Lily StClair:** Don't worry.

**Brett StClair:** Oh, sorry. I've got Ian there.

**Dorte Dye:** Did you deny

**Brett StClair:** I nearly denied him accidentally.

**Dorte Dye:** them?

**Brett StClair:** Hello, Ian.

**Max Kingaby:** I am

**Dorte Dye:** Morning.

**Brett StClair:** You're on

**Ian Johnson:** Yeah,

**Brett StClair:** mute.

**Ian Johnson:** say relax you back from your holiday,

**Max Kingaby:** I am but I was saying to the guys Wednesday evening I go to a beaver.

**Ian Johnson:** mate.

**Max Kingaby:** So,

**Ian Johnson:** What kind of shop are you running there,

**Max Kingaby:** shortlived

**Brett StClair:** Got to ask myself the same question.

**Ian Johnson:** Brett?

**Brett StClair:** George and I working over the weekends and late evenings and everyone else is

**Max Kingaby:** in in fairness,

**Brett StClair:** partying.

**Max Kingaby:** I I was working it out. I have only taken two days annual leave this year.

### **00:02:34**

**Brett StClair:** Well, all that happens is you can't carry over more than sex. No

**Max Kingaby:** I've I feel like I've holidayed a lot.

**Brett StClair:** problem.

**Max Kingaby:** Like I don't really need any more days off, but I've just done it in like good times. I don't know, like over weekends and

**Ian Johnson:** the naive the naivity of youth. Max,

**Max Kingaby:** stuff.

**Ian Johnson:** I would just stop talking if I were you, dude. Because the basement crosses My work is not hard. So I feel like I'm holidaying all the time.

**Max Kingaby:** I love what I do and I love the people I'm

**Ian Johnson:** Very good. Very

**Brett StClair:** And in the end,

**Ian Johnson:** good.

**Max Kingaby:** around.

**Brett StClair:** what meet the uh junior version of Brett.

**Ian Johnson:** Oh,

**Dorte Dye:** The better if you

**Ian Johnson:** what? Okay. I've just I'm only literally I'm a bit slow today, so I've just put those two things together on your prompt.

**Dorte Dye:** want.

**Ian Johnson:** Hi, Lily. How you doing?

**Lily StClair:** Hello.

### **00:03:26**

**Lily StClair:** Good things in you.

**Ian Johnson:** Yeah, right.

**Brett StClair:** So, Lily's just joined the team.

**Ian Johnson:** Thanks.

**Brett StClair:** Um, so first day for her. So, it's figuring out what it's like to work with these bunch of Well, we all know what Max is like.

**Ian Johnson:** Relax. That's what Max is like. It look stretched out and stay safe for us.

**Brett StClair:** So what we've still got to do is we've actually got to find two more sessions for the content works. I'm not going to use this as the content workforce session. I think we can do this in parallel. Um uh so this is about getting the tone right on well not the tone this is getting your offer your ICPS a lot of the work which you've already actually done in your documents. Um, so what I've done is I've already pre-run um some of this and uploaded all of your documentation plus I've linked it to our vault and it's consumed the vault as well and I've got it all ready to go. And we've done this twice before.

### **00:04:30**

**Brett StClair:** Um, so like this this is a a new version. We've called it uh an actual onboarding skill set to try and make it a lot slicker than previously. Um I'm expecting this could go fairly smoothly. But what it will do is one spends a lot of time thinking about your targeted audience and how you position your product. That's what definitely happens in these sessions compared to where the content and the audience side. We're thinking about how to talk to your audience, how you want to position stuff to audience. This is really maybe to set the scene a bit more. What do the agents do? The agents will look at your ICPs and personas. It will um figure out who is best for you to target. And so we'll use a bunch of lead databases, databases. You might have LinkedIn. And it goes through and it starts doing research on each of the possible leads that we could be reaching out to. That's really really really really important uh because we try to build up as much detail whether it's around their Facebook around their LinkedIn around whatever data is online around this particular person and when then we link it to our internal persona types as well.

### **00:05:48**

**Brett StClair:** So, if they're a CEO or they're a COO, um, we're starting to build up over time on those kind of more broader terms. um they prefer to be contacted in the morning. They you've got more luck with an outreach uh on a Monday afternoon. So we look at those kind of things. Then we also look at how we going to do an outreach.

**Ian Johnson:** Yeah.

**Brett StClair:** Is it which is the better channel? Uh what is the frequency? How long do we leave between each outreach? All of that is what we're building up in our repositories and our engines. And we're continuously refining these things. And so as we approach this, we're trying to figure out how do we help it target the right audience. It will do a fairly good job on doing the first set of kind of structures of what we wanted to say and how we wanted to say in the outreach based on the offer. And so the offer has got to be well defined.

### **00:06:44**

**Brett StClair:** So what are you offering? Why are you offering all that kind of stuff? Um then we try not to touch it. We let it optimize itself. Um, so the agent gets better at understanding how they respond, what's responded, and it will start refining that message better and better. You can see what it says. We've got full order trails and all that kind of stuff. So, we'll give you access once we've configured everything, but there's lots of moving parts on this. Um, as you can imagine, you'll have up to 200 outreaches. um I think it's a month on LinkedIn. Um because they got all these various constraints. So we don't want to blow out the LinkedIn kind of capacity. That's per week. Um so you want to be on sales navigator when we do the outreach. We want to make sure that your LinkedIn profile is where you want it to be. That's going to be important. And then we do outbound uh emails.

### **00:07:44**

**Brett StClair:** So outbound emails, I'll be bringing George in there. We're going to set up a bunch of um domains for you. Um well, you guys will need to set up on your side. So, it'll be like uh the TXN global um a TXN global, whatever. So, we've got a whole lot of rule sets around how to set that up and the type of names and emails that you need. And then what we do is we start a warming phase. And so it takes between probably about one and two weeks to warm up domains and emails depending on the state of your domains currently and the state of your emails. And you really have no idea. We have to run all the tests first. So we run all the different tests. We get a feeling on where it is. What you don't want to be doing is we're never going to be sending email campaigns, etc. out on your main domain. You've got to keep that as clean as possible.

**Ian Johnson:** Just tell me just a couple of couple of questions.

### **00:08:43**

**Ian Johnson:** So the first one is um so what role do you guys play if any role in identifying the target companies?

**Brett StClair:** So what we will do is our AI will help shape and I identify sets of companies. We will sit with you. So, Max will sit with you literally and we'll start going through email list. Do I like that? Does that feel right? Does this feel right? Is this who I want to be going after? You'll do like probably 3 400 and you'll get bored, but we'll have a good sense. Our agents will have a good sense of what's needed. And every time we go, well, this is what we've selected. We want more profiles like this. you will get to a point where you saturated um depending on where in the market, how you targeting, all those kind of things. Um I don't know how big your market is or how small it is. Um um but ideally you want to kind of saturate it if if if possible.

### **00:09:44**

**Brett StClair:** Um the numbers are big in this game because your conversion rates are like 0.01% 01% to get a response. Um, you're talking fairly big numbers on outreach. Um, you want to be protecting your brand. You want to be protecting um your domains. So, we put all those protections in place. Um, email converts less than LinkedIn. Uh, LinkedIn, if done right, you can actually get some nice responses from it and it manages the response.

**Ian Johnson:** Yeah.

**Brett StClair:** Um cuz once those responses start coming in from in from LinkedIn, by the way, your inbox just feels like chaos. Um let the agent manage it. It knows what it said to the person, how it said it. Its goal is to try to get you a meeting. That's what its goal is. Um so you have you guys run email campaigns before, by the way. I just want to get a sense of your experience in the email campaigns.

**Ian Johnson:** Well, I've run email campaigns previously. Obviously, we haven't run any at TXM because we're not we haven't launched yet.

### **00:10:57**

**Ian Johnson:** But yeah,

**Brett StClair:** Yeah. So, it's all about protecting the domain,

**Ian Johnson:** I think

**Brett StClair:** by the way, because you don't want to be hit by spam filters. You don't want to abuse the situation. You don't want to be just completely spamming them with rubbish. You want to be incredibly respectful as you're going through it. And then you want to pull out. Once it's too much, that's it. We qualify the lead out. You don't just continuously hammer

**Ian Johnson:** Yeah, I suppose. So, that was one of the things that I just wanted to touch on.

**Brett StClair:** it.

**Ian Johnson:** So, um, number one, I've got I've got a list that Claude pulled together as part of a overall go to market, um, planning exercise, which I can send across about 126 accounts they pulled

**Brett StClair:** Please

**Ian Johnson:** across Europe. Um, which I don't know. I'm still I'm still somewhat unconvinced that that's really a high enough number. I I think there's many more than that, but so I'm not quite that clear um how Claude is going about doing that.

### **00:12:01**

**Ian Johnson:** And bearing in mind, it's not using any paid subscriptions or anything to do any of that work. So, it's just basically what I can find um without subscription. So, I can send that across. I think just on the email domain things though, ultimately where we will end up is we will end up with a number of salespeople each of each of which will have a territory. um and that they will be responsible for outbound within their own name when it comes to making calls. I think I already replied an email and said, you know, I'm not for going down the path of AI outbound voice at this stage, but to

**Brett StClair:** By the way, we don't do AI outbound voice.

**Ian Johnson:** me

**Brett StClair:** We do inbound voice, which means if a lead comes in from somewhere, our agents will pick it up, respond via WhatsApp, do um a call back and all that kind of stuff. So, there's a reason why we don't do voice outbound. The regulations around it are really, really, really, really heavy.

### **00:13:16**

**Brett StClair:** And they have to have engaged with you because you can imagine a world where you just get a ton of telephone numbers and you just let this voice, this agent go

**Ian Johnson:** Well, let's let's figure that out when we get to that point because I think the the the notion of an immediate response to an

**Brett StClair:** crazy.

**Ian Johnson:** inbound lead is fine, but then that inbound lead needs needs to be picked up by a human at TXN rather than any kind of voice call from AI because the numbers just won't be bigger. We're not talking about 20 or 30,000 target accounts here,

**Brett StClair:** Great.

**Ian Johnson:** right? This is not going to be a mass thing. But specifically to the email domain piece, I'm unconvinced that there's a spam issue if an email is being sent from directly from an individual's account. Now, I don't see us necessarily sending emails from a TXN generic account um because I think that's too impersonal and it doesn't mirror the structure that we will have as a business as we start to bring salespeople in. So I think for me the the outbound piece is really about what of the heavy lifting can be taken away by you guys so that the salesperson's role is primarily to validate and um to and to make sure that the evolution the agency is coming up with is still staying

### **00:14:55**

**Ian Johnson:** in line with what the STR strategies either from company perspective or their own individual point of view um and then um ultimately to manage those LinkedIn and email campaigns. But to me the emails can go out in an individual's name with axm.global extension. So initially they would all go from me and then as we bring sales people on they'll start to go

**Brett StClair:** Yeah.

**Ian Johnson:** based on depending on whose territory the target belongs to. Does that make

**Brett StClair:** Yeah. So, we can do that. We can definitely do it from you.

**Ian Johnson:** sense?

**Brett StClair:** Um is better, right? It's not going to be a Hi there. This is a generic bot thing. It'll be addressed from you. It'll be from your email, but the domains will be not exactly TX's core primary domain. Um, just because we don't want to risk getting your core primary on any form of red list or spam list. um you want to keep that as so when I say clean that you shouldn't be sending high volume emails from there.

### **00:16:09**

**Brett StClair:** Um, and sometimes we can see literally by doing checks on people's domains, we can see if they've run a 500 kind of quick email push through Gmail kind of thing because it actually flags. Um, you get like kind of uh color gradient responses when we do checks. And so if it's sitting in amber, we know that the person's been trying to run some campaigns. And then what we do is we warm them. and we'll warm them with fake email addresses. Um, so the warming is just literally going through it's very cool generic kind of email. It's got nothing really to do with your business or harm. We pick like kind of targeted audiences and nothing to do with the domain and it warms it. It's actually like a process that it goes through. And what that does is it gets all the different mail serving engines kind of comfortable and gets you into the green on everything. Once it's in the green, then we're very, very careful to keep it in the green and we're continuously monitoring it.

### **00:17:08**

**Brett StClair:** I do agree with you. You want your outreach. Just got to set your expectations on the responses. The responses feel like nothing. So, everyone gets excited. It's like,"Yeah, I'm going to run like 500, 600 emails out. I can't wait. The money's going to stop pouring in." No, it doesn't. You'll be lucky if you get a response. Um, and so we then have follow-up responses that are built to kind of engage with the right audience. So, you know, like if it's a other salesperson, yeah, you're going to miss out on the opportunity, you know, or if it's a CEO, then it's, you know, we know we respect your time and everything. When's a good time to be able to and the AI works out how it's going to respond that way. Um otherwise you're writing a s\*\*\* ton of different uh like I've done some email campaigns in my Teraflow days where we were running a million emails a day. Um, and the sequencing and different campaigns that you have to run to be able to support that were vast, but we had such a broad market.

### **00:18:11**

**Brett StClair:** Um,

**Ian Johnson:** Yeah.

**Brett StClair:** you know, you're a technology services business.

**Ian Johnson:** Yeah.

**Brett StClair:** What can we do for you? Yes, we can do that. You know, so it was terrible. Um, but you've got a really nice niche specific, very focused kind of business. So, I think it'll do it'll do a lot better. I.e., not 0.01%, but 0.02%. Double

**Ian Johnson:** Yeah, like like I know I know what to expect when we do this stuff.

**Brett StClair:** um

**Ian Johnson:** I think it's just important to understand that we just need to think about when we start the outbound campaigns aligned with the content management piece as well and the launch overall because you know we

**Brett StClair:** Yes.

**Ian Johnson:** we need to try to start to warm the market um based

**Brett StClair:** Yes.

**Ian Johnson:** on you know the people that we're already connected to the people that um pay corp, direct transacts, all of those kind of things that broaden that reach in the LinkedIn network.

**Brett StClair:** you're talking about certain things that relate to when they reach out when you reach out to the base that are

### **00:19:17**

**Ian Johnson:** Um

**Brett StClair:** connecting to you. We're going okay now we're going to reach out to them via email or via a I'm seeing in stuff. Yes. Oh, that's tent. Yes.

**Ian Johnson:** correct

**Brett StClair:** That's the goal. That's why we like to do content workforce and outbound together. That's really important that we do. And I've actually just I've got the outbound to actually have a look at what your where you are

**Ian Johnson:** Yeah.

**Brett StClair:** with your content workforce and it's taken that into effect. And as we progress the content workforce, I'll keep getting it to update and look at that as well.

**Ian Johnson:** Okay. Cool. Okay.

**Brett StClair:** Okay. So,

**Ian Johnson:** Good.

**Brett StClair:** I'm going to share my screen. I'm going to it's a slightly different screen because I'm running um clawed uh code on this um and I've ingested everything. So, it'll be a dark screen. Um just let me know if I need to zoom in on it.

### **00:20:13**

**Brett StClair:** Um can everything everyone see this? Okay.

**Max Kingaby:** Yeah.

**Ian Johnson:** Yeah. Whoa.

**Dorte Dye:** Thank

**Brett StClair:** It's asking about pricing and packaging from Ian,

**Dorte Dye:** you.

**Brett StClair:** but that's just because I think somewhere you refer to that in your packs, but this should be teed up to do a set of questions. Can everyone read it? Okay. Okay.

**Dorte Dye:** Yep.

**Ian Johnson:** Yeah.

**Brett StClair:** And so again, how we'll manage it is the same way that Max is managing it. As you want to speak, I'll then hit the record button and it will do the necessary paste, etc. into it. Okay, for this first four blocking decisions, everything downstream in heresies

**Ian Johnson:** So just just on one I think let's be realistic about the fact that it's highly unlikely that um the CPO's heard of either TXN or direct transact. I don't see why anybody in Europe would really have any knowledge of a South African payment business to be to be brutally honest. So in the first cold email, I think we've got to think about what is the content strategy going to be in terms of how we set the scene.

### **00:22:29**

**Ian Johnson:** So yeah, it doesn't I I I'm comfortable that the CPO would never have heard of TXN. Can direct transacts name appear? Yeah, direct transacts and PayP's name can appear, but it's just as I've said, it's just not the lead message because nobody cares enough. If two if um you know Open AAI and Anthropic had decided to launch a business together, you can understand why OpenAI and Anthropic would be the would be a launch message and everybody would know who those two would be and they would be interested in understanding what happened. Um but ultimately it's not it's not going to be the thing that get grabs anyone's attention. the fact that direct transact and pay corpor have launched a business together. That being said, Brett, to be clear, and I'm talking to Bronwin on Wednesday, it might be when the initial press release stuff gets done that that that is the lead that Pay Corp and Direct Transact go with because they're announcing the fact that those two companies have launched a new company. Let's

### **00:23:49**

**Dorte Dye:** You're mute.

**Ian Johnson:** go mute.

**Brett StClair:** Apologies for that. Phone was ringing and I know it's a delivery, but I think we've got everything. Why is it not pasting? There we go. Um, so I got up to Brunin. You're going to have a chat to Bronnin.

**Ian Johnson:** Yeah. About So if you think if you think about how this is uh got to go. So, the first thing is there's got to be an announcement to the general market about TXN. And the only way to get any traction with that notice really is for that to come about the launch of TXN and the fact that TXN is a joint venture between Direct Transact and Pay Corp and then we can talk about what TXN is. Okay. So, that's the first thing you got to go out there and say,"Hey, there's a new company here." Um, in terms of when we get spec when we start specifically targeting uh target leads or when we as individuals start putting content out, the direct transact pay corp joint ownership shouldn't be ignored.

### **00:25:25**

**Ian Johnson:** but it's simply not the lead message. It It's something that needs to be announced and then after it's done, it's a reason to believe, but it's not the lead message. Um, in number two, the answer is either or. So there are occasions where we can authorize a transaction based on a balance that we hold on behalf of the client. Um but increasingly in this market it typically is that the authorization gets rooted to the customer for them to make a decision as to whether or not to authorize. But it's an either or. Sorry, it's it's both, not an either or. three. I mean, I would challenge why we're getting into that level of detail in outbound emails or LinkedIn anyway. Um the answer is that all client data is segregated, but Gotcha. um there are a number of components within the overall architecture that are effectively shared. So I don't think Dorte since I was away that we arrived at a point of um any deviation from that. So the original plan B was that each individual client would have their own environment.

### **00:27:26**

**Ian Johnson:** All of it.

**Brett StClair:** I

**Ian Johnson:** What DT came back with was um this kind of centralized

**Brett StClair:** remember.

**Ian Johnson:** resource that would manage um everybody coming into one central place and then um the APIs hitting segregated databases. Um,

**Brett StClair:** Okay.

**Ian Johnson:** however, we have the ability for clients to stand them up in a

**Brett StClair:** Yeah.

**Ian Johnson:** completely separate environment if that really is important to them. So, the the lead is and what we expect to be initially with the more standardized clients is that it's just the data that's segregated. There's obviously, you know, there's obviously protections in there through authentication and all those kind of different things, but the key thing being could one client take out all of the clients, that is still something that we consider to be a potential risk. So if there was a, you know, one client that started flooding the system with bad API calls or whatever it might be, is there a risk that that could impact other clients? Yes, we believe there still is a risk that it could impact other clients.

### **00:28:53**

**Ian Johnson:** Um, but that's an ongoing conversation with my myself and the guys at uh at DT about the architecture that has been proposed. But again, I think the key thing for me with three is I'm just not sure how important a message it is. And I'm not sure why it's uh not sure why either two or three are necessarily considered to

**Dorte Dye:** Mhm.

**Ian Johnson:** be blockers.

**Brett StClair:** I wouldn't worry about it so much. It's building this knowledge base right right now.

**Ian Johnson:** Yeah,

**Brett StClair:** So,

**Ian Johnson:** that's fine.

**Brett StClair:** it's looked at everything and there are a bunch of gaps that it's starting to see. So, it's going to probably walk us through the gaps initially and then start going,"This is what I think we should be doing.

**Ian Johnson:** So pricing. So how does actually pay you said as you'd say across the table? Uh okay. So there's the pricing is based on on two core principles. One is fixed license fee, monthly license fee. And the other is um per transaction or authentication fees that are based on um a tiered a volume tiered structure.

### **00:30:14**

**Ian Johnson:** So the more you process, the lower the individual unit fee is per transaction authentication. license is a flat monthly fee. You need to access

**Max Kingaby:** Sorry. Just

**Brett StClair:** Here we

**Ian Johnson:** the

**Max Kingaby:** Sorry,

**Brett StClair:** go.

**Max Kingaby:** I thought I was was on mute, but I didn't realize this guy was on call next to me. Apologies.

**Brett StClair:** Is the guy trying to call me?

**Max Kingaby:** No, there was some guy speaking Arabic or something down the phone and and I was just sat there going,"Oh, I'm on mute." But wasn't on mute for any of it and realized you heard his whole conversation. So, sorry.

**Ian Johnson:** Yeah, just reading that it's the it's the unit fee peruthentication.

**Brett StClair:** Trying to get a delivery in this building is almost impossible. Sorry, my apologies. Go for it.

**Max Kingaby:** I just saw George walk past with all the delivery stuff, right?

**Brett StClair:** Yeah, that's cool. He's still down there. If you if he's in the office, please tell him to go back down

### **00:31:59**

**Max Kingaby:** Okay. is in the office of E26.

**Brett StClair:** again.

**Ian Johnson:** Yeah, I mean there's some issues with the language that's written, but um the so the fees are there's one fee per settled transaction and there's one fee for each 3D secure authentication. Those are the volume based variable prices. And then there's the fixed monthly license fee which is effectively a fee per client to access the platform that includes the control center knowledge hub and unlimited API calls. And initially the plan is that will also include the the AI elements.

**Brett StClair:** So, how do we get this on here? Okay, just load this in. I'm not going to do a summary like we did last time. I want to give it the full load because I think now it's going to enter the actual interview phase. Okay, so captured fair challenge. You're right. Okay. Yep. Yep. Yep. Yep. Follow up. Balance is at launch. Fault vision says in the MVP TXN doesn't hold funds every authorization pass through you said there are occasions where TXN authorizes against a balance it holds okay don't know if we need this disclosure do we name numbers now bound blah blah blah blah I think the question is no and ignore ignore and no

### **00:34:44**

**Ian Johnson:** When you say disclosure, are they talking about disclosing prices? Uh,

**Brett StClair:** Yeah.

**Ian Johnson:** no.

**Brett StClair:** Um, let's worry about it later. For balances and disclosure, definitely no. Do not name numbers, please. Okay. Then it's saying point one. Describe what TXN sells as if to a technical friend. No marketing allowed.

**Ian Johnson:** So, TXN is a card issuing processing platform. So, we sit in between um a client who wants to issue cards to its customers, whether they're consumers or corporates. and the card schemes Visa and Mastercard. So there's two sides to it. One is allowing a client to be able to manage card holder. accounts so that they can effectively request cards whether they're physical or digital. So, Apple Pay or Google Pay. And then the other side of it is the pure processing which is um handling the messages that come from Visa and Mastercard. Whenever one of those cards is presented at any merchant around the world, um that will trigger a message to be received by us as the issuer processor to to manage that stage of the transaction.

### **00:36:32**

**Ian Johnson:** Typically, that message is a request for authorization. So we're managing okay we have a request from this merchant to authorize a request to authorize um spend on this card and then on the issuing side we will check either we will check the balance and any specific um restrictions that have been set on that card on the on by the client or we will route it to the client directly for them to answer um whether or not we approve or decline. So that's the kind of authorization flow. Then if the transaction is authorized, we will then receive messages from Visa and Mastercard confirming that that transaction has been completed and therefore on the issuing side we're advising the client that they need to pay Visa and Mastercard for that transaction. Obviously, we're aggregating all of that data that takes place each day to advise the client of all of the transactions of that day that have been authorized and cleared. And therefore, the client then knows, okay, this is how much needs to be paid in order to satisfy what is owed to Visa and Mastercard.

### **00:38:18**

**Brett StClair:** So, I'm amazed that it hasn't noticed my spinners.

**Dorte Dye:** Honestly, I did because I keep correcting mine as well. I spent the whole weekend in Claude Cord. I want to know

**Brett StClair:** Okay, here we go. Here's a question one back to you. Adjective stripped. How does that sound?

**Dorte Dye:** I think the um pick up this visa master card is good. We're launching this video. The massacre comes later As it said,

**Brett StClair:** Nice.

**Ian Johnson:** Yeah. Again, I I'm unconcerned about saying Visa and Mastercard because that's something that can be handled in the conversation that pretty much as soon as we're finished launching MVP will be that getting Mastercard certification that you'll be delighted to know is going to be the

**Dorte Dye:** Yes, it

**Ian Johnson:** number one. Um so I'm not concerned about saying it's Visa and Mastercard because ultimately um we can deal with that

**Dorte Dye:** is.

**Ian Johnson:** in conversation. Um terms of how it's been written the top piece pretty comfortable with it.

### **00:39:57**

**Ian Johnson:** There's more there's more data we can feed in that might help Brett. So M Mike is I don't know if he sent it to you as well, but Mike just sent me the draft knowledge hub content um to go through.

**Dorte Dye:** Mhm.

**Ian Johnson:** So think about it,

**Dorte Dye:** I got it.

**Ian Johnson:** Brett. The knowledge hub is the place where prospective clients will go to to understand more about TXN. Okay. Um, and in those guides that Mike has produced, there's quite a lot that talks about what our role is and what other how the how the whole end to- end card life cycle fits together. So once they're approved, which I don't anticipate taking very long because it's high priority from our point of view, we could theoretically send those across to you to ingest more of that information because that is going to be in the public domain. We are going to be saying these things to people. Whereas some of the other documents you've seen so far, well, all of them are internally fa focused.

### **00:41:18**

**Ian Johnson:** So that how we talk about the product and the platform internally, not necessarily how we'll talk about it

**Brett StClair:** Nice.

**Ian Johnson:** externally.

**Brett StClair:** Yeah, those will help big time. Um, so did you see the last point on question one?

**Ian Johnson:** What single outcome the client is paying for?

**Dorte Dye:** Let's

**Brett StClair:** Can you please suggest five options that you think could be the single line that we could use for question one?

**Dorte Dye:** go.

**Brett StClair:** Let's see what it says. Sometimes in these scenarios, it comes up with some options and we can rework those options cuz that's hard. You comfortable with that?

**Ian Johnson:** Yeah.

**Brett StClair:** Anything kind of tickle your fancy combination of stay away or let's take one and and work it a bit.

**Ian Johnson:** Not really.

**Brett StClair:** I don't like any of this. I think you're trying to be too fancy.

**Ian Johnson:** No.

**Brett StClair:** Let's just do a single simple line about what TXN is. Give me five examples. They're trying to be too

**Ian Johnson:** I think there's two things there.

### **00:43:52**

**Brett StClair:** wordy.

**Ian Johnson:** There's there's this where it's more of

**Brett StClair:** See like

**Ian Johnson:** a it's more of a tagline versus what is it that you guys actually

**Brett StClair:** Correct. Yeah, this is a what what actually do you do in one

**Ian Johnson:** do?

**Brett StClair:** line?

**Dorte Dye:** B is awful. See,

**Brett StClair:** Should

**Dorte Dye:** I don't know. I don't like any of them. I don't I don't like the modern card this year because everyone keeps saying

**Brett StClair:** we insurance provider saying they're technology based

**Dorte Dye:** that.

**Brett StClair:** brokers?

**Ian Johnson:** I think I think D is the one that's probably got the most opportunity which is to me I think the key thing is TXN is a coition platform for any company launch launching and operating a payment card program or something along that. I think that the key part for me is that it's any. So it doesn't matter who you are. You don't have to be a bank, don't have to be you can be somebody a trade platform, you can be a marketplace, you can be whatever.

### **00:45:22**

**Ian Johnson:** It's anyone. And and that is what we are. with the platform for anyone who wants to launch and operate their own or run their own car program. I think if we think about the target audience, Brett, and the people that we're targeting, if we if we've done that part properly, then we won't have to explain too much. about things like what is a car what's a car program. Um so to me it's kind of all right. I mean again it depends on what's being used for.

**Brett StClair:** It is

**Ian Johnson:** Um the the bottom line is whoever receives this

**Brett StClair:** awesome.

**Ian Johnson:** outbound should know broadly what a card what a card issuing platform is and that you need one for a card program. If we if we go back to content work that we did that we're still doing we had those two distinct types of companies that might launch a card program. You had one where it was core, so you have to do it. So, it's it's a part of the product, so you have no choice.

### **00:46:46**

**Ian Johnson:** In which case, you probably know um more than the other um type, which is a company that doesn't really know an awful lot about launching and running card programs, but sees an opportunity to create more value in their business and for their clients by launching the car program. those people probably need a we shouldn't assume that they're necessary as though it favor with some of the language. So to me, you have to keep the language as simple as possible if it's going to be generically used across the board. But D is the closest one for

**Dorte Dye:** Agreed. If you change the four to any then it's

**Ian Johnson:** me.

**Brett StClair:** Any

**Dorte Dye:** powerful.

**Ian Johnson:** I don't want I don't want to run a car program though, just for the record.

**Brett StClair:** particular one has given has some more options. Looks like three

**Dorte Dye:** What was

**Brett StClair:** more.

**Dorte Dye:** programs?

**Brett StClair:** By the way, this is it's important that we do to spend time here. So, like let's take the time.

### **00:48:24**

**Dorte Dye:** I would say

**Brett StClair:** Let's say one.

**Dorte Dye:** one.

**Brett StClair:** Do we want to do you want to is the words quick, simple, needing to be in there? Effective, efficient.

**Ian Johnson:** That's what I was just thinking again trying to understand what this sentence is going to be used for because if I look at one and let's let's follow you what you said look um d about that being the best one if it's being used as some kind of a tagline or something in, you know, in an email, then to me, we can get rid of card issuing platform and we can say TXN is the platform for any company launching or operating same card program because you're making more of a bold statement that we are the

**Dorte Dye:** Yeah, like

**Ian Johnson:** platform.

**Dorte Dye:** that.

**Ian Johnson:** That's that would be that's again it still describes what we do.

**Brett StClair:** Let's see if see what it comes up with. TXN is a card issuing platform for any company launching and operating its own anchor line. TXN is the platform for any company launching and operating a card program.

### **00:50:26**

**Dorte Dye:** Yeah, the anchor looks better.

**Ian Johnson:** You really are a geek, bro. I've got time. Yeah, I like working with you guys, but I keep reading the this sort for 12 seconds, breathe for 17 seconds. The thing about the whiteboard, I'm like, it has time to do this

**Max Kingaby:** It was it was cuz we went to the toilet,

**Ian Johnson:** stuff.

**Max Kingaby:** left our me and Brett Brett and I both left our laptops open and George had come back and changed all of ours to say I am a loser. I you know I am s\*\*\* in my job and and then we had to learn how to change it back.

**Brett StClair:** Then we thought we'd do fun things like take the piss out of corporate and enterprise working

**Ian Johnson:** Lily, your dad's a geek. If you haven't figured out already your dad's a geek,

**Brett StClair:** conditions.

**Ian Johnson:** don't don't don't let it kind of infiltrate you and catch it from crying out loud. It's already too late for Max.

**Dorte Dye:** It's the best way of

### **00:51:58**

**Max Kingaby:** To be fair, to be fair, I'll take it.

**Dorte Dye:** learning.

**Max Kingaby:** I just got called a geek there. I'll take that.

**Brett StClair:** So let's go with the anchor angle.

**Ian Johnson:** Mag.

**Brett StClair:** You can start seeing what it's trying to do now, right? It's going, okay, so what confuses people, you know, when if you're in the market, what do you sometimes get confused with? Um it I think that where we're going now is around the pigeon hole. Sometimes you want to create a bit of a pigeon hole so you are put into that bracket quite easily so you can find the right people. You can get into the apples and pears conversations. Um any views on that line

**Ian Johnson:** I think for me f firstly

**Brett StClair:** here?

**Ian Johnson:** we don't we have to imagine what we might be confused we're in the market because we're not in the market. As it said already from some of the objection material, things that we are very clear that we want to avoid is giving the impression that these two companies, Pay Corp and Direct Transact are launching a a joint venture company that is basically just there to target companies outside of South Africa.

### **00:53:35**

**Ian Johnson:** So it's not it's not any different. Um and that be because of the legacy sorry because of the heritage in processing there's an assumption that therefore we have a legacy platform. So if you say direct transact as one of the owners has been operating has been issue an issue process for 25 years that automatically in my opinion runs a risk of somebody going,"So your platform's 25 years old?" No, no,

**Dorte Dye:** Yep.

**Ian Johnson:** it's not. And therefore the the challenge is to ensure that it's the knowhow and the heritage of these two companies plus their money that is the thing that TXN utilizes. But from a technology point of view, the focus needs to be on what TXN as a individual independent company is bringing to market and why. So the things for me Brett what one of the things that's the biggest challenge is how do we talk about you know for me first and foremost I've always believed that the only place that you can compete in this marketplace well they can compete on price but we're not going to do that no one's interested in doing that but really is in the experience that clients have.

### **00:55:16**

**Ian Johnson:** So, how easy is it to be able to do the things that clients want to do? We talked about the content piece. Um, so not having to have expertise. Um, not having to employ large groups of people on the client side to be able to manage programs, etc. Um, and some of the content stuff that we're doing around the how we're using AI to deliver those some of those outcomes is important, but I want to avoid doing what some of our competitors do, which is, you know, some of them there's there's a competitor called Thread who have suddenly announced themselves as the AI issue No, no, they're not. It's absolute nonsense.

**Dorte Dye:** It just

**Ian Johnson:** It So,

**Dorte Dye:** seemed

**Ian Johnson:** we we are going to have people who increasingly will use AI powered or whatever else it might be. But as you know because you've been involved in these conversations for a very long time. Yes, we have been thinking about this from day one but not about how do we use AI but how can AI help us deliver this vision of giving the best possible customer experience.

### **00:56:44**

**Ian Johnson:** Um, and I think that's the that's the nut that we've got to somehow crack in terms of how we position ourselves. So yes, we don't want we don't want people to think TXN is basically a wraparound a legacy platform. Number one. Number two, we don't want people to think that we're just another card issuing platform that has decided to stick AI in its marketing collateral without actually having really done anything of any substance. So that's the those are the things that we've got to balance really.

**Brett StClair:** I think that's really good. And bear in mind when you are in the market and you're sitting in front of your customer and you're talking them through and you're testing lines and you're testing approaches, you can also then come back and we can re realign this continuously, right? Um, okay. Let's see what it said.

**Dorte Dye:** Yeah. And where we compete is good.

**Brett StClair:** I agree. By the way, what I like about this skill is it'll pick up stuff that isn't that is relevant in other questions and preload into the questions as well.

### **00:58:57**

**Brett StClair:** So, check it out. It's picking up core messaging for question 10\. It'll load in there.

**Ian Johnson:** Yeah.

**Brett StClair:** picked up as threads. Uh threats

**Dorte Dye:** That's right.

**Brett StClair:** So before we go into the next one, yeah, what what does TXN sell? I mean, does TXN sell anything in this offer that hasn't covered so far? So, are we missing anything? Are there any kind of core offerings that you want to call out, I guess?

**Ian Johnson:** That is it for today.

**Brett StClair:** Yeah, I think that's it. What I'm going to do is I'm just going to get it to do a where we are status kind of print out to HTML. I'm going to send that to you guys so you can have a review. Um we've got two more sessions and we'll walk through it. Um do can I grab some time with you? I mean uh have a look through diaries and see if we can get two more for the content

**Dorte Dye:** Yep.

**Brett StClair:** workforce and let me know if we got gaps.

### **01:01:06**

**Dorte Dye:** Never mind.

**Brett StClair:** It's Max and myself. So, um,

**Max Kingaby:** What?

**Brett StClair:** morning's also pretty free. We don't have to worry about a George or

**Ian Johnson:** Just out of interest,

**Brett StClair:** son

**Ian Johnson:** uh, Brett, have you talked to have you ever talked to Bronwin about the content workforce stuff? I don't mean in relation to TXN,

**Max Kingaby:** Yes.

**Ian Johnson:** I mean just generally.

**Dorte Dye:** Yeah.

**Ian Johnson:** No.

**Brett StClair:** no.

**Ian Johnson:** Okay.

**Brett StClair:** Uh we've done it in a TXM context and then just generally took her through it so she has a a good sense of what the content workforce is.

**Ian Johnson:** Oh, so she

**Dorte Dye:** Yes.

**Ian Johnson:** does.

**Dorte Dye:** We had we had a good session and I think she was interested in maybe to utilize it for the payrop

**Ian Johnson:** Okay. I didn't I meant to join the dots on that. I know that before I went away and asked if it could you can have that session.

**Dorte Dye:** group.

**Brett StClair:** Yes,

**Ian Johnson:** That's fine.

### **01:01:57**

**Brett StClair:** that's the session we've had. Yeah.

**Ian Johnson:** Okay. Excellent. All right. Good.

**Brett StClair:** I think she wants to keep an eye, see how you guys go.

**Max Kingaby:** You're the guinea pigs.

**Ian Johnson:** Yeah. Yeah, I can completely understand.

**Brett StClair:** Yeah.

**Max Kingaby:** What did you guys think of the manifesto document that I uh sent you?

**Ian Johnson:** Okay.

**Max Kingaby:** Was that all all good in the end?

**Ian Johnson:** I need to take a a look at it, Max.

**Max Kingaby:** Awesome.

**Ian Johnson:** I still have a look at it um today and come back to you. But I mean, as it was as we were going through it, I felt comfortable that we're in the we're on the right track, for sure.

**Max Kingaby:** Yeah.

**Ian Johnson:** Um I I think in my mind, the the big thing is just going to be the layering of the messages. I had so ultimately and I'll talk to Brahman about this on Wednesday and talk to Steve you know pay tomorrow first and foremost DT and payor Have TXN TXN can't announce itself and expect anybody to be remotely interested.

### **01:03:05**

**Ian Johnson:** I mean um and that in itself would at least just for for people that follow DT pay whatever it is might be on LinkedIn for those networks pick up from

**Dorte Dye:** Yep.

**Ian Johnson:** uh industry bulletins, blogs, whatever it might be that will at least see the thing. The next thing we just need to think about what comes next from the content point. So um you've then got three people who've got some form of network across LinkedIn and myself, Mike and and Da and then it's what do we do what are we going to do next from a from a content point of view. So I see it as DT and pay court first as three next and then that has somewhat at least through a network a kind of networking um approach at least got the name out there and a little bit of the story out there and then at least there's something that's got that's announced TXN on as broad a reach as we can from those individuals and then we can start as TXM starting to launch content and our individual content.

### **01:04:33**

**Ian Johnson:** Um, so I'm going to go I I'm happy with where it's going. I I genuinely am happy with where we're going. I just want us to make sure that um we're we're clear not just on on what we can do with you guys, but how it f fits in with the overall approach to launching from a go to market point of view. That's all. But I'm I'm good with where we're going with it.

**Brett StClair:** Brilliant. Okay,

**Ian Johnson:** Okay.

**Brett StClair:** thank

**Ian Johnson:** I'll leave I'll leave you a lot to do geek geeky things.

**Brett StClair:** you.

**Ian Johnson:** Um D is going to get next sessions in right

**Dorte Dye:** Yeah. I mean, we have to borrow one anyway with George, right? There was one where we need Mike and George or was it just

**Ian Johnson:** we

**Dorte Dye:** George?

**Brett StClair:** Um George is going to step in once he can see a certain amount of work. And what we need him to do is he's going to be um it'll be around the email configs and setting up all the

### **01:05:30**

**Dorte Dye:** It's

**Brett StClair:** emails and what needs to be set up and how we're going to warm them up. So I reckon what we'll do is maybe we set up a half an hour session and I don't know Ian if you need to be part of that. We'll just get Mike. And who runs your domains?

**Dorte Dye:** Jacob. Hope everybody Watch out

**Brett StClair:** Okay. So, we'll sit with you then.

**Dorte Dye:** yet.

**Brett StClair:** We'll give you kind of what we need and how we need it. And George is going to have to run with that. He's got all the text specs.

**Ian Johnson:** and then we've got staff works conversation later today.

**Max Kingaby:** Nice. Yeah.

**Dorte Dye:** Yes.

**Max Kingaby:** Till

**Brett StClair:** Is it Is it confirmed?

**Ian Johnson:** Right.

**Dorte Dye:** Yeah. Even though No,

**Brett StClair:** Eh,

**Max Kingaby:** four.

**Dorte Dye:** I've sent Armand Sher to just check if they're okay with it, but I had he hadn't replied yet.

**Brett StClair:** okay. Cool. Good cool.

**Dorte Dye:** So, I I guess it is on.

**Ian Johnson:** See you later.

**Dorte Dye:** Okay.

**Brett StClair:** Happy.

**Dorte Dye:** Speak later.

**Max Kingaby:** Cheers guys.

**Brett StClair:** Awesome.

**Ian Johnson:** Thanks.

**Max Kingaby:** Bye.

**Brett StClair:** Byebye.

### **Transcription ended after 01:06:58**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*