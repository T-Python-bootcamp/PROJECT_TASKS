from database import Base
from sqlalchemy import Column,Integer,String,Date

class Tasks(Base):
     __tablename__='tasks'
     id=Column(Integer,primary_key=True,index=True)
     title =Column(String,index=True)
     description=Column(String,index=True) 
     status=Column(String,index=True) 
     deadline=Column(Date,index=True)
