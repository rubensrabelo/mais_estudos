import pandas as pd


def process_movie_data(movie: dict) -> dict:
    """
    Extrai apenas as colunas de interesse do JSON retornado pela API.
    """
    if not movie:
        return None

    return {
        "Series_Title": movie.get("Title"),
        "Released_Year": movie.get("Year"),
        "Certificate": movie.get("Rated"),
        "Runtime": movie.get("Runtime"),
        "Genre": movie.get("Genre"),
        "IMDB_Rating": movie.get("imdbRating"),
        "Overview": movie.get("Plot"),
        "Meta_score": movie.get("Metascore"),
        "Director": movie.get("Director"),
        "Stars": movie.get("Actors"),
        "No_of_Votes": movie.get("imdbVotes"),
        "Gross": movie.get("BoxOffice"),
    }


def create_dataframe(movies: list[dict]) -> pd.DataFrame:
    """
    Cria um DataFrame a partir de uma lista de dicionários.
    """
    return pd.DataFrame(movies)
