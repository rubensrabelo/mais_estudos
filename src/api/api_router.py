from fastapi import APIRouter

from .routes import infor_router
from .routes import plot_router
from .routes import hypotheses_router
from .routes import recommendation_router

api_router = APIRouter()

api_router.include_router(
    infor_router,
    prefix="/infos",
    tags=["Movies Info"]
)

api_router.include_router(
    plot_router,
    prefix="/plots",
    tags=["Movies Analysis"]
)

api_router.include_router(
    hypotheses_router,
    prefix="/hypotheses",
    tags=["Hypotheses"]
)

api_router.include_router(
    recommendation_router,
    prefix="/recommendations",
    tags=["Recommendation"]
)
