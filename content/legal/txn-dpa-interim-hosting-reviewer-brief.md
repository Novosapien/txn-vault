---
description: "Reviewer brief for the interim-hosting DPA: why a separate instrument, the positions taken, the negotiables and floors, and the open variables before signature"
---

# Reviewer brief: Data Processing Agreement (Interim Hosting)

**Instrument:** [[txn-novosapien-dpa-interim-hosting]] · **Companion:** [[txn-novosapien-data-protection-guidelines]]
**Draft v0.1, 13 November 2026.** For Brett's review, then TXN's counsel.

---

## 1. Why this exists, and why it could not wait for the MSA

Ian stated it on the 11 November call ([[2026-11-11-personal-data-alignment]]): there is no signed
agreement and no data processing agreement, and the hosting arrangement must be papered **before
launch**. His reason is the correct one. The GDPR position was not live two months ago because
Novosapien was not storing or hosting anything. It now is.

The MSA ([[txn-agentic-ai-layer-msa]]) is drafted to v0.3 but unsigned, and launch is days away. This
DPA therefore **stands alone** (clause 1.3) and takes effect whether or not the MSA is signed. On MSA
signature it is appended as an appendix and continues to govern the Interim Service. That matches the
structure both sides agreed on the call: standard terms, with an appendix per service bought.

## 2. The factual correction that drives the whole document

**MSA Schedule 3 is wrong about the interim service**, and would have been bounced on it.

| MSA Schedule 3 says | Reality for the Interim Service |
|---|---|
| Production runs in TXN's European Azure environment, managed by Direct Transact | Novosapien hosts it in **Novosapien's own Azure subscription**, North Europe (Ireland) |
| Hosting is provided by TXN or its partners; Novosapien has no liability for it (clause 4.6) | Novosapien hosts it, so clause 4.6 does **not** cover it |
| Model providers are Novosapien's sub-processors pre-cutover, TXN's after | Correct, and now also true of **Microsoft** and **Sentry**, which Schedule 3 never listed |
| Backup and DR are TXN's responsibility (Part C(j)) | For this node they are **Novosapien's** (Annex B(k)) |

This is Dörte's 27 October question answered on paper: *"where is that all sitting, are you liable
because you're hosting."* For the Interim Service the answer is yes, and the document says so rather
than inheriting an exclusion that does not apply.

**Sub-processors named for the first time:** Microsoft (Azure, Ireland), Google (Vertex AI, EU
multi-region), Sentry (Frankfurt). Anthropic and OpenAI are **not** listed, because the interim service
does not use them. LangSmith and Supabase are expressly out, and the outbound firewall blocks both.

## 3. Positions taken, and why

| Position | Where | Rationale |
|---|---|---|
| **Scope lock**: public documentation only, no client data, no credentials, no TxnGlobal.API, mock API only | 1.2 | This is the whole risk argument. It cannot change without TXN's written agreement and an updated Annex A |
| **Full Article 28(3) obligations**, eight lettered paragraphs | 3 | [[txn-counterparty-review]] flagged that listing the facts of processing without the obligations would get both documents bounced by TXN's DPO. Fixed here |
| **24-hour breach notification**, by email and telephone | 7 | House floor. Supports TXN's own 72-hour Article 33 window. Confirmed deliverable by Brett, July 2026 |
| **Access is controlled by the agreement, not a claim of impossibility** | 6.2 | George's honest admission on the call was that Novosapien *could* open the Front Door logs. Ian's answer was that this is true of all IT and the control is the agreement. 6.2 is that control: a binding undertaking not to access or correlate except for a named purpose, every access by a named individual and logged, and no approaching an ISP to identify an IP holder. **This is the clause Ian is actually buying** |
| **Zero data retention before go-live** | 5.3 | Two limbs, deliberately. Caching is disabled from go-live and is entirely in Novosapien's control. The abuse-monitoring exception needs Google's approval, so it is drafted as requested before go-live and effective on approval, with a written notice to TXN if it is not granted. An unconditional promise on a third party's approval would be a standing breach |
| **20 Business Days' sub-processor notice** with a right to object and terminate | 4.2 | Standard, and more generous than the MSA's "prior written notice" with no period |
| **Deletion confirmed in writing within 10 Business Days** of cutover | 10.2 | Direct Transact asked for this explicitly at Q01(g) |
| **£100,000 liability cap**, one pool with the MSA | 12.3, 12.4 | See section 4 |

## 4. The commercial variable to settle: the cap

**£100,000 is the one number in the document, and it is Brett's to change.**

The reasoning: the Interim Service holds no client data, no cardholder data and no credentials. The
worst realistic loss is visitor IP addresses from a 30-day firewall log plus chat text that visitors
were told not to put personal data into. £100,000 is well above a plausible loss on that footprint and
sits comfortably inside the £1m cyber cover Novosapien already holds.

**The argument against it**, which TXN's counsel may make: the MSA carries a £250,000 data protection
super-cap, and this is the one service Novosapien actually hosts, so a *lower* cap on the hosted
service reads the wrong way round. The answer is scope, not confidence: the MSA cap covers Console
user data and support access across the whole platform; this covers a public documentation assistant.

Clause 12.4 stops the two stacking. A claim on the same facts is capped once, at the **higher** of the
two. That protects Novosapien from double exposure and protects TXN from the cap being argued down.

**If pushed, the fallback is to mirror the MSA at £250,000.** It is affordable against the cyber cover
and it removes the only line in the document a counterparty is likely to spend time on.

## 5. Negotiables and floors

| Term | Hold | Floor / trade |
|---|---|---|
| Scope lock (1.2) | Hold absolutely | Not negotiable. Everything else rests on it |
| 24-hour breach notice (7.1) | Hold | Do not agree "immediately" or 1 hour without a rota that supports it |
| Liability cap (12.3) | £100,000 | £250,000, mirroring the MSA. Never uncapped |
| Audit, once per 12 months, 20 BD notice (11.2) | Hold | Unlimited audits on demand is the thing to resist; a breach already unlocks extra |
| Sub-processor notice, 20 BD (4.2) | Hold | 30 BD is acceptable |
| ISO 27001 / SOC 2 (Annex B(l)) | **Claim nothing** | Novosapien holds neither. Do not accept a drafting change that implies otherwise. A good-faith alignment roadmap is the most to offer |
| Governing law, England and Wales (13.4) | Hold | TXN is in Cyprus and may ask. Flag to counsel before conceding; it changes every other risk assessment |
| TOMs (Annex B) | **Every line is what Novosapien actually does today** | Do not let a redline add a measure that is not operated. An agreed TOM that is not performed is a breach from day one |

## 6. Open before signature

| Item | Owner |
|---|---|
| TXN's Cypriot company (HE) number | TXN |
| TXN's named contact for instructions and breach notice (Annex A) | TXN |
| TXN's notice email address (13.2) | TXN |
| Confirm the cap at £100,000 or £250,000 | Brett |
| Disable model prompt caching, request the abuse-monitoring exception | Novosapien, before go-live |
| Browser identifier to session storage, and stripped on write to the long-term store | Novosapien, before launch |
| Confirm the launch date, 16 or 17 November | TXN (Ian), [[open-questions]] #130 |

## 7. Honest limitations

- This is a competent first draft, not a solicitor's sign-off. It should be reviewed by a qualified
  solicitor before execution, and TXN's counsel should confirm the Cyprus-specific points: the local
  implementation of Article 5(3) of the ePrivacy Directive, and the legitimate interest assessment.
- **The legitimate interest assessment does not exist yet** ([[open-questions]] #129). The DPA puts it
  on TXN at clause 2.4, which is correct in law, but Novosapien owes the factual input.
- Annex B states the measures Novosapien operates for this service. It makes no certification claim and
  should not be edited to imply one.
- This DPA covers the **Interim Service only**. Support and maintenance of the AI layer, which Ian
  wants papered immediately after launch, still has no instrument. MSA Schedule 3 should be rebased on
  the corrected hosting premise in section 2 when the MSA next moves.
