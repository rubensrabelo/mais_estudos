import pandas as pd

from api.repositories import df
from api.utils import summary_stats, correlations


def get_summary() -> dict:
    """
    Retorna estatísticas resumidas do dataset de filmes.
    """
    return summary_stats(df)


def get_correlations() -> pd.DataFrame:
    """
    Retorna a matriz de correlação das variáveis numéricas do dataset.
    """
    return correlations(df)
