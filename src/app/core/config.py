from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global Application Settings Management Engine.

    Automatically loads environment variables from a local .env file
    and enforces strict type-safe boundaries for configuration items.
    """
    # Application Configuration Fields
    PROJECT_NAME: str = "Automated Business Auditor"
    ENVIRONMENT_TIER: Literal["development",
                              "staging", "production"] = "development"

    # Securely point Pydantic to read from local root .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Gracefully ignores unmapped environment flags
    )

# Instantiate a single-source-of-truth settings instance to import across the project
settings = Settings()

