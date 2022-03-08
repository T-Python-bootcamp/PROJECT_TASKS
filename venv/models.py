from database import Base
from sqlalchemy import String,Integer,Column,Text,Date,Enum

class Task(Base):
    __tablename__='tasks'
    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    title=Column(String(255),nullable=False,index=True)
    description = Column(Text,index=True)
    status = Column(Enum('Done','Not Done',name='progress_status'), nullable=False,index=True)
    deadline = Column(Date,nullable=False,index=True)
    # def __repr__(self):
    #     return f"<Item name={self.name} price={self.price}>"
