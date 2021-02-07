from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
   

    # path('activate/<uidb64>/<token>/',activate, name='activate'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
