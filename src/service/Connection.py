import os
import uuid

from dotenv import load_dotenv
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
            load_dotenv()

            address = os.getenv("ADDRESS")
            port = os.getenv("PORT")
            user = os.getenv("USER")
            password = os.getenv("PASS")
            dbName = os.getenv("DB_NAME")

            Connection.__instance = self
            print('mariadb+mariadbconnector://'+str(user)+':'+str(password)+'@'+str(address)+':'+str(port)+'/'+str(dbName))
            self.engine = create_engine('mariadb+mariadbconnector://'+str(user)+':'+str(password)+'@'+str(address)+':'+str(port)+'/'+str(dbName))
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
