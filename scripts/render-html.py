#!/usr/bin/env python3
"""Render TXN outbound vault documents to self-contained, TXN-styled HTML.

    python3 scripts/render-html.py offer
    python3 scripts/render-html.py personas

The markdown in content/outbound/ stays the source of truth. These are generated
views of it: edit the markdown, then regenerate. Never edit the HTML by hand.
Brand CSS is lifted from the newest onboarding tracker so every document in the
set reads as one series.
"""
import re, sys, glob, datetime, html as H

VAULT = "/home/brett/Programming/txn/txn-vault/content/outbound"
OUTDIR = "/home/brett/shared/clients/txn/outbound"

DOCS = {
    "offer": {
        "slug": "txn-offer",
        "sources": [f"{VAULT}/offer.md"],
        "eyebrow": "TXN &middot; Cold Outreach Workforce &middot; Offer",
        "title": "The offer",
        "sub": ("The factual-claims universe the outbound workforce grounds every message in. Everything in here is "
                "permitted truth that the agents may state and the critic will pass. No prospect ever reads it. It is "
                "not marketing copy. Judge it only on whether every line is true and defensible."),
        "meta": [("Structure", "Offer Structure v2"), ("Blocking gaps", "0")],
    },
    "personas": {
        "slug": "txn-buyer-personas",
        "sources": [f"{VAULT}/buyer-personas.md", f"{VAULT}/personas-icp-1.md",
                    f"{VAULT}/personas-icp-2.md", f"{VAULT}/personas-icp-3.md",
                    f"{VAULT}/personas-icp-4.md"],
        "eyebrow": "TXN &middot; Cold Outreach Workforce &middot; Buyer Personas",
        "title": "The buyer personas",
        "sub": ("Eleven individual buyers across the four ICPs, each a child of exactly one ICP and inheriting its "
                "dominant pain, written in their own first-person voice. They feed the workforce's persona grading, "
                "which is stricter than ICP grading. No prospect ever reads them."),
        "meta": [("Personas", "11 across 4 ICPs"), ("Sections each", "12")],
    },
}

EXTRA = """<style>
.toc{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px 24px;margin:0 0 34px}
.toc h3{margin:0 0 12px;font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.toc ol{margin:0;padding-left:20px;columns:2;column-gap:34px}
.toc li{margin-bottom:6px;break-inside:avoid}
.toc a{color:var(--text-high);text-decoration:none;border-bottom:1px solid var(--border)}
.toc a:hover{color:var(--accent);border-bottom-color:var(--accent)}
.banner{background:#eef1fe;border:1px solid #c3caf9;border-radius:12px;padding:18px 22px;margin:0 0 30px}
.banner p{margin:0 0 9px;color:#26307a}.banner p:last-child{margin:0}
code{font-family:var(--mono);font-size:.88em;background:#f3f4f6;border:1px solid var(--border-subtle);
border-radius:4px;padding:1px 5px;color:var(--text-high)}
.wl{font-family:var(--mono);font-size:.86em;color:var(--accent);background:#eef1fe;
border:1px solid #dfe3fb;border-radius:4px;padding:1px 5px}
h1.part{font-size:27px;font-weight:800;letter-spacing:-.02em;color:var(--text-primary);
margin:52px 0 18px;padding:22px 0 0;border-top:3px solid var(--accent);scroll-margin-top:20px}
h2{scroll-margin-top:20px}
table{width:100%;border-collapse:collapse;font-size:14px;margin:0 0 18px}
th,td{text-align:left;padding:9px 11px;border-bottom:1px solid var(--border);vertical-align:top}
th{font-family:var(--mono);font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--text-muted);font-weight:500}
hr{border:none;border-top:1px solid var(--border);margin:36px 0}
@media print{
 body{background:#fff}.toc{page-break-after:always}
 h1.part{page-break-before:always}h2{page-break-after:avoid}table{page-break-inside:avoid}
}
@media (max-width:720px){.toc ol{columns:1}}
</style>"""


def inline(s):
    s, codes = H.escape(s), []
    s = re.sub(r"`([^`]+)`", lambda m: (codes.append(m.group(1)), f"\x00{len(codes)-1}\x00")[1], s)
    s = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r'<span class="wl">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"~~(.+?)~~", r"<s>\1</s>", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{codes[int(m.group(1))]}</code>", s)


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>|[*`\[\]]", "", t).lower()).strip("-")


def convert(md, multi):
    """Return (banner_html, body_html, toc entries). In multi mode the file's h1 becomes a part heading."""
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)
    lines, banner, body, toc = md.split("\n"), [], [], []
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        m = re.match(r"^# (.+)$", ln)
        if m:
            if multi:
                sid = slug(m.group(1))
                toc.append((sid, m.group(1), True))
                body.append(f'<h1 class="part" id="{sid}">{inline(m.group(1))}</h1>')
            i += 1
            continue
        if ln.startswith(">"):
            blk = []
            while i < n and lines[i].startswith(">"):
                txt = re.sub(r"^>\s?", "", lines[i])
                txt = re.sub(r"^\[!\w+\]\s*", "", txt)
                if txt.strip():
                    blk.append(inline(txt))
                i += 1
            if blk:
                html_blk = "<p>" + "</p><p>".join(blk) + "</p>"
                (body if (multi and body) else banner).append(
                    f'<div class="banner">{html_blk}</div>' if (multi and body) else html_blk)
            continue
        if re.match(r"^---+$", ln.strip()):
            body.append("<hr>")
            i += 1
            continue
        m = re.match(r"^(#{2,4}) (.+)$", ln)
        if m:
            lvl, txt = len(m.group(1)), m.group(2)
            if lvl == 2:
                sid = slug(txt)
                toc.append((sid, txt, False))
                body.append(f'<h2 id="{sid}">{inline(txt)}</h2>')
            else:
                body.append(f"<h{lvl}>{inline(txt)}</h{lvl}>")
            i += 1
            continue
        if ln.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, data = (rows[0], rows[2:]) if len(rows) >= 2 and all(
                re.fullmatch(r":?-{2,}:?", c) for c in rows[1]) else (None, rows)
            t = "<table>"
            if head:
                t += "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>"
            t += "<tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r)
                                     + "</tr>" for r in data) + "</tbody></table>"
            body.append(t)
            continue
        if re.match(r"^\s*[-*] ", ln):
            items, base = [], len(ln) - len(ln.lstrip())
            while i < n and re.match(r"^\s*[-*] ", lines[i]):
                ind = len(lines[i]) - len(lines[i].lstrip())
                items.append((ind, inline(re.sub(r"^\s*[-*] ", "", lines[i]))))
                i += 1
            out, depth = [], 0
            for ind, txt in items:
                d = 1 if ind > base else 0
                while depth < d:
                    out.append("<ul>")
                    depth += 1
                while depth > d:
                    out.append("</ul>")
                    depth -= 1
                out.append(f"<li>{txt}</li>")
            out += ["</ul>"] * depth
            body.append("<ul>" + "".join(out) + "</ul>")
            continue
        para = []
        while i < n and lines[i].strip() and not lines[i].startswith(("|", "#", ">")) \
                and not re.match(r"^\s*[-*] ", lines[i]) and not re.match(r"^---+$", lines[i].strip()):
            para.append(inline(lines[i]))
            i += 1
        body.append("<p>" + "<br>".join(para) + "</p>")
    return banner, body, toc


def main(key):
    cfg = DOCS[key]
    css = re.search(r"<style[^>]*>.*?</style>",
                    open(sorted(glob.glob(f"{OUTDIR}/txn-outbound-onboarding-progress-*.html"))[-1],
                         encoding="utf-8").read(), re.S).group(0)
    now = datetime.datetime.now(datetime.timezone.utc)
    stamp_file, stamp = now.strftime("%Y-%m-%d-%H%M"), now.strftime("%-d %B %Y, %H:%M UTC")
    multi = len(cfg["sources"]) > 1

    banner, body, toc = [], [], []
    for src in cfg["sources"]:
        b, d, t = convert(open(src, encoding="utf-8").read(), multi)
        if not banner:
            banner = b
        else:
            body.extend(f'<div class="banner">{x}</div>' for x in b)
        body.extend(d)
        toc.extend(t)

    toc_html = ('<div class="toc"><h3>Contents</h3><ol>' + "".join(
        f'<li><a href="#{s}">{"<strong>" if top else ""}{H.escape(t)}{"</strong>" if top else ""}</a></li>'
        for s, t, top in [(s, t, x[2] if len(x) > 2 else False) for x in toc for s, t in [(x[0], x[1])]])
        + "</ol></div>")

    meta = "".join(f"<span>{k} <b>{v}</b></span>" for k, v in
                   [("Generated", stamp)] + cfg["meta"] + [("Prepared by", "Novosapien")])

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TXN: {cfg['title']}, {stamp}</title>
{css}{EXTRA}</head><body>
<header class="doc"><div class="wrap">
<div class="eyebrow">{cfg['eyebrow']}</div>
<h1>{cfg['title']}</h1>
<p class="sub">{cfg['sub']}</p>
<div class="meta">{meta}</div>
</div></header>
<div class="wrap">
<div class="banner">{''.join(banner)}</div>
{toc_html}
{''.join(body)}
<p class="foot" style="margin-top:40px;font-size:12.5px;color:#6b7280">
Generated {stamp} from {', '.join('<code>' + s.split('/outbound/')[1] + '</code>' for s in cfg['sources'])}
in the TXN vault, which is the source of truth. This page is a rendering of those documents, not a second copy:
edit the markdown, then regenerate.
</p>
</div></body></html>"""

    assert "—" not in doc and "§" not in doc and "&sect;" not in doc
    out = f"{OUTDIR}/{cfg['slug']}-{stamp_file}.html"
    open(out, "w", encoding="utf-8").write(doc)
    print("written", out, len(doc), "|", len(toc), "toc entries |", len(body), "blocks")


if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else ""
    if key not in DOCS:
        sys.exit(f"usage: render-html.py [{' | '.join(DOCS)}]")
    main(key)
