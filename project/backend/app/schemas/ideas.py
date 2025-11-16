
from pydantic import BaseModel

class IdeaBase(BaseModel):
    title: str
    description: str

class IdeaCreate(IdeaBase):
    pass

class IdeaResponse(IdeaBase):
    id: int
    category: str | None = None
    difficulty: str | None = None

    class Config:
        orm_mode = True
