from datetime import date
from pydantic import BaseModel
from typing import Optional


class Tasks(BaseModel):
    id : Optional[int]
    title :str
    description : Optional[str] = None
    status : str
    deadline: date

    class Config:
        orm_mode = True

class Change_status(BaseModel):
    status : str

    class Config:
        orm_mode = True
