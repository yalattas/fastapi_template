from sqlalchemy import Boolean, Column, String, and_
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError
from apps.core.models import Base

from conf.database import get_db
from apps.iam import app

db = get_db()

class User(Base):
    __tablename__ = f"{app.app_name}_users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    #TODO: add regex validation
    is_active = Column(Boolean, default=True)
    def __init__(self, id):
        self.id = id
    def get_or_create_user(self, id):
        return db.query(User).filter(self.id == id).first()
    def save(self) -> None:
        db.add(self)
        db.commit()
    def __str__(self) -> str:
        return self.id

class SessionLog(Base):
    __tablename__ = f"{app.app_name}_session_log"

    session_id = Column(String, primary_key=True)
    client_id = Column(String)
    user_id = Column(String)

    def __str__(self):
        return '{} Logged in at {}'.format(self.session_id, self.created_at)

    def create(self) -> None:
        db.add(self)
        db.commit()

    def save(self) -> None:
        db.merge(self)
        db.commit()

    def exist(self) -> bool:
        record = db.query(SessionLog).filter(self.session_id == self.session_id).first()
        return record is not None