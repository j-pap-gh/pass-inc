from typing import List

from sqlalchemy.orm import Session

from .db_models import IncomeStreamDB
from .models import IncomeStream, IncomeStreamCreate


class IncomeRepository:
    """Database-backed repository using SQLAlchemy."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def list_streams(self) -> List[IncomeStream]:
        records = self.db.query(IncomeStreamDB).all()
        return [IncomeStream.model_validate(r) for r in records]

    def add_stream(self, payload: IncomeStreamCreate) -> IncomeStream:
        record = IncomeStreamDB(
            name=payload.name,
            income_type=payload.income_type,
            amount_per_period=payload.amount_per_period,
            period=payload.period,
            currency=payload.currency,
            start_date=payload.start_date,
            notes=payload.notes,
        )
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return IncomeStream.model_validate(record)

    def delete_stream(self, stream_id: int) -> None:
        record = self.db.query(IncomeStreamDB).filter(IncomeStreamDB.id == stream_id).first()
        if not record:
            raise KeyError(f"Income stream {stream_id} not found")
        self.db.delete(record)
        self.db.commit()
