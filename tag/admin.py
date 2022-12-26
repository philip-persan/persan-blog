from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'id', 'name'
    list_per_page = 40
