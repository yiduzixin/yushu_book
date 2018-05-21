"""
Created by 逗蛆 on 2018/5/20

"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

__author__ = "逗蛆"

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True   #不创建表
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
