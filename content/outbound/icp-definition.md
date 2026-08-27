---
description: "TXN's own Ideal Customer Profile: firmographics, triggers, anti-profile, the ten-parameter scoring framework, tiering, and the Named Account List method"
---

# TXN ICP Definition (v0.4)

> **Source of truth:** `TXN_GTM_ICP_Definition_v0.4.docx` in the outbound folder (`programming/txn/outbound`, mirrored at `shared/clients/txn/outbound`), delivered by Ian Johnson on 24 August 2026. This page is a readable mirror. Edit the source document, then re-mirror. Routed from [[outbound]].

---

TXN Global
Ideal Customer Profile
Who TXN sells to, and who to deprioritise
Version 0.4   |   Author: I. Johnson   |   13/07/2026

## 1. Document Control
| Version | Date | Author | Owner | Description |
| 0.1 | 22/04/2026 | I. Johnson | I. Johnson | Initial version. |
| 0.2 | 01/05/2026 | I. Johnson | I. Johnson | Section 8 (Tiering) and scoring framework. |
| 0.3 | 22/04/2026 | I. Johnson | I. Johnson | Completed Section 9 (Named Account List Method) covering selection criteria, sources, Claude's role in discovery and refresh, storage and format, refresh cadence, governance, and review. Single-owner, monthly refresh. |
| 0.4 | 13/07/2026 | I. Johnson | I. Johnson | Firmographic reconciliation. (1) Section 3 ICP Statement widened to 10-5,000 employees with 20-2,000 as ideal band; "planning to launch" clarified as equal weight to "migrating" in trigger detection. (2) Section 4.3 Company Size expanded to 10-5,000 with rationale for the range. (3) Section 5 adds equal-weight note for launch versus migrate. (4) Section 7 sub-scale operator anti-profile reframed as judgement pattern (small program in small market with no scale ambition), not a headcount threshold. (5) Section 8.1.3 adds reconciliation note tying scoring bands to Section 4.3 range. (6) Section 8.2 adds explicit clarification that P2 Company Size DQ does not disqualify. (7) Spelling standardised: "programme/programmes" replaced with "program/programs" throughout per Core Messaging v2.5 tone rules. |

## 2. Purpose
Define the Ideal Customer Profile for TXN. The ICP is the filter used by Marketing to target, by Sales to qualify, and by Product to prioritise. It is the anchor document for downstream GTM work including personas, messaging, qualification, campaign targeting, and the Named Account List. Everything downstream must be consistent with this document.

## 3. ICP Statement
TXN sells to companies providing, or looking to provide, payment card programs with 10 to 5,000 employees in the EEA plus the United Kingdom. The ideal band is 20 to 2,000 employees where the account scores Priority 1 or Priority 2 on the Section 8.1.3 sizing framework; smaller companies (10 to 19 employees) and larger companies (2,001 to 5,000 employees) remain in scope as Priority 3 candidates where sub-sector fit and triggers are strong. Companies fewer than 10 or more than 5,000 receive zero points on parameter P2 but are not, on that basis alone, disqualified per Section 8.2.
The company is either looking to launch a new payment card program to its customer base or is looking to migrate an existing payment card program from a competitor. Both intents are weighted equally in trigger detection, discovery, and outbound prioritisation. Launching and migrating are treated as parallel workstreams, not sequential.
These companies value the ability to self-serve their card programs by building to a comprehensive API suite and by using intuitive, comprehensive web applications provided by an issuer processor. They are seeking to move quickly with product launches, product evolution, and market expansion.
Currently, they look to issuer processors such as Marqeta, Paymentology, Thredd, Enfuce, Episode Six, and Pismo to provide these services. These competitors have significant gaps in their offerings and often drive clients to build more capabilities themselves to maximise efficiency in managing their card programs.

## 4. Firmographic Criteria

### 4.1 Sectors
FinTech, Banking, Financial Services, Retail.

### 4.2 Sub-sectors
Digital Banking, Expense Management, Lending (SMB), Lending (Consumer), FX Payments, Investment Management, Disbursement, Payments, BaaS, Retail, Ecommerce, Crypto.

### 4.3 Company Size
10 to 5,000 employees. The ideal band is 20 to 2,000 employees, where the account scores Priority 1 (50 to 1,000 employees) or Priority 2 (20 to 49 or 1,001 to 2,000 employees) on the Section 8.1.3 sizing framework.
Sub-20 employees remains in scope as Priority 3, particularly for seed and Series A fintechs planning card launches where sub-sector fit and triggers are strong. Above 2,000 up to 5,000 remains in scope as Priority 3, subject to the Tier 1 bank anti-profile exclusion at Section 7. Fewer than 10 or more than 5,000 receives zero points on parameter P2 but does not, on that basis alone, disqualify the account per Section 8.2.

### 4.4 Geography
EEA plus the United Kingdom. Phased outbound priority:
MVP: Poland, Czech Republic, Romania, Hungary.
Phase 1a: Spain, Portugal, Greece.
Phase 1b: Netherlands, Belgium, Austria.
Opportunistic: the remaining EEA plus United Kingdom markets. No EEA plus UK company is excluded from consideration; phasing governs outbound prioritisation and ABM targeting only. Inbound enquiries from anywhere in scope are accepted and qualified normally.

### 4.5 Regulatory Regime
EEA plus the United Kingdom.

### 4.6 Ownership Model
Private companies, listed companies, VC-backed, PE-controlled.

## 5. Behavioural and Situational Triggers
Triggers are the signal that an ICP-fit company is active now. Each trigger has observable signals used for detection and scoring. Companies planning to launch a new card program are weighted equally to companies migrating from an existing incumbent; discovery and outbound treat both as parallel workstreams.
New market entry: public announcement of geographic expansion, licence application filings, hiring in the target country, partner search signals.
Incumbent contract expiry: public reference to a multi-year contract with a named incumbent nearing its anniversary; RFP-like activity; executive remarks on platform change.
Incumbent service performance issues: public incident posts, press coverage of outages, customer complaints on social channels, reports of migration activity.
New product launch: roadmap announcements, funding round press releases referencing card products, hiring for card program roles, beta program invitations. Applies equally to first-time launches by companies with no existing program.

## 6. Technographic Signals
Processor: any incumbent processor is deemed a legitimate target. Named competitors include Marqeta, Paymentology, Thredd, Enfuce, Episode Six, Pismo, Carta, Visa DPS, HPS, i2C, Minisait, Thales, and Tribe, along with in-house legacy processors.
Tech stack: expectation is that the company's tech stack is cloud-based, most likely using AWS, Azure, or Google Cloud. API-first architecture is a strong positive signal.
Engineering capability: in almost all instances the company will have its own in-house engineering team, and will more than likely be utilising AI tools to accelerate development cycles.
Scheme and BIN sponsor signals: existing BIN sponsor relationship (for example Paynetics, DiPocket, Modulr, Transact Payments, Enfuce as sponsor, or Railsr), direct scheme principal membership, Apple Pay and Google Pay integration, named 3DS partner.

## 7. Anti-Profile
Any match on the anti-profile is an automatic disqualification regardless of aggregate score.
Sub-scale operators, defined by a specific pattern rather than a headcount threshold: a card program with limited scale ambition (fewer than 10,000 cards projected within 18 months), confined to a small single-market audience, with no engineering or product capacity to grow. Early-stage companies with clear scale ambition (Series A or later, or seed-stage with a defined product roadmap and hiring plan) do not match this pattern regardless of current headcount.
Governments and local governments.
Tier 1 banks (for example Barclays, BNP Paribas).
Petrol retail companies.
Companies looking for bespoke, non-platform-based solutions where the IP developed rests with the company.
Companies looking for on-premises hosting of an issuer processor solution.
Companies reported in the press as having difficulties with any local regulator, or under sanctions exposure.
Companies with limited capital available for investment and operational expenses.
Companies in active administration, insolvency, or pending wind-down.

## 8. Tiering
Tiering governs how an account is treated across Marketing and Sales. Each account is assigned a tier based on a scoring framework (Section 8.1), subject to gating rules (Section 8.2), with the resulting tier defined in Section 8.3 and the associated actions in Section 8.4.

### 8.1 Scoring Framework
Each account is scored across ten parameters to a total of 100 points. Triggers carry the largest single weight because they are the strongest indicator of why now. Geography is weighted above the standard firmographic fields because the GTM phasing governs outbound effort.

### 8.1.1 Weight Summary
| # | Parameter | Source Section | Max |
| 1 | Sub-sector / Use Case Fit | Section 4.2 | 10 |
| 2 | Company Size (employees) | Section 4.3 | 10 |
| 3 | Geography / Region Phase | Section 4.4 | 12 |
| 4 | Regulatory Licence Status | Section 4.5 | 8 |
| 5 | Ownership and Funding Stage | Section 4.6 | 8 |
| 6 | Behavioural / Situational Triggers | Section 5 | 20 |
| 7 | Incumbent Processor Signal | Section 6 | 8 |
| 8 | Tech Stack and Engineering | Section 6 | 6 |
| 9 | Scheme / BIN Sponsor Signal | Section 6 | 8 |
| 10 | Card Program Scale and Ambition | Sections 3 and 4 | 10 |

### 8.1.2 Sub-sector / Use Case Fit (max 10)
| Band | Points | Definition |
| P1 | 10 | Digital Banking, Neobank. |
| P2 | 7 | Expense Management, Lending (SMB or Consumer), BaaS, FX Payments. |
| P3 | 4 | Investment Management, Disbursement, Payments, Ecommerce, Retail, Gift Card. |
| DQ | 0 | Outside the listed sub-sectors; crypto-only with no fiat rails; staff-card-only use. |

### 8.1.3 Company Size, Employees (max 10)
| Band | Points | Definition |
| P1 | 10 | 50 to 1,000 employees. |
| P2 | 7 | 20 to 49, or 1,001 to 2,000 employees. |
| P3 | 4 | 10 to 19, or 2,001 to 5,000 employees. |
| DQ | 0 | Fewer than 10, or more than 5,000 employees. |

Section 4.3 defines the firmographic range as 10 to 5,000 employees. The scoring bands above allocate points across that range: sub-20 (10 to 19) and 2,001-plus (up to 5,000) score 4 points (Priority 3); fewer than 10 and more than 5,000 score 0. Per Section 8.2, a DQ band on parameter P2 (Company Size) contributes zero points but does not, on its own, disqualify the account. A small start-up with strong sub-sector fit, geography fit, licence fit, and active triggers can still qualify as Priority 3 or higher.

### 8.1.4 Geography / Region Phase (max 12)
| Band | Points | Definition |
| P1 | 12 | MVP markets: Poland, Czech Republic, Romania, Hungary. |
| P2 | 8 | Phase 1a and 1b markets: Spain, Portugal, Greece, Netherlands, Belgium, Austria, United Kingdom. |
| P3 | 5 | Rest of EEA, including France, Germany, Italy, Ireland, the Baltics, and the Nordics (Norway and Sweden are flagged price-sensitive but remain P3). |
| DQ | 0 | Outside EEA plus UK. MENA and Africa markets are handled as later-phase and are not disqualified on geography alone. |

### 8.1.5 Regulatory Licence Status (max 8)
| Band | Points | Definition |
| P1 | 8 | Holds an EMI or credit institution licence in EEA or UK; scheme principal member. |
| P2 | 6 | Holds a PI licence; EMI licence in application; active BIN sponsor agreement in place. |
| P3 | 3 | No licence but engaged with a BIN sponsor; regulated under a secondary regime. |
| DQ | 0 | Unlicensed with no sponsor route; licence revoked; sanctions exposure. |

### 8.1.6 Ownership and Funding Stage (max 8)
| Band | Points | Definition |
| P1 | 8 | VC-backed Series B to D with last raise within 24 months; PE-backed with a growth mandate; listed with a growth profile. |
| P2 | 6 | VC Series A; bootstrapped but profitable; PE-backed with a stable mandate. |
| P3 | 3 | Seed stage with strong investors; established private with flat growth. |
| DQ | 0 | In administration, insolvency, or pending wind-down; sanctions exposure. |

### 8.1.7 Behavioural / Situational Triggers (max 20)
| Band | Points | Definition |
| P1 | 20 | Two or more active triggers within 12 months (for example new funding round plus incumbent contract expiry window, or announced product launch plus hiring signals). |
| P2 | 14 | One strong active trigger (announced product launch, funding round within 12 months, public incumbent service issue, executive change in product or tech). |
| P3 | 7 | Weak or historical trigger (incumbent contract signed 2 to 3 years ago, early roadmap hints, low-signal hiring). |
| DQ | 0 | Recently signed a multi-year incumbent contract within the last 12 months with no offsetting trigger. |

### 8.1.8 Incumbent Processor Signal (max 8)
| Band | Points | Definition |
| P1 | 8 | Confirmed incumbent is Marqeta, Paymentology, Thredd, Enfuce, Episode Six, Pismo, or a legacy processor with known gaps. |
| P2 | 6 | Using a smaller or less-known processor, or a hybrid in-house solution. |
| P3 | 3 | Running a card program but incumbent unknown. |
| DQ | 0 | No card program and no stated plan to launch one. |

### 8.1.9 Tech Stack and Engineering (max 6)
| Band | Points | Definition |
| P1 | 6 | Cloud-native (AWS, Azure, or GCP), API-first architecture visible, AI tooling adoption signals. |
| P2 | 4 | Cloud-based with a modern stack but not API-first. |
| P3 | 2 | Hybrid stack; limited public technology signals. |
| DQ | 0 | On-premises requirement; no in-house engineering team. |

### 8.1.10 Scheme / BIN Sponsor Signal (max 8)
| Band | Points | Definition |
| P1 | 8 | Existing BIN sponsor relationship (for example Paynetics, DiPocket, Modulr, Transact Payments, Enfuce as sponsor, Railsr), or scheme principal. |
| P2 | 6 | Scheme participation visible (Apple Pay and Google Pay live, named 3DS partner). |
| P3 | 3 | No visible BIN sponsor but licensing signals suggest one is imminent. |
| DQ | 0 | No scheme participation path. |

### 8.1.11 Card Program Scale and Ambition (max 10)
| Band | Points | Definition |
| P1 | 10 | More than 500,000 cards in issue today or projected within 18 months, or a multi-product card roadmap. |
| P2 | 7 | 100,000 to 500,000 cards in issue or projected. |
| P3 | 4 | 10,000 to 100,000 cards in issue or projected. |
| DQ | 0 | Fewer than 10,000 cards projected; single staff-card use case only. |

### 8.2 Gating Rules
Aggregate scoring determines tier, but the following gating rules override the total score. Any gating hit disqualifies the account regardless of how it scores on other parameters.
Any match against the Anti-Profile (Section 7) disqualifies the account.
A DQ band on any of the four critical parameters disqualifies the account: Sub-sector (8.1.2), Geography (8.1.4), Regulatory Licence Status (8.1.5), or Triggers (8.1.7).
DQ bands on the remaining parameters contribute zero points but do not on their own disqualify the account. In particular, a DQ band on parameter P2 Company Size (fewer than 10 or more than 5,000 employees) is not a gating disqualifier: the account can still qualify as Priority 3 or higher if other parameters score sufficiently.

### 8.3 Tier Definitions
| Tier | Total Score | Additional Rules |
| Priority 1 (Tier 1) | 80 to 100 | No DQ on any parameter; no anti-profile match. |
| Priority 2 (Tier 2) | 60 to 79 | No DQ on gating parameters; no anti-profile match. |
| Priority 3 (Tier 3) | 40 to 59 | No DQ on gating parameters; no anti-profile match. |
| Disqualified | Below 40 | Or any gating DQ, or any anti-profile match. |

### 8.4 Tier Actions
Tier 1: accounts are identified and an Account-Based Marketing campaign is executed alongside a sustained, highly tailored outbound sales campaign. Any inbound lead is treated with high importance and urgency.
Tier 2: accounts are identified and LinkedIn marketing approaches are used alongside direct email marketing campaigns. Any inbound lead is handled by Sales and treated with high importance and urgency.
Tier 3: no LinkedIn or direct email marketing campaigns. Any inbound lead is handled by Sales and treated with medium importance and urgency.
Disqualified: no proactive activity. Inbound leads are politely declined or deferred, with a record kept in case qualification changes materially.

## 9. Named Account List Method
This section sets out how named accounts are selected, maintained, refreshed, and retired. The Named Account List is the operating register of ICP-fit companies under active consideration, and it is the single starting point for all Marketing and Sales motion across tiers.

### 9.1 Purpose and Scope
The Named Account List is the register of companies identified as ICP-fit and considered candidates for proactive engagement. Every record carries a score against Section 8, a derived tier, and a set of attached contacts and trigger events. The list is the single operating view of TXN's addressable market at any point in time, and drives the tiered activity defined in Section 8.4.
The list is not a marketing contact database. It is deliberately narrow: only companies that pass firmographic, anti-profile, and minimum-score thresholds appear. Companies evaluated and disqualified are retained on the register with a Disqualified status for audit, re-qualification, and lookback.

### 9.2 Selection Criteria
A company is added to the Named Account List when it meets all of the following:
Passes the firmographic criteria of Section 4 (sector, sub-sector, size, geography, regulatory regime, ownership).
Clears the Section 7 anti-profile with no matches.
Scores 40 or above against the Section 8 scoring framework and is assigned Tier 1, 2, or 3.
Operates in EEA plus UK territory with a registered entity or a documented intent to register.
Has at least one identified contact or a clear path to discovering one within 30 days of addition.

### 9.3 Sources
Candidates are surfaced from two tiers of source.

### 9.3.1 Primary (authoritative, structured)
Regulatory registers: EBA public register of Payment Institutions and Electronic Money Institutions, plus national equivalents (FCA in the UK, BaFin in Germany, KNF in Poland, CNB in the Czech Republic, ANAF in Romania, MNB in Hungary, and equivalents across remaining EEA jurisdictions). These are the single highest-quality feeds because they pre-filter to licensed entities.
Scheme and BIN Sponsor directories: Visa's published partner directory, Mastercard Connect, and the public client pages of Paynetics, DiPocket, Modulr, Transact Payments, Enfuce as sponsor, and Railsr.
Competitor case study pages: Marqeta, Paymentology, Thredd, Enfuce, Episode Six, and Pismo all publish client references on their websites. These are companies currently under contract with an incumbent and are the highest-fit targets for contract-expiry plays.

### 9.3.2 Secondary (signal-rich, unstructured)
Fintech databases: Dealroom.co (European focus, generous free tier, prioritised for Europe), Crunchbase, Pitchbook, Sifted database.
News and trigger feeds: Sifted, Finextra, The Paypers, FinTech Futures, Finovate. Used to detect funding rounds, product launches, executive moves, incumbent churn.
Job posting signals: LinkedIn, Welcome to the Jungle (EU). Keyword searches such as Marqeta, card issuing, BIN Sponsor, Apple Pay integration surface companies hiring for card program roles.
Contact enrichment: Apollo.io or ZoomInfo for contact data; LinkedIn Sales Navigator for verification. Treated as a separate refresh layer given paid tooling and independent update cycles.

### 9.4 Claude's Role in Discovery and Refresh
Claude operates as the orchestration layer above the list. It is responsible for discovery, initial classification, and scheduled refresh; the owner retains decision authority on list composition.

### 9.4.1 What Claude does
Runs a monthly scheduled task (see Section 9.6) to scan the primary and secondary sources for new candidate companies.
Applies Section 4 firmographic filters and Section 7 anti-profile exclusions to each candidate before surfacing.
Drafts a provisional score against the Section 8 framework using publicly available data, with a provisional tier recommendation and rationale.
Produces a shortlist of new candidates with score drafts for owner review, alongside a refreshed view of existing records where any attribute has changed (employee count, funding stage, regulatory status, new trigger events).
Writes every refresh run to the Audit Log tab of the workbook, capturing records checked, records changed, new accounts added, tier changes, and triggers detected.

### 9.4.2 What Claude does not do autonomously
Pull personal contact email addresses at scale. Contact enrichment remains a human-initiated action through Apollo, ZoomInfo, or LinkedIn Sales Navigator.
Send outbound messages. Claude may draft tailored outbound copy on request, but sending remains a human action.
Promote an account between tiers. Claude surfaces proposed changes; the owner approves or rejects.
Archive or retire records without owner approval.

### 9.5 Storage and Format
The Named Account List is held in a single Excel workbook, TXN_GTM_Qualification_Matrix, in 07_GTM/04_Sales_Motion/. Despite the legacy filename, this workbook is both the scoring engine and the Named Account List register. Sheet layout:
02_Scoring_Register: one row per account. Carries firmographic attributes, Section 8 scoring, derived tier, recommended action, status, and workflow fields.
03_Contacts: one row per contact, with foreign key to Account ID. Carries name, title, role category (Champion, Economic Buyer, Primary User, Influencer), contact details, and engagement history.
04_Triggers: one row per detected trigger event, with foreign key to Account ID. Carries date, trigger type, description, source URL, priority, and action taken.
05_Audit_Log: one row per refresh run. Captures what Claude or the owner did and what changed.
Reference tabs (Parameter Reference, Anti-Profile Reference, Tier Definitions, Lookups) hold band definitions, validated values, and dropdown sources.
The data model is CRM-ready. When a CRM is in place, every column translates column-for-column: Account ID becomes the CRM record identifier, Contacts becomes the CRM contacts object with Account ID as the relationship key, Triggers becomes activities or events, and the Audit Log becomes the system audit trail. The workbook is a staging layer until the CRM is in place, after which the workbook is archived.

### 9.6 Refresh Cadence
| Cadence | Activity | Who |
| Monthly (full-list) | Claude scans primary and secondary sources, produces a shortlist of new candidates and a refresh delta on existing records. Owner reviews and approves within one working week. | Claude + Owner |
| 90-day rolling | Every record is re-scored and re-checked on a rolling 90-day basis (one third of the list each month), so no record goes stale. | Claude |
| Event-driven | When Claude detects a high-priority trigger (new funding round, incumbent announcement, executive change), it surfaces it inside the month regardless of the rolling review window. | Claude |
| Ad-hoc | New candidates discovered by the owner or team are added immediately with a provisional score, then validated at the next monthly refresh. | Owner |

### 9.7 Governance
Ian Johnson is the Named Account List owner. Owner approval is required for the following:
Adding a new account to the list.
Any tier change, whether an upgrade or a downgrade.
Archiving or retiring an account (moving to Dormant status).
Any structural change to the workbook schema (new tab, new column, new validated value).
Day-to-day data entry does not require approval. Adding contacts to the Contacts tab, recording activities and notes, and logging triggers in the Triggers tab are free actions.
When an SDR or sales hire joins, this owner role can be delegated. Structural changes remain an owner-approved action.

### 9.8 Review and Retirement
An account is archived (moved to Dormant status) when any of the following apply:
A deprioritisation trigger is hit: the account signs a new multi-year contract with an incumbent, is acquired by a Tier 1 bank, or loses its regulatory licence.
Twelve months pass with no engagement and no new triggers of any kind.
A re-scoring pass puts the account below the 40-point threshold.
An anti-profile match is newly discovered that was not visible at the time of original scoring.
Archived accounts remain in the workbook for audit and for re-qualification if circumstances materially change. A Dormant account is re-activated by a new scoring pass and owner approval.
