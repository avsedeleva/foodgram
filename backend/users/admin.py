from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Управление публикациями в админке."""

    list_display = ('pk', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username',)
    empty_value_display = '-empty-'