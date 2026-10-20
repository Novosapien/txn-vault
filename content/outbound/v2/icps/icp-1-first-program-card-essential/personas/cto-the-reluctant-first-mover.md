---
description: "TXN ICP 1 buyer persona v2: the CTO or Head of Engineering who must approve an integration in a domain the team has not worked in; technical veto. The 12-section persona, ready to load, with its sources and gaps below"
status: draft, 19 Oct 2026, reworked from personas-icp-1.md (4 Sep)
---

# ICP 1 persona: CTO or Head of Engineering

> **Up:** [[icp-1-first-program-card-essential|ICP 1]]. The text between the two horizontal rules follows the 12-section persona standard (`cofounder: …/concepts/guidelines/buyer-persona.md`) and is what loads into the product's persona `definition`. Message rules live in the [[messaging-protocol|messaging protocol]], not here. Every quote is derived, not heard from a buyer.

---

### CTO or Head of Engineering (Approver, technical veto)

**1.0 Archetype Name** The Reluctant First Mover

**2.0 Role & Functional Identity**
- **2.1 Primary Function:** Owns the technical relationship with the platform, and must approve an integration in a regulated domain the team has not worked in.
- **2.2 Core Responsibilities:**
  - Judging the platform on its API, its behaviour under failure and its operating model, not on its screens.
  - Owning the integration with the company's product, ledger and internal systems, for as long as the company exists.
  - Deciding where the authorisation logic lives: with the company or with the platform.
  - Being the escalation point for every processing problem, whoever caused it.
- **2.3 Scope, Seniority & Authority:** Scope: department to business. Seniority: executive. Decision Authority: an absolute technical veto and a joint say on the vendor; owns engineering hiring; does not own the commercial decision.

**3.0 Psychographic Profile**
- **Identity & Self-Image:** The person who keeps the promises other people make. Pragmatic, and proud of never having shipped something that took the company down.
- **Core Values / What They Optimise For:** Predictable behaviour under failure. What the system does when something upstream is wrong matters more than the happy path.
- **How They Measure Their Own Worth:** By what does not happen: no incidents, no surprise dependencies, no decision that has to be unwound later.
- **Worldview & Biases Toward This Category:** Assumes documentation describes the best case. Reads a developer portal as a reference for the company behind it. Distrusts anything called intelligent until told exactly where it sits in the request path.

**4.0 A Day in the Life**
They are asked to sign off an architecture in a domain where they cannot yet tell a good answer from a plausible one. Normally an hour with a vendor's documentation tells them whether the vendor knows its job; here the documentation mostly teaches them the vocabulary. The architecture document they must present has open unknowns in it. Whatever they choose, every processing problem the company ever has will reach their desk.

**5.0 Pains & Fears (Expanded Dossier)**
- **5.1 Operational Pains (Daily Fires):**
  - **"I am evaluating a regulated system with nothing to compare it against."** I can assess an API; I cannot yet tell whether the operating model behind it is normal.
  - **"Every question about failure gets answered with a feature."** I asked what happens when the platform is unavailable mid-authorisation and got a paragraph about resilience.
  - **"Half of what I need is in scheme specifications, not in the documentation."** So I depend on the vendor's own account of the vendor.
- **5.2 Strategic & Political Pains:**
  - **"I hold the veto and have the least evidence I have ever had for using it."**
  - **"This decision outlives me in the role."** Card platforms do not get swapped casually.
  - **"Product is choosing and engineering is carrying."** The selection follows product criteria; the consequences are operational.
- **5.3 The Deepest Fear:** A live incident, on money, caused inside the platform, with a fix that is not theirs to make, and having to tell the founders they do not know when it will be resolved.

**6.0 What They've Already Tried (and Why It Disappointed)**
- **Read several vendors' API documentation in full:** learned the shape of the domain, and nothing about who behaves well when something breaks.
- **Asked directly about failure modes, retries and stand-in processing:** got marketing language more often than mechanism.
- **Tried to hire someone who has done this before:** slow and expensive, and that person would become a single point of dependency.

**7.0 Decision Criteria & Objections**
- **What they weigh evaluating this category:**
  - Whether everything is reachable through the API, or the screens can do things the API cannot.
  - Whether a sandbox call and a production call behave the same.
  - Whether the company can take the authorisation decision itself, in real time, when it wants to.
  - What is logged and auditable, and whether anything non-deterministic sits near the transaction path.
- **Objections / sources of resistance:**
  - "Can I control authorisation decisions in real time? What happens if my system is down?"
  - "Show me your retry and webhook failure model. How do I know I received every event?"
  - "You have no live clients yet. Nobody has run this under load."
  - "Who holds the PCI accreditation: you, or the people running your infrastructure?"
  - "If I cannot get a working sandbox integration in an afternoon, I am not interested."
  - "Where exactly does the intelligence layer sit? If it is anywhere near authorisation, we are done."

**8.0 Trigger Events (Why Now)**
- The core banking or ledger platform going live, which makes the card the last unknown in the architecture.
- A launch date agreed without them, which turns an evaluation into a deadline.
- A failed attempt to hire card or payments expertise.

**9.0 Information Diet & Trusted Voices**
- The vendor's developer portal and sandbox, read as evidence about the company. A gated sandbox is a bad sign.
- Engineering peers at companies that already run a program, asked privately for the operational story.
- Status pages and public incident histories.

**10.0 Success Metrics (What "Good" Looks Like)**
- From an architecture document full of unknowns, to one where every dependency and its failure behaviour is written down.
- From a sandbox that only approximates production, to one they trust enough to test against.
- From needing a card specialist on the team, to an integration their existing engineers own.
- From being the escalation point for problems they cannot fix, to operations making their own configuration changes without an engineering ticket.

**11.0 The Message That Lands**
Speak about mechanism, not outcome. Two structural facts earn a reply: everything is available through the API before it appears in any screen, and the intelligence layer runs alongside the platform, outside the real-time transaction path, with a person in the decision loop.

**12.0 Example Titles**
Chief Technology Officer · VP Engineering · Head of Engineering · Head of Platform · Technical Co-Founder

---

## Sources

| Part | Source |
|---|---|
| Role (approver, technical veto) | The ICP 1 buying group in [[icp-definition]] §10 (Novosapien drafting): the CTO validates feasibility and holds the veto. Not confirmed by Ian for ICP 1 |
| Sections 2, 3, 4, 6, 8, 9, 10 | Derived by Novosapien from ICP 1, the offer and the 4 Sep persona. No buyer was interviewed |
| Section 5 pains | Derived from the ICP 1 pains and from Ian's primary-user scaffold ([[persona-primary-user]] §5: authorisation control, failure behaviour). Every quote is derived |
| Section 7 objections | Ian's primary-user scaffold ([[persona-primary-user]] §7): real-time authorisation control, system down, retry and webhook failure, sandbox in an afternoon. "No live clients yet": Novosapien, from Ian's 25 Aug remark on track record ([[outbound]], no transcript). The PCI question: the 4 Sep persona; the offer's credentials section holds the answer |
| Section 11 | [[offer]]: step 9 (API first), step 10 (intelligence layer outside the transaction path, a person in the loop) |

## Gaps to settle

| Gap | Why it matters |
|---|---|
| Does the CTO hold a veto in ICP 1? | Sets how the CTO message is pitched |
| Real buyer language for the quotes | Every quote is derived; Ian and Dorte should correct them |
| Triggers and information diet | Derived from the ICP signals and role conventions, not from real deals |

## What was cut from the 4 Sep version

| Section | Removed or changed | Why |
|---|---|---|
| 2.2 | "Holding the veto, and knowing that a veto exercised on instinct costs credibility" | Repeated in 2.3 and 5.2 |
| 4 | First person changed to third person; "forty minutes", "four times", "on Thursday" | Invented specifics; the gold example is third person |
| 6 | "Four vendors", and "a genuinely good answer from a person who then left the process" | Invented specifics |
| 6 | "Sketched the pieces they could build themselves" | Same attempt as the CPO's in-house scoping |
| 7 | Objection "Which of these do you hold today, and which are you building towards?" | Covered by the PCI objection |
| 7 | Objections from Ian's primary-user scaffold added (real-time control, system down, retry and webhook failure, sandbox in an afternoon) | Grounds the objections in a TXN document |
| 8 | "A regulatory authorisation progressing"; "a security or architecture review scheduled by an investor" | The first sits with the CPO; the second is invented |
| 9 | "Scheme and regulatory primary sources"; "reachable through technical substance rather than outreach" | Low value; channel guidance belongs in the [[messaging-protocol|messaging protocol]] |
| 11 | "Acknowledge the pre-launch position"; the accreditation wording (PCI held by Direct Transact); "do not lead with the owners"; "do not compare with a named competitor" | Message rules, now in the [[messaging-protocol|messaging protocol]]. The PCI answer stays in the offer |
| 12 | "Director of Payments Engineering" | Trimmed list |
