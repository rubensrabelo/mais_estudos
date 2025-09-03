from fastapi import APIRouter
from api.services import movies_plot_service

router = APIRouter()


@router.get("/correlations/save")
def save_heatmap():
    """
    Gera e salva um heatmap de correlação do dataset de filmes.
    """
    filepath = movies_plot_service.plot_corr_heatmap()
    return {"message": "Imagem salva com sucesso!", "path": filepath}


@router.get("/imbd_vs_gross/save")
def save_imbd_vs_gross():
    """
    Gera e salva um gráfico de dispersão entre IMDB Rating e Gross.
    """
    filepath = movies_plot_service.plot_imbd_vs_gross()
    return {"message": "Imagem salva com sucesso!", "path": filepath}


@router.get("/genres/save")
def save_genres():
    """
    Gera e salva um gráfico de distribuição de filmes por gênero.
    """
    filepath = movies_plot_service.plot_genres()
    return {"message": "Imagem salva com sucesso!", "path": filepath}


@router.get("/histogram/{column}/save")
def save_histogram(column: str):
    """
    Gera e salva um histograma da coluna especificada do dataset.
    """
    filepath = movies_plot_service.plot_histogram(column)
    return {"message": "Imagem salva com sucesso!", "path": filepath}
