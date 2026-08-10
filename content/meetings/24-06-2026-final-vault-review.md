---
type: general
subtype: final-review / proposal-review
date: 2026-06-24
title: "Final Vault Review with Proposal Review"
participants:
  - Brett StClair (Novosapien)
  - George Westbrook (Novosapien)
  - Max Kingaby (Novosapien)
  - Hasan Mohammed Ahmed (Novosapien)
  - Ian Johnson (TXN)
  - Michael Moores (TXN)
  - Dorte Dye (TXN)
status: digested
digested: 2026-07-03
description: "Digest of the 2026-06-24 TXN final vault and proposal review (Meet AI summary) — proposal as source of truth, JWT auth settled, AI-to-AI testing, Sept GTM"
---

# Final Vault Review with Proposal Review (24 Jun 2026)

> **Post-call digest.** General final-review / proposal-review call (Google Meet AI summary, not a verbatim transcript). This digest records what resolved and where it landed; the source summary follows below.

## Decisions (aligned)

- **Proposal = single source of truth.** The vault **proposal document** is designated the single source of truth for the project's solution architecture, plans, and development approach. Brett to formalise it into a **solution architecture document** (incoming artifact — flagged, not yet in the vault). Logged in [[architecture]].
- **AI-to-AI automated testing.** AI-driven automated testing is the strategy for the **July→September** iterations (to harden robustness and optimise prompts), rather than relying on manual user feedback alone. See [[open-questions]] #43.

## Resolved / advanced (gap register)

- **Authentication — JWT confirmed (#9, #31).** Reuse **Console authentication** and append the **user ID to every tool call / data-access request**, so every agent action is authenticated and scoped to the user's Console permissions. Auth *mechanism* now settled; #31 stays open only on the sandbox-key build. See [[agent-access-layer]].
- **Testing methodology (#43).** **Headless AI-to-AI testing** in the admin-vault review space — the AI runs defined user journeys **thousands of times in parallel** to validate success criteria and surface prompt / tool-call / MCP-stability issues; replaces manual onboarding-flow testing. Runs July→September.
- **Model optimisation (#24).** Larger models (e.g. Opus 4.8) optimise the prompts/pipelines of smaller **production** models: big models for testing, small for prod — a cost lever.

## Sharpened but still open

- **#48 Multi-tenancy — now a live disagreement.** Ian (TXN CEO) wants **individual ring-fenced client stacks** for security; **DT** proposes **central API management + an orchestration layer**. To be resolved with the CTO (the *Confirm Architecture* action). Changes the deployment shape for everything downstream. See [[integrations]].
- **#49 Infra / AI components.** The AI architecture is **containerised** (Azure **or** GCP; managed via **Terraform + Azure DevOps CI/CD**), so infra location matters less. But the **AI-specific components inside Azure are not yet specified** (Ian's concern about operationalisation delays) → the *Define AI Requirements* action (Brett + George).

## Timeline (updated from 18-06)

- **Go-to-market: September.** **First client onboarded: December.** **DT completes its work: October** — Ian noted the October DT date complicates end-to-end testing (full UX eval needs the Console + AI finished first).
- Developer-portal core: **end-July**, then **August** iteration via standups → **September** launch. (Refines the 18-06 "market launch early October".)
- **Marketing messaging is gated** on finalising the "AI story" scope and the September-GTM vs December-operational deliverables (Ian) — priority so the team doesn't mislead prospects.

## Action items

- **[Dorte Dye, Michael Moores]** Review the proposal in the vault; confirm phase-2 / phase-3 feature prioritisation.
- **[Brett]** Publish the proposal + review tool into the vault.
- **[Ian Johnson, Michael Moores]** Confirm the target architecture (ring-fenced vs central — #48) and share the diagram.
- **[Brett, George]** Define AI requirements: specify the missing infrastructure components + authentication for the agentic channel (#49).
- **[Brett]** Hold a ~30-min session presenting the AI architecture + a live agent demo (to address DT's risk-averse stance on certification/security).

---

**

Jun 24, 2026

## Final vault review with proposal review

Invited [michael.moores@txn.global](mailto:michael.moores@txn.global) [Max Kingaby](mailto:max@rebel-labs.co) [dorte.dye@txn.global](mailto:dorte.dye@txn.global) [ianj@txn.global](mailto:ianj@txn.global) [Brett StClair](mailto:brett@rebel-labs.co) [George Westbrook](mailto:george@rebel-labs.co) [Hasan Mohammed Ahmed](mailto:hasan@rebel-labs.co)

Attachments [Final vault review with proposal review](https://calendar.google.com/calendar/event?eid=NGcxbTJ0bmJkaDk3a29rbnR0OXN2N2gwajMgYnJldHRAcmViZWwtbGFicy5jbw)

Meeting records [Recording](https://drive.google.com/file/d/1lgPOPo8nyXyJR1rYgyr2Q9cl1z0sMJCu/view?usp=drive_web) 

  
  

### Summary

Meeting addressed timeline constraints and architectural disagreements, resulting in a decision to utilize containerized deployment strategies.  
  
Timeline and delivery constraints  
Development cycles target September go-to-market dates while managing complex testing requirements for AI components. Delivering core developer portal features by late July enables iterative refinement.  
  
Architectural and testing methodology  
Containerized environments ensure portability across cloud providers, mitigating concerns regarding specific infrastructure requirements. Headless testing utilizes intelligent model optimization to validate user journeys while maintaining strict security via token authentication.  
  
Feature prioritization and documentation  
Establishing a unified solution architecture document will resolve discrepancies regarding stack isolation. Aligning on these deliverables remains critical for finalizing external messaging strategies for phase 2 and phase 3 development.

  
  

### Decisions

Aligned

- AI-driven automated testing strategy Automated AI-to-AI testing will be utilized for iterations between July and September to ensure robustness and optimize prompts, rather than relying solely on manual user feedback.
    
- Proposal document as single source of truth The vault proposal document is designated as the single source of truth for the project's solution architecture, plans, and development approach.
    

  

We've updated the Decisions section using your feedback.

Let us know what you think: [Helpful](https://google.qualtrics.com/jfe/form/SV_5p6FWBVWvynleNU?isGoogler=no&isHelpful=yes) or [Not Helpful](https://google.qualtrics.com/jfe/form/SV_5p6FWBVWvynleNU?isGoogler=no&isHelpful=no)

  
  

### Next steps

- ![unticked](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
    
    [Dorte Dye, Michael Moores] Review Proposal: Evaluate prioritized features for phase 2 and phase 3 within the vault.
    
- ![unticked](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
    
    [Brett StClair] Publish Proposal: Upload the project proposal and review tool into the vault by this afternoon.
    
- ![unticked](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
    
    [Ian Johnson, Michael Moores] Confirm Architecture: Finalize the target architecture and share the diagram with the team.
    
- ![unticked](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
    
    [Brett StClair, George Westbrook] Define AI Requirements: Specify missing infrastructure components and authentication processes for the agentic channel.
    

  
  

### Details

- Go-to-Market Timeline and Testing Constraints: Ian Johnson stated that the objective is to onboard the first client in December, with a go-to-market date of September. While DT indicated they will complete their work in October, Ian Johnson noted that this timeline complicates testing, as full user experience evaluation depends on the console and AI components being finished first.
    
- Developer Portal Delivery and Iteration: Brett StClair confirmed that the core components for the developer portal will be delivered at the end of July. The team will perform iterations throughout August to refine these components, using standups to collect feedback and address errors before the September launch.
    
- AI-Driven Headless Testing Methodology: George Westbrook described the testing process within the "admin vault" review space. The team uses headless testing, where the AI executes defined user journeys thousands of times in parallel to validate success criteria. This process allows the team to identify issues with prompts, tool calls, and Model Context Protocol (MCP) server stability automatically.
    
- Model Optimization and Efficiency: George Westbrook explained that the team leverages larger, more intelligent models, such as Opus 4.8 A, to optimize the prompts and pipelines of smaller models. This strategy allows the team to achieve cost savings by using smaller models for production while utilizing the intelligence of larger models for testing, which replaces the need for manual onboarding flow testing.
    
- Clarification of Infrastructure Requirements: Ian Johnson expressed concern regarding the lack of clarity on AI-specific infrastructure requirements within the Azure environment. While Michael Moores confirmed that a working architecture design exists, there is an urgent need to identify the specific components required for the AI implementation to prevent operationalization delays.
    
- Containerized Architecture and Deployment: Brett StClair and George Westbrook clarified that the AI architecture is containerized, making the environment—whether Azure or GCP—less critical for portability. They noted that everything is managed via Terraform scripts and standard Azure DevOps CI/CD pipelines to ensure consistency.
    
- Client Stack Isolation and Architecture: Ian Johnson discussed the requirement for individual, ring-fenced client stacks to ensure security, which contrasts with the proposal from DT that utilizes central API management and an orchestration layer. This discrepancy regarding the target architecture for the business requires resolution with the CTO to ensure it aligns with client expectations.
    
- Authentication and Security Protocols: Ian Johnson and George Westbrook discussed the use of JWT (JSON Web Token) tokens for security. George Westbrook confirmed that they will reuse console authentication and append user IDs to every tool call or data access request. This ensures that every action taken by an agent is authenticated and aligned with the user's defined permissions.
    
- Request for Architectural Transparency: Brett StClair proposed holding a half-hour session to present the AI architecture and demonstrate how the agent components function. This session aims to help the team visualize the architecture and address the risk-averse nature of the DT organization regarding certification and security compliance.
    
- Prioritization of Features: Brett StClair committed to uploading the current proposal to the vault and requested that Dorte Dye and Michael Moores review it to ensure that features for phase two and phase three are prioritized correctly.
    
- Marketing Messaging Dependencies: Ian Johnson noted that marketing messaging is currently held up because the full scope of the "AI story" and specific deliverables for the September go-to-market versus the December operational date are not yet finalized. Achieving certainty on these deliverables is a priority to ensure the team does not mislead potential clients.
    
- Documentation and Next Steps: Brett StClair committed to updating the proposal into a formal solution architecture document to serve as a single source of truth. Ian Johnson will coordinate internal discussions regarding the architecture and communicate the necessary adjustments to the team, and they agreed to schedule a future team dinner once the current phase is stabilized.
    

**