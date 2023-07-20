
from pydantic import BaseModel
from typing import Optional, List




class UserBase(BaseModel):
    name: str
    username: str
    status: bool
    password: str



class UserCreate(UserBase):
    pass



class UserUpdate(UserBase):
    id: int





class Token(BaseModel):
    access_token = str
    token = str


class TokenData(BaseModel):
    id: Optional[str] = None

class UserCurrent(BaseModel):
    id:int
    name: str
    username: str
    password:str
    status: bool