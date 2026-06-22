from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate
from app.services.user import create_user

router = APIRouter(prefix = "/user")


@router.post("/")
def create_user_route(data:UserCreate,db:Session = Depends(get_db)):
    new_user = create_user(data,db)
    if new_user:
        return {"message": "User Created Successfully",
                "user" : {
                    "id" : new_user.id,
                    "email" : new_user.email,
                    "user_type": new_user.user_type
                }}
    else:
        raise HTTPException(status_code = 400,detail = "Email already exists")