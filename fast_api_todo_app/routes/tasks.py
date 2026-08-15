from fastapi import APIRouter, status, Depends
from schemas.task import TaskUpdate, TaskPatch, TaskResponse
from dependencies.tasks import get_task
from sqlalchemy.orm import Session
from database import get_db
from models import Task

router = APIRouter(prefix='/tasks')



@router.get('/', response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def all_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.get('/{task_id}', response_model=TaskResponse)
def read_task(task = Depends(get_task)):
    return task

@router.delete('/{task_id}', response_model=TaskResponse)
def delete_task(task = Depends(get_task), db: Session = Depends(get_db)):
    db.delete(task)
    db.commit()

    return task

@router.put('/{task_id}', response_model=TaskResponse)
def update_task(task_update: TaskUpdate, task = Depends(get_task), db: Session = Depends(get_db)):
    task.title = task_update.title
    task.description = task_update.description
    task.completed = task_update.completed
    db.commit()
    db.refresh(task)
    return task

@router.patch('/{task_id}', response_model=TaskResponse)
def patch_task(task_patch: TaskPatch, task = Depends(get_task), db: Session = Depends(get_db)):
    if task_patch.title is not None:
        task.title = task_patch.title
    if task_patch.description is not None:
        task.description = task_patch.description
    if task_patch.completed is not None:
        task.completed = task_patch.completed

    db.commit()
    db.refresh(task)

    return task
