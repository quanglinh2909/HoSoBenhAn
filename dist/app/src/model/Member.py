
from sqlalchemy import Column, String,TEXT

from src.model.Base import Base


class Member(Base):
    __tablename__ = 'member'
    FullName = Column(String(250), nullable=True)
    Birthday = Column(String(250), nullable=True)
    CCCD = Column(String(250), nullable=True)
    Relatives = Column(String(250), nullable=True)
    InfoRelatives = Column(String(250), nullable=True)
    DateIn = Column(String(250), nullable=True)
    Province = Column(String(250), nullable=True)
    District = Column(String(250), nullable=True)
    Ward = Column(String(250), nullable=True)
    Address = Column(String(250), nullable=True)
    CDB = Column(TEXT, nullable=True)
    Note = Column(TEXT, nullable=True)
    Avatar = Column(String(250), nullable=True)
    Type = Column(String(10), nullable=True)
    # cân nặng
    CN = Column(String(250), nullable=True)
    # đường huyết
    DH = Column(String(250), nullable=True)
    # huyết áp
    HA = Column(String(250), nullable=True)

    #thuoc dieu tri
    Medicine = Column(TEXT, nullable=True)
    #trieu chung
    Symptoms = Column(TEXT, nullable=True)
    #benh khac
    OtherMedicalConditions = Column(TEXT, nullable=True)

