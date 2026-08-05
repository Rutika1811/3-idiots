from pydantic import BaseModel


class FriendCreate(BaseModel):
    code_name: str
    real_name: str
    friendship_key: str
    emoji: str | None = None


class FriendResponse(BaseModel):
    id: int
    code_name: str
    real_name: str
    emoji: str | None = None

    class Config:
        from_attributes = True

class FriendLogin(BaseModel):
    code_name: str
    friendship_key: str


class LoginResponse(BaseModel):
    message: str
    friend: FriendResponse