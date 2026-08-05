from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

print("✅ memories.py loaded")

router = APIRouter(
    prefix="/memories",
    tags=["Memories"]
)


@router.post("/", response_model=schemas.MemoryResponse)
def create_memory(
    memory: schemas.MemoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_memory(db, memory)