from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql://postgres:12345678@localhost:5432/fastapi_db"
engine = create_engine(url=db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
