from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Passive Income Tracker"
    environment: str = "development"
    debug: bool = True

    # SQLite database in the repo directory by default
    database_url: str = "sqlite:///./pass_inc.db"

    class Config:
        env_file = ".env"


settings = Settings()
