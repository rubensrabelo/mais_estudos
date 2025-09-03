import pandas as pd


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria novas colunas no DataFrame de filmes com informações de gêneros, ano,
    idade, diretores e indicador de sucesso.
    """
    df["Genre_list"] = (
        df["Genre"].fillna("")
        .apply(lambda s: [g.strip() for g in s.split(",")] if s else [])
    )
    df["n_genres"] = df["Genre_list"].apply(len)
    df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")

    from datetime import datetime
    current_year = datetime.now().year
    df["Age"] = current_year - df["Released_Year"]

    top_directors = df["Director"].value_counts().nlargest(20).index.tolist()
    df["Director_top20"] = (
        df["Director"].apply(lambda x: x if x in top_directors else "other")
    )
    df["Director_freq"] = (
        df["Director"].map(df["Director"].value_counts()).fillna(0)
    )

    df["is_hit"] = (df["Gross"] > df["Gross"].quantile(0.75)).astype(int)

    return df
