import pandas as pd

from api.repositories import df
from api.utils import summary_stats, correlations


def get_summary() -> dict:
    return summary_stats(df)


def get_correlations() -> pd.DataFrame:
    return correlations(df)
