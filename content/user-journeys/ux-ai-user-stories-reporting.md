---
component: "[[agent-inbox-alerts]]"
type: user-journey
author: M.Moores
status: imported
---

# AI User Stories Reporting v1.0

> **Component:** [[agent-inbox-alerts]] · **Journeys index:** [[user-journeys]] · **Vision:** [[vision]]

AI generated reports from conversational queries with governed data access Version: 1.0 Author: M.Moores Date: 06/03/2026 Natural Language Reporting in TXN Console

### Document Control

# Date Author Description 1.0 06/03/2026 M.Moores Initial version

## 1. Purpose

This document defines the behavioural journey through which users generate operational and analytical reports using natural language queries within the TXN Console.

The journey illustrates how TXN Intelligence interprets conversational reporting requests and generates structured reports using authorised platform data.

Reports are generated according to the user’s role based permissions and programme scope to ensure that only authorised data is returned.

Generated reports can be saved and reused later without requiring AI processing, allowing users to run the same report repeatedly while reducing AI usage and operational cost.

Its purpose is to:

- Enable users to create custom reports using natural language queries
- Improve accessibility of platform analytics without requiring technical report building
- Ensure reporting remains governed by role based access control
- Allow reusable report templates to be saved after initial creation

This journey focuses on AI assisted report generation and reuse within the TXN Console.

It does not cover data warehouse architecture or analytics infrastructure design.

## 2. Persona

### Primary Persona

Programme Operations Administrator using TXN Console analytics to monitor programme activity and operational performance.

### Secondary Persona

Customer Success Manager reviewing programme performance metrics and operational insights.

## 3. Context

Users often require custom reports that are not available as predefined analytics views.

Traditionally these reports require manual configuration of filters, grouping rules, and metrics within reporting tools.

TXN Intelligence allows users to describe the report they require using natural language.

Examples may include requests such as:

- Show me the top 10 merchants in France
- Show transaction volume by merchant category this month
- Show the highest value transactions for Program X last week

The AI system interprets the request, applies access governance rules, and generates a structured report within the TXN Console.

Once created, reports can be saved as reusable report templates that can be executed later without requiring AI interpretation.

## 4. Trigger

One or more of the following:

- A user opens the reporting interface within the TXN Console
- A user requests a custom report that does not exist in predefined dashboards
- A user enters a natural language reporting query in the Console reporting assistant

## 5. Primary Outcome

The user receives a structured report generated from their natural language request within the TXN Console.

## 6. Secondary Outcomes

- Users can generate custom reports without technical reporting expertise
- Data access remains governed by role and programme permissions
- Saved report templates can be reused without invoking AI processing
- Operational insights become easier to obtain across the platform

## 7. Journey Flow

### Step 1 - Open Reporting Assistant in TXN Console

User Action The user navigates to the reporting section of the TXN Console and opens the natural language reporting assistant.

Information Presented A conversational interface allowing the user to describe the report they want to generate.

Decision Point User enters a natural language query describing the report requirements.

Risks Users may submit ambiguous or incomplete reporting requests.

Expected System Behaviour The assistant accepts conversational input and may request clarification if required.

### Step 2 - Submit Natural Language Query

User Action The user enters a reporting request such as:

- Show me the top 10 merchants in France.

Information Presented The system displays the interpreted query including detected filters, groupings, and metrics.

Decision Point User confirms that the interpreted request matches their intended report.

Risks Incorrect interpretation of the reporting intent.

Expected System Behaviour The system translates the natural language request into a structured reporting query and presents the interpreted parameters for confirmation.

### Step 3 - Validate Governance and Data Access

User Action The platform evaluates the requested report against access control rules.

Information Presented Governance checks including:

- User role permissions
- Programme scope
- Authorised data domains

Decision Point The system determines whether the user is authorised to access the requested data.

Risks Reports exposing unauthorised data.

Expected System Behaviour The system enforces role based access control and restricts the report dataset to authorised information.

### Step 4 - Generate Structured Report

User Action The system generates the requested report within the TXN Console reporting interface.

Information Presented

- A structured report containing the requested metrics and filters.
- Example output may include a ranked list of merchants based on transaction

volume within France.

Decision Point User reviews whether the report answers their question.

Risks Reports may not fully match the user’s expectations.

Expected System Behaviour The system clearly presents the report structure and allows the user to refine the query if needed.

### Step 5 - Save Report for Reuse

User Action The user chooses to save the generated report as a reusable report template.

Information Presented Options allowing the user to name and store the report configuration.

Decision Point User determines whether the report should be reused later.

Risks Users may recreate reports unnecessarily.

Expected System Behaviour The system stores the structured report configuration so that it can be executed again without invoking AI interpretation.

### Step 6 - Reuse Saved Report

User Action At a later time the user runs the saved report directly from the reporting interface.

Information Presented The stored report configuration executes using the current dataset.

Decision Point User reviews the updated report results.

Risks Saved reports may become outdated if underlying data structures change.

Expected System Behaviour The system executes the saved report without requiring AI processing while ensuring governance rules remain enforced.

## 8. Control and Risk Considerations

- All generated reports must respect role based access control and programme

scope.

- Natural language queries must be validated before report execution.
- Sensitive financial and transaction data must remain protected.
- Saved reports must revalidate permissions when executed.
- AI generated queries must remain auditable for governance and troubleshooting.

## 9. Governance Boundaries

This journey does not cover:

- Analytics infrastructure or data warehouse architecture
- External reporting integrations
- AI model training or natural language processing implementation.