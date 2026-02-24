from datetime import datetime


def calculate_fraud_risk(expense: dict) -> dict:
    risk_score = 0.0

    # High amount risk
    if expense["amount"] > 1000:
        risk_score += 0.3

    # Weekend submission risk
    expense_date = datetime.strptime(str(expense["date"]), "%Y-%m-%d")
    if expense_date.weekday() >= 5:
        risk_score += 0.2

    # Suspicious keywords
    suspicious_keywords = ["crypto", "reimbursement", "personal", "cash"]
    description = expense["description"].lower()

    for word in suspicious_keywords:
        if word in description:
            risk_score += 0.2
            break

    # Cap at 1.0
    risk_score = min(risk_score, 1.0)

    if risk_score >= 0.7:
        level = "high"
    elif risk_score >= 0.4:
        level = "medium"
    else:
        level = "low"

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": level
    }
