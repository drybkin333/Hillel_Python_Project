from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from models.users import User


def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return user