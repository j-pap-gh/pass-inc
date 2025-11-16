from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Recommendation
from ..repository import IncomeRepository
from ..services import baseline_recommendations

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

DUMMY_USER_ID = 1  # TODO: replace with real current_user.id


@router.get("/", response_model=List[Recommendation])
def get_recommendations(
    include_paywalled: bool = Query(False),
    db: Session = Depends(get_db),
) -> List[Recommendation]:
    repo = IncomeRepository(db, user_id=DUMMY_USER_ID)
    streams = repo.list_streams()
    recs = baseline_recommendations(streams)

    if not include_paywalled:
        recs = [r for r in recs if not r.paywalled]

    return recs


@router.get("/paywalled-preview", response_model=Optional[Recommendation])
def get_paywalled_preview(db: Session = Depends(get_db)) -> Optional[Recommendation]:
    repo = IncomeRepository(db, user_id=DUMMY_USER_ID)
    streams = repo.list_streams()
    recs = baseline_recommendations(streams)
    paywalled = [r for r in recs if r.paywalled]
    return paywalled[0] if paywalled else None
