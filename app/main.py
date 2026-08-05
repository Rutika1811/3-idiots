print("🚀 MAIN.PY IS RUNNING")

from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import friends, memories

app = FastAPI(
    title="Memory Vault API",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(friends.router)
app.include_router(memories.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Memory Vault ❤️"
    }