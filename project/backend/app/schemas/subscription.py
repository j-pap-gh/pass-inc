
from pydantic import BaseModel

class CheckoutSession(BaseModel):
    checkout_url: str
