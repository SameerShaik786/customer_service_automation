from fastapi import FastAPI
from app.routes import user
from app.core.database import Base, engine
from app.models.user import User

app = FastAPI(title="AI Agent Marketplace Backend")

Base.metadata.create_all(bind=engine)

app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Agent Marketplace Backend!"}


