from pydantic import BaseModel
from datetime import date
from typing import Optional


class ExpenseRequest(BaseModel):
    employee_id: str
    amount: float
    category: str
    description: str
    date: date
    receipt_text: Optional[str] = None
