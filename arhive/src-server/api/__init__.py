from fastapi import APIRouter

from .budget import router as budget_router
from .category import router as category_router
from .debt import router as debt_router
from .goal import router as goal_router
from .user import router as user_router

api_router = APIRouter(prefix="/api")

api_router.include_router(user_router)
api_router.include_router(budget_router)
api_router.include_router(goal_router)
api_router.include_router(category_router)
api_router.include_router(debt_router)
