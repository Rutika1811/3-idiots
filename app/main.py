from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(
    title="Memory Vault API",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Welcome to Memory Vault ❤️"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }