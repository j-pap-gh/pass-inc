
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import require_admin
from app.schemas.ideas import IdeaCreate
from app.services.ideas_service import IdeasService

router = APIRouter()

@router.get("/ideas")
def admin_list(db: Session = Depends(get_db), admin=Depends(require_admin)):
    return IdeasService(db).admin_list_ideas()

@router.post("/ideas")
def admin_add(payload: IdeaCreate, db: Session = Depends(get_db), admin=Depends(require_admin)):
    return IdeasService(db).create_idea(payload)
