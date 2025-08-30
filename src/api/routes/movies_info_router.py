from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.services import movies_info_service

router = APIRouter()


@router.get("/summary")
def get_summary():
    stats = movies_info_service.get_summary()
    return JSONResponse(content=stats)


@router.get("/correlations")
def get_corr():
    corr = movies_info_service.get_correlations()
    return JSONResponse(content=corr.to_dict())
