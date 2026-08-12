from fastapi import APIRouter, status, Depends
from schemas.task import TaskCreate, TaskUpdate, TaskPatch, TaskResponse
from database import tasks
from dependencies.tasks import get_task
from dependencies.users import get_user

router = APIRouter(prefix='/tasks')



@router.get('/', response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def all_tasks():
    return tasks

@router.post('/', response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate):
    new_task = {
        'id' : len(tasks) + 1,
        'title' : task_create.title,
        'description' :task_create.description,
        'completed': False
    }

    tasks.append(new_task)

    return new_task

@router.get('/{task_id}', response_model=TaskResponse)
def read_task(task = Depends(get_task)):
    return task

@router.delete('/{task_id}', response_model=TaskResponse)
def delete_task(task = Depends(get_task)):
    tasks.remove(task)

    return task

@router.put('/{task_id}', response_model=TaskResponse)
def update_task(task_update: TaskUpdate, task = Depends(get_task)):
    task['title'] = task_update.title
    task['description'] = task_update.description
    task['completed'] = task_update.completed

    return task

@router.patch('/{task_id}', response_model=TaskResponse)
def patch_task(task_patch: TaskPatch, task = Depends(get_task)):
    if task_patch.title is not None:
        task['title'] = task_patch.title
    if task_patch.description is not None:
        task['description'] = task_patch.description
    if task_patch.completed is not None:
        task['completed'] = task_patch.completed

    return task
