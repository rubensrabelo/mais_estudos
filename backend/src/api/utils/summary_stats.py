import pandas as pd


def summary_stats(df: pd.DataFrame) -> dict:
    return {
        "count": len(df),
        "gross_mean": float(df["Gross"].mean()),
        "rating_mean": float(df["IMDB_Rating"].mean()),
        "meta_mean": float(df["Meta_score"].mean()),
        "top_director": df["Director"].value_counts().idxmax()
    }
