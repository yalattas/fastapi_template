from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from conf.database import get_db
from apps.app1 import app
from apps.core.models import Base


db = get_db()

class UserApp1(Base):
    __tablename__ = f"{app.app_name}_users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String)
    first_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    items = relationship("ItemApp1", back_populates="owner")

class ItemApp1(Base):
    __tablename__ = f"{app.app_name}_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=False)
    owner_id = Column(Integer, ForeignKey(UserApp1.id))

    owner = relationship("UserApp1", back_populates="items")
