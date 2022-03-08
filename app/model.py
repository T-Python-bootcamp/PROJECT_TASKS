from sqlite3 import Date
from database import Base 
from sqlalchemy import String, Integer, Column,Date

class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(String, nullable=False)
    deadline = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Student name={self.title}>"
