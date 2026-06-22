import uuid
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import get_db
from app.schemas.user import UserCreate

def create_user(data:UserCreate,db:Session):

    if is_user_present(data,db):
        return None

    new_user = User(
        id =  str(uuid.uuid4()),
        name = data.name,
        email = data.email,
        password = data.password,
        user_type = data.user_type
    )

    db.add(new_user)
    db.commit()
    return new_user

def is_user_present(data: UserCreate, db: Session):
    return db.query(User).filter(User.email == data.email).first()
