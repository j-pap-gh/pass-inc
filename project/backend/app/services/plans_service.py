
import json
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Plan

class PlansService:
    def __init__(self, db: Session):
        self.db = db

    def list_plans(self, user):
        plans = self.db.query(Plan).all()
        return [
            self._deserialize_plan(p)
            for p in plans
            if user.is_premium or p.risk != "premium"
        ]

    def get_plan(self, plan_id: int, user):
        plan = self.db.query(Plan).filter(Plan.id == plan_id).first()
        if not plan:
            raise HTTPException(404, "Plan not found")
        if plan.risk == "premium" and not user.is_premium:
            raise HTTPException(403, "Premium required")
        return self._deserialize_plan(plan)

    def _deserialize_plan(self, plan: Plan):
        return {
            "id": plan.id,
            "title": plan.title,
            "summary": plan.summary,
            "capital": plan.capital,
            "timeframe": plan.timeframe,
            "risk": plan.risk,
            "details": plan.details,
            "steps": json.loads(plan.steps or "[]")
        }
