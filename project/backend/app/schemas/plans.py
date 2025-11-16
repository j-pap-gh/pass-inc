
from pydantic import BaseModel
from typing import List, Optional

class PlanBase(BaseModel):
    title: str
    summary: str
    capital: str
    timeframe: str
    risk: str
    details: Optional[str] = None
    steps: List[str] = []

class PlanCreate(PlanBase):
    pass

class PlanResponse(PlanBase):
    id: int

    class Config:
        orm_mode = True
