---
component: "[[a2a-endpoint]]"
type: user-journey
author: M.Moores
status: imported
---

# AI User Stories Mapping v1.0

> **Component:** [[a2a-endpoint]] · **Journeys index:** [[user-journeys]] · **Vision:** [[vision]]

Secure execution of operational TXN API actions by authorised client AI systems through MCP governance Version: 1.0 Author: M.Moores Date: 06/03/2026 Governed AI Initiated API Actions via MCP

### Document Control

# Date Author Description 1.0 05/03/2026 M.Moores Initial version

## 1. Purpose

This document defines the behavioural journey through which a client owned AI system securely interacts with operational capabilities exposed by the TXN API platform through the Model Context Protocol.

The journey illustrates how an external AI system can request operational actions within the TXN ecosystem while remaining subject to strict governance, permission controls, and approval boundaries.

The AI interaction occurs through MCP connectivity which acts as the controlled interface between external AI systems and the TXN platform.

Its purpose is to:

- Clarify how external AI systems securely request operational actions
- Define how permissions, risk classification, and approval requirements are enforced
- Ensure that all AI initiated actions remain governed, auditable, and explainable
- Provide a behavioural foundation for User Stories and Requirements

This journey focuses on governed AI interaction with TXN operational APIs.

It does not define MCP protocol implementation details or encryption mechanisms.

## 2. Persona

### Primary Persona

Customer Owned AI Agent operating within the client organisation and interacting with the TXN platform through MCP connectivity.

### Secondary Persona

Programme Operations Administrator who retains approval authority for high impact configuration changes.

## 3. Context

Clients may operate their own AI systems capable of analysing operational data and initiating requests to adjust programme configuration or operational parameters.

Examples may include:

- Adjusting spend limits across card products
- Modifying operational thresholds
- Responding to observed risk conditions
- Automating operational adjustments across multiple programmes

To enable this safely, TXN exposes operational capabilities through the Model Context Protocol which provides a governed interaction layer between AI systems and TXN APIs.

This layer ensures that AI systems:

- Operate only within permitted capabilities
- Respect role based access permissions
- Remain subject to risk classification and approval workflows
- Produce fully auditable operational actions

AI systems do not interact directly with internal TXN services. All requests must pass through MCP governance controls.

## 4. Trigger

One or more of the following:

- A client AI system generates an operational request based on analysis or user

instruction

- A human operator issues a natural language instruction through their AI system
- An automated operational rule within the client AI system proposes a configuration

change

- The AI system submits an operational request through MCP to the TXN platform

## 5. Primary Outcome

The AI initiated operational request is evaluated against governance rules and either executed, rejected, or routed for approval within the TXN platform.

## 6. Secondary Outcomes

- Operational changes are executed safely and within authorised scope
- High impact actions are routed through appropriate approval workflows
- All AI initiated requests and actions are recorded for audit and traceability
- Client AI systems can interact with TXN capabilities without compromising platform

governance

## 7. Journey Flow

### Step 1 - Submit AI Request through MCP

User Action

- A client owned AI system submits an operational request to the TXN platform

through the MCP interface.

- Example request may include adjusting spend limits across card products.

Information Presented The MCP gateway receives the request including:

- Requested action
- Target programme or product scope
- Identity of the requesting system
- Authentication credentials and permission scope

Decision Point The platform determines whether the AI system is authorised to request the specified action.

Risks Unauthorised systems attempting to initiate operational actions.

Expected System Behaviour The MCP gateway validates authentication credentials and verifies that the AI system is authorised to request actions within the specified scope.

### Step 2 - Interpret Requested Action

User Action The MCP service interprets the AI request and maps it to the appropriate TXN API capabilities.

Information Presented Structured action request describing:

- Operational action requested
- Target configuration objects
- Scope of impact

Decision Point The platform determines the classification of the requested action.

Possible classifications may include:

- Read only information request
- Configuration modification
- Operational parameter adjustment

Risks Incorrect mapping of the request to system capabilities.

Expected System Behaviour The MCP layer maps the request to permitted API capabilities and validates that the action exists within the registered capability set.

### Step 3 - Evaluate Governance and Risk Controls

User Action The platform evaluates the request against governance policies.

Information Presented Governance checks including:

- Role based permission validation
- Programme level access scope
- Risk classification of the requested action
- Environment context such as sandbox or production

Decision Point The platform determines whether the action can proceed automatically or requires human approval.

Risks High impact actions executed without appropriate oversight.

Expected System Behaviour

- The system enforces governance controls and blocks requests that exceed

permitted authority.

- Actions requiring approval are routed to authorised operators within the TXN

Console.

### Step 4 - Request Human Approval if Required

User Action If required, the platform surfaces the AI initiated request within the TXN Console for human review.

Information Presented Operators see:

- The requested action
- The scope of impact
- The reason provided by the AI system
- The expected configuration change

Decision Point The authorised user chooses whether to approve or reject the action.

Risks Operators approving actions without understanding the impact.

Expected System Behaviour The Console presents clear impact summaries and requires explicit approval before executing configuration changes.

### Step 5 - Execute Authorised API Action

User Action Once governance checks and approvals are satisfied, the platform executes the authorised operational action through the TXN API.

Information Presented Confirmation that the action has been executed including the resulting configuration state.

Decision Point The system verifies that the action completed successfully.

Risks Partial execution or unintended configuration effects.

Expected System Behaviour The system validates the resulting state and confirms that the requested change was applied correctly.

### Step 6 - Generate Audit Record and Explanation

User Action The platform records the AI initiated request and execution outcome.

Information Presented Audit records capturing:

- Identity of the requesting AI system
- Authorised user approvals if applicable
- Configuration changes performed
- Timestamp and environment context

Decision Point The system confirms that a complete audit record exists.

Risks Incomplete traceability of AI initiated operational changes.

Expected System Behaviour All requests, approvals, and resulting actions are recorded in immutable audit logs accessible for operational review and regulatory audit.

## 8. Control and Risk Considerations

- All AI initiated actions must pass through MCP governance controls.
- External AI systems must not have direct access to internal TXN services.
- Operational actions must respect role based permissions and programme scope.
- High impact configuration changes must require explicit human approval.
- All AI initiated requests and resulting actions must be logged with full traceability.

## 9. Governance Boundaries

This journey does not cover:

- Direct access to internal TXN services
- Internal TXN AI agents operating within the platform
- Low level MCP protocol implementation
- Infrastructure or cryptographic control mechanisms.