"""
Created by 逗蛆 on 2018/5/20

"""
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = "逗蛆"


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
