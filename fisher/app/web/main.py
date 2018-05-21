"""
Created by 逗蛆 on 2018/5/20

"""
from app.web import web

__author__ = "逗蛆"


@web.route('/')
def index():
    return 'hello'


@web.route('/personal')
def personal_center():
    pass
