
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.ideas_service import IdeasService

router = APIRouter()

@router.get("/")
def list_public_ideas(db: Session = Depends(get_db)):
    return IdeasService(db).list_ideas()
