from sqlalchemy.orm import Session
import schemas
import models



def create_task(task: schemas.Task, db: Session):
    newTask = models.Tasks(title=task.title, description=task.description,
                           status=task.status, deadline=task.deadline)

    db.add(newTask)
    db.commit()
    db.refresh(newTask)


def getTasksAll(db: Session):
    return db.query(models.Tasks).order_by(models.Tasks.deadline.desc()).all()


def taskDelete(id: int, db: Session):
    # task = db.query(models.Task).filter(models.Task.id == id).get()
    task = db.query(models.Tasks).get(id)
    db.delete(task)
    db.commit()


def updateTask(task: schemas.Task, db: Session):
    db.query(models.Tasks).filter(models.Tasks.id == task.id).update(
        {models.Tasks.title: task.title,
         models.Tasks.description: task.description,
         models.Tasks.status: task.status,
         models.Tasks.deadline: task.deadline
         })
    db.commit()


def search_task(query: str, db: Session):
    tasks = db.query(models.Tasks).filter(models.Tasks.title.contains(query)).all()
    return tasks
