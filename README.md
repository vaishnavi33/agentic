Enterprise Agentic AI for Financial Compliance & Fraud Governance
Overview

This project implements a governed multi-agent AI system designed to evaluate financial expense submissions within enterprise environments.
The architecture combines retrieval-augmented reasoning, tool orchestration, fraud risk scoring, meta-evaluation, escalation logic, and immutable audit logging to simulate production-grade financial AI governance.Unlike standard RAG-based chat systems, this design prioritizes determinism, traceability, resilience, and structured decision-making aligned with real-world compliance requirements.

Problem Statement
Financial organizations face operational and regulatory risk from:
Misclassified expense submissions
Fraudulent reimbursements
Policy non-compliance
Inconsistent manual review processes
Traditional review workflows are reactive, difficult to scale, and challenging to audit.

This project introduces a governed agentic AI decision engine that:
Grounds reasoning in retrieved policy documents
Applies behavioral risk scoring
Enforces structured escalation rules
Logs every decision in an immutable audit trail

The objective is to simulate a production-ready compliance review system rather than a conversational AI prototype.
System Architecture
High-Level Flow:
User Input
→ Planner Agent
→ Retrieval Agent (FAISS + Embeddings)
→ Compliance Reasoning Agent (LLM)
→ Self-Evaluator Agent
→ Controlled Retry Loop
→ Fraud Risk Scoring Agent
→ Escalation Engine
→ Immutable Audit Logger

Agent Responsibilities
Planner Agent
Determines which tools and reasoning steps are required based on expense attributes.

Retrieval Agent
Performs semantic search over embedded policy documents to provide grounded context.

Compliance Reasoning Agent
Generates structured decisions strictly grounded in retrieved policy clauses.

Self-Evaluator Agent
Audits reasoning for grounding, hallucination risk, and logical consistency. Can trigger bounded retry.

Fraud Risk Agent
Applies deterministic heuristics such as high-value thresholds and suspicious keyword detection.

Escalation Engine
Escalates decisions when:
Compliance outcome is rejected
Fraud risk is elevated
Confidence is low
Grounding is insufficient
Audit Logger
Writes append-only structured JSON entries for regulatory traceability.
Enterprise Governance Features
Multi-agent orchestration with controlled execution
Reflection-based retry loop with bounded limits
Deterministic escalation enforcement
Append-only audit logging (JSONL format)
LLM timeout protection
Safe fallback handling for malformed model output
Structured response schema for downstream systems
Failure-resilient logging that never interrupts API execution

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
This system extends beyond traditional Retrieval-Augmented Generation by incorporating:
Planner-controlled tool orchestration
Meta-evaluation of reasoning quality
Autonomous but bounded retry correction
Fraud scoring layer
Deterministic escalation logic
Immutable audit trace
The architecture reflects production-oriented financial AI governance rather than a chatbot demonstration.
Technology Stack
FastAPI (API layer)
FAISS (Vector similarity search)
SentenceTransformers (Embeddings)
Ollama + Llama3 (Local LLM)

Python

Structured JSONL audit logging
