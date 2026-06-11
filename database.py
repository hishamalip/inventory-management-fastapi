import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:12345678@localhost:5432/postgres"
)
engine = create_engine(url=db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
