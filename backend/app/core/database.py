from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine("postgresql://neondb_owner:npg_UyKwaxu2ocD1@ep-long-frog-aty905vu-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require",echo= True)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind = engine
)


Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
