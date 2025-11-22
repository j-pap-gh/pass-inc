from datetime import datetime, timedelta
from jose import jwt
from src.pass_inc.config import settings


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.refresh_token_expire_days)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.refresh_secret_key, algorithm=settings.algorithm)


def decode_refresh_token(token: str):
    return jwt.decode(token, settings.refresh_secret_key, algorithms=[settings.algorithm])
