from typing import List , Optional
from pydantic import BaseModel



class Blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode=True
    




class User(BaseModel):
    id=int
    name:str
    email:str
    password:str
    class Config():
        orm_mode=True


class Showuser(BaseModel):
    id=int
    name:str
    email:str
    blogs1:List[Blog]=[]
    
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:Showuser

    class Config():
        orm_mode=True

class Blogpost(BaseModel):
    title:str
    body:str
    creator:Showuser

    class Config():
        orm_mode=True


class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None




    