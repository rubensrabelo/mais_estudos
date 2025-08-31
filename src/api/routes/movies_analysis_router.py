from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from api.services import movies_analysis_service

router = APIRouter()


@router.get("/plot/correlations")
def get_heatmap():
    buf = movies_analysis_service.plot_corr_heatmap()
    return StreamingResponse(buf, media_type="image/png")


@router.get("/plot/imbd_vs_gross")
def plot_imbd_vs_gross():
    buf = movies_analysis_service.plot_imbd_vs_gross()
    return StreamingResponse(buf, media_type="image/png")


@router.get("/plot/genres")
def plot_genres():
    buf = movies_analysis_service.plot_genres()
    return StreamingResponse(buf, media_type="image/png")
