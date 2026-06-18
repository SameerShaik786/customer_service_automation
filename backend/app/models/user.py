from sqlalchemy import Column, String
from app.core.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        String(36),
        primary_key=True,
        unique=True,
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )