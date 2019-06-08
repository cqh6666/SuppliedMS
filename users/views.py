from django.shortcuts import render

from django.views.generic.base import View


# Create your views here.


class IndexView(View):
    def get(self,request):
        return render(request,"index.html")


class LoginView(View):
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        pass