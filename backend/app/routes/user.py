from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.user import create_user, authenticate_user
from app.schemas.user import UserCreate, UserLogin, UserRead, Token
from app.core.database import get_db
from app.core.security import create_access_token

router = APIRouter(prefix="/user")

@router.get('/')
def read_root():
    return {"message":"User route is working!"}

@router.post("/register", response_model=UserRead)
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    user_created = create_user(data, db)
    return {"id": user_created.id, "email": user_created.email}

@router.post("/login", response_model=Token)
def login_user(data: UserLogin, db: Session = Depends(get_db)):
    user_present = authenticate_user(data, db)
    if not user_present:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user_present.email})
    return {"access_token": access_token, "token_type": "bearer"}

    
