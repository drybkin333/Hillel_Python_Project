from fastapi import HTTPException
from database import users


def get_user(user_id: int):
    for user in users:
        if user['user_id'] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail='User not found'
    )