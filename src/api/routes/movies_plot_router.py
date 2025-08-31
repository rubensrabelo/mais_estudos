from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from api.services import movies_plot_service

router = APIRouter()


@router.get("/correlations", response_class=StreamingResponse)
def get_heatmap() -> StreamingResponse:
    buf = movies_plot_service.plot_corr_heatmap()
    return StreamingResponse(buf, media_type="image/png")


@router.get("/imbd_vs_gross", response_class=StreamingResponse)
def plot_imbd_vs_gross() -> StreamingResponse:
    buf = movies_plot_service.plot_imbd_vs_gross()
    return StreamingResponse(buf, media_type="image/png")


@router.get("/genres", response_class=StreamingResponse)
def plot_genres() -> StreamingResponse:
    buf = movies_plot_service.plot_genres()
    return StreamingResponse(buf, media_type="image/png")


@router.get("/histogram/{column}", response_class=StreamingResponse)
def histogram(column: str) -> StreamingResponse:
    """
    Histograma para variáveis numéricas:
    - IMDB_Rating
    - Gross
    - No_of_Votes
    - Runtime_min
    """
    buf = movies_plot_service.plot_histogram(column)
    return StreamingResponse(buf, media_type="image/png")
