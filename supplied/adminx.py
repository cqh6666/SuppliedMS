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
from .models import SuppliedInfo,SuppliedLend


class SuppliedInfoAdmin(object):
    pass

class SuppliedLendAdmin(object):
    pass


xadmin.site.register(SuppliedInfo,SuppliedInfoAdmin)
xadmin.site.register(SuppliedLend,SuppliedLendAdmin)