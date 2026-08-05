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

def create_memory(db: Session, memory: schemas.MemoryCreate):

    new_memory = models.Memory(
        title=memory.title,
        story=memory.story,
        place=memory.place,
        date=memory.date,
        mood=memory.mood,
        emoji=memory.emoji,
        created_by=memory.created_by
    )

    db.add(new_memory)
    db.commit()
    db.refresh(new_memory)

    return new_memory

def get_memories(db: Session):
    return db.query(models.Memory).all()

def get_memories(db: Session):
    memories = db.query(models.Memory).all()
    return memories