from xmlrpc.client import Boolean
from databsae import Base
from sqlalchemy import Column,Integer,String,Date,Boolean
class Task(Base):
     __tablename__="PROJECTTasks"

    #  اذا بدا بشرطتين معناه برايفت!
     id=Column(Integer,primary_key=True,index=True)
     title=Column(String,index=True)
     description=Column(String,index=True)
     status=Column(Boolean,index=True)
     deadline=Column(Date,index=True)