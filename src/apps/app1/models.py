from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from conf.database import get_db
from ..app1 import app

Base = declarative_base()
db = get_db()

class User(Base):
    __tablename__ = f"{app.app_name}_users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String)
    first_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = f"{app.app_name}_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=False)
    owner_id = Column(Integer, ForeignKey(User.id))

    owner = relationship("User", back_populates="items")
