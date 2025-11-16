
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.logging_config import setup_logging
from app.database import Base, engine

# Routers will be added in Step 2D
# from app.controllers.ideas_controller import router as ideas_router
# from app.controllers.plans_controller import router as plans_router
# from app.controllers.admin_controller import router as admin_router
# from app.controllers.ai_controller import router as ai_router
# from app.controllers.subscription_controller import router as subscription_router

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Passive Income Platform API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # updated to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router registration (enabled in Step 2D)
# app.include_router(ideas_router, prefix="/ideas", tags=["Ideas"])
# app.include_router(plans_router, prefix="/plans", tags=["Plans"])
# app.include_router(admin_router, prefix="/admin", tags=["Admin"])
# app.include_router(ai_router, prefix="/ai", tags=["AI"])
# app.include_router(subscription_router, prefix="/subscribe", tags=["Stripe"])

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "1.0.0"}
