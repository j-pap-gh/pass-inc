from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr


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


class TokenData(BaseModel):
    user_id: int | None = None
