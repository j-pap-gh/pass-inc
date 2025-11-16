from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session

from .config import settings


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""


engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if settings.database_url.startswith("sqlite") else {},
)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def get_db():
    """
    FastAPI dependency that provides a DB session and ensures it's closed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Create database tables.
    Call this manually (e.g. via a one-off script) when you change models.
    """
    from . import db_models  # noqa - ensure models are imported

    Base.metadata.create_all(bind=engine)
