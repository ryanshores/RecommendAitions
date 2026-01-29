import os
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"),
        env_file_encoding='utf-8',
        extra='ignore'
    )

    TMDB_API_KEY: SecretStr
    TMDB_BASE_URL: str = "https://api.themoviedb.org/3/"
    OLLAMA_URL: str = "http://localhost:11434/api/chat"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3600


settings = Settings()