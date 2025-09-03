import requests

from ..config import BASE_URL, API_KEY


def fetch_movie(title: str) -> dict:
    """
    Busca dados de um filme pelo título na API do OMDb.
    """
    url = f"{BASE_URL}?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data if data.get("Response") == "True" else None
