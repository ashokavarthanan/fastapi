from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(50))
    user_id = Column('user_id', Integer, ForeignKey("users.id"), nullable=False)
    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String(50))
    email = Column(String(50))
    password = Column(String(255))
    blogs = relationship("Blog", back_populates="creator")