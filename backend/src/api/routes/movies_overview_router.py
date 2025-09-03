from fastapi import APIRouter
from pydantic import BaseModel

from api.services import movies_overview_service as service

router = APIRouter()


class OverviewRequest(BaseModel):
    overview: str


@router.get("/wordcloud/save", response_model=dict)
def wordcloud() -> dict:
    """
    Gera e salva uma wordcloud dos filmes, retornando o caminho do arquivo.
    """
    filepath = service.save_wordcloud()
    return {"message": "Imagem salva com sucesso!", "path": filepath}


@router.get("/top-words", response_model=dict)
def top_words(genre: str, top_n: int = 15) -> dict:
    """
    Retorna as palavras mais frequentes em descrições de filmes de um gênero.
    """
    return service.top_words_by_genre(genre, top_n)


@router.post("/predict-genre", response_model=dict)
def predict_genre(request: OverviewRequest) -> dict:
    """
    Recebe a descrição de um filme e retorna os gêneros mais prováveis.
    """
    return service.predict_genre(request.overview, top_n=5)
