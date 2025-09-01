import pandas as pd

from api.repositories import df
from api.utils import add_global_ranking


def recommend_movie():
    """Retorna o melhor filme pelo ranking global."""
    df_ranked = add_global_ranking(df)
    best_movie = df_ranked.sort_values("Global_Score").iloc[0]

    return {
        "title": best_movie["Series_Title"],
        "year": int(best_movie["Released_Year"]),
        "imdb": best_movie["IMDB_Rating"],
        "meta_score": (
            float(best_movie["Meta_score"])
            if not pd.isna(best_movie["Meta_score"]) else None
        ),
        "votes": int(best_movie["No_of_Votes"]),
        "gross": float(best_movie["Gross"]),
    }


def top10_movies():
    """
    Retorna os top 10 filmes pelo ranking global, ordenados por IMDB Rating.
    """
    df_ranked = add_global_ranking(df)

    top10 = df_ranked.sort_values("Global_Score").head(10)
    # top10 = top10.sort_values("IMDB_Rating", ascending=False)

    return [
        {
            "title": row["Series_Title"],
            "year": int(row["Released_Year"]),
            "imdb": row["IMDB_Rating"],
            "meta_score": (
                float(row["Meta_score"])
                if not pd.isna(row["Meta_score"]) else None
            ),
            "votes": int(row["No_of_Votes"]),
            "gross": float(row["Gross"]),
            "global_score": float(row["Global_Score"])
        }
        for _, row in top10.iterrows()
    ]
