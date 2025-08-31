from .movies_info_router import router as infor_router
from .movies_plot_router import router as plot_router
from .movies_hypotheses_router import router as hypotheses_router
from .movies_recommendation_router import router as recommendation_router

__all__ = [
    "infor_router",
    "plot_router",
    "hypotheses_router",
    "recommendation_router",
]
