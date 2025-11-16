from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import IncomeStream, IncomeStreamCreate, IncomeSummary
from ..repository import IncomeRepository
from ..services import summarize_income

router = APIRouter(prefix="/income", tags=["income"])


@router.get("/", response_model=List[IncomeStream])
def list_income_streams(db: Session = Depends(get_db)) -> List[IncomeStream]:
    repo = IncomeRepository(db)
    return repo.list_streams()


@router.post("/", response_model=IncomeStream, status_code=201)
def create_income_stream(
    payload: IncomeStreamCreate,
    db: Session = Depends(get_db),
) -> IncomeStream:
    repo = IncomeRepository(db)
    return repo.add_stream(payload)


@router.delete("/{stream_id}", status_code=204)
def delete_income_stream(
    stream_id: int,
    db: Session = Depends(get_db),
) -> None:
    repo = IncomeRepository(db)
    try:
        repo.delete_stream(stream_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Income stream not found")


@router.get("/summary", response_model=IncomeSummary)
def get_income_summary(db: Session = Depends(get_db)) -> IncomeSummary:
    repo = IncomeRepository(db)
    streams = repo.list_streams()
    return summarize_income(streams)
