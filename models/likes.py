from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Likes(Base):
    __tablename__ = "Likes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("Posts.id"), nullable=False)
    like = Column(Boolean, nullable=True, default=True)
    status = Column(Boolean, nullable=True, default=True)

    post = relationship("Posts", back_populates='like')