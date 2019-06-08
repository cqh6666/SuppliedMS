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
from .models import CheckTable


class CheckTableAdmin(object):
    pass


xadmin.site.register(CheckTable,CheckTableAdmin)