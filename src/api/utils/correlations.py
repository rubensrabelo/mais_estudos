import pandas as pd


def correlations(df: pd.DataFrame) -> pd.DataFrame:
    num_cols = [
        "Gross",
        "IMDB_Rating",
        "Meta_score",
        "Runtime_min",
        "No_of_Votes",
        "Age",
        "n_genres",
        "Director_freq"
    ]
    return df[num_cols].corr()
