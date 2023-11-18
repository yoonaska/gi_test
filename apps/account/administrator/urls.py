from django.urls import path, include,  re_path
from django.contrib import admin
from . import views


urlpatterns = [       
   re_path(r'^register/', include([
      path('admin-profile-register', views.CreateOrUpdateRegisterAPIView.as_view()),
      path('admin-profile-status-change',views.ActiveOrInactivateAdminProfileApiView.as_view()),
      path('get-admin-profile',views.GetUsersApiView.as_view()),
   ])),
]


