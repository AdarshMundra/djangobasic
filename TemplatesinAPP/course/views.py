from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learndj(request):
    return render(request,"LearnDjango.html")
def learnpy(request):
    return render(request,"LearnPython.html")
