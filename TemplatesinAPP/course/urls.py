from . import views
from django.urls import path

urlpatterns = [
    path('learndj/',views.learndj),
    path('learnpy/', views.learnpy)

]
