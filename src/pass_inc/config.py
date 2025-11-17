from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Passive Income Tracker"
    environment: str = "development"
    debug: bool = True

    # SQLite database in the repo directory by default
    database_url: str = "sqlite:///./pass_inc.db"

    # JWT / auth configuration
    secret_key: str = "change-me-in-production"  # used by auth.py
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
