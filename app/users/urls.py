from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import *
from django.conf.urls.static import static



urlpatterns = [
    path("",EmployeeListView.as_view(),name="list_users"),
    path("create",CreateUserView.as_view(),name="create_user"),
    path("edit/<int:pk>",EditUserView.as_view(),name="edit_user"),

    
    # path('activate/<uidb64>/<token>/',activate, name='activate'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
