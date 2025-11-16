
from sqlalchemy.orm import Session
from app.models import Idea
from app.schemas.ideas import IdeaCreate

class IdeasService:
    def __init__(self, db: Session):
        self.db = db

    def list_ideas(self):
        return self.db.query(Idea).all()

    def admin_list_ideas(self):
        return self.db.query(Idea).all()

    def create_idea(self, payload: IdeaCreate):
        idea = Idea(
            title=payload.title,
            description=payload.description
        )
        self.db.add(idea)
        self.db.commit()
        self.db.refresh(idea)
        return idea
