import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"


def generate_compliance_decision(expense_data: dict, retrieved_policies: list[str]):

    prompt = f"""
You are a financial compliance AI assistant.

Expense Details:
Employee ID: {expense_data['employee_id']}
Amount: {expense_data['amount']}
Category: {expense_data['category']}
Description: {expense_data['description']}

Relevant Policies:
{chr(10).join(retrieved_policies)}

Respond STRICTLY in JSON:
{{
  "decision": "approved | flagged | rejected",
  "reasoning": "...",
  "confidence": 0.0-1.0
}}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        result = response.json()
        raw_output = result.get("response", "").strip()

        return json.loads(raw_output)

    except Exception:
        return {
            "decision": "flagged",
            "reasoning": "LLM failure fallback triggered.",
            "confidence": 0.3
        }