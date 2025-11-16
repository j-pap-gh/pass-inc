from typing import List

from fastapi import APIRouter, HTTPException

from ..models import IncomeStream, IncomeStreamCreate, IncomeSummary
from ..repository import income_repo
from ..services import summarize_income

router = APIRouter(prefix="/income", tags=["income"])


@router.get("/", response_model=List[IncomeStream])
def list_income_streams() -> List[IncomeStream]:
    return income_repo.list_streams()


@router.post("/", response_model=IncomeStream, status_code=201)
def create_income_stream(payload: IncomeStreamCreate) -> IncomeStream:
    return income_repo.add_stream(payload)


@router.delete("/{stream_id}", status_code=204)
def delete_income_stream(stream_id: int) -> None:
    try:
        income_repo.delete_stream(stream_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Income stream not found")


@router.get("/summary", response_model=IncomeSummary)
def get_income_summary() -> IncomeSummary:
    streams = income_repo.list_streams()
    return summarize_income(streams)
