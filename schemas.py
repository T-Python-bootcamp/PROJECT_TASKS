from datetime import date
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: Optional[int]
    title:  str
    description: str
    status: str
    deadline: date

    class Config:
        orm_mode = True
