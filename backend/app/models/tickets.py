from app.core.database import Base
from sqlalchemy import String,Text,func,Enum,ForeignKey,Column,DateTime

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(
        String(36),
        primary_key= True
    )

    user_id = Column(
        ForeignKey("users.id"),
        nullable= False
    )

    ticket_content = Column(
        Text,
        nullable= False
    )

    category = Column(
        Enum("billing","technical","general","unclassified", name="ticket_category_enum"),
        default="unclassified",
        nullable = False
    )

    status = Column(
        Enum("open", "ai_handling", "escalated", "resolved", "closed", name="ticket_status_enum"),
        default= "open",
        nullable= False
    )

    resolved_by_type = Column(
        Enum("agent","human", name="ticket_resolved_by_type_enum"),
        default= "agent",
        nullable= False
    )

    resolved_by_human_id = Column(
        ForeignKey("humans.id"),
        nullable= True
    )
    

    created_at = Column(
        DateTime(timezone = True),
        server_default= func.now(),
        nullable = False
    )