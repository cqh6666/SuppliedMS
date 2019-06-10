from django.shortcuts import render

from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse


from supplied.models import SuppliedInfo
from .models import UserProfile,UserComment
from .forms import RegisterForm,LoginForm
# Create your views here.


class IndexView(View):
    def get(self,request):
        all_supplied = SuppliedInfo.objects.all()
        return render(request, 'index.html', {
            "all_supplied": all_supplied,
        })


class LoginView(View):
    def get(self,request):
        return render(request,"login.html",{})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=email,password=password)
            if user is not None:
                login(request,user)
                return render(request, "ok.html",{"msg":"登录成功"})
            else:
                return render(request,"error.html",{"msg":"用户或密码错误"})
        else:
            return render(request,"login.html",{"login_form":login_form})


class RegisterView(View):
    """
    注册
    """
    def get(self,request):
        return render(request,"register.html",{})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('username','')
            if UserProfile.objects.filter(username=username):
                return render(request,"error.html",{"msg":"用户已存在"})

            first_name = request.POST.get('first_name','')
            college = request.POST.get('college','')
            mobile = request.POST.get('mobile','')
            organization = request.POST.get('organization','')
            position = request.POST.get('position','')
            password = request.POST.get('password','')

            user = UserProfile()
            user.first_name = first_name
            user.username = username
            user.college = college
            user.mobile = mobile
            user.organization = organization
            user.position = position
            user.password = make_password(password)

            user.save()

            loginUser = authenticate(username=username, password=password)
            login(request, loginUser)
            return render(request,"ok.html",{"msg":"注册成功..."})
        else:
            return render(request, "error.html",{"msg":"注册出了些问题..."})


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))



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


class tableView(View):
    def get(self,request):
        return render(request, "LendTable.html", {})