from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import numpy as np

from api.services.movies_imdb_rating_service import get_features


def evaluate_model_performance(
    model: RandomForestRegressor,
    df_ref: pd.DataFrame
) -> tuple[float, float, float]:
    """
    Calcula métricas de desempenho do modelo em um DataFrame de referência.
    """
    features = get_features(df_ref)
    X = df_ref[features]
    y = df_ref["IMDB_Rating"]

    y_pred = model.predict(X)

    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    return rmse, mae, r2
