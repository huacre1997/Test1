from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",include(("base.urls","base"),namespace="base")),
    path("empleados/",include(("users.urls","users"),namespace="users")),
    path("empresas/",include(("business.urls","business"),namespace="business")),

    path('admin/', admin.site.urls),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)