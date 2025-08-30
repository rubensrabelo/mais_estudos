from api.repositories import get_dataset
from api.utils import summary_stats, correlations

df = get_dataset()


def get_summary():
    return summary_stats(df)


def get_correlations():
    return correlations(df)
