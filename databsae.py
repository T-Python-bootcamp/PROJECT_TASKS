from sqlalchemy import create_engine
# 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Postgressql_url="postgresql://postgres:123@localhost:5433/project"


engine=create_engine(Postgressql_url)
localsession=sessionmaker(bind=engine,autocommit=False,autoflush=False)
# 

Base=declarative_base()