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
from .models import UserProfile

class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username','college','mobile','email','organization','position','password']