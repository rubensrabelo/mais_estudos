from fastapi import APIRouter
from pydantic import BaseModel

from api.repositories import df, df_test
from api.services.movies_imdb_rating_service import (
    predict_movie, load_model, preprocess_imdb
)
from api.services.movies_imdb_rating_service import evaluate_model_performance 

router = APIRouter()

model = load_model()
df_ref = preprocess_imdb(df)
df_ref_test = preprocess_imdb(df_test)


class MovieInput(BaseModel):
    Series_Title: str
    Released_Year: str
    Certificate: str
    Runtime: str
    Genre: str
    Overview: str
    Meta_score: float
    Director: str
    Star1: str
    Star2: str
    Star3: str
    Star4: str
    No_of_Votes: int
    Gross: str


@router.get("/metrics", response_model=dict)
def get_model_metrics() -> dict:
    """
    Retorna métricas de performance do modelo.
    """
    rmse, mae, r2 = evaluate_model_performance(model, df_ref_test)

    return {
        "RMSE": rmse,
        "MAE": mae,
        "R2": r2
    }


@router.post("/predict", response_model=dict)
def predict_imdb(movie: MovieInput) -> dict:
    movie_dict = movie.model_dump()
    prediction = predict_movie(movie_dict, model=model, df_ref=df_ref)
    return {"IMDB_Prediction": prediction}
