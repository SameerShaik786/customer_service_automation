from app.core.database import Base
from sqlalchemy import Text,String,Column,ForeignKey,Enum,Float,DateTime,func

class AgentRun(Base):
    __tablename__ = "agents_run"

    id = Column(
        String(36),
        primary_key= True
    )
    ticket_id = Column(
        ForeignKey("tickets.id"),
        nullable = False
    )
    agent_type = Column(
        Enum("billing","technical","general","main", name="agent_type_enum"),
        default= "main",
        nullable= False
    )
    input = Column(
        Text,
        nullable = False
    )
    output = Column(
        Text,
        nullable= False
    )
    confidence_score = Column(
        Float,
        default = 0,
        nullable = False
    )
    status = Column(
        Enum("solved","escalated", name="agent_status_enum"),
        nullable= False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )