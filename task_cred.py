from turtle import title
from sqlalchemy import desc
from sqlalchemy.orm import Session
import models, schemas


def get_all_tasks(db:Session):
     return db.query(models.Task).all()


def create_task (task:schemas.Task, db :Session):
    newTask= models.Task(title=task.title,  description= task.description,status=task.status  ,deadline=task.deadline)



  


    db.add(newTask)
    db.commit()
    db.refresh(newTask)    





def update_task(task : schemas.Task, db : Session):
    db.query(models.Task).filter(models.Task.id == task.id).update({models.Task.title : task.title, models.Task.description : task.description,models.Task.status : task.status,models.Task.deadline : task.deadline,})
    db.commit()   


def delete_task(id: int, db : Session):
    task = db.query(models.Task).get(id)
    db.delete(task)
    db.commit()  


def update_one_task(task : schemas.Task, db : Session):
    db.query(models.Task).filter(models.Task.id == task.id  ).update({  models.Task.status : task.status})
    db.commit()  



def get_deadline_task(db:Session):
     return db.query(models.Task).order_by(models.Task.deadline).all()


def searsh_task(db:Session):
     return db.query(models.Task.id).filter(models.Task.id).all()       


     

    
        