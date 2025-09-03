from fastapi import APIRouter

from api.services import movies_hypotheses_service as service

router = APIRouter()


@router.get("/genre_vs_gross", response_model=dict)
def genre_vs_gross() -> dict:
    """
    Retorna análise da relação entre gêneros de filmes e a variável Gross.
    """
    result = service.genre_vs_gross()
    return result


@router.get("/runtime_vs_rating", response_model=dict)
def runtime_vs_rating() -> dict:
    """
    Retorna análise da relação entre duração do filme e avaliação no IMDB.
    """
    result = service.runtime_vs_rating()
    return result


@router.get("/votes_vs_gross", response_model=dict)
def votes_vs_gross() -> dict:
    """
    Retorna análise da relação entre número de votos e a variável Gross.
    """
    result = service.votes_vs_gross()
    return result


@router.get("/year_vs_success", response_model=dict)
def year_vs_success() -> dict:
    """
    Retorna análise da relação entre ano de lançamento e sucesso do filme.
    """
    result = service.year_vs_success()
    return result
