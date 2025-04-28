from fastapi import APIRouter

from models.user import UserModel

router = APIRouter(prefix="/user", tags=["Пользователи"])


@router.get("/current", summary="Текущий пользователь")
def get_user() -> UserModel: ...
