from app.core.database import Base
from sqlalchemy import Column,String,Enum,DateTime,func

class User(Base):

    __tablename__ = "users"
    
    id = Column(
        String(36),
        primary_key= True,
        nullable= False
    )

    name = Column(
        String(255),
        nullable= False
    )

    email = Column(
        String(255),
        unique= True,
        nullable= False
    )

    password = Column(
        String(255),
        nullable= False
    )

    user_type = Column(
        Enum("Human","Admin","Customer",name="user_type_enum"),
        default="Customer",
        nullable= False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable = False
    )
