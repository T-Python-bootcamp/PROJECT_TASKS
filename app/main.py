# Task management application

from fastapi import FastAPI,status, HTTPException
from sqlalchemy import desc
from database import SessionLocal
import model, schema
from database import Base,engine

app=FastAPI()

Base.metadata.create_all(engine)
db = SessionLocal()


@app.get("/tasks/all")
def disply_all_tasks():
    items= db.query(model.Tasks).all()
    return items


@app.get("/tasks/sorted")
def disply_sorted_tasks():
    items = db.query(model.Tasks).order_by(desc(model.Tasks.deadline)).all()
    return items


@app.post('/new-task', response_model=schema.Tasks, status_code=status.HTTP_201_CREATED)
def create_task(item: schema.Tasks):
    new_item = model.Tasks(
        id = item.id,
        title = item.title,
        description = item.description,
        status = item.status,
        deadline = item.deadline
    )

    db.add(new_item)
    db.commit()
    return new_item

@app.put('/update/{item_id}',response_model=schema.Tasks,status_code=status.HTTP_200_OK)
def update_task(item_id:int,item:schema.Tasks):
    item_to_update=db.query(model.Tasks).filter(model.Tasks.id==item_id).first()
    item_to_update.title=item.title
    item_to_update.description=item.description
    item_to_update.status=item.status
    item_to_update.deadline=item.deadline

    db.commit()
    return item_to_update


@app.get('/search/{item}', status_code=status.HTTP_200_OK)
def search_task(item:str):
    item_to_update = db.query(model.Tasks).filter(model.Tasks.title==item).all()
    return item_to_update


@app.put('/update/status/{item_id}',response_model=schema.Change_status,status_code=status.HTTP_200_OK)
def update_status(item_id:int,item:schema.Change_status):
    item_to_update=db.query(model.Tasks).filter(model.Tasks.id==item_id).first()
    item_to_update.status=item.status

    db.commit()
    return item_to_update

@app.delete('/remove/{item_id}')
def delete_task(item_id: int):
    item_to_delete = db.query(model.Tasks).filter(model.Tasks.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete