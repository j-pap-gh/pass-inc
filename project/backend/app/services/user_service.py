
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import User
from app.utils.security import verify_password, create_jwt

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def authenticate(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(401, "Invalid credentials")
        token = create_jwt({"sub": user.id})
        return {"token": token, "user": user}
