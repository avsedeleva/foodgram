from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Tag, Ingredient
from .serializers import TagSerializers, IngredientSerializer
from .filters import IngredientFilter


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = TagSerializers
    pagination_class = None

class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientSerializer
    pagination_class = None
    filterset_class = IngredientFilter