from django.shortcuts import render

from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
from django.http import JsonResponse

from .models import UserProfile,UserComment
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
    """
    注册
    """
    def get(self,request):
        return render(request,"register.html",{})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return render(request,"index.html",{"register_form":register_form})
        else:
            return render(request, "register.html",{"register_form":register_form})


class CommentView(View):
    """
    显示所有评论
    """
    def get(self,request):
        all_comments = UserComment.objects.all()
        return render(request,"comment.html",{"all_comments":all_comments})


class AddCommentView(View):
    """
    动态添加评论
    """
    def post(self,request):
        content = request.POST.get('content')

        if not request.user.is_authenticated():
            return JsonResponse({ "status":"fail","msg":"用户未登录"})

        if content:
            comment = UserComment()
            comment.user = request.user
            comment.comments = content
            comment.save()
            return JsonResponse({"status":"success","msg":"评论成功"})