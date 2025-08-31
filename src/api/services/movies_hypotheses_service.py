import pandas as pd

from api.repositories import df


# Filmes de ação e aventura tendem a ter maiores bilheterias (Gross).
def genre_vs_gross() -> dict:
    genre_gross = (
        df.explode("Genre_list")
        .groupby("Genre_list")["Gross"]
        .median()
        .sort_values(ascending=False)
    )
    return genre_gross.to_dict()


# Filmes com runtime mais longo podem ter avaliações mais altas no IMDB.
def runtime_vs_rating() -> dict:
    corr = df["Runtime_min"].corr(df["IMDB_Rating"], method="spearman")
    return {"spearman_corr": corr}


# Filmes com muitos votos no IMDB tendem a ter maior faturamento.
def votes_vs_gross() -> dict:
    corr = df["No_of_Votes"].corr(df["Gross"], method="spearman")
    return {"spearman_corr": corr}


# O fator "tempo" (idade do filme) pode ser importante: clássicos antigos
# com notas altas ainda geram receita em relançamentos (The Godfather, 1972).
def year_vs_success() -> dict:
    df["Age"] = 2025 - df["Released_Year"]
    decade = (df["Released_Year"] // 10) * 10
    avg_by_decade = (
        df.groupby(decade)["Gross"].median().sort_values(ascending=False)
    )
    result = {}
    for k, v in avg_by_decade.items():
        result[str(k)] = None if pd.isna(v) else float(v)
    return result
