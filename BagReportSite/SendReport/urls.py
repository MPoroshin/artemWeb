from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.BagReportCreateView.as_view(), name ='Bager'),
    path('home', views.BagReportCreateView.as_view(), name ='Bager'),
    path('great', views.success, name='great'),
    path('search', views.search, name = 'search')

]