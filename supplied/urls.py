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
from .views import LendTableView,SuppliedInfoView,SubmitView

urlpatterns = [
    #用户信息
    url(r'^table/(?P<supplied_id>.*)/$', LendTableView.as_view(), name="LendTable"),
    url(r'^submit',SubmitView.as_view(),name="submit"),
    url(r'^info/$',SuppliedInfoView.as_view(),name="SuppliedInfo")

]