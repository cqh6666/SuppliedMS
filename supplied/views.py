import time

from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse

from .models import SuppliedInfo,SuppliedLend


# Create your views here.


class LendTableView(View):
    def get(self,request,supplied_id):
        supplied = SuppliedInfo.objects.get(id=int(supplied_id))

        if request.user.is_authenticated():
            return render(request, 'LendTable.html', {"supplied":supplied})
        else:
            return render(request,"index.html",{})


class SubmitView(View):
    def post(self,request):
        supplied = SuppliedInfo.objects.get(id=int(request.POST.get('supplied_id')))
        specification = request.POST.get('specification','')
        number =request.POST.get('number','')
        lend_time = request.POST.get('lend_time','')
        return_time = request.POST.get('return_time','')
        user = request.user

        if supplied and user:
            lend_table = SuppliedLend()
            lend_table.name = supplied
            lend_table.specification = specification
            lend_table.number = number
            lend_table.lend_time = lend_time
            lend_table.return_time = return_time
            lend_table.user = user
            lend_table.save()
            return render(request,"ok.html",{"msg":"申请成功,请等待管理员通过验证"})
        else:
            return render(request,"error.html",{"msg":"似乎有些bug,请重新填写!"})



class SuppliedInfoView(View):
    def get(self,request):
        all_supplied = SuppliedInfo.objects.all()
        return render(request,'SuppliedInfo.html',{
            "all_supplied":all_supplied,
        })


class LendListView(View):
    def get(self,request):
        is_lend = request.GET.get('is_lend','')
        subtitle = "当前可借用物资"
        if is_lend == "0":
            subtitle = "当前不可借用物资"
        all_list = SuppliedInfo.objects.filter(is_lend=is_lend)

        return render(request,'LendList.html',{
            "all_list":all_list,
            "subtitle":subtitle,
            "is_lend":is_lend
        })


class CheckedView(View):
    def get(self,request):
        is_lend = int(request.GET.get('is_lend',""))
        subtitle = "当前已外借的记录"
        if is_lend == 0:
            subtitle = "当前未外借的记录"

        all_list = SuppliedLend.objects.filter(is_lend=is_lend)
        return render(request,'checklist.html',{
            "all_list":all_list,
            "subtitle":subtitle
        })


class CheckView(View):
    def get(self,request):
        """查看未审核的申请表"""
        all_table = SuppliedLend.objects.filter(is_check=0)
        return render(request,'shenhe.html',{"all_table":all_table})


class CheckTable(View):
    def post(self,request):
        """ajax请求 审核申请表同意或拒绝"""
        is_lend = int(request.POST.get('is_lend'))
        this_id = int(request.POST.get('this_id'))
        if this_id:
            SuppliedLend.objects.filter(id=this_id).update(
                is_check=1,
                is_lend=is_lend
            )
            return JsonResponse({"status": "success", "msg": "完成申请"})
        else:
            return JsonResponse({"status": "fail", "msg": "出现错误"})
