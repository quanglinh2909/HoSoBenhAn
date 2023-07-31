from src.model.Member import Member
from src.model.User import User

def addModle(engine):
    User.__table__.create(bind=engine, checkfirst=True)
    Member.__table__.create(bind=engine, checkfirst=True)




