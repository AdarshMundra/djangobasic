from django.shortcuts import render

# Create your views here.
def feesinfo(request):
    return render(request,"feeinfo.html")