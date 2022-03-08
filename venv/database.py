from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
url=f"postgresql://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('ROUTE')}/{os.environ.get('DATABASE_NAME')}"
engine=create_engine(url,echo=True)
localSession=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()
