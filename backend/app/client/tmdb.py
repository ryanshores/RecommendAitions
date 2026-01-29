import requests

from backend.app.config import settings

BASE_URL = settings.TMDB_BASE_URL
API_KEY = settings.TMDB_API_KEY

def get_trending(media_type: str = "all", time_window: str = "week"):
    url = f"{BASE_URL}trending/{media_type}/{time_window}"
    params = {"api_key": API_KEY.get_secret_value()}
    return requests.get(url, params=params).json()["results"]