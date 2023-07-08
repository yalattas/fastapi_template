from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.settings import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_size=5, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()