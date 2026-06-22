---
title: "Umbraco Changelog Content Model"
type: vendor-spec
source: "SuperUltra design team (micaela@superultra.co)"
received-from: Michael
date: 2026-05
status: reference
maps-to:
  - "[[developer-support]]"
  - "[[architecture]]"
---

# Umbraco Changelog Content Model

> **Reference material (placed):** Vendor proposal from the SuperUltra design team, received from Michael. Converted from `TXN-Umbraco-Changelog-Content-Model.docx`. This is a *starting point for conversation, not a fixed specification.* It defines the Umbraco content types for the Changelog and What's Coming sections of the TXN Developer Portal, the "change log from git/Linear in business-readable English" referenced in [[developer-support]]. Reference for the **out-of-scope** Developer Portal build (Stackworkz + SuperUltra), routed from [[developer-support]].

**Prepared by:** SuperUltra · **For:** TXN / Umbraco Development Team · **Date:** May 2026

A reference for the development team: the content types and fields required in Umbraco to support the Changelog and What's Coming sections of the TXN Developer Portal.

---

## Overview

This document is a proposal from the SuperUltra design team. It outlines the content types and fields we believe Umbraco should support for the Changelog and What's Coming sections of the TXN Developer Portal. As with the [[umbraco-guide-content-model|Content Block Framework]], this is a starting point for conversation, not a fixed specification.

The **Changelog** section gives developers a clear, structured record of what has changed in the TXN platform over time. The **What's Coming** section allows the TXN team to be transparent about direction without making date commitments.

This document covers content types and fields only. Visual design, layout, and component styling will follow in Figma once the content model is agreed.

### How to read this document

There are two content types covered in this document:

- **Change Entry:** a full record of a shipped change. Has more fields to capture the detail developers need.
- **Upcoming Change Entry:** a lightweight entry for signalling what is coming next. Intentionally minimal to avoid false promises.

For each content type you will find a short description of its purpose and a properties table showing each field, whether it is required, and any relevant notes.

### General principles

- The two content types are deliberately separate. A Change Entry and an Upcoming Change Entry are different things: keeping them as distinct types in Umbraco makes the editor experience cleaner and prevents fields irrelevant to one type from appearing in the other.
- Attached guides on Change Entries are built using the same content structure as standard guides (see [[umbraco-guide-content-model]]) but live as child nodes under the changelog entry in the Umbraco content tree. They are not part of the main docs navigation and are only surfaced through the entry they belong to.

---

## Content Types

### 01 · Change Entry

A full record of a change that has already shipped. This is the primary content type in the Changelog section. It carries everything a developer needs to understand what changed, when, and what action (if any) they need to take.

| Field | Required | Notes |
|-------|----------|-------|
| `date` | Yes | The date the change was released. Displayed on the changelog timeline. |
| `change_type` | Yes | The type of change. Options: New, Improved, Fixed, Breaking Change, Deprecated. |
| `product_area` | Yes | The product area the change affects. Options to be confirmed: suggested starting set Payments, Webhooks, Cards, Console, Authentication, API. Used for filtering on the changelog page. |
| `version` | No | The API or platform version this change applies to. Optional: not all changes will be tied to a specific version number. |
| `title` | Yes | The change title. Displayed as the primary heading on the entry. |
| `description` | Yes | Rich text body. Editors can use bold, bullet lists, inline links, and inline code. Same editor experience as guide pages. |
| `affected_endpoints` | No | The endpoints impacted by this change. A tags field: editors enter/select endpoint names such as `POST /v1/cards`. Applies to Breaking Change and Deprecated entries only. Not used on New, Improved, or Fixed entries. |
| `migration_notes` | No | Describes why it breaks existing integrations, and the steps required to migrate. |
| `attached_guide` | No | An optional guide document attached specifically to this entry. Built using the same content structure as standard guides but not part of the main docs navigation: only surfaced through this entry. Lives as a child node under the change entry in the Umbraco content tree. |
| `external_link` | No | An optional external link, for example "View in Console" or "Try in Sandbox". Only appears if URL is filled in. |
| `image` | No | An optional image to accompany the entry. Most useful for UI or console changes where a visual communicates the change faster than text alone. |

The `attached_guide` field gives editors the flexibility to go deep when a change warrants it, for example a deprecation with a migration path, or a major new feature that needs fuller explanation. There is no restriction on which change types can have an attached guide. The editorial team decides when one is needed.

### 02 · Upcoming Change Entry

A lightweight entry for signalling what is coming next. This content type powers the What's Coming section and is intentionally minimal. The goal is to give developers visibility into direction without the team making commitments they cannot keep.

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Yes | The upcoming change title. |
| `description` | Yes | Rich text body. Same formatting options as the Change Entry description: bold, bullet lists, inline links, inline code. |
| `product_area` | No | Optional product area tag. Useful for filtering but kept optional as the scope of upcoming changes may not always be fully defined at the time of publishing. |
| `prioritised` | No | A yes/no toggle. Controls display order: prioritised entries appear above others in the What's Coming section. This flag is not visible to developers on the portal; it only affects the order in which entries are presented. |

There is no date field on this content type. This is intentional. Publishing a date on a future change makes it a public commitment. If something slips, that becomes a visible broken promise. Keeping it title and description only means the team can be transparent about direction without being held to a timeline.

---

## Field Summary

A quick reference of all fields across both content types.

| Content Type | Field | Required | Notes |
|--------------|-------|----------|-------|
| Change Entry | `date` | Yes | Release date. Displayed on timeline. |
| Change Entry | `change_type` | Yes | New, Improved, Fixed, Breaking Change, Deprecated. |
| Change Entry | `product_area` | Yes | Used for filtering. Options to be confirmed. |
| Change Entry | `version` | No | API or platform version. Optional. |
| Change Entry | `title` | Yes | Primary heading of the entry. |
| Change Entry | `description` | Yes | Rich text. Bold, bullets, links, inline code. |
| Change Entry | `affected_endpoints` | No | Tags field. Breaking Change and Deprecated entries only. |
| Change Entry | `migration_notes` | No | Rich text. Breaking Change entries only. Replaces description as primary body. |
| Change Entry | `attached_guide` | No | Optional child guide. Not in main nav. |
| Change Entry | `external_link_label` | No | Label for optional external link. |
| Change Entry | `external_link_url` | No | URL for optional external link. |
| Change Entry | `image` | No | Optional image. Useful for UI changes. |
| Upcoming Change Entry | `title` | Yes | Primary heading of the entry. |
| Upcoming Change Entry | `description` | Yes | Rich text. Same options as Change Entry. |
| Upcoming Change Entry | `product_area` | No | Optional. May not always be known yet. |
| Upcoming Change Entry | `prioritised` | No | Yes/no toggle. Controls display order. Not visible to developers on the portal. |

---

## Next Steps (from SuperUltra)

As with the Content Block Framework, SuperUltra would like feedback before anything is built. Anything in this document that is not feasible as described: they are open to alternatives and happy to revisit any field or approach.

_Questions about this document: micaela@superultra.co_
