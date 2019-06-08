# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :        chen
   date：          2019/6/8
-------------------------------------------------
   Change Activity:
                   2019/6/8:
-------------------------------------------------
"""

import xadmin
from .models import UserComment


class UserCommentAdmin(object):
    pass


xadmin.site.register(UserComment,UserCommentAdmin)