from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from api.services import movies_analysis_service

router = APIRouter()


@router.get("/plot/correlations", response_class=StreamingResponse)
def get_heatmap() -> StreamingResponse:
    buf = movies_analysis_service.plot_corr_heatmap()
    return StreamingResponse(buf, media_type="image/png")


@router.get("/plot/imbd_vs_gross", response_class=StreamingResponse)
def plot_imbd_vs_gross() -> StreamingResponse:
    buf = movies_analysis_service.plot_imbd_vs_gross()
    return StreamingResponse(buf, media_type="image/png")


@router.get("/plot/genres", response_class=StreamingResponse)
def plot_genres() -> StreamingResponse:
    buf = movies_analysis_service.plot_genres()
    return StreamingResponse(buf, media_type="image/png")
