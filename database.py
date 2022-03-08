from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:admin123@localhost/postgres", echo=True)

Base = declarative_base()
localSession = sessionmaker(bind = engine)
