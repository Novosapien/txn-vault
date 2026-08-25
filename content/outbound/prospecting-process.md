---
description: "TXN's seven-stage prospecting process from account discovery to booked meeting, including the three discovery sub-scans, Freshsales model, and phased rollout"
---

# TXN Prospecting Process (v0.4)

> **Source of truth:** `TXN_GTM_Prospecting_Process_v0.4.docx` in the outbound folder (`programming/txn/outbound`, mirrored at `shared/clients/txn/outbound`), delivered by Ian Johnson on 24 August 2026. This page is a readable mirror. Edit the source document, then re-mirror. Routed from [[outbound]].

---

TXN Global
GTM Process Document
Prospecting Process
End-to-end from account discovery to meeting booked
Version 0.4   |   Author: I. Johnson   |   13/07/2026

## 1. Document Control
| Version | Date | Author | Owner | Description |
| 0.1 | 08/07/2026 | I. Johnson | I. Johnson | Initial version. End-to-end process definition with recommended tooling stack as open decisions. |
| 0.2 | 08/07/2026 | I. Johnson | I. Johnson | Five changes reflecting owner review. (1) Reframed LinkedIn constraint as ToS-driven, not Claude-specific; codified the human-plus-Claude workflow with Sales Navigator. (2) Restructured into Phase A (manual, low-volume, Stage 1 first) and Phase B (automation, only if warranted). (3) Added LinkedIn to Stage 1 sources and added a trigger-sources table. (4) Dropped dedicated sending domain from the immediate critical path; Phase A uses the owner mailbox at low volume. (5) Changed footer address recommendation to TXN's registered business address. |
| 0.3 | 13/07/2026 | I. Johnson | I. Johnson | Added Section 4.1.2 Multi-market discovery cadence. Codifies the operating rule that Stage 1 account seeding and trigger logging must both be completed for the current market before starting discovery for the next market. Prevents the pattern where account inflow outpaces trigger enrichment and leaves the Priority tier structure misleadingly low across the pipeline. |
| 0.4 | 13/07/2026 | I. Johnson | I. Johnson | Added Section 4.1.3 Use-case-driven discovery. Adds use case as a third discovery lens alongside geography and sub-sector, mapped to the ten Vision Discussion Document V3 patterns (SMB Lending, BNPL, Online Travel, On-Demand Services, Expense Management, Media Buying, Digital Banks, Credit/Chargecard Programmes, Digital Asset/Crypto, Investment & Trading Platforms). Codifies the three-part discovery pattern: sub-sector scan + use-case scan + incumbent-customer scan. Addresses the pattern where sub-sector-primary discovery under-surfaces companies whose card programme is a strategic fit but not yet a public signal (canonical example: Trade Republic pre-Marqeta). |

## 2. Purpose and scope
This document defines the end-to-end prospecting process TXN operates against European fintechs, digital banks, and embedded finance companies that fit the Ideal Customer Profile in TXN_GTM_ICP_Definition_v0.3. The process runs from account discovery through to a confirmed discovery meeting scheduled in Freshsales. Everything downstream of that meeting is handled by the Sales Motion process in TXN_GTM_Sales_Process_and_Stages_v0.3.
This is the anchor reference for the prospecting phase. Every downstream artefact (sequence templates, Freshsales configuration, tool selection, compliance policies, metrics dashboards) is derived from this process, not the reverse. When something in this document feels wrong, propose a change; do not quietly deviate.

### 2.1 How to use this document
Read Section 3 for the process overview and Sections 4.1 to 4.7 for the detailed stage definitions. Read Section 6 to understand how the process is implemented in two phases: Phase A is the manual, low-volume validation phase that runs first, and Phase B introduces automation only if the Phase A output warrants it. Read Section 7 for the recommended tooling stack, Section 8 for compliance requirements, Section 9 for metrics, and Section 10 for the prerequisite workstreams for each phase.

### 2.2 Refresh cadence
Quarterly review minimum. Interim revisions triggered by material changes to ICP v0.3, Core Messaging v2.5, the tooling stack selection, or Freshsales instrumentation. Version bump on any substantive change; prior version is archived in 99_Archive/.

### 2.3 Relationship to other documents
This document is downstream of ICP v0.3 (defines who prospects are), Core Messaging v2.5 (defines what to say to them), the persona set in 02_ICP_&_Personas (defines whose lens the message uses), and the AI Messaging Framework v1.0 and JV Messaging Framework v2.1 (define constrained language). It is upstream of the Sales Motion documents in 04_Sales_Motion, the Marketing collateral in 05_Marketing, and the Freshsales configuration itself.
The register that carries account records through the process is TXN_GTM_Qualification_Matrix_v0.2.xlsx, held in 04_Sales_Motion. The workbook is the staging layer for the scoring formulas; Freshsales is the operational system that Sales and Owner use daily.

## 3. Process overview
The prospecting process is seven stages. Each stage has a defined owner (Claude, Owner, or Tool), a set of inputs and outputs, a Freshsales write, and an exit criterion. The stages run in sequence per contact, though the overall pipeline runs continuously with new accounts entering Stage 1 on the monthly discovery cycle.

| # | Stage | Who | Freshsales action |
| 1 | Account discovery | Claude + Owner | Create / update Account record; set stage = Prospect |
| 2 | Account qualification and tiering | Claude drafts, Owner approves | Write Tier, Score, Rationale to Account |
| 3 | Contact discovery and enrichment | Owner + Sales Nav, Claude structures | Create Contact records linked to Account |
| 4 | Personalisation research | Claude (from owner-captured signals) | Attach Personalisation Notes to Contact |
| 5 | Sequence drafting and sending | Claude drafts, Owner sends (Phase A) / Platform sends (Phase B) | Log outbound Activity; update Contact status |
| 6 | Reply triage and follow-up | Claude triages, Owner acts on positives | Update Contact Reply status; log Activity |
| 7 | Meeting booked and handoff to Sales Motion | Owner | Create Meeting record; set stage = Discovery Scheduled |

The seven-stage flow is designed to be executable in two phases. Phase A runs the entire process manually with Claude and the Owner using existing tools (Sales Navigator, Freshsales, owner mailbox). Phase B introduces automation for the stages that become time-critical at higher volume. The delegation model between Claude and Owner is codified in ICP v0.3 Section 9.4 and applies in both phases.

# 4. Stage definitions

## 4.1 Stage 1: Account discovery
Find companies in the EEA plus United Kingdom that match the ICP v0.3 firmographic filter (sector, sub-sector, size, geography, regulatory regime, ownership) and clear the anti-profile. This stage is defined in detail in ICP v0.3 Section 9. What follows here is the operational specifics on how Claude and the Owner interact.
| Attribute | Value |
| Owner | Claude drafts, Owner approves list additions |
| Cadence | Monthly full-list scan; event-driven within month for high-priority triggers |
| Inputs | ICP v0.3 firmographic filter; ICP v0.3 anti-profile; ICP v0.3 source list (Section 9.3) |
| Outputs | Provisional new account rows in Qualification Matrix 02_Scoring_Register with source, discovery date, and initial signal notes |
| Primary sources | EBA public register plus national regulators (FCA in the UK, BaFin in Germany, KNF in Poland, CNB in the Czech Republic, ANAF in Romania, MNB in Hungary, and equivalents across remaining EEA jurisdictions); Visa Partner Directory; Mastercard Connect; BIN sponsor client pages (Paynetics, DiPocket, Modulr, Transact Payments, Enfuce as sponsor, Railsr); competitor case study pages |
| Secondary sources | Dealroom.co (European focus, free tier); Crunchbase; Sifted database; industry news (Sifted, Finextra, The Paypers, FinTech Futures, Finovate); LinkedIn (job posting signals, executive moves, company page announcements, roadmap posts via owner-driven Sales Navigator); Welcome to the Jungle (EU job board) |
| Freshsales write | On owner approval: create Account record with fields (Name, Country, Sector, Sub-sector, Employees, Regulatory Status, BIN Sponsor if known, Incumbent Processor if known, Source, Discovery Date, Trigger Notes). Stage = Prospect |
| Exit criterion | Account exists in both Qualification Matrix and Freshsales with a minimum viable fields set |

Claude runs a monthly scheduled task against the primary and secondary sources listed above. New candidates are surfaced to the Owner as a shortlist with initial signal notes. The Owner approves additions within one working week. Approved candidates are written to the Qualification Matrix and to Freshsales as an Account record in the Prospect stage.
Event-driven additions happen mid-cycle when Claude detects a high-priority trigger. Trigger sources are set out below and vary by trigger type. All trigger detection in Phase A relies on free or existing sources; paid real-time detection tools sit in Phase B and activate only if the monthly scan misses too many events to justify the cost.

### 4.1.1 Trigger sources
The four canonical trigger types (new product launch or roadmap, incumbent contract expiry or dissatisfaction, executive change into a product or engineering role, new market entry) come from ICP v0.3 Section 5. The table below shows what signals each trigger, what sources Claude can use to detect it, and which phase the source belongs to.

| Trigger event | What signals it | Sources Claude can use | Phase |
| New product launch or roadmap | Press announcement; funding round PR referencing card products; hiring for card program roles; beta program invitations | Web search; company press pages; Sifted / Finextra / The Paypers / FinTech Futures / Finovate; Crunchbase and Dealroom for the funding-round trigger; LinkedIn job listings via owner-driven Sales Navigator | A |
| Incumbent contract expiry or dissatisfaction | Public reference to a multi-year contract with a named incumbent nearing anniversary; RFP-like activity; executive remarks on platform change; public incident posts; press coverage of outages | Web search; competitor case study pages; industry news feeds; incident status pages of the six named incumbents | A |
| Executive change into a product or engineering role | LinkedIn "started a new position" post; press announcement; company blog | LinkedIn via owner-driven Sales Navigator (primary); web search on the individual name (secondary) | A |
| New market entry | Public geographic expansion announcement; licence application filings; hiring in the target country; partner search signals | Regulatory registers (EBA and national); press announcements; company blog; LinkedIn job listings for target country | A |
| Real-time trigger detection (all types) | Any of the above, delivered on the day the signal appears rather than in the monthly scan | Google Alerts (free, low fidelity); Feedly (paid, RSS-based); Owler or Crayon (paid, sales-intel focused, best signal-to-noise) | B (evaluate only if monthly scan misses too many events) |

### 4.1.2 Multi-market discovery cadence
When running Stage 1 across multiple markets, complete both account seeding and trigger logging for the current market before starting discovery for the next market. Do not open discovery in market N+1 while market N still has accounts sitting at P6 = 0 for lack of logged triggers.
The reason: without triggers logged, the auto-scoring engine returns misleadingly low tier assignments. Accounts that should be Priority 1 sit at Priority 2 or 3, and outreach prioritisation drifts. The pattern to avoid is discovering four markets, logging triggers for only the first, and then treating the aggregate tier distribution as if it were representative.
The operating rule is therefore: for each market, complete Stage 1 in the sequence (a) surface candidates from primary and secondary sources, (b) seed candidates into 02_Scoring_Register with input columns populated, (c) log detected trigger events into 04_Triggers with dates, priorities, and source URLs, (d) verify the resulting tier distribution reads sensibly against the market's known fintech landscape. Only when all four steps are complete for the current market does the next market's discovery start.
Applies to the MVP markets (Poland, Czech Republic, Romania, Hungary) and to any subsequent Phase 1a and 1b market rollouts. Applies equally to the monthly refresh cycle: complete the current month's refresh across all seeded markets before starting the next month's.

### 4.1.3 Use-case-driven discovery
Discovery uses three lenses in parallel, not sequentially: geography, sub-sector, and use case. Geography maps ICP v0.4 Section 4.4 phasing. Sub-sector maps ICP v0.4 Section 4.2. Use case maps to the ten patterns identified in the Vision Discussion Document V3 Sample Use Cases section: SMB Lending, BNPL, Online Travel, On-Demand Services, Expense Management, Media Buying, Digital Banks, Credit / Chargecard Programmes, Digital Asset / Crypto, Investment and Trading Platforms. The Vision Document explicitly names this list as non-exhaustive; other use cases surface with market experience.
Why the third lens matters: sub-sector-driven discovery weights companies with visible card programmes or explicit card-adjacent products. Use-case-driven discovery surfaces companies whose card programme is a strategic fit but not yet a public signal. Trade Republic is the canonical example: it did not have a card programme until it launched with Marqeta in H2 2022; before that it was a Vision-fit prospect that would not have surfaced under a sub-sector-plus-card-signal filter. Trading platforms without cards, OTAs without supplier-card programmes, on-demand services without driver-payout programmes, and expense management platforms without an issuing layer all fall in the same category. Every one of them is a Vision use case that deserves representation in the register regardless of card-signal visibility today.
Operational rule: for each market discovery pass, run three sub-scans in parallel and consolidate before scoring. Sub-scan 1 is sub-sector-primary, per ICP v0.4 Section 4.2. Sub-scan 2 is use-case-primary, working through the ten Vision use cases and surfacing companies that fit the use case even without visible card signals. Sub-scan 3 is incumbent-customer, systematically working through published customer references of Marqeta, Paymentology, Thredd, Enfuce, Episode Six, and Pismo. Any company that appears as a published customer of one of the six named incumbents is a proven ICP fit by definition, whatever sub-sector it occupies. Consolidate the three sub-scan outputs, deduplicate, then apply Section 8 scoring.
Geographic adjacency: candidates whose HQ is outside the current MVP market but whose operations meaningfully touch the market may be logged either with the MVP market's country prefix (if a distinct local entity or decision authority exists) or with the HQ market's prefix with an operational-footprint note (if decisioning is central). This is a judgement call per candidate. Examples: Trade Republic (Germany HQ, live in all MVP markets) is logged with a DE prefix and MVP operational-footprint notes; a Polish subsidiary of a foreign fintech with distinct decision authority is logged with a PL prefix.
Backfill: the first four MVP markets (Poland, Czech Republic, Romania, Hungary) were scoped with sub-sector-primary discovery only. A supplemental use-case + adjacent-geo + incumbent-customer pass in July 2026 backfilled the missed candidates. From v0.4 forward, the three-part discovery pattern applies to every market discovery pass.

## 4.2 Stage 2: Account qualification and tiering
Score each account across the ten parameters defined in ICP v0.3 Section 8.1, apply the gating rules in Section 8.2, and assign a tier (Priority 1, 2, 3, or Disqualified). Tier drives the downstream activity level per Section 8.4.
| Attribute | Value |
| Owner | Claude drafts provisional score, Owner approves final tier |
| Cadence | On account addition; 90-day rolling re-score; event-driven on trigger detection |
| Inputs | Account record; ICP v0.3 Section 8 scoring framework (10 parameters, 100 points max) |
| Outputs | Score across ten parameters; aggregate tier (Priority 1 / 2 / 3 / Disqualified); gating check outcome; scoring rationale note |
| Tools | Qualification Matrix workbook (deterministic scoring formulas per Section 8.1); Claude for parameter interpretation |
| Freshsales write | Update Account fields: Tier, Score, Scoring Rationale, Gating Flags, Last Scored Date |
| Exit criterion | Account has approved tier; downstream activity level is unambiguous per ICP v0.3 Section 8.4 |

Claude drafts the provisional score using publicly available data and its interpretation of the ICP v0.3 band definitions. The Owner reviews and can adjust bands where the public signal is inconclusive. Once approved, the tier is written to the Freshsales Account record. Tier changes require Owner approval; Claude surfaces proposed changes but does not promote accounts autonomously.
The 90-day rolling re-score ensures no record goes stale. One third of the list is re-scored each month, and any material attribute change (employee count, funding stage, licence status, new trigger event) triggers a same-month re-score.

## 4.3 Stage 3: Contact discovery and enrichment
For each Priority 1 and Priority 2 Account, find named humans who match the persona role targets, verify their emails, and create Contact records in Freshsales linked to the Account. Priority 3 accounts get contact discovery on inbound only.
| Attribute | Value |
| Owner | Owner drives via LinkedIn Sales Navigator; Claude structures the output |
| Cadence | Triggered per account after tiering (Priority 1 and 2 in Phase A; Priority 3 on inbound only) |
| Inputs | Account record; role targets per persona (see Sub-section below); owner-captured Sales Navigator profile results |
| Outputs | Named contacts with verified emails, titles, LinkedIn URLs, mapped to Champion / Economic Buyer / Primary User persona archetypes |
| Phase A tools | LinkedIn Sales Navigator (owner-driven for search and profile capture); Claude for structuring, deduplication, role classification; free email verification via MX check plus manual sanity check; email pattern inference from LinkedIn URL plus domain (first.last@domain.com, first@domain.com etc.) |
| Phase B tools | Add Apollo or Cognism for automated contact discovery at scale; add Bouncer or NeverBounce for automated email verification. Introduce only if account volume from Phase A justifies the tooling cost |
| Freshsales write | Create one Contact record per named human, linked to Account. Fields: Name, Title, Role Category (Champion / Economic Buyer / Primary User / Influencer / DACI Role), Email, Email Verified Status, LinkedIn URL, Country, Discovery Source |
| Exit criterion | At least two verified contacts per Tier 1 account (ideally covering Champion + Primary User); one contact per Tier 2 account |

### 4.3.1 Role targets per persona
The persona archetypes below map to real-world titles. Discovery targets any of the listed titles within the role category. Additional titles may be added where the target company uses non-standard nomenclature.

| Persona archetype | Target roles (any of) |
| Champion | Chief Product Officer, VP Product, Head of Product, Director of Product (card programs, payments, or issuing) |
| Economic Buyer | Chief Financial Officer (primary), Chief Executive Officer / Founder (secondary on strategic deals) |
| Primary User | Chief Technology Officer, Head of Engineering, VP Engineering (payments or platform) |
| Head of Payments | Head of Payments, Director of Payments, VP Payments (DACI Driver role) |
| Risk and Compliance | Chief Risk Officer, Head of Compliance (DACI Contributor role on regulated targets) |

### 4.3.2 The LinkedIn constraint and the human-plus-Claude workflow
LinkedIn's Terms of Service prohibit automated access, unauthenticated scraping, or bot use of any kind. This is a LinkedIn constraint, not a Claude constraint, and it applies to every tool that touches LinkedIn (Apollo, Cognism, Kaspr, and others use licensed data feeds or user-authenticated browser sessions to work around this legitimately). Claude does not access LinkedIn autonomously.
The correct workflow at Phase A volume is human-plus-Claude with LinkedIn Sales Navigator. The Owner runs the Sales Navigator searches, opens the target company page, filters by title against the persona role targets in Section 4.3.1, and captures the profile results (name, title, LinkedIn URL, and any relevant profile signal). The captured data is passed to Claude, which structures it for Freshsales, deduplicates against existing contacts, classifies role fit against the persona archetypes, and produces the personalisation snippet for Stage 4 from any LinkedIn post content the Owner captures alongside the profile. This turns Sales Navigator into a research surface rather than a discovery bottleneck, and it is compliant with LinkedIn's terms.
Email discovery at Phase A volume works via inference. LinkedIn URL plus company domain typically resolves to one of a small number of email patterns (first.last, first, f.last, etc.). Claude proposes the two or three most probable patterns; the Owner sends a test to the top pattern from ianj@txn.global; a bounce indicates the wrong pattern and the next pattern is tried. This is slower than an automated verification service (Bouncer, NeverBounce) but for 5 to 15 emails per week the cost difference is not worth the tooling. At Phase B, automated verification takes over.

## 4.4 Stage 4: Personalisation research
For each Contact, produce two to four sentences of relevant, verifiable personalisation grounded in a public source. This is what separates warm outbound from spam. No personalisation, no send.
| Attribute | Value |
| Owner | Claude |
| Cadence | Per contact, before the first outbound message |
| Inputs | Contact record; owner-captured public activity (LinkedIn posts, podcast appearances, company announcements); news search results |
| Outputs | Two to four sentences of personalisation, one hook line, and one relevance link to the target message pillar per contact |
| Tools | LinkedIn Sales Navigator (owner-driven, output pasted to Claude); news search via web; podcast search; target company website; Claude for synthesis and pillar mapping |
| Freshsales write | Attach Personalisation Notes to Contact record. Include hook line, source of hook (post URL / press URL), target message pillar (1 to 5 per Core Messaging Section 6) |
| Exit criterion | Contact has a personalisation snippet grounded in a verifiable public source; no personalisation, no send |

The personalisation must connect to one of the five messaging pillars defined in Core Messaging v2.5 Section 6. Claude captures the connection in the Personalisation Note so the sequence drafter (also Claude) knows which pillar to lead with in the introduction email. This is the mechanism by which the messaging library flows into individual outbound touches.
Examples of qualifying personalisation: a recent LinkedIn post from the Contact about card program challenges (points to a specific pillar), a company funding round mentioning new product surfaces (points to Pillar 1: Launch and evolve products faster), an executive move creating a re-platforming window (points to Pillar 5: Manage card program efficiently and effectively). Examples of non-qualifying personalisation: generic congratulations on a funding round; a shared alma mater; any personalisation that could be applied to a hundred other contacts.

## 4.5 Stage 5: Sequence drafting and sending
Draft the outbound sequence (4 to 6 touches over 20 to 30 days) using the messaging library, the persona lens, and the personalisation snippet. Phase A sends manually from ianj@txn.global; Phase B introduces a dedicated sending domain and automated sequencing platform only if volume growth demands it.
| Attribute | Value |
| Owner | Claude drafts every email; Owner sends manually in Phase A, sending platform sends automatically in Phase B |
| Cadence | Four to six touches over 20 to 30 days; sending days weighted Tuesday to Thursday |
| Inputs | Contact record with persona archetype and personalisation notes; Core Messaging v2.5 pillars, positioning, tone rules; AI Messaging Framework anchor phrase where relevant; sequence template for the persona |
| Outputs | Sequence of tailored emails: introduction, nudge, value-add, break-up. Optional LinkedIn touch between emails. Each email under 120 words. British English, program spelling, no em dashes, TXN tone rules per Core Messaging Section 10 |
| Phase A sending | Owner sends manually from ianj@txn.global. No automated sequences, no tracking pixels, no separate sending domain. Each email looks like a bespoke 1:1 message because it is |
| Phase B sending | Introduce a dedicated sending domain (lookalike of txn.global), warmed inboxes, and a sending platform (Smartlead, Instantly, or Apollo). Only triggered if Phase A volume growth demands automation. See Section 6 for the phase transition criteria |
| Freshsales write | Log each send as an Activity linked to Contact. Update Contact Sequence Status (In Sequence / Completed / Replied / Bounced / Unsubscribed). Phase A: owner logs after send; Phase B: platform logs via integration |
| Exit criterion | Sequence completes, or a reply of any kind arrives (positive, negative, unsubscribe, bounce) |

### 4.5.1 Why Phase A uses the owner mailbox
At Phase A volume (5 to 15 highly personalised sends per week, one at a time, no automation), sending from ianj@txn.global is genuinely safe and appropriate. This is not "cold outbound" in the technical sense that email filters worry about; it is founder-led business development, indistinguishable from the many bespoke 1:1 emails that founders send every day. Reputation risk is minimal because volume is minimal, personalisation is high, and each send looks like a normal human email to a filter.
The threshold at which a dedicated sending domain becomes worthwhile is roughly: automated multi-touch sequences (a platform sending Day 4, Day 8, Day 15 without owner action), multiple contacts at the same company hit in the same week, or 20-plus sends per day. Below that threshold, the owner mailbox is the right sender. Phase transition criteria in Section 6.3 make this concrete.

### 4.5.2 Sequence structure
The standard sequence is 5 touches over 24 days, with sends weighted Tuesday to Thursday and skipped on public holidays in the target country. LinkedIn touches are optional between emails for Priority 1 accounts.
Day 1: Introduction. Personalisation hook, single pillar reference, low-commitment CTA (invitation to reply, not to book).
Day 4: Nudge. Different angle to Day 1, one specific proof point from Core Messaging Section 9 persona proof.
Day 8: Value-add. Send a specific asset (case study, competitor differentiation snapshot, sub-sector one-pager) that is relevant to the persona and the personalisation angle.
Day 15: Angle change. Different pillar, different proof point, different tone. Sometimes framed as "one last idea before I stop reaching out".
Day 24: Break-up. Explicit close-out, low-pressure, sometimes generates a reply where earlier touches did not.

### 4.5.3 Sending rules
British English throughout; program and programs, not programme and programmes.
No em dashes; use commas, colons, parentheses, or full stops instead.
No AI-isms: no revolutionary, transformative, seamlessly, cutting-edge, leverage (as verb), best-in-class, or synergies.
Ownership references use the approved formulations: Direct Transact, our co-founding owner, and Paycorp, our co-founding owner. Banned phrases per Core Messaging Section 10 must not appear.
Each email under 120 words. Subject line under 60 characters. One CTA per email.
No two contacts at the same company receive identical text. Claude varies the opening, the pillar reference, and the proof point across contacts.
Sending window: 08:00 to 17:00 local time in the target country. Sends outside window queue to the next available slot.
Unsubscribe link or plain-text reply instruction in the footer of every email; TXN's registered business address as the reachable postal address.

## 4.6 Stage 6: Reply triage and follow-up
Every reply is triaged within one business day. Positive replies escalate to the Owner immediately. Objections receive a drafted response for Owner review. Not-interested and unsubscribe replies write to the Suppression List. Bounces flag the Account for re-enrichment.
| Attribute | Value |
| Owner | Claude triages replies; Owner acts on positives |
| Cadence | Same-day for positive replies; within one business day for objections and negative replies; batched for unsubscribes and bounces |
| Inputs | Inbound reply text; Contact record; sequence context |
| Outputs | Classified reply (Positive / Objection / Not-Now / Not-Interested / Unsubscribe / Bounce); recommended next action; draft response where appropriate |
| Tools | Phase A: owner forwards or pastes reply to Claude; Claude classifies and drafts. Phase B: sending platform API for inbound; Claude for classification and draft |
| Freshsales write | Update Contact Reply Status; log Activity with reply text and classification; on Unsubscribe or Not-Interested add to Suppression List; on Bounce mark email as invalid and flag Account for re-enrichment |
| Exit criterion | Reply is classified and next action is queued |

### 4.6.1 Reply classification
Positive: contact wants to talk. Any expression of interest, question about the platform, or explicit meeting request. Escalation to Owner same-day.
Objection: contact is engaged but has a concern (timing, budget, incumbent contract, competitor preference, technical fit). Claude drafts a response tied to the objection type, Owner reviews before send.
Not-Now: contact is not opposed but is not available. Automated nurture cadence enters (a lighter-touch monthly touch for six months).
Not-Interested: explicit rejection. Suppression list, no further contact from this contact for 12 months.
Unsubscribe: explicit unsubscribe request. Suppression list permanent. Suppress the contact's domain if the language suggests company-wide preference.
Bounce: email delivery failed. Mark email invalid, flag Account for re-enrichment, remove contact from active sequences.

## 4.7 Stage 7: Meeting booked and handoff to Sales Motion
On positive reply, the Owner schedules a discovery meeting in Freshsales, and Claude drafts a pre-meeting brief. The Account moves from Prospect to Discovery Scheduled. Prospecting is complete; the account enters the Sales Motion defined in TXN_GTM_Sales_Process_and_Stages_v0.3.
| Attribute | Value |
| Owner | Owner |
| Cadence | Same-day on positive reply |
| Inputs | Positive reply; Contact and Account records |
| Outputs | Scheduled discovery meeting in Freshsales linked to Account and Contact; pre-meeting brief drafted by Claude covering account context, personalisation source, and message pillar the contact responded to |
| Tools | Freshsales calendar integration; scheduling link (Calendly or equivalent) if used |
| Freshsales write | Create Meeting record. Update Account Stage from Prospect to Discovery Scheduled. Update Contact status to Engaged |
| Exit criterion | Meeting exists in Freshsales with a confirmed time and attendees; pre-meeting brief exists; prospecting motion is complete. Handoff to the Sales Motion process defined in TXN_GTM_Sales_Process_and_Stages_v0.3 |

The pre-meeting brief covers: what the Account is, who the Contact is and their persona archetype, the personalisation source used in the sequence, the pillar the Contact responded to, the recent trigger events that indicate this is a Right Time conversation, and the relevant sub-section of Core Messaging Section 12 for competitor context if an incumbent was named in the reply. The brief is written to a Freshsales Note against the Meeting record.

## 5. Freshsales as system of record
Freshsales holds the truth for every account, contact, activity, and meeting. Every stage in Section 4 writes to Freshsales on entry, exit, or state change. The Qualification Matrix workbook remains the scoring engine and the staging register for the scoring formulas; Freshsales is the operational system that Owner uses daily.

### 5.1 Entity model
Account: one record per company. Fields defined in Stage 1. Stages: Prospect, Discovery Scheduled, In Discovery, Qualified, Opportunity, Customer, Dormant, Disqualified.
Contact: one record per named human. Fields defined in Stage 3. Linked to Account by foreign key.
Activity: one record per outbound send, inbound reply, or manual interaction. Linked to Contact.
Meeting: one record per scheduled or completed meeting. Linked to Account and one or more Contacts.
Suppression List: separate table maintained in Freshsales; reconciled with sending platform nightly at Phase B.

### 5.2 Custom fields required
Freshsales does not carry all the fields needed by this process out of the box. The following custom fields need to be added during Phase A configuration (Prerequisite P1 in Section 10).
Account: Tier (P1 / P2 / P3 / Disqualified), Score, Scoring Rationale, Gating Flags, Last Scored Date, Discovery Source, Incumbent Processor, BIN Sponsor, Regulatory Status, Trigger Notes.
Contact: Role Category (Champion / Economic Buyer / Primary User / Head of Payments / Risk and Compliance / Other), Email Verified Status, Sequence Status, Reply Status, Personalisation Note, Target Message Pillar.
Activity: Sequence Stage (Day 1 / Day 4 / Day 8 / Day 15 / Day 24 / LinkedIn / Inbound), Send Timestamp, Reply Timestamp, Classification.

# 6. Phased implementation approach
The process is implemented in two phases. Phase A runs the entire seven-stage flow manually with Claude, the Owner, and existing tools. The purpose of Phase A is to validate that the process actually produces the volume of qualified opportunities expected, and to surface any tuning needed on the ICP filter, the messaging, or the sequence design. Phase B introduces automation for the stages that become time-critical at higher volume, and only activates if Phase A output warrants the tooling investment.

## 6.1 Phase A: manual validation
Phase A is designed for the launch-phase reality: low volume, high personalisation, single-owner operation, and no critical dependency on paid tooling beyond the Owner's existing Sales Navigator and Freshsales subscriptions. Its objective is to prove that the ICP filter and messaging produce booked discovery meetings at a rate that justifies scaling. If it does, Phase B follows. If it does not, the diagnosis is easier because the tooling has not obscured the underlying signal.

### 6.1.1 Phase A activities by week
The plan below covers the first six weeks and is designed to have the first sequenced sends in market by end of Week 6.

| Week | Activities | Deliverables |
| Week 1 (this week) | Freshsales configuration (Prerequisite P4 below): custom fields, pipeline stages, suppression list, meeting linking. Populate persona documents with pain-signal hooks (Prerequisite P5). Populate Qualification Matrix with 5 to 10 seed accounts from MVP markets to validate scoring formulas (Prerequisite P8). | Freshsales configured for the process. Persona docs at v0.2 with real pain hooks. Qualification Matrix seeded and validated. |
| Week 2 | Run Stage 1 discovery for one full month equivalent. Claude scans primary and secondary sources including LinkedIn Sales Navigator (owner-driven), regulatory registers, competitor case study pages, Sifted / Finextra / Dealroom. Compile candidate account list. | Candidate list of 40 to 60 ICP-fit accounts across MVP markets, with source and initial signal notes for each. |
| Week 3 | Run Stage 2 scoring and tiering for the candidate list. Claude drafts scores; Owner approves final tiers. Write approved accounts to Freshsales. | 15 to 25 Priority 1 and 2 accounts confirmed in Freshsales, ready for contact discovery. |
| Week 4 | Run Stage 3 contact discovery for Priority 1 accounts (target 2 contacts per account) using owner-driven Sales Navigator. Claude structures results, deduplicates, classifies role fit. Verify emails via free MX check plus manual sanity check. | 20 to 40 verified contacts across Priority 1 accounts, in Freshsales with persona classification. |
| Week 5 | Stage 4 personalisation research per contact. Stage 5 sequence drafting per contact (Claude drafts full 5-touch sequence). Owner reviews and adjusts. | Personalisation snippets and full sequences drafted for the first cohort. Ready to send. |
| Week 6 | Owner sends Day 1 of sequences for the first cohort (5 to 15 sends per day, spaced across Tuesday to Thursday). Claude sits ready for reply triage. Continue Stage 1 discovery in parallel to keep the funnel filling. | First cohort in market. Reply triage active. Live process metrics starting to accumulate. |

### 6.1.2 Phase A exit criteria
Phase A is complete when three conditions hold together for at least four consecutive weeks:
Stage 1 discovery is producing at least 15 new Priority 1 or 2 accounts per month on average.
Stage 5 sending is running at 15 to 30 sends per week with reply rate above 5%.
Stage 7 is producing at least 2 booked discovery meetings per month.
If these conditions hold, Phase B tooling investment is justified. If they do not, the diagnosis focuses on ICP filter, messaging, and personalisation before adding tooling that would only amplify a broken signal.

## 6.2 Phase B: automation and scale
Phase B is triggered by the criteria in Section 6.3, not by a calendar date. It introduces automation for the stages that become time-critical at higher volume: automated contact discovery via Apollo or Cognism, automated sequencing via Smartlead or Instantly on a dedicated warmed sending domain, automated email verification, and (optionally) paid real-time trigger detection. The seven-stage flow does not change; the tools that execute each stage change.

## 6.3 Phase transition criteria
Phase B activates on any of the criteria below, evaluated monthly by the Owner. Multiple criteria hitting simultaneously indicate urgency; a single criterion hitting is sufficient to start the Phase B workstream for that specific tooling area.

| Criterion | Phase A holds | Trigger Phase B |
| Monthly send volume | Under 40 sends per week | 40 or more sends per week sustained |
| Sequence follow-ups | Fully manual, owner clicks send each time | Manual follow-ups become a time sink; owner is spending more than 1 hour per day on sending mechanics |
| Contact discovery volume | Under 30 new contacts per month, manual LinkedIn Sales Navigator handles it | Over 30 new contacts per month, manual discovery starts missing candidates |
| Deliverability signals | Reply rate over 8%, bounce rate under 2%, no spam complaints | Bounce rate above 3% or any spam complaint; suggests separate sending domain needed |
| Owner capacity | Owner running the motion alongside other duties without difficulty | Owner is capacity-blocked; hiring an SDR or delegating requires more automation |

## 7. Recommended tooling stack
The stack below is split by phase. Phase A relies on existing subscriptions (Freshsales, LinkedIn Sales Navigator, owner mailbox) plus free sources; Phase B introduces paid category tools only where the transition criteria in Section 6.3 justify them.

| Category | Purpose | Phase A option | Phase B option |
| CRM | System of record for accounts, contacts, activities, meetings | Freshsales (already selected) | Freshsales |
| B2B data (accounts) | Company discovery signals for ICP-fit accounts | Regulatory registers (free); Dealroom.co free tier; Crunchbase; Sifted; competitor case studies; owner-driven LinkedIn Sales Navigator | Apollo / Cognism / Clay (evaluate if Phase A volume warrants) |
| B2B data (contacts) | Named contact discovery | Owner-driven LinkedIn Sales Navigator plus Claude for structuring | Apollo or Cognism for automated discovery at scale |
| Email verification | Confirm email deliverability before send | Free MX check plus manual sanity check on inferred emails | Bouncer, NeverBounce, or ZeroBounce |
| Personalisation research | LinkedIn post surfacing, news, podcast signals | Owner captures via Sales Navigator plus news search; Claude synthesises | Clay for orchestrated enrichment; keep LinkedIn Sales Navigator as the base |
| Sending platform | Send emails, log activity | Owner sends manually from ianj@txn.global; logs to Freshsales after send | Smartlead, Instantly, or Apollo (bundles data plus sending); dedicated sending domain plus warmed inboxes |
| Sending domain | Domain used for outbound | txn.global (owner mailbox) at Phase A volumes | Dedicated lookalike (txn-connect.com, gettxn.com, join-txn.com) with SPF / DKIM / DMARC and 4 to 6 weeks warm-up |
| Trigger detection | Real-time signal on new fundings, executive moves, incumbent events | Monthly Claude scan of web search plus RSS-equivalent via free feeds; Google Alerts for the top 20 Priority 1 accounts | Feedly, Owler, or Crayon (evaluate only if the monthly scan misses too many events) |
| Scheduling | Book discovery meetings on positive reply | Freshsales Calendar or Calendly | Same |

The critical-path tooling for Phase A is Freshsales configuration (Prerequisite P1). Everything else in Phase A uses tools that already exist or are free. Phase B tooling decisions are made against the transition criteria at the time they trigger, so specific tool selection can wait.

## 8. Compliance and deliverability
Outbound to EEA and UK targets is governed by GDPR (legitimate interest basis for B2B in most jurisdictions), PECR (UK specific), and country-specific rules. Non-compliance risks both regulatory action and, at Phase B, sending domain damage. The rules below are the baseline; compliance boilerplate for the footer is developed in Prerequisite P5.

### 8.1 Sending domain and infrastructure
Phase A: send from ianj@txn.global. Volume kept under 40 sends per week. No automated sequences, no tracking pixels, no separate sending domain.
Phase B (triggered by Section 6.3): register a dedicated sending domain that is not txn.global; configure SPF, DKIM, and DMARC; provision 3 to 5 mailboxes; warm each for 4 to 6 weeks before serious volume; cap volume per inbox at 30 to 50 sends per business day; rotate inboxes across contacts.
At all volumes: never send bulk cold outbound from a customer, partner, or investor communication mailbox. txn.global stays clean at Phase B by moving cold outbound to the dedicated domain.

### 8.2 GDPR (EEA)
Legitimate interest is the lawful basis. Justification: the contact holds a role for which TXN's platform is directly relevant, and outreach is proportionate to the professional context.
Documentable justification per ICP segment (digital banking, expense management, lending, FX, BaaS). Store the justification in the compliance folder alongside the process.
Every email carries a clear unsubscribe mechanism (link or plain-text reply instruction).
Every unsubscribe is honoured within 48 hours. Suppression list is permanent.
Contact right-to-erasure requests handled within 30 days and logged in Freshsales.

### 8.3 UK PECR
Corporate subscribers (companies with named contacts) are permitted under legitimate interest. Sole traders and unincorporated partnerships are consent-based; exclude these from outbound.
Sender identification (TXN's registered business address) in every footer.

### 8.4 Country-specific
Germany: consent-based cold email under UWG. Excluded from proactive outbound. Reach via LinkedIn only, or wait for inbound.
Poland, Czech Republic, Romania, Hungary (MVP markets): permitted under legitimate interest with the standard footer boilerplate.
France: permitted under legitimate interest, but soft-opt-in convention is watched. Use the same standard.
Netherlands: permitted; opt-out honoured.

### 8.5 Footer address
Every outbound email carries a footer with TXN's registered business address, an unsubscribe mechanism, and a brief legitimate-interest statement. Address is TXN Global's registered address, not Direct Transact's or Paycorp's: TXN is the entity making the offer, and routing sender identity through a co-founding owner's address serves no purpose. The exact boilerplate is drafted in Prerequisite P5.

## 9. Metrics and iteration
The process is measured stage by stage. Each stage has one primary metric with a target range and a watch signal. Weekly review inside the Owner ops rhythm; monthly review at the process level to spot compounding shifts. Metrics apply to both phases; the interpretation of deliverability changes between manual (Phase A) and automated (Phase B) sending.

| Stage | Metric | Target range | Watch signal |
| 1: Discovery | New accounts added per month | 15 to 30 in first 90 days | Below 10 means source coverage is thin; above 40 means qualification is too loose |
| 2: Qualification | Pass rate to Tier 1 or 2 | 25% to 40% of new accounts | Below 20% means ICP filter is too broad; above 50% means it is too generous |
| 3: Contact discovery | Verified contacts per Tier 1 account | At least 2 | Fewer than 2 means Sales Navigator coverage or classification is under-serving |
| 4: Personalisation | % of contacts with a personalisation snippet | 100% before send | Any send without personalisation breaks the process |
| 5: Sending | Deliverability (inbox placement) | Above 90% in Phase A given manual sending and low volume | Below 85% means content quality, list hygiene, or (in Phase B) sending domain reputation needs work |
| 5: Sending | Reply rate | 5% to 10% | Below 3% means the offer or targeting is off; above 12% is worth studying to replicate |
| 6: Reply triage | Positive reply rate (as % of sends) | 0.5% to 2% | Below 0.5% means the offer is not resonating; above 2% is worth propagating |
| 7: Meeting booked | Positive reply to meeting conversion | Above 60% | Below 50% means the scheduling or follow-up step is losing intent |

The single most important metric in Phase A is reply rate (Stage 5). A high reply rate at low volume is the strongest possible signal that the ICP filter, personalisation, and messaging are working, and it justifies Phase B tooling investment when the transition criteria hit. A low reply rate at low volume is a signal that adding automation will not help; the fix is upstream in ICP, personas, or messaging.

## 10. Prerequisites and enabling workstreams
The prerequisites are split by phase. Phase A prerequisites gate the ability to start; Phase B prerequisites activate on the transition criteria in Section 6.3.

### 10.1 Phase A prerequisites
Seven workstreams to enable Phase A. Ordered by dependency; P1 is the critical path because Freshsales must exist before any account or contact is written.

| # | Workstream | Estimated effort | Status |
| P1 | Freshsales instrumentation: custom fields per Section 5.2, pipeline stages, reply status values, suppression list, meeting linking | 3 to 5 days configuration | Not started |
| P2 | Populate persona documents in ICP_&_Personas with pain-signal hooks and CTA anchors (Champion, Economic Buyer, Primary User) | 2 to 3 focused sessions | v0.1 exists, needs content pass |
| P3 | Draft persona-specific sequence templates (5 emails each) for the three primary personas | 2 to 3 days for drafting and review | Not started |
| P4 | Define suppression list source of truth in Freshsales; document maintenance rules | 1 day configuration | Not started |
| P5 | GDPR footer boilerplate with TXN registered business address; documentable legitimate interest justification per ICP segment | 1 to 2 days drafting and legal review | Not started |
| P6 | Confirm LinkedIn Sales Navigator subscription is active for the owner | Same day | Existing subscription assumed |
| P7 | Seed Qualification Matrix with 5 to 10 accounts from MVP markets to validate scoring formulas end to end | 2 days seeding and validation | Workbook exists at v0.2 |

### 10.2 Phase B prerequisites (deferred, triggered by Section 6.3)
Five workstreams for Phase B. None of these are critical-path for the initial launch; each activates on its specific transition trigger.

| # | Workstream | Trigger to activate | Estimated effort |
| P8 | Register dedicated sending domain (lookalike); configure SPF / DKIM / DMARC; provision 3 to 5 mailboxes; begin warm-up | Send volume approaching 40 per week sustained; or bounce rate above 3% | 1 day setup, 4 to 6 weeks warm-up |
| P9 | Evaluate and contract B2B data provider (Apollo, Cognism, or Clay) | Contact discovery volume exceeds 30 new contacts per month, or Sales Navigator coverage gaps identified | 3 to 5 days |
| P10 | Evaluate and contract sending platform (Smartlead, Instantly, or Apollo) | Manual follow-up time exceeds 1 hour per day; owner capacity constrained | 2 to 3 days |
| P11 | Evaluate real-time trigger detection tooling (Feedly, Owler, Crayon) | Monthly scan repeatedly misses trigger events worth acting on same-day | 2 days |
| P12 | Add email verification tooling (Bouncer, NeverBounce) | Contact discovery moves to automated pipeline via Apollo or Cognism | 1 day integration |

## 11. Refresh cadence and governance
This document is owned by Ian Johnson (ianj@txn.global). Quarterly review minimum. Interim revisions triggered by material changes to ICP v0.3, Core Messaging v2.5, the tooling stack selection, Freshsales schema, or metric targets. Version bump on any substantive change; prior version archived in 99_Archive/. Contributors propose changes via the Owner; day-to-day operating decisions (adjusting sequence copy, adding new sources, refining targeting parameters) do not require version bumps but are logged in the Owner ops rhythm notes.
Phase transition decisions are made by the Owner, informed by the metrics in Section 9 and the transition criteria in Section 6.3. Any Phase B tooling contract is a formal change; the Owner records the decision and its rationale in the Migration Register.

# Appendix A. Related documents
The following documents form the canon this process is derived from. Any change to a canon document should trigger a review of this document within one business week.
TXN_GTM_ICP_Definition_v0.3.docx: who TXN sells to, scoring framework, tiering, anti-profile, Named Account List method. Location: 07_GTM/02_ICP_&_Personas/
TXN_Core_Messaging_v2.5.docx: positioning, pillars, tone, competitor differentiation snapshot, persona proof, boilerplate. Location: 07_GTM/03_Positioning_&_Messaging/
TXN_AI_Messaging_Framework_v1.0.docx: approved anchor phrase, asset-by-asset AI copy adaptations. Location: 07_GTM/03_Positioning_&_Messaging/
TXN_JV_Messaging_Framework_v2.1.docx: approved and banned ownership formulations for Direct Transact and Paycorp. Location: 07_GTM/03_Positioning_&_Messaging/
TXN_GTM_Persona_Champion_v0.1.docx, TXN_GTM_Persona_Economic_Buyer_v0.1.docx, TXN_GTM_Persona_Primary_User_v0.1.docx: persona lenses for personalisation and sequence variation. Location: 07_GTM/02_ICP_&_Personas/
TXN_GTM_Qualification_Matrix_v0.2.xlsx: the register that carries account records through the scoring and tiering process. Location: 07_GTM/04_Sales_Motion/
TXN_GTM_Competitive_Landscape_v0.2.docx: competitor detail underpinning sequence drafting and objection handling. Location: 07_GTM/06_Competitive_&_Market_Intel/
TXN_GTM_Sales_Process_and_Stages_v0.3.docx: downstream Sales Motion picked up at the meeting-booked handoff point. Location: 07_GTM/04_Sales_Motion/
