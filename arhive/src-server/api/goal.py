from typing import Annotated

from fastapi import APIRouter, Path

from models.goal import (
    CreateGoalModel,
    CreateIncomeGoalModel,
    GoalModel,
    IncomeGoalModel,
)

router = APIRouter(prefix="/goal", tags=["Финансовые цели"])


@router.get("/", summary="Список целей", description="Получение списка целей")
def list_goal() -> list[GoalModel]: ...


@router.post("/", summary="Создание цели", description="Создание записи цели")
def create_goal(data: CreateGoalModel): ...


@router.patch(
    "/{goal_id}", summary="Обновление цели", description="Обновление записи цели"
)
def update_goal(
    goal_id: Annotated[int, Path(title="Идентификатор финансовой цели")],
    data: CreateGoalModel,
) -> GoalModel: ...


@router.delete(
    "/{goal_id}", summary="Удаление цели", description="Удаление записи цели"
)
def delete_goal(
    goal_id: Annotated[int, Path(title="Идентификатор финансовой цели")],
): ...


@router.get("/{goal_id}/income", summary="Список пополнений цели")
def list_income(
    goal_id: Annotated[int, Path(title="Идентификатор финансовой цели")],
) -> list[IncomeGoalModel]: ...


@router.post("/{goal_id}/income", summary="Создание пополнения цели")
def create_income(
    goal_id: Annotated[int, Path(title="Идентификатор финансовой цели")],
    data: CreateIncomeGoalModel,
) -> IncomeGoalModel: ...


@router.delete("/{goal_id}/income", summary="Удалить пополнения цели")
def delete_income(
    goal_id: Annotated[int, Path(title="Идентификатор финансовой цели")],
): ...


@router.patch("/{goal_id}/{income_id}/execute", summary="Выполнить пополнение цели")
def execution_income(
    goal_id: Annotated[int, Path(title="Идентификатор финансовой цели")],
    income_id: Annotated[int, Path(title="Идентификатор транзакции")],
) -> IncomeGoalModel: ...


@router.patch(
    "/{goal_id}/{income_id}/cancel", summary="Отмена транзакции пополнения цели"
)
def cancel_income(
    goal_id: Annotated[int, Path(title="Идентификатор финансовой цели")],
    income_id: Annotated[int, Path(title="Идентификатор транзакции")],
) -> IncomeGoalModel: ...
