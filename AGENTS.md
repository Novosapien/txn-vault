# txn Vault

This is the product knowledge vault for **TXN**. It is an Obsidian vault that doubles as a Quartz docs site and a Codex knowledge base.

## Git Workflow

- **Never commit directly to main.** Always create a branch named after the user (e.g., `george`) and open a pull request.
- Push the branch to origin and open a PR for review.
- All merges to main happen through pull requests only.

## Content Structure

All product content lives in `content/`. The structure follows the directory-brain pattern — every directory has a named entry-point file that serves as both router and summary.

```
content/
├── index.md              ← Project landing page
├── vision.md             ← Product vision
├── components/           ← Component map + per-component directories
├── architecture/         ← Cross-cutting technical decisions
├── meetings/             ← Meeting transcripts with frontmatter
└── drafts/               ← Work-in-progress
```

## Available Skills

| Skill | Purpose |
|-------|---------|
| `/product-manager` | Thinking partner, meeting classification, routing |
| `/product-vision` | Extract vision from transcript |
| `/product-component` | Extract components from transcript |
| `/product-sub-component` | Extract sub-components and entity journeys |

## Key Conventions

- **Wikilinks:** Shortest-path Obsidian wikilinks (`[[vision]]` not `[[../vision]]`)
- **Backfilling:** When creating a child document, immediately update the parent's routing table
- **Meetings:** Agent classifies transcripts and writes frontmatter + post-call analysis
- **Naming:** Lowercase, hyphen-separated. Files named after the thing they describe.
- **Navigation:** Agents enter at `content/index.md` and follow wikilinks. If an agent needs `find` or `ls` to locate a document, the knowledge graph has a broken link.

## Description frontmatter

Every markdown document in this vault carries a one-line `description:` in its
YAML frontmatter.

- When you create a markdown file, write its description in the same edit.
- When you edit a markdown file, re-read its description. If the description no
  longer matches what the page now says, rewrite it in the same edit.
- Format: one line, at most 160 characters, double-quoted, a sentence that says
  what the document IS. Never a quote from the page, a table fragment, or
  dialogue. Over 160 characters is INVALID, not merely truncated downstream.
- If you cannot summarise the page faithfully from its content, leave
  `description:` absent and say so — a confident wrong line is worse than none.
- Exempt (no description): files named `changelog.md` or `*changelog*.md`, files
  named `TEMPLATE.md` or `*template*.md`, and empty files.
