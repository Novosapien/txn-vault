# TXN — Integrations

> **Architecture:** [[architecture]]

Third-party services, APIs, and data feeds that the product depends on, plus the build-partner environments Novosapien's AI layer plugs into.

## Build partners, environments & stack

_Surfaced in the [[29-05-2026-stackworkz-meeting]] (ways-of-working call between Novosapien, Stackworkz, and TXN)._

| Partner | Builds | Stack | Infra |
|---------|--------|-------|-------|
| **Stackworkz** | TXN Console (frontend + back-end-for-frontend) and Developer Portal | C#/.NET BFF · React + Material UI front end · **Umbraco headless** CMS (exposes APIs) | DevOps · **VM-based** dev environment |
| **Direct Transact (DT)** | Core API / card-system backend + Data Lake | _(not detailed)_ | **Kubernetes** |
| **Super Ultra** | Design (Console + Developer Portal) | — | — |

**Coupling:** Stackworkz's BFF talks to DT's Core API **over API only** — the same API TXN's clients use directly. **Permissions and user management live in the Stackworkz BFF, not the Core API** — this is the source of truth the [[agent-access-layer]] permission model must mirror.

## Integrations

| Service | Purpose | Status | Notes |
|---------|---------|--------|-------|
| Umbraco (headless) CMS | Source of Developer Portal docs/content; exposes APIs | Available | Stackworkz can expose docs via API for AI search — feeds [[developer-support]] |
| DT Core API | Card issuing + transaction processing; the tool surface agents act on | In build (DT) | Wrapped by [[agent-access-layer]] |
| Data Lake (DT) | Analytics/insight source for AI recommendations + alerts | Planned (DT) | Access pattern for AI **open** — see below |

## Open questions

- **AI data access** — does AI consume data via a **data-lake plug-in** (DT exposes tables) or **pull-and-aggregate through the Core API**? DT is open to either; depends on their timeline and priorities. Affects [[agent-access-layer]] and the data & insight layer.
- **Dev environment** — build inside Stackworkz's existing (cost-controlled) environment for a consolidated setup, vs. a TXN-controlled Azure environment. Cost attribution unresolved; **Mike (TXN CTO) to resolve with Ian (TXN CEO)**.
- **Card-API MCP ownership** — see the MCP-ownership split in [[agent-access-layer]].
