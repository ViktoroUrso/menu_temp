"""Tag Menu Admin module."""
from django.contrib import admin
from .models import TagMenu


@admin.register(TagMenu)
class TagMenuAdmin(admin.ModelAdmin):
    """TagMenu attributes."""
    list_display = ('name', 'url', 'parent', 'display_children', 'root')
    fields = ['name', 'url', 'parent']
