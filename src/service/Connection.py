import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.constants.Global import PATH_DATABASE
from src.model.AddModel import addModle
from src.model.Base import Base


class Connection():
    __instance = None

    def __init__(self):
        if Connection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Connection.__instance = self
            self.engine = create_engine('sqlite:///{}'.format(PATH_DATABASE))
            Base.metadata.create_all(self.engine)
            self.DBSession = sessionmaker(bind=self.engine)
            self.session = self.DBSession()
            # render model have in project
            addModle(self.engine)
    #connect pool

    @staticmethod
    def getInstance():
        if Connection.__instance == None:
            Connection()
        return Connection.__instance
