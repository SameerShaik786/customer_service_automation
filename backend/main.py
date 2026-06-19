from fastapi import FastAPI
from app.routes import user
from app.routes.agents import router as agents_router
from app.core.database import Base, engine
from app.models.user import User
from app.models.agent import Agent

app = FastAPI(title="AI Agent Marketplace Backend")

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(agents_router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Agent Marketplace Backend!"}


