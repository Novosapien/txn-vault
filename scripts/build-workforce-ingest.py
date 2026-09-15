#!/usr/bin/env python3
"""Emit the TXN outbound artefacts as workforce-ready Markdown.

    python3 scripts/build-workforce-ingest.py

The vault documents are written for people: frontmatter, routers, wikilinks,
authoring apparatus. The Cold Outreach Workforce stores one row per object and
feeds its `definition` / `description` field verbatim to the agents. So this
splits the vault set into one self-contained file per row, strips the apparatus,
flattens the links, and re-labels the ICP records into the canonical template the
grading rubric is written against.

The vault stays the source of truth. Re-run after any edit; never hand-edit the
output.
"""
import re, os, datetime

VAULT = "/home/brett/Programming/txn/txn-vault/content/outbound"
OUT = "/home/brett/shared/clients/txn/outbound/workforce-ingest"

NOW = datetime.datetime.now(datetime.timezone.utc)
STAMP = NOW.strftime("%-d %B %Y, %H:%M UTC")

ICPS = [
    (1, "first-program-card-essential", "First program, card is essential", "EXPOSURE"),
    (2, "new-program-incumbent-stays", "New program, incumbent stays", "CONSTRAINT"),
    (3, "industry-inference", "Industry inference", "FALLING BEHIND"),
    (4, "full-switch", "Full switch", "ENTRAPMENT"),
]

# Wikilink targets that have no meaning outside the vault, rendered as plain prose.
LINK_NAMES = {
    "offer": "the offer", "offer-draft": "the superseded offer draft",
    "icp-definition": "the ICP definition", "buyer-personas": "the buyer personas",
    "outbound": "the outbound engagement record", "open-questions": "the open questions register",
    "delivery": "the delivery record", "delivery-schedule": "the delivery schedule",
    "commercial": "the commercial record", "vision": "the product vision",
    "qualification-matrix": "the qualification matrix", "prospecting-process": "the prospecting process",
    "fraud-risk-assist": "the fraud and risk assist component",
    "persona-champion": "the champion scaffold", "persona-primary-user": "the primary-user scaffold",
    "persona-economic-buyer": "the economic-buyer scaffold",
    "personas-icp-1": "the ICP 1 personas", "personas-icp-2": "the ICP 2 personas",
    "personas-icp-3": "the ICP 3 personas", "personas-icp-4": "the ICP 4 personas",
    "2026-09-02-outbound-workforce-icp-qualification": "the 2 September session record",
    "2026-09-03-outbound-workforce-icp-statuses": "the 3 September session record",
}


def read(name):
    return open(f"{VAULT}/{name}", encoding="utf-8").read()


def clean(t, drop_router=True):
    """Strip frontmatter, vault routers and wikilinks."""
    t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)
    if drop_router:
        t = re.sub(r"(?m)^> \*\*(Up|Parent ICP|Readable HTML version|Status|Built|Upstream)\*\*.*\n", "", t)
    t = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]",
               lambda m: LINK_NAMES.get(m.group(1), m.group(1).replace("-", " ")), t)
    return re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"


def fix_tables(t):
    """icp-definition.md writes tables without a header separator. Add one so the
    output is valid Markdown for anything downstream that parses it."""
    out, lines, i = [], t.split("\n"), 0
    while i < len(lines):
        if lines[i].startswith("|"):
            blk = []
            while i < len(lines) and lines[i].startswith("|"):
                blk.append(lines[i]); i += 1
            if len(blk) > 1 and not re.fullmatch(r"\|[\s:|-]+\|?", blk[1].strip()):
                cols = len([c for c in blk[0].strip().strip("|").split("|")])
                blk.insert(1, "|" + "|".join(["---"] * cols) + "|")
            out += blk
        else:
            out.append(lines[i]); i += 1
    return "\n".join(out)


def section(text, start_pat, end_pat=None):
    m = re.search(start_pat, text, re.M)
    if not m:
        return ""
    rest = text[m.start():]
    if end_pat:
        e = re.search(end_pat, rest[1:], re.M)
        if e:
            rest = rest[:e.start() + 1]
    return rest.rstrip() + "\n"


HEADER = """<!-- GENERATED. Source of truth is the TXN vault at content/outbound/.
     Rebuild with: python3 scripts/build-workforce-ingest.py
     Never hand-edit this file: the next rebuild overwrites it. -->

"""

RULES = """## Standing rules, binding on every message

These are not style preferences. The critic enforces them, and each one was ruled by the client.

1. **Never name a competitor of TXN's.** Contrast against categories only, even if the prospect names one first.
2. **Never criticise the competition**, named, implied or by category. Binding in all four ICPs, including where the buyer is actively leaving somebody. State what TXN does, never what the other cannot. The "where it falls short" material in the offer is context-not-quotable: ground on it, never voice it.
3. **Never claim TXN is accredited.** TXN holds no accreditation of its own. PCI is held by Direct Transact, its co-founding owner. SOC 2 and ISO 27001 are unknown. The only permitted form is that the platform is operated within Direct Transact's accredited environment.
4. **Never lead with the owners.** Direct Transact and Paycorp do not appear in first touch or the follow-up sequence. They are credibility deployed later, by a person.
5. **No pricing figures, ever.** Ground on the shape of the pricing. Figures are a conversation for a human.
6. **Never describe how the platform was built.** The claim is that the platform is TXN's. No code lineage, in either direction.
7. **Never describe the launch process.** The under-ten-business-day figure is quotable as a stated target. The mechanism behind it is not written down, so it may not be described.
8. **Never offer to share the reissue cost.** ICP 4 only. It is not an existing lever.
9. **Naming a prospect's own peer is not the same as naming a competitor.** ICP 3 only, where the peer is the qualification evidence and the opening. What may never be said is which processor that peer used.
"""


def build_offer():
    t = clean(read("offer.md"))
    doctrine = section(t, r"^## Vocabulary doctrine", r"^## Section 1:")
    body = section(t, r"^## Section 1:", r"^## The gaps list")
    return (HEADER
            + "# TXN Offer\n\n"
            + "> **Object:** the Offer. One row. This document fills its description field and flows verbatim to the creation, critic and iteration agents, so everything in it is permitted truth and nothing outside it may be stated.\n"
            + f"> **Generated** {STAMP} from the TXN vault. Authoring apparatus removed: the build notes, the gaps list and the self-review gate live in the vault copy.\n\n"
            + doctrine + "\n" + body)


def build_icps():
    src = fix_tables(clean(read("icp-definition.md"), drop_router=False))
    # Inherited fit definition: every ICP carries these unchanged.
    inherited = "\n".join([
        section(src, r"^## 3\. ICP Statement", r"^## 4\."),
        section(src, r"^## 4\. Firmographic Criteria", r"^## 5\."),
        section(src, r"^## 5\. Behavioural", r"^## 6\."),
        section(src, r"^## 6\. Technographic", r"^## 7\."),
        section(src, r"^## 7\. Anti-Profile", r"^## 8\."),
    ])
    files = []
    for n, slug, name, pain in ICPS:
        nxt = rf"^### ICP {n+1}\." if n < 4 else None
        rec = section(src, rf"^### ICP {n}\. ", nxt)
        # Re-label into the canonical template the grading rubric is written against.
        rec = re.sub(rf"^### ICP {n}\. .*$", f"### ICP Definition: {name}", rec, count=1, flags=re.M)
        rec = rec.replace("**Archetype name:**", "**1. ICP Archetype Name:**")
        rec = rec.replace("**Core thesis.**", "**2. Core Thesis.**")
        rec = rec.replace("#### Tier 1: business type",
                          "**3. Rubric-Aligned Profile**\n\n#### Tier 1: Specific Business Type (50% weight)")
        rec = rec.replace("#### Tier 2: business model", "#### Tier 2: Business Model Category (30% weight)")
        rec = rec.replace("#### Tier 3: firmographics", "#### Tier 3: Firmographics (20% weight)")
        rec = rec.replace("#### Disqualifiers", "**4. Disqualification Criteria (Anti-Signals)**")
        rec = rec.replace("#### Buying group", "**5. Buying Group**")
        rec = rec.replace("#### Signal to pain mapping",
                          f"**6. Archetype-to-Pain Mapping (sharpened for {pain})**")
        doc = (HEADER
               + f"# ICP {n}: {name}\n\n"
               + f"> **Object:** an ICP. One row. This document fills its definition field, and the Tier 1, 2 and 3 weights below are the grading rubric the workforce scores leads against: Tier 1 business type 50 per cent, Tier 2 business model 30 per cent, Tier 3 firmographics 20 per cent, grade A at 70 per cent or above.\n"
               + f"> **Dominant pain:** {pain.lower()}. One pain per ICP, distinct from the other three.\n"
               + f"> **Personas:** held as separate rows, in personas/, each a child of this ICP.\n"
               + f"> **Generated** {STAMP} from the TXN vault.\n\n"
               + rec.rstrip() + "\n\n---\n\n"
               + "## Inherited fit definition\n\n"
               + "Every ICP inherits these unchanged. They decide who is in the market at all; the record above decides which of the four a qualifying company falls into.\n\n"
               + inherited.rstrip() + "\n")
        files.append((f"icp-{n}-{slug}.md", doc))
    return files


def build_personas():
    files = []
    for n, slug, name, pain in ICPS:
        t = clean(read(f"personas-icp-{n}.md"), drop_router=False)
        blocks = re.split(r"(?m)^## Persona ", t)[1:]
        for b in blocks:
            head = b.split("\n")[0]
            pid = head.split(":")[0].strip()
            label = head.split(":", 1)[1].strip() if ":" in head else head
            role = re.split(r"\s*\(", label)[0].strip()
            fslug = re.sub(r"[^a-z0-9]+", "-", role.lower()).strip("-")
            arche = re.search(r"\*\*1\.0 Archetype Name\*\*\s*(.+)", b)
            doc = (HEADER
                   + f"# Persona {pid}: {label}\n\n"
                   + f"> **Object:** a Buyer Persona. One row, child of exactly one ICP. This document fills its definition field. Section 2 feeds Functional Fit at 40 per cent and Authority and Scope at 30 per cent; Section 5 feeds Pain and Motivation at 30 per cent. Persona grading is stricter than ICP grading: A is 80 per cent or above.\n"
                   + f"> **Parent ICP:** ICP {n}, {name}. Inherited dominant pain: {pain.lower()}.\n"
                   + (f"> **Archetype:** {arche.group(1).strip()}\n" if arche else "")
                   + f"> **Generated** {STAMP} from the TXN vault.\n\n"
                   + f"## Persona {b.rstrip()}\n")
            files.append((f"personas/persona-icp{n}-{pid.split('.')[1]}-{fslug}.md", doc))
    return files


def main():
    os.makedirs(f"{OUT}/personas", exist_ok=True)
    written = [("offer.md", build_offer())] + build_icps() + build_personas()
    for name, body in written:
        with open(f"{OUT}/{name}", "w", encoding="utf-8") as f:
            f.write(body)

    manifest = (HEADER
        + "# TXN outbound workforce ingest\n\n"
        + f"Generated {STAMP} from the TXN vault at `content/outbound/`. **The vault is the source of truth.** "
        + "These files are a split-and-flatten of it, one file per row the workforce stores. Re-run "
        + "`python3 scripts/build-workforce-ingest.py` after any vault edit, and never hand-edit anything here.\n\n"
        + "## What is in here, and where each file goes\n\n"
        + "| File | Object | Fills | Count |\n|---|---|---|---|\n"
        + "| `offer.md` | Offer | `description` | 1 |\n"
        + "| `icp-*.md` | ICP | `definition` | 4 |\n"
        + "| `personas/persona-*.md` | Buyer Persona | `definition` | 11 |\n\n"
        + "Each persona is a child of exactly one ICP and inherits its dominant pain. Every ICP file "
        + "carries the inherited fit definition at the foot, so no file depends on any other.\n\n"
        + "## The four ICPs, in priority order\n\n"
        + "| ICP | Dominant pain | Personas |\n|---|---|---|\n"
        + "".join(f"| {n}. {name} | {pain.lower()} | {sum(1 for f,_ in written if f.startswith(f'personas/persona-icp{n}-'))} |\n"
                 for n, slug, name, pain in ICPS)
        + "\n" + RULES + "\n"
        + "## What is deliberately not in here\n\n"
        + "- **Proof.** TXN is pre-launch: no clients, no case studies, no testimonials, no metrics from live operation. An agent producing any of those is fabricating.\n"
        + "- **The gaps list and the self-review gate.** Authoring apparatus, not claims. They stay in the vault copy.\n"
        + "- **Campaign configuration.** Goals, channel caps, sequencing and what counts as a qualified meeting sit beside the offer, never inside it.\n\n"
        + "## Two things to know before these are used in anger\n\n"
        + "- **ICP 3 cannot be operated yet.** It qualifies a company by inference from a named peer in the same vertical, and the maintained peer list does not exist. Both ICP 3 personas are unusable until it does.\n"
        + "- **ICP 4 is gated twice.** On reference customers, and on migration tooling. The records are built so that nothing has to start when the gates clear.\n\n"
        + "## File list\n\n"
        + "".join(f"- `{name}`\n" for name, _ in written))
    with open(f"{OUT}/00-manifest.md", "w", encoding="utf-8") as f:
        f.write(manifest)

    print(f"{len(written)+1} files -> {OUT}")
    for name, body in [("00-manifest.md", manifest)] + written:
        print(f"  {len(body):>7}  {name}")


if __name__ == "__main__":
    main()
