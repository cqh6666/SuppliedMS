# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :        chen
   date：          2019/6/8
-------------------------------------------------
   Change Activity:
                   2019/6/8:
-------------------------------------------------
"""

from django.conf.urls import url, include
from .views import SuppliedInfoView

urlpatterns = [
    #用户信息
    url(r'^info/$', SuppliedInfoView.as_view(), name="SuppliedInfo"),

]