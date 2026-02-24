def plan_actions(expense: dict) -> dict:
    actions = []

    # Always retrieve if description contains financial keywords
    if any(word in expense["description"].lower() for word in ["crypto", "stocks", "investment", "refund", "travel"]):
        actions.append("retrieve_policies")

    # If amount very high, prioritize fraud analysis
    if expense["amount"] > 5000:
        actions.append("high_priority_fraud_check")

    # Always run compliance reasoning
    actions.append("compliance_reasoning")

    return {"planned_actions": actions}