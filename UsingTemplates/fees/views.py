from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(request):
    dici={
        "content" :"content",
    "content2":"content2"
    }
    return render(request,"fees/learndj.html",context=dici)

def learn_python(request):
    return HttpResponse("<h1>Hello Python</h1>")