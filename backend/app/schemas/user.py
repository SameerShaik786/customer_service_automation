from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: str
    email: EmailStr
    name: str
    user_type: str
    created_at: Optional[str] = None


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    user_type: Optional[str] = Field(default="Customer")


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    password: Optional[str] = None
    user_type: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str
