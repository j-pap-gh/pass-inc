from datetime import date
from typing import Optional

from sqlalchemy import Date, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base
from .db_user_models import UserDB
from .models import IncomeType


class IncomeStreamDB(Base):
    __tablename__ = "income_streams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    income_type: Mapped[IncomeType] = mapped_column(Enum(IncomeType), nullable=False)
    amount_per_period: Mapped[float] = mapped_column(Float, nullable=False)
    period: Mapped[str] = mapped_column(String(32), nullable=False, default="monthly")
    currency: Mapped[str] = mapped_column(String(8), nullable=False, default="USD")
    start_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)

    # new: link to User
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped[UserDB] = relationship("UserDB", back_populates="income_streams")
