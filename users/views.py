from django.shortcuts import render

from django.views.generic.base import View


# Create your views here.


class IndexView(View):
    def get(self,request):
        return render(request,"index.html")


class LoginView(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request,"login.html")


class RegisterView(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request, "login.html")