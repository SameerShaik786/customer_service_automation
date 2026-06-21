from typing import Optional

from pydantic import BaseModel, Field


class HumanCreate(BaseModel):
    user_id: str
    status: Optional[str] = Field(default="active")


class HumanUpdate(BaseModel):
    status: Optional[str] = None
