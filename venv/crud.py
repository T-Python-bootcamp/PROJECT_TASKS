from sqlalchemy.orm import session
import schemas,models

def create_task(task:schemas.Task,db:session):
    newTask=models.Task(title=task.title,description=task.description,status=task.status,deadline=task.deadline)
    db.add(newTask)
    db.commit()
    db.refresh(newTask)

def get_all_tasks(db:session):
    return db.query(models.Task).all()

def get_all_tasks_sorted(db:session):
    return db.query(models.Task).order_by('deadline').all()

def delete_task(id:int,db:session):
    task = db.query(models.Task).get(id)
    db.delete(task)
    db.commit()
    db.refresh()

def update_task(id:int,status:str,db:session):
    task=db.query(models.Task).filter(models.Task.id==id)
    task.update({models.Task.status:status})
    db.commit()
    db.refresh(task)

def search_task(title:str,db:session):
    return db.query(models.Task).filter(models.Task.title==title).all()
