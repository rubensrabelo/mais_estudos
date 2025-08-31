from .movies_info_router import router as infor_router
from .movies_analysis_plot_router import router as analysis_router

__all__ = [
    "infor_router",
    "analysis_router",
]
