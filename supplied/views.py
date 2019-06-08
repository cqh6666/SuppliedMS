from django.shortcuts import render
from django.views.generic.base import View

from .forms import LendTableForm
from .models import SuppliedInfo,LendTable
# Create your views here.


class LendTableView(View):
    def get(self,request,supplied_id):
        supplied = SuppliedInfo.objects.get(id=int(supplied_id))

        if request.user.is_authenticated():
            return render(request,'LendTable.html',{"supplied":supplied})
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
            lend_table = LendTable()
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
            "all_supplied":all_supplied
        })
