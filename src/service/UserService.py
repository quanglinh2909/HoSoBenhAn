import bcrypt
from sqlalchemy import and_

from src.model.User import User
from src.service.BaseService import BaseService


class UserService(BaseService):

    def login(self, UserName, password):
        try:
            self.session = self.DBSession()
            res = self.session.query(User).filter(and_(User.UserName == UserName, User.IsDelete == False)).first()
            if res is not None:
                if bcrypt.checkpw(password.encode('utf-8'), res.Password.encode('utf-8')):
                    return True
            return False
        except:
            return False
        finally:
            self.session.close()

    def getById(self, id):
        try:
            self.session = self.DBSession()
            return self.session.query(User).filter(User.ID == id).first()
        except Exception as e:
            return None
        finally:
            self.session.close()
