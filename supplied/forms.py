# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     forms
   Description :
   Author :        chen
   date：          2019/6/8
-------------------------------------------------
   Change Activity:
                   2019/6/8:
-------------------------------------------------
"""
from django import forms
from .models import LendTable


class LendTableForm(forms.ModelForm):
    class Meta:
        model = LendTable
        fields = ['name','specification','number','organization','mobile']