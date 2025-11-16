
from sqlalchemy import Column, Integer, String, Text, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)

class Idea(Base):
    __tablename__ = "ideas"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    category = Column(String, nullable=True)
    difficulty = Column(String, nullable=True)

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    summary = Column(Text)
    capital = Column(String)
    timeframe = Column(String)
    risk = Column(String)
    details = Column(Text)
    steps = Column(Text)  # JSON stored as string
