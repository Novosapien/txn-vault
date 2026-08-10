---
title: "Umbraco Guide Content Model"
type: vendor-spec
source: "SuperUltra design team (micaela@superultra.co)"
received-from: Michael
date: 2026-05
status: reference
maps-to:
  - "[[developer-support]]"
  - "[[docs-mcp-server]]"
  - "[[portal-co-pilot]]"
  - "[[architecture]]"
description: "SuperUltra's May 2026 vendor proposal for the Umbraco content blocks on TXN Developer Portal guide pages — 13 block specs with field tables and open questions"
---

# Umbraco Guide Content Model

> **Reference material (placed):** Vendor proposal from the SuperUltra design team, received from Michael. Converted from `TXN-Umbraco-Guide-Content-Model.docx`. This is a *starting point for conversation, not a fixed specification.* It defines the Umbraco content blocks for guide pages on the TXN Developer Portal, the docs source that grounds [[developer-support]] (the "Umbraco headless CMS docs source"). Reference for the **out-of-scope** Developer Portal build (Stackworkz + SuperUltra), routed from [[developer-support]].

**Prepared by:** SuperUltra · **For:** TXN / Umbraco Development Team · **Date:** May 2026

A reference for the development team: the content blocks required in Umbraco to support flexible, consistent guide pages on the TXN Docs.

---

## Overview

This document is a proposal from the SuperUltra design team. It outlines the content blocks we believe Umbraco should support to enable flexible, consistent guide pages on the TXN Developer Portal.

The scope of this document is a **single guide page only**. The API Reference section is out of scope: that will be auto-generated from the OpenAPI spec (see [[txn-api-reference]]) and handled separately.

This document covers **structure and content fields only**. Visual design, spacing, colour, and typography will follow in a Figma component set once the structural build is agreed. The intention is that styling can be applied on top of the block structure without requiring changes to the underlying build.

### How to read this document

Blocks are divided into two categories:

- **Fixed blocks:** proposed as present on every guide page, not editable by content editors.
- **Optional blocks:** editors choose and combine these to build the body of a guide.

For each block you will find a short description of its purpose and a properties table showing each field, whether it is required, and any relevant notes.

### General principles

- Headings within a guide are handled through the **Rich Text Block** rather than as a separate block type. Editors select a heading style from the paragraph style options within that block.
- Blocks are focused on a single job. If an editor needs a heading above an image or a stepper, they add a Rich Text Block above it rather than building heading fields into every block.
- The CMS should be **usable by non-technical editors**: field labels and helper text in Umbraco written in plain language where possible.
- Where a block includes repeating items (steps, cards, tabs), editors can add, remove, and reorder items freely.
- **Guide-level metadata** (`last_updated`, `product_area`, `category`) sits at the document type level in Umbraco, not as content blocks. These fields control navigation placement and are separate from the block structure described here.

---

## Fixed Blocks

One block appears on every guide page and is not editable or removable by content editors. This gives every guide a consistent starting point.

### 01 · Guide Header

Sits at the top of every guide page. Provides the page title and a short description that orientates the reader before they begin.

| Field | Proposed | Notes |
|-------|----------|-------|
| `title` | Yes | The guide title. Displayed as the primary page heading. |
| `description` | Yes | A short summary of what the guide covers. Displayed directly below the title. |
| `last_updated` | Auto | Set by Umbraco on publish. Not filled in by editors. Displayed in the guide header as metadata so readers can assess how current the content is. |

This block appears once at the top of every guide and is not editable in terms of structure: only the title and description content would be filled in by editors.

The following fields sit at the **document type level** in Umbraco rather than within the block itself. They are filled in when the guide is created and control how the guide is classified and where it appears in navigation.

| Field | Required | Notes |
|-------|----------|-------|
| `product_area` | Yes | The product area this guide belongs to. Options to be confirmed: suggested starting set Payments, Cards, Webhooks, Authentication, API. Affects where the guide is surfaced in navigation. |
| `category` | Yes | The navigation grouping within the product area. Editors select an existing category or create a new one. Determines the section the guide sits under in the left nav. |

---

## Optional Content Blocks

The blocks editors can choose from to build the body of a guide. They can be added in any combination and any order between the Guide Header and the Related Reads section.

### 02 · Rich Text Block

The standard text block for body content, explanations, and inline formatting. Editors choose from a set of predefined paragraph styles to maintain typographic consistency across guides.

| Field | Notes |
|-------|-------|
| `paragraph style` | Preset styles only: Heading, Subheading, Body, Caption. No freeform font sizing. |
| `bold` | Can be applied to any selected text within the block. |
| `italic` | Can be applied to any selected text within the block. |
| `strikethrough` | Can be applied to any selected text within the block. |
| `hyperlink` | Editors select text and attach a URL. Supports internal and external links. |
| `bullet list` | Unordered list with basic nesting support. |
| `numbered list` | Ordered list with basic nesting support. |
| `inline code` | Marks a word or short phrase as code. Renders in monospaced font with a subtle background. Used for field names, endpoint paths, and short code references within body text. |

Paragraph styles are preset and fixed. Formatting options are constrained to what Markdown syntax supports (determined by Umbraco's rich text editor). Underline and text colour are not available. This keeps typographic consistency across all guides without requiring design review on every edit.

> **Open question (flagged by SuperUltra):** Headings entered via the Rich Text Block need to be reliably extractable for in-page navigation and table-of-contents generation. The development team should confirm this is technically feasible before the approach is finalised. If headings cannot be reliably extracted from rich text content, a dedicated Heading Block will be needed.

### 03 · Image Block

For screenshots, diagrams, architecture maps, and other visual assets. Images default to full content width and scale proportionally.

| Field | Required | Notes |
|-------|----------|-------|
| `image` | Yes | The image asset. Supported formats: PNG, JPG, SVG. Proposed: minimum resolution requirement and maximum file size cap to protect display quality. |
| `alt text` | Yes | A text description of the image for screen readers and accessibility. Not visible to sighted readers but required on every image. |
| `caption` | No | Optional label displayed below the image. Editors switch this on when needed. |

Images default to full content width and scale proportionally. No freeform sizing. The proposal to enforce a minimum resolution and file size cap is subject to developer confirmation.

### 04 · Table Block

For structured, comparative, or reference data. Common use cases include parameter references, field definitions, and comparison tables.

| Field | Required | Notes |
|-------|----------|-------|
| `header row` | No | Included by default. Editors can remove it if not needed. When present, the first row is treated as the table header. |
| `columns` | Yes | Number of columns. Set when the table is created. |
| `rows` | Yes | Editors can add as many rows as needed. |
| `cell content` | Yes | Each cell supports plain text, bold, inline links, and inline code. No nested blocks, no colour, no bullet lists within cells. |

Cell formatting is intentionally limited to keep tables readable and consistent. If content within a cell requires more than basic formatting, it is a signal the content should be restructured outside the table.

### 05 · Code Block

For code samples. The editor can choose between two modes: selecting an operation from the OpenAPI spec, or authoring code manually. Both modes render with syntax highlighting, a language picker, and a copy-to-clipboard button.

| Field | Required | Notes |
|-------|----------|-------|
| `mode` | Yes | The code entry mode. Options: OpenAPI (selects an operation from the spec, content renders automatically) or Manual (editor authors the code directly). |
| `operation` | Conditional | Required when mode is OpenAPI. The editor selects an operation from the API spec (e.g. `POST /v1/cards`). All block content renders automatically from this selection. |
| `language` | Conditional | Required when mode is Manual. The programming language for syntax highlighting. In Manual mode, each block is one language: editors add multiple blocks if they need the same example in more than one language. |
| `code` | Conditional | Required when mode is Manual. The code content authored directly by the editor. |

A language picker and copy-to-clipboard button are always included on the rendered block. These are not configurable by editors. In OpenAPI mode, code is generated across multiple languages automatically.

### 06 · Callout Block

Used to draw attention to important information that sits outside the main reading flow. The callout type drives both the icon and the visual treatment automatically: editors do not configure these separately.

| Field | Required | Notes |
|-------|----------|-------|
| `type` | Yes | Determines the icon and visual styling of the callout automatically. Options: Info, Note, Warning, Danger. |
| `title` | No | Optional. Many callouts are a single sentence where a title adds unnecessary visual noise. The callout type and icon already communicate the intent. Add a title when the callout message benefits from a clear header. |
| `description` | Yes | The callout body text. Supports inline formatting and links. |

Type and description are required on every callout. Title is optional.

### 07 · Stepper Block

Used for sequential, numbered instructions. The primary block for how-to guides and integration walkthroughs.

| Field | Default | Notes |
|-------|---------|-------|
| `steps` | Yes | Repeating. Editors add as many steps as needed and can reorder them freely. |
| `step number` | Auto | Assigned automatically in sequence. Updates if steps are reordered. |
| `step heading` | Yes | A short title for the step. |
| `step description` | Yes | The step instructions. Supports inline formatting and links from the Rich Text options. |
| `nested block` | No | Each step can optionally include an additional content block to support the instruction, for example a code block, image, or callout. |

Step numbers are assigned automatically so editors do not need to manage them manually.

### 08 · Button Block

Used for prominent calls to action within a guide, such as linking to the sandbox, a download, or a next step that warrants more visibility than an inline hyperlink.

| Field | Default | Notes |
|-------|---------|-------|
| `label` | Yes | The button text displayed to the reader. |
| `URL` | Yes | The destination. Supports internal and external links. |
| `type` | Yes | Primary or Secondary. Drives the visual styling. To be defined in Figma. |

### 09 · Link Card Block

A navigational block used to surface links to other pages or resources in a card format. The entire card is clickable. Editors can add one card or multiple cards in a single block.

| Field | Default | Notes |
|-------|---------|-------|
| `cards` | Yes | Repeating. Editors add one or more cards within the block. |
| `card title` | Yes | The title displayed on the card. |
| `card description` | Yes | A short line of supporting context for the link destination. |
| `card URL` | Yes | The destination URL. The entire card is clickable. |

The Link Card is a navigational element: its purpose is to take the reader somewhere. Worth distinguishing clearly from the Content Card block in the Umbraco interface so editors reach for the right one.

### 10 · Content Card Block

Used to present a piece of content or information in a structured card format. Unlike the Link Card, the Content Card is not inherently a navigation element: it can include an optional button if a call to action is needed. Editors can display cards in a grid layout or a list layout.

| Field | Default | Notes |
|-------|---------|-------|
| `image` | No | Optional image displayed within the card. |
| `title` | Yes | The card title. |
| `description` | Yes | Supporting body text for the card. |
| `button` | No | Optional call to action button within the card. Includes a label and a URL. |
| `layout` | Yes | Controls how cards are displayed when multiple are present. Options: Grid (side by side) or List (stacked rows). Editors add multiple content cards within a single block instance. |

The Content Card is for presenting information; the Link Card is for navigation. Both should be clearly named and described in the Umbraco interface to help editors make the right choice.

### 11 · Divider Block

A simple visual separator used to create a clear break between sections of a guide without introducing a new heading. Keeps the reading flow clean on longer pages.

| Field | Proposed | Notes |
|-------|----------|-------|
| `style` | No | Visual style. Options to be confirmed at styling phase. Defaults to a simple horizontal line. |

From a content perspective, dividers work best used sparingly. If content needs a break, consider whether a heading in the Rich Text Block would serve the reader better by also giving navigational context.

### 12 · Video Embed Block

Used to embed video content directly in a guide page. Suitable for tutorial videos, product walkthroughs, and demos that support or replace written instructions.

| Field | Proposed | Notes |
|-------|----------|-------|
| `URL` | Yes | The video URL. Supported platforms (e.g. YouTube, Loom). |
| `caption` | No | Optional label displayed below the video. |

### 14 · Related Reads

An optional closing section editors can add when there are relevant guides or resources worth linking to. Not every guide will need one. The section title is locked to "Related Reads" so that when it does appear, it looks consistent across all guides.

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Fixed | Always displays as "Related Reads" and is not editable by content editors. |
| `cards` | Yes | Repeating. Suggested minimum of one card and maximum of three. |
| `card title` | Yes | The title of the linked guide or resource. |
| `card description` | Yes | A short description of where the link leads. |
| `card URL` | Yes | The destination URL. The entire card is clickable. |

Maximum of three cards proposed to keep the section focused. Open to discussion if a different limit makes more sense technically.

---

## Block Summary

A quick reference of all content blocks covered in this document.

| # | Block | Purpose |
|---|-------|---------|
| 01 | Guide Header | Fixed. Required on every guide. Title and description. |
| 02 | Rich Text Block | Body text with paragraph styles, inline formatting, links, lists, and inline code. |
| 03 | Image Block | Visual assets with alt text and optional caption. |
| 04 | Table Block | Structured data with a default header row and basic cell formatting. |
| 05 | Code Block | Code samples with syntax highlighting, language selection, and copy button. |
| 06 | Callout Block | Info, Note, Warning, and Danger callouts with automatic icon and styling. |
| 07 | Stepper Block | Numbered sequential steps with automatic numbering. |
| 08 | Button Block | Primary or secondary call to action button with label and URL. |
| 09 | Link Card Block | Navigational cards linking to other pages or resources. |
| 10 | Content Card Block | Information cards with optional image and button. Grid or list layout. |
| 11 | Divider Block | Simple visual separator between sections. |
| 12 | Video Embed Block | Embedded video from YouTube or Loom with optional caption. |
| 13 | Related Reads | Optional closing section. Up to three links to related guides. Title is locked. |

---

## Next Steps (from SuperUltra)

SuperUltra want feedback on this proposal before anything is built. Specific things to discuss:

- Anything in this document that is not possible or would need to be approached differently. They are open to alternatives.
- **Open question:** Can headings entered via the Rich Text Block be reliably extracted for in-page navigation and table-of-contents generation? If not, a dedicated Heading Block will be needed instead.
- **Open question:** Code Block (OpenAPI mode) - TXN has multiple API specs (Payments, Cards, Webhooks). When an editor opens the operation picker, should they select which spec first, and then only see operations from that spec? Or will all operations from all specs appear in one list? Showing everything together would be unmanageable. SuperUltra suggest scoping by spec first, but Stackworx to confirm the approach before building the picker.
  - **TXN direction (2026-06, in debate, leaning many):** TXN currently leans toward a **many-spec basis** (separate specs) rather than the single combined `TxnGlobal` spec they shipped on 29 May. Not final, but it aligns with SuperUltra's "scope by spec first" picker. See [[developer-support#Reference Material]].

_Questions about this document: micaela@superultra.co_
