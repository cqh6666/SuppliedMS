from django.shortcuts import render

from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse


from supplied.models import SuppliedInfo
from .models import UserProfile,UserComment
from .forms import RegisterForm,LoginForm,ModifyForm
# Create your views here.


class IndexView(View):
    def get(self,request):
        all_supplied = SuppliedInfo.objects.all().order_by("-is_lend")

        search_keyword = request.GET.get('keyword',"")
        if search_keyword:
            all_supplied = SuppliedInfo.objects.filter(name=search_keyword).order_by("-is_lend")

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


class UserShow(View):
    def get(self,request):
        if not request.user.is_authenticated():
            return render(request,"error.html",{"msg":"用户未登录"})
        user = request.user
        return render(request,"PersonalInfo.html",{"all_user":user})


class UserModify(View):
    def get(self,request):
        if not request.user.is_authenticated():
            return render(request,"error.html",{"msg":"用户未登录"})
        user = request.user
        return render(request,"ModifyPersonalInfo.html",{"all_user":user})
    def post(self,request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            user = request.user
            user.first_name = request.POST.get('first_name')
            user.college = request.POST.get('college')
            user.mobile = request.POST.get('mobile')
            user.organization = request.POST.get('organization')
            user.position = request.POST.get('position')
            user.save()
            return render(request,"ok.html",{"msg":"成功修改个人信息"})
        else:
            return render(request,"error.html",{"msg":"修改个人信息出现了错误"})


class UserAuthShow(View):
    def get(self,request):
        user = request.user
        if not user.is_superuser:
            return render(request,"error.html",{"msg":"权限不够,无法访问!"})
        all_user = UserProfile.objects.filter(is_superuser=0)
        return render(request,"UserAuth.html",{
            "all_user":all_user
        })


class GrantUserAuth(View):
    def post(self,request):
        auth = int(request.POST.get('auth'))
        this_id = int(request.POST.get('this_id'))

        if this_id:
            UserProfile.objects.filter(id=this_id).update(
                is_staff=auth
            )
            return JsonResponse({"status":"success","msg":"授权成功"})
        else:
            return JsonResponse({"status": "fail", "msg": "授权出现错误"})