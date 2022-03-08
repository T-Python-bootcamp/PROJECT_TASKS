from sqlite3 import Date
from typing import Optional
from xmlrpc.client import Boolean
from pydantic import BaseModel

class Task(BaseModel):
    id :Optional[str]
    title: str
    description:str
    status:Boolean
    deadline: Date




    class Config:
        orm_mode=True