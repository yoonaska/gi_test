from django.urls import path, include,  re_path
from django.contrib import admin
from . import views

urlpatterns = [
          
   re_path(r'^notes/', include([
      path('create-or-update-notes', views.CreateOrUpdateNotesApiView.as_view()),
      path('destroy-notes',views.DestroyNotesApiView.as_view()),
      path('get-notes-view',views.NotesListApiView.as_view()),
   ])),
]


