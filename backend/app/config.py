import os
from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

class AuthSettings(BaseModel):
    key: SecretStr | None = None
    expire_in_minutes: int = 30

class TMDBSettings(BaseModel):
    api_key: SecretStr | None = None
    base_url: str = "https://api.themoviedb.org/3/"

class OllamaSettings(BaseModel):
    url: str = "http://localhost:11434/api/chat"

class Settings(BaseSettings):
    tmdb: TMDBSettings = TMDBSettings()
    ollama: OllamaSettings = OllamaSettings()
    auth: AuthSettings = AuthSettings()

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra='ignore',
        env_nested_delimiter="__",
    )


settings = Settings()