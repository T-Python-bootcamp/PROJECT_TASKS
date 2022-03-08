from pydantic import BaseModel
from fastapi import FastAPI, Body
from typing import Optional
from sqlalchemy import insert
import models 
from database import localSession

app = FastAPI()
db = localSession()

class Task(BaseModel):
    id: Optional[int]
    title: str
    describtion: str
    status: str
    deadline: str

    class Config:
        orm_mode = True

@app.get('/tasks')
def get_tasks(id: Optional[str] = None):
    if id:
        result = db.query(models.Tasks).filter(models.Tasks.id == id).all()
        return result
    else:
        result = db.query(models.Tasks).order_by(models.Tasks.deadline).all()
        return result


@app.get('/tasks/{task}')
def get_tasks(task):

    result = db.query(models.Tasks).filter(models.Tasks.title.like(f"{task}%")).all()
    return result



@app.post("/task")
def add_task(task: Task):
    db.execute(insert(models.Tasks).values(title = task.title, describtion = task.describtion ,status = task.status ,deadline = (task.deadline).replace("-","")))
    db.commit()
    return f"Task '{task.title}' is added successfully"


@app.put("/task")
def update_task(task: Task):
    
    result = db.query(models.Tasks).filter(models.Tasks.id == task.id).update(
    {
        "id":task.id,
        "title":task.title,
        "describtion": task.describtion, 
        "status": task.status, 
        "deadline": task.deadline
    })
    if result:
        db.commit()
        return f"Task '{task.id}' is updated successfully"
    else:
        return f"Provided task is not exist!"


@app.put("/task_status")
def update_task(id: int = Body(...), status: str = Body(...)):
    
    result = db.query(models.Tasks).filter(models.Tasks.id == id).update(
    {
        "status": status
    })
    if result:
        db.commit()
        return f"Task '{id}' status is updated successfully"
    else:
        return f"Provided task is not exist!"
    

@app.delete("/task")
def delete_task(id: int = Body(...)):
    result = db.query(models.Tasks).filter(models.Tasks.id == id).delete()
    
    if result:
        db.commit()
        return f"Task '{id}' is deleted successfully"
    else:
        return f"Provided task is not exist!"

