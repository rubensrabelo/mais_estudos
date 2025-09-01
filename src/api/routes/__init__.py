from .movies_info_router import router as infor_router
from .movies_plot_router import router as plot_router
from .movies_hypotheses_router import router as hypotheses_router
from .movies_recommendation_router import router as recommendation_router
from .movies_gross_analysis_router import router as gross_analysis
from .movies_overview_router import router as overview_analysis
from .movies_imdb_rating_router import router as imdb_rating_router

__all__ = [
    "infor_router",
    "plot_router",
    "hypotheses_router",
    "recommendation_router",
    "gross_analysis",
    "overview_analysis",
    "imdb_rating_router",
]
