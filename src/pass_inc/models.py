from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class IncomeType(str, Enum):
    DIVIDEND = "dividend"
    RENTAL = "rental"
    ROYALTY = "royalty"
    INTEREST = "interest"
    BUSINESS = "business"
    OTHER = "other"


class IncomeStream(BaseModel):
    id: int = Field(..., description="Unique ID of the income stream")
    name: str = Field(..., description="Name of the passive income stream")
    income_type: IncomeType
    amount_per_period: float = Field(..., ge=0.0, description="Amount per period")
    period: str = Field(
        "monthly",
        description="Period for this income: daily, weekly, monthly, yearly",
    )
    currency: str = Field("USD", description="Currency code")
    start_date: Optional[date] = None
    notes: Optional[str] = None


class IncomeStreamCreate(BaseModel):
    name: str
    income_type: IncomeType
    amount_per_period: float = Field(..., ge=0.0)
    period: str = "monthly"
    currency: str = "USD"
    start_date: Optional[date] = None
    notes: Optional[str] = None


class IncomeSummary(BaseModel):
    total_monthly: float
    total_yearly: float
    currency: str = "USD"


class Recommendation(BaseModel):
    title: str
    description: str
    difficulty: str  # e.g. "beginner", "intermediate", "advanced"
    estimated_monthly: float
    category: str  # e.g. "digital products", "investing", etc.
    paywalled: bool = False
