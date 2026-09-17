---
description: "Review of Dorte Dye's 41 open console feedback records, the transcript evidence behind each theme, and the questions TXN must answer"
---

# TXN: Dorte's feedback review (2026-09-17)

> **Index:** [[index]] · **Delivery:** [[delivery]] · **Component:** [[full-agentic-experience]]
>
> **Source:** The TXN admin panel feedback queue, schema `txn.feedback`, read on 17 September 2026. All 41 records that Dorte Dye submitted are open at `review_status = New`. The agent-side evidence comes from the conversation transcripts in the agent database, which this review read in full.

## What this document is

Dorte ran the UAT sessions on 21 August, 8 September and 11 September, and added one record on 14 September. This review groups every record she filed, states what the transcript shows behind it, and separates the defects Novosapien must fix from the questions only TXN can answer.

The queue holds 90 open records in total. The other 49 come from Michael Moores and from Novosapien's own test accounts, and they are out of scope here.

## The headline

**Approval gates did not run.** Between 8 and 14 September the agent made **68 writes** across nine conversations and rendered **zero approval cards**. The writes include card blocks, card terminations, account closures, spend-control creates and a spend-limit change. Earlier conversations on 15 August and 3 September did render approval cards, so this is a regression, not an absent feature.

The agent also stated the position to Dorte in plain words: *"Approvals are disabled in this deployment. The platform does not pause for interactive confirmation gates in this environment."*

Two consequences are already on record:

- The agent closed two accounts for James Thornton that held **£184,200.00 and €2,340.00** after a single "Proceed" reply. No approval card, no balance warning beyond a sentence in the plan.
- The agent changed a live daily spend control from £200.00 to £500.00, and ran the backtest and the write in the same turn (record `b938d267`, 14 September).

## Theme 1 — Approvals and impact previews

| Record | Date | What Dorte said | What the transcript shows |
|--------|------|-----------------|---------------------------|
| `f28b9779` | 11 Sep 12:51 | "It didn't ask for approval or told me the impact" | Two £500 spend overrides written with no gate |
| `c5e9620f` | 11 Sep 12:53 | The explanation was good, the response was slow | The agent said approvals are disabled and impact backtests apply only to programme-level controls |
| `b938d267` | 14 Sep 16:04 | "It changed the limit without me reviewing the impact first — no request for approval either" | Backtest, write, read-back and two test authorisations in one turn |

**Novosapien owns this.** The approval gate is the core safety promise of the governed-write design, and it must hold in UAT and in production.

## Theme 2 — Speed

Eight of Dorte's records name speed. The transcripts give the numbers.

| Record | Date | Comment | Measured |
|--------|------|---------|----------|
| `a681f8d9` | 11 Sep 13:14 | "it took quite a while to action — not sure if this flow adds value at this speed" | PIN reset, 22 to 33 s per turn |
| `e755b47a` | 11 Sep 13:18 | "takes too long. I stopped to add comment" | 119 s to the first action |
| `0f6b1662` | 11 Sep 13:22 | "far too slow!" | 100 s to list one cardholder's transactions |
| `2af1f478` | 11 Sep 13:26 | "too slow" | Same PIN-reset conversation |
| `dcc346e2` | 11 Sep 13:27 | "too slow" | 90 s to find one declined transaction |
| `07d12e29` | 11 Sep 14:00 | "took far too long 11 tool calls" | 119 s before the plan appeared |
| `57b9ac2b` | 11 Sep 15:12 | "getting to the program list took ages" | 142 s, more than 30 calls |
| `c5e9620f` | 11 Sep 12:53 | "Slow in response but good response" | 39 to 59 s per turn |

**Cause, from the tool traces:** the agent re-reads its SOP files on almost every turn, pages `list_cardholders` up to six times in one turn, repeats `get_cardholder_cards` ten times in a single message, and sometimes spawns a subagent for a lookup it already holds. The speed remediation recorded in [[delivery]] on 16 September addresses this workstream.

## Theme 3 — Too much ceremony for a simple action

- **"Freeze" is not a test run.** Dorte asked the agent to freeze a card. The agent ran the `suspend-card` procedure, which suspends the card, tests a declined payment, reactivates the card and tests an approved payment. The card ends **active**, which is the opposite of the request. She asked afterwards: *"i don't understand why dod you reactive the card?"* (`07d12e29`).
- **The same procedure ran twice.** In conversation `6a8f42e5` the full suspend-and-reactivate cycle ran in two consecutive assistant turns, 11 seconds apart, after Dorte sent two messages in quick succession. That is eight writes for one request (`e755b47a`).
- **A terminated card still got the full diagnosis.** The agent ran its four decline checks on a card that reads terminated. Dorte: *"not sure why I need all the checks if you could have just told me the card is terminated"* (`0ae502b8`).

## Theme 4 — Lost and stolen card handling

| Record | Comment | Transcript |
|--------|---------|------------|
| `adb18359` | "I can't give it the expiry date and it still lets me block the card — asking for the last 4 digit for a the card when showing it to me seems pointless" | The agent demanded the last four digits and the expiry, then said the platform holds no expiry date, then blocked on the last four digits alone |
| `cfd5417c` | "it also didn't ask if is lost or stolen" | The agent went to a permanent termination without that question |

**A defect the transcript adds:** the replacement card came back with the **same card ID and the same last four digits** as the terminated card (`f46af31e-977a-54f0-b100-22525ff53d7a`, `•••• 5126`). The agent then told Dorte it was "a completely distinct card record". The mock API mints deterministic identifiers, and two spend controls in separate conversations also share one ID (`2cc0f527-24a9-5600-ab0d-f25cb659b7f8`). Test data must not produce a collision that the agent then explains away.

## Theme 5 — Only offer what the platform supports

| Record | Comment |
|--------|---------|
| `23525b06` | "We need to make sure that we only offer what we are capable of. we can't do Google and ApplePay yet (same for 3DS but that will be address before console launch)" |
| `ece4cb44` | "why asking if I want to fund the account if it is not possible?" |
| `0914fd73` | "different answer in product then UAT — there is asked me for the funding source" |
| `da7d55d0` | "if only prefund is available can you not auto set it?" |

The agent offers Apple Pay provisioning, 3-D Secure enrolment and account funding, then says funding cannot be done from the console. In UAT it asks for the funding type. In production it defaults to `Prefunded` and admits the omission only when challenged.

## Theme 6 — Spend controls

- **A unit defect.** The agent created a €1,000 daily control and a €3,000 monthly control. The platform stored `1000` and `3000` **minor units**, so the real limits were €10.00 and €30.00. A €50 test payment then declined. Dorte: *"unit issue — needs to be fixed in the back"* (`46c11fa7`). The agent's explanation put the error on the operator's input, although the agent built the call.
- **Scope is disputed.** The agent states that spend controls sit at BIN sponsor level and cannot be scoped to a programme. Dorte answered directly: *"Spend controls are not applied at BIN Sponsor Level at all."* She also found that the agent treats every programme as hers under an admin login (`fe01fe0c`), and that it asked for the limit before it asked for the programme (`57b9ac2b`).
- **Merchant categories.** When the agent blocks a category it names no MCC. Dorte asked for the list: *"does wire transfer has an MCC too? if so list"* (`3e0da486`).
- **A question for TXN, not for us.** *"1. Automated flow @Mike I assume we need to check that with each Sponsor?"* (`a4bf2d31`).

## Theme 7 — Rendered components and chat data

- **Every rich card failed.** `render_transactions`, `render_card_detail`, `render_cardholder_detail`, `render_transaction_detail` and `render_account_detail` failed in 24 of the 28 transcripts, from 4 August to 14 September, in UAT and in production. The error is the same each time: `Cannot read the seed export at /app/seed/fixtures.json ... Set SEED_FIXTURES`. The environment variable is not set on the deployed service. The agent falls back to a plain table, so the data still reaches the operator.
- **The raw error reaches the operator.** Michael's records show the developer text in the chat, for example "Couldn't render render_transactions / txns: Required; cards: Required". Dorte's records do not name it, but her sessions hit the same failure.
- **Seed data quality.** "some phone numbers are marked some not" (`2a835458`) and "not all emails match the name" (`23e1c745`). For example, Marcus Chen's record carries `liam.p@apexdigital.io`.

## Theme 8 — Console pages, 21 August and 8 September

| Record | Page | Comment |
|--------|------|---------|
| `438b8d4b`, `01f69e8b`, `013aa6e6` | Access > Users | "I canged the department, role and program access and it wouldn't save" |
| `ea7a355c` | Access > Users | The change appeared only after the user went back to active |
| `7878847f` | Access > Users | The save took a long time, and the dotted-line state looks too much like the new one |
| `ace13efd` | Configure > Program overview | "can't terminate" — the confirm dialog does not complete |
| `681ebb9d`, `b364bb18` | Configure > Program overview | "not required in the console", "this should also sit in the crm not in the console" |
| `126cca8a`, `7c26f7ef` | Configure > Card products | "the card format is off they are all too wide" |
| `ac9a5232` | Service > Cardholder groups | "the new group button does not work for me" |
| `6a068497` | Integrate > API keys | The information tooltip closes before the guide link can be clicked |
| `55c06818` | Production overview | The ⌘K search returns "No results for report a card lost" |
| `0f98792f` | UAT overview | "the page never reaches an idle state, so the extension times out every time" |
| `6d7f8d2c`, `c09f41f6` | Agent chat | "we should not reference DT — terminology for AC is not right ... Customer Success Manager" |
| `78012945` | Agent chat | "it should be all captial — not sure why travel and credit is not" |

## What Dorte praised

> "this is brilliant - spend control section" — `d0558a60`, 11 September 14:24.

She also called the agent's explanation of the UAT approval position a good answer, even while she marked the response slow (`c5e9620f`).

## Questions for TXN

1. **Card block verification.** The console holds no card expiry date. What must an operator confirm before a block: the last four digits alone, or something else? When must the agent ask whether a card is lost or stolen?
2. **Spend control scope.** At what level do controls really apply — programme, product, or BIN sponsor? Dorte rejects the sponsor-level answer the agent gives.
3. **Programme ownership.** What should an admin user see? The agent treats every programme on the estate as theirs.
4. **Supported features at launch.** Confirm which of Apple Pay, Google Pay, 3-D Secure and account funding the agent may offer. If `Prefunded` is the only funding type, the agent can set it and say so.
5. **Console scope.** Program overview: remove the page, or keep it and fix the terminate action?
6. **The sponsor question.** Dorte's own note to Michael asks whether the automated flow needs a check with each sponsor.

## Where the work goes next

Every theme above becomes one scoped piece of work through the triage route: `/client-feedback-triage txn` proposes the buckets, the triage document records them, and each bucket opens a `/discovery` run. This review is the evidence layer under that process. No record has been marked or commented in the panel yet.
