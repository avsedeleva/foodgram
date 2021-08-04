from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

v1_router = DefaultRouter()

v1_router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
