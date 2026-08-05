from sqlalchemy.orm import Session
from app import models, schemas


def create_friend(db: Session, friend: schemas.FriendCreate):
    new_friend = models.Friend(
        code_name=friend.code_name,
        real_name=friend.real_name,
        friendship_key=friend.friendship_key,
        emoji=friend.emoji
    )

    db.add(new_friend)
    db.commit()
    db.refresh(new_friend)

    return new_friend

def authenticate_friend(db: Session, login_data: schemas.FriendLogin):
    friend = (
        db.query(models.Friend)
        .filter(models.Friend.code_name == login_data.code_name)
        .first()
    )

    if not friend:
        return None

    if friend.friendship_key != login_data.friendship_key:
        return None

    return friend