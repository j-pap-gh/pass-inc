from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application configuration."""
    app_name: str = "Passive Income Tracker"
    environment: str = "development"
    debug: bool = True

    # SQLite database in the repo directory by default
    database_url: str = "sqlite:///./pass_inc.db"

    # JWT / auth configuration
    secret_key: str  # required, loaded from environment
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # Refresh token configuration
    refresh_secret_key: str  # required, loaded from environment
    refresh_token_expire_days: int = 7

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
