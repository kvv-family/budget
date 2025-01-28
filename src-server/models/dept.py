from datetime import date

from pydantic import BaseModel


class DeptModel(BaseModel):
    id: int
    description: str
    amount: float
    date: date
    is_credit: bool
    closed: bool


class CreateDeptModel(BaseModel):
    description: str
    amount: float
    date: date
    is_credit: bool
    closed: bool = False