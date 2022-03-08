from optparse import Option
from typing import Optional
from pydantic import BaseModel
from datetime import date



class Task( BaseModel):
    id : Optional[int]
    title: str
    description: str
    status: str
    deadline: date

    class Config:
        orm_mode= True