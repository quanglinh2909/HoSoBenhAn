from src.model.Config import Config
from src.model.Member import Member
from src.service.BaseService import BaseService
from sqlalchemy import and_, or_


class ConfigService(BaseService):

    def getById(self, id):
        try:
            self.session = self.DBSession()
            return self.session.query(Config).filter(Config.ID == id).first()
        except Exception as e:
            return None
        finally:
            self.session.close()

    def getByKey(self, key):
        try:
            self.session = self.DBSession()
            return self.session.query(Config).filter(Config.Key == key).first()
        except Exception as e:
            return None
        finally:
            self.session.close()
