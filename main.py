from sqlalchemy.orm import session
from fastapi import FastAPI,Depends
from database import engine,localsession,Base
import models,crud,schemas


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=localsession()
    try:
        yield db
    finally:
        db.close()



@app.post("/tasks/create")
def createTask(task:schemas.Tasks, db:session=Depends(get_db)):
    crud.create_task(task,db)
    return {"msg":"new task created"}

@app.get("/tasks/all")
def getAll(db:session=Depends(get_db)):
    return crud.get_all(db)

@app.get("/tasks/sorted")
def getsorted(db:session=Depends(get_db)):
    return crud.get_sorted(db)

@app.delete("/tasks/delete/{id}")
def deleteTask(id:int,db:session=Depends(get_db)):
    crud.delete_task(id,db)
    return {"msg":"delete task done"}

@app.put("/tasks/update/{id}")
def updateTask(id:int,task:schemas.Tasks,db:session=Depends(get_db)):
    crud.update_task(id,task,db)
    return {"msg":"update task done"}

@app.get("/tasks/{id}")
def gettask(id:int,db:session=Depends(get_db)):
    return crud.get_task(id,db)

@app.patch("/tasks/status/{id}")
def statusTask(id:int,task:schemas.Tasks,db:session=Depends(get_db)):
    crud.status_task(id,task,db)
    return {"msg":"change status of task"}


