from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import engine, localsession, Base
import models, schemas
import task_crud
from sqlalchemy import desc


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = localsession()

    try:
        yield db
    finally:
        db.close()


@app.post("/task/new")
def newtask(task : schemas.Task, db : Session = Depends(get_db)):
    task_crud.create_task(task, db)
    return {"msg" : "new task is created ."}

@app.get("/task/all")
def getAllTasks(db : Session = Depends(get_db)):
     return task_crud.get_all_tasks(db)


@app.delete('/task/{task_id}')
def deleteTask(task_id: int,db: Session = Depends(get_db)):
    db_task = task_crud.delete(db, task_id)
    return {"msg" : "deleted task ."}

@app.put("/task/updateAll")   
def newTask (task : schemas.Task ,db :Session =Depends(get_db)):
  task_crud.update_task(task, db)
  return {"msg":"update task "}

@app.put("/task/updateStatus")   
def newStatus (task : schemas.Task ,db :Session =Depends(get_db)):
  task_crud.update_status_task(task, db)
  return {"msg":"update status "}

@app.get("/tasks/sort")
def getSortTasks(db : Session = Depends(get_db)):
     return task_crud.get_sort_tasks(db)


@app.get('/task/search/{Title}')
def searchTask(Title:str,db : Session = Depends(get_db)):
     return task_crud.update_task(task, db)