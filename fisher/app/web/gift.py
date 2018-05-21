"""
Created by 逗蛆 on 2018/5/20

"""
from app.web import web
from flask_login import login_required

__author__ = "逗蛆"


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
