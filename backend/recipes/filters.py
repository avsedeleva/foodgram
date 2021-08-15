from django_filters import FilterSet, filters

from .models import Ingredient


class IngredientFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Ingredient
        fields = ('name', )