from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class GoalModel(BaseModel):
    id: int
    name: str
    target_amount: float
    current_amount: float
    calculate_amount: float
    deadline: date
    user: int


class CreateGoalModel(BaseModel):
    name: str
    target_amount: int
    current_amount: int
    deadline: date


class IncomeGoalModel(BaseModel):
    id: int
    amount: float
    status: bool
    goal: int
    create_at: datetime
    execution_at: Optional[str] = None


class CreateIncomeGoalModel(BaseModel):
    amount: float
