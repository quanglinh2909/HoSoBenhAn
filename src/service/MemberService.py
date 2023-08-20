from sqlalchemy.orm import sessionmaker

from src.model.Member import Member
from src.service.BaseService import BaseService
from sqlalchemy import and_, or_


class MemberService(BaseService):

    def getById(self, id):
        try:
            self.session = self.DBSession()
            return self.session.query(Member).filter(Member.ID == id).first()
        except Exception as e:
            return None
        finally:
            self.session.close()

    def getPage(self, page, limit, type):
        try:
            self.session = self.DBSession()

            # xap xep theo ngay tao moi nhat
            return self.session.query(Member).where(and_(Member.IsDelete == False, Member.Type == type)).order_by(
                Member.CreatedAt.desc()).offset((page - 1) * limit).limit(limit).all()
        except Exception as e:
            return []
        finally:
            self.session.close()

    def getTotal(self, type):
        try:
            self.session = self.DBSession()
            return self.session.query(Member).where(and_(Member.IsDelete == False, Member.Type == type)).count()
        except Exception as e:
            return 1
        finally:
            self.session.close()

    def getAllByType(self, type):
        try:
            self.session = self.DBSession()

            return self.session.query(Member).where(and_(Member.IsDelete == False, Member.Type == type)).all()
        except Exception as e:
            return None
        finally:
            self.session.close()

    def search(self, key, page, limit, type):
        try:
            # self.session.expire_all()
            self.session = self.DBSession()
            return self.session.query(Member).where(
                and_(Member.IsDelete == False, Member.Type == type,
                     or_(Member.FullName.like(f"%{key}%"), Member.CCCD.like(f"%{key}%")))).order_by(
                Member.CreatedAt.desc()).offset((page - 1) * limit).limit(limit).all()
        except Exception as e:
            return None
        finally:
            self.session.close()
