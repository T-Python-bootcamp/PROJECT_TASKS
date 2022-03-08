from fastapi import Depends, FastAPI 
from typing import Optional
from sqlalchemy.orm import Session
from database import engine , localsession, Base
import schemas
import task_crud

Base.metadata.create_all(bind = engine)

def get_DB():
    db = localsession()
    try :
        yield db
    finally:
        db.close()

app = FastAPI()


@app.post("/task/add")
def addTask(task : schemas.Task , db : Session = Depends(get_DB)):
    task_crud.add_task(task , db)
    return {"message" : "new task is created"}

@app.get("/task/all")
def getAllTasks(db : Session = Depends(get_DB)):
    return task_crud.all_tasks(db)
    
@app.put("/task/edit")
def editTask(task : schemas.Task , db : Session = Depends(get_DB)):
    task_crud.upadte_task(task , db)
    return {"message":f"Task is update {task}"}

@app.delete("/task/delete/{task_id}")
def deleteTAsks(task_id : int , db : Session = Depends(get_DB)):
    task_crud.delete_task(task_id , db)
    return {"message" : f"Successfuly delete {task_id} task"}

@app.get("/tasks/search/")
def search(db: Session = Depends(get_DB), query: Optional[str] = None):
    taskSearch = task_crud.search_task(query, db)
    return {"Search": taskSearch}


