from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AgentBase(BaseModel):
    name: str
    description: str
    system_prompt: str = Field(..., alias="systemPrompt")
    config: Optional[Dict[str, Any]] = None
    status: Optional[str] = "active"
    nodes: Optional[List[Dict[str, Any]]] = None
    edges: Optional[List[Dict[str, Any]]] = None

    class Config:
        allow_population_by_field_name = True


class AgentCreate(AgentBase):
    pass


class AgentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    system_prompt: Optional[str] = Field(None, alias="systemPrompt")
    config: Optional[Dict[str, Any]] = None
    status: Optional[str] = None
    nodes: Optional[List[Dict[str, Any]]] = None
    edges: Optional[List[Dict[str, Any]]] = None

    class Config:
        allow_population_by_field_name = True


class AgentRead(BaseModel):
    id: str
    user_id: str
    name: str
    description: str
    system_prompt: str
    config: Dict[str, Any]
    status: str
    endpoint: str
    total_runs: int
    total_cost: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True




