from django.shortcuts import render
from enroll.models import Student
from .forms import StudentRegestration

# Create your views here.

def student_info(request):
    stud = Student.objects.all()
    return render(request,'enroll/studetails.html',{'stud':stud})


def showformData(request):
    fm = StudentRegestration()
    return  render(request,"enroll/userregestration.html",{"form":fm})