from sqlalchemy.orm import session
import models,schemas
from sqlalchemy import desc
from sqlalchemy.ext.mutable import MutableList




def create_task(task:schemas.Tasks,db:session):
    newTask=models.Tasks(title=task.title , description=task.description , status=task.status , deadline=task.deadline)
    db.add(newTask)
    db.commit()
    db.refresh(newTask)




def get_all(db:session):
    return db.query(models.Tasks).all()

def get_sorted(db:session):
    return db.query(models.Tasks).order_by(desc(models.Tasks.deadline)).all()
    

def delete_task(id:int,db:session):
    task=db.query(models.Tasks).get(id)
    db.delete(task)
    db.commit()

def update_task(id:int,task:schemas.Tasks,db:session):
    db.query(models.Tasks).filter(models.Tasks.id==id).update({models.Tasks.title :task.title,models.Tasks.description:task.description,models.Tasks.status:task.status,models.Tasks.deadline:task.deadline})
    db.commit()

def get_task(id:int,db:session):
    return db.query(models.Tasks).get(id)

def status_task(id:int,task:schemas.Tasks,db:session):
    db.query(models.Tasks).filter(models.Tasks.id==id).update({models.Tasks.status:task.status})
    db.commit()


    
 
    