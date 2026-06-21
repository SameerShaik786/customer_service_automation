from typing import Optional

from pydantic import BaseModel, Field


class TicketCreate(BaseModel):
    user_id: str
    ticket_content: str
    category: Optional[str] = Field(default="unclassified")


class TicketUpdate(BaseModel):
    ticket_content: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    resolved_by_type: Optional[str] = None
    resolved_by_human_id: Optional[str] = None
