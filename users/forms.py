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
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name','college','mobile','username','organization','position','password']


class ModifyForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name','college','mobile','organization','position']