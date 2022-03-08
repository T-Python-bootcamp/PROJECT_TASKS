from fastapi import Depends,FastAPI
from sqlalchemy.orm import session
from database import engine,localSession,Base
import schemas
import crud

Base.metadata.create_all(bind=engine)
app=FastAPI()

def get_db():
    db=localSession()
    try:
        yield db
    finally:
        db.close()


@app.post('/task/new')
def New_Task(task:schemas.Task,db:session=Depends(get_db)):
    crud.create_task(task,db)
    return {"msg":"new Task is made"}
    
@app.get('/tasks/all')
def Get_All(db:session=Depends(get_db)):
    return crud.get_all_tasks(db)

@app.get('/tasks/sorted')
def Get_All_Sorted(db:session=Depends(get_db)):
    return crud.get_all_tasks_sorted(db)

@app.delete('/tasks/delete/{id}')
def Delete_Task(id:int,db:session=Depends(get_db)):
    crud.delete_task(id,db)
    return {"msg":f"deleted the task #{id} successfully"}

@app.put('/tasks/update')
def Update_Task(id:int,status:str,db:session=Depends(get_db)):
    if status == 'Done' or status == 'Not Done':
        crud.update_task(id,status,db)
    return {"msg":"task updated successfully"}

@app.get('/tasks/search')
def Search_Task(title:str,db:session=Depends(get_db)):
    return crud.search_task(title,db)


