from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categories'

router = routers.SimpleRouter()
router.register('', views.CategoryViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls) )
]