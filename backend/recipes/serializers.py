from rest_framework import serializers

from .models import Tag, Ingredient


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ('amount', )
