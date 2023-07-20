from pydantic import BaseModel
from typing import Optional, List


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    id: int
    status: bool
