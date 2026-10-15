from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'

router = routers.SimpleRouter()
router.register('', views.ProductViewSet, basename='produtos')

urlpatterns = [
    path('', include(router.urls) )
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)