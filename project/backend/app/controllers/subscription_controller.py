
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.services.subscription_service import SubscriptionService

router = APIRouter()

@router.post("/start-checkout")
def start_checkout(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return SubscriptionService(db).start_checkout(user)

@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("Stripe-Signature")
    if not sig_header:
        raise HTTPException(400, "Missing Stripe signature")
    return SubscriptionService(db).webhook(payload, sig_header)
