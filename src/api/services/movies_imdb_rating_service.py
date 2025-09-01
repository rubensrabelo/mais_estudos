import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

from api.repositories import df
from api.utils.preprocess_imdb import preprocess_imdb

MODEL_PATH = "data/imdb_predictor.pkl"


def get_features(df: pd.DataFrame) -> list[str]:
    """
    Retorna a lista de colunas usadas como features no modelo.
    """
    feature_cols = [
        "Meta_score",
        "No_of_Votes_log",
        "Gross_log",
        "Runtime_min",
        "Age"
    ]
    feature_cols += [col for col in df.columns if col.startswith("genre_")]
    feature_cols += [col for col in df.columns if col.startswith("cert_")]
    return feature_cols


def train_model(
        df: pd.DataFrame
) -> tuple[RandomForestRegressor, list[str], float]:
    """
    Treina o Random Forest no dataset e salva o modelo.
    Retorna:
        model: RandomForestRegressor treinado
        features: lista de features usadas
        rmse: raiz do erro quadrático médio no treino
    """
    if df is None:
        df = preprocess_imdb(df)

    features = get_features(df)
    X = df[features]
    y = df["IMDB_Rating"]

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)

    rmse = np.sqrt(mean_squared_error(y, model.predict(X)))
    return model, features, rmse


def load_model() -> RandomForestRegressor:
    """
    Carrega o modelo salvo ou treina se não existir.
    """
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        model, _, _ = train_model(preprocess_imdb(df))
    return model


def predict_movie(
    movie_dict: dict[str, any],
    model: RandomForestRegressor | None = None,
    df_ref: pd.DataFrame | None = None
) -> float:
    """
    Recebe um dicionário de filme e retorna a previsão de IMDB_Rating.
    """
    if model is None:
        model = load_model()

    if df_ref is None:
        df_ref = preprocess_imdb(df)

    features = get_features(df_ref)

    df_new = pd.DataFrame([movie_dict])

    df_new["Gross"] = float(str(movie_dict["Gross"]).replace(",", ""))
    df_new["Gross_log"] = np.log1p(df_new["Gross"])
    df_new["No_of_Votes_log"] = np.log1p(df_new["No_of_Votes"])
    df_new["Runtime_min"] = int(str(movie_dict["Runtime"]).split()[0])
    df_new["Age"] = 2025 - int(movie_dict["Released_Year"])

    for col in [c for c in features if c.startswith("cert_")]:
        df_new[col] = int(col.split("_")[1] == movie_dict["Certificate"])

    genres = movie_dict["Genre"].split(", ")
    for col in [c for c in features if c.startswith("genre_")]:
        genre_name = col.split("_")[1]
        df_new[col] = int(genre_name in genres)

    X_new = df_new[features]
    prediction = float(model.predict(X_new)[0])
    return prediction
