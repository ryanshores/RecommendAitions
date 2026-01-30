import requests

from config import settings

BASE_URL = settings.tmdb.base_url
API_KEY = settings.tmdb.api_key

def get_trending(media_type: str = "all", time_window: str = "week"):
    url = f"{BASE_URL}trending/{media_type}/{time_window}"
    params = {"api_key": API_KEY.get_secret_value()}
    return requests.get(url, params=params).json()["results"]