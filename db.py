from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#database url
import os


import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SQLALCHEMY_DATABASE_URL = 'sqlite:///'+os.path.join(BASE_DIR,'base.db?check_same_thread=False')


engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_recycle=300)



SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()