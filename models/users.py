from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from db import Base




class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    token = Column(String(400), default='',nullable=True)

    post = relationship("Posts", back_populates='author')
