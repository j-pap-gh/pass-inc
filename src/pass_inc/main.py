from fastapi import FastAPI

from .api.routes_auth import router as auth_router
from .api.routes_income import router as income_router
from .api.routes_recommendations import router as recommendations_router
from .config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    @app.get("/health", tags=["health"])
    def health():
        return {"status": "ok", "environment": settings.environment}

    app.include_router(auth_router)
    app.include_router(income_router)
    app.include_router(recommendations_router)

    return app


app = create_app()
