from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/', views.BagReportCreateView.as_view(), name ='Bager'),
    path('great', views.success, name='great'),

]