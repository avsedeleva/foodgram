from django.contrib import admin
from .models import Tag, Ingredient, Recipe
from import_export.admin import ImportExportModelAdmin, ImportMixin

from .resource import IngredientResource


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Управление публикациями в админке."""

    list_display = ('pk', 'name', 'color', 'slug')
    search_fields = ('name',)
    empty_value_display = '-empty-'

@admin.register(Ingredient)
class IngredientAdmin(ImportMixin, admin.ModelAdmin):
    """Управление публикациями в админке."""

    list_display = ('pk', 'name', 'measurement_unit', 'amount')
    search_fields = ('name',)
    empty_value_display = '-empty-'
    resource_class = IngredientResource
    from_encoding = "utf-8-sig"

'''class IngredientImportAdmin(ImportExportModelAdmin):
    resource_class = IngredientResource

admin.site.register(Ingredient, (IngredientAdmin, IngredientImportAdmin))'''
