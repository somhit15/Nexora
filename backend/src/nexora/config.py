from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Nexora"
    environment: str = "dev"
    log_level: str = "INFO"

    database_url: str = Field(
        default="", description="Database URL for connecting to the database"
    )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
