from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from conf.database import get_db, SessionLocal
from ..iam import app

Base = declarative_base()
db = get_db()

class User(Base):
    __tablename__ = f"{app.app_name}_users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    #TODO: add regex validation
    is_active = Column(Boolean, default=True)

class SessionLog(Base):
    __tablename__ = f"{app.app_name}_session_log"

    session_id = Column(String, primary_key=True)
    client_id = Column(String)
    user_id = Column(String, ForeignKey(User.id))

    def save(self) -> None:
        session = SessionLocal()
        session.add(self)
        session.commit()
        session.close()

    def __str__(self):
        return '{} Logged in at {}'.format(self.session_id, self.created_at)