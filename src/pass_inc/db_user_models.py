from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class PlanType(str, Enum):
    FREE = "free"
    PRO = "pro"


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    plan = Column(Enum(PlanType), nullable=False, default=PlanType.FREE)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # relationship to income streams
    income_streams = relationship("IncomeStreamDB", back_populates="owner")
