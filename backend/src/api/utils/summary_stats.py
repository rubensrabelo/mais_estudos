import pandas as pd


def summary_stats(df: pd.DataFrame) -> dict:
    """
    Retorna estatísticas resumidas do DataFrame de filmes, incluindo
    medidas descritivas, destaques e apenas colunas com valores ausentes
    (ordenadas em ordem decrescente).
    """
    missing = df.isna().sum()
    missing = missing[missing > 100].sort_values(ascending=False).to_dict()

    stats = {
        "count": len(df),
        "missing_values": missing,
        "gross": {
            "mean": float(df["Gross"].mean()),
            "median": float(df["Gross"].median()),
            "std": float(df["Gross"].std()),
            "min": float(df["Gross"].min()),
            "max": float(df["Gross"].max()),
            "top_movie": df.loc[df["Gross"].idxmax(), "Series_Title"],
        },
        "imdb_rating": {
            "mean": float(df["IMDB_Rating"].mean()),
            "median": float(df["IMDB_Rating"].median()),
            "std": float(df["IMDB_Rating"].std()),
            "top_movie": df.loc[df["IMDB_Rating"].idxmax(), "Series_Title"],
        },
        "meta_score": {
            "mean": float(df["Meta_score"].mean()),
            "median": float(df["Meta_score"].median()),
            "std": float(df["Meta_score"].std()),
            "top_movie": df.loc[df["Meta_score"].idxmax(), "Series_Title"],
        },
        "directors": {
            "unique_count": df["Director"].nunique(),
            "top_director": df["Director"].value_counts().idxmax(),
            "top_director_count": int(df["Director"].value_counts().max()),
        },
    }

    if "Released_Year" in df.columns:
        top_year = df["Released_Year"].value_counts().idxmax()
        stats["years"] = {
            "min": int(df["Released_Year"].min()),
            "max": int(df["Released_Year"].max()),
            "most_common_year": int(top_year),
            "most_common_year_count": int(
                df["Released_Year"].value_counts().max()
            ),
        }

    return stats
