from pydantic import BaseModel


class BudgetModel(BaseModel):
    id: int
    month: str
    limit: float
    category: int


class CreateBudgetModel(BaseModel):
    month: str
    limit: float
    category: int