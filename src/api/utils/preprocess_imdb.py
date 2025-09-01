import pandas as pd
import numpy as np


def preprocess_imdb(df: pd.DataFrame, top_genres: int = 5) -> pd.DataFrame:
    """
    Pré-processa o dataset para previsão de IMDB Rating.
    """
    df = df.copy()

    df["Gross"] = df["Gross"].replace(r"[\$,]", "", regex=True).astype(float)
    df["Gross_log"] = np.log1p(df["Gross"])
    df["No_of_Votes_log"] = np.log1p(df["No_of_Votes"])

    df["Runtime_min"] = df["Runtime"].str.extract(r"(\d+)").astype(float)

    df = pd.get_dummies(df, columns=["Certificate"], prefix="cert")

    top_genres_list = (
        df["Genre_list"]
        .explode()
        .value_counts()
        .nlargest(top_genres).index.tolist()
    )
    for genre in top_genres_list:
        df[f"genre_{genre}"] = (
            df["Genre_list"].apply(lambda x: int(genre in x))
        )

    return df
