---
component: "[[a2a-endpoint]]"
type: user-journey
author: M.Moores
status: imported
---

# AI Transaction Query v1.0

> **Component:** [[a2a-endpoint]] · **Journeys index:** [[user-journeys]] · **Vision:** [[vision]]

Secure access to TXN transaction and entity data by authorised client AI systems through MCP connectivity Version: 1.0 Author: M.Moores Date: 06/03/2026 Governed AI Transaction Data Query via MCP

### Document Control

# Date Author Description 1.0 06/03/2026 M.Moores Initial version

## 1. Purpose

This document defines the behavioural journey through which a client owned AI system securely queries transaction and entity level data from the TXN platform through the Model Context Protocol.

The journey illustrates how external AI systems can retrieve operational data such as transaction history, card activity, or account level information in order to support client owned customer service or cardholder support tools.

The AI interaction occurs through MCP connectivity which acts as the controlled interface between external AI systems and the TXN platform APIs.

Its purpose is to:

- Clarify how external AI systems securely query transactional and entity data
- Define how permissions and data access scope are enforced
- Ensure that all AI initiated queries remain governed and auditable
- Provide a behavioural foundation for User Stories and Requirements

This journey focuses on governed AI access to TXN entity and transaction data.

It does not define MCP protocol implementation details or data storage architecture.

## 2. Persona

### Primary Persona

Customer Owned AI Agent integrated into the client organisation support systems and interacting with TXN through MCP connectivity.

### Secondary Persona

Cardholder Support System using the client AI agent to provide automated responses to cardholder enquiries.

## 3. Context

Client organisations may operate their own AI driven customer service systems such as chatbots or support assistants.

These systems may assist cardholders with questions such as:

- Why a transaction was declined
- Whether a transaction has been completed or settled
- Recent card activity or transaction history
- Card or account status information

To enable this capability, the client AI system must be able to securely query transactional and entity data held within the TXN platform.

TXN provides this access through the Model Context Protocol which governs how external systems interact with TXN APIs.

This approach ensures that AI systems:

- Access only permitted data within the authorised client scope
- Respect privacy and data protection boundaries
- Produce fully auditable data access activity
- Operate within secure and governed API interaction patterns

External AI systems do not access internal TXN services directly. All queries must pass through MCP governance controls.

These systems may assist cardholders with questions such as:

- Why a transaction was declined
- Whether a transaction has been completed or settled
- Recent card activity or transaction history
- Card or account status information

For example a cardholder may ask:

- Why did my payment fail at a merchant?

The client AI system can retrieve the relevant transaction information from the TXN platform and interpret the decline reason and associated programme rule to generate a plain language explanation for the cardholder.

## 4. Trigger

One or more of the following:

- A cardholder asks a question through the client chatbot regarding a transaction
- A support agent uses the client AI assistant to retrieve transaction information
- The client AI system attempts to retrieve cardholder activity to assist with a support

interaction

- The AI system submits a governed query request through MCP to the TXN platform

## 5. Primary Outcome

The client AI system securely retrieves the authorised transaction or entity data required to respond to the cardholder enquiry.

## 6. Secondary Outcomes

- Cardholders receive faster responses through automated support channels
- Support agents have quicker access to transaction level information
- Client organisations can integrate TXN data into their own support experiences
- All AI initiated queries remain traceable and governed

## 7. Journey Flow

### Step 1 - Cardholder Support Query Initiated

User Action A cardholder asks a question through the client organisation support interface such as a chatbot or support application.

Information Presented The client AI system receives the cardholder request which may reference:

- A specific transaction
- Recent account activity
- Card status or transaction history

Decision Point The AI system determines whether TXN transaction or entity data is required to answer the query.

Risks The AI system attempting to retrieve data outside its authorised scope.

Expected System Behaviour The client AI system prepares a structured query request for the TXN platform through MCP.

### Step 2 - Submit Transaction Data Query through MCP

User Action The client AI system submits a query request through the MCP interface to retrieve the relevant data.

Information Presented The MCP gateway receives the request including:

- Requested data type such as transaction history or transaction details
- Identity of the requesting system
- Authentication credentials and permission scope

Decision Point The platform determines whether the requesting system is authorised to retrieve the requested data.

Risks Unauthorised systems attempting to access sensitive transaction data.

Expected System Behaviour The MCP gateway validates authentication credentials and confirms that the request falls within the permitted data scope.

### Step 3 - Validate Data Access Scope

User Action The MCP layer evaluates the request against governance and access control rules.

Information Presented Access validation checks including:

- Client programme scope
- Cardholder data access permissions
- Environment context such as sandbox or production

Decision Point The platform determines whether the query is authorised.

Risks Cross client data exposure or excessive data retrieval.

Expected System Behaviour The system restricts data access strictly to the authorised programme and cardholder

### context.

### Step 4 - Execute Authorised Data Query

User Action The platform executes the authorised request through the TXN API entity endpoints.

Information Presented The relevant data is retrieved including transaction attributes, timestamps, merchant information, and transaction status.

Decision Point The system verifies that the returned data aligns with the requested query scope.

Risks Incomplete or inconsistent data retrieval.

Expected System Behaviour The system returns only the authorised data fields required to fulfil the request.

### Step 5 - Return Data to Client AI System

User Action The retrieved data is returned through MCP to the client AI system.

Information Presented Structured transaction or entity data which the client AI system can interpret.

Decision Point The AI system determines how to present the information within the client support interface.

Risks Incorrect interpretation of transaction data by the client AI system.

Expected System Behaviour The platform returns structured data aligned with API specifications to ensure consistent interpretation.

### Step 6 - Respond to Cardholder Query

User Action The client AI system interprets the retrieved data and generates a response for the cardholder.

Information Presented A plain language explanation describing the relevant transaction information or account activity.

For example the AI may combine transaction data and programme configuration context to explain the outcome.

Example explanation:

- The payment was declined because international transactions are currently disabled

on your card.

Other explanations may include:

- Transaction declined due to spend limit being exceeded
- Transaction declined due to merchant category restrictions
- Transaction declined because the card was temporarily locked

Decision Point The AI system determines whether the query has been resolved or requires escalation to a human support agent.

Risks Incorrect or misleading explanation provided to the cardholder.

Expected System Behaviour The client AI system generates explanations based on authorised transaction data retrieved from the TXN platform while respecting programme scope and data access permissions.

## 8. Control and Risk Considerations

- All client AI queries must pass through MCP governance controls.
- External AI systems must not access TXN services directly.
- Data access must be restricted to authorised programme and cardholder scope.
- Sensitive personal data must remain protected under applicable data protection

requirements.

- All AI initiated data queries must be recorded for audit and monitoring purposes.

## 9. Governance Boundaries

This journey does not cover:

- Client side chatbot implementation
- Internal TXN data storage architecture
- AI model training or reasoning processes
- Infrastructure or cryptographic control mechanisms.