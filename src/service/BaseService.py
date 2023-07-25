from abc import abstractmethod

from src.service.Connection import Connection


class BaseService():
    session = Connection.getInstance().session

    def create(self, data):
        try:
            self.session.add(data)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def update(self, data):
        try:
            self.session.merge(data)
            self.session.commit()

            return True
        except Exception as e:
            print(e)
            self.session.rollback()

            return False

    def delete(self, data):
        try:
            self.session.delete(data)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def deleteAll(self, Entity):
        try:
            self.session.query(Entity).delete()
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    def deleteByID(self, id, Entity):
        try:
            self.session.query(Entity).filter(Entity.ID == id).delete()
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False


    def getAll(self, Entity):
        try:
            return self.session.query(Entity).where(Entity.IsDelete == False).all()
        except Exception as e:
            print(e)
            return []


    @abstractmethod
    def getById(self, id):
        pass
