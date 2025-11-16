from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..auth import get_current_user
from ..db import get_db
from ..models import Recommendation
from ..repository import IncomeRepository
from ..services import baseline_recommendations
from ..user_models import UserRead

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.get("/", response_model=List[Recommendation])
def get_recommendations(
    include_paywalled: bool = Query(False),
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> List[Recommendation]:
    repo = IncomeRepository(db, user_id=current_user.id)
    streams = repo.list_streams()
    recs = baseline_recommendations(streams)

    # NOTE: plan awareness will come in Stage 3
    if not include_paywalled:
        recs = [r for r in recs if not r.paywalled]

    return recs


@router.get("/paywalled-preview", response_model=Optional[Recommendation])
def get_paywalled_preview(
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
) -> Optional[Recommendation]:
    repo = IncomeRepository(db, user_id=current_user.id)
    streams = repo.list_streams()
    recs = baseline_recommendations(streams)
    paywalled = [r for r in recs if r.paywalled]
    return paywalled[0] if paywalled else None
