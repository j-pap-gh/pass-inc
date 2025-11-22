from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..auth import get_current_user
from ..db import get_db
from ..models import IncomeStream, IncomeStreamCreate, IncomeSummary
from ..repository import IncomeRepository
from ..services import summarize_income
from ..user_models import UserRead

router = APIRouter(prefix="/income", tags=["income"])

@router.get("/", response_model=List[IncomeStream])
def list_income_streams(
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> List[IncomeStream]:
    repo = IncomeRepository(db, user_id=current_user.id)
    return repo.list_streams()

@router.post("/", response_model=IncomeStream, status_code=201)
def create_income_stream(
    payload: IncomeStreamCreate,
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> IncomeStream:
    repo = IncomeRepository(db, user_id=current_user.id)
    return repo.add_stream(payload)

@router.put("/{stream_id}", response_model=IncomeStream)
def update_income_stream(
    stream_id: int,
    payload: IncomeStreamCreate,
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> IncomeStream:
    repo = IncomeRepository(db, user_id=current_user.id)
    try:
        return repo.update_stream(stream_id, payload)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{stream_id}", response_model=IncomeStream)
def partial_update_income_stream(
    stream_id: int,
    payload: IncomeStreamCreate,
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> IncomeStream:
    repo = IncomeRepository(db, user_id=current_user.id)
    try:
        return repo.update_stream(stream_id, payload)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{stream_id}", status_code=204)
def delete_income_stream(
    stream_id: int,
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> None:
    repo = IncomeRepository(db, user_id=current_user.id)
    try:
        repo.delete_stream(stream_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Income stream not found")

@router.get("/summary", response_model=IncomeSummary)
def get_income_summary(
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> IncomeSummary:
    repo = IncomeRepository(db, user_id=current_user.id)
    streams = repo.list_streams()
    return summarize_income(streams)
