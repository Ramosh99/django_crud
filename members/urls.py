from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('template/', views.testing, name='template'),
    path('members/details/<int:id>', views.details, name='details'),  
    path('master/',views.master,name='master'),
]