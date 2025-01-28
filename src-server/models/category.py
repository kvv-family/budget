from pydantic import BaseModel


class CategoryModel(BaseModel):
    id: int
    name: str
    icon: str
    is_income: bool


class CreateCategoryModel(BaseModel):
    name: str
    icon: str
    is_income: bool