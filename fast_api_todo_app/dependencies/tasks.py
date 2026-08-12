from fastapi import HTTPException, status
from database import tasks

def get_task(task_id: int):
    for i in tasks:
        if i['id'] == task_id:
            return i

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
