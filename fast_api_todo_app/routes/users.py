from fastapi import APIRouter, status, Depends, HTTPException
from schemas.user import UserCreate, UserPatch, UserResponse
from schemas.task import TaskCreate, TaskResponse
from database import get_db
from models import User, Task
from sqlalchemy.orm import Session
from dependencies.users import get_user

router = APIRouter(prefix='/users')

@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_create.email).first()
    if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Email already exists'
            )

    existing_user = db.query(User).filter(User.phone == user_create.phone).first()
    if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Phone already exists'
            )

    new_user = User(
        username = user_create.username,
        email = user_create.email,
        password = user_create.password,
        phone = user_create.phone
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/', response_model=list[UserResponse])
def all_users(db: Session = Depends(get_db)):
    return db.query(User).all()



@router.get('/{user_id}', response_model=UserResponse)
def read_user(user = Depends(get_user)):
    return user

@router.patch('/{user_id}', response_model=UserResponse)
def patch_user(user_patch: UserPatch, user = Depends(get_user), db: Session = Depends(get_db)):
    if user_patch.password is not None:
        user.password = user_patch.password

    if user_patch.email is not None:
        existing_user = db.query(User).filter(User.email == user_patch.email,
            User.user_id != user.user_id).first()

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Email already exists'
            )

        user.email = user_patch.email

    if user_patch.phone is not None:
        existing_user = db.query(User).filter(User.phone == user_patch.phone,
            User.user_id != user.user_id ).first()

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Phone already exists'
            )

        user.phone = user_patch.phone

    db.commit()
    db.refresh(user)

    return user

@router.delete('/{user_id}', response_model=UserResponse)
def delete_user(user=Depends(get_user), db: Session = Depends(get_db)):
    db.delete(user)
    db.commit()
    return user

@router.post('/{user_id}/tasks', response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, user=Depends(get_user), db: Session = Depends(get_db)):

    new_task = Task(
        title = task_create.title,
        description = task_create.description,
        completed = False,
    )
    user.tasks.append(new_task)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get('/{user_id}/tasks', response_model=list[TaskResponse])
def get_user_tasks(user=Depends(get_user)):
    return user.tasks