from pydantic import BaseModel
from typing import List,Optional

class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    user: str
    email: str
    password: str

class ShowUser(BaseModel):
    user: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowUserId(BaseModel):
    id: int
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    email: Optional[str] = None

