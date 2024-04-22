from . import views
from django.urls import path

urlpatterns = [
    path('feesinfo/',views.feesinfo)
]
