from fastapi import APIRouter
from api.services import movies_gross_analysis_service as service

router = APIRouter()


@router.get("/correlation")
def gross_correlation():
    return service.gross_correlation()


@router.get("/regression")
def gross_regression():
    return service.gross_regression()


@router.get("/top_categories")
def gross_top_categories():
    return service.gross_top_categories()


@router.get("/all")
def gross_factors_all():
    """Retorna correlação, regressão e top categorias em um único endpoint"""
    return service.gross_factors_all()
