from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Postgressql_url = "postgresql://postgres:123456@localhost:5432/tasksdb"
engine = create_engine(Postgressql_url) 

localsession = sessionmaker(bind=engine , autocommit=False , autoflush=False)

Base = declarative_base()