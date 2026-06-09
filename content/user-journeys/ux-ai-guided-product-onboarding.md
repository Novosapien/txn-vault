---
component: "[[co-pilot]]"
type: user-journey
author: M.Moores
status: imported
---

# AI Guided Product Onboarding v1.0

> **Component:** [[co-pilot]] · **Journeys index:** [[user-journeys]] · **Vision:** [[vision]]

AI assisted configuration guidance for launching and maintaining card programs Version: 1.0 Author: M.Moores Date: 05/03/2026 AI Guided Product Onboarding and Configuration Optimisation

### Document Control

# Date Author Description 1.0 05/03/2026 M.Moores Initial version

## 1. Purpose

This document defines the behavioural journey through which a Programme Manager or Operations user receives AI guided recommendations when onboarding a new client or configuring a card programme within the TXN platform.

The journey illustrates how TXN Intelligence assists users by analysing programme intent, regional context, and risk profile to generate prescriptive configuration recommendations.

AI guidance is surfaced directly within the TXN Console during the normal programme onboarding and configuration workflow. The AI capability operates as an assistive layer within the Console user interface rather than a separate system.

Its purpose is to:

- Clarify how AI supports onboarding and configuration decisions within the TXN

Console

- Define how recommendations are generated, explained, and approved
- Reduce operational errors caused by manual configuration
- Provide a behavioural foundation for User Stories and Requirements

This journey focuses on AI assisted guidance and recommendation review within the Console experience.

It does not cover the technical implementation of configuration controls within the platform.

## 2. Persona

### Primary Persona

- Programme Operations Administrator: Responsible for onboarding new clients and

configuring card programme parameters including limits, controls, and product structures using the TXN Console.

### Secondary Persona

- Programme Technical Operator: Responsible for validating configuration behaviour

and ensuring programme settings operate as expected.

## 3. Context

A new client is being onboarded to the TXN platform or an existing programme configuration is being reviewed through the TXN Console.

Programme setup requires decisions across multiple areas including:

- Product structures
- Spend limits and transaction thresholds
- Merchant category controls
- Regional restrictions and transaction rules

These decisions are traditionally based on experience, manual review, and historical precedent.

TXN Intelligence is integrated into the TXN Console configuration workflow and provides AI driven recommendations informed by historical TXN platform data and aggregated patterns from comparable programmes operating in similar regions.

AI recommendations remain advisory and require explicit user approval before application.

## 4. Trigger

One or more of the following:

- A Programme Manager initiates onboarding for a new client programme within the

TXN Console

- A user begins configuration of a new card product within the Console programme

management interface

- A user requests configuration optimisation suggestions while reviewing an existing

programme configuration

- The Console detects configuration gaps or potential optimisation opportunities and

surfaces an AI recommendation prompt

## 5. Primary Outcome

The user receives clear AI generated configuration recommendations within the TXN Console interface aligned to programme intent and risk profile and safely applies approved settings to the programme configuration.

## 6. Secondary Outcomes

- User gains confidence in recommended configuration decisions
- Programme setup is completed faster and with fewer manual errors
- Configuration conflicts and compliance issues are detected before application
- Users understand the reasoning behind each recommended configuration

## 7. Journey Flow

### Step 1 - Access Programme Configuration in TXN Console

User Action

- The user logs into the TXN Console and navigates to the programme onboarding or

configuration interface.

Information Presented

- Programme configuration interface displaying current or default settings including

product structures, limits, and control parameters.

Decision Point

- User chooses to configure the programme manually or request AI configuration

guidance.

Risks

- Users may misconfigure programme settings due to lack of experience or

incomplete knowledge.

Expected System Behaviour

- The Console clearly presents an option to request AI configuration

recommendations based on programme intent and context.

### Step 2 - Provide Programme Context

User Action

- The user provides contextual information describing the intended programme

configuration.

Information Presented Structured input fields capturing information such as:

- Region or regions of operation
- Product type and intended usage
- Target customer profile
- Risk tolerance or fraud sensitivity

Decision Point

- User confirms the contextual information describing the programme.

Risks

- Incomplete or inaccurate inputs may lead to inappropriate recommendations.

Expected System Behaviour

- The Console validates required inputs and provides guidance explaining the

purpose of each field.

### Step 3 - Generate AI Configuration Recommendations

User Action

- The user requests AI generated configuration recommendations.

Information Presented AI generated suggestions including:

- Recommended product group structures
- Suggested spend limits and thresholds
- Merchant and transaction type control settings

Each recommendation includes a clear explanation describing the reasoning and data patterns informing the suggestion.

Decision Point

- User reviews whether the recommendations align with programme objectives.

Risks

- Users may distrust recommendations if reasoning is unclear.

Expected System Behaviour

- The Console displays explainable recommendations including reasoning summaries

and confidence indicators.

### Step 4 - Review Validation and Compliance Checks

User Action

- User reviews validation results associated with the recommended configuration.

Information Presented Validation checks confirming that recommendations:

- Do not conflict with existing configuration rules
- Align with regional requirements
- Do not violate platform policy constraints

Decision Point

- User confirms whether the configuration is safe to apply.

Risks

- Conflicting rules or hidden dependencies could introduce operational risk.

Expected System Behaviour

- The Console automatically performs conflict detection and clearly highlights any

issues requiring resolution.

### Step 5 - Approve or Adjust Recommendations

User Action

- User reviews each recommended configuration and chooses whether to approve,

modify, or reject individual settings.

Information Presented

- Editable configuration settings alongside AI recommendation explanations.

Decision Point

- User decides whether to apply the configuration exactly as recommended or modify

specific parameters.

Risks

- Users may blindly accept recommendations without fully reviewing them.

Expected System Behaviour

- The Console requires explicit approval before applying configuration changes and

clearly highlights the impact of each change.

### Step 6 - Apply Approved Configuration

User Action

- User confirms the approved configuration settings and applies them to the

programme within the Console.

Information Presented

- Confirmation of applied configuration changes and summary of approved

recommendations.

Decision Point

- User confirms that onboarding configuration is complete.

Risks

- Unapproved automated configuration changes could introduce operational risk.

Expected System Behaviour

- The Console applies configuration only after explicit user approval and records the

action in the audit log including the AI recommendation context.

## 8. Control and Risk Considerations

- AI recommendations must remain advisory and never apply configuration

automatically.

- All configuration changes must require explicit user approval through the TXN

Console workflow.

- AI recommendations must include clear reasoning describing the factors influencing

each suggestion.

- Validation checks must detect configuration conflicts before changes are applied.
- All AI generated recommendations and approvals must be logged for audit and

traceability.

## 9. Governance Boundaries

This journey does not cover:

- Autonomous AI modification of programme configuration
- Low level configuration engine implementation
- Fraud monitoring or transaction level risk analysis
- AI model training or data pipeline architecture.