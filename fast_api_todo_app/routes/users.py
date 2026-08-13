from fastapi import APIRouter, status, Depends, HTTPException
from schemas.user import UserCreate, UserPatch, UserResponse
from schemas.task import TaskCreate, TaskResponse
from database import users, tasks
from dependencies.users import get_user

router = APIRouter(prefix='/users')

@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate):
    for user in users:
        if user['email'] == user_create.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Email already exists'
            )

        if user['phone'] == user_create.phone:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Phone already exists'
            )
    new_user = {
        'user_id': len(users) + 1,
        'username': user_create.username,
        'email': user_create.email,
        'password': user_create.password,
        'phone': user_create.phone
    }
    users.append(new_user)

    return new_user

@router.get('/', response_model=list[UserResponse])
def all_users():
    return users


@router.get('/{user_id}', response_model=UserResponse)
def read_user(user = Depends(get_user)):
    return user

@router.patch('/{user_id}', response_model=UserResponse)
def patch_user(user_patch: UserPatch, user = Depends(get_user)):
    if user_patch.password is not None:
        user['password'] = user_patch.password

    if user_patch.email is not None:
        user['email'] = user_patch.email

    if user_patch.phone is not None:
        user['phone'] = user_patch.phone

    return user

@router.delete('/{user_id}', response_model=UserResponse)
def delete_user(user=Depends(get_user)):
    users.remove(user)
    return user

@router.post('/{user_id}/tasks', response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, user=Depends(get_user)):
    new_task = {
        'id': len(tasks) + 1,
        'title': task_create.title,
        'description': task_create.description,
        'completed': False,
        'user_id': user['user_id']
    }

    tasks.append(new_task)

    return new_task

@router.get('/{user_id}/tasks', response_model=list[TaskResponse])
def get_user_tasks(user=Depends(get_user)):
    user_tasks = []
    for task in tasks:
        if task['user_id'] == user['user_id']:
            user_tasks.append(task)

    return user_tasks