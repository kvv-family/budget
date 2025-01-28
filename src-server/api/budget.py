from typing import Annotated

from fastapi import APIRouter, Path

from models.budget import BudgetModel, CreateBudgetModel

router = APIRouter(prefix="/budget", tags=["Бюджет"])


@router.get("/", summary="Список бюджетов")
def list_budgets() -> list[BudgetModel]:
    return [BudgetModel(id=0, month="test", limit=0.0, category=1)]


@router.post("/", summary="Создание бюджета")
def create_budget(data: CreateBudgetModel) -> BudgetModel: ...


@router.patch("/{budget_id}", summary="Обновление бюджета")
def update_budget(
    budget_id: Annotated[int, Path(title="Идентификатор бюджета")],
    data: CreateBudgetModel,
) -> BudgetModel: ...


@router.delete("/{budget_id}", summary="Удаление бюджета")
def delete_budget(
    budget_id: Annotated[int, Path(title="Идентификатор бюджета")],
): ...
