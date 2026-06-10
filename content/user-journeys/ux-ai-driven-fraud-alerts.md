---
component: "[[fraud-risk-assist]]"
type: user-journey
author: M.Moores
status: imported
---

# AI Driven Fraud Alerts v1.0

> **Component:** [[fraud-risk-assist]] · **Journeys index:** [[user-journeys]] · **Vision:** [[vision]]

AI detection of emerging fraud patterns and merchant risk signals across programs Version: 1.0 Author: M.Moores Date: 06/03/2026 AI Driven Fraud Pattern Alerts

### Document Control

# Date Author Description 1.0 06/03/2026 M.Moores Initial version

## 1. Purpose

This document defines the behavioural journey through which TXN Intelligence identifies emerging fraud patterns within transaction activity and generates actionable risk alerts.

The journey illustrates how AI analyses transaction behaviour across merchants, cardholders, and programmes to detect patterns that may indicate fraudulent activity.

When suspicious behaviour is detected the system generates alerts within the TXN Console along with contextual insights, merchant risk scoring, and recommended mitigation actions.

Its purpose is to:

- Detect emerging fraud patterns across transaction activity
- Provide early warning signals to risk and operations teams
- Surface merchant risk indicators and behavioural anomalies
- Provide a behavioural foundation for User Stories and Requirements

This journey focuses on AI driven fraud pattern detection and alerting.

It does not cover automated transaction blocking or enforcement actions.

## 2. Persona

### Primary Persona

Risk and Fraud Analyst responsible for monitoring transaction activity and identifying potential fraud patterns.

### Secondary Persona

Programme Operations Administrator monitoring operational risk indicators within the TXN Console.

## 3. Context

Payment transaction activity generates large volumes of behavioural data across merchants, cardholders, and programmes.

Fraud patterns may emerge through abnormal behaviour such as:

- Unusual transaction volume increases
- Suspicious merchant activity
- Unexpected geographic transaction behaviour
- Repeated declines followed by successful transactions

Traditional fraud monitoring often relies on static rules which may fail to detect emerging behavioural patterns.

TXN Intelligence continuously analyses transaction activity across programmes and merchants to identify signals that may indicate fraudulent behaviour.

When potential fraud patterns are detected the system generates alerts and provides contextual insights to assist risk teams in assessing the situation.

## 4. Trigger

One or more of the following:

- AI detects abnormal transaction behaviour associated with a merchant
- AI detects a sudden increase in transaction volume across multiple programmes
- AI identifies unusual merchant or cardholder behavioural patterns
- Transaction activity deviates significantly from historical fraud baselines

## 5. Primary Outcome

The system generates a fraud risk alert describing the detected pattern and associated risk indicators.

## 6. Secondary Outcomes

Fraud risks are identified earlier

- Risk teams receive contextual insights to assist investigation
- Merchant level risk signals become easier to identify
- Operational visibility of fraud patterns improves

## 7. Journey Flow

### Step 1 - Monitor Transaction Activity

User Action TXN Intelligence continuously analyses transaction data across merchants, cardholders, and programmes.

Information Presented Transaction datasets including merchant activity, transaction volume, decline behaviour, and geographic patterns.

Decision Point The system evaluates whether the observed behaviour deviates from expected transaction patterns.

Risks Normal transaction fluctuations may appear suspicious.

Expected System Behaviour The system analyses behavioural patterns using historical transaction data and fraud indicators.

### Step 2 - Detect Suspicious Merchant Behaviour

User Action The AI system identifies unusual merchant activity that may indicate fraud risk.

Information Presented Examples may include:

- Merchant suddenly receiving high transaction volume across multiple programmes
- Unexpected increases in transaction approvals after repeated declines
- Unusual geographic transaction patterns

Decision Point The system determines whether the behaviour represents a potential fraud pattern.

Risks False positives may generate unnecessary alerts.

Expected System Behaviour The system evaluates the behaviour using contextual signals and assigns a fraud risk score.

### Step 3 - Calculate Merchant Risk Score

User Action The AI system calculates a risk score associated with the merchant or transaction pattern.

Information Presented Risk indicators including:

- Merchant activity changes
- Transaction pattern anomalies
- Cross programme behavioural signals

Decision Point The system determines whether the risk score exceeds the alert threshold.

Risks Incorrect scoring may misrepresent actual fraud risk.

Expected System Behaviour The system calculates risk scores using behavioural analysis and historical fraud signals.

### Step 4 - Generate Fraud Alert

User Action The system generates a fraud alert within the TXN Console.

Information Presented Alert details including:

- Affected merchant
- Detected behavioural pattern
- Calculated risk score

Decision Point Risk teams review the alert to determine whether investigation is required.

Risks Critical alerts may be overlooked if alert volume is high.

Expected System Behaviour The Console displays fraud alerts within the operational monitoring interface.

### Step 5 - Provide Recommended Risk Controls

User Action The system provides recommended actions to mitigate potential fraud risk.

Information Presented Recommended actions may include:

- Review merchant activity
- Apply additional transaction monitoring
- Adjust programme risk controls

Decision Point Risk teams determine whether mitigation actions should be applied.

Risks Incorrect mitigation actions could impact legitimate transactions.

Expected System Behaviour The system presents recommended actions while leaving final decisions to authorised personnel.

### Step 6 - Initiate Investigation

User Action Risk teams investigate the fraud alert using TXN Console tools.

Information Presented Relevant transaction data, merchant activity history, and associated programme context.

Decision Point Risk teams determine whether the behaviour represents confirmed fraud or benign activity.

Risks Delayed investigation may allow fraudulent activity to continue.

Expected System Behaviour The Console provides access to relevant transaction and merchant data required for investigation.

## 8. Control and Risk Considerations

- Fraud alerts must include explainable reasoning and supporting data.
- AI driven fraud detection must remain auditable and transparent.
- Risk alerts must not automatically block transactions without authorised controls.
- Risk scoring models must be monitored for accuracy and bias.
- All alerts and associated analysis must be logged for audit purposes.

## 9. Governance Boundaries

This journey does not cover:

- Automated transaction blocking or card suspension
- Fraud case management workflows
- External fraud intelligence integrations
- AI model training or fraud model infrastructure.