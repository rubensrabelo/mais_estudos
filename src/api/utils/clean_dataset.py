import pandas as pd
import numpy as np

from repositories import movie_data


def clean_dataset() -> pd.DataFrame:
    def parse_number(x):
        if pd.isna(x):
            return np.nan
        s = str(x).replace(",", "").strip()

        try:
            return float(s)
        except Exception:
            return np.nan

    movie_data["Gross"] = movie_data["Gross"].apply(parse_number)
    movie_data["No_of_Votes"] = movie_data["No_of_Votes"].apply(parse_number)

    movie_data["Runtime_min"] = (
        movie_data["Runtime"].str.extract(r"(\d+)").astype(float)
    )

    movie_data["IMDB_Rating"] = (
        pd.to_numeric(movie_data["IMDB_Rating"], errors="coerce")
    )
    movie_data["Meta_score"] = (
        pd.to_numeric(movie_data["Meta_score"], errors="coerce")
    )

    return movie_data
