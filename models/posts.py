from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Posts(Base):
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    content = Column(Text,  nullable=False)
    likes = Column(Integer,  default=0)
    dislikes = Column(Integer,default=0)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    status = Column(Boolean, nullable=True, default=True)

    like = relationship("Likes", back_populates='post')
    author = relationship("Users", back_populates='post')