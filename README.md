# agenticThis project implements a governed multi-agent AI system designed to evaluate financial expense submissions in enterprise environments.

The system combines retrieval-augmented reasoning, multi-agent orchestration, fraud risk scoring, self-evaluation, escalation logic, and immutable audit logging to simulate production-grade financial AI governance. Unlike standard RAG chatbots, this architecture emphasizes determinism, traceability, resilience, and structured decision-making.

Problem Statement

Financial organizations face significant risk from:

Misclassified expense submissions

Fraudulent reimbursements

Regulatory non-compliance

Inconsistent manual review processes

Traditional workflows are reactive and difficult to audit.

This project introduces a governed agentic AI decision engine that evaluates expense submissions, grounds reasoning in policy documents, scores behavioral risk, enforces escalation rules, and logs every decision for compliance auditing.

System Architecture

High-Level Flow:

User Input
→ Planner Agent
→ Retrieval Agent (FAISS + Embeddings)
→ Compliance Reasoning Agent (LLM)
→ Self-Evaluator Agent
→ Retry Loop (if reasoning quality is weak)
→ Fraud Risk Scoring Agent
→ Escalation Engine
→ Immutable Audit Logger

Agent Responsibilities

Planner Agent
Determines which tools and actions should execute based on expense attributes.

Retrieval Agent
Uses vector embeddings and FAISS to retrieve relevant financial policy clauses.

Compliance Reasoning Agent
Generates structured compliance decisions grounded strictly in retrieved policies.

Self-Evaluator Agent
Audits reasoning output for grounding, hallucination, and logical consistency. Can trigger retry.

Fraud Risk Agent
Applies rule-based heuristics such as high-value thresholds, suspicious keywords, and behavioral flags.

Escalation Engine
Escalates decisions when:

Compliance decision is rejected

Fraud risk is high

Confidence is low

Grounding is weak

Audit Logger
Appends structured decision trace to an immutable JSONL file for compliance auditing.

Enterprise Governance Features

Multi-agent orchestration

Reflection-based retry loop

Deterministic escalation logic

Append-only structured audit logging

LLM timeout protection

Safe fallback handling for malformed model output

Retry limits to prevent infinite loops

Structured JSON responses

Failure-resilient logging

Example API Response
{
  "planned_actions": ["retrieve_policies", "compliance_reasoning"],
  "decision": {
    "decision": "flagged",
    "reasoning": "...",
    "confidence": 0.82
  },
  "evaluation": {
    "grounded": true,
    "reasoning_quality": 0.88,
    "needs_retry": false
  },
  "fraud_risk": {
    "risk_score": 0.5,
    "risk_level": "medium"
  },
  "retry_count": 0,
  "escalated_for_review": true
}
Why This Is Not Just RAG

This system goes beyond basic Retrieval-Augmented Generation by implementing:

Planner-controlled orchestration

Meta-evaluation of reasoning quality

Autonomous retry correction

Fraud scoring layer

Deterministic escalation logic

Immutable audit trail

It reflects production-oriented financial AI governance rather than a chatbot demonstration.

Technology Stack

FastAPI (API layer)

FAISS (Vector similarity search)

SentenceTransformers (Embeddings)

Ollama + Llama3 (Local LLM)

Python

Structured JSONL logging