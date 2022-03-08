from typing import Optional
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import engine, localsession
import models
import schemas
import task_crud
models.Base.metadata.create_all(bind=engine)


def get_DB():
    db = localsession()

    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/task/new")
def newTask(task: schemas.Task, db: Session = Depends(get_DB)):
    task_crud.create_task(task, db)
    return {"msg": "new task has been created"}


@app.get("/tasks/all")
def getAllTasks(db: Session = Depends(get_DB)):
    return task_crud.getTasksAll(db)


@app.delete("/tasks/delete/{id}")
def deleteTask(id: int, db: Session = Depends(get_DB)):
    task_crud.taskDelete(id, db)
    return {"msg": f"task with id ({id}) deleted successfully"}


@app.put("/tasks/update")
def updateTask(task: schemas.Task, db: Session = Depends(get_DB)):
    task_crud.updateTask(task, db)
    return {"msg": "the task has been updated"}


@app.get("/search/")
def search(db: Session = Depends(get_DB), query: Optional[str] = None
           ):
    tasks = task_crud.search_task(query, db=db)
    return {"tasks": tasks}
