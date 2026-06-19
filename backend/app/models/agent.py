from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, JSON, String, Text, func
from app.core.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(
        String(36),
        primary_key=True,
        unique=True,
        nullable=False
    )

    user_id = Column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    system_prompt = Column(
        Text,
        nullable=False
    )

    config = Column(
        JSON,
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="active"
    )

    endpoint = Column(
        String(255),
        nullable=False
    )

    total_runs = Column(
        Integer,
        nullable=False,
        default=0
    )

    total_cost = Column(
        Float,
        nullable=False,
        default=0.0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


