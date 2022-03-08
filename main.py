from ast import Return
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing import Optional
# سشن الاتصال مع الداتا بيز
import models,scemas
import Taskcrud
from databsae import localsession,engine

models.Base.metadata.create_all(bind=engine)



app=FastAPI()


def get_db():
    db= localsession()
    try:
        yield db
    finally:
        db.close()


@app.get("/alltask")
def get_taks(db:Session=Depends(get_db)):
    return Taskcrud.get_all_taks(db)




@app.get("/tasks/search/")
def search(db: Session = Depends(get_db), query: Optional[str] = None):
     taskSearch = Taskcrud.search_task(query, db)
     return {"Search": taskSearch}


@app.get("/tasks")
def get_all_taks1(db:Session=Depends(get_db)):
    return Taskcrud.get_all_takss(db)

@app.post("/post/task")
def add_task(task:scemas.Task,db:Session=Depends(get_db)):
    Taskcrud.new_post(task,db)
    return {"msg":"created is done!"}




@app.put("/task_update")
def update_task(task:scemas.Task,db:Session=Depends(get_db)):
    Taskcrud.update_task1(task,db)
    return{"msg":"the updated is done!"}

@app.delete("/delete/taks/{id}")
def del_task(id:int,db:Session=Depends(get_db)):
    Taskcrud.delete_task(id,db)
    return {"msg":f"delted the tssk{id} id"}





