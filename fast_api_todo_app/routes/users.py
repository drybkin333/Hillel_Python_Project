from fastapi import APIRouter, status, Depends
from schemas.user import UserCreate, UserPatch, UserResponse
from database import users
from dependencies.users import get_user

router = APIRouter(prefix='/users')

@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate):
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