from user_task.db.base import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    sex = Column(Boolean, default=False)
    age = Column(Integer, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    father_name = Column(String, index=True, nullable=True)
    address = Column(String, index=True)
    e_mail = Column(String, index=True, nullable=True)
    login = Column(String, index=True)
