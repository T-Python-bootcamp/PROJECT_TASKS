from sqlalchemy.orm import Session
import schemas , models

def add_task(task : schemas.Task , db : Session):
    newTask = models.Task(
        task_title = task.task_title,
        task_description =task.task_description,
        task_status = task.task_status,
        task_deadline = task.task_deadline
    )

    db.add(newTask)
    db.commit()
    db.refresh(newTask)


def all_tasks(db : Session):
    return db.query(models.Task).order_by(models.Task.task_deadline.desc()).all()


def upadte_task(task , db : Session):
    db.query(models.Task).filter(models.Task.task_id == task.task_id).update({models.Task.task_title : task.task_title , 
    models.Task.task_description : task.task_description ,
    models.Task.task_status : task.task_status , 
    models.Task.task_deadline : task.task_deadline
    })
    db.commit()

def delete_task(task_id : int , db : Session):
    task = db.query(models.Task).get(task_id)
    db.delete(task)
    db.commit()

def search_task(query: str, db: Session):
    searchTask = db.query(models.Task).filter(models.Task.task_title.contains(query)).all()
    return searchTask