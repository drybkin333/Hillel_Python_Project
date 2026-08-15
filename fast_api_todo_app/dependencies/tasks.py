from fastapi import HTTPException, status, Depends
from database import get_db
from sqlalchemy.orm import Session
from models.tasks import Task

def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')

    return task