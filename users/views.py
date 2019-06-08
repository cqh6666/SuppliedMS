from django.shortcuts import render

from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login

from .models import UserProfile
from .forms import RegisterForm,LoginForm
# Create your views here.


class IndexView(View):
    def get(self,request):
        return render(request,"index.html")


class LoginView(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                return render(request, "index.html",{})
            else:
                return render(request,"index.html",{"msg":"用户名或密码错误"})
        else:
            return render(request,"index.html",{"login_form":login_form})


class RegisterView(View):
    def get(self,request):
        return render(request,"register.html",{})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_profile = UserProfile()
            user_profile.username = request.POST.get("name")
            user_profile.email = request.POST.get("email")
            user_profile.college = request.POST.get("college")
            user_profile.mobile = request.POST.get("mobile")
            user_profile.organization = request.POST.get("organization")
            user_profile.position = request.POST.get("position")
            user_profile.password = make_password(request.POST.get("password"))
            user_profile.save()
            return render(request,"index.html",{"register_form":register_form})
        else:
            return render(request, "register.html",{"register_form":register_form})