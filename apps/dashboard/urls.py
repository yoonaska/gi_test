from django.urls import path, include,  re_path
from django.contrib import admin
from . import views


urlpatterns = [
   path('', views.HomeView.as_view(), name='home.index'),
]
