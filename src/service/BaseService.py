from abc import abstractmethod

from src.service.Connection import Connection


class BaseService():
    DBSession = Connection.getInstance().DBSession



    def create(self, data):
        try:
            self.session = self.DBSession()
            self.session.add(data)
            self.session.commit()
            self.session.refresh(data)
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def update(self, data):
        try:
            self.session = self.DBSession()
            self.session.merge(data)
            self.session.commit()
            self.session.refresh(data)
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def delete(self, data):
        try:
            self.session = self.DBSession()
            self.session.delete(data)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def deleteAll(self, Entity):
        try:
            self.session = self.DBSession()
            self.session.query(Entity).delete()
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def deleteByID(self, id, Entity):
        try:
            self.session = self.DBSession()
            self.session.query(Entity).filter(Entity.ID == id).delete()
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def remove(self, id, Entity):
        try:
            self.session = self.DBSession()
            self.session.query(Entity).filter(Entity.ID == id).update({"IsDelete": True})
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def getAll(self, Entity):
        try:
            self.session = self.DBSession()
            return self.session.query(Entity).where(Entity.IsDelete == False).all()
        except Exception as e:
            print(e)
            return []
        finally:
            self.session.close()

    @abstractmethod
    def getById(self, id):
        pass
