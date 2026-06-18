from fastapi import FastAPI

app = FastAPI(title = "AI Agent Marketplace Backend")

@app.get("/")
def home():
    return {"message": "Welcome to the AI Agent Marketplace Backend!"}