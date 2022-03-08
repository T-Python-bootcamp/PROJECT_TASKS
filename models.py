
from database import Base
from sqlalchemy import Column, Date, Integer, String,Enum


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column("status",Enum("done","not done", name="status"))
    deadline = Column(Date)