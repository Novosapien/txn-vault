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
| Umbraco (headless) CMS | Source of Developer Portal docs/content; exposes APIs | Available | Stackworkz can expose docs via API for AI search — feeds [[developer-support]]. Content model defined by SuperUltra — see [[umbraco-guide-content-model]] + [[umbraco-changelog-content-model]] |
| DT Core API | Card issuing + transaction processing; the tool surface agents act on | In build (DT) | Wrapped by [[agent-access-layer]]. OpenAPI spec: [[txn-api-reference]] (`txn-api-spec.yaml`) |
| Data Lake (DT) | Analytics/insight source for AI recommendations + alerts | Planned (DT) | Access pattern for AI **open** — see below |

## Reference artifacts

Partner-supplied specs and definitions held in the vault for context (these are out-of-scope builds; see [[components#Out of scope for Novosapien]]).

| Artifact | From | What it is | Link |
|----------|------|-----------|------|
| TXN Global API (OpenAPI v1) | Direct Transact | The "DT YAML" the portal API reference renders from; grounds the MCP/sandbox. 51 endpoints, ~464 schemas | [[txn-api-reference]] |
| Umbraco Guide content model | SuperUltra | Content blocks for Developer Portal guide pages | [[umbraco-guide-content-model]] |
| Umbraco Changelog content model | SuperUltra | Content types for the Changelog + What's Coming sections | [[umbraco-changelog-content-model]] |
| Workstream 1 & 2 architecture (draft) | Michael | Proposed Azure multi-region deployment | [[workstream-1-2-architecture]] |

## Open questions

- **AI data access** — does AI consume data via a **data-lake plug-in** (DT exposes tables) or **pull-and-aggregate through the Core API**? DT is open to either; depends on their timeline and priorities. Affects [[agent-access-layer]] and the data & insight layer.
- **Dev environment — RESOLVED: TXN-controlled Azure.** The platform will run on a **TXN-controlled Azure environment**, drawn out in [[workstream-1-2-architecture]] (multi-region AKS, Front Door, API Management, Key Vault). This settles the earlier open question (build inside Stackworkz's existing environment vs. a TXN-controlled Azure environment). The previously recorded partner stack (DT on Kubernetes, Stackworkz VM-based dev env) describes the build partners' own environments; the target deployment platform is TXN's Azure.
- **Card-API MCP ownership — RESOLVED (18-06):** docs/dev-portal MCP = Stackworkz; card-acquiring-API MCP = DT; DT owns and manages all of it post-handover ([[open-questions]] #8).
- **DT multi-tenancy (18-06, open)** — DT built **one central system** for every client; TXN leans **per-client** isolation (the API gateway is a single containerised instance, but databases are per-client). The driver is commercial (clients expect their data fully separate) and risk (per-client limits one client's load affecting others). Being ironed out with DT ([[open-questions]] #48). **24-06:** now a live disagreement — Ian (TXN CEO) wants **ring-fenced per-client stacks**; DT proposes **central API management + an orchestration layer**; to be resolved with the CTO (the *Confirm Architecture* action).
- **TXN ↔ DT infrastructure separation (18-06, open)** — DT's current build sits **inside the DT domain** (their emails / VPNs) and uses 3+ core services shared with DT's own clients; end goal is **full separation** on TXN-controlled Azure in Europe (see [[workstream-1-2-architecture]]). DT can grant access to TXN, not the reverse; the environment must be stood up before access is granted ([[open-questions]] #49). **24-06:** Novosapien's AI layer is **containerised** (Azure **or** GCP; Terraform + Azure DevOps CI/CD), so infra location is less critical for portability; the **AI-specific components inside Azure still need specifying** (the *Define AI Requirements* action).

## Timeline (from 18-06)

- **Developer portal:** end-July (APIs as soon as possible; DT delivery is Visa-certification-first, so webhooks/spend-controls come later).
- **Console (config portion):** October; remaining surfaces (e.g. customer service) follow.
- **Market launch:** early October.
- **Super Ultra → Stackworkz console handover:** 9 July (Figma component frameworks; portal handover already done).

**Update (24-06, [[24-06-2026-final-vault-review]]):**

- **Go-to-market: September.** **First client onboarded: December.** **DT completes its work: October** — Ian flagged the October DT date complicates end-to-end testing (full UX eval needs the Console + AI finished first).
- Developer-portal core **end-July**, then **August** iteration via standups → **September** launch (refines the "early October" line above).
- **Marketing messaging is gated** on finalising the "AI story" scope and the September-GTM vs December-operational deliverables.

**Update (28-07, [[2026-07-28-agentic-pilot-kickoff]]):**

- **The Console is renamed the "Control Center."**
- **Stackworkz** have handed over the **knowledge hub** (DT code review in progress, some items outstanding) and are now scoping the Control Center: same frame-first approach, waiting on DT APIs before wiring connections.
- The **Super Ultra prototype is final**: the two-week extension ended and nothing newer is coming; Novosapien's pilot replica is built from it (Michael to confirm it matches the final version).
- **"Sunpox" access is outstanding** _(name as transcribed; possibly a transcription error)_, blocking knowledge-hub sign-in, so testing is look-and-feel only for now. Target: knowledge hub done for the **September launch**; the Control Center has more breathing room.
