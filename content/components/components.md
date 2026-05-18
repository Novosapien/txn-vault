# TXN — Components

> **Vision:** [[vision]]

## Overview

This is the component map for **Novosapien's deliverables within the TXN product** — the agentic AI layer that gets embedded into TXN's three product surfaces (Core API, Console, Developer Portal). The platform itself is built by other partners (see [[vision#Scope boundary]]) and is not represented here as a Novosapien component.

Components below were first surfaced in the [[13-05-2026-txn-vision-meeting|vision meeting]]. Each will be formalised through a dedicated component deep-dive session.

**Status legend:**
- **Collecting** — surfaced in vision; details still being gathered
- **Defined** — component document exists with scope, sub-components, and acceptance criteria
- **Ready for build** — defined, prioritised, and queued for implementation
- **In build** / **Complete** — implementation states

## Components

| Component | What it does | Status | Link |
|-----------|-------------|--------|------|
| In-app Co-pilot | AI assistant rendered inside Console + Portal — recommends actions, explains impact, executes on confirmation | Collecting | [[in-app-co-pilot]] |
| Agent Inbox / Alerts | Proactive notification surface where the AI pre-investigates issues and proposes executable plans for approval | Collecting | [[agent-inbox]] |
| Scoped Support Chatbot | Documentation-scoped chatbot in the Developer Portal with defensive fallback routing to internal queues | Collecting | [[scoped-support-chatbot]] |
| MCP Server | Direct agent access to TXN capabilities via Model Context Protocol — for Claude and other LLMs | Collecting | [[mcp-server]] |
| A2A Endpoint | Agent-to-agent communication endpoint for clients running their own agents against TXN | Collecting | [[a2a-endpoint]] |
| Internal Ops Agents | TXN's own agentic operations — release notes, support triage, doc self-healing, simulation testing | Collecting | [[internal-ops-agents]] |

## Out of scope for Novosapien

These are part of the TXN product but built by other partners. They appear here as **context** — Novosapien's components integrate with them but do not deliver them.

| Component | Built by | Reference material |
|-----------|---------|--------------------|
| Core API | TXN dev team | Core API documentation (from TXN) |
| TXN Console (frontend + backend) | TXN console build team (frontend designed by third-party) | Console design prototype documentation |
| Developer Portal (site + Umbraco CMS) | Third-party portal team | Developer portal site documentation |
| Data Lake | DT (TXN's internal dev partner) | _(schema input from Novosapien for AI consumption)_ |
