from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..auth import authenticate_user, get_password_hash
from ..auth.utils import create_access_token, create_refresh_token, decode_refresh_token
from ..auth.schemas import Token, TokenRefreshRequest
from ..db import get_db
from ..db_user_models import UserDB, PlanType
from ..user_models import UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def signup(payload: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    # Check if user already exists
    existing = db.query(UserDB).filter(UserDB.email == payload.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed_password = get_password_hash(payload.password)
    db_user = UserDB(
        email=payload.email,
        username=payload.username or payload.email,
        hashed_password=hashed_password,
        plan=PlanType.free,
        is_active=True,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserRead.model_validate(db_user)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    claims = {"sub": str(user.id)}
    access_token = create_access_token(claims)
    refresh_token = create_refresh_token(claims)
    return Token(access_token=access_token, refresh_token=refresh_token)

@router.post("/refresh", response_model=Token)
def refresh(payload: TokenRefreshRequest) -> Token:
    try:
        decoded = decode_refresh_token(payload.refresh_token)
        user_id = decoded.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        claims = {"sub": user_id}
        access_token = create_access_token(claims)
        refresh_token = create_refresh_token(claims)
        return Token(access_token=access_token, refresh_token=refresh_token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired or invalid refresh token")
