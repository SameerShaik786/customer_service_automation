from fastapi import FastAPI
from app.core.database import Base,engine
from app.models import user,humans,agents_run,tickets
from app.routes import ticket as ticket_router
from app.routes import user as user_router

app = FastAPI()
app.include_router(user_router.router)
app.include_router(ticket_router.router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind = engine)

@app.get("/")
def hello():
    return {"message":"Hello World"}

