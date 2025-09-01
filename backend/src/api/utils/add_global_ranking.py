import pandas as pd


def add_global_ranking(df: pd.DataFrame, weights: dict = None) -> pd.DataFrame:
    """
    Adiciona ranking global com possibilidade de pesos.
    """

    # Mais foco na avaliação do público
    if weights is None:
        weights = {"imdb": 2, "votes": 2, "gross": 1, "meta": 1}

    df_ranked = df.copy()
    df_ranked["Rank_IMDB"] = df_ranked["IMDB_Rating"].rank(ascending=False)
    df_ranked["Rank_Votes"] = df_ranked["No_of_Votes"].rank(ascending=False)
    df_ranked["Rank_Gross"] = df_ranked["Gross"].rank(ascending=False)
    df_ranked["Rank_Meta"] = df_ranked["Meta_score"].rank(ascending=False)

    df_ranked["Global_Score"] = (
        df_ranked["Rank_IMDB"] * weights["imdb"]
        + df_ranked["Rank_Votes"] * weights["votes"]
        + df_ranked["Rank_Gross"] * weights["gross"]
        + df_ranked["Rank_Meta"] * weights["meta"]
    )

    return df_ranked
