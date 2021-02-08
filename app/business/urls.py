  
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import BusinessView,CreateBusinessView,EditBusinessView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path("<>",ChangeBusiness.as_view(),name="change_business"),

    path("",BusinessView.as_view(),name="list_business"),
    path("create/",CreateBusinessView.as_view(),name="create_business"),
    path("edit/<int:pk>/",EditBusinessView.as_view(),name="edit_business"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)