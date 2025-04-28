from typing import Annotated

from fastapi import APIRouter, Path

from models.dept import CreateDeptModel, DeptModel

router = APIRouter(prefix="/dept", tags=["Долги"])  # Долги


@router.get("/", description="Получение списка долгов", summary="Список долгов")
def list_dept() -> list[DeptModel]: ...


@router.post("/", description="Создание долга", summary="Создание долга")
def create_dept(data: CreateDeptModel) -> DeptModel: ...


@router.patch("/", description="Обновление записи долга", summary="Обновление долга")
def update_dept(data: CreateDeptModel) -> DeptModel: ...


@router.delete(
    "/{dept_id}", summary="Удаление долга", description="Удаление записи долга"
)
def delete_dept(
    category_id: Annotated[int, Path(title="Идентификатор долга")],
): ...
