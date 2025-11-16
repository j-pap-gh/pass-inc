from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Passive Income Tracker"
    environment: str = "development"
    debug: bool = True

    # Placeholder for future configuration
    # database_url: str = "sqlite:///./pass_inc.db"
    # openai_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
