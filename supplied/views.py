import time

from django.shortcuts import render
from django.views.generic.base import View

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
        is_check = request.GET.get('is_check',"")
        subtitle = "当前已外借的记录"
        if is_check == "0":
            subtitle = "当前未外借的记录"

        all_list = SuppliedLend.objects.filter(is_check=is_check)
        return render(request,'checklist.html',{
            "all_list":all_list,
            "subtitle":subtitle
        })
