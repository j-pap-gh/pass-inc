from typing import List, Optional

from fastapi import APIRouter, Query

from ..models import Recommendation
from ..repository import income_repo
from ..services import baseline_recommendations

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.get("/", response_model=List[Recommendation])
def get_recommendations(include_paywalled: bool = Query(False)) -> List[Recommendation]:
    streams = income_repo.list_streams()
    recs = baseline_recommendations(streams)

    if not include_paywalled:
        recs = [r for r in recs if not r.paywalled]

    return recs


@router.get("/paywalled-preview", response_model=Optional[Recommendation])
def get_paywalled_preview() -> Optional[Recommendation]:
    """
    Example endpoint: show a single blurred/preview recommendation
    to tease premium features.
    """
    streams = income_repo.list_streams()
    recs = baseline_recommendations(streams)
    paywalled = [r for r in recs if r.paywalled]
    return paywalled[0] if paywalled else None
