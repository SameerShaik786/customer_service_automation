from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://neondb_owner:npg_UyKwaxu2ocD1@ep-long-frog-aty905vu-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    bind=engine
)

Base = declarative_base()



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()  