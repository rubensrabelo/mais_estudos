import os
import pandas as pd

from .preprocessing import load_and_clean_dataset, feature_engineering

CSV_FILE_MODEL = os.path.join("data", "desafio_indicium_imdb.csv")
CSV_FILE_TEST = os.path.join("data", "imdb_movies_for_test.csv")

_movie_data = None


def get_dataset(path: str) -> pd.DataFrame:
    global _movie_data
    if _movie_data is None:
        df = load_and_clean_dataset(path)
        df = feature_engineering(df)
        _movie_data = df
    return _movie_data.copy()


movie_data_model = get_dataset(CSV_FILE_MODEL)
movie_data_test = get_dataset(CSV_FILE_MODEL)
