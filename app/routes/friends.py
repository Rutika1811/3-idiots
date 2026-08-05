print("✅ friends.py loaded")

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/friends",
    tags=["Friends"]
)


@router.post("/register", response_model=schemas.FriendResponse)
def register_friend(
    friend: schemas.FriendCreate,
    db: Session = Depends(get_db)
):
    return crud.create_friend(db, friend)

@router.post("/login", response_model=schemas.LoginResponse)
def login_friend(
    login_data: schemas.FriendLogin,
    db: Session = Depends(get_db)
):
    friend = crud.authenticate_friend(db, login_data)

    if not friend:
        raise HTTPException(
            status_code=401,
            detail="Invalid Code Name or Friendship Key ❤️"
        )

    return {
        "message": f"Welcome back, {friend.code_name}! ❤️",
        "friend": friend
    }