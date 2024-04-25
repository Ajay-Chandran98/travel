from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('ministers/',  views.ministers_list, name='ministers_list'),
    #path('add/',views.addition,name='addition'),
    #path('multiply/', views.multiplication, name='multiply'),
    #path('subtract/', views.subtraction, name='subtract'),

]