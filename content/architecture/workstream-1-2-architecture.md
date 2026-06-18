---
title: "TXN Proposed Workstream 1 & 2 Architecture (1st Draft)"
type: architecture-diagram
source: "Michael (Azure architecture draft)"
received-from: Michael
date: 2026-06
status: reference
artifact: "workstream-1-2-architecture.png"
maps-to:
  - "[[architecture]]"
  - "[[integrations]]"
---

# TXN Proposed Workstream 1 & 2 Architecture (1st Draft)

> **Reference artifact (placed, 1st draft):** First-draft Azure infrastructure architecture for Workstreams 1 & 2, received from Michael. The image below is the canonical artifact; the text underneath is a transcription so the diagram is searchable and wikilinkable inside the vault. Routed from [[architecture]]. Treat the specifics as 1st-draft and verify against the source image before relying on them.
>
> **Platform confirmed (2026-06):** This **TXN-controlled Azure** environment is the agreed deployment platform (resolves the dev-environment open question in [[integrations]]). The diagram itself is still a 1st draft; the *decision* to run on TXN's Azure is settled. The earlier "DT: Kubernetes / Stackworkz: VM-based" note describes the build partners' own environments, not the target platform.

![[workstream-1-2-architecture.png]]

---

## What the diagram shows

A multi-region Azure deployment for the TXN platform, drawn as two parallel traffic flows (Workstream 1 and Workstream 2, distinguished by colour in the legend) running from external actors at the top, down through edge/security/routing, into per-region application clusters, and back out.

### Actors (top of the flow)

- Consultant
- Customer / Banker
- Program Manager

### Edge and routing

- **Azure Web Application Firewall (WAF)** - threat detection on inbound requests.
- **Azure Front Door (Global)** - global entry point; routes to the optimal region.
- **Identity & Access Management (IAM)** - centralised authentication.

### Regional deployment (active-active, two regions)

The platform is mirrored across two sites for geographic redundancy:

- **Site A - Region 1**
- **Site B - Region 2**

Each region contains:

- **API Management Service** - authenticates and routes API requests.
- **Azure Kubernetes Service (AKS) cluster** with separated node roles: Web Node (serves UI), API Node (processes API calls), Backend Services.
- **Key Vault** - secrets management.
- **Scale Units** (e.g. Scale Unit 1, Scale Unit 2) - horizontal scale within the region.
- **SQL Server / database** - with read replicas; data replicated across regions for disaster recovery.

---

## Architecture patterns and design principles (transcribed from the diagram)

**High availability**
- Multi-region deployment ensures service continuity.
- Automatic failover at multiple layers.
- Load balancing across multiple nodes in Azure Kubernetes Service.

**Security in depth**
- Multiple security layers (WAF through API Management into AKS network policies).
- Centralised authentication with Identity & Access Management (IAM).
- DDoS protection.
- Audit logging for compliance.

**Scalability**
- Horizontal scaling via AKS.
- Auto-scaling based on demand.
- CDN for content delivery optimisation.
- Database read replicas for performance.

**Microservices architecture**
- Separation of concerns (API, Backend Services, Web Application).
- Independent deployment and scaling.
- Resilience through isolation.

**Geographic redundancy**
- Active-active deployment across two Azure regions.
- Data replication for disaster recovery.
- Reduced latency through geo-routing.

---

## Traffic flow (normal inbound path, transcribed)

1. **Inbound** - user accesses the application via the frontend.
2. **Security** - request passes through the WAF for threat detection.
3. **Routing** - Azure Front Door routes to the optimal region.
4. **Authentication** - user validated against IAM.
5. **API gateway** - API Management authenticates and routes the request.
6. **Processing** - request reaches the AKS cluster (Web Node serves UI; API Node processes API calls).
7. **Backend** - Backend Services handle transaction processing; secrets retrieved from Key Vault.
8. **Data** - the database serves/persists data.
9. **Response** - data flows back through the same path to the user.

_(Workstream 1 and Workstream 2 flows are colour-coded in the legend; the exact per-workstream routing differences should be confirmed against the source image.)_

---

## Why it matters to the vault

- This is the underlying **platform infrastructure** for Workstreams 1 & 2: the deployment substrate the TXN product components run on.
- It should inform [[architecture]] (cross-cutting technical decisions) and connects to [[integrations]] (how external/edge services attach).
- The API Management + WAF + IAM edge is where the [[agent-access-layer]] external API surface and the [[developer-support]] portal/MCP exposure ultimately land.
