---
description: "Register of TXN's build partners, third-party integrations and reference artifacts, with open infra questions and the shifting delivery timeline"
---

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
| DT Core API | Card issuing + transaction processing; the tool surface agents act on | In build (DT) | Wrapped by [[agent-access-layer]]. OpenAPI specs: [[txn-api-reference]] (`txn-api-spec-external.yaml` + `txn-api-spec-internal.yaml`, July split; latest going forward) |
| Data Lake (DT) | Analytics/insight source for AI recommendations + alerts | Planned (DT) | Access pattern for AI **open** — see below |

## Reference artifacts

Partner-supplied specs and definitions held in the vault for context (these are out-of-scope builds; see [[components#Out of scope for Novosapien]]).

| Artifact | From | What it is | Link |
|----------|------|-----------|------|
| TXN Global API (OpenAPI v1) | Direct Transact | The "DT YAML" the portal API reference renders from; grounds the MCP/sandbox and the pilot mock API. **Now split** (July specs, latest): **external** (30 paths, 99 ops, ~325 schemas) + **internal** (7 paths, 23 ops, ~71 schemas); paths pluralised. Supersedes the May single spec | [[txn-api-reference]] |
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

**Update (03-08, [[2026-08-03-first-standup-pilot-demo]]):**

- **The pilot mock API is still built on the old May YAML.** George: *"it's currently on the old YAML file, but very easy to port it over."* The July external/internal split ([[txn-api-reference]]) is the spec of record, so the **port is outstanding** — see [[open-questions]] #32.
- **Three services now stand up the pilot**, all Novosapien-side: the **Control Center replica** (real look and behaviour, hardcoded mock data, not connected to live APIs), a **dedicated mock API service** with a data store behind it and randomised payloads, and the **MCP server** as a **separate service on top of** that API rather than inside it — because DT owns the Core API, the usual embedded pattern is unavailable ([[mcp-server]]).
- **Deployment for TXN review:** the build is being deployed with **basic authentication** so Michael and Dorte can use it in their own sessions and try to break it, alongside the screenshot **feedback tool**. Estimated a day or two from the 3 August standup.
- **Delivery shape confirmed:** everything bedded down by **end of August**, then the **final two weeks are formal UAT** — environments stitched up, deployments and CI/CD proper. Brett flagged **review turnaround as the binding constraint**, since each round of use surfaces more change.


**Update (13-08, [[2026-08-13-agentic-standup]]):**

- **Sentry error tracking to be added** on the Novosapien side, with errors **linked to the feedback records** so a UI drawing, an in-chat agent-feedback note and the underlying stack error resolve to one view rather than three. George: *"then we're getting a holistic overview of not just the feedback... but also any errors as well."*
- **Final wireframes exist and supersede the prototype.** Michael has them and will share; they are wireframes rather than a clickable prototype. Design alignment still to settle: **where the agent lives**, the **AI button in the header**, and how both translate into the **knowledge hub**. Michael is bundling this into his feedback. A UI rebuild against final designs is **two to three days** of work, because the functionality behind the agent is portable and only the surface changes ([[open-questions]] #35).
- **Stackworkz sync call targeted for Friday next week.** Dorte is arranging it; TXN's own weekly Stackworkz call is Wednesdays, and Stackworkz have a **new project manager** (the previous one is on maternity leave). The plan is to give Stackworkz **access to the console build** so they can click through the agent and check design alignment, fonts and payload rendering, ahead of any hand-over or collection points between the two teams.


**Update (18-08, [[2026-08-18-agentic-standup]]):**

- **Stackworkz have no deployment scheduled.** Dorte hopes for one within the next couple of weeks, at which point the two builds can be aligned properly. Items also remain outstanding from DT.
- **The Stackworkz call is confirmed for Friday**, with their new project manager in place. Agenda from the Novosapien side: confirm whether the prototype Novosapien rebuilt from is the one Stackworkz are working to, and agree how work moves between the two teams in either direction.
- **DT is the binding constraint on the wider timeline.** Dorte, asked whether finishing the pilot early would help: it would help "tremendously", but DT has to finish first and "everyone else is finishing before they finish".


**Update (20-08, [[2026-08-20-agentic-standup]]):**

- **Stackworkz have the console foundation in place**: login, menus, screens and access. Michael's read is that this makes it a good moment for the two teams to talk, and that pulling their work in *"shouldn't be too much difficult"*.
- **Direct Transact's JWT process is settled and they are building the SDK**, so authentication for the agent's requests will be available. Michael suggests a conversation with DT specifically about authentication: how the agent obtains access to the various endpoints and works out which to call. Much of that context comes from the console, which already knows which programmes a given user can reach.
- **A PIN-layer change has landed on the platform**: PINs previously sat behind a separate authentication endpoint, and that layer has been scrapped in favour of central JWT. It does not change the shape of the card-service workflow, but it removes the authenticate step from it.
