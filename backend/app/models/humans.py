from app.core.database import Base
from sqlalchemy import Column,Text,String,Enum,ForeignKey,func,DateTime

class Human(Base):
    __tablename__ = "humans"

    id = Column(
        String(36),
        primary_key= True
    )

    user_id = Column(
        ForeignKey("users.id"),
        nullable= False
    )

    status = Column(
        Enum("active","inactive", name="human_status_enum"),
        default="active",
        nullable = False
    )

    created_at = Column(
    DateTime(timezone=True),
    server_default=func.now(),
    nullable=False
    )


