from api.repositories import df
from api.utils import summary_stats, correlations


def get_summary():
    return summary_stats(df)


def get_correlations():
    return correlations(df)
