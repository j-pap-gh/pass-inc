from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class IncomeType(str, Enum):
    DIVIDEND = "dividend"
    RENTAL = "rental"
    ROYALTY = "royalty"
    INTEREST = "interest"
    BUSINESS = "business"
    OTHER = "other"


class IncomeStreamBase(BaseModel):
    name: str
    income_type: IncomeType
    amount_per_period: float = Field(..., ge=0.0)
    period: str = "monthly"
    currency: str = "USD"
    start_date: Optional[date] = None
    notes: Optional[str] = None


class IncomeStreamCreate(IncomeStreamBase):
    pass


class IncomeStream(IncomeStreamBase):
    id: int = Field(..., description="Unique ID of the income stream")

    class Config:
        from_attributes = True  # allows .from_orm / from SQLAlchemy objects


class IncomeSummary(BaseModel):
    total_monthly: float
    total_yearly: float
    currency: str = "USD"


class Recommendation(BaseModel):
    title: str
    description: str
    difficulty: str
    estimated_monthly: float
    category: str
    paywalled: bool = False
