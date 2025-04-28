from typing import Annotated

from fastapi import APIRouter, Path

from models.category import CategoryModel, CreateCategoryModel

router = APIRouter(prefix="/category", tags=["Категория"])


@router.get("/", summary="Список категорий", description="Получение списка категорий")
async def list_category() -> list[CategoryModel]: ...


@router.post("/", summary="Создание категории", description="Создание записи категории")
async def create_category(data: CreateCategoryModel) -> CategoryModel: ...


@router.patch(
    "/{category_id}",
    summary="Обновление категории",
    description="Обновление записи категории",
)
async def update_category(
    category_id: Annotated[int, Path(title="Идентификатор категории")],
    data: CreateCategoryModel,
) -> CategoryModel: ...


@router.delete("/{category_id}")
async def delete_category(
    category_id: Annotated[int, Path(title="Идентификатор категории")],
): ...
