from sqlalchemy import Column, Integer, String, Date
from database import Base

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), nullable=False)
    describtion = Column(String, nullable=False)
    status = Column(String(10), nullable=False)
    deadline = Column(Date, nullable=False)

    def __repr__(self):
        return f"Task info\nID: {self.id}\ntitle: {self.title}\nDescribtion: {self.describtion}\nStatus: {self.status}\nDeadline: {self.deadline}"