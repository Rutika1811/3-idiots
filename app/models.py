from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True, index=True)
    code_name = Column(String, unique=True, nullable=False, index=True)
    real_name = Column(String, nullable=False)
    friendship_key = Column(String, nullable=False)
    emoji = Column(String, nullable=True)
    profile_photo = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

from sqlalchemy import Text, Date


class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    story = Column(Text, nullable=False)

    place = Column(String)

    date = Column(Date)

    mood = Column(String)

    emoji = Column(String)

    created_by = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)