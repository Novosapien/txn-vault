---
description: "Raw research corpus behind the discovery source register: eight research streams, seven adversarial validation reports, and the client-facing register"
---

# Research

The working corpus behind [[discovery-sources]]. Routed from [[outbound]].

Commissioned in the ICP interview of 25 August 2026 and run over a single day. Eight research streams produced 299 source entries. Seven independent validators were then told to attack the findings rather than confirm them, each re-fetching claims with a different toolchain.

**This directory holds the evidence, not the conclusion.** [[discovery-sources]] is the synthesis and the document to read first. Everything here is the working out: what was fetched, what it returned, and what a second agent found when it tried to knock the claim down.

## Why the raw files are kept

Ian asked specifically for validation that the research was not invented. That request is only answerable if the primary material survives. Each entry carries the URL that was actually fetched, a per-claim confidence grade, and an evidence note recording what the retrieval returned. The validation reports then re-test those claims and name every correction. Deleting the working files would leave the synthesis unfalsifiable.

## The streams

| Stream | What it covers | Entries | Validation |
|--------|----------------|---------|------------|
| [[stream-01-cee-accelerators]] | The four MVP markets, plus regional programmes that recruit into them. Bank-run programmes are the fintech-dense layer and they are split: two excellent and current, several quietly dead. | 35 | [[validation-01-cee-accelerators]] |
| [[stream-02-paneuropean-accelerators]] | Programmes that recruit across borders. Denser in fintech than the national programmes, and more of it is already prospected by competitors. | 34 | [[validation-02-paneuropean-accelerators]] |
| [[stream-02b-accelerator-leads-followup]] | A second pass chasing accelerator leads the first pass could not close, plus the national startup registers it surfaced. | 27 | **Not validated** |
| [[stream-03-investor-portfolios]] | Fund portfolio pages, treated as a new-deal feed. The prize is a per-company investment date in served HTML, which turns a crawl into a change feed. | 54 | [[validation-03-investor-portfolios]] |
| [[stream-04-scheme-and-sponsors]] | Visa and Mastercard programmes, BIN sponsors, programme managers and the trade associations around them. Read here for the negative space, because this layer observes companies that already have a card programme. | 37 | [[validation-04-scheme-and-sponsors]] |
| [[stream-05-vertical-saas-fringe]] | The companies that will need cards and do not know it yet. Hiring signals, vertical SaaS marketplaces, trademark filings and regulatory registers, none of which is a card signal. | 30 | [[validation-05-vertical-saas-fringe]] |
| [[stream-06-events-media-communities]] | Pitch shortlists and awards shortlists are the reliable artefact, published by name in plain HTML weeks ahead because the organiser wants the coverage. | 42 | [[validation-06-events-media-communities]] |
| [[stream-07-southern-benelux-nordics]] | National statutory registers and ecosystem directories outside CEE. This is where the Phase 1a markets turn out to be better covered than three of the four MVP markets. | 40 | [[validation-07-southern-benelux-nordics]] |

## The validation reports

| Report | Headline verdict |
|--------|------------------|
| [[validation-01-cee-accelerators]] | The file is sound. It was not invented. Three inflated counts and two company names attributed to lists they were not on. |
| [[validation-02-paneuropean-accelerators]] | The research is real. The failure mode is not fabrication, it is walls reported where none exist. |
| [[validation-03-investor-portfolios]] | All 54 entries checked, not a sample. Character drift of 0.5 to 2 per cent in both directions is itself evidence the numbers were measured. |
| [[validation-04-scheme-and-sponsors]] | An unusual density of falsifiable detail, correct essentially every time. One entry materially wrong. |
| [[validation-05-vertical-saas-fringe]] | The file is trustworthy. None of the corrections changes a conclusion, and two of the three top-line findings get stronger. |
| [[validation-06-events-media-communities]] | The research is real. The precise counts are unreliable, and one market-coverage claim directly misleads on an MVP market. |
| [[validation-07-southern-benelux-nordics]] | Two access claims and one population figure were materially wrong. Three sources were undersold and are upgraded. |

**No fabricated source was found in any stream.** The total fabrication yield across all seven checks was two company names attributed to lists they were not on. Three systematic defects were found instead: counts estimated where counting was possible and usually high, sources written off as blocked that were not, and `Verified` applied per entry rather than per claim.

## The client deliverable

`txn-discovery-source-register.html` is the TXN-branded register built from these files: all 299 sources, filterable by stream, market, source type, access route and confidence, with every validator correction printed on the entry it corrects. It is a single self-contained file and is the version to send.

## Open action

[[stream-02b-accelerator-leads-followup]] has had no independent adversarial check. It was written after the validation agents finished. Its 27 entries include four national startup registers that now sit among the strongest sources in the whole corpus, so validating it is worth doing.
