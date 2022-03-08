from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Postgresql_url = "postgresql://postgres:123456aSd@localhost:5432/"
engine = create_engine(Postgresql_url)

localsession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()