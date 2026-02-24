import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"


def evaluate_decision(expense_data: dict, decision: dict, policies: list[str]):

    prompt = f"""
You are an AI auditor reviewing a financial compliance decision.

Expense:
{expense_data}

Policies:
{policies}

Decision:
{decision}

Evaluate:
1. Is the reasoning strictly grounded in provided policies?
2. Is there any hallucination?
3. Is the logic consistent?

Respond STRICTLY in JSON:
{{
  "grounded": true/false,
  "reasoning_quality": 0.0-1.0,
  "needs_retry": true/false
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
        # Safe fallback
        return {
            "grounded": False,
            "reasoning_quality": 0.3,
            "needs_retry": False
        }