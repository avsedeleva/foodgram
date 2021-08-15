from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, IngredientViewSet

v1_router = DefaultRouter()

v1_router.register('tags', TagViewSet)
v1_router.register('ingredients', IngredientViewSet)

urlpatterns = [

    path('', include(v1_router.urls)),

]