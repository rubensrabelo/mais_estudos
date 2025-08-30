import os
import pandas as pd

from .preprocessing import load_and_clean_dataset, feature_engineering

CSV_FILE = os.path.join("data", "desafio_indicium_imdb.csv")

_movie_data = None


def get_dataset() -> pd.DataFrame:
    global _movie_data
    if _movie_data is None:
        df = load_and_clean_dataset(CSV_FILE)
        df = feature_engineering(df)
        _movie_data = df
    return _movie_data.copy()
