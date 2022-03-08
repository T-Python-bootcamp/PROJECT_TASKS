from fastapi import FastAPI ,Depends
from sqlalchemy.orm import Session
from database import engine ,localsession ,Base
import task_cred
import schemas

Base.metadata.create_all(bind=engine)
app= FastAPI()



def get_db():
    db=localsession()
    try:
        yield db
    finally:
        db.close()

@app.get("/task/all")
def getAllTasks(db :Session =Depends(get_db)):
     return task_cred.get_all_tasks(db) 



@app.post("/task/all")   
def newTask (task : schemas.Task ,db :Session =Depends(get_db)):
  task_cred.create_task(task,db) 
  return {"msg":"new task is done"} 



@app.put("/task/all")   
def newTask (task : schemas.Task ,db :Session =Depends(get_db)):
  task_cred.update_task(task,db) 
  return {"msg":"new task is updeted"} 

@app.delete("/task/all{id}/")   
def newTask (task : schemas.Task ,db :Session =Depends(get_db)):
  task_cred.delete_task(task.id,db) 
  return {"msg":"new task is deleted"} 



@app.patch("/task/all")   
def newTask (task : schemas.Task ,db :Session =Depends(get_db)):
  task_cred.update_one_task(task,db) 
  return {"msg":"new task is status"} 



@app.get("/task/deadline")
def order_deadline(db :Session =Depends(get_db)):
     return task_cred.get_deadline_task(db) 


@app.get("/task/sersh{task}")
def  search_all_taskes(db :Session =Depends(get_db)):
     return task_cred.searsh_task(db)     




 
       