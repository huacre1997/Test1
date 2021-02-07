  
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import BusinessView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",BusinessView.as_view(),name="business_list"),
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)