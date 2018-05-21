"""
Created by 逗蛆 on 2018/5/7

"""
from flask import Blueprint

__author__ = "逗蛆"

web = Blueprint('web', __name__)  # __name__代表蓝图所在的模块

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
