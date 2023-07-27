from src.model.Member import Member
from src.service.BaseService import BaseService
from sqlalchemy import and_, or_


class MemberService(BaseService):

    def getById(self, id):
        try:
            return self.session.query(Member).filter(Member.ID == id).first()
        except Exception as e:
            return None

    def getPage(self, page, limit, type):
        try:
            # xap xep theo ngay tao moi nhat
            return self.session.query(Member).where(and_(Member.IsDelete == False, Member.Type == type)).order_by(
                Member.CreatedAt.desc()).offset((page - 1) * limit).limit(limit).all()
        except Exception as e:
            return None

    def getTotal(self, type):
        try:
            return self.session.query(Member).where(and_(Member.IsDelete == False, Member.Type == type)).count()
        except Exception as e:
            return None

    def search(self, key, page, limit, type):
        try:
            return self.session.query(Member).where(
                and_(Member.IsDelete == False, Member.Type == type,
                     or_(Member.FullName.like(f"%{key}%"), Member.CCCD.like(f"%{key}%")))).order_by(
                Member.CreatedAt.desc()).offset((page - 1) * limit).limit(limit).all()
        except Exception as e:
            return None
