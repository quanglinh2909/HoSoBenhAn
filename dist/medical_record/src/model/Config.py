
from sqlalchemy import Column, String,TEXT

from src.model.Base import Base


class Config(Base):
    __tablename__ = 'config'
    Key = Column(String(250), nullable=True)
    Value = Column(String(250), nullable=True)


