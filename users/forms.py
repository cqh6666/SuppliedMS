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


class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

class RegisterForm(forms.Form):
    name = forms.CharField(required=True)
    college = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    email = forms.CharField(required=True)
    organization = forms.CharField(required=True)
    position = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)