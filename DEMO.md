# AI Delivery Agent — Demo

This document demonstrates how the AI Delivery Agent analyzes the synthetic project portfolio and presents decision-support information to a manager.

All project, resource, financial, KPI, Jira-style, and Confluence-style data shown in this demo are synthetic and created solely for prototype purposes.

The demo does not represent a live connection to Jira, Confluence, HR, financial, or other enterprise systems.
---

## Portfolio Executive Summary

The Agent provides a concise management view of the portfolio before presenting detailed project-level analysis.

The summary is designed to show:

- Overall project status
- Upcoming critical milestone or deadline
- Key delivery concern
- Cross-project dependency impact
- Relevant resource, financial, or KPI signals

Example output format:

| Project | Overall Status | Upcoming Critical Point / Date | Short Note |
|---|---|---|---|
| PRJ-001 — Payment API Modernization | — | 30.09.2026 | — |
| PRJ-002 — Mobile Checkout Revamp | — | 25.09.2026 | — |
| PRJ-003 — Customer Self-Service Portal | — | 15.10.2026 | — |
| PRJ-004 — AI Recommendation Engine | — | 10.10.2026 | — |
| PRJ-005 — Data Platform Migration | — | 20.09.2026 | — |
| PRJ-006 — Cloud Infrastructure Upgrade | — | 05.09.2026 | — |
| PRJ-007 — Identity & Access Security Upgrade | — | 15.09.2026 | — |
| PRJ-008 — CRM Integration Program | — | 05.10.2026 | — |

> Status and short-note fields are intentionally not pre-filled here. They should be generated from the available prototype data and decision policy rather than manually invented for the demo.
> ---

## Example Decision-Support Flow

For each project, the Agent separates source-backed information from calculations and interpretation.

### FACT

Information directly supported by the available project data or documentation.

### CALCULATED

Information derived from source data using a repeatable calculation.

### INFERENCE

A logical conclusion based on available facts and/or calculated information. An inference is not presented as a confirmed fact.

### ROOT CAUSE CANDIDATE

When the available evidence indicates a possible cause, the Agent can identify it as a Root Cause Candidate rather than presenting it as a definitive root cause.

### RECOMMENDATION

Based on the available evidence, the Agent can suggest an action for management consideration.

### HUMAN APPROVAL

Critical actions remain subject to explicit human approval.

Examples include:

- Resource reassignment
- Deadline or milestone changes
- Scope changes
- Priority changes
- Risk acceptance or closure
- Changes to source-system data

**The Agent recommends. The manager decides.**
---

## Example Project Analysis

A project-level analysis can combine multiple data sources before producing a management recommendation.

### Example: PRJ-001 — Payment API Modernization

The Agent can evaluate the project using:

- Project schedule and progress data
- Jira-style issues, blockers, effort, and dependencies
- Confluence-style project documentation
- Resource allocation and capacity data
- Financial data including budget, CAPEX, OPEX, and Expected ROI
- KPI target and current values

The analysis then follows the governed decision flow:

**Source Data → Risk Detection → Root Cause Candidate Analysis → Resource / Capacity Analysis → Recommendation → Human Approval**

If the available evidence is insufficient to support a conclusion, the Agent should return **UNKNOWN** rather than inventing missing information.

If a recommendation involves a critical management action, such as resource reassignment, scope change, priority change, or deadline change, execution remains subject to explicit human approval.
---

## Example Project Analysis

A project-level analysis can combine multiple data sources before producing a management recommendation.

### Example: PRJ-001 — Payment API Modernization

The Agent can evaluate the project using:

- Project schedule and progress data
- Jira-style issues, blockers, effort, and dependencies
- Confluence-style project documentation
- Resource allocation and capacity data
- Financial data including budget, CAPEX, OPEX, and Expected ROI
- KPI target and current values

The analysis then follows the governed decision flow:

**Source Data → Risk Detection → Root Cause Candidate Analysis → Resource / Capacity Analysis → Recommendation → Human Approval**

If the available evidence is insufficient to support a conclusion, the Agent should return **UNKNOWN** rather than inventing missing information.

If a recommendation involves a critical management action, such as resource reassignment, scope change, priority change, or deadline change, execution remains subject to explicit human approval.
---

## What This Demo Demonstrates

This demo shows how the prototype is designed to:

- Combine structured portfolio data with project documentation
- Analyze delivery risk across multiple dimensions
- Investigate possible root causes without automatically treating resource capacity as the cause
- Consider cross-project dependencies and potential downstream impact
- Evaluate resource/capacity, financial, and KPI signals
- Separate FACT, CALCULATED, INFERENCE, and UNKNOWN
- Produce management-oriented recommendations
- Keep critical management decisions under Human Approval

The purpose of the prototype is not to automate management decisions, but to provide traceable decision support based on the available data.

**AI supports the decision. Human accountability remains with the manager.**
