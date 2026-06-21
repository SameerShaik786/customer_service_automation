from typing import Optional

from pydantic import BaseModel, Field


class AgentRunCreate(BaseModel):
    ticket_id: str
    agent_type: Optional[str] = Field(default="main")
    input: str
    output: str
    confidence_score: Optional[float] = Field(default=0.0)
    status: str


class AgentRunUpdate(BaseModel):
    agent_type: Optional[str] = None
    input: Optional[str] = None
    output: Optional[str] = None
    confidence_score: Optional[float] = None
    status: Optional[str] = None
