from turtle import title
from sqlalchemy import desc
from sqlalchemy.orm import Session
import models, schemas


def create_task (task:schemas.Task, db :Session):
    newtask = models.Task(title=task.title,  description= task.description,status=task.status  ,deadline=task.deadline)
    db.add(newtask)
    db.commit()
    db.refresh(newtask)

def get_all_tasks(db : Session):
    return db.query(models.Task).all()

def delete(db: Session,task_id):
     db_task= db.query(models.Task).filter_by(id=task_id).first()
     db.delete(db_task)
     db.commit()
     
def update_task(task : schemas.Task, db : Session):
    db.query(models.Task).filter(models.Task.id == task.id).update({models.Task.title : task.title,models.Task.description : task.description, models.Task.status : task.status , models.Task.deadline : task.deadline})
    db.commit()

def get_sort_tasks(db : Session):
    return  db.query(models.Task).order_by(desc(models.Task.deadline)).all()
    db.commit()

def search_task(db: Session,Title:str):
        return  db.query(models.Task).filter(models.Task.title==Title).all()

def update_status_task(task : schemas.Task, db : Session):
    db.query(models.Task).filter(models.Task.id == task.id).update({ models.Task.status : task.status})
    db.commit()
