from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.services import movies_info_service

router = APIRouter()


@router.get("/summary", response_model=dict)
def get_summary() -> dict:
    stats = movies_info_service.get_summary()
    return JSONResponse(content=stats)


@router.get("/correlations", response_model=dict)
def get_corr() -> dict:
    corr = movies_info_service.get_correlations()
    return JSONResponse(content=corr.to_dict())
