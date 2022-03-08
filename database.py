from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

postgresql_url="postgresql://postgres:Almasah1&2@localhost:5000/Schoole"
engine =create_engine(postgresql_url)
localsession = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()