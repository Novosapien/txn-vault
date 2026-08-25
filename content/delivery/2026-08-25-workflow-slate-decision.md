---
description: "TXN's decision on the ten-workflow candidate slate: Michael's ranked order, the principle behind it, and what it settles and leaves open"
---

# TXN: workflow slate decision (2026-08-25)

> **Index:** [[index]] · **Delivery:** [[delivery]] · **Component:** [[full-agentic-experience]]
>
> **Source:** Email from **Michael Moores**, Global Head of Technology, TXN, to George Westbrook, 25 August 2026. Recorded here because it is a decision rather than a meeting, and the vault has no other home for the workflow slate.

## What this settles

The Novosapien candidate slate, *Ten new workflows, you choose what earns a build*, was sent to TXN asking for a decision on every card: build next, park, or not this. **That confirmation had not come back**, and it was tracked as the open item blocking forward workflow planning ([[delivery]], flight plans v4 and v5).

**It has now come back.** Michael has ranked all ten and named a flagship. The blocker is cleared.

## The principle TXN applied

> "The principle we have applied is **depth before breadth** for the initial workflow build."

One complete loop built properly, rather than ten shallow ones. This is the same instinct behind the six SOPs already operational.

## The decision

### Build first, the flagship

**Decline investigation, with the fix attached** (slate candidate 3).

Michael's reasoning, recorded because the criteria are reusable for future ranking:

- Highest daily volume of anything on the list
- The investigation half already runs in the pilot as `investigate-declines`
- No external dependency
- It is where TXN's operators naturally start
- Done properly it is a complete loop: cause identified, explained in language TXN can give a customer, fix offered, fix proven
- The fix half reuses the spend-control workflow already built, *"which is what makes it deep without being expensive"*

### Then, in TXN's stated order

| TXN rank | Slate # | Workflow | Tool coverage today | Build cost |
|---|---|---|---|---|
| **1** | 3 | **Decline investigation, with the fix attached** | 5 of 6 | Low |
| 2 | 4 | VIP spend exception | 2 of 4 | Medium |
| 3 | 2 | Card service actions | **0 of 6** | High, needs a tool-building round first |
| 4 | 5 | Merchant control change with impact | 2 of 5 | Medium |
| 5 | 1 | Cardholder offboarding | 5 of 6 | Low |
| 6 | 6 | Bulk change with a scaled confirmation | 3 of 5 | Medium, also needs the irreversible-action policy settled ([[open-questions]] #26) |
| 7 | 8 | Alert to investigation to proposed plan | 6 of 6 | Lowest on the slate, but alert detection is unowned |
| 8 | 7 | Create a monitoring alert by conversation | 2 of 3 | Partner blocked: needs Direct Transact to agree an alert write |
| 9 | 9 | Scheduled performance report with drivers | 3 of 4 | Partner blocked: needs the data lake, which DT has not delivered |
| 10 | 10 | Guided product launch | 2 of 6 | Largest build on the slate |

**Tool coverage** counts how many of each workflow's listed endpoints already exist as MCP tools. It is the cost signal, not a comment on value. TXN ranked by value, which is the right basis for the decision; the coverage column is recorded alongside it so sequencing can be planned with both numbers visible.

**Worth noting when the order is scheduled:** the two cheapest builds on the slate sit at ranks 5 and 7, and the most expensive sits at rank 3. Card service actions has **no tool coverage at all**, so it needs a full tool-building round before any of it can run. Adjusting for this is straightforward and TXN's ranking does not need to change; it is a scheduling observation rather than a challenge to the decision.

### Candidates 8, 9 and 10 are now legitimised

All three were **Novosapien concepts TXN had not asked for** and were marked as such in the slate and the flight plans. TXN has now ranked them, so they are TXN-wanted work rather than Novosapien suggestions. Candidate 8 in particular is the cheapest build on the whole slate at 6 of 6 coverage.

## What TXN is still doing

> "We are still completing our review. We have written all thirteen up as journey documents on our side and will confirm the endpoints, the approval gates and the rest through next week. We will also look at producing more workflows where we have identified them."

Three things follow from this:

1. **TXN is producing journey documents for all thirteen workflows.** Thirteen is most likely the ten candidates plus the three the slate describes as already operational. This is valuable material and should come into the vault when it lands.
2. **Endpoints and approval gates confirmed through next week**, which is input arriving during the pilot's final fortnight.
3. **More workflows to come**, so the slate is a starting point rather than a closed set.

## What this does not settle

| Open item | Why it still matters |
|-----------|---------------------|
| **Where the cut line falls.** The slate asked for build next, park, or not this. TXN ranked all ten and parked or rejected none | A ranked list without a line under it does not bound scope. Ranks 8 and 9 are partner blocked regardless of position, so they cannot be scheduled on rank alone |
| **The slate's descriptions of the three "operational" workflows are inaccurate**, and TXN may be writing journey documents against them | The slate describes cardholder onboarding as operational; it is not implemented and the tool surface does not support it. Lost or stolen card is only partially implemented. **The long-standing alignment action is now more pressing**, because TXN is documenting against those descriptions |
| **The word "pilot."** Michael frames this as *"the initial workflow build in the pilot"* | The pilot build definition is frozen and it completes 7 September. This work lands after acceptance. Worth confirming the landing point with TXN so both sides hold the same picture |

## What it answers by implication

**Who the operator is.** [[open-questions]] and flight plan v4 both carried the question of whether the pilot's operator is a customer-service agent or a programme administrator. Michael's phrasing points to the former: *"where our operators naturally start"* and *"explained in language we can give a customer."* Worth confirming explicitly, since it shapes field-level detail per persona and the design of several ranked workflows.

---

## Source

Email from Michael Moores to George Westbrook, 25 August 2026. Reproduced below; the LinkedIn signature block has been trimmed.

> Thanks George,
>
> Thanks for the two documents. They gave us what we needed to make a call, and the level of detail on the endpoints and the governance pattern was genuinely useful. We have decided on the order below. The principle we have applied is depth before breadth for the initial workflow build in the pilot.
>
> **Build first**
>
> Decline investigation, with the fix attached. This is our pick for the flagship build. It is the highest daily volume of anything on the list, the investigation half already runs in the pilot, it has no external dependency, and it is where our operators naturally start. Done properly it is a complete loop: cause identified, explained in language we can give a customer, fix offered, fix proven. The fix half reuses the spend-control workflow you have already built, which is what makes it deep without being expensive.
>
> **Then, in this order**
>
> 2. VIP spend exception
> 3. Card service actions
> 4. Merchant control change with impact
> 5. Cardholder offboarding
> 6. Bulk change with a scaled confirmation
> 7. Alert to investigation to proposed plan
> 8. Create a monitoring alert by conversation
> 9. Scheduled performance report with drivers
> 10. Guided product launch
>
> We are still completing our review. We have written all thirteen up as journey documents on our side and will confirm the endpoints, the approval gates and the rest through next week. We will also look at producing more workflows where we have identified them.
>
> Kind regards,
> Mike Moores
> Global Head of Technology
