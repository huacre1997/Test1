from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import *
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('home', IndexView.as_view(), name="home"),
    path("logout",Logout.as_view(),name="logout")
    # path('login',Login.as_view(),name="login"),
 

    # path('activate/<uidb64>/<token>/',activate, name='activate'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
