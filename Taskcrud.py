from operator import mod
from sqlalchemy.orm import Session
import models,scemas



def get_all_takss(db:Session):
    return db.query(models.Task).all()

def get_all_taks(db:Session):
    return db.query(models.Task).order_by(models.Task.deadline).all()

def search_task(query: str, db: Session):
    searchTask = db.query(models.Task).filter(models.Task.title.contains(query)).all()
    return searchTask 

def new_post(task:scemas.Task,db:Session):
    newpost=models.Task(title=task.title,description=task.description,status=task.status,deadline=task.deadline)
    db.add(newpost)
    db.commit()
    db.refresh(newpost)


def update_task1(task:models.Task,db:Session):
    db.query(models.Task).filter(models.Task.id==task.id).update({models.Task.title:task.title,models.Task.description:task.description,models.Task.status:task.status,models.Task.deadline:task.deadline})
    db.commit()


def delete_task(id:int,db:Session):
    task = db.query(models.Task).get(id)
    db.delete(task)

    db.commit()




