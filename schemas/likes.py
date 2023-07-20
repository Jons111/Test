from pydantic import BaseModel
from typing import Optional, List


class LikeBase(BaseModel):
    post_id: int
    like: bool


class LikeCreate(LikeBase):
    pass


class LikeUpdate(LikeBase):
    id: int
    status: bool
