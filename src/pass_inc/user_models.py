from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr
from typing import Optional

class PlanType(str, Enum):
    FREE = "free"
    PRO = "pro"


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    plan: PlanType
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

from typing import Optional  # make sure this import exists near the top

class TokenData(BaseModel):
    user_id: Optional[int] = None
