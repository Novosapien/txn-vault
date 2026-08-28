---
description: "Architecture hub — index of sections plus decisions log: CRM as system of record, TXN-controlled Azure platform, two doc stores, containerised AI layer"
---

# TXN — Architecture

> **Project:** [[index]]
> **User journeys:** [[ux-ai-cost-governance|AI Cost Governance]] (cross-cutting AI-infra concern) — see [[user-journeys]]

Cross-cutting technical decisions that affect the whole product. This directory covers tech stack choices, infrastructure, and third-party integrations.

## Sections

| Section | What it covers | Status | Link |
|---------|---------------|--------|------|
| Integrations | Third-party services, APIs, data feeds, build-partner environments | Collecting | [[integrations]] |
| Workstream 1 & 2 deployment | TXN-controlled Azure multi-region platform (Front Door, WAF, IAM, API Management, AKS, Key Vault, SQL) | Confirmed · diagram 1st draft | [[workstream-1-2-architecture]] |

## Decisions

_Cross-cutting calls made in client sessions._

- **CRM (Freshsales) is the system of record for client data** _(Ian, [[10-06-2026-developer-support-and-internal-ops]])._ Everything client-related lives in the CRM; the Console receives the data it needs *sent* to it, rather than context being split across systems or written directly to the Console. Flat documents are avoided — they limit how the data items can be reused. Shapes what [[internal-ops-agents]] (customer onboarding) writes to, and what [[agent-access-layer]] / the Console read.
- **TXN runs its own operations through the agentic experience + Teams, not bespoke Console admin UI** _(Ian, same session)._ TXN-as-user accesses AI-driven information through the Claude-like experience ([[full-agentic-experience]]) and receives alerts in Teams; do **not** build more AI-management software into the Console. Affects where internal alerts/reviews surface and keeps the Console from bloating.
- **Platform runs on a TXN-controlled Azure environment** _(confirmed 2026-06)._ The deployment target is TXN's own Azure (multi-region AKS, Front Door, API Management, Key Vault) as drawn in [[workstream-1-2-architecture]], not Stackworkz's existing dev environment. Resolves the dev-environment open question in [[integrations]].
- **Documentation is hosted in two stores** _(Mike, same session)._ The **DT YAML** is the source for the API reference (the same API the portal renders); **guides + change log live in Umbraco** (headless CMS, API-accessible). The AI reads both; Umbraco supports **edit-via-API in draft mode** for the [[internal-ops-agents]] knowledge engine.
- **The AI layer is containerised and cloud-portable** _(Brett/George, [[24-06-2026-final-vault-review]])._ Novosapien's AI architecture is fully containerised and managed via **Terraform + Azure DevOps CI/CD**, so the cloud (Azure **or** GCP) is not critical for portability; it targets TXN's Azure for production. Open: the **AI-specific components inside Azure are not yet specified** ([[open-questions]] #49).
- **AI-to-AI automated testing** _(aligned, same call)._ Headless AI runs user journeys thousands of times in parallel (**July→September**) to validate success criteria and optimise prompts, replacing manual onboarding-flow testing ([[open-questions]] #43).
- **The proposal document is the single source of truth** _(aligned, same call)._ The vault **proposal** — to be formalised into a **solution architecture document** — is the SSOT for solution architecture, plans, and development approach. _(Incoming artifact: flagged, not yet uploaded to the vault.)_
- **The AI layer deploys into Direct Transact's environment, and the central services are shared rather than per-client** _(Michael, [[2026-08-26-stackworkz-agent-demo]])._ Brett asked whether Novosapien would deploy into Stackworkz's Azure; Michael: *"will deploy into DT's. So yes, it's all the same."* The shape he described: **the APIs are instance-per-client**, while **knowledge hub, console and the AI sit as one central scalable layer**, and *"the client won't get their own layer."* This is a partial answer to the multi-tenancy question at [[open-questions]] #48 and #56: isolation exists at the API instance, not across the shared services the agent runs in.
- **Stackworkz builds TXN's user and permission framework, and the agent scopes against it** _(Michael, same session)._ A backend API with four role templates (TXN, bin sponsor, client self-issuing, client with a programme manager), TXN governing the ceiling, clients building roles beneath it, and user-level overrides on top. Closes [[open-questions]] #71. Leaves open whether the MCP surface needs its own model for system and agent-to-agent access (#73).
- **TXN will run as a subscription inside DT's Azure tenant** _(Michael, [[2026-08-25-agentic-standup]])._ Confirmed: *"we have confirmed that we will at least for now be going in the DT tenant as one of our own subscriptions"*, with access arranged so Novosapien's pipelines can run there. This is a **narrowing of the earlier "TXN-controlled Azure environment" decision** rather than a contradiction: still Azure, but inside DT's tenancy for now. It leaves an unresolved consequence, whether Azure hosting constrains which AI models and frameworks can be used ([[open-questions]] #70), with precedent that DT rejected several third-party frameworks for the console before agreement.
- **Client-stack isolation is unresolved** _(Ian, same call)._ Ian wants **individual ring-fenced client stacks** for security; DT proposes **central API management + an orchestration layer**. To be resolved with the CTO ([[open-questions]] #48); it changes the deployment shape downstream.

## Open Questions

Tracked centrally in the [[open-questions]] register. Architecture-level items currently **open**: the **client-stack-isolation / multi-tenancy** call (#48 — ring-fenced vs central), **TXN ↔ DT infrastructure separation + AI-component spec** (#49), the AI-ready downloadable doc file (#20), and the **AI data-access** pattern (data-lake plug-in vs Core-API pull — see [[integrations]]). _Recently resolved: site-wide LLM owner (#3), MCP-ownership split (#8), CRM ↔ Console split (#19), dev-environment = TXN Azure._


**Update (13-08, [[2026-08-13-agentic-standup]]):** **TXN runs its own vault alongside this one, deliberately.** Michael's holds everything TXN-wide: a **nightly sync from SharePoint**, meetings, decisions, and his **full release testing and UAT logs**. This vault holds the architectural, foundational and vision material. Michael describes them as working hand in hand and, usefully, says this one **finds contradictions and gaps in TXN's own documentation**. Access runs through the vault MCP connector, deployed company-wide at TXN. No consolidation is planned or needed; the split is the working arrangement.


**Update (20-08, [[2026-08-20-agentic-standup]]): the DT architecture question is now an IP question, at board level.** It has stopped being about cost or which tenant the platform sits in. Michael: *"it's not really a technical thing anymore... it's an IP discussion."* DT wants to **retain its IP and its access**; TXN needs DT to have **no access to the data**, because under GDPR *"we can't have people in South Africa looking at our data."* That constraint holds whichever tenant is chosen, so the tenancy decision no longer settles it. Being worked at board level rather than between the architecture teams, which makes the resolution date harder to predict. Tracked at [[open-questions]] #48 and #49.


**Update (25-08, [[2026-08-25-agentic-standup]]): three architecture items opened in one standup.**

- **Storage for the agent's own data has no home yet.** George asked where chats and alerts get stored, *"is it interacting with the database you've already got or having a specific smaller one just for the chats?"* Michael tied it to the data lake work in progress: pooling client data centrally *"brings in GDPR regulations"*, and if Novosapien stores client data inside agent responses it lands on the same side of the line as client data. **Novosapien will not have production database access**, so a connection mechanism has to be designed. Michael is writing the deployment document to DT and will add it as an open question to them ([[open-questions]] #69).
- **Model and framework choice may be constrained by the tenancy.** See the decision above and [[open-questions]] #70. **Action sits with Novosapien**: produce the list of models and frameworks we intend to use so Michael can put it to DT before it becomes a late constraint on the wire-in.
- **DT has no alerting system.** Recorded here because it is an architecture fact as much as a component one: there is no platform-side alerting to integrate with, and Michael wants the AI layer to become the central store that other systems feed into ([[open-questions]] #68, [[alert-detection]]).


**Update (26-08, [[2026-08-26-stackworkz-agent-demo]]): the approval-routing fork, raised by the partner.**

Ruan Sunkel of Stackworkz asked where the MCP server sits and what it talks to, and named the consequence: the Control Center *"is effectively just a proxy to the server. So we add authorization, extra user authorization which can include agent authorization as well."* Therefore *"if the MCP server talks directly to DT, then yeah, good luck with the approvals."*

**Michael confirmed the hard constraint: *"this approval part is console specific. DT aren't building any approval layer or anything like that."*** Routing the agent straight to DT bypasses the only approval layer that will exist in production.

The emerging shape is a split by traffic type: **system-to-system** (agent to agent) direct to DT endpoints, and **user-to-system** through the Console. The pilot's approval gating is in-chat against the mock, so nothing has tested it. Tracked at [[open-questions]] #74 and it gates the wire-in.

Also from that session: Michael raised whether an agent should carry **more** permission than the user driving it, *"a user can't do this without approval but an agent can"*, and whether agent actions enter Stackworkz's approval queue or bypass it. The **data lake structure went to DT on 25 August** with AI access considered, and Michael is pushing for a joint presentation to Novosapien and Stackworkz ([[open-questions]] #69).
