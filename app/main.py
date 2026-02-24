from fastapi import FastAPI
from app.schemas import ExpenseRequest
from rag.vector_store import VectorStore
from rag.ingest import load_policies
from agents.generator import generate_compliance_decision
from agents.fraud_scorer import calculate_fraud_risk
from agents.self_evaluator import evaluate_decision
from agents.planner import plan_actions
from agents.audit_logger import log_decision


app = FastAPI(title="Agentic Finance AI")

vector_store = VectorStore()


@app.on_event("startup")
def startup_event():
    policies = load_policies("data/sample_policies.txt")
    vector_store.add_documents(policies)
    print("Policies loaded into vector store.")


@app.get("/")
def root():
    return {"message": "Agentic Finance AI is running"}


@app.post("/submit-expense")
def submit_expense(expense: ExpenseRequest):

    expense_data = expense.dict()

    plan = plan_actions(expense_data)
    actions = plan["planned_actions"]

    retrieved_policies = []
    decision = None
    evaluation = None
    risk = None
    escalated = False
    retry_count = 0
    MAX_RETRIES = 1

    # Step 1 — Retrieval
    if "retrieve_policies" in actions:
        query = f"{expense.description} {expense.category}"
        retrieved_policies = vector_store.search(query)

    # Step 2 — Initial Reasoning
    if "compliance_reasoning" in actions:
        decision = generate_compliance_decision(
            expense_data,
            retrieved_policies
        )

    # Step 3 — Self Evaluation
    if decision:
        evaluation = evaluate_decision(
            expense_data,
            decision,
            retrieved_policies
        )

    # Step 4 — Retry Loop
    if (
        evaluation
        and evaluation.get("needs_retry")
        and retry_count < MAX_RETRIES
    ):
        retry_count += 1

        query = f"{expense.description} {expense.category} compliance violation policy"
        retrieved_policies = vector_store.search(query)

        decision = generate_compliance_decision(
            expense_data,
            retrieved_policies
        )

        evaluation = evaluate_decision(
            expense_data,
            decision,
            retrieved_policies
        )

    # Step 5 — Fraud Risk
    risk = calculate_fraud_risk(expense_data)

    # Step 6 — Escalation
    if (
        (decision and decision["decision"] == "rejected")
        or (risk and risk["risk_level"] == "high")
        or (decision and decision["confidence"] < 0.6)
        or (evaluation and not evaluation.get("grounded", True))
    ):
        escalated = True

    # Step 7 — Audit Logging
    log_decision({
        "expense_input": expense_data,
        "planned_actions": actions,
        "decision": decision,
        "evaluation": evaluation,
        "fraud_risk": risk,
        "retrieved_policies": retrieved_policies,
        "retry_count": retry_count,
        "escalated_for_review": escalated
    })

    return {
        "planned_actions": actions,
        "decision": decision,
        "evaluation": evaluation,
        "fraud_risk": risk,
        "retrieved_policies": retrieved_policies,
        "retry_count": retry_count,
        "escalated_for_review": escalated
    }