
from sqlalchemy import Column, String

from src.model.Base import Base


class User(Base):
    __tablename__ = 'user'
    Password = Column(String(250), nullable=False)
    UserName = Column(String(250), nullable=False)
