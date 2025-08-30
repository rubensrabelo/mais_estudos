import pandas as pd
import numpy as np


def load_and_clean_dataset(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    def parse_number(x):
        if pd.isna(x):
            return np.nan
        s = str(x).replace(",", "").strip()

        try:
            return float(s)
        except Exception:
            return np.nan

    df["Gross"] = df["Gross"].apply(parse_number)
    df["No_of_Votes"] = df["No_of_Votes"].apply(parse_number)

    df["Runtime_min"] = (
        df["Runtime"].str.extract(r"(\d+)").astype(float)
    )

    df["IMDB_Rating"] = (
        pd.to_numeric(df["IMDB_Rating"], errors="coerce")
    )
    df["Meta_score"] = (
        pd.to_numeric(df["Meta_score"], errors="coerce")
    )

    return df
