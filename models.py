from database import Base
from sqlalchemy import Column , Integer , String , Enum , Text , Date



class Task(Base):
    __tablename__ = "tasks"
    task_id =Column(Integer , primary_key=True , index=True)
    task_title = Column(String , index=True)
    task_description = Column(Text , index=True)
    task_status = Column("status" ,Enum("done" , "not done" , name = "status") )
    task_deadline = Column(Date , index=True)