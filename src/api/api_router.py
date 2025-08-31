from fastapi import APIRouter

from .routes import infor_router
from .routes import analysis_router

api_router = APIRouter()

api_router.include_router(
    infor_router,
    prefix="/info",
    tags=["Movies Info"]
)

api_router.include_router(
    analysis_router,
    prefix="/analysis/plot",
    tags=["Movies Analysis"]
)
