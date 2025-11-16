
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.services.plans_service import PlansService

router = APIRouter()

@router.get("/")
def list_plans(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return PlansService(db).list_plans(user)

@router.get("/{plan_id}")
def get_plan(plan_id: int, user=Depends(get_current_user), db: Session = Depends(get_db)):
    return PlansService(db).get_plan(plan_id, user)
