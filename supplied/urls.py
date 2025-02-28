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
from .views import LendTableView,SuppliedInfoView,SubmitView,LendListView,CheckedView,CheckView,CheckTableView,UserLendListView,SuppliedInfoShowView,LendTableInfoShowView,PrintTableView

urlpatterns = [
    #用户信息
    url(r'^table/(?P<supplied_id>.*)/$', LendTableView.as_view(), name="LendTable"),
    url(r'^supplied_info/(?P<supplied_id>.*)/$', SuppliedInfoShowView.as_view(), name="SuppliedInfoShow"),
    url(r'^lendtable_info/(?P<table_id>.*)/$', LendTableInfoShowView.as_view(), name="lendtable_info"),
    url(r'^submit/',SubmitView.as_view(),name="submit"),
    url(r'^info/$',SuppliedInfoView.as_view(),name="SuppliedInfo"),
    url(r'^lendlist/$',LendListView.as_view(),name="LendList"),
    url(r'^user_lendlist',UserLendListView.as_view(),name="UserLendList"),
    url(r'^checklist/$',CheckedView.as_view(),name="checklist"),
    url(r'^shenhe/$', CheckView.as_view(), name="shenhe"),
    url(r'^CheckTable/$', CheckTableView.as_view(), name="CheckTable"),

    url(r'^print_table/(?P<table_id>.*)/$',PrintTableView.as_view(),name="PrintTable")

]