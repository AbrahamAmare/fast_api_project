from datetime import datetime
from typing import Optional
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Post(BaseModel):
    title: str
    content: str
    isPublished: bool = False

    # class Config:
    #     orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str
    isPublished: bool = False

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    owner_id: int
    owner: UserResponse
    created_at: datetime

    class Config:
        from_attributes = True
class PostWithVoteResponse(BaseModel):
    Post: PostResponse
    votes: int

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
