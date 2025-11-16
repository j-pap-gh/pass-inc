
import stripe
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.config import settings
from app.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscriptionService:
    def __init__(self, db: Session):
        self.db = db

    def start_checkout(self, user: User):
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            success_url="http://localhost:5173/premium-success",
            cancel_url="http://localhost:5173/upgrade",
            line_items=[{
                "price": settings.PREMIUM_PRICE_ID,
                "quantity": 1
            }],
            client_reference_id=str(user.id)
        )
        return {"checkout_url": session.url}

    def webhook(self, payload: bytes, sig_header: str):
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except Exception as e:
            raise HTTPException(400, f"Webhook error: {str(e)}")

        if event["type"] == "checkout.session.completed":
            user_id = int(event["data"]["object"]["client_reference_id"])
            user = self.db.query(User).filter(User.id == user_id).first()
            if user:
                user.is_premium = True
                self.db.commit()

        return {"status": "ok"}
