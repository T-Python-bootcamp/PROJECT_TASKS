from datetime import date
from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    task_id : Optional[int]
    task_title : str
    task_description : str
    task_status : str
    task_deadline : date

    class Config:
        orm_mode = True