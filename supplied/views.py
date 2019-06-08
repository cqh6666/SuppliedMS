from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class SuppliedInfoView(View):
    def get(self,request):
        return render(request,'LendTable.html',{})
    def post(self,request):
        pass
