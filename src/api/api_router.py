from fastapi import APIRouter

from .routes import infor_router
from .routes import plot_router
from .routes import hypotheses_router

api_router = APIRouter()

api_router.include_router(
    infor_router,
    prefix="/info",
    tags=["Movies Info"]
)

api_router.include_router(
    plot_router,
    prefix="/plot",
    tags=["Movies Analysis"]
)


api_router.include_router(
    hypotheses_router,
    prefix="/hypotheses",
    tags=["Hypotheses"]
)
