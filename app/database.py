from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine=create_engine("postgresql://postgres:123@localhost/FastApiProject",echo = True)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)