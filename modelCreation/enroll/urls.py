from django.urls import path
from . import views

urlpatterns = [
    path('stu/',views.student_info),
    path('register/',views.showformData),
]