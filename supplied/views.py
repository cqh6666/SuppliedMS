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
        organization = request.POST.get('organization','')
        mobile = request.POST.get('mobile','')
        user = request.user

        if supplied and user:
            lend_table = SuppliedLend()
            lend_table.name = supplied
            lend_table.specification = specification
            lend_table.number = number
            lend_table.organization = organization
            lend_table.mobile = mobile
            lend_table.user = user
            lend_table.save()
            return render(request,"index.html",{})
        else:
            return render(request,"index.html",{})



class SuppliedInfoView(View):
    def get(self,request):
        all_supplied = SuppliedInfo.objects.all()
        return render(request,'SuppliedInfo.html',{
            "all_supplied":all_supplied,
        })


class LendListView(View):
    def get(self,request):
        is_lend = request.GET.get('is_lend','')
        all_list = SuppliedInfo.objects.filter(is_lend=is_lend)
        return render(request,'LendList.html',{
            "all_list":all_list,
        })


class CheckedView(View):
    def get(self,request):
        is_check = request.GET.get('is_check',"")
        all_list = SuppliedLend.objects.filter(is_check=is_check)
        return render(request,'checklist.html',{
            "all_list":all_list
        })
