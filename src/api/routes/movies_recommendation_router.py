from fastapi import APIRouter
from api.services import movies_recommendation_service as service

router = APIRouter()


@router.get("/", response_model=dict)
def recommendation_movie() -> dict:
    """Recomenda um filme baseado no equilíbrio entre IMDB + Votes + Gross."""
    return service.recommend_movie()


@router.get("/top10", response_model=list[dict])
def top10_movies() -> list[dict]:
    """Recomenda um filme baseado no equilíbrio entre IMDB + Votes + Gross."""
    return service.top10_movies()
