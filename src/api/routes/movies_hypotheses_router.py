from fastapi import APIRouter

from api.services import movies_hypotheses_service as service

router = APIRouter()


@router.get("/genre_vs_gross", response_model=dict)
def genre_vs_gross() -> dict:
    result = service.genre_vs_gross()
    return result


@router.get("/runtime_vs_rating", response_model=dict)
def runtime_vs_rating() -> dict:
    result = service.runtime_vs_rating()
    return result


@router.get("/votes_vs_gross", response_model=dict)
def votes_vs_gross() -> dict:
    result = service.votes_vs_gross()
    return result


@router.get("/year_vs_success", response_model=dict)
def year_vs_success() -> dict:
    result = service.year_vs_success()
    return result
