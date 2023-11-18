
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    
    re_path(r'^admin/', include([
        path('login',views.AdminLoginView.as_view()),
        path('logout/', views.LogoutAPIView.as_view(), ),
    ])),

]

