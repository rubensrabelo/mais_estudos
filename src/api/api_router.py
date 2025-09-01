from fastapi import APIRouter

from .routes import infor_router
from .routes import plot_router
from .routes import hypotheses_router
from .routes import recommendation_router
from .routes import gross_analysis
from .routes import overview_analysis

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

api_router.include_router(
    gross_analysis,
    prefix="/gross_analysis",
    tags=["Gross Analysis"]
)

api_router.include_router(
    overview_analysis,
    prefix="/overview_analysis",
    tags=["Overview Analysis"]
)
